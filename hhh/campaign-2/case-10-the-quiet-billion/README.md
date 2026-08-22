# HHH Campaign 2 · Core Case 10 — The Quiet Billion

**Case:** `HHH-C2-CASE10`
**Runtime source:** *Hunger, Harvest, & History*, Campaign 2 Level 3
**Setting:** Mexico and South Asia, 1968 — the Mexican wheat programme, the Norin 10 dwarfing
source, the transfer to South Asia and the Indian wheat record are **historical**; the recovered
record, the two wheats, the pedigree records, Dr. Rao and the Failure Report are **reconstructed**
**Instructional type:** `CORE_CASE`
**Version:** 0.1
**Status:** `APPROVED_STABLE` — released 2026-08-22
**Blueprint:** `hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md`, Core Case 10
**Audit baseline:** `hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md`
**Game commit:** `d9fc16baf272cb543c29cbd0c06ec85efad60be8`

The fourth unit of Campaign 2, and the first HHH case whose culminating product is a
**Qualified Historical Finding** — a five-part finding that has to carry quantitative evidence
with its units, a second documented source, a causal qualification, an explicit statement of what
the evidence does not prove, and a claim about the evidence that would be needed next. Produced
against curriculum main `a64d3ccc104a23ac1be99a435948ed39d09cf967` and the approved Blueprint.

## Release state

| Gate | State |
| --- | --- |
| Package status | `APPROVED_STABLE` |
| Owner review | `OWNER_REVIEW_PASS` |
| Print status | `PASS` |
| Approval date | 2026-08-22 |
| Owner | Nate / Owner |
| Release record | [`history/release-v0.1.json`](history/release-v0.1.json) |
| Approval record | [`history/CASE10_OWNER_APPROVAL_v0.1.md`](history/CASE10_OWNER_APPROVAL_v0.1.md) |

The owner passed both gates and approved the byte set for release. The two statements are
recorded separately and exactly as given, and are **not** combined into a single quotation:

| Gate | Result | Exact owner statement |
| --- | --- | --- |
| On-screen visual and content review | **PASS** | `CASE10_OWNER_SCREEN_REVIEW_PASS` |
| Physical print review | **PASS** | `CASE10_OWNER_PRINT_PASS` |

Their approved interpretation is only that owner on-screen visual and content review passed and
that owner physical print review passed. The owner supplied no browser, printer, print scale,
paper type, paper size, colour or grayscale print mode, print setting or physical-print method,
and none is asserted anywhere in this release; the engineering colour and grayscale render
checks in the release record are a separate internal measurement and are not a description of
the owner's review or print environment.

### Printable baseline and certified-source commit are not the same commit

| | Commit |
| --- | --- |
| **Owner-approved printable baseline** | `990dce582f12d2f726b45b7c039ef0d34adc5c29` |
| **Released certified-source commit** | the release-conversion commit recorded in `history/release-v0.1.json` |

The owner reviewed and printed `990dce5`. Release conversion changes no printable source:
`content.html`, `presentation.css` and `layout-overrides.json` are byte-identical to that commit,
and only `task-registry.js` moves, in its two lifecycle keys, neither of which renders. Because
the released `task-registry.js` bytes first exist at the release-conversion commit, that commit
is the first in this line whose tree carries the complete released four-source byte set, and the
release record's source pins name it rather than the printable baseline. The two are recorded
separately and deliberately, and conflating them is the error this section exists to prevent.

**No owner-approved bundle exists and none is claimed.** The release-history schema requires no
bundle field, and there is no evidence that the owner inspected or approved any bundle file.

### Release provenance

Three linear commits carried this case to owner approval, each reviewed before the next was
authorised.

