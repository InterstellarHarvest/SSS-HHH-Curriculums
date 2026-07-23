# VISUAL_STYLE_GUIDE_v0.6

> **Repository Draft**  
> **Projects:** *Space Sprout Sleuth* (SSS) and *Hunger, Harvest, & History* (HHH)  
> **Status:** v0.6 — Diagrams, Figures, Maps, Timelines, Graphs, Captions, and Source Status  
> **Supersedes:** `VISUAL_STYLE_GUIDE_v0.5.md`  
> **Decision records:** `decision-labs/v0.3/VISUAL_STYLE_GUIDE_v0.3_DECISIONS.md`, `decision-labs/v0.4/VISUAL_STYLE_GUIDE_v0.4_DECISIONS.md`, `decision-labs/v0.5/VISUAL_STYLE_GUIDE_v0.5_DECISIONS.md`, and `decision-labs/v0.6/VISUAL_STYLE_GUIDE_v0.6_DECISIONS.md`  
> **Next planned revision:** v0.7 — Institutional insignia, section-icon vocabulary, semantic markers, and publication-status marks

---

## Document Control

| Field | Value |
|---|---|
| Document | Visual Style Guide |
| Version | 0.6 |
| Applies to | Student materials, teacher materials, printable resources, digital documents, diagrams, assessments, reference sheets, and curriculum-facing promotional graphics |
| Primary use | Establish the shared visual system and exact standards for typography, color, icons, page architecture, components, diagrams, figures, maps, timelines, graphs, captions, attribution, and source status |
| Source of truth | This guide governs curriculum visuals; game lore and canonical organization names remain governed by the game repositories |
| Current maturity | Institutional identity, typography, grayscale, accent palettes, icons, page architecture, component systems, explanatory diagrams, figures, maps, timelines, graphs, captions, and source-status conventions are locked; insignia, image reuse, assessment, accessibility, and production systems remain in development |

### Normative Language

The terms **must**, **must not**, **should**, **should not**, and **may** are used deliberately.

- **Must / must not:** required for visual consistency.
- **Should / should not:** preferred unless a documented exception improves clarity or accessibility.
- **May:** optional and context-dependent.

---

# 1. Revision Scope

Version 0.6 carries forward all approved v0.5 standards and locks the shared explanatory-visual language used across SSS and HHH curriculum materials.

The following project-defining visual choices are approved:

- **Label system:** direct labels
- **Line hierarchy:** two neutral weights plus one instructional accent
- **Connector and arrow style:** orthogonal connectors
- **Ordinary figure framing:** thin technical frame
- **Caption and source treatment:** caption metadata band
- **Graph and category differentiation:** direct labels plus shapes and line styles
- **Status and uncertainty key:** shown when a figure contains multiple evidence states
- **Geographic maps:** sourced geometry required
- **Source status:** explicitly stated for original, adapted, reproduced, schematic, reconstructed, fictional, modeled, illustrative, and not-to-scale figures

The v0.6 decision was reviewed primarily in the SSS quantitative-graph context. The same shared visual logic applies across SSS and HHH diagrams, timelines, provenance chains, maps, and graphs.

This revision defines:

- direct-label placement;
- numbered-key exceptions;
- line and arrow hierarchy;
- orthogonal connector behavior;
- figure framing;
- graph and chart standards;
- scientific mechanism diagrams;
- timelines;
- provenance diagrams;
- map standards;
- uncertainty and reconstruction markings;
- captions;
- source-status metadata;
- figure numbering;
- legends;
- grayscale-independent data encoding;
- figure CSS and SVG tokens;
- explanatory-visual quality-control checks.

The grayscale preview was not recorded as viewed in the decision note. The visual decisions are approved, but representative visuals still require production grayscale and photocopy testing before v1.0.

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
- Technical label headings as the ordinary section-heading system
- Left-rule pale-field callouts
- Prompt-above-box response areas
- Ruled grayscale-first technical tables
- Neutral side-stripe teacher notes
- 3 px technical component rounding
- Multiple functional evidence-layout families
- Direct labeling as the ordinary explanatory-visual default
- Two neutral line weights plus one instructional accent
- Orthogonal connectors as the ordinary process and relationship default
- Thin technical frames around ordinary figures
- Caption metadata bands with explicit source status
- Direct graph labels combined with shapes and line styles
- Explicit documented, inferred/reconstructed, and fictional-status keys
- Sourced geographic geometry for curriculum maps

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

# 29. Component-System Principles

## 29.1 Open Document Surface

Curriculum pages remain documents, not dashboards.

The ordinary page should primarily use:

- headings;
- paragraphs;
- directions;
- rules;
- tables;
- figures;
- response areas;
- selective callouts;
- selective teacher notes.

Do not place every section inside a bordered or tinted card.

## 29.2 Component Test

A component is justified when it improves at least one of the following:

- hierarchy;
- grouping;
- readability;
- task completion;
- evidence comparison;
- status recognition;
- teacher usability;
- accessibility.

If an ordinary heading and paragraph communicate the content clearly, do not add a panel.

## 29.3 Shared Geometry

SSS and HHH use the same component geometry.

They differ through:

- institutional accent color;
- terminology;
- insignia;
- subject-specific figure and evidence content.

They do not use separate table, response-box, or teacher-note systems.

## 29.4 Technical Rounding

Printed curriculum components use a subtle **3 px technical radius** in editable HTML.

This applies to:

- response boxes;
- callouts with full outer borders;
- teacher-note borders;
- compact labeled panels;
- selected form controls in digital copies.

The radius should read as a softened technical corner, not as an app card.

Do not use:

- large rounded cards;
- pill-shaped content boxes;
- decorative bubbles;
- mixed arbitrary radii.

Rules, table cells, page borders, and major structural divisions may remain square when rounding would weaken alignment.

---

# 30. Technical Label Heading System

## 30.1 Approved Default

The ordinary section heading uses a **Technical Label Heading**.

Its anatomy is:

1. a short bordered technical label;
2. the section heading;
3. optional supporting rule or spacing.

Example:

```text
[01 · LAUNCH]  Mission question
```

Example:

```text
[EVIDENCE]  Compare the records
```

Example:

```text
[TEACHER NOTE]  Watch for
```

## 30.2 Purpose

The technical label provides subtle in-universe mission-document character while the heading remains plain and educational.

The label may communicate:

- sequence;
- task type;
- evidence phase;
- document role;
- optional status;
- source category.

The label must not require students to decode fictional terminology before understanding the task.

## 30.3 Label Content

Preferred label forms:

- `01 · LAUNCH`
- `02 · INVESTIGATE`
- `EVIDENCE`
- `COMPARE`
- `UNGRADED`
- `OPTIONAL`
- `TEACHER NOTE`
- `SOURCE STATUS`
- `EXIT`

Labels should normally contain no more than:

- 2–3 short words; or
- one sequence number and one short word.

Avoid long sentences inside labels.

## 30.4 Visual Treatment

The default label uses:

