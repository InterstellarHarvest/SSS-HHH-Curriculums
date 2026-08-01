# SSS/HHH Curriculum Editor

The repository-local Curriculum Editor is the canonical interface for SSS Campaign 1 Cases 01–03. It discovers each case through the v2 registry, loads the native `source/case-package.json`, verifies package-controlled source hashes, and mounts worksheet-only content in an open Shadow DOM.

Status: `IMPLEMENTED · OWNER_GATE_OPEN · CASE04_NOT_STARTED`

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

The package’s `content.html`, `presentation.css`, `task-registry.js`, and referenced assets are canonical. Complete editable documents and role documents are assembled on demand. Old embedded documents and release outputs are absent from the current tree and recoverable through the commands in `history/release-vX.json`.

## Validation

```bash
python3 shared/validation/validate_canonical_case_structure.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/run_browser_tests.py
```

The browser suite covers all 24 case/role/presentation states, role and case switching, Grayscale persistence, response/edit isolation, editable-copy and worksheet exports, isolated print documents, keyboard access, announcements, page fit, identities, and JavaScript errors. Screenshots are temporary; reproduce visual evidence with `run_browser_tests.py`.

The server binds to `127.0.0.1` and serves repository files read-only. Packages are trusted repository content; downloaded editable HTML contains JavaScript and should be treated accordingly.
