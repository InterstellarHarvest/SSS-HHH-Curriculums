# Proposed Cleanup Plan v1

**Status:** PROPOSAL ONLY — OWNER REVIEW REQUIRED — NO DELETIONS AUTHORIZED

**Baseline:** `66b4d5514d55aa4ce9972bea46227d7362d10ce3`

No tracked file meets the strict evidence threshold for `SAFE_DELETE`. The only low-risk tracked consolidation proposal is the reproducible set of full-resolution Phase 2 master/editor page captures; it is not authorized until the owner confirms that retained contact sheets, page-level diff captures, parity JSON, and deterministic generators are sufficient.

## Totals

- SAFE_DELETE: 0 files / 0 bytes
- SAFE_ARCHIVE_OR_CONSOLIDATE: 86 files / 8,886,331 bytes (8.47 MiB)
- RETAIN: 390 files / 22,670,489 bytes
- AMBIGUOUS_OWNER_DECISION: 1 files / 18,403 bytes
- Protected ledger: 110 items; 109 tracked and 1 local/untracked

## SAFE_DELETE

None. Exact byte duplication is concentrated in semantically distinct validation evidence, and every other apparent legacy item remains protected, referenced, or provenance-bearing.

## SAFE_ARCHIVE_OR_CONSOLIDATE

These files are mechanically reproducible and summarized by retained owner-review evidence. Consolidation means remove them from the tracked working set only after an owner-approved archive/evidence-manifest decision; it does not authorize discarding the audit record of their paths and hashes.

| Path | Bytes | Refs | Retained superseder | Risk |
|---|---:|---:|---|---|
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-04-editor.png` | 169,852 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-04-master.png` | 169,852 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-01-master.png` | 168,008 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-01-editor.png` | 168,006 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-05-master.png` | 164,724 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-05-editor.png` | 164,723 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-03-editor.png` | 159,001 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-03-master.png` | 159,001 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-07-editor.png` | 157,475 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-07-master.png` | 157,474 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-04-editor.png` | 152,277 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-04-master.png` | 152,277 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-02-editor.png` | 149,166 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-02-master.png` | 149,166 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/answer-02-editor.png` | 147,550 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/answer-02-master.png` | 147,550 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-02-editor.png` | 138,608 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-02-master.png` | 138,605 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/answer-03-editor.png` | 138,256 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/answer-03-master.png` | 138,256 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/student-01-editor.png` | 134,850 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/student-01-master.png` | 134,850 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/grayscale-01-editor.png` | 133,556 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/grayscale-01-master.png` | 133,556 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-05-master.png` | 127,386 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-05-editor.png` | 127,383 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-01-editor.png` | 125,059 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-01-master.png` | 125,058 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-06-editor.png` | 125,026 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/teacher-06-master.png` | 125,026 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-03-editor.png` | 123,917 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-03-master.png` | 123,917 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/answer-03-editor.png` | 119,886 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/answer-03-master.png` | 119,886 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-07-editor.png` | 112,987 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-07-master.png` | 112,987 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/answer-01-editor.png` | 108,067 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/answer-01-master.png` | 108,067 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-06-editor.png` | 103,517 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/teacher-06-master.png` | 103,517 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/answer-01-editor.png` | 97,720 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/answer-01-master.png` | 97,720 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-01-editor.png` | 95,725 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-01-master.png` | 95,725 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/student-01-editor.png` | 95,559 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/student-01-master.png` | 95,559 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/grayscale-01-editor.png` | 94,838 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/grayscale-01-master.png` | 94,837 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-01-editor.png` | 94,011 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-01-master.png` | 94,011 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/student-03-editor.png` | 93,000 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/student-03-master.png` | 93,000 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/grayscale-03-editor.png` | 92,352 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/grayscale-03-master.png` | 92,352 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/answer-02-editor.png` | 84,349 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/answer-02-master.png` | 84,349 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/student-02-editor.png` | 82,887 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/student-02-master.png` | 82,887 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/grayscale-02-editor.png` | 82,491 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/grayscale-02-master.png` | 82,491 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/student-02-editor.png` | 75,450 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/student-02-master.png` | 75,450 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/grayscale-02-master.png` | 74,988 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/grayscale-02-editor.png` | 74,987 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-06-master.png` | 73,437 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-06-editor.png` | 73,435 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-02-editor.png` | 72,985 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-02-master.png` | 72,985 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-03-editor.png` | 72,908 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-03-master.png` | 72,908 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-03-editor.png` | 66,827 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-03-master.png` | 66,827 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/student-03-editor.png` | 57,727 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/student-03-master.png` | 57,727 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/grayscale-03-editor.png` | 57,207 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/grayscale-03-master.png` | 57,206 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-04-editor.png` | 48,760 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-04-master.png` | 48,760 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-05-editor.png` | 47,715 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-05-master.png` | 47,715 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-04-master.png` | 45,872 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/accessible-04-editor.png` | 45,871 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case02/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-02-editor.png` | 43,298 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-02-master.png` | 43,298 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-05-editor.png` | 33,900 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-editor-contact-sheet.png` | LOW |
| `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/accessible-05-master.png` | 33,900 | 1 | `apps/curriculum-editor/tests/screenshots/parity-phase2/sss-c1-case01/all-roles-master-contact-sheet.png` | LOW |

