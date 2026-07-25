# Mission Title and Continuation Header Parity — v1.0.3 Clarification

**Applies to:** SSS and HHH Student worksheets, Accessible editions, Teacher packets, Answer Keys, editable HTML masters, templates, published outputs, and validation harnesses  
**Status:** Approved production clarification  
**Effective with:** SSS Campaign 1, Case 02 — Lunar Greenhouse correction pass

## 1. Canonical structural precedent

The approved SSS Campaign 1 Case 01 v1.0 Mission Title Block and continuation-header anatomy are the production precedent for later SSS cases. Later cases replace case-specific text, role labels, status, and institutional variables; they do not invent a different banner hierarchy or geometry.

Visual variation between cases belongs in the case accent, instructional figure, evidence component, and content—not in a redesigned publication header.

## 2. First-page Mission Title Block

Every independent Student, Accessible, Teacher, and Answer Key output begins with the same structural hierarchy:

1. Student and Accessible outputs place Name, Date, and Period above the Mission Title Block on page 1 only.
2. A narrow institutional rail appears at the left edge of the block.
3. A technical line identifies the institution and document role.
4. The primary title uses the visible form `CASE NN · CASE TITLE` for SSS case packets.
5. A concise subtitle identifies campaign, setting, and/or science focus.
6. A compact filled publication-status mark appears below the subtitle.
7. The institutional insignia appears at the right.
8. A thin bottom rule closes the block.

Internal document codes, repository paths, filenames, commit hashes, source-master identifiers, and build provenance do not appear above or inside the prominent title. Curriculum version and game compatibility remain in HTML metadata and the quiet publication footer. A visible version value must not be placed in a separate boxed panel beside the title.

## 3. Continuation header

Every later page uses the shared compact continuation structure:

1. compact institutional insignia at left;
2. technical line in the form `Institution · Document Role · Continued`;
3. a page-specific title describing the material on that page;
4. one thin bottom rule.

The page-specific title is not replaced by a repeated generic case title. Do not split the header into unrelated left and right banner systems, place the institution on one side and the case title on the other, or create a new continuation-header composition for each case.

## 4. Cross-role parity

Student, Accessible, Teacher, and Answer Key roles use the same Mission Title Block and continuation-header anatomy. Role differences are expressed through the role label, page-specific title, page composition, and content—not through a separate visual header system.

HHH uses the same structural anatomy with TAA identity variables and HHH document language.

## 5. Validation requirement

Case-level and shared validation must assert, where applicable:

1. each role's first page uses the canonical Mission Title Block contract;
2. the visible case title uses `CASE NN · CASE TITLE`;
3. internal document codes and visible version boxes are absent from the prominent title block;
4. continuation pages use the compact insignia + technical line + page-specific title structure;
5. continuation headers do not merely repeat the generic case title;
6. Student and Accessible identification remains above the title block on page 1 only;
7. all revised roles remain free of overflow after header normalization.

## 6. Case 02 application

The initial Case 02 validation build accidentally introduced a three-column banner with an identity block at left, an internal `SSS-C1-CASE02` code above the title, and a boxed version/status panel at right. Its continuation pages also used a split left/right banner unlike Case 01.

The corrected Case 02 build restores the approved Case 01 hierarchy across Student, Teacher, Answer Key, Accessible, and Grayscale outputs. The internal case code remains available in metadata and footers only.
