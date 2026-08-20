# Core Case 08 — The Floating Gardens — Owner Approval v0.1

**Case ID:** `HHH-C2-CASE08`
**Runtime title:** The Floating Gardens
**Curriculum version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-20

The second released unit of Campaign 2, and the first HHH case whose culminating
product is a geographic and historical systems explanation with source qualification.

## Owner statement

> Approved, including physical print review complete and approved.

**Recorded exactly as given.** Its approved interpretation is only that on-screen
owner visual and content review passes and that physical print review passes. The owner
supplied no browser, printer, print scale, paper type, paper size, colour or grayscale
print mode, print setting or physical-print method, and none is asserted anywhere in
this release. The engineering colour and grayscale render checks recorded in the
release record are a separate internal measurement and are not a description of the
owner's review or print environment.

## Owner-approved printable baseline

```text
a3bbb0388cdb4233500fcfd4deadc8c939a7426e
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

| Source | SHA-256 at `a3bbb038` |
| --- | --- |
| `content.html` | `531fe23cf43356e4fe1f7e6bf289c8d78c8335472f6e8ed1da77df89f7eb7c7e` |
| `presentation.css` | `858d3b35f60481b831b539c2a69bad60877e689b629525085138bce9dbdfeba4` |
| `task-registry.js` | `6763aa4dc9f7609723984c405e694d401a9ce7c73557006f1a6ed7af0228ad24` |
| `layout-overrides.json` | `e8bf275ff5251da07070a501ff60d5e273845951300704a800e5880a204efd02` |

The first, second and fourth are the released certified hashes unchanged. Only
`task-registry.js` is restamped by release conversion, to carry the lifecycle keys.

## No bundle is claimed

**No owner-approved bundle exists and none is claimed.** The release-history schema
requires no bundle field, so none is recorded. A git bundle was produced during the
original implementation report, but it covered the pre-remediation candidate
`00f21423fdaf781be5e418b749369ad22d950b47` rather than this approved baseline, and
there is no evidence that the owner inspected or approved any bundle file. It is
therefore not release evidence and is not referenced by this record.

## Gates

| Gate | Result |
| --- | --- |
| On-screen owner visual and content review | **PASS** |
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
INDEPENDENT_CASE08_POST_OWNER_PASS — READY_FOR_RELEASE_CONVERSION
```

## Review and remediation provenance

Two linear commits, zero merges, each independently reviewed before the next was
authorised. The sequence is recorded here so the approval cannot be misread.

| # | Stage | Outcome |
| --- | --- | --- |
| 1 | `00f21423fdaf781be5e418b749369ad22d950b47` | Original candidate. |
| 2 | Full independent review | `CASE08_REMEDIATION_REQUIRED` — five findings, F1 to F5. The lesson architecture itself passed. |
| 3 | `a3bbb0388cdb4233500fcfd4deadc8c939a7426e` | Bounded remediation child closing F1 to F5, changing no architecture. |
| 4 | Independent remediation re-review | `CASE08_REMEDIATION_REVIEW_PASS` against `a3bbb038`. |
| 5 | Owner screen review | **PASS** |
| 6 | Owner physical print review | **PASS** |
| 7 | Post-owner read-only confirmation | `INDEPENDENT_CASE08_POST_OWNER_PASS — READY_FOR_RELEASE_CONVERSION` |

The five remediated findings were: F1, the lakeshore-settlement relationship was true
of the plate but uncertified and visually disagreed with the drawing; F2, the H3 figure
contract forbade a drawn causeway count while requiring a causeway drawing, which no
finite drawing can satisfy; F3, three documents claimed an Accessible figure-label
support that does not exist; F4, the H8 extended description named an arrow the figure
does not draw; F5, the Teacher Guide said "three published sources" above a four-source
table.

## Post-review change control

**The exact commit the owner approved was independently confirmed after approval, with
no modifications.** The post-owner confirmation was read-only and changed no bytes.

**No commit existed after the owner-approved printable baseline before release
conversion began.** `a3bbb038` was the branch tip when this conversion started, no
descendant existed, and no tag or other ref contained it.

The only post-approval change is the release lifecycle stamp, which is non-rendering
metadata.
