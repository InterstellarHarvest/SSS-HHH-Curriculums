# Campaign 1 Synthesis — The Temporal Agricultural Archive — Owner Approval v0.1

**Unit ID:** `HHH-C1-SYNTHESIS`
**Display label:** Campaign 1 Synthesis
**Title:** The Temporal Agricultural Archive
**Instructional type:** `SYNTHESIS`
**Curriculum version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-18

## Owner statement

> I approve the Campaign 1 Synthesis.

## Owner-approved printable baseline

```text
f14797872f22fc13d4d0999871b081f88fb1e848
```

This is the exact commit the owner reviewed and approved. It is the printable
baseline for this release.

Release conversion changes no printable source. `content.html`,
`presentation.css` and `layout-overrides.json` are byte-identical to that commit,
and only `task-registry.js` moves, in its two lifecycle keys, neither of which
renders. The commit whose tree first carries the released certified source bytes
is therefore the release-conversion commit rather than the printable baseline,
and the two are recorded separately and deliberately, following the Case 03,
Case 04, Case 05 and Case 06 precedent.

## Owner-approved source hashes

| Source | SHA-256 |
| --- | --- |
| `content.html` | `941d652a90e5ac8ddd879d9d587d8d556548cbccde8d74543754dc5a8b99ccf2` |
| `presentation.css` | `101dbad6acdcaf5eba57ac7f2189eaaf6f7953b6d9e214d29d3315eb04a3a365` |
| `task-registry.js` | `c6bf63a26a6c810f51cf50ef80ca6c35c2cee686c68fc10cc1fd160ee49adc7f` |
| `layout-overrides.json` | `28f32b8e51e5317b72ec51d46717dd7868c5377b3ddffac78a3aee5a65b70033` |

The first, second and fourth are the released certified hashes unchanged. Only
`task-registry.js` is restamped by release conversion, to carry the lifecycle
keys.

## Gates

| Gate | Result |
| --- | --- |
| On-screen review, all four roles | **PASS** |
| Print status | **PASS** |

The owner reviewed the rendered packet through the local Curriculum Editor served
from the exact baseline above.

**No canonical PDF was produced, approved, or required.** Production is HTML-only.
Any PDF exported from a browser is noncanonical and carries no accessibility
guarantee. PDF generation is not a project release gate.

## Classroom pages approved

| Role | Pages |
| --- | --- |
| Student Mission | 7 |
| Teacher Guide | 7 |
| Answer Key | 5 |
| Accessible Mission | 11 |
| **Total** | **30** |

Six visible instructional tasks. Task 1 is reference and is not keyed; the Answer
Key omits it silently and does not renumber.

## Review and correction provenance

The commit that was first built as a candidate and the commit the owner approved
are **not** the same commit for this unit. The sequence is recorded here so the
approval cannot be misread.

1. Candidate 1 was built at `2f8ffd647f9b12b86f9e9e0a90d49e65b623f94d`.
2. An independent review of that candidate produced bounded findings.
3. Those findings were remediated at `05f3eee7dab37848a271379e7eae9d357ac3b895`:
   an Answer Key block that had been emitted under the wrong task heading was
   moved into the Task 2 material it keys, and four semantic guards were added to
   the unit validator.
4. A focused re-review found one remaining **blocking** source-certification
   failure: the unit asserted a Case 04 scale and interval the released Case 04
   package does not certify.
5. That was corrected at `a6b08c5f51d0b73de6398d56a6f2a3f2a90fc3db`, across all
   eight occurrences found by a programmatic sweep of the unit.
6. The owner then made a wording decision during owner review: the learner-facing
   chronology component was renamed from "rail" to "timeline"
   (`5107639cb777ea97e5c75de21156578ee8b9d9fc`), because "rail" had never been
   learner-facing language in this curriculum and "timeline" is the established
   house term the same learners already met in Case 01.
7. The registry's chronology scale note was restated in the same terminology at
   `9247e11a41d83a567da623ff51009e5308550e11`, preserving the nonuniform-span
   distinction the original wording carried.
8. The remaining registry prose and accessibility metadata were brought into
   agreement with the rendered text at
   `f14797872f22fc13d4d0999871b081f88fb1e848`.
9. The owner reviewed and approved that commit.

The five commits after the original candidate, linear and with zero merges:

| # | Commit | Subject |
| --- | --- | --- |
| 1 | `05f3eee7dab37848a271379e7eae9d357ac3b895` | Repair Campaign 1 Synthesis candidate 1 after independent review |
| 2 | `a6b08c5f51d0b73de6398d56a6f2a3f2a90fc3db` | Correct the uncertified Case 04 scale and interval claims |
| 3 | `5107639cb777ea97e5c75de21156578ee8b9d9fc` | Rename the learner-facing chronology component from "rail" to "timeline" |
| 4 | `9247e11a41d83a567da623ff51009e5308550e11` | Restate the chronology scale note in timeline terminology |
| 5 | `f14797872f22fc13d4d0999871b081f88fb1e848` | Restate the remaining registry prose in timeline terminology |

Commits 3, 4 and 5 changed terminology only. Commits 4 and 5 changed no rendered
byte at all: `content.html` is byte-identical from `5107639` through
`f147978`.

## Post-review change control

**No commit exists after the owner-approved printable baseline before release
conversion begins.** `f147978` was the branch tip when this conversion started.

The only post-approval change is the release lifecycle stamp, which is
non-rendering metadata.
