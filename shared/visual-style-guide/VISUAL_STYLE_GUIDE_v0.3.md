# VISUAL_STYLE_GUIDE_v0.3

> **Repository Draft**  
> **Projects:** *Space Sprout Sleuth* (SSS) and *Hunger, Harvest, & History* (HHH)  
> **Status:** v0.3 — Typography, Grayscale, Institutional Color, and Icon System  
> **Supersedes:** `VISUAL_STYLE_GUIDE_v0.2.md`  
> **Decision record:** `decision-labs/v0.3/VISUAL_STYLE_GUIDE_v0.3_DECISIONS.md`  
> **Next planned revision:** v0.4 — Page grid, document anatomy, headers, footers, and page templates

---

## Document Control

| Field | Value |
|---|---|
| Document | Visual Style Guide |
| Version | 0.3 |
| Applies to | Student materials, teacher materials, printable resources, digital documents, diagrams, assessments, reference sheets, and curriculum-facing promotional graphics |
| Primary use | Establish the shared visual system and exact typography, grayscale, institutional color, and icon standards |
| Source of truth | This guide governs curriculum visuals; game lore and canonical organization names remain governed by the game repositories |
| Current maturity | Institutional identity, typography, grayscale, accent palettes, and general icon usage are locked; page geometry and production templates remain in development |

### Normative Language

The terms **must**, **must not**, **should**, **should not**, and **may** are used deliberately.

- **Must / must not:** required for visual consistency.
- **Should / should not:** preferred unless a documented exception improves clarity or accessibility.
- **May:** optional and context-dependent.

---

# 1. Revision Scope

Version 0.3 locks the following project-defining choices:

- **Primary typeface:** Inter
- **Technical and metadata typeface:** JetBrains Mono
- **Shared grayscale foundation:** Cool Mission Gray
- **SSS institutional palette:** Orbital Cyan + Botanical Green
- **HHH institutional palette:** Archive Amber + Record Cyan
- **General icon family:** Phosphor
- **Default icon treatment:** Phosphor Regular at a reinforced print weight

This revision also defines:

- approved font weights and fallback stacks;
- print and digital type hierarchy;
- exact grayscale and institutional color values;
- acceptable color roles;
- grayscale-survival requirements;
- contrast expectations;
- icon sizes, placement, and exceptions;
- CSS design tokens suitable for editable HTML masters.

This revision does **not** approve the provisional insignia or diagram artwork shown in the v0.3 decision lab. Those visuals were testing placeholders only.

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

# 19. Editable HTML Design Tokens

Editable HTML masters should begin with the following shared tokens or their documented equivalent.

```css
:root {
  /* Typography */
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

  /* Shared grayscale */
  --paper: #ffffff;
  --ink: #18212b;
  --muted: #4b5967;
  --rule: #8c9aa8;
  --panel: #edf1f4;
  --panel-light: #f7f9fa;

  /* SSS */
  --sss-primary: #0b6f82;
  --sss-secondary: #147a45;
  --sss-soft: #e7f3f5;

  /* HHH */
  --hhh-primary: #8a5a00;
  --hhh-secondary: #0b6f82;
  --hhh-soft: #f5eddd;

  /* Shared semantic states */
  --critical: #8f2f2f;
  --success: #236b3b;
  --caution: #8a5a00;
  --information: #0b6f82;
}
```

Template-specific aliases may then map the active institution:

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

Do not duplicate slightly altered values across files. Approved values should remain centralized.

---

# 20. Quality-Control Checklist

A page passes the v0.3 visual-system review when all applicable answers are **yes**.

## 20.1 Typography

- [ ] Inter is used for headings and body copy.
- [ ] JetBrains Mono is limited to technical or metadata roles.
- [ ] Body text remains within the approved size range.
- [ ] Weight and spacing create hierarchy without excessive decoration.
- [ ] All caps are limited to short labels and metadata.
- [ ] No novelty, game, handwriting, or faux-historical font has been introduced.

## 20.2 Grayscale

- [ ] Mission Ink is used for primary text.
- [ ] Technical Slate is not used below a readable contrast threshold.
- [ ] Instrument Gray is not used for essential small text.
- [ ] Pale panels are reinforced by borders when their boundary matters.
- [ ] Meaning survives grayscale conversion.
- [ ] Meaning does not depend on color alone.

## 20.3 SSS Color

- [ ] Orbital Cyan is the primary SAA accent.
- [ ] Botanical Green has a plant- or growth-specific role.
- [ ] Cyan Field is used sparingly.
- [ ] Accent coverage remains restrained.
- [ ] The page does not resemble a luminous game interface.

## 20.4 HHH Color

- [ ] Archive Amber is the primary TAA accent.
- [ ] Record Cyan represents verification, analysis, or continuity.
- [ ] Archive Field is used sparingly.
- [ ] The page does not use fake parchment or sepia decoration.
- [ ] Amber identity is not mistaken for an unlabeled warning.

## 20.5 Icons

- [ ] Phosphor is used for ordinary interface-style icons.
- [ ] Default icons follow the Regular reinforced-print treatment.
- [ ] Unfamiliar icons include text labels.
- [ ] Icon size matches the intended function.
- [ ] Icons are not being used as scattered decoration.
- [ ] Scientific diagrams have not been replaced with generic icons.
- [ ] Institutional insignia remain separate from the icon system.

## 20.6 Placeholder Exclusion

- [ ] The temporary SAA insignia from the v0.3 lab is not used.
- [ ] The temporary v0.3 lab diagrams are not used as approved figures.
- [ ] Only approved identity and diagram assets are included in production documents.

---

# 21. Deferred Specifications

The following items remain deliberately unresolved:

- final SAA insignia artwork;
- print-ready TAA insignia adaptation;
- insignia clear-space and minimum-size rules;
- page grid and exact Letter-size geometry;
- standard header and footer templates;
- component dimensions;
- formal diagram language;
- data-visualization rules;
- game-asset audit by file;
- final export and repository-production standards;
- complete accessibility and photocopy test results.

These items must be resolved before v1.0.

---

# 22. Decision Record

The v0.3 decision process selected:

| Decision | Approved result |
|---|---|
| Typography | Inter + JetBrains Mono |
| Shared grayscale | Cool Mission Gray |
| SSS palette | Orbital Cyan + Botanical Green |
| HHH palette | Archive Amber + Record Cyan |
| Icon treatment | Phosphor Regular at reinforced print weight |

The SSS typography, grayscale, color, and icon choices were exported from the interactive decision lab.

The HHH palette was subsequently approved as:

- Archive Amber `#8a5a00`
- Record Cyan `#0b6f82`
- Archive Field `#f5eddd`

The insignia and diagram placeholders were explicitly rejected as visual-quality references and remain unapproved.

---

# 23. Version History

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
