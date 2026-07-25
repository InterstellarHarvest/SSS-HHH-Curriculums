# Case 02 Structural Stress-Test Report

**Case:** SSS Campaign 1, Case 02 — Lunar Greenhouse  
**Build:** v1.0  
**Status:** VALIDATION BUILD  
**Date:** 2026-07-24

## Executive result

Case 02 successfully operates as the second implementation of the approved SSS/HHH production system without redesigning the governing architecture. It proves that the Case 01 foundation can support a different scientific practice, a different central visual, a compact continuous-flow Accessible edition, and role-isolated independent outputs.

Automated status: **PASS**.  
Owner physical print status: **OPEN**.  
Case 03 work: **not begun**.

## 1. Framework elements reused unchanged

The following Case 01 contracts were retained:

- Letter-size fixed page shell with explicit margins and screen-only overflow warnings
- Student identification row before the first mission title block, on Student and Accessible page 1 only
- Mission title block, continuation header, publication footer, version/status mark, and compatibility baseline
- Shared CSS token architecture for geometry, neutral system, institutional colors, type scale, and grayscale overrides
- Grayscale-first rules with no whole-page rasterizing filter
- Technical label headings, Phosphor-style line-icon slots, callouts, technical tables, response blocks, CER hierarchy, teacher notes, and answer blocks
- Blank, unruled, fillable response fields with stable `data-field` and `data-persist-id` values
- Student / Teacher / Answer / Accessible / All Pages role architecture
- Local persistence, fill mode, edit mode, margin controls, density controls, guides, boundaries, print, portable HTML download, selective clearing, reset, and overflow diagnostics
- Role changes that update only the role state and preserve all other settings/content
- Teacher production metadata restricted to footer/metadata/report channels
- Exact Student / Accessible / Teacher-reference / Answer-Key task parity controlled by a canonical registry
- Independent output generation and PDF preflight
- Academic grading separated from game score, speed, rank, rapport, and optional exploration

## 2. Case 02-specific components

Case 02 adds content-specific components without changing shared geometry:

- Six-stage `.process-chain` model with dependency arrows
- `.process-stage`, `.stage-num`, `.stage-entry`, `.stage-status`, and `.failed-stage`
- Curriculum-original `pollination-process-model.svg`
- Linear Accessible process model that preserves the same six terms and task title
- Failed-step analysis with separate fields for the step, two observations, and one downstream effect
- Competing-diagnosis analysis centered on mechanism rather than source transcription
- Pollination-specific content-regression checks for clue IDs, diagnoses, process order, science qualifications, and excluded fabricated/unsupported source claims

## 3. Reusable framework additions

The stress test produced additions that should be available to later cases:

### 3.1 Generic process-model component

The process chain is not pollination-specific in its geometry. Later cases can reuse the same component for cause/effect, timelines, systems, or engineering sequences by replacing labels and status markers.

### 3.2 Accessible continuous-flow pagination

Accessible tasks continue in sequence and share pages when larger type and adequate response areas still fit without overflow. Numbered tasks are not automatically isolated on separate pages. Task 5 is kept intact on one page; Tasks 3–4 and 6–7 are paired.

### 3.3 Null-safe persistent-state loader

The first browser pass revealed that `JSON.parse(null)` returns `null`, not the fallback object. The state/content loader now explicitly returns the fallback for null/empty values before object operations. This should be carried into any extracted shared renderer.

### 3.4 Role-stripped standalone HTML generation

A hidden Teacher/Answer role inside a Student HTML file is not strong enough isolation for independent distribution. The output generator removes all non-target role pages from each standalone artifact. Student and Accessible HTML files therefore contain no Teacher or Answer Key content.

### 3.5 Content-order safeguards

Vocabulary lists use alphabetical order for consistent lookup. Word banks that populate a sequence use a fixed shuffled order so the bank does not reveal the solution. Student-facing pages omit grading-policy commentary; teachers control grading decisions through Teacher materials.

### 3.6 Output-level validation

The harness checks each standalone artifact independently, not only the master. It verifies visible page count, zero overflow, JavaScript execution, role isolation, grayscale initialization, PDF dimensions, page count, status text, and checksums.

## 4. Case 01 assumptions that failed or required revision

### Assumption A — The evidence-source matrix could remain the central task

