# HHH Campaign 1 · Synthesis — The Temporal Agricultural Archive

**Unit:** `HHH-C1-SYNTHESIS`
**Runtime source:** *Hunger, Harvest, & History*, Campaign 1 Level 7 — **framing only**
**Instructional type:** `SYNTHESIS`
**Display label:** Campaign 1 Synthesis
**Version:** 0.1
**Status:** `APPROVED_STABLE` — released 2026-08-18
**Blueprint:** `hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md`, §8.2 and Campaign 1 Synthesis — C1 L7
**Audit baseline:** `hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md`
**Game commit:** `d9fc16baf272cb543c29cbd0c06ec85efad60be8`

The Campaign 1 Synthesis, and the closing unit of Campaign 1. The first released
HHH special unit that is not a numbered Core Case, released at v0.1 on
2026-08-18. Produced against the released Core Case 06 baseline
`1109e5f13e5a59718e7ba08d5bb93b7bc0ecc318` and the approved Blueprint.

## This is not a numbered Core Case

It is **not `Case 07`**, it is not `CORE_CASE`, and no role displays it as one.
Campaign 2 Core Case 07 — *The Audit* — is a separate later unit and is out of
scope here. The registry reservation for this unit already carried the canonical
identity (`displayOrder` 8, `displayLabel` `Campaign 1 Synthesis`,
`instructionalType` `SYNTHESIS`); this package activates it rather than inventing
it.

The contextual subtitle **Campaign 1 Synthesis · The Long Yield** is not invented
for the packet: *The Long Yield* is the runtime tagline of C1 L7 and the title of
its finale card.

## Release state

| Gate | State |
| --- | --- |
| Package status | `APPROVED` |
| Owner review | `OWNER_REVIEW_PASS` — Nate / Owner, 2026-08-18 |
| Physical print review | `PASS` |
| Release record | [`history/release-v0.1.json`](history/release-v0.1.json) |
| Approval record | [`history/SYNTHESIS_OWNER_APPROVAL_v0.1.md`](history/SYNTHESIS_OWNER_APPROVAL_v0.1.md) |

**Owner-approved printable baseline:** `f14797872f22fc13d4d0999871b081f88fb1e848`.
Release conversion left `content.html`, `presentation.css` and
`layout-overrides.json` byte-identical to that commit; only `task-registry.js`
moved, and only in its two lifecycle keys, neither of which renders. The release
record pins the commit whose tree first carries the released certified bytes,
which is the release-conversion commit rather than the printable baseline; the two
are recorded separately and deliberately.

**The commit first built as a candidate and the commit the owner approved are not
the same commit.** Candidate 1 `2f8ffd6` underwent independent review, bounded
remediation at `05f3eee`, a focused re-review that found one remaining blocking
source-certification failure, its correction at `a6b08c5`, and three owner
terminology commits ending at `f147978`, which the owner approved. The full
sequence is recorded in the approval record and the release record.

Production is HTML-only. No canonical PDF artifact exists, PDF generation is not a
release gate, and any PDF exported from the browser is noncanonical and carries no
accessibility guarantee.

## Learning goal and guiding question

**Learning goal.** Students will use evidence from Campaign 1 to trace continuity
and change in agricultural knowledge, systems, and record preservation across
time, explaining how knowledge was preserved, transferred, tested, or revised and
why a correct local mechanism may still be insufficient to explain a broader
historical outcome.

**Guiding question.** How does agricultural knowledge change as people preserve,
transfer, test, and revise it—and why does the historical record matter?

**Primary reasoning:** campaign synthesis + continuity/change + reflection.
**Primary families:** H6 continuity/change comparison + H2 cross-case chronology.
**Culminating product:** a historical continuity/change synthesis using evidence
from at least two earlier cases.
**Readiness:** `READY_AS_SYNTHESIS_NOT_CORE_CASE`.

## Structure

Six tasks. The titles are identical in the Student, Teacher, Answer Key and
Accessible editions.

