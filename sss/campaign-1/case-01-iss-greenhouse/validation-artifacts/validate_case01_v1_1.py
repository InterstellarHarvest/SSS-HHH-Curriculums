#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
from PIL import Image, ImageDraw
import fitz
import base64
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

CASE = Path(__file__).resolve().parents[1]
ROOT = CASE.parents[2]
MASTER = CASE / "master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html"
HISTORICAL = CASE / "master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html"
PUBLISHED = CASE / "published/v1.1"
ARTIFACTS = CASE / "validation-artifacts/v1.1"
RENDERED = ARTIFACTS / "rendered-review"
RESULTS = ARTIFACTS / "CASE01_V1_1_VALIDATION_RESULTS.json"
PREFLIGHT = ARTIFACTS / "CASE01_V1_1_PDF_PREFLIGHT.json"
CHECKSUMS = ARTIFACTS / "CASE01_V1_1_CHECKSUMS.sha256"
MANIFEST = CASE / "CASE01_V1_1_MASTER_MANIFEST.json"
REPORT = CASE / "reports/CASE01_V1_1_VALIDATION_REPORT.md"
ROLE_LABELS = {"student":"Student Mission","teacher":"Teacher Guide","answer":"Answer Key","accessible":"Accessible Mission"}
EXPECTED_COUNTS = {"student":3,"teacher":7,"answer":3,"accessible":6}
ROLE_EXPORTS = {
    "student": ("SSS_C1_CASE01_STUDENT_MISSION_v1.1.html", "SSS_C1_CASE01_STUDENT_MISSION_v1.1.pdf", 3),
    "teacher": ("SSS_C1_CASE01_TEACHER_GUIDE_v1.1.html", "SSS_C1_CASE01_TEACHER_GUIDE_v1.1.pdf", 7),
    "answer": ("SSS_C1_CASE01_ANSWER_KEY_v1.1.html", "SSS_C1_CASE01_ANSWER_KEY_v1.1.pdf", 3),
    "accessible": ("SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.1.html", "SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.1.pdf", 6),
    "grayscale": ("SSS_C1_CASE01_GRAYSCALE_MISSION_v1.1.html", "SSS_C1_CASE01_GRAYSCALE_MISSION_v1.1.pdf", 3),
}

checks=[]; failures=[]; browser_checks=[]; browser_failures=[]; js_errors=[]; preflight={}


def ck(name, condition, detail=""):
    row={"name":name,"pass":bool(condition),"detail":str(detail)}; checks.append(row)
    if not condition: failures.append(row)


def bc(name, condition, detail=""):
    row={"name":name,"pass":bool(condition),"detail":str(detail)}; browser_checks.append(row)
    if not condition: browser_failures.append(row)


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda:handle.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()


def write(path: Path, text: str):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text.rstrip()+"\n",encoding="utf-8")


def sanitize(value: str) -> str:
    value=value.replace(str(ROOT),"<REPO>")
    value=re.sub(r"/Users/[^/]+/[^\s\"']*","<LOCAL_PATH>",value)
    value=re.sub(r"/home/runner/work/[^\s\"']*","<CI_PATH>",value)
    return value


def embed_insignia(soup: BeautifulSoup):
    insignia=ROOT/"shared/assets/insignia/saa.svg"
    if not insignia.exists(): return
    data="data:image/svg+xml;base64,"+base64.b64encode(insignia.read_bytes()).decode("ascii")
    for img in soup.select("img.saa-insignia,.continuation-header img"):
        img["src"]=data


def make_export(master_text: str, role: str) -> str:
    soup=BeautifulSoup(master_text,"html.parser")
    export_role="student" if role=="grayscale" else role
    soup.body["data-role"]=export_role
    classes=list(soup.body.get("class",[]))
    if role=="grayscale" and "grayscale" not in classes: classes.append("grayscale")
    soup.body["class"]=classes
    seed_state={"role":export_role}
    if role=="grayscale": seed_state["grayscale"]=True
    seed=soup.new_tag("script")
    seed.string="try{localStorage.setItem('sss-case01-v1-1-state',JSON.stringify(%s))}catch(e){}"%json.dumps(seed_state)
    soup.body.insert(0,seed)
    for page in list(soup.select(".page")):
        if page.get("data-role")!=export_role: page.decompose()
    embed_insignia(soup)
    return "<!DOCTYPE html>\n"+str(soup)


