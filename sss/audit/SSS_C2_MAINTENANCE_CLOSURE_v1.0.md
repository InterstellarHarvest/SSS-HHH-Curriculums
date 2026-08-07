# SSS Campaign 2 — Maintenance and Closure Record v1.0

**Date:** 2026-08-06
**Type:** Repository maintenance and baseline certification. **Not a curriculum audit.**

---

## 1. Scope

This pass makes the Campaign 2 baseline clean, synchronized, documented and mechanically
certified. All six packages were already remediated, owner-reviewed, print-approved,
corrected where required, and integrated before it began.

**In scope**

- Preflight verification of both repositories against their expected synchronized SHAs.
- Mechanical integrity verification of the six current approved releases.
- Repair of the shared-validator defects recorded in §§12–13 of
  `SSS_C2_CAMPAIGN_COMPLETION_AUDIT_v1.0.md`.
- A shared release-integrity check covering release → pinned commit → certified source blobs.
- Retirement of the orphaned repository-cleanup audit validator.
- Synchronization of current-state documentation.
- One exact final-tip run of the complete validation estate.

**Explicitly out of scope — no such review was performed**

Curriculum quality, Accessible differentiation, Teacher Edition quality, Answer Key
pedagogy, standards quality, visual design, and cross-case consistency. Those belong to the
later unified SSS Campaign 1 + Campaign 2 post-finalization audit. **This record does not
claim that audit has passed.** The blocker and thirty-four major defects recorded in
`SSS_C2_CAMPAIGN_COMPLETION_AUDIT_v1.0.md` §14 were remediated in the per-case remediation
cycles that preceded this pass; their evidence is in each package's release records, and
this record does not restate it.

No approved package content was altered in this pass. One release record was corrected,
because the release it certified was mechanically invalid — see §3.

---

## 2. Baseline

| | |
|---|---|
| Curriculum repository | `InterstellarHarvest/SSS-HHH-Curriculums` |
| Starting curriculum SHA | `81eef7067268865fec368f50db2d363e0354ae1a` |
| Final curriculum SHA | *(the integrated maintenance tip; see §11)* |
| Game repository | `InterstellarHarvest/Space-Sprout-Sleuth` |
| Game SHA | `29c3b222c53f51de11a3aa83e896a6d0ef6fb490` |
| Maintenance branch | `maintenance/sss-c2-finalization` (local only) |
| Maintenance worktree | `/private/tmp/sss-c2-finalization` |

Local `main`, `origin/main` and the live remote `main` were verified equal to the expected
SHA in both repositories before any change was made, and both primary worktrees were clean.

---

## 3. Six-case final inventory

All six are `APPROVED_STABLE`, owner-approved, and print-approved `PASS at 100% / Actual
Size`. Each is a corrective v1.1 reissue of an approved v1.0; both records are retained in
each package, and the v1.0 records are unmodified since the commit that wrote them.

| Case | Title | Version | Student | Teacher | Answer Key | Accessible | Release commit |
|---:|---|---:|---:|---:|---:|---:|---|
| 01 | Heavy Hands | 1.1 | 5 | 9 | 4 | 8 | `8ab60f3a` |
| 02 | The Missing Dance | 1.1 | 6 | 8 | 4 | 8 | `43858eaa` |
| 03 | The Wrong Color of Light | 1.1 | 5 | 8 | 4 | 8 | `2d4a62ea` |
| 04 | The Silent Grove | 1.1 | 6 | 8 | 4 | 8 | `3fe64b9c` |
| 05 | Too Clean a Room | 1.1 | 7 | 9 | 5 | 7 | `7c69585e` |
| 06 | The First Garden | 1.1 | 6 | 8 | 5 | 7 | `f3e3ed7f` |

**Totals:** Student 35, Teacher 50, Answer Key 26, Accessible 46 — 157 pages.

### Source certification: PASS, after one repair

**One release blocker was found and fixed.** Campaign 2 Case 02's v1.1 record pinned
`canonicalSourceApprovalCommit` to `a3b78819`, its last candidate commit. That commit does
not contain the task registry the record certifies: it holds `8f5595c9…` where the record
certifies `061473c6…`. The registry received its lifecycle promotion in the release commit
`43858eaa` itself, one commit later. The pin therefore certified source that did not exist
at the commit named.

This is the fifth instance of one defect class, after Cases 01, 02 and 04 at v1.0 and Case
05 at v1.1. Every validator missed all five for the same reason: they compared the record
to the package and never the record to the commit.

