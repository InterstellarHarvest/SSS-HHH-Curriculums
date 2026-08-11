# Campaign 1 Case 01 v1.2 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-10**

Title: **ISS Greenhouse**

Curriculum: **SSS · Campaign 1 · Case 01**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective of: **1.1** (superseded and retained unchanged)

## What this release corrects

Final system release closing the SSS correctness-remediation and visual-modernization program for ISS Greenhouse.

- C1C1-T01 Teacher procedure skipped Student Task 5. The timed procedure now routes every numbered task.
- C1C1-AK01 Answer Key Task 3 omitted the required observation/inference fields. The key now completes every keyable subpart.
- C1C1-ACC01 Several Accessible tasks were insufficiently hand-holding. Chunked directions, evidence cues and partial completion were added without changing the accepted response space.
- C1C1-SYS01 Teacher task coverage and Answer Key subfield coverage are now enforced repo-wide by shared validation rather than per case.
- C1C1-GS01 Rendered grayscale retained tinted callout surfaces. The case-scoped shared visual layer now neutralises them to rgb(242, 242, 242) and rgb(230, 230, 230); no case source changed.

## Approved release

- Owner review of the complete corrective and visually modernized program: **OWNER_REVIEW_PASS**
- On-screen content and visual review, including grayscale: **PASS**
- Physical print at 100% / Actual Size: **PASS** — Google Chrome, owner-reported 2026-08-10, tested baseline `105467f997b1425b7f40e8150749c70e09ed4771`
- Student Mission: 3 pages
- Teacher Guide: 8 pages
- Answer Key: 3 pages
- Accessible Mission: 6 pages
- Fixed Letter geometry: 816 × 1056 CSS-pixel worksheet pages with 720 × 960 CSS-pixel page frames.
- Grayscale remains a presentation-only state and does not create another role, page-count category, or output filename.
- HTML-only canonical production: there is no canonical project PDF artifact and no PDF release gate. Manually produced PDFs remain noncanonical and require their own accessibility review before distribution.
- Canonical browser registration remains 2375; the recorded 2374 total is the accepted candidate-specific same-Mac differential only. No general browser, Mac, Chrome, platform, or environment exception exists.
- `NO_GENERATED_ARTIFACTS_COMMITTED`: no master, published role HTML, PDF, screenshot, browser profile, or generated release file is committed at this or any retained version.

## Retained records

All earlier release and owner-approval records in `history/` are retained byte-identical. None was edited to
describe v1.2 content and no known historical defect was corrected in place; the v1.2 release record
represents the superseded release through `priorApprovedReleases` instead.

The owner approves Campaign 1 Case 01 v1.2 in its current condition, subject to the repository release
validation recorded in `release-v1.2.json`.
