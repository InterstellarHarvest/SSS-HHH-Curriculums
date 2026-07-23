# VISUAL_STYLE_GUIDE_v0.4

> **Repository Draft**  
> **Projects:** *Space Sprout Sleuth* (SSS) and *Hunger, Harvest, & History* (HHH)  
> **Status:** v0.4 — Page Architecture, Mission Title Block, Grid, Margins, and Publication Metadata  
> **Supersedes:** `VISUAL_STYLE_GUIDE_v0.3.md`  
> **Decision records:** `decision-labs/v0.3/VISUAL_STYLE_GUIDE_v0.3_DECISIONS.md` and `decision-labs/v0.4/VISUAL_STYLE_GUIDE_v0.4_DECISIONS.md`  
> **Next planned revision:** v0.5 — Component library, response areas, tables, callouts, and instructional page elements

---

## Document Control

| Field | Value |
|---|---|
| Document | Visual Style Guide |
| Version | 0.4 |
| Applies to | Student materials, teacher materials, printable resources, digital documents, diagrams, assessments, reference sheets, and curriculum-facing promotional graphics |
| Primary use | Establish the shared visual system, typography, color, icon, page-grid, header, footer, margin, and document-anatomy standards |
| Source of truth | This guide governs curriculum visuals; game lore and canonical organization names remain governed by the game repositories |
| Current maturity | Institutional identity, typography, grayscale, accent palettes, icons, page geometry, margins, first-page headers, continuation headers, and publication footers are locked; component and diagram systems remain in development |

### Normative Language

The terms **must**, **must not**, **should**, **should not**, and **may** are used deliberately.

- **Must / must not:** required for visual consistency.
- **Should / should not:** preferred unless a documented exception improves clarity or accessibility.
- **May:** optional and context-dependent.

---

# 1. Revision Scope

Version 0.4 carries forward all approved v0.3 standards and locks the shared page architecture used by both curricula.

The following project-defining choices are now approved:

- **First-page header:** Mission Title Block
- **Continuation header:** compact institutional continuation header
- **Underlying page system:** 12-column modular grid
- **Default margins:** 0.50 inches on every side for every document role
- **Default density:** Balanced
- **Footer:** split publication-metadata rule
- **Visible student header metadata:** instructional identity only
- **Production metadata:** quiet footer placement
- **Role-switch behavior in editable masters:** preserves user-selected margins and layout settings

The v0.4 decision note originally exported the demo's default Identity Rail selection. The owner subsequently amended only that one selection to **Mission Title Block**. All other exported default selections remain approved.

This revision defines:

- the US Letter page model;
- first-page and continuation-page anatomy;
- exact visible header content;
- separation of student-facing identity from production metadata;
- modular column behavior;
- default margin behavior;
- information-density rules;
- standard footer content;
- page numbering;
- editable-master state persistence;
- page-overflow priorities;
- HTML design tokens for page architecture.

This revision does **not** approve final SAA insignia artwork, a print-redrawn TAA insignia, or a formal diagram language.

---

# 2. Purpose

This guide establishes a unified visual language for the *Space Sprout Sleuth* and *Hunger, Harvest, & History* curriculum projects.

The system must:

- present both curricula as professionally produced educational materials;
- preserve a recognizable connection to their shared fictional universe;
- distinguish SAA documents from TAA documents without making them appear unrelated;
- remain fully usable in grayscale;
- prioritize scientific and historical explanation over decoration;
- support ordinary classroom printing, photocopying, projection, and digital distribution;
- allow multiple authors or designers to create consistent pages without relying on undocumented taste.

The games are the investigative environments.

The curricula are the scientific, historical, and instructional documentation surrounding those environments.

Curriculum materials must not look like game merchandise, fan material, or lightly reformatted screenshots.

---

# 3. Core Design Position

## 3.1 Visual Formula

The shared curriculum system combines:

- NASA mission documentation;
- scientific field notebooks;
- government technical manuals;
- modern laboratory workbooks;
- archival research packets;
- restrained, selective in-universe details.

The resulting documents should feel credible in a classroom before their fictional context is noticed.

## 3.2 Priority Order

When design goals compete, use this order:

1. Readability
2. Instructional clarity
3. Accessibility
4. Diagrammatic explanation
5. Information organization
6. Institutional identity
7. Atmosphere
8. Decoration

Decoration must never displace explanation.

## 3.3 Visual Test

Every non-text visual element must do at least one of the following:

- explain information;
- organize information;
- identify the document or institution;
- direct attention;
- establish a necessary historical or scientific context.

If it does none of these, remove it.

---

# 4. Locked Project Decisions

## 4.1 Shared System

- Hybrid professional and in-universe visual style
- Moderate immersion
- Grayscale-first production
- NASA-inspired mission-document aesthetic
- Diagrams prioritized over decoration
- Mixed layouts, with panels used only where useful
- Blank bordered response boxes
- Phosphor icon family for interface-style symbols
- Selective reuse of game assets
- Thin, technical borders rather than decorative frames
- Professional typography rather than game or novelty fonts
- Inter + JetBrains Mono typography system
- Cool Mission Gray shared neutral system
- Mission Title Block as the shared first-page header
- Compact institutional continuation headers
- 12-column modular page grid
- 0.50-inch default margins for every document role
- Balanced default information density
- Split publication-metadata footer
- Production metadata excluded from the prominent visible header

## 4.2 Institutional Marks

- HHH uses the **Temporal Agricultural Archive (TAA)** insignia.
- SSS requires an **SAA sister insignia** built from the same design family.
- The existing TAA game sprite is a visual source, not automatically the final print master.
- The SAA sister insignia remains to be finalized in a later identity revision.
- The insignia and diagram placeholders in the v0.3 decision lab are not approved artwork.

---

# 5. Canonical Institutional Terminology

## 5.1 Solar Agricultural Authority

**Canonical full name:** Solar Agricultural Authority  
**Canonical abbreviation:** SAA  
**Associated curriculum:** *Space Sprout Sleuth*

The SSS repository consistently uses **Solar Agricultural Authority**. Earlier curriculum-guide wording that expanded SAA as “Space Agricultural Authority” or “Space Agriculture Authority” was incorrect.

### Required Usage

Use:

> Solar Agricultural Authority (SAA)

Do not use:

- Space Agricultural Authority
- Space Agriculture Authority
- Solar Agriculture Authority
- Space Agronomy Authority

### Institutional Character

For curriculum visual purposes, SAA is presented as an international and interplanetary scientific authority operating across the solar system. It investigates plant-growth failures, develops agricultural understanding, and supports successful cultivation beyond Earth.

SAA materials should suggest:

