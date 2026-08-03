# SSS/HHH Current Project State

Project state content verified from curriculum repository baseline
`b07b2f8e36871f15d14e6c012e0eb55398d43dc4`

Last updated: 2026-08-03

## Purpose and authority

This document is the current operational handoff for project-management and production conversations. Repository sources, governing documents, schemas, and release records remain authoritative. Update this handoff only at meaningful merged milestones. The recorded SHA identifies the repository state used to verify the handoff contents; it is not intended to identify the commit containing this document. Every new conversation must independently fetch the repository and verify live main before relying on this handoff.

This document does not replace Git history, case release histories, governing curriculum documents, or other authoritative repository records. It is not a running development diary or a record of speculative plans and stale branches.

## Repository

Curriculum repository:

- <https://github.com/InterstellarHarvest/SSS-HHH-Curriculums>

Related game repositories:

- <https://github.com/InterstellarHarvest/Space-Sprout-Sleuth>
- <https://github.com/InterstellarHarvest/Hunger-Harvest-History>

Verified project-state baseline:
`b07b2f8e36871f15d14e6c012e0eb55398d43dc4`

The live main branch may be newer because this handoff is itself committed after the baseline it documents. Always fetch the repository and resolve the current main SHA before beginning work.

Frozen Case 06 game-source baseline: `a7a725121f261373df32a5366c70e7df73ddf8f3`

No production branches are intentionally active at this checkpoint.

## Approved curriculum releases

| Curriculum | Campaign | Case | Title | Version | Student | Teacher | Answer Key | Accessible | Status |
|---|---:|---:|---|---:|---:|---:|---:|---:|---|
| SSS | 1 | 01 | ISS Greenhouse Module | 1.1 | 3 | 7 | 3 | 6 | APPROVED_STABLE |
| SSS | 1 | 02 | Lunar Greenhouse | 1.0 | 3 | 7 | 3 | 7 | APPROVED_STABLE |
| SSS | 1 | 03 | Mars Habitat | 1.1 | 4 | 8 | 4 | 7 | APPROVED_STABLE |
| SSS | 1 | 04 | Hayes Orbital Station | 1.0 | 4 | 7 | 4 | 7 | APPROVED_STABLE |
| SSS | 1 | 05 | Sub Surface Bunker | 1.0 | 4 | 8 | 4 | 7 | APPROVED_STABLE |

Cases 01–05 are the five released core cases and the approved production baseline. SSS Campaign 1 contains seven curriculum-sequenced cases and is not complete: Case 06 is **First Contact Protocol** (runtime `alien1`), and Case 07 is **The Gift** (runtime `alien2`; source-development label `Case 6b`). Case 07 is the Campaign 1 culmination. Cases 04 and 05 were produced natively through the mature canonical workflow. All five released Accessible editions use content-driven page counts and dedicated canonical CER pages; Student, Teacher, and Answer Key page counts remain fixed.

## Canonical case structure

```text
case-XX-slug/
├── README.md
├── source/
│   ├── case-package.json
│   ├── content.html
│   ├── presentation.css
│   ├── task-registry.js
│   └── optional referenced source files
├── assets/                     optional and referenced only
└── history/                    APPROVED_STABLE only
    ├── release-vX.json
    └── optional owner-approval record
```

Draft cases contain a README and canonical source files. Approved releases require release history. Generated HTML, editable masters, role exports, PDFs, screenshots, and validation evidence are temporary and are not committed.

## Canonical roles and presentation

The only curriculum document roles are:

- Student
- Teacher
- Answer Key
- Accessible

Grayscale is a Boolean presentation toggle, never:

- a role;
- a document type;
- a separate output;
- an additional page count.

## Release lifecycle

```text
DRAFT
→ VALIDATION_BUILD
→ OWNER_GATE_OPEN
→ APPROVED_STABLE
```

Owner review and print acceptance are required before approval. Release history is created only when a case becomes `APPROVED_STABLE`. Approval and repository workflow metadata must never appear on printable classroom pages.

## Protected shared components

The shared system owns these components, and case-specific CSS may not redefine them:

- Student and Accessible Name / Date / Period row
- first-page mission title block
- SAA insignia and institutional lockup
- continuation-page header
- publication footer
- canonical CER

A new case changes the text and case content, not the geometry or visual implementation of these components.

The subtitle convention is:

`Campaign # · Case # · Location`

When a location has two related parts, separate those parts with a comma rather than another middle dot.

Example: `Campaign 1 · Case 04 · L2 Lagrange Point, Orbital Research Station`

## Editor and publishing rules

- The central Curriculum Editor is the canonical production interface.
- Student and Accessible response-height authoring is constrained to explicit eligible areas; every other Student and Accessible response area is explicitly locked.
- Accessible page counts are content-driven, normally one to three complete tasks per page, with dedicated near-full-page CER treatment.
- Student and Accessible vertical resizing use the released source-controlled authoring workflow; no redesign is authorized.
- Worksheet pages remain fixed at Letter geometry at all editor viewport widths.
- Narrow screens use horizontal worksheet scrolling rather than page shrinkage.
- Page size is 816 × 1056 CSS pixels.
- Page frame is 720 × 960 CSS pixels with 48-pixel insets.
- Editor-only geometry rules do not enter exports or print.
- Role exports and editable copies are generated on demand.
- Isolated printing excludes editor chrome.
- Browser PDFs require separate accessibility verification.

