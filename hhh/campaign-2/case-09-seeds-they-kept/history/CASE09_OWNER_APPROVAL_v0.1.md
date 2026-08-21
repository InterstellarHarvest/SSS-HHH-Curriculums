# Core Case 09 — The Seeds They Kept — Owner Approval v0.1

**Case ID:** `HHH-C2-CASE09`
**Runtime title:** The Seeds They Kept
**Curriculum version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-21

The third released unit of Campaign 2, and the first HHH case whose culminating product
is a **Collection Continuity Judgment** — a provenance and continuity judgment that has
to survive documented movement, reproduction and loss.

## Owner statements

The owner gave **two separate statements**, one per gate. They are recorded here exactly
as given and are deliberately **not** combined into a single polished quotation.

**On-screen / content / visual review:**

> approved good and stable

**Physical print review:**

> physical print approved

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
0202027acca362bc4b2ed4f3cee81dcdb564ee2b
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

| Source | SHA-256 at `0202027` |
| --- | --- |
| `content.html` | `2904f736c83993daf0585d5bdeed2d630a91e7847c6d43cff81fe3e5c26722cb` |
| `presentation.css` | `e7d180b152c654e22866dd56a39caff20c7ebc4435eac4b0a4a8a1c9e42c5b4e` |
| `task-registry.js` | `527f68218683d490e0e898f515537cd16fd683e2f42f51b1da4cb6808659382d` |
| `layout-overrides.json` | `590500580cd97aa47b33994f35242884b713772d803ccecc4345d1d68fd9b60f` |

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
| On-screen owner visual and content review | **PASS** | `approved good and stable` |
| Physical print review | **PASS** | `physical print approved` |

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
INDEPENDENT_CASE09_POST_OWNER_PASS — READY_FOR_RELEASE_CONVERSION
```

## Review and remediation provenance

Two linear commits, zero merges, each independently reviewed before the next was
authorised. The sequence is recorded here so the approval cannot be misread.

| # | Stage | Outcome |
| --- | --- | --- |
| 1 | `9bfbe76f8119cd76838562506a995c30895a617c` | Original candidate. |
| 2 | Full independent review | `CASE09_INDEPENDENT_REVIEW_BLOCKED` — exactly one `REQUIRED_REMEDIATION` finding. |
| 3 | `0202027acca362bc4b2ed4f3cee81dcdb564ee2b` | Bounded remediation child closing that finding, changing no architecture. |
| 4 | Independent remediation disposition | `CASE09_REMEDIATION_VERIFICATION_PASS` against `0202027`. |
| 5 | Owner on-screen / content / visual review | **PASS** — `approved good and stable` |
| 6 | Owner physical print review | **PASS** — `physical print approved` |
| 7 | Post-owner read-only disposition | `INDEPENDENT_CASE09_POST_OWNER_PASS — READY_FOR_RELEASE_CONVERSION` |

**The single blocker.** The full independent review returned exactly one
`REQUIRED_REMEDIATION` finding: the Accessible edition's Task 5 and Task 6 writing areas
were compressed below their Student equivalents. The bounded remediation child closed
it.

**What that same review passed.** The review passed the source estate, the H13
narrowing, the Loskutov certification, the two-layer truth, the standards, the
lifecycle, the parity, the no-game route and the Case09-local structural exemption
mechanism. The one finding was the only blocker.

## Post-review change control

**The exact commit the owner approved was independently confirmed after approval, with
no modifications.** The post-owner confirmation was read-only and changed no bytes.

It proved, at the time it ran, that:

- `0202027acca362bc4b2ed4f3cee81dcdb564ee2b` was unchanged;
- no descendant of it existed;
- no remote Case 09 branch existed;
- no tag and no release existed;
- the four owner-approved source hashes were intact;
- the candidate was mechanically green;
- no source or lifecycle mutation had occurred after owner approval.

**No commit existed after the owner-approved printable baseline before release
conversion began.** `0202027` was the branch tip when this conversion started, no
descendant existed, and no tag or other ref contained it.

The only post-approval change is the release lifecycle stamp, which is non-rendering
metadata.
