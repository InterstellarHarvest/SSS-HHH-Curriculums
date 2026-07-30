#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, os, re, shutil, socket, subprocess, threading, time
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from bs4 import BeautifulSoup
from pypdf import PdfReader
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
MASTER=ROOT/'master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html'
PUB=ROOT/'published'
VAL=ROOT/'validation-artifacts'
REPORTS=ROOT/'reports'
RESULTS=VAL/'CASE03_V1_VALIDATION_RESULTS.json'
CHECKSUMS=VAL/'CASE03_V1_CHECKSUMS.sha256'
GAME='2a6e8a7bb75c8c96f26f9ebfe7523668107ab712'
TASKS=[
('1','Define the measurement'),
('2','Read the spectral-transmission data'),
('3','Compare quantity and quality'),
('4','Connect the symptom pattern'),
('5','Select and reject diagnoses'),
('6','Model the mechanism'),
('7','Write the case conclusion'),
('8','Transfer the analysis'),
('9','Exit ticket'),
]
ROLES={
'student':('SSS_C1_CASE03_STUDENT_MISSION_v1.0.html','SSS_C1_CASE03_STUDENT_MISSION_v1.0.pdf',4,'Student Mission'),
'teacher':('SSS_C1_CASE03_TEACHER_GUIDE_v1.0.html','SSS_C1_CASE03_TEACHER_GUIDE_v1.0.pdf',8,'Teacher Guide'),
'answer':('SSS_C1_CASE03_ANSWER_KEY_v1.0.html','SSS_C1_CASE03_ANSWER_KEY_v1.0.pdf',4,'Answer Key'),
'accessible':('SSS_C1_CASE03_ACCESSIBLE_MISSION_v1.0.html','SSS_C1_CASE03_ACCESSIBLE_MISSION_v1.0.pdf',6,'Accessible Mission'),
'grayscale':('SSS_C1_CASE03_GRAYSCALE_MISSION_v1.0.html','SSS_C1_CASE03_GRAYSCALE_MISSION_v1.0.pdf',4,'Student Mission'),
}
checks=[]
def check(group,name,ok,detail=''):
    checks.append({'group':group,'name':name,'pass':bool(ok),'detail':str(detail)})

