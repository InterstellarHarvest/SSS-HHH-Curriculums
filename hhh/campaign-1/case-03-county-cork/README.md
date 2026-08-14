# HHH Campaign 1 — Core Case 03 · County Cork

**Identity:** `HHH-C1-CASE03` · instructional type `CORE_CASE` · registry title *County Cork* · learner-facing label **3 - County Cork**

The third full historical Core Case in Hunger, Harvest, & History. Produced against the
released Core Case 02 baseline `ca21e3eda282c1d46b53abe7966e9e0176db96bc` and the approved
Blueprint.

## What this case teaches

Why potato late blight became a famine. The reasoning operations are multiple causation,
contextualization and corroboration, and the disciplinary problem is **sufficiency**: a
documented biological cause is available, it is correct, and it does not explain the death
toll. The culminating product is a **multi-causal historical explanation** (Task 8) with
four required components: what the blight did and what it explains, two conditions carrying
specific sourced evidence, one explained interaction between conditions, and a stated limit
followed by a closing sentence pitched at the right strength. Task 9 transfers the
crop-failure/famine distinction to an invented district the case never supplied.

## Deliberate design decisions

**A control, not a disclaimer.** Case 01's spine was chronology and Case 02's was scale;
this one's is sufficiency, and it is settled by evidence rather than by assertion. The blight
struck Belgium and Ireland in the same two years. **Belgium lost almost 90% of its 1845 potato
harvest against Ireland's roughly 30%** — the larger crop loss — and Belgian famine mortality
ran 30–40% above normal while Ireland's ran at about three times normal. Same organism, bigger
crop failure, far smaller death toll. That comparison is Task 4 Part B, and it is what makes
"blight alone caused the famine" fail in front of the student rather than being pre-empted by
the teacher. Every later task stands on the space it opens.

**Task 2 is deliberately not corrected.** Learners arrive holding the single-cause
explanation, and the packet asks them to write it down on page 4 before they have the
evidence to revise it. The Teacher Guide says explicitly not to correct it, and the last
minutes of period 3 send them back to that page. The case is designed so the student changes
their own mind; that is the historical skill, and telling them the answer is complicated on
day one teaches a slogan instead.

**The causes map carries no weights, and says so on the figure.** The Blueprint's warning
about Family H5 is that arrow geometry can imply unsupported certainty. Nothing in this
packet ranks the four conditions, so the four condition boxes are one row of identical width,
their four converging arrows are drawn identically, and a printed note inside the drawing
states that every arrow means *contributed to* and that nothing here ranks them. A browser
assertion measures the four box widths off the rendered figure, because a stylesheet edit
could weight one box while every sentence on the page stayed true.

**A real 1846 document sits beside written-for-the-game dialogue on purpose.** Source D is
Nicholas Cummins's letter from Skibbereen, published in *The Times* on 24 December 1846 — a
real, named, dated, published account. Sources A–C are the Archive's scenes. Task 5 rows one
and two make the difference assessable, and the printed status lines are bound to
`caseSources`, so relabelling either one becomes a contradiction between two files rather
than a proofreading question. The letter is quoted only as far as its opening sentence; the
packet says in print that what follows is severe and is not reproduced.

**The export question is left undecided, because it is.** Task 7 Claim 4 asks whether keeping
the exported food in Ireland would *by itself* have prevented the famine, and the keyed mark
is **?**. Both published positions are carried: Bourke's tabulation of the official grain
returns showing imports exceeding exports by 1847, and Kinealy's argument that those returns
are flawed, under-record what left, cover only grain and cannot gauge food loss, with imports
becoming significant only after spring 1847. Nothing in the packet weighs food that left
against food that was needed, so a Y and an N are equally unsupported. The Answer Key credits
a defended N at the level below full marks and says why.

**Single causation is refused in both directions.** Claim 2 is the biological single cause the
audit required qualifying; Claim 5 is the political single cause students reach for once they
meet the export and relief evidence. Both are marked **N**. The Answer Key states that
"the British government caused the famine" fails the culminating product exactly as
"the blight caused the famine" does, and should be returned rather than scored generously.

