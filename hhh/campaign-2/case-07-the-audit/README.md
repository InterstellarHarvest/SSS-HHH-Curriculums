# HHH Campaign 2 · Core Case 07 — The Audit

**Case:** `HHH-C2-CASE07`
**Runtime source:** *Hunger, Harvest, & History*, Campaign 2 Level 0
**Setting:** TAA Facility, 2387 — **fictional**
**Instructional type:** `CORE_CASE`
**Version:** 0.1
**Status:** `DRAFT` — unreleased candidate, owner review not started
**Blueprint:** `hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md`, Core Case 07
**Audit baseline:** `hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md`
**Game commit:** `d9fc16baf272cb543c29cbd0c06ec85efad60be8`

The first unit of Campaign 2, and the first HHH case whose culminating product is a
provenance and authenticity judgment. Produced against the synchronized Campaign 1
baseline `c078025678d18fb4ade9f3d15a390f01b4100733` and the approved Blueprint.

## Release state

| Gate | State |
| --- | --- |
| Package status | `DRAFT` |
| Owner review | `OWNER_REVIEW_NOT_STARTED` |
| Print status | `NOT_RUN` |
| Release record | none — an unreleased candidate has no release history |
| Approval record | none |

This is a **candidate**, not a release. No `history/` directory exists, no release or
owner-approval record has been created, and none may be created before the owner has
passed both the Curriculum Editor review and a physical print test. An unreleased
native candidate is not `APPROVED_STABLE`.

Production is HTML-only. No canonical PDF artifact exists, PDF generation is not a
release gate, and any PDF exported from the browser is noncanonical and carries no
accessibility guarantee.

## Game-baseline note

The Phase 1 Master Game Audit read C2 L0 at game commit
`9b8545ed6ecf98b337326390400076e36789e056` and raised one finding against it,
`HHH-GAME-C2L0-001`, classified `GAME_REMEDIATION_BLOCKS_FINALIZATION`.

**That dependency is closed.** It was resolved in the game at
`d9fc16baf272cb543c29cbd0c06ec85efad60be8`, which is the current game authority and
the commit this package is produced against; the remediation dependency tracker
records it as `RESOLVED_VERIFIED` at that commit and this package changes nothing in
the tracker. The remediated level states the governing rule correctly, and this
package neither reopens the game nor propagates the retired heuristic.

**The rule the closed finding establishes, and which this package teaches:**
authenticity is evaluated through multiple factors such as materials, handwriting,
provenance, custody and corroboration; unexplained neatness may prompt questions;
**no single surface feature proves authenticity or forgery**; a clean working
document can be genuine; a forgery can imitate corrections.

## Central learning goal

> Evaluate which competing record is better supported as authentic by tracing
> provenance and transmission, comparing discrepancies, and corroborating independent
> evidence—without treating neatness or corrections as proof.

**Guiding question:** Which report is better supported as authentic, and how does the
chain of evidence justify that judgment?

**Primary reasoning:** source criticism + provenance + corroboration.
**Primary families:** H9 competing-record comparison + H1 provenance chain.
**Culminating product:** a Record Validation Memorandum — a provenance/authenticity
judgment.
**Intended evidence judgment:** **Copy B is better supported as authentic**, on a
multi-factor route.

## Source status

Three bands, marked in markup (`data-evidence-layer`) and in printed text as a
`SOURCE STATUS · <CLASSIFICATION>` band on every evidence object.

| Band | Marked | What it covers |
| --- | --- | --- |
| `fictional` | `FICTIONAL CASE EVIDENCE` | The Temporal Agricultural Archive, the audit, both competing copies, both custody histories, the recall and the re-filing, and every count, name and date belonging to any of them. |
| `real` | `DOCUMENTED` | Diplomatics as the name and definition of the discipline; the identification of Mabillon's *De Re Diplomatica* (1681) in the SAA dictionary entry; the description of the work as weighing context with internal and external characteristics; the four properties of a trustworthy record. |
| `curriculum-model` | `CURRICULUM-ORIGINAL SCHEMATIC` | The three figures drawn for this packet. |

