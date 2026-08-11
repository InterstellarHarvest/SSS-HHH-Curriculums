# Campaign 1 Case 04 v1.1 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-10**

Title: **Hayes Orbital Station**

Curriculum: **SSS · Campaign 1 · Case 04**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective of: **1.0** (superseded and retained unchanged)

## What this release corrects

Final system release closing the correctness-remediation and visual-modernization program for Hayes Orbital Station.

- C1C4-T02 The authoritative Teacher source list was absent and is now printed.
- C1C4-T03 The common quick plus 4/3/2/1 analytic rubric system was absent and is now printed.
- C1C4-UI01 The required diagnosis selection had no persisted digital control.
- C1C4-T04 Runtime clue identifiers were visible in Teacher content and were removed.
- C1C4-T05 The Teacher Guide stated an incorrect Accessible page count.
- C1C4-ACC01 Accessible Tasks 5 and 7 received targeted refinement.
- C1C4-SYS01 Visible runtime identifiers and cross-role page references are now rejected repo-wide by shared validation.
- C1C4-VIS01/VIS02/VIS03 Incident log, closed fault loop and engineering control loop modernized through the shared visual layer.

## Approved release

- Owner review of the complete corrective and visually modernized program: **OWNER_REVIEW_PASS**
- On-screen content and visual review, including grayscale: **PASS**
- Physical print at 100% / Actual Size: **PASS** — Google Chrome, owner-reported 2026-08-10, tested baseline `105467f997b1425b7f40e8150749c70e09ed4771`
- Student Mission: 4 pages
- Teacher Guide: 7 pages
- Answer Key: 4 pages
- Accessible Mission: 7 pages
- Fixed Letter geometry: 816 × 1056 CSS-pixel worksheet pages with 720 × 960 CSS-pixel page frames.
- Grayscale remains a presentation-only state and does not create another role, page-count category, or output filename.
- HTML-only canonical production: there is no canonical project PDF artifact and no PDF release gate. Manually produced PDFs remain noncanonical and require their own accessibility review before distribution.
- Canonical browser registration remains 2375; the recorded 2374 total is the accepted candidate-specific same-Mac differential only. No general browser, Mac, Chrome, platform, or environment exception exists.
- Frozen game-source baseline: `2bfdb0aadf6ce33b6664cd104b11a891cb55efaf`. The game repository was not modified by this release.
- `NO_GENERATED_ARTIFACTS_COMMITTED`: no master, published role HTML, PDF, screenshot, browser profile, or generated release file is committed at this or any retained version.

## Retained records

All earlier release and owner-approval records in `history/` are retained byte-identical. None was edited to
describe v1.1 content and no known historical defect was corrected in place; the v1.1 release record
represents the superseded release through `priorApprovedReleases` instead.

The owner approves Campaign 1 Case 04 v1.1 in its current condition, subject to the repository release
validation recorded in `release-v1.1.json`.
