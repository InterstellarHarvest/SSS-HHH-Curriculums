# Campaign 2 Case 01 v1.1 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-06**

Title: **Heavy Hands**

Curriculum: **SSS · Campaign 2 · Case 01**

Runtime ID: **heavy_hands**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective of: **1.0**

## Gates

- On-screen content and visual review, including grayscale: **PASS**
- Generated PDF review: **PASS**
- Physical print at 100% / Actual Size: **PASS**

The physical-print gate was re-run for this release rather than carried over. All four printable
roles changed and the Teacher Guide gained a page, so the v1.0 attestation could not stand.

## Approved page counts

- Student Mission: **5 pages** (unchanged)
- Teacher Guide: **9 pages** (8 at v1.0)
- Answer Key: **4 pages** (unchanged)
- Accessible Mission: **8 pages** (unchanged)

The Teacher increase is forced by the correction and was measured, not estimated. With the
attributed conditions table, the *Reported is not tested* note and the GC-1445 limits note present,
`teacher-guide-04` overflowed its printable area by **245 pixels** and `teacher-guide-08` by **54**.
The essential evidence ledger now spans two pages — the reference figure, the gravity profile and
the crop history on page 4; the reported conditions and the Concord records on page 5 — and the
quick-grading guidance moved onto the discussion page.

Accessible was held at 8 pages deliberately. It runs one task per page across eight tasks, so a
ninth page would leave a continuation page carrying no complete task, which the shared Accessible
page contract forbids. Task 1 and the CER page were fitted within that constraint instead.

Measured slack after correction, in CSS pixels of a 936-pixel content area, with no page
overflowing in any role:

- Student 30 / 143 / 76 / 362 / 39
- Teacher 252 / 42 / 275 / 281 / 337 / 152 / 216 / 403 / 61
- Answer Key 147 / 471 / 49 / 185
- Accessible 8 / 432 / 391 / 354 / 521 / 332 / 0 / 211

Fixed Letter geometry is unchanged: 816 × 1056 CSS-pixel worksheet pages with 720 × 960 CSS-pixel
page frames, PASS for all four roles. Grayscale remains a presentation-only state and creates no
further role, page-count category, or output filename.

## Reported versus tested

This is the correction the release turns on. The v1.0 packet taught that soil, nutrients, light and
water were each changed or verified across three plantings without effect. The canonical runtime
records **two** interventions: Crop 2 reformulated the soil, Crop 3 used new seed stock. Nutrients,
light and water are reported by the botanist as **present conditions** — *"Nutrients: precise.
Light: calibrated to Vress-standard grow spectrum. Water: clean."* — and were never varied.

The Campaign 2 completion audit states that water is never mentioned in the case. It is, but only as
a present reading, so the audit's conclusion holds and this correction is written to the runtime
text rather than to the audit's summary.

A present reading says what a condition **is**. It does not say what happens when that condition
changes, so it never rules a condition out. The packet now teaches that distinction rather than
leaving it implicit:

- both learner editions print the botanist's present-condition report beside Table 1;
- Table 2 asks whether a condition was **changed between plantings**, not "changed or verified";
- both editions state on the page that **N marks an untested condition, not an eliminated one**;
- the Teacher evidence ledger gains a *Reported by* column and a *Reported is not tested* note;
- the task registry gains a machine-checkable `historicalControls` ledger and a `controlsPolicy`.

Every affected location was corrected: the registry source ledger, the Teacher lesson overview, the
Teacher evidence ledger, both learner editions' Task 1, and Answer Key Tasks 1 and 5. **No invented
replacement control was introduced** — unsupported rows were removed, not substituted.

## Task 1 correction

The v1.0 Answer Key marked nutrient supply *"Y — verified against the cultivation standard"* and
grow-light spectrum *"Y — calibrated to the homeworld standard"*. Neither is supported by the packet
or by the game.

Task 1 now marks soil and seed stock **Y** and the other three rows **N**, each with the printed
evidence supporting it. Its marking note names reading a present value as a completed test as the
error the task exists to catch, and refuses "N means it cannot be the cause" as an answer. Every
required response is answerable from the page, and Teacher, Answer Key, Student and Accessible use
the same categories. The task id `C2-C01-T1` and the task order are unchanged.

