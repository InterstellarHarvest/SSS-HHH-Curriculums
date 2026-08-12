# Hunger, Harvest, & History Curriculum Blueprint

**Version:** 1.0  
**Phase:** HHH Curriculum Blueprint — Phase 2  
**Status:** `APPROVED — GOVERNING HHH CURRICULUM ARCHITECTURE`  
**Owner approval:** 2026-08-11  
**Curriculum repository:** `InterstellarHarvest/SSS-HHH-Curriculums`  
**Blueprint authoring baseline:** `2c221119c3221f3109c56ee1a0da95309ea281a8`  
**Authoritative HHH game baseline audited by Phase 1:** `9b8545ed6ecf98b337326390400076e36789e056`  
**Program:** *Hunger, Harvest, & History*  
**Institution:** Temporal Agricultural Archive (TAA)  
**Primary audience:** Middle school, with adaptation possible for older learners  
**Primary standards homes:** C3 Framework historical inquiry + CCSS History/Social Studies disciplinary literacy

---

# 1. Authority and phase boundary

Phase 1 is closed. This Blueprint does not repeat the HHH Master Game Audit, reopen its historical/scientific verification, perform more pre-HHH cleanup, or silently revise game conclusions.

The governing Phase 1 audit artifacts are:

- `hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md`
- `hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json`

Those two files are the authoritative HHH game-audit baseline for this Blueprint.

The audit itself records the curriculum SHA that was current during the Phase 1 read-only audit. This Blueprint is authored from the later owner-authorized curriculum baseline `2c221119c3221f3109c56ee1a0da95309ea281a8`, where the completed audit artifacts are committed. That later commit does not reopen or replace the Phase 1 game baseline.

Shared curriculum production authority remains:

- `shared/curriculum-bible/SSS_HHH_CURRICULUM_BIBLE_v1.3.md`
- `shared/implementation/SSS_TO_HHH_PRODUCTION_LESSONS_v1.0.md`
- `shared/implementation/SSS_HHH_TEACHER_EDITION_CONTRACT_v1.0.md`
- `shared/implementation/SSS_HHH_ACCESSIBLE_ADAPTATION_CONTRACT_v1.0.md`
- `shared/visual-style-guide/VISUAL_STYLE_GUIDE_v1.0.md`
- controlling visual-style amendments
- current package, registry, layout, lifecycle, editor, and validation contracts

SSS is frozen and complete. It is a regression, production-system, and methodological reference only. HHH must inherit the mature shared production system without reopening SSS content or treating SSS scientific task architecture as the HHH instructional model.

---

# 2. Purpose

This Blueprint translates the completed HHH game audit and the locked Phase 2 owner decisions into a repeatable HHH curriculum system before any individual HHH case package is produced.

It defines:

- the complete 15-unit curriculum sequence;
- which game levels function as Orientation, Core Cases, Synthesis, or Capstone;
- the historical-reasoning architecture used across HHH;
- Student, Teacher, Answer Key, and Accessible role architecture;
- the HHH source-status and provenance system;
- the two-layer truth policy for fictional/future cases;
- no-game evidence requirements and Campaign 2 classroom access;
- standards strategy;
- recurring task and visual families;
- assessment and rubric rules;
- package, folder, registry, and schema implications;
- dependencies on game remediation;
- production order and gates for the next phase.

This document is not an individual case package and does not authorize case production by itself. The approved Blueprint will govern later HHH case production together with the shared Curriculum Bible and implementation contracts.

---

# 3. Locked owner decisions

## 3.1 Program topology

HHH contains **12 numbered Core Cases** plus three deliberately different program units:

- C1 L0 — Archive Orientation — not a numbered Core Case;
- C1 L1–L6 — Core Cases 01–06;
- C1 L7 — Campaign 1 Synthesis/Debrief — not a numbered Core Case;
- C2 L0–L5 — Core Cases 07–12;
- C2 L6 — Program Capstone — not Case 13.

There is **no Core Case 13**.

## 3.2 Historical argument / CER policy

Every Core Case culminates in an evidence-based historical reasoning product, but the form must fit the disciplinary work of the case.

CER remains an approved shared component. It is **not** mandatory in every HHH case.

Approved culminating products include:

- historical explanation;
- evidence-based argument;
- source/provenance or authenticity judgment;
- multi-causal explanation;
- continuity/change synthesis;
- canonical CER when Claim–Evidence–Reasoning genuinely fits;
- capstone deliberation where multiple conclusions may be defensible.

## 3.3 Fictional/future case policy

Core Cases 06, 11, and 12 remain in the core sequence.

HHH uses an explicit **two-layer truth policy**:

1. **In-world / fictional evidence** establishes what is observed, claimed, disputed, forged, or true inside the HHH narrative.
2. **Real-world historical/scientific evidence** separately establishes what is documented, inferred, debated, analogous, or unsupported outside the game.

The two layers may be compared but must never be silently merged.

## 3.4 Campaign 2 classroom access

HHH will **not** add a special Campaign 2 teacher level selector, direct-launch mode, injected save state, developer shortcut, or other game bypass merely for curriculum access.

Every Campaign 2 Core Case must instead have a complete no-game evidence fallback. Normal gameplay remains usable when the class has naturally reached the relevant level.

No assessment may require evidence that exists only in an inaccessible game state.

## 3.5 Package and repository treatment

All 15 curriculum units use the same mature package/editor/validation pipeline.

The instructional types are:

- `ORIENTATION`
- `CORE_CASE`
- `SYNTHESIS`
- `CAPSTONE`

Every unit lives inside the campaign folder to which it belongs and appears in instructional order. Archive Orientation uses `case-00-...` as its folder name so it sorts before Core Case 01 while remaining pedagogically an Orientation.

---

# 4. HHH instructional identity

HHH is an **archival and historical inquiry curriculum**, not SSS with historical vocabulary substituted for scientific vocabulary.

The game is an investigative environment. The curriculum is the historical, archival, evidentiary, geographic, quantitative, and source-critical documentation surrounding that environment.

The recurring HHH question is not merely:

> What is the correct diagnosis?

It is closer to:

> What does the evidence establish, how do we know, what does it not establish, and what historical interpretation is justified?

HHH therefore emphasizes:

- source status;
- provenance;
- corroboration;
- chronology;
- geographic context;
- continuity and change;
- cause and consequence;
- multiple causation;
- competing interpretations;
- authenticity and transmission;
- quantitative evidence where appropriate;
- distinction between local mechanism and broader historical causation;
- distinction between documented, reconstructed, inferred, debated, and fictional claims;
- evidence-based argumentation with uncertainty.

A worksheet must not become a transcript log of game clues. Students should process evidence rather than copy it.

---

# 5. Complete curriculum topology