- JetBrains Mono;
- 7.5–9 pt print size;
- 500–600 weight;
- short uppercase text;
- institutional primary accent;
- 0.75–1 pt border;
- 3 px technical radius;
- compact horizontal padding.

The heading uses Inter at the approved section-heading size.

## 30.5 Heading Alignment

Preferred arrangement:

```text
[LABEL] Heading
```

The label and heading align on a shared optical center.

A thin horizontal rule may continue beneath the heading when the page needs stronger separation, but the rule is not mandatory on every component.

## 30.6 Plain-Heading Exception

Use a plain heading without a technical label when:

- the label would repeat the heading;
- the content is long-form prose;
- the page already contains many labeled steps;
- a formal lesson-plan section benefits from quieter hierarchy;
- accessibility requires reduced visual complexity.

The technical label system is the default component treatment, not a requirement to label every heading.

## 30.7 Prohibited Use

Do not:

- place a different color on every label;
- use fictional clearance levels;
- use decorative serial numbers with no meaning;
- create labels longer than the heading;
- place labels on ordinary body paragraphs;
- use labels as a substitute for numbered directions.

---

# 31. Callout System

## 31.1 Approved Default

The ordinary priority callout uses:

- a 3 px left rule;
- a pale field;
- a short bold title;
- concise supporting text;
- 3 px technical corner rounding where the outer shape is visible.

## 31.2 Appropriate Uses

Use callouts for:

- science focus;
- history focus;
- evidence rules;
- source-status boundaries;
- safety or caution;
- critical misconceptions;
- concise definitions needed at the point of use;
- optional extensions;
- technical fallback;
- important conclusions in teacher copies.

Do not use callouts for ordinary explanatory paragraphs.

## 31.3 Institutional Callouts

### SSS

Default identity callout:

- left rule: Orbital Cyan;
- pale field: Cyan Field;
- text: Mission Ink.

Botanical Green may be used only when the callout is specifically about:

- plant growth;
- viable biological conditions;
- botanical structure;
- successful cultivation.

### HHH

Default identity callout:

- left rule: Archive Amber;
- pale field: Archive Field;
- text: Mission Ink.

Record Cyan may be used when the callout is specifically about:

- verification;
- linked records;
- source comparison;
- scientific continuity.

## 31.4 Semantic Callouts

Semantic callouts use explicit labels and icons when appropriate.

| Type | Rule color | Required label |
|---|---|---|
| Critical | Critical Red | Critical, Error, or Do Not |
| Caution | Caution Amber | Caution |
| Confirmed | Success Green | Confirmed |
| Information | Information Cyan | Information or Note |
| Fiction boundary | Technical Slate or documented special token | Fictional Context |
| Source uncertainty | Technical Slate or Archive Amber | Uncertain, Debated, or Incomplete |

Color alone must not define the callout.

## 31.5 Callout Length

Preferred callout length:

- title: 1 line;
- body: 1–4 short sentences;
- lists: no more than 4 items unless the callout is a dedicated procedure.

Long content should become a normal section rather than an oversized callout.

## 31.6 Nested Components

Do not place:

- a callout inside another callout;
- a response box inside an ordinary callout;
- a full data table inside a small callout;
- several adjacent callouts with no ordinary content between them.

---

# 32. Response-Area System

## 32.1 Approved Default

The ordinary written-response component uses:

1. a prompt above the box;
2. optional concise response guidance;
3. a blank bordered response box.

The response box is:

- white;
- blank;
- unruled;
- rectangular;
- clearly bordered;
- subtly rounded at 3 px;
- sized to the expected response.

## 32.2 Prompt Treatment

The prompt uses Inter at ordinary body or direction size.

It should:

- state one clear task;
- specify evidence or reasoning expectations;
- avoid combining several unrelated questions;
- remain outside the writing area.

## 32.3 Response Guidance

Optional guidance may state:

- expected sentence count;
- number of evidence sources;
- required diagram labels;
- response type;
- whether the task is ungraded or optional.

Examples:

```text
ONE OR TWO SENTENCES
```

```text
CITE AT LEAST TWO SOURCES
```

```text
LABEL ROOT, STEM, AND DIRECTIONAL CUE
```

Guidance uses JetBrains Mono in Technical Slate and remains subordinate to the prompt.

## 32.4 Size Families

Use the smallest box that reasonably supports the required response.

| Family | Typical use | Approximate print height |
|---|---|---:|
| Micro | one term, number, or short phrase | 0.25–0.35 in |
| Short | 1–2 sentences | 0.55–0.75 in |
| Medium | 2–4 sentences | 0.9–1.25 in |
| Tall | compact CER reasoning, explanation, or design response | 1.4–2.0 in |
| Extended | synthesis or formal reflection | 2.25 in or more |

Extended boxes may require a dedicated page or continuation page.

## 32.5 Drawing and Annotation Areas

A drawing area may use the same outer geometry as a response box but must be labeled for its intended use.

Permitted additions include:

- a light coordinate grid;
- a diagram frame;
- a provided base figure;
- a map boundary;
- a graph axis;
- a scale or legend zone.

Do not add notebook lines to drawing or written response areas.

## 32.6 Digital Fillable Areas

Fillable HTML response areas should:

- preserve the printed box dimensions;
- use transparent or white input backgrounds;
- use Inter;
- maintain visible focus indication;
- expand only when the template permits page reflow;
- avoid silently uploading student content.

## 32.7 Numbered Responses

Numbered response panels may be used for:

- multi-step assessments;
- repeated evidence questions;
- formal worksheets requiring clear item numbering.

They are not the default ordinary response treatment because the colored number block adds visual weight.

## 32.8 Prohibited Response Treatments

Do not use:

- ruled notebook lines;
- dotted handwriting lines;
- decorative parchment;
- speech bubbles;
- dialogue boxes;
- gradient fills;
- character portraits attached to answer areas;
- icons repeated inside blank writing space.

---

# 33. Table System

## 33.1 Approved Default

The ordinary student table is a **Ruled Technical Table**.

It uses:

- a full visible grid;
- Cool Panel header fill;
- Mission Ink header text;
- Instrument Gray borders;
- Inter body text;
- JetBrains Mono only where fixed-width data benefits;
- 3 px outer rounding only where technically practical.

The table remains grayscale-first.

## 33.2 Appropriate Uses

Use tables for:

- evidence matrices;
- source comparisons;
- observations;
- data readings;
- cause/effect relationships;
- design constraints;
- vocabulary comparisons;
- teacher procedures;
- rubric criteria.

Do not use a table when a short list or sentence communicates the information more clearly.

## 33.3 Student Handwriting Tables

Student-facing tables must provide:

- sufficient row height;
- clear column boundaries;
- prompts or labels that fit without crowding;
- adequate writing width;
- no essential distinction based on fill color alone.

Do not use minimal horizontal-rule tables for handwritten evidence collection.

## 33.4 Header Treatment

Ordinary table headers use:

- Cool Panel;
- Mission Ink;
- 7.5–9 pt label text;
- short labels;
- left alignment by default.

Institutional color may appear in:

- the table title;
- a technical label above the table;
- a narrow category marker.

