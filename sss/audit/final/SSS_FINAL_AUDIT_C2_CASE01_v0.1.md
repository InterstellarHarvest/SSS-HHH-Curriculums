# SSS Final Unified Audit — Campaign 2 Case 01

**Case:** SSS-C2-CASE01 — Heavy Hands  
**Audit status:** `AUDIT_COMPLETE — REMEDIATION_REQUIRED`  
**Owner disposition:** `OWNER_ACCEPTED`  
**Audit date:** 2026-08-07

## Frozen authority

- Curriculum baseline: `f7a24423f802a095aa149f923d05475ba2837599`
- Game baseline: `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`
- Package version: `1.1`
- Student pages: 5
- Teacher pages: 9
- Answer Key pages: 4
- Accessible pages: 8

Campaign 2 mechanical release integrity is accepted as already certified. This audit concerns instructional quality and consistency only.

## Overall assessment

Heavy Hands is a carefully remediated package with excellent numerical/source-boundary discipline. It clearly separates conditions actually changed across plantings from present readings, keeps the raw centrifuge profile Teacher-only where appropriate, and avoids asking learners to calculate from values they were not given.

The main defects are Teacher-template drift, a Teacher-authorized reduction of a required five-source task, failure to use the common four-level rubric contract, and Accessible workload that remains too close to the Student edition in Tasks 5–6.

## Findings

| ID | Severity | Finding |
|---|---|---|
| C2C1-T01 | Major | Nine-page Teacher Guide does not conform to corrected C1 Case 01 seven-page architecture |
| C2C1-T02 | Major | Teacher Guide explicitly permits shortening required Task 5 from five evidence sources to three |
| C2C1-T03 | Major | Teacher formal rubric uses Secure/Developing/Not yet rather than common quick + full 4/3/2/1 rubric contract |
| C2C1-ACC01 | Major quality gap | Accessible Tasks 5–6 retain nearly the full repeated evidence/diagnosis workload |
| C2C1-T04 | Moderate | Suggested pacing totals 105 minutes and is not normalized to the common one-period Teacher flow |
| C2C1-VIS01 | Enhancement | Tuber-span/size-dependence figure modernization |
| C2C1-VIS02 | Enhancement | Across-bed radial-profile diagnostic modernization |
| C2C1-VIS03 | Enhancement | Missing-specification / design-comparison panel modernization |

## C2C1-T01 — Teacher template drift

The Teacher Guide has nine pages and substantial case-specific material: standards caveats, vocabulary, numerical ledger, reported-condition/source tables, precedent records, science boundaries, misconception corrections, accessibility guidance, rubric, answers, and references.

Most is useful. It should be reorganized into corrected Case 01 architecture rather than preserved as a separate nine-page Teacher design.

Particularly strong content to preserve during normalization:

- reported-vs-tested distinction
- exact numerical ledger and precision cautions
- direction-vs-magnitude misconception controls
- withdrawn/conditional standards language
- source boundary separating physics, case evidence, case inference, and engineering extrapolation
- learner-visible versus Teacher-only data policy

## C2C1-T02 — Teacher Guide authorizes incomplete Task 5

Task registry defines Task 5 as connecting **all five evidence sources** and giving each source a contribution and limit.

Teacher Page 4 says that without gameplay teachers may “skip Task 5 down to three sources if time is short.”

That changes the graded task itself rather than providing access to the same task. It also conflicts with the Answer Key's completed five-source exemplar and the task registry's explicit instructional purpose.

### Required remediation

Do not reduce the required source count in ordinary Teacher procedure. If an accommodation legitimately requires fewer sources for an individual learner, that belongs in explicit differentiation guidance with a documented assessment implication, not in the default lesson fallback.

## C2C1-T03 — rubric contract mismatch

Teacher Page 9 provides a useful three-level rubric:

- Secure
- Developing
- Not yet

for magnitude/direction, evidence, reported values, and bounded claim.

It does not meet the definitive shared rubric structure requiring a quick rubric plus a complete four-level analytic rubric.

### Required remediation

Normalize Page 6-equivalent scoring support to the common quick + 4/3/2/1 structure while preserving the strong case-specific descriptors.

