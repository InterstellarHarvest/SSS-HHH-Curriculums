# SSS Campaign 2 · Case 01 — Heavy Hands

Released native curriculum package. Package ID `SSS-C2-CASE01`, runtime ID `heavy_hands`.
The current release is the v1.1 corrective release; v1.0 is the prior approved release and its
history records are retained unchanged.

| Field | Value |
|---|---|
| Title | Heavy Hands |
| Runtime investigation | Vressk Centrifuge Habitat |
| Location | Kepler-442b Orbit |
| Subtitle | Campaign 2 · Case 01 · Kepler-442b Orbit, Vressk Territory |
| Institutional identity | Space Sprout Sleuth / Solar Agricultural Agency (SAA) |
| Version | 1.1 (corrective release of 1.0) |
| Lifecycle | `APPROVED_STABLE` — owner approved 2026-08-06, print gate PASS at 100% / Actual Size. The prior v1.0 release was approved 2026-08-04 and its records are retained unchanged |
| Frozen game baseline | recorded in `source/task-registry.js` as `gameCommit` |

Case 03 was produced first as the Campaign 2 pilot. This case keeps its canonical runtime
number and is registered as Case 01, ahead of Case 03 in the Campaign 2 case list.

## Contents

```text
case-01-heavy-hands/
├── README.md
├── history/
│   ├── CASE01_OWNER_APPROVAL_v1.0.md   retained byte-identical
│   ├── CASE01_OWNER_APPROVAL_v1.1.md
│   ├── release-v1.0.json               retained byte-identical
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

1. Frame What Has Already Been Tested
2. Ride the Merry-Go-Round
3. Think Like the Investigator
4. Why the Biggest Tubers Bend Most
5. Connect the Five Evidence Sources
6. Diagnose and Reject Alternatives
7. Explain the Diagnosis with CER
8. Write the Missing Habitat Specification

Role page counts: Student 5, Teacher 9, Answer Key 4, Accessible 8. The Accessible edition runs
one task per page, which puts the Claim-Evidence-Reasoning frame on a page of its own, with six
sentence starters and a pointer to the pages holding the evidence.

## Science boundary

`source/task-registry.js` is the ledger of record. It carries the five formal clues and their task
coverage, the exact numerical ledger, the source-status split between established physics and
case-specific evidence, the correct diagnosis and its three rejected alternatives, the prohibited
claims, and the figure provenance. Case-scoped assertions in
`apps/curriculum-editor/tests/validate_case01_campaign2.py` enforce that ledger against the
printable content.

It also carries the ledgers added by the v1.1 correction: `historicalControls` (which conditions
the game reports as changed between plantings, which are reported only as present values, and the
rule that a present reading never rules a condition out), `learnerEvidencePolicy` (which values are
supplied to learners, which are withheld, and which are Teacher-only), `standards` with the exact
learner evidence each retained claim rests on, and `withdrawnStandards`.

Three rules dominate the case and are enforced mechanically:

- the reported direction is radially outward at every sampled radius, so no role may describe the
  apparent gravity as tilting, rotating or reversing across the bed — the difference is one of
  magnitude only;
- no role may assert that the habitat is calibrated too strong, that Earth crops detect a
  difference of this size, or that a larger ring is guaranteed to fix the crop;
- no role may present nutrients, light or water as a variable that was changed, tested, verified or
  ruled out — the game reports them only as present conditions — and `Ring Status: NOMINAL` may not
  be expanded into unreported absences;
- every graded Answer Key expectation and every clause of the CER exemplar must be producible from
  the Student edition alone and, independently, from the Accessible edition alone;
- the packet requires no calculation anywhere, and learners never meet `a = ω²r`. The habitat's own
  readings differ by less than a tenth of one percent, because a 20 cm bed sits inside a 224.9 m
  radius; a ring with a classroom-friendly spread would need a radius of about two metres — roughly four
  metres across — and would have to spin near 30 RPM. Task 2 therefore teaches the relationship with a merry-go-round and three
  invented values, and the reported readings appear as reference evidence in a case file rather than
  as arithmetic. The `0.0018 g` / `0.00187 g` rounding relationship is Teacher-facing only.

The Task 2 analogy is marked `data-analogy` and states on the page that its values are not
measurements from the habitat. Validation enforces both that marking and that the invented values
never appear outside the block.

Alternatives the packet lists in order to reject them are marked `data-candidate-claim`, and
misconceptions quoted in the Teacher Guide so they can be corrected are marked `data-quoted-claim`.
Both are excluded from the prohibited-claim scan, which therefore measures what the packet asserts
rather than what it corrects.

## Standards

Claimed: MS-LS1-5 direct (Tasks 1 and 7), MS-ETS1-1 direct (Task 8), MS-ETS1-2 supporting and
conditional on whether the class runs the Task 8 comparison systematically. `MS-ETS1-3` was claimed
in v1.0 and is **withdrawn** in v1.1: the Concord records that justified it are Teacher-facing, no
task asks students to analyse several design solutions, and no standard replaces it. No mathematics
standard is claimed. The exact learner evidence behind each retained claim is recorded in
`source/task-registry.js` under `standards`.

## Working on this case

Serve the repository root and open the central editor:

```bash
python3 apps/curriculum-editor/serve.py
```

Then open <http://127.0.0.1:8000/apps/curriculum-editor/?case=SSS-C2-CASE01>.

Validation:

```bash
python3 apps/curriculum-editor/tests/validate_case01_campaign2.py
python3 apps/curriculum-editor/tests/test_case01_mutations.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE01
python3 apps/curriculum-editor/tests/run_browser_tests.py
python3 apps/curriculum-editor/tests/run_pdf_tests.py
```
