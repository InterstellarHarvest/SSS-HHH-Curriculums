# SSS-HHH Curriculums

Shared curriculum repository for **Space Sprout Sleuth (SSS)** and **Hunger, Harvest, & History (HHH)**.

Canonical released SSS Campaign 1 Cases 01–07 and Campaign 2 Cases 01–06: `APPROVED_STABLE`

SSS Campaign 1 contains seven released curriculum-sequenced cases. Cases 01–05 are the five core cases. Case 06, **First Contact Protocol** (runtime `alien1`), is the first-contact bonus case. Case 07, **The Gift** (runtime `alien2`; former source-development label `Case 6b`), is the approved Campaign 1 culmination.

SSS Campaign 2 is complete. All six cases are produced, owner-approved, print-approved and released. Each was reissued as a corrective v1.1 following the Campaign 2 completion audit; both the v1.0 and v1.1 records are retained, and the v1.0 records are unmodified. Case 03, **The Wrong Color of Light** (runtime `wrong_color_light`), was the first produced Campaign 2 package; it keeps its runtime case number and is not renumbered as Campaign 2 Case 01.

| Case | Title | Version | Student | Teacher | Answer Key | Accessible |
|---:|---|---:|---:|---:|---:|---:|
| 01 | Heavy Hands | 1.1 | 5 | 9 | 4 | 8 |
| 02 | The Missing Dance | 1.1 | 6 | 8 | 4 | 8 |
| 03 | The Wrong Color of Light | 1.1 | 5 | 8 | 4 | 8 |
| 04 | The Silent Grove | 1.1 | 6 | 8 | 4 | 8 |
| 05 | Too Clean a Room | 1.1 | 7 | 9 | 5 | 7 |
| 06 | The First Garden | 1.1 | 6 | 8 | 5 | 7 |

The registry holds thirteen cases across two campaigns, which is 104 case/role/presentation states.

## Canonical production workflow

The registered case package and its package-controlled files are the only active source. For the currently registered SSS cases, launch the central Curriculum Editor from the repository root:

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/>. The Curriculum, Campaign, and Case selectors are scoped: the Case menu lists exactly the cases registered under the selected campaign. The editor owns instructional editing, response entry, display settings, role switching, clean browser printing, editable-copy export, and worksheet export.

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
python3 shared/validation/validate_release_integrity.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/run_browser_tests.py
python3 apps/curriculum-editor/tests/run_pdf_tests.py
```

`validate_static.py` chains the canonical-structure, release-integrity and layout-override validators, the six Campaign 2 case validators and mutation suites, the corrective-release lifecycle tests, and the authoring-service tests, so running it alone covers the first two commands above. The browser and PDF suites are separate because both require installed Google Chrome.

`validate_release_integrity.py` proves that every approved release's `canonicalSourceApprovalCommit` really contains the source blobs its record certifies. Several historical releases shipped with a pin that did not, because every other validator compared the record to the package and never the record to the commit.

Browser validation renders all role/presentation states and its screenshot smoke check in a temporary directory. PDF validation generates print documents for the registry-derived case editions. A full validation run must not leave generated repository files behind.

Retired validators are recorded in [`shared/validation/RETIRED_VALIDATORS.md`](shared/validation/RETIRED_VALIDATORS.md), which states why each was retired and how to recover it from Git.

## Governing documents

Production work follows the current Curriculum Bible, Visual Style Guide and amendments, repository architecture, package schemas, and case package/history records. Versioned historical documents remain historical context; the canonical case-structure migration record supersedes earlier cleanup proposals without altering their original audit snapshots.
