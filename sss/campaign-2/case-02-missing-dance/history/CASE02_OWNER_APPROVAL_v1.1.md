# SSS Campaign 2 · Case 02 — The Missing Dance · Owner approval v1.1 (corrective release)

| Field | Value |
|---|---|
| Case | `SSS-C2-CASE02` |
| Runtime case | `missing_dance` — Ares Botanical Garden, Olympia District, Mars |
| Version | 1.1 |
| Corrective of | 1.0 |
| Owner | Nate / Owner |
| Approval date | 2026-08-06 |
| Lifecycle | `APPROVED_STABLE` |
| Owner review | `OWNER_REVIEW_PASS` |
| Merge status | `READY_TO_MERGE` |
| Frozen game baseline | `29c3b222c53f51de11a3aa83e896a6d0ef6fb490` |
| Canonical source approval commit | `a3b7881932d93afb4c13cc72ba4b4e77786fd245` |
| Original v1.0 approval commit | `b4534579eab9f97195e55ef49aaa245a7fbb74f0` |

## Release gates

- On-screen content and visual review: **PASS**
- Generated PDF review: **PASS**
- Physical print at 100% / Actual Size: **PASS**
- Artifact policy: **NO_GENERATED_ARTIFACTS_COMMITTED**

All three gates were completed against the v1.1 packet. The v1.0 gates are not carried forward;
they remain recorded in `CASE02_OWNER_APPROVAL_v1.0.md` as evidence of what was approved on
2026-08-05.

## Why v1.1 exists

The Campaign 2 completion audit found that released v1.0 asked learners to mark a table column that
was not printed, and graded them against evidence their editions did not carry. Those are defects in
a packet that had already passed a physical print gate, which is why this is a corrective release
rather than an edit.

No investigation, diagnosis, task sequence or case fiction changed. The eight tasks keep their
identifiers and order in every role.

## Corrected Task 1 usability

Task 1 asks learners to rule things out by marking each record `OK` or `?`. In v1.0:

- neither learner edition printed a column to mark in;
- the Student directions referred to "the last column", which held evidence text, not a response;
- the Accessible directions named a **Table 1a** that the packet never rendered;
- the Answer Key completed a seven-row table while learners held a differently shaped one;
- the Teacher Guide described a row split that did not match the printed table, and referenced a
  **Figure 2** that does not exist.

In v1.1 both learner editions carry a writable `OK or ?` mark cell on every row, the directions name
the table that is actually printed, and the Answer Key is an exact row-for-row mirror of it. The
learner table was consolidated from seven rows to six by merging the rows that all report normal;
the Answer Key and Teacher Guide were rebuilt against that six-row shape.

## Evidence made available to learners

Two graded claims in the v1.0 Answer Key could not be reached from any learner edition:

- the **100–150 Hz** comparison band for periodic signals in other Telluvian gardens;
- the **Telluvian lyre-moth** and its hovering wingbeat near **124 Hz**.

Both now appear in the Student and Accessible editions. `Poricidal anther` and `buzz pollination`
are defined just in time for learners in both editions rather than assumed. Case-scoped validation
now fails the build if a graded Answer Key claim depends on evidence absent from the learner
editions, or present in only one of them.

## Standards withdrawn

| Standard | v1.0 | v1.1 |
|---|---|---|
| MS-LS1-4 | Direct | Direct — unchanged |
| MS-ETS1-1 | Direct | Direct — unchanged |
| MS-PS4-1 | Conditional | Conditional — unchanged |
| **MS-LS2-2** | Supporting | **Withdrawn** |
| **MS-ETS1-3** | Supporting | **Withdrawn** |

Neither withdrawn standard is met by what this packet actually asks learners to do. No mathematics
standard is claimed; the packet requires no calculation.

## Accessible differentiation and page counts

| Role | v1.0 | v1.1 |
|---|---|---|
| Student | 5 | **6** |
| Teacher | 8 | 8 |
| Answer Key | 4 | 4 |
| Accessible | 8 | 8 |

Adding a response column overflowed the first page of both learner editions. The Student edition
gained a page, with Task 1 moved onto its own. The Accessible edition cannot carry a task-free page
under the one-to-three-tasks-per-page rule, so it held 8 pages by consolidating table rows and
moving glossary entries to the point of use. Accessible differentiation remains inside the band set
by the approved cases, and every page fits in every role.

## Final `OK or ?` column-width correction

The last owner-review item. The response column was slightly too narrow and wrapped its heading.

| Role | Inner width before | Heading needs | Inner width after | Lines |
|---|---:|---:|---:|---:|
| Student | 28.9 px | 39.1 px | 47.6 px | 1 |
| Accessible | 36.8 px | 44.0 px | 47.6 px | 1 |
| Answer Key | 40.9 px | 39.1 px | 40.9 px — unchanged | 1 |

The Answer Key's status table has three columns and already fitted, so it was not touched; the rule
is scoped to the fourth column, which only the learner editions have, leaving the Answer Key's
"Why" column at its full width. Row wording, row order, table semantics, the response boxes and the
evidence column are unchanged, and the change is grayscale-neutral.

## Preservation of v1.0

The v1.0 release is **superseded, not withdrawn**. Both of its records are retained byte-identical:

- `history/release-v1.0.json`
- `history/CASE02_OWNER_APPROVAL_v1.0.md`

Neither was edited to describe v1.1. `release-v1.1.json` carries v1.0 inside
`priorApprovedReleases`, including its approval date and commit, its source hashes, its frozen DOM
baselines and its 5 / 8 / 4 / 8 page counts. Case-scoped validation fails the build if a retained
v1.0 record is rewritten to describe v1.1 content.

Frozen Student, Teacher and Answer Key DOM baselines were regenerated for v1.1. All three differ
from v1.0's, so approved-baseline enforcement cannot be satisfied by the superseded markup.

## Artifacts

**No generated artifacts are committed at either version.** This case was authored natively as a
case package and reissued the same way; no PDF, role document or screenshot was ever generated or
tracked for it. The canonical source at the approval commit is the whole release.

## Game repository

Untouched throughout the remediation. Local, `origin` and the live remote all remain at
`29c3b222c53f51de11a3aa83e896a6d0ef6fb490`, and every game worktree was clean at the release gate.
