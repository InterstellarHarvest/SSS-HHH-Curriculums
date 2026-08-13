# HHH Campaign 1 — Core Case 02 · Sumer

**Identity:** `HHH-C1-CASE02` · instructional type `CORE_CASE` · registry title *Sumer* · learner-facing label **2 - Sumer**

The second full historical Core Case in Hunger, Harvest, & History, produced against the
released Core Case 01 baseline and the approved Blueprint.

## What this case teaches

How irrigation, a shallow water table, inadequate drainage and evaporation can combine to
salinize a field — and how far that mechanism can legitimately be carried when explaining
much larger historical change. The reasoning operations are cause and consequence, systems
reasoning, and source comparison.

The culminating product is a **qualified causal explanation** (Task 8) with four required
components: the field mechanism in order with the difference named, two sources with their
statuses, one thing the evidence cannot show about the wider history, and a closing sentence
that states the salt claim at the right strength. Task 9 transfers the reasoning to an
invented district the case never supplied.

## Deliberate design decisions

**Scale is the spine.** Case 01's spine was chronology; this one's is scale. The notice on
learner page 1 names both questions the case asks — one about a single field, one about a
region across centuries — and says which of them the packet settles. Every later task sits
on one side of that line or tests it, and Task 7 makes the distinction assessable with a
three-mark scheme rather than two: **Y** supported, **N** contradicted, **?** this case
cannot decide it. A student who marks everything N has flattened exactly what is being
measured.

**The mechanism figure is a control, not an illustration.** The two soil sections in Task 4
are drawn from the same river water under the same sun and differ in one thing: whether the
water can leave. That comparison is what turns the marsh from scenery into evidence, and it
is why the shared-water statement is printed above both sections rather than inside either.
The water table is drawn high in one and low in the other, so the difference the task assesses
is visible before any paragraph is read.

**A measurement is not the same as an inference drawn from it.** Task 6 row two is the
documented soil science; row four is *using the modern crop measurements to judge an ancient
field*. Merging them is the specific error the task exists to catch, and the Teacher Guide
says so. No soil-salinity value is claimed for antiquity anywhere in this package.

**Consistency is not proof.** Task 5 sets the measured salt tolerances of barley and wheat
beside the reported change from wheat to barley. The two agree — and the task asks why that
agreement does not prove salinization, then asks for a rival explanation that fits the same
record. That rival explanation is the one actually published against the salinization thesis
in 1985, not one invented for the worksheet.

**No canonical CER.** A Claim–Evidence–Reasoning frame asks a student to defend a position.
The honest position on this case's region-scale dispute is that the evidence in the packet
does not decide it, so a CER frame would push students toward the overclaim the case exists
to prevent. Teacher page 4 states the rationale for classroom readers.

**Two periods, stated.** Nine tasks with this evidence load do not honestly fit one period.
Period 1 ends after Task 4; period 2 covers Tasks 5 to 9. The Teacher Guide names the
assessed route rather than compressing it.

**Dossier placement.** The dossier is Student page 2 and Accessible pages 2–3; the setting
diagram and modern report are Student page 3 and Accessible page 4; the cross-sections are
Student page 4 and Accessible page 5; the measurements are Student page 5 and Accessible
page 7; the competing-pressures panel is Student page 7 and Accessible page 9. Together they
carry every source the case assesses, so the packet is independently teachable and assessable
with no device in the room, and the fallback stays inside the four-role package without
creating a fifth role.

**Why there is no `source/evidence-ledger.json`.** The Blueprint names a structured ledger as
the preferred implementation *when useful*. The registered package schema is closed
(`additionalProperties: false`), its `sourceHashes` object is closed, and the shared HHH
source-ownership check requires a package to pin exactly its four canonical sources — so a
fifth file could only be carried as an embedded asset, which would push production metadata
into classroom output, or as an unreferenced orphan. The evidence model is therefore carried
where the released Case 01 carries it and where validation can already reach it: the
`caseSources` array in `task-registry.js`, extended here to the full Blueprint §11.6 field
set including `contribution`, `limitation`, `gameCorrespondence` and `fallbackCorrespondence`,
plus the Teacher Guide source ledger on page 6. No shared schema was changed for this case.

## Source provenance

**Game material.** Dossier cards A and B quote HHH Level 2 at the integrated game baseline
`d9fc16baf272cb543c29cbd0c06ec85efad60be8`. Those quotations are labelled
`STATUS: reconstructed` on the page and are never presented as testimony. Card C is
**paraphrased rather than quoted** — see the game-remediation section below. Card D, the
Background block, the modern-plain panel, the setting diagram, the cross-sections, the
tolerance figure and the competing-pressures panel are curriculum-authored from the
references below and contain no game material.

