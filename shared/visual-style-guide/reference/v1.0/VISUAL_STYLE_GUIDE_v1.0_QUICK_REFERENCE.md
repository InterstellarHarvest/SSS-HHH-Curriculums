# VISUAL_STYLE_GUIDE_v1.0 — Quick Reference

> Use this file for ordinary production decisions.  
> The authoritative standard remains `../../VISUAL_STYLE_GUIDE_v1.0.md`.

## Core Page

| Rule | Standard |
|---|---|
| Page | US Letter, portrait |
| Margins | 0.50 inches on all sides |
| Grid | 12 columns, approximately 0.125-inch gutter |
| Density | Balanced |
| Body type | Inter |
| Technical type | JetBrains Mono |
| Corners | 3 px technical rounding |
| Student identification | Name · Date · Period; topmost on first Student/Accessible page only |
| First-page identity | Student identification row, then Mission Title Block |
| Later pages | Compact continuation header |
| Footer | Split metadata, page number right |

## Print Type Reminder

A 96 px/in page preview must use point-equivalent CSS sizes. Ordinary body text is approximately 14.3 px for 10.75 pt; ordinary table text is approximately 12.7 px for 9.5 pt. Do not judge the approved scale from an undersized browser mockup.

## Page-Fill Rule

- Expand useful student response, drawing, graphing, and annotation areas before leaving avoidable blank space beneath them.
- In stacked CER, preserve minimum Claim / Evidence / Reasoning hierarchy, then add surplus height equally to all three.
- For short teacher or reference pages, combine pages or add a genuine notes area before accepting large blank regions.
- Teacher notes areas should occupy the remaining usable body space on short one-page teacher references, with a practical minimum height.
- Accessible response, drawing, and annotation areas should expand into remaining printable space; there is no arbitrary maximum box height when the larger area improves physical usability.
- Do not enlarge type or add decoration merely to fill paper.

## Institutional Identity

| SSS / SAA | HHH / TAA |
|---|---|
| Solar Agricultural Agency | Temporal Agricultural Archive |
| Orbital Cyan `#0b6f82` | Archive Amber `#8a5a00` |
| Botanical Green `#147a45` | Record Cyan `#0b6f82` |
| Cyan Field `#e7f3f5` | Archive Field `#f5eddd` |
| `shared/assets/insignia/saa.svg` | `shared/assets/insignia/taa.svg` |

Use the insignia once in the first-page header. Do not repeat it in every footer.

## SSS and HHH Differentiation

The shared geometry is intentional.

Use recurring structures to distinguish them:

| SSS / SAA | HHH / TAA |
|---|---|
| Mission and system status | Accession and source status |
| Environment readings | Period, region, and chronology |
| Mechanism and diagnosis | Provenance and source limitation |
| Engineering recommendation | Historical interpretation |
| Operational tone | Archival tone |

Do not invent unrelated border systems merely to increase visual difference.

## Ordinary Section

```text
[PHOSPHOR ICON + TECHNICAL LABEL] Section Heading
```

Use icons for recurring standardized sections. Use a plain heading or label-only heading for one-off subsections.

For numbered tasks, the standard title is 11.5 pt (14 pt in Accessible). Use a semantic technical label and show the number exactly once in `N · Title`. Never pair `TASK 01` with `1 · Title`.

## Choose the Component

| Need | Use |
|---|---|
| Ordinary prose or directions | Open section |
| Priority explanation or status | Left-rule pale-field callout |
| Short written response | Prompt + blank box |
| CER | Shared three-row label-block + response-field component |
| Five-stage mechanism | Deterministic equal-stage process grid; Accessible uses the vertical variant |
| Evidence collection | Ruled technical table |
| Two things compared | Matched comparison |
| Ordered events | Timeline |
| System interaction | Systems diagram |
| Source relationships | Provenance diagram |
| Spatial evidence | Sourced map |
| Numerical evidence | Graph with direct labels, shapes, and line styles |
| Teacher facilitation note | Neutral side stripe |
| Model answer | Dedicated answer-key block |
| Formal scoring | Analytic criteria grid |
| Completion check | Checklist rubric |
| New vocabulary | Term-definition table |

## Exact-Match Word Banks

Use for constrained fill-in-the-blank tasks when exact technical wording may be hard to retrieve.

- One bank entry per blank.
- Include all expected answers.
- No decoys, extras, or omissions.
- Repeat entries when reused.
- Keep phrase answers intact.
- Place beside the task on the same page.
- Standard, Accessible, and Answer Key wording must match exactly.

