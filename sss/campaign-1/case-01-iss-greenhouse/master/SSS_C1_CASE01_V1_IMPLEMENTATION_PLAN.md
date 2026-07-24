# SSS Case 01 v1.0 — Implementation Plan and Completion Record

**Status:** Implemented for release-candidate validation on 2026-07-24

## Scope

Reconcile Case 01 into a coherent v1.0 validation master and reusable production foundation without redesigning the approved curriculum or visual system.

## Completed implementation

- Corrected the malformed Teacher procedure sentence.
- Synchronized all controlled source Markdown with the v1.0 HTML and task registry.
- Added Curriculum Bible v1.3 completed-exemplar requirements while preserving v1.2 task-reference and Teacher-metadata rules.
- Promoted v1.0 as the current Case 01 validation master in README and manifest.
- Marked v0.2/v0.3 assets historical.
- Limited Student response clearing to Student and Accessible fields.
- Added a separate Teacher/Answer Key notes-clear action.
- Made downloaded edited HTML portable by embedding the SAA insignia.
- Clarified Reset This File behavior and implemented restoration to the content embedded in the open file.
- Reconciled the blockers document with the completed game-content and source audits.
- Added content-regression checks for task headings, exemplar coverage, and malformed text.
- Generated Student, Teacher, Answer Key, Accessible, and Grayscale release-candidate PDFs.
- Retained VALIDATION BUILD pending owner physical print testing.

## Reusable foundation contracts

Later cases must reuse, rather than fork, the following:

- fixed Letter page shell and overflow warning;
- role values `student`, `teacher`, `answer`, `accessible`, and `all`;
- persistent state and content IDs;
- first-page-only Student identification row;
- exact task registry and heading parity checks;
- independent Answer Key with completed exemplars;
- selective Student response clearing and separate Teacher-notes clearing;
- portable edited-HTML download behavior;
- reset-to-open-file semantics;
- semantic grayscale tokens;
- content and PDF regression harness.

## Remaining owner action

Perform and document physical print testing. No other SSS case begins as part of this workstream.
