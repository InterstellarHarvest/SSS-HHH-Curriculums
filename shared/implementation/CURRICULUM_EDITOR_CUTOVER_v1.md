# Curriculum Editor Cutover v1

**Status:** APPROVED · OWNER REVIEW PASS · READY TO MERGE

**Effective cases:** SSS-C1-CASE01 v1.1 · SSS-C1-CASE02 v1.0 · SSS-C1-CASE03 v1.1

## Decision

The central Curriculum Editor is the canonical active authoring and customization workflow for the three effective cases. Start it from the repository root:

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/>. The canonical flow is the central editor plus shared shell v1.0 plus the registered current approved package. Its exact visible action order is **Print / Save PDF**, **Download Editable Copy**, **Download Worksheet**, **Clear Responses**, and **Reset This Case**. Download Editable Copy produces a portable all-role editable HTML document with its toolbar and current changes. Download Worksheet produces only the selected role as clean HTML without editing controls.

The registered package is `CANONICAL_ACTIVE_SOURCE`. Current approved standalone masters and role HTML files are immutable `APPROVED_RELEASE_SNAPSHOT` artifacts. Their embedded editors are `DEPRECATED_COMPATIBILITY`: they remain available for release fidelity, provenance, and validation, but active documentation does not direct users to customize through them.

## Effective packages

| Case | Package | SHA-256 |
|---|---|---|
| 1 - ISS Greenhouse v1.1 | `sss/campaign-1/case-01-iss-greenhouse/source/editor-package/case-package.v1.1.json` | `de7f64a57dade5c7c2fe123c98eef766292d2661bf2edd86bb1e7e9c53a9fd81` |
| 2 - Lunar Greenhouse v1.0 | `sss/campaign-1/case-02-lunar-greenhouse/source/editor-package/case-package.v1.0.json` | `d0075ec0259bd34b105415c5f1db809a1ffeabecb499370a3a230a94a0c3cb64` |
| 3 - Mars Habitat v1.1 | `sss/campaign-1/case-03-mars-habitat/source/editor-package/case-package.v1.1.json` | `f00d1617a2bee6630e43ff8ebb8f30d047412d0c86ed933c9cf2e0f2203a203d` |

All protected master and current role paths and hashes are recorded in the machine-readable companion. Phase 1 acceptance is commit `7b5b724b4941a7ad926fe1b0d644f6905ff55067`; Phase 2 owner approval is commit `e347370ed55913f04b54b8e942f191808f8e4aa9`.

## Artifact policy

- Approved masters and role HTML remain immutable release snapshots; no toolbar, script, or embedded runtime is stripped.
- All historical PDFs are `RETAINED` byte-identical evidence. Repository production and validation do not create, regenerate, normalize, modify, or remove PDFs.
- A PDF made through the browser requires separate accessibility review before distribution, publication, or archival use.
- Repository cleanup is `NOT_STARTED`. Case 04 is `NOT_STARTED`. Nothing is deleted in this cutover.

## Forward production rule

For a new case or future approved revision:

1. Author and maintain package-controlled content, task definitions, assets, and presentation sources.
2. Load and validate those sources through the central editor.
3. Generate portable complete and role-specific HTML through the approved publishing workflow.
4. Validate structure, geometry, presentation, page fit, accessibility, printing, and all required parity contracts.
5. Freeze approved release artifacts as immutable snapshots.
6. Never return an approved release snapshot to service as the ongoing editable source.

This rule is prospective. It does not rewrite the package or release history of Cases 01–03.

## Evidence and approval

The Phase 1 and Phase 2 acceptance records remain governing evidence. Nate / Owner approved the cutover on 2026-08-01 after the documented launch path, Cases 01–03 central loading, active documentation consistency, canonical workflow, release-snapshot retention, deprecated compatibility classification, and no-premature-deletion checks passed. The approval record is `apps/curriculum-editor/CUTOVER_OWNER_APPROVAL.md`, the completed checklist is `apps/curriculum-editor/CUTOVER_OWNER_REVIEW_CHECKLIST.md`, and machine-readable results are in `apps/curriculum-editor/CUTOVER_VALIDATION_RESULTS.json`.

The cutover validator is `shared/validation/validate_curriculum_editor_cutover.py`; the retained-runtime inventory is `shared/implementation/CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json`. Repository cleanup and Case 04 remain `NOT_STARTED`. This branch is ready for fast-forward merge, but the approval does not itself merge it.
