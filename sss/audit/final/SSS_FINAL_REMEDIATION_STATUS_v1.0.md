# SSS Final Remediation — Validation Status

**Branch:** `remediate/sss-final-system`
**Baseline:** `f7a24423f802a095aa149f923d05475ba2837599` (curriculum), `29c3b222c53f51de11a3aa83e896a6d0ef6fb490` (game)
**Status:** ready for owner review. Not merged. All thirteen packages are corrective DRAFT candidates.
**Owner acceptances recorded:** Teacher page-count exceptions for SSS-C1-CASE01 (8 pages) and SSS-C2-CASE01 (9 pages), 2026-08-07.

This records what the automated validation covers, what it deliberately does not, and
which findings were dispositioned rather than changed. It supersedes any earlier
statement that full PDF validation gates this work.

---

## 1. PDF and print validation — OWNER-MANUAL-VALIDATION

**PDF/PRINT VALIDATION: OWNER-MANUAL-VALIDATION / explicitly outside automated
final-remediation scope by owner decision on 2026-08-07.**

Nate tests PDF export and physical printing manually. The `pdf-pr` CI job has been
removed from the pull-request gate. `apps/curriculum-editor/tests/run_pdf_tests.py` and
`apps/curriculum-editor/tests/pdf-harness.html` are retained and can be run on demand.

A PDF-specific failure is not a remediation blocker, and curriculum must not be altered
to satisfy a PDF-specific automated test.

Note that page-fit is still enforced: the browser harness asserts that no page's content
overflows its fixed Letter frame, in every role, in both colour and grayscale. That is a
DOM-geometry contract, independent of PDF rendering.

---

## 2. Automated validation — current results

| Gate | Result |
| --- | --- |
| Remediation pipeline idempotency (`git diff --exit-code`) | clean |
| `git diff --check` | clean |
| Final cross-edition quality contract (v3) | 0 failures, 10 manual-review flags |
| Final audit-specific accessibility contract (v2) | 0 failures |
| Corrective-candidate lifecycle contract | 0 failures |
| Corrective-release lifecycle unit tests | 25 tests, OK |
| Generic release integrity | PASS 40/40 |
| Corrective-aware canonical case structure | PASS |
| Layout overrides | PASS, 13 cases |
| **Curriculum-editor browser harness (Chromium)** | **PASS 2292/2292, 0 JavaScript errors** |
| Legacy static suite (CI diagnostic, continue-on-error) | 516/545 — see §4 |

The harness gained 13 assertions in the cleanup wave (load-announcement lifecycle neutrality), so the total moved 2279 -> 2292. Every assertion passes.

---

## 3. Defects found and repaired during final validation

The Chromium harness failed 2192/2279 when this phase began. Four distinct causes, three
of them real product defects introduced by the remediation itself:

**3.1 Stale harness roster fixture — validator defect.** The `canonicalCases` table still
recorded pre-remediation approved versions and `APPROVED_STABLE` status. 81 failures
across six per-case assertions. The fixture stays hand-maintained rather than derived from
the registry, so the version-parity assertions remain meaningful.

**3.2 Printable blocks inserted outside the content area — product defect.** The wave-1 and
wave-3 transformers appended the analytic rubric, controlled reference lists and the task
route with a helper that inserted "before the page footer". The publication footer is a
*sibling* of `.content-area` inside `.page-frame`, so nine Teacher pages across six cases
received printable material outside the content area. Because `.page-frame` is a column
flex container and `.content-area` is its `flex: 1 1 0` item, each misplaced block stole
height from the real content area until its text overlapped the misplaced block; the blocks
also escaped `checkOverflow()` entirely and were unreachable to the layout-override resize
system. The helper is fixed and `repair_misplaced_page_frame_blocks.py` relocated the nine
committed pages. The four baseline `div.student-id` page-frame siblings are deliberate
identity marks and were left untouched.

**3.3 Case 07 Task 4 status fields overlapping their stage responses — product defect.**
The wave-4 transformer added a persisted stage-status control per model stage, but Case 07
has no `.stage-status` rule, so the control stayed a plain inline span. An inline
non-replaced box ignores `min-height` and paints border and vertical padding outside its
line box, so every status field bled ~4px up over the stage response above it — six
overlapping printed fields per page, in both the Student and Accessible editions.

