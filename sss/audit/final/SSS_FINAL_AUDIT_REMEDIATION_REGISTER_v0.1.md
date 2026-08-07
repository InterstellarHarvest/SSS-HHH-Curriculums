# SSS Final Unified Audit — Remediation Register

**Document:** `SSS_FINAL_AUDIT_REMEDIATION_REGISTER_v0.1.md`  
**Status:** `ACTIVE_LIVING_REGISTER`  
**Audit branch:** `audit/sss-final-c1-c2`  
**Updated:** 2026-08-07  
**Scope:** Space Sprout Sleuth Campaign 1 Cases 01–07 and Campaign 2 Cases 01–06

## 1. Frozen starting authority

- Curriculum: `f7a24423f802a095aa149f923d05475ba2837599`
- Game: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`
- Campaign 2 maintenance disposition: `CAMPAIGN_2_MAINTENANCE_CLOSED`
- Campaign 2 baseline disposition: `CAMPAIGN_2_BASELINE_FROZEN`

The audit does not re-question the mechanical validity of those releases. It may identify quality defects in released packages. This branch is documentation-only during the case-audit phase.

## 2. Audit order

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

## 3. Locked audit standards

### Teacher Edition
Corrected C1 Case 01 is the definitive Teacher Edition structural source. Target seven-page architecture:
1. preparation / launch / diagnosis / lesson flow / essential evidence / sticking point / collection / fallback
2. overview / guiding question / standards / objectives / success criteria / vocabulary / materials
3. detailed timed procedure and facilitation
4. formative checks / assessment / accessibility / misconceptions / source-science status / fallback
5. evidence architecture / reasoning / distractors / scientific boundary
6. quick rubric + complete 4/3/2/1 analytic rubric
7. authoritative sources / no-game evidence digest / classroom-technical fallback

### Accessible Edition
Accessible editions are hand-holding versions of Student sheets, not separate lessons and not merely enlarged reflows. Use task-specific chunking, sentence frames, direct evidence cues, partial completion, selected response, worked examples, reduced repeated writing, and larger response areas where justified. Preserve essential learning goals and canonical CER.

### Answer Keys
Every keyable field/subpart requires a visible completed exemplar. Accepted alternatives should be concise and useful.

### Visual modernization
Record exact-data figures, diagrams, timelines, process models, and engineering schematics for later separate design remediation. Authoritative numeric graphics remain deterministic SVG/HTML/CSS.

### Science verification
No broad external science re-verification. Check internal consistency, obvious science errors, and game/curriculum contradictions.

## 4. Severity / status vocabulary

**Blocker** wrong science/answer, missing essential task, contradiction, unusable essential content.  
**Major** Teacher/Student mismatch, incomplete key, inadequate Accessible adaptation, missing template/rubric contract, serious functional/layout problem.  
**Moderate** meaningful ambiguity, implementation leakage, grayscale defect, consistency/accessibility barrier.  
**Minor** metadata/wording/copy-paste/low-risk implementation issue.  
**Enhancement** worthwhile non-defect improvement.  
**Shared-system gap** validator/editor/process weakness.

Statuses: `OPEN` · `IN_REMEDIATION` · `FIXED_PENDING_VALIDATION` · `VALIDATED_PENDING_OWNER` · `OWNER_ACCEPTED` · `DEFERRED_VISUAL_PHASE` · `NO_ACTION_REQUIRED`

## 5. Case audit status

| # | Case | Audit status | Owner disposition | Record |
|---:|---|---|---|---|
| 1 | C1 Case 01 — ISS Greenhouse | `AUDIT_COMPLETE — REMEDIATION_REQUIRED` | `OWNER_ACCEPTED` | `SSS_FINAL_AUDIT_C1_CASE01_v0.1.md` |
| 2 | C1 Case 02 — Lunar Greenhouse | `AUDIT_COMPLETE — REMEDIATION_REQUIRED` | `OWNER_ACCEPTED` | `SSS_FINAL_AUDIT_C1_CASE02_v0.1.md` |
| 3 | C1 Case 03 — Mars Habitat | `AUDIT_COMPLETE — REMEDIATION_REQUIRED` | `OWNER_ACCEPTED` | `SSS_FINAL_AUDIT_C1_CASE03_v0.1.md` |
| 4 | C1 Case 04 — Hayes Orbital Station | `AUDIT_COMPLETE — REMEDIATION_REQUIRED` | `OWNER_ACCEPTED` | `SSS_FINAL_AUDIT_C1_CASE04_v0.1.md` |
| 5 | C1 Case 05 — Sub Surface Bunker | `AUDIT_COMPLETE — REMEDIATION_REQUIRED` | `OWNER_ACCEPTED` | `SSS_FINAL_AUDIT_C1_CASE05_v0.1.md` |
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
| C1C1-T01 | C1C1 | Teacher | Teacher procedure skips Student Task 5 | `OPEN` |
| C1C1-AK01 | C1C1 | Answer Key | Task 3 omits required O/I exemplar fields | `OPEN` |
| C1C1-ACC01 | C1C1 | Accessible | Several tasks remain too close to full Student demand | `OPEN` |
| C1C2-T01 | C1C2 | Teacher | Teacher Guide does not conform to corrected Case 01 template | `OPEN` |
| C1C2-T02 | C1C2 | Rubric | Formal analytic rubric lacks 4/3/2/1 descriptors | `OPEN` |
| C1C2-ACC01 | C1C2 | Accessible | Insufficient hand-holding differentiation | `OPEN` |
| C1C3-T01 | C1C3 | Teacher | Eight-page Teacher Guide diverges from corrected template | `OPEN` |
| C1C3-T02 | C1C3 | Teacher | Detailed procedure skips Tasks 4 and 5 | `OPEN` |
| C1C3-T03 | C1C3 | Rubric | Formal rubric lacks full 4/3/2/1 descriptors | `OPEN` |
| C1C3-UI01 | C1C3 | Fillable HTML | Required diagnosis selection cannot be stored digitally | `OPEN` |
| C1C4-T01 | C1C4 | Teacher | Teacher pages do not serve common template roles | `OPEN` |
| C1C4-T02 | C1C4 | Teacher sources | Authoritative source list absent | `OPEN` |
| C1C4-T03 | C1C4 | Rubric | Common quick + full analytic rubric absent | `OPEN` |
| C1C4-UI01 | C1C4 | Fillable HTML | Required diagnosis selection cannot be stored digitally | `OPEN` |
| C1C5-T01 | C1C5 | Teacher | Eight-page Teacher Guide diverges from corrected seven-page template | `OPEN` |
| C1C5-T02 | C1C5 | Teacher | Detailed facilitation explicitly covers only Tasks 3, 5, and 7 | `OPEN` |
| C1C5-T03 | C1C5 | Rubric | Full 4/3/2/1 analytic rubric contract absent | `OPEN` |
| C1C5-UI01 | C1C5 | Fillable HTML | Task 4 best-diagnosis selection has no persisted digital control | `OPEN` |

### Moderate

| ID | Case | Area | Finding | Status |
|---|---|---|---|---|
| C1C1-GS01 | C1C1 | Grayscale | Rendered grayscale retains tinted callout surfaces | `OPEN` |
| C1C2-T03 | C1C2 | Teacher | Runtime clue IDs visible | `OPEN` |
| C1C3-AK01 | C1C3 | Answer Key | Task 4 does not visibly mirror all Student subfields | `OPEN` |
| C1C3-AK02 | C1C3 | Answer Key | Accepted-alternative guidance too thin | `OPEN` |
| C1C3-ACC01 | C1C3 | Accessible | Targeted hand-holding still needed | `OPEN` |
| C1C3-DATA01 | C1C3 | Data | `700 nm+` boundary ambiguity | `OPEN` |
| C1C3-T04 | C1C3 | Teacher | Production/release-management material printed | `OPEN` |
| C1C4-T04 | C1C4 | Teacher | Runtime clue IDs visible | `OPEN` |
| C1C4-T05 | C1C4 | Teacher | Wrong Accessible page count | `OPEN` |
| C1C4-ACC01 | C1C4 | Accessible | Task 5 and Task 7 need stronger structure | `OPEN` |
| C1C5-T04 | C1C5 | Teacher | Internal game navigation-node paths printed | `OPEN` |
| C1C5-ACC01 | C1C5 | Accessible | Task 5 remains nearly full sequencing demand | `OPEN` |
| C1C5-ID01 | C1C5 | Identity | Curriculum learner-facing location disagrees with frozen game / approved location decision | `OPEN` |

### Minor

| ID | Case | Area | Finding | Status |
|---|---|---|---|---|
| C1C2-META01 | C1C2 | Editor metadata | Wrong Accessible Task 8 resize label | `OPEN` |
| C1C2-META02 | C1C2 | Package metadata | Identity metadata drift | `OPEN` |
| C1C3-META01 | C1C3 | Editor metadata | Stale/misleading response labels | `OPEN` |
| C1C3-META02 | C1C3 | Package metadata | Identity metadata drift | `OPEN` |

### Shared-system gaps

| ID | Origin | Finding | Status |
|---|---|---|---|
| C1C1-SYS01 | C1C1 | Cross-role validation should catch missing Teacher task coverage and missing Answer Key subfields | `OPEN` |
| C1C3-SYS01 | C1C3 | Validate persistent fill-mode representation for every required response action | `OPEN` |
| C1C4-SYS01 | C1C4 | Reject visible runtime IDs and verify declared cross-role page-count references | `OPEN` |
| C1C5-SYS01 | C1C5 | Reject internal game-node navigation paths from classroom Teacher content | `OPEN` |

### Visual enhancements

| ID | Case | Candidate | Status |
|---|---|---|---|
| C1C1-VIS01 | C1C1 | Earth-gravity vs microgravity mechanism schematic | `DEFERRED_VISUAL_PHASE` |
| C1C2-VIS01 | C1C2 | Pollination telemetry strip | `DEFERRED_VISUAL_PHASE` |
| C1C3-VIS01 | C1C3 | Optical-transmission channels | `DEFERRED_VISUAL_PHASE` |
| C1C3-VIS02 | C1C3 | Quantity-vs-spectrum diagnostic panel | `DEFERRED_VISUAL_PHASE` |
| C1C3-VIS03 | C1C3 | Spectral-loss/chlorophyll mechanism chain | `DEFERRED_VISUAL_PHASE` |
| C1C4-VIS01 | C1C4 | Incident timeline | `DEFERRED_VISUAL_PHASE` |
| C1C4-VIS02 | C1C4 | Reactor failure loop | `DEFERRED_VISUAL_PHASE` |
| C1C4-VIS03 | C1C4 | Reactor-control feedback schematic | `DEFERRED_VISUAL_PHASE` |
| C1C5-VIS01 | C1C5 | Radiation-to-growth hazard pathway | `DEFERRED_VISUAL_PHASE` |
| C1C5-VIS02 | C1C5 | Four-source evidence convergence schematic | `DEFERRED_VISUAL_PHASE` |
| C1C5-VIS03 | C1C5 | Engineering requirements panel | `DEFERRED_VISUAL_PHASE` |

## 7. Confirmed passes / preserve

### C1C1
Core diagnosis/evidence PASS; game/curriculum parity PASS; Accessible CER preserve; most Answer Key exemplars strong.

### C1C2
Teacher task coverage PASS; Answer Key PASS; game/curriculum parity PASS; Accessible CER preserve; rendered grayscale PASS.

### C1C3
Diagnosis/evidence PASS; game/curriculum parity PASS; graph numeric accuracy PASS; grayscale PASS; figure descriptions PASS; Accessible CER preserve.

### C1C4
All Student tasks covered in Teacher procedure PASS; Answer Key PASS; game/curriculum parity PASS; science qualification strong; Accessible CER preserve; grayscale PASS.

### C1C5
Answer Key complete PASS; four-source evidence model strong; radiation/exposure uncertainty language strong; science qualification strong; Accessible CER preserve; game/curriculum science/evidence parity PASS.

## 8. Cross-case patterns

### Teacher standardization
Teacher drift persists through Cases 02–05. Seven-page count alone is insufficient; page roles must be common. Cases 02–05 all fail the definitive rubric contract in different ways. Cases 01, 03, and 05 have incomplete detailed procedure traceability.

### Accessible differentiation
Cases 03–05 show the preferred direction: chunked prompts, direct facts, sentence frames, linear organizers. Mechanism-sequencing tasks remain a recurring place where partial completion is needed. Do not collapse useful Student structure in Accessible editions.

### Answer Key validation
Require visible subfield correspondence, not merely generally correct paragraphs. Case 05 is a strong completed-exemplar model.

### Fillable-response validation
Cases 03–05 confirm a systemic required-selection problem: printed choice/circle tasks can lack persisted digital selection controls.

### Implementation leakage
Cases 02 and 04 expose runtime clue IDs; Case 05 exposes game node paths. Classroom-facing Teacher content should use durable visible labels, not internal code identifiers.

### Identity synchronization
Case 05 introduces a learner-facing curriculum/game location mismatch. Identity fields should be checked across package metadata, worksheet subtitle, and game-facing case identity.

### Visual modernization
Candidate families: mechanism pathways, evidence convergence, scientific data panels, timelines, recurrence loops, engineering control/requirements diagrams.

## 9. Post-audit remediation sequence

1. freeze completed register
2. separate shared vs case-local fixes
3. formalize Teacher-template and Accessible-adaptation contracts
4. create isolated remediation branches/worktrees
5. fix shared validator/editor contracts
6. remediate cases in controlled order
7. run current + targeted new regression checks
8. owner-review remediated cases
9. perform visual phase separately
10. final preservation/regression report + SSS→HHH production lessons

## 10. Living-document rules

After each accepted case audit, update case status, findings, passes, and supported cross-case patterns. Do not silently alter prior accepted findings. Keep visual enhancements separate from defects. Historical frozen release records remain historical.

## 11. Current summary

Audits completed: **5 / 13**  
Owner accepted: **5 / 13**

- Blockers: **0**
- Major: **18**
- Moderate: **13**
- Minor: **4**
- Shared-system gaps: **4**
- Deferred visual enhancements: **11**

Next audit target: **C1 Case 06 — First Contact Protocol**