**The non-merger rule** is printed on page 1 of both learner editions: getting the TAA
case right proves nothing about the real world, and a real archival principle proves
nothing about the TAA.

Every deterministic invented value sits inside a node carrying `data-fictional-data`,
and every such node sits inside a fictional or curriculum-model evidence object.

Visible provenance follows
[`STUDENT_FACING_METADATA_AND_VISUAL_HIERARCHY_v1.0.1.md`](../../../shared/visual-style-guide/amendments/STUDENT_FACING_METADATA_AND_VISUAL_HIERARCHY_v1.0.1.md):
the band carries the classification and nothing else, and the one place a learner could
mistake an organiser for case evidence — the multi-factor framework figure — carries a
single short caption saying so. The machine-readable evidence-layer markup is unchanged
and is still what validation binds to.

### No new source certification was performed

The real-world layer uses **only** the two Phase 1 certified sources, `H10` and `H11`:

| Source | Certifies |
| --- | --- |
| **Society of American Archivists, *Dictionary of Archives Terminology*, "diplomatics"** | The name and definition of the discipline; Mabillon's *De Re Diplomatica* (1681); the description of the work as weighing context with internal and external characteristics rather than any "too clean" rule. |
| **U.S. National Archives, trustworthy-records guidance** | Reliability, authenticity, integrity and usability as four separate properties of a trustworthy record, which is what supports multi-factor authenticity reasoning. |

No historical forgery example, handwriting claim, forensic technique, statistic or
additional archival assertion appears anywhere in the package. If a later revision
needs one, that is a source-certification dependency for the PMO, not an authoring
decision.

## Structure

Eight tasks. The numbers and titles are the Student worksheet's, and the Accessible
edition and every keyed Answer Key section preserve them exactly.

| # | Title | Function | Family |
| --- | --- | --- | --- |
| 1 | Build the Case Vocabulary | reference / vocabulary | — |
| 2 | Set an Authenticity Test | initial interpretation **(non-keyable)** | — |
| 3 | Separate a Clue from Proof | misconception barrier | multi-factor framework |
| 4 | Trace Each Copy's Provenance | provenance / transmission | H1 |
| 5 | Weigh the Four Evidence Sources | contribution-and-limitation + evidentiary role | H4 |
| 6 | Compare the Competing Records | matched comparison | H9 |
| 7 | Validate the Better-Supported Record | culminating product | H9 + H1 |
| 8 | Test What Would Change Your Confidence | transfer / exit | — |

### Task 2 is deliberately not keyed

It records what a learner would verify **before** the method arrives. There is no
correct answer, and keying it would convert a record of provisional thinking into a
hidden multiple-choice item — penalising exactly the useful mistake the sequence is
built to expose. The Answer Key omits it without renumbering, which is the shared
task-reference rule, and the Teacher Guide carries the guidance for reading it.

### CER is deliberately not used

The Blueprint permits canonical CER only where its structure genuinely supports the
case, and names a **provenance/authenticity judgment** as this case's product. A CER
frame would force one claim to the front and demote everything else to support, and
this case assesses the opposite operation: the relationship between records, what each
source can and cannot establish, the corroboration between an amended page and an
independently recorded custody event, and a named clue that must be **refused**. The
Record Validation Memorandum keeps all six of those as separately scored parts. This
follows the precedent set by Core Case 06, which declined CER on the same Blueprint
ground; no role renders the shared canonical CER component and no role declares a CER
contract.

### Role page counts

Roles and page counts: Student 8 · Teacher 7 · Answer Key 4 · Accessible 10.

**Student, 8:** page 1 front matter and Task 1; page 2 Sources A to C; page 3 Source D
and Task 2; page 4 the real-world reference card and the misconception barrier; pages 5
to 7 one task each; page 8 the memorandum and the transfer exit together.