Do not fill ordinary student table headers with saturated institutional color by default.

## 33.5 Row Treatment

Default rows remain white.

Very light alternating rows may be used for:

- teacher reference tables;
- long digital tables;
- dense answer keys.

Alternating fills must not be required to track rows after photocopying.

## 33.6 Numeric Alignment

- align text labels left;
- align comparable numerical data consistently;
- use tabular numerals;
- include units in headers where possible;
- do not repeat units in every cell when one column header suffices.

## 33.7 Table Borders

Preferred border hierarchy:

- outer border: 1–1.25 pt;
- header separation: 1 pt;
- internal cells: 0.5–0.75 pt.

Cell borders must survive classroom printing.

## 33.8 Wide Tables

When a table cannot fit legibly:

1. shorten labels;
2. restructure into grouped sections;
3. move explanatory prose outside the table;
4. split the table;
5. use an approved landscape page;
6. reduce type only as a last resort.

Do not compress an unreadable table into portrait format merely to avoid a page change.

## 33.9 Rubric Exception

Formal rubrics may use:

- smaller approved table text;
- denser cell padding;
- repeated header rows;
- landscape orientation.

Rubrics must still meet readability and grayscale standards.

---

# 34. Teacher-Note System

## 34.1 Approved Default

Teacher notes use a **Neutral Side Stripe**.

They include:

- a Technical Slate side rule;
- Cool Wash or white background;
- a short JetBrains Mono label;
- concise Inter body text;
- 3 px technical rounding.

## 34.2 Neutrality Rule

Teacher notes normally use neutral grayscale rather than SSS or HHH identity colors.

This keeps them visually separate from:

- student callouts;
- institutional identity;
- science/history focus boxes;
- evidence content.

## 34.3 Appropriate Labels

Preferred labels include:

- Teacher Note
- Watch For
- Misconception
- Facilitation
- Timing
- Accessibility
- Differentiation
- Answer Guidance
- Technical Fallback
- Source Boundary

## 34.4 Appropriate Uses

Teacher notes may contain:

- likely misconceptions;
- teacher prompts;
- timing adjustments;
- accessibility reminders;
- accepted response ranges;
- facilitation cautions;
- science/fiction boundaries;
- historical source limitations;
- technical fallback guidance.

## 34.5 Teacher-Only Visibility

In shared editable masters:

- teacher notes are hidden in student view;
- teacher notes appear in teacher and all-pages views;
- teacher notes never print in student packets;
- hidden teacher notes must not leave unexplained blank space in student output.

## 34.6 Answer Guidance

Model answers should not be presented as ordinary neutral teacher notes when a dedicated answer-key structure is more usable.

Use teacher notes for concise guidance, not for hiding a complete answer key throughout the student page.

---

# 35. Evidence-Layout Families

## 35.1 Functional Selection

Evidence layout is selected by the reasoning task, not by visual preference.

Several layout families are approved.

## 35.2 Evidence Matrix

Use when students must connect:

- source;
- observation;
- relevance;
- reliability;
- claim support.

Common columns:

```text
Evidence Source | Observation | Why It Matters
```

## 35.3 Matched Comparison

Use when students compare:

- two conditions;
- two sources;
- true and false records;
- competing explanations;
- before and after states;
- Earth and off-world systems.

Matched panels should use equal width and equivalent internal hierarchy.

## 35.4 Sequence or Timeline

Use when order is central:

- historical chronology;
- process stages;
- experimental sequence;
- evidence provenance;
- causal progression.

Time must proceed consistently, normally left to right or top to bottom.

## 35.5 Cause-and-Effect Chain

Use when students must connect:

```text
Condition → Mechanism → Observable Effect
```

Arrows and labels must remain interpretable in grayscale.

## 35.6 Systems Model

Use when the task requires:

- inputs;
- processes;
- outputs;
- feedback;
- interacting environmental variables;
- system boundaries.

Do not overload a systems model with decorative machinery.

## 35.7 Source-Provenance Relationship

Use when HHH students must trace:

- original source;
- copy;
- later interpretation;
- archive relationship;
- uncertainty;
- verification.

Connections should state the relationship rather than rely only on line color.

## 35.8 Design-Constraint Analysis

Use when students compare:

- criterion;
- constraint;
- proposed response;
- tradeoff;
- evidence.

## 35.9 Uncertainty Ranking

Use when evidence must be ordered by:

- confidence;
- reliability;
- explanatory power;
- remaining uncertainty.

The ranking scale must include text labels, not color alone.

## 35.10 Layout Consistency

All evidence layouts use the shared:

- typography;
- grayscale;
- technical labels;
- border weights;
- 3 px rounding;
- institutional accents;
- caption system.

The internal structure varies; the visual family does not.

---

# 36. Component Spacing and Combination

## 36.1 Vertical Spacing

Preferred spacing:

- label to heading: 0.05–0.08 in;
- heading to content: 0.06–0.10 in;
- prompt to guidance: 0.03–0.05 in;
- guidance to response box: 0.04–0.07 in;
- component to component: 0.12–0.20 in;
- major section break: 0.20–0.30 in.

## 36.2 Adjacent Components

Related components may sit side by side when:

- they have equivalent importance;
- their prompts remain readable;
- answer spaces remain adequate;
- the relationship is useful.

Do not place unrelated activities side by side merely to fill the grid.

## 36.3 Panel Competition

Avoid pages containing all of the following at once:

- multiple tinted callouts;
- several full-grid tables;
- repeated bordered teacher notes;
- numbered response panels;
- multiple figures.

When many strong components are required, distribute them across pages or reduce their visual intensity.

## 36.4 Repetition

Repeated components should use identical:

- labels;
- padding;
- borders;
- corner radius;
- heading placement;
- response guidance.

Do not redesign the same component within one packet.

---

# 37. Component Color and Grayscale Rules

## 37.1 Default Structure

Ordinary structure uses:

- Mission Ink;
- Technical Slate;
- Instrument Gray;
- Cool Panel;
- Cool Wash.

Institutional color identifies or emphasizes; it does not replace the grayscale hierarchy.

## 37.2 Grayscale Survival

Every component must retain:

- boundary;
- label;
- hierarchy;
- semantic meaning;
- writing-area visibility;

when printed in grayscale.

## 37.3 Photocopy Requirements

Photocopy testing must confirm:

- technical labels remain visible;
- pale callout fields do not erase the text or rule;
- response-box borders remain intact;
- table grids remain traceable;
- teacher side stripes remain distinct;
- 3 px corners do not create broken border artifacts.

## 37.4 Color-Only Prohibition

Do not use color alone to distinguish:

- student versus teacher content;
- caution versus identity;
- source reliability;
- correct versus incorrect;
- evidence categories;
- optional versus required.

Use explicit labels and structural differences.

---

# 38. Component HTML Tokens

Editable HTML masters should add these component tokens to the v0.4 page system.