**Real-world evidence.** Every number, mechanism statement and disputed reading in the packet
traces to one of the seven references listed on Teacher page 7:

- FAO, *Water Quality for Agriculture* (Irrigation and Drainage Paper 29 rev. 1, 1985), crop
  salt-tolerance annex as revised after Maas & Grattan 1999 — the two thresholds (barley
  8.0 dS/m, wheat 6.0 dS/m) and the germination caveat.
- FAO, *Wastewater treatment and use in agriculture*, ch. 5 — capillary rise from a shallow
  water table, evaporation leaving salts behind, and the downward-flux/drainage requirement.
- FAO, *Irrigation in the Middle East region in figures — AQUASTAT Survey 2008*, Iraq profile
  — rainfall under 100 mm over 60% of the country in the south; poor drainage and salinity as
  the named hazards; the shallow saline water table; the 1970 degradation finding; the 565 km
  outfall drain completed December 1992.
- Jacobsen & Adams 1958, *Science* 128(3334):1251–1258 — the influential wheat-to-barley
  reading, presented as a reading rather than as a finding.
- Powell 1985, *ZA* 75(1):7–38 — the published challenge on translation and on barley's own
  productivity and tolerance of seasonal variation; the rival explanation in Task 5 Part C.
- Altaweel et al. 2019, *IRAQ* 81:23–46 — the audit's own source [H2]; reviews the evidence,
  records Powell's criticism, and cautions against generalizing limited samples.
- Artzy & Hillel 1988, *Geoarchaeology* 3(3):235–238 — the reply on the other side, carried so
  the dispute reads as live rather than settled in either direction.

**No false precision.** The 1958 study's specific crop percentages and yield figures are
deliberately **not** reproduced. Those numbers are precisely what the 1985 critique disputes,
they could not be verified from an accessible copy of the 1958 paper during production, and
printing them would have manufactured exactly the certainty this case is required to qualify.
The packet states the shape of the reported change and attributes it, and nothing more.

## Game-remediation dependencies

`HHH-GAME-C1L2-001` — **resolved and verified** against `d9fc16b`. The required
`irrigation_practice` clue reads “without the old fallow **rest**.” at `hhh_data.js:695`, so the
truncation is gone and the clue is quotable. Dossier card A quotes it verbatim.

`HHH-GAME-C1L2-002` — **curriculum qualification delivered, not deferred.** The audit found
that wording implying a uniquely first human-made agricultural crisis, or broad decline from
one cause, overstates historical certainty. The local mechanism is kept in full and taught as
established science. The broader claims are qualified structurally rather than by a
disclaimer: the page-1 notice names the two scales and says the big one is unsettled; Task 5
separates consistency from proof and supplies the published rival explanation; Task 6 row four
separates a measurement from an inference drawn from it; Task 7 marks the single-cause claim
**N** and the power-moved-north claim **?**; Task 8 requires a closing sentence at the right
strength; and the analytic rubric scores scale discipline as its own criterion. The four
prohibited formulations are recorded in `task-registry.js` under `scaleBoundary.prohibitedClaims`
and appear nowhere in any role.

`HHH-GAME-C1L2-003` — **nonblocking polish, still open at the audited baseline.** The level's
`scribe_record` summary contains broken syntax around “Yet, wrote the cause down…”. That
wording is reproduced nowhere in this package. Dossier card C states the same usable evidence
— falling tallies, barley displacing wheat, and a recorded cause the ground does not support —
in curriculum voice. No change was made to the game in this workstream.

## Package contents

```
source/case-package.json     canonical registered package
source/content.html          all four roles as one worksheet fragment
source/presentation.css      case presentation, TAA identity, HHH tokens
source/task-registry.js      nine tasks, authoritative for numbers and titles
source/layout-overrides.json response eligibility and lock classification
```

Roles and page counts: Student 8 · Teacher 7 · Answer Key 5 · Accessible 11.
Grayscale is a presentation state on every role, never a fifth role.

## Lifecycle

Unreleased validated candidate. `status: VALIDATION_BUILD`, registry
`packageStatus: VALIDATION`, approval `OWNER_REVIEW_NOT_STARTED`, print `NOT_RUN`.
Version 0.1.

There is no release record, no history directory and no owner-approval record, because
nothing has been approved. Physical print has not been run and is an owner gate. Production is
HTML-only; no canonical PDF artifact exists and PDF generation is not a release gate.