**Teacher, 7:** the shared seven-function architecture, one function per page, with no
extra appendix.

**Answer Key, 4:** Task 2 is not keyed, and Tasks 5 and 6 are keyed as completed
matrices rather than as prose, which is what holds the key to four pages while every
keyable field still carries a completed exemplar.

**Accessible, 10:** page 1 front matter; page 2 Task 1; pages 3 and 4 the dossier split
in two; page 5 the reference card and Task 2; pages 6 to 9 one task each; page 10 the
memorandum and the transfer exit, as in the Student edition. The reading pages carry
intentional reserve rather than compressed work: the next task in each case cannot fit
without cramping its response space.

## Figures

Three, all curriculum-original, all deterministic HTML and CSS. No photographs, no
generated art.

| Figure | Task | What it does |
| --- | --- | --- |
| Multi-factor authenticity framework | 3 | Five families of evidence — materials, handwriting, provenance, custody, corroboration — converging on one judgment, with the governing rule printed inside the figure. |
| Two-copy provenance and custody comparison | 4 | Both recorded trails, with the two links Copy B has and Copy A does not drawn in double border, and the head of **both** trails drawn dashed and labelled `NOT RECORDED`. |
| Evidence-weight organiser | 5 | The three evidentiary roles as named kinds. No number appears in it. |

The dashed head of the provenance figure is the point of that figure as much as the
trails are: neither record reaches the making of either copy, and the diagram says so
rather than inventing a creation event to complete the pattern.

## The no-game dossier

Campaign 2 has **no** teacher level selector, no direct-launch mode, no injected state
and no developer shortcut, and none will be built. A class reaches Level 0 only by
finishing Campaign 1 in the game. Every assessed piece of evidence therefore exists in
the learner packet, in four clearly labelled records:

- **A · the audit briefing** — what the re-scan found, and that the job is now to judge
  which finished record is true.
- **B · the pattern across the flagged records** — the insertions are non-random and
  sit at points of transfer; which is silent about any particular page.
- **C · the TAA audit log** — the insertion signature, the verified audit custody, and
  the method note that names the differential comparison against recorded custody.
- **D · the competing memo pair and their custody histories** — both pages, both
  trails, and the note on file recording the reason for the recall.

No runtime correct-answer flag, hint or resolution text is reproduced as learner
evidence, and no assessed item depends on a line that appears only in play. Normal
gameplay is an optional evidence-acquisition route; the dossier is the stable
assessment record in both routes, and the Teacher Guide supplies both.

## The evidence that carries the case

One pairing, and it is a pairing rather than a single record:

- Copy B's **page** carries a margin note correcting a grain count.
- Copy B's **custody trail** carries a recall whose recorded reason was to correct a
  grain count.

Two records, produced at different times by different processes, agreeing. The audit
log licenses the trail — its own custody is verified end to end — and also establishes
that the forgeries are expert, which is what removes any weight from Copy A looking
finished. Copy A's history is corroborated by nothing at all.

**The route this package refuses** is `Copy B has corrections, therefore it is
authentic`. It reaches the right record by reasoning that would reach the same answer
about a forgery given corrections on purpose, and the Answer Key refuses it at every
level.

## Standards

Three directly assessed, two supporting, no NGSS at any status.

| Standard | Status |
| --- | --- |
| C3 D3.1.6-8 | Directly assessed |
| C3 D3.2.6-8 | Directly assessed |
| CCSS RH.6-8.6 | Directly assessed |
| CCSS RH.6-8.9 | Supporting |
| CCSS WHST.6-8.1 | Supporting |

There is no science content in this case, so no NGSS performance expectation is
claimed at any status — not even Contextual.

## Declared Accessible adaptations

Four, and only four; the Accessible edition was authored alongside the Student edition
rather than retrofitted.