```css
:root {
  /* Component geometry */
  --component-radius: 3px;
  --component-border: 0.75pt;
  --response-border: 1.1pt;
  --callout-rule: 3px;

  /* Component spacing */
  --component-space-small: 0.06in;
  --component-space-medium: 0.12in;
  --component-space-large: 0.20in;

  /* Component surfaces */
  --teacher-note-rule: var(--muted);
  --teacher-note-fill: var(--panel-light);
}
```

## 38.1 Technical Label

```css
.technical-label {
  display: inline-block;
  border: 0.75pt solid var(--institution-primary);
  border-radius: var(--component-radius);
  padding: 0.03in 0.06in;
  color: var(--institution-primary);
  font-family: var(--font-technical);
  font-size: 8pt;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
```

## 38.2 Priority Callout

```css
.callout {
  border-left: var(--callout-rule) solid var(--institution-primary);
  border-radius: var(--component-radius);
  background: var(--institution-soft);
  padding: 0.08in 0.10in;
}
```

## 38.3 Response Area

```css
.response-box {
  min-height: var(--response-height, 0.75in);
  border: var(--response-border) solid var(--ink);
  border-radius: var(--component-radius);
  background: var(--paper);
}
```

## 38.4 Technical Table

```css
.technical-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  border: 1pt solid var(--rule);
  border-radius: var(--component-radius);
  overflow: hidden;
}

.technical-table th,
.technical-table td {
  border-right: 0.5pt solid var(--rule);
  border-bottom: 0.5pt solid var(--rule);
  padding: 0.05in 0.06in;
}

.technical-table th {
  background: var(--panel);
  color: var(--ink);
}
```

## 38.5 Teacher Note

```css
.teacher-note {
  border-left: 3px solid var(--teacher-note-rule);
  border-radius: var(--component-radius);
  background: var(--teacher-note-fill);
  padding: 0.08in 0.10in;
}
```

Exact implementation may vary when browser table border behavior requires square internal cells. The visible result, not one particular CSS technique, controls.

---

# 39. Component Quality-Control Checklist

A page passes the v0.5 component review when all applicable answers are **yes**.

## 39.1 Section Headings

- [ ] Ordinary sections use the Technical Label Heading where useful.
- [ ] Labels are short and functional.
- [ ] Students can understand the heading without interpreting fictional language.
- [ ] Labels do not use arbitrary serial numbers.
- [ ] Long-form formal sections may use the approved plain-heading exception.

## 39.2 Callouts

- [ ] Callouts are reserved for priority content.
- [ ] The default uses a left rule and pale field.
- [ ] The title states the callout purpose.
- [ ] Semantic callouts include explicit labels.
- [ ] Callouts are not nested.
- [ ] The page is not dominated by adjacent callouts.

## 39.3 Response Areas

- [ ] The prompt appears above the box.
- [ ] The response area is blank and unruled.
- [ ] Guidance is concise and subordinate.
- [ ] The box size matches the expected response.
- [ ] The border survives grayscale and photocopying.
- [ ] No decorative content appears inside the writing space.

## 39.4 Tables

- [ ] Ordinary student tables use the ruled technical treatment.
- [ ] Headers remain grayscale-first.
- [ ] Cells provide adequate writing space.
- [ ] Borders remain visible in print.
- [ ] Units and labels are consistent.
- [ ] An alternate layout was considered before shrinking an oversized table.

## 39.5 Teacher Notes

- [ ] Teacher notes use the neutral side stripe.
- [ ] Labels identify the note's purpose.
- [ ] Teacher notes are hidden from student output.
- [ ] Notes do not compete with institutional callouts.
- [ ] Full answer keys are not fragmented into repeated small notes.

## 39.6 Geometry

- [ ] Ordinary component rounding is 3 px.
- [ ] Large app-style radii are absent.
- [ ] Table alignment is not weakened by inconsistent rounding.
- [ ] Repeated components use identical geometry.

## 39.7 Evidence Structures

- [ ] The layout matches the reasoning task.
- [ ] Labels explain relationships directly.
- [ ] Meaning survives grayscale.
- [ ] The structure follows the shared component family.
- [ ] The activity is not a generic clue-transcription log.

---

# 40. Explanatory-Visual Principles

## 40.1 Function Before Atmosphere

Every explanatory visual must primarily:

- explain a mechanism;
- organize evidence;
- compare conditions;
- show chronology;
- locate an event;
- display data;
- trace provenance;
- communicate uncertainty;
- distinguish observed from inferred information.

A figure must not exist merely to make a page look scientific, historical, or futuristic.

## 40.2 Shared Visual Family

SSS and HHH use the same explanatory-visual grammar:

- direct labels;
- restrained line hierarchy;
- orthogonal connectors;
- one instructional accent;
- technical frames;
- caption metadata bands;
- explicit source status;
- grayscale-independent meaning.

They differ through:

- institutional accent;
- subject matter;
- terminology;
- map, timeline, scientific, or archival content.

## 40.3 Flat Clarity

Prefer:

- flat schematics;
- clean orthographic views;
- direct comparisons;
- simplified cutaways;
- controlled cross sections;
- clearly aligned timelines and graphs.

Avoid perspective, decorative depth, or simulated interfaces when they reduce explanatory clarity.

## 40.4 Visual Accuracy

A figure must distinguish:

- measured or observed;
- documented;
- inferred;
- modeled;
- reconstructed;
- uncertain;
- hypothetical;
- fictional.

The guide's style may simplify appearance. It must not simplify away the status of the evidence.

---

# 41. Label System

## 41.1 Approved Default

Use **direct labels** by default.

Place the label:

- beside the object;
- beside the line;
- within an open region;
- at the end of a data series;
- near the relevant event;
- beside the source relationship.

The reader should not need to repeatedly move between a figure and a distant legend.

## 41.2 Direct-Label Requirements

Direct labels must:

- avoid covering essential content;
- use short wording;
- remain horizontal when practical;
- use consistent terminology;
- remain readable in grayscale;
- connect clearly to the labeled feature.

## 41.3 Leader Lines

Leader lines use the secondary neutral line weight.

They should:

- begin close to the feature;
- end close to the label;
- avoid crossing;
- avoid acute angles;
- avoid decorative curves;
- remain visually lighter than the object they identify.

## 41.4 Numbered-Key Exception

A numbered key may be used when:

- the figure contains many small parts;
- direct labels would overlap;
- labels would obscure a photograph or scan;
- a repeated image must stay compact;
- tactile or accessibility adaptation benefits from ordered annotation.

Number markers must:

- follow one sequence;
- use legible numerals;
- remain consistent in size;
- connect to a clearly ordered key.

## 41.5 Hybrid Labels

A hybrid system may:

- directly label major structures;
- number secondary structures;
- directly label data series;
- use a key for technical details.

Hybrid figures should not create two competing label hierarchies.

## 41.6 Label Typography

Preferred figure labels:

- Inter;
- 8–10 pt in print;
- 400–600 weight;
- Mission Ink;
- white or pale field only when required for separation.

Technical metadata inside figures may use JetBrains Mono at 7–9 pt.

---

# 42. Line Hierarchy

## 42.1 Approved System

Use:

