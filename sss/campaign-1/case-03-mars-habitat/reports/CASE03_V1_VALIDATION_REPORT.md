# Case 03 v1.0 HTML Validation Report

**Case:** SSS Campaign 1, Case 03 - Mars Habitat

**Status:** VALIDATION BUILD

**Artifact policy:** HTML_ONLY

**Game baseline:** `c6c17be57880b365793fdf99ff4ad09b62ecacce`

**Automated HTML result:** PASS - 115/115 consolidated assertions

**Shared shell contract:** PASS - 355/355 assertions

**Editor-shell browser result:** PASS - 45/45 assertions

**Owner browser physical-print gate:** OPEN

## Canonical artifact set

Case 03 is assembled from shared editor shell v1.0 plus Case 03 content/configuration. The portable editable master declares `<meta name="sss-editor-shell" content="1.0">` and remains self-contained. The five independent role outputs are Student, Teacher, Answer Key, Accessible, and Grayscale HTML.

No PDF is generated, stored, preflighted, checksummed, validated, or required. The browser **Print / Save PDF** action is preserved for optional manual use and explicitly warns that browser PDF accessibility is not guaranteed.

## Active release gates

- Static HTML validation
- Browser behavior validation
- Role isolation
- Portability and serialization
- Accessibility
- Overflow and print-preview checks
- HTML page counts
- HTML checksum verification
- Rendered browser review
- Owner physical print test through the browser dialog at 100% / Actual Size

## HTML page counts

- Student Mission: 4
- Teacher Guide: 8
- Answer Key: 4
- Accessible Mission: 6
- Grayscale Student Mission: 4

All six canonical HTML checksum-ledger entries verify. All 26 pages rendered in the browser with zero flagged overflow and passed contact-sheet inspection.

## Accessibility coverage

Validation covers document language/title, one page-title heading per page, logical heading hierarchy, alternative text and SVG names/descriptions, table captions and scoped headers, named editable fields, keyboard focus, role isolation, self-contained resources, direct chart labels/patterns, and non-color-dependent meaning.

If an owner or end user manually creates a PDF, private convenience use inherits the limitations of the export method. A PDF intended for distribution, publication, or archival must separately verify tags, reading order, headings, alt text, tables, field labels, selectable text, title/language metadata, and screen-reader usability.

## Institutional identity correction

The canonical expansion is **Solar Agricultural Agency**. This remains a follow-up correction after initial Case 03 commit `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`; it does not rewrite that initial publication history.

## Release gate

Automated HTML and browser results are recorded in `validation-artifacts/`. Case 03 remains VALIDATION BUILD until all automated gates, rendered browser review, and the owner physical-print checklist pass.
