# HHH Campaign 2 · Core Case 09 — The Seeds They Kept

**Case:** `HHH-C2-CASE09`
**Runtime source:** *Hunger, Harvest, & History*, Campaign 2 Level 2
**Setting:** Leningrad, 1941 — the siege, the collection, Vavilov's arrest and death, the
staff who starved beside the seed and the postwar regeneration are **historical**; the
keeper, the Archive's scan and ledger, the recovered recording and the Consumption Report
are **reconstructed**
**Instructional type:** `CORE_CASE`
**Version:** 0.1
**Status:** `DRAFT` — unreleased candidate
**Blueprint:** `hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md`, Core Case 09
**Audit baseline:** `hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md`
**Game commit:** `d9fc16baf272cb543c29cbd0c06ec85efad60be8`

The third unit of Campaign 2, and the first HHH case whose culminating product is a
**Collection Continuity Judgment** — a provenance and continuity judgment that has to
survive documented movement, reproduction and loss. Produced against curriculum main
`0626468629d0f9bfed65b9371e2968c43c70cd1e` and the approved Blueprint.

## Candidate state

| Gate | State |
| --- | --- |
| Package status | `DRAFT` |
| Owner review | `OWNER_REVIEW_NOT_STARTED` |
| Print status | `NOT_RUN` |
| Release record | none — no `history/` directory exists |
| Approval record | none |

**This candidate is unreleased.** No owner visual review has been performed, no
physical print test has been run, and no approval or release record exists. Nothing in
this package may be read as a claim that either gate has been met.

Production is HTML-only. No canonical PDF artifact exists, PDF generation is not a
release gate, and any PDF exported from the browser is noncanonical and carries no
accessibility guarantee.

## Game-baseline note

The Phase 1 Master Game Audit read C2 L2 at game commit
`9b8545ed6ecf98b337326390400076e36789e056` and raised two findings against it.

**`HHH-IMP-C2L2-001` is `RESOLVED_VERIFIED` at the current game commit.** The street
evidence, once insight-flagged although it gated the vault, is now an operationally
required clue; the level has six required evidence clues and no insight-flagged source;
the vault still unlocks on the street evidence and the office on the keeper's testimony;
the node-level bonus scoring survives. This package pins that resolution in
`runtimeDependency`, verifies it against the shared tracker's resolution evidence, does
not modify the game, does not recreate the old optional-clue reading, and leaves the
tracker untouched.

**`HHH-GAME-C2L2-001` is a teacher qualification**, open at the audited baseline by
design, and this package carries it in every role: published accounts disagree on how
many staff died, so every count is printed with its source attached and qualified; and
Vavilov, arrested in 1940 and dead in Saratov in January 1943, is kept on his own
strand of the chronology, apart from the colleagues who actually kept the collection.

## Central learning goal

> Explain why preserving crop genetic diversity during the Siege of Leningrad mattered
> and use chronology, provenance, collection continuity, and corroboration to evaluate
> what the evidence can establish about the collection's survival.

**Guiding question:** How can historians tell whether a collection survived a crisis as
the same continuing collection, and what can each source actually prove?

**Primary reasoning:** provenance + collection continuity/change + corroboration +
chronology + ethical historical reasoning.
**Primary families:** H2 two-strand chronology + H1 accession/provenance chain + H4
corroboration matrix.
**Culminating product:** a Collection Continuity Judgment.

**The distinction the package teaches:** collection continuity does not require physical
immobility or perfect survival. The real collection was divided, partly flown to
Krasnoufimsk, evacuated in part over Lake Ladoga, re-sown in suburban fields under fire,
partly lost, and checked and regenerated in 1946 — and it is the same collection,
because the accessions, the records and the named custodians carried its identity across
every change.

## Source status

Three bands, marked in markup (`data-evidence-layer`) and in printed text as a
`SOURCE STATUS · <CLASSIFICATION>` band on every evidence object.

| Band | Marked | What it covers |
| --- | --- | --- |
| `reconstructed` | `RECONSTRUCTED GAME EVIDENCE` | Sources A to F: the street, Dr. Morozov, the Archive's preservation scan, the accession ledger and its cross-reference, the recovered Vavilov record and the Consumption Report, with every date, count, seal, signature and reading belonging to them. |
| `documented` | `DOCUMENTED` | Sources G, H and I: the Crop Trust account of Vavilov, Loskutov's archival history of the Institute's wartime work, and the Institute's present identity. |
| `curriculum-model` | `CURRICULUM-ORIGINAL SCHEMATIC` | The two figures drawn for this packet from the documented sources. |

