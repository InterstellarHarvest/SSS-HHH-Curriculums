# Cleanup Owner Review Checklist v1

**Audit baseline:** `66b4d5514d55aa4ce9972bea46227d7362d10ce3`

**Decision status:** PENDING OWNER REVIEW

## Scope and protections

- [ ] Confirm the inventory scope is the 477-file required baseline; the five records and validator are separate audit additions to avoid a self-hash cycle.
- [ ] Confirm the central Curriculum Editor and current Case 01 v1.1, Case 02 v1.0, and Case 03 v1.1 packages remain canonical production.
- [ ] Confirm all approved masters and role HTML files remain immutable and no embedded runtime is stripped from them.
- [ ] Confirm Case 03 v1.0 and all unique historical/provenance records remain retained.
- [ ] Confirm all approvals, cutover/reconciliation records, protected ledgers, current builders, and active validators remain retained.
- [ ] Confirm Case 04 remains `NOT_STARTED`.

## Historical PDF contradiction

- [ ] Resolve `sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/teacher_v1.0_revalidated.pdf`: it is one of 20 ledger-protected PDFs and exists locally with the recorded hash, but it is absent from the baseline Git tree and ignored only by local `.git/info/exclude`.
- [ ] Until resolved, do not delete, regenerate, normalize, or modify that local PDF or any of the 19 tracked historical PDFs.
- [ ] If tracking/LFS is chosen, add it in a separately reviewed artifact-governance change and rerun all protected-ledger validators.
- [ ] If ledger amendment is chosen, obtain explicit owner approval and preserve readable provenance for the prior 20-PDF assertion.

## Screenshot policy

- [ ] Decide whether to consolidate the 86 reproducible full-resolution Phase 2 master/editor page captures (8,886,331 bytes).
- [ ] Confirm that the retained all-role master/editor/diff contact sheets, all page-level diff images, approved parity JSON/totals, and parity generator are sufficient evidence before consolidation.
- [ ] If approved, update only non-frozen screenshot indexes/documentation and preserve this audit's original path/hash record.
- [ ] Rerun Phase 2 parity/static, cutover, and cleanup-audit validators after any consolidation.

## Legacy workflow (44 items)

- [ ] Confirm 27 immutable/provenance HTML artifacts are `RETAIN_PERMANENTLY`.
- [ ] Confirm 17 fixtures, historical sources, and build/validation tools are `RETAIN_UNTIL_LATER_COMPATIBILITY_MILESTONE` because current validators/manifests/docs still depend on them.
- [ ] Define a future compatibility milestone and replacement reproduction contract before relocating or removing any of those 17 items.
- [ ] Do not run legacy PDF-generating harnesses merely to test cleanup.

## Stale validator decision

- [ ] Decide whether to repair or archive `shared/validation/validate_editor_shell_contract.py`; it is unreferenced and fails both retained Case 03 configurations while the accepted current static suites pass.
- [ ] Before archival, compare its unique assertions with `apps/curriculum-editor/tests/validate_static.py`, `validate_phase2_static.py`, and the case-owned shell validator.
- [ ] If repaired, require it to pass current approved release metadata without modifying frozen master HTML.

## Decision

- [ ] APPROVE audit as written; authorize no cleanup yet.
- [ ] APPROVE the Phase 2 master/editor capture consolidation in a separate implementation pass.
- [ ] REQUEST CHANGES with exact paths and revised retention evidence.

Owner: ____________________

Date: ____________________

Notes: ____________________
