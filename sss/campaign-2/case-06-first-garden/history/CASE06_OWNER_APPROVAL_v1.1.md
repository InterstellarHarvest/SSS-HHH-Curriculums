# Campaign 2 Case 06 v1.1 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-06**

Title: **The First Garden**

Curriculum: **SSS · Campaign 2 · Case 06**

Runtime ID: **first_garden**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective of: **1.0**

## Gates

- On-screen content and visual review, including grayscale: **PASS**
- Generated PDF review: **PASS**
- Physical print at 100% / Actual Size: **PASS**

The physical-print gate was re-run for this release rather than carried over. Every learner page
changed, and the Student edition gained a page, so the v1.0 attestation could not stand.

## Approved page counts

- Student Mission: **6 pages** (5 at v1.0)
- Teacher Guide: **8 pages** (unchanged)
- Answer Key: **5 pages** (unchanged)
- Accessible Mission: **7 pages** (unchanged)

The Student increase is forced by restored evidence and was measured, not estimated: with the five
Task 4 source reports present, `student-mission-04` overflowed its printable area by 106 pixels, so
Task 5 moved to a page of its own. The approved combined Student CER and Task 7 page under
`data-student-cer-page="combined-v1.0"` is unchanged and still fits, with 11 pixels of reserve. The
Accessible CER keeps its dedicated page under `data-accessible-cer-page="canonical-v1.0"`.

Accessible was briefly taken to 8 pages while Task 4's five source reports were carried in
one-source-at-a-time blocks. That layout left a continuation page with no complete task on it, which
the shared Accessible page contract forbids, so Task 4 was rebuilt as Table 5 on the Case 05 model
instead — the campaign's reference implementation for this exact task. Accessible therefore stays at
7 pages, and both learner editions now number the same six evidence tables.

Fixed Letter geometry is unchanged: 816 × 1056 CSS-pixel worksheet pages with 720 × 960 CSS-pixel
page frames, PASS for all four roles. Grayscale remains a presentation-only state and creates no
further role, page-count category, or output filename.

## Figure A correction

Figure A is a plan view of circular patches where the surveyed compounds are abundant, drawn inside
ground where the same compounds fall to trace levels, because *circular patches of approximately
four to six metres in diameter* is what the survey reports.

Two unsupported claims are removed:

- A dimension line spanned the gap between the first two circles, labelled **"about 3 m"**. That is
  Dr. Nova's described separation between thriving and failing ground repurposed as a surveyed
  patch-edge offset — which the packet's own precision ledger already forbids: *"a described
  separation, not a surveyed boundary offset."* The line, its ticks and the matching
  extended-description clause are gone from both learner editions.