def sha(path:Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

# STATIC MASTER / SOURCE
html=MASTER.read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')
visible=' '.join(x.get_text(' ',strip=True) for x in soup.select('section.page'))
check('static','master exists',MASTER.exists())
for meta,val in [('sss-case','SSS-C1-CASE03'),('sss-status','validation-build'),('sss-game-baseline',GAME),('sss-page-identity','1.0.4'),('sss-balanced-page-fill','1.0.2'),('sss-visible-production-status','none')]:
    m=soup.find('meta',attrs={'name':meta})
    check('static',f'metadata {meta}',m is not None and m.get('content')==val,m.get('content') if m else 'missing')
check('static','canonical institution agency','Solar Agricultural Agency' in visible)
check('static','wrong institution expansions absent',all(x not in visible for x in ['Solar Agricultural Authority','Space Agricultural Authority','Space Agricultural Agency','Solar Agriculture Agency']))
check('static','student identification only first student and accessible pages',len(soup.select('.student-id'))==2,len(soup.select('.student-id')))
for role,(_,_,count,footer_role) in ROLES.items():
    target='student' if role=='grayscale' else role
    pages=soup.select(f'section.page[data-role="{target}"]') if role!='grayscale' else soup.select('section.page[data-role="student"]')
    check('static',f'{role} master page count',len(pages)==count,len(pages))
    if role!='grayscale':
        for i,p in enumerate(pages,1):
            footer=p.select_one('.footer')
            check('identity',f'{role} footer {i}',footer is not None and footer.get_text(' ',strip=True)==f'{footer_role} {i} of {count}',footer.get_text(' ',strip=True) if footer else 'missing')
            header_ok=bool(p.select_one('.first-header') if i==1 else p.select_one('.cont-header'))
            check('identity',f'{role} header {i}',header_ok)

# Task title parity: Student controls; Accessible and Answer repeat all exact titles.
for role in ['student','accessible','answer']:
    roletext=' '.join(x.get_text(' ',strip=True) for x in soup.select(f'section.page[data-role="{role}"]'))
    for n,title in TASKS:
        check('task parity',f'{role} task {n} exact title',roletext.count(title)==1,roletext.count(title))
# Teacher only references tasks 2,3,6 directly; those exact references must be present.
teachertext=' '.join(x.get_text(' ',strip=True) for x in soup.select('section.page[data-role="teacher"]'))
for n,title in [('2',TASKS[1][1]),('3',TASKS[2][1]),('6',TASKS[5][1])]:
    check('task parity',f'teacher direct reference task {n}',title in teachertext)

# Data visualization assertions
for value in ['280','68%','47 sols','92%','88%','31%','12%','400-500 nm','500-600 nm','600-700 nm','700 nm+','FS-7 FULL SPECTRUM','BP-4 BLUE PASS']:
    check('data',f'exact value/text {value}',value in visible)
for label in ['Transmission (%)','Wavelength band','Game-provided sensor data']:
    check('graph',f'graph label {label}',label in html)
for pid in ['diag','dots','cross','horiz']:
    check('graph',f'grayscale pattern {pid}',f'id="{pid}"' in html)
check('graph','direct bar labels',all(f'>{v}%<' in html for v in [92,88,31,12]))
check('graph','SVG titles and descriptions',len(soup.select('svg[role="img"] title'))>=3 and len(soup.select('svg[role="img"] desc'))>=3)
check('graph','axes and units not color-only','Transmission (%)' in html and 'Wavelength band' in html and all(x in html for x in ['url(#diag)','url(#dots)','url(#cross)','url(#horiz)']))
check('graph','no continuous-spectrum precision claim','No continuous spectrum or intermediate values are inferred' in visible or 'does not imply a continuous measured spectrum' in visible)

correct='The light delivery system is filtering out red wavelengths needed for chlorophyll biosynthesis.'
check('content','exact correct diagnosis',correct in visible)
for phrase in ['wrong BP-4','red/deep-red rejection','new chlorophyll','new growth bleaches']:
    check('content',f'mechanism element {phrase}',phrase.lower() in visible.lower())
check('content','reject low-total-light explanation','not enough total light' in visible.lower() or 'low total light' in visible.lower())
check('content','brightness misconception warning','more brightness always fixes' in visible.lower() or 'increasing brightness alone' in visible.lower())
check('content','red-only misconception warning','plants only need red' in visible.lower() or 'plants do not use only red' in visible.lower())
check('content','green-is-useless misconception warning','green light is useless' in visible.lower())
check('content','dust-only rejected','dust' in visible.lower() and 'does not explain' in visible.lower())
# Stale dataset prohibited in printable/master.
for stale in ['8%, 12%, 45%', '55%, 35%', 'borosilicate', 'Loss through pipe (%)', 'stated 12 m light-pipe losses']:
    check('regression',f'stale content absent: {stale}',stale not in html)
# Printable production metadata absent from page text.
machine_prefix='/'+'mnt'+'/'+'data'+'/'
for forbidden in ['VALIDATION BUILD',GAME,'SSS_C1_CASE03_EDITABLE_MASTER','CASE03_V1_CHECKSUMS',machine_prefix,'github.com/']:
    check('identity','printable metadata absent: '+('machine-local path' if forbidden==machine_prefix else forbidden[:28]),forbidden not in visible)
# Accessibility and interaction structure.
check('accessibility','skip link',bool(soup.select_one('a[href="#workspace"]')))
check('accessibility','all figures labeled',all(svg.find('title') or svg.get('aria-label') for svg in soup.select('figure svg')))
check('accessibility','response textboxes labeled',all(n.get('role')=='textbox' and n.get('aria-multiline')=='true' for n in soup.select('.response[contenteditable="true"]')))
check('accessibility','accessible role larger type','.accessible{font-size:13pt' in html and len(soup.select('section.page.accessible[data-role="accessible"]'))==6)
check('publishing','local persistence code',"localStorage.setItem(KEY" in html and "localStorage.getItem(KEY" in html)
check('publishing','selective response clearing',"querySelectorAll('.response[contenteditable=\"true\"]')" in html)
check('publishing','reset behavior',"localStorage.removeItem(KEY)" in html)
check('publishing','portable downloaded HTML',"function portable(role,gray=false)" in html and "new Blob([text]" in html)
check('publishing','overflow warning logic','has-overflow' in html and 'scrollHeight>c.clientHeight+2' in html)
check('publishing','standalone control guards',all(x in html for x in ['if(roleSelect)','if(grayToggle)','if(clearBtn)','if(resetBtn)','if(downloadBtn)']))

# Standalone static checks.
for role,(htmlname,pdfname,count,footer_role) in ROLES.items():
    p=PUB/htmlname
    txt=p.read_text(encoding='utf-8')
    ss=BeautifulSoup(txt,'html.parser')
    check('portable',f'{role} standalone exists',p.exists())
    check('portable',f'{role} standalone page count',len(ss.select('section.page'))==count,len(ss.select('section.page')))
    check('portable',f'{role} toolbar absent',not ss.select('.toolbar'))
    check('portable',f'{role} self-contained','http://' not in txt and 'https://' not in txt and '<style>' in txt and '<script' in txt)
    check('portable',f'{role} source master metadata',bool(ss.find('meta',attrs={'name':'sss-source-master','content':'SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html'})))

# Browser checks using set_content. Network navigation is blocked in this execution environment.
with sync_playwright() as pw:
    browser_executable = next(
        path for path in [
            os.environ.get('CHROMIUM_EXECUTABLE'),
            '/usr/bin/chromium',
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        ]
        if path and Path(path).exists()
    )
    browser=pw.chromium.launch(headless=True,executable_path=browser_executable,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1200})
    # about:blank has an opaque-origin Storage getter; install an in-memory Storage-compatible object.
    page.evaluate("Object.defineProperty(window,'localStorage',{configurable:true,value:{_d:{},getItem(k){return Object.prototype.hasOwnProperty.call(this._d,k)?this._d[k]:null},setItem(k,v){this._d[k]=String(v)},removeItem(k){delete this._d[k]},clear(){this._d={}}}})")
    errors=[]
    page.on('pageerror',lambda e: errors.append(str(e)))
    page.set_content(html,wait_until='load')
    page.wait_for_timeout(250)
    check('browser','master loads without JS errors',not errors,' | '.join(errors))
    check('browser','initial student pages visible',page.locator('section.page[data-role="student"]:visible').count()==4,page.locator('section.page:visible').count())
    first=page.locator('section.page[data-role="student"] .response[contenteditable="true"]').first
    first.fill('persistence test')
    page.wait_for_timeout(500)
    first.fill('')
    page.evaluate('load()')
    check('browser','response persistence',page.locator('section.page[data-role="student"] .response[contenteditable="true"]').first.inner_text()=='persistence test')
    for role in ['teacher','answer','accessible','student']:
        page.select_option('#roleSelect',role)
        page.wait_for_timeout(150)
        count=ROLES[role][2]
        check('browser',f'{role} role isolation',page.locator(f'section.page[data-role="{role}"]:visible').count()==count and page.locator('section.page:visible').count()==count,page.locator('section.page:visible').count())
        check('browser',f'{role} zero overflow',page.locator(f'section.page[data-role="{role}"].has-overflow').count()==0,page.locator(f'section.page[data-role="{role}"].has-overflow').count())
    page.select_option('#roleSelect','student')
    idf=page.locator('.student-id .id-field').first
    idf.fill('Nate Test')
    resp=page.locator('section.page[data-role="student"] .response[contenteditable="true"]').first
    resp.fill('clear me')
    page.click('#clearBtn'); page.wait_for_timeout(100)
    check('browser','selective clear clears responses',resp.inner_text()=='')
    check('browser','selective clear preserves ID',idf.inner_text()=='Nate Test')
    page.check('#grayToggle')
    check('browser','grayscale class toggles',page.locator('body.grayscale').count()==1)
    portable=page.evaluate("portable('accessible',false)")
    portable_soup=BeautifulSoup(portable,'html.parser')
    portable_count=len(portable_soup.select('section.page[data-role="accessible"]'))
    check('browser','portable accessible page count',portable_count==6,portable_count)
    check('browser','portable output excludes toolbar','class="toolbar"' not in portable)
    page.locator('body').press('Tab'); page.locator('body').press('Tab')
    focused=page.evaluate("document.activeElement && document.activeElement.matches('button,select,[contenteditable=true],a,input')")
    check('browser','keyboard focus reaches interactive element',bool(focused),focused)
    page.on('dialog',lambda d:d.accept())
    page.click('#resetBtn'); page.wait_for_timeout(150)
    check('browser','reset clears saved fields',page.locator('[contenteditable="true"]').evaluate_all("els=>els.every(e=>e.innerHTML==='')"))
    for role,(htmlname,_,count,_) in ROLES.items():
        errs=[]
        sp=browser.new_page(viewport={'width':1440,'height':1200})
        sp.evaluate("Object.defineProperty(window,'localStorage',{configurable:true,value:{_d:{},getItem(k){return Object.prototype.hasOwnProperty.call(this._d,k)?this._d[k]:null},setItem(k,v){this._d[k]=String(v)},removeItem(k){delete this._d[k]},clear(){this._d={}}}})")
        sp.on('pageerror',lambda e,errs=errs:errs.append(str(e)))
        stxt=(PUB/htmlname).read_text(encoding='utf-8')
        sp.set_content(stxt,wait_until='load'); sp.wait_for_timeout(200)
        check('browser',f'{role} standalone no JS errors',not errs,' | '.join(errs))
        check('browser',f'{role} standalone visible pages',sp.locator('section.page:visible').count()==count,sp.locator('section.page:visible').count())
        check('browser',f'{role} standalone zero overflow',sp.locator('section.page.has-overflow').count()==0,sp.locator('section.page.has-overflow').count())
        sp.close()
    browser.close()