| # | Stage | Outcome |
| --- | --- | --- |
| 1 | `17f81c1cfe7e19a496af428a90c2793d7986d77b` | Original implementation candidate. |
| 2 | `456ee72a5b0cce4784199a976a794fd215f256f8` | PMO bounded remediation — the Case 09 forward-coupled validator, the Case 10 total sixty-minute route, and the Government of India 2015 edition and table pin. |
| 3 | Full independent review | `CASE10_INDEPENDENT_REVIEW_FAIL` — exactly two `REQUIRED_REMEDIATION` blockers. |
| 4 | `990dce582f12d2f726b45b7c039ef0d34adc5c29` | Independent-review remediation closing both blockers. |
| 5 | Independent remediation verification | `CASE10_INDEPENDENT_REMEDIATION_VERIFICATION_PASS`. |
| 6 | Owner on-screen / content / visual review | **PASS** — `CASE10_OWNER_SCREEN_REVIEW_PASS` |
| 7 | Owner physical print review | **PASS** — `CASE10_OWNER_PRINT_PASS` |

The two blockers were the Task 6 Answer Key's use of an off-route Dr. Rao adoption detail that
was unavailable in the learner editions, and the Task 7 Answer Key's description of India's 12.26
to 20.09 Mt six-year rise as having "nearly doubled". The same review passed the broader
historical, source, design, visual, accessibility and preservation architecture. The remediation
removed the unreachable detail, replaced the magnitude overstatement with the exact endpoints,
added Case 10-local Answer-Key evidence-reachability protection, and hardened the
production-versus-yield semantic protection. No post-owner independent review was commissioned
for Case 10 and none is claimed.

Production is HTML-only. No canonical PDF artifact exists, PDF generation is not a release gate,
and any PDF exported from the browser is noncanonical and carries no accessibility guarantee.

## Game-baseline note

The Phase 1 Master Game Audit read C2 L3 at game commit
`9b8545ed6ecf98b337326390400076e36789e056` and raised one finding against it.

**`HHH-GAME-C2L3-001` is a curriculum qualification**, `CURRICULUM_QUALIFICATION_REQUIRED` and
open at the audited baseline by design. The audit found the core semi-dwarf, lodging and rust
story sound but held that exact field-yield claims and any "one seed saved a billion" shorthand
must not replace broader irrigation, fertiliser and institutional context. This package carries
that qualification in every role and **does not modify the game, reopen the game audit or
initiate game remediation**; the shared remediation tracker is untouched.

Current game main is three commits after the audited baseline. The intervening remediation
affects other levels; C2 L3 carries no substantive post-audit change. The level's shape is
asserted in the scoped validator against the audit's own static content inventory — four
operationally required clues, two insight-flagged sources — rather than against the game, which
this package does not read.

## Central learning goal

Evaluate competing Green Revolution claims by interpreting quantitative wheat evidence,
separating reconstructed game evidence from documented history, and explaining how improved
wheat varieties contributed to production gains within a larger system of agronomy, inputs,
institutions and policy — without treating one statistic or the phrase "saved a billion lives"
as proof of a single cause.

**Guiding question.** How should historians explain the 1960s wheat gains when the numbers rose,
improved varieties mattered, several conditions changed at once, and both the strongest success
story and the strongest failure story claim more than the evidence can prove?

The packet's conclusion is deliberately **more qualified than the game's**. It rejects both
extremes: the overclaim that one seed caused the Green Revolution and therefore saved a counted
number of lives, and the overcorrection that the gains were unreal because the Green Revolution
had environmental, distributional and social costs. What it teaches is that improved semi-dwarf
wheat was an important contributor to large productivity and production gains, realised through
an interacting system, and that a correct agricultural mechanism does not settle questions of
hunger, distribution, environment, policy or human welfare.

## The title boundary

The title is the game's. "A billion lives" is **not** a Case 10 historical statistic, and the
packet never converts the game's language into an observed measurement. Both learner editions
carry this on page 1:

> The title comes from the game. Treat "a billion lives" as a claim that would require a stated
> method and counterfactual, not as a measurement supplied by this packet.

No task asks a learner to calculate, repeat, validate or endorse a numerical lives-saved figure,
no exemplar states one, and the Answer Key refuses one at every level.

## Source status

Three controlled evidence layers, marked in `data-evidence-layer` and printed as the short
`SOURCE STATUS` label the Case 07 amendment requires.