- The extended descriptions assigned individual measurements to the drawn circles ("the three drawn
  here are about five, six and four metres"), inventing three measured patches from a reported
  range. Those clauses are gone.

The figure now carries exactly one quantity: the survey's reported diameter range. It is not to
scale, states no distance between patches, and gives no individual patch a measurement of its own.
Its caption and extended description both state that it shows the reported pattern rather than
mapping the garden. Pattern fills, direct labels and grayscale legibility are unchanged.

`task-registry.js` `figureProvenance` — the declared ledger of record — described a twelve-metre
strip with abundance from 0 to 5 metres and trace levels from 5 to 8. It now describes the rendered
plan view and records that the figure is not to scale, as does `sourceStatus.figures`, the README,
and the Teacher Guide's figures-and-tables ledger.

## Evidence-availability corrections

An Answer Key must be producible from the evidence a learner actually holds. Three failures are
corrected:

- **Task 4 graded five sources; three had no printed statement in any learner edition.** The Answer
  Key graded against Kess's mechanism, `Section 14.7` (printed one task later) and `GC-2201`
  (printed nowhere a learner could read). Student Table 5 now carries a *Source and what it reports*
  column: Dr. Nova and Delegate Vorn-Shael are summarised and cross-referenced to records printed
  earlier in the same edition, while Delegate Kess, Delegate Ilreth-Mar and the Federation Database
  print their statements at the task. The Accessible edition carries the matching Table 5 in plainer
  register.
- **Accessible Task 1 was unanswerable.** Its table had dropped the Student edition's record column,
  so no Accessible learner could tell which of the nine rows was never tested. The column is
  restored in shorter register, and the Accessible survey table gains the reduced-transport row the
  Answer Key credits.
- **Task 3's third rejection had no record in either learner edition.** The Answer Key rejects
  invasive organisms because the patchiness predates the summit by decades; neither the Student nor
  the Accessible edition printed that. Both now do.

The Answer Key was also regraded to the wording learners hold: its "reduced transport signature"
clause now uses the printed comparison, and it records that the Accessible edition lists the
signalling compounds without naming the three individually.

## Task 1 analogy placement

The building-inspection analogy that the v1.0 approval record binds to Task 1 was printed on page 2,
*after* Task 1, in both learner editions. It now prints inside Task 1 — after the task heading and
before the record the task is graded on — as Case 05 places its rain-gauge analogy. Both editions'
Task 1 directions now send the reader to the example first. The analogy still introduces no numeric
value at all and still states on the page that it is not a garden record.

## Cross-role numbering

The Student vocabulary table was numbered `Table 1` while the Accessible equivalent was unnumbered,
so every Student evidence table sat one number above its Accessible counterpart and four Teacher and
Answer Key references misresolved for Accessible readers. Vocabulary is now an unnumbered aid in
both editions, and every remaining number is an evidence table meaning the same record in both.
"Figure A and Table 2 report the same survey", "Table 3 supplies the piece students need" and
"Tables 1–6 are the case records" resolve in either hand.

## Teacher Guide synchronization

Four statements the owner-review revision `59005a8` left behind are corrected: Figure A described as
drawn along a twelve-metre strip and as "the strip"; the claim that the CER occupies a full page in
**both** learner editions, when the Student CER uses the approved combined Task 6/7 contract; the
claim that the Accessible edition's evidence is identical, when its presentation is not; and the
analogy located on Student page 2. The guide now describes the adaptation the case ships.

## Accessible differentiation

The Accessible edition carries the same evidence and the same diagnosis as the Student edition and
presents them differently: one task per page, every record rewritten in plainer register and
shortened, sentence frames or a word bank on each page, and a dedicated CER page. Measured
similarity is **56.0%**, inside the 70% ceiling. At v1.0 it measured 51.0% and was the most
differentiated edition in either campaign; restoring the evidence its own tasks are graded on moved
it to second, behind Case 05's 55.4%. That is the intended trade: the audit recorded this edition as
structurally the most ambitious in the campaign and the least self-sufficient, and self-sufficiency
was the defect.

## Standards outcome

- **MS-ETS1-1 — direct, assessed at Task 7.** Students write the two success criteria the trial must
  meet and name one constraint it must work within, against a printed record specifying organism
  identification, pathogen and invasion screening, prior approval under Section 14.7, replicated
  untreated control plots, and scheduled monitoring.
- **MS-LS2-3 — supporting, at Task 5.** Students order a pathway in which fungi receive plant carbon
  and can improve a host's acquisition of phosphorus, nitrogen or water. Supporting and not direct
  because the case supplies no cycling or energy-flow measurement at all.
- **MS-LS2-2 — withdrawn**, not downgraded. Its performance expectation predicts patterns of
  interactions among organisms across multiple ecosystems; this packet holds one restored terrace
  with two bed histories, and the task named to carry it was a source contribution-and-limit matrix
  rather than the construction of an explanation, which happens at Task 6. **No life-science
  standard is substituted for it.**
- **MS-ETS1-2 — withdrawn.** Task 3 weighs competing explanations, not competing design solutions
  against shared criteria. Task 3 was **not** expanded into a design comparison in order to keep the
  standard.

Both withdrawals record what would be needed before the standard could return, in
`task-registry.js` `standardsWithdrawn` and `productionCautions`. No mathematics standard is
claimed; the case contains no calculation.

## Science boundary

Every approved protection is retained and mechanically demonstrated: no "wood wide web" as settled
science, no mother-tree claim, no forest or garden superorganism, no collective fungal intention, no
claim the network was never restored, no claim that particular partners are confirmed absent, no
guaranteed cure, no promised recovery time, no unscreened transfer, no claim that Earth origin makes
transfer risk-free, no waiver of Section 14.7, no universal fungal benefit, no named commercial
product, no blame assigned to the restoration team, and no global hyphal-length or carbon-flux
figures in any learner role. "Trace levels only" never becomes zero, absent, or none. The
mycorrhizal explanation remains a candidate cause throughout.

## v1.0 preservation

`history/release-v1.0.json` and `history/CASE06_OWNER_APPROVAL_v1.0.md` are retained **byte-identical**
and were not edited to describe v1.1. v1.0 is represented in `release-v1.1.json` as the prior
approved release, carrying its own approval date, commit, source hashes, DOM baselines and page
counts (Student 5, Accessible 7).

Two known v1.0 record defects are deliberately **not** corrected, because v1.0's records are
immutable historical evidence: its accepted-validation figures were understated at the commit they
describe (`148/148` and `static 576/576`, where the released tree produced `153/153` and `580/580`),
and its `sourceHashes` omits `layoutOverrides`, as all six Campaign 2 v1.0 records do. Both are
repaired going forward — the v1.1 record pins all four source hashes and records the totals its own
suites actually produce.

The frozen Student, Teacher and Answer Key DOM baselines were regenerated for v1.1. All three differ
from v1.0's, so approved-baseline enforcement cannot be satisfied by the superseded v1.0 markup.

## Generated artifacts

None. Case 06 was authored natively as a case package and reissued the same way. No master, published
role HTML, PDF, screenshot, or other generated release artifact was created or committed at either
version. Git history remains authoritative for recovery.

## Campaign-level work deferred

This approval covers Case 06 only. Campaign 2 is **not** complete: Cases 01, 04 and 05 remain
unremediated against `sss/audit/SSS_C2_CAMPAIGN_COMPLETION_AUDIT_v1.0.md`, and the shared-validation
maintenance, the cleanup-audit retirement and the `CURRENT_PROJECT_STATE.md` correction the audit
records in §12 and §13 are all out of scope here and remain open.
