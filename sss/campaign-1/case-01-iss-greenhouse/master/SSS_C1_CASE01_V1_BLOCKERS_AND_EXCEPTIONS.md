# SSS Case 01 v1.0 Blockers and Justified Exceptions

## 1. Unresolved blockers before release approval

### 1.1 Physical print sample

**Status:** Open release blocker  
**Required action:** print Student, Teacher, Answer Key, Accessible, and Grayscale samples at 100% scale on an ordinary school printer.

Confirm:

- no printer-imposed scaling;
- 0.50-inch safe margins remain intact;
- thin rules reproduce cleanly;
- grayscale fills remain distinguishable;
- writing areas have practical physical height;
- duplex orientation is correct where used.

The implementation must remain `VALIDATION BUILD` until this is complete.

### 1.2 Deterministic offline fonts

**Status:** Open publishing decision  
**Current behavior:** the master declares Inter and JetBrains Mono through the same web-font import pattern used by the v1.0 reference implementation, with system fallbacks.

In an offline classroom or archived build:

- Inter may resolve from the operating system;
- JetBrains Mono may fall back to Consolas or another monospace font;
- line wrapping can vary slightly between systems.

A repository-wide font packaging or approved system-font policy is needed for deterministic offline output. No font files are included in this migration package.

### 1.3 Tagged accessible PDF

**Status:** Conditional blocker  
**Applies when:** a tagged PDF or PDF/UA file is required as an official accessible edition.

The HTML Accessible Edition passes the implemented screen-reader and keyboard basics, and its print layout is parallel and readable. Chromium’s generated PDFs are not tagged. A separate tagged-PDF publishing pipeline is required for formal PDF accessibility compliance.

### 1.4 Content-source and game-baseline verification

**Status:** Outside visual-migration scope; pending curriculum/source QA

- Source URLs were preserved but not independently re-researched.
- Standards statements were preserved but not re-aligned.
- Game compatibility baseline `2a6e8a7` was preserved but not re-tested against game source.

No content was invented to close these gaps.

## 2. Justified implementation exceptions

### 2.1 Student packet increased from two pages to three

**Reason:** the approved type scale, usable evidence rows, diagnosis space, stacked CER hierarchy, engineering fields, and exit ticket could not coexist on two Letter pages without unacceptable compression.

**Decision:** repaginate. Do not reduce type or writing space.

### 2.2 Answer Key increased from two pages to three

**Reason:** the two-page key was too compressed for live instructional use and left no practical annotation area after the models were made readable.

**Decision:** separate evidence/alternatives, mechanism/diagnosis, and CER/design/exit into three pages.

### 2.3 Accessible Edition uses six pages

**Reason:** larger type, reduced density, one-column sequencing, and expanded physical response areas are required for a genuinely parallel accessible edition.

**Decision:** retain the same numbered task order and instructional expectations while permitting additional pages.

### 2.4 Teacher page count remains seven

The short teacher pages were not padded with decorative material. Genuine planning and reference notes areas were added to use remaining printable space. The existing seven-page role structure remains practical and coherent.

### 2.5 Grayscale implemented through tokens, not a page filter

The whole-workspace filter produced an image-only PDF in Chromium. That was an accessibility and publishing failure.

The final grayscale mode changes semantic color variables and filters only artwork. This is an implementation correction required to satisfy the approved grayscale and accessibility intent.

### 2.6 Publication status remains “Validation Build”

The master is not marked Approved because physical print, final content/source QA, and any tagged-PDF requirement remain open. This prevents a visually complete file from being mistaken for a released curriculum artifact.

## 3. No governing-document conflict found

No exception required changing:

- Mission Title Block architecture;
- continuation headers;
- 0.50-inch margins;
- Inter + JetBrains Mono intent;
- Phosphor icon family;
- 12-column grid;
- callout treatment;
- blank response boxes;
- stacked CER;
- teacher-note neutrality;
- answer-key separation;
- accessible-edition parallelism.