| Curriculum position | Game source | Runtime title | Instructional type | Primary historical-reasoning role |
|---|---|---|---|---|
| Archive Orientation | C1 L0 | Temporal Agricultural Archive Facility | `ORIENTATION` | Source status, archive procedure, provenance orientation |
| Core Case 01 | C1 L1 | The Fertile Crescent | `CORE_CASE` | Chronology, cumulative change, reconstruction vs. documentation |
| Core Case 02 | C1 L2 | Sumer | `CORE_CASE` | Cause/consequence, systems reasoning, local mechanism vs. broader claim |
| Core Case 03 | C1 L3 | County Cork | `CORE_CASE` | Multiple causation, contextualization, corroboration |
| Core Case 04 | C1 L4 | Karlsruhe | `CORE_CASE` | Technological change, mechanism/tradeoffs, attribution |
| Core Case 05 | C1 L5 | The Dust Bowl | `CORE_CASE` | Multiple causation, human-environment systems, policy response |
| Core Case 06 | C1 L6 | The Vertical Farm | `CORE_CASE` | Systems causation, evidence audit, institutional accountability |
| Campaign 1 Synthesis | C1 L7 | The Temporal Agricultural Archive | `SYNTHESIS` | Continuity/change, cumulative agricultural knowledge, historical memory |
| Core Case 07 | C2 L0 | The Audit | `CORE_CASE` | Authenticity, provenance, corroboration, source criticism |
| Core Case 08 | C2 L1 | The Floating Gardens | `CORE_CASE` | Geographic reasoning, engineered landscapes, source limitation |
| Core Case 09 | C2 L2 | The Seeds They Kept | `CORE_CASE` | Provenance, collection continuity, corroboration, ethical history |
| Core Case 10 | C2 L3 | The Quiet Billion | `CORE_CASE` | Quantitative evidence, competing interpretation, causal qualification |
| Core Case 11 | C2 L4 | The Bloom That Needed Poison | `CORE_CASE` | Fictional record analysis, policy revision, analogy boundaries |
| Core Case 12 | C2 L5 | The Living Record | `CORE_CASE` | Documented/inferred/debated/fictional status, contested interpretation |
| Program Capstone | C2 L6 | The Source | `CAPSTONE` | Cross-case synthesis, provenance, archive ethics, competing values |

The 15-unit structure follows the game sequence while preserving the audit finding that C1 L0, C1 L7, and C2 L6 do not function like ordinary historical cases.

---

# 6. Progression of historical reasoning

## 6.1 Campaign 1

Campaign 1 introduces the basic archival routine and then develops increasingly complex causal and historical reasoning:

1. source/provenance orientation;
2. cumulative selection and long-term change;
3. environmental systems and qualified causation;
4. biological trigger versus social/political famine causation;
5. scientific/technological process and historical attribution;
6. human-environment interaction and policy response;
7. future system failure and institutional interpretation;
8. continuity/change synthesis across the campaign.

Campaign 1 should make one recurring lesson explicit: **a correct local mechanism is not automatically a complete explanation of a broader historical outcome.**

## 6.2 Campaign 2

Campaign 2 increases the source-reasoning demand:

1. authenticity and provenance;
2. engineered historical landscapes and source limitation;
3. continuity of a collection through crisis;
4. forged/competing records and quantitative claims;
5. fictional policy records versus real scientific analogy;
6. documented, inferred, debated, and fictional scientific/historical claims;
7. archive ethics and value conflict where no single moral answer is academically mandated.

Campaign 2 should feel like students are increasingly **auditing the record itself**, not simply accepting an archive entry because it exists.

---

# 7. Standard Core Case Student architecture

HHH uses a recurring functional spine, not a rigid identical worksheet.

A normal Core Case should contain the following functions in this order. Functions may be split into more than one numbered task or combined when the case genuinely requires it. Exact task numbers and titles are case-specific and are locked in the task registry at production.

## Function 1 — Reference / vocabulary

Provide only terms needed to perform the case reasoning.

Rules inherited from the shared system apply:

- student-facing vocabulary is alphabetical unless the terms themselves form an essential sequence;
- exact-match word banks are used only for constrained recall;
- sequence banks use a fixed non-answer order;
- Student and Accessible banks use the same entries;
- the Answer Key uses exact matching terminology.

## Function 2 — Initial interpretation

Students make a brief provisional interpretation, identify a needed kind of evidence, or state what they would verify first.

This establishes a starting point without revealing the final historical interpretation.

Internal grading-policy commentary does not appear on Student or Accessible pages.

## Function 3 — Historical context

Students orient to the time, place, process, or system needed to interpret the evidence.

Possible forms:

- timeline;
- sourced map;
- system cross-section;
- brief contextual source;
- comparison of conditions;
- period/region reference strip.

The context task must support later reasoning rather than become detached background trivia.

## Function 4 — Source status / provenance

Students identify what a source is, where it came from, what relationship it has to other records, and/or what it can and cannot establish.

Not every case needs an identical provenance table, but every Core Case must make source status visible where misunderstanding is possible.

## Function 5 — Evidence analysis

This is usually the major case-specific organizer.

Approved families include:

- source contribution-and-limitation matrix;
- chronology/evidence chain;
- sourced map analysis;
- quantitative data display;
- multiple-causation organizer;
- mechanism or systems diagram;
- continuity/change comparison;
- provenance chain;
- competing-record comparison;
- evidence-status convergence diagram.

Students record only evidence needed for the reasoning task.

## Function 6 — Competing interpretations / causation

Students test alternative explanations, records, causal claims, or interpretations.

Depending on the case, this may require students to:

- reject an unsupported record;
- rank evidence strength;
- distinguish contributing cause from sole cause;
- identify what a source cannot prove;
- separate local mechanism from broader historical explanation;
- identify what additional evidence would be needed.

## Function 7 — Culminating historical reasoning product

The final product must match the case's disciplinary reasoning.

It may be:

- a historical explanation;
- evidence-based argument;
- source/provenance judgment;
- multi-causal explanation;
- continuity/change synthesis;
- canonical CER when appropriate.

The required product must use specific evidence and preserve source-status qualifications.

## Function 8 — Transfer / exit

Students apply the reasoning operation to a new source, situation, or historical question.

The exit should measure transfer rather than simple recall of the game’s final answer.

## Optional extension

An optional extension may deepen source limitation, comparison, or application. It must not raise the base requirement for other students and must not be necessary to earn full credit on the standard task contract.

---

# 8. Special-unit Student architecture

## 8.1 Archive Orientation

Archive Orientation is not forced into the Core Case spine.

It should teach:

- archive;
- record;
- source status;
- provenance;
- corroboration;
- accession;
- the difference between a preserved claim and verified historical truth;
- the fictional status of the TAA/Concord framing.

Its culminating product is a short archive-procedure/source-status explanation rather than a historical diagnosis.

