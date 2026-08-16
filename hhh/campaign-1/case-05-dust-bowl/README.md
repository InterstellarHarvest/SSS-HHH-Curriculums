# HHH Campaign 1 · Core Case 05 — The Dust Bowl

**Case ID:** `HHH-C1-CASE05`
**Runtime title:** The Dust Bowl
**Instructional type:** `CORE_CASE`
**Game source:** Campaign 1 · Level 5
**Version:** 0.1
**Status:** `VALIDATION_BUILD` — first reviewable candidate, not released

The fifth full historical Core Case in Hunger, Harvest, & History. Produced against
the released Core Case 04 baseline `661c5c0caad2e6996dff20f86c7565d19116b1ec` and
the approved Blueprint, and against the integrated game baseline
`d9fc16baf272cb543c29cbd0c06ec85efad60be8`.

## Candidate state

| Gate | State |
| --- | --- |
| Package status | `VALIDATION` |
| Owner review | `OWNER_REVIEW_NOT_STARTED` |
| Print status | `NOT_RUN` |
| Release record | none — no `release-v0.1.json` exists at candidate stage |
| Approval record | none |

Production is HTML-only. No canonical PDF artifact exists, PDF generation is not a
release gate, and any PDF exported from the browser is noncanonical and carries no
accessibility guarantee.

## Central learning goal

Explain the Dust Bowl through the interaction among drought, the removal of
prairie cover, wind erosion, land use, and the conservation and policy response.

The central student move is that **a case with two causes cannot be answered by
choosing one of them** — and that the failure runs in both directions. A learner
who leaves believing it was only the weather has missed the case; a learner who
leaves believing the drought was irrelevant has missed it just as completely, and
that second failure is the one this packet is built around.

## The causal frame

Every role carries the same four labelled roles plus one feedback relation. The
frame is declared in `task-registry.js` under `causalFrame` and is marked in
`content.html` with `data-causal-role`, so it can be validated structurally rather
than inferred from prose.

| Role | Gloss | In this case |
| --- | --- | --- |
| `CONDITION` | what arrived | the drought of the 1930s |
| `VULNERABILITY` | what the land was already like | prairie sod broken for cropland, bare between crops |
| `MECHANISM` | how the soil actually left | wind erosion, which requires both of the above |
| `RESPONSE` | what was done about it | conservation practice and the Soil Conservation Act |
| *feedback* | mechanism → condition | bare ground and dust amplified the drought (modelled) |

Giving the drought a named slot is the structural discharge of
`HHH-GAME-C1L5-002`. It cannot quietly disappear from a role that every document
prints.

## Structure

Nine tasks, derived from the Dust Bowl rather than from an earlier case's shape:

| # | Task | Function |
| --- | --- | --- |
| 1 | Build the Case Vocabulary | reference / vocabulary |
| 2 | Record a First Explanation | provisional interpretation |
| 3 | Locate the Plains and Read the Drought | geographic and climatic context (H3) |
| 4 | Trace How Soil Leaves a Field | soil and erosion system (H8) |
| 5 | Read the Fence Line | controlled comparison / evidence analysis |
| 6 | Build the Causation Map | multiple causation (H5) |
| 7 | Order the Response | policy and response sequence (H11) |
| 8 | Weigh Five Claims | competing interpretations |
| 9 | Explain the Dust Bowl | culminating product, with transfer as Part D |

All four Blueprint-named families for this case are present: H5 at Task 6, H8 at
Task 4, H3 at Task 3 and H11 at Task 7.

There is no separate tenth transfer task. The transfer operation is the same
operation Parts A to C assess, and it is carried as Part D of the culminating
product rather than re-measured on a page of its own.

Canonical CER is deliberately **not** used. The Blueprint names a *qualified
multi-causal explanation* as this case's product, and a single claim-evidence-
reasoning frame would collapse four causal roles and a feedback relation into one
claim — which is the error the case exists to refuse.

### Task 3 comes before the land-use evidence, on purpose

