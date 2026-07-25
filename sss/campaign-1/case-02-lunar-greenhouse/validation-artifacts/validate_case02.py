#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json, os, re, sys, traceback
CASE=Path(__file__).resolve().parents[1];REPO=CASE.parents[2]
MASTER=CASE/'master/SSS_C1_CASE02_EDITABLE_MASTER_v1.1.html'
RESULTS=Path(__file__).with_name('CASE02_VALIDATION_RESULTS.json')
TASKS={1:'Vocabulary',2:'Initial thinking',3:'Model the pollination sequence',4:'Identify the failed step',5:'Test the competing explanations',6:'Diagnose and reject an alternative',7:'Claim-Evidence-Reasoning',8:'Design a reliable pollination support',9:'Exit ticket'}
ROLE_COUNTS={'student':2,'teacher':7,'answer':3,'accessible':5}
ROLE_LABELS={'student':'Student Mission','teacher':'Teacher Guide','answer':'Answer Key','accessible':'Accessible Mission'}
checks=[];fail=[];browser=[];bfail=[];js=[]
def ck(n,c,d=''):
 r={'name':n,'pass':bool(c),'detail':d};checks.append(r)
 if not c:fail.append(r)
text=MASTER.read_text(encoding='utf-8');soup=BeautifulSoup(text,'html.parser')
ck('master v1.1',soup.find('meta',attrs={'name':'sss-master-version','content':'1.1'}) is not None)
ck('historical v1.0 preserved',(CASE/'master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html').exists())
ck('review status metadata',soup.find('meta',attrs={'name':'sss-status','content':'review'}) is not None)
printable=' '.join(p.get_text(' ',strip=True) for p in soup.select('.page')).upper()
ck('no printable status words','VALIDATION BUILD' not in printable and 'APPROVED' not in printable)
ck('location-only subtitle',all(x.select_one('.mission-subtitle').get_text(' ',strip=True)=='Campaign 1 · Case 02 · Shackleton Crater, Lunar South Pole' for x in soup.select('.mission-title-block')))
ck('three-line first-page institution',all([y.get_text(strip=True) for y in x.select('.institution > span')]==['Solar','Agricultural','Agency'] for x in soup.select('.mission-title-block')))
ck('three-line continuation institution',all([y.get_text(strip=True) for y in x.select('.institution > span')]==['Solar','Agricultural','Agency'] for x in soup.select('.continuation-header')))
ck('compact header CSS',all(x in text for x in ['min-height:.78in','font-size:26pt','font-size:9pt;line-height:11.5pt','margin-bottom:.055in']))
ck('process model central','Model the pollination sequence' in text and 'process-chain' in text)
ck('no Case 01 evidence matrix','Investigate four evidence sources' not in text)
ck('no unsupported frequency/airflow values',not re.search(r'60\s*[–-]\s*90\s*Hz|0\.5\s*[–-]\s*1\.0\s*m/s',text,re.I))
for role,count in ROLE_COUNTS.items():
 pages=soup.select(f'.page[data-role="{role}"]'); ck(f'{role} count',len(pages)==count,str(len(pages)))
 for i,p in enumerate(pages,1):
  f=p.select_one('.publication-footer');ck(f'{role} footer {i}',f and f.get_text(' ',strip=True)==f'{ROLE_LABELS[role]} {i} of {count}',f.get_text(' ',strip=True) if f else '')
  if i>1:
   h=p.select_one('.continuation-header');ck(f'{role} generic continuation {i}',h and h.select_one('h1').get_text(' ',strip=True)=='Lunar Greenhouse' and h.select_one('.continuation-role').get_text(' ',strip=True)==f'{ROLE_LABELS[role]} · Continued')
student={int(h['data-task-id']):h.get_text(' ',strip=True).split('·',1)[-1].strip() for h in soup.select('.page[data-role="student"] .task-heading')}
accessible={int(h['data-task-id']):h.get_text(' ',strip=True).split('·',1)[-1].strip() for h in soup.select('.page[data-role="accessible"] .task-heading')}
answer={int(h['data-task-id']):h.get_text(' ',strip=True).split('·',1)[-1].strip() for h in soup.select('.page[data-role="answer"] .task-heading')}
ck('student task parity',student==TASKS,str(student));ck('accessible task parity',accessible==TASKS,str(accessible));ck('answer task parity',answer=={i:TASKS[i] for i in range(3,10)},str(answer))
sv=[x.get_text(' ',strip=True) for x in soup.select('.page[data-role="student"] .vocab-term')]
av=[x.get_text(' ',strip=True) for x in soup.select('.page[data-role="accessible"] .vocab-term')]
ck('student vocabulary alphabetical',sv==sorted(sv,key=str.casefold),str(sv));ck('accessible vocabulary alphabetical',av==sorted(av,key=str.casefold),str(av))
wb=soup.select_one('.page[data-role="student"] .word-bank-terms')
if wb:
 terms=[x.strip() for x in wb.get_text(' ',strip=True).split('·')]; sequence=['viable pollen in anthers','physical agitation','pollen reaches stigma','pollen tube growth','fertilization','fruit set']
 ck('sequence bank shuffled',terms!=sequence,str(terms))
