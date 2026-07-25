# SSS Campaign 1, Case 02 — Lunar Greenhouse

This directory is the second validated implementation of the shared SSS-HHH curriculum production system and the first structural stress test of the Case 01 production foundation.

## Current master

`master/SSS_C1_CASE02_EDITABLE_MASTER_v1.1.html`

- **Master version:** v1.1 review build
- **Historical master:** `master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html`
- **Game baseline:** `2a6e8a7`
- **Curriculum Bible:** v1.3
- **Student identity:** Process Modeler
- **Task registry:** `source/task-registry.js` v1.0

The v1.1 master applies the universal first-page banner, generic continuation header, minimal role-plus-position footer, and printable-metadata separation in `UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md`. Production status remains in metadata and repository records rather than on classroom pages.

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
- `source/figure-research-and-rights.md`
- `source/task-registry.js`

## Original figure

`assets/pollination-process-model.svg`

The figure is curriculum-original. Authoritative diagrams were researched, but no external figure was copied or adapted because reuse rights were not explicit.

## Published outputs

The editable HTML master is the layout authority during review. Fixed PDFs are generated only when needed for testing and are not committed by default. The `published/` folder is reserved for approved release outputs after automated review and owner physical print testing.

## Validation

Run:

```bash
python validation-artifacts/validate_case02.py
```

The default harness validates content, role isolation, persistence, selective clearing, reset behavior, portable HTML serialization, accessibility, grayscale behavior, overflow, and the v1.1 page-identity contract without retaining PDFs.
