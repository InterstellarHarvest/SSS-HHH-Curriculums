# SSS-HHH Curriculum Bible

**Version:** 1.3  
**Effective date:** 2026-07-24  
**Predecessor:** `SSS_HHH_CURRICULUM_BIBLE_v1.2.md`  
**Status:** Approved governing successor for release-candidate production

## 1. Authority and preservation of v1.2

Curriculum Bible v1.3 incorporates **all requirements, definitions, protections, publishing rules, accessibility rules, task-reference rules, and Teacher-metadata rules in v1.2 without deletion or relaxation**. The complete v1.2 document remains in the repository as the retained predecessor and historical record.

Where this document is silent, the text of v1.2 continues unchanged. Where this document adds a rule, the new rule is cumulative. Section 7 explicitly supersedes the predecessor's fixed-PDF and stored-output production requirements for all current cases.

The approved v1.0.1 visual-system amendments also remain controlling:

- `STUDENT_IDENTIFICATION_ROW_PLACEMENT_v1.0.1.md`
- `EXACT_MATCH_WORD_BANKS_v1.0.1.md`
- `TASK_REFERENCE_PARITY_v1.0.1.md`
- `TEACHER_TASK_REFERENCE_EMPHASIS_v1.0.1.md`
- `TEACHER_PRODUCTION_METADATA_VISIBILITY_v1.0.1.md`

## 2. Carried-forward task-reference rule

The Student worksheet remains the source of truth for numbered task identifiers and visible task titles.

1. Every keyed Answer Key section preserves the Student task's original number and exact visible title.
2. Non-keyable tasks may be omitted silently. Later Answer Key sections retain their original numbers and are not renumbered.
3. Accessible editions preserve the same numbered identifiers and exact titles.
4. A Teacher document that points to a specific Student task uses the same number and exact title.
5. A direct Teacher reference is bold in full, including the number; surrounding prose remains regular weight.
6. Technical labels may describe teacher function but never replace the shared task identifier.
7. A canonical task registry, when present, controls spelling, capitalization, numbering, and answer-key mapping.

## 3. Carried-forward Teacher production-metadata rule

Ordinary Teacher-facing classroom pages must not contain a visible body section devoted to internal compatibility or production lineage.

The following belong in HTML metadata, quiet publication footers, manifests, validation reports, migration reports, decision records, and Git history rather than ordinary Teacher-page body content:

- source-master version;
- migration date;
- repository path or internal filename;
- commit hash;
- validation history;
- checksum;
- build provenance;
- implementation notes intended for maintainers.

A concise game compatibility value may remain in the publication footer. Separate administrator, deployment, release-management, and technical-compatibility documents may display production metadata when operationally necessary.

## 4. New v1.3 requirement: completed Answer Key exemplars

### 4.1 Required coverage

Every keyable Student task must have a **completed exemplar** in the controlled Answer Key. A scoring note, accepted-answer list, rubric descriptor, or statement that answers may vary does not substitute for a completed exemplar.

A completed exemplar must:

1. use the exact Student task number and title;
2. answer every required field or subpart of the task;
3. model the expected depth without becoming an unnecessarily long essay;
4. show how evidence supports an interpretation when reasoning is assessed;
5. preserve the exact terms or phrases used by an exact-match word bank;
6. include a criterion and constraint when the Student task requires both;
7. answer the transfer question rather than merely restating the case diagnosis;
8. remain scientifically qualified where the governing audit requires qualification.

### 4.2 Evidence and reasoning tasks

For an evidence matrix, competing-explanation analysis, CER, mechanism model, or similar multi-part task, the exemplar must visibly complete each row, component, or labeled field needed to demonstrate proficient work.

For CER, the Answer Key must provide a complete Claim, Evidence, and Reasoning model. The Evidence model uses specific case evidence from more than one source when the case supports it. The Reasoning model explains the mechanism connecting evidence to the claim.

