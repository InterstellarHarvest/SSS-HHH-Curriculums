# Editor Shell Standard v1.0

The shared editor shell supplies reusable toolbar markup, component styles, CER geometry, and an icon sprite to the central Curriculum Editor. It does not assemble or store complete case documents.

Canonical shell files:

- `toolbar.html`
- `editor-shell.css`
- `curriculum-components.css`
- `cer.css`
- `icons.svg`

The central editor owns runtime behavior and portable serialization. Case packages own worksheet content, case presentation, task definitions, page counts, output names, Accessible layout eligibility/overrides, and any case-specific icons or assets.

The shell’s Role selector contains Student, Teacher, Answer Key, Accessible, and the complete-copy-only All Pages editing view. Grayscale is a separate Boolean presentation toggle for every role. It changes presentation tokens only and is never a role or output profile.

Accessible vertical response sizing is a central authoring primitive, not case CSS. Future SSS and HHH packages declare eligible substantial response fields through the shared `layout-overrides.schema.v1.json` contract. The editor supplies the same vertical-only handles, 4px snapping, bounds, page safety, drafts, sparse persistence, and export/print behavior. CER and all Student, Teacher, and Answer Key fields remain protected from this primitive.

Generated editable copies, selected-role worksheets, print documents, screenshots, and PDFs are not shell source files and are not committed. Validation assembles them temporarily from package sources.
