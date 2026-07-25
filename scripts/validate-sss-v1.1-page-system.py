#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
ROLES={'student':'Student Mission','teacher':'Teacher Guide','answer':'Answer Key','accessible':'Accessible Mission'}
CASES=[
 ('case01',ROOT/'sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html','ISS Greenhouse Module','Campaign 1 · Case 01 · Low Earth Orbit'),
 ('case02',ROOT/'sss/campaign-1/case-02-lunar-greenhouse/master/SSS_C1_CASE02_EDITABLE_MASTER_v1.1.html','Lunar Greenhouse','Campaign 1 · Case 02 · Shackleton Crater, Lunar South Pole')]
fail=[]; checks=[]
def ck(name,condition,detail=''):
 checks.append({'name':name,'pass':bool(condition),'detail':detail})
 if not condition: fail.append(checks[-1])
for key,path,title,subtitle in CASES:
 ck(f'{key} v1.1 exists',path.exists(),str(path))
 if not path.exists(): continue
 text=path.read_text(encoding='utf-8'); soup=BeautifulSoup(text,'html.parser')
 ck(f'{key} v1.1 metadata',soup.find('meta',attrs={'name':'sss-master-version','content':'1.1'}) is not None)
 ck(f'{key} no visible production status',not soup.select('.page .publication-mark,.page .status-mark,.page .footer-status'))
 ck(f'{key} status words absent from printable pages',all(x not in ' '.join(p.get_text(' ',strip=True) for p in soup.select('.page')).upper() for x in ['VALIDATION BUILD','APPROVED']))
 for role,label in ROLES.items():
  pages=soup.select(f'.page[data-role="{role}"]'); total=len(pages)
  ck(f'{key} {role} pages present',total>0,str(total))
  if not pages: continue
  first=pages[0].select_one('.mission-title-block[data-header-contract="universal-v1.1"]')
  ck(f'{key} {role} first banner',first is not None)
  if first:
   ck(f'{key} {role} first title',first.select_one('.hero-title') and first.select_one('.hero-title').get_text(' ',strip=True)==title)
   ck(f'{key} {role} subtitle',first.select_one('.mission-subtitle') and first.select_one('.mission-subtitle').get_text(' ',strip=True)==subtitle)
   ck(f'{key} {role} identity right structure',bool(first.select_one('.identity-mark .institution') and first.select_one('.identity-mark .document-role')))
   ck(f'{key} {role} institution three-line lockup',[x.get_text(strip=True) for x in first.select('.identity-mark .institution > span')]==['Solar','Agricultural','Agency'])
   ck(f'{key} {role} role label',first.select_one('.document-role').get_text(' ',strip=True)==label)
  for idx,p in enumerate(pages,1):
   footer=p.select_one('.publication-footer[data-footer-contract="universal-v1.1"]')
   ck(f'{key} {role} footer {idx}',footer is not None and footer.get_text(' ',strip=True)==f'{label} {idx} of {total}',footer.get_text(' ',strip=True) if footer else 'missing')
   if idx>1:
    h=p.select_one('.continuation-header[data-header-contract="universal-v1.1"]')
    ck(f'{key} {role} continuation {idx}',h is not None)
    if h:
     ck(f'{key} {role} generic continuation title {idx}',h.select_one('.continuation-copy h1').get_text(' ',strip=True)==title)
     ck(f'{key} {role} generic continuation role {idx}',h.select_one('.continuation-role').get_text(' ',strip=True)==f'{label} · Continued')
     ck(f'{key} {role} institution on right {idx}',bool(h.select_one('.continuation-identity .institution')))
     ck(f'{key} {role} continuation three-line lockup {idx}',[x.get_text(strip=True) for x in h.select('.continuation-identity .institution > span')]==['Solar','Agricultural','Agency'])
 ck(f'{key} no legacy Page footer',not any(re.fullmatch(r'Page\s+\d+\s+of\s+\d+',f.get_text(' ',strip=True)) for f in soup.select('.publication-footer')))
 ck(f'{key} no top banner accent rule in v1.1 CSS','border-top:0' in text and 'data-header-contract="universal-v1.1"' in text)
 ck(f'{key} compact banner geometry',all(x in text for x in ['min-height:.78in','font-size:26pt','font-size:9pt;line-height:11.5pt','margin-bottom:.055in']))
amend=ROOT/'shared/visual-style-guide/amendments/UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md'
ck('v1.0.4 amendment exists',amend.exists(),str(amend))
if amend.exists():
 at=amend.read_text(encoding='utf-8')
 ck('amendment complete',all(x in at for x in ['location','generic header','Minimal printable footer','Production metadata separation','creates a v1.1 master']))
bible=ROOT/'shared/curriculum-bible/SSS_HHH_CURRICULUM_BIBLE_v1.3.md'
ck('Bible references v1.0.4',bible.exists() and 'UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md' in bible.read_text(encoding='utf-8'))
result={'pass':not fail,'checks':checks,'failures':fail}
out=ROOT/'SSS_V1_1_PAGE_SYSTEM_VALIDATION_RESULTS.json';out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'{sum(c["pass"] for c in checks)}/{len(checks)} checks passed')
if fail:
 for f in fail: print('FAIL:',f['name'],f['detail'])
 sys.exit(1)
