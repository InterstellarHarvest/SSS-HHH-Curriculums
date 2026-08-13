# Owner Approval — HHH Campaign 1 · Core Case 01 · The Fertile Crescent · v0.1

**Curriculum:** Hunger, Harvest, & History (HHH)
**Campaign:** Campaign 1
**Unit:** The Fertile Crescent — `HHH-C1-CASE01` · instructional type `CORE_CASE`
**Version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-13

## Decision

**Release status:** `APPROVED_STABLE`
**Review status:** `OWNER_REVIEW_PASS`

Owner statement of record:

> "I approve Core Case 01. The owner clarity corrections pass, on-screen review passes, and
> physical printing at 100% / Actual Size passes."

## What the owner reviewed

| Check | Result |
|---|---|
| Owner clarity corrections | **PASS** |
| On-screen review | **PASS** |
| Physical print | **PASS** |
| Physical print basis | Browser print dialog at 100% / Actual Size |

All four roles were approved: **Student Mission**, **Teacher Guide**, **Answer Key** and
**Accessible Mission**.

**Tested owner-approved content baseline:** `8683277d3654eeea492be28daa85a6632499e431`

That commit carries the exact printable byte set the owner reviewed on screen and printed on
paper. Release conversion did not alter it: `content.html`, `presentation.css` and
`layout-overrides.json` are byte-identical to that commit, and the only source that moved is
`task-registry.js`, which carries the lifecycle stamp and renders nothing. The Student,
Teacher, Answer Key and Accessible pages the owner approved are the pages this release
publishes, so no repeat print was required.

## Released role page counts

| Role | Pages |
|---|---|
| Student Mission | 7 |
| Teacher Guide | 7 |
| Answer Key | 4 |
| Accessible Mission | 9 |

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
`3364fe9a0dbd545703f1ba1959dabc8f1e118da2`:

1. full review — `INDEPENDENT_CASE01_REVIEW_CORRECTIONS_REQUIRED` (four required corrections:
   chronology containment, Accessible source-status scope, README page-count drift, and the
   9,844 / 804 evidence overstatement);
2. bounded re-review — `INDEPENDENT_CASE01_BOUNDED_REREVIEW_CORRECTIONS_REQUIRED` (two required
   corrections: chronology rail framing, and a defeatable evidence-count regression guard);
3. micro-rereview — `INDEPENDENT_CASE01_MICRO_REREVIEW_PASS — READY_FOR_OWNER_GATE`.

An owner clarity pass followed the gate at the owner's direction, replacing the Task 3 rail
with a plotted timeline, removing "rail" from learner-facing wording, and simplifying the
Task 3 explanation and question. That pass changed presentation only; the certified
chronology, sources and evidence claims were unchanged.

## Release record

`hhh/campaign-1/case-01-fertile-crescent/history/release-v0.1.json`

This is a first release. There is no prior approved release, no corrective reissue, and no
former generated artifact to recover.