## 8.2 Campaign 1 Synthesis

The Campaign 1 Synthesis depends on Cases 01–06 and should provide concise evidence recaps rather than require perfect memory.

It should ask students to trace continuity/change, preservation, transfer, or consequences across at least two earlier cases.

Its culminating product is a short cross-case synthesis about agricultural knowledge, change, and historical memory.

## 8.3 Program Capstone

The Program Capstone uses the C2 L6 confrontation as a culminating deliberation.

Students must:

- assemble evidence from prior Campaign 2 investigations;
- trace provenance and the manipulation of records;
- represent the opposing thesis fairly;
- identify uncertainty and competing values;
- justify an archive/record decision with evidence.

There is no teacher-preferred moral answer.

The rubric scores evidence use, provenance reasoning, representation of competing positions, qualification, and justification.

---

# 9. Culminating-product policy

## 9.1 Historical explanation

Use when students must explain change, cause, consequence, mechanism, or historical process.

## 9.2 Evidence-based argument

Use when several interpretations or records compete and students must defend the best-supported position.

## 9.3 Provenance/authenticity judgment

Use when the central question is which record is more credible, continuous, authentic, or better supported.

## 9.4 Multi-causal explanation

Use when one cause is insufficient and students must explain interaction among several contributing conditions.

## 9.5 Continuity/change synthesis

Use for cross-period or cross-case reasoning about what changed, what persisted, and why.

## 9.6 CER

Use canonical Claim–Evidence–Reasoning only when its structure genuinely supports the case.

When CER is used:

- shared CER geometry and task-reference rules apply;
- the Answer Key includes a complete Claim, Evidence, and Reasoning exemplar;
- the Accessible edition uses the protected canonical Accessible CER and exact required subtitle;
- Evidence should use more than one source when the case supports it;
- Reasoning must connect evidence to the historical interpretation, not simply restate the claim.

## 9.7 Capstone deliberation

Use when evidence constrains the decision but does not produce one uniquely correct moral or policy choice.

Do not convert deliberation into a hidden multiple-choice key.

---

# 10. Four-role architecture

Every HHH package uses exactly four instructional roles:

- Student;
- Teacher;
- Answer Key;
- Accessible.

Grayscale remains a presentation state, not a fifth role.

## 10.1 Student

Student materials must:

- begin Page 1 with Name / Date / Period above all other printable content;
- use TAA printable identity and shared page geometry;
- present tasks in canonical order;
- focus on evidence processing rather than clue transcription;
- make required learner actions persistent in digital fill mode;
- preserve source status and historical qualification;
- provide response space proportional to expected writing;
- avoid visible production metadata or runtime identifiers.

Page count is case-driven. HHH is not locked to the old SSS double-sided-sheet assumption.

## 10.2 Teacher

HHH inherits the seven-function Teacher contract.

### Function 1 — teacher launch sheet

Must include:

- before-class preparation;
- normal game route where applicable;
- explicit no-game route;
- central historical interpretation / case resolution;
- concise lesson-flow overview;
- essential evidence;
- likely sticking point;
- what to collect;
- classroom/technical fallback;
- teacher framing line or equivalent.

### Function 2 — lesson and standards overview

Must include:

- lesson overview;
- guiding historical question;
- standards alignment with Direct / Supporting / Contextual status;
- measurable objectives;
- success criteria;
- vocabulary;
- materials/technology;
- preparation notes.

### Function 3 — complete teaching procedure

Must account for every Student task in instructional order.

Direct references use the exact Student task number and title in bold.

HHH cases may use timed or period-based flow. Do not force a source-heavy case into an unrealistic universal 60-minute structure.

### Function 4 — assessment and support

Must include:

- formative checks;
- assessment guidance;
- actual Accessible adaptations used;
- misconceptions;
- historical/scientific/source-status boundaries;
- no-game fallback guidance.

### Function 5 — evidence and reasoning architecture

Must include:

- source/evidence architecture;
- reasoning path;
- competing interpretation/distractor treatment;
- what each source contributes;
- what each source cannot establish alone where relevant;
- source-status and fiction boundaries;
- instructional emphasis.

Runtime clue IDs, node IDs, code paths, internal filenames, and production metadata are prohibited from Teacher-visible content.

### Function 6 — grading contract

Must include:

1. a concise classroom quick rubric; and
2. a complete analytic 4/3/2/1 rubric.

Criteria are case-specific but must assess the actual historical reasoning product.

### Function 7 — sources and complete fallback

Must include:

- authoritative historical/scientific source list;
- source/provenance notes;
- a complete student-safe no-game evidence digest/dossier or equivalent;
- classroom/technical fallback.

The preferred Teacher implementation remains the shared seven-function architecture. Extra pages are allowed only when a genuinely necessary source/fallback appendix or case-specific instructional need cannot fit without harming usability.

## 10.3 Answer Key

Every keyable Student task has a completed exemplar.

The key must:

- preserve exact Student task number and title;
- visibly answer every required field/subpart;
- use source-specific evidence;
- show historical qualification where required;
- distinguish model response from acceptable alternatives;
- recognize defensible alternative interpretations when the prompt permits them;
- never become narrower than the Accessible prompt;
- never present reconstructed game dialogue as real-world primary-source evidence.

For open historical arguments, the key provides a model proficient response and explicit acceptable-variation guidance rather than implying one exact wording is mandatory.

For the Program Capstone, no moral option is keyed as academically correct.

## 10.4 Accessible

Accessible is authored together with Student, not retrofitted later.

It preserves:

- the same essential learning target;
- the same task order and exact task titles;
- the same evidence relationships;
- the same source-status boundaries;
- the same acceptable answer space.

It may reduce avoidable burden through:

- shorter/chunked directions;
- one action per step;
- source pointers;
- plain-language vocabulary beside the task;
- sentence frames;
- exact phrase banks;
- partially completed source rows;
- modeled first examples;
- prefilled non-target classifications;
- reduced repeated writing;
- bounded selection where open recall is not the target;
- bullets, labels, diagrams, typed response, dictation, or scribing where appropriate.

For multi-source HHH matrices, the preferred pattern is to model or prefill part of the repeated work and preserve the final cross-source synthesis as the independent reasoning target.

Accessible page count is content-driven. Continuous-flow pagination and proportional response-space rules remain controlling.

---

# 11. Source-status and provenance system

HHH requires source status to be designed into each case from the beginning.

## 11.1 Two separate classification axes

Teacher/source records must distinguish **source origin** from **evidentiary status**.

### Source origin / provenance

Examples:

- real historical primary source;
- real modern secondary/scholarly source;
- government/institutional record;
- archaeological or scientific evidence;
- game reconstruction of a historical person/event;
- fictional in-world testimony;
- fictional in-world archive/scan;
- curriculum-original schematic;
- adapted/reproduced source.

