# Curriculum Editor Architecture v1.0

**Status:** Phase 1 implementation

**Application:** `apps/curriculum-editor/`

**Proof package:** `SSS-C1-CASE03` v1.0

**Package schema:** `shared/implementation/case-package.schema.v1.json`

## 1. Architecture boundary

The central application owns the library rail, toolbar orchestration, editing state, autosave, overflow reporting, and export assembly. The shared shell remains the canonical source for toolbar markup, worksheet presentation, CER geometry, common components, icons, and established control behavior. The case package owns instructional content, case layout CSS, task definitions, metadata, assets, roles, page counts, and filenames.

```text
case-registry.v1.json
        │ editorPackage
        ▼
Case 03 package ── content / task definitions / case CSS / assets
        │
        ├──────── shared shell toolbar / CSS / CER / icons
        │
        ▼
central Curriculum Editor
        ├── local recovery state (case + version + document key)
        ├── self-contained complete editable HTML
        └── self-contained selected-role HTML
```

The approved `SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html` is not a runtime dependency. It remains a byte-identical parity reference and approved release artifact. The package points directly to the existing Case 03 source fragment, task registry, and case CSS.

## 2. Runtime load sequence

1. `editor-app.js` fetches `shared/implementation/case-registry.v1.json`.
2. It discovers the current Case 03 `editorPackage` path; the existing `master` and `roles` registry paths remain unchanged.
3. It validates supported schema/shell versions and required role/package fields.
4. It fetches every declared shared shell, task, content, style, and source-backed asset path. Missing files fail with a visible load error.
5. It parses the JSON-compatible task-registry assignment and expands each `data-shell-task-heading` placeholder with the canonical Phosphor/task-heading component.
6. It rejects runtime/style/iframe elements in the instructional fragment and verifies persistence IDs and embedded asset selectors.
7. It injects the canonical shared toolbar into the application-owned toolbar host, adds the Phase 1 **Download Current Role** action, and binds every control to one `applyState()` path.
8. It restores local recovery state and announces the loaded case through a polite live region.

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
- accessibility: document language/title, load announcement, extended-description selectors, and the manual-PDF warning.

All package paths are repository-relative, may not traverse upward, and must resolve to files. Grayscale maps to Student source pages because the governing printable-page contract defines grayscale as a production mode rather than a separate instructional role.

Validation rejects unsupported schema versions, missing package/content/style/task files, missing role definitions, invalid task placeholders, invalid source-backed asset paths, and missing embedded asset selectors. The registry schema permits an optional `editorPackage`, allowing approved historical cases to remain registered without pretending they have been migrated.

## 4. Editing and recovery state

One state object controls role, four independent margins, density, edit/fill modes, grayscale, guides, and boundaries. `applyState()` updates body tokens/classes, controls, visible pages, editable nodes, status text, and overflow checks.

- Fill Responses exposes only `[data-response]` and supported ordinary form fields on the selected source role.
- Edit Text additionally exposes `[data-editable]` nodes. Structural attributes, IDs, task keys, role boundaries, and component metadata are never editable.
- Input saves by stable `data-persist-id` under `curriculum-editor:<documentKey>:content`.
- State saves under `curriculum-editor:<documentKey>:state`.
- Role switching does not reconstruct pages. Student and Accessible response IDs remain independent; Teacher/Answer instructional boundaries remain isolated by page role.
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

Selected-role serialization filters the clone to that role's source pages, applies the grayscale flag where required, and omits the toolbar, library rail, and central statuses. It retains inline print CSS and the portable runtime, so response editing/recovery and browser printing work without repository files or preexisting storage.

Exports use browser download blobs and never silently write or overwrite repository paths.

## 6. Accessibility behavior

- The library uses an `aside`, labelled navigation, explicit selector labels, and a role fieldset/legend.
- DOM order is toolbar → library/editor shell → status → worksheet pages; printable visual page order does not replace DOM reading order.
- Hidden roles receive both `hidden` and `aria-hidden`; only the selected source role remains in the accessibility tree.
- Response fields retain programmatic names, textbox roles, and multiline metadata from the approved source.
- Inactive edit/response nodes use `contenteditable="false"` and `tabindex="-1"`; active nodes use visible focus styles and keyboard reachability.
- Load, local-save, overflow, and error messages have status/alert semantics. Live announcements are limited to the three user-relevant state channels.
- Page regions, heading hierarchy, table captions, figure captions/labels, extended descriptions, non-color task/component cues, and selectable text come from the approved Case 03 source and shared shell.
- Application layout adapts at 980 px and 700 px, focus is visible, and reduced-motion preferences disable transitions/animation.
- Grayscale uses token overrides rather than whole-page filters, retaining selectable text and non-color distinctions.

The interface and documentation repeat the governing warning: browser PDF export does not guarantee PDF accessibility; distribution/publication/archive PDFs need separate verification.

## 7. Validation model

`tests/validate_static.py` is a zero-write validator. It checks both JSON schemas, semantic package references, required negative failure cases, task/component/accessibility structure, page-count contracts, approved Case 03 manifest hashes, Case 01/02 Git protection, and absence of PDF work.

`tests/run_browser_tests.py` starts an ephemeral local server and installed headless Chrome. Its in-browser harness checks exact control order/count, five-role isolation and page counts, response/text modes, independent margins and other layout controls, print-preview events, role-specific clear/reset, autosave reload, complete serialization, fresh-context behavior, current-role export, semantic components, zero overflow, and a temporary rendered screenshot. Test profiles and screenshots are created outside the repository and discarded.

No validator generates or inspects PDFs.

## 8. Known limitations

- Phase 1 supports only the current Case 03 package. There is no historical-version browser.
- The selectors reflect the normal Curriculum → Campaign → Case → Role path; single available values are disabled to avoid suggesting unavailable cases.
- Recovery state is local to a browser origin/profile and does not synchronize.
- Trusted repository packages may supply HTML fragments and CSS. The app is not a sandbox for untrusted curriculum packages.
- Browser and physical print results remain subject to owner testing at 100% / Actual Size.
- PDF accessibility is outside this HTML-only implementation.

## 9. Phase 2 migration plan — not executed

Cases 01 and 02 must be migrated independently and additively:

1. Inventory each approved master, role output, source file, task mapping, visual differences, and release checksum record.
2. Freeze and verify every historical approved master, role HTML, and retained PDF hash before package work.
3. Extract or author a case-owned instructional fragment, task registry, case CSS, asset inventory, role/page mapping, and package JSON without editing the approved master or outputs.
4. Resolve legacy behavior through package adapters or an explicitly versioned shared-shell successor; do not silently rewrite shell v1.0 or copy a full editor into the package.
5. Run the same negative package tests, role/edit/autosave/export tests, accessibility checks, page-count/overflow review, and browser screenshots for that case.
6. Add only the `editorPackage` reference to its existing registry entry. Preserve its `master`, `roles`, version, status, and historical-PDF policy paths.
7. Re-verify all frozen hashes, conduct owner browser/physical review, and merge each migration through a separate reviewed change.

Historical masters are retained as release records and parity references. Deletion or replacement is not part of Phase 2 unless a later owner-approved preservation policy explicitly authorizes it.
