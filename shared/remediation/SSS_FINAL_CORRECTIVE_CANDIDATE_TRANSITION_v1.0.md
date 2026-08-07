# SSS Final Corrective-Candidate Transition v1.0

**Status:** `CANDIDATES_OPEN — VALIDATION_IN_PROGRESS`  
**Branch:** `remediate/sss-final-system`  
**Frozen curriculum authority:** `f7a24423f802a095aa149f923d05475ba2837599`  
**Frozen game authority:** `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`

## Why the lifecycle changed

The unified final audit and remediation changed canonical curriculum source after the previous releases were approved. Modified source cannot continue to advertise the superseded approved version or its owner/print gates. The repository's established corrective-release lifecycle is therefore now active for all thirteen SSS packages.

## Candidate versions

| Case | Previous approved release | Corrective candidate |
|---|---:|---:|
| C1 Case 01 — ISS Greenhouse | 1.1 | 1.2 |
| C1 Case 02 — Lunar Greenhouse | 1.0 | 1.1 |
| C1 Case 03 — Mars Habitat | 1.1 | 1.2 |
| C1 Case 04 — Hayes Orbital Station | 1.0 | 1.1 |
| C1 Case 05 — Sub Surface Bunker | 1.0 | 1.1 |
| C1 Case 06 — First Contact Protocol | 1.0 | 1.1 |
| C1 Case 07 — The Gift | 1.0 | 1.1 |
| C2 Case 01 — Heavy Hands | 1.1 | 1.2 |
| C2 Case 02 — The Missing Dance | 1.1 | 1.2 |
| C2 Case 03 — The Wrong Color of Light | 1.1 | 1.2 |
| C2 Case 04 — The Silent Grove | 1.1 | 1.2 |
| C2 Case 05 — Too Clean a Room | 1.1 | 1.2 |
| C2 Case 06 — The First Garden | 1.1 | 1.2 |

## Candidate state

For every package:

- registry/package status: `DRAFT`
- central package status: `DRAFT`
- owner gate: `OWNER_REVIEW_NOT_STARTED`
- print gate: `NOT_RUN`
- no candidate approval date
- no current `releaseHistory` / `historyRecord` pointer
- package output/document identity names the corrective-candidate version
- current canonical source hashes certify the remediated sources
- task-registry lifecycle metadata is reset where that registry already supports it
- previous game/audit baselines are retained as historical inputs; the frozen game repository itself is unchanged

## Historical preservation

A compare from frozen curriculum main through the corrective-candidate head shows no changed file under any SSS case `history/` directory. Previous release records, owner approvals, audit records, and accepted lifecycle history remain byte-preserved.

The corrective-candidate validator separately requires:

- the prior `release-v<approved>.json` file to remain present,
- no `release-v<candidate>.json` file to exist before new approval,
- no historical file to differ from frozen main,
- all current source hashes to match the candidate source.

## Validation state entering this phase

Already passed on the remediated source before lifecycle reopening:

- deterministic transformer idempotency
- final cross-edition Teacher/Answer/digital-action quality contract across all 13 cases
- audit-specific Accessible remediation contract across all 13 cases
- legacy full static suite diagnostic

The next gate validates the candidate lifecycle itself, generic release integrity, canonical package structure, layout overrides, then candidate-aware static/browser/print/PDF regression.

No new release or owner approval is claimed by this record.