Ordering is an argument here. A class that meets the ploughing first hears the
drought as the excuse it was actually used as in 1935 and spends the rest of the
case dismissing it. A class that first reads a fourteen-year, continent-wide
drought out of a government record cannot dismiss it later. The Teacher Guide
names cutting Task 3 as the one cut that changes the lesson.

### Role page counts

| Role | Pages | Why |
| --- | --- | --- |
| Student | 10 | 1 vocabulary, 2 dossier pages carrying seven sources, 6 task pages one per reasoning operation with its figure, 1 culminating |
| Teacher | 8 | the shared seven-function contract, with Function 7 split across pages 7 and 8 because the nine-row source ledger and the complete fallback map cannot share one page without dropping the ledger below a readable size |
| Answer Key | 6 | completed exemplars for all nine keyed tasks, with the three boundary floors written out |
| Accessible | 17 | content-driven: the dossier chunks across four pages, and Tasks 3, 4, 5 and 6 each split their figure from their constructed responses so no answer requires a page-flip |

Roles and page counts: Student 10 · Teacher 8 · Answer Key 6 · Accessible 17.

## Figures

Four, all curriculum-original, all grayscale-safe, none requiring colour.

- **The region diagram** (`data-region-contract`) — three nested bands: the
  drought, the Great Plains, and the worst-hit core. It is deliberately **not a
  map**: no source in this packet supplies a surveyed boundary for the area that
  blew away, so the figure commits only to containment and relative size, and its
  printed note refuses every reading the shape cannot bear. The size difference
  between the outer band and the inner box *is* the argument — a continental dry
  area and a concentrated blowing area, which is what makes a second cause
  necessary.
- **The erosion system** (`data-erosion-contract`) — the soil profile beside the
  transport sequence, with the four printed conditions wind erosion requires. Two
  stages are learner responses. The four core readings sit in a definition list so
  a learner can see all four at once and notice that not one of them says *none*.
- **The causation map** (`data-causation-contract`) — four roles at identical
  width, because no source in this packet ranks them. The feedback is held below
  the row with its own printed word rather than drawn as a curved arrow, because a
  modelled relation should not look like the four observed roles above it.
- **The policy sequence** (`data-sequence-contract`) — six entries, first and last
  fixed. Entry 6 is the argument: the rains returned across the same years the
  conservation programme spread, and the warning is printed inside the rail rather
  than in the caption, because the confound is evidence and not a remark.

## The two audit boundaries

### `HHH-GAME-C1L5-001` — subsoil, resolved game-side, taught curriculum-side

`RESOLVED_VERIFIED` at the integrated game baseline. The zero-life and zero-growth
absolutes the Phase 1 audit rejected were replaced in the game before this package
was authored, and the readings a learner now meets are bounded comparatives: *a
trace*, *far below the range of living topsoil*, *broken down*, *far too little to
carry a crop*.

This package does not merely avoid the old wording. It **teaches the distinction**:
Task 4 Part C asks directly what those readings do and do not establish, and Task 8
Claim 4 makes the absolute reading a claim to be refused. The Answer Key carries an
explicit floor and the rubric carries another.

The runtime clue identifier for the core source is named in the audit resolution as
non-player-facing and was deliberately left unchanged in the game. It is prohibited
from every role of this package, along with every other runtime clue tag, source
key, location id and node name; a guard enforces the whole list.

### `HHH-GAME-C1L5-002` — drought, discharged structurally

`CURRICULUM_QUALIFICATION_REQUIRED`, and treated as a design requirement rather
than a disclaimer. The runtime level's summing-up presses hard in one direction —
the drought *only pulled the trigger*, and in one line *didn't cause this*. As
rhetoric against the "act of God" excuse of 1935 that is doing honest work; as
history handed to a thirteen-year-old it produces the overcorrection the case is
named for.

It is discharged in five places rather than one: the drought holds a named causal
role in every document; Task 3 establishes it on the instrumental record before land
use is mentioned; Task 4 Part B assigns it a named condition of the mechanism, and
requires a *different* condition for the ploughing; Task 6 Part B makes the learner
write what happens without it; and Task 8 Claims 2 and 3 are opposites that are
both marked **N**.