ck('accessible continuous packing',[[int(h['data-task-id']) for h in p.select('.task-heading')] for p in soup.select('.page[data-role="accessible"]')]==[[1,2],[3,4],[5],[6,7],[8,9]])
ck('v1.0.4 amendment',(REPO/'shared/visual-style-guide/amendments/UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md').exists())
POLY="""<script>(()=>{const s={};Object.defineProperty(window,'localStorage',{value:{getItem:k=>Object.prototype.hasOwnProperty.call(s,k)?s[k]:null,setItem:(k,v)=>{s[k]=String(v)},removeItem:k=>{delete s[k]},clear:()=>{for(const k in s)delete s[k]},key:i=>Object.keys(s)[i]||null,get length(){return Object.keys(s).length}},configurable:true});})();</script>"""
try:
 with sync_playwright() as pw:
  b=pw.chromium.launch(headless=True,executable_path=os.environ.get('CHROMIUM_PATH','/usr/bin/chromium'),args=['--no-sandbox'])
  page=b.new_page(viewport={'width':1500,'height':1100});page.on('pageerror',lambda e:js.append(str(e)))
  page.set_content(text.replace('</head>',POLY+'</head>',1),wait_until='load');page.wait_for_timeout(400)
  def bc(n,c,d=''):
   r={'name':n,'pass':bool(c),'detail':d};browser.append(r)
   if not c:bfail.append(r)
  bc('JS initialized',page.evaluate('!!window.__case02'))
  page.evaluate("window.__case02.setRole('student')");page.wait_for_timeout(80)
  geom=page.evaluate("""() => { const id=document.querySelector('.page[data-role=student] .student-id'); const h=document.querySelector('.page[data-role=student] .mission-title-block'); const sub=h.querySelector('.mission-subtitle'); const hero=h.querySelector('.hero-title'); const ci=document.querySelector('.page[data-role=student] .continuation-identity'); const ins=ci?.querySelector('.saa-insignia'); const inst=ci?.querySelector('.institution'); const hs=getComputedStyle(h); return {headerHeight:h.getBoundingClientRect().height,idGap:h.getBoundingClientRect().top-id.getBoundingClientRect().bottom,afterGap:parseFloat(hs.marginBottom),subtitle:getComputedStyle(sub).fontSize,hero:getComputedStyle(hero).fontSize,continuationGap:ins&&inst?inst.getBoundingClientRect().left-ins.getBoundingClientRect().right:0,institutionAlign:inst?getComputedStyle(inst).textAlign:''}; }""")
  bc('compact first-page header',geom['headerHeight']<=82,str(geom))
  bc('tight identification-to-banner spacing',geom['idGap']<=5,str(geom))
  bc('tight banner-to-content spacing',geom['afterGap']<=6,str(geom))
  bc('first-page title is 26pt',abs(float(geom['hero'].replace('px',''))-34.6667)<0.2,str(geom))
  bc('subtitle is 9pt',abs(float(geom['subtitle'].replace('px',''))-12)<0.2,str(geom))
  bc('continuation lockup padding',geom['continuationGap']>=7,str(geom))
  bc('continuation institution left aligned',geom['institutionAlign']=='left',str(geom))
  for role,count in ROLE_COUNTS.items():
   page.evaluate('(r)=>window.__case02.setRole(r)',role);page.wait_for_timeout(80)
   bc(f'{role} visible pages',page.locator('.page:visible').count()==count)
   bc(f'{role} zero overflow',page.evaluate('window.__case02.checkOverflow()')==0)
  page.evaluate("window.__case02.setRole('student')")
  page.locator('[data-field="student-task2"]').evaluate("el=>{el.innerHTML='PERSIST';el.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:'x'}));}")
  serial=page.evaluate('window.__case02.serializePortableHTML()');bc('portable HTML persists response','PERSIST' in serial and 'universal-v1.1' in serial)
  page.evaluate('window.__case02.resetSource(true)');bc('reset clears response',page.locator('[data-field="student-task2"]').inner_text()=='')
  bc('no JavaScript errors',not js,str(js));b.close()
except Exception:
 bfail.append({'name':'browser exception','pass':False,'detail':traceback.format_exc()})
result={'case':'SSS-C1-CASE02','master_version':'1.1','pass':not fail and not bfail,'static_checks':checks,'static_failures':fail,'browser_checks':browser,'browser_failures':bfail,'pdfs_retained':False}
RESULTS.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'{sum(x["pass"] for x in checks)}/{len(checks)} static; {sum(x["pass"] for x in browser)}/{len(browser)} browser checks passed')
if fail or bfail: sys.exit(1)