- scientific field operations;
- controlled investigations;
- orbital and planetary research;
- evidence-based diagnosis;
- public-service technical authority;
- practical, contemporary mission work.

SAA must not be visually framed as:

- a military command;
- a police agency;
- a secret intelligence organization;
- a commercial space corporation;
- a child-oriented “junior agent” club.

Its authority comes from scientific competence and public responsibility.

## 5.2 Temporal Agricultural Archive

**Canonical full name:** Temporal Agricultural Archive  
**Canonical abbreviation:** TAA  
**Associated curriculum:** *Hunger, Harvest, & History*

The TAA is a Concord institution founded jointly by humanity and the Zhel’ii. Its mandate is to study, document, preserve, and protect pivotal moments in the agricultural histories of member species.

### Institutional Character

TAA materials should suggest:

- archival rigor;
- historical evidence;
- preservation of records;
- provenance and source comparison;
- continuity across time;
- careful observation;
- institutional memory.

TAA must not be visually framed as:

- fantasy time magic;
- steampunk history;
- a museum gift shop;
- an antiquarian society;
- a secret occult archive.

Its authority comes from disciplined documentation and protection of the historical record.

## 5.3 Curriculum Titles

Use the following exact forms:

- *Space Sprout Sleuth*
- *Hunger, Harvest, & History*

Requirements:

- Preserve the ampersand in *Hunger, Harvest, & History*.
- Preserve the comma after “Harvest.”
- Do not abbreviate curriculum titles in student-facing display headings unless space requires it.
- SSS and HHH may be used in internal documentation, file names, production notes, and compact metadata.

---

# 6. Source-of-Truth Hierarchy

When names, lore, or visual conventions conflict, use the following hierarchy:

1. Shipped game content and current repository documentation
2. This visual style guide
3. Approved curriculum templates and component files
4. Production notes
5. Older drafts, demonstrations, and exploratory assets

A curriculum document must not silently rewrite game lore.

A deliberate lore change requires:

- an explicit project decision;
- updates to the relevant game or canonical design documentation;
- an entry in this guide’s version history;
- replacement of outdated templates and assets.

---

# 7. Brand Architecture

## 7.1 Shared Curriculum Family

SSS and HHH belong to one visual family but represent different institutions.

The shared curriculum system is not a third fictional organization and must not receive an invented seal, department name, or authority mark.

Shared family traits include:

- the same typographic foundation;
- the same page grid;
- the same component geometry;
- the same grayscale hierarchy;
- the same Phosphor icon rules;
- the same accessibility standards;
- the same restrained mission-document tone;
- the same diagram conventions.

## 7.2 Institutional Layer

| Attribute | SSS / SAA | HHH / TAA |
|---|---|---|
| Primary function | Scientific investigation of plant growth beyond Earth | Documentation and protection of agricultural history |
| Visual emphasis | Operations, systems, diagnosis, environments | Archives, evidence, provenance, chronology |
| Document character | Mission packet or technical investigation file | Archive packet or historical field record |
| Spatial motif | Orbit, station, habitat, controlled system | Thread, sequence, record, continuity |
| Botanical motif | Living sprout, leaf, root, cultivation system | Grain, seed, lineage, preserved record |
| Preferred diagrams | Systems, causes, experimental comparisons | Timelines, maps, source comparisons |
| Primary accent | Orbital Cyan | Archive Amber |
| Secondary accent | Botanical Green | Record Cyan |
| Institutional tone | Operational and empirical | Archival and evidentiary |

## 7.3 Relationship Rule

The two visual identities must feel like sister institutions within one future scientific culture.

They must not:

- use unrelated typographic systems;
- use radically different border geometry;
- use different icon families;
- use competing levels of immersion;
- appear to come from different publishers.

They should differ through:

- insignia;
- accent treatment;
- terminology;
- diagram emphasis;
- selected motif;
- document metadata.

## 7.4 Co-Branded Materials

A page may display both institutional marks only when its content genuinely connects both curricula or institutions.

Co-branded pages must:

- use a neutral shared header structure;
- give the two marks equal visual weight;
- keep the curriculum title more prominent than either mark;
- avoid inventing a combined SAA–TAA seal;
- remain visually balanced in grayscale.

Routine SSS pages should use only SAA identity.

Routine HHH pages should use only TAA identity.

---

# 8. Moderate Immersion Standard

## 8.1 Definition

Moderate immersion means the fictional institutions are visible, but educational function remains immediately clear.

A student should understand what to do without decoding role-play language.

## 8.2 Acceptable Treatment

Acceptable:

> SAA Observation Record  
> Record two differences between the plant samples.

Acceptable:

> TAA Evidence Comparison  
> Compare the two accounts and identify where they disagree.

Acceptable:

> Mission Reference: L2-HAB-04

## 8.3 Excessive Treatment

Avoid:

> Cadet, prove your worth to the Authority by unlocking the secret specimen file!

Avoid:

> Temporal Operative Clearance Required

Avoid:

> Your heroic mission begins now!

Avoid fake bureaucracy that adds no instructional value.

## 8.4 Insufficient Treatment

A document is also off-system when all institutional identity is removed and it resembles a generic worksheet assembled from unrelated classroom templates.

At minimum, a curriculum page should normally include:

- curriculum identification;
- appropriate SAA or TAA identity;
- consistent shared typography and geometry;
- a controlled header or footer system.

---

# 9. Typography System

## 9.1 Approved Typeface Pairing

The curriculum uses two type families.

### Primary Typeface

**Inter**

Use Inter for:

- document titles;
- section headings;
- subheadings;
- body copy;
- directions;
- questions;
- teacher guidance;
- tables;
- captions when a technical treatment is unnecessary.

### Technical Typeface

**JetBrains Mono**

Use JetBrains Mono for:

- document identifiers;
- mission or archive reference codes;
- compact metadata;
- measurement labels;
- diagram coordinates;
- data values when fixed alignment matters;
- figure numbers;
- version information;
- small institutional labels.

JetBrains Mono must not become the default body typeface. It provides technical contrast, not atmosphere through overuse.

## 9.2 Font Stacks

Editable HTML masters should use:

```css
--font-body:
  "Inter",
  "Arial",
  "Helvetica Neue",
  Helvetica,
  sans-serif;

--font-technical:
  "JetBrains Mono",
  "SFMono-Regular",
  Consolas,
  "Liberation Mono",
  "Courier New",
  monospace;
```

For browser-based editable masters, web fonts may be loaded from an approved source. Published PDFs must embed the fonts or convert the text through an export method that preserves appearance and searchability.

Do not distribute font files through the curriculum repository unless their licenses and redistribution terms have been explicitly reviewed.

## 9.3 Approved Weights

### Inter

