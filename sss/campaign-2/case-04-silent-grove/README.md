# SSS Campaign 2 · Case 04 — The Silent Grove

Released native curriculum package. Package ID `SSS-C2-CASE04`, runtime ID `silent_grove`.
The current version is the v1.1 corrective release; the superseded v1.0 records are retained
unchanged in `history/`.

| Field | Value |
|---|---|
| Title | The Silent Grove |
| Runtime investigation | Zhel'ii Diaspora Grove |
| Location | Drift Vessel Thal-Oren |
| Subtitle | Campaign 2 · Case 04 · Drift Vessel Thal-Oren, Inter-system Transit |
| Institutional identity | Space Sprout Sleuth / Solar Agricultural Agency (SAA) |
| Version | 1.2 (corrective release of 1.1) |
| Lifecycle | `APPROVED_STABLE` — owner approved 2026-08-10, print gate PASS at 100% / Actual Size. The superseded v1.1 (2026-08-06) and v1.0 (2026-08-05) records are retained unchanged |
| Frozen game baseline | recorded in `source/task-registry.js` as `gameCommit` |

## Contents

```text
case-04-silent-grove/
├── README.md
├── history/                 v1.0 retained byte-identical; v1.1 is the current release
│   ├── CASE04_OWNER_APPROVAL_v1.0.md
│   ├── CASE04_OWNER_APPROVAL_v1.1.md
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

Eight tasks, in this order and with these identifiers across all four roles:

1. Separate What Changed from What Held
2. What a Reading Can and Cannot Tell You
3. Find the Pattern a Total Hides
4. Weaken the Competing Explanations
5. Connect the Five Evidence Sources
6. Diagnose and Model the Mechanism
7. Explain the Diagnosis with CER
8. Specify a Dark Period and a Monitored Trial

Role page counts: Student 6, Teacher 8, Answer Key 4, Accessible 8.

The case turns on a distinction the other Campaign 2 cases do not make: the failure is the removal of a
recurring cue, not the removal of a substance. Task 3 is the load-bearing task — a daily total cannot show
that a function was timed.

Tasks 2 and 3 teach their ideas with short everyday examples before turning to the grove, following the
convention Campaign 2 Case 01 established with its merry-go-round. Task 2 uses a kitchen scale reading
`0 kg` for an envelope and two witnesses timing the same rain shower; Task 3 uses two people who each
sleep eight hours in different patterns. Each example is marked `data-analogy`, prints a visible line
saying its values are not grove measurements, and is validated to keep those values out of the rest of the
packet. The grove's own records are a reference case file the later tasks argue from, never something a
task asks a student to copy out.

## Science boundary

`source/task-registry.js` is the ledger of record. It carries the five formal clues and their task
coverage, the exact numerical ledger, the source-status split between established Earth chronobiology and
records made for this grove, the correct diagnosis and its three rejected alternatives, the prohibited
claims, and the figure provenance. Case-scoped assertions in
`apps/curriculum-editor/tests/validate_case04_campaign2.py` enforce that ledger against the printable
content.

## Standards

Case 04 v1.1 claims **no NGSS performance expectation as directly assessed**. `MS-LS1-5` and
`MS-ETS1-1` were both claimed as direct in v1.0 and are **withdrawn as direct**; no standard
replaces either. MS-LS1-5 is retained as supporting and bounded at Task 7 — the case holds
growth constant deliberately, so the packet carries the explanation practice, not the
performance expectation. MS-ETS1-1 is retained as supporting at Task 8, because the Student
task does not ask students to account for impacts on people. MS-ETS1-2 remains supporting and
conditional. What the packet does assess directly is the science and engineering practices and
crosscutting concepts listed in the Teacher Guide. The exact assessed practice and learner
evidence behind each retained claim are recorded in `source/task-registry.js` under `standards`.

It also carries the ledgers added by the v1.1 correction: `standards` with the exact assessed practice
and learner evidence behind each retained claim, `withdrawnStandards`, `learnerEvidencePolicy` (which
facts are supplied to learners, which are withheld, and which are Teacher-only), and
`alternativeSourceFidelity` (the runtime wording each rejected alternative must keep).

Five rules dominate the case and are enforced mechanically:

- no printable role may generalise this grove's dark-interval requirement into a rule for plants;
- `0.0 ppb` is always a reading at the instrument's reporting threshold and never an absolute absence;
- the reported `40–80 ppb` healthy range is never collapsed into a single value;
- no figure may draw a curve, and the only figure in the packet belongs to a teaching example and says so;
- no teaching-example value may appear anywhere outside its own analogy block.

The two ship logs give different days — Day −80 and Day −83 — for the start of complete silence. The
packet presents both records and never asks a student to reconcile, average, or choose between them.

## Working on this case

Serve the repository root and open the central editor:

```bash
python3 apps/curriculum-editor/serve.py
```

Then open <http://127.0.0.1:8000/apps/curriculum-editor/?case=SSS-C2-CASE04>.

Validation:

```bash
python3 apps/curriculum-editor/tests/validate_case04_campaign2.py
python3 apps/curriculum-editor/tests/test_case04_mutations.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE04
python3 apps/curriculum-editor/tests/run_browser_tests.py
python3 apps/curriculum-editor/tests/run_pdf_tests.py
```

The v1.2 final-system release (owner approved 2026-08-10, physical print PASS at 100% / Actual Size on Google Chrome) closes the SSS correctness-remediation and visual-modernization program for this case. The prior release records are retained unchanged in `history/`.

Retained releases: `history/release-v1.1.json` (owner approved 2026-08-06) and `history/release-v1.0.json`, both retained byte-identical alongside their owner-approval records. The current release record is `history/release-v1.2.json`.
