# Curriculum Editor Cutover Owner Review Checklist

**Cutover status:** APPROVED

**Owner gate:** OWNER REVIEW PASS

**Merge status:** READY TO MERGE

Owner: Nate / Owner  Date: 2026-08-01

Browser/version: Not recorded

## Launch and case loading

- [x] From the repository root, `python3 apps/curriculum-editor/serve.py` starts the documented local server.
- [x] <http://127.0.0.1:8000/apps/curriculum-editor/> loads without a JavaScript error.
- [x] `1 - ISS Greenhouse` loads current package SSS-C1-CASE01 v1.1.
- [x] `2 - Lunar Greenhouse` loads current package SSS-C1-CASE02 v1.0.
- [x] `3 - Mars Habitat` loads current package SSS-C1-CASE03 v1.1.
- [x] Versions are not offered in the primary case menu.

## Canonical workflow

- [x] The root, application, architecture, handoff, registry, and all three case READMEs consistently identify the central editor as canonical.
- [x] **Download Editable Copy** produces a portable editable complete copy containing all roles, the toolbar, and current changes.
- [x] **Download Worksheet** produces clean role-specific HTML for the selected case/role without editing controls.
- [x] **Print / Save PDF** opens clean isolated-role browser printing without application chrome.
- [x] **Clear Responses** clears response fields only in the selected role after confirmation.
- [x] **Reset This Case** restores only the loaded case/version to approved defaults after explicit confirmation.
- [x] The visible and keyboard action order is Print / Save PDF, Download Editable Copy, Download Worksheet, Clear Responses, Reset This Case.
- [x] The documentation states that browser-created PDFs require separate accessibility review.

## Retention and scope

- [x] Approved standalone masters and role HTML are clearly described as immutable approved release snapshots.
- [x] Embedded case-owned editors are clearly described as deprecated compatibility implementations.
- [x] Protected hash validation confirms no approved artifact changed.
- [x] PDF inventory/hash validation confirms no PDF was added, removed, or modified.
- [x] No compatibility, provenance, validation, approved, or historical file was deleted.
- [x] Repository cleanup remains a separate `NOT_STARTED` phase.
- [x] Case 04 remains `NOT_STARTED`.

## Owner decision

- [x] PASS — approve cutover in a separate additive acceptance record/commit.
- [ ] RETURN — record required changes below.

Notes:

Owner review passed. The additive acceptance record is `CUTOVER_OWNER_APPROVAL.md`.
