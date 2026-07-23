# VISUAL_STYLE_GUIDE_v1.0 — Asset Inventory

> **Purpose:** Record the shared visual assets and dependencies governed by v1.0.  
> **Rule:** Do not claim an asset variant exists unless its repository path is confirmed.

## 1. Confirmed Shared Assets

| Asset | Repository path | v1.0 role |
|---|---|---|
| SAA insignia | `shared/assets/insignia/saa.svg` | Primary scalable SSS curriculum mark |
| TAA insignia | `shared/assets/insignia/taa.svg` | Primary scalable HHH curriculum mark |

These are the insignias used by v1.0 reference templates.

## 2. Required Logical Variants

The visual system requires these outputs when the use case demands them:

- primary institutional color;
- one-color dark;
- one-color reversed;
- grayscale;
- simplified small size;
- pixel form for explicitly game-derived contexts.

A logical variant may be produced from the primary master when reliable. A separate file should be inventoried only after it exists.

## 3. Typography Dependencies

| Dependency | Use |
|---|---|
| Inter | Body, headings, tables, captions, prompts |
| JetBrains Mono | Metadata, technical labels, source status, codes |
| Phosphor Regular | Recurring section icons and semantic markers |

Do not commit or distribute font binaries through this reference package.

## 4. Game Assets

Game sprites, screenshots, and UI elements remain in their source repositories or packages unless intentionally copied into a curriculum case.

When reused, record:

- source project;
- repository path or asset identifier;
- crop;
- scale;
- modification;
- source-status caption;
- curriculum package destination.

## 5. Case-Specific Source Inventory

Each case should maintain an inventory with:

| Field | Required |
|---|---|
| Asset ID | Yes |
| File name | Yes |
| Curriculum destination | Yes |
| Source or creator | Yes |
| Date or period | When relevant |
| License / rights | Yes |
| Source status | Yes |
| Adaptation notes | When changed |
| Alt text | Digital use |
| Print test | When published |

## 6. Source-Status Vocabulary

Use only accurate labels:

- Curriculum-Original Figure
- Adapted From
- Reproduced From
- Schematic
- Reconstruction
- Model Output
- Illustrative Data
- Not to Scale
- Fictional Visualization
- Student-Created Figure
- Source Unknown
- Attribution Disputed
- Game Asset
- Game Screenshot
- Source Excerpt
- Cropped Excerpt

## 7. Reference Package Files

| File | Role |
|---|---|
| `VISUAL_STYLE_GUIDE_v1.0.md` | Authoritative visual standard |
| `VISUAL_STYLE_GUIDE_v1.0_QUICK_REFERENCE.md` | Production lookup |
| `VISUAL_STYLE_GUIDE_v1.0_ASSET_INVENTORY.md` | Asset governance |
| `VISUAL_STYLE_GUIDE_v1.0_COMPLIANCE_CHECKLIST.md` | Release gate |
| `VISUAL_STYLE_GUIDE_v1.0_TEMPLATE_GALLERY.html` | Reference implementation |

## 8. Historical Files

Guides v0.1–v0.9 and decision labs remain decision records. Candidate or placeholder artwork inside them is not an approved production asset unless separately listed above.
