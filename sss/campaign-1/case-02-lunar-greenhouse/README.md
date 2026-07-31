# SSS Campaign 1, Case 02 - Lunar Greenhouse

## Current production track

- Master: `master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html`
- Curriculum version: v1.0
- Balanced Page Fill and Vertical Rhythm: v1.0.2
- Game baseline: `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`
- Status: APPROVED

The current v1.0 master combines the approved Printable Page Identity v1.0.4 system with Balanced Page Fill and Vertical Rhythm v1.0.2. The contradictory Case 02 v1.1 master/manifest layer remains excluded.

## Outputs

- Student Mission HTML maintenance build: 3 pages
- Teacher Packet: 7 pages
- Answer Key: 3 pages
- Accessible Mission: 5 pages
- Grayscale Mission HTML maintenance build: 3 pages

Task 7 on the standard Student and Grayscale worksheets now uses the shared full-width `student-v1.0` Claim/Evidence/Reasoning component. The Accessible edition was already suitable and remains unchanged.

This was an HTML-only maintenance build. The approved checksum-controlled PDFs were not regenerated: Student and Grayscale PDFs remain 2 pages, Teacher 7, Answer 3, and Accessible 5. Run:

```bash
python validation-artifacts/build_case02_cer_html.py
python validation-artifacts/validate_case02_cer_html.py
```

Do not run the legacy full release builder merely to reproduce this HTML-only maintenance change; that harness regenerates PDFs.

## Release gate

The approved PDF/physical-print release record remains intact. The updated Student HTML layout has a separate validation-build maintenance status pending any future PDF/print release cycle.
