# HHH Campaign 2 · Core Case 08 — The Floating Gardens

**Case:** `HHH-C2-CASE08`
**Runtime source:** *Hunger, Harvest, & History*, Campaign 2 Level 1
**Setting:** Tenochtitlan, 1487 — the system is **historical**; the 1487 scene is **reconstructed**
**Instructional type:** `CORE_CASE`
**Version:** 0.1
**Status:** `APPROVED_STABLE` — released 2026-08-20
**Blueprint:** `hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md`, Core Case 08
**Audit baseline:** `hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md`
**Game commit:** `d9fc16baf272cb543c29cbd0c06ec85efad60be8`

The second unit of Campaign 2, and the first HHH case whose culminating product is a
geographic and historical systems explanation with source qualification. Produced
against curriculum main `337b6b23acb39b0df3bba248315839901c4a2eba` and the approved
Blueprint.

## Release state

| Gate | State |
| --- | --- |
| Package status | `APPROVED_STABLE` |
| Owner review | `OWNER_REVIEW_PASS` |
| Print status | `PASS` |
| Approval date | 2026-08-20 |
| Owner | Nate / Owner |
| Release record | [`history/release-v0.1.json`](history/release-v0.1.json) |
| Approval record | [`history/CASE08_OWNER_APPROVAL_v0.1.md`](history/CASE08_OWNER_APPROVAL_v0.1.md) |

The owner passed both gates — on-screen visual and content review, and physical print
review — and approved the byte set for release, stating: *"Approved, including physical
print review complete and approved."* The owner supplied no browser, printer, print
scale, paper type, paper size, colour or grayscale print mode or print setting, and none
is asserted anywhere in this release; the engineering colour and grayscale render checks
in the release record are a separate internal measurement.

### Printable baseline and certified-source commit are not the same commit

| | Commit |
| --- | --- |
| **Owner-approved printable baseline** | `a3bbb0388cdb4233500fcfd4deadc8c939a7426e` |
| **Released certified-source commit** | the release-conversion commit recorded in `history/release-v0.1.json` |

The owner reviewed and printed `a3bbb03`. Release conversion changes no printable
source: `content.html`, `presentation.css` and `layout-overrides.json` are
byte-identical to that commit, and only `task-registry.js` moves, in its two lifecycle
keys, neither of which renders. Because the released `task-registry.js` bytes first
exist at the release-conversion commit, the release record's source pins name that
commit rather than the printable baseline. The two are recorded separately and
deliberately, and conflating them is the error this section exists to prevent.

**No owner-approved bundle exists and none is claimed.** The release-history schema
requires no bundle field. The bundle produced during the original implementation report
covered the pre-remediation candidate `00f21423`, not this approved baseline, and there
is no evidence the owner inspected or approved any bundle file.

Production is HTML-only. No canonical PDF artifact exists, PDF generation is not a
release gate, and any PDF exported from the browser is noncanonical and carries no
accessibility guarantee.

## Game-baseline note

The Phase 1 Master Game Audit read C2 L1 at game commit
`9b8545ed6ecf98b337326390400076e36789e056` and raised one finding against it,
`HHH-GAME-C2L1-001`, classified `CURRICULUM_QUALIFICATION_REQUIRED`.

**That dependency is a teacher qualification, not a blocker.** There is no game
remediation requirement for Case 08 and this package requests none: the runtime title
stays as it is, the curriculum carries the qualification the audit asked for, and the
shared remediation dependency tracker is untouched.

**The qualification this package carries:** *"Floating Gardens"* is the runtime title
and a conventional English nickname. Chinampas are **raised fields** — ground built up
in shallow water from lake sediment, branches and decaying vegetation, on a staked
structure set into the lake bottom, with canals on either side. The nickname is taught
as a name; the construction is taught as the thing.

**Both halves of the qualification are enforced.** The packet does not teach that
chinampas floated, and it does not teach the opposite overcorrection either. Nothing in
it says or implies that the lake system was perfect or incapable of environmental
change: INAH records a severe flood in 1604 and four later rebuildings of the same
causeway, and the packet prints that.

## Central learning goal

> Explain chinampas as an engineered wetland/raised-field agricultural system
> integrating canals, soil renewal, intensive cultivation and hydrologic management,
> while evaluating what each class of source can and cannot establish about it.

**Guiding question:** How did the chinampa system work as an engineered landscape, and
what can each kind of source actually establish about it?

