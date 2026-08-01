# Canonical Case Structure Migration v1

**Status:** `APPROVED`

**Owner review:** `OWNER_REVIEW_PASS`

**Merge status:** `READY_TO_MERGE`

**Case 04:** `CASE04_NOT_STARTED`
**Baseline:** `c79bdc1f5b69bee9efb86998b375c5583542764f`

This is the additive execution and owner-supersession record for the canonical Cases 01–03 migration. It does not alter the original `REPOSITORY_INVENTORY_v1` or `PROPOSED_CLEANUP_PLAN_v1` snapshots. The 2026-08-01 owner decision authorizes the cleanup and supersedes that earlier conservative proposal wherever they conflict.

Owner testing by Nate / Owner passed on 2026-08-01. The signed decision is recorded in `CANONICAL_CASE_STRUCTURE_OWNER_APPROVAL_v1.md`. Accepted implementation commits are `34cbe2815e68eac577347a6f8c9d8eb54a085f0a` and `41554da0c7c1d25dee5958bacf6594f1643d5aec`; the reviewed branch also contains the pre-approval Case 03 Grayscale correction `85b0373a9b3301dab4071b78c3cb069ee31a5609`.

## Outcome

Cases 01–03 now contain only a README, canonical package-controlled worksheet sources, referenced optional icon source, and one compact current release-history record. The central Curriculum Editor discovers them through registry v2. Student, Teacher, Answer Key, and Accessible are the only roles. Grayscale is a Boolean presentation state for all four roles.

Generated editable documents, role HTML, PDFs, and routine screenshots are no longer permanent repository artifacts. Git history preserves every removed tracked file; each current release history gives the former complete document and four role paths, SHA-256 values, approved commit, page counts, validation status, and recovery syntax.

## Governing rules

- Canonical source is the registered case package and its package-controlled files under `source/`.
- Student, Teacher, Answer Key, and Accessible are the only instructional roles.
- Grayscale is only a Boolean presentation toggle; it is never a role, output type, filename, or page-count category.
- Generated editable copies, worksheets, PDFs, screenshots, and release documents are not committed.
- Prior approved artifacts are recovered through Git and compact release-history records.
- The canonical case folder structure is mandatory for Case 04 onward.

## Measured implementation change

These cleanup metrics are the implementation snapshot at `34cbe2815e68eac577347a6f8c9d8eb54a085f0a`; later recovery-metadata, validation, and approval records are additive.

- Tracked files: 483 before; 119 after.
- Tracked worktree content: 33,677,690 bytes before; 4,878,081 bytes after; net reduction 28,799,609 bytes. The 377 deleted paths contained 28,791,930 bytes at baseline.
- Path records: 8 exact renames, 13 additions, 20 modifications, and 377 deletions.
- Removed tracked artifacts: 19 PDFs; 27 stored release HTML files; 1 temporary generated portability-test HTML; 172 screenshots.
- Removed unused case assets: 2.
- Removed ignored local artifact: `teacher_v1.0_revalidated.pdf`, 483,312 bytes, SHA-256 `a7b4db344183939e160ed6188b40363b91e032cd1bebc3295034d9d6b5439dd3`; it was not imported.

The paired JSON contains the eight exact source moves, deletion-category totals, schema/registry changes, retired-validator map, and machine-readable validation results.

## Canonical files

- Package schema: `shared/implementation/case-package.schema.v2.json`
- Registry schema: `shared/implementation/case-registry.schema.v2.json`
- Registry: `shared/implementation/case-registry.v2.json`
- Structure gate: `shared/validation/validate_canonical_case_structure.py`
- Static gate: `apps/curriculum-editor/tests/validate_static.py`
- Browser gate: `apps/curriculum-editor/tests/run_browser_tests.py`

The browser gate generates all required role/export/print documents in memory or temporary storage, checks eight role/presentation combinations per case (24 total), and discards temporary output. It is the reproducible visual evidence command; no screenshots are retained.

Final owner-approval results: structure PASS for 3/3 cases, static PASS 72/72, browser PASS 358/358, all 24 presentation states PASS, recovery commits 13/13, recovery paths 25/25, recovery hashes 25/25, and zero JavaScript errors. The browser total includes a temporary rendered-screenshot smoke check whose output was discarded.

## Recovery

Recover any former tracked artifact without changing branches or history:

```sh
git show c79bdc1f5b69bee9efb86998b375c5583542764f:<former-path> > <destination>
```

Use the exact former paths in each `history/release-vX.json`. Earlier approved versions noted by the case README/history can likewise be inspected with `git show <approved-commit>:<path>`.

The migration is approved and ready for a fast-forward merge by the owner or integrator. No merge was performed, Git history was not rewritten, no PDF was generated, and Case 04 was not begun.
