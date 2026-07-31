# HTML-Only Production and Manual PDF Accessibility — v1.0.6

**Status:** OWNER-DIRECTED CANONICAL AMENDMENT  
**Effective:** SSS Campaign 1 Case 03 and all later SSS/HHH production

## Canonical production artifacts

New curriculum production is HTML-only. Required artifacts are:

- one portable, self-contained editable-master HTML file;
- independent Student HTML;
- independent Teacher HTML;
- independent Answer Key HTML;
- independent Accessible HTML;
- independent Grayscale HTML.

Routine production must not generate, regenerate, store, preflight, checksum, validate, or require PDF files. Existing approved Case 01 and Case 02 PDFs are historical release artifacts and remain untouched.

## Required HTML accessibility validation

Production validation covers semantic structure, logical reading order, heading hierarchy, alternative text, table semantics, programmatic field labels, document title and language, keyboard use, non-color-dependent meaning, role isolation, portability, serialization, overflow, print-preview behavior, HTML page counts, HTML checksums, and rendered browser review.

## Browser print and manually created PDFs

The editable-master toolbar retains **Print / Save PDF** because owners and end users may print through the browser dialog or create a convenience PDF.

Browser PDF export is not a canonical production step and is never assumed to create an accessible PDF. Any PDF intended for distribution, publication, or archival use requires a separate accessibility review of tagging, reading order, headings, alternative text, tables, form-field labels, selectable text, title/language metadata, and screen-reader usability.

Physical print testing is performed from the browser print dialog at **100% / Actual Size**.

## Release logic

No project PDF is created, so there is no project PDF release gate. A manually created PDF is outside the canonical artifact set and does not become an approved distribution artifact without its own accessibility verification.
