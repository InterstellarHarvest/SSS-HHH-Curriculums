# Owner Approval — HHH Campaign 1 Core Case 03 · County Cork · v0.1

**Case:** `HHH-C1-CASE03` — County Cork
**Instructional type:** `CORE_CASE`
**Version:** 0.1 — first release
**Owner:** Nate / Owner
**Approval date:** 2026-08-14
**Approval status:** `APPROVED`
**Print status:** `PASS`

## Owner approval, verbatim

> “I approve Core Case 03. On-screen review passes and physical printing at 100% / Actual Size
> passes.”

## What was approved

The owner reviewed and approved the independently reviewed corrected candidate.

**Owner-approved printable baseline:**

```
384bd5790bcc760b6b692c4a872451073e1c0dbb
```

Every printable byte the owner saw on screen and printed on paper is the byte set at that
commit: `source/content.html`, `source/presentation.css` and `source/layout-overrides.json`.
Release conversion changed none of them.

## Review lineage

| Stage | Commit | Disposition |
|---|---|---|
| Production candidate | `59780c898ff926bb9047d9740ebb8b85f125db63` | `INDEPENDENT_CASE03_REVIEW_CORRECTIONS_REQUIRED` |
| Corrected candidate | `384bd5790bcc760b6b692c4a872451073e1c0dbb` | `INDEPENDENT_CASE03_REVIEW_PASS — READY_FOR_OWNER_GATE` |
| Owner gate | `384bd5790bcc760b6b692c4a872451073e1c0dbb` | `APPROVED` — this record |

The bounded correction pass between those two commits carried four blocking findings (a wrong
Bourke DOI, a superseded article title, an Accessible scaffold that disclosed a keyed claim, and
a regression guard that protected literal phrases rather than the concept) and six promoted
observations. It changed no historical architecture, no task, no mark, no page count and no
figure design.

**No post-review art-direction commits exist.** Nothing was changed between the close of
independent review and this approval. The commit the independent reviewer passed and the commit
the owner approved and printed are the same commit, so the owner's print approval covers exactly
the reviewed byte set. Case 02's post-gate art-direction disclosure does not apply here and is
deliberately not reproduced.

## Verification performed by the owner

| Check | Result |
|---|---|
| On-screen review, all four roles | **PASS** |
| Physical print | **PASS** |
| Print basis | Browser print dialog at **100% / Actual Size**, US Letter portrait |

## Roles and page counts approved

| Role | Pages |
|---|---|
| Student Mission | 8 |
| Teacher Guide | 7 |
| Answer Key | 6 |
| Accessible Mission | 13 |

34 printable pages in total. Grayscale is a presentation state on every role and was reviewed as
such; it is not a fifth role and creates no additional page-count category.

## Production basis

Production is HTML-only and package-source based. No canonical PDF artifact exists for this
case, PDF generation is not a release gate, and any PDF exported from the browser is
noncanonical and carries no accessibility guarantee. The approval above refers to the owner's
own physical print through the browser print dialog.