**The non-merger rule** is printed on page 1 of both learner editions: reconstructed game
evidence can support reasoning inside the case but cannot establish what happened to the
real collection, and a documented source can establish what happened to the real
collection but cannot prove any event in the game.

**Marked in-game quotations.** Where a task quotes a claim made inside the game in order
to test it — the scan's line that the seed never left the room, the report's four
claims — the quotation is wrapped in `data-game-claim` inside a task marked
`data-tests-game-claim`. The scoped validator excuses such quotations, and the
reconstructed cards themselves, from the two historical-claim guards and nothing else,
and proves with mutation controls that the same sentence unmarked, or inside a documented
card, fires.

Visible provenance follows
[`STUDENT_FACING_METADATA_AND_VISUAL_HIERARCHY_v1.0.1.md`](../../../shared/visual-style-guide/amendments/STUDENT_FACING_METADATA_AND_VISUAL_HIERARCHY_v1.0.1.md):
every learner-facing band is the short controlled label and nothing else.

## Source certification

The Phase 1 audit is **not modified**. Its certified sources `H13` and `H14` are reused,
and **exactly one** source is certified case-locally — the one the PMO authorized. The
bounds are machine-readable in `source/task-registry.js` under `sourceCertification`.

| Source | Certifies | Does not certify |
| --- | --- | --- |
| **Crop Trust, "Nikolai Vavilov: The Father of Genebanks"** (audit `H14`) | Born 1887; 115 expeditions to 64 countries, 1916–1933; the 1926 centres-of-origin theory; more than 250,000 seed samples; arrest in 1940 during an expedition in western Ukraine; a death sentence commuted to twenty years; death in incarceration in Saratov on 26 January 1943 of starvation; the 900-day siege during which the staff refused to eat the seeds even as they starved to death; genebanks as a standard part of the food system. | The arrest month; any staff count; any staff name; any movement, division, evacuation or reproduction of the collection; anything in the game. |
| **I. G. Loskutov, "Wartime activities of the Vavilov Institute", *Proceedings on Applied Botany, Genetics and Breeding*, 2021, 182(2):151–162, DOI 10.30901/2227-8834-2021-2-151-162** (case-local) | The failed rail evacuation of August 1941 and the ring closing on 8 September 1941; the division, tying, sealing and inventory of the collection; the Pavlovsk potato harvest under fire; famine from November 1941 and the 125-gram ration; named staff dead of hunger and exhaustion at their posts, more than twenty by the article's count, and more than thirty researchers lost in the first autumn; the flights and the Ladoga evacuation to Krasnoufimsk and the more than 100,000 accessions kept there; potato and cereal reproduction in 1942 and 1943; losses of about 40,000 accessions across the war; the February 1944 return; the 1946 check and emergency regeneration programme; the distinction between preserved collection identity and literal immobility. | Dr. Morozov; the Consumption Report; the Archive's scan; the game's ledger; the claim that every accession stayed untouched in one room; zero losses; a single settled death count; any quotation attributed to Vavilov or any runtime dialogue; any exact game forensic result; the arrest month; the day the siege was lifted. |
| **N. I. Vavilov All-Russian Institute of Plant Genetic Resources (VIR), "About institute"** (audit `H13`) | The Institute's present name and status as a Federal Research Center, and its continued existence today. | Any siege-period event, count or date; anything in the game. As consulted for this candidate on 2026-08-20 the page read "page under construction" and carried no siege narrative, so it is used for institutional identity only. |

No historical, biographical, chronological, quantitative or institutional claim appears
anywhere in the package that is not on one of those lists. If a later revision needs
one, that is a source-certification dependency for the PMO, not an authoring decision.

## Structure

Eight tasks. The numbers and titles are the Student worksheet's, and the Accessible
edition and every keyed Answer Key section preserve them exactly.

| # | Title | Function | Family |
| --- | --- | --- | --- |
| 1 | Build the Case Vocabulary | reference / vocabulary | — |
| 2 | Set a Continuity Test | provisional thinking **(non-keyable)** | — |
| 3 | Separate Vavilov's Timeline from the Siege | two-strand chronology | H2 |
| 4 | Trace the Collection Through Crisis | provenance / continuity chain | H1 |
| 5 | Compare What the Sources Can Establish | status, contribution, limitation, corroboration matrix | H4 |
| 6 | Test the Consumption Report | competing record, inside the game | — |
| 7 | Make a Collection Continuity Judgment | culminating product | H1 + H4 |
| 8 | Transfer the Method | transfer / exit | — |

### Task 2 is deliberately not keyed

