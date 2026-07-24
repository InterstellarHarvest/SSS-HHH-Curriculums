# SSS Case 01 v1.0 Validation Report

**Implementation under test:** `SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`  
**Validation date:** 2026-07-23  
**Browser engine:** Headless Chromium 144  
**Validation status:** **PASS FOR REPOSITORY REVIEW — NOT YET RELEASE-APPROVED**

## 1. Result summary

The migrated master passed the automated and rendered checks for:

- role isolation;
- expected page counts;
- fixed US Letter output;
- visible overflow detection;
- grayscale output;
- print preview state;
- publishing-state preservation across role changes;
- response-content restoration into a fresh document DOM;
- keyboard and screen-reader markup basics;
- source metadata and canonical SAA asset references.

Release approval remains blocked by the human physical-print gate and the decisions listed in `SSS_C1_CASE01_V1_BLOCKERS_AND_EXCEPTIONS.md`.

## 2. Output validation

| Output | Pages | Visible overflow | PDF openable | Searchable text | Result |
|---|---:|---:|---:|---:|---|
| Student | 3 | 0 | Yes | Yes | Pass |
| Teacher Quick Start / Teacher packet | 7 | 0 | Yes | Yes | Pass |
| Dedicated Answer Key | 3 | 0 | Yes | Yes | Pass |
| Parallel Accessible Edition | 6 | 0 | Yes | Yes | Pass with PDF-tagging limitation |
| All Pages audit view | 19 | 0 | Yes | Yes | Pass |
| Student grayscale | 3 | 0 | Yes | Yes | Pass |

Machine-readable evidence is stored in `validation-artifacts/validation-results.json`.

## 3. Page-fill validation

### Student packet

- Page 1 uses remaining printable space for initial-thinking writing.
- Page 2 allocates practical row height to four evidence sources, competing explanations, and the mechanism comparison.
- Page 3 preserves Claim < Evidence < Reasoning minimum hierarchy and uses the remaining space for the stacked CER task.
- Engineering and exit-ticket areas remain usable without enlarging type or adding decoration.

### Teacher packet

- Existing seven-page content structure was retained.
- Short lesson-plan, assessment, case-analysis, rubric, and reference pages include genuine editable notes regions.
- Teacher notes use a neutral technical treatment rather than answer-key or student-response styling.
- The references and technical-fallback page no longer leaves an avoidable lower-page void.

### Answer key

- The key mirrors the student task order.
- Model responses use dedicated answer blocks.
- The first and second key pages include usable teacher note regions rather than dead paper.
- Model CER remains readable at instructional-use density.

### Accessible edition

- The accessible packet uses six pages, larger body type, reduced density, one-column task flow, and larger response areas.
- Numbered task order remains 1 through 9.
- Case identity, mission question, evidence structure, competing explanations, diagnosis, CER, engineering response, exit ticket, and optional extension remain parallel to the standard student packet.

## 4. State and interaction validation

### 4.1 Independent roles

Validated roles:

- Student
- Teacher
- Answer Key
- Accessible
- All Pages

Changing role does not reset:

- margin setting;
- density setting;
- grayscale state;
- print-preview state;
- edit state;
- fillable state;
- saved instructional edits;
- saved response content.

### 4.2 Persistence

A response was entered into the initial-thinking field, saved by the document event handler, and then loaded into a fresh document DOM seeded with the saved local-storage records. The value restored correctly.

### 4.3 Print behavior

- `@page` is US Letter portrait.
- Browser page margin is zero; document margins are controlled inside the page.
- Publishing controls, screen directions, skip link, and overflow warnings do not print.
- Role selectors determine the printed packet without temporarily changing the role.
- Page numbering is role-specific and correct.

## 5. Accessibility basics

Automated markup checks found:

- one English-language document root;
- one main landmark;
- 19 named page regions;
- one skip link to the document workspace;
- zero images without `alt` attributes;
- zero unnamed buttons;
- zero unlabeled selects;
- zero response fields without accessible names;
- zero tables without captions;
- zero duplicate IDs;
- zero page regions with broken heading references.

Editable and response regions enter the tab order only when Edit or Fillable Student mode is active.

### Accessible PDF limitation