| Layer | Printed label | What it covers |
| --- | --- | --- |
| `reconstructed` | `RECONSTRUCTED GAME EVIDENCE` | Sources A to E and every number, name and reading inside them |
| `documented` | `DOCUMENTED` | Sources F to I, the four certified real-world sources |
| `curriculum-model` | `CURRICULUM-ORIGINAL FIGURE` | Figures 1, 2 and 3 |

Both learner editions print the non-merger rule on page 1:

> Reconstructed game evidence can support a judgment about the game's record. It cannot establish
> a real historical claim. Documented historical evidence can support claims about the Green
> Revolution. It cannot prove that a game record is genuine.

Where a task quotes a claim made inside the game in order to test it, the quotation is wrapped in
`data-game-claim` inside a task marked `data-tests-game-claim`. The scoped validator excuses
reconstructed cards and marked quotations from the two classes the game itself asserts — the
billion-lives filing claim and the sole-cause interpretation under test — and from nothing else,
and proves with structural mutation controls that the same sentence unmarked, or inside a
documented card, still fires.

## Source certification

Four real-world sources, and no others, support every claim this packet makes about the world.
They are the PMO-locked estate, bounded claim by claim in `sourceCertification`.

| PMO id | Printed | Source |
| --- | --- | --- |
| A | F | Government of India, Directorate of Economics and Statistics, *Agricultural Statistics at a Glance 2015*, Table 4.7(a): "Wheat: All-India Area, Production and Yield alongwith coverage under Irrigation", crop years 1964-65 to 1969-70 |
| B | G | Norman E. Borlaug, Nobel Lecture, "The Green Revolution, Peace, and Humanity", 11 December 1970 — a **primary participant source** |
| C | H | CIMMYT, "From east Asia to south Asia, via Mexico: how one gene changed the course of history" |
| D | I | Prabhu L. Pingali, "Green Revolution: Impacts, limits, and the path ahead", *PNAS*, 2012, 109(31):12302-12308 |

The Phase 1 audit is not modified. Its certified pointer for this level, `H15`, is recorded as
reused but is **not relied on for any printed claim**: every Nobel-derived claim rests on the text
of the 1970 lecture itself, which the PMO authorised and which was read in full for this
candidate. No historical, biographical, chronological, quantitative or institutional claim appears
anywhere in the package that is not on one of the certification's bounded lists.

The six-year series is pinned to a stated statistical edition: **Government of India,
Directorate of Economics and Statistics, *Agricultural Statistics at a Glance 2015*, Table
4.7(a)**. That edition supports the locked values, **the locked series is implemented exactly**,
and its internal arithmetic is self-consistent: area multiplied by yield reproduces production to
within published rounding in all six crop years. Later editions revise some historical values;
that is a reason to cite the edition, which the packet now does in the learner Source F card, in
the Teacher source estate and in `sourceCertification`, and not an error in these pages.

The two consulted sources date India's large seed purchase differently — 1966 in Borlaug's
lecture, 1967 in CIMMYT's account. The packet's chronology is settled: the bulk-shipment dates in
Figure 2 are Source G's, and Source H carries the broader transmission sequence. The Teacher
Guide records that as a disagreement between two sources rather than as an open question, and no
learner task is built on it.

## Structure

Eight numbered tasks, in this order and with these exact titles:

1. Build the Case Vocabulary
2. Set the Claim Test
3. Keep the Evidence Layers Separate
4. Read the Numbers Carefully
5. Trace the Wheat and the Package
6. Test the Failure Report
7. Test the Competing Interpretations
8. Write a Qualified Historical Finding

The numbers and titles are preserved exactly in the Student edition, in the Accessible edition,
in every keyed Answer Key section, and in every direct Teacher reference — each of which is bold
under `TEACHER_TASK_REFERENCE_EMPHASIS_v1.0.1`.

### Task 2 is deliberately not keyed

