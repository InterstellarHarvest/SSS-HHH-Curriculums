#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from bs4 import BeautifulSoup
import copy, hashlib, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
ROLE_LABELS = {"student":"Student Mission","teacher":"Teacher Guide","answer":"Answer Key","accessible":"Accessible Mission"}
CONFIG = {"title":"ISS Greenhouse Module","subtitle":"Campaign 1 · Case 01 · Low Earth Orbit"}
CSS = '\n/* Universal printable page identity contract — v1.1 / amendment v1.0.4 */\n.mission-title-block[data-header-contract="universal-v1.1"]{\n  display:grid;grid-template-columns:.08in minmax(0,1fr) 1.78in;gap:.14in;align-items:center;\n  border-top:0;border-bottom:1px solid var(--line);padding:0 0 .12in;margin-bottom:.11in;\n}\n.mission-title-block[data-header-contract="universal-v1.1"] .mission-rail{height:100%;min-height:1.12in;background:var(--institution,var(--cyan));}\n.mission-title-block[data-header-contract="universal-v1.1"] .mission-title-copy{min-width:0;padding:0;border:0;}\n.mission-title-block[data-header-contract="universal-v1.1"] .hero-title{margin:.02in 0 .035in;font-size:var(--hero);line-height:var(--hero-lh);letter-spacing:-.025em;color:var(--ink);}\n.mission-title-block[data-header-contract="universal-v1.1"] .mission-subtitle{margin:0;color:var(--ink);font-size:var(--deck);line-height:var(--deck-lh);}\n.mission-title-block[data-header-contract="universal-v1.1"] .identity-mark{display:flex;align-items:center;justify-self:end;gap:.09in;min-width:0;}\n.mission-title-block[data-header-contract="universal-v1.1"] .identity-mark .saa-insignia{width:.64in;height:.64in;flex:0 0 .64in;object-fit:contain;justify-self:auto;}\n.mission-title-block[data-header-contract="universal-v1.1"] .identity-copy{min-width:0;}\n.mission-title-block[data-header-contract="universal-v1.1"] .identity-copy .institution{font:700 var(--small)/1.25 "JetBrains Mono",monospace;letter-spacing:.04em;text-transform:uppercase;color:var(--ink);}\n.mission-title-block[data-header-contract="universal-v1.1"] .identity-copy .document-role{margin-top:.025in;font-size:var(--small);line-height:var(--small-lh);color:var(--muted);}\n.continuation-header[data-header-contract="universal-v1.1"]{\n  display:grid;grid-template-columns:minmax(0,1fr) 1.78in;gap:.14in;align-items:center;\n  border-top:0;border-bottom:1px solid var(--line);padding:0 0 .075in;margin-bottom:.09in;\n}\n.continuation-header[data-header-contract="universal-v1.1"] .continuation-copy{text-align:left;min-width:0;}\n.continuation-header[data-header-contract="universal-v1.1"] .continuation-copy h1{margin:0;font-size:var(--title);line-height:var(--title-lh);letter-spacing:-.012em;color:var(--ink);}\n.continuation-header[data-header-contract="universal-v1.1"] .continuation-role{margin-top:.01in;font-size:var(--deck);line-height:var(--deck-lh);color:var(--muted);}\n.continuation-header[data-header-contract="universal-v1.1"] .continuation-identity{display:flex;align-items:center;justify-self:end;gap:.075in;min-width:0;}\n.continuation-header[data-header-contract="universal-v1.1"] .continuation-identity .saa-insignia{width:.36in;height:.36in;flex:0 0 .36in;object-fit:contain;}\n.continuation-header[data-header-contract="universal-v1.1"] .continuation-identity .institution{font:700 var(--micro)/1.25 "JetBrains Mono",monospace;letter-spacing:.045em;text-transform:uppercase;color:var(--ink);}\n.publication-footer[data-footer-contract="universal-v1.1"]{display:flex;justify-content:flex-end;align-items:flex-end;border-top:1px solid var(--line);padding-top:.045in;margin-top:.08in;text-align:right;color:var(--muted);font:600 var(--micro)/var(--micro-lh) "JetBrains Mono",monospace;}\n.publication-footer[data-footer-contract="universal-v1.1"] span{margin-left:auto;text-align:right;}\n.publication-mark,.status-mark{display:none!important;}\n@media (max-width:900px){\n  .mission-title-block[data-header-contract="universal-v1.1"]{grid-template-columns:.08in minmax(0,1fr) 1.55in;}\n  .continuation-header[data-header-contract="universal-v1.1"]{grid-template-columns:minmax(0,1fr) 1.55in;}\n}\n'
COMPACT_HEADER_CSS = r'''
/* Compact universal header geometry correction */
.student-id{margin-bottom:.03in;}
.mission-title-block[data-header-contract="universal-v1.1"]{
  grid-template-columns:.08in minmax(0,1fr) 1.70in;gap:.12in;
  padding:0 0 .055in;margin-bottom:.055in;
}
.mission-title-block[data-header-contract="universal-v1.1"] .mission-rail{min-height:.78in;}
.mission-title-block[data-header-contract="universal-v1.1"] .hero-title{margin:0 0 .01in;font-size:26pt;line-height:29pt;}
.mission-title-block[data-header-contract="universal-v1.1"] .mission-subtitle{font-size:9pt;line-height:11.5pt;}
.mission-title-block[data-header-contract="universal-v1.1"] .identity-mark{gap:.09in;}
.mission-title-block[data-header-contract="universal-v1.1"] .identity-mark .saa-insignia{width:.58in;height:.58in;flex-basis:.58in;}
.mission-title-block[data-header-contract="universal-v1.1"] .identity-copy{text-align:left;}
.mission-title-block[data-header-contract="universal-v1.1"] .identity-copy .institution{font:700 8.2pt/1.12 "JetBrains Mono",monospace;text-align:left;}
.mission-title-block[data-header-contract="universal-v1.1"] .identity-copy .institution span{display:block;}
.mission-title-block[data-header-contract="universal-v1.1"] .identity-copy .document-role{font-size:8.5pt;line-height:11pt;}
.continuation-header[data-header-contract="universal-v1.1"]{
  grid-template-columns:minmax(0,1fr) 1.58in;gap:.14in;
  padding:0 0 .055in;margin-bottom:.07in;
}
.continuation-header[data-header-contract="universal-v1.1"] .continuation-role{font-size:9pt;line-height:11.5pt;}
.continuation-header[data-header-contract="universal-v1.1"] .continuation-identity{gap:.09in;}
.continuation-header[data-header-contract="universal-v1.1"] .continuation-identity .saa-insignia{width:.34in;height:.34in;flex-basis:.34in;}
.continuation-header[data-header-contract="universal-v1.1"] .continuation-identity .institution{font:700 7pt/1.12 "JetBrains Mono",monospace;text-align:left;}
.continuation-header[data-header-contract="universal-v1.1"] .continuation-identity .institution span{display:block;}
'''
CSS += COMPACT_HEADER_CSS


