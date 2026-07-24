# SSS Case 01 v1.0 Release-Candidate Validation Report

**Validation date:** 2026-07-24  
**Master:** `SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`  
**SHA-256:** `56c8374bb4192e783346588ca7202e2f01a7808dcec121ef68464092dad65710`  
**Status:** PASS FOR RELEASE-CANDIDATE REVIEW — VALIDATION BUILD

## Executive result

The reconciled Case 01 master passed every automated and digital visual check. It is not release-approved because the owner physical print test remains open.

- Static/content checks: **16/16 passed**
- Live browser checks: **13/13 passed**
- JavaScript errors: **0**
- Visible overflow: **0 pages**
- PDF preflight warnings: **0**

## Role and overflow results

| Role | Expected pages | Actual pages | Overflow |
|---|---:|---:|---:|
| Student | 3 | 3 | 0 |
| Teacher | 7 | 7 | 0 |
| Answer Key | 3 | 3 | 0 |
| Accessible | 6 | 6 | 0 |
| All Pages | 19 | 19 | 0 |

## Content regression

Passed checks include:

- exact Tasks 1–9 in Student and Accessible roles;
- exact Tasks 3–9 in the Answer Key;
- synchronized controlled Markdown sources;
- exact Task 5 word bank;
- completed Answer Key exemplars;
- bold exact Teacher task references;
- corrected institutional name to the canonical Solar Agricultural Agency (acronym SAA retained);
- absence of `Students complete Students complete`;
- absence of dangling `. and reasoning`;
- absence of prohibited Teacher compatibility/source-baseline body content.

## Accessibility and interaction

Passed:

- unique DOM IDs;
- programmatic response names and stable fields;
- first-page-only Name/Date/Period placement;
- keyboard activation in Fill and Edit modes;
- persistence across reload;
- Student/Accessible-only response clearing;
- separate Teacher/Answer Key note clearing;
- reset to the content embedded in the open file.

## Serialization

Downloaded edited HTML passed portability and reset tests. The download embeds the SAA insignia as a data URI, preserves edited content, removes runtime overflow state, and resets to the content embedded in that downloaded copy.

## PDF generation

| Output | Pages | SHA-256 |
|---|---:|---|
| Student Mission | 3 | `de5ad2675d1a77b0914e9a899c1111c1ba20470b6afa0c12d86cb3b3604a297a` |
| Teacher Packet | 7 | `ec0836256eb51ef33fe6157983ab6e2e7b47328b8ad9c4722bf5d0fb7c9f516f` |
| Answer Key | 3 | `bcb38bba1a6fbd472a521601a13bb25344c2ae0f5809b9d3dd183c48ac49ab5f` |
| Accessible Mission | 6 | `5d847ae08d34267ce7ff7420cf2e2179618e775674a606a44a22a967d7c8dd6f` |
| Grayscale Review | 19 | `91088dec260d7135df0589721bcb4d3476ad58f01aa5fa3dbc2ba8bb8b8e702d` |

All five PDFs opened successfully, were text-based rather than scanned, contained no XFA, and produced no preflight warnings. All 38 pages were rendered with PDFium and visually reviewed.

## Remaining release gate

The owner must print all five review outputs at 100% scale and complete `published/SSS_C1_CASE01_v1.0_RC_PRINT_TEST_CHECKLIST.md`. Until that test passes, all artifacts retain **VALIDATION BUILD** status.