Fixed by repinning to `43858eaadd…`, the commit that contains the certified blobs, matching
what the other five cases do and the repair already applied to Case 05 in `81eef70`.
`formerArtifactRecoveryCommit` moved with it and the release commit joined
`correctiveReviewCommits`. **No package content changed; no re-print is implicated.**

With that repair, all four source blobs of all six current releases hash to exactly what
their records certify, both on disk and at their pinned commits.

### Frozen baselines: PASS

Every current release freezes Student, Teacher and Answer Key DOM baselines, and all match
the rendered markup. Case 05's Student baseline is deliberately identical to its v1.0
baseline because no v1.1 correction touched the Student edition; a corrective release is
not required to change every role's markup, and the checks were written so it need not.

### Retained prior releases: PASS

Each of the six retained `release-v1.0.json` records has been touched by exactly one commit
— the one that wrote it. Each is accompanied by its `CASE0N_OWNER_APPROVAL_v1.0.md`, and
each is indexed inside the v1.1 record with hashes, baselines and page counts that match the
retained record verbatim.

### Tracked artifacts: PASS

No PDF, screenshot, generated role document, `.pyc` or `__pycache__` is tracked.

---

## 4. Shared-validator repairs

### A. Campaign 1 Case 07 had no resize coverage — fixed

`browser-harness.html` listed 12 of 13 cases in `accessibleEligibleCounts` and
`studentEligibleCounts`. The loop iterates the maps, so `SSS-C1-CASE07` — a released case —
received zero resize-eligibility, layout-panel and invalid-default coverage. Both maps now
carry its audited values, Accessible 23 and Student 11, derived from its
`layout-overrides.json` and corroborated by `STUDENT_LAYOUT_COUNTS` in `validate_static.py`.

Two assertions now require both maps to name **exactly** the roster in
`case-registry.v2.json`, fetched at run time. A case cannot be silently omitted again.

### B. Grayscale coverage was 7 of 13, with one unreachable check — fixed

The grayscale palette roster excluded six cases, including the three newest approved
Campaign 2 cases, which had no grayscale palette assertion at all. A second, disagreeing
roster guarded the SAA-insignia assertion, making it dead code for `SSS-C1-CASE06`.

Both rosters are gone. Grayscale palette, rendered-fill and SAA-insignia assertions now run
for every registered case in every role. No approved artwork was altered to satisfy them;
two real Campaign 1 gaps surfaced instead and are recorded exactly — see §8.

### C. Structural validation was Campaign 1 only — fixed

`validate_canonical_case_structure.py` hard-coded `sss/campaign-1` and a seven-case roster,
and reported `"cases": 7` against a thirteen-case registry. Campaign 2 was structurally
covered only because each `validate_caseNN_campaign2.py` re-implemented it by hand; a
fourteenth case would have received none.

It now derives its roster from `case-registry.v2.json` and cross-checks it against the
filesystem in both directions, so a registered case without a directory and a directory
without a registry entry both fail. Cases are keyed `campaign-N/case-NN`, which resolves the
`campaign-1/case-01` ↔ `campaign-2/case-01` collision. Corrective releases are handled
through `corrective_release_lifecycle`, so retained superseded records are correct rather
than a violation. It reports `"cases": 13` across both campaigns.

Campaign 1's historical exceptions are preserved verbatim: its exact commit pins, its two
pre-canonical prior-release indexes, its per-case native no-artifact recovery wording, and
the `roleHtmlAvailability` assertion, now scoped to `campaign-1/case-01` alone. The three
oldest Campaign 1 releases keep their inline owner approval; every later release must carry
a standalone owner-approval record for its own version and for each retained version.

Verified by negative test: breaking a Campaign 2 corrective prior index, unregistering a
Campaign 2 case, and deleting a Campaign 2 owner-approval record each produce a named failure.

### D. Stale wording — fixed

`validate_static.py` described the registry as "the approved Campaign 1 cases plus the
unreleased Campaign 2 case". `browser-harness.html` routed Campaign 2 Cases 04–06 — the
three newest approved cases in the repository — down a branch labelled "legacy protected
components". Both corrected. The geometry branch is now split on whether a case predates
shared printable-v1.1 rather than on a hand-kept list, which moved Campaign 2 Cases 04–06
onto the strict branch, where they pass.

### E. PDF workflow documentation — fixed

