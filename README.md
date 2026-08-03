# SSS-HHH Curriculums

Shared curriculum repository for **Space Sprout Sleuth (SSS)** and **Hunger, Harvest, & History (HHH)**.

Canonical released core Cases 01–05: `APPROVED_STABLE`

SSS Campaign 1 contains seven curriculum-sequenced cases. Cases 01–05 are the released core cases; Case 06 is **First Contact Protocol** (runtime `alien1`), and Case 07 is **The Gift** (runtime `alien2`; source-development label `Case 6b`). Case 07 is the Campaign 1 culmination. Cases 06–07 are not yet implemented or registered in this repository, and Campaign 2 must not begin before both are released unless the owner explicitly redirects the project.

## Canonical production workflow

The registered case package and its package-controlled files are the only active source. For the currently registered SSS Campaign 1 Cases 01–05, launch the central Curriculum Editor from the repository root:

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/>. The editor owns instructional editing, response entry, display settings, role switching, clean browser printing, editable-copy export, and worksheet export.

The four document roles are Student, Teacher, Answer Key, and Accessible. Grayscale is a Boolean display/print/export presentation toggle available for every role. It never changes role identity, page count, autosave scope, or the normal role filename.

Editable copies and role worksheets are generated on demand. PDFs, generated role HTML, editable-copy HTML, validation screenshots, and routine validation output are not committed. Prior release artifacts remain recoverable from Git using each case’s compact `history/release-vX.json` record.

## Architecture

Current cases follow:

```text
case-XX-slug/
├── README.md
├── source/
│   ├── case-package.json
│   ├── content.html
│   ├── presentation.css
│   ├── task-registry.js
│   └── optional referenced source files
├── assets/                  optional and referenced only
└── history/                 APPROVED_STABLE only
    ├── release-vX.json
    └── optional owner-approval record
```

Unreleased native cases require the README and canonical `source/` files but do not receive release history until `APPROVED_STABLE`. Native releases explicitly record when no former generated artifacts ever existed.

Key implementation records:

- Current project state: [`shared/project-management/CURRENT_PROJECT_STATE.md`](shared/project-management/CURRENT_PROJECT_STATE.md)
- `shared/implementation/case-registry.v2.json`
- `shared/implementation/case-package.schema.v2.json`
- `shared/implementation/case-registry.schema.v2.json`
- `shared/implementation/CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md`
- `shared/implementation/REPOSITORY_CURRICULUM_LIBRARY_ARCHITECTURE.md`
- `shared/cleanup/CANONICAL_CASE_STRUCTURE_OWNER_APPROVAL_v1.md`

## Validation

```bash
python3 shared/validation/validate_canonical_case_structure.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/run_browser_tests.py
```

Browser validation renders all role/presentation states and its screenshot smoke check in a temporary directory. A full validation run must not leave generated repository files behind.

## Governing documents

Production work follows the current Curriculum Bible, Visual Style Guide and amendments, repository architecture, package schemas, and case package/history records. Versioned historical documents remain historical context; the canonical case-structure migration record supersedes earlier cleanup proposals without altering their original audit snapshots.
