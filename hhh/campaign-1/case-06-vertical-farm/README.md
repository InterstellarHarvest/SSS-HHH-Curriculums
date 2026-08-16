# HHH Campaign 1 · Core Case 06 — The Vertical Farm

**Case:** `HHH-C1-CASE06`
**Runtime source:** *Hunger, Harvest, & History*, Campaign 1 Level 6
**Setting:** a commercial vertical farm, 2041 — **fictional**
**Instructional type:** `CORE_CASE`
**Version:** 0.1
**Blueprint:** `hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md`, Core Case 06
**Audit baseline:** `hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md`
**Game commit:** `d9fc16baf272cb543c29cbd0c06ec85efad60be8`

## Release state

| Field | Value |
| --- | --- |
| `status` | `VALIDATION_BUILD` |
| `packageStatus` | `VALIDATION` |
| `ownerReviewStatus` | `OWNER_REVIEW_NOT_STARTED` |
| `printStatus` | `NOT_RUN` |
| release record | none — this package has never been released |
| approval record | none |

This is a validation candidate. It has not been approved, released, printed or
owner-reviewed, and it carries no history directory.

## Game-baseline note

The Phase 1 Master Game Audit read C1 L6 at game commit
`9b8545ed6ecf98b337326390400076e36789e056`. The current game authority is
`d9fc16baf272cb543c29cbd0c06ec85efad60be8`.

**C1 L6 did not change between those two commits.** The complete diff between
them touches two files, `hhh_data.js` and `hhh_campaign_2_data.js`; within
`hhh_data.js` every hunk falls in L1, L2, L3 or L5. The L6 block — its briefing,
its three locations, its ten sources, its diagnoses and its resolution text — is
byte-identical at both commits. The Phase 1 C1 L6 evidence inventory therefore
remains applicable in full, and all ten audited sources were re-read at the
current baseline and match the inventory exactly.

## Central learning goal

Distinguish hardware performance from failure of a biological nitrogen-cycling
subsystem, and evaluate institutional misattribution of a complex system failure.

**Primary reasoning:** systems causation + evidence audit + institutional
accountability.
**Primary families:** H8 systems trace, H9 competing-record comparison, H2 event
log.
**Culminating product:** a systems and evidence-audit explanation.
**Readiness:** `READY_WITH_TEACHER_QUALIFICATION`.
**Two-layer truth:** mandatory, and implemented as an assessed obligation rather
than a notice.

## Two-layer truth

This is the fictional case of Campaign 1. Everything in it belongs to exactly one
of three declared layers, marked in markup (`data-evidence-layer`) and in printed
text (a `STATUS` line on every evidence object).

| Layer | Marked | What it covers |
| --- | --- | --- |
| `fictional` | `FICTIONAL CASE EVIDENCE` | The 2041 facility, the crops, the engineering logs, the biological trace, the maintenance chronology, the public statement, the media archive — and every date, day number and duration belonging to any of them. |
| `real` | `DOCUMENTED` | Nitrification; the ammonia/ammonium forms and the pH relationship; nitrite and nitrate; the diversity of nitrifying organisms; plant uptake of inorganic nitrogen; the variability of ammonium tolerance. |
| `curriculum-model` | `modeled` | The five figures drawn for this packet. |

**The non-merger rule** is printed on page 1 of both learner editions: getting the
2041 case right proves nothing about the real world, and a real scientific finding
proves nothing about 2041. **Task 8 Part A makes it assessable** — every piece of
evidence a learner cites must carry its source letter *and* its layer, and rubric
criterion 3 scores it.

Every deterministic fictional value sits inside a node carrying
`data-fictional-data`, and the chronology figure — the only figure that displays
such values — prints the words `FICTIONAL CASE DATA` in its own status line.

## Structure

Eight tasks. The count is not inherited from Case 05; it is what this case's ten
required instructional functions collapse to once transfer is folded into the
culminating product and the two claim-audits are folded into one task.

