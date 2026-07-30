# SSS Campaign 1, Case 01 — ISS Greenhouse Module

This directory contains the first validated production foundation for the shared SSS-HHH curriculum system.

## Current approved master

`master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`

- **Version:** v1.0 (approved stable release)
- **Status:** APPROVED
- **Game baseline:** `2a6e8a7`
- **Curriculum Bible:** v1.3
- **Task registry:** `source/task-registry.js` v1.0

Use this file, not the v0.2 or v0.3 prototypes, for validation, PDF generation, and future framework extraction.

## Controlled source documents

- `source/student-mission-sheet.md`
- `source/lesson-plan.md`
- `source/quick-start.md`
- `source/teacher-case-analysis.md`
- `source/answer-key.md`
- `source/quick-rubric.md`
- `source/formal-rubric.md`
- `source/references.md`
- `source/technical-notes.md`
- `source/task-registry.js`

The Markdown sources, HTML master, Answer Key exemplars, and task registry use the same exact numbered task titles.

## Published v1.0 PDFs

- `published/SSS_C1_CASE01_STUDENT_MISSION_v1.0.pdf`
- `published/SSS_C1_CASE01_TEACHER_PACKET_v1.0.pdf`
- `published/SSS_C1_CASE01_ANSWER_KEY_v1.0.pdf`
- `published/SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.0.pdf`
- `published/SSS_C1_CASE01_GRAYSCALE_REVIEW_v1.0.pdf`

These are the current published outputs; the owner completed physical print testing at 100% scale on 2026-07-24.

## Validation

Run from `validation-artifacts/`:

```bash
python validate_case01_rc.py
```

The harness validates role counts, overflow, accessibility basics, persistence, selective clearing, reset behavior, portable HTML serialization, task-heading/content regression, grayscale, and all five PDF outputs.

## Historical files

`SSS_C1_CASE01_EDITABLE_MASTER_v0.2.html`, `SSS_C1_CASE01_EDITABLE_MASTER_v0.3.html`, and v0.2/v0.3 PDFs are retained for provenance only. They are not current production or validation artifacts.

## Release gate

The owner completed physical print testing at 100% scale on 2026-07-24. Case 01 is the approved stable v1.0 release; the visible status is **APPROVED** and no release blockers remain.

<!-- PRINTABLE_PAGE_IDENTITY_V1_0_4_START -->
## Case 01 v1.1 approved stable successor

- Approved historical master: `master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html` — unchanged.
- Design successor: `master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html`.
- Governing identity rule: `shared/visual-style-guide/amendments/PRINTABLE_PAGE_IDENTITY_v1.0.4.md`.
- Status: APPROVED pending owner physical 100% print testing.

The v1.1 successor changes printable first-page identity, continuation identity, footer treatment, and visible production-metadata separation only. Instructional content and publishing behavior remain inherited from approved v1.0.
<!-- PRINTABLE_PAGE_IDENTITY_V1_0_4_END -->

<!-- FINAL_APPROVAL_2026_07_30_START -->
## Approved stable release

Case 01 v1.1 is the approved stable printable-identity successor as of 2026-07-30. Automated validation and the owner 100%-scale physical print test both pass. Tester: Nate / Owner. Printer/copier: Not recorded. Paper: Not recorded. Approved Case 01 v1.0 remains byte-identical and retained as the prior release.
<!-- FINAL_APPROVAL_2026_07_30_END -->