`run_pdf_tests.py` is now named in the root README validation workflow and in
`CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md`. Browser and PDF remain manual Chrome-dependent
suites, and that is now stated rather than implied by omission.

---

## 5. Shared release-integrity protection

New: `shared/validation/validate_release_integrity.py`, chained into `validate_static.py`.

It derives its roster from the canonical registry and, for every approved release, checks
lifecycle, registry/package/record identity agreement, owner approval, print `PASS`,
accepted-validation `PASS`, the standalone owner-approval record, fixed-role page counts,
well-formed digests, and a `canonicalSourceApprovalCommit` that resolves. For releases
written under the current contract it additionally proves that **every certified source blob
exists at the pinned commit with exactly the certified hash** — the check whose absence let
five false pins ship — and that a corrective release's retained prior records are
unmodified, correctly indexed, and genuinely superseded by changed source.

**Two record formats, stated rather than hidden.** Campaign 1's releases predate this
contract: they carry no frozen DOM baselines, omit `layoutOverrides` from `sourceHashes`,
and for Cases 01–03 certify source at `master/` and `published/` paths the canonical
migration retired. Rewriting them would destroy the evidence of what was approved. They are
therefore exempt from blob-level certification, the exemption is **asserted to be confined
to Campaign 1**, and the exempt cases are **printed by name on every run**. Any case in any
later campaign must carry a contract-format release. The exemption can only shrink, and it
disappears when Campaign 1 is reissued.

Current result: `PASS 390/390` across 13 cases; 6 fully certified against their pinned
commits; 7 named as legacy-format.

**Deferred as agreed:** the cross-role table/figure reference resolver. Generalizing it from
the existing per-case checks is not the small deterministic change that would justify
including it here. It belongs to the later validation work.

---

## 6. Cleanup-audit retirement

`shared/validation/validate_repository_cleanup_audit.py` is deleted. The record is
`shared/validation/RETIRED_VALIDATORS.md`.

It was a baseline-anchored no-change control for a cleanup *proposal* that authorized no
deletions. It crashed on missing inputs; the deletions were owner-authorized by the
canonical case-structure migration, which names this exact workflow in its
`validatorRetirement` and supersedes the conservative proposal that had listed the inputs as
RETAIN. **Its missing inputs are intentional and were not restored.** It could not pass even
if they were: it requires 477 tracked files against 244, requires that no baseline file was
moved or deleted against a migration that moved 377 paths, and requires Campaign 2 Case 04
to be `NOT_STARTED` against a released v1.1. Nothing executed it and it was in no validation
contract.

The retirement record states its former purpose, the retirement reason, why the missing
inputs are intentional, that it was never a release gate, what now answers its one live
question, and the `git show` command that recovers it. The two surviving references are
inside frozen baseline-anchored audit snapshots and are deliberately not edited.

The repository no longer presents an active validator that simply crashes.

---

## 7. Documentation synchronization

Corrected to current state, with counts derived from the repository:

- `README.md` — Campaign 2 recorded as complete with the six-case version and page-count
  table; validation workflow now includes `validate_release_integrity.py` and
  `run_pdf_tests.py`; retirement record linked.
- `apps/curriculum-editor/README.md` — "seven released Campaign 1 cases" and "Campaign 2
  production remains unstarted" replaced with the thirteen released cases across two
  campaigns.
- `shared/project-management/CURRENT_PROJECT_STATE.md` — release table completed with all
  six Campaign 2 cases and their v1.1 page counts; "the remaining Campaign 2 cases are
  unproduced" removed; the six accepted v1.1 release commits recorded; baseline SHA and date
  updated; next-phase section points at the outstanding whole-SSS audit.
- `CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md` and
  `REPOSITORY_CURRICULUM_LIBRARY_ARCHITECTURE.md` — "all 40 case/role/presentation states"
  corrected to the registry-derived 104 across thirteen cases; release-integrity and PDF
  validators documented.

Immutable historical v1.0 records, frozen approval records, and the baseline-anchored
cleanup snapshots were not rewritten.

**`location` field convention, documented not normalized.** Campaign 2 Cases 01–05 record
the runtime *investigation* name; Case 06 records the runtime *location*. Each case validator
encodes its own reading, both pass, and no active contract depends on the distinction. It is
now written down in `CURRENT_PROJECT_STATE.md`. The packages were not touched for
consistency alone.

---

## 8. Remaining known issues

### 8a. Actual unresolved repository defects