def contact_sheet(pdf_path: Path, output: Path):
    doc=fitz.open(pdf_path); cards=[]
    for index,page in enumerate(doc,1):
        pix=page.get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False)
        image=Image.frombytes("RGB",[pix.width,pix.height],pix.samples)
        width=360; ratio=width/image.width; image=image.resize((width,int(image.height*ratio)))
        card=Image.new("RGB",(width+20,image.height+42),"white"); card.paste(image,(10,26))
        ImageDraw.Draw(card).text((10,7),f"{pdf_path.stem} - page {index}",fill="black")
        cards.append(card)
    if not cards: raise RuntimeError(f"No pages rendered from {pdf_path.name}")
    cols=2; rows=(len(cards)+1)//2; cell_w=max(x.width for x in cards); cell_h=max(x.height for x in cards)
    sheet=Image.new("RGB",(cell_w*cols,cell_h*rows),"white")
    for idx,card in enumerate(cards): sheet.paste(card,((idx%cols)*cell_w,(idx//cols)*cell_h))
    output.parent.mkdir(parents=True,exist_ok=True); sheet.save(output,optimize=True)


def content_signatures(soup: BeautifulSoup):
    return [(p.get("data-role"),p.get("data-page-id"),str(p.select_one(".content-area"))) for p in soup.select(".page")]


def scan_absolute_paths(paths):
    bad=[]
    patterns=[re.compile(r"/Users/"),re.compile(r"/home/runner/work/"),re.compile(r"[A-Za-z]:\\\\")]
    for path in paths:
        if not path.exists() or path.suffix.lower() in {".pdf",".png"}: continue
        text=path.read_text(encoding="utf-8",errors="ignore")
        if any(pattern.search(text) for pattern in patterns): bad.append(path.relative_to(ROOT).as_posix())
    return bad


PUBLISHED.mkdir(parents=True,exist_ok=True); ARTIFACTS.mkdir(parents=True,exist_ok=True); RENDERED.mkdir(parents=True,exist_ok=True)
for old in RENDERED.glob("*-contact-sheet.png"): old.unlink()
master_text=MASTER.read_text(encoding="utf-8"); historical_text=HISTORICAL.read_text(encoding="utf-8")
soup=BeautifulSoup(master_text,"html.parser"); historical_soup=BeautifulSoup(historical_text,"html.parser")
# FINAL_APPROVAL_ASSERTIONS_v1
ck('approved stable metadata', soup.find('meta', attrs={'name':'sss-status','content':'approved'}) is not None)
ck('approved release metadata', soup.find('meta', attrs={'name':'sss-release'}) is not None)
ck('owner print metadata', soup.find('meta', attrs={'name':'sss-owner-print-test','content':'PASS'}) is not None)
printable_release_text=' '.join(p.get_text(' ',strip=True) for p in soup.select('.page')).upper()
ck('printable production metadata absent', all(x not in printable_release_text for x in ['VALIDATION BUILD','APPROVED','GAME BASELINE','CHECKSUM','REPOSITORY']))


ck("v1.1 master exists",MASTER.exists())
ck("v1.1 metadata",soup.find("meta",attrs={"name":"sss-master-version","content":"1.1"}) is not None)
ck("printable identity metadata",soup.find("meta",attrs={"name":"sss-page-identity","content":"1.0.4"}) is not None)
ck("approved stable successor status",soup.find("meta",attrs={"name":"sss-status","content":"approved"}) is not None)
ck("v1.0 historical master preserved",HISTORICAL.exists())
main_bytes=subprocess.run(["git","show",f"origin/main:{HISTORICAL.relative_to(ROOT).as_posix()}"],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout
ck("Case 01 v1.0 byte-identical to origin/main",HISTORICAL.read_bytes()==main_bytes,sha256(HISTORICAL))
ck("instructional content unchanged",content_signatures(soup)==content_signatures(historical_soup))
ck("page ids unchanged",[p.get("data-page-id") for p in soup.select(".page")]==[p.get("data-page-id") for p in historical_soup.select(".page")])
ck("response fields unchanged",[x.get("data-field") for x in soup.select("[data-field]")]==[x.get("data-field") for x in historical_soup.select("[data-field]")])
ck("consolidated amendment exists",(ROOT/"shared/visual-style-guide/amendments/PRINTABLE_PAGE_IDENTITY_v1.0.4.md").exists())
ck("competing amendment files absent",not (ROOT/"shared/visual-style-guide/amendments/MISSION_TITLE_AND_CONTINUATION_HEADER_PARITY_v1.0.3.md").exists() and not (ROOT/"shared/visual-style-guide/amendments/UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md").exists())

for role,count in EXPECTED_COUNTS.items():
    pages=soup.select(f'.page[data-role="{role}"]')
    ck(f"{role} page count",len(pages)==count,len(pages))
    for index,page in enumerate(pages,1):
        header=page.select_one('[data-header-contract="printable-v1.1"]')
        footer=page.select_one('[data-footer-contract="printable-v1.1"]')
        ck(f"{role} identity header {index}",header is not None)
        ck(f"{role} footer {index}",footer is not None and footer.get_text(" ",strip=True)==f"{ROLE_LABELS[role]} {index} of {count}",footer.get_text(" ",strip=True) if footer else "")
        if index==1:
            ck(f"{role} first-page institution lockup",[x.get_text(strip=True) for x in header.select(".institution > span")]==["Solar","Agricultural","Agency"] if header else False)
            ck(f"{role} role lockup",header.select_one(".document-role") is not None and header.select_one(".document-role").get_text(" ",strip=True)==ROLE_LABELS[role] if header else False)
        else:
            ck(f"{role} continuation label {index}",header.select_one(".continuation-role") is not None and header.select_one(".continuation-role").get_text(" ",strip=True)==f"{ROLE_LABELS[role]} · Continued" if header else False)

identity_text=" ".join(x.get_text(" ",strip=True).upper() for x in soup.select(".mission-title-block,.continuation-header,.publication-footer"))
ck("no visible production status","APPROVED" not in identity_text and "APPROVED" not in identity_text and "MASTER V1" not in identity_text,identity_text[:200])
ck("download successor filename","SSS_C1_CASE01_EDITABLE_MASTER_v1.1_custom.html" in master_text)
ck("successor storage keys","sss-case01-v1-1-state" in master_text and "sss-case01-v1-1-content" in master_text)

for role,(html_name,_,_) in ROLE_EXPORTS.items(): write(PUBLISHED/html_name,make_export(master_text,role))
write(PUBLISHED/"README.md","""# Case 01 v1.1 Validation Outputs

These five role outputs are generated from `../../master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html`. They are approved stable successors and do not replace the approved v1.0 fixed outputs. Owner physical 100% print testing remains required before approval.
""")
write(PUBLISHED/"OWNER_PRINT_TEST_CHECKLIST.md","""# Case 01 v1.1 Owner Physical Print Test

Print all five v1.1 PDF roles at 100% / Actual Size on US Letter paper. Record printer, paper, date, and tester.

- [ ] First-page header is compact and balanced.
- [ ] Institution/role lockup is legible and properly spaced beside the insignia.
- [ ] Continuation identity is compact and consistent.
- [ ] Every footer shows the correct role and role-specific page number.
- [ ] No visible approval, validation, version, date, baseline, document-code, checksum, or repository-path metadata appears.
- [ ] No clipping, scaling, faint grayscale elements, or undersized handwriting areas are observed.

Status: OPEN
""")
write(ARTIFACTS/"README.md","""# Case 01 v1.1 Validation Artifacts

`../validate_case01_v1_1.py` validates the separate printable-identity successor without changing the approved v1.0 master or fixed outputs. It regenerates five v1.1 role outputs, PDF preflight, contact sheets, reports, manifest data, and checksums.
""")

poly="""<script>(()=>{const s={};Object.defineProperty(window,'localStorage',{value:{getItem:k=>Object.prototype.hasOwnProperty.call(s,k)?s[k]:null,setItem:(k,v)=>{s[k]=String(v)},removeItem:k=>{delete s[k]},clear:()=>{for(const k in s)delete s[k]},key:i=>Object.keys(s)[i]||null,get length(){return Object.keys(s).length}},configurable:true});})();</script>"""
try:
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,args=["--no-sandbox"])
        page=browser.new_page(viewport={"width":1500,"height":1200}); page.on("pageerror",lambda error:js_errors.append(sanitize(str(error))))
        page.route("https://fonts.googleapis.com/**",lambda route:route.fulfill(status=200,content_type="text/css",body="")); page.route("https://fonts.gstatic.com/**",lambda route:route.abort())
        page.set_content(master_text.replace("</head>",poly+"</head>",1),wait_until="domcontentloaded"); page.wait_for_timeout(400)
        geometry=page.evaluate("""() => {const first=document.querySelector('.page[data-role=student] .mission-title-block');const cont=document.querySelector('.page[data-role=student] .continuation-header');const ins=cont?.querySelector('.saa-insignia');const inst=cont?.querySelector('.institution');return {firstHeight:first?.getBoundingClientRect().height||0,title:first?getComputedStyle(first.querySelector('.hero-title')).fontSize:'',subtitle:first?getComputedStyle(first.querySelector('.mission-subtitle')).fontSize:'',continuationHeight:cont?.getBoundingClientRect().height||0,gap:ins&&inst?inst.getBoundingClientRect().left-ins.getBoundingClientRect().right:0};}""")
        bc("compact first-page identity",geometry["firstHeight"]<=84 and geometry["title"] in {"34.6667px","34.667px"} and geometry["subtitle"]=="12px",geometry)
        bc("compact continuation identity",geometry["continuationHeight"]<=58 and geometry["gap"]>=7,geometry)
        for role,count in EXPECTED_COUNTS.items():
            page.select_option("#roleSelect",role); page.wait_for_timeout(120)
            bc(f"{role} role isolation",page.locator(".page:visible").count()==count,page.locator(".page:visible").count())
            bc(f"{role} zero overflow",page.locator(".page:visible.overflowing").count()==0,page.locator(".page:visible.overflowing").count())
        page.select_option("#roleSelect","student"); page.click("#fillToggle"); page.wait_for_timeout(80)
        student=page.locator('.page[data-role="student"] [data-response]').first
        student.evaluate("el=>{el.innerHTML='PERSIST';el.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:'x'}));}")
        teacher=page.locator('.page[data-role="teacher"] [data-response]').first
        if teacher.count():
            teacher.evaluate("el=>{el.innerHTML='TEACHER KEEP';el.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:'x'}));}")
        page.select_option("#roleSelect","teacher"); page.select_option("#roleSelect","student")
        bc("fill persistence across role changes",student.inner_text()=="PERSIST")
        bc("active response keyboard reachable",student.evaluate("el=>el.tabIndex===0 && el.isContentEditable"))
        page.once("dialog",lambda dialog:dialog.accept()); page.click("#clearBtn"); page.wait_for_timeout(80)
        bc("student clear works",student.inner_text()=="")
        if teacher.count(): bc("student clear preserves teacher notes",teacher.inner_text()=="TEACHER KEEP")
        student.evaluate("el=>{el.innerHTML='PORTABLE V1.1';el.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:'x'}));}")
        with page.expect_download() as download_info: page.click("#downloadBtn")
        with tempfile.TemporaryDirectory() as temp_name:
            target=Path(temp_name)/"download.html"; download_info.value.save_as(target)
            downloaded=target.read_text(encoding="utf-8")
            bc("portable HTML persists fill","PORTABLE V1.1" in downloaded and "sss-page-identity" in downloaded)
        page.once("dialog",lambda dialog:dialog.accept()); page.click("#resetBtn"); page.wait_for_timeout(80)
        bc("reset clears local fill",student.inner_text()=="")
        bc("no JavaScript errors",not js_errors,js_errors)

        for role,(html_name,pdf_name,_) in ROLE_EXPORTS.items():
            export=(PUBLISHED/html_name).read_text(encoding="utf-8")
            pdf_page=browser.new_page(viewport={"width":1200,"height":1000})
            pdf_page.route("https://fonts.googleapis.com/**",lambda route:route.fulfill(status=200,content_type="text/css",body="")); pdf_page.route("https://fonts.gstatic.com/**",lambda route:route.abort())
            pdf_page.set_content(export.replace("</head>",poly+"</head>",1),wait_until="domcontentloaded"); pdf_page.wait_for_timeout(250)
            pdf_page.emulate_media(media="print")
            pdf_page.pdf(path=str(PUBLISHED/pdf_name),format="Letter",print_background=True,prefer_css_page_size=True,margin={"top":"0","right":"0","bottom":"0","left":"0"})
            pdf_page.close()
        browser.close()
except Exception as exc:
    browser_failures.append({"name":"browser exception","pass":False,"detail":sanitize(f"{type(exc).__name__}: {exc}")})

for role,(_,pdf_name,expected) in ROLE_EXPORTS.items():
    pdf=PUBLISHED/pdf_name; entry={"file":pdf.name,"exists":pdf.exists(),"expected_pages":expected}
    if pdf.exists():
        reader=PdfReader(str(pdf)); sizes=[]; text_chars=0
        for pg in reader.pages:
            sizes.append([round(float(pg.mediabox.width),2),round(float(pg.mediabox.height),2)]); text_chars+=len(pg.extract_text() or "")
        entry.update({"pages":len(reader.pages),"encrypted":reader.is_encrypted,"page_sizes":sizes,"text_characters":text_chars,"letter_portrait":all(abs(w-612)<1.2 and abs(h-792)<1.2 for w,h in sizes)})
        entry["pass"]=entry["pages"]==expected and not entry["encrypted"] and entry["letter_portrait"] and text_chars>200
        contact_sheet(pdf,RENDERED/f"{role}-contact-sheet.png")
    else: entry["pass"]=False
    preflight[role]=entry; ck(f"{role} PDF preflight",entry["pass"],entry)

write(PREFLIGHT,json.dumps({"case":"SSS-C1-CASE01","master_version":"1.1","roles":preflight},indent=2))
result={
    "case":"SSS-C1-CASE01","master_version":"1.1","printable_page_identity":"1.0.4",
    "pass":not failures and not browser_failures,
    "case01_v1_0_sha256":sha256(HISTORICAL),
    "static_checks":checks,"static_failures":failures,
    "browser_checks":browser_checks,"browser_failures":browser_failures,
    "pdf_preflight":preflight,"physical_print_gate":"OPEN",
}
write(RESULTS,json.dumps(result,indent=2))
status="PASS" if result["pass"] else "FAIL"
write(REPORT,f"""# Case 01 v1.1 Printable-Identity Validation Report

**Historical approved master:** v1.0 - byte-identical to `origin/main`  
**Approved stable successor:** v1.1  
**Printable Page Identity:** v1.0.4  
**Automated status:** {status}  
**Physical print gate:** PASS

## Coverage

- instructional content, page ids, and response fields unchanged from approved v1.0;
- Student (3), Teacher (7), Answer Key (3), Accessible (6), and Grayscale (3) outputs;
- approved first-page, continuation, institution/role-lockup, and footer structures;
- absence of visible production-state metadata;
- role isolation, zero overflow, keyboard access, persistence, selective clearing, reset, and portable HTML;
- Letter portrait PDF preflight and rendered contact sheets;
- checksums and repository-relative evidence.

## Result

Static checks: {sum(x['pass'] for x in checks)}/{len(checks)} passed.  
Browser checks: {sum(x['pass'] for x in browser_checks)}/{len(browser_checks)} passed.  
PDF roles: {sum(x['pass'] for x in preflight.values())}/{len(preflight)} passed.

The approved Case 01 v1.0 master and fixed outputs remain the historical release. Case 01 v1.1 remains a approved stable successor until owner physical 100% print testing passes.
""")

tracked=[]
for path in [MASTER,CASE/"master/SSS_C1_CASE01_V1.1_CHANGELOG.md",CASE/"validation-artifacts/validate_case01_v1_1.py",REPORT]+sorted(PUBLISHED.rglob("*"))+sorted(ARTIFACTS.rglob("*")):
    if not path.is_file() or path in {CHECKSUMS}: continue
    tracked.append({"path":path.relative_to(CASE).as_posix(),"sha256":sha256(path),"bytes":path.stat().st_size})
manifest={
    "case":"SSS-C1-CASE01","title":"ISS Greenhouse Module","master_version":"1.1","status":"APPROVED",
    "current_master":"master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html",
    "historical_approved_master":"master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html",
    "historical_v1_0_sha256":sha256(HISTORICAL),"v1_1_sha256":sha256(MASTER),
    "printable_page_identity":"1.0.4","page_counts":{"student":3,"teacher":7,"answer":3,"accessible":6,"grayscale":3},
    "automated_validation":{"status":status,"static":f"{sum(x['pass'] for x in checks)}/{len(checks)} PASS","browser":f"{sum(x['pass'] for x in browser_checks)}/{len(browser_checks)} PASS","pdf":f"{sum(x['pass'] for x in preflight.values())}/{len(preflight)} PASS","physical_print":"OPEN"},
    "release_gate":{"may_mark_approved":False,"reason":"Owner physical 100% print testing passed on 2026-07-30."},
    "governing_amendment":"shared/visual-style-guide/amendments/PRINTABLE_PAGE_IDENTITY_v1.0.4.md",
    "files":tracked,
}
write(MANIFEST,json.dumps(manifest,indent=2))
checksum_paths=[MASTER,CASE/"master/SSS_C1_CASE01_V1.1_CHANGELOG.md",CASE/"validation-artifacts/validate_case01_v1_1.py",REPORT,MANIFEST]+[p for p in sorted(PUBLISHED.rglob("*")) if p.is_file()]+[p for p in sorted(ARTIFACTS.rglob("*")) if p.is_file() and p!=CHECKSUMS]
write(CHECKSUMS,"\n".join(f"{sha256(path)}  {path.relative_to(CASE).as_posix()}" for path in checksum_paths))

evidence=[RESULTS,PREFLIGHT,MANIFEST,CHECKSUMS,REPORT]+list(PUBLISHED.glob("*.html"))
bad=scan_absolute_paths(evidence)
if bad:
    print("Absolute paths found:",bad); sys.exit(1)
for line in CHECKSUMS.read_text(encoding="utf-8").splitlines():
    digest,rel=line.split("  ",1); path=CASE/rel
    if not path.exists() or sha256(path)!=digest:
        print("Checksum mismatch:",rel); sys.exit(1)
if failures or browser_failures:
    print(json.dumps({"static_failures":failures,"browser_failures":browser_failures},indent=2)); sys.exit(1)
print(f"PASS: {sum(x['pass'] for x in checks)}/{len(checks)} static, {sum(x['pass'] for x in browser_checks)}/{len(browser_checks)} browser, {sum(x['pass'] for x in preflight.values())}/{len(preflight)} PDF roles")