Chromium-generated PDFs are not tagged PDFs. The parallel Accessible Edition is therefore validated primarily as accessible HTML and as a visually accessible print edition. A tagged-PDF export pipeline is required if tagged PDF/UA output becomes a formal deliverable.

## 6. Grayscale validation

The first grayscale implementation used `filter: grayscale(1)` on the complete workspace. Chromium rasterized that PDF, which made text extraction fail.

That implementation was rejected.

The final implementation uses:

- grayscale CSS design-token overrides for text, rules, fills, and status colors;
- grayscale filtering only on the insignia and framed artwork.

The resulting grayscale PDF remains text-based and searchable. Meaning is retained through labels, icons, borders, line weights, and text—not color alone.

## 7. Compliance checklist disposition

### 7.1 Identity and hierarchy

| Check | Result | Evidence |
|---|---|---|
| SAA identity correct | Pass | Solar Agricultural Authority used throughout |
| Canonical insignia used | Pass | Relative reference to `shared/assets/insignia/saa.svg` |
| First page uses Mission Title Block | Pass | First page of each independent role |
| Continuation pages use compact headers | Pass | 15 continuation headers |
| Production metadata absent from prominent header | Pass | Version, baseline, date, and status confined to quiet mark/footer/meta |
| Filled publication-status mark | Pass | `VALIDATION BUILD` mark |

### 7.2 Page and typography

| Check | Result | Evidence |
|---|---|---|
| US Letter portrait | Pass | PDF page size 612 × 792 points |
| Default margins 0.50 inches | Pass | Shared `--margin: .5in` and approved control default |
| 12-column grid | Pass | `.grid-12` and reusable spans |
| Balanced density default | Pass | `balanced` default state |
| Inter + JetBrains Mono system | Conditional pass | Declared correctly; deterministic offline packaging remains open |
| Approved point-equivalent scale | Pass | Shared print-type variables |
| No emergency type reduction | Pass | Student and key repaginated instead |

### 7.3 Components

| Check | Result | Evidence |
|---|---|---|
| Phosphor Regular recurring icons | Pass | Nine embedded official regular symbols |
| Technical Label Headings | Pass | 66 standardized section labels |
| Left-rule pale-field callouts | Pass | Science, caution, fiction, and optional variants |
| Prompt above blank box | Pass | Student and accessible response blocks |
| Three stacked CER boxes | Pass | Standard and accessible packets |
| Ruled technical tables | Pass | Vocabulary, evidence, timing, rubric, and answer tables |
| Neutral teacher notes | Pass | Teacher-note and notes-area treatment |
| Dedicated answer blocks | Pass | Independent key pages |
| Captioned tables | Pass | All tables include captions, visually hidden where appropriate |

### 7.4 Content separation and metadata

| Check | Result | Evidence |
|---|---|---|
| Teacher answers absent from student output | Pass | Independent role selectors; no answer-inline system |
| Dedicated Answer Key | Pass | Three-page independent role |
| Accessible edition parallel | Pass | Six-page role with same identifiers/order |
| Source and compatibility metadata | Pass | Head metadata and split footers retain `2a6e8a7` |
| Quiet footer metadata | Pass | Split Metadata Rule |
| Correct page numbering | Pass | Role-specific page totals verified in PDF |

### 7.5 Release blockers

| Check | Result | Note |
|---|---|---|
| No visible overflow | Pass | All roles, grayscale, and preview |
| No placeholders | Pass | No TODO/TBD/placeholder tokens |
| No blurred pixel art | Not applicable | Embedded game-art header was removed; only canonical vector insignia used |
| Human 100% print sample | Pending | Required before Approved status |
| Tagged accessible PDF | Pending if required | Accessible HTML/print edition passes; Chromium PDF is untagged |

## 8. Renderer and PDF notes

PDFs were rendered through Poppler/PDFium tooling for visual review. No clipped text, missing pages, black boxes, or visible broken glyphs were found.

Poppler emitted non-fatal `Bad bounding box in Type 3 glyph` warnings for some vector icon/insignia glyphs generated by Chromium. The rendered marks were visually intact. This should be monitored if the project changes PDF generation engines.

## 9. Validation artifacts

The validation package includes:

- role PDFs;
- grayscale PDF;
- screen workspace screenshots;
- PDF-render contact sheets;
- machine-readable JSON results;
- the repeatable Playwright validation script.