### Evidentiary status

Use the shared controlled concepts accurately:

- documented / observed;
- inferred;
- reconstructed;
- modeled;
- debated / uncertain;
- fictional / hypothetical.

A source may occupy more than one category when necessary, but the labels must not become contradictory.

## 11.2 Game-source rule

A game character, dialogue node, TAA record, scan, codex, forensic report, or future record is **not automatically a real historical primary source** because the runtime presents it as testimony or an archive.

The curriculum must independently state its real-world status.

## 11.3 Contribution-and-limitation rule

For major evidence sources, production planning should record:

- what the source contributes;
- what it can establish;
- what it cannot establish alone;
- what corroboration is required;
- whether its relationship to other evidence is documented, inferred, reconstructed, debated, or fictional.

This carries forward one of the strongest structures in the Phase 1 audit.

## 11.4 Historical reconstruction rule

Reconstructed dialogue or scenes may orient students or model a plausible historical situation, but they must never be presented as verbatim surviving testimony unless an actual source supports that claim.

Precise dates, motives, individuals, counts, or causal claims must not be manufactured merely to make the story cleaner.

## 11.5 Map and quantitative-source rule

Historical geographic geometry must be sourced.

Quantitative displays must preserve:

- units;
- date/period;
- data status;
- ranges and uncertainty;
- source attribution;
- distinctions among measured, reported, estimated, modeled, reconstructed, or illustrative data.

No decorative numbers may masquerade as historical measurements.

## 11.6 Structured evidence ledger

Each HHH package should maintain a case evidence/source ledger as a referenced canonical source asset when useful. A structured `source/evidence-ledger.json` is the preferred HHH implementation because it can be validated without creating a new document role.

At minimum, the ledger should support:

- stable source identifier;
- display title;
- creator/institution when known;
- date/period;
- source type/origin;
- evidentiary status;
- provenance/relationship;
- contribution;
- limitation;
- rights/attribution where applicable;
- game/fallback correspondence.

The ledger is production metadata/source control, not an automatically printed table.

---

# 12. Two-layer truth policy for fictional/future cases

The two-layer truth policy is mandatory for Core Cases 06, 11, 12, the fictional portions of special units, and any later HHH material combining fictional records with real scholarship.

## Layer A — in-world / fictional truth

Students may determine, using in-game evidence:

- what occurred inside the fictional case;
- which in-world record is forged or better supported;
- how a fictional policy changed;
- what an in-world system did;
- what fictional actors claim.

## Layer B — real-world evidence / analogy

Students separately evaluate:

- what actual science/history establishes;
- what is supported only in some systems;
- what is debated;
- what is merely analogous;
- what does not have real-world support.

## Non-merger rule

A correct in-world conclusion does not prove a real-world claim.

A real-world analogy may illuminate a fictional mechanism without becoming evidence that the fictional event literally occurred.

Teacher materials, Student source-status labels when needed, Answer Keys, Accessible scaffolds, and figures must preserve this separation.

---

# 13. No-game evidence fallback

A complete no-game route is a program requirement.

Every Core Case must be teachable and assessable without requiring successful gameplay. Special units must also provide an equivalent fallback when their learning target depends on game evidence.

## 13.1 Equivalence standard

The fallback must preserve:

- the same central learning goal;
- the same essential evidence relationships;
- the same source-status distinctions;
- the same culminating reasoning product;
- the same rubric criteria;
- the same task identifiers where the Student packet is shared.

It is not an easier substitute and not a transcript dump.

## 13.2 Permitted fallback forms

Depending on the case:

- source cards;
- short archival excerpts;
- sourced maps;
- timelines;
- data tables/graphs;
- screenshots;
- evidence summaries;
- reconstructed vignettes with explicit status labels;
- policy/record excerpts;
- deterministic diagrams.

## 13.3 Package placement

The fallback remains inside the existing four-role package system. It does not create a fifth `fallback` role.

A case may implement the student-safe evidence dossier as:

- Student evidence pages usable with or without gameplay;
- a clearly marked Teacher-reproducible student-safe appendix;
- or another package-contained approach that preserves role isolation and does not expose answers.

## 13.4 Campaign 2 rule

Campaign 2 Core Cases 07–12 must be independently teachable through their fallback dossiers if a class has not naturally progressed to the corresponding game level.

No special Campaign 2 launch bypass will be built for the curriculum.

---

# 14. Standards strategy

HHH uses **task-first alignment**.

A historical topic appearing in a lesson does not by itself create a standards alignment.

Every standards claim is classified as:

- **Directly Assessed** — the Student task and rubric actually measure the standard;
- **Supporting** — the standard is meaningfully practiced or supports the assessed task;
- **Contextual** — relevant content is present but is not directly assessed.

## 14.1 Strongest C3 program homes

Candidate recurring standards include:

- `D3.1.6-8` — gathering/evaluating sources where explicitly assessed;
- `D3.2.6-8` — evaluating source credibility/usefulness where explicitly assessed;
- `D2.His.1.6-8` — connections among events/developments and broader context;
- `D2.His.2.6-8` — continuity/change;
- `D2.His.14.6-8` — multiple causes/effects;
- `D4.1.6-8` — evidence-based argumentation where the culminating product genuinely requires it.

## 14.2 Strongest CCSS History/Social Studies homes

Candidate recurring standards include:

- `RH.6-8.1`
- `RH.6-8.2`
- `RH.6-8.6`
- `RH.6-8.7`
- `RH.6-8.8`
- `RH.6-8.9`
- `WHST.6-8.1`
- `WHST.6-8.2`

## 14.3 NGSS boundary

NGSS is used only when a case actually assesses a science/engineering practice or disciplinary idea.

Sumer, Haber, Dust Bowl, Vertical Farm, and First Garden contain genuine science. If the HHH task is primarily historical/source reasoning, NGSS is Supporting or Contextual rather than falsely presented as Directly Assessed.

---

# 15. Recurring HHH task and visual families

HHH uses the shared visual system and TAA archival archetype. New figures must belong to controlled functional families rather than becoming one-off decorative designs.

## Family H1 — source/provenance chain

Use for:

- original → copy → interpretation;
- accession continuity;
- forged/altered record relationships;
- transmission history.

## Family H2 — chronology/event rail

Use for:

- ordered change;
- event/source/publication date distinctions;
- long-duration processes;
- policy/technology sequences.

Uncertain dates use ranges or explicit qualification rather than false precision.

## Family H3 — sourced historical map

Use when geographic context is part of the reasoning.

Geometry, boundaries, routes, dates, and reconstructed extents must be sourced and status-labeled.

## Family H4 — source contribution-and-limitation matrix

Use when students must decide what each source contributes and what it cannot establish alone.