**Primary reasoning:** geographic reasoning + systems/contextualization + source limitation.
**Primary families:** H3 sourced historical map + H8 agroecosystem cross-section + H4
source contribution-and-limitation comparison.
**Culminating product:** an Engineered Landscape Explanation.

## Source status

Four bands, marked in markup (`data-evidence-layer`) and in printed text as a
`SOURCE STATUS · <CLASSIFICATION>` band on every evidence object.

| Band | Marked | What it covers |
| --- | --- | --- |
| `reconstructed` | `RECONSTRUCTED GAME EVIDENCE` | Sources A to E: the farmer, the soil reading, the lake works, the harvest count and the buried collapse account, with every count, name and reading belonging to them. |
| `documented` | `DOCUMENTED` | Sources G and H: the FAO documentation of the chinampa system, and INAH's archaeological reporting and hydraulic-works record. |
| `historical-map` | `HISTORICAL MAP` | Source F: the plan of Tenochtitlan published at Nuremberg in 1524, held by the Library of Congress. |
| `curriculum-model` | `CURRICULUM-ORIGINAL SCHEMATIC` | The two figures drawn for this packet. |

**The non-merger rule** is printed on page 1 of both learner editions: reconstructed
game evidence can support reasoning inside the case but cannot establish what happened
in 1487, and a real-world source can document the system but cannot prove any event in
the game.

Visible provenance follows
[`STUDENT_FACING_METADATA_AND_VISUAL_HIERARCHY_v1.0.1.md`](../../../shared/visual-style-guide/amendments/STUDENT_FACING_METADATA_AND_VISUAL_HIERARCHY_v1.0.1.md):
every learner-facing band is the short controlled label and nothing else, and the
scoped validator asserts that no other status string is printed anywhere. The
adaptation and basis lines that the two figures need under Visual Style Guide §§45–47
live in the caption metadata band, once, in the ordinary caption position.

## Source certification

The Phase 1 audit is **not modified**. Its certified source `H12` is reused as it
stands, and three further sources are certified **case-locally**, each bounded to the
claims it actually supports. The bounds are machine-readable in
`source/task-registry.js` under `sourceCertification`.

| Source | Certifies | Does not certify |
| --- | --- | --- |
| **FAO GIAHS, "Chinampas Agricultural System in Mexico City, Mexico"** (audit `H12`) | Wetland raised-field agriculture; construction from lake-bottom sediment, branches and decaying vegetation; the staking sequence and the two soil layers; the ahuejote willow; canals averaging ~1.5 m deep and 4–6 m wide; organic-matter renewal from aquatic vegetation; intensive year-round cultivation; canals as flood regulation; continuity today; designation in 2017; and the summary's own "floating artificial islands" wording. | Any particular year; anything in the game's case; any archaeological date; any claim that the fields floated. |
| **INAH, bulletin of 9 January 2024 on *Arqueología Mexicana* no. 184** | Chinampas far older than the Mexica; earliest in the basin 900–1200 CE at Xaltocan; adoption around the basin's lakes; a 2015 salvage excavation identifying chinampas and canals in use 1300–1521 CE in a Mexica district of ancient México-Tenochtitlan; the crops recovered. | Anyone's words; the date of any particular plot; any event in the game; any yield, area or population figure. |
| **INAH, "El Albarradón de San Cristóbal"** | Pre-Hispanic hydraulic infrastructure in the basin; a dike built against flooding at Tenochtitlan, to separate the waters within Lake Texcoco; attribution to Moctezuma Ilhuicamina and Nezahualcóyotl; destruction on Cortés's orders; rebuilding after the 1604 flood and in 1675, 1692, 1743 and 1856. | **Which part of the lake held which water**; the game's reconstructed east-and-west arrangement, which this source is expressly not used to certify; any salinity measurement; a date for the pre-Hispanic work; that the standing structure is preserved rather than rebuilt. |
| **Library of Congress, *Second Letter of Hernán Cortés*, Nuremberg: F. Peypus, 1524** | Publication at Nuremberg in 1524; the first published plan of Tenochtitlan, labelled *Temixtitan*; the letter dated 30 October 1520 and the plan depicting the city that year; the city founded in the fourteenth century on an island in the salt lake of Texcoco; wide causeways connecting the island city to the shores; the plan oriented with west at the top; the city attacked and destroyed in May 1521. Added on review, from direct inspection of the digitised plate: that the plate depicts settlements around the lake and along its shores, several carrying place-name labels; and that it draws the causeway connections at visibly uneven lengths and angles. | The city or its farmland in 1487; any count, direction or length of causeways; **any number of settlements, or the position, spacing or extent of any one of them**; the shoreline geometry or any distance; the placement of any settlement or causeway as it stood in 1487; any agricultural detail; any reading of the plan as a survey or an aerial view. |