| # | Title | Function | Keyed |
| --- | --- | --- | --- |
| 1 | Read the Campaign Record | six cross-case evidence recaps; reference | no |
| 2 | Trace the Long Yield | cross-case chronology; one continuity, one change | yes |
| 3 | Compare Continuity and Change | paired early/late comparison, ten fields | yes |
| 4 | Test the Limits of a Correct Mechanism | mechanism against broader outcome, two cases | yes |
| 5 | Write the Archive Synthesis | culminating product | yes |
| 6 | What Should the Archive Preserve? | transfer / exit | yes |

Roles and page counts: Student 7 · Teacher 7 · Answer Key 5 · Accessible 11.

### Why Task 1 is not keyed

It is reference. Six cards carrying setting, change, certified evidence, what the
evidence supports, what it does not establish alone, source status and an archive
thread — and no response field. It exists so that no later task depends on
remembering an investigation the class may have closed weeks ago. The Answer Key
omits it silently and does not renumber, per the task-reference parity rule.

### Why Cases 01 and 04 are absent from Task 4

Task 4 offers exactly Cases 02, 03, 05 and 06. Case 01's reasoning is cumulative
change across generations rather than a mechanism falling short of an outcome, and
Case 04's is attribution across distinct kinds of work. Forcing either into the
mechanism/broader-outcome frame for symmetry would teach a false shape. **Case 04
is used instead as the worked contrast in the Accessible edition, precisely
because it cannot be chosen** — the model cannot be copied into an answer.

### CER is deliberately not used

The Blueprint names a continuity/change synthesis (§9.5) for cross-case reasoning
about what changed and what persisted, and permits CER (§9.6) only where its
structure genuinely supports the unit. The Archive Synthesis carries a continuity,
a change, evidence from two or more cases, a qualification, and a statement about
historical memory. A CER frame would have to elect one of those as *the* claim and
demote the rest to support. Evidence and reasoning remain assessed — through the
synthesis itself and through rubric criteria 2 and 4. **No role renders the
canonical CER component and no role prints a Claim/Evidence/Reasoning structure.**

## Evidence recaps — the six cases

Every recap carries seven labelled fields and preserves the qualification its own
case established. **No recap introduces a new external factual claim.**

| Case | Archive thread | Carried-forward core idea | Preserved qualification |
| --- | --- | --- | --- |
| 01 · The Fertile Crescent | PRESERVE | Repeated selection, seed saving and replanting contributed to domestication, cumulatively. | **Cultivation is not domestication.** No first person, field or date; the 804 identifiable spikelets out of 9,844 carry the trend, not the 9,844. |
| 02 · Sumer | RECORD | Irrigation, water table, evaporation and salt accumulation support the field-scale salinization mechanism. | The **region-scale** decline is argued among scholars and is not settled here; the tablet reading is contested. |
| 03 · County Cork | RESPOND | *Phytophthora infestans* explains the potato blight. | The pathogen alone does not explain famine mortality; crop dependence and social/political context contributed and are not ranked. |
| 04 · Karlsruhe | TRANSFER | Laboratory scientific possibility is distinct from industrially workable ammonia synthesis. | Careful attribution across Haber, Le Rossignol, Mittasch and Bosch; the exact 1909 demonstration date is debated. |
| 05 · The Dust Bowl | RESPOND | Drought, exposed soil, wind erosion, and the later conservation response interact. | **Both** "weather alone" and "the weather was irrelevant" are refused; so is "the plough alone". Conservation and the returning rains cannot be separated. |
| 06 · The Vertical Farm | PRESERVE | Two-layer truth, mandatory. | Layer 1 (the 2041 facility) is **fictional**; Layer 2 (nitrification, organism diversity, plant uptake) is **real published science**. The two never merge. |

**Archive Orientation is not one of the six evidence selections.** Its
methodological rule is carried forward instead — *preservation does not equal
historical verification* — through the printed evidence-status key on page 1 of
both learner editions and through Task 6.

## Game treatment and the no-game route

C1 L7 is **framing, not an evidence base**. The single finale excerpt is printed
once per learner edition inside a node marked `data-game-framing="fictional"`,
under a status line that says in plain words that it proves nothing. Nova's
testimony, the grove observation and the Archive's finale statements are never
used to support a real-world historical claim, and no Answer Key exemplar rests on
that node.

**The no-game route is the default route.** Every assessed task is answerable from
the six recap cards, the chronology rail and the supplied pointers. Gameplay is
never required, and the Teacher Guide states the no-game route on pages 1, 4 and 7.

