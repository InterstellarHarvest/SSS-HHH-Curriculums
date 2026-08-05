# SSS Campaign 2 · Case 05 — Too Clean a Room

Draft native curriculum package. Package ID `SSS-C2-CASE05`, runtime ID `too_clean_room`.

| Field | Value |
|---|---|
| Title | Too Clean a Room |
| Runtime investigation | Concord Botanical Vault |
| Location | Lagrange Point 5 |
| Subtitle | Campaign 2 · Case 05 · Lagrange Point 5, Concord Neutral Zone |
| Institutional identity | Space Sprout Sleuth / Solar Agricultural Agency (SAA) |
| Version | 1.0 |
| Lifecycle | `DRAFT` — owner review not started, print gate not run |
| Frozen game baseline | recorded in `source/task-registry.js` as `gameCommit` |

## Contents

```text
case-05-too-clean-room/
├── README.md
└── source/
    ├── case-package.json
    ├── content.html
    ├── layout-overrides.json
    ├── presentation.css
    └── task-registry.js
```

No `history/` directory exists yet, and no generated PDF, role document, or screenshot is committed
for this case.

## Instructional shape

Seven tasks, in this order and with these identifiers across all four roles:

1. Sort What Was Specified from What Was Not
2. What a Reading Can and Cannot Tell You
3. Read the Decline and the Failed Adjustments
4. Connect the Five Evidence Sources
5. Diagnose, Reject the Alternatives, and Model the Mechanism
6. Explain the Diagnosis with CER
7. Specify a Monitored Trial and Recommend a Response

Role page counts: Student 7, Teacher 9, Answer Key 5, Accessible 7. Task 6 occupies a full page of its
own in the Student and Accessible editions, so the explanation is written in one sitting.

The Student edition is one page above the 4–6 planning range, and that is a measured result rather than
a drafting habit. With the CER on a page of its own, the browser matrix measured every pairing of the
middle tasks at roughly 1 140–1 200 px against a 936 px content frame, so no two of Tasks 3, 4 and 5 can
share a Letter page without cutting an evidence table or a response area. Seven tasks on seven pages is
the smallest arrangement that keeps each task atomic. The bottom reserve that remained on Student pages
2, 3 and 5 was given back to the response areas rather than filled with content.

The case turns on something none of the earlier Campaign 2 cases asks for: the failure is a condition
the facility controlled to its limit and never wrote a biological specification for. Every monitored
reading is correct, so the reasoning cannot start from an anomaly. Task 1 separates what was specified
from what was not, and Task 3 carries the load — a condition that never changed produces an output that
falls every month, and five adjustments that changed nothing are evidence rather than dead ends.

Task 2 teaches its idea with a short everyday example before turning to the vault, following the
convention Campaign 2 Case 01 established. A rain gauge marked only in whole millimetres reads `0 mm`
on two nights that were not the same. The example is marked `data-analogy`, prints a visible line saying
its values are not vault measurements, and is validated to keep those values out of the rest of the
packet.

Task 7 is a specification task, not a procedure. Students define what an approved trial must include and
what would stop it. The packet states on the page that no student names a radiation source, a device, or
an operating setting, because those decisions belong to the qualified radiation-protection and
radiological-engineering team.

## Science boundary

`source/task-registry.js` is the ledger of record. It carries the five formal clues and their task
coverage, the numerical ledger, the source-status split across established Earth science, case-specific
evidence, modeled evidence, case inference and engineering extrapolation, the correct diagnosis and its
three rejected alternatives, eighteen prohibited claims, the figure provenance, and the production
cautions. Case-scoped assertions in `apps/curriculum-editor/tests/validate_case05_campaign2.py` enforce
that ledger against the printable content.

Five rules dominate the case and are enforced mechanically:

- the radiation-responsive pathway is species-specific, and no printable role may generalise it to
  plants, Earth organisms, or people;
- `<0.01 mGy/day` is always a reading at the monitor's detection limit and never an absence, a zero, or
  the value `0.01`;
- absorbed dose stays in milligray and is never restated in sievert or as a human risk figure;
- `about 8.4 mGy/day` is a record from one surveyed site, never an optimum or a target, and two dose
  conditions never become a response curve;
- no printable role names an isotope, a source, a device, or an operating setting.

Two canonical sources disagree with each other, and the packet follows the stronger one. The design
document describes the mechanism as "radiation as nutrient" and proposes installing calibrated radiation
sources; the shipped runtime describes a species-specific radiation-responsive pathway and requires a
licensed, shielded, monitored trial with controls and stop criteria. The packet follows the runtime. The
internal clue tag reads `HORMESIS_OBLIGATE_RADIATION`, but the record it opens is titled obligate
radiation-triggered metabolism and carries an advisory against generalisation; the word *hormesis*
appears nowhere in the printable packet.

## Working on this case

Serve the repository root and open the central editor:

```bash
python3 apps/curriculum-editor/serve.py
```

Then open <http://127.0.0.1:8000/apps/curriculum-editor/?case=SSS-C2-CASE05>.

Validation:

```bash
python3 apps/curriculum-editor/tests/validate_case05_campaign2.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE05
python3 apps/curriculum-editor/tests/run_browser_tests.py
python3 apps/curriculum-editor/tests/run_pdf_tests.py
```