| Weight | Use |
|---:|---|
| 400 | Body copy, captions, ordinary directions |
| 500 | Labels, short prompts, table emphasis |
| 600 | Subheadings, component titles, compact emphasis |
| 700 | Major headings and document titles |

Avoid 800 and 900 in ordinary curriculum materials. Heavy weights make the system feel promotional rather than documentary.

### JetBrains Mono

| Weight | Use |
|---:|---|
| 400 | Metadata, captions, ordinary codes |
| 500 | Labels and measurements requiring emphasis |
| 600 | Small headings or identifiers when print reproduction requires reinforcement |

Do not use JetBrains Mono 700 or 800 as a decorative display style.

## 9.4 Print Type Scale

The following sizes apply to standard US Letter pages unless an approved template specifies otherwise.

| Role | Typeface | Weight | Preferred size | Acceptable range | Line height |
|---|---|---:|---:|---:|---:|
| Packet or cover title | Inter | 700 | 28 pt | 24–32 pt | 1.05–1.15 |
| Page title | Inter | 700 | 22 pt | 19–26 pt | 1.10–1.20 |
| Section heading | Inter | 600–700 | 15 pt | 14–18 pt | 1.15–1.25 |
| Subheading | Inter | 600 | 12 pt | 11–14 pt | 1.20–1.30 |
| Body text | Inter | 400 | 10.75 pt | 10.25–11.5 pt | 1.40–1.55 |
| Directions or prompts | Inter | 500 | 10.75 pt | 10.25–12 pt | 1.35–1.50 |
| Table body | Inter | 400–500 | 9.5 pt | 9–10.5 pt | 1.25–1.40 |
| Caption | Inter | 400 | 8.5 pt | 8–9.5 pt | 1.30–1.45 |
| Technical label | JetBrains Mono | 400–600 | 8 pt | 7.5–9 pt | 1.25–1.40 |
| Footer metadata | JetBrains Mono | 400–500 | 7.5 pt | 7–8.5 pt | 1.20–1.35 |

Body text must not be reduced merely to fit an overfilled page. Edit, split, or restructure the content instead.

## 9.5 Digital Type Scale

For responsive HTML resources:

| Role | Preferred size |
|---|---:|
| Main title | 2–2.5rem |
| Page or activity title | 1.5–2rem |
| Section heading | 1.2–1.4rem |
| Subheading | 1.05–1.2rem |
| Body | 1rem |
| Supporting text | 0.875–0.95rem |
| Technical metadata | 0.75–0.85rem |

Digital body text should remain at or above 16 CSS pixels under ordinary browser zoom.

## 9.6 Heading Treatment

Headings should communicate hierarchy through:

- size;
- weight;
- spacing;
- rules or alignment when useful.

Do not rely on:

- multiple accent colors;
- shadows;
- outlines;
- gradients;
- decorative display fonts;
- all caps at large sizes.

### Capitalization

Use title case or sentence case for ordinary titles and headings.

All caps may be used for:

- short institutional labels;
- compact metadata;
- table headers;
- figure identifiers;
- document classifications.

All-caps strings should generally remain under 35 characters and use modest tracking.

## 9.7 Tracking and Spacing

Recommended letter spacing:

- Large Inter titles: `-0.02em` to `0`
- Ordinary Inter text: normal
- Small Inter labels: `0` to `0.02em`
- JetBrains Mono metadata: `0.04em` to `0.10em`
- All-caps metadata: `0.06em` to `0.12em`

Avoid wide tracking in body copy.

Paragraphs should use spacing between paragraphs rather than first-line indentation.

## 9.8 Emphasis

Use emphasis in this order:

1. wording and placement;
2. semibold weight;
3. institutional or semantic accent;
4. bordered callout where necessary.

Avoid long passages of bold text.

Italics may be used for:

- curriculum and publication titles;
- biological names;
- limited conventional emphasis.

Do not use italics for instructions that students must read quickly.

Underlining is reserved for:

- hyperlinks;
- short fill-in fields;
- conventional document notation when unavoidable.

## 9.9 Numerals and Data

Use tabular numerals when aligned numeric data requires it.

JetBrains Mono is preferred for:

- coordinates;
- instrument readings;
- data labels;
- mission dates;
- archive codes.

Do not switch entire tables to monospace unless fixed-width alignment provides a real benefit.

---

# 10. Shared Grayscale Foundation

## 10.1 Approved Palette: Cool Mission Gray

| Token | Name | Value | Primary role |
|---|---|---|---|
| `--paper` | Paper White | `#ffffff` | Default page background |
| `--ink` | Mission Ink | `#18212b` | Main text, strong borders |
| `--muted` | Technical Slate | `#4b5967` | Secondary text, captions |
| `--rule` | Instrument Gray | `#8c9aa8` | Rules, dividers, inactive outlines |
| `--panel` | Cool Panel | `#edf1f4` | Callouts, table headers, grouped metadata |
| `--panel-light` | Cool Wash | `#f7f9fa` | Very light differentiation |
| `--black` | Process Black | `#000000` | Rare maximum-density reproduction need |

## 10.2 Contrast Expectations

On white:

- Mission Ink has an approximate contrast ratio of **16.3:1**.
- Technical Slate has an approximate contrast ratio of **7.2:1**.
- Instrument Gray has an approximate contrast ratio of **2.9:1**.

Therefore:

- Mission Ink and Technical Slate may be used for ordinary text.
- Instrument Gray must not be used for essential small text.
- Instrument Gray is intended for borders, rules, nonessential annotation, and large graphical marks.
- Panel colors are backgrounds, not text colors.

Exact conformance must be checked in the final output format because rasterization, printer behavior, and transparency can alter effective contrast.

## 10.3 Grayscale Hierarchy

Use grayscale values consistently:

- **Mission Ink:** primary text and decisive structure
- **Technical Slate:** secondary text and supporting labels
- **Instrument Gray:** rules, axes, inactive boundaries
- **Cool Panel:** grouped information
- **Cool Wash:** subtle alternate rows or low-priority fields

Do not create arbitrary one-off grays.

## 10.4 Border Density

Preferred print border weights:

| Use | Preferred weight |
|---|---:|
| Fine divider | 0.5 pt |
| Ordinary component border | 0.75–1 pt |
| Response box | 1–1.25 pt |
| Major document division | 1.5–2 pt |
| Diagram primary path | 1–1.5 pt |
| Diagram secondary path | 0.75–1 pt |

Very light hairlines may disappear on classroom printers and photocopiers.

## 10.5 Grayscale-First Rule

Every page must remain understandable when:

- printed in black and white;
- photocopied;
- viewed with reduced color saturation;
- printed by a device that shifts colors unpredictably.

