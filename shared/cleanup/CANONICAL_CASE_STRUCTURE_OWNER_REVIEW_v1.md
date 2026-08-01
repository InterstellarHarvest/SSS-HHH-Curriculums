# Canonical Case Structure Owner Review v1

**Implementation status:** `APPROVED`

**Review status:** `OWNER_REVIEW_PASS`
**Merge status:** `READY_TO_MERGE`
**Case 04 status:** `CASE04_NOT_STARTED`

Owner review was completed by Nate / Owner on 2026-08-01. The additive decision record is `CANONICAL_CASE_STRUCTURE_OWNER_APPROVAL_v1.md`.

## Owner checklist

- [x] Cases 01–03 each contain only `README.md`, canonical `source/` files, referenced optional source assets, and `history/release-vX.json`.
- [x] The central editor loads all three packages through registry v2.
- [x] Student, Teacher, Answer Key, and Accessible are the only instructional roles.
- [x] Grayscale can be enabled independently for each of the four roles and does not change role identity or page count.
- [x] No separate Grayscale document type, output name, role selector entry, autosave role, or page-count category is produced.
- [x] Download Editable Copy includes all four roles, the editing toolbar, current edits/responses, and current Grayscale state.
- [x] Download Worksheet includes only the selected role, applies its current presentation state, and uses that role's normal filename.
- [x] Print / Save PDF builds a clean isolated document for the selected role with no application chrome, blank page, or screen page shadow.
- [x] Current role page counts are 3/7/3/6 for Case 01, 3/7/3/5 for Case 02, and 4/8/4/7 for Case 03.
- [x] Package schema v2, registry schema v2, release-history schema v1, source hashes, worksheet structure, task registry, CER/process atomicity, phrase-bank contract, and accessibility checks pass.
- [x] Original-release approval commits and canonical-source approval commits have distinct, explicit meanings and resolve to existing commits.
- [x] Case 01 v1.0 and Case 03 v1.0 are fully indexed; Case 02 explicitly records no earlier approved release.
- [x] Direct `git show` validation proves every declared recovery path exists and all 25 recovered byte streams match their SHA-256 values.
- [x] All 24 case/role/color-or-Grayscale presentation states pass page-count, page-fit, identity, export, and print checks.
- [x] The browser suite reports zero JavaScript errors.
- [x] No tracked PDFs, generated release HTML, stored editable documents, or routine screenshots remain.
- [x] Prior artifacts can be recovered with the paths, hashes, commits, and commands in each compact history record.
- [x] A full validation run leaves the worktree clean after commit.
- [x] Case 04 remains not started.

## Reproduction commands

```sh
python3 shared/validation/validate_canonical_case_structure.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/run_browser_tests.py
```

Browser validation uses temporary output and leaves no generated evidence in the repository. PDF generation is outside this review and must not be performed.

## Owner decision

- [x] `ACCEPTED`
- [ ] `CHANGES_REQUESTED`

Owner: Nate / Owner  Date: 2026-08-01