# PDF checks and rendering.
render_root=VAL/'rendered-review'
if render_root.exists(): shutil.rmtree(render_root)
render_root.mkdir(parents=True)
pdf_summary={}
for role,(_,pdfname,count,footer_role) in ROLES.items():
    p=PUB/pdfname
    check('pdf',f'{role} PDF exists',p.exists())
    reader=PdfReader(str(p))
    check('pdf',f'{role} PDF page count',len(reader.pages)==count,len(reader.pages))
    alltext='\n'.join((pg.extract_text() or '') for pg in reader.pages)
    for i,pg in enumerate(reader.pages,1):
        box=pg.mediabox
        check('pdf',f'{role} page {i} letter size',abs(float(box.width)-612)<1 and abs(float(box.height)-792)<1,f'{float(box.width)}x{float(box.height)}')
        txt=pg.extract_text() or ''
        check('pdf',f'{role} footer {i}',f'{footer_role} {i} of {count}' in txt)
    for forbidden in ['VALIDATION BUILD',GAME,machine_prefix,'SSS_C1_CASE03_EDITABLE_MASTER']:
        check('pdf',f'{role} no visible metadata '+('machine-local path' if forbidden==machine_prefix else forbidden[:18]),forbidden not in alltext)
    if role in ['student','answer','accessible','grayscale']:
        for v in ['280','92%','88%','31%','12%']:
            check('pdf',f'{role} contains {v}',v in alltext)
    for stale in ['45%','65%','55%','35%','greatest loss','Loss through pipe']:
        check('pdf',f'{role} stale PDF content absent {stale}',stale not in alltext)
    if role=='teacher':
        for v in ['68%','47 sols','FS-7','BP-4','92%, 88%, 31%, 12%']:
            check('pdf',f'teacher current runtime evidence {v}',v in alltext)
    check('pdf',f'{role} ASCII-safe bytes',all(b<128 for b in p.read_bytes()))
    out=render_root/role; out.mkdir()
    subprocess.run(['pdftoppm','-png','-r','140',str(p),str(out/'page')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    imgs=sorted(out.glob('page-*.png'))
    check('render',f'{role} rendered page count',len(imgs)==count,len(imgs))
    check('render',f'{role} nonempty rendered pages',all(x.stat().st_size>15000 for x in imgs),[x.stat().st_size for x in imgs])
    pdf_summary[role]={'pdf':pdfname,'pages':count,'sha256':sha(p),'bytes':p.stat().st_size}

# Checksums for all repository-intended files, excluding transient renders and checksum itself.
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(ROOT)
    if rel.parts[:2]==('validation-artifacts','rendered-review'): continue
    if rel.parts[:2]==('validation-artifacts','renderer-parity'): continue
    if '__pycache__' in rel.parts: continue
    if rel.name in {'.DS_Store','CASE03_GITHUB_HANDOFF.md'}: continue
    if rel.name=='CASE03_V1_CHECKSUMS.sha256': continue
    files.append(p)
CHECKSUMS.write_text('\n'.join(f'{sha(p)}  {p.relative_to(ROOT).as_posix()}' for p in files)+'\n',encoding='ascii')
check('checksum','checksum ledger created',CHECKSUMS.exists() and len(CHECKSUMS.read_text().splitlines())==len(files),len(files))

status=all(c['pass'] for c in checks)
counts={}
for c in checks:
    g=c['group']; counts.setdefault(g,{'pass':0,'total':0}); counts[g]['total']+=1; counts[g]['pass']+=int(c['pass'])
result={'case':'SSS-C1-CASE03','version':'1.0','status':'PASS' if status else 'FAIL','build_status':'VALIDATION BUILD','game_commit':GAME,'page_counts':{r:v[2] for r,v in ROLES.items()},'groups':counts,'total':{'pass':sum(c['pass'] for c in checks),'total':len(checks)},'pdfs':pdf_summary,'failures':[c for c in checks if not c['pass']],'checks':checks}
RESULTS.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':result['status'],'total':result['total'],'groups':counts,'failures':result['failures'][:10]},indent=2))
raise SystemExit(0 if status else 1)