**The variety story is qualified rather than repeated.** The game's field survey finds one
clonal variety and no plant standing clear of the rot, and that is kept. What is added is the
qualification the scholarship actually supports: **every potato variety commonly grown in
Ireland at the time also fell to the blight**, so planting a different one would not by itself
have saved the crop. What uniformity removed was not resistance; what dependence removed was
anything to fall back on.

**The place figure is not a map.** A drawn map of Ireland would have to claim a coastline, and
famine intensity drawn onto one would claim a geography this packet cannot source. The figure
is a nested place diagram — Europe, Ireland, Munster, County Cork, with Cork and Skibbereen
named inside it and Belgium marked at the European level — asserting only what is inside what.
Every name prints at readable size rather than surviving in the accessibility description
alone, which is the Case 02 lesson, and the figure states in print that nothing is to scale or
in its true position.

**"Timeline", not "rail".** The chronology figure is called a timeline on every learner page.
Its two strands, CROP and RELIEF, each print their own word on every row rather than relying
on a tint, and the sequence they make visible — the largest relief measures arriving after the
second and worst failure, and the soup kitchens closing the same summer they reached three
million people — is what Task 7 Claim 5 is read against.

**No canonical CER.** A Claim–Evidence–Reasoning frame asks a student to defend one position.
This case's product is an explanation that must hold several conditions together and state
what it cannot settle, and a frame built for taking a side would push toward exactly the
single-cause account the case exists to prevent. Teacher page 5 states the reasoning
architecture for classroom readers.

**Three periods, stated.** Nine tasks with seven sources, four figures and this evidence load
do not honestly fit one period or two. Period 1 ends after Task 3, period 2 covers Tasks 4
and 5, period 3 covers Tasks 6 to 9. The Teacher Guide names the assessed route rather than
compressing it, and page 1 carries a fallback priority that says which criterion is lost if a
period is lost.

**Emotional load is addressed, not avoided.** Teacher page 4 carries a note on it. The subject
is the deaths of about a million people; the packet treats those deaths as evidence because
that is what the archive does, and says so.

**Why there is no `source/evidence-ledger.json`.** The Blueprint names a structured ledger as
the preferred implementation *when useful*. The registered package schema is closed
(`additionalProperties: false`) and its `sourceHashes` object is closed, and the shared HHH
source-ownership check requires a package to pin exactly its four canonical sources — so a
fifth file could only be carried as an embedded asset, pushing production metadata into
classroom output, or as an unreferenced orphan. The evidence model therefore lives where
Cases 01 and 02 carry it and where validation can already reach it: the `caseSources` array in
`task-registry.js`, at the full Blueprint §11.6 field set including `contribution`,
`limitation`, `gameCorrespondence` and `fallbackCorrespondence`, plus the Teacher Guide source
ledger on page 6. No shared schema was changed for this case.

`caseSources` carries **ten** entries, one per Teacher-ledger row plus the Lumper
qualification, which is a separate reading from the dependence evidence and is registered
separately so its own limitation travels with it. The tenth is the curriculum-original causes
map: it is registered at `evidentiaryStatus: modeled`, its limitation states plainly that it
is a drawing made to organise an argument rather than evidence, and Task 5 row five requires
the learner to say so.

## Source provenance

**Game material.** Dossier cards A, B and C quote or paraphrase HHH Level 3 at the integrated
game baseline `d9fc16baf272cb543c29cbd0c06ec85efad60be8`. Those cards are labelled
`STATUS: reconstructed · written for the game` and are never presented as testimony. A browser
assertion rejects any status line on a game-origin block that uses the words *primary source*,
*eyewitness*, *first-hand* or *testimony*.

**Real-world evidence.** Every figure, date and claim in the packet traces to one of the eleven
references listed on Teacher page 7:

- Coomber, Saville & Ristaino, *Nature Communications* 15:6488 (2024) — *P. infestans* as an
  oomycete; FAM-1 as the lineage of the Famine epidemics; 1845–1852, about a million dead and
  about a million emigrating.
- University of Minnesota Extension, *Late blight* — the pathogen as a water mold; the lesion
  and sporulation sequence on the leaf underside; tuber decay; cool damp conditions; thousands
  of sporangia per lesion in under five days.
