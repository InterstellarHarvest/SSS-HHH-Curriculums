# Case 03 v1.0 Validation Report

**Case:** SSS Campaign 1, Case 03 - Mars Habitat  
**Status:** VALIDATION BUILD  
**Curriculum baseline:** `e524d333f28a1515571f038e3ed494d87aa812d3`  
**Game baseline:** `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`  
**Automated result:** PASS - 355/355 assertions  
**Physical 100%-scale print gate:** OPEN

## Institutional identity correction
The canonical SAA expansion is **Solar Agricultural Agency**. This is a follow-up terminology correction after Case 03 was first committed to `main` at `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`; it does not replace or rewrite that initial commit. The corrected master, all standalone HTML outputs, all PDFs, alt text, lockups, print checklist, PDF generator, and validator now match approved Case 01/02 usage. The validator requires Agency and rejects Authority and Space variants on printable pages. The current game repository still requires a separate lore-only naming patch; the science/runtime audit remains anchored to the recorded game baseline.

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
The execution sandbox blocks direct browser navigation to `file://`, localhost, and synthetic network origins. Chromium behavior was therefore exercised with the complete HTML injected into a browser document and an in-memory Storage-compatible object. This still executed the production JavaScript and validated persistence/load behavior, controls, role switching, clearing, reset, portable generation, keyboard focus, overflow detection, and each standalone role output.

## PDF preflight
All five PDFs opened successfully, were unencrypted, contained searchable text, were not classified as scanned/image-only, contained no XFA, and produced no preflight warnings.

## Rendered review
PASS. See `CASE03_RENDERED_REVIEW.md`. Poppler/PDFium differences were antialiasing-only; no missing or clipped content was found.

## Release gate
Automated validation is complete. The case remains VALIDATION BUILD until the owner prints every role at 100% / Actual Size and completes `published/OWNER_PRINT_TEST_CHECKLIST.md`.
