# Core Case 07 — The Audit — Owner Approval v0.1

**Case ID:** `HHH-C2-CASE07`
**Runtime title:** The Audit
**Curriculum version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-19

First released unit of Campaign 2, and the first HHH case whose culminating product is
a provenance and authenticity judgment rather than an explanation.

## Owner statement

> I approve Core Case 07. On-screen visual review passes and physical print review
> passes.

**Recorded exactly as given.** The owner supplied no print scale, browser, printer,
paper or colour mode, and none is asserted anywhere in this release. The engineering
colour and grayscale render checks recorded in the release record are a separate
internal measurement and are not a description of the owner's physical print method.

## Owner-approved printable baseline

```text
14b301c42d80c5d4a0a62bc94530ea6638b5a62c
```

This is the exact commit the owner reviewed on screen and printed. It is the printable
baseline for this release.

Release conversion changes no printable source. `content.html`, `presentation.css` and
`layout-overrides.json` are byte-identical to that commit, and only `task-registry.js`
moves, in its two lifecycle keys, neither of which renders. The commit whose tree first
carries the released certified source bytes is therefore the release-conversion commit
rather than the printable baseline, and the two are recorded separately and
deliberately.

## Owner-approved candidate bundle

```text
05fb11ef3da0f8af1f67a91e04bf3c745121ef468206dde1a710288b4d96360f
```

`hhh-c2-case07-the-audit-candidate.bundle`, over
`c078025678d18fb4ade9f3d15a390f01b4100733..14b301c42d80c5d4a0a62bc94530ea6638b5a62c`.
Retained as evidence of the exact byte set the owner approved.

## Owner-approved source hashes

| Source | SHA-256 |
| --- | --- |
| `content.html` | `aee07fc3700856d24c4ba388dbe30c1bbebb65bc9f9cc0c1565997902495a155` |
| `presentation.css` | `0f0d4232ed1e80fd1ed773c346051ee5c11ac32ba47a798c28fcac02a4f866dc` |
| `task-registry.js` | `934396d75886ee635eed66ff074ee2c27585b87acd7e7129362968259bda6c64` |
| `layout-overrides.json` | `bd973232e602051decf99d8ad38ee93adcce768ec3ea360f8ef7903bb3a1ba02` |

The first, second and fourth are the released certified hashes unchanged. Only
`task-registry.js` is restamped by release conversion, to carry the lifecycle keys.

## Gates

| Gate | Result |
| --- | --- |
| On-screen / Curriculum Editor visual review, all four roles | **PASS** |
| Physical print review | **PASS** |

**No canonical PDF was produced, approved, or required.** Production is HTML-only. Any
PDF exported from a browser is noncanonical and carries no accessibility guarantee. PDF
generation is not a project release gate.

## Classroom pages approved

| Role | Pages |
| --- | --- |
| Student Mission | 8 |
| Teacher Guide | 7 |
| Answer Key | 4 |
| Accessible Mission | 10 |
| **Total** | **29** |

Eight visible instructional tasks. Task 2 is deliberately non-keyable and is omitted
from the Answer Key without renumbering.

## Independent engineering disposition

```text
INDEPENDENT_CASE07_POST_OWNER_PASS — READY_FOR_RELEASE_CONVERSION
```

## Review and remediation provenance

Five linear commits, zero merges, each independently reviewed before the next was
authorised. The sequence is recorded here so the approval cannot be misread.

| # | Commit | Contribution |
| --- | --- | --- |
| 1 | `fcb3b9060cd608baaa650e2b5f219a477df3b355` | Original candidate. Full independent review returned `CASE07_INDEPENDENT_REVIEW_REMEDIATION_REQUIRED` on two findings. |
| 2 | `143f953dde7c15f470926c0acc2806009340f412` | Substantive remediation: corrected the Task 3 item 3 evidence attribution from the audit log to the note on file, and demoted CCSS RH.6-8.9 from directly assessed to supporting. |
| 3 | `0c4e0560ea625cfea3ba6b5070254880c025e96d` | Standards-lock dependency: validator partition updated to the corrected ruling. Independent re-review returned `CASE07_REMEDIATION_REREVIEW_PASS_WITH_NONBLOCKING_NOTES`. |
| 4 | `45e3826741e56ab5554d608a84ad3a08868f563d` | Shared clarification `STUDENT_FACING_METADATA_AND_VISUAL_HIERARCHY_v1.0.1`, codifying the owner's visual ruling for future cases. |
| 5 | `14b301c42d80c5d4a0a62bc94530ea6638b5a62c` | Owner visual remediation: concise `SOURCE STATUS · <CLASSIFICATION>` bands, removed nested figure frames, label/field grouping. Independent review returned `CASE07_OWNER_VISUAL_REVIEW_PASS_WITH_NONBLOCKING_NOTES`. |

The owner then completed Curriculum Editor visual review and physical print review
against commit 5 and approved that exact byte set.

## Post-review change control

**The exact commit the owner approved was independently confirmed after approval, with
no modifications.** The post-owner confirmation was read-only and changed no bytes.

**No commit exists after the owner-approved printable baseline before release
conversion begins.** `14b301c` was the branch tip when this conversion started, and no
tag or other ref contained it.

The only post-approval change is the release lifecycle stamp, which is non-rendering
metadata.
