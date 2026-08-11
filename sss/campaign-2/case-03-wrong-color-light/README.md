# SSS Campaign 2 · Case 03 — The Wrong Color of Light

Released native curriculum package. Package ID `SSS-C2-CASE03`, runtime ID `wrong_color_light`.
The current release is the v1.1 corrective release; v1.0 is superseded, not withdrawn, and its
history records are retained unchanged.

| Field | Value |
|---|---|
| Title | The Wrong Color of Light |
| Runtime investigation | Oolian Mariculture Dome |
| Location | Trench Shelf IV |
| Subtitle | Campaign 2 · Case 03 · Trench Shelf IV, Kepler-186f (Ocean) |
| Institutional identity | Space Sprout Sleuth / Solar Agricultural Agency (SAA) |
| Version | 1.2 (corrective release of 1.1) |
| Lifecycle | `APPROVED_STABLE` — owner approved 2026-08-10, print gate PASS at 100% / Actual Size |
| Prior approved release | 1.0, owner approved 2026-08-04, print gate PASS at 100% / Actual Size |
| Retained history | `history/release-v1.0.json` and `history/CASE03_OWNER_APPROVAL_v1.0.md`, unchanged |
| Frozen game baseline | recorded in `source/task-registry.js` as `gameCommit` |

## Contents

```text
case-03-wrong-color-light/
├── README.md
├── history/
│   ├── CASE03_OWNER_APPROVAL_v1.0.md
│   ├── CASE03_OWNER_APPROVAL_v1.1.md
│   ├── release-v1.0.json
│   └── release-v1.1.json
└── source/
    ├── case-package.json
    ├── content.html
    ├── layout-overrides.json
    ├── presentation.css
    └── task-registry.js
```

No generated PDF, role document, or screenshot is committed for this case, at either version.
`history/` holds one release record and one owner-approval record per approved version. The v1.0
records are retained byte-identical and were not edited to describe v1.1.

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

Role page counts: Student 5, Teacher 8, Answer Key 4, Accessible 8 — unchanged from v1.0.

## What v1.1 corrected

- Task 5 printed `total PAR alone proves no effective spectrum` in both learner editions, inverting
  the reasoning rule the Teacher Guide and Answer Key state and grade against. All four roles now
  carry one rule, stated in full in a marked `data-reasoning-rule` block in each learner edition.
- Task 1 asked for a changed/kept classification before the Student edition printed the controlling
  record. Both learner editions now carry a marked `data-change-record` naming all four conditions,
  on the page of the task that needs it, and stay differentiated in register.
- The Answer Key reasoned at Task 4 from a runtime-only 30%-higher photon flux, and graded Task 8's
  intensity criterion against an unprinted old-dome level. Both now rest on printed evidence.
- The approximate `~14 µmol/m²/s` value carried an invented provenance (`an approximation from an
  incomplete weighting model`) the canonical game source does not establish. It is removed; the
  value stays Teacher-facing, approximate, and outside student calculation.
- `MS-PS4-2` is withdrawn as a direct standard and not replaced. No task develops or uses a model of
  light reflected, absorbed or transmitted through a material.
- Four printable text errors are repaired, one of them in an Accessible direction.

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
python3 apps/curriculum-editor/tests/test_case03_mutations.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE03
python3 apps/curriculum-editor/tests/run_browser_tests.py
```

The v1.2 final-system release (owner approved 2026-08-10, physical print PASS at 100% / Actual Size on Google Chrome) closes the SSS correctness-remediation and visual-modernization program for this case. The prior release records are retained unchanged in `history/`.

Retained releases: `history/release-v1.1.json` (owner approved 2026-08-06) and `history/release-v1.0.json`, both retained byte-identical alongside their owner-approval records. The current release record is `history/release-v1.2.json`.