## Source estate

**Twelve** canonical sources in `task-registry.js` under `caseSources`, carrying
**four** distinct evidentiary statuses — `documented` (5), `modeled` (5),
`reconstructed` (1) and `debated` (1). Every learner-facing STATUS line is bound to
one of them by `data-source-id`, and the Teacher source ledger covers all twelve in
**nine printed rows**: the four curriculum-original figures share a single row under
a declared grouping rule (`data-ledger-grouping`), because they have the same
author, the same status and the same limitation class.

| Source | Origin | Status |
| --- | --- | --- |
| The Archive's plains (C1 L5) | game reconstruction | `reconstructed` |
| NOAA NCEI drought record | government climate record | `documented` |
| SCS erosion surveys and plough-up figures, via Coppess 2019 | modern scholarly synthesis | `documented` |
| Wind-erosion science, UNL Extension | established science | `documented` |
| Soil Conservation Act, 49 Stat. 163 | real historical primary source | `documented` |
| Cook, Miller & Seager 2009 (PNAS) | peer-reviewed modelling | `modeled` |
| Worster 1979 / Cunfer 2005 | scholarly disagreement | `debated` |
| Mullins, *Okie Migrations* (OHS) | reference work by a named historian | `documented` |
| Region diagram | curriculum-original | `modeled` |
| Erosion system figure | curriculum-original | `modeled` |
| Causation map | curriculum-original | `modeled` |
| Policy sequence | curriculum-original | `modeled` |

Two **supporting references** are carried inside the row of the source they
corroborate: Schubert and others 2004 under the modelling study, for the drought's
ocean origin; and Gregory 1989 under the encyclopedia entry, as the standard study
behind its account of migrant origins. Neither supplies learner-facing evidence.

### Things this packet deliberately does not print

- **An exact date for Bennett's testimony.** That he testified for the bill in the
  spring of 1935, that dust off the plains reached Washington more than once that
  spring, and that the Act was approved on 27 April are documented. The dramatic
  version — that he stalled until the dust arrived on cue — is told by USDA itself,
  but published accounts give different dates for the decisive appearance and dust
  had already reached the capital earlier that spring while hearings were under way.
  The packet prints the season. The Teacher Guide records the disagreement.
- **A total for the shelterbelt programme.** Published totals differ substantially
  between accounts, so the sequence names the programme by its dates and purpose.
- **Any numerical apportionment of the causes.** No source in this packet says the
  drought was some percentage of it and the ploughing the rest, so the causation map
  assigns no weights and the rubric does not reward a learner for inventing them.

## Declared Accessible adaptations

Four, all declared in `task-registry.js` under `accessibleAdaptations` and printed
in the Teacher scoring note:

1. **Task 5** — the COVER row is supplied complete on both sides as a worked model.
   The Accessible learner completes **eight** cells; the Student learner completes
   ten. The row that carries the reasoning is THE DRY YEARS, and it is the
   learner's in both editions.
2. **Task 6** — two of the eight factor cards are pre-placed, one in CONDITION and
   one in RESPONSE. The Accessible learner places **six**. No role is completed for
   them, and the condition-against-vulnerability judgement is untouched. The
   feedback relation is printed on the map in **both** editions and is graded in
   neither, so it is not a difference between them; Parts B and C are identical.
3. **Task 7** — the Accessible rail repeats each slot's date, so ordering is a
   matching operation rather than a recall one. Part B is unchanged.
4. **Task 8** — each claim carries a printed pointer to the source that bears on
   it. The pointer names a source; the mark is still a judgement.

No Student answer space was reduced anywhere to pay for these supports, and every
Accessible response field is sized above its Student equivalent.

