# SSS → HHH Production Lessons v1.0

**Status:** `IMPLEMENTATION_HANDOFF`  
**Source:** final unified SSS Campaign 1 + Campaign 2 audit and corrective remediation  
**Applies to:** future SSS maintenance and all HHH case production

## Purpose

The final SSS audit showed that the strongest individual lessons were not enough to guarantee a consistent curriculum system. Most post-release defects came from each case independently re-solving Teacher structure, accessibility, digital response behavior, scoring, lifecycle metadata, and validation.

HHH should therefore begin from shared production contracts and shared validators rather than treating those concerns as cleanup work after lesson writing.

## 1. Author the Teacher Edition from one shared template

The corrected Campaign 1 Case 01 Teacher architecture is the system authority.

Use the shared Teacher contract:

`shared/implementation/SSS_HHH_TEACHER_EDITION_CONTRACT_v1.0.md`

Default seven-page instructional roles:

1. preparation, launch path, diagnosis, lesson flow, essential evidence, collection, fallback
2. overview, guiding question, standards, objectives, success criteria, vocabulary, materials
3. complete timed task-by-task procedure
4. formative assessment, access supports, misconceptions, science/source boundaries, fallback
5. evidence architecture, reasoning path, distractors, scientific boundaries
6. quick rubric plus complete 4/3/2/1 analytic rubric
7. authoritative sources, no-game evidence digest, classroom/technical fallback

Case-specific variation is allowed when the instructional task genuinely requires it. Independent redesign of the Teacher document is not.

## 2. Treat Student → Teacher task traceability as a production invariant

Several approved SSS Teacher Guides omitted numbered Student tasks from the actual lesson procedure even though those tasks still appeared elsewhere in rubrics or keys.

For every numbered Student task, production must establish:

`Student task → Teacher procedure → assessment/collection guidance → Answer Key when keyable`

The task registry should drive this check mechanically. A task appearing somewhere in a Teacher document is not sufficient; the actual teaching procedure must account for it.

## 3. Build the Answer Key as a completed exemplar, field by field

A correct paragraph is not enough when the Student task contains several explicit fields, rows, classifications, marks, or subparts.

For every keyable task:

- map every required Student subpart
- visibly complete every required field or row
- preserve units, bounds, qualifiers, and categories
- include concise acceptable alternatives when more than one answer is legitimately defensible
- do not make the key more restrictive than the learner prompt

The final SSS audit caught omissions that task-number-only validation did not.

## 4. Author Accessible and Student editions together

Use:

`shared/implementation/SSS_HHH_ACCESSIBLE_ADAPTATION_CONTRACT_v1.0.md`

Do not finish the Student packet and then create an Accessible packet by enlarging type and response boxes.

Accessible should be the same investigation with a more guided route:

- chunk directions
- use one action per step
- define vocabulary beside the task
- point directly to relevant evidence
- use sentence frames and word banks where appropriate
- partially complete repeated tables or pathway models
- model one row/stage when repetition is not the learning target
- reduce repeated writing while preserving the reasoning operation
- accept bullets, labels, diagrams, or short phrases where full prose is not the objective

The learner must still demonstrate the essential concept independently.

## 5. Reduce repeated workload, not the learning goal

The most common late-SSS Accessible weakness was a multi-source organizer that remained nearly identical to Student work: for example, five sources × contribution + limitation = ten open responses plus synthesis.

Preferred HHH pattern:

- model one full source row
- prefill selected contribution or limitation cells
- keep representative independent rows
- preserve the final evidence-convergence/synthesis judgment

The goal is to remove executive-function repetition, not scientific reasoning.

## 6. Preserve the canonical CER contract

Do not redesign a successful CER page merely because surrounding Accessible tasks are being simplified.

Canonical Accessible subtitle:

> You may write sentences or use bullet points. Use evidence from more than one source.

CER remains a full protected page where the approved package contract requires it. Response-area growth remains proportional to expected writing rather than unused page space.

## 7. Every printable learner action must work digitally

SSS exposed several tasks whose printed instruction said to mark, circle, choose, or put an X, while fillable HTML offered no persistent way to perform that action.

HHH production must treat the following as response operations:

- mark
- circle
- select
- choose
- classify
- rank
- place an X

Each requires a persistent, keyboard-operable response control or an equivalent persisted state.

Do not rely on a decorative square, printed checkbox glyph, or visual box with no response identity.

## 8. Classify every persistent response in the layout contract

When a new `data-response` / persisted control is introduced, its layout behavior must be explicit.

- compact marks, statuses, choices, or labels → normally locked
- short evidence phrases → compact bounded response
- substantive explanations/design responses → resizable within declared bounds
- CER → protected/locked according to the CER contract

No persistent response should silently fall outside the layout registry.

## 9. Keep implementation metadata out of classroom documents

