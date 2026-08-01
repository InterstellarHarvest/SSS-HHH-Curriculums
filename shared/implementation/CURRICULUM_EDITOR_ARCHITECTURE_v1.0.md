# Curriculum Editor Architecture v1.0

**Status:** Phase 1 accepted for Case 03 · Phase 2 VALIDATION_BUILD for Cases 01/02 · owner and physical-print gates OPEN

**Application:** `apps/curriculum-editor/`

**Packages:** `SSS-C1-CASE01` v1.1 · `SSS-C1-CASE02` v1.0 · `SSS-C1-CASE03` v1.1

**Package schema:** `shared/implementation/case-package.schema.v1.json`

## 1. Architecture boundary

The central application owns the library rail, toolbar orchestration, editing state, autosave, page-fit reporting, presentation isolation, isolated role printing, and export assembly. The shared shell remains the canonical source for toolbar markup, CER geometry, common components, icons, and established control behavior. The case package owns the hash-verified worksheet-only DOM and presentation CSS, task definitions, metadata, assets, roles, page counts, and filenames.

```text
case-registry.v1.json
        │ editorPackage
        ▼
selected current case package ── extracted content / exact presentation CSS / hashes
        │
        ├──────── shared shell toolbar / CSS / CER / icons
        │
        ▼
central Curriculum Editor
        ├── local recovery state (case + version + document key)
        ├── self-contained complete editable HTML
        └── self-contained selected-role HTML
```

The approved `SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html` remains a byte-identical historical release at SHA-256 `c97a880f0be0c58848c0d8a7394ce75925aff26f3fb542dc4d63cca25a9b6bce`. Its known split Accessible CER is not the current parity target. The corrected and owner-approved `SSS_C1_CASE03_EDITABLE_MASTER_v1.1.html` is the current Case 03 approved stable master and golden Phase 1 parity reference. Neither complete master is a central-editor runtime dependency.

`build_case03_v1_1.py` verifies the historical hash, extracts the worksheet DOM and exact case presentation, applies the owner-authorized Accessible reflow and Task 6 phrase bank, and deterministically emits controlled v1.1 sources, the approved successor master, five independent role outputs, package metadata, hashes, and release manifest. Existing approved cases use this hash-verified extraction/reconciliation path; future cases authored natively in the central editor use their package as canonical source from inception. Page counts alone never establish migration parity.

## 2. Runtime load sequence

1. `editor-app.js` fetches `shared/implementation/case-registry.v1.json`.
2. It discovers the current Case 01 v1.1, Case 02 v1.0, and Case 03 v1.1 `editorPackage` records in case-number order; historical releases remain metadata/artifacts rather than a prominent selector.
3. It validates supported schema/shell versions and required role/package fields.
4. It fetches every declared shared shell, task, extracted content, presentation stylesheet, and source-backed asset path, then verifies the package content, case CSS, and presentation SHA-256 values before mounting.
5. It parses the task registry and validates/expands any declared task-heading placeholder; the v1.1 extraction already contains the exact expanded master headings.
6. It rejects runtime/style/iframe elements in the instructional fragment and verifies persistence IDs and embedded asset selectors.
7. It mounts the exact worksheet presentation in an open Shadow DOM. The app CSS cannot select worksheet descendants, and the scoped worksheet CSS cannot select application chrome. The application-owned toolbar remains outside the shadow root, removes the duplicate Role selector, and controls the isolated document through the same state path.
8. It restores local recovery state for that exact curriculum/campaign/case/version and announces the case, version, role, and grayscale state through a polite live region. Switching packages replaces the worksheet Shadow DOM, styles, icons, font activation, and output configuration.

After toolbar mounting, the application measures its rendered height and writes that value to `--app-toolbar-offset`. A `ResizeObserver`, font-ready callback, and viewport-resize callback keep the editor layout padding and library rail top/height synchronized as controls wrap. CSS supplies only an initial fallback before measurement.

The small Python server exposes the repository root so declared package paths resolve consistently over HTTP. It adds no write endpoint, database, account, or network service.

## 3. Versioned case-package contract

Schema version 1 separates editor mechanics from case data. Its required fields cover:

