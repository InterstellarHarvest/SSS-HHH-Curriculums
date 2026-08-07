# Retired validators

A validator that no longer describes this repository is retired, not left in place to
crash. This file is the record of why. Git history remains the forensic recovery
mechanism for every entry below; nothing here needs to be restored to the working tree
to be recovered.

---

## `validate_repository_cleanup_audit.py`

**Retired:** 2026-08-06, in the Campaign 2 finalization maintenance pass.
**Last commit before retirement:** `c79bdc1f5b69bee9efb86998b375c5583542764f`
**Recover with:** `git show c79bdc1^:shared/validation/validate_repository_cleanup_audit.py`

### Former purpose

A baseline-anchored, no-change control for the repository cleanup audit. It asserted
that the working tree still matched the frozen inventory taken at
`66b4d5514d55aa4ce9972bea46227d7362d10ce3` — 477 tracked files, no baseline file
deleted, moved or modified, and Campaign 2 Case 04 `NOT_STARTED` in three manifests. It
was written to guard a *proposal*: `PROPOSED_CLEANUP_PLAN_v1` authorized no deletions at
all, and this validator existed to prove none had happened.

### Why it is retired

1. **Its inputs were intentionally retired.** It reads five files. One
   (`CLEANUP_OWNER_REVIEW_CHECKLIST_v1.md`) was never committed at any commit. The other
   four — `CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json`,
   `phase2-protected-artifacts.v1.json`, `CURRICULUM_EDITOR_CUTOVER_v1.json` and
   `CUTOVER_VALIDATION_RESULTS.json` — existed at the audit baseline and were deleted in
   `34cbe28`, the canonical case-structure migration. The frozen cleanup plan listed them
   as RETAIN, but `CANONICAL_CASE_STRUCTURE_MIGRATION_v1.md` records that the 2026-08-01
   owner decision "supersedes that earlier conservative proposal wherever they conflict",
   and `CANONICAL_CASE_STRUCTURE_OWNER_APPROVAL_v1.md` closes that the approval "does not
   restore any retired or generated artifact". **The missing inputs are intentional. They
   must not be restored.**

2. **It could not pass even if every input were restored.** It is a no-change assertion
   against a baseline that no longer describes this repository. It requires 477 tracked
   files; the tree it was retired from tracks 244. It requires that no baseline file was deleted, moved or
   modified; the approved migration moved or deleted 377 paths. It requires Campaign 2
   Case 04 to be `NOT_STARTED`; Case 04 is released at v1.1, `APPROVED_STABLE`.

3. **It was superseded by name.** `CANONICAL_CASE_STRUCTURE_MIGRATION_v1.json`
   `validatorRetirement[1]` retires "Phase 2 protected-inventory, reconciliation, package
   builder, binding audit, and cutover validator" — this workflow — and names its
   replacement: "schema v2 closed models, source hashes, compact histories, registry
   discovery, and structure/static gates".

4. **It was not part of the validation contract.** Nothing executed it. The root README
   validation workflow excluded it, `validate_static.py` never chained it, and the only
   live reference was its own self-listing in its `AUDIT_ADDITIONS` set. A prior audit had
   already classified it "Retired legacy-cleanup audit utility | NOT CURRENT / not counted."

### What replaces it

Nothing needs to. Its one live question — *has anything been deleted or altered that
should not have been?* — is now answered by mechanisms anchored to the current repository
rather than to a superseded snapshot:

- `validate_canonical_case_structure.py` — canonical layout, forbidden directories, no
  stored generated HTML, no tracked PDFs, across every registered case in every campaign.
- `validate_release_integrity.py` — every approved release certifies source that its
  pinned commit actually contains, and retained prior records are unmodified since the
  commit that wrote them.
- `validate_static.py` — package/registry/schema agreement and tracked-artifact controls.

### Surviving references

`shared/cleanup/PROPOSED_CLEANUP_PLAN_v1.json` and
`shared/cleanup/REPOSITORY_INVENTORY_v1.json` still name this file. Both are frozen,
baseline-anchored audit snapshots — the plan is marked "PROPOSAL ONLY — OWNER REVIEW
REQUIRED — NO DELETIONS AUTHORIZED" and both are pinned to `66b4d55`. They record what was
true at that baseline and are deliberately not edited. `CANONICAL_CASE_STRUCTURE_MIGRATION_v1`
supersedes them.
