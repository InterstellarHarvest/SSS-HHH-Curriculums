# Core Case 10 — The Quiet Billion — Owner Approval v0.1

**Case ID:** `HHH-C2-CASE10`
**Runtime title:** The Quiet Billion
**Curriculum version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-22

The fourth released unit of Campaign 2, and the first HHH case whose culminating product
is a **Qualified Historical Finding** — a five-part finding that has to carry quantitative
evidence with its units, a second documented source, a causal qualification, an explicit
statement of what the evidence does not prove, and a claim about the evidence that would
be needed next.

## Owner statements

The owner gave **two separate statements**, one per gate. They are recorded here exactly
as given and are deliberately **not** combined into a single polished quotation.

**On-screen / content / visual review:**

> CASE10_OWNER_SCREEN_REVIEW_PASS

**Physical print review:**

> CASE10_OWNER_PRINT_PASS

**Recorded exactly as given.** Their approved interpretation is only that:

- owner on-screen visual and content review passed;
- owner physical print review passed.

**No print method is asserted.** The owner supplied no browser, printer, printer model,
print scale, paper type, paper size, colour or grayscale physical-print mode, print
setting, PDF workflow or other physical-print method, and none is asserted anywhere in
this release. The instructions the owner was given before printing are not evidence of
what settings the owner actually used, and no setting is inferred from them. The
engineering colour and grayscale render checks recorded in the release record are a
separate internal measurement and are not a description of the owner's review or print
environment.

## Owner-approved printable baseline

```text
990dce582f12d2f726b45b7c039ef0d34adc5c29
```

This is the exact commit the owner reviewed on screen and printed. It is the printable
baseline for this release.

Release conversion changes no printable source. `content.html`, `presentation.css` and
`layout-overrides.json` are byte-identical to that commit, and only `task-registry.js`
moves, in its two lifecycle keys, neither of which renders. The complete released
four-source byte set therefore cannot exist at the printable baseline: the released
`task-registry.js` bytes are created by release conversion, so the commit whose tree
first carries all four released hashes is the release-conversion commit. The two commit
identities are recorded separately and deliberately throughout, and conflating them is
the error this section exists to prevent.

## Owner-approved source hashes

| Source | SHA-256 at `990dce5` |
| --- | --- |
| `content.html` | `f63bb550049de09053a73dc36551677bd3e0838528e282bf702f67bb97e2a597` |
| `presentation.css` | `73e2d41b4d1bccd6824438fc90c53ec798e71cf99b69d115f5b30e39fc2ce2f4` |
| `task-registry.js` | `2860c58282a9c8905de3d507c44c2d679be8490e4c9f39bb3add9868f6a1915e` |
| `layout-overrides.json` | `7d9180892cca2ac927aa4adb53a171a1a30b9431e065ca509e6e69fee99f65b4` |

The first, second and fourth are the released certified hashes unchanged. Only
`task-registry.js` is restamped by release conversion, to carry the lifecycle keys, and
the released four-source set is therefore first created by release conversion.

## No bundle is claimed

**No owner-approved bundle exists and none is claimed.** The release-history schema
requires no bundle field, so none is recorded. No bundle file is referenced by this
record, and no bundle is treated as release evidence. Implementation tooling is not
evidence of owner bundle approval.

## Gates

| Gate | Result | Exact owner statement |
| --- | --- | --- |
| On-screen owner visual and content review | **PASS** | `CASE10_OWNER_SCREEN_REVIEW_PASS` |
| Physical print review | **PASS** | `CASE10_OWNER_PRINT_PASS` |

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

## Review and remediation provenance

Three linear commits, zero merges, each reviewed before the next was authorised. The
sequence is recorded here so the approval cannot be misread.

| # | Stage | Outcome |
| --- | --- | --- |
| 1 | `17f81c1cfe7e19a496af428a90c2793d7986d77b` | Original implementation candidate. |
| 2 | `456ee72a5b0cce4784199a976a794fd215f256f8` | PMO bounded remediation. |
| 3 | Full independent review | `CASE10_INDEPENDENT_REVIEW_FAIL` — exactly two `REQUIRED_REMEDIATION` blockers. |
| 4 | `990dce582f12d2f726b45b7c039ef0d34adc5c29` | Independent-review remediation closing both blockers. |
| 5 | Independent remediation verification | `CASE10_INDEPENDENT_REMEDIATION_VERIFICATION_PASS` against `990dce5`. |
| 6 | Owner on-screen / content / visual review | **PASS** — `CASE10_OWNER_SCREEN_REVIEW_PASS` |
| 7 | Owner physical print review | **PASS** — `CASE10_OWNER_PRINT_PASS` |

**The PMO bounded remediation.** `456ee72a5b0cce4784199a976a794fd215f256f8` corrected
three bounded items: the Case 09 forward-coupled validator, the Case 10 total
sixty-minute route, and the Government of India 2015 edition and table pin.

**The two blockers.** The full independent review returned `CASE10_INDEPENDENT_REVIEW_FAIL`
with exactly two `REQUIRED_REMEDIATION` findings:

- the Task 6 Answer Key used an off-route Dr. Rao adoption detail that was unavailable in
  the learner editions;
- the Task 7 Answer Key described India's 12.26 to 20.09 Mt six-year rise as having
  "nearly doubled".

**What that same review passed.** The review passed the broader historical, source,
design, visual, accessibility and preservation architecture. Those two findings were the
only blockers.

**The remediation.** `990dce582f12d2f726b45b7c039ef0d34adc5c29` removed the unreachable
Task 6 adoption detail, replaced the magnitude overstatement with the exact endpoints,
added Case 10-local Answer-Key evidence-reachability protection, and hardened the
production-versus-yield semantic protection.

**The verification.** The independent remediation verification confirmed, independently,
that both blockers were closed, that the reachability guard was effective, that the
`analyticVocabulary` seam was acceptable, that the production/yield guard was effective
and not overbroad, that validation was green and that preservation was green. Its
disposition was `CASE10_INDEPENDENT_REMEDIATION_VERIFICATION_PASS`.

**No further independent disposition exists.** No post-owner independent review was
commissioned for Case 10 and none is claimed here. The PMO froze `990dce5` as the
printable baseline after the two owner gates.

## Post-review change control

**No commit existed after the owner-approved printable baseline before release
conversion began.** `990dce582f12d2f726b45b7c039ef0d34adc5c29` was the branch tip when
this conversion started. Release conversion verified, before changing any byte, that the
local branch, the remote-tracking branch and the live `refs/heads/` reference on the
origin all named `990dce5`; that the branch had no descendant commit on any reference;
that local `main`, `origin/main` and the live `refs/heads/main` all still named
`a64d3ccc104a23ac1be99a435948ed39d09cf967`; that the ancestry was exactly
`a64d3cc → 17f81c1 → 456ee72 → 990dce5`; and that the feature worktree was clean with no
tracked modification, no untracked file and no stash. That is release-conversion
engineering verification, and it is not an independent review disposition.

The only post-approval change is the release lifecycle stamp, which is non-rendering
metadata.