| # | Title | Function | Family |
| --- | --- | --- | --- |
| 1 | Build the Case Vocabulary | reference / vocabulary | — |
| 2 | Record a First Audit Question | initial interpretation | — |
| 3 | Draw the System Boundary | system context / boundary | H8 |
| 4 | Trace the Nitrogen Pathway | systems trace | H8 |
| 5 | Order the Failure | event chronology | H2 |
| 6 | Audit the Records | source / evidence audit | H9 |
| 7 | Weigh the Accounts, Audit the Record | competing explanations **(A–B)** + institutional accountability **(C–E)** | H9 |
| 8 | Explain the Failure | culminating product **+ transfer (Part D)** | — |

### Task 7 is one task, and it runs over two pages

Parts A and B (five competing accounts) and Parts C to E (the public record) were
authored as two tasks and folded into one at owner review. They are one judgment
made twice on the same evidence, and split they double-counted it: the learner
marked the inquiry's verdict as Account 2 and then marked the same verdict again
as statement claim 2. Both audit-mandated items survive the fold intact —
**Account 4**, which discharges `HHH-GAME-C1L6-001` as an assessed judgment, and
**Account 5**, the case's uncertainty requirement.

The task spans Student pages 9–10 and Accessible pages 14–16. Each continuation
page is declared in `continuationPages` and must print `Task 7 · continued`; the
scoped validator resolves both directions, so a continuation page cannot lose its
heading and an undeclared one cannot appear.

### Task 2 comes before the science file, on purpose

Ordering is an argument here. A class that reads the microbiology first arrives
at the case file already knowing what to look for, and the audit degenerates into
a treasure hunt. A class that has to ask its own question first, from an
incomplete record, discovers something more useful: that the question you ask
determines the answer you can get — which is exactly how the inquiry inside the
case reached the wrong verdict while asking a perfectly reasonable question.

### CER is deliberately not used

The Blueprint permits CER and names a *systems and evidence-audit explanation* as
this case's product. The culminating task has to carry two findings a single
claim cannot hold at once — that a biological subsystem failed, and that the
record which named the cause was wrong about it — plus a bounded exoneration and
an open institutional question. A CER frame would force one of those to be *the*
claim and demote the rest to support, which is the move the case exists to refuse.

### Role page counts

Roles and page counts: Student 11 · Teacher 10 · Answer Key 5 · Accessible 17.

The Student edition is longer than Case 05's because it carries two complete
evidence layers: five fictional case records and five real scientific sources,
each with its own status line and its own printed limitation. The real estate is
printed on three learner cards rather than five — the two papers that retired the
two-species rule share card G, and the two plant reviews share card H — because
each pair answers one question and reads as one card. No claim and no printed
limitation was dropped to do it, and the Teacher ledger still cites all five
sources separately. The Teacher Guide
runs to ten pages because the source ledger is split by layer across two of them,
which is what makes the two-layer boundary teachable rather than merely stated.
The Accessible edition gives the first audit question a page of its own and
splits every multi-part task across pages, so Tasks 5 and 6 each run across two
and Task 7 across three. It was recomposed rather than allowed to grow: one dossier card per page
left more than half of several pages empty, which the Accessible Adaptation
Contract treats as page count without accessibility gain.

## Figures

Five, all curriculum-original, all deterministic HTML and CSS. No photographs, no
generated art, no faux-antique or futuristic styling.

| Figure | Task | What it does |
| --- | --- | --- |
| System boundary | 3 | One loop, two zones, and a monitoring band that visibly **stops** at the line between them. |
| Nitrogen pathway | 4 | Four stages beside the control panel that doses them, with the plant-uptake and organism-diversity boundaries printed on the figure itself. |
| Chronology | 5 | Six slots with the engineering rail running unbroken beneath all of them. Every value labelled fictional case data. |
| Record-audit matrix | 6 | Five records, two identical columns, no ranking. |
| Public-record comparison | 8 | Three claims against the evidence, with a third column held open for what stays unanswered. |

## The audit dependency: `HHH-GAME-C1L6-001`

