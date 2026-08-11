# SSS/HHH Current Project State

Project state content verified from curriculum repository baseline
`105467f997b1425b7f40e8150749c70e09ed4771` (the visual-modernization closeout), with the
thirteen-case final system release prepared on `release/sss-final-system` and held unpushed.

Last updated: 2026-08-11

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
`81eef7067268865fec368f50db2d363e0354ae1a`

The live main branch may be newer because this handoff is itself committed after the baseline it documents. Always fetch the repository and resolve the current main SHA before beginning work.

Frozen Case 06 game-source baseline: `d723fb9b8085905a6048575a2cb3bb0fce1d312b`

Frozen Case 07 game-source baseline: `a813c209dfde00634103f74d6673e7d4433e0e63`

Frozen Campaign 2 game-source baseline: `46b9387bca95736f164f905596e3dd8b13968661`

## Approved curriculum releases

| Curriculum | Campaign | Case | Title | Version | Student | Teacher | Answer Key | Accessible | Status |
|---|---:|---:|---|---:|---:|---:|---:|---:|---|
| SSS | 1 | 01 | ISS Greenhouse Module | 1.2 | 3 | 8 | 3 | 6 | APPROVED_STABLE |
| SSS | 1 | 02 | Lunar Greenhouse | 1.1 | 3 | 7 | 3 | 7 | APPROVED_STABLE |
| SSS | 1 | 03 | Mars Habitat | 1.2 | 4 | 8 | 4 | 7 | APPROVED_STABLE |
| SSS | 1 | 04 | Hayes Orbital Station | 1.1 | 4 | 7 | 4 | 7 | APPROVED_STABLE |
| SSS | 1 | 05 | Sub Surface Bunker | 1.1 | 4 | 8 | 4 | 7 | APPROVED_STABLE |
| SSS | 1 | 06 | First Contact Protocol | 1.1 | 5 | 8 | 5 | 7 | APPROVED_STABLE |
| SSS | 1 | 07 | The Gift | 1.1 | 6 | 8 | 6 | 8 | APPROVED_STABLE |
| SSS | 2 | 01 | Heavy Hands | 1.2 | 5 | 9 | 4 | 8 | APPROVED_STABLE |
| SSS | 2 | 02 | The Missing Dance | 1.2 | 6 | 8 | 4 | 8 | APPROVED_STABLE |
| SSS | 2 | 03 | The Wrong Color of Light | 1.2 | 5 | 8 | 4 | 8 | APPROVED_STABLE |
| SSS | 2 | 04 | The Silent Grove | 1.2 | 6 | 8 | 4 | 8 | APPROVED_STABLE |
| SSS | 2 | 05 | Too Clean a Room | 1.2 | 7 | 9 | 5 | 7 | APPROVED_STABLE |
| SSS | 2 | 06 | The First Garden | 1.2 | 6 | 7 | 5 | 7 | APPROVED_STABLE |

Cases 01–05 are the five released core cases. Case 06, **First Contact Protocol** (runtime `alien1`), is the first released first-contact bonus case. Case 07, **The Gift** (runtime `alien2`; former source-development label `Case 6b`), is the released Campaign 1 culmination. Cases 04–07 were produced natively through the mature canonical workflow. All registered Accessible editions use content-driven page counts and dedicated canonical CER pages; Student, Teacher, and Answer Key page counts remain fixed. The seven-case Campaign 1 curriculum sequence is approved and released.

Campaign 2 curriculum production is complete. All six cases are produced, owner-approved, print-approved and released, and were produced against the frozen Campaign 2 game-source baseline `46b9387bca95736f164f905596e3dd8b13968661`. Case 03, **The Wrong Color of Light** (runtime `wrong_color_light`), was produced first; it remains Campaign 2 Case 03 and is not renumbered as Campaign 2 Case 01.

Every Campaign 2 case was reissued as a corrective v1.1, and every case in both campaigns has since been reissued again by the final system release following the Campaign 2 completion audit. Each package retains both its v1.0 and v1.1 release and owner-approval records; the v1.0 records are unmodified and are indexed inside the v1.1 record as prior approved releases.

