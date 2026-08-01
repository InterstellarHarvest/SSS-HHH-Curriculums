# SSS/HHH Curriculum Editor — approved canonical workflow

This repository-local browser application loads the current Case 01 v1.1, Case 02 v1.0, and Case 03 v1.1 packages. It does not open, iframe, rewrite, or execute a complete approved master. Worksheet-only DOM and exact presentation stylesheets are generated deterministically from their authorized goldens and mounted in an open Shadow DOM so application and worksheet CSS cannot affect each other.

**Phase 2 status:** OWNER REVIEW PASS · READY TO MERGE

Cases 01, 02, and 03 are accepted in the central editor. The current maintained Case 01 v1.1 and Case 02 v1.0 HTML presentations, exact Phase 2 parity, browser print previews, and physical printing passed owner review on 2026-08-01 at 100% / Actual Size.

The central editor is now the approved canonical active authoring and customization interface for these current releases. Their registered packages are the canonical active editable production sources. Approved standalone masters and role HTML remain immutable release snapshots; embedded case-owned editors are deprecated compatibility implementations and are not the active workflow. Cutover status is **APPROVED · OWNER REVIEW PASS · READY TO MERGE**.

## Launch

From the repository root:

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/>. Stop the server with `Ctrl-C`.

The server is required. `file://` is not a supported production path because the application fetches the registry, package, content, shared shell, styles, icons, and task registry as separate repository resources.

## Multi-case workflow

1. Choose the current Case 01, Case 02, or Case 03 package, then choose a role in the library rail. The exact primary case labels are `1 - ISS Greenhouse`, `2 - Lunar Greenhouse`, and `3 - Mars Habitat`. The rail contains only Student, Teacher, Answer Key, and Accessible; versions are not selected in the primary case menu and historical versions are not exposed.
2. Use **Fill responses** for response fields or **Edit text** for explicitly marked instructional nodes.
3. Changes autosave to local browser storage under the package's curriculum/campaign/case/version document key. Selected case, role, edits, and responses remain isolated while switching.
4. Use the actions in this order: **Print / Save PDF**, **Download Editable Copy**, **Download Worksheet**, **Clear Responses**, and **Reset This Case**.
5. **Download Editable Copy** creates a self-contained portable editable HTML document containing every role, the editing toolbar, current instructional edits, current responses, current display settings, role switching, and local editing and printing capabilities.
6. **Download Worksheet** creates a clean self-contained HTML worksheet containing only the selected role, its current responses and instructional edits, and the selected Grayscale state when applicable. It contains no editing toolbar, role selector, application chrome, or authoring controls.

The **Page shadow** toggle is on by default and changes only the screen-only shadow used to separate worksheet pages visually. It does not change page geometry, margins, printable area, guides, page-fit detection, or export pagination, and shadows never print. Page-fit status reads **Pages fit**, **1 page too full**, or **N pages too full**. A page is too full when content extends beyond its printable page area.

Grayscale is a toolbar presentation modifier, not a library role. It remains on when switching among instructional roles and never changes the selected role or page set. Student with Grayscale enabled maps to the canonical Grayscale Mission output name. Other roles retain their own output identity while exporting with grayscale presentation. Grayscale uses token overrides and keeps `Student Mission` identity in the canonical Student Grayscale footer.

The central toolbar omits the duplicate Role selector because the library rail is authoritative. A complete portable HTML export restores the shared-shell Role selector because that file has no library rail.

**Clear Responses** removes response and note fields only from the selected source role; it does not remove instructional edits or affect other roles or cases. **Reset This Case** restores only the loaded case/version to its approved package defaults and removes that case/version's locally saved responses, instructional edits, display settings, and role selection. It does not affect another case/version, unrelated browser storage, the curriculum library, or repository files. In a downloaded complete HTML file, Reset This Case preserves the instructional edits embedded in that file and clears response recovery work, matching shared-shell v1.0 behavior.

## Portable output and printing

Both download actions inline the selected package's hash-verified presentation CSS, icon sprite, page content, figures/insignia, current edits, current responses, configuration, and portable runtime. Filenames retain the selected case and version. They do not overwrite repository files.

The **Print / Save PDF** button first validates page fit, serializes the current role with current edits, responses, margins, density, Grayscale, and Guides, and loads that clean self-contained role document into a temporary same-origin print iframe. The app waits for the document, fonts, images, and embedded assets; focuses that isolated document; and invokes its browser print dialog. The print document physically contains only the selected role pages and exact worksheet CSS—no toolbar, library rail, application headings/statuses, authoring controls, or page shadow. The editor remains open and unchanged.

