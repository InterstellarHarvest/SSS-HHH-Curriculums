# VISUAL_STYLE_GUIDE_v1.0 — Post-Gallery Review Audit

## Review Basis

The v1.0 package was checked against the approved decisions carried through v0.9 and against the rendered SSS student and Teacher Quick Start screenshots.

## Findings

### 1. Reference template typography was undersized

The guide approved:

- 10.75 pt body;
- 9.5 pt table text;
- 15 pt section headings;
- 22 pt page titles.

The original gallery used values such as 8–9 px body text and 7–7.5 px table text. Those values were substantially smaller than the approved print scale.

**Correction:** the gallery now uses point-equivalent CSS values for its 96 px/in US Letter page.

### 2. Student pages lacked a page-fill rule

The original gallery used fixed response heights and left avoidable space beneath the CER stack.

**Correction:** student pages now treat the printable body as flexible. CER boxes preserve minimum Claim / Evidence / Reasoning sizes and share surplus page height.

### 3. Teacher reference pages demonstrated excessive unused space

The original Teacher Quick Start omitted several items listed in the guide's own typical anatomy and declared `Page 1 of 2` despite a lightly used page.

**Correction:** the reference now includes purpose, materials, diagnosis, procedure, misconception, fallback, required artifacts, and a genuine teacher-notes area. It demonstrates a one-page quick start rather than padding or forcing a second page.

### 4. SSS / HHH differentiation was underdemonstrated

The guide already distinguished:

- SSS as operational and systems-oriented;
- HHH as archival and provenance-oriented.

The original gallery mostly demonstrated color and insignia changes.

**Correction:** the HHH reference now includes accession, period, region, record status, chronology, source excerpt, and provenance structures. The SSS reference retains mission, environment, mechanism, diagnosis, and CER structures.

### 5. Locked decisions remain consistent

The audit found no current-rule conflicts for:

- Mission Title Block;
- 0.50-inch margins;
- 12-column grid;
- three stacked CER boxes;
- every recurring standardized section using an icon;
- filled publication-status marks;
- term-definition vocabulary tables;
- analytic rubrics;
- dedicated answer keys;
- parallel accessible editions.

Occurrences of `placeholder` and `provisional` remain only in historical warnings, release blockers, or deprecation language.


### 6. Teacher notes row was implicitly auto-sized

The teacher template contained five grid rows, but the CSS declared only four. The Teacher Notes section therefore fell into an implicit auto-sized row and remained a narrow strip.

**Correction:** the teacher grid now declares five rows, with the final row defined as `minmax(150px, 1fr)`. The notes box also has a 150 px minimum, so it expands into the remaining printable area while remaining editable later.


### 7. Accessible response areas were still minimum-sized

The accessible reference increased type and minimum response height but did not allow the response sections to become the page's flexible rows.

**Correction:** the accessible page now uses a fixed US Letter body with a flex-column wrapper. Its Evidence and Claim sections occupy flexible grid rows with larger minimum heights and expand into the remaining printable body. The guide now explicitly states that accessible response containers have no arbitrary maximum height when larger space improves physical usability.

## Result

The revised v1.0 package is more faithful to its own approved typography, page-use, institutional-archetype, and production rules.

Physical printer and photocopy tests remain release activities for actual production templates.
