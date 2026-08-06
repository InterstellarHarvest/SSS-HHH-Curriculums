# SSS Campaign 2 · Case 06 — The First Garden

Released native curriculum package. Package ID `SSS-C2-CASE06`, runtime ID `first_garden`.

| Field | Value |
|---|---|
| Title | The First Garden |
| Runtime investigation | The First Garden (`first_garden`) |
| Location | Restored Terrace |
| Subtitle | Earth |
| Campaign position | Campaign 2, case 6 of 6 — bonus finale, hidden until the five main cases are complete |
| Institutional identity | Solar Agricultural Agency (SAA) |
| Version | 1.0 |
| Lifecycle | `APPROVED_STABLE` · `OWNER_REVIEW_PASS` · print `PASS` |
| Frozen game baseline | `29c3b222c53f51de11a3aa83e896a6d0ef6fb490` |

## Contents

```text
case-06-first-garden/
├── README.md
├── history/
│   ├── CASE06_OWNER_APPROVAL_v1.0.md
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

Seven tasks, in this order and with these identifiers across all four roles:

1. `C2-C06-T1` — Sort What Was Tested from What Was Never Tested
2. `C2-C06-T2` — Read the Pattern in the Site Survey
3. `C2-C06-T3` — Weigh the Explanations
4. `C2-C06-T4` — Show Where the Five Sources Converge
5. `C2-C06-T5` — Model the Candidate Pathway
6. `C2-C06-T6` — Explain the Diagnosis with CER
7. `C2-C06-T7` — Specify the Screened, Approved Trial

Task 7 asks what the trial must include and why, and stops there. The runtime's reform-recommendation thread —
proposing risk-tiered biosafety standards — turns on Concord politics rather than the garden's evidence, so it is
carried as Teacher-facing discussion rather than a written student prompt.

Role page counts: Student 5, Teacher 8, Answer Key 5, Accessible 7. The Accessible CER is a dedicated page
carrying `data-accessible-cer-page="canonical-v1.0"`. In the Student edition the CER shares its page with Task 7
under `data-student-cer-page="combined-v1.0"`, the same combined form Campaign 1 Case 07 uses: on its own the CER
left roughly half a page empty, and the trial specification reads naturally straight after the explanation it
constrains.

This case is shorter than Campaign 2 Cases 01–05 on the Student side because its evidence is different in kind,
not smaller in quantity. Cases 01–05 each turn on a measured value checked against a written specification, and
each therefore needs page area for a quantitative record, a unit-discipline task and a precision ledger. Case 06
reports almost no quantities: the surveyed patch diameter of approximately four to six metres, the roughly three
metres between thriving and failing ground, and a set of durations. Its reasoning is about scope, elimination and
convergence, and it contains no calculation at all. A precision task and a quantitative comparison figure would
both have been decorative here, so neither exists.

For the same reason the packet carries one figure rather than two, no timeline, and no trend graph. The case
reports no time series and no dated events; there is nothing to plot. Figure A is a plan view: circular patches
where the surveyed compounds are abundant, drawn inside ground where the same compounds fall to trace levels,
because "circular patches of approximately four to six metres in diameter" is what the survey actually reports.
Both its caption and its extended description state that it shows the reported pattern rather than mapping the
garden.

What the case does need, and gets, is space for triangulation. No source resolves the investigation alone — this
is the only Campaign 2 case in which every source is a person or an archive, with no sensor panel and no specimen
examination — so Task 4 is the packet's spine and receives a full five-source contribution-and-limit matrix.

## Science boundary

`source/task-registry.js` is the ledger of record. It carries the source ledger, the numerical ledger, the
source-status separation between established Earth science, case-specific evidence and published global
estimates, the correct diagnosis, the three rejected alternatives, twenty prohibited claims, figure provenance,
and the production cautions that record where canonical sources disagree.

Case-scoped assertions in `apps/curriculum-editor/tests/validate_case06_campaign2.py` enforce that ledger against
the rendered content, with self-tested detectors that must fire on the claim each exists to catch.

Four rules dominate the case and are enforced mechanically:

- The mycorrhizal explanation is always a **candidate cause**, never a proven mechanism, and compatible partners
  are never declared certainly absent.
- **"Trace levels only"** never becomes zero, absent, or none. The compounds between the patches are detected.
- No printable role proposes moving living material without identification, provenance and pathogen screening,
  host-compatibility checks, approval, untreated controls and monitoring.
- The popular-science framings the approved science-source register rejects — the "wood wide web", preferential
  feeding by mature trees, the forest as one organism — appear nowhere except inside explicitly quoted
  misconception blocks in the Teacher Guide.

Where canonical sources conflict, the shipped runtime and the science-source register win. The design document
`resources/CASE_6_IMPLEMENTATION_PLAN.md` describes the mechanism as the "wood wide web" and states as fact that
the connections "were never fully restored"; the shipped runtime supersedes both, and the game's own content
suite asserts against that wording. The packet follows the runtime.

## Working on this case

Serve the repository root and open the central editor:

```bash
python3 apps/curriculum-editor/serve.py
```

Then open <http://127.0.0.1:8000/apps/curriculum-editor/?case=SSS-C2-CASE06>.

Validation:

```bash
python3 apps/curriculum-editor/tests/validate_case06_campaign2.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE06
python3 apps/curriculum-editor/tests/run_browser_tests.py
python3 apps/curriculum-editor/tests/run_pdf_tests.py
```
