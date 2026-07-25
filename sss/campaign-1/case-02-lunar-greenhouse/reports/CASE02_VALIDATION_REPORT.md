# Case 02 Validation Report

**Artifact:** SSS Campaign 1, Case 02 — Lunar Greenhouse  
**Version:** v1.0  
**Status:** VALIDATION BUILD  
**Validation date:** 2026-07-24

## Result

Automated validation: **PASS**  
Physical print test: **OPEN**  
Release/approval status: **NOT AUTHORIZED**

## Automated checks

| Suite | Result |
|---|---:|
| Static content, task parity, accessibility, science regressions, role isolation | 94 / 94 passed |
| Browser behavior, persistence, clearing, reset, portable serialization, overflow, outputs | 33 / 33 passed |
| Master JavaScript errors | 0 |
| Default overflow warnings | 0 |

## Independent outputs

| Output | Pages | Size | Role isolation | Status visible |
|---|---:|---|---|---|
| Student | 2 | Letter | Passed | VALIDATION BUILD |
| Teacher | 7 | Letter | Passed | VALIDATION BUILD |
| Answer Key | 3 | Letter | Passed | VALIDATION BUILD |
| Accessible | 5 | Letter | Passed | VALIDATION BUILD |
| Grayscale Student | 2 | Letter | Passed | VALIDATION BUILD |

## Behaviors exercised

- Student/Teacher/Answer/Accessible/All role switching
- Settings retained across role changes
- Fill mode and instructional edit mode
- Stable local response/content persistence
- Current-role-only clearing
- Full source reset
- Portable downloaded HTML serialization with current content embedded
- Independent role-stripped HTML outputs
- Grayscale token mode without whole-page filter
- Default-margin overflow diagnostics
- PDF generation, Letter-size preflight, expected page counts, text/status extraction

## Content regressions exercised

- Exact task numbers/titles across Student, Accessible, Teacher direct references, and Answer Key
- Answer Key contains only keyable Tasks 3–9 without renumbering
- Every keyable task and required subpart has a completed exemplar
- Exact six-entry word bank parity and completed wording
- Sequential word bank order is shuffled rather than solution-ordered
- Student and Accessible vocabulary lists are alphabetical
- Student-facing pages contain no grading-policy disclaimer
- Accessible tasks pack continuously as 1–2 / 3–4 / 5 / 6–7 / 8–9
- Process model is central; Case 01 evidence-matrix title is absent
- Correct failure at physical agitation/pollen release
- All four runtime clue IDs documented
- All four diagnosis options preserved
- Fictional NASA brief and unsupported universal numeric targets excluded
- Pollination, fertilization, and fruit set remain distinct
- Canonical institutional name is Solar Agricultural Agency
- Case 01 first-page and continuation-header anatomy is preserved across all roles
- Internal case code and visible version box are absent from the prominent title
- Continuation headers use page-specific titles and computed left alignment

## Visual review

All 19 PDF pages were rendered to PNG and reviewed in a contact sheet. Full-size inspection covered both Student pages, Teacher page 1, Answer Key page 1, and representative Accessible pages. No clipping, spill pages, missing text, role leakage, or color-only meaning was observed.

Rendering emitted non-blocking Type 3 glyph bounding-box warnings from the PDF renderer. Extracted text, page geometry, page counts, and visual output remained correct. The owner physical print test is the deciding gate for any printer-specific concern.

## Open physical print gate

Print each PDF at **100% / Actual Size**, not “Fit,” on ordinary Letter paper. Confirm:

- no edge clipping;
- footer remains readable;
- response boxes remain usable;
- grayscale process/status differences remain clear;
- no unexpected blank pages;
- front/back Student pairing is correct;
- ordinary photocopy retains hierarchy and hatch/outline meaning.

Record the result in `published/OWNER_PRINT_TEST_CHECKLIST.md`. Do not change the visible status until that test passes.

## Header-parity correction

Owner visual review identified banner drift from the approved Case 01 production foundation. The corrected build removes `SSS-C1-CASE02` and the boxed version panel from the prominent first-page title, restores the Case 01 rail/title/insignia/status hierarchy, and replaces split continuation banners with compact page-specific continuation headers across every role.
## v1.1 compact-header correction

The v1.1 master now uses a compact first-page banner with a 26 pt title, 9 pt location subtitle, reduced identification-to-banner and banner-to-content spacing, and a fixed three-line Solar / Agricultural / Agency lockup beside the insignia. Continuation headers use the same lockup on the right.

Validation after this correction: **53/53 static checks** and **19/19 browser checks**, with zero default overflow. No new PDFs were generated or committed for this master-only review correction.

