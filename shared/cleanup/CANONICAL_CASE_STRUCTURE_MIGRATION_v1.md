# Canonical Case Structure Migration v1

**Status:** `IMPLEMENTED`

**Owner gate:** `OWNER_GATE_OPEN`

**Case 04:** `CASE04_NOT_STARTED`
**Baseline:** `c79bdc1f5b69bee9efb86998b375c5583542764f`

This is the additive execution and owner-supersession record for the canonical Cases 01–03 migration. It does not alter the original `REPOSITORY_INVENTORY_v1` or `PROPOSED_CLEANUP_PLAN_v1` snapshots. The 2026-08-01 owner decision authorizes the cleanup and supersedes that earlier conservative proposal wherever they conflict.

## Outcome

Cases 01–03 now contain only a README, canonical package-controlled worksheet sources, referenced optional icon source, and one compact current release-history record. The central Curriculum Editor discovers them through registry v2. Student, Teacher, Answer Key, and Accessible are the only roles. Grayscale is a Boolean presentation state for all four roles.

Generated editable documents, role HTML, PDFs, and routine screenshots are no longer permanent repository artifacts. Git history preserves every removed tracked file; each current release history gives the former complete document and four role paths, SHA-256 values, approved commit, page counts, validation status, and recovery syntax.

## Measured change

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

Final pre-commit results: structure PASS for 3/3 cases, static PASS 69/69, browser PASS 354/354, all 24 presentation states PASS, and zero JavaScript errors. The browser total includes a temporary rendered-screenshot smoke check whose output was discarded.

## Recovery

Recover any former tracked artifact without changing branches or history:

```sh
git show c79bdc1f5b69bee9efb86998b375c5583542764f:<former-path> > <destination>
```

Use the exact former paths in each `history/release-vX.json`. Earlier approved versions noted by the case README/history can likewise be inspected with `git show <approved-commit>:<path>`.

No merge was performed, Git history was not rewritten, no PDF was generated, and Case 04 was not begun.