- identity: schema version, case/curriculum/campaign IDs, title, subtitle/location, version, and release status;
- institution: identity ID, full name, three-line lockup, and insignia selector;
- persistence: globally unique case/version/document key;
- shell: version, canonical toolbar, shared styles, and icon sprite;
- instruction: HTML-fragment source and case-specific CSS sources;
- tasks: source, global assignment name, and task-registry schema version;
- assets: source-backed or content-embedded assets, MIME/type, selector where applicable, and embed requirement;
- roles: supported roles, default role, source-role mapping, document role, page count, and grayscale flag;
- output: complete and five current-role filenames;
- defaults: role, edit/fill modes, four margins, density, grayscale, Guides, and Page shadow (stored internally as `boundaries` for backward compatibility);
- accessibility: document language/title, load announcement, extended-description selectors, and the manual-PDF warning;
- approval: date, tester, owner-review and browser physical-print results, scale, printer/paper record, and artifact policy;
- migration provenance: golden/historical/successor master paths and hashes, pre-maintenance hash where applicable, reconciliation record, reason, and deterministic builder;
- Phase 2 authorization where applicable: maintenance revision, owner/date, validation status, and open owner/physical-print gates;
- presentation: extracted content/case/presentation hashes and required isolation mode.

All package paths are repository-relative, may not traverse upward, and must resolve to files. The package retains a Grayscale output profile mapped to Student source pages for export compatibility. Central navigation exposes only Student, Teacher, Answer Key, and Accessible; Grayscale is an independent presentation modifier.

Validation rejects unsupported schema versions, missing package/content/style/task files, missing role definitions, invalid task placeholders, invalid source-backed asset paths, and missing embedded asset selectors. The registry schema permits an optional `editorPackage`, allowing approved historical cases to remain registered without pretending they have been migrated.

## 4. Editing and recovery state

One state object controls role, four independent margins, density, edit/fill modes, grayscale, Guides, and Page shadow. The backward-compatible `boundaries` property controls only screen box shadow. `applyState()` mirrors relevant tokens onto the application body and the isolated worksheet-document root, then updates controls, visible pages, editable nodes, status text, and page-fit checks.

- Fill Responses exposes only `[data-response]` and supported ordinary form fields on the selected source role.
- Edit Text additionally exposes `[data-editable]` nodes. Structural attributes, IDs, task keys, role boundaries, and component metadata are never editable.
- Input saves by stable `data-persist-id` under `curriculum-editor:<documentKey>:content`.
- State saves under `curriculum-editor:<documentKey>:state`.
- Role switching does not reconstruct pages or change the Grayscale modifier. Student and Accessible response IDs remain independent; Teacher/Answer instructional boundaries remain isolated by page role.
- Clear Current Role requires confirmation in normal use and removes only selected-role response/note nodes.
- Reset Source requires confirmation in normal use, restores the in-memory package baseline, deletes both recovery keys, and reapplies package defaults.

Local storage is explicitly recovery state. It is not the canonical customized document.

## 5. Serialization and selected-role export

Complete serialization clones the live worksheet, copies current values, removes content-editing attributes and transient page overflow classes, and then embeds:

- shared components/editor/CER CSS;
- selected case CSS;
- Phosphor symbols and inline insignia/figures;
- all role pages and current instructional/response content;
- toolbar markup and current state;
- a standalone portable runtime and package/output configuration.

The exported file receives a derived document key, so it cannot collide with the central app or another export. In a fresh context, the embedded DOM supplies its instructional Reset Source baseline. Responses open with their embedded values but are cleared by Reset Source, matching shared-shell v1.0 behavior.

Selected-role serialization filters the clone to that role's source pages, applies the current Grayscale modifier, and omits the toolbar, library rail, and central statuses. Student plus Grayscale uses the canonical Grayscale Mission filename; another grayscale-presented role retains its own filename and document identity. The file retains inline print CSS and the portable runtime, so response editing/recovery and browser printing work without repository files or preexisting storage.

Print / Save PDF reuses that selected-role serialization boundary to create a temporary same-origin iframe. Its document physically contains only the selected role pages, current edits/responses and presentation settings, exact package CSS, and embedded assets. It excludes all application chrome and authoring controls, forces Page shadow off, waits for load, `document.fonts.ready`, and image decode/load completion, then focuses the iframe and calls that window's `print()`. `afterprint` removes the iframe, with a delayed fallback. The parent editor is never replaced or printed. App-level print CSS separately hides/reset the complete chrome as defensive fallback protection.

The complete portable export reconstructs the shared Role selector because it has no library rail. Its selector contains the four instructional roles plus the shell's All Pages audit view; Grayscale remains a separate toggle.

Exports use browser download blobs and never silently write or overwrite repository paths.

## 6. Accessibility behavior

