# SSS Campaign 2 · Case 06 — The First Garden

Released native curriculum package. Package ID `SSS-C2-CASE06`, runtime ID `first_garden`.
v1.1 is a corrective release; v1.0 is preserved as the prior approved release and its history
records are retained unchanged.

| Field | Value |
|---|---|
| Title | The First Garden |
| Runtime investigation | The First Garden (`first_garden`) |
| Location | Restored Terrace |
| Subtitle | Earth |
| Campaign position | Campaign 2, case 6 of 6 — bonus finale, hidden until the five main cases are complete |
| Institutional identity | Solar Agricultural Agency (SAA) |
| Version | 1.1 (corrective release) |
| Lifecycle | `APPROVED_STABLE` · `OWNER_REVIEW_PASS` · print `PASS` — owner approved 2026-08-06 |
| Prior approved release | 1.0, owner approved 2026-08-05, print gate PASS at 100% / Actual Size |
| Retained history | `history/release-v1.0.json` and `history/CASE06_OWNER_APPROVAL_v1.0.md`, unchanged |
| Frozen game baseline | `29c3b222c53f51de11a3aa83e896a6d0ef6fb490` |

## Contents

```text
case-06-first-garden/
├── README.md
├── history/
│   ├── CASE06_OWNER_APPROVAL_v1.0.md
│   ├── CASE06_OWNER_APPROVAL_v1.1.md
│   ├── release-v1.0.json
│   └── release-v1.1.json
└── source/
    ├── case-package.json
    ├── content.html
    ├── layout-overrides.json
    ├── presentation.css
    └── task-registry.js
```

No generated PDF, role document, or screenshot is committed for this case at either version.

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

Role page counts: Student 6, Teacher 8, Answer Key 5, Accessible 7. Only Student changed, from 5, to carry
the evidence Task 4 is graded on (see "What v1.1 corrects"). The Accessible CER is
a dedicated page carrying `data-accessible-cer-page="canonical-v1.0"`. In the Student edition the CER shares its
page with Task 7 under `data-student-cer-page="combined-v1.0"`, the same combined form Campaign 1 Case 07 uses:
on its own the CER left roughly half a page empty, and the trial specification reads naturally straight after the
explanation it constrains. That page is unchanged and still fits.

This case carries fewer quantities than Campaign 2 Cases 01–05, because its evidence is different in kind.
Cases 01–05 each turn on a measured value checked against a written specification, and each therefore needs page
area for a quantitative record, a unit-discipline task and a precision ledger. Case 06 reports almost no
quantities: the surveyed patch diameter of approximately four to six metres, the roughly three metres between
thriving and failing ground, and a set of durations. Its reasoning is about scope, elimination and convergence,
and it contains no calculation at all. A precision task and a quantitative comparison figure would both have been
decorative here, so neither exists.

For the same reason the packet carries one figure rather than two, no timeline, and no trend graph. The case
reports no time series and no dated events; there is nothing to plot. Figure A is a plan view: circular patches
where the surveyed compounds are abundant, drawn inside ground where the same compounds fall to trace levels,
because "circular patches of approximately four to six metres in diameter" is what the survey actually reports.
It is not to scale, and it draws no distance between patches, because the survey reports none. Both its caption
and its extended description state that it shows the reported pattern rather than mapping the garden.

What the case does need, and gets, is space for triangulation. No source resolves the investigation alone — this
is the only Campaign 2 case in which every source is a person or an archive, with no sensor panel and no specimen
examination — so Task 4 is the packet's spine. Each of its five sources reports on the learner page, and each
learner then writes that source's contribution and its limit.

## What v1.1 corrects

- **Task 4 graded evidence no learner held.** Three of the five sources had no printed statement in any learner
  edition, and the Answer Key graded against Kess's mechanism, `Section 14.7` and `GC-2201` — the last of which
  appeared nowhere a learner could read. Student Table 5 gains a `Source and what it reports` column; the
  Accessible edition gains the matching Table 5 in plainer register, on the Case 05 model.
- **Accessible Task 1 was unanswerable.** Its table dropped the Student's record column, so no Accessible learner
  could tell which of the nine rows was never tested. The column is restored in shorter register.
- **Task 3's third rejection had no record.** Neither learner edition dated the patchiness, which the
  invasive-organism rejection needs. Both now print that it predates the summit by decades.
- **Figure A carried an unsupported offset.** The plan view kept a dimension line labelled `about 3 m` spanning
  the gap between two patches — Dr. Nova's described bed separation repurposed as a surveyed boundary offset,
  against the packet's own precision ledger. It is removed, along with per-patch metre assignments.
- **The ledger of record described a superseded figure.** `figureProvenance` and `sourceStatus.figures` described
  a twelve-metre strip; they now describe the rendered plan view.
- **Table numbering diverged between learner editions.** The Student vocabulary table was numbered while the
  Accessible equivalent was not, so four Teacher and Answer Key references misresolved for Accessible readers.
  Vocabulary is now an unnumbered aid in both, and every remaining number is an evidence table meaning the same
  record in both editions.
- **The Teacher Guide had not received the owner-review revision.** It described a twelve-metre strip, a full-page
  Student CER, an Accessible edition with identical evidence, and an analogy on Student page 2. All four are
  corrected, and the guide now describes the actual Accessible adaptation.
- **The analogy printed after the task it teaches.** It now prints inside Task 1 in both learner editions,
  as Case 05 places its rain-gauge analogy.
- **Standards overclaimed.** `MS-LS2-2` is withdrawn: its performance expectation predicts patterns across
  multiple ecosystems and this packet holds one restored terrace with two bed histories. `MS-ETS1-2` is withdrawn:
  Task 3 compares explanations, not design solutions. No standard is substituted for either. `MS-ETS1-1` remains
  direct and `MS-LS2-3` supporting, each with its assessed task evidence recorded in `source/task-registry.js`.

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
python3 apps/curriculum-editor/tests/test_case06_mutations.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE06
python3 apps/curriculum-editor/tests/run_browser_tests.py
python3 apps/curriculum-editor/tests/run_pdf_tests.py
```
