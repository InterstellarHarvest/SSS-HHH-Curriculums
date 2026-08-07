# SSS Final Unified Audit — Remediation Register

**Status:** `CASE_AUDIT_COMPLETE — REMEDIATION_OPEN`  
**Audit branch:** `audit/sss-final-c1-c2`  
**Completed:** 2026-08-07  
**Scope:** Space Sprout Sleuth Campaign 1 Cases 01–07 and Campaign 2 Cases 01–06

## 1. Frozen starting authority

- Curriculum: `f7a24423f802a095aa149f923d05475ba2837599`
- Game: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`
- Campaign 2 maintenance disposition: `CAMPAIGN_2_MAINTENANCE_CLOSED`
- Campaign 2 baseline disposition: `CAMPAIGN_2_BASELINE_FROZEN`

The thirteen-case audit is complete. The frozen release baselines remain historical authority for what was released; the findings below identify post-release quality defects and enhancements to remediate without rewriting release history.

The audit branch remained documentation-only throughout the case-audit phase. No curriculum package, shared validator, or game source was modified during these thirteen audits.

## 2. Locked audit standards

### Teacher Edition

Corrected C1 Case 01 is the definitive Teacher Edition structural source. The common target is a seven-page system serving these instructional roles:

1. preparation, launch path, diagnosis, lesson flow, essential evidence, sticking point, collection, fallback, teacher line
2. overview, guiding question, standards, objectives, success criteria, vocabulary, materials, planning notes
3. complete timed procedure and facilitation
4. formative checks, assessment, accessibility, misconceptions, source/science status, fallback
5. evidence architecture, reasoning path, distractors, scientific boundary, instructional emphasis
6. quick rubric plus complete 4/3/2/1 analytic rubric
7. authoritative sources, no-game evidence digest, classroom/technical fallback

Case-specific variation and explicitly declared multi-period implementation are permitted when genuinely required. Independent document redesign, missing rubric/source/procedure functions, and silent scope changes are not.

### Accessible Edition

Accessible editions are hand-holding versions of Student sheets, not separate lessons and not merely enlarged/reflowed copies. Appropriate adaptations include chunked directions, sentence frames, worked examples, partial completion, direct evidence cues, reduced repeated writing, selected response, prefilled classifications/model stages, and larger response space where justified.

The essential learning goal remains intact. Approved canonical CER treatment remains intact unless an already-approved case-specific combined contract applies.

### Answer Keys

Every keyable field/subpart and required visual/status/marking action requires a visible completed exemplar. Acceptable alternatives should be concise and useful. Student and Accessible prompt wording must agree with the Answer Key's accepted response space.

### Fillable HTML

Every required learner operation must have a persistent fill-mode representation. A printable checkbox, circle, X mark, or status action that cannot be recorded digitally is a defect.

### Visual modernization

Figure/diagram/data-display modernization was audited during the case reviews but is deferred to a separate design phase. Exact scientific/data graphics should remain deterministic SVG/HTML/CSS rather than generated images.

### Science verification

No broad external science re-verification was performed. The audit checked internal consistency, obvious scientific problems, source-status boundaries, numerical discipline, and game/curriculum contradictions.

## 3. Case audit status

| # | Case | Audit disposition | Stable audit record |
|---:|---|---|---|
| 1 | C1 Case 01 — ISS Greenhouse | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C1_CASE01_v0.1.md` |
| 2 | C1 Case 02 — Lunar Greenhouse | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C1_CASE02_v0.1.md` |
| 3 | C1 Case 03 — Mars Habitat | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C1_CASE03_v0.1.md` |
| 4 | C1 Case 04 — Hayes Orbital Station | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C1_CASE04_v0.1.md` |
| 5 | C1 Case 05 — Sub Surface Bunker | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C1_CASE05_v0.1.md` |
| 6 | C1 Case 06 — First Contact Protocol | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C1_CASE06_v0.1.md` |
| 7 | C1 Case 07 — The Gift | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C1_CASE07_v0.1.md` |
| 8 | C2 Case 01 — Heavy Hands | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C2_CASE01_v0.1.md` |
| 9 | C2 Case 02 — The Missing Dance | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C2_CASE02_v0.1.md` |
| 10 | C2 Case 03 — The Wrong Color of Light | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C2_CASE03_v0.1.md` |
| 11 | C2 Case 04 — The Silent Grove | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C2_CASE04_v0.1.md` |
| 12 | C2 Case 05 — Too Clean a Room | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C2_CASE05_v0.1.md` |
| 13 | C2 Case 06 — The First Garden | `OWNER_ACCEPTED · REMEDIATION_REQUIRED` | `SSS_FINAL_AUDIT_C2_CASE06_v0.1.md` |

## 4. Major remediation register

All findings below are `OPEN` unless otherwise stated.

### Campaign 1

- `C1C1-T01` — Teacher procedure skips Student Task 5.
- `C1C1-AK01` — Answer Key Task 3 omits required O/I fields.
- `C1C1-ACC01` — several Accessible tasks remain insufficiently hand-holding.
- `C1C2-T01` — Teacher Guide does not conform to corrected Case 01 structure.
- `C1C2-T02` — full analytic 4/3/2/1 rubric missing.
- `C1C2-ACC01` — Accessible edition insufficiently hand-holding.
- `C1C3-T01` — Teacher Guide structural drift / eight pages.
- `C1C3-T02` — Teacher procedure skips Tasks 4 and 5.
- `C1C3-T03` — complete analytic rubric missing.
- `C1C3-UI01` — required diagnosis selection cannot be persisted in fillable HTML.
- `C1C4-T01` — Teacher Guide page roles drift from common template.
- `C1C4-T02` — authoritative Teacher source list absent.
- `C1C4-T03` — common quick + analytic rubric system absent.
- `C1C4-UI01` — required diagnosis selection cannot be persisted digitally.
- `C1C5-T01` — Teacher Guide structural drift / eight pages.
- `C1C5-T02` — detailed facilitation explicitly covers only Tasks 3, 5, and 7.
- `C1C5-T03` — full analytic rubric contract absent.
- `C1C5-UI01` — best-supported diagnosis selection has no persisted digital control.
- `C1C6-T01` — Teacher Guide structural drift / eight pages.
- `C1C6-T02` — Teacher assessment matrix does not use common rubric contract.
- `C1C6-UI01` — best-supported diagnosis selection has no persisted digital control.
- `C1C7-T01` — Teacher Guide structural drift / eight pages.
- `C1C7-UI01` — best-supported diagnosis selection has no persisted digital control.
- `C1C7-UI02` — required missing-stage X/status markings in Task 4 lack persisted digital controls.
- `C1C7-AK01` — Answer Key Task 4 omits the required missing-stage X/status subpart.

### Campaign 2

- `C2C1-T01` — nine-page Teacher Guide diverges from common template.
- `C2C1-T02` — Teacher fallback explicitly permits reducing required five-source Task 5 to three sources.
- `C2C1-T03` — Teacher rubric uses only three performance levels.
- `C2C1-ACC01` — Accessible Tasks 5–6 remain too close to the full Student workload.
- `C2C2-T01` — eight-page Teacher Guide diverges from common template.
- `C2C2-T02` — Teacher rubric uses only three performance levels.
- `C2C2-ACC01` — Accessible Tasks 5–6 remain too close to the full Student workload.
- `C2C3-T01` — eight-page Teacher Guide diverges from common template.
- `C2C3-T02` — Teacher rubric uses only Full/Partial levels.
- `C2C3-ACC01` — Accessible Task 5 requires ten source-analysis responses plus synthesis.
- `C2C4-T01` — eight-page Teacher Guide diverges from common template.
- `C2C4-T02` — Teacher rubric uses only Full/Partial levels.
- `C2C4-ACC01` — Accessible Task 5 requires ten source-analysis responses plus synthesis.
- `C2C4-ACC02` — Accessible Task 8 explicitly permits choosing the five-hour trial minimum while Student/Teacher/Answer guidance expects a specification above that minimum using the historically supported six-hour schedule.
- `C2C5-T01` — nine-page Teacher Guide diverges from common template.
- `C2C5-T02` — Teacher Guide contains no common quick rubric or 4/3/2/1 analytic rubric.
- `C2C5-T03` — Teacher Guide has source-status prose but no printed authoritative reference list.
- `C2C5-ACC01` — Accessible Task 4 requires ten source-analysis responses plus synthesis.
- `C2C6-T01` — eight-page Teacher Guide diverges from common template.
- `C2C6-T02` — Teacher Guide has task notes but no coherent timed procedure / class-flow route.
- `C2C6-T03` — Teacher Guide contains no common quick rubric or 4/3/2/1 analytic rubric.
- `C2C6-T04` — Teacher Guide has science-boundary prose but no printed authoritative reference list.
- `C2C6-ACC01` — Accessible Task 4 requires ten source-analysis responses plus synthesis.

## 5. Moderate remediation register

### Campaign 1

- `C1C1-GS01` — rendered grayscale retains tinted callout surfaces.
- `C1C2-T03` — runtime clue IDs visible in Teacher content.
- `C1C3-AK01` — Task 4 key does not visibly mirror all Student response fields.
- `C1C3-AK02` — accepted-alternative guidance too thin for some open responses.
- `C1C3-ACC01` — targeted Accessible hand-holding still needed.
- `C1C3-DATA01` — `700 nm+` creates a boundary ambiguity with the 400–700 nm task.
- `C1C3-T04` — production/release-management material appears in the Teacher Guide.
- `C1C4-T04` — runtime clue IDs visible in Teacher content.
- `C1C4-T05` — Teacher Guide states an incorrect Accessible page count.
- `C1C4-ACC01` — Accessible Tasks 5 and 7 need targeted refinement.
- `C1C5-T04` — internal game-node paths are printed in Teacher content.
- `C1C5-ACC01` — Accessible mechanism sequencing needs partial completion.
- `C1C5-ID01` — learner-facing curriculum/game location identity drift.
- `C1C6-ACC01` — Accessible diagnosis/intervention workload needs targeted partial scaffolding.
- `C1C7-T02` — Teacher pacing places intervention before CER contrary to registry/Student order.
- `C1C7-ACC01` — Accessible Tasks 4, 5, and 7 need targeted scaffolding.

### Campaign 2

- `C2C1-T04` — undeclared core route totals 105 minutes.
- `C2C2-PACE01` — undeclared core route totals 110 minutes.
- `C2C2-TASK01` — `OK / ?` coding conflates whether an observation is established with whether it remains diagnostically important.
- `C2C3-PACE01` — undeclared core route totals 125 minutes.
- `C2C4-PACE01` — undeclared core route totals 140 minutes.
- `C2C5-ACC02` — Accessible Task 5 still requires four B/R marks, three written rejections, and all three mechanism stages despite useful supports.
- `C2C6-ACC02` — Accessible Task 3 still requires four B/R marks plus three written alternative rejections despite useful context.

C2 Case 05's explicitly declared two-period route is **not** a pacing defect. It demonstrates the preferred way to handle a legitimately longer case.

## 6. Minor remediation register

- `C1C2-META01` — wrong Accessible resize label for Task 8.
- `C1C2-META02` — package identity metadata drift.
- `C1C3-META01` — stale/misleading editor resize labels.
- `C1C3-META02` — package identity metadata drift.

## 7. Shared-system gaps

- `C1C1-SYS01` — validate Teacher task coverage and Answer Key subfield coverage against Student requirements.
- `C1C3-SYS01` — every required learner operation must have a persistent fill-mode representation.
- `C1C4-SYS01` — reject visible runtime IDs and verify cross-role page references/counts.
- `C1C5-SYS01` — reject internal game-node navigation paths from Teacher-facing content.
- `C1C7-SYS01` — Answer Key validation must include required visual/status subparts, not text fields only.
- `C2C1-SYS01` — default fallback/differentiation may not silently reduce registry-defined graded scope.
- `C2C4-SYS01` — Student/Accessible prompt wording must agree with Answer Key acceptance criteria.
- `C2C6-SYS01` — Teacher package validation should require the common functional set: usable procedure/class flow, rubric system, and authoritative source function rather than merely a fixed page count.

## 8. Deferred visual-modernization catalog

**35 enhancements identified; all status `DEFERRED_VISUAL_PHASE`.**

### C1

- `C1C1-VIS01` — gravity vs microgravity mechanism schematic.
- `C1C2-VIS01` — pollination telemetry/process strip.
- `C1C3-VIS01` — optical-transmission channels.
- `C1C3-VIS02` — quantity-vs-spectrum diagnostic panel.
- `C1C3-VIS03` — spectral-loss/chlorophyll mechanism chain.
- `C1C4-VIS01` — incident/change timeline.
- `C1C4-VIS02` — repeating reactor-failure loop.
- `C1C4-VIS03` — reactor-control feedback schematic.
- `C1C5-VIS01` — radiation-to-growth hazard pathway.
- `C1C5-VIS02` — four-source evidence convergence.
- `C1C5-VIS03` — engineering requirements panel.
- `C1C6-VIS01` — docking/signal timing strip.
- `C1C6-VIS02` — atmosphere→signal→network→partnership systems model.
- `C1C6-VIS03` — signal-safe intervention comparison.
- `C1C7-VIS01` — matched-primary vs trace-context diagnostic.
- `C1C7-VIS02` — mature-source→cue→path→receptor→commitment→symbiosis model.
- `C1C7-VIS03` — intervention decision/monitoring matrix.

### C2

- `C2C1-VIS01` — tuber-span / size-dependence figure.
- `C2C1-VIS02` — across-bed radial-profile telemetry.
- `C2C1-VIS03` — missing-specification / design-comparison panel.
- `C2C2-VIS01` — poricidal-cone cutaway.
- `C2C2-VIS02` — vibration→pollen-release pathway.
- `C2C2-VIS03` — four-setting safe-trial control panel.
- `C2C3-VIS01` — GRO-9 discrete spectrum display.
- `C2C3-VIS02` — response-band vs fixture-output diagnostic.
- `C2C3-VIS03` — spectral-match mechanism/specification panel.
- `C2C4-VIS01` — same-total/different-pattern timing figure.
- `C2C4-VIS02` — discrete within-cycle signalling record.
- `C2C4-VIS03` — dark-period specification / monitored-trial panel.
- `C2C5-VIS01` — detection-limit teaching graphic.
- `C2C5-VIS02` — six-month production-monitor display.
- `C2C5-VIS03` — species-specific signal/pathway/product + safe-trial panel.
- `C2C6-VIS01` — site-survey patch diagnostic.
- `C2C6-VIS02` — candidate mycorrhizal pathway.
- `C2C6-VIS03` — screened/approved ecological trial panel.

## 9. Confirmed strengths to preserve

- Core case diagnoses/evidence chains and frozen game/curriculum parity generally hold across the audited set; no Blocker was found.
- Later Campaign 1 and Campaign 2 packages show increasingly strong source-status, numerical-precision, and uncertainty controls.
- C1 Case 07 demonstrates that a complete four-level analytic rubric can coexist with complex case-specific content.
- C2 Answer Keys are generally strong completed-exemplar models.
- C2 Cases 01–06 use persisted status fields and avoid the print-only digital-selection defects found in C1 Cases 03–07.
- Accessible canonical CER treatment is consistently strong and should be preserved.
- C2 Cases 02–06 are especially strong at preserving inequalities, ranges, reporting thresholds, modeled-vs-measured distinctions, missing values, and case-specific boundaries.
- Cases 05–07 of C1 and all C2 cases provide valuable examples of explicit uncertainty language and of ending in a monitored test/engineering decision rather than pretending the evidence already proves intervention success.

## 10. Cross-case remediation streams

### Stream A — Teacher Edition normalization

Normalize later Teacher Guides into the corrected Case 01 functional architecture without discarding good case-specific content. Key recurring defects:

- independent page organization
- missing or inconsistent rubric systems
- incomplete/absent timed procedure
- absent authoritative reference list in some cases
- code/runtime implementation leakage
- hidden 105–140 minute routes rather than declared class-period planning

### Stream B — Accessible adaptation standard

Formalize the hand-holding standard now demonstrated by the strongest later cases:

- model one row in repeated evidence tables
- prefill selected contribution/limit cells
- model one rejected alternative
- prefill one mechanism stage when sequencing load is high
- preserve useful separate response fields rather than collapsing them
- reduce writing load without changing accepted answer space
- keep canonical CER structure

The five-source `contribution + limit` task family is the clearest systemic target: C2 Cases 01–06 repeatedly reproduce 10 open source cells plus synthesis.

### Stream C — Fillable-response validation

Add validation for required non-text learner operations:

- diagnosis selection
- status/classification marking
- X/missing-stage marking
- other printed-only interactions

### Stream D — Answer Key traceability

Validate every Student/Accessible requirement against a visible key exemplar, including table rows, labels, status marks, and visual subparts.

### Stream E — Classroom-facing implementation hygiene

Reject:

- runtime clue IDs
- internal node paths
- production/release-management text
- stale cross-role page references

### Stream F — Identity and metadata synchronization

Compare package metadata, printed subtitle/location, and frozen game identity systematically.

### Stream G — Visual modernization

Modernize the 35 recorded figure families after correctness remediation. Target modern-retro SAA technical documentation; preserve exact data and current page footprints wherever practical.

## 11. Recommended remediation order

1. Freeze this completed audit register as the accepted finding baseline.
2. Write the corrected Teacher Edition template contract and Accessible adaptation standard from the audit evidence.
3. Implement shared validator/editor checks before mass package remediation where possible.
4. Remediate systemic Teacher structure/rubric/source/procedure defects.
5. Remediate Accessible repeated-workload patterns.
6. Fix Answer Key and fillable-response defects.
7. Fix moderate/minor identity, metadata, grayscale, and classroom-facing leakage issues.
8. Run current validators plus new targeted regression contracts.
9. Perform owner review of remediated cases.
10. Run visual-modernization work separately.
11. Produce final preservation/regression report and SSS→HHH production lessons.

## 12. Final case-audit summary

Audits complete / owner accepted: **13 / 13**

- **Blockers: 0**
- **Major findings: 48**
- **Moderate findings: 23**
- **Minor findings: 4**
- **Shared-system gaps: 8**
- **Deferred visual enhancements: 35**

The thirteen-case discovery/audit phase is complete. The next phase is controlled remediation, not further case discovery.