Classification: `CURRICULUM_QUALIFICATION_REQUIRED`. Teacher qualification, not
game remediation. The case is produced against the current game and corrects the
model in print.

The runtime level's closing note presents the real-world biology as two partner
microbes, *Nitrosomonas* and *Nitrospira*. That was standard textbook framing and
is no longer adequate. **The finding is discharged as design, not as disclaimer:**

- **Consortium composition.** Source G is in the packet for this.
  **Task 7 Part A, Account 4** — *a nitrifying community is always exactly two species* —
  is an account the learner marks **N** using the packet's own printed evidence.
  The learner refuses the simplification; the teacher does not correct it.
- **Plant-usable forms.** The boundary note is printed on the Task 4 figure in
  both learner editions: plants take up nitrate **and** ammonium, through separate
  transporters. The Answer Key carries a floor against the nitrate-only claim.
- **Toxicity threshold.** **No number appears anywhere in this packet**, because
  Source H establishes that the threshold varies with species, ecotype, cultivar
  and conditions. EPA's ammonia toxicity material is about aquatic animals and is
  scoped as such wherever it is used.
- **Ammonia vs ammonium.** Both terms are printed with their formulas in every
  learner edition, along with the pH relationship, and `ammonium` is assessed as a
  term in its own right in Task 1.

## Source estate

Fifteen canonical sources: five fictional, five real, five curriculum figures.
The Teacher ledger prints them in eleven rows across two pages, with the five
figures grouped under a declared grouping rule.

### Layer 1 — fictional (5)

`facility-record`, `engineering-log`, `consortium-trace`,
`maintenance-chronology`, `public-statement`. All `fictional / hypothetical`.

### Layer 2 — real (5)

Every load-bearing real-world claim was independently certified against the
published source before authoring.

| Source | Certifies |
| --- | --- |
| **US EPA, CADDIS Volume 2: Ammonia** (updated 22 Jan 2026) | Ammonia nitrogen = ammonium (NH₄⁺) + ammonia (NH₃); pH raises the more toxic unionized form; nitrification = oxidation of ammonia to nitrite and nitrate by bacteria and other microbes. **Limit:** aquatic life, not crops; no plant threshold. |
| **Daims et al., *Nature* 528(7583):504–509 (2015)**, doi:10.1038/nature16461, with **van Kessel et al., *Nature* 528(7583):555–559 (2015)**, doi:10.1038/nature16459 | Comammox — single *Nitrospira* encoding all enzymes for complete nitrification. Retires the word *always*. |
| **Bartelme, McLellan & Newton, *Front. Microbiol.* 8:101 (2017)**, doi:10.3389/fmicb.2017.00101 | In a real commercial RAS biofilter, ammonia-oxidising archaea dominated at ~6×10⁵ times the abundance of *Nitrosomonas*, and comammox *Nitrospira* carried the most abundant ammonia-oxidising gene — while designers typically cite *Nitrosomonas* and *Nitrobacter*. |
| **Hachiya & Sakakibara, *J. Exp. Bot.* 68(10):2501–2512 (2017)**, doi:10.1093/jxb/erw449 | Plants acquire inorganic N mainly as nitrate **and** ammonium; mixtures beat either alone. |
| **Esteban, Ariz, Cruz & Moran, *Plant Science* 248:92–101 (2016)**, doi:10.1016/j.plantsci.2016.04.008 | Ammonium toxicity threshold depends on species, ecotype, cultivar and conditions; some species prefer ammonium. |

### Things this packet deliberately does not print

- **Any ammonia or ammonium toxicity threshold for plants.** No source supports a
  universal one, and Source H establishes that none exists.
- **Any species composition for the fictional consortium.** The fictional record
  names none, and Source G is why the textbook pair is not substituted.
- **Any named trigger for the collapse.** Three candidates are logged inside three
  days and nothing separates them.
- **Any counterfactual about whether better monitoring would have saved the crop.**
  The packet supports the *question*, not the answer.
