# SSS-HHH Curriculums

Repository for the classroom curriculum system shared by **Space Sprout Sleuth (SSS)** and **Hunger, Harvest, & History (HHH)**.

## Governing documents

Use the following hierarchy for production work:

1. `shared/curriculum-bible/SSS_HHH_CURRICULUM_BIBLE_v1.3.md`
2. `shared/visual-style-guide/VISUAL_STYLE_GUIDE_v1.0.md` and approved v1.0.1 amendments
3. `shared/implementation/SSS_HHH_V1_EDITABLE_MASTER_HANDOFF.md`
4. Game-specific audit and blueprint documents
5. Case-level controlled sources, task registry, validation master, and release manifest

Curriculum Bible v1.3 carries forward v1.2, adds the completed-exemplar requirement, and records the HTML-only production decision effective with Case 03.

## Repository map

- `shared/` - governing standards, shared implementation guidance, and institutional assets
- `sss/` - Space Sprout Sleuth audit, blueprint, and case curriculum
- `hhh/` - Hunger, Harvest, & History curriculum work
- `resources/` - planning and support artifacts

## Current production foundation

For active customization of SSS Campaign 1 Cases 01–03, use the canonical central Curriculum Editor from the repository root:

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/>. Select the current case in the primary case menu; versions are not selected there. The action order is **Print / Save PDF**, **Download Editable Copy**, **Download Worksheet**, **Clear Responses**, and **Reset This Case**. Download Editable Copy produces the portable all-role editable HTML with its toolbar and current changes. Download Worksheet produces only the selected role as clean HTML without editing controls.

The registered current case package is the canonical active editable production source. New cases and future revisions use package-controlled content, task definitions, assets, and presentation sources with `shared/implementation/editor-shell/v1.0/`, then validate and publish through the central editor. Approved standalone masters and role HTML files are immutable release snapshots. Their embedded editors remain present only for compatibility and provenance; do not use them as the active customization workflow.

Approved historical PDFs remain unchanged retained artifacts. Routine repository production does not create PDFs. A PDF created through the browser requires separate accessibility review before distribution, publication, or archival use.

The approved cutover record is `shared/implementation/CURRICULUM_EDITOR_CUTOVER_v1.md`; owner approval is recorded in `apps/curriculum-editor/CUTOVER_OWNER_APPROVAL.md`. Repository cleanup and Case 04 are separate phases and remain `NOT_STARTED`.

## Historical artifacts

Files labeled v0.2 or v0.3 are retained only for provenance and comparison. They are not current validation masters and must not be used as production templates.

## Scaling rule

Do not begin another case by copying an approved or historical standalone master. Author package-controlled sources, load and validate them through the central editor, publish the approved HTML set, then freeze that set as immutable release snapshots.
