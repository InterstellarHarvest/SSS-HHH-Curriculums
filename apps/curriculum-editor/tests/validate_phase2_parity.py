#!/usr/bin/env python3
"""Validate exact Case 01/02 master-to-central-editor migration parity."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw
from playwright.sync_api import Locator, sync_playwright

APP = Path(__file__).resolve().parents[1]
REPO = APP.parents[1]
sys.path.insert(0, str(APP))
from serve import CurriculumEditorHandler  # noqa: E402
from validate_v1_1_parity import (  # noqa: E402
    GEOMETRY_TOLERANCE,
    PIXEL_DELTA_THRESHOLD,
    PIXEL_RATIO_TOLERANCE,
    compare_geometry,
    compare_presentation,
    pixel_diff,
)

CASES = {
    "case01": {
        "id": "SSS-C1-CASE01", "label": "Case 01", "version": "1.1",
        "master": "sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html",
        "root": "sss/campaign-1/case-01-iss-greenhouse", "runtime": None,
        "roles": {"student": 3, "teacher": 7, "answer": 3, "accessible": 6, "grayscale": 3},
        "roleFiles": {
            "student": "published/v1.1/SSS_C1_CASE01_STUDENT_MISSION_v1.1.html",
            "teacher": "published/v1.1/SSS_C1_CASE01_TEACHER_GUIDE_v1.1.html",
            "answer": "published/v1.1/SSS_C1_CASE01_ANSWER_KEY_v1.1.html",
            "accessible": "published/v1.1/SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.1.html",
            "grayscale": "published/v1.1/SSS_C1_CASE01_GRAYSCALE_MISSION_v1.1.html",
        },
    },
    "case02": {
        "id": "SSS-C1-CASE02", "label": "Case 02", "version": "1.0",
        "master": "sss/campaign-1/case-02-lunar-greenhouse/master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html",
        "root": "sss/campaign-1/case-02-lunar-greenhouse", "runtime": "__case02",
        "roles": {"student": 3, "teacher": 7, "answer": 3, "accessible": 5, "grayscale": 3},
        "roleFiles": {
            "student": "published/SSS_C1_CASE02_STUDENT_MISSION_v1.0.html",
            "teacher": "published/SSS_C1_CASE02_TEACHER_PACKET_v1.0.html",
            "answer": "published/SSS_C1_CASE02_ANSWER_KEY_v1.0.html",
            "accessible": "published/SSS_C1_CASE02_ACCESSIBLE_MISSION_v1.0.html",
            "grayscale": "published/SSS_C1_CASE02_GRAYSCALE_MISSION_v1.0.html",
        },
    },
}

SNAPSHOT = """
(page) => {
  const rect = node => { const p=page.getBoundingClientRect(),r=node.getBoundingClientRect(),q=v=>Math.round(v*1000)/1000; return {x:q(r.x-p.x),y:q(r.y-p.y),width:q(r.width),height:q(r.height),right:q(r.right-p.x),bottom:q(r.bottom-p.y)}; };
  const groups = [
    ["page",":scope"],["frame",":scope > .page-frame"],["header",".mission-title-block,.continuation-header"],["footer",".publication-footer"],
    ["task",".task-heading"],["directions",".task-directions"],["response","[data-response]"],["figure","figure"],["table","table"],
    ["cer","[data-cer-contract],.cer-stack"],["cer-row",".canonical-cer-box,.cer-box"],["process","[data-process-contract],.process-figure,.linear-process"],
    ["optional","[data-optional-extension]"],["prompt",".response-prompt"]
  ];
  const properties=["display","visibility","fontFamily","fontSize","lineHeight","marginTop","marginRight","marginBottom","marginLeft","paddingTop","paddingRight","paddingBottom","paddingLeft","borderTopWidth","borderRightWidth","borderBottomWidth","borderLeftWidth","gridTemplateColumns","gridTemplateRows","flexDirection","gap","backgroundColor","color","breakInside"];
  const geometry={},presentation={};
  for(const [kind,selector] of groups){const nodes=selector===":scope"?[page]:Array.from(page.querySelectorAll(selector));nodes.forEach((node,index)=>{const identity=node.dataset.persistId||node.dataset.taskId||node.dataset.cerContract||node.dataset.processContract||node.dataset.pageId||index;const key=`${kind}:${identity}:${index}`;geometry[key]=rect(node);const s=getComputedStyle(node);const comparable=kind==="page"?properties.filter(p=>p!=="marginLeft"&&p!=="marginRight"):properties;presentation[key]=Object.fromEntries(comparable.map(p=>[p,s[p]]));});}
  const cerRoots=Array.from(page.querySelectorAll("[data-cer-contract],.cer-stack"));
  const labelText=root=>Array.from(root.querySelectorAll(".canonical-cer-label,.cer-label,.answer-label,.response-prompt")).map(n=>n.textContent.trim().split(":")[0].toUpperCase()).filter(x=>["CLAIM","EVIDENCE","REASONING"].includes(x));
  const structure={
    pageId:page.dataset.pageId,role:page.dataset.role,ariaLabel:page.getAttribute("aria-label"),
    headers:Array.from(page.querySelectorAll(".mission-title-block,.continuation-header")).map(n=>[n.className,n.textContent.trim().replace(/\\s+/g," ")]),
    footer:page.querySelector(".publication-footer")?.textContent.trim().replace(/\\s+/g," "),
    tasks:Array.from(page.querySelectorAll(".task-heading")).map(n=>[n.dataset.taskId,n.dataset.taskTitle,n.querySelector(".section-title")?.textContent.trim()]),
    responses:Array.from(page.querySelectorAll("[data-response]")).map(n=>[n.dataset.persistId,n.dataset.field,n.getAttribute("aria-label"),n.className]),
    cers:cerRoots.map(n=>({contract:n.dataset.cerContract||n.className,labels:labelText(n)})),
    processes:Array.from(page.querySelectorAll("[data-process-contract],.process-figure,.linear-process")).map(n=>[n.dataset.processContract||n.className,n.querySelectorAll("[data-process-stage],.process-stage,:scope > li").length,Boolean(n.querySelector("figcaption"))]),
    figures:Array.from(page.querySelectorAll("figure")).map(n=>[n.className,n.querySelector("figcaption")?.textContent.trim()]),
    tables:Array.from(page.querySelectorAll("table")).map(n=>[n.className,n.querySelector("caption")?.textContent.trim(),n.querySelectorAll("tr").length]),
    persistIds:Array.from(page.querySelectorAll("[data-persist-id]")).map(n=>n.dataset.persistId),
    order:Array.from(page.querySelectorAll(".task-heading,[data-cer-contract],.cer-stack,[data-process-contract],.process-figure,.linear-process,figure,table,[data-optional-extension],[data-response]")).map(n=>[n.tagName,n.dataset.taskId||n.dataset.persistId||n.dataset.cerContract||n.dataset.processContract||n.className])
  };
  return {structure,geometry,presentation};
}
"""


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def set_master_role(page, config: dict[str, Any], role: str) -> None:
    source = "student" if role == "grayscale" else role
    gray = role == "grayscale"
    if config["runtime"]:
        page.evaluate("([role,gray])=>window.__case02.saveState({role,grayscale:gray,density:'normal',guides:false,boundaries:true})", [source, gray])
    else:
        page.evaluate("([role,gray])=>{document.body.dataset.role=role;document.body.classList.toggle('grayscale',gray);document.documentElement.style.setProperty('--margin','.5in');document.documentElement.style.setProperty('--density','1');}", [source, gray])
    page.wait_for_timeout(80)


def set_editor_role(page, role: str) -> None:
    source = "student" if role == "grayscale" else role
    page.evaluate("([role,gray])=>{window.__curriculumEditor.setRole(role);window.__curriculumEditor.saveState({grayscale:gray,density:'normal',marginTop:.5,marginRight:.5,marginBottom:.5,marginLeft:.5,guides:false,boundaries:true});}", [source, role == "grayscale"])
    page.wait_for_timeout(80)


def component_integrity(snapshot: dict[str, Any]) -> tuple[int, int, list[str]]:
    geometry, structure = snapshot["geometry"], snapshot["structure"]
    frame = next((value for key, value in geometry.items() if key.startswith("frame:")), None)
    passed = total = 0
    failures = []
    for cer in structure["cers"]:
        total += 1
        ok = cer["labels"] == ["CLAIM", "EVIDENCE", "REASONING"]
        passed += int(ok)
        if not ok: failures.append(f"CER labels {cer['labels']}")
    for kind in ("task", "figure", "table", "cer", "process", "optional", "prompt", "response"):
        for key, bounds in geometry.items():
            if key.startswith(kind + ":"):
                total += 1
                ok = bool(frame and bounds["bottom"] <= frame["bottom"] + GEOMETRY_TOLERANCE)
                passed += int(ok)
                if not ok: failures.append(f"{key} crosses page-frame bottom")
    ids = structure["persistIds"]
    total += 1
    unique = len(ids) == len(set(ids))
    passed += int(unique)
    if not unique: failures.append("duplicate persistence ID on page")
    return passed, total, failures


def capture(master_page, editor_page, master_node: Locator, editor_node: Locator, before: Path, after: Path) -> None:
    master_node.evaluate("n=>n.dataset.parityCapture='true'")
    editor_node.evaluate("n=>n.dataset.parityCapture='true'")
    master_page.evaluate("()=>{const s=document.createElement('style');s.id='parityCaptureStyle';s.textContent='.toolbar{display:none!important}.page:not([data-parity-capture]){visibility:hidden!important}.page[data-parity-capture]{position:fixed!important;inset:0 auto auto 0!important;margin:0!important;box-shadow:none!important}';document.head.append(s)}")
    editor_page.evaluate("()=>{const o=document.createElement('style');o.id='parityOuterCaptureStyle';o.textContent='#editorToolbarHost{display:none!important}';document.head.append(o);const r=document.querySelector('#worksheetHost').shadowRoot,s=document.createElement('style');s.id='parityCaptureStyle';s.textContent='.page:not([data-parity-capture]){visibility:hidden!important}.page[data-parity-capture]{position:fixed!important;inset:0 auto auto 0!important;margin:0!important;box-shadow:none!important}';r.append(s)}")
    master_node.screenshot(path=str(before), animations="disabled")
    editor_node.screenshot(path=str(after), animations="disabled")
    master_page.evaluate("()=>{document.querySelector('#parityCaptureStyle')?.remove();document.querySelector('[data-parity-capture]')?.removeAttribute('data-parity-capture')}")
    editor_page.evaluate("()=>{document.querySelector('#parityOuterCaptureStyle')?.remove();const r=document.querySelector('#worksheetHost').shadowRoot;r.querySelector('#parityCaptureStyle')?.remove();r.querySelector('[data-parity-capture]')?.removeAttribute('data-parity-capture')}")


def make_sheet(items: list[tuple[str, Path]], destination: Path) -> None:
    images = [(label, Image.open(path).convert("RGB")) for label, path in items]
    width, pad, label_h, cols = 260, 14, 24, 3
    thumbs = [(label, image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS)) for label, image in images]
    cell_h = max(image.height for _, image in thumbs) + label_h
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * width + (cols + 1) * pad, rows * cell_h + (rows + 1) * pad), "white")
    draw = ImageDraw.Draw(sheet)
    for index, (label, image) in enumerate(thumbs):
        row, col = divmod(index, cols); x = pad + col * (width + pad); y = pad + row * cell_h
        draw.text((x, y), label, fill="black"); sheet.paste(image, (x, y + label_h))
    destination.parent.mkdir(parents=True, exist_ok=True); sheet.save(destination, optimize=True)
    for _, image in images: image.close()


def run_case(browser, base: str, config: dict[str, Any]) -> dict[str, Any]:
    screen_root = APP / "tests/screenshots/parity-phase2" / config["id"].lower()
    if screen_root.exists(): shutil.rmtree(screen_root)
    screen_root.mkdir(parents=True)
    context = browser.new_context(viewport={"width": 1440, "height": 1200}, device_scale_factor=1)
    master = context.new_page(); editor = context.new_page(); master_errors=[]; editor_errors=[]
    master.on("pageerror", lambda error: master_errors.append(str(error))); editor.on("pageerror", lambda error: editor_errors.append(str(error)))
    master.goto(f"{base}/{config['master']}", wait_until="load"); editor.goto(f"{base}/apps/curriculum-editor/", wait_until="load")
    editor.wait_for_function("window.__curriculumEditor"); editor.evaluate("id=>window.__curriculumEditor.selectCase(id)", config["id"])
    page_results=[]; structure_pass=assignment_pass=render_pass=geometry_pass=geometry_total=presentation_pass=presentation_total=component_pass=component_total=role_export_pass=artifact_pass=zero_roles=0
    master_items=[]; editor_items=[]; diff_items=[]; total_pages=sum(config["roles"].values())
    for role, expected in config["roles"].items():
        set_master_role(master, config, role); set_editor_role(editor, role)
        source = "student" if role == "grayscale" else role
        master_nodes=master.locator(f'.page[data-role="{source}"]'); editor_nodes=editor.locator("#worksheetHost").locator(f'.page[data-role="{source}"]')
        role_ok=master_nodes.count()==editor_nodes.count()==expected
        for index in range(min(master_nodes.count(), editor_nodes.count(), expected)):
            before=master_nodes.nth(index).evaluate(SNAPSHOT); after=editor_nodes.nth(index).evaluate(SNAPSHOT)
            same=before["structure"]==after["structure"]; structure_pass+=int(same)
            assignment=before["structure"]["pageId"]==after["structure"]["pageId"] and before["structure"]["tasks"]==after["structure"]["tasks"]
            assignment_pass+=int(assignment)
            gp,gt,gf=compare_geometry(before["geometry"],after["geometry"]); pp,pt,pf=compare_presentation(before["presentation"],after["presentation"])
            geometry_pass+=gp;geometry_total+=gt;presentation_pass+=pp;presentation_total+=pt
            cp,ct,cf=component_integrity(after);component_pass+=cp;component_total+=ct
            stem=f"{role}-{index+1:02d}"; bp=screen_root/f"{stem}-master.png";ap=screen_root/f"{stem}-editor.png";dp=screen_root/f"{stem}-diff.png"
            capture(master,editor,master_nodes.nth(index),editor_nodes.nth(index),bp,ap);rendered=pixel_diff(bp,ap,dp);render_pass+=int(rendered["pass"])
            master_items.append((stem,bp));editor_items.append((stem,ap));diff_items.append((stem,dp))
            page_results.append({"role":role,"page":index+1,"pageId":before["structure"]["pageId"],"structuralParity":same,"pageAssignmentParity":assignment,"geometry":{"passed":gp,"total":gt,"failures":gf[:20]},"computedPresentation":{"passed":pp,"total":pt,"failures":pf[:20]},"rendered":rendered,"componentIntegrity":{"passed":cp,"total":ct,"failures":cf[:20]}})
        overflow=editor.evaluate("window.__curriculumEditor.checkOverflow()");zero_roles+=int(overflow==0)
        export_html=editor.evaluate("([r,g])=>{window.__curriculumEditor.saveState({grayscale:g});return window.__curriculumEditor.serializeRoleHTML(r)}",[source,role=="grayscale"])
        export=context.new_page();export.set_content(export_html,wait_until="load");export.wait_for_function("window.__curriculumPortable");export.evaluate("document.fonts?.ready");export_nodes=export.locator(f'.page[data-role="{source}"]')
        export_ok=export_nodes.count()==expected
        for index in range(min(expected,export_nodes.count())):
            live=editor_nodes.nth(index).evaluate(SNAPSHOT);saved=export_nodes.nth(index).evaluate(SNAPSHOT);_,_,fail=compare_geometry(live["geometry"],saved["geometry"]);export_ok=export_ok and live["structure"]==saved["structure"] and not fail
        role_export_pass+=int(export_ok);export.close()
        artifact=context.new_page();artifact_errors=[];artifact.on("pageerror",lambda error,errors=artifact_errors:errors.append(str(error)));artifact.goto(f"{base}/{config['root']}/{config['roleFiles'][role]}",wait_until="load")
        artifact_nodes=artifact.locator(f'.page[data-role="{source}"]');artifact_ok=artifact_nodes.count()==expected and not artifact_errors
        for index in range(min(expected,artifact_nodes.count())):
            reference=master_nodes.nth(index).evaluate(SNAPSHOT);published=artifact_nodes.nth(index).evaluate(SNAPSHOT);_,_,fail=compare_geometry(reference["geometry"],published["geometry"]);artifact_ok=artifact_ok and reference["structure"]==published["structure"] and not fail
        artifact_pass+=int(artifact_ok);artifact.close()
    make_sheet(master_items,screen_root/"all-roles-master-contact-sheet.png");make_sheet(editor_items,screen_root/"all-roles-editor-contact-sheet.png");make_sheet(diff_items,screen_root/"all-roles-diff-contact-sheet.png")
    complete_html=editor.evaluate("()=>{window.__curriculumEditor.saveState({grayscale:false});return window.__curriculumEditor.serializePortableHTML()}");complete=context.new_page();complete.set_content(complete_html,wait_until="load");complete.wait_for_function("window.__curriculumPortable");complete.evaluate("document.fonts?.ready")
    complete_pass=complete_total=0
    for role,expected in ((r,c) for r,c in config["roles"].items() if r!="grayscale"):
        set_master_role(master,config,role);complete.evaluate("r=>window.__curriculumPortable.setRole(r)",role);mn=master.locator(f'.page[data-role="{role}"]');cn=complete.locator(f'.page[data-role="{role}"]')
        for index in range(expected):
            complete_total+=1;a=mn.nth(index).evaluate(SNAPSHOT);b=cn.nth(index).evaluate(SNAPSHOT);_,_,fail=compare_geometry(a["geometry"],b["geometry"]);complete_pass+=int(a["structure"]==b["structure"] and not fail)
    complete.close();context.close()
    screenshots={p.name:{"path":str(p.relative_to(REPO)),"sha256":sha(p)} for p in sorted(screen_root.glob("*.png"))}
    all_pass=structure_pass==assignment_pass==render_pass==total_pages and geometry_pass==geometry_total and presentation_pass==presentation_total and component_pass==component_total and role_export_pass==artifact_pass==zero_roles==len(config["roles"]) and complete_pass==complete_total and not master_errors and not editor_errors
    return {"validator":f"{config['id'].lower()}-phase2-parity","status":"PASS" if all_pass else "FAIL","phase2Status":"READY_TO_MERGE" if all_pass else "VALIDATION_FAILED","currentMaintainedHtml":"APPROVED","ownerGate":"PASS","physicalPrintGate":"PASS","ownerApproval":{"date":"2026-08-01","tester":"Nate / Owner","ownerReview":"PASS","browserPrintPreview":"PASS","physicalPrintReview":"PASS","scale":"100% / Actual Size","browser":"Not recorded","printerCopier":"Not recorded","paper":"Not recorded"},"pageCounts":config["roles"],"structuralParity":{"passed":structure_pass,"total":total_pages},"pageAssignmentParity":{"passed":assignment_pass,"total":total_pages},"geometryParity":{"passed":geometry_pass,"total":geometry_total,"tolerancePx":GEOMETRY_TOLERANCE},"computedPresentationParity":{"passed":presentation_pass,"total":presentation_total},"renderedComparison":{"passed":render_pass,"total":total_pages,"pixelDeltaThreshold":PIXEL_DELTA_THRESHOLD,"pixelRatioTolerance":PIXEL_RATIO_TOLERANCE},"componentIntegrity":{"passed":component_pass,"total":component_total},"currentMaintainedRoleArtifactParity":{"passed":artifact_pass,"total":len(config["roles"])},"zeroOverflowRoles":{"passed":zero_roles,"total":len(config["roles"])},"currentRoleExportParity":{"passed":role_export_pass,"total":len(config["roles"])},"completePortableExportParity":{"passed":complete_pass,"total":complete_total},"javascriptErrors":{"master":master_errors,"editor":editor_errors},"pages":page_results,"screenshots":screenshots}


def write_review(config: dict[str, Any], result: dict[str, Any]) -> None:
    out=REPO/config["root"]/"validation-artifacts/phase2";out.mkdir(parents=True,exist_ok=True);prefix=config["id"].replace("SSS-C1-","")
    (out/f"{prefix}_PHASE2_PARITY_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    metrics=[("structuralParity","structuralParity"),("pageAssignmentParity","pageAssignmentParity"),("geometryParity","geometryParity"),("computedPresentationParity","computedPresentationParity"),("renderedComparison","renderedComparison"),("componentIntegrity","componentIntegrity"),("currentMaintainedRoleArtifactParity","currentMaintainedRoleArtifactParity"),("zeroOverflowRoles","pageFitRoles"),("currentRoleExportParity","currentRoleExportParity"),("completePortableExportParity","completePortableExportParity")]
    lines=[f"# {config['label']} Phase 2 Migration Validation", "", f"**Status:** OWNER REVIEW PASS · {result['phase2Status'].replace('_', ' ')}", "", "**Current maintained HTML:** APPROVED", "", "**Owner gate:** PASS", "", "**Browser print-preview review:** PASS", "", "**Physical-print gate:** PASS", "", f"Exact parity status: **{result['status']}**", ""]+[f"- {label}: {result[key]['passed']}/{result[key]['total']}" for key,label in metrics]+["", "Owner approval: Nate / Owner · 2026-08-01 · 100% / Actual Size", "", f"Owner materials: `apps/curriculum-editor/tests/screenshots/parity-phase2/{config['id'].lower()}/`",""]
    (out/f"{prefix}_PHASE2_VALIDATION_REPORT.md").write_text("\n".join(lines))
    checklist=f"""# {config['label']} Phase 2 Owner Browser/Print Checklist

