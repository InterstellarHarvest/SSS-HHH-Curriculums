# Canonical Case Structure Owner Approval v1

**Decision:** `APPROVED`

**Review status:** `OWNER_REVIEW_PASS`

**Merge status:** `READY_TO_MERGE`

**Approval date:** 2026-08-01

**Tester:** Nate / Owner

**Branch:** `feature/canonical-case-structure`

**Case 04:** `CASE04_NOT_STARTED`

## Approved implementation

The owner reviewed and accepted the canonical Cases 01–03 migration implemented by:

- `34cbe2815e68eac577347a6f8c9d8eb54a085f0a`
- `41554da0c7c1d25dee5958bacf6594f1643d5aec`

The reviewed branch also includes the pre-approval Case 03 Grayscale correction `85b0373a9b3301dab4071b78c3cb069ee31a5609`.

Owner testing passed for the final case-folder structure, registry v2 loading for Cases 01–03, the four-role model, independent Grayscale presentation for every role, both HTML download paths, isolated printing, Git recovery metadata, generated-artifact removal, and clean validation behavior.

## Accepted results

- Final case-folder structure: PASS.
- Cases 01–03 load through registry v2: PASS.
- Student, Teacher, Answer Key, and Accessible are the only instructional roles: PASS.
- Grayscale works independently for every role: PASS.
- No Grayscale role, output type, filename, or page-count category exists: PASS.
- Download Editable Copy: PASS.
- Download Worksheet: PASS.
- Clean isolated printing: PASS.
- Git recovery metadata: PASS.
- Generated-artifact removal: PASS.
- Validation leaves a clean worktree: PASS.
- Case 04 remains `NOT_STARTED`.

## Governing rules

1. Canonical source is the registered case package and its package-controlled files under `source/`.
2. Student, Teacher, Answer Key, and Accessible are the only instructional roles.
3. Grayscale is only a Boolean presentation toggle. It is never a role, output type, filename, or page-count category.
4. Generated editable copies and worksheets are not committed.
5. PDFs are not committed.
6. Generated screenshots are not committed.
7. Prior approved artifacts are recovered through Git and compact release-history records.
8. The canonical case folder structure is mandatory for Case 04 onward.

## Final validation evidence

- Canonical structure: 3/3 PASS.
- Static/schema/package validation: 72/72 PASS.
- Browser validation: 358/358 PASS.
- Role/presentation matrix: 24/24 PASS.
- Recovery commit references: 13/13 PASS.
- Recovery paths: 25/25 PASS.
- Recovery hashes: 25/25 PASS.
- JavaScript errors: 0.
- Tracked generated artifacts: 0.

The browser suite covers editable-copy exports, worksheet exports, isolated print documents, page counts, page fit, role identity, Grayscale independence, and temporary rendered evidence. Temporary output is discarded.

## Disposition

The canonical case-structure migration is approved and ready for a fast-forward merge by the owner or integrator. This approval does not authorize Codex to merge the branch, does not begin Case 04, and does not restore any retired or generated artifact.