1. **Campaign 1 Case 01 does not neutralize its callout fills under grayscale**, in all four
   roles. `callout callout-neutral`, `callout callout-success` and `callout callout-neutral
   optional-extension` render tinted backgrounds with grayscale on. This is a real defect in
   an approved package and would print as tint on a grayscale run. It was invisible while
   the grayscale roster covered 7 of 13. It is recorded exactly in the harness, so it cannot
   grow or spread, and is carried to the whole-SSS audit — correcting approved Campaign 1
   presentation is that audit's work, not a Campaign 2 maintenance pass's.
2. **Campaign 1 Cases 01, 02 and 06 leave declared palette tokens tinted under grayscale.**
   Their rendered surfaces are neutral (Case 01 excepted, per above) and their insignia are
   neutralized, so the practical impact is smaller than item 1, but the token state is not
   what the contract intends. Recorded exactly, same disposition.

Both are asserted as *exact* recorded state, not suppressed: any change in either direction,
for any case, fails the suite.

### 8b. Frozen historical inaccuracies, deliberately preserved

1. Campaign 1's seven release records are legacy-format — no frozen DOM baselines, no
   `layoutOverrides` in `sourceHashes`. Cases 01–03 additionally certify hashes and pins for
   `master/` and `published/` source the canonical migration retired, so those records cannot
   be blob-certified against this tree.
2. Campaign 2's six retained v1.0 records carry the stale accepted-validation figures and,
   for Cases 01, 02 and 04, the false `canonicalSourceApprovalCommit` pins that the
   completion audit found. They are retained byte-identical by design; the v1.1 records
   carry the corrected pins and the true figures.
3. The frozen cleanup snapshots still list the retired cleanup validator as an addition.
4. Campaign 1 Case 04's release record freezes an Accessible page count of 6 against the
   package's current 7. Accessible pagination is content-driven and the fixed roles agree,
   which is why the check is scoped to the three fixed roles.

### 8c. Quality questions deferred to the whole-SSS audit

Curriculum quality, Accessible differentiation, Teacher Edition quality, Answer Key
pedagogy, standards quality, visual design, and cross-case consistency across both
campaigns. Also deferred, from the completion audit's own follow-up recommendations: the
cross-role reference resolver and the revision-propagation check. **No such review was
performed in this pass.**

---

## 9. Final-tip validation

Run once, at the exact tree committed for integration.

| Suite | Result |
|---|---|
| Canonical case structure | PASS, 13 cases across `campaign-1` and `campaign-2`; 61 commit references, 25 artifact hashes, 8 prior-release entries |
| Release integrity | PASS 390/390; 6 fully certified against their pinned commits, 7 legacy-format named |
| Layout overrides | PASS, 13 cases; Accessible 201 eligible / 274 locked, Student 118 eligible / 365 locked |
| Campaign 2 case validators | Case 01 135/135, Case 02 108/108, Case 03 107/107, Case 04 139/139, Case 05 165/165, Case 06 230/230 |
| Campaign 2 mutation suites (6) | PASS, chained through full static |
| Corrective-release lifecycle | PASS 25/25 |
| Authoring service | PASS 13/13 |
| Full static | PASS 601/601 |
| Full browser | PASS 2280/2280 across all 104 case/role/presentation states, 0 JavaScript errors |
| Full PDF | PASS 316/316 on the registry-derived roster |
| `git diff --check` | clean |

Static rose from 600 to 601: the release-integrity validator joined the chain.

All registered cases load, all roles render, every page fits, grayscale coverage executes
for all thirteen cases, PDF generation completes, source certifications pass, frozen
baselines pass, no generated artifact is tracked, and validation leaves the worktree clean.

Browser rose from 2161 to 2280 assertions: Campaign 1 Case 07 joined resize coverage, and
grayscale palette, rendered-fill and insignia coverage widened from 7 cases to 13.

---

## 10. Disposition

**CAMPAIGN_2_MAINTENANCE_CLOSED**

**CAMPAIGN_2_BASELINE_FROZEN**

Six approved package releases; honest shared-validator coverage; valid current source
certification; valid current frozen baselines; obsolete cleanup machinery retired;
synchronized current documentation; complete final-tip regression PASS; clean synchronized
Git state.

This closes Campaign 2 as a *baseline*. It does not close it as *quality*, and it makes no
claim about the unified SSS Campaign 1 + Campaign 2 post-finalization audit, which has not
been performed.