| id | Task | What | Effect |
| --- | --- | --- | --- |
| `t3-modelled-judgment` | 3 | Item 3 is supplied complete as a worked example with its reason printed. | Accessible marks **5** items; Student marks 6. The neatness and corrections items stay independent. |
| `t4-supplied-totals` | 4 | Both recorded custody totals are printed on the figure. | Counting is supplied; the reasoning is not. |
| `t5-modelled-row` | 5 | The audit-briefing row is worked in full. | Accessible completes **8** matrix fields; Student completes 12. |
| `t5-prefilled-row` | 5 | The pattern row's first cell is supplied. | The judgment in that row is preserved. |

Everything else changes the route rather than the demand: bounded choices in Tasks 2
and 8, sentence openers in Task 7, source pointers in Task 6. **No Accessible-only
obligation exists** — every assessed Accessible response has a Student counterpart,
checked structurally against `editionResponseContract`.

Task 2 is the one declared **chunking** split: one open listing of two kinds of
evidence becomes two bounded slots, one per kind. It is not a scored difference.

## Semantic regression contract

The registry owns the vocabulary; the scoped validator compiles it. **Five closed
negative classes**, each anchored to a named subject register, each paired with a
positive structural requirement checked against markup rather than prose:

| Class | Rejects | Positive counterpart |
| --- | --- | --- |
| `neatProvesForged` | a clean or pristine record *proves* forgery | the multi-factor rule must be printed in both learner editions |
| `correctionsProveAuthentic` | corrections *prove* the record genuine | the framework figure must carry the printed rule in both learner editions |
| `messyIsGenuine` | a messy working record is *automatically* genuine | Task 3's neatness item and corrections item must both exist and both be marked `Q` |
| `noCorrectionsProveForgery` | an absence of corrections *proves* forgery | the matched comparison must state in print that surface characteristics do not settle it |
| `visibleCorrectionsProveAuthenticity` | visible corrections *prove* authenticity | the Answer Key must print the floors it refuses at every level |

**This guard is bounded on purpose.** It is a defence against one known high-risk
misconception, not a proof that every possible bad paraphrase has been detected. Every
class is a closed set anchored to a subject; none enumerates synonyms for an open
concept; and the validator's own docstring says plainly that an unseen paraphrase can
pass it and that ordinary cross-role manual review remains required.

Each class ships with **negative controls** the validator must flag and **positive
controls** it must not, including the five sentences that have to stay legal:
*Unexplained neatness may prompt closer examination* · *Corrections can be one clue
when they match a documented record history* · *A clean record can be authentic* · *A
forged record can imitate corrections* · *No single surface feature proves
authenticity or forgery.*

Exemption is a closed contract. A node is excused only by naming a registered
exemption id that resolves for its own role, so a Teacher page can quote the
misconception in order to refuse it while a learner page cannot. Two mutation controls
prove that an unregistered id and a borrowed-role id both excuse nothing.

## Validation

- `apps/curriculum-editor/tests/validate_hhh_case07_the_audit.py` — the Case 07 scoped
  validator, chained into `validate_static.py` alongside the other HHH case validators.
- `shared/validation/validate_hhh_activation.py --expect-editor-ready 9`
- `shared/validation/validate_canonical_case_structure.py`
- `shared/validation/validate_layout_overrides.py`
- `apps/curriculum-editor/tests/validate_static.py`
- `shared/validation/run_curriculum_browser_harness.py`

## Preservation

This package adds files under `hhh/campaign-2/case-07-the-audit/` and touches nothing
else in the curriculum tree. `sss/**`, `hhh/campaign-1/**`, `hhh/audit/**`,
`hhh/blueprint/**`, `hhh/production/**`, the shared contracts and schemas, the shared
validators, the visual style guide and the Curriculum Bible are all unmodified. The
game is unmodified.

The only changes outside this directory are the narrowly necessary activation of the
existing Case 07 entry in the shared case registry, the registration of the case in the
browser-harness eligibility roster, and the addition of the Case 07 scoped validator
and its chaining line.
