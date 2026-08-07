# SSS Final Unified Audit — Remediation Register

**Document:** `SSS_FINAL_AUDIT_REMEDIATION_REGISTER_v0.1.md`  
**Status:** `ACTIVE_LIVING_REGISTER`  
**Audit branch:** `audit/sss-final-c1-c2`  
**Created:** 2026-08-07  
**Scope:** Space Sprout Sleuth Campaign 1 Cases 01–07 and Campaign 2 Cases 01–06

## 1. Frozen starting authority

The unified final SSS audit begins from these frozen release baselines:

- Curriculum: `f7a24423f802a095aa149f923d05475ba2837599`
- Game: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`
- Campaign 2 maintenance disposition: `CAMPAIGN_2_MAINTENANCE_CLOSED`
- Campaign 2 baseline disposition: `CAMPAIGN_2_BASELINE_FROZEN`

The audit does not re-question the mechanical validity of those releases. It may identify quality defects in released packages.

This branch is documentation-only during the case-audit phase. No curriculum package, shared validator, or game source remediation is authorized merely by recording a finding here.

## 2. Audit order

Cases are processed strictly in this order:

1. C1 Case 01 — ISS Greenhouse
2. C1 Case 02 — Lunar Greenhouse
3. C1 Case 03 — Mars Habitat
4. C1 Case 04 — Hayes Orbital Station
5. C1 Case 05 — Sub Surface Bunker
6. C1 Case 06 — First Contact Protocol
7. C1 Case 07 — The Gift
8. C2 Case 01 — Heavy Hands
9. C2 Case 02 — The Missing Dance
10. C2 Case 03 — The Wrong Color of Light
11. C2 Case 04 — The Silent Grove
12. C2 Case 05 — Too Clean a Room
13. C2 Case 06 — The First Garden

## 3. Audit standards locked for this phase

### Teacher Edition

Corrected C1 Case 01 is the definitive Teacher Edition structural source.

Later Teacher editions should function like the same seven-page template populated with case-specific content, including where applicable:

- Page 1: preparation, launch path, diagnosis, lesson flow, essential evidence, sticking point, collection, fallback, teacher line
- Page 2: overview, guiding question, standards, objectives, success criteria, vocabulary, materials, planning notes
- Page 3: detailed timed procedure and facilitation
- Page 4: formative checks, assessment, accessibility, misconceptions, source/science status, fallback
- Page 5: evidence architecture, reasoning path, distractors, scientific boundary, instructional emphasis
- Page 6: quick rubric plus complete analytic 4/3/2/1 rubric
- Page 7: authoritative sources, no-game evidence digest, classroom/technical fallback

Case-specific variation is permitted when the task or case genuinely requires it. Independent redesign and arbitrary scope drift are not.

### Accessible Edition

Accessible editions are hand-holding versions of the Student sheets, not separate lessons and not merely large-print reflows.

Task-specific adaptations may include:

- shorter chunks
- explicit directions
- reduced writing
- sentence starters
- word banks
- partially completed models
- prefilled evidence or classifications
- worked examples
- fewer simultaneous evidence demands
- selected-response or labeled-diagram options
- broader acceptable answers
- direct evidence cues
- more response space where justified

The essential learning goal should remain intact.

Accessible CER pages remain under the approved canonical CER contract unless an already-approved case-specific combined contract applies.

### Answer Keys

Every keyable field/subpart requires a completed exemplar. Acceptable alternatives should be concise and useful rather than exhaustive.

### Visual modernization

Visual modernization findings are recorded during case audits but implemented later on separate design/remediation work.

Primary target: figures, diagrams, graphs, maps, process models, and similar explanatory visuals. Minor surrounding polish may be recommended where it improves hierarchy without materially changing page geometry.

Do not use generative imagery for authoritative numeric graphs, labels, scales, or exact scientific diagrams where deterministic SVG/HTML/CSS is more reliable.

### Science verification

Do not repeat a broad external science-verification campaign. Check internal consistency, obvious scientific problems, and game/curriculum contradictions. External verification is reserved for a specific material uncertainty or defect.

## 4. Severity and status vocabulary

### Severity

- **Blocker** — wrong science/answer, missing essential task, game/curriculum contradiction, unusable or unreachable essential content
- **Major** — Teacher/Student mismatch, incomplete Answer Key, inadequate Accessible adaptation, missing rubric/template contract, serious print/layout problem
- **Moderate** — meaningful ambiguity, visible implementation leakage, grayscale defect, meaningful consistency/accessibility barrier
- **Minor** — metadata, wording, copy/paste, low-risk implementation or consistency issue
- **Enhancement** — worthwhile improvement that is not a release-quality defect
- **Shared-system gap** — validator/editor/process weakness that allowed or could allow defects across cases

### Remediation status

- `OPEN`
- `IN_REMEDIATION`
- `FIXED_PENDING_VALIDATION`
- `VALIDATED_PENDING_OWNER`
- `OWNER_ACCEPTED`
- `DEFERRED_VISUAL_PHASE`
- `NO_ACTION_REQUIRED`

## 5. Case audit status

| Order | Case | Audit status | Owner disposition | Audit record |
|---:|---|---|---|---|
| 1 | C1 Case 01 — ISS Greenhouse | `AUDIT_COMPLETE — REMEDIATION_REQUIRED` | `OWNER_ACCEPTED` | `SSS_FINAL_AUDIT_C1_CASE01_v0.1.md` |
| 2 | C1 Case 02 — Lunar Greenhouse | `AUDIT_COMPLETE — REMEDIATION_REQUIRED` | `OWNER_ACCEPTED` | `SSS_FINAL_AUDIT_C1_CASE02_v0.1.md` |
| 3 | C1 Case 03 — Mars Habitat | `NOT_STARTED` | — | — |
| 4 | C1 Case 04 — Hayes Orbital Station | `NOT_STARTED` | — | — |
| 5 | C1 Case 05 — Sub Surface Bunker | `NOT_STARTED` | — | — |
| 6 | C1 Case 06 — First Contact Protocol | `NOT_STARTED` | — | — |
| 7 | C1 Case 07 — The Gift | `NOT_STARTED` | — | — |
| 8 | C2 Case 01 — Heavy Hands | `NOT_STARTED` | — | — |
| 9 | C2 Case 02 — The Missing Dance | `NOT_STARTED` | — | — |
| 10 | C2 Case 03 — The Wrong Color of Light | `NOT_STARTED` | — | — |
| 11 | C2 Case 04 — The Silent Grove | `NOT_STARTED` | — | — |
| 12 | C2 Case 05 — Too Clean a Room | `NOT_STARTED` | — | — |
| 13 | C2 Case 06 — The First Garden | `NOT_STARTED` | — | — |

## 6. Open remediation findings

### Major

| ID | Case | Area | Finding | Status |
|---|---|---|---|---|
| C1C1-T01 | C1 Case 01 | Teacher | Teacher Guide skips Student Task 5 in lesson flow and detailed procedure | `OPEN` |
| C1C1-AK01 | C1 Case 01 | Answer Key | Task 3 omits required O/I exemplar fields | `OPEN` |
| C1C1-ACC01 | C1 Case 01 | Accessible | Several tasks remain too close to full Student cognitive/writing demand | `OPEN` |
| C1C2-T01 | C1 Case 02 | Teacher | Seven-page Teacher Guide does not conform to corrected Case 01 structural template | `OPEN` |
| C1C2-T02 | C1 Case 02 | Teacher rubric | Formal analytic rubric is only a list of dimensions, with no 4/3/2/1 descriptors | `OPEN` |
| C1C2-ACC01 | C1 Case 02 | Accessible | Accessible edition mostly spreads the same tasks out rather than providing enough hand-holding | `OPEN` |

### Moderate

| ID | Case | Area | Finding | Status |
|---|---|---|---|---|
| C1C1-GS01 | C1 Case 01 | Grayscale | Rendered grayscale retains tinted neutral/optional/success callout surfaces | `OPEN` |
| C1C2-T03 | C1 Case 02 | Teacher | Visible runtime clue IDs appear in Teacher evidence table | `OPEN` |

### Minor

| ID | Case | Area | Finding | Status |
|---|---|---|---|---|
| C1C2-META01 | C1 Case 02 | Editor metadata | Accessible Task 8 design resize label incorrectly says `Regolith-medium design` | `OPEN` |
| C1C2-META02 | C1 Case 02 | Package metadata | Package subtitle/location disagree with displayed worksheet/game identity | `OPEN` |

### Shared-system gaps

| ID | Origin | Finding | Status |
|---|---|---|---|
| C1C1-SYS01 | C1 Case 01 | Existing validation did not catch a numbered Student task missing from Teacher procedure or a required Student subfield missing from the Answer Key | `OPEN` |

### Visual enhancements

| ID | Case | Candidate | Status |
|---|---|---|---|
| C1C1-VIS01 | C1 Case 01 | Redesign Earth-gravity vs microgravity mechanism organizer as a same-footprint SAA technical schematic | `DEFERRED_VISUAL_PHASE` |
| C1C2-VIS01 | C1 Case 02 | Redesign six-stage pollination process as a same-footprint reproductive telemetry strip | `DEFERRED_VISUAL_PHASE` |

## 7. Confirmed passes / no-action findings

These are recorded to prevent unnecessary later reopening.

### C1 Case 01

- central diagnosis and evidence chain: PASS
- game/curriculum parity: PASS
- Tasks 1 and 2 omitted from Answer Key: correct by design
- Accessible canonical CER: PASS / preserve
- Answer Key Tasks 4–9: strong completed exemplars
- page-count change not required for currently identified defects

### C1 Case 02

- Student/Teacher numbered-task coverage: PASS
- Answer Key Tasks 3–9: PASS / complete exemplars
- game/curriculum parity: PASS
- Accessible canonical CER: PASS / preserve
- rendered grayscale behavior: PASS
- dormant tinted CSS tokens are not automatically a defect
- page-count change not required for currently identified defects

## 8. Cross-case patterns observed so far

### Teacher standardization

The first two cases already show that Teacher Guides can contain good instructional information while still drifting from a common production template.

The final remediation should prioritize **content-preserving normalization into corrected Case 01 architecture**, not wholesale Teacher rewrites.

### Accessible differentiation

Both audited cases demonstrate a recurring distinction:

- physical accessibility / larger layout may be good
- cognitive and instructional hand-holding may still be insufficient

The likely shared adaptation standard will need to explicitly encourage partial completion, worked examples, reduced repeated writing, direct evidence cues, and sentence frames.

### Answer Key validation

Case 01 demonstrates that a key can look complete while still omit a required Student subfield. Case 02 demonstrates the desired completed-exemplar pattern.

Future shared validation should mechanically compare keyable Student task fields/subparts to Answer Key coverage where feasible.

### Visual modernization

The first two candidates are both process/mechanism models that can be improved substantially without changing page footprints.

The target direction remains modern-retro scientific / SAA mission-document information design, not decorative illustration.

## 9. Remediation dependency notes

Do not begin package remediation case-by-case while the unified audit is still discovering system-wide patterns unless a newly discovered issue is truly release-blocking.

Preferred sequence after all 13 audits:

1. freeze the completed audit register
2. identify shared fixes versus case-local fixes
3. formalize corrected Teacher-template and Accessible-adaptation contracts
4. create isolated remediation branches/worktrees
5. fix shared validator/editor contracts where appropriate
6. remediate cases in controlled order
7. run current validators plus new targeted regression checks
8. owner-review remediated cases
9. perform visual-modernization phase separately
10. produce final SSS preservation/regression report and SSS→HHH production lessons

## 10. Living-document rules

After each case audit is owner accepted:

1. add/update the case row in Section 5
2. add every accepted finding to the appropriate Section 6 table
3. add important passes to Section 7
4. update cross-case patterns only when supported by multiple cases or a clear system-level implication
5. do not silently change the meaning/severity of previously accepted findings
6. if a prior audit finding is later corrected by new evidence, document the correction explicitly in both the case audit record and this register
7. visual enhancements remain separate from defects
8. historical frozen release records are not rewritten merely because a post-release audit finds a defect

## 11. Current register summary

Audits completed: **2 / 13**  
Owner accepted: **2 / 13**

Open findings currently recorded:

- Major: **6**
- Moderate: **2**
- Minor: **2**
- Shared-system gaps: **1**
- Deferred visual enhancements: **2**
- Blockers: **0**

Next audit target:

**C1 Case 03 — Mars Habitat**
