# Campaign 2 Case 05 v1.1 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-06**

Title: **Too Clean a Room**

Curriculum: **SSS · Campaign 2 · Case 05**

Runtime ID: **too_clean_room**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective of: **1.0** (approved 2026-08-05, superseded and retained unchanged)

## What this corrective release fixes

This is a narrow corrective release. Four printable defects are repaired and nothing else about
the case is revised.

- **Teacher page 9 printable-text corruption.** The guide printed a bare `X` where a clause
  belongs: "Tasks 1–3 sit naturally in the first, Tasks 4–7 in the second. **X** so the
  explanation is written in one sitting rather than assembled in margins." It is present in the
  original draft commit and in every commit since, so no earlier clean revision exists. The
  clause is restored from the package's own README and the v1.0 approval, both of which already
  stated the same page fact, and now reads "Task 6 occupies a full page of its own in both
  learner editions, so the explanation is written in one sitting rather than assembled in
  margins." It states existing page structure and introduces no teaching procedure.
- **Accessible briefing stakes restored.** "several Concord species" and "supplies are running
  out" occurred zero times in the Accessible edition. That sentence is the packet's only printed
  impacts-on-people evidence, which the direct MS-ETS1-1 alignment rests on, and one of the
  constraints the Answer Key accepts at Task 7.
- **Accessible Task 5 rejection evidence restored.** The word bank offered "uptake is normal"
  while the word "uptake" appeared nowhere else in that edition. The specimen record now reads
  "The cells are healthy and nutrient uptake is normal," matching the Student edition and the
  Answer Key.
- **Answer Key Task 7 constraints corrected.** The key accepted "staff exposure limits apply"
  and "only a small number of specimens exist," neither printed in either learner edition. Both
  are replaced by Table 7 requirements both editions print.

Only the Teacher defect was found by the Campaign 2 completion audit. The other three were
found by independent verification during remediation.

## Approved release

- On-screen content and visual review: **PASS**
- Generated PDF review: **PASS**
- Physical print at 100% / Actual Size: **PASS**
- Student Mission: 7 pages
- Teacher Guide: 9 pages
- Answer Key: 5 pages
- Accessible Mission: 7 pages
- Page counts are unchanged from v1.0 and were re-measured after the corrections in the browser
  matrix and in generated PDFs, in colour and in grayscale. The corrections added two short
  clauses and one sentence inside existing blocks and moved no page boundary.
- Grayscale remains a presentation-only state and does not create another role, page-count
  category, or output filename.
- Fixed Letter geometry: 816 × 1056 CSS-pixel worksheet pages with 720 × 960 CSS-pixel page
  frames; PASS for all four roles.
- Seven tasks in the approved order with exact identifiers across Student, Answer Key, and
  Accessible.
- Task 6 holds the Claim–Evidence–Reasoning explanation on a full page of its own in both
  learner editions — the fact the repaired Teacher sentence now states.
- Task 2 teaches by labelled everyday analogy — a rain gauge marked only in whole millimetres
  reading 0 mm on two different nights — and only then applies the detection-limit idea to the
  vault. The analogy states in the student text that its values are not vault measurements.
- Teaching figures are lettered and the vault's records are numbered tables, so a student can
  tell illustration from evidence at a glance. Tables 1–7 and Figures A and B are numbered
  identically in both learner editions, so every Teacher and Answer Key reference resolves in
  the edition the reader actually holds.
- Every value, proper noun and accepted constraint the Answer Key grades on or accepts is
  printed in both learner editions, on or before the page of the task that requires it.
- Source boundary carried by provenance wording rather than repeated disclaimers; established
  Earth radiation science stays distinct from records made for this vault, and modeled evidence
  stays distinct from both.
- Prohibited-claim guards retained and demonstrated: radiation described as a nutrient, a
  general claim that plants or people benefit from ionizing radiation, DNA damage described as
  beneficial, radiation-powered photosynthesis asserted, the vault reading treated as absolute
  zero or as exactly 0.01 mGy/day, absorbed dose restated in sievert, the homeworld site record
  presented as an optimum, a dose-response curve claimed from two dose conditions, the modeled
  Rhessi figure presented as measured, intention attributed to the bloom, shielding itself
  called a mistake, the internal hormesis framing, and any isotope, source, device or operating
  setting.
- The Accessible edition remains rewritten rather than reflowed: **55.4%** similar to the
  Student edition at 1788 words against 2108, one task per page, nine scaffold blocks, word
  banks, and a full-page CER. Both v1.1 corrections restore evidence its own prompts and word
  bank already required; nothing in its design was changed.
- Accessible page density, response-area sizing, resize eligibility, and explicit
  eligible-or-locked enforcement: PASS.
- Campaign-scoped editor navigation: Campaign 1 lists exactly its seven cases and Campaign 2
  lists Cases 01–06 in numerical order; PASS.
- Download Editable Copy, Download Worksheet, isolated printing, and runtime-error checks: PASS.
- Standards unchanged and independently re-verified against learner-visible task evidence:
  MS-ETS1-1 as the single direct assessment with Task 7 as its task evidence; MS-LS1-5 as
  supporting and bounded, because the records show growth was unaffected and the mechanism is a
  regulated pathway outside that standard's assessment boundary; MS-ETS1-2 as supporting and
  conditional, anchored to the two actual solutions Task 7 names. Nothing was added, removed or
  re-rated. The task registry now records the assessed practice, assessing task, learner
  evidence and limitation behind each claim.
- Frozen game-source baseline: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`. The game repository
  was not modified by this corrective release.
- `NO_GENERATED_ARTIFACTS_COMMITTED`: no master, published role HTML, PDF, screenshot, browser
  profile, or generated release file is committed at v1.0 or v1.1.

## Retained v1.0 records

`history/release-v1.0.json` and `history/CASE05_OWNER_APPROVAL_v1.0.md` are retained
byte-identical. Neither is edited to describe v1.1 content, and neither has its known defects
corrected in place. Those defects are recorded in the v1.1 release record instead: a
`canonicalSourceApprovalCommit` that does not contain the task registry it certifies, a
`sourceHashes` block that omits `layoutOverrides`, and a campaign-wide comparative claim
about this Accessible edition. That comparative was true when written and is not repeated here; the measured figure is recorded instead.

The owner approves Campaign 2 Case 05 v1.1 in its current condition. This approval records the
classroom-material and physical-print gates for the corrected packet and authorizes integration
into curriculum main.
