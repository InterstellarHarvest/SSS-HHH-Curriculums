# Core Case 06 — The Vertical Farm — Owner Approval v0.1

**Case ID:** `HHH-C1-CASE06`
**Runtime title:** The Vertical Farm
**Curriculum version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-16

## Owner statement

> I approve Core Case 06. On-screen review passes and physical printing at 100% / Actual Size passes.

## Owner-approved printable baseline

```text
865cae7177cafdcc19dcff1a6b13340d14e0f393
```

This is the exact commit the owner reviewed on screen and printed. It is the
printable baseline for this release.

Release conversion changes no printable source. `content.html`,
`presentation.css` and `layout-overrides.json` are byte-identical to that commit,
and only `task-registry.js` moves, in its two lifecycle keys, neither of which
renders. The commit whose tree first carries the released certified source bytes
is therefore the release-conversion commit rather than the printable baseline,
and the two are recorded separately and deliberately.

## Owner-approved candidate bundle

```text
ca5c0ae00633c9b9f36fc40d0ccb26dca3ed1f3f23f71bc0115016d6b91a3300
```

`hhh-c1-case06-vertical-farm-candidate.bundle`, over
`6b0e060adb54fd6b91adff766bb537f1a40b8798..865cae7177cafdcc19dcff1a6b13340d14e0f393`.
Retained as evidence of the exact byte set the owner approved.

## Owner-approved source hashes

| Source | SHA-256 |
| --- | --- |
| `content.html` | `ab7cd44ce5d49f529ba03553fb22732636d0c6c0bcb8249b990275b3c143a2c7` |
| `presentation.css` | `db63f27b17745d618cb8edd97520db891b99612a2739b4c7acb739e406c9b238` |
| `task-registry.js` | `a218391dc5b7d5b782f85d28161a4307abaffdaaf09fff5c1857cb12579455c7` |
| `layout-overrides.json` | `e5c5173694ce87bb9da403a9615bac77c9a98769b1abe7793684cb2343db3516` |

The first, second and fourth are the released certified hashes unchanged. Only
`task-registry.js` is restamped by release conversion, to carry the lifecycle
keys.

## Gates

| Gate | Result |
| --- | --- |
| On-screen review, all four roles | **PASS** |
| Physical print, browser at 100% / Actual Size | **PASS** |

The owner reviewed the rendered packet through the local Curriculum Editor
served from the exact baseline above, and printed it from the browser print
dialog at 100% / Actual Size with no fit-to-page or shrink-to-fit scaling.

**No canonical PDF was produced, approved, or required.** Production is HTML-only.
Any PDF exported from a browser is noncanonical and carries no accessibility
guarantee. PDF generation is not a project release gate.

## Classroom pages approved

| Role | Pages |
| --- | --- |
| Student Mission | 11 |
| Teacher Guide | 10 |
| Answer Key | 5 |
| Accessible Mission | 17 |
| **Total** | **43** |

Eight visible instructional tasks.

## Independent engineering disposition

```text
INDEPENDENT_CASE06_POST_OWNER_TRIM_PASS — READY_FOR_RELEASE_CONVERSION
```

## Review and correction provenance

Unlike Case 05, the commit that passed the first full independent review and the
commit the owner approved are **not** the same commit for this case. The sequence
is recorded here so the approval cannot be misread.

1. The original full independent review passed candidate
   `781c6f633558e6f188b39458d10099b43c68e986`.
2. Owner review then generated bounded classroom corrections — not defects, but
   the owner's own direction on packet length and task structure.
3. A correction rereview found three remapping defects.
4. Those were corrected.
5. The final microfix rereview passed.
6. The owner made one final STATUS-tail trim while the owner gate was still open.
7. The owner reviewed and physically printed the resulting commit,
   `865cae7177cafdcc19dcff1a6b13340d14e0f393`.
8. The owner approved that exact commit.
9. A read-only post-owner trim confirmation then passed against the **same**
   commit, changing no bytes.

The five owner-correction commits after the originally reviewed candidate, linear
and with zero merges:

| # | Commit | Subject |
| --- | --- | --- |
| 1 | `c80c11f74051a350866bff52fcd82a1999f9b5a4` | Owner review round 1: trim STATUS suffixes and lift Part A above its figure |
| 2 | `ef9c90189e6636ed484a0008fb100c2da6de38b9` | Merge the science file onto three learner cards and drop Student to 11 pages |
| 3 | `bcf92ae9eb95c288af8c3b9a3e49731d14d21539` | Fold Task 7 into Task 8 as one five-part task, and cut the Answer Key to 5 pages |
| 4 | `a4e60d518ebd3b3e635e72dc3e196c414399980a` | Correct Case 06 source spans and fallback task map |
| 5 | `865cae7177cafdcc19dcff1a6b13340d14e0f393` | Trim the redundant tail from the fictional STATUS line |

## Post-review change control

**The exact commit the owner approved was independently confirmed after approval,
with no modifications.** The post-owner trim confirmation was read-only and
changed no bytes.

**No commit exists after the owner-approved printable baseline before release
conversion begins.** `865cae7` was the branch tip when this conversion started.

The only post-approval change is the release lifecycle stamp, which is
non-rendering metadata.