Color may reinforce meaning but must not carry meaning alone.

Use at least one additional differentiator:

- labels;
- symbols;
- line styles;
- patterns;
- direct annotation;
- position;
- border shape;
- numbering.

## 10.6 Photocopy Survival

Before publication, test representative pages using:

1. grayscale PDF conversion;
2. ordinary black-and-white printing;
3. one photocopy generation;
4. reduced-size printing when likely in classroom use.

The test must confirm that:

- response-box boundaries remain visible;
- table rules remain distinct;
- icons remain recognizable;
- accent-dependent labels remain understandable;
- pale panels do not disappear if their boundary matters;
- small metadata remains readable.

The v0.3 decision note did not record a grayscale preview. The owner subsequently approved the system, but a production grayscale test remains required before v1.0 approval.

---

# 11. SSS Institutional Color System

## 11.1 Approved Palette: Orbital Cyan + Botanical Green

| Token | Name | Value | Role |
|---|---|---|---|
| `--sss-primary` | Orbital Cyan | `#0b6f82` | SAA identity, scientific focus, active emphasis |
| `--sss-secondary` | Botanical Green | `#147a45` | Plant biology, growth, viable conditions |
| `--sss-soft` | Cyan Field | `#e7f3f5` | Pale panel tint and selected background |
| `--sss-paper` | Paper White | `#ffffff` | Default page background |
| `--sss-ink` | Mission Ink | `#18212b` | Primary text |

Approximate contrast on white:

- Orbital Cyan: **5.8:1**
- Botanical Green: **5.4:1**

Both may be used for ordinary-size text when applied without transparency. Mission Ink remains the default body-text color.

## 11.2 Color Roles

### Orbital Cyan

Use for:

- SAA identity bars;
- active section markers;
- scientific variable emphasis;
- figure callouts;
- selected labels;
- compact document references;
- primary diagram paths.

Do not use Orbital Cyan for large background fields containing long text.

### Botanical Green

Use for:

- botanical structures;
- successful growth or viable conditions;
- plant-specific category labels;
- growth-related diagram paths;
- secondary identity emphasis.

Botanical Green must not automatically mean “correct answer.” Academic correctness should be communicated through wording and assessment design, not color alone.

### Cyan Field

Use for:

- restrained callout backgrounds;
- selected table headers;
- small metadata fields;
- diagram zones.

Do not cover large percentages of a page with Cyan Field.

## 11.3 SSS Accent Balance

On an ordinary student page:

- Mission Ink and grayscale should dominate.
- Orbital Cyan should be the most visible accent.
- Botanical Green should appear less frequently and with a specific botanical purpose.
- Total visible accent coverage should usually remain below approximately 15% of the printed page.

The page must not look like a green environmental-education brochure or a luminous game interface.

---

# 12. HHH Institutional Color System

## 12.1 Approved Palette: Archive Amber + Record Cyan

| Token | Name | Value | Role |
|---|---|---|---|
| `--hhh-primary` | Archive Amber | `#8a5a00` | TAA identity, chronology, preserved evidence |
| `--hhh-secondary` | Record Cyan | `#0b6f82` | Verification, scientific continuity, linked records |
| `--hhh-soft` | Archive Field | `#f5eddd` | Pale panel tint and selected background |
| `--hhh-paper` | Paper White | `#ffffff` | Default page background |
| `--hhh-ink` | Mission Ink | `#18212b` | Primary text |

Approximate contrast on white:

- Archive Amber: **5.9:1**
- Record Cyan: **5.8:1**

Both may be used for ordinary-size text when applied without transparency. Mission Ink remains the default body-text color.

## 12.2 Color Roles

### Archive Amber

Use for:

- TAA identity bars;
- chronology markers;
- source and provenance labels;
- archive references;
- primary timeline paths;
- selected historical-evidence emphasis.

Archive Amber must not imitate aged parchment. The TAA is a future scientific institution, not a replica historical society.

### Record Cyan

Use for:

- verified connections;
- scientific analysis;
- cross-source links;
- continuity across records;
- secondary diagram paths;
- shared-family connection to SAA.

### Archive Field

Use for:

- restrained source-note panels;
- timeline metadata;
- evidence-register headers;
- selected archive callouts.

Do not apply faux paper texture, stains, torn edges, or sepia overlays.

## 12.3 HHH Accent Balance

On an ordinary student page:

- Mission Ink and grayscale should dominate.
- Archive Amber should be the primary identity accent.
- Record Cyan should be used selectively to represent verification, continuity, or technical analysis.
- Total visible accent coverage should usually remain below approximately 15% of the printed page.

The page must not become uniformly brown, antique, sepia, or parchment-like.

---

# 13. Shared Semantic Color

Institutional accents identify the curriculum. Semantic colors communicate states.

| Semantic role | Value | Required companion |
|---|---|---|
| Critical error or prohibition | `#8f2f2f` | Label and warning icon |
| Success or confirmed completion | `#236b3b` | Label or check icon |
| Caution | `#8a5a00` | “Caution” label and warning icon |
| Informational emphasis | `#0b6f82` | Descriptive label or information icon |

## 13.1 Conflict Rule

Because Archive Amber and Record Cyan are institutional colors in HHH:

- color alone must never indicate caution or information;
- semantic states must always use explicit labels and icons;
- urgent warnings in HHH should use the critical-red system rather than relying only on amber;
- identity color must not be interpreted automatically as status color.

## 13.2 Prohibited Semantic Use

Do not use:

- red for ordinary decoration;
- green as a universal “correct answer” highlight;
- gray alone to indicate disabled or inaccessible content when the distinction matters;
- color-only legends.

---

# 14. Color Application Rules

## 14.1 Default Text

Use Mission Ink for:

- body copy;
- instructions;
- questions;
- most headings;
- table content;
- captions requiring maximum readability.

Accent-colored text is reserved for short labels and controlled emphasis.

## 14.2 Large Color Fields

Large saturated backgrounds are generally prohibited in student and teacher documents.

Permitted exceptions:

- covers;
- section dividers;
- compact title bands;
- small institutional identity zones;
- digital-only navigation surfaces.

Large fields must retain sufficient contrast and must not consume excessive printer ink in the standard classroom edition.

## 14.3 Transparency

Do not reduce the opacity of essential text.

Transparent accent fills may be used only when:

- their boundary is independently visible;
- contrast remains adequate;
- grayscale reproduction remains understandable.

## 14.4 Gradients

Decorative gradients are prohibited.

A restrained technical gradient may be used only when it explains a continuous quantity, such as:

- intensity;
- concentration;
- temperature;
- chronology;
- probability.

The gradient must include labels or a scale and remain interpretable in grayscale.

## 14.5 Patterns

