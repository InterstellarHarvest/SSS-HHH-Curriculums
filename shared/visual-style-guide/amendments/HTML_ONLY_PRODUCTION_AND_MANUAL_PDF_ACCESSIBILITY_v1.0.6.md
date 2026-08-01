# HTML-Only Production and Manual PDF Accessibility — v1.0.6

**Status:** OWNER-DIRECTED CANONICAL AMENDMENT  
**Effective:** all current SSS/HHH cases and all later production; canonical-source clarification effective 2026-08-01

## Canonical production artifacts

Canonical curriculum production is package-source based. The permanent required sources are:

- the registered `source/case-package.json`;
- worksheet-only `source/content.html`;
- `source/presentation.css`;
- `source/task-registry.js`;
- only referenced optional source assets;
- a compact approved-release history record.

The central Curriculum Editor generates a portable editable copy or one selected-role worksheet when requested. The instructional roles are Student, Teacher, Answer Key, and Accessible. Grayscale is a Boolean display, print, and export presentation state available to each role; it is not a fifth role or a separate document profile.

Generated editable copies, role HTML, PDFs, and routine rendered evidence are temporary and must not be committed. Prior approved artifacts remain recoverable from Git history. Routine production must not generate, regenerate, store, preflight, checksum, validate, or require PDF files.

## Required HTML accessibility validation

Production validation assembles from canonical sources in temporary storage and covers semantic structure, logical reading order, heading hierarchy, alternative text, table semantics, programmatic field labels, document title and language, keyboard use, non-color-dependent meaning, role isolation, portability, serialization, overflow, print behavior, exact role page counts, source hashes, and rendered browser review. Temporary output is discarded after validation.

## Browser print and manually created PDFs

The central editor and generated editable-copy toolbar retain **Print / Save PDF** because owners and end users may print through the browser dialog or create a convenience PDF.

Browser PDF export is not a canonical production step and is never assumed to create an accessible PDF. Any PDF intended for distribution, publication, or archival use requires a separate accessibility review of tagging, reading order, headings, alternative text, tables, form-field labels, selectable text, title/language metadata, and screen-reader usability.

Physical print testing is performed from the browser print dialog at **100% / Actual Size**.

## Release logic

No project PDF is created, so there is no project PDF release gate. A manually created PDF is outside the canonical artifact set and does not become an approved distribution artifact without its own accessibility verification.
