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

New cases use `shared/implementation/editor-shell/v1.0/` plus case content/configuration. Beginning with Case 03, canonical production artifacts are the portable editable-master HTML and five independent role HTML files. Routine production does not create PDFs.

Approved Case 01 and Case 02 PDFs remain unchanged historical artifacts. The browser Print / Save PDF action is available for optional manual use, but its output requires accessibility verification before distribution.

## Historical artifacts

Files labeled v0.2 or v0.3 are retained only for provenance and comparison. They are not current validation masters and must not be used as production templates.

## Scaling rule

Do not begin another case by copying a historical or case-specific master. Assemble it from the canonical shared editor shell and registered case content/configuration after checking the governing documents and task registry.