Use patterns sparingly for grayscale differentiation.

Preferred patterns:

- diagonal hatch;
- dot field;
- horizontal rule;
- crosshatch;
- dashed boundary.

Patterns must remain coarse enough to survive classroom printing.

---

# 15. Icon System

## 15.1 Approved Family

**Phosphor Icons** is the approved family for general interface-style symbols.

Use Phosphor for:

- instructional cues;
- navigation;
- status indicators;
- document controls;
- familiar actions;
- compact metadata;
- warnings;
- simple categories.

## 15.2 Approved Treatment

The default treatment is:

> **Phosphor Regular at a reinforced print weight**

For a standard 24 × 24 icon coordinate system, the target visible stroke is approximately **2 px**.

This treatment was selected to:

- retain the clarity of Phosphor Regular;
- survive classroom printing better than a lighter stroke;
- avoid the visual heaviness of Phosphor Bold at ordinary sizes.

## 15.3 Practical Implementation

### SVG or Editable Vector Use

When stroke control is available:

- use Regular geometry;
- target a 2 px stroke on a 24 px viewBox;
- use round line caps and joins where consistent with the source icon;
- preserve the original proportions;
- do not outline the icon with a second stroke.

### Packaged Fixed-Weight Icons

When only published Phosphor weights are available:

- use **Regular** at 20 px and above;
- test **Bold** only for icons at 16 px or below, or for known low-quality print environments;
- do not mix Regular and Bold arbitrarily on one page;
- document any size-dependent fallback in the template.

The term “reinforced print weight” is a production target, not a new unofficial Phosphor family name.

## 15.4 Standard Sizes

| Context | Preferred size | Minimum |
|---|---:|---:|
| Inline with body text | 16–18 px / 12–14 pt | 16 px |
| Component label | 20 px / 15 pt | 18 px |
| Section heading | 24 px / 18 pt | 20 px |
| Standalone instructional cue | 28–32 px / 21–24 pt | 24 px |
| Major status or navigation control | 32–40 px | 28 px |

A small icon must not be expected to carry complex scientific meaning.

## 15.5 Icon Color

Default icon color:

- Mission Ink for ordinary instructional symbols;
- institutional primary accent for selected section cues;
- semantic color only for explicit status states.

Icons inside pale panels may use the institutional primary accent when contrast is adequate.

Do not use multiple accent colors within a single ordinary Phosphor icon.

## 15.6 Icon and Label Relationship

Unfamiliar icons must be paired with text.

Preferred arrangements:

- icon followed by label;
- icon above a short label in compact navigation;
- icon within a heading row;
- icon beside a direct warning or status term.

Do not place a standalone icon where students must guess its meaning.

## 15.7 Icon Spacing

Preferred spacing:

- inline icon to text: 0.3–0.45em;
- heading icon to text: 6–10 px;
- icon to containing border: at least one-half the icon width;
- separate icon groups: at least one icon width.

Align icons optically with the text, not only by bounding box.

## 15.8 Filled and Duotone Icons

Filled and duotone Phosphor icons are not the default.

They may be used only when:

- a specific status requires stronger differentiation;
- the use is documented in an approved component;
- grayscale behavior is tested;
- the page does not mix styles casually.

## 15.9 Prohibited Icon Use

Do not:

- scatter icons as decoration;
- use icons as bullet points throughout long text;
- replace scientific diagrams with generic icons;
- use an icon without a clear semantic role;
- distort or rotate icons without functional reason;
- combine unrelated icon families;
- place icons inside extended response boxes;
- use game badges as substitutes for ordinary instructional icons.

## 15.10 Custom Icons

A custom icon may be created when Phosphor does not contain a scientifically or historically adequate symbol.

Custom icons must:

- match Phosphor’s basic stroke logic;
- remain legible at the intended size;
- include a text label when unfamiliar;
- be tested in grayscale;
- be added to the approved asset library;
- document its meaning and permitted contexts.

Custom scientific figures are not “icons” merely because they are small.

## 15.11 Separation of Visual Systems

Phosphor icons must not replace:

- SAA or TAA insignia;
- scientific diagrams;
- historical source images;
- botanical anatomy;
- project-specific evidence symbols;
- game rank badges;
- curriculum logos.

Institutional marks and explanatory figures follow separate systems.

---

# 16. Insignia System

## 16.1 TAA Source Mark

The existing TAA game insignia is a 96 × 96 pixel-art mark combining:

- a central grain or wheat form;
- enclosing temporal or orbital arcs;
- cool-cyan and amber accents;
- a compact near-circular silhouette;
- a technical future-archive character.

The game sprite is a source reference, not yet the universal curriculum master.

## 16.2 Required TAA Curriculum Set

The eventual curriculum-ready TAA mark set should include:

1. Primary color mark
2. One-color dark mark
3. One-color light or reversed mark
4. Grayscale mark
5. Simplified small-size mark
6. Pixel-art source mark for explicitly game-derived contexts

## 16.3 SAA Sister Insignia Requirement

The SAA mark must belong visibly to the same design family as the TAA mark while remaining distinct.

It should combine:

- a living sprout, leaf, or cultivation symbol;
- orbital, solar, habitat, or controlled-growth geometry;
- a compact institutional silhouette;
- strong monochrome behavior;
- small-size legibility.

It must avoid:

- generic leaf-and-planet clip art;
- military wings;
- shield-heavy police imagery;
- rockets as the dominant symbol;
- recycling-symbol resemblance;
- imitation of the NASA insignia;
- confusing similarity to the TAA wheat-and-thread composition.

## 16.4 Placeholder Status

The SAA mark and diagram figures in `VISUAL_STYLE_GUIDE_v0.3_DECISION_LAB.html` were temporary visual placeholders.

They must not be:

- extracted for use in curriculum materials;
- treated as approved concepts;
- added to the permanent asset library;
- used as the basis for print templates.

A future visual decision lab will compare intentional insignia candidates.

---

# 17. Diagrams and Illustrations

Diagrams receive priority over decorative artwork.

Preferred forms include:

- labeled scientific illustrations;
- system diagrams;
- cross sections;
- experimental comparisons;
- process flows;
- cause-and-effect chains;
- timelines;
- maps;
- evidence relationships.

The crude diagrams in the v0.3 decision lab are not style references.

Future diagram standards must define:

- line hierarchy;
- arrowheads;
- labels;
- leaders;
- annotation zones;
- figure numbering;
- legends;
- patterns;
- grayscale differentiation;
- source and caption treatment.

Until that revision, diagrams should remain clean, direct, and restrained rather than imitating the temporary lab graphics.

---

# 18. Panels, Borders, and Response Areas

## 18.1 Borders

Borders should be:

