# SSS Campaign 1, Case 02 - Lunar Greenhouse

## Current production track

- Master: `master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html`
- Curriculum version: v1.0
- Balanced Page Fill and Vertical Rhythm: v1.0.2
- Game baseline: `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`
- Status: APPROVED

The original print-approved v1.0 HTML byte set is retained as `PRE_MAINTENANCE_PRINT_APPROVED_HISTORICAL`. The maintained v1.0 master and five role HTML files, maintenance revision `2026-07-31`, are `CURRENT_HTML_MIGRATION_BASELINE` and `OWNER_AUTHORIZED_FOR_PHASE2`. Historical physical-print evidence remains preserved but does not transfer to the maintained HTML. Its physical-print gate is `OPEN` until Phase 2 owner review. No new curriculum version was created. See `CASE02_CURRENT_HTML_RECONCILIATION_2026-07-31.json`.

The current v1.0 master combines the approved Printable Page Identity v1.0.4 system with Balanced Page Fill and Vertical Rhythm v1.0.2. The contradictory Case 02 v1.1 master/manifest layer remains excluded.

## Outputs

- Student Mission HTML maintenance build: 3 pages
- Teacher Packet: 7 pages
- Answer Key: 3 pages
- Accessible Mission: 5 pages
- Grayscale Mission HTML maintenance build: 3 pages

Every maintained HTML role now uses semantic task labels with the task number appearing once in the title; duplicated labels such as `TASK 01` are prohibited. Standard task titles render at 11.5pt, while Accessible titles retain the canonical 14pt size. Task 7 on the standard Student and Grayscale worksheets also uses the shared full-width `student-v1.0` Claim/Evidence/Reasoning component. The Accessible CER layout remains unchanged.

Student page 2 converts lower-page surplus into larger Task 4–6 writing fields. Student page 3 stacks Tasks 8 and 9 as separate full-width sections; open-response tasks are no longer paired side by side merely to fill a row. The measured lower-page reserves are 100.3px and 115.3px respectively.

This was an HTML-only maintenance build. The approved checksum-controlled PDFs were not regenerated: Student and Grayscale PDFs remain 2 pages, Teacher 7, Answer 3, and Accessible 5. Run:

```bash
python validation-artifacts/build_case02_cer_html.py
python validation-artifacts/validate_case02_cer_html.py
```

Do not run the legacy full release builder merely to reproduce this HTML-only maintenance change; that harness regenerates PDFs.

## Release gate

The approved PDF/physical-print release record remains intact. The maintained HTML layout has a separate validation-build maintenance status pending any future print release cycle.