Task 2 records what a learner would require before treating "a billion lives were saved" as a
measured fact, taken after the reconstructed records and deliberately before the documented
sources arrive. It is **omitted from the Answer Key without renumbering**, the later tasks keep
their Student numbers, no learner page prints grading commentary or reveals a preferred answer,
and the Accessible edition scaffolds the question with stems without answering it.

### CER is deliberately not used

Canonical CER is **declined**, on the Blueprint ground Cases 06, 07, 08 and 09 established. The
case assesses six obligations that a claim-evidence-reasoning sequence would flatten into one,
and the three that would be lost are precisely the three the case exists for: the causal
qualification, the explicit statement of what the evidence does not prove, and the next-evidence
claim. No role renders `[data-cer-contract]`, `.canonical-cer` or `.cer-stack`, and no layout area
is locked for a CER reason.

### No exact-match word bank

None is authorised by the design lock and none is used. The nine definitions are printed as a
glossary the learner keeps using all lesson, so Task 1 requires applying a term to a thing in this
case rather than generating one from memory.

### The sixty-minute classroom route

The canonical no-game packet route is **approximately sixty minutes in total**, and the reading
sits inside it rather than beside it:

| Segment | Min |
| --- | --- |
| Launch / source-status boundary | 3 |
| 1 · Build the Case Vocabulary | 4 |
| Read reconstructed Sources A-E | 5 |
| 2 · Set the Claim Test | 3 |
| Read documented Sources F-I | 4 |
| 3 · Keep the Evidence Layers Separate | 4 |
| 4 · Read the Numbers Carefully | 8 |
| 5 · Trace the Wheat and the Package | 6 |
| 6 · Test the Failure Report | 6 |
| 7 · Test the Competing Interpretations | 6 |
| 8 · Write a Qualified Historical Finding | 9 |
| Close / collect | 2 |
| **Total** | **60** |

Tasks account for 46 minutes and the unnumbered launch, reading and close segments for 14. The
Teacher Guide invites a teacher to extend individual tasks where the calendar allows, but the
canonical route is executable as written. Gameplay is not inserted into the sixty minutes: a
class taking the game route plays in a separate period. The scoped validator checks the registry
arithmetic, checks that the twelve printed procedure steps themselves sum to sixty, and fails any
regression to "sixty minutes of task time plus a separate reading allowance".

### Role page counts

Roles and page counts: Student 8 · Teacher 7 · Answer Key 4 · Accessible 10.

Those are the locked targets, met exactly. Zero overflow in every role, in colour and in
grayscale.

## Figures

Three deterministic HTML and CSS figures. No generative art, and no imagery of any kind beyond
the shared institutional insignia.

- **Figure 1 · the India wheat record, 1964-65 to 1969-70.** Production and yield as **two
  separate graphs on two separate printed scales**, never one dual-axis graph, with the area sown
  and the irrigated share of the wheat area in an accompanying table. Every value is the exact
  published figure and every bar prints its own number, so the figure is readable with no colour.
- **Figure 2 · the wheat crosses borders.** The documented route from Japan through the United
  States and Mexico to India and West Pakistan, drawn as a route and not a map, printing that it
  represents no political geography and that the wheat did not travel by itself.
- **Figure 3 · the production package.** Six interacting contributors converging on one outcome,
  each printing a connector word from the controlled set — *contributed to*, *enabled*, *worked
  with* — under a printed rule that no contributor produced the result alone and that a correct
  mechanism is not a measured share.

## The no-game dossier

Campaign 2 has no level selector and no shortcut, so every assessed strand is printed. Five
reconstructed sources are reproduced in both learner editions:

- **Source A** · the recovered Borlaug record, with the Archive's annotation and its filing claim
- **Source B** · the two wheats and the trait scan
- **Source C** · the pedigree records
- **Source D** · Dr. Rao's deployment testimony
- **Source E** · the Failure Report

Sources A to D are runtime-required. **Source E is runtime-optional and curriculum-assessed**, so
it is printed in full: no learner's ability to complete Task 6 depends on finding it in play. The
level's optional survey of the harvest running to the horizon is **not assessed** and is
deliberately not reproduced, which the Teacher Guide states.

