# Owner Approval — HHH Campaign 1 Core Case 04 · Karlsruhe · v0.1

**Case:** `HHH-C1-CASE04` — Karlsruhe
**Instructional type:** `CORE_CASE`
**Version:** 0.1 — first release
**Owner:** Nate / Owner
**Approval date:** 2026-08-15
**Approval status:** `APPROVED`
**Print status:** `PASS`

## Owner approval, verbatim

> “I approve Core Case 04. On-screen review passes and physical printing at 100% / Actual Size
> passes.”

## What was approved

The owner reviewed and approved the independently reviewed corrected candidate.

**Owner-approved printable baseline:**

```
29b34b31ab5b553093e134fcedb5a41b07b2c4f8
```

Every printable byte the owner saw on screen and printed on paper is the byte set at that
commit: `source/content.html`, `source/presentation.css` and `source/layout-overrides.json`.
Release conversion changed none of them.

## Accepted independent-review disposition

```
INDEPENDENT_CASE04_PARSER_NO_SHIFT_FINAL_PASS — READY_FOR_OWNER_GATE
```

## Review lineage

| Stage | Commit | Disposition |
|---|---|---|
| Production candidate | `1e7feb8ced4431cab6f91a3534ba368c705a4016` | corrections required — six blocking findings, four promoted observations |
| First correction pass | `d748b68616db52a62822dfdfb6352ee25fc07885` | corrections required — two remaining targets |
| Second correction pass | `20ebcc08b2120332e8876f172aae15fa263cc350` | corrections required — catalyst-guard escapes |
| Catalyst-guard correction | `0cec4eb94b48c5936bb1c612848886dbf8e028db` | `INDEPENDENT_CASE04_CATALYST_FINAL_REREVIEW_CORRECTIONS_REQUIRED` |
| Fail-closed convergence pass | `7e682a373311ae7991596d698c51a10fbc2139b6` | corrections required — two parser findings |
| Parser and no-shift correction | `29b34b31ab5b553093e134fcedb5a41b07b2c4f8` | `INDEPENDENT_CASE04_PARSER_NO_SHIFT_FINAL_PASS — READY_FOR_OWNER_GATE` |
| Owner gate | `29b34b31ab5b553093e134fcedb5a41b07b2c4f8` | `APPROVED` — this record |

Every review round after the first was bounded to the findings it was opened for. The whole
correction sequence changed **no** historical architecture, no task, no claim judgment, no page
count and no figure design. The last four rounds are entirely a story about the case's semantic
regression contract: they moved the catalyst guard from an open blacklist of wrong verbs to a
closed fail-closed contract in which any catalyst-and-ammonia sentence must resolve to an
approved function, a registered descriptive claim or a registered evaluative exemption. The
classroom bytes have been unchanged since `5fa9709f…`, the content hash carried by every
commit from `8d795af` onward.

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
| Print basis | Browser print dialog at **100% / Actual Size** |

The owner reviewed the case through the repository-local Curriculum Editor served from the Case
04 worktree at the approved commit.

## Roles and page counts approved

| Role | Pages |
|---|---|
| Student Mission | 8 |
| Teacher Guide | 7 |
| Answer Key | 6 |
| Accessible Mission | 14 |

35 printable pages in total. Grayscale is a presentation state on every role and was reviewed as
such; it is not a fifth role and creates no additional page-count category.

## Production basis

Production is HTML-only and package-source based. No canonical PDF artifact exists for this
case, PDF generation is not a release gate, and any PDF exported from the browser is
noncanonical and carries no accessibility guarantee. The approval above refers to the owner's
own physical print through the browser print dialog.