- The library uses an `aside`, labelled navigation, explicit selector labels, and a role fieldset/legend.
- DOM order is toolbar → library/editor shell → status → open worksheet shadow root. The open root retains normal keyboard focus traversal and a labelled worksheet main landmark; printable page order does not replace DOM reading order.
- Hidden roles receive both `hidden` and `aria-hidden`; only the selected source role remains in the accessibility tree.
- Response fields retain programmatic names, textbox roles, and multiline metadata from the approved source.
- Inactive edit/response nodes use `contenteditable="false"` and `tabindex="-1"`; active nodes use visible focus styles and keyboard reachability.
- Load, local-save, page-fit, and error messages have status/alert semantics. Page fit reads `Pages fit`, `1 page too full`, or `N pages too full`; warning treatment appears only above zero. Live announcements are limited to the three user-relevant state channels.
- Page regions, heading hierarchy, table captions, figure captions/labels, extended descriptions, non-color task/component cues, and selectable text come from the approved Case 03 source and shared shell.
- Application layout adapts at 980 px and 700 px, measures wrapped toolbar height at every viewport, keeps focus visible, and honors reduced-motion preferences.
- Grayscale uses token overrides rather than whole-page filters, retaining selectable text and non-color distinctions.

The interface and documentation repeat the governing warning: browser PDF export does not guarantee PDF accessibility; distribution/publication/archive PDFs need separate verification.

## 7. Validation model

`tests/validate_static.py` retains the 103 accepted Phase 1 static/package assertions for Case 03. `tests/validate_phase2_static.py` adds Case 01/02 schema and semantic package validation, golden/extraction hash checks, task and binding-rule checks, deterministic extraction, the reconciled protected-artifact ledger, and the no-PDF rule.

`tests/run_browser_tests.py` retains every Phase 1 browser assertion and adds repeated Case 01 → Case 02 → Case 03 cycling. It checks exact case labels/order, keyboard and disabled-selector semantics, per-role page fit, Page shadow geometry isolation, all 15 clean print profiles/page counts, first and continuation identity, chrome exclusion, package-specific styles/content/assets, role/edit/response/autosave isolation, output identities, announcements, duplicate light-DOM IDs, and stale Shadow DOM cleanup.

`tests/validate_phase2_parity.py` renders each Case 01/02 maintained master and isolated central worksheet in the same installed browser, viewport, fonts, defaults, role, and grayscale state. Across all 43 role-profile pages it compares DOM structure, task/page assignment, page-relative critical geometry, computed presentation, and page pixels. It also validates current maintained role HTML, current-role export geometry, complete portable export geometry, component containment, all profiles reporting Pages fit, and JavaScript errors. The accepted Case 03 threshold remains a channel delta of 8 and at most 0.05% differing pixels; thresholds were not loosened.

The protected ledger covers masters, current role HTML, controlled sources/assets, manifests, validation/owner records, and every Case 01/02 historical PDF. Validators hash PDFs but never generate, normalize, or inspect/re-save them.

## 8. Phase 2 validation status and limitations

- Nate / Owner accepted the central editor and Case 03 v1.1 proof package in Phase 1. Its package, tests, and approved artifacts remain unchanged except for generic backward-compatible multi-case application/schema support.
- Case 01 v1.1 and Case 02 v1.0 are now discoverable exact migration packages. Their current maintained HTML bytes are owner-authorized Phase 2 goldens, while their earlier physically print-approved bytes/PDFs remain historical evidence.
- Case 01/02 automated parity is a validation result, not owner acceptance. Status remains `VALIDATION_BUILD`; `OWNER_GATE_OPEN` and `PHYSICAL_PRINT_GATE_OPEN` remain open until review of both maintained standalone HTML and central-editor rendering at 100% / Actual Size.
- There is no historical-version browser. Curriculum/campaign selectors remain disabled while only one value exists; the three-value case selector is enabled.
- Recovery state is local to a browser origin/profile, is isolated by curriculum/campaign/case/version, and does not synchronize.
- Trusted repository packages may supply HTML fragments and CSS. The app is not a sandbox for untrusted curriculum packages.
- Embedded case-owned editors remain present. Central-editor cutover, embedded-editor removal, repository cleanup, Case 04, and HHH production are not authorized.
- PDF accessibility is outside this HTML-only implementation.

## 9. Protected history and remaining cutover boundary

`phase2-protected-artifacts.v1.json` freezes Case 01/02 masters, role outputs, controlled sources/assets, manifests, validation/owner records, reconciliation records, and PDFs at the separate reconciliation commit. The generic migration builder verifies each maintained golden, task registry, and controlled-source hash before emitting additive content/CSS/icon/task/package files. It never changes an approved artifact.

Current maintained Case 01/02 standalone HTML remains canonical until the owner closes both Phase 2 gates. The owner must review the maintained standalone pages, central-editor pages, retained master/editor/diff contact sheets, and physical browser output. A later, separately authorized cutover may establish the central editor as canonical; this branch neither performs nor implies that cutover.
