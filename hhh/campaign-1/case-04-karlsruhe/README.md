# HHH Campaign 1 · Core Case 04 — Karlsruhe

**Case ID:** `HHH-C1-CASE04`
**Runtime title:** Karlsruhe
**Instructional type:** `CORE_CASE`
**Game source:** Campaign 1 · Level 4
**Version:** 0.1
**Status:** `APPROVED_STABLE` — released 2026-08-15

The fourth full historical Core Case in Hunger, Harvest, & History, released at v0.1 on
2026-08-15. Produced against the released Core Case 03 baseline
`674052ac6935a4a386281ba6542cbb522ed75d04` and the approved Blueprint.

## Release state

| Gate | State |
| --- | --- |
| Package status | `APPROVED` |
| Owner review | `OWNER_REVIEW_PASS` — Nate / Owner, 2026-08-15 |
| Print status | `PASS` — owner physical print at 100% / Actual Size |
| Release record | [`history/release-v0.1.json`](history/release-v0.1.json) |
| Approval record | [`history/CASE04_OWNER_APPROVAL_v0.1.md`](history/CASE04_OWNER_APPROVAL_v0.1.md) |

**Owner-approved printable baseline:** `29b34b31ab5b553093e134fcedb5a41b07b2c4f8`.
Release conversion left `content.html`, `presentation.css` and `layout-overrides.json`
byte-identical to that commit; only `task-registry.js` moved, and only in its two lifecycle
keys, neither of which renders. The release record pins the commit whose tree first carries
the released certified bytes, which is the release-conversion commit rather than the
printable baseline; the two are recorded separately and deliberately.

Production is HTML-only. No canonical PDF artifact exists, PDF generation is not a release
gate, and any PDF exported from the browser is noncanonical and carries no accessibility
guarantee.

## Central learning goal

Explain the pressure, temperature, catalyst and recycle tradeoffs that made
ammonia synthesis workable, and place Haber's laboratory result and Bosch's
industrial scale-up in the correct historical relationship.

The central student move is that **a scientifically possible reaction is not
automatically an industrially workable technology**.

## Structure

Eight tasks, derived from Karlsruhe rather than from an earlier case's shape:

| # | Task | Function |
| --- | --- | --- |
| 1 | Build the Case Vocabulary | reference / vocabulary |
| 2 | Record a First Explanation | provisional interpretation |
| 3 | Read the Two Tradeoffs | mechanism and tradeoff (H8) |
| 4 | Complete the Process Loop | process / system (H8) |
| 5 | Sort the Work and Put It in Order | technology sequence and attribution (H11) |
| 6 | Decide What Each Source Can Show | evidence / source distinction (H4) |
| 7 | Weigh Five Claims | competing interpretations |
| 8 | Explain What Made the Process Workable | culminating product, with transfer as Part D |

There is no separate ninth transfer task. The transfer operation is the same
operation Parts A to C assess, and it is carried as Part D of the culminating
product rather than re-measured on a page of its own.

Canonical CER is deliberately **not** used. The reasoning this case assesses is
that several things had to be true at once and several people made them true; a
single claim-evidence-reasoning frame would collapse that.

### Role page counts

| Role | Pages | Why |
| --- | --- | --- |
| Student | 8 | 1 vocabulary, 2 dossier pages carrying the six learner-facing sources (one of them a real patent), 4 task pages one per reasoning operation with its figure, 1 culminating |
| Teacher | 7 | the shared seven-function Teacher contract |
| Answer Key | 6 | completed exemplars for all eight keyed tasks, with the two boundary floors written out |
| Accessible | 14 | content-driven: the dossier chunks across three pages, and Tasks 3, 4 and 5 each split their figure from their constructed responses so no answer requires a page-flip |

Roles and page counts: Student 8 · Teacher 7 · Answer Key 6 · Accessible 14.

## Figures

Three, all curriculum-original, all grayscale-safe, none requiring colour.

- **The tradeoff panel** (`data-tradeoff-contract`) — two levers, each with what
  it buys and what it costs, plus the **temperature ladder**. The ladder is the
  audit-required device: it places the 400–500 °C operating range against lead's
  melting point of 327 °C so that "compromise" cannot be read as ordinary
  warmth. It draws **no curve**, because no source in this package supplies the
  measured values a curve would need.
- **The process loop** (`data-process-contract`) — six stages closing into a
  recycle. Three are given, three are learner responses. Every arrow is a
  movement of gas that a source describes.
- **The technology sequence** (`data-sequence-contract`) — three lanes at equal
  width: the laboratory, the catalyst search, and the plant. Equal weight is the
  argument; a figure that drew the plant lane as a footnote would make the claim
  the packet spends two tasks refuting.

## Declared Accessible adaptation

In **6 · Decide What Each Source Can Show**, the Accessible edition supplies row
one complete as a worked model. The Accessible learner therefore classifies
**four** rows and completes **twelve** cells independently; the Student learner
classifies five and completes fifteen. This is a modelled row under the
Accessible Adaptation Contract, not a disclosed answer, and it is documented
everywhere it is scored: on the Accessible page itself, in the Teacher access
supports, in the Teacher scoring note, and in the Answer Key. No Student answer
space was reduced to pay for it, and a guard prevents any role from claiming
that nothing is disclosed while the prefill exists.