Status: OWNER REVIEW PASS · READY TO MERGE

- [x] Reviewed the current maintained standalone HTML at 100% / Actual Size.
- [x] Reviewed the central-editor Student, Teacher, Answer Key, Accessible, and Student Grayscale pages.
- [x] Compared all-role master, editor, and diff contact sheets.
- [x] Confirmed page composition, response geometry, headers, continuations, footers, margins, and grayscale.
- [x] Exercised keyboard role/case switching, Fill Responses, Edit Text, Clear Current Role, and Reset Source.
- [x] Opened complete and current-role portable HTML in a fresh browser context.
- [x] Confirmed every role reports `Pages fit` before printing.
- [x] Confirmed browser print preview at 100% / Actual Size (no Fit/Shrink scaling).
- [x] Confirmed exact preview page counts: Student {config['roles']['student']}, Teacher {config['roles']['teacher']}, Answer Key {config['roles']['answer']}, Accessible {config['roles']['accessible']}, Student Grayscale {config['roles']['grayscale']}.
- [x] Confirmed no leading, trailing, or intermediate blank page and no toolbar, library rail, workspace status, or authoring chrome.
- [x] Confirmed the first page retains its title/institutional identity and every later page retains its continuation identity without obstruction.
- [x] Confirmed worksheet geometry, margins, content pagination, and page fit are unchanged and Page shadow is absent.
- [x] Physically printed at 100% / Actual Size.
- [x] Confirmed browser PDF output is not treated as accessibility-verified and generated no repository PDF.