1. primary neutral line;
2. secondary neutral line;
3. one instructional accent line.

## 42.2 Primary Neutral Line

Use Mission Ink for:

- major structure;
- system boundaries;
- primary anatomy;
- axes;
- confirmed routes;
- document outlines;
- key object silhouettes.

Preferred print weight:

- 1.25–1.75 pt.

## 42.3 Secondary Neutral Line

Use Technical Slate or Instrument Gray for:

- leader lines;
- construction guides;
- minor internal structures;
- grid lines;
- reference boundaries;
- secondary context;
- uncertain supporting geometry.

Preferred print weight:

- 0.6–1 pt.

## 42.4 Instructional Accent

Use the institutional primary accent for:

- the variable being taught;
- the active pathway;
- the critical comparison;
- the selected series;
- the emphasized region;
- the focus event.

Accent must reinforce a label, line style, shape, or position.

## 42.5 Expanded Color Prohibition

Do not create multi-color diagrams simply because several variables exist.

When categories must differ, prefer:

- direct labels;
- shape;
- line style;
- pattern;
- position;
- border style.

Color remains supplemental.

## 42.6 Internal Consistency

Within one figure:

- equivalent objects use equivalent line weights;
- one relationship type uses one line style;
- one category uses one marker shape;
- one uncertainty level uses one treatment.

Do not change line meaning midway through a figure.

---

# 43. Connectors and Arrows

## 43.1 Approved Default

Use **orthogonal connectors** as the ordinary default for:

- system diagrams;
- cause-and-effect chains;
- process flows;
- provenance diagrams;
- source relationships;
- engineering pathways;
- policy relationships.

Orthogonal connectors use horizontal and vertical segments with right-angle turns.

## 43.2 Arrowhead

The default arrowhead is a compact filled triangle.

It must:

- remain visible at ordinary print size;
- not overpower the line;
- align cleanly with the path;
- clearly indicate direction.

## 43.3 Connector Routing

Orthogonal connectors should:

- leave objects from a clear side;
- use as few turns as possible;
- avoid crossing objects;
- avoid crossing labels;
- align to the page or figure grid;
- keep parallel relationships evenly spaced.

## 43.4 Relationship Labels

When the connection itself carries meaning, label it.

Examples:

- influences;
- causes;
- copied from;
- cited by;
- translated from;
- derived from;
- amended by;
- moves toward;
- transfers;
- blocks;
- increases;
- decreases;
- supports;
- contradicts.

Do not let every arrow imply an unspecified relationship.

## 43.5 Connector Exceptions

Curved connectors may be used when:

- showing orbit;
- showing circulation;
- showing a biological pathway;
- distinguishing a feedback loop;
- avoiding unavoidable overlap.

Straight connectors may be used for:

- simple timelines;
- direct measurement;
- leader lines;
- graph series.

Orthogonal is the ordinary relationship default, not a rule that every line in every visual must turn at right angles.

## 43.6 Bidirectional Relationships

Use a double arrow only when the relationship is genuinely bidirectional.

Feedback loops should state the feedback relationship explicitly.

## 43.7 No-Direction Relationships

Use a line without an arrowhead when showing:

- association;
- alignment;
- shared provenance;
- comparison;
- boundary;
- correspondence.

---

# 44. Figure Framing

## 44.1 Approved Default

Ordinary figures use a **Thin Technical Frame**.

The frame provides:

- a printable boundary;
- separation from surrounding text;
- a stable annotation area;
- consistent figure geometry;
- reliable placement in the modular grid.

## 44.2 Frame Treatment

Use:

- 0.75–1 pt Instrument Gray border;
- 3 px technical radius;
- white background;
- internal padding;
- no decorative shadow;
- no double ornamental border.

## 44.3 Appropriate Uses

Use the standard frame for:

- diagrams;
- graphs;
- timelines;
- maps;
- provenance figures;
- sourced screenshots;
- archive scans;
- student annotation figures;
- comparative illustrations.

## 44.4 Open-Figure Exception

An open figure may be used when:

- it consists of a single simple object;
- its edges are obvious;
- the caption directly follows it;
- a frame would add unnecessary visual weight;
- the figure is integrated into nearby text.

## 44.5 Pale-Field Exception

A pale figure field may be used for:

- dense multi-layer diagrams;
- white objects that need separation;
- grouped maps or scans;
- digital-only interactive visuals.

Pale fields must remain visible but restrained in grayscale.

## 44.6 Figure Padding

Provide sufficient internal padding for:

- labels;
- arrowheads;
- legends;
- scale bars;
- map keys;
- annotation.

Nothing should appear accidentally clipped against the frame.

---

# 45. Figure Captions and Metadata Bands

## 45.1 Approved Default

Use a **Caption Metadata Band** beneath the figure.

The band contains:

1. figure number and descriptive caption;
2. source-status metadata;
3. source or attribution;
4. scale or reconstruction notice when required.

## 45.2 Visual Treatment

The metadata band uses:

- Cool Wash or white field;
- 0.75–1 pt border;
- 3 px technical radius;
- Inter for the descriptive caption;
- JetBrains Mono for source metadata;
- Mission Ink and Technical Slate;
- no saturated background.

## 45.3 Caption Anatomy

Example:

```text
Figure 3. Root orientation under two directional-cue conditions.

SOURCE STATUS · CURRICULUM-ORIGINAL SCHEMATIC
ADAPTED FROM · SOURCE NAME
NOT TO SCALE
```

## 45.4 Caption Writing

A caption should state:

- what is shown;
- what comparison or relationship matters;
- what the reader should notice when necessary.

A caption should not merely repeat the figure title.

## 45.5 Figure Numbering

Number figures sequentially within:

- one document;
- one packet;
- one controlled lesson package.

Use:

```text
Figure 1
Figure 2
Figure 3
```

Do not restart numbering on every page unless each page is a fully independent document.

## 45.6 Table Numbering

Number formal reference tables when cross-references require it.

Student activity tables do not need numbers when the heading already identifies them clearly.

## 45.7 Source Metadata

Use a short technical line.

Examples:

```text
SOURCE STATUS · CURRICULUM-ORIGINAL FIGURE
```

```text
ADAPTED FROM · NASA · PLANT GRAVITY PERCEPTION
```

```text
REPRODUCED FROM · PUBLIC-DOMAIN ARCHIVE
```

```text
RECONSTRUCTION · BASED ON SOURCES A–C
```

```text
FICTIONAL VISUALIZATION · GAME SETTING
```

---

# 46. Source-Status Vocabulary

## 46.1 Approved Terms

Use the following controlled terms accurately.

### Curriculum-Original Figure

Created specifically for the curriculum.

### Adapted From

Redrawn, simplified, reorganized, recolored, cropped, or otherwise altered from a source.

### Reproduced From

Shown substantially as the source published it.

### Schematic

Simplified to explain structure or relationship.

### Reconstruction

Represents a past system, object, event, or state based on evidence.

### Model Output

Generated from a stated computational, statistical, physical, or conceptual model.

### Illustrative Data

Values are examples and are not presented as measured lesson evidence.

