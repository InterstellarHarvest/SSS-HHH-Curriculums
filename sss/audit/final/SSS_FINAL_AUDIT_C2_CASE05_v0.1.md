# SSS Final Unified Audit — Campaign 2 Case 05

**Case:** SSS-C2-CASE05 — Too Clean a Room  
**Audit status:** `AUDIT_COMPLETE — REMEDIATION_REQUIRED`  
**Owner disposition:** `OWNER_ACCEPTED`  
**Audit date:** 2026-08-07

## Frozen authority

- Curriculum: `f7a24423f802a095aa149f923d05475ba2837599`
- Game: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`
- Package version: `1.1`
- Student pages: 7
- Teacher pages: 9
- Answer Key pages: 5
- Accessible pages: 7

Campaign 2 release integrity is accepted. This audit concerns instructional quality and cross-case consistency only.

## Overall assessment

Too Clean a Room is one of the most careful science-boundary packages in SSS. It keeps absorbed dose in milligray, refuses conversion to sievert without weighting factors, preserves the `<0.01 mGy/day` inequality, separates a surveyed site record from a modeled comparison, keeps the species-specific pathway bounded, and ends in a monitored trial rather than an operational radiation prescription.

The Answer Key is complete and the required learner actions are digitally represented. Remediation is required for Teacher-template conformity, the complete absence of the shared grading-rubric system and printed reference list, and the recurring five-source workload in the Accessible edition.

## Findings

| ID | Severity | Finding |
|---|---|---|
| C2C5-T01 | Major | Nine-page Teacher Guide does not conform to corrected C1 Case 01 seven-page architecture |
| C2C5-T02 | Major | Teacher Guide contains task notes but no quick rubric and no complete 4/3/2/1 analytic rubric |
| C2C5-T03 | Major | Teacher Guide contains source-status prose but no printed authoritative reference list for the Earth-science comparisons |
| C2C5-ACC01 | Major quality gap | Accessible Task 4 still requires ten source-analysis responses plus synthesis |
| C2C5-ACC02 | Moderate quality gap | Accessible Task 5 still requires four B/R marks, three written rejections, and all three open mechanism stages despite otherwise useful supports |
| C2C5-VIS01 | Enhancement | Detection-limit teaching figure modernization |
| C2C5-VIS02 | Enhancement | Six-month production-decline figure modernization |
| C2C5-VIS03 | Enhancement | Species-specific signal→pathway→product model / monitored-trial panel modernization |

## C2C5-T01 — Teacher template drift

The Teacher Guide uses nine pages organized around purpose/objectives, standards, vocabulary/source status, science boundaries, misconception corrections, task notes, precision ledger, and running/access framing.

The content is strong, but it functions as another independent Teacher-document design rather than the corrected Case 01 template.

### Required remediation

Normalize the existing material into the common seven-page architecture, preserving:

- the unusually strong species-specific safety boundary
- established Earth science versus case-specific evidence versus modeled evidence
- precision/detection-limit cautions
- misconception corrections
- task-specific marking notes
- explicit two-period implementation note where needed

The declared two-period route is a legitimate case-specific instructional variation. The defect is not that this case takes two periods; it is that the Teacher pages do not use the common instructional architecture.

## C2C5-T02 — no shared grading rubric

Teacher Pages 6–7 provide useful task-by-task notes and marking guidance, but the nine-page Teacher Guide contains no quick rubric and no four-level analytic rubric.

This is a stronger rubric defect than the two- or three-level C2 cases: there is no common performance-level rubric at all.

### Required remediation

Create the common Page 6-equivalent structure:

1. quick `Secure / Developing / Beginning` rubric
2. complete `4 / 3 / 2 / 1` analytic rubric

Use the existing case-specific success criteria as source material: reading precision, unit discipline, null-result use, bounded claims, mechanism order, and safe/testable engineering specification.

## C2C5-T03 — authoritative references absent

The Teacher Guide has an excellent source-status ledger and discusses established Earth radiation science and the 2007 melanized-fungi study, but no classroom-facing authoritative reference list or source URLs/citations are printed in the Teacher Guide.

### Required remediation

Restore the Case 01 final-page source function by listing the controlled authoritative sources already used during package production. Do not initiate a new broad science-research campaign merely to rewrite the case.

## Student → Teacher task coverage

**PASS / preserve**

Teacher task-note pages explicitly cover Tasks 1–7, and the running note identifies a coherent two-period division:

- Period 1: Tasks 1–3
- Period 2: Tasks 4–7

The detailed substance should be preserved during template normalization.

## Answer Key verdict

**PASS / preserve**

The Answer Key visibly completes all seven tasks:

- Task 1: all six M/N classifications + explanation
- Task 2: detection-limit, unit, and modeled-value subparts
- Task 3: onset month, delayed-decline reasoning, and five null-result interpretation
- Task 4: all five source contribution/limit pairs + synthesis
- Task 5: all B/R diagnoses, all three rejections, and all mechanism stages
- Task 6: complete bounded CER
- Task 7: measurement criterion, non-exposed comparison chamber, constraint, minimum-effective-exposure reasoning, and policy recommendation

Accepted variation is appropriately broad where multiple constraints/recommendations are defensible.

## C2C5-ACC01 — five-source workload remains too high

Accessible Tasks 1–3 are genuinely scaffolded through simpler vocabulary, a detection-limit analogy, direct tables, sentence frames, and shorter wording.

Task 4 still requires:

- 5 contribution responses
- 5 limitation responses
- 1 synthesis response

for **11 independent open responses**, essentially the Student workload with simpler prose.

### Required remediation

Model one complete source row and prefill selected contribution/limit cells so the learner demonstrates the source-limit distinction without performing all ten pairings independently.

## C2C5-ACC02 — diagnosis/mechanism task still dense

Accessible Task 5 improves wording and supplies a useful evidence word bank, but still asks learners to:

- mark four diagnoses B/R
- write evidence against all three rejected alternatives
- sequence all three mechanism phrases

### Recommended remediation

Model one rejected alternative or prefill one evidence rejection, and consider supplying one middle mechanism stage. Preserve the learner’s responsibility to identify the best diagnosis and causal order.

This is Moderate rather than Major because the task already contains materially better support than the Standard edition.

## CER

**PASS — preserve.**

Accessible CER remains on a dedicated page with the canonical subtitle, direct source-count reduction, required qualifiers, and sentence frames.

## Fillable HTML

**PASS**

M/N classifications, B/R diagnosis marks, mechanism stages, CER fields, and engineering responses all have persisted writable controls. No C1-style print-only selection defect was found.

## Game / curriculum parity

**PASS**

Runtime identity matches:

- Concord Botanical Vault
- Lagrange Point 5
- Concord Neutral Zone

The task registry is explicitly pinned to the frozen game commit. Core case evidence and diagnosis are consistent with the released Campaign 2 investigation.

## Science / numerical / safety discipline

**PASS / preserve**

Particularly strong controls:

- `<0.01 mGy/day` is a bound, never zero and never exactly 0.01
- absorbed dose remains in gray/milligray; sievert is explicitly not derivable from supplied information
- `about 8.4 mGy/day` remains a surveyed homeworld site record, not an optimum or prescription
- `about 12 mGy/day` remains a modeled average for a different species
- six monthly production values remain discrete; no interpolation
- two dose conditions do not become a response curve
- the species-specific karreth pathway is never generalized to plants, Earth organisms, or people
- melanized-fungi work is treated narrowly and never as radiation-powered photosynthesis or obligate-radiation proof
- the final task asks for trial requirements, control, measurement, staged exposure, authorization, and stop criteria — not a source, device, or operating setting
- radiation protection remains the default outside the documented species-specific case

## Visual modernization candidates

### C2C5-VIS01 — detection-limit analogy

Refine the whole-millimetre rain-gauge example into a cleaner instrument-resolution graphic while preserving that it is a teaching example, not vault data.

### C2C5-VIS02 — production decline

Modernize the six discrete monthly production bars into an SAA production-monitor panel while keeping all six exact reported values and drawing nothing between months.

### C2C5-VIS03 — mechanism and monitored trial

Redesign the missing exposure → quiescent pathway → lost compound-production model alongside the safe engineering logic: approved team → non-exposed comparison → dosimetry + production measurement → retained containment → staged trial → prewritten stop rule.

The engineering graphic must remain high-level and non-operational.

## Shared-system implications

Case 05 reinforces:

- later C2 Teacher Guides can be rich in source-boundary content yet omit the common rubric/source-list contracts
- five-source contribution/limit tasks remain the clearest repeated Accessible burden
- explicit multi-period teaching can be legitimate if declared; it should not be confused with the hidden 105–140 minute “one route” pacing drift in Cases 01–04

## Final disposition

`AUDIT_COMPLETE — REMEDIATION_REQUIRED`

No curriculum/game package files were modified.