Required post-consolidation validation: update non-frozen screenshot indexes/documentation, rerun Phase 2 parity and static suites, rerun cutover validation, rerun this audit validator, and obtain owner review of retained evidence.

## RETAIN

Retain 390 tracked files. This includes the canonical application and packages; all immutable masters/role outputs; all historical PDFs; governing docs; approvals; reconciliation and checksum ledgers; current builders/validators; final contact sheets/diff evidence; historical reports and standards; and all 44 legacy-workflow items until their recorded milestones.

The complete path-by-path RETAIN list and rationale is in `PROPOSED_CLEANUP_PLAN_v1.json`.

## AMBIGUOUS_OWNER_DECISION

1 tracked file requires an owner decision: `shared/validation/validate_editor_shell_contract.py`. It is unreferenced and fails both retained Case 03 master/config pairs, while the accepted current static suites pass. Repair it for current metadata/component evolution or archive it only after confirming its unique assertions are covered.

## Local-only temporary material

The audit observed 31 ignored `.DS_Store`/`__pycache__` files. They may be removed locally without changing Git history. The ignored protected PDF is explicitly excluded from this local-cleanup recommendation.

## Contradictions and gates

- **PROTECTED_PDF_NOT_TRACKED:** The protected ledger declares 20 historical PDFs, but the baseline Git tree contains only 19 PDFs. teacher_v1.0_revalidated.pdf exists locally and matches the ledger but is excluded by .git/info/exclude, which is not shared repository state. Decide whether to add the protected PDF to version control/LFS or amend the ledger and validators through a separately approved artifact-governance change. Do not delete the local file meanwhile.
- **BASELINE_SCOPE_AVOIDS_SELF_HASH:** An inventory cannot include its own final SHA-256 without a circular definition. This inventory therefore covers every file tracked at the required baseline commit; the five records and validator are separately constrained as the only allowed additions. Retain the baseline-anchored scope for reproducible validation, or define a future detached manifest/signature if hashes of audit outputs are required.
- **CURRENT_DOCS_REFERENCE_LEGACY_TOOLS:** Several case READMEs and the accepted static/cutover validators still reference items labeled legacy or candidate for later cleanup. They are not safe deletion candidates now. Establish and validate replacement reproduction paths before retiring or relocating legacy tools and fixtures.
- **STALE_SHARED_SHELL_VALIDATOR:** shared/validation/validate_editor_shell_contract.py has no detected current references and does not pass either retained Case 03 master/config pair: v1.0 reports 373/377 and v1.1 reports 378/379. The accepted current editor static suites still pass (103/103 and 74/74). Choose whether to repair this generic validator for current release metadata/component evolution or archive it after confirming its unique checks are covered by retained validators.

Case 04 remains `NOT_STARTED`. No file was deleted, moved, renamed, or rewritten during this pass.
