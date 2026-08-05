# SSS Campaign 2 · Case 01 — Heavy Hands · Owner approval v1.0

| Field | Value |
|---|---|
| Case | `SSS-C2-CASE01` |
| Runtime case | `heavy_hands` — Vressk Centrifuge Habitat, Kepler-442b Orbit |
| Version | 1.0 |
| Owner | Nate / Owner |
| Approval date | 2026-08-04 |
| Lifecycle | `APPROVED_STABLE` |
| Owner review | `OWNER_REVIEW_PASS` |
| Merge status | `READY_TO_MERGE` |
| Frozen game baseline | `29c3b222c53f51de11a3aa83e896a6d0ef6fb490` |
| Canonical source approval commit | `864156f068cf89b595e1a394f1a4294c839f2876` |

## Release gates

- On-screen content and visual review: **PASS**
- Generated PDF review: **PASS**
- Physical print at 100% / Actual Size: **PASS**
- Artifact policy: **NO_GENERATED_ARTIFACTS_COMMITTED**

## Accepted validation

| Suite | Result |
|---|---|
| Case 01 case-scoped | 69/69 |
| Case 03 case-scoped | 54/54, package byte-identical |
| Canonical case structure | PASS |
| Full static | 432/432 |
| Layout overrides | PASS across 9 registered cases |
| Authoring service | 13/13 |
| Full browser matrix | 1597/1597 across 72 case/role/presentation states |
| `git diff --check` | clean |

## Approved instructional shape

Eight tasks, identical identifiers and order in every role:

1. Frame What Has Already Been Tested
2. Ride the Merry-Go-Round
3. Think Like the Investigator
4. Why the Biggest Tubers Bend Most
5. Connect the Five Evidence Sources
6. Diagnose and Reject Alternatives
7. Explain the Diagnosis with CER
8. Write the Missing Habitat Specification

Role page counts: Student 5, Teacher 8, Answer Key 4, Accessible 8.

## Standards accepted at approval

- Direct: **MS-LS1-5**, **MS-ETS1-1**
- Supporting: **MS-ETS1-2** (conditional on the class running the Task 8 comparison systematically), **MS-ETS1-3**
- **No mathematics standard is claimed.** The packet requires no calculation anywhere, so the CCSS claims carried by an earlier draft were withdrawn rather than left unsupported.

## Decisions accepted at approval

- **Case number retained.** Case 03 was produced first as the Campaign 2 pilot. Case 01 keeps its runtime case number and is listed ahead of Case 03. Case 03's package, history and approval record are byte-identical; only its registry `displayOrder` moved from 8 to 9 so the Case menu lists Case 01 first.
- **Teaching analogy over game numbers.** The habitat's readings differ by less than a tenth of one percent across a 20 cm bed, because that bed sits inside a 224.9 m radius. A ring with a classroom-friendly spread would be about two metres across and would have to spin near 30 RPM. Learners therefore meet the relationship through a merry-go-round with three riders and invented values, marked `data-analogy` and stated on the page as not being measurements from the habitat. The reported values are retained in the Teacher Guide as reference evidence.
- **Precision material is Teacher-facing.** The relationship between the directly reported `0.00187 g` and the `0.0018 g` obtained by subtracting two rounded endpoints is offered as an optional Teacher extension, not a student task.
- **Accessible edition is a rewrite, not a reflow.** Measured at 67.7% word-sequence similarity to the Student edition, inside the 43–68% band set by the approved cases, with its own wording throughout, a word bank and a vocabulary list.

## Enforced at approval

Case-scoped validation fails the build if any role asserts that the apparent gravity tilts, rotates or
reverses across the bed; that the habitat is calibrated too strong; that Earth crops detect a
difference of this size; that the Coriolis effect is the cause; that a remedy is guaranteed; or that
the two reported difference values conflict. It also fails if the raw gravity profile reaches a
learner edition, if the analogy's invented values appear outside their marked block, if the Accessible
edition rises above 80% similarity to the Student edition, or if any internal clue tag becomes
printable.