### 4.3 Engineering and application tasks

When a task requests a design, criterion, and constraint, the Answer Key supplies all three. The model must address the actual case mechanism rather than offer a generic improvement.

### 4.4 Acceptable variation

Reasonable alternative wording and other defensible solutions may follow the completed exemplar. Variation guidance is supplemental; it cannot replace the model response.

### 4.5 Accessible parity

The same task expectation governs the Standard and Accessible editions. The Answer Key may use one shared exemplar when both editions assess the same task, but it must match the exact shared task identifier and answer all required fields.

Accessible pagination is content-driven rather than tied to the Student page count. Pages normally contain one to three complete tasks, with substantially larger response areas than the Student edition. Complex tasks may stand alone, and intentional unused space is acceptable when the next task cannot fit without compression. Short labels and classifications remain compact; ordinary substantial writing may use approximately one-third of the writable page, and substantial models or multipart organizers may use approximately one-half.

Every Accessible CER is a dedicated near-full page using the shared `accessible-v1.0` Claim/Evidence/Reasoning component, the Case 03 teal, and this exact subtitle: `You may write sentences or use bullet points. Use evidence from more than one source.` Case-specific reasoning guidance must preserve the assessment requirement without revealing an answer.

## 5. Release-candidate application

SSS Campaign 1 Case 01 is the first implementation of this v1.3 requirement. Its controlled Answer Key includes completed exemplars for Tasks 3 through 9, while Tasks 1 and 2 remain non-keyable and are omitted without renumbering.

## 6. Version record

- **v1.3:** Carries forward all v1.2 rules and adds the completed-exemplar Answer Key requirement.
- **v1.2:** Added task-reference parity, Teacher task-reference emphasis, and Teacher production-metadata visibility rules while retaining prior curriculum and publishing standards.
- **v1.1:** Clarified that extended-response boxes are blank and unruled.
- **v1.0:** Established the initial approved governing standard.

## 7. Canonical package-source production decision

Current SSS/HHH production is package-source based and HTML-only. The registered package and its package-controlled `source/content.html`, `source/presentation.css`, `source/task-registry.js`, and referenced optional assets are the canonical production source. `content.html` is a worksheet-page fragment, not a complete embedded editor.

The four instructional roles are Student, Teacher, Answer Key, and Accessible. Grayscale is an independent Boolean presentation state for every role. It never creates another role, output profile, filename class, or page-count category.

The central Curriculum Editor generates portable editable copies and selected-role worksheets on demand. Generated HTML, PDFs, screenshots, and routine validation output are not committed. Prior approved release artifacts remain recoverable through Git history and compact case history records. Routine case production does not generate, regenerate, store, preflight, checksum, validate, or require PDFs.

The shared editor shell preserves the browser **Print / Save PDF** action for optional owner or end-user use. Browser export is not evidence that a PDF is accessible. Any manually created PDF intended for distribution, publication, or archival requires separate verification of tags, reading order, headings, alt text, tables, field labels, selectable text, title/language metadata, and screen-reader usability.

Release gates operate from canonical package sources and use temporary assembled documents: schema and source-hash validation, browser behavior, four-role isolation, color and Grayscale presentation states, portability/serialization, accessibility, package-declared page counts, clean isolated printing, and owner physical testing through the browser print dialog at 100% / Actual Size. Accessible validation enforces usability and structure without imposing a cross-case page-count target. Temporary generated output is discarded.

<!-- PRINTABLE_PAGE_IDENTITY_V1_0_4_START -->
## Printable Page Identity — v1.0.4

Printable page identity is governed by `shared/visual-style-guide/amendments/PRINTABLE_PAGE_IDENTITY_v1.0.4.md`. It changes publication identity and metadata visibility only; it does not change instructional content, task order, evidence requirements, assessment boundaries, or accessibility expectations.
<!-- PRINTABLE_PAGE_IDENTITY_V1_0_4_END -->