- thin;
- straight;
- technical;
- consistent;
- used to organize rather than decorate.

Permitted directions include:

- single-line frames;
- subtle double rules;
- corner registration marks;
- controlled metadata bands;
- open-sided technical dividers.

Rounded app-card styling should not become the default page language.

## 18.2 Panels

Use panels when they improve grouping or hierarchy.

Appropriate panel uses:

- document metadata;
- evidence summaries;
- vocabulary;
- teacher guidance;
- warnings;
- source notes;
- compact data displays.

Do not place every paragraph in a separate box.

## 18.3 Response Areas

Student response areas must be:

- blank;
- rectangular;
- clearly bordered;
- sized for the expected response;
- visually separate from explanatory text;
- printable without color.

Do not use:

- notebook lines by default;
- decorative parchment;
- handwriting fonts;
- speech bubbles;
- game-dialog boxes;
- patterned fills.

---

# 19. Page Model

## 19.1 Default Page

The default curriculum page is:

- US Letter;
- 8.5 × 11 inches;
- portrait;
- white;
- designed for ordinary classroom printers;
- visible as a page boundary in editable HTML;
- free of screen shadows and controls in print.

Landscape may be used only when the material genuinely requires it, such as:

- a wide comparison matrix;
- a complex map;
- a timeline that becomes illegible in portrait;
- a formal rubric with many required columns.

Landscape is an exception, not an alternate default.

## 19.2 Default Margins

Every document role defaults to:

```text
Top:    0.50 in
Right:  0.50 in
Bottom: 0.50 in
Left:   0.50 in
```

This applies equally to:

- student missions;
- evidence pages;
- teacher quick-start guides;
- formal lesson plans;
- answer keys;
- rubrics;
- reference sheets;
- assessments.

Teacher documents must not automatically switch to wider margins.

## 19.3 Margin Exceptions

Wider margins may be used only when a specific page requires them for:

- binding;
- extensive teacher annotation;
- unusually long-form reading;
- an institutional submission requirement;
- accessibility;
- reliable reproduction by a known printer.

A wider-margin exception must be intentional and page- or template-specific.

Changing document role in an editable publishing master must not change the active margin values.

## 19.4 Printable Safety

No required content may depend on a printer's non-printable edge.

Headers, footers, borders, response areas, and page numbers must remain entirely inside the selected content margins.

Decorative elements must never extend outside the printable safety area in a way that causes clipping or inconsistent output.

---

# 20. Modular Grid System

## 20.1 Approved Grid

The shared curriculum system uses a **12-column modular grid**.

The grid is virtual. It guides placement but does not need to be visible in published materials.

The same grid applies to SSS and HHH.

## 20.2 Approved Column Arrangements

Common arrangements include:

| Arrangement | Typical use |
|---|---|
| 12 | Long-form directions, readings, response areas, formal lesson prose |
| 8 / 4 | Teacher procedure plus quick-reference notes |
| 7 / 5 | Evidence task plus explanatory figure |
| 6 / 6 | Comparisons, matched response areas, before/after evidence |
| 4 / 4 / 4 | Compact metadata, three-part comparisons, option groups |
| 3 / 3 / 3 / 3 | Small repeated data cells only |
| 9 / 3 | Main instructional content plus a narrow reference rail |

Do not force content into columns merely because the grid permits it.

## 20.3 Grid Consistency

Within one page:

- columns must align;
- gutters must remain consistent;
- adjacent blocks should share visible edges;
- response areas should align with related prompts;
- figures and tables should align with the text that introduces them.

A page should not use several unrelated left edges.

## 20.4 Grid Gutter

The default print gutter is approximately **0.125 inches**.

A template may adjust the gutter modestly when:

- dense tables need more width;
- three or four repeated components need equal spacing;
- a large figure requires additional width.

Gutter changes must remain consistent within the page.

## 20.5 Spacing Rhythm

Use a restrained spacing rhythm derived from multiples of 4 and 8 CSS pixels in editable HTML.

Preferred print-space increments are approximately:

- 0.04 in;
- 0.08 in;
- 0.12 in;
- 0.16 in;
- 0.24 in.

The rhythm is a design aid, not a requirement to force every text line onto a literal baseline grid.

---

# 21. Information Density

## 21.1 Approved Default

The approved default is **Balanced**.

Balanced density means:

- the intended lesson fits its controlled page count;
- body text remains within the v0.3 type standards;
- response areas match the expected response;
- panels do not consume unnecessary space;
- whitespace separates tasks without making the page feel empty;
- figures are large enough to explain rather than decorate.

## 21.2 Open Density

Open density may be used for:

- younger readers;
- accessibility versions;
- major synthesis pages;
- diagram-centered pages;
- short reference sheets;
- pages intended for projection.

Open density must not increase page count without instructional benefit.

## 21.3 Compact Density

Compact density is reserved for:

- rubrics;
- answer keys;
- teacher-reference tables;
- source lists;
- controlled metadata;
- data-heavy evidence pages.

Compact density must not become the ordinary student-page style.

## 21.4 Overflow Priority

Resolve page overflow in this order:

1. remove unnecessary wording;
2. simplify or combine redundant labels;
3. reduce nonessential spacing;
4. move optional content;
5. add a deliberate page;
6. reduce type only as a last resort and never below the approved minimum.

Do not solve overflow by automatically switching to Compact density.

---

# 22. First-Page Header

## 22.1 Approved Architecture

The approved first-page header is the **Mission Title Block**.

The Mission Title Block uses:

- a narrow institutional accent rule or rail;
- a left-aligned title stack;
- a reserved insignia position;
- a strong activity or document title;
- a restrained contextual subtitle;
- no prominent production metadata.

The header should feel like an authentic mission or archive document without resembling a game HUD.

## 22.2 Header Hierarchy

The preferred hierarchy is:

1. issuing institution and document role;
2. activity, case, chapter, or document title;
3. campaign, setting, topic, or investigation focus;
4. institutional insignia.

Example SSS student header:

```text
SOLAR AGRICULTURAL AUTHORITY · STUDENT MISSION

CASE 01 · ISS GREENHOUSE MODULE
Campaign 1 · Low Earth Orbit · Gravitropism in Microgravity

[SAA INSIGNIA]
```

Example HHH student header:

```text
TEMPORAL AGRICULTURAL ARCHIVE · EVIDENCE RECORD

CASE 01 · THE FIRST FIELDS
Campaign 1 · Agricultural Origins · Comparing Historical Evidence

[TAA INSIGNIA]
```

## 22.3 Visible Header Content

The first-page header may prominently include:

- institution;
- curriculum or game title when useful;
- document role;
- campaign;
- case or chapter;
- activity title;
- setting;
- science or history focus;
- insignia.

