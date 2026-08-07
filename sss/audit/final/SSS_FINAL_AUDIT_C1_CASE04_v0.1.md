# SSS Final Unified Audit — Campaign 1 Case 04

**Case:** SSS-C1-CASE04 — Hayes Orbital Station  
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
- Teacher pages: 7
- Answer Key pages: 4
- Accessible pages: 7

The approved release baseline is treated as immutable starting authority. This audit identifies post-release quality defects and enhancements; it does not challenge the mechanical validity of the prior release.

## Overall assessment

Case 04 is one of the stronger instructional packages in Campaign 1. All eight Student tasks are represented in the detailed Teacher procedure, the Answer Key is complete and useful, the science qualifications are careful, and the Accessible edition contains meaningful scaffolding.

Primary remediation is still required for Teacher-template conformity, source/rubric completeness, digital diagnosis selection, and several smaller Teacher/Accessible inconsistencies.

## Findings register

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| C1C4-T01 | Major | Teacher Guide substantially diverges from corrected C1 Case 01 page architecture | Standardize |
| C1C4-T02 | Major | Teacher Guide contains no authoritative source/reference list | Correct |
| C1C4-T03 | Major | Teacher Page 6 does not provide the required quick + full 4/3/2/1 rubric system | Correct |
| C1C4-UI01 | Major | Task 4 diagnosis selection is impossible to complete in fillable HTML | Correct |
| C1C4-T04 | Moderate | Internal runtime clue IDs are visibly printed on Teacher Page 3 | Remove |
| C1C4-T05 | Moderate | Teacher Guide incorrectly says the Accessible Mission is six pages; approved package has seven | Correct |
| C1C4-ACC01 | Moderate quality gap | Accessible edition is good overall but Task 5 and Task 7 need stronger hand-holding | Refine |
| C1C4-VIS01 | Enhancement | Change-to-crash timeline modernization | Visual phase |
| C1C4-VIS02 | Enhancement | Crash/recovery cycle modernization | Visual phase |
| C1C4-VIS03 | Enhancement | Independent reactor-control diagram modernization | Visual phase |

## C1C4-T01 — Teacher Edition template drift

Case 04 has seven Teacher pages, but the seven pages do not serve the same instructional roles as corrected C1 Case 01.

Current structure:

1. lesson focus, diagnosis, student product, collection, broad timing, materials
2. objectives, standards, success criteria
3. procedure for Tasks 1–3 plus clue IDs
4. procedure for Tasks 4–8 plus discussion questions
5. science qualifications and misconceptions
6. task-by-task point scoring
7. fallback, accessibility, technical contingency, conferencing CER

### Required remediation

Normalize content into the corrected Case 01 seven-page architecture:

1. preparation / launch / diagnosis / complete timing / essential evidence / sticking point / collection / fallback
2. overview / guiding question / standards / objectives / success criteria / vocabulary / materials
3. complete detailed Tasks 1–8 procedure
4. formative checks / assessment / accessibility / misconceptions / science qualification / fallback
5. evidence architecture / causal reasoning / distractors / reactor-specific science boundary
6. common quick + analytic rubrics, retaining useful case-specific scoring notes where space permits
7. sources / no-game evidence digest / technical fallback

The existing content is largely useful and should be reorganized rather than rewritten from scratch.

## Student → Teacher procedure parity

**PASS**

Teacher Page 3 explicitly covers Tasks 1–3. Teacher Page 4 explicitly covers Tasks 4–8. All eight numbered Student tasks are represented in detailed procedure.

This coverage should be preserved during template normalization.

## C1C4-T02 — authoritative Teacher source list absent

The Teacher Guide contains no authoritative references section.

This is material because the Teacher Guide includes substantial science background on:

- spirulina/cyanobacteria terminology
- photoinhibition
- photooxidative stress
- continuous-light qualifications
- reactor-control qualifications

### Required remediation

Add a concise authoritative source list to the final Teacher page, reusing controlled case-production sources where available rather than initiating a new broad science-research campaign.

## C1C4-T03 — common rubric contract absent

Teacher Page 6 provides useful task-by-task point scoring totaling 30 points, plus acceptable alternatives and revision cues.

However, it does not provide the definitive Case 01 rubric system:

1. quick Secure / Developing / Beginning rubric
2. full 4 / 3 / 2 / 1 analytic rubric with descriptors

### Required remediation

Restore the common rubric structure. Retain the useful task-specific scoring notes and revision cues in compact form where practical.

Common rubric structure does not require discarding good case-specific scoring guidance.

## C1C4-UI01 — Task 4 diagnosis selection is not digitally fillable

Student and Accessible Task 4 require learners to choose one diagnosis. Both editions display small square selection marks implemented as styled spans rather than response controls.