The final audit repeatedly found runtime clue IDs, release-management wording, page-count drift, figure-rights notes, and other implementation information in Teacher-facing material.

Printable Student, Accessible, Teacher, and Answer Key documents must not expose:

- runtime clue/node IDs
- branch names or commit SHAs
- lifecycle/status banners
- release/merge instructions
- validation status
- internal repository paths
- production-only copyright/figure-development notes

Store those in manifests, audit records, validation reports, and Git history instead.

## 10. Use one shared rubric system

Do not let each HHH case invent its own scoring architecture.

Default Teacher Page 6 contains:

- a quick classroom rubric
- a complete 4/3/2/1 analytic rubric with case-specific descriptors

Case-specific point scoring may supplement the common rubric when useful, but should not replace it.

## 11. Preserve measurement and source-status discipline from Campaign 2

Campaign 2 established strong practices that should carry directly into HHH:

- measured ≠ modeled ≠ reported ≠ inferred
- a detection limit is not zero
- inequalities remain inequalities
- ranges remain ranges
- units remain attached to quantities
- one site record is not an optimum
- a case-specific hypothesis is not universal science
- missing data should remain visibly missing
- conflicting records should be compared rather than silently reconciled
- unsupported claims should become “test next” recommendations rather than conclusions

This precision is one of the strongest parts of the finished SSS system.

## 12. Make corrective releases explicit instead of rewriting approved history

When an approved package needs a genuine post-release correction:

1. preserve the approved release and owner records
2. increment the package version
3. reopen the new version as an unreleased corrective candidate
4. remove only the current-version release pointer
5. reset owner/print gates for the candidate
6. validate the candidate independently
7. create new release/approval records only after approval

Never rewrite the historical record to make the corrected content look as though it was always the approved release.

## 13. Separate correctness remediation from visual modernization

Do not combine content correction and aesthetic figure redesign in one remediation baseline.

Correctness phase:

- curriculum parity
- Teacher/Answer/Accessible fixes
- digital actions
- lifecycle
- static/browser/print validation

Visual phase:

- graphs
- timelines
- pathways
- system diagrams
- evidence-convergence figures
- biological/engineering schematics

This separation keeps regression evidence interpretable.

## 14. Use deterministic graphics for exact scientific information

For graphs, axes, exact values, technical labels, process stages, or scientific annotations, prefer deterministic SVG/HTML/CSS or equivalent editable vector construction.

Generative imagery is appropriate for:

- illustrative cutaways
- non-data habitat/equipment concepts
- art-direction exploration

Do not use generated imagery as the authoritative source of graph values, scales, units, or exact scientific labels.

## 15. Build visual families, not one-off figures

The SSS audit identified recurring figure families that should become reusable HHH components:

- telemetry/data panels
- process/pathway diagrams
- timelines/event logs
- evidence-convergence maps
- engineering control loops
- specification/verification panels
- biological cutaways
- intervention-comparison panels

The visual target remains professional mission documentation with modern information design, grayscale-first readability, restrained retro-space-agency cues, and scientific clarity before decoration.

## 16. Validation should encode system contracts, not one historical release

Shared validators should test invariants that remain correct through Draft → owner review → approved release.

Avoid hard-coded assumptions such as:

- one case must always be version `1.0`
- one package must always be `APPROVED_STABLE`
- one historical response count can never legitimately change

Prefer:

- registry/package lifecycle parity
- lifecycle-schema correctness
- task traceability
- completed-key subparts
- digital markability
- layout classification
- canonical geometry
- print/PDF page counts
- source-hash consistency
- grayscale readability

Release-specific frozen-baseline validators may remain as historical evidence, but should not be the only validator for a legitimate corrective candidate.

## 17. Production order for an HHH case

Recommended order:

1. lock case evidence and learning goal
2. author task registry
3. author Student and Accessible task structures together
4. author Answer Key field-by-field from the task registry
5. populate the shared Teacher template
6. classify all response controls in layout metadata
7. run cross-edition traceability and accessibility checks
8. run browser/fill-mode validation
9. run PDF/print geometry validation
10. perform owner content review
11. create/freeze release records
12. perform visual modernization only on a separate controlled branch when needed

## Definition of production-ready

An HHH case is not production-ready merely because all four documents render.

It is production-ready when:

- every task maps across applicable editions
- Teacher procedure can run the actual Student lesson
- Answer Key visibly completes every required keyable subpart
- Accessible support reduces avoidable burden while preserving the learning target
- every required learner action is digitally recordable
- all responses are layout-classified
- sources and science boundaries are teacher-visible where required
- no production metadata leaks into classroom pages
- static, browser, print/PDF, lifecycle, and package-integrity gates pass
- owner review has explicitly approved the candidate

This is the production baseline HHH should inherit from SSS rather than reconstructing the system case by case.
