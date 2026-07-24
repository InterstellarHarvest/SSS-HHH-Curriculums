# SSS Case 01 v1.0 — Blockers and Justified Exceptions

**Reconciled:** 2026-07-24  
**Status:** Release candidate; not release-approved

## 1. Closed release gate — physical print test

### 1.1 Owner physical print test

**Status:** CLOSED — passed 2026-07-24 (tester: Nate / Owner)

Print the following at 100% scale on an ordinary school printer:

- Student Mission
- Teacher Packet
- Answer Key
- Accessible Mission
- Grayscale Review

Confirm:

- no printer-imposed scaling;
- 0.50-inch safe margins remain intact;
- thin rules reproduce cleanly;
- grayscale fills remain distinguishable;
- writing areas have practical physical height;
- duplex orientation is correct where used;
- the SAA insignia and all glyphs render cleanly.

The owner recorded this test as passed on 2026-07-24; the HTML and PDFs are labeled **APPROVED**.

## 2. Open repository-wide publishing decisions that do not block Case 01 content reconciliation

### 2.1 Deterministic offline fonts

The master requests Inter and JetBrains Mono through the approved web-font pattern and provides system fallbacks. A future repository-wide decision may package approved fonts or standardize on installed system fonts for deterministic offline line wrapping. No font files are included in this release.

This is a shared publishing-policy decision, not an unresolved Case 01 content or game-compatibility blocker.

### 2.2 Tagged PDF / PDF-UA pipeline

The HTML Accessible role supports semantic headings, programmatic labels, keyboard fill, and parallel task content. Chromium-generated PDFs are not guaranteed to be tagged PDF/UA files. A separate tagged-PDF workflow is required only when formal PDF accessibility compliance is an institutional deliverable.

This conditional requirement does not invalidate the Accessible HTML or the current print-review PDF.

## 3. Closed blockers

### 3.1 Content-source verification — CLOSED

The SSS Master Audit v1.0 verified the scientific architecture and appropriate qualification. The Case 01 Game-Content Audit verified all printed source URLs and corrected the citation attribution and NASA label in the v1.0 packet.

### 3.2 Game-baseline verification — CLOSED

The Game-Content Audit crosswalked the curriculum against the canonical runtime at game commit `2a6e8a7`, confirmed the four evidence sources, diagnosis options, correct diagnosis, clue gate, mechanism, and worksheet-only engineering application, and found the packet compatible with the live baseline.

### 3.3 Source/master synchronization — CLOSED FOR RC

The controlled Markdown sources, task registry, HTML master, Answer Key exemplars, manifest, and validation content checks now use the same v1.0 task architecture.

## 4. Justified implementation exceptions

### 4.1 Student packet uses three pages

Approved type scale, usable evidence rows, diagnosis space, CER hierarchy, engineering fields, and the exit ticket cannot fit on two Letter pages without unacceptable compression. Repagination is preferred over shrinking type or response space.

### 4.2 Answer Key uses three pages

Three pages keep evidence/alternatives, mechanism/diagnosis, and CER/design/exit models legible and usable during instruction.

### 4.3 Accessible Edition uses six pages

Larger type, reduced density, one-column sequencing, and expanded response areas require additional pages while preserving the exact task order and expectations.

### 4.4 Teacher Packet uses seven pages

The seven-page role contains the quick start, formal lesson plan, assessment/access notes, case analysis, rubrics, references, fallback, and genuine note areas without decorative padding.

### 4.5 Grayscale uses semantic tokens

Grayscale mode replaces semantic color variables and filters artwork rather than applying a whole-page filter that could rasterize or damage PDF accessibility.

## 5. Governing-document conflict review

No project-wide policy conflict was found. The approved v1.0 release preserves the approved Mission Title Block, continuation headers, 0.50-inch margins, type hierarchy, Phosphor icons, mixed grid, blank response boxes, stacked CER, Teacher-note treatment, independent Answer Key, accessible parity, task-reference parity, and Teacher metadata visibility rules.
