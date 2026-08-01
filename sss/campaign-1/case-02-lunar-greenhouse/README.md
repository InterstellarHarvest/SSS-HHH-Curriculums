# SSS Campaign 1, Case 02 - Lunar Greenhouse

## Canonical active customization

Use the central Curriculum Editor, not the embedded editor in the standalone master, for active Case 02 customization:

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/> and select `2 - Lunar Greenhouse`. Versions are not selected in the primary case menu. The registered v1.0 package is the canonical active editable production source. Use **Print / Save PDF**, **Download Editable Copy** for the portable all-role editable document, **Download Worksheet** for clean selected-role HTML without editing controls, **Clear Responses**, and **Reset This Case**, in that order. Browser-created PDFs require separate accessibility review.

The v1.0 standalone master and role HTML files remain immutable approved release snapshots. Their embedded runtime is deprecated compatibility only; it is retained byte-identical for approval evidence and parity.

## Current production track

- Master: `master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html`
- Curriculum version: v1.0
- Balanced Page Fill and Vertical Rhythm: v1.0.2
- Game baseline: `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`
- Status: APPROVED

The original print-approved v1.0 HTML byte set is retained as `PRE_MAINTENANCE_PRINT_APPROVED_HISTORICAL`. The maintained v1.0 master and five role HTML files, maintenance revision `2026-07-31`, are the approved current HTML presentation and exact Phase 2 parity baseline. Nate / Owner passed browser review, print-preview review, and physical printing on 2026-08-01 at 100% / Actual Size. Historical PDFs remain retained, current production remains HTML-based, and no new PDFs were generated. No new curriculum version was created. See the immutable reconciliation snapshot `CASE02_CURRENT_HTML_RECONCILIATION_2026-07-31.json` and its additive Phase 2 owner-approval record.

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

The approved historical PDF/physical-print release record remains intact. The maintained HTML layout separately passed the Phase 2 owner browser, print-preview, and physical-print reviews on 2026-08-01. The central workflow is canonical; cutover is `APPROVED` with `OWNER_REVIEW_PASS` and `READY_TO_MERGE`.