- Ronsijn & Vanhaute (Ghent University), RTÉ *The Great Irish Famine* — the two-country
  comparison: Courtrai in June 1845, Ireland by mid-September; almost 90% of Belgium's 1845
  harvest against about 30% of Ireland's and over three quarters in 1846; over 40,000 famine
  deaths each in Belgium and Prussia at 30–40% above normal against about a million in Ireland
  at about three times normal.
- O'Keeffe (University College Cork), RTÉ — a third of the population taking about 90% of its
  food from the potato by the 1830s; 10–14 lb a day for a labourer in the west; nearly six
  tonnes from an acre of ridged beds; a quarter of a million acres under potatoes in County
  Cork; 8.2 million people in 1841 with nearly half of rural families in one-room cabins.
- Reilly (Maynooth University), RTÉ — the cottier class at more than three million in the early
  1840s; about 200 days' labour a year under unwritten agreements terminable at a moment's
  notice; almost no cash and persistent debt.
- Ó Gráda, *History Ireland* — the Lumper's introduction and spread, and the qualification this
  case depends on: every other variety commonly sown at the time also succumbed to the blight.
- Bourke, *Irish Historical Studies* 20/78 (1976) — the grain-trade tabulation showing imports
  exceeding exports by 1847, carried as one published reading rather than a settled figure.
- Kinealy, *History Ireland* — almost 4,000 vessels in 1847; over three million live animals
  1846–50; the argument that the official returns are flawed and cannot gauge food loss.