## Game dependencies

Both Case 04 entries in the game-remediation dependency tracker are addressed
**curriculum-side**. No game edit is required for this package and none was made.

- **`HHH-GAME-C1L4-001`** (nonblocking polish) — the malformed word in the Level 4
  pressure field-note summary was verified as still present in the game bytes at
  `d9fc16b`. The faulty wording is **not reproduced anywhere in this package**;
  where the idea is needed it is paraphrased accurately. Teacher page 3 tells the
  teacher what a student on the game route may see and that it is a typing error.
- **`HHH-GAME-C1L4-002`** (curriculum qualification required) — treated as a
  design requirement rather than a disclaimer. It shapes the tradeoff figure and
  its ladder, Task 3 Parts C and D, Task 4 Part B, Task 5, Task 7 Claims 2 to 4,
  the Teacher qualification note, the misconceptions table, both Answer Key
  floors, and rubric criteria 1 to 3.

## Source estate

**Eight** canonical sources in `task-registry.js` under `caseSources`, carrying
**four** distinct evidentiary statuses across them — `documented` (4),
`modeled` (2), `reconstructed` (1) and `estimated` (1). Every learner-facing
STATUS line is bound to one of them, and the Teacher source ledger covers all
eight in **seven printed rows**: the two curriculum-original figures share a
single row under a declared grouping rule (`data-ledger-grouping`), because they
have the same author, the same status and the same limitation class. A parity
guard checks ledger coverage against the canonical estate in both directions.

One **supporting reference** is carried: BASF's own corporate chronology for
1913, which corroborates the attribution split from the industrial party's side.
It supplies no learner-facing evidence, so it is printed inside the Travis row
rather than registered as a canonical source of its own.

| Source | Origin | Status |
| --- | --- | --- |
| The Archive's laboratory | game reconstruction | `reconstructed` |
| Haber and Le Rossignol, US Patent 1,202,995 | real historical primary source | `documented` |
| Travis 2015 (RSC Historical Group) | modern scholarly | `documented` |
| Appl 1997 (IFA) | modern institutional / technical | `documented` |
| Established equilibrium chemistry | established science | `documented` |
| Erisman and others 2008 | peer-reviewed estimate | `estimated` |
| The process loop figure | curriculum-original | `modeled` |
| The tradeoff panel | curriculum-original | `modeled` |

The two scholarly sources **disagree on the date of the 1909 demonstration**.
That disagreement is real, is printed on both cards, and is the evidence for
Task 6 row three and Task 7 Claim 5. The year is documented; the date is not.

They also use **8%** differently, and the packet keeps the two apart: Travis
reports a figure Haber **calculated** in advance (about 8% at 600 °C and 200
atmospheres); Appl reports a result **obtained** with osmium (about 8% by volume
at 175 bar and 600 °C). Bar and atmospheres are not treated as interchangeable
and no conversion is performed between them.

The **15 / 98** conversion figures are printed as **reported worked examples for
one typical plant**, never as constants: the source supplying them states that
the single-pass figure varies from plant to plant, and the packet says so in
both learner editions.

## No-game fallback

Complete. Every assessed task is answerable from the printed dossier and the
three figures. Teacher page 7 carries the task-by-task fallback map and the list
of load-bearing facts that are carried in **both** learner editions.

## Semantic regression contract

The case carries a scoped validator,
[`apps/curriculum-editor/tests/validate_hhh_case04_karlsruhe.py`](../../../apps/curriculum-editor/tests/validate_hhh_case04_karlsruhe.py),
chained into static validation. Beyond the ordinary structural guards it enforces five
bounded semantic contracts — temperature, catalyst, attribution, recycle and demonstration
date — and the catalyst contract is the strictest of them.

The catalyst guard is **fail-closed**. Any sentence in any role that names a catalyst and
names ammonia must resolve to one of exactly three things: an approved function (rate,
pathway, or a bound-invariant no-shift statement), a registered descriptive claim identified
by the SHA-256 fingerprint of its normalised text, or a registered evaluative exemption.
Anything else fails, whatever verb it uses. That design replaced an open blacklist of wrong
verbs, which could not converge: reviewers kept finding new ways to say *increases the yield*.
Internal punctuation cannot create a safety boundary — sentences are split on terminal
punctuation only, with decimal and initial guards — so a semicolon or an em dash cannot sever
a catalyst from the product claim it governs. Registration is by fingerprint rather than by
markup, so no attribute in `content.html` can authorise its own sentence.

## Preservation

This package adds files under `hhh/campaign-1/case-04-karlsruhe/` and changes one
registry entry. Nothing under `sss/`, `hhh/audit/`, `hhh/blueprint/`,
`hhh/production/`, Archive Orientation, Case 01, Case 02, Case 03 or Case 05 is
modified.
