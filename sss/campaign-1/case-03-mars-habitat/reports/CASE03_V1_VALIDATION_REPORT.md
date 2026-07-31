# Case 03 v1.0 HTML Validation Report

**Case:** SSS Campaign 1, Case 03 - Mars Habitat

**Release status:** APPROVED STABLE

**Approval date:** 2026-07-31

**Artifact policy:** HTML_ONLY

**Game baseline:** `c6c17be57880b365793fdf99ff4ad09b62ecacce`

**Automated HTML result:** PASS - 142/142 consolidated assertions

**Shared shell and registry contract:** PASS - 377/377 assertions

**Editor-shell browser result:** PASS - 97/97 assertions

**Owner browser physical-print gate:** PASS - Nate / Owner, 2026-07-31

## Canonical artifact set

Case 03 is assembled from shared editor shell v1.0 plus Case 03 content/configuration. The portable editable master declares `<meta name="sss-editor-shell" content="1.0">` and remains self-contained. Its toolbar markup, CSS, JavaScript, controls, labels, order, grouping, sizing, spacing, and behavior match the approved Case 02 editable master. The five independent role outputs are Student, Teacher, Answer Key, Accessible, and Grayscale HTML.

No PDF is generated, stored, preflighted, checksummed, validated, or required. The browser **Print / Save PDF** action is preserved exactly as implemented in Case 02 for optional manual use. Shared documentation—not a Case 03 toolbar redesign—states that browser PDF accessibility is not guaranteed.

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

## Component and page-identity correction

The follow-up component handoff is implemented in full: canonical CER variants; exact PPFD first-use wording and units; independent Task 3 label/track/value columns; compact runtime-data captions; deterministic five-stage Task 6 models; removed Student/Accessible science-boundary and production-commentary boxes; optional end-of-worksheet extensions; one semantic task label and one task number per heading; and mandatory Phosphor icons. The approved Case 01/02 Name/Date/Period row, color insignia, Agency lockup, title block, continuation header, and institutional accent rail now govern every role.

Balanced Page Fill v1.0.2 now governs the Case 03 Student and Accessible worksheet rhythm. Response areas and inter-task spacing expand into available writable space while preserving page counts and zero overflow. Automated browser validation enforces a 40–180 CSS-pixel reserve beneath each final content element; the measured Student range is 44.3–120.2 pixels and the Accessible range is 71.6–168.2 pixels.

Student page 1 now preserves a measured 17.3px break between the Task 1 response and Task 2 heading. Optional extensions use the universal Case 01 neutral component: solid 4px slate rail, neutral field, dark technical label/wrench icon, and no dashed green treatment.

## Accessibility coverage

Validation covers document language/title, one page-title heading per page, logical heading hierarchy, alternative text and SVG names/descriptions, table captions and scoped headers, named editable fields, keyboard focus, role isolation, self-contained resources, direct chart labels/patterns, and non-color-dependent meaning.

If an owner or end user manually creates a PDF, private convenience use inherits the limitations of the export method. A PDF intended for distribution, publication, or archival must separately verify tags, reading order, headings, alt text, tables, field labels, selectable text, title/language metadata, and screen-reader usability.

## Institutional identity correction

The canonical expansion is **Solar Agricultural Agency**. This remains a follow-up correction after initial Case 03 commit `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`; it does not rewrite that initial publication history.

## Release gate

Automated HTML and browser results are recorded in `validation-artifacts/`. All automated gates, rendered browser review, and the owner physical-print checklist passed. Case 03 is APPROVED STABLE under the HTML-only production policy as of 2026-07-31. Browser/printer and paper details were not recorded.