def set_meta(soup, name, content):
    tag = soup.find('meta', attrs={'name': name})
    if tag is None:
        tag = soup.new_tag('meta')
        tag['name'] = name
        soup.head.append(tag)
    tag['content'] = content

def clone_insignia(old_header, soup):
    ins = old_header.select_one('.saa-insignia')
    if ins is None:
        ins = soup.new_tag('img')
        ins['class'] = ['saa-insignia']
        ins['src'] = '../../../../shared/assets/insignia/saa.svg'
    else:
        ins = copy.deepcopy(ins)
    if ins.name == 'img':
        ins['alt'] = 'Solar Agricultural Agency insignia'
        ins.attrs.pop('aria-hidden', None)
    else:
        ins['aria-label'] = 'Solar Agricultural Agency insignia'
        ins['role'] = 'img'
    ins['class'] = list(dict.fromkeys(ins.get('class', []) + ['saa-insignia']))
    return ins

def build_institution(soup):
    inst = soup.new_tag('div')
    inst['class'] = ['institution']
    inst['aria-label'] = 'Solar Agricultural Agency'
    for word in ('Solar', 'Agricultural', 'Agency'):
        span = soup.new_tag('span')
        span.string = word
        inst.append(span)
    return inst

def transform_master(source, target):
    soup = BeautifulSoup(source.read_text(encoding='utf-8'), 'html.parser')
    set_meta(soup, 'sss-master-version', '1.1')
    set_meta(soup, 'sss-visible-production-status', 'none')
    set_meta(soup, 'sss-source-master', source.name)
    set_meta(soup, 'sss-status', 'review')
    if soup.title:
        soup.title.string = re.sub(r'v1\.0', 'v1.1', soup.title.get_text())
    for node in soup.find_all(string=re.compile(r'(SPACE|SOLAR) AGRICULTURAL AUTHORITY', re.I)):
        node.replace_with(re.sub(r'(SPACE|SOLAR) AGRICULTURAL AUTHORITY', 'SOLAR AGRICULTURAL AGENCY', str(node), flags=re.I))
    for el in soup.select('.publication-mark,.status-mark'):
        el.decompose()
    for opt in soup.select('option'):
        if opt.string:
            opt.string = opt.string.replace(' · approved',' · default').replace(' · draft',' · alternate')
    for p in soup.select('.screen-instructions'):
        p.string = p.get_text().replace('approved 0.50-inch','default 0.50-inch')
    for role, label in ROLE_LABELS.items():
        pages = soup.select(f'.page[data-role="{role}"]')
        total = len(pages)
        for idx, page in enumerate(pages, 1):
            old = page.select_one('.mission-title-block,.continuation-header')
            if old is None:
                raise RuntimeError(f'Missing header for {role} page {idx}')
            old_h1 = old.find('h1')
            h1_id = old_h1.get('id') if old_h1 else page.get('aria-labelledby')
            insignia = clone_insignia(old, soup)
            if idx == 1:
                new = soup.new_tag('header')
                new['class'] = ['mission-title-block']
                new['data-header-contract'] = 'universal-v1.1'
                rail = soup.new_tag('div'); rail['class']=['mission-rail']; rail['aria-hidden']='true'; new.append(rail)
                cp = soup.new_tag('div'); cp['class']=['mission-title-copy']
                h = soup.new_tag('h1'); h['class']=['hero-title']; h.string=CONFIG['title']
                if h1_id: h['id']=h1_id
                cp.append(h)
                sub = soup.new_tag('p'); sub['class']=['mission-subtitle']; sub.string=CONFIG['subtitle']; cp.append(sub)
                new.append(cp)
                ident = soup.new_tag('div'); ident['class']=['identity-mark']; ident.append(insignia)
                ic = soup.new_tag('div'); ic['class']=['identity-copy']
                inst = build_institution(soup); ic.append(inst)
                dr = soup.new_tag('div'); dr['class']=['document-role']; dr.string=label; ic.append(dr)
                ident.append(ic); new.append(ident)
            else:
                new = soup.new_tag('header')
                new['class']=['continuation-header']; new['data-header-contract']='universal-v1.1'
                cp = soup.new_tag('div'); cp['class']=['continuation-copy']
                h = soup.new_tag('h1'); h.string=CONFIG['title']
                if h1_id: h['id']=h1_id
                cp.append(h)
                rr = soup.new_tag('div'); rr['class']=['continuation-role']; rr.string=f'{label} · Continued'; cp.append(rr)
                new.append(cp)
                ci = soup.new_tag('div'); ci['class']=['continuation-identity']; ci.append(insignia)
                inst = build_institution(soup); ci.append(inst)
                new.append(ci)
            old.replace_with(new)
            old_footer = page.select_one('.publication-footer')
            footer = soup.new_tag('footer'); footer['class']=['publication-footer']; footer['data-footer-contract']='universal-v1.1'
            sp = soup.new_tag('span'); sp.string=f'{label} {idx} of {total}'; footer.append(sp)
            if old_footer: old_footer.replace_with(footer)
            else: page.select_one('.page-frame').append(footer)
            page['aria-label'] = f'{label} page {idx} of {total}'
    style = soup.find('style')
    if style: style.append('\n' + CSS + '\n')
    out = str(soup)
    out = out.replace('SSS_C1_CASE01_EDITABLE_MASTER_v1.0_custom.html','SSS_C1_CASE01_EDITABLE_MASTER_v1.1_custom.html')
    out = out.replace('sss-case01-v1-state','sss-case01-v1-1-state').replace('sss-case01-v1-content','sss-case01-v1-1-content')
    out = out.replace('Publishing Master v1.0','Publishing Master v1.1').replace('Editable Master v1.0','Editable Master v1.1')
    out = out.replace('source validation build','embedded source version')
    target.write_text('<!DOCTYPE html>\n' + out.split('<!DOCTYPE html>',1)[-1].lstrip(), encoding='utf-8')