**Failed.** Reusing the Case 01 matrix would flatten the scientific practice and violate the approved audit. Case 02 required a process model in which the first failed event could be located.

### Assumption B — The Accessible edition could remain near the Case 01 page count

**Required two revisions.** The initial four-page composition overflowed, but the first seven-page correction isolated tasks too aggressively and left excessive unused space. Owner review established a better rule: preserve larger type and response space while packing related tasks continuously. The validated edition now uses five pages, keeps Task 5 intact, pairs Tasks 3–4 and 6–7, and has zero overflow.

### Assumption C — Hidden roles were equivalent to independent outputs

**Failed.** Hidden pages are acceptable in the editable master, but not as the strongest distribution boundary. Standalone HTML generation now strips other roles entirely.

### Assumption D — Missing local-storage JSON would always produce an object

**Failed during validation.** The null-state load crashed before controls initialized. The loader was corrected and regression-tested.

### Assumption E — Runtime numeric values could move directly into curriculum design criteria

**Failed on science review.** The game’s exact airflow/frequency values are local case fiction/design data. The curriculum assesses the mechanism, criterion, constraint, and verification rather than memorization of unsupported universal thresholds.

### Assumption F — “Reuse the Mission Title Block” allowed a new banner hierarchy

**Failed on owner visual review.** The first Case 02 build used a different three-column banner, exposed the internal case code above the worksheet title, boxed the version/status at right, and used split continuation banners.

**Resolution:** the Case 01 v1.0 first-page and continuation-header anatomy is now explicitly frozen by shared amendment v1.0.3. Case-specific variation must occur in instructional content and figures, not through a new publication banner.

## 5. Validation evidence

- Static/content/accessibility checks: **53/53 passed**
- Browser behavior/output checks: **19/19 passed**
- Compact first-page header geometry, 26 pt title, 9 pt subtitle, tight vertical spacing, and three-line institutional lockup: **passed**
- Independent PDFs: Student 2 pages; Teacher 7; Answer Key 3; Accessible 5; Grayscale 2
- PDF page dimensions: Letter, 612 × 792 points
- Rendered-page visual review: 19-page contact sheet plus full-size spot checks
- Overflow warnings at default settings: zero in every role/output
- Physical print test: not yet performed by owner

## 6. Readiness for Case 03

**Structural conclusion:** The shared system is ready to support Case 03. Case 02 demonstrates that the foundation can change the central scientific practice and visual structure without forking the publishing framework.

**Release conclusion:** Case 02 itself is not approved yet. Its visible status must remain **VALIDATION BUILD** until the owner completes physical 100% print testing and records the result. Case 03 is outside this work and has not been started.

## 7. Recommended framework extraction after owner approval

After the physical print gate passes, the following may be extracted into shared production code without changing visible output:

1. null-safe state/content persistence;
2. role-stripped output generation;
3. process-chain component and accessible continuous-flow pagination rules;
4. common task-parity and role-isolation assertions;
5. common PDF page-count/Letter-size/status preflight.

Do not perform a project-wide refactor during Case 02 validation unless the owner explicitly opens that scope.

## 8. Project-wide rule promotion

The Case 02 corrections are promoted from local implementation findings to the approved shared clarification `CONTENT_ORDERING_AND_ACCESSIBLE_FLOW_v1.0.2.md`. Curriculum Bible v1.3 now lists that amendment as controlling. Cases 03 and later therefore inherit the vocabulary-ordering, sequence-bank shuffling, nonredundant-direction, Teacher-only grading-commentary, and Accessible continuous-flow pagination rules without relying on agents to rediscover this report. The companion `MISSION_TITLE_AND_CONTINUATION_HEADER_PARITY_v1.0.3.md` amendment also freezes the Case 01 header anatomy and prohibits case-level banner redesign.

## v1.1 page-identity correction

Owner review found that the Case 02 v1.0 banner, continuation headers, visible production-status marks, and metadata-heavy footer had drifted from the desired universal system. The v1.1 master corrects that drift and establishes the shared v1.0.4 rule:

- title/location left, institutional identity right;
- one left accent rail on first pages and no top accent rule;
- generic continuation headers within each role;
- role-plus-position footer only;
- no printable approval, validation, version, baseline, date, or document-code metadata;
- fixed outputs deferred until release testing.

This is a reusable framework correction and must be applied to Case 01 v1.1 and all future masters.