This is a signature HHH family.

## Family H5 — multiple-causation map

Use when several interacting causes contribute to a historical outcome.

Do not let arrow geometry imply unsupported certainty.

## Family H6 — continuity/change comparison

Use for campaign synthesis and cases where practices, records, systems, or outcomes change across time.

## Family H7 — quantitative historical evidence display

Use sourced graphs, tables, or comparison panels with direct labels, units, date, and data status.

## Family H8 — mechanism/system diagram

Use only when a real physical, biological, agricultural, or engineered mechanism is necessary to understand the historical reasoning.

The mechanism must not displace source evaluation.

## Family H9 — competing-record/authenticity comparison

Use matched records plus independent provenance/corroboration evidence.

Surface neatness alone must never function as an authenticity test.

## Family H10 — evidence-status convergence

Use when several claims differ in status: documented, inferred, debated, reconstructed, or fictional.

This is especially important for Core Case 12.

## Family H11 — policy/technology change sequence

Use for amendment, adoption, implementation, response, and consequence.

## Family H12 — capstone evidence ledger / competing-values matrix

Use for the Program Capstone to organize evidence, competing interpretations, uncertainty, values, and final justification without pre-keying one moral choice.

---

# 16. Assessment and rubric architecture

## 16.1 Academic grading principle

Grade the historical reasoning demonstrated in the curriculum task, not game performance.

Never grade:

- game score;
- speed;
- optional dialogue completion;
- discovery of bonus content;
- ability to progress through game mechanics without support.

## 16.2 Quick rubric

Every Core Case Teacher package includes a concise quick rubric. Criterion names may vary by case, but the rubric should normally cover:

- evidence/source use;
- historical reasoning or causation;
- source/provenance/qualification where relevant;
- communication/completion.

## 16.3 Analytic rubric

Every Core Case Teacher package includes a complete 4/3/2/1 analytic rubric.

Possible criteria include:

- source selection;
- corroboration;
- provenance/authenticity reasoning;
- chronology/context;
- cause/consequence;
- multiple causation;
- evidence sufficiency;
- interpretation of quantitative/visual evidence;
- qualification/uncertainty;
- historical explanation;
- argumentation;
- communication.

Only criteria actually assessed by the Student task should appear.

## 16.4 Capstone rubric

The Program Capstone rubric must assess:

- accurate use of cross-case evidence;
- provenance reasoning;
- fair representation of the opposing thesis;
- uncertainty/limitation;
- justification of the final archive decision;
- communication.

The selected moral/policy outcome is not itself a correctness criterion.

---

# 17. Case-by-case Blueprint profiles

## Archive Orientation — C1 L0

**Instructional type:** `ORIENTATION`  
**Central learning goal:** Distinguish archive procedure, record status, and source handling from the fictional institutional story.  
**Primary reasoning:** provenance/source-status orientation.  
**Primary family:** H1 source/provenance chain + source-status sorting.  
**Culminating product:** short archive-procedure/source-status explanation.  
**Boundary:** TAA, Concord, Zhel’ii, thread/resonance technology are fictional. Archival reasoning vocabulary is transferable.  
**Fallback:** compact orientation dossier with explicit fictional-context labels.  
**Readiness:** `READY_WITH_BOUNDARY_NOTE`.

## Core Case 01 — C1 L1 — The Fertile Crescent

**Central learning goal:** Explain cereal domestication as cumulative selection produced through repeated harvesting, seed saving, and replanting while distinguishing cultivation from later morphological domestication.  
**Primary reasoning:** chronology + cause/change over time + inference from archaeobotanical traits.  
**Primary families:** H2 chronology rail + H4 contribution/limitation + H10 status comparison.  
**Culminating product:** qualified historical explanation of selection across generations.  
**Boundary:** the woman, dialogue, and exact event are reconstructed/fictionalized; non-shattering evidence is real but the process is gradual and geographically variable.  
**Fallback:** archaeobotanical evidence plus a clearly labeled reconstructed harvesting vignette.  
**Production gate:** `GAME_REMEDIATION_REQUIRED` — do not finalize against a precise single-person 9700 BCE domestication event or insufficiently qualified reconstruction framing.

## Core Case 02 — C1 L2 — Sumer

**Central learning goal:** Explain how irrigation, shallow groundwater, inadequate drainage, and evaporation can contribute to salinization while evaluating the limits of salinity as a sole explanation for broad historical decline.  
**Primary reasoning:** cause/consequence + systems reasoning + source comparison.  
**Primary families:** H8 mechanism/system diagram + H4 source matrix + H3 sourced map.  
**Culminating product:** qualified causal explanation separating local field mechanism from civilization-wide claims.  
**Boundary:** salinization is historically important; reconstructed dialogue is not direct historical testimony; the scale of salinity’s role in broad decline is debated.  
**Fallback:** field profile, irrigation/drainage schematic, crop-tolerance comparison, and sourced historical excerpts.  
**Production gate:** `GAME_REMEDIATION_REQUIRED` — correct the truncated required clue before finalization and preserve qualification of broader decline claims.

## Core Case 03 — C1 L3 — County Cork

**Central learning goal:** Explain why potato late blight became famine by integrating biological crop failure with crop dependence, poverty/land systems, food access, exports, relief, and historical context.  
**Primary reasoning:** multiple causation + contextualization + corroboration.  
**Primary families:** H5 multiple-causation map + H4 contribution/limitation + H2 chronology + H3 sourced map.  
**Culminating product:** multi-causal historical explanation.  
**Boundary:** the pathogen is documented science; game characters are reconstructed; famine causation cannot be reduced to one biological variable.  
**Fallback:** sourced blight evidence, dependence/land/relief context, and food/export records; invented dialogue must not be presented as primary testimony.  
**Production gate:** `GAME_REMEDIATION_REQUIRED` — correct universalizing Lumper/dependence language and overcompressed famine causation before finalization.

## Core Case 04 — C1 L4 — Karlsruhe

**Central learning goal:** Explain the pressure/temperature/catalyst/recycle tradeoffs that made ammonia synthesis workable and place Haber’s laboratory result and Bosch’s industrial scale-up in correct historical relationship.  
**Primary reasoning:** technological change + mechanism/tradeoff reasoning.  
**Primary families:** H8 process/system diagram + H11 technology sequence + H4 evidence/source distinction.  
**Culminating product:** historical-technological explanation of the workable process and attribution.  
**Boundary:** Haber laboratory synthesis and Bosch industrial engineering are distinct; “moderate” temperature is a relative process compromise.  
**Fallback:** qualitative process evidence + short Haber/Bosch historical source set.  
**Readiness:** `READY_AFTER_POLISH_AND_QUALIFICATION`.

## Core Case 05 — C1 L5 — The Dust Bowl