The visible first-page header must not prominently include:

- curriculum version;
- game commit hash;
- publication date;
- draft status;
- compatibility baseline;
- internal file name;
- repository path;
- page count;
- technical document code.

Those items belong in the footer or source metadata.

## 22.4 Student Identification Row

Student documents place the identification row immediately below the first-page header.

Default fields:

```text
Name
Class / Period
Date
```

Additional fields may be added only when required, such as:

- group name for an optional collaborative extension;
- teacher name;
- school;
- course;
- student ID where institutionally required.

Do not crowd the header with form fields.

## 22.5 Teacher Documents

Teacher-facing documents use the same Mission Title Block architecture.

The role label changes appropriately:

- Teacher Quick Start
- Formal Lesson Plan
- Teacher Case Analysis
- Answer Key
- Technical Notes

Teacher pages do not receive a different visual identity or automatic margin system.

---

# 23. Continuation Header

## 23.1 Purpose

Continuation pages retain identity without repeating the full first-page masthead.

## 23.2 Approved Content

A continuation header contains:

- a compact SAA or TAA mark;
- the activity or document title;
- the document role;
- the word **Continued** when useful.

Example:

```text
[SAA]  Case 01 · ISS Greenhouse Module
       Student Mission · Continued
```

## 23.3 Excluded Content

Continuation headers should not contain:

- version;
- commit hash;
- publication date;
- compatibility information;
- large campaign metadata;
- repeated student name fields;
- a second full-size insignia.

Page number and publication metadata remain in the footer.

## 23.4 Space Use

The continuation header must be substantially smaller than the first-page Mission Title Block.

It should not reduce usable content space merely to repeat identity.

---

# 24. Publication Footer

## 24.1 Approved Architecture

The approved footer is the **Split Metadata Rule**.

It uses:

- a thin rule;
- quiet technical text on the left;
- page number on the right.

## 24.2 Student-Page Footer

A published student page may use:

```text
SSS-C1-01 · Curriculum v1.0 · Game baseline 2a6e8a7 · Published 2026-07-22
Page 1 of 2
```

The specific values are variables.

The footer fields are permanent production concepts.

## 24.3 Variable Fields

The following values change by release:

- document code;
- curriculum version;
- compatible game release or commit;
- publication date;
- status;
- page number;
- page total.

Do not hard-code sample values into reusable templates.

## 24.4 Required and Optional Footer Fields

Required for published curriculum documents:

- page number;
- curriculum version;
- campaign/case or document identifier;
- compatibility baseline where applicable.

Normally included:

- publication date.

Optional:

- Draft, Review, Approved, Deprecated, or Archived status;
- copyright or license line;
- source-package identifier;
- teacher-edition designation.

## 24.5 Footer Priority

Footer metadata is intended for:

- teachers;
- reviewers;
- repository maintainers;
- graduate-program reviewers;
- compatibility tracking.

It must remain readable but visually subordinate to student content.

## 24.6 Footer Exclusions

Do not place in the footer:

- instructional directions;
- required source evidence;
- vocabulary definitions;
- answer cues;
- important safety warnings.

A footer may not become a second content panel.

---

# 25. Page Anatomy by Document Role

## 25.1 Student Mission

Typical sequence:

1. Mission Title Block
2. Student identification row
3. Mission or investigation question
4. Science or history focus
5. Directions
6. Case-specific evidence task
7. Diagnosis or interpretation
8. CER or equivalent reasoning response
9. Application
10. Exit ticket
11. Optional extension
12. Publication footer

## 25.2 Evidence Page

Typical sequence:

1. Mission Title Block or continuation header
2. Evidence-page title
3. source or observation instructions;
4. primary figure, table, timeline, map, or evidence structure;
5. response or annotation area;
6. source caption;
7. publication footer.

An evidence page should not imitate a game inventory or clue screen.

## 25.3 Teacher Quick Start

Typical sequence:

1. Mission Title Block
2. lesson purpose;
3. duration and materials;
4. correct diagnosis or central interpretation;
5. essential science or historical context;
6. procedure by time;
7. likely sticking point;
8. collection requirements;
9. fallback procedure;
10. publication footer.

## 25.4 Formal Lesson Plan

Typical sequence:

1. Mission Title Block
2. overview and document metadata;
3. audience and course context;
4. objectives and success criteria;
5. standards;
6. materials and preparation;
7. procedure;
8. assessment;
9. differentiation and accessibility;
10. misconceptions;
11. science/fiction or source-status boundaries;
12. technical fallback;
13. references;
14. publication footer.

Long formal prose should default to a single readable column. Modular columns may be used for compact repeated information.

## 25.5 Answer Key

The answer key should mirror the student document's order where practical.

Use:

- identical section titles;
- clear model responses;
- accepted alternatives;
- common incomplete responses;
- teacher notes visually distinguished from student prompts.

Do not compress the answer key so aggressively that it becomes hard to use during instruction.

---

# 26. Editable-Master Behavior

## 26.1 State Persistence

Changing document role or preview mode must preserve the active user-selected:

- margins;
- density;
- grayscale state;
- page guides;
- visibility settings;
- optional-section choices where compatible.

A role change must not silently reset margins.

## 26.2 Defaults

The source master opens with:

- US Letter portrait;
- 0.50-inch margins;
- Balanced density;
- student view where the document includes student pages;
- color preview;
- page boundaries visible;
- production guides hidden.

## 26.3 Margin Controls

Editable masters may allow margin adjustment from 0.25 to 1.00 inches.

The reset control returns every role to 0.50 inches.

## 26.4 View Modes

Where applicable, publishing masters should support:

- Student
- Teacher
- Answer Key
- All Pages
- Edit
- Fillable Student
- Grayscale
- Print Preview

View-mode controls are screen-only and never appear in published output.

## 26.5 Overflow Warnings

Each fixed page should detect content overflow and display a visible screen-only warning.

Overflow warnings must not print.

---

# 27. Editable HTML Page Tokens

Editable HTML masters should incorporate the v0.3 typography and color tokens plus the following page tokens.

```css
:root {
  /* Page model */
  --page-width: 8.5in;
  --page-height: 11in;

  /* Universal defaults */
  --margin-top: 0.5in;
  --margin-right: 0.5in;
  --margin-bottom: 0.5in;
  --margin-left: 0.5in;

  /* Grid */
  --grid-columns: 12;
  --grid-gutter: 0.125in;

  /* Spacing rhythm */
  --space-1: 0.04in;
  --space-2: 0.08in;
  --space-3: 0.12in;
  --space-4: 0.16in;
  --space-6: 0.24in;

  /* Structure */
  --ordinary-border: 0.75pt;
  --response-border: 1.1pt;
  --major-rule: 1.5pt;
}
```

