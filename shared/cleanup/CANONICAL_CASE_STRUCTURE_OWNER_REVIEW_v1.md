# Canonical Case Structure Owner Review v1

**Implementation status:** `IMPLEMENTED`

**Review status:** `OWNER_GATE_OPEN`
**Case 04 status:** `CASE04_NOT_STARTED`

Do not mark this migration accepted until the owner completes this review.

## Owner checklist

- [ ] Cases 01–03 each contain only `README.md`, canonical `source/` files, referenced optional source assets, and `history/release-vX.json`.
- [ ] The central editor loads all three packages through registry v2.
- [ ] Student, Teacher, Answer Key, and Accessible are the only instructional roles.
- [ ] Grayscale can be enabled independently for each of the four roles and does not change role identity or page count.
- [ ] No separate Grayscale document type, output name, role selector entry, autosave role, or page-count category is produced.
- [ ] Download Editable Copy includes all four roles, the editing toolbar, current edits/responses, and current Grayscale state.
- [ ] Download Worksheet includes only the selected role, applies its current presentation state, and uses that role's normal filename.
- [ ] Print / Save PDF builds a clean isolated document for the selected role with no application chrome, blank page, or screen page shadow.
- [ ] Current role page counts are 3/7/3/6 for Case 01, 3/7/3/5 for Case 02, and 4/8/4/7 for Case 03.
- [ ] Package schema v2, registry schema v2, source hashes, worksheet structure, task registry, CER/process atomicity, phrase-bank contract, and accessibility checks pass.
- [ ] All 24 case/role/color-or-Grayscale presentation states pass page-count, page-fit, identity, export, and print checks.
- [ ] The browser suite reports zero JavaScript errors.
- [ ] No tracked PDFs, generated release HTML, stored editable documents, or routine screenshots remain.
- [ ] Prior artifacts can be recovered with the paths, hashes, commits, and commands in each compact history record.
- [ ] A full validation run leaves the worktree clean after commit.
- [ ] Case 04 remains not started.

## Reproduction commands

```sh
python3 shared/validation/validate_canonical_case_structure.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/run_browser_tests.py
```

Browser validation uses temporary output and leaves no generated evidence in the repository. PDF generation is outside this review and must not be performed.

## Owner decision

- [ ] `ACCEPTED`
- [ ] `CHANGES_REQUESTED`

Owner: ____________________  Date: ____________________