## Accessible edition

Authored alongside the Student edition, not retrofitted. Same six tasks, same
titles, same order, continuous flow — not one task per page.

| id | Task | What |
| --- | --- | --- |
| `a-chunked-recaps` | 1 | Recaps set larger, one or two to a page, each field on its own labelled line. |
| `a-rail-supplied` | 2 | Every date and case identity printed on the rail. |
| `a-t2-frames` | 2 | Sentence openers on both responses. |
| `a-t3-frames` | 3 | A sentence frame in every organizer cell; permitted case numbers printed as options. |
| `a-t3-short-phrases` | 3 | Short evidence phrases accepted in the four upper cells, stated in the directions. |
| `a-t4-pointers` | 4 | Each permitted case names the recap card and the exact line to use. |
| `a-t4-frames` | 4 | Sentence frames and hints on all four stages. |
| `a-t4-contrast-strip` | 4 | A worked *explains* / *does not explain alone* contrast built on **Case 04**, which cannot be chosen. |
| `a-t5-bullets` | 5 | Bullet points permitted; five labelled prompts with sentence openers. |
| `a-t6-two-steps` | 6 | Collected as two steps where the Student edition collects one field. |

**No assessed conclusion is revealed by any scaffold**, and no Accessible-only
obligation exists. The only response-count difference is the declared Task 6
chunking, which splits one obligation into two steps without changing it.

## Standards

**Directly assessed:** C3 `D2.His.2.6-8`, C3 `D2.His.1.6-8`, C3 `D2.His.14.6-8`,
CCSS `RH.6-8.1`, CCSS `WHST.6-8.2`.
**Supporting:** C3 `D3.2.6-8`, CCSS `RH.6-8.9`.

**No NGSS Performance Expectation is claimed**, directly or contextually. **C3
`D4.1.6-8` is not claimed**: the culminating product is an explanatory synthesis,
not a formal evidence-based argument with counterclaims.

## Figures

Five, all curriculum-original, all deterministic HTML and CSS. No map, no
screenshot, no decorative artwork.

| Figure | Task | What it does |
| --- | --- | --- |
| Six evidence recap cards | 1 | Seven labelled fields each; the *does not establish alone* line is boxed. |
| Cross-case chronology rail | 2 | Six rows, dates supplied, with the mixed-precision disclosure printed above the rail rather than footnoted. |
| Continuity/change organizer | 3 | Two columns for the chosen pair, four comparison rows, two full-width rows. |
| Mechanism-versus-broader-explanation organizer | 4 | Four stages, twice. The *does not explain alone* stage is the only one set in the institutional accent. |
| Evidence-status key | 1 | Six statuses in words, plus the Archive rule that preservation is not verification. |

## Semantic regression contract

The registry owns the vocabulary; the scoped validator compiles it. Nine closed
negative classes, each paired with a positive structural requirement, because a
guard that only forbade a sentence would be satisfied by a packet that said
nothing at all. Seven of the nine reuse the literal prohibition registers the
released Cases 01–06 already declared, so the Synthesis cannot quietly relax a
boundary an approved case established.

Exemption is a closed contract: a node is excused only by naming a registered
exemption id that resolves, for its role, to the class it would otherwise violate.
The Teacher misconceptions table and the Answer Key scoring floors are the only
registered exemptions, because both must be able to state a refused claim in order
to refuse it.

Every guard ships with negative controls the validator must flag and positive
controls it must not.

## Preservation

This package adds files under `hhh/campaign-1/synthesis-campaign-1/` and touches
nothing else in the curriculum tree. `sss/**`, `hhh/audit/**`, `hhh/blueprint/**`,
`hhh/production/**`, HHH Cases 00–06, the shared contracts and schemas, the visual
style guide and the Curriculum Bible are all unmodified. The game is unmodified.

The only changes outside this directory are the narrowly necessary registration of
the unit in the shared case registry and the test-harness roster, and the addition
of the scoped validator. **No shared schema or production contract was modified:**
`case-package.schema.v2.json` and `case-registry.schema.v2.json` already permitted
`HHH-C1-SYNTHESIS`, `SYNTHESIS` and the `Campaign 1 Synthesis` display label.
