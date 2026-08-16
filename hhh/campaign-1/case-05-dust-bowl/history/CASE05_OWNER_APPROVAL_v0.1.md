# Core Case 05 — The Dust Bowl — Owner Approval v0.1

**Case ID:** `HHH-C1-CASE05`
**Runtime title:** The Dust Bowl
**Curriculum version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-16

## Owner statement

> I approve Core Case 05. On-screen review passes and physical printing at 100% / Actual Size passes.

## Owner-approved printable baseline

```text
8bf2d6a299f96228fc0f1bbdb6e50000074e7298
```

This is the exact commit the owner reviewed on screen and printed. It is the
printable baseline for this release.

Release conversion changes no printable source. `content.html`,
`presentation.css` and `layout-overrides.json` are byte-identical to that commit,
and only `task-registry.js` moves, in its two lifecycle keys, neither of which
renders. The commit whose tree first carries the released certified source bytes
is therefore the release-conversion commit rather than the printable baseline,
and the two are recorded separately and deliberately.

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
| Student Mission | 10 |
| Teacher Guide | 8 |
| Answer Key | 6 |
| Accessible Mission | 17 |
| **Total** | **41** |

## Independent engineering disposition

```text
INDEPENDENT_CASE05_FINAL_CONFIRMATION_PASS — READY_FOR_OWNER_GATE
```

Engineering review was closed at the baseline above before the owner gate opened.

## Post-review change control

**No classroom-content change and no artwork change was made after independent
review closed, and none after owner approval.** The commit the independent
reviewer passed, the commit the owner reviewed on screen, and the commit the
owner printed are the same commit: `8bf2d6a`. The owner's approval therefore
covers exactly the reviewed byte set.

The only post-approval change is the release lifecycle stamp, which is
non-rendering metadata.
