# SSS Campaign 1, Case 01 — ISS Greenhouse Module

This directory contains the first validated production foundation for the shared SSS-HHH curriculum system.

## Current approved master

`master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html`

- **Curriculum version:** v1.1 (current release)
- **HTML maintenance revision:** 2026-07-31
- **Phase 2 status:** CURRENT_HTML_MIGRATION_BASELINE · OWNER_AUTHORIZED_FOR_PHASE2
- **Physical-print gate for maintained HTML:** OPEN
- **Status:** APPROVED
- **Game baseline:** `2a6e8a7`
- **Curriculum Bible:** v1.3
- **Task registry:** `source/task-registry.js` v1.0

Use the maintained v1.1 HTML byte set as the exact Phase 2 migration and parity reference. The retained v1.0 master is the prior approved release; v0.2 and v0.3 remain prototypes. Do not regenerate PDFs from this baseline.

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

These are retained v1.0 historical outputs; the owner completed physical print testing at 100% scale on 2026-07-24.

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

## HTML task-heading maintenance

The maintained v1.1 master and five role HTML files now use the canonical task-title scale: 11.5 pt for standard roles and 14 pt for Accessible. This is an HTML-only maintenance correction. Run `validation-artifacts/build_case01_html_maintenance.py` and `validation-artifacts/validate_case01_html_maintenance.py`; do not run the legacy release validator, which generates PDFs. Existing approved PDFs remain byte-identical historical artifacts, and physical-print approval is not claimed for the updated HTML until separately tested.

Optional extensions explicitly declare shared component contract `canonical-v1.0` while preserving the approved Case 01 neutral callout, solid slate rail, and wrench-icon geometry that governs later cases.

The original print-approved v1.1 HTML hashes are preserved as `PRE_MAINTENANCE_PRINT_APPROVED_HISTORICAL`. The maintained v1.1 master and role HTML are the owner-authorized current Phase 2 parity baseline. Historical physical-print evidence is preserved but is not inherited by the maintained HTML; its physical-print gate remains open until Phase 2 owner review. No new curriculum version was created. See `CASE01_CURRENT_HTML_RECONCILIATION_2026-07-31.json`.
