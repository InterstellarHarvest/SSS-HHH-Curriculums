# Case 03 v1.0 Validation Report

**Case:** SSS Campaign 1, Case 03 - Mars Habitat  
**Status:** VALIDATION BUILD  
**Curriculum baseline:** `e524d333f28a1515571f038e3ed494d87aa812d3`  
**Game baseline:** `c6c17be57880b365793fdf99ff4ad09b62ecacce`  
**Automated result:** PASS - 355/355 assertions  
**Physical 100%-scale print gate:** OPEN

## Shared editor-shell and task-heading maintenance

Case 03 now targets shared editor shell v1.0. The editable master is assembled from the exact shared toolbar, CSS, JavaScript runtime, icon sprite, task-heading contract, and CER component plus Case 03 content/configuration. The completed master remains a self-contained portable HTML file and declares `<meta name="sss-editor-shell" content="1.0">`.

- Shared-shell static contract: 338/338 PASS
- Browser/editor behavior: 34/34 PASS
- Fresh-storage serialization: PASS for instructional edits and responses
- Reset Source in downloaded edited master: PASS; restores embedded edited source
- Independent role serialization: PASS; authoring toolbar removed
- HTML page counts: Student 4, Teacher 8, Answer 4, Accessible 6, Grayscale 4
- HTML overflow: 0 across all roles
- Task heading parity: PASS; exact semantic label, icon, number-once title, and configured title

This was an HTML-only maintenance build. No PDF was generated or modified. The five existing PDFs, their prior 5/5 preflight results, and their 4/8/4/6/4 page counts remain the checksum-controlled artifacts from the preceding validation build. The physical-print gate remains OPEN.

## Institutional identity correction
The canonical SAA expansion is **Solar Agricultural Agency**. This is a follow-up terminology correction after Case 03 was first committed to `main` at `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`; it does not replace or rewrite that initial commit. The corrected master, all standalone HTML outputs, all PDFs, alt text, lockups, print checklist, PDF generator, and validator now match approved Case 01/02 usage. The validator requires Agency and rejects Authority and Space variants on printable pages. The game repository canonicalized the same name at `c6c17be57880b365793fdf99ff4ad09b62ecacce`, which is now the current Case 03 compatibility baseline. The former commit `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712` remains recorded only as the historical commit used for the original runtime science audit.

## Page counts
- Student Mission: 4
- Teacher Guide: 8
- Answer Key: 4
- Accessible Mission: 6
- Grayscale Student Mission: 4

## Validation coverage
- Static structure, current-master metadata, printable identity, role-specific footers, and production-metadata separation.
- Exact Student/Accessible/Answer task-title parity for Tasks 1-9 and exact Teacher direct references.
- Current-main data values: 280 PPFD, 12 m silica pipe, 68% aggregate transmission, 47-sol filter replacement, 92/88/31/12 transmission, FS-7, and BP-4.
- Graph axes, units, wavelength bands, direct values, patterns, captions, source status, SVG title/description support, and no invented continuous spectrum.
- Correct diagnosis, filter-to-symptom mechanism, low-total-light rejection, dust-only rejection, and absence of brightness/red-only/green-is-useless misconceptions.
- Role isolation, editable fields, persistence, selective clearing, reset, grayscale mode, portable role download, keyboard focus, standalone HTML behavior, and zero overflow.
- PDF openability, Letter geometry, page counts, role footers, text extraction, ASCII-safe storage, current data, stale-value absence, and rendered page counts.
- Checksum generation, preflight, rendered review, and renderer parity.

## Browser execution note
The editor-shell validator opened the master and a newly serialized edited copy through `file://` in separate clean browser contexts. This exercised the production localStorage path, embedded-source reset, role isolation, typography, and overflow checks without a synthetic storage substitute.

## PDF preflight
All five PDFs opened successfully, were unencrypted, contained searchable text, were not classified as scanned/image-only, contained no XFA, and produced no preflight warnings.

## Rendered review
PASS. See `CASE03_RENDERED_REVIEW.md`. Poppler/PDFium differences were antialiasing-only; no missing or clipped content was found.

## Release gate
Automated validation is complete. The case remains VALIDATION BUILD until the owner prints every role at 100% / Actual Size and completes `published/OWNER_PRINT_TEST_CHECKLIST.md`.
