# SSS/HHH Accessible Adaptation Contract v1.0

**Status:** `FINAL_SSS_REMEDIATION_CONTRACT`  
**Authority:** post-release unified SSS Campaign 1 + Campaign 2 audit

## Purpose

The Accessible edition is the same lesson made more navigable and more supported. It is not a different lesson, not a low-expectation substitute, and not a Student worksheet with larger type and larger boxes.

The governing target is a **hand-holding version of the Student edition** that preserves the essential learning goal while reducing avoidable reading, working-memory, inference, organization, and writing burden.

## Core equivalence rule

For every Student task, the Accessible edition must preserve:

- the same essential learning target
- the same underlying evidence relationship
- the same central diagnosis/mechanism when the case has one
- the same scientific and numerical boundaries
- the same task order unless an approved case-specific layout contract says otherwise

The Accessible prompt may change the route to the answer. It must not accidentally change the accepted answer space in a way the common Answer Key rejects.

## Default support hierarchy

Use the least intrusive support that makes the task independently usable. Supports may be combined.

1. shorter/chunked directions
2. one action per step
3. plain-language vocabulary beside the task
4. explicit evidence pointers
5. sentence frames or response stems
6. word/phrase banks
7. a worked example that uses analogous or non-answer content
8. partially completed rows or model stages
9. prefilled labels/statuses that are not themselves the learning target
10. reduced repeated writing while preserving the reasoning operation
11. selected-response or bounded-choice support where open recall is not the target
12. bullets, labels, diagrams, dictation, or typed responses accepted instead of full prose where appropriate

## Partial-completion policy

Partial completion is explicitly allowed and expected when a task's burden comes from repetition rather than from the reasoning target.

### Five-source contribution/limit tasks

A five-source table requiring ten open responses plus synthesis is normally too close to the full Student workload.

Preferred Accessible patterns include:

- fully model Source 1; students complete Sources 2–5
- prefill each source's contribution and ask only for the limit
- prefill alternating contribution/limit cells
- give two selectable candidate limits and ask the learner to justify one
- reduce each source to one short response plus one final synthesis

The final synthesis remains because convergence across sources is usually the learning target.

### Mechanism/pathway tasks

If the Student edition requires several blank stages, the Accessible edition should generally provide:

- first and last stages fixed
- at least one middle stage completed or strongly cued when sequencing itself is not the sole target
- an exact phrase bank when ordering is the target
- a short prompt asking what the model still does not establish when boundary reasoning matters

### Alternative-diagnosis tasks

When the Student edition requires selecting the best diagnosis and writing multiple rejection paragraphs, the Accessible edition may:

- pre-mark obvious rejected statuses
- ask for evidence against only one or two alternatives
- provide a word bank of relevant evidence
- keep the best-supported choice and one evidence-based rejection as the minimum independent reasoning product

Do not remove alternative evaluation entirely when it is central to the task.

## Reading and evidence-load policy

Accessible pages should avoid requiring learners to repeatedly search several pages for the evidence needed for one prompt.

Where practical:

- place the needed evidence on the same page
- summarize a previously introduced record without changing its meaning
- bold or label the exact column/row needed
- explicitly say which table/figure to use
- avoid decorative or implementation detail that competes with the task

## Writing-load policy

Response-area size follows expected response, not available white space.

- one word / label / classification -> compact field
- short evidence phrase -> short field
- several sentences / explanation -> medium or large field
- CER -> approved canonical CER layout

Do not enlarge short-answer fields merely to consume page space.

## CER policy

The approved Accessible CER remains a full, protected page unless an already-approved case-specific combined contract exists.

Canonical subtitle:

> You may write sentences or use bullet points. Use evidence from more than one source.

CER should not be redesigned merely because the surrounding Accessible tasks are being remediated.

## Numerical and science boundaries

Accessibility does not permit changing the science.

Preserve exactly:

- inequalities such as `<5%` and `<0.01 mGy/day`
- ranges such as `40–80 ppb`
- `about`, `approximately`, `modeled`, `reported`, and detection-limit qualifiers
- distinctions between measured, modeled, inferred, and established values
- case-specific versus established-Earth-science boundaries

Simplifying vocabulary is allowed. Removing a qualifier that changes the claim is not.

## Answer Key compatibility

The common Answer Key must explicitly recognize the Accessible wording where the Accessible edition uses a legitimately different response form.

Validation and review must compare:

`Accessible prompt -> permitted response -> Answer Key acceptance language`

The Silent Grove final audit demonstrated why this matters: a prompt that invites either a five-hour or six-hour design choice cannot share a key that accepts only the six-hour choice.

## Digital fill-mode policy

Every required action must be recordable in fill mode.

If the printable instruction says:

- mark
- circle
- select
- choose
- put an X
- classify
- rank

then the HTML must expose a persistent `data-response` control or equivalent persistent state for that action.

A purely visual print instruction with no persistent digital control is a defect.

## Teacher guidance requirement

Teacher Editions should name the meaningful adaptations actually present in the Accessible packet, not merely state that an Accessible edition exists.

Teacher guidance should identify, as applicable:

- prefilled elements
- reduced repeated writing
- word/phrase banks
- selected-response support
- acceptable response modes
- when the teacher may scribe/read aloud
- what essential criterion still must be demonstrated independently

## Page-count policy

Do not add Accessible pages by default. Recompose within the approved page count when possible.

Extra space/pages are justified only when accessibility genuinely requires them. A page-count increase is not a substitute for reducing repeated workload.

## Validation implications

Mechanical checks should flag for manual review:

- tasks with unusually high counts of open response controls
- Accessible tasks that have the same or greater number of blank response controls as the corresponding Student task
- multi-source matrices with no modeled/prefilled cell
- prompt wording that conflicts with Answer Key acceptance language
- required mark/select actions without persistent controls

Manual review remains required because meaningful scaffolding cannot be reduced to response-count arithmetic alone.

## HHH production rule

Future HHH Accessible editions should be authored from this contract at first production. Do not create the full Student task first and postpone accessibility to a later cleanup pass when the task can be scaffolded structurally from the beginning.