Browser PDF export does not guarantee PDF accessibility. Any PDF distributed, published, or archived requires separate accessibility verification. This application does not create, validate, preflight, checksum, or store PDFs. PDF/manual printing remains exclusively a browser-print-dialog action.

## Validation

Static/package validation requires Python and Beautiful Soup 4:

```bash
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/validate_phase2_static.py
```

Browser validation uses the installed Google Chrome executable directly and creates only temporary profiles/screenshots:

```bash
python3 apps/curriculum-editor/tests/run_browser_tests.py
```

Exact master/editor/export parity uses Playwright, Pillow, and the installed Chrome executable. It retains contact sheets and the corrected Accessible Task 7 comparison under `tests/screenshots/parity-v1.1/`:

```bash
python3 apps/curriculum-editor/tests/validate_v1_1_parity.py
python3 apps/curriculum-editor/tests/validate_phase2_parity.py
```

To use a different Chrome-compatible executable:

```bash
python3 apps/curriculum-editor/tests/run_browser_tests.py --chrome /path/to/chrome
```

The Phase 2 static suite validates both migrated package schemas, deterministic extraction, the protected-artifact ledger, binding rules, reconciliation records, Case 03 Phase 1 regression, and the no-PDF rule. The browser suite retains every accepted Phase 1 assertion and adds repeated three-case switching, exact dropdown labels, page-fit language, Page shadow behavior, isolated print DOMs for all 15 case/role profiles, page counts, first/continuation identity, chrome exclusion, state/content isolation, stale-style/DOM checks, case-specific exports, and accessibility announcements. The Phase 2 parity suite checks all 43 Case 01/02 role-profile pages for structure, task assignment, geometry, computed presentation, rendered pixels, component containment, current maintained role HTML, complete portable export, and current-role export parity.

The current owner-review capture is [curriculum-editor-wide-desktop.png](tests/screenshots/curriculum-editor-wide-desktop.png) at 1440×1200.

## Security and local-file assumptions

- The server binds to `127.0.0.1` by default and serves repository files read-only through Python's static handler. Do not bind it to an external interface on an untrusted network.
- Case packages are trusted repository code/content. The app rejects scripts, styles, links, and iframes inside instructional content fragments, but package CSS and the portable runtime are still executable presentation assets controlled by repository owners.
- Local storage is recovery state, not a durable database or synchronization service. Downloaded HTML is the portable handoff format.
- Downloaded HTML contains JavaScript for local editing and printing. Treat customized files from unknown sources as untrusted files.
- No authentication, cloud service, backend database, or external runtime API is used.

## Cutover status and retained compatibility boundary

- Only current releases are selectable: Case 01 v1.1, Case 02 v1.0, and Case 03 v1.1.
- Historical-version browsing and a prominent version selector are intentionally absent.
- The current Case 01, Case 02, and Case 03 packages are canonical active sources. Approved/current standalone masters and role files remain immutable approved release snapshots and parity references; they are not ongoing editable sources.
- Autosave is browser-profile and origin specific; it does not synchronize between devices or browsers.
- Browser print behavior and physical results remain browser/driver dependent; owner review passed at 100% / Actual Size.
- Case 03 owner review and browser physical-print review passed on 2026-07-31 at 100% / Actual Size; printer and paper were not recorded.
- Case 01/02 owner review, browser print-preview review, physical-print review, and exact migration parity passed on 2026-08-01. Browser, printer/copier, and paper were not recorded.
- Embedded case-owned editors remain present as deprecated compatibility implementations. Removing them is not authorized. Repository cleanup, Case 04, and HHH production have not started.
- HTML accessibility is validated; manually created PDFs require their own accessibility review.
- Cutover is `APPROVED` with `OWNER_REVIEW_PASS` and `READY_TO_MERGE`; see `CUTOVER_OWNER_APPROVAL.md`. Repository cleanup and Case 04 remain `NOT_STARTED`.

See [CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md](../../shared/implementation/CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md) for the contract, load sequence, accessibility model, validation coverage, and cutover boundary.

See [PHASE1_ACCEPTANCE.md](PHASE1_ACCEPTANCE.md) for the final owner-accepted validation summary and cutover boundary.