## Answer Key evidence boundary

An Answer Key must be producible from the evidence a learner actually holds. Six expectations failed
that test, and each item was classified before any remedy was written:

| Evidence | Classification | Outcome |
|---|---|---|
| Radii, magnitudes, `0.00187 g`, rotation rate | Teacher-only enrichment | withdrawn from every graded expectation |
| `0.3%`, `80 m`, `300 m`, `GC-1445` | unnecessary or unsupported | withdrawn |
| `±0.05 g` and the endpoints at Task 6 | essential, but printed at Task 8 | removed from the Task 6 and Task 7 exemplars; kept at Task 8 |
| Botanist's present-condition report | **essential and missing** | now printed in both learner editions at Task 1 |
| `600 m`, `GC-1208`, `20 cm`, onset days | already supplied | retained |

Task 5 is regraded against the summaries in learner Table 4, with gameplay detail accepted as a
bonus rather than required. Task 6 rejects over-calibration from the three-place result printed on
Student page 2 and Accessible page 3. The Task 7 CER exemplar is rebuilt so every clause is
producible from the Student edition alone and, independently, from the Accessible edition alone; it
also drops `a = ω²r`, which the guide's own assessment boundary says learners never meet, and
reasons from the merry-go-round relationship instead.

**The quantitative profile is unchanged and remains Teacher-facing.** The completion audit
re-derived the whole profile from `a = ω²r` and confirmed every figure correct at its authored
precision. Learners meet the relationship through the labelled analogy and the qualitative
three-place result, which is the design v1.0 chose deliberately and this release preserves.

## Teacher Guide correction

- **Stale Task 3 instructions removed.** Commit `bf0ad45` removed all arithmetic from Task 3, but
  the guide still described it in three places: *"Task 3 needs one subtraction of four-decimal
  values"*, a preparation note keyed to the rounding idea, and a ledger row reading *"What Task 3
  produces. Accept it, and require the explanation."* All three now describe the Task 3 that exists.
  **No arithmetic was restored in order to make the stale text true.** The precision explanation is
  retained where it is instructionally supported — as a Teacher-facing optional extension, which now
  states that no student can be asked to produce the subtraction because neither endpoint is printed
  in any learner edition.
- **Rubric, objectives and success criteria made scorable.** The formal *Precision* dimension, one
  measurable objective and one success criterion graded `2.0991 g`, `2.1009 g`, `0.00187 g` and
  `2.88966 RPM`. None reaches a learner. The dimension is reframed as *Reported values only*, scored
  on the values the packet prints — `2.10 g`, `±0.05 g`, `20 cm`, `600 m`, the onset days — and on
  inventing no quantity the case does not report, which is visible in Tasks 6, 7 and 8. Every rubric
  dimension and success criterion now maps to a visible student product.
- **Completeness.** Annotated answers covered Tasks 1, 3, 4 and 8 only. Tasks 2, 5, 6 and 7 now
  carry purpose, the evidence students should use, expected reasoning, acceptable alternatives,
  misconceptions and a scoring indicator, without duplicating the Answer Key.

## GC-1445 and attribution

`GC-1445` had its qualifier dropped and was reused as radius evidence. The Concord table now reads
*"No misalignment reported — with the qualifier the record attaches: low gravitropic precision"*, a
Teacher note records that the same database concludes **gradient sensitivity is species-dependent**
and that the record therefore establishes nothing about a safe radius and nothing about gorlroot,
and a claims-to-correct entry blocks the misuse. The Answer Key no longer cites it. Both Concord
records stay Teacher-facing; Table 7 gives learners the one figure they need.

Two claims were attributed to the wrong source and are corrected rather than withdrawn, because the
game does support them:

- *"The archive says the bed-scale difference is negligible."* It is the **botanist** who says it,
  twice, and it is a person's assessment rather than an archived measurement.
- *"Nominal; no vibration and no wobble reported."* The sensor array reports only *Ring Status:
  NOMINAL*. It is the **botanist** who separately reports steady RPM with no vibration and no
  wobble. A nominal status is not a report about every mechanical condition that went unmentioned.

The Teacher evidence ledger now names the reporting source for every row.

## Standards outcome