A standard page shell may use:

```css
.page {
  position: relative;
  width: var(--page-width);
  height: var(--page-height);
  background: var(--paper);
  break-after: page;
}

.page-content {
  position: absolute;
  top: var(--margin-top);
  right: var(--margin-right);
  bottom: var(--margin-bottom);
  left: var(--margin-left);
  overflow: hidden;
}

.modular-grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: var(--grid-gutter);
}
```

Institution-specific documents retain the v0.3 institutional aliases:

```css
.sss-document {
  --institution-primary: var(--sss-primary);
  --institution-secondary: var(--sss-secondary);
  --institution-soft: var(--sss-soft);
}

.hhh-document {
  --institution-primary: var(--hhh-primary);
  --institution-secondary: var(--hhh-secondary);
  --institution-soft: var(--hhh-soft);
}
```

Header components must use variable content rather than sample release values.

---

# 28. Page-Architecture Quality-Control Checklist

A page passes the v0.4 review when all applicable answers are **yes**.

## 28.1 Page Model

- [ ] The page is US Letter portrait unless an approved exception applies.
- [ ] All four margins default to 0.50 inches.
- [ ] Changing document role does not change the margin setting.
- [ ] Required content remains inside the printable safety area.
- [ ] Screen shadows, controls, and guides do not print.

## 28.2 Grid

- [ ] Content aligns to the 12-column modular grid.
- [ ] Gutters are consistent.
- [ ] The page does not use several unrelated left edges.
- [ ] Columns are used only when they improve comprehension.
- [ ] Response boxes align with their prompts.

## 28.3 Density

- [ ] Balanced density is used by default.
- [ ] Body text remains within the approved v0.3 size range.
- [ ] Compact density is justified by content type.
- [ ] Overflow was not solved by indiscriminate type reduction.
- [ ] Whitespace separates tasks without wasting the page.

## 28.4 Header

- [ ] The first page uses the Mission Title Block.
- [ ] The institution and document role are visible.
- [ ] The activity title is the dominant header element.
- [ ] The insignia remains subordinate to the document title.
- [ ] Version, commit, publication date, and status are absent from the prominent header.
- [ ] Student identification fields appear below the header rather than inside it.

## 28.5 Continuation Pages

- [ ] The continuation header is substantially smaller than the first-page header.
- [ ] It includes the institution, title, and continuation role.
- [ ] It does not repeat production metadata.
- [ ] It does not repeat student identification fields.
- [ ] The footer carries page numbering.

## 28.6 Footer

- [ ] The footer uses the split metadata rule.
- [ ] Variable metadata values are populated from the release.
- [ ] Page number and total are accurate.
- [ ] Footer text is readable but subordinate.
- [ ] No required instructional content appears in the footer.

## 28.7 Editable Master

- [ ] Role changes preserve selected settings.
- [ ] Reset returns margins to 0.50 inches.
- [ ] Overflow warnings are visible on screen.
- [ ] Overflow warnings do not print.
- [ ] Grayscale preview remains available.

---

# 29. Deferred Specifications

The following items remain deliberately unresolved:

- final SAA insignia artwork;
- curriculum-ready TAA insignia adaptation;
- insignia clear-space and minimum-size rules;
- complete component library;
- exact response-box size families;
- detailed table variants;
- formal diagram language;
- data-visualization standards;
- game-asset audit by file;
- final export and repository-production standards;
- completed accessibility and photocopy test results.

These items must be resolved before v1.0.

---

# 30. Decision Record

## 30.1 v0.3 Decisions Carried Forward

| Decision | Approved result |
|---|---|
| Typography | Inter + JetBrains Mono |
| Shared grayscale | Cool Mission Gray |
| SSS palette | Orbital Cyan + Botanical Green |
| HHH palette | Archive Amber + Record Cyan |
| Icon treatment | Phosphor Regular at reinforced print weight |

## 30.2 v0.4 Decisions

| Decision | Approved result |
|---|---|
| First-page header | Mission Title Block |
| Continuation header | Compact institutional continuation header |
| Underlying grid | 12-column modular grid |
| Universal default margins | 0.50 inches on every side |
| Default density | Balanced |
| Footer | Split publication-metadata rule |
| Header production metadata | Excluded |
| Footer production metadata | Included quietly |
| Role-switch behavior | Preserve active user settings |

The exported v0.4 decision note recorded the demo defaults. The owner subsequently changed only the header choice from Identity Rail to Mission Title Block. All other exported default selections remained approved.

---

# 31. Version History

## v0.4

- Locked the Mission Title Block as the shared first-page header.
- Removed production metadata from the prominent visible header.
- Locked compact institutional continuation headers.
- Locked the 12-column modular grid.
- Locked 0.50-inch margins for every document role.
- Clarified that wider margins are deliberate page-specific exceptions.
- Locked Balanced information density as the default.
- Locked the Split Metadata Rule footer.
- Defined variable versus permanent publication metadata.
- Defined page anatomy for student, evidence, teacher, formal-lesson, and answer-key documents.
- Required editable masters to preserve settings when switching document roles.
- Added page, grid, margin, density, header, footer, and state-persistence HTML tokens.
- Added a v0.4 page-architecture quality-control checklist.

## v0.3

- Locked Inter as the primary curriculum typeface.
- Locked JetBrains Mono as the technical and metadata typeface.
- Defined approved weights, sizes, spacing, and fallback stacks.
- Locked the Cool Mission Gray palette.
- Locked SSS Orbital Cyan + Botanical Green.
- Locked HHH Archive Amber + Record Cyan.
- Defined color roles, contrast expectations, and grayscale rules.
- Locked Phosphor Regular at a reinforced print weight.
- Defined icon sizes, placement, labels, and exceptions.
- Added editable HTML design tokens.
- Explicitly rejected the v0.3 lab insignia and diagrams as approved artwork.
- Added a v0.3 visual-system quality-control checklist.

## v0.2

- Corrected the canonical SAA expansion to **Solar Agricultural Authority**.
- Established the source-of-truth hierarchy.
- Defined the shared curriculum brand architecture.
- Distinguished SAA and TAA institutional character.
- Defined moderate-immersion boundaries.
- Documented the existing TAA insignia at a conceptual level.
- Established the design brief for the future SAA sister insignia.
- Added document identification examples and an identity QA checklist.
- Preserved the locked visual decisions from v0.1.

## v0.1

- Established the initial shared visual direction.
- Locked the hybrid professional/in-universe approach.
- Locked grayscale-first production.
- Locked Phosphor as the general icon family.
- Established diagrams over decoration.
- Established mixed layouts and blank bordered response boxes.
