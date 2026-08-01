# Curriculum Editor Architecture v1.0

**Status:** Phase 1 accepted · owner review PASS · ready to merge

**Application:** `apps/curriculum-editor/`

**Proof package:** `SSS-C1-CASE03` v1.1

**Package schema:** `shared/implementation/case-package.schema.v1.json`

## 1. Architecture boundary

The central application owns the library rail, toolbar orchestration, editing state, autosave, overflow reporting, presentation isolation, and export assembly. The shared shell remains the canonical source for toolbar markup, CER geometry, common components, icons, and established control behavior. The case package owns the hash-verified worksheet-only DOM and presentation CSS, task definitions, metadata, assets, roles, page counts, and filenames.

```text
case-registry.v1.json
        │ editorPackage
        ▼
Case 03 package ── extracted content / exact presentation CSS / hashes
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
2. It discovers the current Case 03 v1.1 `editorPackage`; the registry retains v1.0 under historical-release metadata.
3. It validates supported schema/shell versions and required role/package fields.
4. It fetches every declared shared shell, task, extracted content, presentation stylesheet, and source-backed asset path, then verifies the package content, case CSS, and presentation SHA-256 values before mounting.
5. It parses the task registry and validates/expands any declared task-heading placeholder; the v1.1 extraction already contains the exact expanded master headings.
6. It rejects runtime/style/iframe elements in the instructional fragment and verifies persistence IDs and embedded asset selectors.
7. It mounts the exact worksheet presentation in an open Shadow DOM. The app CSS cannot select worksheet descendants, and the scoped worksheet CSS cannot select application chrome. The application-owned toolbar remains outside the shadow root, removes the duplicate Role selector, and controls the isolated document through the same state path.
8. It restores local recovery state and announces the loaded case through a polite live region.

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
- defaults: role, edit/fill modes, four margins, density, grayscale, guides, and boundaries;
- accessibility: document language/title, load announcement, extended-description selectors, and the manual-PDF warning;
- approval: date, tester, owner-review and browser physical-print results, scale, printer/paper record, and artifact policy;
- migration provenance: historical/successor master paths and hashes, reconciliation reason, and deterministic builder;
- presentation: extracted content/case/presentation hashes and required isolation mode.

All package paths are repository-relative, may not traverse upward, and must resolve to files. The package retains a Grayscale output profile mapped to Student source pages for export compatibility. Central navigation exposes only Student, Teacher, Answer Key, and Accessible; Grayscale is an independent presentation modifier.

Validation rejects unsupported schema versions, missing package/content/style/task files, missing role definitions, invalid task placeholders, invalid source-backed asset paths, and missing embedded asset selectors. The registry schema permits an optional `editorPackage`, allowing approved historical cases to remain registered without pretending they have been migrated.

## 4. Editing and recovery state

One state object controls role, four independent margins, density, edit/fill modes, grayscale, guides, and boundaries. `applyState()` mirrors relevant tokens onto the application body and the isolated worksheet-document root, then updates controls, visible pages, editable nodes, status text, and overflow checks.

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
- Case 03 CSS;
- Phosphor symbols and inline insignia/figures;
- all role pages and current instructional/response content;
- toolbar markup and current state;
- a standalone portable runtime and package/output configuration.

The exported file receives a derived document key, so it cannot collide with the central app or another export. In a fresh context, the embedded DOM supplies its instructional Reset Source baseline. Responses open with their embedded values but are cleared by Reset Source, matching shared-shell v1.0 behavior.

Selected-role serialization filters the clone to that role's source pages, applies the current Grayscale modifier, and omits the toolbar, library rail, and central statuses. Student plus Grayscale uses the canonical Grayscale Mission filename; another grayscale-presented role retains its own filename and document identity. The file retains inline print CSS and the portable runtime, so response editing/recovery and browser printing work without repository files or preexisting storage.

The complete portable export reconstructs the shared Role selector because it has no library rail. Its selector contains the four instructional roles plus the shell's All Pages audit view; Grayscale remains a separate toggle.

Exports use browser download blobs and never silently write or overwrite repository paths.

## 6. Accessibility behavior

- The library uses an `aside`, labelled navigation, explicit selector labels, and a role fieldset/legend.
- DOM order is toolbar → library/editor shell → status → open worksheet shadow root. The open root retains normal keyboard focus traversal and a labelled worksheet main landmark; printable page order does not replace DOM reading order.
- Hidden roles receive both `hidden` and `aria-hidden`; only the selected source role remains in the accessibility tree.
- Response fields retain programmatic names, textbox roles, and multiline metadata from the approved source.
- Inactive edit/response nodes use `contenteditable="false"` and `tabindex="-1"`; active nodes use visible focus styles and keyboard reachability.
- Load, local-save, overflow, and error messages have status/alert semantics. Live announcements are limited to the three user-relevant state channels.
- Page regions, heading hierarchy, table captions, figure captions/labels, extended descriptions, non-color task/component cues, and selectable text come from the approved Case 03 source and shared shell.
- Application layout adapts at 980 px and 700 px, measures wrapped toolbar height at every viewport, keeps focus visible, and honors reduced-motion preferences.
- Grayscale uses token overrides rather than whole-page filters, retaining selectable text and non-color distinctions.

The interface and documentation repeat the governing warning: browser PDF export does not guarantee PDF accessibility; distribution/publication/archive PDFs need separate verification.

## 7. Validation model

`tests/validate_static.py` checks both JSON schemas, semantic package references, required negative failure cases, task/component/accessibility structure, atomic CER authorship, the 4/8/4/7/4 page-count contract, deterministic rebuilding, v1.0 preservation, v1.1 manifest hashes, Case 01/02 Git protection, and absence of PDF work.

`tests/run_browser_tests.py` starts an ephemeral local server and installed headless Chrome. Its in-browser harness checks exact control order/count, four-role navigation plus Student Grayscale, responsive toolbar/layout alignment at 1440/1100/820/640 px, response/text modes, independent margins and other layout controls, print-preview events, role-specific clear/reset, autosave reload, complete serialization, fresh-context behavior, current-role export, semantic components, zero overflow, and a temporary rendered screenshot. Test profiles and temporary smoke screenshots are discarded; the requested owner-review 1440×1200 capture is retained under `tests/screenshots/`.

`tests/validate_v1_1_parity.py` renders the v1.1 master and isolated central worksheet in the same installed browser, viewport, fonts, defaults, role, and grayscale state. For all 27 role-profile pages it compares DOM/page assignment, normalized critical geometry, computed presentation, and page pixels; it also validates independent v1.1 role files, current-role export geometry, zero overflow, and CER page-frame containment. Pixel comparison ignores channel deltas up to 8 and permits at most 0.05% differing page pixels for SVG/text antialiasing. Owner visual review of the retained master/editor/diff contact sheets remains a required migration gate.

No validator generates or inspects PDFs.

## 8. Phase 1 acceptance and known limitations

- Nate / Owner accepted the central editor and Case 03 v1.1 proof package on 2026-07-31. Exact structural, page-assignment, geometry, computed-presentation, rendered, portable-export, current-role export, accessibility, zero-overflow, and browser physical-print gates pass.
- Phase 1 supports only the current approved Case 03 v1.1 package. There is no historical-version browser.
- The selectors reflect the normal Curriculum → Campaign → Case → Role path; single available values are disabled to avoid suggesting unavailable cases.
- Recovery state is local to a browser origin/profile and does not synchronize.
- Trusted repository packages may supply HTML fragments and CSS. The app is not a sandbox for untrusted curriculum packages.
- Cases 01 and 02 remain unmigrated. Embedded editors must not yet be stripped from Cases 01–03.
- Case 03 v1.1 proves the central architecture, but the central editor becomes fully canonical only after Phase 2 parity and owner-approved cutover.
- PDF accessibility is outside this HTML-only implementation.

## 9. Phase 2 migration plan — not executed

Cases 01 and 02 must be migrated independently and additively:

1. Inventory each approved master, role output, source file, task mapping, visual differences, and release checksum record.
2. Freeze and verify every historical approved master, role HTML, and retained PDF hash before package work.
3. Treat the approved master as the golden migration reference. Verify its hash, deterministically extract/reconcile a worksheet-only DOM and exact presentation CSS, and record all source/presentation hashes without editing the approved master or outputs.
4. Resolve legacy behavior through package adapters or an explicitly versioned shared-shell successor; do not silently rewrite shell v1.0 or copy a full editor into the package.
5. Isolate worksheet presentation from application CSS. Prove structural, page-assignment, geometry, computed-style, and rendered parity in addition to role/edit/autosave/export, accessibility, page-count, and overflow behavior. CER and other atomic components must remain wholly inside one page; page counts alone are insufficient.
6. Add only the `editorPackage` reference to its existing registry entry. Preserve its `master`, `roles`, version, status, and historical-PDF policy paths.
7. Re-verify all frozen hashes, conduct owner browser and physical-print review, and merge each migration through a separate reviewed change. Owner visual review is a mandatory migration gate.

Historical masters are retained as release records and parity references. Deletion or replacement is not part of Phase 2 unless a later owner-approved preservation policy explicitly authorizes it.

Phase 2 migrations are additive. Until both Case 01 and Case 02 pass independent parity and cutover review, all embedded Case 01–03 editors remain in place.
