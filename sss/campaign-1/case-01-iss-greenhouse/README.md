# SSS Campaign 1, Case 01 — ISS Greenhouse Module

This directory contains the first validated production foundation for the shared SSS-HHH curriculum system.

## Current validation master

`master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`

- **Version:** v1.0 release candidate
- **Status:** VALIDATION BUILD
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

## Release-candidate PDFs

- `published/SSS_C1_CASE01_STUDENT_MISSION_v1.0_RC.pdf`
- `published/SSS_C1_CASE01_TEACHER_PACKET_v1.0_RC.pdf`
- `published/SSS_C1_CASE01_ANSWER_KEY_v1.0_RC.pdf`
- `published/SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.0_RC.pdf`
- `published/SSS_C1_CASE01_GRAYSCALE_REVIEW_v1.0_RC.pdf`

These remain review artifacts until the owner completes physical print testing at 100% scale.

## Validation

Run from `validation-artifacts/`:

```bash
python validate_case01_rc.py
```

The harness validates role counts, overflow, accessibility basics, persistence, selective clearing, reset behavior, portable HTML serialization, task-heading/content regression, grayscale, and all five PDF outputs.

## Historical files

`SSS_C1_CASE01_EDITABLE_MASTER_v0.2.html`, `SSS_C1_CASE01_EDITABLE_MASTER_v0.3.html`, and v0.2/v0.3 PDFs are retained for provenance only. They are not current production or validation artifacts.

## Release gate

The only open Case 01 release-approval blocker is owner physical print testing. Do not change the visible status from **VALIDATION BUILD** until that test is documented as passed.