def append_controlled(path, marker, heading, body):
    if not path.exists():
        return False
    text = path.read_text(encoding='utf-8')
    start = f'<!-- {marker}_START -->'
    end = f'<!-- {marker}_END -->'
    block = start + '\n## ' + heading + '\n\n' + body.strip() + '\n' + end
    pattern = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
    if pattern.search(text):
        text = pattern.sub(block, text)
    else:
        text = text.rstrip() + '\n\n' + block + '\n'
    path.write_text(text, encoding='utf-8')
    return True

def update_readme(path):
    text = path.read_text(encoding='utf-8') if path.exists() else '# SSS Campaign 1, Case 01 — ISS Greenhouse Module\n'
    marker='V1.1_PAGE_IDENTITY'
    start=f'<!-- {marker}_START -->'; end=f'<!-- {marker}_END -->'
    block=(start+'\n## Current v1.1 review master\n\n'
           '`master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html`\n\n'
           'The approved v1.0 master and its fixed outputs remain unchanged as the historical release. The v1.1 master applies the universal printable page identity system: location-only subtitle, institutional identity at right, generic continuation headers, role-plus-position footers, and no visible production metadata.\n\n'
           'Fixed v1.1 PDFs are not committed during review. Generate temporary test output only when needed; publish fixed files after automated review and owner physical print testing.\n'
           +end)
    text = re.sub(re.escape(start)+r'.*?'+re.escape(end), block, text, flags=re.S) if start in text else text.rstrip()+'\n\n'+block+'\n'
    path.write_text(text, encoding='utf-8')