Accepted curriculum release commits for the current Campaign 2 v1.1 releases:

| Case | Release commit |
|---:|---|
| 01 | `8ab60f3ad29d84bdc72e4197503315bba477f750` |
| 02 | `43858eaad10bd5e5645624d46e851cf6f56dd57d` |
| 03 | `2d4a62eaf39458755b4ee0751bb8225bd219f105` |
| 04 | `3fe64b9c9854d7f357fe0f89410f77a1d00c8177` |
| 05 | `7c69585eff2bb2f40f8d307b45472bcc225260f1` |
| 06 | `f3e3ed7fefb375a97594be99d9744fff4d8f6f0b` |

The thirteen registered cases are 104 case/role/presentation states.

**Package `location` convention.** Campaign 2 Cases 01–05 record the runtime *investigation* name in `location`; Case 06 records the runtime *location*. Both readings are internally consistent, each case validator encodes its own, and no active contract depends on the distinction. The divergence is documented rather than normalized.

The central editor library is campaign-scoped: the Curriculum selector controls the available campaigns and the Campaign selector controls the Case menu, which lists exactly the cases registered under the selected campaign.

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

Case 07 approved stable-release state:

- canonical structure: PASS
- static validation: 358/358 in the approved release state
- browser validation: 1090/1090 across all 56 case/role/presentation states
- browser-PDF pagination validation: 170/170
- role/presentation matrix: 56/56
- layout contracts: Accessible 94 eligible and 115 explicitly locked response areas; Student 56 eligible and 161 explicitly locked response areas
- authoring/security validation: 13/13
- JavaScript runtime errors: 0
- all current page counts and page-fit checks: PASS
- Case 07 manual print-media visual inspection: 28/28 pages
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

SSS Campaign 1 contains seven released curriculum-sequenced cases. Cases 01–05 are the five core cases; Case 06 — **First Contact Protocol** (runtime `alien1`) — is the first-contact bonus case; and Case 07 — **The Gift** (runtime `alien2`; former source-development label `Case 6b`) — is the approved culmination.

Next authorized production target: **None recorded**

Campaign 2 is complete and frozen at six released cases. Producing any further SSS case, or any HHH case, requires separate owner authorization.

The outstanding curriculum work of record is the unified SSS Campaign 1 + Campaign 2 post-finalization quality audit. No broad curriculum-quality, Accessible-differentiation, Teacher Edition, Answer Key, standards or visual review has been performed since the Campaign 2 completion audit; the Campaign 2 finalization pass was mechanical maintenance only. Issues it deferred to that audit are listed in `sss/audit/SSS_C2_MAINTENANCE_CLOSURE_v1.0.md`.

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

## Final system release — thirteen cases

The SSS correctness-remediation and visual-modernization programs are both complete. The final
system release promotes all thirteen packages to `APPROVED_STABLE` at the versions in the table
above, owner **Nate / Owner**, approval date **2026-08-10**, physical print **PASS at 100% /
Actual Size** on Google Chrome against tested baseline `105467f997b1425b7f40e8150749c70e09ed4771`.

Each case carries a new `history/release-vX.Y.json` and `CASENN_OWNER_APPROVAL_vX.Y.md`; every
earlier release and owner-approval record is retained byte-identical, and each new record
represents its immediate predecessor through `priorApprovedReleases`. The visual-modernization
inventory is 36 of 36 complete with zero findings remaining, canonical browser registration
remains 2375, and the recorded 2374 total remains the accepted candidate-specific same-Mac
differential only — no general browser, Mac, Chrome, platform or environment exception exists.

HTML-only canonical production is unchanged: there is no canonical project PDF artifact and no
PDF release gate, and manually produced PDFs remain noncanonical and require their own
accessibility review before distribution.

The release is prepared on `release/sss-final-system` and is held unpushed for independent
review. It is not merged, and merge readiness is a separate evaluation.