No runtime correct-answer flag, candidate-record label, hint, resolution text, clue identifier,
node identifier or control label is reproduced anywhere, and no invented quotation the game
attributes to Norman Borlaug — a real historical person — appears in any role.

## Standards

**Directly assessed:** C3 D2.His.14.6-8 · C3 D3.3.6-8 · C3 D3.4.6-8 · C3 D4.1.6-8 ·
CCSS RH.6-8.7 · CCSS WHST.6-8.1

**Supporting:** C3 D3.2.6-8 · CCSS RH.6-8.8

**Contextual:** none. **No NGSS performance expectation is claimed at any status**, and no
contextual standard is claimed either: no task asks a learner to construct a scientific
explanation, model a natural system or analyse scientific data.

## Declared Accessible adaptations

Five scored differences, and only five. Everything else changes the route, not the demand, and
**all five obligations of the Qualified Historical Finding remain**.

| Adaptation | Effect |
| --- | --- |
| `t3-figure-row-modelled` | The curriculum-figure row of the three-layer table is worked in full; four cells remain |
| `t4-first-read-modelled` | The first of the four reads is worked; three remain, on identical data with identical units |
| `t5-route-mostly-supplied` | Three of the four route stages are given; Mexico is answered |
| `t6-modelled-comparison` | One complete claim-versus-evidence comparison is modelled; three tests remain |
| `t7-first-position-modelled` | Interpretation A is worked in both cells; B and C remain |

Route-only supports — sentence frames in Tasks 2, 4 and 8, a lower-density dossier over more
pages, bullets accepted throughout — change no obligation. The Accessible edition remains
continuous-flow: Tasks 6 and 7 share page 9, and no page is padded with whitespace.

## Semantic regression contract

Five closed negative classes guard the five high-risk misconceptions:

`livesSavedAsMeasurement` · `seedAloneCausation` · `productionIsYield` · `dwarfingCausesRust` ·
`productionEndsHunger`

Each is subject-anchored, requires an affirmative unnegated predicate, and ships with negative
controls it must flag and positive controls it must not. Only the two classes the game itself
asserts are excused inside a reconstructed evidence object or a marked quotation; the other three
are excused nowhere in the learner editions at all. Exemptions are **concept-scoped**: an
exemption that allows two classes cannot quietly excuse the other three, and a mutation control
proves it. The guard is bounded and claims no general semantic completeness.

## Validation

- Case 10 scoped validator — `apps/curriculum-editor/tests/validate_hhh_case10_the_quiet_billion.py`.
  It validates this release's `history/release-v0.1.json` directly against
  `shared/implementation/case-release-history.schema.v1.json`, following Case 08 and Case 09,
  because `validate_static.py`'s release-history schema loop is bound to the SSS partition and
  does not reach an HHH package
- static repository validation — `apps/curriculum-editor/tests/validate_static.py --skip-mutation-tests`
- browser render, geometry, overflow and layout harness — `apps/curriculum-editor/tests/run_browser_tests.py`
- canonical case structure, release integrity, HHH activation, layout overrides, HHH operational,
  corrective lifecycle, authoring security and server lifecycle validators
- `git diff --check`

## Preservation

This release adds files under `hhh/campaign-2/case-10-the-quiet-billion/` and touches nothing
else in the curriculum tree. Outside the package the only changes are the narrowly necessary
registration and then release conversion of the existing Case 10 entry in the shared case
registry, the registration of the case in the browser-harness eligibility roster, and the Case 10
scoped validator with its chaining line in `validate_static.py`.

`sss/**`, `hhh/campaign-1/**`, `hhh/campaign-2/case-07-the-audit/**`,
`hhh/campaign-2/case-08-floating-gardens/**`, `hhh/campaign-2/case-09-seeds-they-kept/**`,
`hhh/audit/**`, `hhh/blueprint/**`, `hhh/production/**`, the shared contracts, schemas and
validators, the visual style guide and the Curriculum Bible are untouched, as is the game.
