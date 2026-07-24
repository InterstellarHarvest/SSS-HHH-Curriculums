# SSS Case 01 v1.0 Implementation Plan

**Purpose:** migrate the real Case 01 editable master to the approved v1.0 visual and publishing system while preserving instructional intent and creating the production foundation for later SSS and HHH cases.

This document records the pre-edit plan used for the migration and marks the completed disposition of each item.

## 1. Priority order

### Priority 0 — release-critical framework

| Work item | Planned action | Disposition |
|---|---|---|
| Canonical identity | Remove embedded header art and reference `shared/assets/insignia/saa.svg` | Completed |
| Role isolation | Create independent Student, Teacher, Answer Key, Accessible, and All Pages views | Completed |
| Print geometry | Retain fixed US Letter; enforce 0.50-inch approved default across roles | Completed |
| Overflow | Keep visible screen-only warnings; correct hidden-page false positives | Completed |
| Typography | Apply Inter + JetBrains Mono and approved point-equivalent scale | Completed |
| Header/footer | Replace `.hdr` with Mission Title Block, continuation header, and split metadata footer | Completed |
| Answer safety | Remove inline answer-reveal architecture from student pages | Completed |
| Persistence | Save controls, editable content, and response content in local storage | Completed |
| Accessible output | Build a parallel accessible packet with the same task identifiers and order | Completed |

### Priority 1 — page components and page fill

| Work item | Planned action | Disposition |
|---|---|---|
| Grid | Establish 12-column page grid and reusable spans | Completed |
| Section headings | Add recurring Phosphor Regular icons and Technical Label Headings | Completed |
| Callouts | Standardize left-rule pale-field semantic callouts | Completed |
| Responses | Use prompt-above-box blank response areas | Completed |
| CER | Use three stacked boxes with preserved minimum hierarchy and shared surplus | Completed |
| Tables | Standardize ruled technical tables and captions | Completed |
| Teacher notes | Expand notes into unused page space where appropriate | Completed |
| Answer notes | Add dedicated answer-key note space instead of leaving dead paper | Completed |
| Grayscale | Replace whole-workspace filter with grayscale tokens and image-only filtering | Completed |

### Priority 2 — validation and handoff

| Work item | Planned action | Disposition |
|---|---|---|
| Page counts | Validate every role and All Pages output | Completed |
| PDF render | Render and inspect Student, Teacher, Answer, Accessible, and Grayscale PDFs | Completed |
| State behavior | Confirm role changes preserve margin, density, grayscale, preview, edit, and fill states | Completed |
| Content restore | Confirm saved response content loads into a fresh document DOM | Completed |
| Accessibility basics | Check names, labels, captions, page regions, skip link, and duplicate IDs | Completed |
| Reusable foundation | Document shared CSS, components, JavaScript, and case-specific boundaries | Completed |

## 2. Planned page architecture

The baseline 11-page package was retained as instructional source material but repaginated where required by print usability.

| Output role | Baseline | Planned v1.0 | Reason |
|---|---:|---:|---|
| Student | 2 | 3 | Evidence, CER, and written reasoning could not remain usable in two pages at the approved scale |
| Teacher | 7 | 7 | Existing role structure was sound; short pages receive genuine notes space |
| Answer Key | 2 | 3 | Models and accepted variation required usable scan density and instructional notes |
| Accessible | 0 | 6 | Larger type, reduced density, simplified task grouping, and larger writing areas |
| All Pages | 11 | 19 | Audit view of all independent roles |

## 3. Reusable shared components

The following components were planned as framework code rather than Case 01-specific markup:

- `.page`, `.page-frame`, and `.content-area`
- `.mission-title-block`
- `.continuation-header`
- `.publication-footer`
- `.publication-mark` and `.footer-status`
- `.grid-12` and span utilities
- `.section-heading`, `.technical-label`, and embedded Phosphor symbol sprite
- `.callout` semantic variants
- `.response-block` and `.response-area`
- `.cer-stack` and `.cer-block`
- `.tech-table`
- `.teacher-note`
- `.answer-block`
- `.notes-area`
- role selectors based on `data-role`
- local-storage state and content persistence
- screen-only overflow warnings
- grayscale token overrides

## 4. Case 01-specific content boundary

The following were planned to remain content data, not shared framework logic:

- case title and subtitle;
- mission question;
- vocabulary terms and definitions;
- evidence-source labels and prompts;
- competing explanations;
- mechanism sentence frames;
- diagnosis, CER, engineering, and exit prompts;
- teacher timing and facilitation language;
- misconceptions and science-status boundaries;
- rubrics;
- answer-key models;
- sources and game compatibility metadata.

Later cases should replace these values without editing the shared component contracts.

## 5. Obsolete CSS to remove

The following v0.3 patterns were identified for deletion rather than compatibility layering:

- `.hdr` and its heavy accent border
- `.header-art` and embedded base64 image data
- `.badge` as a generic pill treatment
- `.answer-inline` and `body.show-answers`
- `.cer` side-label grid and fixed-height variants
- `.question-box` as a generic answer substitute
- `.two-col` and `.three-col` as the primary page-grid system
- `.audience-student`, `.audience-teacher`, and `.audience-answer` view coupling
- whole-workspace grayscale filtering
- hidden-page overflow evaluation
- prototype footer variants

## 6. Obsolete JavaScript to remove

- Runtime-only `editing` and `filling` booleans without persisted state
- Temporary role mutation during print
- `Show answers` toggle
- Teacher print mode that automatically includes answer pages
- Reset behavior that reconstructs only the v0.3 state model
- Download naming tied to v0.3
- Overflow checking that treats hidden pages as zero-height printable pages

## 7. Risk register and mitigation

| Risk | Consequence | Planned mitigation | Result |
|---|---|---|---|
| Approved type scale causes overflow | Illegible emergency type reduction | Repaginate student and answer sets | Mitigated |
| Flexible boxes grow unpredictably | Footer collision or clipped content | Fixed Letter frame + flex growth + screen warning | Mitigated |
| Role change resets controls | User loses publishing setup | Single persisted state object; role changes update one field only | Mitigated |
| Teacher answers leak to student output | Invalid student packet | Independent role classes and no inline answer reveal | Mitigated |
| Grayscale rasterizes PDF | Searchability and accessibility loss | Grayscale variables; filter only raster/vector artwork | Mitigated |
| Accessible copy drifts from standard copy | Instructional inequivalence | Preserve numbered task order and identifiers | Mitigated |
| External font request unavailable | Fallback typography in offline use | Standards-compliant fallback stack; document packaging risk | Partially mitigated |
| Browser PDF is untagged | Accessible PDF may not meet tagged-PDF requirements | Treat accessible HTML as primary; flag tagged-PDF pipeline separately | Open |
| Physical printer variance | Unexpected scaling or clipping | Require 100% physical print sample before release status | Open |

## 8. Destructive-change policy

The original v0.3 source file is not overwritten in this migration package. The new implementation is written as:

`SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`

Repository maintainers can review and replace the canonical master only after the physical print and final content-review gates are complete.