### Not to Scale

Sizes, distances, or proportions are intentionally nonliteral.

### Fictional Visualization

Represents a fictional organism, device, environment, or event.

### Student-Created Figure

Produced by a learner.

### Source Unknown

The original source cannot be established.

### Attribution Disputed

The source or authorship is contested.

## 46.2 Multiple Status Terms

A figure may require more than one term.

Example:

```text
CURRICULUM-ORIGINAL SCHEMATIC · FICTIONAL VISUALIZATION · NOT TO SCALE
```

## 46.3 Status Accuracy

Do not label a redraw “original” merely because it was newly rendered.

Do not label a reconstruction as direct evidence.

Do not label fictional game art as a scientific diagram of Earth biology.

---

# 47. Evidence Status and Uncertainty

## 47.1 Required Explicitness

Figures containing multiple evidence states must state them in a key or direct labels.

The v0.6 convention is:

| Status | Default line treatment |
|---|---|
| Observed or documented | Solid |
| Inferred, modeled, reconstructed, or uncertain | Dashed |
| Fictional or hypothetical visualization | Dotted |

## 47.2 Text Required

Line style must always be paired with:

- direct text;
- legend;
- caption;
- source-status line.

## 47.3 Pattern Treatment

Uncertain regions may use:

- diagonal hatch;
- coarse dot pattern;
- dashed boundary;
- lighter neutral fill.

Do not use blur, glow, or transparency as the only uncertainty cue.

## 47.4 Confidence Levels

When several confidence levels matter, use clear wording:

- High confidence
- Moderate confidence
- Low confidence
- Unknown
- Disputed

Do not invent numerical confidence values without evidence.

## 47.5 Fiction Boundary

Fictional elements should be labeled at the figure level or component level.

Do not mark every fictional line individually if one clear status band covers the whole figure.

---

# 48. Scientific Mechanism Diagrams

## 48.1 Required Elements

A scientific mechanism figure should identify:

- system or organism;
- input or condition;
- mechanism;
- response;
- observable effect;
- evidence status;
- direction of influence;
- scale status.

## 48.2 Preferred Structure

Use a clear flow such as:

```text
Condition → Biological or Physical Mechanism → Observable Pattern
```

Orthogonal connectors should carry relationship labels when the verb matters.

## 48.3 System Boundary

Show the system boundary when:

- inputs and outputs matter;
- several environmental variables interact;
- a feedback loop exists;
- an engineering intervention changes the system.

## 48.4 Anatomy

Scientific anatomy should be:

- simplified but recognizable;
- labeled directly;
- proportionally honest where relevant;
- marked “not to scale” where simplified;
- free of decorative texture that obscures structure.

## 48.5 Cross Sections and Cutaways

Use cross sections when internal structure matters.

Include:

- cut-plane indication when useful;
- labels;
- orientation;
- scale or not-to-scale notice;
- material differentiation through pattern or label.

## 48.6 Cause and Correlation

Arrows must not imply causation unless the curriculum can support a causal relationship.

Use wording such as:

- associated with;
- observed alongside;
- may influence;
- proposed mechanism;
- supported explanation;

when causal certainty is limited.

## 48.7 Fictional Biology

Fictional organisms or technologies may appear in mechanism figures when clearly labeled.

The figure must distinguish:

- established principle;
- plausible extrapolation;
- fictional system.

---

# 49. Systems Diagrams

## 49.1 Appropriate Uses

Use systems diagrams for:

- growth environments;
- water delivery;
- nutrient flow;
- light systems;
- heat exchange;
- sensor networks;
- agricultural infrastructure;
- historical water-management systems;
- food-distribution systems.

## 49.2 Node Types

Nodes may represent:

- source;
- process;
- storage;
- organism;
- environment;
- decision;
- record;
- output.

Node labels should use nouns.

Connector labels should use verbs or relationships.

## 49.3 Inputs and Outputs

Inputs and outputs should align consistently.

Do not scatter them randomly around a system.

## 49.4 Feedback

Feedback loops must:

- use explicit direction;
- state whether feedback is positive, negative, stabilizing, or reinforcing when relevant;
- avoid circular arrows with no explanation.

## 49.5 System Density

When a system contains too many parts:

- divide into layers;
- create an overview and detail figure;
- group nodes;
- use a numbered key;
- move nonessential detail to a teacher figure.

Do not shrink the entire system until labels become unreadable.

---

# 50. Timelines

## 50.1 Direction

Time moves consistently:

- left to right; or
- top to bottom.

Do not switch direction within one timeline.

## 50.2 Date Alignment

Dates must align to one clear axis.

Distinguish:

- event date;
- source date;
- publication date;
- reconstruction date.

## 50.3 Event Types

Equivalent event types use equivalent geometry.

Possible categories include:

- agricultural event;
- environmental event;
- document creation;
- later interpretation;
- policy decision;
- technological change.

Use labels and shapes, not color alone.

## 50.4 Uncertain Dates

Use:

- approximate labels;
- range bars;
- dashed boundary;
- `c.` for circa where appropriate;
- explicit uncertainty notes.

Do not place an uncertain event at a precise point without qualification.

## 50.5 Timeline Breaks

A compressed or broken timescale must be clearly marked.

Do not imply equal time intervals when the timeline is not proportional.

## 50.6 Source Relationship

A timeline does not automatically establish provenance.

When source relationships matter, add a provenance diagram or explicit connection labels.

---

# 51. Provenance Diagrams

## 51.1 Purpose

Use provenance diagrams to show how one record relates to another.

## 51.2 Relationship Labels

Approved examples:

- copied from;
- cited by;
- translated from;
- summarized by;
- amended by;
- derived from;
- preserved in;
- disputed attribution;
- later interpretation;
- corroborated by;
- contradicted by.

## 51.3 Source Nodes

Each source node should identify:

- source type;
- date or period;
- creator or institution when known;
- archive or record identifier when useful;
- evidence status.

## 51.4 Original Versus Copy

Do not visually imply that a copy is identical to an original unless verified.

Use:

- amendment mark;
- missing-section note;
- uncertainty label;
- relationship description.

## 51.5 Direction

Connectors should ordinarily flow from earlier source to later derivative.

A separate line may show later verification of an earlier source.

## 51.6 Disputed Provenance

Disputed relationships use:

- dashed connector;
- explicit `DISPUTED` label;
- caption note;
- source-status explanation.

---

# 52. Maps

## 52.1 Sourced Geometry Requirement

Every production geographic map must use sourced geographic geometry.

Do not invent:

- coastlines;
- rivers;
- borders;
- region outlines;
- routes;
- city locations;
- territorial extents.

## 52.2 Source Identification

Map metadata must identify:

- geometry source;
- data source;
- represented date or period;
- projection where relevant;
- adaptation or reconstruction status.

## 52.3 Context

Show enough surrounding geography to understand:

- location;
- movement;
- neighboring regions;
- water systems;
- environmental context.

Do not crop so tightly that the highlighted feature loses geographic meaning.

## 52.4 Map Layers