def main():
    case = ROOT/'sss/campaign-1/case-01-iss-greenhouse'
    source = case/'master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html'
    target = case/'master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html'
    if not source.exists():
        raise SystemExit(f'Missing required Case 01 v1.0 master: {source}')
    transform_master(source, target)
    update_readme(case/'README.md')
    changelog = ('# SSS Case 01 v1.1 Page-Identity Changelog\n\n'
                 '- Preserves the approved v1.0 master unchanged.\n'
                 '- Adds the universal first-page title/institution banner.\n'
                 '- Uses `Campaign 1 · Case 01 · Low Earth Orbit` as the banner subtitle.\n'
                 '- Replaces page-specific continuation titles with one generic role-level continuation header.\n'
                 '- Reduces printable footers to role plus `N of total`.\n'
                 '- Removes visible approval, validation, version, date, baseline, and document-code metadata from printable pages.\n'
                 '- Retains all instructional content and validated publishing behavior.\n')
    (case/'master/SSS_C1_CASE01_V1.1_CHANGELOG.md').write_text(changelog, encoding='utf-8')
    manifest = {
      'case':'SSS-C1-CASE01','current_master':'master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html',
      'historical_master':'master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html','master_version':'1.1',
      'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'v1_1_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
      'governing_amendment':'shared/visual-style-guide/amendments/UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md',
      'fixed_output_policy':'No new v1.1 PDFs committed during review.'}
    (case/'CASE01_V1_1_MASTER_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')

    shared_body = '''This document now follows `UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md`: first-page title/location copy at left with institutional identity at right; generic role-level continuation headers; role-plus-position printable footers; no visible production status, version, baseline, date, or document code; and v1.1 successor files rather than overwriting v1.0 masters.'''
    paths = [
      ROOT/'shared/visual-style-guide/VISUAL_STYLE_GUIDE_v1.0.md',
      ROOT/'shared/visual-style-guide/reference/v1.0/VISUAL_STYLE_GUIDE_v1.0_QUICK_REFERENCE.md',
      ROOT/'shared/implementation/SSS_HHH_V1_EDITABLE_MASTER_HANDOFF.md',
      ROOT/'sss/blueprint/SSS_CURRICULUM_BLUEPRINT_v1.0.md']
    for p in paths:
        append_controlled(p,'UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1_0_4','Universal printable page identity — v1.0.4',shared_body)
    checklist = ROOT/'shared/visual-style-guide/reference/v1.0/VISUAL_STYLE_GUIDE_v1.0_COMPLIANCE_CHECKLIST.md'
    checklist_body = '''- [ ] First-page banner uses left accent rail, title/location at left, and institution/role at right.
- [ ] Subtitle contains campaign, case, and location only.
- [ ] Continuation header is generic within the role and places institutional identity at right.
- [ ] Printable footer contains only the role and `N of total`.
- [ ] No printable approval, validation, version, baseline, date, or document-code metadata appears.
- [ ] A v1.0 master remains preserved when a v1.1 successor is created.'''
    append_controlled(checklist,'UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1_0_4','Universal printable page identity — v1.0.4',checklist_body)
    print(f'Created {target.relative_to(ROOT)}')
    print('Case 01 v1.0 and existing fixed v1.0 outputs were not modified.')

if __name__ == '__main__':
    main()
