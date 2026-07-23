# VISUAL_STYLE_GUIDE_v0.6 — Decision Brief

> **Status:** Project-defining explanatory-visual checkpoint  
> **Purpose:** Select the shared visual language for scientific diagrams, systems models, historical timelines, provenance diagrams, data graphs, sourced maps, captions, and source-status distinctions.

## Existing Locked Standards

Versions 0.1–0.5 already require:

- professional, moderately immersive curriculum documents;
- grayscale-first production;
- Inter + JetBrains Mono;
- Cool Mission Gray;
- SSS Orbital Cyan + Botanical Green;
- HHH Archive Amber + Record Cyan;
- Phosphor icons at reinforced Regular weight;
- Mission Title Block first-page headers;
- compact continuation headers;
- a 12-column modular grid;
- 0.50-inch margins for every document role;
- Balanced information density;
- Technical Label Headings;
- left-rule pale-field callouts;
- prompt-above-box blank response areas;
- ruled technical tables;
- neutral side-stripe teacher notes;
- 3 px technical component rounding;
- diagrams prioritized over decoration.

Version 0.6 must define how explanatory visuals themselves are constructed.

## Project Needs Confirmed by the Game and Curriculum Sources

SSS requires visual structures for:

- environmental systems;
- cause and mechanism;
- plant orientation and response;
- spectral and sensor comparison;
- growth patterns;
- process sequences;
- engineering recommendations;
- interacting variables.

HHH requires visual structures for:

- chronology;
- provenance;
- primary and later records;
- conflicting accounts;
- geographic context;
- water and agricultural systems;
- source uncertainty;
- reconstructed versus documented information;
- quantitative historical comparison.

Both curricula require:

- data tables and graphs;
- captions;
- source attribution;
- original versus adapted figure labeling;
- grayscale-independent meaning;
- explicit science/fiction or documented/inferred boundaries.

## Lead-Design Recommendation

### Label System

**Direct labels**

Place terms beside the objects, paths, or regions they identify.

Use a numbered key only when:

- direct labels would overlap;
- a figure contains many small parts;
- a repeated visual requires compact annotation;
- accessibility improves through a structured key.

A hybrid figure may directly label major elements and number secondary details.

### Line Hierarchy

**Two neutral weights + one instructional accent**

Use:

- a heavier Mission Ink line for primary structure;
- a lighter Technical Slate line for construction, leaders, axes, and secondary context;
- one institutional accent for the variable, path, or relationship being taught.

Do not create rainbow diagrams.

### Connector and Arrow Style

**Compact filled arrow**

Use a small triangular head on a simple line.

Exceptions:

- orthogonal connectors for dense system diagrams;
- no arrowhead for undirected relationships;
- double arrows only when the relationship is genuinely bidirectional.

Open chevrons are less reliable at small print sizes.

### Figure Framing

**Open figure**

The ordinary figure sits directly on the page grid.

Use a thin technical frame when:

- a student must annotate inside the figure;
- the background would otherwise be ambiguous;
- a map, scan, screenshot, or reproduced image requires a boundary.

Use a pale field sparingly for especially complex figures.

### Caption and Source Treatment

**Stacked caption + source line**

Use:

```text
Figure 1. What the figure shows and why it matters.
SOURCE STATUS · ORIGINAL / ADAPTED / REPRODUCED / SCHEMATIC / RECONSTRUCTION / FICTIONAL · SOURCE
```

The caption uses Inter. The source-status line uses JetBrains Mono in Technical Slate.

### Data-Series Differentiation

**Direct labels + shapes + line styles**

Color may reinforce categories, but graphs must also use:

- direct labels;
- different marker shapes;
- solid, dashed, or dotted lines;
- patterns when fills are necessary.

Legends remain available when direct labeling is impractical.

### Status and Uncertainty

Use explicit labels plus stable line conventions:

- **solid:** observed, documented, or directly sourced;
- **dashed:** inferred, modeled, reconstructed, or uncertain;
- **dotted:** fictional visualization or hypothetical extension.

These meanings must be written in the figure or key. Line style alone is not sufficient.

## Scientific Diagram Requirements

Scientific figures should define:

- system boundary;
- primary structures;
- highlighted variable;
- direction of influence;
- mechanism;
- observed effect;
- inferred relationship;
- scale or “not to scale” status.

Avoid:

- decorative machinery;
- unlabeled arrows;
- complex perspective when a flat schematic is clearer;
- generic icons in place of meaningful anatomy;
- impossible precision.

## Timeline Requirements

Timelines should:

- move consistently left to right or top to bottom;
- align dates;
- distinguish event date from source date;
- label gaps and uncertainty;
- avoid decorative zigzags;
- use equal visual rules for equivalent events;
- distinguish a later interpretation from a contemporary record.

## Provenance Requirements

Provenance diagrams should state the relationship on each connection:

- copied from;
- cited by;
- translated from;
- derived from;
- amended by;
- later interpretation;
- disputed attribution.

Do not let every line imply the same relationship.

## Map Requirements

Production maps must:

- use sourced geographic geometry;
- identify the map source;
- state the represented period;
- preserve surrounding geographic context;
- label reconstructed or uncertain extents;
- distinguish locations, routes, regions, and boundaries;
- avoid invented coastlines or political borders;
- include scale, north arrow, or projection only when useful and accurate.

The decision lab's map tab is only an annotation-style test and is not geographic data.

## Graph Requirements

Graphs must include:

- descriptive title or caption;
- labeled axes;
- units;
- readable tick labels;
- source status;
- direct series labels where possible;
- grayscale-independent marks;
- zero baseline when the chart type requires it;
- uncertainty indication when supported by data.

Do not fabricate data merely to fill a graph-shaped activity.

## Caption and Source Vocabulary

Approved source-status terms should include:

- Curriculum-original figure
- Adapted from
- Reproduced from
- Schematic
- Reconstruction
- Model output
- Illustrative data
- Not to scale
- Fictional visualization
- Student-created figure
- Source unknown or disputed

These labels must be used accurately.

## Decisions Required Before v0.6 Is Locked

- default label system;
- line hierarchy;
- connector and arrow style;
- ordinary figure framing;
- caption and source treatment;
- graph/category differentiation;
- approval of stable observed, inferred/reconstructed, and fictional-status conventions.

Use `VISUAL_STYLE_GUIDE_v0.6_DECISION_LAB.html` to compare the system across mechanism, timeline, graph, map-treatment, and provenance examples in both SSS and HHH.

Export the active settings as `VISUAL_STYLE_GUIDE_v0.6_DECISIONS.md`.