These are review evidence, not proposed permanent curriculum-source files unless the repository adopts a validation-artifact policy.

---

## 10. Revalidation Addendum — post-edit layout regression (2026-07-23)

**Reason:** After the original validation, the game-content audit applied four small text edits to `SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html` (two Teacher notes on the distractor and engineering panels, and two Teacher source-list label corrections). Because even pure text can change wrapping, the render/overflow regression was rerun against the edited file.

**Note on tooling:** The `validation-artifacts/` directory and its `validation-results.json` / `run_validation.py` referenced above were review evidence from the original pass and had not been committed to the repository. This rerun therefore used an equivalent headless-Chromium harness that drives the packet's own role/overflow/grayscale/print-preview logic; the harness and its JSON output are now stored under `../validation-artifacts/` for reproducibility.

**Build under test (post-edit):**
`SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`
SHA-256 `5ccac6bf6ff64dd20596a18abdc264b3105f245ee7777e4cbc9731ba536eb83b` (see `../validation-artifacts/CHECKSUMS.txt`).

**Environment:** Headless Chromium via Playwright (Chromium 1217, node v20.20.2).

**Results — all PASS, identical to the pre-edit baseline:**

| Check | Expected | Post-edit result |
|---|---|---|
| Student pages | 3 | 3, no overflow |
| Teacher pages | 7 | 7, no overflow |
| Answer Key pages | 3 | 3, no overflow |
| Accessible pages | 6 | 6, no overflow |
| All Pages view | 19 | 19, no overflow |
| Teacher grayscale | fits, no overflow | 7 pages, no overflow |
| Teacher print preview | fits, no overflow | 7 pages, no overflow |
| Edit/fill + persistence | response restores after reload | token written, restored after full reload |
| Teacher PDF page count | 7 | 7 (`../validation-artifacts/teacher_v1.0_revalidated.pdf`) |
| Console / page JS errors | none | none |

The overflow test replicates the packet's own logic (`.page-frame`/`.content-area` `scrollHeight` vs `clientHeight`, 2 px tolerance) and the built-in status line reported "no visible overflow" for every role at 0.50 in margins / balanced density. The two Teacher notes did not push their pages (Teacher p.4 engineering panel, Teacher p.5 distractor table) into overflow, and no page count changed.

**Publishing artifacts not regenerated:** no v1.0 published PDFs, contact sheets, checksummed bundles, or packaged ZIPs exist in the repository (only v0.2/v0.3 PDFs under `published/`). v1.0 remains a **Validation Build**; those packaged outputs are produced at release time, after the human print/font/tagged-PDF gates clear. The single revalidation Teacher PDF above is regression evidence, not a published deliverable.

**Verdict unchanged:** PASS FOR REPOSITORY REVIEW — NOT YET RELEASE-APPROVED. The post-edit build is layout-clean and matches the pre-edit page geometry.

---

## 11. Revalidation Addendum — student-form rules update (2026-07-23)

**Reason:** The approved student-form clarifications were applied to the repo via `SSS_HHH_STUDENT_FORM_RULES_UPDATE_FIXED/` (combined dry-run passed, reporting `USING BIBLE: shared/curriculum-bible/SSS_HHH_CURRICULUM_BIBLE_v1.2.md`, then applied). Two changes touch the Case 01 packet layout:

1. **Student identification row** (Name / Date / Period) moved to the first printable element of Student page 1 and Accessible page 1, above the Mission Title Block; not repeated on continuation, Teacher, or Answer Key pages.
2. **Exact-match WORD BANK for Task 5** added to Student page 2 and Accessible page 3 (four entries: `curve or grow without consistent orientation · downward · settle · settle in one direction`), and the Answer Key mechanism wording aligned to the bank (removed "with gravity/downward").

**Build under test (post-update):** `SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`
SHA-256 `3a4e7ba45c536c617c77140ed9882f7d50e0ed7be32ad2cbe48dff99bea6bb7e` (supersedes the prior `5ccac6bf…`; see `../validation-artifacts/CHECKSUMS.txt`).

**Environment:** Headless Chromium via Playwright (Chromium 1217, node v20.20.2).

**Results — all PASS, page geometry unchanged from baseline:**