- Gray (Queen's University Belfast), RTÉ *Famine Ireland* — the relief chronology: Indian corn
  to Cork in early 1846, public works over 700,000 in March 1847, soup kitchens over three
  million in July 1847 and discontinued in August, then the Poor Law.
- O'Keeffe, RTÉ *Famine Ireland* — the Poor Law Extension Act of June 1847, the Gregory
  quarter-acre clause, relief costs moved onto Irish rates, evictions rising after 1847.
- Cummins, letter to the Duke of Wellington, *The Times*, 24 December 1846 — Source D.

**No false precision.** No death figure is attached to any single policy decision. No condition
on the causes map is weighted against another. Every quantity that appears is a national or
institutional figure reported by the historians above, and none is presented as a measurement
of County Cork. The one County Cork quantity in the packet — a quarter of a million acres under
potatoes — is attributed and is about acreage, not mortality.

## Game-remediation dependencies

`HHH-GAME-C1L3-001` — **resolved and verified independently against `d9fc16b`**. The audit
recorded three universalizing formulations in the level's correct diagnosis and closing record:
"whole country", "every field was the same plant repeated", and "nothing else grown to fall
back on". All three are gone at the integrated baseline. `hhh_data.js` now reads "around a
third of Ireland's people — its poorest tenant families above all — lived mainly on the
potato", "field after field held the same plant repeated", and "Other food was grown in Ireland
all through the hunger, but the poorest had no claim to it", with causation split explicitly:
"The blight killed the potato; poverty, the land system, and the choices of those in power made
the deaths." The severe Lumper clonal-dependence vulnerability is retained, as the disposition
requires. Verified by direct byte inspection of the level at `d9fc16b`, not from the tracker
summary.

The curriculum keeps the disposition rather than merely inheriting it. The three audited
universals are recorded in `task-registry.js` under `causationBoundary.prohibitedClaims`,
together with three single-cause formulations this case must also refuse, and a browser
assertion reads that list from the registry and keeps every phrase out of every role.

One observation is recorded rather than corrected: the level's traveller says the blight has
struck "the whole country" and "the whole island". That is a character's claim about the
*extent of the disease* after a four-day walk, not a claim about dependence, and the audit
itself classifies that source as in-game testimony that "cannot alone establish system-wide
prevalence". The packet treats it that way: the traveller appears in dossier card C reporting
what they have passed in four days, and Task 5 row one requires the learner to state what the
Archive's scenes cannot establish.

## Package contents

```
source/case-package.json     canonical registered package
source/content.html          all four roles as one worksheet fragment
source/presentation.css      case presentation, TAA identity, HHH tokens
source/task-registry.js      nine tasks, authoritative for numbers and titles
source/layout-overrides.json response eligibility and lock classification
```

Roles and page counts: Student 8 · Teacher 7 · Answer Key 6 · Accessible 13.
Grayscale is a presentation state on every role, never a fifth role.

### Why those counts

**Student 8.** Page 1 framing and vocabulary; page 2 the whole dossier — seven sources and
the documented background on one spread, because the no-game route has to reach further than
the game does (Level 3 ends in 1845 and everything dated 1846 or later exists only in the
packet) and because Tasks 5 and 8 both reason across sources that a page break would separate;
page 3 the first reading with the timeline and place figure; page 4 the trigger and its
control, which must sit together or Part B loses its evidence; page 5 the five-row source
matrix, which is the only content on its page because fifteen handwritten cells need the room;
page 6 the causes map; page 7 the five claims; page 8 the explanation and the transfer. The
dossier was drafted across two pages and merged: each was little more than half full, and two
half-empty reading pages are worse than one complete evidence spread. Case 02 needed eight
pages for four sources and three figures; this case fits seven sources and four into the same
eight.

**Teacher 7.** The shared seven-function contract, unextended.

**Answer Key 6.** Nine tasks, one more than Case 02's five-page key needed, because the matrix
exemplar is fifteen cells rather than twelve and because Tasks 6, 7 and 8 each require a full
page: the interaction exemplar, the five marks with the reason for each plus the undecidable
claim's rationale, and the four-component culminating model.

**Accessible 13.** Five more than the Student edition, and each is a specific adaptation
rather than the same material spread thinner. The dossier occupies four pages instead of one,
so no page mixes a heavy reading load with a heavy writing load. Task 4 is split so the
two-country comparison sits on the same page as the Part B prompt that reasons from it, rather
than a page earlier — the Case 02 lesson about not making a learner flip pages mid-reasoning.
Tasks 8 and 9 take a page each, so the culminating product is not rationed to make room for the
exit. The reading pages end short of the footer on purpose; the Bible permits intentional
unused space, and on an emotionally heavy evidence packet at 10.4pt that white space is a
support rather than a defect.

## Regression protection added with this case

Beyond the generic HHH package checks, the browser harness carries Case-03-specific assertions
covering: the audit-rejected universals and single-cause formulations, read from the registry
rather than hard-coded; severe dependence retained without a whole-country universal; the
reconstruction-and-causation boundary present in both learner editions with the same wording;
learner source statuses compared against `caseSources.evidentiaryStatus`; a primary-source and
eyewitness prohibition scoped to game-origin blocks only, so the case can carry a real 1846
document without weakening the rule; the Skibbereen letter identified by author, publication
and date; the comparison bars measured off the rendered figure so Belgium's larger loss cannot
silently invert; the comparison values compared with the registry; the causes map's four
condition boxes measured for equal width and its four converging arrows counted; the
"contributed to" and no-ranking disclaimers required inside the figure; the timeline's two
strands each printing their own word with relief after the second failure; every place name
required in print with a collision measurement; the keyed claim marks compared with the
registry including exactly one undecidable; both export positions carried; the variety
qualification preserved; and twelve load-bearing no-game facts required in both learner
editions.

Eight negative controls were run against these assertions — an audited universal restored, the
1846 letter relabelled a reconstruction, a game scene relabelled eyewitness testimony, the
comparison inverted, the Belgian value deleted from the Accessible edition, one condition box
weighted, the no-ranking disclaimer deleted, and a prohibited phrase removed from the registry
contract. All eight were caught. The first run of the Belgian-value control was **not** caught,
because the fact test matched the causes map's unrelated "90%"; the test was bound to the
printed comparison value and the control then failed as it should.

## Lifecycle

Production candidate. `status: VALIDATION_BUILD`, registry `packageStatus: VALIDATION`,
approval `OWNER_REVIEW_NOT_STARTED`, print `NOT_RUN`. Version 0.1.

No owner approval has been given. There is no `history/` directory, no release record and no
`APPROVED_STABLE` state, and the registry entry carries no `historyRecord`. This package has
not been reviewed independently, has not been printed, and is not released.

Production is HTML-only; no canonical PDF artifact exists and PDF generation is not a release
gate. A PDF exported from the browser is noncanonical and carries no accessibility guarantee.