It records what a learner would go and look for **before** the documented sources
arrive. There is no correct answer, keying it would convert provisional thinking into a
hidden multiple-choice item, and the packet does not reveal the answer anywhere near it.
The Answer Key omits it without renumbering and the Teacher Guide carries the guidance
for reading it diagnostically. No learner page states any grading policy.

### CER is deliberately not used

The Blueprint names an evidence-based provenance/continuity explanation as this case's
product, and the PMO locked the four-part Collection Continuity Judgment: what the
evidence supports, the strongest links, what testimony or reconstructed evidence cannot
establish, and why crop genetic diversity mattered beyond the siege. A CER frame would
collapse those four into one claim. No role renders the shared canonical CER component
and no role declares a CER contract, following Cases 06, 07 and 08.

### Role page counts

Roles and page counts: Student 8 · Teacher 7 · Answer Key 4 · Accessible 10.

Those are the targets, met exactly.

**Student, 8:** page 1 front matter and Task 1; page 2 reconstructed Sources A to D;
page 3 Sources E and F and Task 2; page 4 the three documented cards; page 5 the
chronology and Task 3; page 6 the continuity chain and Task 4; page 7 the source matrix
and the report test; page 8 the judgment and the transfer exit.

**Teacher, 7:** the shared seven-function architecture, one function per page.

**Answer Key, 4:** Task 2 is not keyed, and Tasks 5 and 6 are keyed as completed
organisers rather than as prose.

**Accessible, 10:** page 1 front matter; page 2 Task 1; pages 3 and 4 the reconstructed
dossier split in two; page 5 Task 2 and Source G; page 6 Sources H and I; pages 7 and
8 one figure task each; page 9 the matrix and the report test; page 10 the judgment and
the transfer exit. Continuous flow: three pages carry two tasks.

## Figures

Two, both curriculum-original, both deterministic HTML and CSS. **No imagery of any
kind** beyond the shared institutional insignia.

| Figure | Task | What it does | Status treatment |
| --- | --- | --- | --- |
| Two timelines on one axis | 3 | Nine dated rows, 1887 to 1946, every row printing `VAVILOV` or `INSTITUTE`, every date from Source G or H. The arrest (1940) sits above the siege (8 September 1941); the death (26 January 1943) sits in Saratov while the Institute's rows continue to the 1946 check. | `SOURCE STATUS · CURRICULUM-ORIGINAL SCHEMATIC`; caption `BASED ON · CROP TRUST · LOSKUTOV … · DOCUMENTED DATES · INTERVALS NOT TO SCALE` |
| The collection-continuity chain | 4 | Eight documented nodes — pre-crisis collection, failed rail evacuation, divided and sealed, partial evacuation, reproduction under siege, losses, check and regeneration, continuing collection — with every link labelled by what carried identity across it, and the printed rule that continuity does not require physical immobility or perfect survival. | `SOURCE STATUS · CURRICULUM-ORIGINAL SCHEMATIC`; caption `BASED ON · LOSKUTOV 2021 · CROP TRUST · RECONSTRUCTION OF A DOCUMENTED SEQUENCE · NOT TO SCALE` |

The `LOSSES` node is drawn as a link in the chain with a double border, not as a break,
because the documented record carries it and the case's conclusion has to survive it.

## The no-game dossier

Campaign 2 has **no** teacher level selector, no direct-launch mode, no injected state
and no developer shortcut, and none will be built. All six operationally required C2 L2
evidence strands are printed as Sources A to F, in the order the game presents them:

- **A · the besieged street** — *siege context.* The silent queue, the ration notice,
  the artillery, the building full of seed.
- **B · Dr. Morozov** — *keeper testimony.* The work went on; the collection was not
  eaten; a colleague died beside the rice; a seed is not food.
- **C · the preservation scan** — *collection condition.* Intact pre-war seals, matching
  counts, no consumption — and the game's own line that the seed never left the room,
  printed so that it can be tested against Source H.
- **D · the accession ledger** — *accession continuity.* Numbers continuous 1940 to
  1946, no renumbering, the same custodians through 1942.
- **E · the recovered Vavilov record** — *Vavilov's fate.* The annotation that breaks the
  report's countersignature; the words the game gives him are not reproduced.
- **F · the Consumption Report** — the competing record under test, with its clean
  finish printed as a reason to look closer and not as a test.

No runtime correct-answer flag, candidate-record label, hint, resolution text, clue
identifier or control label is reproduced anywhere. The Teacher Guide maps each
gameplay evidence object to its printed card and states in terms that neither route is
the reduced version.

## Standards

Seven directly assessed, two supporting, one contextual science entry, no NGSS
performance expectation at any status.

