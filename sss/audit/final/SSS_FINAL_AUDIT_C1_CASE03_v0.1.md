# SSS Final Unified Audit — Campaign 1 Case 03

**Case:** SSS-C1-CASE03 — Mars Habitat  
**Audit phase:** Final SSS Campaign 1 + Campaign 2 unified quality audit  
**Audit status:** `AUDIT_COMPLETE — REMEDIATION_REQUIRED`  
**Owner disposition:** `OWNER_ACCEPTED`  
**Audit date:** 2026-08-07

## Frozen authority

- Curriculum baseline: `f7a24423f802a095aa149f923d05475ba2837599`
- Game baseline: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`
- Curriculum package version: `1.1`
- Package lifecycle at audit start: `APPROVED_STABLE`
- Student pages: 4
- Teacher pages: 8
- Answer Key pages: 4
- Accessible pages: 7

The approved release baseline is treated as immutable starting authority. This audit identifies post-release quality defects and enhancements; it does not challenge the mechanical validity of the prior release.

## Overall assessment

Case 03 is a strong data-analysis lesson. The plotted values are accurate, the game/curriculum evidence chain is coherent, grayscale treatment is strong, and the Accessible edition is substantially better differentiated than Cases 01–02.

The audit found Teacher-template drift, missing Teacher procedure coverage, an incomplete formal rubric, one genuine fillable-HTML response defect, several moderate Answer Key/accessibility/data-presentation issues, two minor metadata issues, and three visual-modernization candidates.

## Findings register

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| C1C3-T01 | Major | Teacher Guide substantially diverges from corrected C1 Case 01 Teacher template | Standardize |
| C1C3-T02 | Major | Detailed Teacher procedure skips Student Tasks 4 and 5 | Correct |
| C1C3-T03 | Major | `Formal rubric dimensions` is not a completed analytic rubric | Correct |
| C1C3-UI01 | Major | Task 5 diagnosis choices cannot be completed in fillable HTML mode | Correct |
| C1C3-AK01 | Moderate | Answer Key Task 4 does not visibly mirror all four Student response components | Correct |
| C1C3-AK02 | Moderate | Acceptable-alternative guidance is too thin for some open responses | Expand concisely |
| C1C3-ACC01 | Moderate quality gap | Accessible edition is genuinely differentiated but Task 6 and a few later prompts need more hand-holding | Refine |
| C1C3-DATA01 | Moderate | `700 nm+` Deep Red label creates a boundary ambiguity with the `inside 400–700 nm` prompt | Clarify |
| C1C3-T04 | Moderate | Teacher page 8 contains production/release-management material | Remove/relocate |
| C1C3-META01 | Minor | Accessible resize metadata contains stale/misleading field labels | Synchronize |
| C1C3-META02 | Minor | Package subtitle/location metadata differs from displayed/game identity | Synchronize |
| C1C3-VIS01 | Enhancement | Spectral-transmission chart is a modernization candidate | Visual phase |
| C1C3-VIS02 | Enhancement | Quantity-versus-spectrum comparison is a modernization candidate | Visual phase |
| C1C3-VIS03 | Enhancement | Mechanism chain is a modernization candidate | Visual phase |

No blocker, wrong plotted value, central diagnosis error, or substantive game/curriculum contradiction was found.

## C1C3-T01 — Teacher Edition template drift

Case 03 contains useful Teacher material but is organized as an independently designed eight-page guide rather than corrected C1 Case 01 architecture.

### Page 1

Current content includes Teacher quick start, correct diagnosis, critical values, central distinction, generic collection language, broad lesson phases, and technical fallback.

Convert to the corrected Case 01 Page 1 structure:

- preparation / before class
- game launch path
- correct diagnosis
- task-linked 60-minute flow
- essential evidence
- likely sticking point
- what to collect
- technical fallback
- teacher line

The current `Collect` box does not actually identify work products to collect.

### Page 2

Current content has objectives, standards, materials/preparation, and success criteria.

Normalize to the Case 01 Page 2 structure and restore:

- lesson overview
- guiding question
- vocabulary
- materials
- planning notes

while retaining useful case-specific content.

### Pages 4–5

Evidence architecture, spectrum analysis, mechanism, and distractor material are strong and should be retained while being reorganized into the common Teacher framework.

### Pages 7–8

References, fallback evidence, filter records, rights notes, and release-management text are split across two pages. After removing non-classroom production material, the useful evidence should be redistributed so the Teacher Guide can likely normalize to seven pages without losing instructional content.

A seven-page result is recommended only if it passes layout and print QA; the objective is template consistency, not compression for its own sake.

## C1C3-T02 — Teacher procedure skips Tasks 4 and 5

The canonical task registry contains nine tasks.

The detailed Teacher procedure explicitly references Tasks 2, 3, 6, 7, 8, and 9 but does not instruct teachers to complete:

- **4 · Connect the symptom pattern**
- **5 · Select and reject diagnoses**

Those are substantive Student tasks and occur conceptually between spectral comparison and final mechanism/CER work.

### Required remediation

Explicitly sequence:

**Tasks 2–3 → Task 4 → Task 5 → Task 6 → Task 7 → Tasks 8–9**

with appropriate timing and facilitation.

Task 1 should also be referenced more explicitly when the Teacher frames PPFD.

## C1C3-T03 — Formal analytic rubric missing

Teacher Page 6 has a useful Secure / Developing / Beginning quick rubric.

Its `Formal rubric dimensions` section only lists assessment categories. It does not provide performance-level descriptors.

### Required remediation

Use the corrected Case 01 analytic structure:

| Criterion | 4 · Accomplished | 3 · Proficient | 2 · Developing | 1 · Beginning |

Populate concise Mars Habitat-specific descriptors.

This is the same systemic defect already observed in C1 Case 02.

## C1C3-UI01 — Task 5 is not fillable digitally

Student and Accessible Task 5 present four visual diagnosis choices using decorative square spans.

The squares are not inputs, persistent response elements, radio controls, checkboxes, or keyboard-operable fillable fields. The central editor activates fillable content through response-bearing elements, so the required diagnosis selection cannot be recorded in fillable HTML mode.

Printed students can mark the boxes with pencil; digital students cannot complete the required selection.

### Required remediation

Make Task 5 a persistent, keyboard-operable, single-selection response in Student and Accessible editions.

A radio-style control is semantically preferable because exactly one diagnosis is intended, provided print/export behavior remains correct.

### Shared-system implication

Add a validation rule that every required Student/Accessible response operation has a persistent interactive or writable representation in fill mode.

## C1C3-AK01 — Task 4 exemplar field parity

Student Task 4 contains four response components:

1. interpretation of older green leaves
2. interpretation of pale new leaves
3. interpretation of healthy roots / failed nutrient additions
4. best overall pattern conclusion

The Answer Key compresses these into one correct paragraph.

The content is correct, but Curriculum Bible v1.3's completed-exemplar contract calls for visibly completing every component of a multi-part task.

### Required remediation

Use a compact completed version of the same three-row table plus the overall conclusion.

## C1C3-AK02 — Acceptable variation guidance

The Task 5 key models perchlorates as the rejected alternative, but a student can validly reject CO₂ or photoperiod when supported by specific contradictory case evidence.

Task 9 likewise allows equivalent language such as:

- PPFD + spectrum
- total photon quantity + wavelength distribution
- intensity/quantity + wavelength-resolved spectral measurement

### Required remediation

Add concise alternative-answer guidance. Do not turn the key into an exhaustive treatise.

## C1C3-ACC01 — Targeted Accessible refinement

Case 03's Accessible edition is meaningfully differentiated and does not require the Major restructuring assigned to Cases 01–02.

Strong adaptations already include:

- Task 1 split into `PPFD tells us` / `PPFD does not tell us`
- Task 2 complete data table plus direct question
- Task 3 shorter focused prompts
- Task 4 pre-supplied old/new/root facts
- larger response areas and type
- dedicated canonical CER page

### Remaining refinements

**Task 5:** shares the digital-selection defect in C1C3-UI01.

**Task 6:** still requires independent placement of all four mechanism phrases, merely in a vertical layout.

Recommended: prefill one stage, preferably `Wrong BP-4 filter installed`, then have the learner complete the remaining causal chain.

**Task 8:** already simplified well; optionally add a sentence frame such as `Brighter light changes the total ______, but the problem is the ______.`

**Task 9:** appropriately compact; no substantial change needed.

### CER

PASS. Preserve the canonical dedicated CER page, subtitle, and case-specific reasoning guidance.

## C1C3-DATA01 — 700 nm boundary ambiguity

Task 2 asks for the lowest-transmission band **inside 400–700 nm**.

The chart labels:

- Blue: 400–500 nm — 92%
- Green: 500–600 nm — 88%
- Red: 600–700 nm — 31%
- Deep red: `700 nm+` — 12%

The intended answer is Red at 31%, but `700 nm+` makes the exact 700 nm boundary visually ambiguous.

### Required remediation

Do not alter runtime values. Clarify curriculum labeling, for example:

- `Deep red · >700 nm`
- or `Deep red · above 700 nm · outside Task 2 PAR comparison`

## C1C3-T04 — Teacher-facing production/release material

Teacher Page 8 visibly contains:

- Figure rights
- Data rights and precision
- Browser physical-print gate
- release-gate / automated-check / owner-print-testing language

This is not ordinary classroom Teacher content and conflicts with Curriculum Bible v1.3's production-metadata separation rule.

### Required remediation

Remove/relocate production-facing material to audit/history/validation records.

Retain useful classroom evidence such as:

- filter replaced 47 sols ago
- required FS-7 model
- incorrect BP-4 model
- dust does not explain selective red rejection

and relocate it into evidence/mechanism/fallback sections.

## C1C3-META01 — Stale Accessible authoring labels

`layout-overrides.json` labels Accessible Task 1 response areas as `Plants observation` and `Habitat observation`, but the actual fields ask what PPFD tells us and does not tell us.

Accessible Task 4 is labeled `Diagnose the failure` although the canonical task is `Connect the symptom pattern`.

Synchronize editor metadata with actual task meaning.

## C1C3-META02 — Package identity drift

Package metadata uses:

- subtitle: `Campaign 1 · Case 03 · Light spectrum versus total intensity`
- location: `Mars Habitat`

The displayed worksheet uses:

`Campaign 1 · Case 03 · Arcadia Planitia, Mars`

The game identifies Arcadia Planitia / Mars.

Synchronize package metadata with the controlled display/game identity.

## Answer Key verdict

Core correctness: **PASS**

- Task 1 correctly distinguishes PPFD quantity from spectral distribution.
- Task 2 correctly identifies Red at 31% as the lowest in-PAR band.
- Task 3 correctly rejects low total quantity and identifies uneven spectral transmission.
- Task 5 diagnosis is correct.
- Task 6 phrase-bank sequence is correct.
- Task 7 CER is coherent.
- Tasks 8–9 correctly answer the transfer questions.

Only field-parity and concise acceptable-variation refinements are required.

## Game / curriculum parity

**PASS**

Confirmed shared values and facts include:

- combined reading: 280
- light-pipe length: 12 m
- Blue transmission: 92%
- Green transmission: 88%
- Red transmission: 31%
- Deep red transmission: 12%
- filter replaced 47 sols ago
- required filter: FS-7 FULL SPECTRUM
- incorrect filter: BP-4 BLUE PASS
- central diagnosis: wavelength-selective filtering, not low total light

No case-changing contradiction was found.

## Graph and figure accuracy

**PASS**

The plotted values accurately represent the discrete runtime measurements. Captions explicitly state that intermediate spectral values are not inferred.

The quantity-versus-spectrum comparison correctly contrasts adequate total PPFD with uneven wavelength transmission.

The figures also provide numeric labels, grayscale-safe patterns, accessible titles/descriptions, captions, and Accessible table backup.

## Grayscale

**PASS as rendered.**

No Case 03 rendered tinted-grayscale defect was identified.

## Visual modernization candidates

### C1C3-VIS01 — Spectral transmission

Redesign the ordinary four-bar graph as an exact SAA optical-transmission scan with four labeled wavelength channels, direct percentages, grayscale-safe rails/patterns, and diagnostic flags on low-transmission bands.

Do not invent a continuous spectrum.

### C1C3-VIS02 — Quantity versus spectrum

Redesign as a dual-channel diagnostic panel:

- Channel A: Total Photon Flux — 280 PPFD — `ADEQUATE`
- Channel B: Spectral Distribution — four exact transmission rails — `UNEVEN`
- diagnostic statement: `Quantity ≠ Distribution`

### C1C3-VIS03 — Mechanism chain

Replace generic rectangles with a deterministic vector chain:

surface collector → wrong filter → spectral loss → chlorophyll-production failure → pale new leaf

Use technical glyphs while preserving exact labels and the Student phrase-bank task.

## Teacher-template summary

- Page 1: substantial conversion needed
- Page 2: useful content, needs common structure
- Page 3: procedure exists but Tasks 4–5 must be restored
- Page 4: evidence content useful
- Page 5: strong mechanism/distractor content
- Page 6: quick rubric good; formal analytic rubric missing
- Page 7: source material useful; normalize format
- Page 8: redistribute useful evidence and remove production content

Likely remediation target: a seven-page Teacher Guide using corrected Case 01 architecture, if all content remains usable and layout validation passes.

## Confirmed passes / preserve

- core diagnosis and evidence chain: PASS
- game/curriculum parity: PASS
- graph numeric accuracy: PASS
- grayscale distinguishability: PASS
- figure captions/descriptions: PASS
- Accessible graph/table support: PASS
- Accessible CER: PASS / preserve
- central Answer Key answers: PASS

## Final disposition

`AUDIT_COMPLETE — REMEDIATION_REQUIRED`

Owner accepted this audit for inclusion in the unified SSS remediation register.

No curriculum package changes were made during this audit.