**Central learning goal:** Explain the Dust Bowl through interaction among drought, removal of prairie cover, erosion, land use, and conservation/policy responses.  
**Primary reasoning:** multiple cause/consequence + human-environment systems + policy response.  
**Primary families:** H5 multiple-causation map + H8 soil/erosion system + H3 map + H11 policy sequence.  
**Culminating product:** qualified multi-causal historical/environmental explanation.  
**Boundary:** drought and land use both matter; exposed subsoil may have lower organic matter/fertility/microbial biomass without being literally biologically dead.  
**Fallback:** USDA/NRCS-sourced photos, map, soil profile, and policy evidence.  
**Production gate:** `GAME_REMEDIATION_REQUIRED` — remove “no microbial life” / “will grow nothing” biological-zero claims before finalization.

## Core Case 06 — C1 L6 — The Vertical Farm

**Central learning goal:** Distinguish hardware performance from failure of a biological nitrogen-cycling subsystem and evaluate institutional misattribution of a complex system failure.  
**Primary reasoning:** systems causation + evidence audit + accountability.  
**Primary families:** H8 systems trace + H9 competing-record comparison + H2 event log.  
**Culminating product:** systems/evidence-audit explanation.  
**Boundary:** 2041 facility/events are fictional; nitrification is real; the game simplifies microbial diversity and nitrogen chemistry.  
**Fallback:** fully fiction-labeled system dossier with chemistry/biology evidence and public-record comparison.  
**Readiness:** `READY_WITH_TEACHER_QUALIFICATION`.  
**Two-layer truth:** mandatory.

## Campaign 1 Synthesis — C1 L7

**Instructional type:** `SYNTHESIS`  
**Central learning goal:** Trace continuity/change in agricultural knowledge, systems, and record preservation across Campaign 1.  
**Primary reasoning:** campaign synthesis + continuity/change + reflection.  
**Primary families:** H6 continuity/change comparison + H2 cross-case chronology.  
**Culminating product:** short evidence-based synthesis using at least two earlier cases.  
**Fallback:** cross-case evidence recap cards plus finale excerpt.  
**Readiness:** `READY_AS_SYNTHESIS_NOT_CORE_CASE`.

## Core Case 07 — C2 L0 — The Audit

**Central learning goal:** Evaluate authenticity through provenance, transmission, discrepancies, and corroboration rather than surface neatness.  
**Primary reasoning:** source criticism + provenance + corroboration.  
**Primary families:** H9 competing-record comparison + H1 provenance chain.  
**Culminating product:** provenance/authenticity argument.  
**Boundary:** diplomatics/provenance are real; TAA memo/audit evidence is fictional; corrections or cleanliness are clues, not authenticity tests by themselves.  
**Fallback:** fictional audit dossier + concise real-world diplomatics/provenance reference.  
**Production gate:** `GAME_REMEDIATION_REQUIRED` — remove/qualify the “too clean = forged” heuristic before finalization.

## Core Case 08 — C2 L1 — The Floating Gardens

**Central learning goal:** Explain chinampas as an engineered wetland/raised-field agricultural system integrating canals, soil renewal, intensive cultivation, and hydrologic management while evaluating source status.  
**Primary reasoning:** geographic reasoning + systems/contextualization + source limitation.  
**Primary families:** H3 sourced map + H8 agroecosystem cross-section + H4 source comparison.  
**Culminating product:** geographic/historical systems explanation with source qualification.  
**Boundary:** chinampas are historical; exact 1487 characters/codex entries/TAA interactions are reconstructions; “floating gardens” is a conventional but potentially misleading label.  
**Fallback:** FAO/archaeological secondary sources, sourced map, and clearly reconstructed chinampa schematic.  
**Readiness:** `READY_WITH_TEACHER_QUALIFICATION`.

## Core Case 09 — C2 L2 — The Seeds They Kept

**Central learning goal:** Explain why preserving crop genetic diversity during the Siege of Leningrad mattered and evaluate testimony, accession continuity, and later reports as evidence for what happened to the collection.  
**Primary reasoning:** provenance + continuity/change + ethical historical reasoning.  
**Primary families:** H2 siege timeline + H1 accession/provenance chain + H4 corroboration matrix.  
**Culminating product:** evidence-based provenance/continuity explanation.  
**Boundary:** siege, collection, Vavilov arrest/death, and preservation are historical; dialogue is reconstructed; published death counts vary by source/definition.  
**Fallback:** VIR/Crop Trust sources, accession-chain diagram, siege timeline, and game testimony labeled as reconstruction.  
**Production gate:** `GAME_REMEDIATION_REQUIRED` — fix the `insight:true` clue that is operationally required to unlock the seed vault, or explicitly normalize its semantics before finalization.

## Core Case 10 — C2 L3 — The Quiet Billion

**Central learning goal:** Evaluate Green Revolution claims through experimental results, pedigree, lodging/rust traits, yield evidence, and broader production context without accepting triumphalist or wholly dismissive records.  
**Primary reasoning:** corroboration + quantitative evidence + cause/consequence + competing interpretation.  
**Primary families:** H7 quantitative evidence + H9 competing record + H2 chronology + H3 map.  
**Culminating product:** qualified evidence-based historical argument about the contribution of improved varieties within a larger input/institutional system.  
**Boundary:** Borlaug, Mexican research, semi-dwarf wheat, and South Asian adoption are historical; exact dialogue/yield numbers and the forged record are constructed for gameplay.  
**Fallback:** strong historical sources plus sourced trial/yield evidence and a clearly fictional forgery record.  
**Readiness:** `READY_WITH_TEACHER_QUALIFICATION`.

## Core Case 11 — C2 L4 — The Bloom That Needed Poison

**Central learning goal:** Practice source reasoning in a clearly fictional case where a universal safety rule harms an organism with different requirements, while separating fictional mechanism from real scientific analogy.  
**Primary reasoning:** competing interpretation + policy revision + source-status reasoning.  
**Primary families:** H10 status matrix + H11 policy chronology + H9 record comparison.  
**Culminating product:** in-world policy/source explanation plus a separate statement of real-world analogy limits.  
**Boundary:** karreth, Concord, and protocol history are fictional; melanized-fungus radiation responses are real research, but a direct “radiation becomes metabolic energy” claim is not a settled equivalent mechanism.  
**Fallback:** fully fiction-labeled protocol dossier + short real-science analogy reference.  
**Readiness:** `READY_WITH_QUALIFICATION_AND_DOC_FIX`.  
**Two-layer truth:** mandatory.

## Core Case 12 — C2 L5 — The Living Record

