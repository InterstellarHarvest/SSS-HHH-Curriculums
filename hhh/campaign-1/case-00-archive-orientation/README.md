# HHH Campaign 1 — Archive Orientation

**Identity:** `HHH-C1-CASE00` · instructional type `ORIENTATION` · registry title *Temporal Agricultural Archive Facility* · learner-facing name **Archive Orientation**

The first Hunger, Harvest, & History curriculum package, and the production-architecture
smoke test the approved Blueprint calls for before Core Case 01.

## What this unit teaches

Archive, record, source status, provenance, corroboration, and accession — and the
difference between a claim an archive has *preserved* and a claim history has *verified*.
It is not a numbered Core Case and is deliberately not forced onto the Core Case spine.

The culminating product is a short archive-procedure and source-status explanation
(Task 5), followed by a transfer exit (Task 6) that applies the procedure to a record the
unit never supplied.

## Deliberate design decisions

**No canonical CER.** The Blueprint fixes this unit's culminating product as an archive
procedure "rather than a historical diagnosis", and there is no competing interpretation
for a Claim–Evidence–Reasoning frame to adjudicate. Using CER here would require
manufacturing a dispute the evidence does not contain, and would set exactly the
imitate-SSS precedent the Blueprint's CER policy exists to prevent. Teacher page 4 states
the rationale for classroom readers.

**Learner-facing title.** Pages print `Archive Orientation` — the registry `displayLabel`
and the name the Blueprint uses for the unit. The registry `title`
(*Temporal Agricultural Archive Facility*) is the in-fiction facility name and appears in
the page subtitle and in the package `title` field, where registry/package parity requires it.

**Fiction boundary, scoped honestly.** TAA, the Concord, the Zhel’ii, and resonance
threading are all named as invented, as the Blueprint boundary requires. The two peoples
sit differently in this level and the framing says so: the **Concord** does not appear in
the orientation and belongs to the wider story, while the **Zhel’ii** do appear — Zel'keth
is Zhel’ii, and Zel'keth's testimony is one of the four orientation sources students weigh
in Task 3. Both are marked fictional in Task 4; being present in the level is not the same
as being real.

**Dossier placement.** The compact orientation dossier is Student page 2 and Accessible
page 3, not a Teacher appendix. That makes the packet independently teachable and
assessable with no device in the room, and keeps the fallback inside the four-role package
without creating a fifth role. The Accessible dossier is an intentionally shortened form
of the same four sources.

## Source provenance

Every dossier quotation is reproduced verbatim from the orientation level at the audited
game baseline `9b8545ed6ecf98b337326390400076e36789e056`, and each quoted source is one of
the four the Phase 1 audit records as required. Nothing in this package quotes optional
dialogue that a playthrough is not guaranteed to reach, and nothing depends on a game
state, score, or completed level.

The unit carries no game-remediation dependency: the audit records `finding_ids: []` and
disposition `READY_WITH_BOUNDARY_NOTE` for this level.

## Package contents

```
source/case-package.json     canonical registered package
source/content.html          all four roles as one worksheet fragment
source/presentation.css      case presentation, TAA identity, HHH tokens
source/task-registry.js      six tasks, authoritative for numbers and titles
source/layout-overrides.json response eligibility and lock classification
```

Roles and page counts: Student 4 · Teacher 7 · Answer Key 3 · Accessible 5.
Grayscale is a presentation state on every role, never a fifth role.

```
history/release-v0.1.json               canonical release record
history/CASE00_OWNER_APPROVAL_v0.1.md    owner approval for v0.1
```

## Lifecycle

Released. `status: APPROVED_STABLE`, registry `packageStatus: APPROVED`, approval
`APPROVED` by Nate / Owner on 2026-08-12, print `PASS` at 100% / Actual Size.

This is the first release of v0.1 — not a corrective reissue. There is no prior approved
release and no former generated artifact: the case was authored natively as a package
source, so `formerArtifacts` is `NO_FORMER_GENERATED_ARTIFACTS`.

The owner reviewed and printed the content at
`05f2b5353b8779d9c5769172d94cd10e9049180f`. Release conversion changed no printable
source — only `task-registry.js` moved, to carry the lifecycle stamp — so the approved
pages and the released pages are the same pages.

Production is HTML-only. No canonical PDF artifact exists and PDF generation is not a
release gate.