- **Any real-world event corresponding to the 2041 case.** None exists, and none
  is implied.

## The accountability boundary

Two-sided, and both sides are required in every role.

**What the evidence establishes:** the machinery met its designed setpoints; the
living subsystem failed first; the public statement's account of a flawed design
is unsupported. The named engineer is cleared of **the failure the statement
describes**.

**What it does not establish:** which logged event caused the collapse; that the
collapse was undetectable; that no person or body could have chosen differently
about what to monitor or how to commission a living subsystem; that the
institution's choice of public account was reasonable.

**Task 7 Part E** requires an open institutional question with the record that
raised it. **A blank Part E is scored as the no-accountability overcorrection**,
because the task prints the requirement explicitly. Rubric criterion 4 carries
floors in **both** directions: adopting the statement's verdict fails, and
concluding that no responsibility arises fails.

## Declared Accessible adaptations

Four, and only four. The Accessible edition was authored alongside the Student
edition, not retrofitted.

| id | Task | What | Effect |
| --- | --- | --- | --- |
| `t4-modelled-stage` | 4 | The first open conversion stage is supplied complete as a worked model. | Accessible completes **1** stage; Student completes 2. |
| `t6-modelled-row` | 6 | The first record row is supplied complete in both cells. | Accessible completes **8** cells; Student completes 10. |
| `t5-dated-cards` | 5 | The four chronology cards carry their day labels. | Ordering becomes matching. No response-count change. |
| `t7-source-pointers` | 7 | Each account in Part A carries a pointer to the source that bears on it. | No response-count change. |

One **chunking** split, which is not a scored difference: Task 7 Part E is
collected as two steps in the Accessible edition (the question, then the record)
where the Student edition collects both in one field. The obligation is identical
and the Answer Key models both halves for both editions.

**No Accessible-only obligation exists.** Every assessed Accessible response has a
Student counterpart, checked structurally against `editionResponseContract`.

## No-game fallback

Complete. A learner who never launches the game can perform **every assessed
task** from Sources A–H and the five figures. Nothing is held back for players,
and no task requires an optional game clue.

## Semantic regression contract

The registry owns the vocabulary; the validator compiles it. Five closed negative
classes, each bound to a named subject where a subject is meaningful, each paired
with a positive structural requirement:

| Class | Guards against | Positive counterpart |
| --- | --- | --- |
| `universalTwoSpecies` | *always / exactly two species* claims about a nitrifying community | the diversity note must be printed in both learner editions |
| `nitrateOnly` | *nitrate is the only usable form* | the both-forms note must be printed in both learner editions |
| `universalToxicityThreshold` | a printed numeric plant toxicity level | the no-threshold rationale must be stated in Teacher and Answer Key |
| `noAccountability` | *no one was responsible for anything* | Task 7 Part E must exist and demand an open question |
| `verdictAdopted` | stating the fictional statement's verdict as a finding | the statement must be marked NOT SUPPORTED in the key |

**Case 05's zero-boundary machinery is deliberately not reproduced.** That guard
existed because the runtime level itself carried the absolute, and reviewers kept
finding fresh English for it. Nothing comparable exists here: the classes above
are genuinely small and finite, every one is anchored to a named subject or a
numeric pattern, and none polices an ordinary verb or an open synonym family.
Every guard ships with negative controls the validator must flag and positive
controls it must not.

Exemption is a closed contract. A node is excused only by naming a registered
exemption id that resolves for its role; markup cannot self-authorize.

## Preservation

This package adds files under `hhh/campaign-1/case-06-vertical-farm/` and touches
nothing else in the curriculum tree. `sss/**`, `hhh/audit/**`, `hhh/blueprint/**`,
`hhh/production/**`, HHH Cases 00–05, the shared contracts and schemas, the visual
style guide and the Curriculum Bible are all unmodified. The game is unmodified.

The only changes outside this directory are the narrowly necessary registration
of Case 06 in the shared case registry and the test-harness roster, and the
addition of the Case 06 scoped validator.