- **MS-LS1-5 — direct, retained**, assessed at Tasks 1 and 7. Table 1's Crop 3 seed-stock change and
  Table 2's unchanged ring radius and rotation rate are both on the learner page, and Task 7
  requires an evidence-based explanation of the growth outcome that uses both. The genetic factor is
  varied in the printed record and the environmental one is not, so the environmental attribution is
  **assessed rather than assumed**.
- **MS-ETS1-1 — direct, retained**, assessed at Task 8, where students write the across-bed
  criterion the specification omitted and name a constraint reported in the case.
- **MS-ETS1-2 — supporting and conditional, retained**, with its limitation intact and strengthened:
  claim it only if the class systematically compares the larger ring against the thinner bed against
  the same criterion and constraint.
- **MS-ETS1-3 — withdrawn.** It was justified by Concord records `GC-1208` and `GC-1445`, which are
  Teacher-facing and appear in no learner edition, and no task asks students to analyse data from
  several design solutions or to combine the best characteristics into a new one. **No task was
  redesigned in order to preserve it, and no standard replaces it.**

No mathematics standard is claimed, and the previously withdrawn mathematics claim does not return
for incidental arithmetic. A machine-checkable `standards` and `withdrawnStandards` ledger is added
to the task registry, recording the exact learner evidence behind every retained claim.

## Accessible corrections

The edition regains *"neither toward the axis nor away from it"*, the clause that rules out a listed
prohibited claim and that the Answer Key CER exemplar quotes back. Its CER page — the hardest task
in the packet — gains sentence starters and a pointer to the pages holding the evidence. It carries
the botanist's present-condition report and the reported-versus-tested rule in its own register.

Every Answer Key expectation is independently producible from the Accessible edition. Differentiation
is preserved rather than flattened: measured similarity is **67.4%**, against 67.7% at v1.0, and the
edition keeps its shorter directions, smaller evidence chunks, just-in-time vocabulary, word bank,
structured prompts and dedicated CER page.

## v1.0 preservation

`history/release-v1.0.json` and `history/CASE01_OWNER_APPROVAL_v1.0.md` are retained
**byte-identical** and were not edited to describe v1.1. v1.0 is represented in `release-v1.1.json`
as the prior approved release, carrying its own approval date, commit, source hashes, DOM baselines
and page counts (Teacher 8).

Three known v1.0 record defects are deliberately **not** corrected, because v1.0's records are
immutable historical evidence:

- Its `canonicalSourceApprovalCommit` `864156f0` is historically inaccurate — that commit carries a
  pre-lifecycle task registry hashing `485076fa…` rather than the `7d92bac9…` the record certifies
  (audit finding M-10). The commit that actually contains all four certified v1.0 sources is
  `a4195913`, recorded in `priorApprovedReleases` as the recovery commit so recovery never depends
  on the inaccurate pin. The Case 01 validator asserts both facts, so neither can change unnoticed.
- Its accepted-validation figures (`69/69`, `static 432/432`) were stale at the commit they describe.
- Its `sourceHashes` omits `layoutOverrides`, as all six Campaign 2 v1.0 records do.

All three are repaired going forward: this v1.1 record pins all four source hashes, records the
totals its own suites actually produce, and names a `canonicalSourceApprovalCommit` whose four
source blobs the validator hashes and compares directly.

The frozen Student, Teacher and Answer Key DOM baselines were regenerated for v1.1. All three differ
from v1.0's, so approved-baseline enforcement cannot be satisfied by the superseded v1.0 markup.

## Generated artifacts

None. Case 01 was authored natively as a case package and reissued the same way. No master,
published role HTML, PDF, screenshot, or other generated release artifact was created or committed
at either version: `NO_GENERATED_ARTIFACTS_COMMITTED`. Git history remains authoritative for
recovery.

## Campaign-level work deferred

This approval covers Case 01 only. Campaign 2 is **not** complete: Cases 04 and 05 remain
unremediated against `sss/audit/SSS_C2_CAMPAIGN_COMPLETION_AUDIT_v1.0.md`, and the shared-validation
maintenance, the cleanup-audit retirement and the `CURRENT_PROJECT_STATE.md` correction the audit
records in §12 and §13 are all out of scope here and remain open.
