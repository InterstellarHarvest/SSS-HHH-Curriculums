import pw from '/Users/MrDashiki/.nvm/versions/node/v20.20.2/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import fs from 'fs';

const FILE = process.argv[2];
const OUTDIR = process.argv[3];
const url = 'file://' + FILE;

const EXPECT = { student: 3, teacher: 7, answer: 3, accessible: 6, all: 19 };

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1400, height: 1200 } });
const jsErrors = [];
page.on('pageerror', e => jsErrors.push(String(e)));
page.on('console', m => { if (m.type() === 'error') jsErrors.push('console:' + m.text()); });

await page.goto(url, { waitUntil: 'networkidle' });

// Find the role <select> (the one whose options include student/teacher/answer/accessible/all)
const roleSel = await page.evaluate(() => {
  const sels = [...document.querySelectorAll('select')];
  for (const s of sels) {
    const vals = [...s.options].map(o => o.value);
    if (['student','teacher','answer','accessible','all'].every(r => vals.includes(r))) {
      s.id = s.id || '__role_select__';
      return '#' + s.id;
    }
  }
  return null;
});
if (!roleSel) { console.log(JSON.stringify({ fatal: 'role select not found' })); await browser.close(); process.exit(1); }

async function setRole(role) {
  await page.selectOption(roleSel, role);
  await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
}

// Independent overflow measurement replicating the packet's own test (frame/content scroll vs client + 2px)
async function measure() {
  return await page.evaluate(() => {
    const pages = [...document.querySelectorAll('.page')].filter(p => getComputedStyle(p).display !== 'none');
    const rows = pages.map((p, i) => {
      const frame = p.querySelector('.page-frame');
      const content = p.querySelector('.content-area');
      const of = (frame.scrollHeight > frame.clientHeight + 2) || (frame.scrollWidth > frame.clientWidth + 2) ||
                 (content.scrollHeight > content.clientHeight + 2) || (content.scrollWidth > content.clientWidth + 2);
      return {
        idx: i + 1,
        cls: p.className.replace(/\s+/g, ' ').trim(),
        appOverflowing: p.classList.contains('overflowing'),
        measuredOverflow: of,
        contentOverBy: Math.max(0, content.scrollHeight - content.clientHeight),
        frameOverBy: Math.max(0, frame.scrollHeight - frame.clientHeight),
      };
    });
    const statusEl = document.querySelector('.toolbar-status, [class*="status"]');
    return { visible: pages.length, rows, status: statusEl ? statusEl.textContent.trim() : null };
  });
}

const report = { file: FILE, jsErrors, roles: {}, toggles: {}, pdf: {} };

for (const role of ['student','teacher','answer','accessible','all']) {
  await setRole(role);
  const m = await measure();
  const overflowing = m.rows.filter(r => r.measuredOverflow || r.appOverflowing);
  report.roles[role] = {
    expectedPages: EXPECT[role], visiblePages: m.visible,
    pageCountOK: m.visible === EXPECT[role],
    overflowCount: overflowing.length,
    overflowPages: overflowing.map(r => ({ idx: r.idx, contentOverBy: r.contentOverBy, frameOverBy: r.frameOverBy, cls: r.cls })),
    status: m.status,
  };
}

// Toggles on the Teacher role (the edited role): grayscale, print-preview
async function toggleCheck(name, buttonMatch) {
  await setRole('teacher');
  const clicked = await page.evaluate((match) => {
    const btns = [...document.querySelectorAll('button')];
    const b = btns.find(x => new RegExp(match, 'i').test(x.textContent) || new RegExp(match, 'i').test(x.id) || new RegExp(match,'i').test(x.getAttribute('aria-label')||''));
    if (b) { b.click(); return b.textContent.trim() || b.id; }
    return null;
  }, buttonMatch);
  await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
  const m = await measure();
  const overflowing = m.rows.filter(r => r.measuredOverflow || r.appOverflowing);
  // toggle back off
  await page.evaluate((match) => {
    const btns = [...document.querySelectorAll('button')];
    const b = btns.find(x => new RegExp(match, 'i').test(x.textContent) || new RegExp(match, 'i').test(x.id) || new RegExp(match,'i').test(x.getAttribute('aria-label')||''));
    if (b) b.click();
  }, buttonMatch);
  return { clicked, visiblePages: m.visible, overflowCount: overflowing.length, overflowPages: overflowing.map(r => ({ idx: r.idx, contentOverBy: r.contentOverBy })), status: m.status };
}

report.toggles.grayscale = await toggleCheck('grayscale', 'gray');
report.toggles.printPreview = await toggleCheck('printPreview', 'preview');

// Persistence check: enter fill/edit, type into a response field, reload, verify it restored
await setRole('student');
const persist = await page.evaluate(async () => {
  const btns = [...document.querySelectorAll('button')];
  const fill = btns.find(x => /fill/i.test(x.textContent) || /fill/i.test(x.id));
  if (fill) fill.click();
  await new Promise(r => requestAnimationFrame(r));
  const resp = document.querySelector('[data-response]');
  if (!resp) return { ok: false, reason: 'no response node' };
  resp.focus();
  resp.innerHTML = 'REGRESSION_PERSIST_TOKEN_42';
  resp.dispatchEvent(new Event('input', { bubbles: true }));
  return { ok: true };
});
await page.evaluate(() => new Promise(r => setTimeout(r, 300)));
await page.reload({ waitUntil: 'networkidle' });
const restored = await page.evaluate(() => {
  return [...document.querySelectorAll('[data-response]')].some(n => /REGRESSION_PERSIST_TOKEN_42/.test(n.innerHTML));
});
report.persistence = { wrote: persist, restoredAfterReload: restored };

// Generate Teacher PDF (edited role) and count pages
await setRole('teacher');
const pdfPath = OUTDIR + '/teacher_v1.0_revalidated.pdf';
await page.pdf({ path: pdfPath, format: 'Letter', printBackground: true, preferCSSPageSize: true, margin: { top: '0', bottom: '0', left: '0', right: '0' } });
const buf = fs.readFileSync(pdfPath);
const pageMatches = (buf.toString('latin1').match(/\/Type\s*\/Page[^s]/g) || []).length;
report.pdf.teacher = { path: pdfPath, approxPageCount: pageMatches, expected: 7 };

fs.writeFileSync(OUTDIR + '/revalidation-results.json', JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
await browser.close();