## C2C1-T04 — pacing drift

Teacher Page 3 suggests:

- 10 min launch
- 15 min Tasks 1–2
- 20 min Task 3
- 15 min Task 4
- 20 min Tasks 5–6
- 25 min Tasks 7–8

Total: **105 minutes**.

This is materially different from the common one-period Teacher architecture used as authority and is likely one reason the Guide later suggests cutting Task 5.

### Required remediation

Rebuild a realistic common-period core route. If the full package is intentionally a multi-period extension, that must be stated explicitly and separated from the standard one-period route rather than silently using a 105-minute pacing block.

## Answer Key verdict

**PASS / preserve**

The key is exceptionally complete and careful:

- Task 1 distinguishes changed vs merely reported conditions and explicitly states N does not mean ruled out.
- Task 2 completes every merry-go-round response and protects direction/magnitude language.
- Task 3 answers question/measurement/specification subparts.
- Task 4 explains size dependence and alternatives.
- Task 5 completes all five sources and limits.
- Task 6 completes diagnosis, all rejections, and the two open model stages.
- Task 7 supplies a bounded multi-source CER.
- Task 8 supplies criterion, constraint, proposal comparison, monitored trial, and stop rule.

No required Answer Key field was found missing.

## C2C1-ACC01 — Accessible workload remains too high in Tasks 5–6

Accessible is substantially better than a reflow in Tasks 1–4 and 7–8: language is simplified, a Task 3 word bank is supplied, the causal idea is repeatedly anchored to the merry-go-round, and the canonical CER has sentence starters and direct page pointers.

Two tasks remain too close to full Student workload.

### Task 5

Learners complete ten open response cells: contribution + limitation for all five sources. This is essentially the Student task with shorter source descriptions.

**Recommended direction:** model one complete source row and/or prefill selected contribution cells so the learner demonstrates the contribution-versus-limit distinction across fewer fully open pairs.

### Task 6

Learners mark four diagnoses, reject three alternatives, and complete two mechanism stages. This remains a dense multi-operation task.

**Recommended direction:** prefill the best-supported candidate status or model one rejected alternative while retaining the evidence-based rejection and mechanism target.

### CER

**PASS — preserve.**

## Fillable HTML

**PASS for required diagnosis selection.**

Unlike C1 Cases 03–07, Heavy Hands gives each `Best?` diagnosis row its own persisted writable response field. The action is therefore digitally representable, even though a dedicated single-selection widget would be cleaner.

## Game / curriculum parity

**PASS**

The package registry points to the frozen final game commit, and runtime identity matches the curriculum:

- Vressk Centrifuge Habitat
- Kepler-442b Orbit
- Vressk Territory

The quantitative model is driven from one canonical runtime calculation and the curriculum's qualitative learner-facing evidence deliberately withholds raw values not needed for graded tasks.

## Numerical/source discipline

**PASS / preserve**

Especially strong safeguards:

- midpoint `2.10 g` remains exactly as reported
- learner editions are not asked to calculate the tiny across-bed difference
- raw radii/magnitudes and `a = ω²r` remain Teacher-facing
- `0.0018 g` versus directly reported `0.00187 g` is explained as rounding, not conflict
- no deformation amount is invented
- direction stays outward at all sampled radii
- present readings are never treated as completed experimental tests
- GC-1445 is explicitly prevented from becoming a universal safe-radius claim

## Visual modernization

### C2C1-VIS01 — tuber span

Redesign the small/medium/large tuber figure as a clearer radial-bed cross-section showing how organ span grows across the same bed depth, without inventing deformation quantities.

### C2C1-VIS02 — across-bed profile

Modernize the Teacher radial profile into an SAA centrifuge telemetry schematic: same outward direction at all points, increasing magnitude with radius, exact reported values retained.

### C2C1-VIS03 — specification/design panel

Present midpoint-only requirement → missing across-bed criterion → two design responses → monitored trial as a compact engineering requirements/verification flow.

## Final disposition

`AUDIT_COMPLETE — REMEDIATION_REQUIRED`

No curriculum/game package files were modified during this audit.
