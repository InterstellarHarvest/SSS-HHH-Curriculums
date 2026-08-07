# SSS Campaign 2 · Case 05 — Too Clean a Room

Released native curriculum package. Package ID `SSS-C2-CASE05`, runtime ID `too_clean_room`.
The current release is the v1.1 corrective release; the superseded v1.0 records are retained
unchanged in `history/`.

| Field | Value |
|---|---|
| Title | Too Clean a Room |
| Runtime investigation | Concord Botanical Vault |
| Location | Lagrange Point 5 |
| Subtitle | Campaign 2 · Case 05 · Lagrange Point 5, Concord Neutral Zone |
| Institutional identity | Space Sprout Sleuth / Solar Agricultural Agency (SAA) |
| Version | 1.1 (corrective release) |
| Lifecycle | `APPROVED_STABLE` — owner approved 2026-08-06, print gate PASS at 100% / Actual Size. Supersedes v1.0, approved 2026-08-05 |
| Frozen game baseline | recorded in `source/task-registry.js` as `gameCommit` |

## Contents

```text
case-05-too-clean-room/
├── README.md
├── history/                 v1.0 records retained byte-identical
│   ├── CASE05_OWNER_APPROVAL_v1.0.md
│   ├── CASE05_OWNER_APPROVAL_v1.1.md
│   ├── release-v1.0.json
│   └── release-v1.1.json
└── source/
    ├── case-package.json
    ├── content.html
    ├── layout-overrides.json
    ├── presentation.css
    └── task-registry.js
```

No generated PDF, role document, or screenshot is committed for this case.

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

## The v1.1 corrective release

Four printable defects, all narrow. `teacher-guide-09` shipped a bare `X` in place of the clause
naming the full-page CER; it is restored to the page-structure statement this README and the v1.0
owner approval both already made. The Accessible edition regained the briefing sentence naming the
patients and the shortage — the packet's only printed impacts-on-people evidence, which the direct
MS-ETS1-1 claim rests on — and the nutrient-uptake statement its own Task 5 word bank offers as
evidence. The Answer Key stopped accepting two Task 7 constraints printed in no learner edition.

No standard was added, removed or re-rated. No Student task, figure or table changed. Page counts
are unchanged at Student 7, Teacher 9, Answer Key 5, Accessible 7.

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
cautions. It also carries the ledgers added by the v1.1 correction: `standards`, recording the
assessed practice, assessing task, learner evidence and limitation behind each of the three current
claims, and `learnerEvidencePolicy`, recording which facts reach both learner editions, which are
Teacher-only, and which are withheld from every role. Case-scoped assertions in
`apps/curriculum-editor/tests/validate_case05_campaign2.py` enforce that ledger against the printable
content, and `apps/curriculum-editor/tests/test_case05_mutations.py` proves each protection fires.

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
python3 apps/curriculum-editor/tests/test_case05_mutations.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE05
python3 apps/curriculum-editor/tests/run_browser_tests.py
python3 apps/curriculum-editor/tests/run_pdf_tests.py
```