No historical, agricultural, hydrological, chronological, quantitative or
archaeological claim appears anywhere in the package that is not on one of those
lists. If a later revision needs one, that is a source-certification dependency for the
PMO, not an authoring decision.

## Structure

Eight tasks. The numbers and titles are the Student worksheet's, and the Accessible
edition and every keyed Answer Key section preserve them exactly.

| # | Title | Function | Family |
| --- | --- | --- | --- |
| 1 | Build the Case Vocabulary | reference / vocabulary | — |
| 2 | Set a Geographic Test | initial interpretation **(non-keyable)** | — |
| 3 | Read the Lake-City Map | sourced historical map + limitation | H3 |
| 4 | Trace the Chinampa System at Two Scales | agroecosystem cross-section | H8 |
| 5 | Compare What the Sources Can Establish | contribution-and-limitation matrix | H4 |
| 6 | Test the Buried Collapse Claim | two-layer evidence separation | — |
| 7 | Explain the Engineered Landscape | culminating product | H8 + H4 |
| 8 | Transfer the Method | transfer / exit | — |

### Task 2 is deliberately not keyed

It records what a learner would go and look for **before** the sources that explain the
system arrive. There is no correct answer, and keying it would convert a record of
provisional thinking into a hidden multiple-choice item. The Answer Key omits it
without renumbering, which is the shared task-reference rule, and the Teacher Guide
carries the guidance for reading it diagnostically. No learner page states any grading
policy.

### CER is deliberately not used

The Blueprint permits canonical CER only where its structure genuinely supports the
case, and names a geographic and historical systems explanation with source
qualification as this case's product. A CER frame would force one claim to the front
and demote everything else to support, and this case assesses the opposite operation:
an accurate definition, two independent sourced links, a relationship between a
landscape and the farming it made possible, an explicit statement of what a named
source cannot establish, and a synthesis in which no part of the system is the claim
because each part only works through the others. This follows the precedent set by
Core Case 06 and Core Case 07; no role renders the shared canonical CER component and
no role declares a CER contract.

### Role page counts

Roles and page counts: Student 8 · Teacher 7 · Answer Key 4 · Accessible 10.

Those are the targets, met exactly.

**Student, 8:** page 1 front matter and Task 1; page 2 the five reconstructed sources;
page 3 Task 2 and the historical map card; page 4 the two documented cards; pages 5 and
6 one figure task each; page 7 the source matrix and the two-layer test; page 8 the
explanation and the transfer exit together.

**Teacher, 7:** the shared seven-function architecture, one function per page, with no
extra appendix.

**Answer Key, 4:** Task 2 is not keyed, and Task 5 is keyed as a completed matrix
rather than as prose, which is what holds the key to four pages while every keyable
field still carries a completed exemplar.

**Accessible, 10:** page 1 front matter; page 2 Task 1; pages 3 and 4 the reconstructed
dossier split in two; page 5 Task 2 and the map card; page 6 the two documented cards;
pages 7 and 8 one figure task each; page 9 the matrix and the two-layer test; page 10
the explanation and the transfer exit, as in the Student edition.

## Figures

Two, both curriculum-original, both deterministic HTML and CSS. **No imagery of any
kind** beyond the shared institutional insignia: no photographs, no generated art, and
no reproduced map plate.

| Figure | Task | What it does | Status treatment |
| --- | --- | --- | --- |
| The lake-city plan, adapted | 3 | Redraws relationships the Library's record states or the plate itself plainly shows: an island city in a lake, causeway connections to the shores at uneven lengths and angles, and settlement ringing the water. | `SOURCE STATUS · CURRICULUM-ORIGINAL SCHEMATIC`; caption `ADAPTED FROM · LIBRARY OF CONGRESS · SECOND LETTER OF HERNÁN CORTÉS, NUREMBERG, 1524 · RECONSTRUCTION · NOT TO SCALE` |
| The chinampa system at two scales | 4 | Panel A cuts through one field — canals, staked structure, the two soil layers, the cultivated surface, the willow, and the **lake bottom running beneath all of it**. Panel B is the basin: chinampa zone, open lake, dike, and the water beyond. | `SOURCE STATUS · CURRICULUM-ORIGINAL SCHEMATIC`; caption `BASED ON · FAO GIAHS CHINAMPAS DOCUMENTATION · INAH HYDRAULIC-WORKS DOCUMENTATION · RECONSTRUCTION · NOT TO SCALE` |

