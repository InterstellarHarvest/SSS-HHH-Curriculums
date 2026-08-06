# Campaign 2 Case 04 v1.1 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-06**

Title: **The Silent Grove**

Curriculum: **SSS · Campaign 2 · Case 04**

Runtime ID: **silent_grove**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective release of: **1.0** (approved 2026-08-05, superseded, records retained unchanged)

## Approved release

- On-screen content and visual review: **PASS**
- Generated PDF review: **PASS**
- Physical print at 100% / Actual Size: **PASS**
- Student Mission: 6 pages
- Teacher Guide: 8 pages
- Answer Key: 4 pages
- Accessible Mission: 8 pages
- Page counts are unchanged from v1.0. The restored Accessible evidence was packed into the existing eight pages rather than split onto a ninth, which the one-task-per-page Accessible contract requires. Three pages overflowed during correction — Student 2 by 21 px, Teacher 7 by 27 px, Accessible 2 by 83 px — and all three were packed; the browser matrix reports Pages fit for all four roles.
- Grayscale remains a presentation-only state and does not create another role, page-count category, or output filename.
- Fixed Letter geometry: 816 × 1056 CSS-pixel worksheet pages with 720 × 960 CSS-pixel page frames; PASS for all four roles.
- Eight tasks in the approved order with exact identifiers across Student, Answer Key, and Accessible; unchanged from v1.0.
- Frozen game-source baseline: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`; unchanged from v1.0.
- `NO_GENERATED_ARTIFACTS_COMMITTED`: no master, published role HTML, PDF, screenshot, browser profile, or generated release file was committed at either version.

## What the owner approved in this correction

- **Accessible Task 2 evidence, restored.** The edition carried no log evidence while retaining the prompt that needs it, and the Answer Key graded four agreements no Accessible student could see. Task 2 now carries a condensed Table 4 organised by record rather than by day, above the prompts. The Accessible edition remains a differentiated edition, not a Student reflow.
- **Task 1 evidence order, corrected.** Both learner editions now print a compact change record on the page of Task 1, in their own register.
- **Unsupported historical-intensity claims, removed.** "Intensity has stayed at 100% … throughout" and "intensity did not change" are gone. The current reading keeps its *Current intensity* label, and the Teacher Guide states that the earlier value is unreported.
- **Task 4 and Task 6 Answer Key reasoning, rebuilt** on the examination record the packet already prints.
- **Runtime-only cultural significance, removed from graded Task 8 expectations**, and retained as Teacher discussion context marked ungradeable.
- **Chemical-filtering drift direction, restored** to what the runtime actually claims, in all four roles.
- **Standards, corrected.** See below.
- **Unchanged 6 / 8 / 4 / 8 page counts**, and the final visual, Accessible, and instructional state.

## Standards

**Case 04 v1.1 claims no NGSS performance expectation as directly assessed.** The owner explicitly accepts this: conservative alignment is preferable to retaining an unsupported direct claim.

- **MS-LS1-5 — withdrawn as direct**, retained as *supporting and bounded* at Task 7. The performance expectation concerns environmental and genetic factors affecting organism growth; this case holds growth constant deliberately, and the packet's own assessment boundary instructs teachers not to report growth evidence from it. A boundary note cannot turn a mismatched performance expectation into a direct standard. The packet carries the explanation practice, not the performance expectation.
- **MS-ETS1-1 — withdrawn as direct**, retained as *supporting* at Task 8. Its direct rating rested partly on Task 8 accounting for impacts on people, which the Student task never asks and whose supporting fact is runtime-only. Campaign 2 Case 03 rates its structurally identical final specification task as supporting. Task 8 was not enlarged in order to preserve the rating.
- **MS-ETS1-2 — supporting and conditional**, limitation intact.
- **No standard replaces either withdrawn direct claim.** No mathematics standard is claimed; the packet requires no calculation anywhere.
- What the packet assesses directly is its science and engineering practices and crosscutting concepts, listed in the Teacher Guide.

## Retained v1.0 history

- `history/release-v1.0.json` and `history/CASE04_OWNER_APPROVAL_v1.0.md` are retained **byte-identical**. Neither was edited to describe v1.1.
- v1.0's known historical defects are **left uncorrected in place** and repaired only going forward in v1.1: the stale `case04Scoped: 75/75` figure (the validator committed alongside it reports 82/82); the `layoutOverrides` hash missing from its `sourceHashes`; the Case 03 copy-paste in its `migrationNotes`; and its `canonicalSourceApprovalCommit` `cec58ccf`, which does not contain the task registry it certifies.
- The commit that actually contains all four certified v1.0 sources is `91c7a3f6615b8a33a37d34ba0146965cfa81bf8c`, recorded in the v1.1 record so recovery never depends on the inaccurate pin. The Case 04 validator asserts both facts, so neither can change unnoticed.

The owner approves Campaign 2 Case 04 v1.1 in its current condition. This approval records the classroom-material and physical-print gates and authorizes integration into curriculum main.
