# SSS Campaign 2 · Case 02 — The Missing Dance · Owner approval v1.0

| Field | Value |
|---|---|
| Case | `SSS-C2-CASE02` |
| Runtime case | `missing_dance` — Ares Botanical Garden, Olympia District, Mars |
| Version | 1.0 |
| Owner | Nate / Owner |
| Approval date | 2026-08-05 |
| Lifecycle | `APPROVED_STABLE` |
| Owner review | `OWNER_REVIEW_PASS` |
| Merge status | `READY_TO_MERGE` |
| Frozen game baseline | `29c3b222c53f51de11a3aa83e896a6d0ef6fb490` |
| Canonical source approval commit | `16c53a4bd50e6b474fe476f6e1da09c61fc5fa13` |

## Release gates

- On-screen content and visual review: **PASS**
- Generated PDF review: **PASS**
- Physical print at 100% / Actual Size: **PASS**
- Artifact policy: **NO_GENERATED_ARTIFACTS_COMMITTED**

Recorded on owner approval of content and printability.

## Accepted validation

| Suite | Result |
|---|---|
| Case 02 case-scoped | 63/63 |
| Case 01 case-scoped | 74/74, package byte-identical |
| Case 03 case-scoped | 54/54, package byte-identical |
| Canonical case structure | PASS |
| Full static | 468/468 |
| Layout overrides | PASS across 10 registered cases |
| Authoring service | 13/13 |
| Full browser matrix | 1744/1744 across 80 case/role/presentation states |
| PDF suite | 244/244 across 40 registry-derived print documents |
| `git diff --check` | clean |

## Approved instructional shape

Eight tasks, identical identifiers and order in every role:

1. Rule Things Out
2. Shake, Don't Touch
3. Look Inside the Flower
4. Ask Without Asking
5. Connect the Five Evidence Sources
6. Diagnose and Reject Alternatives
7. Explain the Diagnosis with CER
8. Specify a Safe Trial

Role page counts: Student 5, Teacher 8, Answer Key 4, Accessible 8.

## Standards accepted at approval

- Direct: **MS-LS1-4**, **MS-ETS1-1**
- Supporting: **MS-LS2-2**, **MS-ETS1-3**
- Conditional: **MS-PS4-1**, claimable only if the class explicitly models the vibration as a wave in terms of amplitude and frequency
- **No mathematics standard is claimed.** The packet requires no calculation anywhere.

## Decisions accepted at approval

- **Sequence derived, not reused.** Tasks 1–4 are specific to this case: a repeated *negative* result is its sharpest evidence, the missing element is an event rather than an object, and a knowledgeable source is bound by a cultural constraint that the investigation works with rather than around.
- **Teaching analogy over garden values.** Task 2 uses a salt shaker with invented grain counts, marked `data-analogy` and stated on the page as not being measurements from the garden. The reported garden values remain case evidence throughout.
- **Ordering.** Case 02 registers between Case 01 and Case 03. Every case keeps its runtime case number; only Case 03's registry `displayOrder` moved from 9 to 10 so the Case menu lists all three in case-number order.

## Enforced at approval

Case-scoped validation fails the build if any role describes the anther cone's pores as opening,
unsealing or sealed; asserts the pollen is blocked; calls 124 Hz a magic frequency or presents it as
sufficient on its own; generalises 124 Hz to Earth flowers; says honeybees perform floral buzzing or
that only bumblebees do; describes the flower as hearing; guarantees a remedy; calls the plant
unhealthy; or recasts the researcher's cultural constraint as secrecy. It also fails if the analogy's
invented counts appear outside their marked block, if the Accessible edition rises above 80%
similarity to the Student edition, or if any internal clue tag becomes printable.

The prohibited scan measures affirmative assertions only: a claim may appear inside a sentence that
forbids it, which is how the packet rules it out.