**3.4 Four over-full Teacher pages — product defect.** The remediation added the material
the Teacher Edition contract requires to Guides whose page allowance was already full:

| Case | Page | Available | Used |
| --- | --- | --- | --- |
| SSS-C1-CASE01 | teacher-3 | 884 | 1363 |
| SSS-C1-CASE02 | teacher-07 | 884 | 1122 |
| SSS-C2-CASE01 | teacher-guide-09 | 936 | 993 |
| SSS-C2-CASE06 | teacher-guide-08 | 936 | 1245 |

Content past a fixed frame is clipped in print. Finding `C2C6-SYS01` settles which side
gives way — a Teacher package is validated on "the common functional set … rather than
merely a fixed page count" — so every block was preserved and each Guide gained one page.
Split points were measured in Chromium and all fall on section headings, so no block is
separated from its heading and no table or list breaks across a seam.

That first pass gave each Guide one extra page (C1-01 7→8, C1-02 7→8, C2-01 9→10,
C2-06 8→9). It has since been superseded by the reflow in section 5, which balances
content across each whole edition instead; see section 5.1 for the final counts.

**3.5 Case 05 location subtitle.** The browser harness and the static suite both still
expected `Europa, orbiting Jupiter`. Audit finding `C1C5-ID01` replaced it with the approved
`Europa, Sub-Surface Bunker`. The content was correct; both expectations were stale.

---

## 4. Explicitly dispositioned, not changed

**4.1 Legacy static suite — 29 release-pinned failures.** The suite is a
`continue-on-error` CI diagnostic. It previously crashed with
`KeyError: 'releaseHistory'` before emitting any assertion; its stale expectations were
corrected so it now runs and reports 516/545. Every remaining failure is one class:

- frozen Student/Teacher/Answer DOM baselines pinned to the approved releases (13),
- completed-release-lifecycle records in task registries (3),
- the non-corrective `validate_canonical_case_structure.py`, superseded by the
  corrective-aware validator that CI gates on (1),
- per-case scoped validators and mutation suites whose baselines assert the approved v1.1
  release state (12).

These are **deliberately left failing.** They exist to detect drift against the approved
release, and the remediation intentionally changed that DOM and reopened those packages as
DRAFT candidates. Re-pinning them now would erase the protection. They are re-pinned when
the owner approves this candidate as a release — that is a release step, not a remediation
step. Every substantive science, standards, clue, figure and prohibited-claim assertion
inside those case-scoped validators passes.

**4.2 Case 07 keeps its own rubric heading.** Case 07 is excluded from `RUBRIC_TARGETS`
because the audit records that it already ships a complete four-level analytic rubric under
"Formal grading dimensions" with `4 · Integrated / 3 · Sound / 2 · Partial / 1 · Beginning`
columns, and calls this "a template-normalization issue, not a missing-rubric defect."

**4.3 Ten accessible-workload manual-review flags.** The quality contract raises these for
owner judgement rather than failing; they are unchanged by this phase.

**4.4 Case 03 reports CHANGE on every remediation run.** Pre-existing cosmetic reporting
quirk. The transformer writes byte-identical output, so the idempotency gate is unaffected.

---

## 5. Final cleanup wave (2026-08-07)

**5.1 Teacher editions reflowed toward the common seven-page architecture.** The first
pass had simply given each over-full Guide one more page. Content is now reflowed across
the whole edition with balanced page loads. Nothing was cut; every block is preserved in
document order and only the page breaks moved.

Teacher blocks are atomic and their order is instructional, so the minimum page count is
an exact quantity. Measured in Chromium with an exact dynamic-programming page-break
search over real rendered block heights:

| Case | Movable blocks | Exact minimum | Outcome |
| --- | --- | --- | --- |
| SSS-C1-CASE02 | 37 | 7 | **7 pages**, worst page 82.4% full |
| SSS-C2-CASE06 | 60 | 6 | **7 pages**, worst page 76.1% full |
| SSS-C2-CASE01 | 68 | 8 | **9 pages** — cannot reach seven |
| SSS-C1-CASE01 | 51 | 8 | **8 pages, untouched** — cannot reach seven |

