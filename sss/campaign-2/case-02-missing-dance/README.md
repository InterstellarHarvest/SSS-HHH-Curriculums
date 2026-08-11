# SSS Campaign 2 · Case 02 — The Missing Dance

Approved corrective release. Package ID `SSS-C2-CASE02`, runtime ID `missing_dance`.

Version **1.1** corrects the defects the Campaign 2 completion audit recorded against v1.0. The approved v1.0
release remains in `history/` and is not rewritten: `release-v1.0.json` and `CASE02_OWNER_APPROVAL_v1.0.md`
continue to describe the v1.0 content that passed its own owner and print gates. v1.0 is superseded, not
withdrawn.

| Field | Value |
|---|---|
| Title | The Missing Dance |
| Runtime investigation | Ares Botanical Garden |
| Location | Olympia District |
| Subtitle | Campaign 2 · Case 02 · Olympia District, Mars |
| Institutional identity | Space Sprout Sleuth / Solar Agricultural Agency (SAA) |
| Version | 1.1 (corrective release; 1.0 retained in `history/`) |
| Lifecycle | `APPROVED_STABLE` · `OWNER_REVIEW_PASS` · print `PASS` · approved 2026-08-10 |
| Frozen game baseline | recorded in `source/task-registry.js` as `gameCommit` |

## What v1.1 corrects

- **Task 1 usability.** Both learner editions now carry a writable `OK or ?` mark cell on every row,
  and the directions name the table the packet actually prints. The Answer Key mirrors that table
  row for row, and the Teacher Guide describes the same six rows.
- **Evidence availability.** The 100–150 Hz comparison band and the Telluvian lyre-moth wingbeat,
  which the Answer Key graded against but no learner edition carried, are now in both learner
  editions. `Poricidal anther` and `buzz pollination` are defined for learners.
- **Standards.** MS-LS2-2 and MS-ETS1-3 withdrawn; neither is met by what the packet asks.
- **Pagination.** Student went 5 → 6 pages so Task 1 has its own page. Accessible held 8.

Nothing about the investigation, diagnosis, task sequence or case fiction changed.

## Contents

```text
case-02-missing-dance/
├── README.md
├── history/            the current v1.1 release, and the retained v1.0 it supersedes
│   ├── CASE02_OWNER_APPROVAL_v1.0.md
│   ├── CASE02_OWNER_APPROVAL_v1.1.md
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

1. Rule Things Out
2. Shake, Don't Touch
3. Look Inside the Flower
4. Ask Without Asking
5. Connect the Five Evidence Sources
6. Diagnose and Reject Alternatives
7. Explain the Diagnosis with CER
8. Specify a Safe Trial

Role page counts: Student 6, Teacher 8, Answer Key 4, Accessible 8. The Accessible edition runs
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

The v1.2 final-system release (owner approved 2026-08-10, physical print PASS at 100% / Actual Size on Google Chrome) closes the SSS correctness-remediation and visual-modernization program for this case. The prior release records are retained unchanged in `history/`.

Retained releases: `history/release-v1.1.json` (owner approved 2026-08-06) and `history/release-v1.0.json`, both retained byte-identical alongside their owner-approval records. The current release record is `history/release-v1.2.json`.
