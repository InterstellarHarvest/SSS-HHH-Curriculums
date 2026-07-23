# VISUAL_STYLE_GUIDE_v0.4 — Decision Brief

> **Status:** Project-defining page-system checkpoint  
> **Purpose:** Select the shared page grid, document anatomy, header, footer, margin, and density rules that will govern SSS and HHH curriculum documents.

## Existing Repository Constraints

The current approved Curriculum Bible already establishes:

- US Letter pages at 8.5 × 11 inches;
- portrait orientation by default;
- 0.50-inch default margins for every document role;
- optional 0.65–0.75-inch margins only when a specific page requires additional readability;
- visible page boundaries and adjustable margins in HTML masters;
- student, teacher, answer-key, edit, and grayscale views;
- explicit overflow warnings;
- PDF as the official fixed release;
- one double-sided Letter sheet as the default student case packet.

The existing SSS Case 01 publishing master demonstrates that these mechanics work. It also reveals several visual-system problems that v0.4 should correct:

- the header depends on a game-art image rather than a controlled institution-mark area;
- page structure is mostly assembled from case-specific CSS rather than a documented shared grid;
- body, table, and metadata text are often smaller than the v0.3 typography standard;
- the page is visually dense enough that future cases could solve overflow by shrinking type;
- continuation-page identity is not yet formalized;
- version and compatibility metadata need a consistent shared footer architecture.

## Lead-Design Recommendation

### Underlying Grid

**12-column modular grid**

This provides one system that can produce:

- one-column prose;
- 7/5 evidence-and-figure pages;
- 8/4 teacher-reference pages;
- 6/6 comparisons;
- 4/4/4 metadata or option groups;
- full-width response and data areas.

A fixed two-column system is too restrictive across the required template families.

### Baseline Rhythm

**8-pixel digital baseline, translated to print spacing tokens**

The baseline should guide spacing rather than force every line of text onto a literal baseline grid. Use multiples of 4 and 8 pixels in HTML and approximately 0.04, 0.08, 0.12, 0.16, and 0.24 inches in print layouts.

### Header

**Identity Rail**

Use:

- a narrow institutional accent rail;
- a reserved insignia slot;
- curriculum and document title stack;
- compact publication metadata.

The first page receives the full identity header. Continuation pages receive a compact header containing the institutional abbreviation, document title, document code, and continuation label.

### Footer

**Split metadata rule**

Place:

- project, curriculum version, compatibility, and status on the left;
- page number and total page count on the right.

This is quiet enough for student pages and easy to scan in longer teacher packets.

### Margins

- Every document role defaults to **0.50 inches** on all sides.
- Wider 0.625–0.75-inch margins remain available only as page-specific exceptions when readability or binding requirements justify them.
- Switching document roles must never change a user-selected margin value.

### Density

**Balanced**

The default must fit the intended page count without dropping below the v0.3 minimum type sizes. Compact density is an exception for tables, rubrics, and controlled metadata—not a general page style.

### Page Anatomy

Every ordinary page should use:

1. institutional header;
2. title and publication metadata;
3. modular body grid;
4. controlled response, figure, data, or note components;
5. publication footer.

Do not repeat the full first-page masthead on every continuation page.

## Important Scope Boundary

The decision lab deliberately uses:

- a labeled circular **mark slot**, not an insignia concept;
- a labeled **approved figure or diagram** block, not a diagram style.

Do not judge insignia or diagram aesthetics from this checkpoint. Those systems will receive separate visual comparison files before they are locked.

## Decisions Required Before v0.4 Is Locked

- Header architecture
- Underlying page grid
- Student and teacher margin defaults
- Default information density
- Footer architecture
- First-page versus continuation-header behavior

Use `VISUAL_STYLE_GUIDE_v0.4_DECISION_LAB.html` to compare all four document roles in both SSS and HHH, including grayscale and grid overlays.

Export the active settings as `VISUAL_STYLE_GUIDE_v0.4_DECISIONS.md`.