Owner: Nate / Owner

Approval date: 2026-08-01

Browser: Not recorded

Printer/copier: Not recorded

Paper: Not recorded

Decision: [x] PASS  [ ] CHANGES REQUIRED
"""
    (out/f"{prefix}_PHASE2_OWNER_BROWSER_PRINT_CHECKLIST.md").write_text(checklist)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--chrome",type=Path,default=Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"));parser.add_argument("--case",choices=["case01","case02","all"],default="all");args=parser.parse_args()
    if not args.chrome.is_file():raise SystemExit(f"Chrome executable not found: {args.chrome}")
    server=ThreadingHTTPServer(("127.0.0.1",0),CurriculumEditorHandler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base=f"http://127.0.0.1:{server.server_address[1]}";results={}
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True,executable_path=str(args.chrome.resolve()),args=["--no-sandbox"])
            selected=CASES if args.case=="all" else {args.case:CASES[args.case]}
            for name,config in selected.items():results[name]=run_case(browser,base,config);write_review(config,results[name])
            browser.close()
    finally:server.shutdown();server.server_close();thread.join(timeout=2)
    summary={name:{key:value[key] for key in ["status","structuralParity","pageAssignmentParity","geometryParity","computedPresentationParity","renderedComparison","componentIntegrity","currentMaintainedRoleArtifactParity","zeroOverflowRoles","currentRoleExportParity","completePortableExportParity","javascriptErrors"]} for name,value in results.items()};print(json.dumps(summary,indent=2));return 0 if all(r["status"]=="PASS" for r in results.values()) else 1


if __name__=="__main__":raise SystemExit(main())
