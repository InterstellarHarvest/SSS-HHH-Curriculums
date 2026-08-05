# SSS Campaign 2 · Case 02 — The Missing Dance

Draft native curriculum package. Package ID `SSS-C2-CASE02`, runtime ID `missing_dance`.

| Field | Value |
|---|---|
| Title | The Missing Dance |
| Runtime investigation | Ares Botanical Garden |
| Location | Olympia District |
| Subtitle | Campaign 2 · Case 02 · Olympia District, Mars |
| Institutional identity | Space Sprout Sleuth / Solar Agricultural Agency (SAA) |
| Version | 1.0 |
| Lifecycle | `DRAFT` — owner review not started, print gate not run |
| Frozen game baseline | recorded in `source/task-registry.js` as `gameCommit` |

## Contents

```text
case-02-missing-dance/
├── README.md
└── source/
    ├── case-package.json
    ├── content.html
    ├── layout-overrides.json
    ├── presentation.css
    └── task-registry.js
```

No `history/` directory exists while the case is `DRAFT`, and no generated PDF, role document,
or screenshot is committed for this case.

## Instructional shape

Eight tasks, in this order and with these identifiers across all four roles:

1. Rule Things Out
2. Shake, Don't Touch
3. Look Inside the Flower
4. Ask Without Asking
5. Connect the Five Evidence Sources
6. Diagnose and Reject Alternatives
7. Explain the Diagnosis with CER
8. Specify a Safe Trial

Role page counts: Student 5, Teacher 8, Answer Key 4, Accessible 8. The Accessible edition runs
one task per page, which puts the Claim-Evidence-Reasoning frame on a page of its own.

The sequence is derived from this case's own reasoning demands rather than reused. Tasks 1 to 4
are specific to it: a repeated *negative* result is the sharpest evidence here, the thing that is
missing is an event rather than an object, and a knowledgeable source is bound by a cultural
constraint that the investigation has to work with rather than around.

## Science boundary

`source/task-registry.js` is the ledger of record. It carries the five formal clues and their task
coverage, the numerical ledger, the source-status split between established buzz-pollination
science and case-specific evidence, the correct diagnosis and its three rejected alternatives, the
prohibited claims, and the figure provenance. Case-scoped assertions in
`apps/curriculum-editor/tests/validate_case02_campaign2.py` enforce that ledger against the
printable content.

Three rules dominate the case and are enforced mechanically:

- the cone's pores are **already present**. No role may describe them as opening, unsealing or
  sealed, and the pollen is retained rather than blocked;
- **124 Hz is never sufficient on its own**. Every mention sits beside amplitude, duration and
  coupling, and stays a measurement for this species rather than an Earth or universal figure;
- honeybees do not perform floral buzzing, and floral buzzing is not limited to bumblebees.

The Earth mechanism (a bee gripping and vibrating a flower) and the case mechanism (a hovering
moth coupling airborne oscillation into a flexible cone) both move pollen through pores that already
exist, but they are different routes and the packet keeps them distinct.

Task 2 uses a salt shaker with invented grain counts, marked `data-analogy` and stated on the page
as not being measurements from the garden. Validation enforces that marking and that the invented
counts never appear outside the block.

## Working on this case

Serve the repository root and open the central editor:

```bash
python3 apps/curriculum-editor/serve.py
```

Then open <http://127.0.0.1:8000/apps/curriculum-editor/?case=SSS-C2-CASE02>.

Validation:

```bash
python3 apps/curriculum-editor/tests/validate_case02_campaign2.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 shared/validation/validate_layout_overrides.py --case SSS-C2-CASE02
python3 apps/curriculum-editor/tests/run_browser_tests.py
```
