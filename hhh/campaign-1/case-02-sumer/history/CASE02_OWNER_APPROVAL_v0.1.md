# Owner Approval — HHH Campaign 1 · Core Case 02 · Sumer · v0.1

**Curriculum:** Hunger, Harvest, & History (HHH)
**Campaign:** Campaign 1
**Unit:** Sumer — `HHH-C1-CASE02` · instructional type `CORE_CASE`
**Version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-13

## Decision

**Release status:** `APPROVED_STABLE`
**Review status:** `OWNER_REVIEW_PASS`

Owner statement of record:

> "I approve Core Case 02. On-screen review passes and physical printing at 100% / Actual
> Size passes."

## What the owner reviewed

| Check | Result |
|---|---|
| On-screen review | **PASS** |
| Physical print | **PASS** |
| Physical print basis | Browser print dialog at 100% / Actual Size |

All four roles were approved: **Student Mission**, **Teacher Guide**, **Answer Key** and
**Accessible Mission**.

**Tested owner-approved content baseline:** `ea2eab2041a76c2f5d19d5d3b2c9d700af80a663`

That commit carries the exact printable byte set the owner reviewed on screen and printed on
paper. Release conversion did not alter it: `content.html`, `presentation.css` and
`layout-overrides.json` are byte-identical to that commit, and the only source that moved is
`task-registry.js`, which carries the lifecycle stamp and renders nothing. The pages the
owner approved are the pages this release publishes, so no repeat print was required.

## Released role page counts

| Role | Pages |
|---|---|
| Student Mission | 8 |
| Teacher Guide | 7 |
| Answer Key | 5 |
| Accessible Mission | 11 |

## Production policy at approval

- HTML-only canonical production; the registered package source is the release.
- No canonical project PDF artifact and no PDF release gate. A PDF exported from the browser
  is noncanonical and carries no accessibility guarantee.
- No generated role HTML, PDF or screenshot is committed.

## Scope of this approval

This record captures the owner's instructional, visual and physical-print approval. It does
not represent the owner as having personally executed the repository's automated validation
suites; those were run by the implementation and independent-review process and are recorded
in `release-v0.1.json` under `acceptedValidation`.

## Independent review preceding this approval

The package was independently reviewed against main baseline
`b220461becc4fa7aadbbbabbb226aa0564c3c685`:

1. full review — `INDEPENDENT_CASE02_REVIEW_CORRECTIONS_REQUIRED`, two blocking findings
   (Teacher Accessible page-count drift; an Answer Key Claim 4 rationale that asserted an
   ancient record of salinity as a cause) plus five promoted observations;
2. bounded re-review — `INDEPENDENT_CASE02_BOUNDED_REREVIEW_PASS — READY_FOR_OWNER_GATE`,
   at candidate `3bbac2bc34e6d0379ec3c884f4f552bf08037948`, with one nonblocking observation
   recorded for the owner (the Claim 4 rationale cites the 1970 degradation finding, which is
   present in the Student modern-report panel and not in the Accessible one; no assessed
   response depends on it).

## Owner art-direction pass after the gate

Three commits followed the bounded re-review, at the owner's direction, and are covered by
this approval because the owner reviewed and printed the resulting pages personally:

1. `998469c` — the repeated "a scene written for the game" status tail was dropped from the
   three Student dossier cards, matching the Accessible edition; the Task 3 setting figure was
   rebuilt from a four-band stack into a schematic side view, because the bands read as a table
   and never showed the near-level ground the task asks about;
2. `0b09d59` — the unexplained dashed field box was removed, reeds were added at the marshes,
   the flow arrow was lifted clear of the slope, the Gulf label was raised, and the figcaption
   was folded into the extended description;
3. `ea2eab2` — the reed bed was extended under the marshes label and the reeds given leaves.

That pass changed presentation and one figure only. No source certification, evidentiary
status, crop-tolerance value, claim mark, task architecture or standards claim was altered.
The geographic sourcing disclaimer the retired figcaption carried — curriculum-created,
nothing to scale, no coastline, no channel courses, no boundaries — is preserved in the
extended description, which prints on the page.

## Release record

`hhh/campaign-1/case-02-sumer/history/release-v0.1.json`

This is a first release. There is no prior approved release, no corrective reissue, and no
former generated artifact to recover.