| Check | Expected | Post-update result |
|---|---|---|
| Student pages | 3 | 3, no overflow |
| Teacher pages | 7 | 7, no overflow |
| Answer Key pages | 3 | 3, no overflow |
| Accessible pages | 6 | 6, no overflow |
| All Pages view | 19 | 19, no overflow |
| Teacher grayscale / print preview | fits | 7 pages, no overflow |
| Edit/fill + persistence | restores after reload | restored |
| Teacher PDF page count | 7 | 7 |
| Console / page JS errors | none | none |

The relocated identification rows and the two new Task 5 word banks did not add pages or trigger overflow in any role. Script-side verification also confirmed exactly one identification row per first page (correct field order), no row on continuation/Teacher/Answer pages, exactly two Task-5 word banks with the one-entry-per-blank contract, and preserved response-field keys (`s2-earth-settle`, `a-micro-root`, etc.).

**Backups:** `.student-id-update-backup/20260723-213011` and `.word-bank-update-backup/20260723-213011` at the repo root.

**Verdict unchanged:** PASS FOR REPOSITORY REVIEW — NOT YET RELEASE-APPROVED.

---

## 12. Revalidation Addendum — task-reference parity, registry-rendered clean source (2026-07-24)

**Reason:** Task-reference parity was first applied by an updater script (commit `b808fd9`). During subsequent working-tree operations the packet was **browser-reserialized** by an external tool (self-closing tags flattened, a runtime `style="--margin…"` injected on `<html>`), diverging from the committed clean source. To guarantee clean bytes, the packet was restored to the exact `63a7ead` source (SHA-256 `3a4e7ba4…`, verified byte-identical) and the parity change was re-applied **without reserialization** and finalized by rendering task references from the canonical `source/task-registry.js`, preserving the original clean serialization.

**Changes (identical intent to `b808fd9`, with refinements):**
- Answer Key headings retitled to Student task ids; Answer Key now begins at Task 3; heading number sequence is **3, 4, 5, 6, 6, 7, 8, 9**.
- Non-keyable Task 2 "Initial Thinking" Answer Key block removed in full (no `INITIAL THINKING` / `Accepted evidence needs` remains).
- Teacher lesson-flow, collection, and procedure references cite the exact numbered task titles; the four in-prose Teacher references are wrapped in `<strong class="task-reference">…</strong>` (with a `.task-reference` style rule), rendered from `source/task-registry.js`. Table structure, headers, rows, and answer text are unchanged.
- **Both** Accessible Task 6 headings now read `6 · Diagnose and reject an alternative` (the script had changed only the first).
- The script's `<!-- …PARITY…: MASTER -->` marker comment is **intentionally omitted** (it was the source of an earlier HTML-validity defect and is not required).

**Canonical task registry:** `source/task-registry.js` (frozen ES module, self-validating) archives the exact task ids/titles; `taskLabel(n)` yields the strings used above (e.g. `6 · Diagnose and reject an alternative`), with Task 6 declaring two Answer Key parts (`diagnosis`, `rejected-alternative`) — the reason the Answer Key sequence carries a doubled 6.

**Build under test:** `SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`
SHA-256 `3a657ddb731ff20d65b7e42521fcde620814d517ed2abb92560b7dca10a1abbe` (supersedes `5b9f1c89…`; see `../validation-artifacts/CHECKSUMS.txt`).

**Serialization integrity:** 563 lines; self-closing tags preserved; no runtime `html` style attribute; text diff vs `63a7ead` is 18 insertions / 17 deletions (small and localized).

**Environment:** Headless Chromium via Playwright (Chromium 1217, node v20.20.2).

| Check | Expected | Result |
|---|---|---|
| Student / Teacher / Answer / Accessible / All pages | 3 / 7 / 3 / 6 / 19 | 3 / 7 / 3 / 6 / 19, no overflow |
| Teacher grayscale / print preview | fits | no overflow |
| Edit/fill + persistence | restores after reload | restored |
| Teacher PDF page count | 7 | 7 |
| Console / page JS errors | none | none |
| Answer Key heading sequence | 3,4,5,6,6,7,8,9 | 3,4,5,6,6,7,8,9 |
| Task 3 table headers / rows | Source · Model evidence · Interpretation / Crew · Sensors · Plants · Logs | intact |

**Verdict unchanged:** PASS FOR REPOSITORY REVIEW — NOT YET RELEASE-APPROVED.