**5.2 Load announcements are lifecycle-neutral.** Campaign 1 Cases 04–07 announced an
"approved package loaded" while reopened as corrective DRAFT candidates. Now "curriculum
package loaded". The browser harness asserts this for all thirteen cases rather than
leaving it to convention.

**5.3 Grayscale gaps carried to the visual backlog.** The recorded token/fill gaps in
Campaign 1 Cases 01, 02 and 06 are **not** remediated here, by owner decision. They are
classified `DEFERRED-VISUAL` in the register and belong to the visual-modernisation
branch. They remain asserted exactly in the browser harness, so they cannot grow or
spread to another case in the meantime.

---

## 6. The two seven-page conflicts — OWNER-ACCEPTED PAGE-COUNT EXCEPTIONS

> **OWNER DECISION, 2026-08-07 — ACCEPTED AS FINAL.**
> **SSS-C1-CASE01 — ISS Greenhouse: 8 Teacher pages accepted.**
> **SSS-C2-CASE01 — Heavy Hands: 9 Teacher pages accepted.**
>
> Approved exceptions to the nominal seven-page Teacher target, because the rendered-height
> analysis below demonstrated that reducing them further would require deleting required
> Teacher content or creating fragile/overfilled layouts. Functional compliance with the
> Teacher Edition contract takes precedence over fixed page-count uniformity.
>
> Both page-count questions are **closed** — not open, not deferred. `C2C1-T01` is
> VALIDATED / OWNER-ACCEPTED-EXCEPTION; Campaign 1 Case 01 has no page-count finding of its
> own, so its exception is recorded at document level. **Neither edition's content or page
> geometry is to be altered further on this basis.** See register section 13.4.

The measured evidence the owner accepted:

Both are the same shape: the Teacher Edition contract requires more content than seven
pages can physically hold, given that tables, lists and callouts cannot be split across a
page break and the block order is instructional.

**SSS-C1-CASE01 — exact minimum 8 pages, currently 8.**
The case was 7 pages before remediation. Audit finding `C1C1-T01` (and governing decision
1, "Case 01 ... corrected for its identified Task 5 omission") required adding the missing
Task 5 procedure step, which renders as a single 493px atomic teacher-note block. Seven
pages hold 6188px of content; the edition now needs 6494px. It is over by 306px — more
than a third of a page — so no arrangement of page breaks fits it into seven. Every
possible eight-page split additionally leaves a page ~99.9% full, so the case is left
exactly as it is rather than re-cut into a tighter fit than it already holds.

*Reaching seven would have required deleting the Task 5 procedure step the audit
required, or a global Teacher density reduction. The owner accepted 8 pages instead on
2026-08-07; this is closed.*

**SSS-C2-CASE01 — exact minimum 8 pages, set to 9.**
Nine pages before remediation. It gained the four-level analytic rubric (`C2C1-T03`), the
declared 105-minute route (`C2C1-T04`) and the science-source ledger. Eight pages is
physically the minimum but leaves the worst page 99.7% full — about three pixels of
slack. A page tuned that tightly on macOS has already been shown in this branch to clip on
the Linux CI runner, where font metrics run taller. Nine pages leaves the worst page 86.5%
full and restores the pre-remediation count.

*Reaching seven would have required removing roughly two pages of required Teacher
function — rubric, route, or source ledger. The owner accepted 9 pages instead on
2026-08-07; this is closed.*

---

## 7. Needs an owner decision

- ~~Accept the two seven-page conflicts and their page counts.~~ **DONE — accepted as
  final by the owner on 2026-08-07 (section 6, register 13.4).** The other eleven cases are
  unchanged this wave; three of thirteen sit at seven pages.
- **PDF and print testing** is yours. Nothing automated covers it. The reflowed Teacher
  Guides (C1-02, C2-01, C2-06) and Case 07's Accessible page 4 are where geometry changed.
- **Approve the candidate for release**, which is what closes the 29
  `RELEASE-BASELINE-PENDING` assertions; they are re-pinned at that point, not before.

## 8. Out of scope, by decision

- 35 `VIS` findings and the grayscale token/fill gaps — `DEFERRED-VISUAL`, next branch.
- PDF/print — `OWNER-MANUAL`.
- Frozen-release static assertions — `RELEASE-BASELINE-PENDING`.
