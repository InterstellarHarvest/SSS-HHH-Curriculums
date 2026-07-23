# VISUAL_STYLE_GUIDE_v0.5 — Decision Brief

> **Status:** Project-defining component-system checkpoint  
> **Purpose:** Select the reusable visual treatments for section headings, callouts, response areas, tables, teacher notes, and component geometry.

## Existing Locked Standards

Versions 0.1–0.4 already require:

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
- blank, unruled response boxes;
- split publication-metadata footers;
- selective panel use;
- diagrams over decoration.

Version 0.5 must convert those principles into a reusable component library.

## Lead-Design Recommendation

### Section Headings

**Rule heading**

Use a short heading and optional technical label above a thin rule.

This treatment:

- works in both curricula;
- aligns with technical-document conventions;
- creates hierarchy without adding another panel;
- survives grayscale and photocopying;
- scales from student pages to formal lesson plans.

### Callouts

**Left rule + pale field**

Use a narrow institutional or semantic rule with a pale field.

This treatment should be reserved for:

- science or history focus;
- evidence rules;
- cautions;
- important source-status explanations;
- concise priority information.

Do not use it for ordinary paragraphs.

### Response Areas

**Prompt above blank box**

Keep:

1. prompt;
2. optional short response guidance;
3. blank bordered writing area.

This is the clearest implementation of the already locked blank, unruled response-box standard.

### Tables

**Ruled technical table**

Use:

- full grid;
- cool-gray header;
- dark readable text;
- sufficient cell height for handwriting when student-facing.

Institutional accent may appear in a small label or heading, but ordinary table headers should remain grayscale-first.

### Teacher Notes

**Neutral side stripe**

Teacher notes should use neutral gray rather than SSS or HHH identity color by default.

This prevents:

- teacher guidance from competing with the institutional system;
- misconceptions from looking like student callouts;
- answer cues from becoming visually prominent in mixed teacher/student masters.

### Corner Geometry

**Sharp corners**

Sharp rectangular geometry best supports the NASA-inspired technical-document aesthetic.

A subtle 3 px radius may remain available for digital-only controls, but printed curriculum components should default to sharp corners.

## Evidence-Layout Families

Version 0.5 should approve multiple functional evidence structures rather than select one universal activity format.

Initial approved families:

- evidence matrix;
- matched comparison;
- sequence or timeline;
- cause-and-effect chain;
- systems model;
- source-provenance relationship;
- design-constraint analysis;
- uncertainty ranking.

The component styling should remain consistent while the internal structure changes according to instructional purpose.

## Component Principle

Do not convert the curriculum into a collection of cards.

The ordinary page should remain an open document surface with:

- section headings;
- rules;
- selective callouts;
- tables;
- response areas;
- figures;
- teacher notes only where needed.

## Decisions Required Before v0.5 Is Locked

- ordinary section-heading treatment;
- priority callout treatment;
- ordinary response-area treatment;
- ordinary student table treatment;
- teacher-note treatment;
- sharp versus subtly rounded print components;
- approval of multiple evidence-layout families.

Use `VISUAL_STYLE_GUIDE_v0.5_DECISION_LAB.html` to compare student and teacher contexts in both SSS and HHH.

Export the active settings as `VISUAL_STYLE_GUIDE_v0.5_DECISIONS.md`.