| Standard | Status |
| --- | --- |
| C3 D2.His.1.6-8 | Directly assessed |
| C3 D2.His.2.6-8 | Directly assessed |
| C3 D3.1.6-8 | Directly assessed |
| C3 D3.2.6-8 | Directly assessed |
| CCSS RH.6-8.1 | Directly assessed |
| CCSS RH.6-8.7 | Directly assessed |
| CCSS WHST.6-8.1 | Directly assessed |
| CCSS RH.6-8.9 | Supporting |
| CCSS WHST.6-8.2 | Supporting |
| crop genetic diversity / germplasm / ex situ conservation | Contextual |

## Declared Accessible adaptations

Six, and only six; the Accessible edition was authored alongside the Student edition.

| id | Task | What | Effect |
| --- | --- | --- | --- |
| `t3-dates-supplied` | 3 | Part A's two dates are supplied as a worked example. | Accessible answers **3** parts; Student answers 4. |
| `t4-ends-supplied` | 4 | Boxes 1 and 5 of the chain are given. | Accessible completes **3** boxes; Student completes 5. |
| `t5-status-prelabeled` | 5 | The status column is printed. | Four compact classifications removed. |
| `t5-modelled-row` | 5 | The keeper row is worked in full. | Accessible completes **9** matrix fields; Student completes 16. |
| `t6-claims-supplied` | 6 | The report's four claims are printed. | Accessible writes the four evidence cells, the verdict and the appearance response. |
| `t8-bounded-choice` | 8 | Two open evidence judgments become one bounded choice from four kinds, two sound and two weaker than they look. | One choice and the same explanation. |

Everything else changes the route rather than the demand: sentence frames in Tasks 2,
3, 4, 6 and 7, and the dossier spread over four pages. **Both figures are identical in
the two editions.** No Accessible-only obligation exists; every assessed Accessible
response has a Student counterpart, checked structurally against
`editionResponseContract`. Accessible pagination is continuous flow.

## Semantic regression contract

The registry owns the vocabulary; the scoped validator compiles it. **Five closed
negative classes**, each anchored to a named subject register, each requiring an
affirmative and unnegated predicate, and each paired with a positive structural
requirement checked against markup:

| Class | Rejects | Positive counterpart |
| --- | --- | --- |
| `vavilovPresentAtSiege` | Vavilov at, guarding or witnessing the Institute during the siege | the two-strand chronology, printed in both learner editions |
| `nothingMovedAsHistory` | the real collection stated to have never left the room, building or city | the continuity chain with its movement links |
| `zeroLossAsHistory` | the real collection stated to have survived with no loss | the `LOSSES` node and the printed "about 40,000 accessions" |
| `cleanProvesForged` | a clean document declared forged because it is clean | the printed rule that appearance is not one of the four tests |
| `settledDeathCount` | a specific staff-death number stated as settled with no qualifier in the proposition | the qualified count language, checked in every role |

The two historical-claim classes are excused inside a reconstructed evidence object and
inside a marked in-game quotation, and nowhere else. **This guard is bounded on
purpose**; an unseen paraphrase can pass it and manual cross-role review remains
required. Each class ships with negative controls the validator must flag and positive
controls it must not, plus structural and exemption mutation controls.

## Validation

- `apps/curriculum-editor/tests/validate_hhh_case09_seeds_they_kept.py` — the Case 09
  scoped validator, chained into `validate_static.py` alongside the other HHH case
  validators. At eventual release this same validator must validate Case 09's release
  record against `case-release-history.schema.v1.json`, following Case 08, because
  `validate_static.py`'s release-history loop does not reach HHH packages.
- `shared/validation/validate_hhh_activation.py --expect-editor-ready 11`
- `shared/validation/validate_canonical_case_structure.py`
- `shared/validation/validate_release_integrity.py`
- `shared/validation/validate_layout_overrides.py`
- `apps/curriculum-editor/tests/validate_static.py`
- `shared/validation/run_curriculum_browser_harness.py`

## Preservation

This candidate adds files under `hhh/campaign-2/case-09-seeds-they-kept/` and touches
nothing else in the curriculum tree. `sss/**`, `hhh/campaign-1/**`,
`hhh/campaign-2/case-07-the-audit/**`, `hhh/campaign-2/case-08-floating-gardens/**`,
`hhh/audit/**`, `hhh/blueprint/**`, `hhh/production/**`, the shared contracts and
schemas, the shared validators, the visual style guide and the Curriculum Bible are all
unmodified. The game is unmodified.

The only changes outside this directory are the narrowly necessary activation of the
existing Case 09 entry in the shared case registry, the registration of the case in the
browser-harness eligibility roster, and the Case 09 scoped validator with its chaining
line in `validate_static.py`.