The lake bottom drawn under the field is the point of the second figure as much as the
layers are, and the sentence printed beside it — *the field is built up from the lake
bottom; it does not float* — is what the whole terminology qualification rests on.

### Why the historical map is adapted rather than reproduced

**This is a deviation from the stated preference and it is reported as one.** The brief
preferred an actual public-domain reproduction or crop for H3, and permitted an
`ADAPTED FROM` redraw where the plate is materially simplified. The redraw was chosen
for three reasons, all of which are the PMO's to overrule:

1. **The repository has never held a raster binary.** `shared/assets/` holds two SVGs
   and nothing else; no HHH or SSS case has ever committed an image. Introducing the
   first one is an architecture decision above the implementation scope this case was
   given, which is the narrowly necessary registry, harness and validator activation.
2. **Print legibility and grayscale.** The plate is a hand-coloured 32 cm folio
   woodcut. It survives grayscale at large sizes, but at the ~4.5 in width a worksheet
   page can give it, the causeway-and-lake relationship the task actually assesses reads
   less clearly than the redraw does, and the packet's brief is grayscale-first.
3. **Framing.** The plate is a conquest-era European print whose centre carries the
   ritual precinct and two racks of severed heads, and the Library of Congress attaches
   a cultural-sensitivity note to the collection. Reproducing it in a packet about
   Mexica agricultural engineering is a defensible editorial choice, but it is the
   owner's to make rather than the implementer's.

Nothing about the H3 obligation is weakened by the choice. The **source** is real,
named, dated and certified; **Source F** carries its provenance and the geography from
the Library's own catalogue record, and the learner reads and critiques *that*. The
figure carries `ADAPTED FROM` and `RECONSTRUCTION` accurately; its connectors are drawn
at uneven lengths and uneven, non-cardinal angles and it prints that their drawn number,
direction and length are **not historical measurements**; its shoreline settlement is drawn
as grouped runs that claim no number, position or spacing; and it prints that the source's
own orientation is west-at-the-top rather than imitating it. The exact asset, if the PMO
directs reproduction instead, is
`https://tile.loc.gov/image-services/iiif/service:gdc:gdcwdl:wd:l_:19:99:4:wdl_19994:ayer_655_51_c8_1524d_014/full/pct:50/0/default.jpg`
— the fold-out leaf, from which the city plan is the right-hand portion.

## The no-game dossier

Campaign 2 has **no** teacher level selector, no direct-launch mode, no injected state
and no developer shortcut, and none will be built. Every assessed piece of evidence
therefore exists in the learner packet. The four required reconstructed strands are all
present, plus the account the case exists to test:

- **A · the farmer at the plots** — *cultivation.* Several harvests a year, no rest,
  canal mud re-laid each season, the plot older than living memory.
- **B · the plot soil** — *soil.* Layered lake mud and decaying green matter, an active
  and continuously replenished nutrient cycle, no salt crust.
- **C · the lake works** — *waterworks.* An earthwork across the open water, pierced by
  gates, with the water held apart on purpose.
- **D · the harvest count** — *harvest record.* Named plots and counted seasons running
  generations deep, painted only where three independent counts agreed.
- **E · the buried collapse account** — the claim under test, and the one thing visible
  in it: it names no plot, no season and no keeper.

No runtime correct-answer flag, candidate-record label, hint, resolution text, clue
identifier, node identifier or control label is reproduced anywhere in the packet, and
no assessed item depends on a line that appears only in play. The Teacher Guide supplies
both routes.

## Standards

Three directly assessed, two supporting, no NGSS at any status.

| Standard | Status |
| --- | --- |
| C3 D2.His.1.6-8 | Directly assessed |
| C3 D3.2.6-8 | Directly assessed |
| CCSS RH.6-8.7 | Directly assessed |
| CCSS RH.6-8.9 | Supporting |
| CCSS WHST.6-8.2 | Supporting |

**RH.6-8.9 is deliberately held at supporting.** The packet does set a plan published in
1524 beside present-day documentation, archaeological reporting and reconstructed
evidence — but no task asks a learner to analyse the relationship between a primary and
a secondary source on the same topic. Tasks 5 and 6 ask what each source can and cannot
carry, which practises the relationship that analysis rests on without performing it.

**No NGSS performance expectation is claimed at any status, not even Contextual.** The
system is agricultural and hydrological and a science standard would be easy to reach
for, but no task asks a learner to construct a scientific explanation, model a natural
system or analyse data.

