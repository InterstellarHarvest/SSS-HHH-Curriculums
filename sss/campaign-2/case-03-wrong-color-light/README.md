# SSS Campaign 2 · Case 03 — The Wrong Color of Light

Released native curriculum package. Package ID `SSS-C2-CASE03`, runtime ID `wrong_color_light`.

| Field | Value |
|---|---|
| Title | The Wrong Color of Light |
| Runtime investigation | Oolian Mariculture Dome |
| Location | Trench Shelf IV |
| Subtitle | Campaign 2 · Case 03 · Trench Shelf IV, Kepler-186f (Ocean) |
| Institutional identity | Space Sprout Sleuth / Solar Agricultural Agency (SAA) |
| Version | 1.0 |
| Lifecycle | `APPROVED_STABLE` — owner approved 2026-08-04, print gate PASS at 100% / Actual Size |
| Frozen game baseline | recorded in `source/task-registry.js` as `gameCommit` |

## Contents

```text
case-03-wrong-color-light/
├── README.md
├── history/
│   ├── CASE03_OWNER_APPROVAL_v1.0.md
│   └── release-v1.0.json
└── source/
    ├── case-package.json
    ├── content.html
    ├── layout-overrides.json
    ├── presentation.css
    └── task-registry.js
```

No generated PDF, role document, or screenshot is committed for this case.

## Instructional shape

Eight tasks, in this order and with these identifiers across all four roles:

1. Frame What Changed
2. Read the GRO-9 Spectrum
3. Compare Lamp Output with Zhal-Kelp Response
4. Use the Timeline and Controls
5. Connect the Five Evidence Sources
6. Diagnose and Reject Alternatives
7. Explain the Diagnosis with CER
8. Write a Better Lighting Specification

Role page counts: Student 5, Teacher 8, Answer Key 4, Accessible 8.

## Science boundary

`source/task-registry.js` is the ledger of record. It carries the five formal clues and their task
coverage, the exact numerical ledger, the source-status split between established Earth science and
case-specific evidence, the correct diagnosis and its three rejected alternatives, the prohibited
claims, and the figure provenance. Case-scoped assertions in
`apps/curriculum-editor/tests/validate_case03_campaign2.py` enforce that ledger against the printable
content.

Two rules dominate the case and are enforced mechanically:

- no figure may draw a continuous action-spectrum curve or imply zero response outside 460–540 nm;
- no printable role may assert that kelp cannot use red light, that one percentage proves the
  diagnosis, or that the narrated recovery is an experimental result.

## Working on this case

Serve the repository root and open the central editor:

```bash
python3 apps/curriculum-editor/serve.py
```

Then open <http://127.0.0.1:8000/apps/curriculum-editor/?case=SSS-C2-CASE03>.

Validation:

```bash
python3 apps/curriculum-editor/tests/validate_case03_campaign2.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE03
python3 apps/curriculum-editor/tests/run_browser_tests.py
```