## Printable-content integrity

Printable roles and exports may not contain:

- lifecycle tokens;
- owner-review status;
- validation status;
- branch names;
- commit hashes;
- merge instructions;
- repository-maintenance language;
- visible production-status banners.

Internal status remains in the package, registry, release history, owner-approval records, and editor chrome only.

## Current validation baseline

Accepted validation state at current main:

- canonical structure: PASS
- static validation: 228/228
- browser validation: 823/823 across all 40 case/role/presentation states
- browser-PDF pagination validation: 122/122
- role/presentation matrix: 40/40
- layout contracts: Accessible 54 eligible and 86 explicitly locked response areas; Student 37 eligible and 112 explicitly locked response areas
- authoring/security validation: 13/13
- JavaScript runtime errors: 0
- all current page counts and page-fit checks: PASS
- protected printable components: PASS
- fixed editor geometry at wide and narrow widths: PASS
- exports and isolated printing: PASS
- printable production-metadata guard: PASS

These totals are checkpoint values and may legitimately increase when new cases or validations are added.

## Governing sources

Use these authoritative source categories without treating this index as a duplicate of their contents:

- Shared curriculum bible and its named controlling approved amendments: [`shared/curriculum-bible/SSS_HHH_CURRICULUM_BIBLE_v1.3.md`](../curriculum-bible/SSS_HHH_CURRICULUM_BIBLE_v1.3.md).
- SSS curriculum blueprint and audit: [`sss/blueprint/SSS_CURRICULUM_BLUEPRINT_v1.0.md`](../../sss/blueprint/SSS_CURRICULUM_BLUEPRINT_v1.0.md) and [`sss/audit/SSS_MASTER_AUDIT_v1.0.md`](../../sss/audit/SSS_MASTER_AUDIT_v1.0.md).
- Visual style guide and amendments: [`shared/visual-style-guide/VISUAL_STYLE_GUIDE_v1.0.md`](../visual-style-guide/VISUAL_STYLE_GUIDE_v1.0.md) and [`shared/visual-style-guide/amendments/`](../visual-style-guide/amendments/).
- Shared implementation architecture and schemas: [`shared/implementation/REPOSITORY_CURRICULUM_LIBRARY_ARCHITECTURE.md`](../implementation/REPOSITORY_CURRICULUM_LIBRARY_ARCHITECTURE.md), [`shared/implementation/CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md`](../implementation/CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md), [`shared/implementation/case-package.schema.v2.json`](../implementation/case-package.schema.v2.json), [`shared/implementation/case-registry.schema.v2.json`](../implementation/case-registry.schema.v2.json), and [`shared/implementation/case-release-history.schema.v1.json`](../implementation/case-release-history.schema.v1.json).
- Central editor and validation suites: [`apps/curriculum-editor/`](../../apps/curriculum-editor/) and [`shared/validation/`](../validation/).
- Each case’s package, task registry, README, and release history: [`sss/campaign-1/`](../../sss/campaign-1/), indexed by [`shared/implementation/case-registry.v2.json`](../implementation/case-registry.v2.json).

## Production workflow for a new case

1. Verify current main and related game baseline.
2. Conduct read-only game and curriculum discovery.
3. Resolve owner design decisions.
4. Correct material game-science wording first when necessary.
5. Create an isolated curriculum feature branch.
6. Implement the native draft without release history.
7. Run complete validation.
8. Conduct visual and instructional owner review.
9. Correct draft findings without weakening shared contracts.
10. Promote to `APPROVED_STABLE` and create release history.
11. Verify branch ancestry and fast-forward merge.
12. Delete completed branches.

## Conversation and responsibility model

- Use one PMO conversation per campaign or meaningful campaign phase.
- Use one implementation conversation per case.
- Use separate conversations and branches for shared editor, schema, validator, or publishing changes.
- Close a case implementation conversation after its approved merge.
- Begin new conversations from this file plus current repository verification.

Conversational memory is helpful context but is not the authoritative project record.

## Next phase

SSS Campaign 1 contains seven curriculum-sequenced cases. Cases 01–05 are the released core cases. Cases 06–07 are the two first-contact bonus cases and remain unreleased.

Next production target: **SSS Campaign 1 · Case 06 — First Contact Protocol** (runtime `alien1`)

Case 07 — **The Gift** (runtime `alien2`; source-development label `Case 6b`) follows Case 06 and is the Campaign 1 culmination. Do not begin Campaign 2 before Cases 06 and 07 are released unless the owner explicitly redirects the project. Case 06 implementation begins only in its authorized production workflow and remains governed by `SSS_CURRICULUM_BLUEPRINT_v1.0.md`; this sequencing correction does not redesign that plan.

## Update policy

Update `CURRENT_PROJECT_STATE.md` only when one of these occurs:

- an approved case is merged;
- a campaign boundary is reached;
- the canonical production architecture changes;
- lifecycle, role, publishing, or validation rules change;
- a new repository becomes authoritative;
- the next production target changes.

Every update must:

- record the verified repository baseline used to prepare the state update;
- update the date;
- remove completed branch information;
- distinguish current facts from future work;
- remain concise enough to read at the beginning of a new conversation.
