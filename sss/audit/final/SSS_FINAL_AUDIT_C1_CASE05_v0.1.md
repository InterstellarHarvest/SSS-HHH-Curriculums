# SSS Final Unified Audit — Campaign 1 Case 05

**Case:** SSS-C1-CASE05 — Sub Surface Bunker  
**Audit phase:** Final SSS Campaign 1 + Campaign 2 unified quality audit  
**Audit status:** `AUDIT_COMPLETE — REMEDIATION_REQUIRED`  
**Owner disposition:** `OWNER_ACCEPTED`  
**Audit date:** 2026-08-07

## Frozen authority

- Curriculum baseline: `f7a24423f802a095aa149f923d05475ba2837599`
- Game baseline: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`
- Curriculum package version: `1.0`
- Package lifecycle at audit start: `APPROVED_STABLE`
- Student pages: 4
- Teacher pages: 8
- Answer Key pages: 4
- Accessible pages: 7

## Overall assessment

Case 05 is scientifically careful and its Answer Key is strong. The four-source evidence architecture, uncertainty language, radiation/exposure distinction, and engineering problem-definition work are all substantial strengths.

Remediation is required for Teacher-template drift, incomplete task-by-task procedure coverage, rubric inconsistency, a fillable diagnosis-selection defect, internal navigation leakage, Accessible process-model scaffolding, and learner-facing location/identity drift.

## Findings register

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| C1C5-T01 | Major | Eight-page Teacher Guide does not conform to corrected seven-page C1 Case 01 Teacher template | Standardize |
| C1C5-T02 | Major | Detailed Teacher facilitation explicitly covers only Tasks 3, 5, and 7 rather than all eight Student tasks | Correct |
| C1C5-T03 | Major | Teacher grading lacks the required full 4/3/2/1 analytic rubric contract | Correct |
| C1C5-UI01 | Major | Task 4 requires circling the best diagnosis but provides no persisted digital selection control | Correct |
| C1C5-T04 | Moderate | Teacher Guide exposes internal game navigation-node paths | Remove |
| C1C5-ACC01 | Moderate quality gap | Accessible Task 5 remains nearly the full six-phrase sequencing demand | Refine |
| C1C5-ID01 | Moderate | Learner-facing curriculum identity disagrees with the frozen game and the approved Case 05 location decision | Synchronize |
| C1C5-VIS01 | Enhancement | Radiation-to-growth pathway modernization | Visual phase |
| C1C5-VIS02 | Enhancement | Four-source evidence convergence modernization | Visual phase |
| C1C5-VIS03 | Enhancement | Engineering criteria/constraints organizer modernization | Visual phase |

## C1C5-T01 — Teacher Edition template drift

Case 05 uses eight Teacher pages rather than the corrected Case 01 seven-page architecture.

Current content is distributed across:

1. overview, diagnosis, duration, sequence, materials
2. objectives, success criteria, standards, vocabulary, prerequisites
3. preparation, facilitation, checks, accessibility
4. evidence analysis and science boundaries
5. misconceptions, alternatives, fallback
6. annotated guidance Tasks 1–4 + quick grading
7. annotated guidance Tasks 5–8 + formal grading dimensions
8. references and technical notes

Much of this content is useful, but the structure does not function as a common Teacher template.

### Required remediation

Normalize into corrected Case 01 architecture, preserving strong content while consolidating to seven Teacher pages if layout permits.

The extra annotated-guidance page can likely be absorbed into the procedure, assessment, evidence, and rubric pages rather than retained as a distinct structural design.

## C1C5-T02 — detailed facilitation does not cover all tasks

Teacher Page 3 explicitly references:

- Task 3 · Converge the Four Clue Routes
- Task 5 · Model the Radiation-to-Growth Pathway
- Task 7 · Define the Engineering Design Problem

It does not explicitly guide:

- Task 1 · Frame the Mission Problem
- Task 2 · Separate Observation from Interpretation
- Task 4 · Compare the Competing Diagnoses
- Task 6 · Explain the Diagnosis with CER
- Task 8 · Recommend Immediate and Durable Responses

Later annotated-grading pages discuss those tasks, but that is not a substitute for a complete timed instructional procedure.

### Required remediation

Create one coherent detailed procedure covering Tasks 1–8 in order, using the existing annotated guidance as source material.

## C1C5-T03 — rubric contract incomplete

Teacher Page 6 provides a Secure / Developing / Beginning quick rubric for Tasks 1–4.

Teacher Page 7 provides another Secure / Developing / Beginning rubric across Evidence, Mechanism, Problem definition, and Communication.

Neither supplies the definitive Case 01 full analytic:

`Criterion | 4 Accomplished | 3 Proficient | 2 Developing | 1 Beginning`

### Required remediation

Retain concise task-specific grading guidance but add the common quick + complete 4/3/2/1 analytic rubric structure on the normalized rubric page.

## C1C5-UI01 — Task 4 best-diagnosis selection is not fillable

Student Task 4 says:

> Compare all four diagnoses ... Circle the best-supported diagnosis.

Accessible Task 4 likewise asks learners to compare all diagnoses and circle the best-supported diagnosis.

The diagnosis rows contain writable evidence-analysis fields, but there is no persisted response control representing the actual final diagnosis selection.

### Required remediation

Add a persisted keyboard-operable single-selection control or an explicit persisted `Best-supported diagnosis` response field in Student and Accessible editions.

This is the third consecutive case confirming the shared fillable-response validation gap.

## C1C5-T04 — internal game navigation paths are teacher-facing

Teacher Page 3 tells teachers to route students through internal node paths such as:

- `crew start → problem_main`
- `sensors start → radiation_detail`
- `plants start → microscope`
- `logs start → construction_log`

These are implementation details rather than stable classroom-facing navigation language.

### Required remediation

Replace code-node paths with durable instructional navigation such as source names, visible UI labels, or evidence targets.

Internal node IDs belong in implementation/validation records, not ordinary Teacher pages.

## Answer Key verdict

**PASS / preserve**

The Answer Key visibly completes all keyable fields:

- Task 1: problem + needed information
- Task 2: all three Observation/Interpretation classifications + why distinction matters
- Task 3: four-route contribution table
- Task 4: four diagnosis analyses + completed best-supported conclusion
- Task 5: complete seven-stage qualitative pathway
- Task 6: complete qualified CER
- Task 7: need, criteria, constraints, verification evidence
- Task 8: immediate response, durable engineering response, justification/verification

It also supplies useful acceptable variation for engineering responses without pretending one design is already validated.

## C1C5-ACC01 — Accessible Task 5 needs partial completion

Case 05's Accessible edition is otherwise strong:

- supported vocabulary
- explicit Observation vs Interpretation definitions and sentence frame
- clue-route table converted to individual evidence cards
- diagnosis comparison spread into clear cards
- canonical CER with uncertainty language and a reasoning frame
- engineering task broken into labeled Need / Criteria / Constraints / Verification fields
- immediate and durable responses kept separate

Task 5 remains the main weakness.

The Accessible edition turns the seven-stage pathway vertical but still requires students to place all six remaining phrases independently.

### Recommended remediation

Prefill one or two intermediate stages, especially the exposure-versus-damage distinction, then have students complete the later biological/growth/convergence links.

This preserves the essential mechanism while reducing sequencing load.

### CER

**PASS — preserve.**

## C1C5-ID01 — location / identity drift

Curriculum package and worksheets identify the case as:

- title: `Sub Surface Bunker`
- subtitle/location: `Europa, orbiting Jupiter`

The frozen game identifies:

- name: `Europa Outpost`
- location: `Sub-Surface Bunker`
- subtitle: `Europa (Jupiter's Moon)`

The approved Case 05 production decision had also established the classroom identity as Europa / Sub-Surface Bunker rather than the vague `orbiting Jupiter` location string.

### Required remediation

Synchronize the case identity across package metadata, printed worksheet subtitle, and game-facing identity while preserving the approved location meaning.

Recommended classroom formulation remains consistent with the approved decision: `Campaign 1 · Case 05 · Europa, Sub-Surface Bunker`.

## Game / curriculum parity

**PASS on science/evidence; identity needs synchronization.**

The frozen game and curriculum agree on the important evidence:

- repeated failure across plantings
- elevated grow-chamber ionizing-radiation monitor status
- crop assessment incomplete
- meristem abnormalities consistent with DNA damage
- shielding/crop protection not verified
- modeled secondary radiation may contribute
- separate crew and crop assessment
- radiation as best-supported diagnosis rather than proof from one clue

No incorrect exact radiation quantities or thresholds are introduced.

## Science qualification

**PASS / preserve**

The package carefully preserves:

- exposure is not identical to biological damage
- meristem abnormalities are consistent with DNA damage without proving an exact molecular mechanism
- ionizing radiation can affect dividing and nondividing cells
- meristem damage is especially disruptive to continued growth
- modeled secondary radiation is conditional, not a measured percentage
- crew criteria do not establish crop safety
- visual symptoms alone are insufficient

This is a strong model for later science-status language.

## Visual modernization candidates

### C1C5-VIS01 — radiation-to-growth pathway

Replace the long box chain with a clean SAA qualitative hazard pathway that visually separates:

`environment → material interaction → exposure evidence → evidence limit → biological evidence → growth consequence → diagnosis convergence`

### C1C5-VIS02 — four-source convergence

Create a four-channel evidence-convergence schematic showing Crew / Sensors / Plants / Logs feeding a qualified diagnosis rather than a single-clue proof arrow.

### C1C5-VIS03 — engineering definition

Modernize the Need / Criteria / Constraints / Verification organizer as a compact mission-engineering requirements panel while retaining the same writable fields.

## Shared-system implications

Case 05 confirms:

- Teacher-template drift persists into later Campaign 1 production.
- Detailed Teacher procedure needs explicit task-registry parity checks.
- Required diagnosis-selection actions need persisted fill controls.
- Internal game/node navigation identifiers should be rejected from Teacher-facing content.
- Accessible mechanism sequencing benefits from intentional partial completion.

## Final disposition

`AUDIT_COMPLETE — REMEDIATION_REQUIRED`

Owner accepted this audit for inclusion in the unified SSS remediation register.

No curriculum package changes were made during this audit.
