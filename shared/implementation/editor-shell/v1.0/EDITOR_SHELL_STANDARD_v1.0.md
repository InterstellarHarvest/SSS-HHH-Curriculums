# Editor Shell Standard v1.0

The shared editor shell supplies reusable toolbar markup, component styles, CER geometry, Accessible-edition layout primitives, and an icon sprite to the central Curriculum Editor. It does not assemble or store complete case documents.

Canonical shell files:

- `toolbar.html`
- `editor-shell.css`
- `curriculum-components.css`
- `cer.css`
- `accessible-edition.css`
- `icons.svg`

The central editor owns runtime behavior and portable serialization. It always appends `accessible-edition.css` after case presentation and protected printable components, so editor views, editable copies, selected-role worksheets, isolated print documents, and future SSS/HHH packages receive the same Accessible defaults. Case packages own worksheet content, case presentation, task definitions, content-driven page counts, output names, Accessible layout eligibility/overrides, and any case-specific icons or assets.

Accessible pages normally contain one to three complete tasks. Their page counts are flexible: response usability and atomic task structure govern pagination. Use the shared `data-accessible-task`, `data-accessible-response`, `data-accessible-cer-page`, and `data-accessible-cer-subtitle` contracts instead of case-ID sizing overrides. Compact labels remain compact; substantial writing and organizers may grow to sensible content-driven sizes.

Every Accessible CER is the only numbered task on its page and uses `data-accessible-cer-page="canonical-v1.0"`, the exact canonical subtitle, and the shared `accessible-v1.0` Claim/Evidence/Reasoning component. The shared Accessible layer owns its Case 03 teal color and near-full-page geometry.

The shell’s Role selector contains Student, Teacher, Answer Key, Accessible, and the complete-copy-only All Pages editing view. Grayscale is a separate Boolean presentation toggle for every role. It changes presentation tokens only and is never a role or output profile.

Accessible vertical response sizing is a central authoring primitive, not case CSS. Future SSS and HHH packages declare eligible substantial response fields through the shared `layout-overrides.schema.v1.json` contract. The editor supplies the same vertical-only handles, 4px snapping, bounds, page safety, drafts, sparse persistence, and export/print behavior. CER and all Student, Teacher, and Answer Key fields remain protected from this primitive.

Generated editable copies, selected-role worksheets, print documents, screenshots, and PDFs are not shell source files and are not committed. Validation assembles them temporarily from package sources.
