# SSS/HHH Teacher Edition Contract v1.0

**Status:** `FINAL_SSS_REMEDIATION_CONTRACT`  
**Authority:** post-release unified SSS Campaign 1 + Campaign 2 audit  
**Template authority:** corrected SSS Campaign 1 Case 01 Teacher Edition

## Purpose

This contract turns the final SSS audit's Teacher Edition findings into a reusable production rule for all SSS remediation and future HHH production. It governs function and recurring structure, not case-specific wording.

A later Teacher Edition may contain case-specific material, but it must look and function like one common Teacher system populated with case content. A case is not permission to invent a new Teacher document.

## Canonical seven-function architecture

The corrected SSS C1 Case 01 Teacher Edition defines seven required instructional functions. The preferred implementation is seven pages. A case may use more pages only when a genuinely necessary case-specific or explicitly multi-period implementation cannot fit without harming usability. Additional pages do not remove any required function.

### Function 1 — teacher launch sheet

Must provide:

- before-class preparation
- game launch path or explicit no-game path
- correct diagnosis / central explanation
- concise lesson-flow overview
- essential evidence
- likely sticking point
- what to collect
- technical/classroom fallback
- teacher line or equivalent framing

### Function 2 — lesson and standards overview

Must provide:

- lesson overview / phenomenon
- guiding or mission question
- standards alignment with limitations
- measurable learning objectives
- success criteria
- academic vocabulary
- materials and technology
- preparation / planning notes

### Function 3 — complete teaching procedure

Must provide:

- coherent timed or period-based flow
- every registry-defined Student task in instructional order
- facilitation prompts where needed
- transitions and collection points
- enough detail that a teacher does not discover required Student work only after opening the learner packet

Every required Student task must be explicitly represented in the Teacher procedure. Grouping adjacent tasks is allowed only when all included task numbers are named.

An explicitly multi-period case may state periods rather than minutes, but the procedure must still give a complete ordered classroom route.

### Function 4 — assessment and support

Must provide:

- formative checks
- assessment guidance
- accessibility/differentiation guidance
- likely misconceptions and redirects
- science/source-status boundaries
- gameplay-unavailable fallback where relevant

### Function 5 — evidence and reasoning architecture

Must provide:

- evidence/source architecture
- reasoning path or mechanism logic
- distractor / competing-explanation treatment
- scientific boundary
- instructional emphasis

Runtime implementation identifiers are never teacher-facing content. Do not print clue IDs, node IDs, source code paths, dialogue routes such as `crew.start->...`, internal release-management notes, or other implementation-only identifiers.

### Function 6 — grading contract

Must provide both:

1. a concise classroom/quick rubric; and
2. a full analytic 4/3/2/1 rubric.

The analytic rubric must use four performance levels and case-appropriate criteria. The exact criterion names may vary, but the system must cover the major assessed reasoning products for the case, including evidence, mechanism/reasoning, appropriate boundaries/precision, and design/communication where those are assessed.

Do not replace this with:

- Full / Partial only
- Secure / Developing / Not yet only
- a point list with no performance-level descriptors
- prose saying the Answer Key is sufficient

### Function 7 — sources and complete fallback

Must provide:

- authoritative source/reference list for any established science used by the Teacher Edition
- standards/source provenance as appropriate
- no-game evidence digest or equivalent complete printed-evidence fallback
- classroom/technical fallback

A source-status ledger is useful but does not substitute for an authoritative reference list when the Teacher Edition draws on external established science.

## Task traceability rule

For each registry-defined task, the system must be able to trace:

`task registry -> Student action -> Teacher procedure/support -> Answer Key exemplar -> Accessible adaptation`

A missing Teacher procedure step is a defect even if the Teacher Guide discusses the concept somewhere else.

## Scope integrity rule

Teacher fallback, shortening, differentiation, or time-saving guidance must not silently remove part of a registry-defined graded task.

If a teacher is given a shortened route, the guide must identify it as a modified assessment route and state what evidence/criterion is no longer being assessed. The default route preserves the full task contract.

## Answer-space integrity

Teacher grading language must agree with both Student and Accessible prompt wording. The Teacher Edition must not narrow an Accessible response space that the Accessible prompt intentionally broadens, nor require evidence that appears only in gameplay when the learner packet is designed to stand alone.

## Timing policy

Cases should provide a realistic core implementation route.

- Single-period cases should identify a teachable core route rather than merely summing every possible discussion block.
- Multi-period cases may remain multi-period when that is genuinely part of the case design and is stated explicitly.
- Optional extension time must be distinguishable from required assessment time.

## Layout policy

Preserve the approved fixed printable geometry and established SAA visual language. Remediation should recompose within the existing Teacher page count where practical. Page-count changes require a genuine instructional/layout reason, not merely convenience.

## Validation implications

Mechanical validation should check at minimum:

- every registry task appears in Teacher instructional support
- a procedure/flow function exists
- a quick rubric exists
- a 4/3/2/1 analytic rubric exists
- an authoritative source/reference section exists where established science is presented
- internal runtime IDs/node paths are absent from Teacher-visible content
- Teacher page references to learner editions agree with package page counts

Manual review remains required for quality of facilitation, pacing, misconceptions, and case-specific depth.

## HHH production rule

HHH starts from this contract rather than from any individual later SSS Teacher Guide. New task types should extend the closest existing Case 01 function rather than creating a new document architecture.