# Campaign 2 Case 01 v1.2 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-10**

Title: **Heavy Hands**

Curriculum: **SSS · Campaign 2 · Case 01**

Runtime ID: **heavy_hands**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective of: **1.1** (superseded and retained unchanged)

## What this release corrects

Final system release closing the correctness-remediation and visual-modernization program for Heavy Hands.

- C2C1-T02 and C2C1-SYS01 Teacher fallback scope integrity. The fallback permitted reducing the registry-defined graded five-source Task 5 to three sources. It now directs the teacher to complete as many source rows as the period allows and assign the remainder for completion, so the graded contract is never silently narrowed.
- C2C1-T04 Declared class-period route. The undeclared 105-minute core route is now an explicit Recommended two-period route carrying a Scope integrity rule that forbids deleting a registry-defined graded source, diagnosis, CER or design requirement to fit one period.
- C2C1-T03 Rubric system. The three-level Secure/Developing/Not yet matrix was replaced by the common quick rubric plus the full 4/3/2/1 analytic rubric across claim, evidence, mechanism, precision and transfer.
- C2C1-ACC01 Accessible workload. Accessible Tasks 5 and 6 were too close to the full Student workload and gained direct evidence cues, a prefilled best-supported marker, and the restated midpoint-only and present-readings qualifications.
- Teacher page redistribution. Four over-full Teacher pages were given the space their content needs; standards alignment, source boundary, the numerical ledger, misconceptions, the analytic rubric and the annotated answers each moved to the page that fits them. Nine Teacher pages are retained under the owner-accepted C2C1-T01 exception of 2026-08-07.
- C2C1-VIS01, VIS02 and VIS03 Radial-bed cutaway, centrifuge telemetry profile and requirement/verification flow modernized through the shared visual layer; no case source changed.

## Approved release

- Owner review of the complete corrective and visually modernized program: **OWNER_REVIEW_PASS**
- On-screen content and visual review, including grayscale: **PASS**
- Physical print at 100% / Actual Size: **PASS** — Google Chrome, owner-reported 2026-08-10, tested baseline `105467f997b1425b7f40e8150749c70e09ed4771`
- Student Mission: 5 pages
- Teacher Guide: 9 pages
- Answer Key: 4 pages
- Accessible Mission: 8 pages
- Fixed Letter geometry: 816 × 1056 CSS-pixel worksheet pages with 720 × 960 CSS-pixel page frames.
- Grayscale remains a presentation-only state and does not create another role, page-count category, or output filename.
- HTML-only canonical production: there is no canonical project PDF artifact and no PDF release gate. Manually produced PDFs remain noncanonical and require their own accessibility review before distribution.
- Canonical browser registration remains 2375; the recorded 2374 total is the accepted candidate-specific same-Mac differential only. No general browser, Mac, Chrome, platform, or environment exception exists.
- Frozen game-source baseline: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`. The game repository was not modified by this release.
- `NO_GENERATED_ARTIFACTS_COMMITTED`: no master, published role HTML, PDF, screenshot, browser profile, or generated release file is committed at this or any retained version.

## Retained records

All earlier release and owner-approval records in `history/` are retained byte-identical. None was edited to
describe v1.2 content and no known historical defect was corrected in place; the v1.2 release record
represents the superseded release through `priorApprovedReleases` instead.

The owner approves Campaign 2 Case 01 v1.2 in its current condition, subject to the repository release
validation recorded in `release-v1.2.json`.
