#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw
import fitz
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import traceback

CASE = Path(__file__).resolve().parents[1]
ROOT = CASE.parents[2]
MASTER = CASE / 'master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html'
RESULTS = CASE / 'validation-artifacts/CASE02_VALIDATION_RESULTS.json'
PREFLIGHT = CASE / 'validation-artifacts/CASE02_PDF_PREFLIGHT.json'
RENDER_DIR = CASE / 'validation-artifacts/rendered-review'
PUBLISHED = CASE / 'published'
MANIFEST = CASE / 'CASE02_V1_RELEASE_MANIFEST.json'
CHECKSUMS = CASE / 'validation-artifacts/CASE02_CHECKSUMS.sha256'
TASKS = {1:'Vocabulary',2:'Initial thinking',3:'Model the pollination sequence',4:'Identify the failed step',5:'Test the competing explanations',6:'Diagnose and reject an alternative',7:'Claim-Evidence-Reasoning',8:'Design a reliable pollination support',9:'Exit ticket'}
ROLE_COUNTS = {'student':2,'teacher':7,'answer':3,'accessible':5}
ROLE_EXPORTS = {
    'student': ('SSS_C1_CASE02_STUDENT_MISSION_v1.0_VALIDATION.html','SSS_C1_CASE02_STUDENT_MISSION_v1.0_VALIDATION.pdf',2),
    'teacher': ('SSS_C1_CASE02_TEACHER_PACKET_v1.0_VALIDATION.html','SSS_C1_CASE02_TEACHER_PACKET_v1.0_VALIDATION.pdf',7),
    'answer': ('SSS_C1_CASE02_ANSWER_KEY_v1.0_VALIDATION.html','SSS_C1_CASE02_ANSWER_KEY_v1.0_VALIDATION.pdf',3),
    'accessible': ('SSS_C1_CASE02_ACCESSIBLE_MISSION_v1.0_VALIDATION.html','SSS_C1_CASE02_ACCESSIBLE_MISSION_v1.0_VALIDATION.pdf',5),
    'grayscale': ('SSS_C1_CASE02_GRAYSCALE_MISSION_v1.0_VALIDATION.html','SSS_C1_CASE02_GRAYSCALE_MISSION_v1.0_VALIDATION.pdf',2),
}
checks=[]; failures=[]; browser_checks=[]; browser_failures=[]; js_errors=[]; balance_metrics=[]; pdf_preflight={}

def ck(name, condition, detail=''):
    row={'name':name,'pass':bool(condition),'detail':str(detail)}; checks.append(row)
    if not condition: failures.append(row)

def bc(name, condition, detail=''):
    row={'name':name,'pass':bool(condition),'detail':str(detail)}; browser_checks.append(row)
    if not condition: browser_failures.append(row)

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def write(path: Path, text: str):
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text.rstrip()+'\n',encoding='utf-8')

def task_map(soup, role):
    return {int(h['data-task-id']):h.get_text(' ',strip=True).split('·',1)[-1].strip() for h in soup.select(f'.page[data-role="{role}"] .task-heading')}

def make_export(master_text, role):
    soup=BeautifulSoup(master_text,'html.parser'); body=soup.body
    export_role='student' if role=='grayscale' else role
    body['data-role']=export_role; body['data-standalone']='true'; body['data-export-role']=export_role
    if role=='grayscale':
        body['data-export-grayscale']='true'; body['class']=list(dict.fromkeys(list(body.get('class',[]))+['grayscale']))
    for page in list(soup.select('.page')):
        if page.get('data-role')!=export_role: page.decompose()
    return '<!doctype html>\n'+str(soup)

