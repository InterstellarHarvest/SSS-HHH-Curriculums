# SSS/HHH Curriculum Editor

The repository-local Curriculum Editor is the canonical interface for SSS Campaign 1 Cases 01–05. It discovers each case through the v2 registry, loads the native `source/case-package.json`, verifies package-controlled source hashes, and mounts worksheet-only content in an open Shadow DOM.

Status: mixed lifecycle; read each package/registry entry for current approval state.

## Launch

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/>. `file://` is unsupported because package resources are fetched independently.

## Roles and Grayscale

The only document roles are Student, Teacher, Answer Key, and Accessible. The library rail and portable editable-copy selector expose those four roles; the portable selector also includes an All Pages editing view.

Grayscale is an independent Boolean presentation toggle. It changes presentation tokens for the selected role without changing that role’s identity, page count, content, response geometry, semantic markup, or autosave namespace. Printing and worksheet export apply the current Grayscale state while retaining the role’s normal filename and identity.

## Editing and exports

- **Download Editable Copy** creates a self-contained HTML copy with all four roles, the editing toolbar, current edits/responses, and the current Grayscale state.
- **Download Worksheet** creates a self-contained HTML worksheet containing only the selected role, current edits/responses, and current Grayscale state. It has no toolbar or application chrome.
- **Print / Save PDF** builds a temporary same-origin print document for the selected role, waits for fonts and images, removes application chrome and page shadows, and opens the browser print dialog.
- **Clear Responses** affects only the selected role’s response fields.
- **Reset This Case** affects only the loaded case/version recovery state.

Generated HTML and PDFs are not written into the repository. A browser-created PDF requires separate accessibility verification before distribution.

## Source and recovery model

The package’s `content.html`, `presentation.css`, `task-registry.js`, `layout-overrides.json`, and referenced assets are canonical. The central shell applies `protected-printable-components.css` after case presentation so identification rows, title and continuation headers, institutional identity, footers, and CER keep one printable contract. New packages opt into the shared component layer and may not redefine protected selectors. Complete editable documents and role documents are assembled on demand. Historical generated artifacts, when they existed, remain recoverable through `history/release-vX.json`; native-only releases record that no former generated artifacts exist.

## Accessible vertical response-area authoring

Each SSS or HHH package must declare `source/layout-overrides.json` using `layout-overrides.schema.v1.json`. Its `areas` list is an explicit allowlist of stable Accessible edition response IDs; compact labels, classifications, criteria/constraints, and CER fields do not belong in it. `overrides` remains a sorted sparse map containing only owner-applied heights. An empty map changes no worksheet geometry.

In Accessible Edit Text mode, eligible fields receive vertical-only pointer and keyboard handles. Values snap to 4px, respect declared bounds, and receive live page-fit/footer safety validation. Pending changes are browser drafts isolated by repository/worktree identity, case, edition, and the content/presentation/layout source hashes. Undo, redo, Reset Area, Reset Page, stale-draft inspect/export/discard, and **Export Layout Changes** do not write repository files. Normal editable-copy, worksheet, print, and PDF pathways omit authoring controls and unapproved draft heights.

**Apply to Source** shows the exact selected changes and requires confirmation. The loopback service accepts only registered Accessible allowlist IDs with matching source-hash preconditions. It independently rejects CER/non-Accessible targets and unknown fields, writes only the sparse layout file plus its package hash, runs focused validation, and rolls both files back on failure. It accepts no client filesystem path. Successful changes intentionally remain uncommitted for owner inspection.

## Validation

```bash
python3 shared/validation/validate_canonical_case_structure.py
python3 shared/validation/validate_layout_overrides.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/test_authoring_service.py
python3 apps/curriculum-editor/tests/run_browser_tests.py
```

The browser suite covers all 40 case/role/presentation states, role and case switching, Grayscale persistence, response/edit isolation, editable-copy and worksheet exports, isolated print documents, keyboard access, announcements, page fit, protected-component and CER geometry, identities, and JavaScript errors. Static validation rejects protected selectors in new case presentation stylesheets. Screenshots are temporary; reproduce visual evidence with `run_browser_tests.py`.

The server binds to `127.0.0.1` by default. Static reads remain repository-root scoped; its authoring endpoints are loopback-only and the apply endpoint has the strict contract described above. Packages are trusted repository content; downloaded editable HTML contains JavaScript and should be treated accordingly.