Possible layers include:

- base geography;
- political or administrative boundary;
- agricultural region;
- route;
- site;
- river or water system;
- uncertainty;
- reconstructed extent.

Each layer must have a direct label or legend entry.

## 52.5 Historical Boundaries

Historical boundaries must:

- identify the represented period;
- distinguish direct control, influence, uncertainty, or source-reported extent when the source permits;
- avoid implying modern borders existed in the past;
- retain a source note.

## 52.6 Routes and Movement

Routes should:

- use directional arrows only when movement direction is known;
- state whether the route is documented, inferred, or illustrative;
- avoid false precision;
- identify start and end points.

## 52.7 Scale, North, and Projection

Include a scale bar, north arrow, or projection only when useful and accurate.

Do not add cartographic decorations automatically.

## 52.8 Schematic Maps

A schematic spatial diagram may be used when geography is not the subject.

It must be labeled:

```text
SCHEMATIC · NOT A GEOGRAPHIC MAP
```

---

# 53. Graphs and Quantitative Figures

## 53.1 Required Elements

Graphs must include:

- descriptive title or caption;
- labeled axes;
- units;
- readable ticks;
- source status;
- grayscale-independent series encoding;
- direct labels where practical.

## 53.2 Approved Series Encoding

Use a combination of:

- direct labels;
- circle, square, triangle, or other distinct markers;
- solid, dashed, and dotted lines;
- fill pattern;
- line weight;
- position.

Color may reinforce one selected or institutional series.

## 53.3 Direct Series Labels

Place labels near the end of each series when space allows.

Do not require the reader to repeatedly compare a distant legend.

## 53.4 Legend Exception

Use a legend when:

- many series exist;
- direct labels overlap;
- categories repeat across several charts;
- the same encoding appears throughout a packet.

## 53.5 Axes

Axes use the primary neutral line.

Grid lines use the secondary neutral line and remain visually subordinate.

## 53.6 Units

Place units:

- in the axis title;
- in the column or row label;
- in the measure label.

Do not rely on a caption alone for units.

## 53.7 Baselines

Use a zero baseline when the chart type or comparison requires it.

A truncated axis must be clearly indicated and justified.

## 53.8 Data Status

Label data as:

- measured;
- reported;
- modeled;
- reconstructed;
- estimated;
- illustrative.

Do not use decorative placeholder data in published lesson materials.

## 53.9 Uncertainty

Show uncertainty when supported through:

- error bars;
- range bands;
- confidence intervals;
- multiple-source range;
- explicit uncertainty notes.

Do not manufacture uncertainty graphics without source support.

## 53.10 Student Graphing Areas

Blank graph areas must include:

- clear axes;
- room for labels;
- appropriate grid;
- scale guidance when required;
- enough space for handwriting.

Do not preselect a misleading scale.

---

# 54. Legends and Keys

## 54.1 When Required

Use a legend or key when:

- direct labels are impossible;
- patterns require explanation;
- evidence status varies;
- a map contains several layers;
- many data series appear;
- numbered annotations are used.

## 54.2 Placement

Place the key:

- within unused figure space;
- directly beneath the figure;
- beside the figure when the grid permits.

Do not separate the key onto another page.

## 54.3 Order

Order legend entries by:

- visual prominence;
- figure reading order;
- chronology;
- category hierarchy.

## 54.4 Key Language

Use explicit labels.

Avoid vague entries such as:

- Type A;
- Other;
- Unknown line;
- Special area;

unless those are genuine defined categories.

---

# 55. Captions, Attribution, and Rights

## 55.1 Attribution Content

Attribution should include as applicable:

- creator;
- organization;
- title;
- year;
- archive;
- license;
- public-domain status;
- source identifier;
- URL in teacher or source documentation.

## 55.2 Student-Facing Attribution

Student pages may use a concise source line.

Teacher materials and references must retain full source information.

## 55.3 Adaptations

When adapting a source, identify the nature of the adaptation when useful:

- simplified;
- cropped;
- relabeled;
- redrawn;
- combined;
- recolored;
- translated;
- not to scale.

## 55.4 Public-Domain Status

Do not claim public-domain status without confirming it.

## 55.5 Game Assets

Game-derived figures must state:

```text
SOURCE · SPACE SPROUT SLEUTH GAME ASSET
```

or:

```text
SOURCE · HUNGER, HARVEST, & HISTORY GAME ASSET
```

when direct reuse is approved.

A later revision will define the complete game-asset reuse system.

---

# 56. Figure Accessibility

## 56.1 Alt Text

Digital figures require alt text that states:

- figure purpose;
- key structure;
- principal comparison;
- essential conclusion;
- uncertainty where relevant.

Do not simply repeat the caption if it does not describe the visual relationships.

## 56.2 Reading Order

Labels, captions, and source notes must appear in a logical DOM reading order.

## 56.3 Color Independence

Every essential distinction uses at least one non-color cue.

## 56.4 Text Size

Figure labels must remain legible at ordinary browser zoom and standard print output.

## 56.5 Complex Figures

Complex digital figures should include:

- concise alt text;
- extended description;
- accessible data table when quantitative;
- plain-text chronology when timeline-based.

---

# 57. Figure HTML and SVG Tokens

Editable masters should add these tokens.

```css
:root {
  --figure-radius: 3px;
  --figure-border: 0.75pt solid var(--rule);
  --figure-padding: 0.12in;

  --figure-line-primary: 1.5pt;
  --figure-line-secondary: 0.75pt;
  --figure-line-accent: 1.75pt;

  --figure-caption-fill: var(--panel-light);
  --figure-caption-border: 0.75pt solid var(--rule);

  --figure-observed-style: solid;
  --figure-inferred-style: dashed;
  --figure-fictional-style: dotted;
}
```

## 57.1 Figure Shell

```css
.figure {
  border: var(--figure-border);
  border-radius: var(--figure-radius);
  background: var(--paper);
  padding: var(--figure-padding);
}
```

## 57.2 Caption Metadata Band

```css
.figure-caption-band {
  margin-top: 0.06in;
  border: var(--figure-caption-border);
  border-radius: var(--figure-radius);
  background: var(--figure-caption-fill);
  padding: 0.07in 0.08in;
}

.figure-caption {
  font-family: var(--font-body);
}

.figure-source-status {
  margin-top: 0.03in;
  color: var(--muted);
  font-family: var(--font-technical);
  font-size: 8pt;
}
```

## 57.3 SVG Classes

```css
.figure-primary {
  fill: none;
  stroke: var(--ink);
  stroke-width: var(--figure-line-primary);
}

.figure-secondary {
  fill: none;
  stroke: var(--muted);
  stroke-width: var(--figure-line-secondary);
}

.figure-accent {
  fill: none;
  stroke: var(--institution-primary);
  stroke-width: var(--figure-line-accent);
}

.figure-inferred {
  stroke-dasharray: 6 4;
}

.figure-fictional {
  stroke-dasharray: 1.5 3;
}
```

## 57.4 Orthogonal Connectors

