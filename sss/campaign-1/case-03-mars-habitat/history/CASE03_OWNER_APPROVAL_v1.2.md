# Campaign 1 Case 03 v1.2 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-10**

Title: **Mars Habitat**

Curriculum: **SSS · Campaign 1 · Case 03**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective of: **1.1** (superseded and retained unchanged)

## What this release corrects

Final system release closing the correctness-remediation and visual-modernization program for Mars Habitat.

- C1C3-T02 The Teacher procedure skipped Tasks 4 and 5 and now routes every numbered task.
- C1C3-T03 The complete analytic rubric was missing and is now printed alongside the quick rubric.
- C1C3-UI01 The required diagnosis selection had no persistent fill-mode representation and now carries a persisted control.
- C1C3-AK01 The Task 4 key did not visibly mirror every Student response field.
- C1C3-AK02 Accepted-alternative guidance was too thin for several open responses.
- C1C3-ACC01 Targeted Accessible hand-holding was added.
- C1C3-DATA01 The 700 nm boundary ambiguity against the 400-700 nm task was corrected.
- C1C3-T04 Production and release-management material was removed from the Teacher Guide.
- C1C3-META01 Stale editor resize labels were corrected; C1C3-META02 package identity drift was reconciled.
- C1C3-VIS01/VIS02/VIS03 Transmission scan, dual-channel diagnostic and spectral-loss chain modernized through the shared visual layer.

## Approved release

- Owner review of the complete corrective and visually modernized program: **OWNER_REVIEW_PASS**
- On-screen content and visual review, including grayscale: **PASS**
- Physical print at 100% / Actual Size: **PASS** — Google Chrome, owner-reported 2026-08-10, tested baseline `105467f997b1425b7f40e8150749c70e09ed4771`
- Student Mission: 4 pages
- Teacher Guide: 8 pages
- Answer Key: 4 pages
- Accessible Mission: 7 pages
- Fixed Letter geometry: 816 × 1056 CSS-pixel worksheet pages with 720 × 960 CSS-pixel page frames.
- Grayscale remains a presentation-only state and does not create another role, page-count category, or output filename.
- HTML-only canonical production: there is no canonical project PDF artifact and no PDF release gate. Manually produced PDFs remain noncanonical and require their own accessibility review before distribution.
- Canonical browser registration remains 2375; the recorded 2374 total is the accepted candidate-specific same-Mac differential only. No general browser, Mac, Chrome, platform, or environment exception exists.
- Frozen game-source baseline: `c6c17be57880b365793fdf99ff4ad09b62ecacce`. The game repository was not modified by this release.
- `NO_GENERATED_ARTIFACTS_COMMITTED`: no master, published role HTML, PDF, screenshot, browser profile, or generated release file is committed at this or any retained version.

## Retained records

All earlier release and owner-approval records in `history/` are retained byte-identical. None was edited to
describe v1.2 content and no known historical defect was corrected in place; the v1.2 release record
represents the superseded release through `priorApprovedReleases` instead.

The owner approves Campaign 1 Case 03 v1.2 in its current condition, subject to the repository release
validation recorded in `release-v1.2.json`.
