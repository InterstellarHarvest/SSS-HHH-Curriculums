# SSS Final Unified Audit — Campaign 1 Case 02

**Case:** SSS-C1-CASE02 — Lunar Greenhouse  
**Audit phase:** Final SSS Campaign 1 + Campaign 2 unified quality audit  
**Audit status:** `AUDIT_COMPLETE — REMEDIATION_REQUIRED`  
**Owner disposition:** `OWNER_ACCEPTED`  
**Audit date:** 2026-08-07

## Frozen authority

- Curriculum baseline: `f7a24423f802a095aa149f923d05475ba2837599`
- Game baseline: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`
- Curriculum package version: `1.0`
- Package lifecycle at audit start: `APPROVED_STABLE`
- Student pages: 3
- Teacher pages: 7
- Answer Key pages: 3
- Accessible pages: 7

The approved release baseline is treated as immutable starting authority. This audit identifies post-release quality defects and enhancements; it does not challenge the mechanical validity of the prior release.

## Audit scope

The final audit checked:

- Student / Teacher / Answer Key / Accessible task parity
- Answer Key completeness and correctness
- Teacher-to-Student procedure and assessment parity
- Teacher Edition conformity to corrected C1 Case 01 architecture
- Accessible Edition differentiation and hand-holding quality
- game-to-curriculum evidence and diagnosis parity
- grayscale and print-facing presentation behavior
- layout and response-area suitability
- code / metadata / validation-system weaknesses
- visual modernization opportunities

## Overall assessment

Case 02 is stronger than Case 01 on basic task parity. All numbered Student tasks are represented in the Teacher teaching sequence, and the Answer Key is a complete-exemplar key.

The primary remediation needs are:

- Teacher Edition structural standardization
- completion of the formal analytic rubric
- removal of visible internal runtime clue IDs
- stronger Accessible hand-holding
- two minor metadata corrections

No Answer Key correctness defect, substantive game/curriculum contradiction, or rendered grayscale defect was found.

## Findings register

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| C1C2-T01 | Major | Teacher Guide does not conform to corrected C1 Case 01 Teacher template | Standardize |
| C1C2-T02 | Major | "Formal analytic rubric" is only a list of dimensions, not a completed analytic rubric | Correct |
| C1C2-T03 | Moderate | Internal runtime clue IDs are visibly exposed on a Teacher worksheet | Remove |
| C1C2-ACC01 | Major quality gap | Accessible edition largely spreads the same tasks out rather than providing enough hand-holding | Differentiate |
| C1C2-META01 | Minor | Accessible Task 8 resize metadata incorrectly says "Regolith-medium design" | Correct |
| C1C2-META02 | Minor | Canonical package subtitle/location metadata disagrees with displayed worksheet/game identity | Synchronize |
| C1C2-VIS01 | Enhancement | Pollination sequence figure is a strong same-footprint modernization candidate | Visual phase |

## C1C2-T01 — Teacher Edition template drift

Case 02 contains substantial useful Teacher content, but its seven Teacher pages were designed as a distinct document rather than as the C1 Case 01 Teacher template populated for Lunar Greenhouse.

### Page 1

Corrected C1 Case 01 authority expects:

- Before class
- Game launch path
- Correct diagnosis
- 60-minute lesson flow
- Essential evidence
- Likely sticking point
- What to collect
- Technical fallback
- Teacher line

Case 02 instead uses:

- One-period purpose
- Distribute
- Correct diagnosis
- Collect
- Likely sticking point
- timing table
- fallback

The teaching sequence itself is good and should largely be retained, but reorganized into the authoritative Page 1 structure.

### Page 2

Corrected Case 01 expects:

- Lesson overview
- Guiding question
- Standards alignment
- Learning objectives
- Success criteria
- Vocabulary
- Materials
- Teacher planning notes

Case 02 currently uses:

- Overview
- Audience
- Prerequisite knowledge
- Standards position
- Measurable objectives
- Success criteria

Useful case-specific prerequisite information may be retained where space permits, but the page should conform to the common structure and restore missing core template components.

### Page 3

**Content pass.**

The detailed procedure correctly sequences:

Task 2 → investigation → Tasks 3–4 → Tasks 5–7 → Task 8 → Task 9.

The page mainly needs visual/template normalization.

### Page 4

Case 02 contains appropriate:

- checks for understanding
- assessment
- accessible participation
- misconceptions
- differentiation
- science boundary

These should be reorganized into the Case 01 Page 4 template:

- Formative checks
- Assessment
- Access
- Misconceptions
- Source/science status
- Fallback
- notes

### Page 5

The evidence-analysis content is strong and corresponds well to the Case 01 evidence-architecture page.

However, visible runtime clue IDs must be removed. See C1C2-T03.

### Page 6

The quick rubric is useful, but the formal analytic rubric is incomplete. See C1C2-T02.

### Page 7

The page correctly provides:

- fallback evidence
- authoritative sources
- source-status awareness

But it should conform to the Case 01 Page 7 structure:

- Authoritative sources
- No-game evidence digest
- Technical/classroom fallback
- notes

The visible "Figure-rights decision" is production/design documentation rather than ordinary classroom Teacher content and should move outside the printable Teacher body.

Source presentation should also be normalized to the common source-list format.

## Student → Teacher task parity

Case 02 performs well here.

| Task | Teacher treatment | Result |
|---|---|---|
| 1 · Vocabulary | reference/support | PASS |
| 2 · Initial thinking | launch | PASS |
| 3 · Model the pollination sequence | evidence processing | PASS |
| 4 · Identify the failed step | evidence processing | PASS |
| 5 · Test the competing explanations | diagnosis | PASS |
| 6 · Diagnose and reject an alternative | diagnosis | PASS |
| 7 · Claim-Evidence-Reasoning | explanation | PASS |
| 8 · Design a reliable pollination support | application | PASS |
| 9 · Exit ticket | independent exit | PASS |

No numbered Student task disappears from the Teacher sequence.

## C1C2-T02 — Formal analytic rubric incomplete

Corrected Case 01 establishes two Teacher rubrics:

1. quick Secure / Developing / Beginning rubric
2. complete analytic 4 / 3 / 2 / 1 rubric with performance descriptors for every criterion

Case 02 correctly supplies the quick rubric.

Its "Formal analytic dimensions" section only names:

- Process-model accuracy
- Failed-step diagnosis
- Evidence selection/diversity
- Alternative evaluation
- CER reasoning
- Engineering response
- Scientific qualification
- Communication/completion

No performance-level descriptors are provided.

A list of dimensions is not a complete analytic rubric.

### Required remediation

Use the Case 01 rubric structure:

| Criterion | 4 · Accomplished | 3 · Proficient | 2 · Developing | 1 · Beginning |

Populate concise Lunar Greenhouse-specific descriptors for each criterion.

Preserve Teacher page count.

## C1C2-T03 — Internal clue IDs visible to teachers

Teacher page 5 exposes implementation identifiers such as:

- `FLOWERS_NO_FRUIT`
- `LOW_AIRFLOW`
- `POLLEN_UNDISTURBED`
- `NO_POLLINATION_PLAN`

These are runtime/debug identifiers, not instructional content.

### Required remediation

Replace the visible clue-ID column with instructional information.

Recommended structure:

| Source | Essential evidence | Evidentiary / instructional role |

Keep the underlying evidence architecture; remove code-facing identifiers from the printable Teacher Guide.

## Answer Key verdict

**PASS**

Tasks 1 and 2 are correctly omitted as non-keyable.

Tasks 3–9 provide completed exemplars.

### Task 3

All six exact word-bank phrases are placed in sequence and the failed step is clearly identified.

### Task 4

All required fields are completed:

- failed step
- observation 1
- observation 2
- downstream result

### Task 5

Every competing diagnosis receives:

- Supported / Weakened classification
- evidence-based reason

### Task 6

Contains:

- diagnosis
- rejected alternative with evidence

### Task 7

Contains complete:

- Claim
- Evidence
- Reasoning

using multiple evidence streams and the biological process model.

### Task 8

Contains:

- design
- criterion
- constraint
- mechanism/success check

and concise acceptable variation.

### Task 9

Answers the transfer problem rather than merely restating the Lunar case diagnosis.

It appropriately explains that if pollen already reaches the stigma, investigators should move downstream to later reproductive steps.

No Answer Key remediation is recommended for Case 02.

## C1C2-ACC01 — Accessible Edition needs more hand-holding

The Accessible Edition already improves physical and visual accessibility through:

- 7 pages instead of 3
- larger base text
- larger response areas
- linear process organization
- simpler vocabulary presentation
- bullets/phrases as acceptable response modes
- dedicated full-page CER
- more breathing room

However, the final SSS standard requires more than spreading the same cognitive task across more space.

### Task 2

The Accessible prompt is essentially the Student task split into shorter sentences.

**Recommended direction:** offer broad process categories, a sentence frame, or a more explicit evidence cue.

### Task 3

The Student uses six process blanks.

The Accessible version converts them into a vertical list, but still requires the learner to independently sequence all six phrases.

**Recommended direction:**

- prefill Step 1: `viable pollen in anthers`
- optionally prefill Step 6: `fruit set`
- have the learner sequence the middle process
- or explicitly model the first relationship

This preserves the concept while reducing organizational load.

### Task 4

Accessible still requires four blank fields:

- failed step
- observation 1
- observation 2
- downstream result

**Recommended direction:** partially provide the confirmed working step and ask students to identify what should happen next, with more direct evidence prompts.

### Task 5

Accessible still requires four classifications and four evidence explanations.

This is the largest repeated-writing burden.

**Recommended direction:**

- provide some classifications
- fully model one distractor
- have students complete shorter evidence phrases
- direct students to specific case evidence
- reduce repeated full-sentence writing

### Task 6

Students still independently construct the full diagnosis and alternative rejection.

**Recommended direction:** use sentence starters and targeted prompts.

### CER

**PASS — no change recommended.**

The dedicated page uses the canonical CER subtitle and suitable case-specific reasoning guidance.

### Task 8

Still asks for all four standard engineering elements.

**Recommended direction:** provide an example support method or partially complete one element where appropriate while retaining criterion/constraint understanding.

### Task 9

The Accessible version is essentially the Student transfer question with a larger box.

**Recommended direction:** break it into a selection plus a short explanation, for example:

- first test: pollen release/transfer / fertilization / fruit growth
- what observation would show whether it is failing?

## C1C2-META01 — layout metadata copy/paste bug

The Accessible Task 8 design field is a pollination-support design, but `layout-overrides.json` labels it:

`Regolith-medium design`

The corresponding Student field is correctly labeled as a pollination-support design.

### Required remediation

Rename the Accessible authoring metadata label to:

`Pollination-support design`

or equivalent case-correct wording.

This is an editor/authoring metadata defect rather than a printed-worksheet content defect.

## C1C2-META02 — package identity metadata drift

The canonical package metadata uses:

- subtitle: `Campaign 1 · Case 02 · Pollination sequence failure`
- location: `Lunar Greenhouse`

The controlled worksheet instead displays:

`Campaign 1 · Case 02 · Shackleton Crater, Lunar South Pole`

The game identifies:

- location: `Shackleton Crater`
- subtitle: `Lunar South Pole`

### Required remediation

Synchronize canonical package identity metadata with the controlled worksheet/game identity.

This is Minor because the learner-facing worksheet itself is already coherent.

## Game / curriculum parity

**PASS**

The game and curriculum agree on the central evidence architecture:

- healthy flowers without fruit
- near-zero air movement
- viable pollen remaining undisturbed on anthers
- clean receptive stigmas
- no implemented pollination plan
- lack of effective pollen release/transfer as the first failed process

No case-changing contradiction was found.

## Grayscale

**Rendered behavior: PASS**

Case 02 has active grayscale overrides for its rendered colors and insignia fills.

Campaign maintenance identified some declared-but-unneutralized dormant palette tokens, but no actual rendered tinted grayscale surfaces were found.

Do not treat unused CSS tokens as a curriculum defect unless they can influence rendered output or provide meaningful maintenance value.

## C1C2-VIS01 — Visual modernization candidate

Task 3 currently presents a six-stage box-and-arrow process:

1 → 2 → 3 → 4 → 5 → 6

It is functional, but still reads as a conventional worksheet flowchart.

### Recommended later same-footprint redesign

Create a Lunar Greenhouse reproductive telemetry strip:

**anther/pollen → vibration → stigma → pollen tube → fertilization → fruit**

Possible treatment:

- small technical botanical glyph/cutaway per stage
- numbered telemetry node
- connecting process rail
- clear failure checkpoint treatment
- editable student response zones
- grayscale-safe line/pattern system

For the Answer Key, Step 2 should visually register as the failed node while downstream stages read as interrupted.

This is an enhancement, not a defect.

## Teacher-template comparison summary

| Page | Corrected C1 Case 01 authority | Case 02 disposition |
|---|---|---|
| 1 | Preparation / launch / diagnosis / timing / evidence / collection / fallback | Needs conversion |
| 2 | Overview / question / standards / objectives / success / vocab / materials | Needs conversion |
| 3 | Detailed procedure | Good content; normalize |
| 4 | Assessment / access / misconceptions / science status / fallback | Good content; restructure |
| 5 | Evidence architecture / reasoning / distractors / boundaries | Good base; remove runtime IDs |
| 6 | Quick + complete analytic rubric | Major missing formal rubric |
| 7 | Sources / evidence digest / fallback | Good base; normalize and remove production-oriented material |

Case 02 should not be rewritten from scratch. Most Teacher content is useful and should be poured into the corrected Case 01 structural mold.

## Final disposition

`AUDIT_COMPLETE — REMEDIATION_REQUIRED`

Owner accepted this audit for inclusion in the unified SSS remediation register.

No curriculum package changes were made during this audit.
