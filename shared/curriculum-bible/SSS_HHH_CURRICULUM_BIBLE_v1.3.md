# SSS-HHH Curriculum Bible

**Version:** 1.3  
**Effective date:** 2026-07-24  
**Predecessor:** `SSS_HHH_CURRICULUM_BIBLE_v1.2.md`  
**Status:** Approved governing successor for release-candidate production

## 1. Authority and preservation of v1.2

Curriculum Bible v1.3 incorporates **all requirements, definitions, protections, publishing rules, accessibility rules, task-reference rules, and Teacher-metadata rules in v1.2 without deletion or relaxation**. The complete v1.2 document remains in the repository as the retained predecessor and historical record.

Where this document is silent, the text of v1.2 continues unchanged. Where this document adds a rule, the new rule is cumulative. No v1.2 requirement is superseded except where v1.3 says so explicitly; v1.3 makes no such exception.

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

## 5. Release-candidate application

SSS Campaign 1 Case 01 is the first implementation of this v1.3 requirement. Its controlled Answer Key includes completed exemplars for Tasks 3 through 9, while Tasks 1 and 2 remain non-keyable and are omitted without renumbering.

## 6. Version record

- **v1.3:** Carries forward all v1.2 rules and adds the completed-exemplar Answer Key requirement.
- **v1.2:** Added task-reference parity, Teacher task-reference emphasis, and Teacher production-metadata visibility rules while retaining prior curriculum and publishing standards.
- **v1.1:** Clarified that extended-response boxes are blank and unruled.
- **v1.0:** Established the initial approved governing standard.