Parity between the editions is not asserted in prose. `task-registry.js` carries an
`editionResponseContract` naming, for every assessed subpart, the exact response
ids each edition collects and which of four difference classes applies —
`parity`, `declared-reduction` (registered against one of the four adaptations
above), `chunking` (a presentation split with an identical obligation), or
`accessible-only`, which is prohibited. The validator checks live markup against
that contract in both directions, so an Accessible edition cannot acquire a
required response the Student edition never asks for.

## No-game fallback

Complete. Every assessed task is answerable from the printed dossier and the four
figures. Teacher page 7 carries the task-by-task fallback map and the list of
load-bearing facts carried in **both** learner editions.

## Semantic regression contract

The case carries a scoped validator,
[`apps/curriculum-editor/tests/validate_hhh_case05_dust_bowl.py`](../../../apps/curriculum-editor/tests/validate_hhh_case05_dust_bowl.py),
chained into static validation. It enforces five bounded contracts — subsoil,
drought, land use, policy and source status — and each pairs a **negative** guard
over a closed class of language with a **positive** structural requirement that the
correct framing is actually present.

The design is a deliberate response to Case 04's experience. Karlsruhe's catalyst
guard began as a blacklist of verbs meaning *increase* and could not converge,
because reviewers kept finding new ways to say it; it had to be rebuilt fail-closed
around a registered fingerprint set. Case 05 avoids that spiral by never policing an
ordinary verb. Its prohibited classes are **absolutes** (*dead*, *lifeless*,
*sterile*, *nothing grows*), **sole-cause markers** (*alone*, *only*, *solely*),
**denials** (*did not cause*, *made no difference*) and **termination verbs**
(*ended*, *stopped*, *cured*) — each a small closed class in English rather than an
open synonym family. Where a boundary could not be policed that way it is enforced
**structurally** instead: the drought's presence as a cause is checked by requiring
`data-causal-role="condition"` in every role, not by reading prose.

Every guard ships with both a **negative control** (a synthetic fragment that must
fail) and a **positive control** (the real package, which must pass), so a guard
that silently stops working is itself a failure. Exemptions are closed and
registered in `task-registry.js`; markup cannot authorise its own sentence.

The validator also protects **accessibility text as a factual surface**: each
figure's `aria-label` is checked against the same contracts as its visible content,
so the causation map's description must name all four roles and the feedback, and
the erosion figure's description may not describe the subsoil in absolutes.

### The subsoil guard is self-sufficient, and the registry drives it

The subsoil contract's negative half is declared in
`subsoilBoundary.prohibitedConceptClasses` as two classes — **biological zero**
and **universal growth zero** — and marked `selfSufficient`. That word carries the
correction: a biological-zero predicate *is itself* the boundary violation when the
subject is the protected layer, so no second life-or-growth token is required. An
earlier form of this guard demanded subject **and** a separate life token **and**
an absolute, and every direct characterization walked through it — "the subsoil is
dead" carries no second life token, because the predicate is the claim.

The eighteen phrases in `subsoilBoundary.prohibitedFramings` are a diagnostic
register, not the matcher; a phrase list cannot be completed. They are
**reconciled** instead: the validator binds each declared phrase to a protected
subject and asserts the concept classes catch it, so the declared contract and the
enforced contract cannot drift apart. There is no second, hand-maintained list in
the validator — the removal of that duplicate is itself asserted.

The positive half, `BOUNDED`, is deliberately **permissive** and asymmetric to the
negative half: it fires only when a life-or-growth claim about the protected layer
carries no comparative frame at all, and any `comparativeMarkers` entry clears it.
A marker missing from that list therefore weakens a secondary diagnostic and can
never open the zero-class hole. Scope stays on the protected subject: a *dead
field* at the surface is outside this contract and is not a violation of it.

## Preservation

This package adds files under `hhh/campaign-1/case-05-dust-bowl/`, adds one
validator, and changes one registry entry and the browser-harness coverage roster.
Nothing under `sss/`, `hhh/audit/`, `hhh/blueprint/`, `hhh/production/`, Archive
Orientation, Case 01, Case 02, Case 03 or Case 04 is modified.
