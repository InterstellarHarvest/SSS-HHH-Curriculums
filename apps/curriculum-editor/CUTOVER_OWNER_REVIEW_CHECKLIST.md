# Curriculum Editor Cutover Owner Review Checklist

**Cutover status:** VALIDATION BUILD

**Owner gate:** OWNER GATE OPEN

**Do not mark accepted in this record until every item below is reviewed by the owner.**

Owner: ____________________  Date: ____________________

Browser/version: ____________________

## Launch and case loading

- [ ] From the repository root, `python3 apps/curriculum-editor/serve.py` starts the documented local server.
- [ ] <http://127.0.0.1:8000/apps/curriculum-editor/> loads without a JavaScript error.
- [ ] `1 - ISS Greenhouse` loads current package SSS-C1-CASE01 v1.1.
- [ ] `2 - Lunar Greenhouse` loads current package SSS-C1-CASE02 v1.0.
- [ ] `3 - Mars Habitat` loads current package SSS-C1-CASE03 v1.1.
- [ ] Versions are not offered in the primary case menu.

## Canonical workflow

- [ ] The root, application, architecture, handoff, registry, and all three case READMEs consistently identify the central editor as canonical.
- [ ] **Download Current HTML** produces a portable editable complete copy.
- [ ] **Download Current Role** produces clean role-specific HTML for the selected case/role.
- [ ] **Print / Save PDF** opens clean isolated-role browser printing without application chrome.
- [ ] The documentation states that browser-created PDFs require separate accessibility review.

## Retention and scope

- [ ] Approved standalone masters and role HTML are clearly described as immutable approved release snapshots.
- [ ] Embedded case-owned editors are clearly described as deprecated compatibility implementations.
- [ ] Protected hash validation confirms no approved artifact changed.
- [ ] PDF inventory/hash validation confirms no PDF was added, removed, or modified.
- [ ] No compatibility, provenance, validation, approved, or historical file was deleted.
- [ ] Repository cleanup remains a separate `NOT_STARTED` phase.
- [ ] Case 04 remains `NOT_STARTED`.

## Owner decision

- [ ] PASS — approve cutover in a separate additive acceptance record/commit.
- [ ] RETURN — keep `OWNER_GATE_OPEN` and record required changes below.

Notes:

______________________________________________________________________________

______________________________________________________________________________