## Response Areas

- Blank and unruled.
- Prompt above the box.
- Guidance in short JetBrains Mono text.
- Size the box to the expected response.
- Claim is shortest; Evidence is taller; Reasoning is tallest.

## Callouts

Use one icon + one technical label.

| Meaning | Treatment |
|---|---|
| Science / History Focus | Institutional color |
| Documented / Confirmed | Success Green |
| Inferred / Debated | Caution Amber |
| Fictional Context | Technical Slate |
| Caution / Error | Critical Red |
| Optional | Institutional secondary |

Never rely on color alone.

## Figures

- Thin technical frame.
- Direct labels.
- Two neutral line weights + one accent.
- Orthogonal connectors for relationships.
- Caption metadata band.
- State whether the figure is original, adapted, reproduced, schematic, reconstructed, modeled, fictional, or not to scale.
- For classroom runtime-data figures, keep provenance to a compact caption. Do not add Student-facing production-commentary boxes such as `SOURCE STATUS` or `GAME-PROVIDED COMPARISON`.

## Recurring Components

- CER always uses the shared Claim / Evidence / Reasoning rows, with fixed accent labels at left and bordered fields at right. Accessible enlarges the same structure; Answer Key completes it.
- A five-stage process uses a deterministic grid with five equal stages and four aligned connectors. Do not use wrapping flex layouts. Accessible uses the shared vertical variant.
- Optional Extension is a canonical end-of-worksheet callout used only after required work and only when meaningful surplus space remains.

## Images

- One image must earn its place.
- Preserve authentic tonal character of historical photographs.
- Label scans and cropped excerpts.
- Use game assets selectively and frame them.
- Scale pixel art with nearest-neighbor, preferably at integer multiples.
- Never present game art as real evidence.

## Covers

Default: Mission-Title Cover.

Use one controlled hero visual. The title remains dominant.

## Teacher and Accessible Output

- Teacher answers never appear in student output.
- Answer keys mirror student section order.
- Keyed Answer Key headings preserve the Student task number and exact visible title; non-keyable tasks may be omitted silently without renumbering later tasks.
- Teacher references to a specific worksheet task use the same number and title.
- Direct Teacher references to a numbered Student task appear in **bold** with the exact number and title (`.task-reference`).
- Ordinary Teacher pages omit visible Compatibility / Source Baseline / provenance body blocks; keep that metadata in the footer, HTML metadata, or repository records.
- Parallel accessible edition preserves the same identifiers and order.
- Accessible versions may enlarge type, reduce density, increase pages, and support alternate response modes.

## Release Blockers

Do not publish with:

- overflow;
- placeholders;
- missing source status;
- missing attribution;
- teacher answers in student pages;
- color-only meaning;
- unsupported map geometry;
- blurred pixel art;
- incorrect page numbering;
- inaccessible required figures;
- missing role or metadata.

## Final Check

Use `VISUAL_STYLE_GUIDE_v1.0_COMPLIANCE_CHECKLIST.md` before release.

## HTML-only production

Beginning with Case 03, ship the portable editable-master HTML plus five independent role HTML files. Do not create PDFs during routine production. Use the browser print dialog at 100% / Actual Size for physical testing. Browser Print / Save PDF remains optional, but the result is not automatically accessible. Shared implementation documentation must state that accessibility verification is required before distribution.

## Balanced Page Fill and Vertical Rhythm v1.0.2

When a page has meaningful surplus height, use it first for restrained separation between major tasks, then for proportionate multi-line writing/model space, then for useful padding. Keep one-word, phrase, classification, status, criterion, constraint, label, and single-line fields compact. Preserve intentional bottom reserve; do not force complete page fill. Human judgment is final.

<!-- PRINTABLE_PAGE_IDENTITY_V1_0_4_START -->
## Printable Page Identity — v1.0.4

This project follows the consolidated `PRINTABLE_PAGE_IDENTITY_v1.0.4.md` rule. First pages use the compact accent-rail/title/location/institution-role structure; continuation pages use the compact case-title/role-continuation structure with institutional identity at right; printable footers contain only role and `N of total`; visible production-state metadata is excluded. Case 01 preserves approved v1.0 and uses a separate v1.1 validation successor. Case 02 applies the identity system to its single reconciled v1.0 master while retaining Balanced Page Fill and Vertical Rhythm v1.0.2.
<!-- PRINTABLE_PAGE_IDENTITY_V1_0_4_END -->