Orthogonal connectors should normally be authored as SVG paths using horizontal and vertical segments.

The arrowhead must scale with the final rendered line.

---

# 58. Explanatory-Visual Quality-Control Checklist

A visual passes the v0.6 review when all applicable answers are **yes**.

## 58.1 Labels

- [ ] Major elements are directly labeled.
- [ ] Numbered keys are used only when crowding requires them.
- [ ] Labels do not overlap essential content.
- [ ] Terminology matches the lesson text.
- [ ] Leader lines do not cross unnecessarily.

## 58.2 Lines and Arrows

- [ ] Primary, secondary, and accent lines have distinct roles.
- [ ] Institutional color is limited to the instructional focus.
- [ ] Orthogonal connectors use few turns.
- [ ] Relationship arrows are labeled where meaning matters.
- [ ] Arrows do not imply unsupported causation.
- [ ] Bidirectional arrows represent genuine two-way relationships.

## 58.3 Figure Frame

- [ ] The ordinary figure uses a thin technical frame.
- [ ] The figure has adequate internal padding.
- [ ] Labels and arrowheads are not clipped.
- [ ] Open or pale-field exceptions are justified.
- [ ] No decorative shadow appears.

## 58.4 Caption and Source

- [ ] The figure has a number when cross-reference requires it.
- [ ] The caption explains what matters.
- [ ] The metadata band states source status.
- [ ] Attribution is accurate.
- [ ] Adaptation, reconstruction, fiction, or scale limitations are identified.

## 58.5 Status and Uncertainty

- [ ] Observed or documented content is identified.
- [ ] Inferred, modeled, reconstructed, or uncertain content is identified.
- [ ] Fictional content is identified.
- [ ] Line style is paired with text.
- [ ] Patterns remain legible in grayscale.

## 58.6 Scientific Figures

- [ ] System boundary is shown when relevant.
- [ ] Inputs, mechanism, and outputs are clear.
- [ ] Anatomy is simplified without becoming misleading.
- [ ] Scale status is stated.
- [ ] Fictional biology is separated from established science.

## 58.7 Timelines

- [ ] Time moves in one direction.
- [ ] Dates align consistently.
- [ ] Event date and source date are distinguished when necessary.
- [ ] Uncertain dates are qualified.
- [ ] Compressed time intervals are marked.

## 58.8 Provenance

- [ ] Each relationship is labeled.
- [ ] Originals, copies, and interpretations are distinguished.
- [ ] Disputed relationships use explicit uncertainty.
- [ ] Source nodes include useful identifying information.

## 58.9 Maps

- [ ] Geographic geometry is sourced.
- [ ] Represented period is identified.
- [ ] Surrounding context is sufficient.
- [ ] Reconstructed or uncertain extents are marked.
- [ ] Projection, scale, and north arrow are used only when accurate and useful.
- [ ] Schematic spatial diagrams are not presented as maps.

## 58.10 Graphs

- [ ] Axes and units are labeled.
- [ ] Data source status is identified.
- [ ] Series use shapes or line styles in addition to color.
- [ ] Direct labels are used where practical.
- [ ] Axis truncation is disclosed.
- [ ] Uncertainty is shown only when supported.
- [ ] Decorative data has not been fabricated.

## 58.11 Accessibility

- [ ] Alt text states the figure's essential purpose.
- [ ] Complex figures have an extended description or table where needed.
- [ ] Meaning survives grayscale.
- [ ] Labels remain legible at output size.
- [ ] DOM reading order is logical.

---

# 59. Deferred Specifications

The following items remain deliberately unresolved:

- final SAA insignia artwork;
- curriculum-ready TAA insignia adaptation;
- insignia clear-space and minimum-size rules;
- complete section-icon vocabulary;
- publication and status stamps;
- image, photograph, screenshot, and game-asset framing;
- cover and packet-opener design;
- assessment and rubric specializations;
- teacher-answer overlays;
- accessibility variants;
- final export and repository-production standards;
- completed grayscale, photocopy, and printer test results.

These items must be resolved before v1.0.

---

# 60. Decision Record

## 60.1 Decisions Carried Forward

| Decision | Approved result |
|---|---|
| Typography | Inter + JetBrains Mono |
| Shared grayscale | Cool Mission Gray |
| SSS palette | Orbital Cyan + Botanical Green |
| HHH palette | Archive Amber + Record Cyan |
| Icon treatment | Phosphor Regular at reinforced print weight |
| First-page header | Mission Title Block |
| Continuation header | Compact institutional continuation header |
| Underlying grid | 12-column modular grid |
| Universal default margins | 0.50 inches on every side |
| Default density | Balanced |
| Footer | Split publication-metadata rule |
| Section heading | Technical label heading |
| Callout | Left rule + pale field |
| Response area | Prompt above blank box |
| Table | Ruled technical table |
| Teacher note | Neutral side stripe |
| Corner geometry | 3 px technical rounding |

## 60.2 v0.6 Decisions

| Decision | Approved result |
|---|---|
| Label system | Direct labels |
| Line hierarchy | Two neutral weights + one accent |
| Connector and arrow style | Orthogonal connectors |
| Figure framing | Thin technical frame |
| Caption and source treatment | Caption metadata band |
| Graph differentiation | Direct labels + shapes + line styles |
| Evidence-status key | Shown when multiple statuses are present |
| Map geometry | Sourced geometry required |
| Source-status wording | Required |

The v0.6 decision note records that the grayscale preview was not viewed. Production grayscale and photocopy testing remains required before v1.0.

---

# 61. Version History

## v0.6

- Locked direct labels as the ordinary figure-labeling system.
- Defined numbered-key and hybrid-label exceptions.
- Locked two neutral line weights plus one instructional accent.
- Locked orthogonal connectors as the ordinary relationship and process default.
- Defined compact filled arrowheads and connector exceptions.
- Locked thin technical figure frames.
- Locked caption metadata bands.
- Defined controlled source-status vocabulary.
- Defined solid, dashed, and dotted evidence-status conventions.
- Defined scientific mechanism and system-diagram rules.
- Defined timeline rules.
- Defined provenance-diagram rules.
- Required sourced geometry for maps.
- Defined graph, data-series, axes, units, and uncertainty standards.
- Defined legends, captions, attribution, rights, and accessibility requirements.
- Added figure HTML and SVG tokens.
- Added a v0.6 explanatory-visual quality-control checklist.

## v0.5

- Locked Technical Label Headings as the ordinary section-heading system.
- Defined approved label content, size, color, and plain-heading exceptions.
- Locked left-rule pale-field callouts.
- Defined institutional and semantic callout variants.
- Locked prompt-above-box response areas.
- Defined response guidance and size families.
- Locked ruled grayscale-first technical tables.
- Defined student, teacher, rubric, and wide-table behavior.
- Locked neutral side-stripe teacher notes.
- Locked 3 px technical component rounding.
- Approved multiple evidence-layout families selected by instructional function.
- Defined component spacing, combination, grayscale, and photocopy rules.
- Added reusable component CSS tokens.
- Added a v0.5 component quality-control checklist.

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