**Central learning goal:** Evaluate a biological/historical claim by separating direct observation of mycorrhizal symbiosis, fossil evidence, inferred network function, debated common-mycorrhizal-network claims, and the fictional First Garden mechanism.  
**Primary reasoning:** source contribution/limitation + contested interpretation + documented/inferred/fictional status.  
**Primary families:** H10 evidence-status convergence + H4 contribution/limitation.  
**Culminating product:** qualified claim distinguishing established, supported-in-some-systems, debated/generalized, and fictional claims.  
**Boundary:** mycorrhizal symbiosis is established; broad CMN sharing/signaling claims require qualification; direct fossil evidence and older evolutionary inference must not be collapsed; First Garden events are fictional.  
**Fallback:** peer-reviewed sources representing the scientific dispute, fossil evidence, and fully fictional-context game evidence.  
**Production gate:** `GAME_REMEDIATION_REQUIRED` — correct/qualify broad CMN transfer claims and fossil chronology before finalization.  
**Two-layer truth:** mandatory.

## Program Capstone — C2 L6 — The Source

**Instructional type:** `CAPSTONE`  
**Central learning goal:** Synthesize provenance, evidence, uncertainty, and archive ethics when competing interpretations cannot be reduced to a single academically correct moral verdict.  
**Primary reasoning:** cross-case synthesis + argumentation + archive ethics + competing values.  
**Primary family:** H12 capstone evidence ledger / competing-values matrix.  
**Culminating product:** evidence-based archive decision/deliberation.  
**Boundary:** ARS, Virel, Concord politics, and final choices are fictional. Any real seed-vault analogy must use current, sourced information rather than a frozen time-sensitive count.  
**Fallback:** Campaign 2 evidence recap/forgery ledger + capstone source set.  
**Status:** owner decision resolved as `CAPSTONE`; any minor time-sensitive game/document update remains a separate remediation item.  
**Two-layer truth:** mandatory where real analogies appear.

---

# 18. Timing and classroom implementation

HHH does not inherit a rigid universal 60-minute case requirement.

Every case must define a **realistic core implementation route**.

- Use one ordinary class period where the evidence load and gameplay permit it.
- Use an explicitly multi-period route when the historical/source work genuinely requires it.
- Do not make the Teacher Guide appear concise by omitting required Student tasks.
- Optional extension time must remain distinct from required assessment time.
- If gameplay consumes more time than expected, the academic reasoning product and essential source work take priority over optional game exploration.

The Teacher procedure must always state the actual route being assessed.

---

# 19. Package and repository architecture

## 19.1 Campaign-local folder rule

Every HHH curriculum unit lives inside the campaign folder to which its game level belongs.

Recommended structure:

```text
hhh/
├── audit/
│   ├── HHH_MASTER_GAME_AUDIT_v0.1.md
│   └── data/
│       └── HHH_STATIC_CONTENT_INVENTORY_v0.1.json
├── blueprint/
│   └── HHH_CURRICULUM_BLUEPRINT_v1.0.md
├── campaign-1/
│   ├── case-00-archive-orientation/
│   ├── case-01-fertile-crescent/
│   ├── case-02-sumer/
│   ├── case-03-county-cork/
│   ├── case-04-karlsruhe/
│   ├── case-05-dust-bowl/
│   ├── case-06-vertical-farm/
│   └── synthesis-campaign-1/
└── campaign-2/
    ├── case-07-archive-audit/
    ├── case-08-floating-gardens/
    ├── case-09-seeds-they-kept/
    ├── case-10-quiet-billion/
    ├── case-11-bloom-needed-poison/
    ├── case-12-living-record/
    └── program-capstone/
```

Folder slugs may be refined during package scaffolding for consistency, but the campaign-local ordering and instructional sequence are locked.

## 19.2 Canonical package sources

Each produced unit uses the existing HTML-only package-source architecture:

- `source/case-package.json`
- `source/content.html`
- `source/presentation.css`
- `source/task-registry.js`
- `source/layout-overrides.json` where required by the current package schema
- referenced optional source assets
- compact release history after approval

Generated role HTML, editable copies, PDFs, screenshots, and routine validation output are temporary and are not committed.

## 19.3 Technical package identities

Recommended technical identities:

- Orientation: `HHH-C1-CASE00` with `instructionalType: ORIENTATION`
- Core Cases: `HHH-C1-CASE01` through `HHH-C1-CASE06`, then `HHH-C2-CASE07` through `HHH-C2-CASE12`, all with `instructionalType: CORE_CASE`
- Campaign 1 Synthesis: `HHH-C1-SYNTHESIS` with `instructionalType: SYNTHESIS`
- Program Capstone: `HHH-C2-CAPSTONE` with `instructionalType: CAPSTONE`

Technical identifiers do not change the learner-facing rule that Orientation, Synthesis, and Capstone are not numbered Core Cases.

---

# 20. Registry and schema implications

The current registry is intentionally uninstantiated for HHH and currently contains `campaigns: []`. That is a clean activation point.

The current HHH registry title is `History's Harvest`. HHH activation must correct it to the canonical curriculum title:

> `Hunger, Harvest, & History`

This is an HHH activation correction, not an SSS cleanup.

## 20.1 Minimal instructional-type extension

Use the smallest shared-system extension required to represent the four HHH instructional types.

Preferred approach:

- add an `instructionalType` property with values `ORIENTATION`, `CORE_CASE`, `SYNTHESIS`, `CAPSTONE`;
- require it for HHH packages/entries through HHH-specific validation or schema conditions;
- leave existing SSS package/registry entries byte-unchanged where possible;
- extend package ID validation only enough to permit `HHH-C1-SYNTHESIS` and `HHH-C2-CAPSTONE` while retaining existing SSS IDs;
- allow nonnumeric display labels for special HHH units while retaining ordinary numeric labels for Core Cases;
- use explicit `displayOrder` to control Curriculum Editor ordering across all 15 units.

Do not create a second package schema, second editor, or second registry solely for HHH special units.

## 20.2 Shared regression rule

Any schema/registry change needed for HHH must run the full shared regression suite against frozen SSS.

Passing HHH activation does not justify changing SSS package content, lifecycle records, task registries, or approved outputs.

---

# 21. Game remediation dependency model

Blueprint work and game remediation may proceed in parallel, but an affected case cannot be finalized against wording the Phase 1 audit already rejected.

## 21.1 Blocking remediation before affected case finalization

| Curriculum unit | Game issue that must be resolved/normalized before finalization |
|---|---|
| Core Case 01 | Precise 9700 BCE single-person/event domestication framing and insufficient reconstruction qualification |
| Core Case 02 | Truncated required clue; preserve qualification of salinization’s broader historical role |
| Core Case 03 | Universalizing Lumper/dependence wording and overcompressed famine causation |
| Core Case 05 | Literal “no microbial life” / “will grow nothing” subsoil claims |
| Core Case 07 | Overgeneralized “too clean” authenticity heuristic |
| Core Case 09 | `insight:true` clue that is operationally required to unlock the next location |
| Core Case 12 | Overstated common-mycorrhizal-network transfer claims and fossil chronology |