They have no:

- `data-response`
- persistent ID
- radio/checkbox input
- keyboard interaction
- stored fill-mode value

Therefore the printed worksheet works, but the fillable HTML cannot record the required diagnosis-selection action.

### Required remediation

Use a persisted keyboard-operable single-selection control for Student and Accessible Task 4.

This confirms the same systemic fillable-response defect found in C1 Case 03.

## C1C4-T04 — visible runtime clue IDs

Teacher Page 3 visibly prints:

- `LIGHTING_SCHEDULE_CHANGED`
- `NO_DARK_PERIOD`
- `PHOTOOXIDATIVE_DAMAGE`
- `DARK_PERIOD_REQUIRED`

These are game runtime identifiers, not classroom-facing instructional labels.

### Required remediation

Replace the code-facing column with a structure such as:

`Evidence source | Essential evidence | Instructional use`

This is a repeated cross-case pattern and is a candidate for shared validation.

## C1C4-T05 — wrong Accessible page count

Teacher Page 7 tells teachers to use the **six-page Accessible Mission**.

The approved package and actual content contain **seven Accessible pages**.

### Required remediation

Correct the Teacher-facing page-count statement and add a cross-role page-count consistency check to future validation if practical.

## Answer Key verdict

**PASS**

The Answer Key provides complete, useful exemplars for all eight keyable tasks.

- Task 1: changed variable + supporting observation
- Task 2: complete five-event timeline + acceptable variation
- Task 3: all four evidence categories completed
- Task 4: diagnosis + correlation/mechanism justification
- Task 5: complete six-stage recurrence cycle + acceptable mechanism language
- Task 6: complete CER
- Task 7: immediate recovery + long-term independent control
- Task 8: cause/effect classification + sequence justification

No Answer Key correction is required.

## C1C4-ACC01 — targeted Accessible refinement

Case 04 is genuinely adapted rather than merely enlarged.

Strong features include:

- supported vocabulary
- explicit step-by-step Task 1 directions
- vertical timeline reading order
- evidence table converted to separate evidence cards
- Task 4 broken into explicit reasoning steps
- Task 4 sentence frame
- dedicated canonical CER page

### Task 5

The Accessible cycle is mostly the Student cycle turned vertical. Stage 1 is supplied, but Stages 2–6 remain independently sequenced.

**Recommended direction:** prefill one additional causal stage, preferably Stage 2, then have the learner sequence damage → functional crash → rebuilding → recurrence.

### Task 7

The Standard Student edition provides two clearly labeled fields:

- Immediate recovery action
- Long-term independent control

The Accessible edition collapses these into one box, which removes useful structure.

**Required direction:** restore two separate guided fields with sentence-starting cues.

### CER

**PASS — preserve.**

## Game / curriculum parity

**PASS**

The game and curriculum agree on:

- four months of stable operation
- lighting change from 16/8 to continuous 24/0
- first crash about one week later
- no independent reactor light control
- recurring roughly 6–8-day crashes
- stable nutrient feed and nominal temperature
- photooxidative damage rather than infection
- survivor rebuilding between crashes
- configuration-specific warning against uncontrolled 24/0 exposure
- continuous operation remaining possible under appropriate independent controls

No substantive contradiction was found.

## Science qualification

**PASS / preserve**

The Teacher Guide correctly avoids:

- calling spirulina a plant
- claiming all spirulina require darkness
- claiming continuous cultivation is impossible
- claiming “dark reactions” require darkness
- treating correlation alone as mechanism

The case-specific qualification that operating limits depend on intensity, duration, mixing, density and broader process conditions is particularly strong.

## Grayscale

**PASS**

No rendered grayscale defect was identified.

## Visual modernization candidates

### C1C4-VIS01 — incident timeline

Modernize the five-box sequence as an SAA incident/event log while preserving only the verified relative timing.

### C1C4-VIS02 — repeating crash cycle

Redesign the six-stage snake layout as an immediately readable closed-loop reactor fault cycle.

### C1C4-VIS03 — independent control system

Redesign `Measure → Compare → Control → Verify` as a technical control-loop schematic showing sensor, controller, independent actuator, reactor and performance feedback.

All should remain deterministic SVG/HTML/CSS rather than generated data graphics.

## Shared-system implications

Case 04 strengthens several cross-case conclusions:

- Teacher page count alone does not prove Teacher-template conformity.
- Visible runtime clue IDs are recurring implementation leakage.
- Required diagnosis choices need persisted digital response controls.
- Accessible adaptations should preserve useful conceptual structure rather than collapse it.

## Final disposition

`AUDIT_COMPLETE — REMEDIATION_REQUIRED`

Owner accepted this audit for inclusion in the unified SSS remediation register.

No curriculum package changes were made during this audit.