## Declared Accessible adaptations

Four, and only four; the Accessible edition was authored alongside the Student edition
rather than retrofitted.

| id | Task | What | Effect |
| --- | --- | --- | --- |
| `t3-supplied-setting` | 3 | Part A is supplied complete as a worked example: the island-in-a-lake setting is named. | Accessible answers **3** parts; Student answers 4. The connection, the geographic reasoning and the limitation all stay independent. |
| `t4-modelled-relationship` | 4 | Part B, the canal functions, is worked in full as a modelled relationship. | Accessible answers **3** parts; Student answers 4. Construction, soil renewal and the basin scale stay independent. |
| `t5-modelled-row` | 5 | The reconstructed-evidence row is supplied complete in both cells. | Accessible completes **5** matrix fields; Student completes 8. |
| `t5-prefilled-cell` | 5 | The FAO row's contribution cell is supplied; its limitation is not. | The judgment in that row is preserved. |

Everything else changes the route rather than the demand: bounded choices in Tasks 2
and 8, direct source pointers and sentence frames in Task 6, sentence openers in Task 7.
**Both figures are identical in the two editions**; the Accessible edition supplies no
figure label that the Student edition does not.
**No Accessible-only obligation exists** — every assessed Accessible response has a
Student counterpart, checked structurally against `editionResponseContract`. Accessible
pagination is continuous flow rather than one task per page.

## Semantic regression contract

The registry owns the vocabulary; the scoped validator compiles it. **Three closed
negative classes**, each anchored to a named subject register, each requiring an
affirmative and unnegated predicate, and each paired with a positive structural
requirement checked against markup rather than prose:

| Class | Rejects | Positive counterpart |
| --- | --- | --- |
| `chinampasFloat` | chinampas literally float, drift, or are rafts | the nickname qualification and the not-floating rule must both be printed in both learner editions |
| `reconstructionAsPrimary` | reconstructed game material presented as surviving 1487 evidence | the four-band source-status notice and the two-layer organiser must both be printed in both learner editions |
| `mapAsExactSnapshot` | the 1524 plan described as an exact map, survey or snapshot of 1487 | the map card's date and provenance limit must be printed in both learner editions |

**This guard is bounded on purpose.** It is a defence against three known
misconceptions, not a proof that every possible bad paraphrase has been detected. Every
class is a closed set anchored to a subject; none enumerates synonyms for an open
concept; and the validator's own docstring says plainly that an unseen paraphrase can
pass it and that ordinary cross-role manual review remains required.

Each class ships with **negative controls** the validator must flag and **positive
controls** it must not, including the five sentences that have to stay legal:
*"Floating gardens" is a conventional nickname* · *Chinampas are raised fields
constructed in wetlands* · *The game reconstructs a plausible scene for investigation* ·
*The 1524 published map can provide geographic evidence while still having limits* ·
*Historical evidence supports chinampa agriculture without proving every detail of the
game scene.*

Exemption is a closed contract. A node is excused only by naming a registered exemption
id that resolves for its own role, so a Teacher page can quote a misconception in order
to refuse it while a learner page cannot. Two mutation controls prove that an
unregistered id and a borrowed-role id both excuse nothing.

## Validation

- `apps/curriculum-editor/tests/validate_hhh_case08_floating_gardens.py` — the Case 08
  scoped validator, chained into `validate_static.py` alongside the other HHH case
  validators.
- `shared/validation/validate_hhh_activation.py --expect-editor-ready 10`
- `shared/validation/validate_canonical_case_structure.py`
- `shared/validation/validate_release_integrity.py`
- `shared/validation/validate_layout_overrides.py`
- `apps/curriculum-editor/tests/validate_static.py`
- `shared/validation/run_curriculum_browser_harness.py`

## Preservation

This release adds files under `hhh/campaign-2/case-08-floating-gardens/` and touches
nothing else in the curriculum tree. `sss/**`, `hhh/campaign-1/**`,
`hhh/campaign-2/case-07-the-audit/**`, `hhh/audit/**`, `hhh/blueprint/**`,
`hhh/production/**`, the shared contracts and schemas, the shared validators, the visual
style guide and the Curriculum Bible are all unmodified. The game is unmodified.

The only changes outside this directory are the narrowly necessary activation and then
release conversion of the existing Case 08 entry in the shared case registry, the
registration of the case in the browser-harness eligibility roster, and the Case 08
scoped validator with its chaining line.
