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

## Choose the Component

| Need | Use |
|---|---|
| Ordinary prose or directions | Open section |
| Priority explanation or status | Left-rule pale-field callout |
| Short written response | Prompt + blank box |
| CER | Three stacked boxes |
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