## 21.2 Qualification/polish dependencies

Other cases retain the Phase 1 audit qualifications even where a hard content blocker was not identified. Examples include:

- Haber vs. Bosch attribution and temperature language;
- Vertical Farm nitrogen-cycle simplification;
- chinampa terminology/source reconstruction;
- Green Revolution causal and quantitative qualification;
- karreth fictional biology vs. real radiobiology analogy;
- time-sensitive real-world analogies in the Program Capstone.

## 21.3 No silent curriculum correction

If the game remains materially wrong or overgeneralized in a way identified by the audit, the curriculum must not silently rewrite the conclusion and pretend parity exists.

Either:

- remediate the game first; or
- preserve the game conclusion as an explicitly bounded in-world/local claim only when the audit supports that treatment.

Game/curriculum disagreements must remain visible in production records until resolved.

---

# 22. Production sequence after Blueprint approval

No individual case package begins during Phase 2 Blueprint drafting.

After owner approval of the Blueprint:

1. promote the approved Blueprint to the controlled version agreed for production;
2. implement the minimal HHH registry/schema activation, including the canonical title correction and instructional-type support;
3. run frozen SSS regression against that shared-system change;
4. establish the HHH game-remediation tracker directly from the existing Phase 1 finding IDs — do not repeat the audit;
5. remediate blocking game issues in controlled work before affected case finalization;
6. produce `case-00-archive-orientation` as the first HHH package and system smoke test;
7. produce Core Case 01 as the first full historical-case prototype;
8. validate the prototype across all four roles, source-status rules, fallback, fill mode, layout, accessibility, and Teacher/Answer traceability;
9. only then scale sequentially through the remaining units in program order;
10. keep correctness/content production separate from optional later visual modernization.

Case production order follows the curriculum sequence unless a documented remediation dependency makes temporary preparation out of order useful. Release/approval order should remain deliberate and traceable.

---

# 23. HHH production-ready definition

An HHH unit is not production-ready merely because four roles render.

Before owner review, the unit must satisfy all applicable requirements below.

## Instructional

- central learning goal matches the Blueprint and audit;
- historical reasoning operation is explicit;
- Student tasks process evidence rather than copy clues;
- culminating product matches the disciplinary task;
- transfer/exit measures reasoning rather than simple recall.

## Source/provenance

- every major source has accurate origin/status;
- reconstructions are labeled;
- fictional records are not presented as real historical primary sources;
- contribution and limitation are represented where relevant;
- maps/data are sourced and dated;
- debated evidence remains debated;
- two-layer truth is explicit where required.

## Cross-role

- task registry is authoritative;
- Teacher procedure accounts for every Student task;
- direct Teacher task references use exact bold number/title;
- every keyable subpart has a completed Answer Key exemplar;
- Accessible adaptations preserve the answer space and meaningfully reduce avoidable burden;
- all required learner actions persist digitally.

## Fallback

- complete no-game route exists;
- fallback contains no answer leakage;
- fallback preserves the same assessed evidence relationships and rubric;
- Campaign 2 does not depend on special game bypass behavior.

## Production

- canonical HTML-only package sources are complete;
- source hashes and layout metadata are correct;
- role isolation passes;
- accessibility passes;
- color and Grayscale pass;
- print geometry and zero-overflow pass;
- no production metadata leaks into classroom pages;
- shared SSS regression remains clean where shared tooling changed.

## Remediation

- all game findings designated blocking for that unit are resolved or explicitly normalized through an owner-approved boundary;
- no audit conclusion has been silently overwritten.

---

# 24. Blueprint decisions intentionally deferred to case production

The Blueprint fixes the system without over-designing case content.

The following are decided per unit within this architecture:

- exact Student task titles and final task count;
- exact page counts for Student, Answer Key, and Accessible;
- whether a particular Core Case uses canonical CER or another approved culminating product;
- exact historical source selections and excerpts;
- case-specific visuals within the approved HHH families;
- exact rubric criteria and descriptors;
- realistic single-period vs. multi-period timing;
- exact placement of a no-game dossier inside the four-role package;
- final learner-facing subtitle/location wording;
- optional extension content.

These are not permission to redesign the program architecture. They are case-level authoring choices constrained by this Blueprint, the audit, and the shared production contracts.

---

# 25. Blueprint approval and phase closeout

The owner approved this Blueprint on 2026-08-11 as the governing HHH architecture. Phase 2 is closed when this approved version is committed under:

```text
hhh/blueprint/
```

The following are locked before case production:

- 15-unit topology;
- 12 Core Case count;
- Orientation / Synthesis / Capstone roles;
- flexible historical-reasoning product policy;
- CER-not-universal policy;
- fictional/future two-layer truth policy;
- complete no-game fallback policy;
- no Campaign 2 direct-launch modification;
- four-role architecture;
- Teacher seven-function contract;
- Answer Key completed-exemplar rule;
- Accessible co-authoring/scaffolding rule;
- source/provenance architecture;
- standards classification strategy;
- recurring HHH visual/task families;
- campaign-local package organization;
- one shared package/registry system with minimal instructional-type extension;
- game-remediation gates;
- production sequence.

The next phase is **HHH production activation and sequential package production**, beginning with the shared HHH activation/regression step and then Archive Orientation / Core Case 01 according to the production sequence above.

---

# 26. Phase 2 decision record

| Decision | Locked result |
|---|---|
| Core case count | 12 |
| C1 L0 | Archive Orientation; package in Campaign 1 as `case-00-...`; not a numbered Core Case |
| C1 L1–L6 | Core Cases 01–06 |
| C1 L7 | Campaign 1 Synthesis/Debrief; not a numbered Core Case |
| C2 L0–L5 | Core Cases 07–12 |
| C2 L6 | Program Capstone; no Case 13 |
| Final reasoning products | Flexible historical reasoning products; CER only when appropriate |
| Fictional Core Cases | Retained under explicit two-layer truth policy |
| Campaign 2 access | Normal game progression when available + complete no-game fallback; no special direct-launch system |
| Package roles | Student / Teacher / Answer Key / Accessible only |
| Grayscale | Presentation state, not role |
| Special-unit production | Same package/editor/validation system as Core Cases |
| Folder rule | Campaign-local and instructional order |
| Registry/schema | Minimal instructional-type support; do not reopen SSS |
| Source status | Origin/provenance and evidentiary status kept distinct |
| Standards | Directly Assessed / Supporting / Contextual |
| Game audit | Phase 1 closed; do not repeat |
| Game conclusions | No silent curriculum rewrite of audited conclusions |

---

**END — `HHH_CURRICULUM_BLUEPRINT_v1.0`**
