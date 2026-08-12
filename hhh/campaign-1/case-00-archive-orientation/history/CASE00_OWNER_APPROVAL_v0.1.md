# Owner Approval — HHH Campaign 1 · Archive Orientation · v0.1

**Curriculum:** Hunger, Harvest, & History (HHH)
**Campaign:** Campaign 1
**Unit:** Archive Orientation — `HHH-C1-CASE00` · instructional type `ORIENTATION`
**Version:** 0.1
**Owner:** Nate / Owner
**Approval date:** 2026-08-12

## Decision

**Release status:** `APPROVED_STABLE`
**Review status:** `OWNER_REVIEW_PASS`

Owner statement of record:

> "I approve Archive Orientation. On-screen review passes and physical printing at 100% / Actual Size passes."

## What the owner reviewed

| Check | Result |
|---|---|
| On-screen review | **PASS** |
| Physical print | **PASS** |
| Physical print basis | Browser print dialog at 100% / Actual Size |

**Tested owner-approved content baseline:** `05f2b5353b8779d9c5769172d94cd10e9049180f`

That commit carries the exact printable byte set the owner reviewed on screen and printed
on paper. Release conversion did not alter it: `content.html`, `presentation.css` and
`layout-overrides.json` are byte-identical to that commit, and the only source that moved
is `task-registry.js`, which carries the lifecycle stamp and renders nothing. The Student,
Teacher, Answer Key and Accessible pages the owner approved are the pages this release
publishes, so no repeat print was required.

## Released role page counts

| Role | Pages |
|---|---|
| Student Mission | 4 |
| Teacher Guide | 7 |
| Answer Key | 3 |
| Accessible Mission | 5 |

## Production policy at approval

- HTML-only canonical production; the registered package source is the release.
- No canonical project PDF artifact and no PDF release gate. A PDF exported from the
  browser is noncanonical and carries no accessibility guarantee.
- No generated role HTML, PDF or screenshot is committed.

## Scope of this approval

This record captures the owner's instructional, visual and physical-print approval.
It does not represent the owner as having personally executed the repository's automated
validation suites; those were run by the implementation and independent-review process and
are recorded in `release-v0.1.json` under `acceptedValidation`.

## Independent review preceding this approval

The package was independently reviewed three times against main baseline
`37be8e16b18be5789ceac13adcdf3dda6eb8ee25`:

1. full review — `INDEPENDENT_REVIEW_CORRECTIONS_REQUIRED` (six required corrections);
2. bounded re-review — `INDEPENDENT_REREVIEW_CORRECTIONS_REQUIRED` (one required correction);
3. final bounded verification — `INDEPENDENT_REREVIEW_PASS — READY_FOR_OWNER_GATE`.

Owner gate followed that pass and is recorded here.

## Release record

`hhh/campaign-1/case-00-archive-orientation/history/release-v0.1.json`

This is a first release. There is no prior approved release, no corrective reissue, and no
former generated artifact to recover.
