# Case 03 Rendered Review

**Build:** v1.0 VALIDATION BUILD  
**Review basis:** final PDFs rendered at 140 DPI with Poppler and PDFium; contact-sheet inspection of every page  
**Result:** PASS

## Findings

| Role | Pages | Review finding |
|---|---:|---|
| Student | 4 | The transmission graph uses direct 92%, 88%, 31%, and 12% labels, four distinct fills, a percent axis, wavelength bands, caption, and source status. Task 5 and Task 6 writing areas were enlarged after review; all other response areas remain proportionate. No clipping or crowded task transitions were observed. |
| Teacher | 8 | Quick start, lesson plan, case analysis, mechanism, rubrics, references, fallback, and print gate remain legible. Current-main filter evidence (68%, 47 sols, FS-7, BP-4) is present. Pages retain intentional bottom reserve rather than enlarged identity or type. |
| Answer Key | 4 | All nine exact task titles have completed exemplars. Graph, mechanism, diagnosis, CER, transfer, and exit responses are legible without answer text collision. |
| Accessible | 6 | Larger type and response areas fit without clipping. Tasks remain in canonical order and continuous flow. Task 2 now uses direct transmission rather than stale loss arithmetic. |
| Grayscale | 4 | The Student layout remains interpretable without color. Bar patterns, direct values, axes, table rules, response boundaries, and institutional structure survive grayscale rendering. |

## Two-renderer comparison
All pages rendered completely in Poppler and PDFium. Pixel differences ranged from ordinary font/line antialiasing to a maximum changed-pixel proportion of 0.0733; diff images followed text and vector edges rather than revealing missing, shifted, or clipped content. No renderer-specific glyph failure, black rectangle, or chart corruption was found.

## Page-fill judgment
The Student Task 5/6 page was the only page where meaningful unused space coexisted with undersized multi-line work areas; those two areas were increased. Other bottom reserves were retained because the nearby fields were short-answer, completed-exemplar, or teacher-reference content and did not warrant artificial expansion.