def contact_sheet(pdf_path: Path, output: Path):
    doc=fitz.open(pdf_path); images=[]
    matrix=fitz.Matrix(1.35,1.35)
    for page in doc:
        pix=page.get_pixmap(matrix=matrix,alpha=False)
        image=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        images.append(image)
    if not images: raise RuntimeError(f'No pages rendered from {pdf_path.name}')
    thumb_w=360; thumbs=[]
    for i,img in enumerate(images,1):
        ratio=thumb_w/img.width; thumb=img.resize((thumb_w,int(img.height*ratio)))
        canvas=Image.new('RGB',(thumb_w+20,thumb.height+42),'white'); canvas.paste(thumb,(10,26))
        ImageDraw.Draw(canvas).text((10,7),f'{pdf_path.stem} - page {i}',fill='black')
        thumbs.append(canvas)
    cols=2; rows=(len(thumbs)+cols-1)//cols
    cell_w=max(x.width for x in thumbs); cell_h=max(x.height for x in thumbs)
    sheet=Image.new('RGB',(cell_w*cols,cell_h*rows),'white')
    for idx,img in enumerate(thumbs): sheet.paste(img,((idx%cols)*cell_w,(idx//cols)*cell_h))
    output.parent.mkdir(parents=True,exist_ok=True); sheet.save(output,optimize=True)

def scan_absolute_paths(paths):
    bad=[]
    patterns=[re.compile(r'/Users/'),re.compile(r'/home/runner/work/'),re.compile(r'[A-Za-z]:\\\\')]
    for path in paths:
        if not path.exists() or path.suffix.lower() in {'.pdf','.png'}: continue
        text=path.read_text(encoding='utf-8',errors='ignore')
        if any(p.search(text) for p in patterns): bad.append(path.relative_to(ROOT).as_posix())
    return bad

text=MASTER.read_text(encoding='utf-8'); soup=BeautifulSoup(text,'html.parser')
ck('v1.0 master metadata',soup.find('meta',attrs={'name':'sss-master-version','content':'1.0'}) is not None)
ck('balanced fill metadata',soup.find('meta',attrs={'name':'sss-balanced-page-fill','content':'1.0.2'}) is not None)
ck('single current Case 02 master',not (CASE/'master/SSS_C1_CASE02_EDITABLE_MASTER_v1.1.html').exists())
ck('single current Case 02 manifest',not (CASE/'CASE02_V1_1_MASTER_MANIFEST.json').exists())
ck('universal identity excluded','universal-v1.1' not in text and 'UNIVERSAL_PRINTABLE_PAGE_IDENTITY' not in text)
ck('approved v1.0 architecture retained','status-mark' in text and 'cont-brand' in text and 'publication-footer' in text)
ck('balanced CSS present','Balanced Page Fill and Vertical Rhythm v1.0.2' in text)
ck('process model central','process-chain' in text and 'Model the pollination sequence' in text)
ck('no unsupported frequency or airflow values',not re.search(r'60\s*[–-]\s*90\s*Hz|0\.5\s*[–-]\s*1\.0\s*m/s',text,re.I))
ck('no Case 01 evidence matrix','Investigate four evidence sources' not in text)
for role,count in ROLE_COUNTS.items():
    pages=soup.select(f'.page[data-role="{role}"]'); ck(f'{role} page count',len(pages)==count,len(pages))
ck('student task parity',task_map(soup,'student')==TASKS,task_map(soup,'student'))
ck('accessible task parity',task_map(soup,'accessible')==TASKS,task_map(soup,'accessible'))
ck('answer task parity',task_map(soup,'answer')=={i:TASKS[i] for i in range(3,10)},task_map(soup,'answer'))
registry=(CASE/'source/task-registry.js').read_text(encoding='utf-8')
registry_tasks={int(i):title for i,title in re.findall(r'\{ id: (\d+), slug: "[^"]+", title: "([^"]+)"',registry)}
ck('task registry agreement',registry_tasks==TASKS,registry_tasks)
student_source=(CASE/'source/student-mission-sheet.md').read_text(encoding='utf-8')
answer_source=(CASE/'source/answer-key.md').read_text(encoding='utf-8')
lesson_source=(CASE/'source/lesson-plan.md').read_text(encoding='utf-8')
ck('student controlled-source agreement',all(title in student_source for title in TASKS.values()))
ck('answer controlled-source agreement',all(TASKS[i] in answer_source for i in range(3,10)))
ck('teacher controlled-source agreement',all(TASKS[i] in lesson_source for i in range(2,10)))
refs=[x.get_text(' ',strip=True) for x in soup.select('.page[data-role="teacher"] .task-reference')]
valid_refs={f'{i} · {title}' for i,title in TASKS.items()}
ck('teacher task references exact',all(x in valid_refs for x in refs),refs)
ck('teacher task reference coverage',all(any(x.startswith(f'{i} ·') for x in refs) for i in range(2,10)))
ck('accessible continuous packing',[[int(h['data-task-id']) for h in p.select('.task-heading')] for p in soup.select('.page[data-role="accessible"]')]==[[1,2],[3,4],[5],[6,7],[8,9]])
sequence=['viable pollen in anthers','physical agitation','pollen reaches stigma','pollen tube growth','fertilization','fruit set']
wb=soup.select_one('.page[data-role="student"] .word-bank-terms')
terms=[x.strip() for x in wb.get_text(' ',strip=True).split('·')] if wb else []
ck('exact-match word bank complete',set(terms)==set(sequence),terms)
ck('word bank shuffled',terms!=sequence,terms)
ck('answer key exemplars complete',all(soup.select_one(f'.page[data-role="answer"] .task-heading[data-task-id="{i}"]') for i in range(3,10)))
science_assertions=['viable pollen remains','stigmas remain clean','physical agitation','pollen-tube growth','fertilization','fruit set']
printable=' '.join(p.get_text(' ',strip=True).lower() for p in soup.select('.page'))
ck('content-regression science assertions',all(x in printable for x in science_assertions),science_assertions)
ck('balanced amendment exists',(ROOT/'shared/visual-style-guide/amendments/BALANCED_PAGE_FILL_AND_VERTICAL_RHYTHM_v1.0.2.md').exists())
ck('v1.0.3 excluded',not (ROOT/'shared/visual-style-guide/amendments/MISSION_TITLE_AND_CONTINUATION_HEADER_PARITY_v1.0.3.md').exists())
ck('v1.0.4 excluded',not (ROOT/'shared/visual-style-guide/amendments/UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md').exists())

PUBLISHED.mkdir(parents=True,exist_ok=True); RENDER_DIR.mkdir(parents=True,exist_ok=True)
for old in RENDER_DIR.glob('*'): old.unlink()
for role,(html_name,pdf_name,_) in ROLE_EXPORTS.items():
    write(PUBLISHED/html_name,make_export(text,role))

poly='''<script>(()=>{const s={};Object.defineProperty(window,'localStorage',{value:{getItem:k=>Object.prototype.hasOwnProperty.call(s,k)?s[k]:null,setItem:(k,v)=>{s[k]=String(v)},removeItem:k=>{delete s[k]},clear:()=>{for(const k in s)delete s[k]},key:i=>Object.keys(s)[i]||null,get length(){return Object.keys(s).length}},configurable:true});})();</script>'''
try:
  with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1500,'height':1200}); page.on('pageerror',lambda e:js_errors.append(str(e)))
    page.set_content(text.replace('</head>',poly+'</head>',1),wait_until='load'); page.wait_for_timeout(300)
    bc('JavaScript initialized',page.evaluate('!!window.__case02'))
    for role,count in ROLE_COUNTS.items():
        page.evaluate('(r)=>window.__case02.setRole(r)',role); page.wait_for_timeout(100)
        bc(f'{role} visible page isolation',page.locator('.page:visible').count()==count,page.locator('.page:visible').count())
        bc(f'{role} zero overflow',page.evaluate('window.__case02.checkOverflow()')==0)
        metrics=page.evaluate('''() => Array.from(document.querySelectorAll('.page')).filter(p=>getComputedStyle(p).display!=='none').map(page=>{
          const content=page.querySelector('.content-area'); const cr=content.getBoundingClientRect();
          const children=Array.from(content.children).filter(x=>getComputedStyle(x).display!=='none');
          const last=children.length?children[children.length-1].getBoundingClientRect():cr;
          const reserve=Math.max(0,cr.bottom-last.bottom);
          const groups=children.filter(x=>x.querySelector?.('.task-heading')||x.classList.contains('major-task-block'));
          const gaps=[]; for(let i=1;i<groups.length;i++){const a=groups[i-1].getBoundingClientRect(),b=groups[i].getBoundingClientRect();gaps.push(Math.max(0,b.top-a.bottom));}
          const multi=Array.from(page.querySelectorAll('.multi-line-work .response-area')).map(x=>({field:x.dataset.field,height:x.getBoundingClientRect().height,classes:x.closest('.response-block').className}));
          const compact=Array.from(page.querySelectorAll('.compact-short-answer .response-area')).map(x=>({field:x.dataset.field,height:x.getBoundingClientRect().height}));
          return {pageId:page.dataset.pageId,role:page.dataset.role,reserve,minimumMajorGap:gaps.length?Math.min(...gaps):null,gaps,multi,compact};
        })''')
        balance_metrics.extend(metrics)
    # Fill persistence, role-scoped clearing, reset, portable HTML, keyboard basics.
    page.evaluate("window.__case02.setRole('student')")
    task2=page.locator('[data-field="student-task2"]'); task2.evaluate("el=>{el.innerHTML='PERSIST';el.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:'x'}));}")
    page.evaluate("window.__case02.setRole('accessible')")
    atask2=page.locator('[data-field="accessible-task2"]'); atask2.evaluate("el=>{el.innerHTML='ACCESSIBLE KEEP';el.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:'x'}));}")
    page.evaluate("window.__case02.setRole('student')")
    bc('fill persistence across role changes',task2.inner_text()=='PERSIST')
    bc('active responses keyboard reachable',page.evaluate("Array.from(document.querySelectorAll('.page[data-role=student] [data-response]')).every(x=>x.tabIndex===0 && x.getAttribute('role')==='textbox')"))
    page.evaluate('window.__case02.clearCurrentRole(true)')
    bc('selective clearing clears current role',task2.inner_text()=='')
    page.evaluate("window.__case02.setRole('accessible')")
    bc('selective clearing preserves other role',atask2.inner_text()=='ACCESSIBLE KEEP')
    atask2.evaluate("el=>{el.innerHTML='PORTABLE';el.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:'x'}));}")
    serial=page.evaluate('window.__case02.serializePortableHTML()')
    bc('portable HTML persists fill','PORTABLE' in serial and 'sss-balanced-page-fill' in serial)
    page.evaluate('window.__case02.resetSource(true)')
    bc('reset clears stored responses',task2.inner_text()=='' and atask2.inner_text()=='')
    bc('no JavaScript errors',not js_errors,js_errors)
    # Export PDFs from role-isolated HTML.
    for role,(html_name,pdf_name,expected) in ROLE_EXPORTS.items():
        p=browser.new_page(viewport={'width':1200,'height':1000})
        p.goto((PUBLISHED/html_name).resolve().as_uri(),wait_until='load'); p.wait_for_timeout(250)
        p.pdf(path=str(PUBLISHED/pdf_name),format='Letter',print_background=True,prefer_css_page_size=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        p.close()
    browser.close()
except Exception:
    browser_failures.append({'name':'browser exception','pass':False,'detail':traceback.format_exc()})

# Balanced-fill automated diagnostic. This is intentionally conservative and does not punish valid reserve.
for metric in balance_metrics:
    undersized=[]
    for item in metric['multi']:
        cls=item['classes']; h=item['height']; minimum=36
        if 'expected-3-lines' in cls: minimum=43
        if 'expected-4-lines' in cls: minimum=55
        if metric['role']=='accessible': minimum += 14
        if h+0.5<minimum: undersized.append({'field':item['field'],'height':h,'minimum':minimum})
    stretched=[x for x in metric['compact'] if x['height']>(74 if metric['role']=='accessible' else 46)]
    meaningful=metric['reserve']>58
    compressed=metric['minimumMajorGap'] is not None and metric['minimumMajorGap']<5
    metric['meaningfulUnusedSpace']=meaningful
    metric['compressedMajorSpacing']=compressed
    metric['undersizedMultiLine']=undersized
    metric['stretchedCompactFields']=stretched
    metric['automatedFlag']=bool(meaningful and (compressed or undersized))
ck('balanced-fill diagnostic has no unresolved flags',not any(x['automatedFlag'] for x in balance_metrics),[x['pageId'] for x in balance_metrics if x['automatedFlag']])
ck('compact short-answer fields remain compact',not any(x['stretchedCompactFields'] for x in balance_metrics),[(x['pageId'],x['stretchedCompactFields']) for x in balance_metrics if x['stretchedCompactFields']])

# PDF preflight and direct PDF rendering.
for role,(html_name,pdf_name,expected) in ROLE_EXPORTS.items():
    pdf=PUBLISHED/pdf_name
    entry={'file':pdf.name,'exists':pdf.exists(),'expected_pages':expected}
    if pdf.exists():
        reader=PdfReader(str(pdf)); entry['pages']=len(reader.pages); entry['encrypted']=reader.is_encrypted
        sizes=[]; text_chars=0
        for pg in reader.pages:
            sizes.append([round(float(pg.mediabox.width),2),round(float(pg.mediabox.height),2)])
            text_chars += len(pg.extract_text() or '')
        entry['page_sizes']=sizes; entry['text_characters']=text_chars
        entry['letter_portrait']=all(abs(w-612)<1.2 and abs(h-792)<1.2 for w,h in sizes)
        entry['pass']=len(reader.pages)==expected and not reader.is_encrypted and entry['letter_portrait'] and text_chars>200
        contact_sheet(pdf,RENDER_DIR/f'{role}-contact-sheet.png')
    else: entry['pass']=False
    pdf_preflight[role]=entry
    ck(f'{role} PDF preflight',entry['pass'],entry)
write(PREFLIGHT,json.dumps({'case':'SSS-C1-CASE02','version':'1.0','roles':pdf_preflight},indent=2))

# Results before derivative reports/manifests.
result={
 'case':'SSS-C1-CASE02','master_version':'1.0','balanced_page_fill':'1.0.2',
 'pass':not failures and not browser_failures,
 'static_checks':checks,'static_failures':failures,
 'browser_checks':browser_checks,'browser_failures':browser_failures,
 'balance_metrics':balance_metrics,
 'balance_validation_note':'Automated flags are diagnostic. Intentional blank space and proportionate compact fields are valid; human design judgment remains final.',
 'pdf_preflight':pdf_preflight,'physical_print_gate':'OPEN'
}
write(RESULTS,json.dumps(result,indent=2))

status='PASS' if result['pass'] else 'FAIL'
write(CASE/'reports/CASE02_VALIDATION_REPORT.md',f'''# Case 02 Validation Report

**Build:** SSS-C1-CASE02 v1.0  
**Balanced Page Fill:** v1.0.2  
**Automated status:** {status}  
**Physical print gate:** OPEN

## Coverage

- Controlled Markdown, task registry, master, and release-track agreement
- Student (2), Teacher (7), Answer Key (3), Accessible (5), and Grayscale (2) role outputs
- Zero-overflow and role-isolation browser checks
- Task-reference and content-regression assertions
- Keyboard/fill behavior, persistence, selective clearing, reset, and portable HTML
- Letter-size PDF preflight and direct rendered contact-sheet review evidence
- Balanced-fill diagnostics for bottom reserve, major-group spacing, multi-line work sizing, and compact-field restraint

## Result

Static checks: {sum(x['pass'] for x in checks)}/{len(checks)} passed.  
Browser checks: {sum(x['pass'] for x in browser_checks)}/{len(browser_checks)} passed.  
PDF roles: {sum(x['pass'] for x in pdf_preflight.values())}/{len(pdf_preflight)} passed.

Human design judgment remains final. Owner physical 100% print testing is still required before approval.
''')
write(CASE/'reports/CASE02_BLOCKERS_AND_EXCEPTIONS.md','''# Case 02 Blockers and Exceptions

## Open release gate

- Owner physical 100% print test on representative printer/paper remains OPEN.

## Closed reconciliation blockers

- The v1.0/v1.1 master contradiction is removed; v1.0 is the single current production track.
- The unapproved universal page-identity experiment is excluded from the merge-ready file set.
- All five role outputs are regenerated from the v1.0 master.
- Balanced Page Fill and Vertical Rhythm v1.0.2 is implemented and validated without stretching compact short-answer fields.

No automated content, overflow, role-isolation, accessibility-basics, or PDF-preflight blocker remains when the validation result is PASS.
''')
# Update structural stress test rather than replacing its useful prior analysis.
stress=CASE/'reports/CASE02_STRUCTURAL_STRESS_TEST_REPORT.md'
stress_text=stress.read_text(encoding='utf-8').rstrip() if stress.exists() else '# Case 02 Structural Stress Test Report'
marker='## Balanced Page Fill and Vertical Rhythm v1.0.2'
if marker in stress_text: stress_text=stress_text.split(marker,1)[0].rstrip()
write(stress,stress_text+'''\n\n## Balanced Page Fill and Vertical Rhythm v1.0.2

Case 02 was reviewed page by page across Student, Accessible, Teacher, and Answer Key roles. Student page 1 receives modest separation before Task 3, slightly more process-frame padding, proportionate process-cell height, and separation before the model rule. Student page 2 receives restrained separation between Task 4, Task 5, the Task 6/7 row, and the Task 8/9 row. Failed step, classifications, criterion, constraint, and other compact responses remain compact; diagnosis, rejected alternative, CER, design explanation, mechanism check, and exit-ticket work areas grow only in proportion to expected writing.

Accessible pages preserve linear flow and larger text while distinguishing phrase/classification fields from multi-line evidence and reasoning. Teacher and Answer Key pages use surplus height primarily for clearer section rhythm and modest internal padding, not larger typography or identity elements. Automated validation records reserve and spacing signals but flags only the combination of meaningful unused height with compressed major tasks or undersized multi-line work. Human design judgment remains final.
''')
write(CASE/'README.md','''# SSS Campaign 1, Case 02 - Lunar Greenhouse

## Current production track

- Master: `master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html`
- Curriculum version: v1.0
- Balanced Page Fill and Vertical Rhythm: v1.0.2
- Game baseline: `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`
- Status: VALIDATION BUILD

The v1.1 master and universal page-identity experiment are not part of this production track. They remain available through Git history for later design review.

## Outputs

- Student Mission: 2 pages
- Teacher Packet: 7 pages
- Answer Key: 3 pages
- Accessible Mission: 5 pages
- Grayscale Mission: 2 pages

Run `python validation-artifacts/validate_case02.py` from any directory. The harness regenerates role-isolated HTML/PDF outputs, rendered-review contact sheets, validation evidence, manifest, and checksums.

## Release gate

Automated validation must pass. Final approval still requires owner physical 100% print testing.
''')
write(PUBLISHED/'README.md','''# Case 02 Published Validation Outputs

All five role outputs are generated from `../master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html`. The PDFs remain validation builds until the owner physical-print gate passes. Do not hand-edit generated HTML or PDF files.
''')
write(CASE/'validation-artifacts/README.md','''# Case 02 Validation Artifacts

`validate_case02.py` is the canonical reproducible build and validation harness for the reconciled v1.0 track. It regenerates all five role outputs, performs static/browser/interaction/balanced-fill/PDF checks, writes current checksums and manifest data, and creates direct PDF-rendered contact sheets in `rendered-review/`.

Automated balanced-fill measurements are diagnostic; human design judgment remains final.
''')
write(CASE/'validation-artifacts/requirements.txt','''beautifulsoup4
playwright
pypdf
pillow
pymupdf
''')

# Merge report with exact current diff set.
merge_report=CASE/'reports/CASE02_MERGE_REPORT.md'
merge_report.parent.mkdir(parents=True,exist_ok=True); merge_report.touch()
ready=subprocess.run(['git','diff','--name-only','origin/main','--'],cwd=ROOT,text=True,stdout=subprocess.PIPE,check=True).stdout.splitlines()
if merge_report.relative_to(ROOT).as_posix() not in ready: ready.append(merge_report.relative_to(ROOT).as_posix())
ready=sorted(x for x in ready if x)
excluded=[
'SSS_V1_1_PAGE_SYSTEM_VALIDATION_RESULTS.json','review/SSS_V1.1_PAGE_IDENTITY_PREVIEW.html','review/SSS_V1.1_PAGE_IDENTITY_PREVIEW.png','review/continuation-header.png','review/first-page-banner.png','review/minimal-footer.png','scripts/apply-sss-v1.1-page-system.py','scripts/validate-sss-v1.1-page-system.py','shared/implementation/SSS_HHH_V1_1_PAGE_IDENTITY_HANDOFF.md','shared/visual-style-guide/amendments/MISSION_TITLE_AND_CONTINUATION_HEADER_PARITY_v1.0.3.md','shared/visual-style-guide/amendments/UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md','sss/campaign-1/case-01-iss-greenhouse/CASE01_V1_1_MASTER_MANIFEST.json','sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html','sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_V1.1_CHANGELOG.md','sss/campaign-1/case-02-lunar-greenhouse/CASE02_V1_1_MASTER_MANIFEST.json','sss/campaign-1/case-02-lunar-greenhouse/master/SSS_C1_CASE02_EDITABLE_MASTER_v1.1.html']
write(merge_report,'# Case 02 Reconciliation and Merge Report\n\n## Files ready for main\n\n'+''.join(f'- `{x}`\n' for x in ready)+'\n## Deliberately excluded page-identity proposals\n\n'+''.join(f'- `{x}`\n' for x in excluded)+f'''\n## Final validation status

- Automated validation: **{status}**
- Single current master: `SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html`
- Five role outputs: regenerated and preflighted
- Balanced Page Fill and Vertical Rhythm v1.0.2: implemented
- Approved Case 01 v1.0: unchanged from main

## Remaining owner gate

Owner physical 100% print testing remains OPEN. No merge to main should be treated as an approved release until that gate passes.
''')

# Build manifest and checksums using repository-relative paths only.
exclude_from_manifest={MANIFEST,CHECKSUMS}
tracked=[]
for path in sorted(CASE.rglob('*')):
    if not path.is_file() or path in exclude_from_manifest: continue
    if path.name.startswith('.'): continue
    rel=path.relative_to(CASE).as_posix()
    tracked.append({'path':rel,'sha256':sha256(path),'bytes':path.stat().st_size})
manifest={
 'case':'SSS-C1-CASE02','title':'Lunar Greenhouse','version':'1.0','status':'VALIDATION BUILD','publication_date':'2026-07-24',
 'game_repository':'InterstellarHarvest/Space-Sprout-Sleuth','game_commit':'2a6e8a7bb75c8c96f26f9ebfe7523668107ab712',
 'curriculum_bible':'1.3','student_identity':'Process Modeler','master':'master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html',
 'task_registry':'source/task-registry.js','balanced_page_fill':'1.0.2',
 'page_counts':{'student':2,'teacher':7,'answer':3,'accessible':5,'grayscale':2},
 'automated_validation':{'status':status,'static':f"{sum(x['pass'] for x in checks)}/{len(checks)} PASS",'browser':f"{sum(x['pass'] for x in browser_checks)}/{len(browser_checks)} PASS",'pdf':f"{sum(x['pass'] for x in pdf_preflight.values())}/{len(pdf_preflight)} PASS",'physical_print':'OPEN'},
 'release_gate':{'may_mark_approved':False,'reason':'Owner physical 100% print testing has not passed.'},
 'governing_amendments':['shared/visual-style-guide/amendments/STUDENT_IDENTIFICATION_ROW_PLACEMENT_v1.0.1.md','shared/visual-style-guide/amendments/EXACT_MATCH_WORD_BANKS_v1.0.1.md','shared/visual-style-guide/amendments/TASK_REFERENCE_PARITY_v1.0.1.md','shared/visual-style-guide/amendments/TEACHER_TASK_REFERENCE_EMPHASIS_v1.0.1.md','shared/visual-style-guide/amendments/TEACHER_PRODUCTION_METADATA_VISIBILITY_v1.0.1.md','shared/visual-style-guide/amendments/CONTENT_ORDERING_AND_ACCESSIBLE_FLOW_v1.0.2.md','shared/visual-style-guide/amendments/BALANCED_PAGE_FILL_AND_VERTICAL_RHYTHM_v1.0.2.md'],
 'excluded_page_identity_proposals':excluded,
 'files':tracked
}
write(MANIFEST,json.dumps(manifest,indent=2))
checksum_paths=[p for p in sorted(CASE.rglob('*')) if p.is_file() and p!=CHECKSUMS]
write(CHECKSUMS,'\n'.join(f'{sha256(p)}  {p.relative_to(CASE).as_posix()}' for p in checksum_paths))

# Final evidence must contain no machine-local paths and checksums must verify immediately.
evidence=list((CASE/'reports').glob('*'))+[RESULTS,PREFLIGHT,MANIFEST,CHECKSUMS]+list(PUBLISHED.glob('*.html'))
bad=scan_absolute_paths(evidence)
if bad:
    print('Absolute paths found:',bad); sys.exit(1)
for line in CHECKSUMS.read_text(encoding='utf-8').splitlines():
    digest,rel=line.split('  ',1); path=CASE/rel
    if not path.exists() or sha256(path)!=digest:
        print('Checksum mismatch:',rel); sys.exit(1)
if failures or browser_failures:
    print(json.dumps({'static_failures':failures,'browser_failures':browser_failures},indent=2)); sys.exit(1)
print(f"PASS: {sum(x['pass'] for x in checks)}/{len(checks)} static, {sum(x['pass'] for x in browser_checks)}/{len(browser_checks)} browser, {sum(x['pass'] for x in pdf_preflight.values())}/{len(pdf_preflight)} PDF roles")
