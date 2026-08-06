# SSS Campaign 2 Completion Audit v1.0

**Disposition: Campaign 2 is NOT ready for formal completion.** One blocker and a substantial body of major
defects were found inside approved, released packages. No approved package was modified by this audit, and no
campaign-level maintenance was performed, because the remediation gate did not pass.

## 1. Authority baseline

| Item | Value |
|---|---|
| Curriculum repository | `InterstellarHarvest/SSS-HHH-Curriculums` |
| Curriculum `main` (local, `origin/main`, live remote) | `bebd935854536a46ff632cec791f95b2c941d087` |
| Game repository (read-only) | `InterstellarHarvest/Space-Sprout-Sleuth` |
| Game `main` (local, `origin/main`, live remote) | `29c3b222c53f51de11a3aa83e896a6d0ef6fb490` |
| Audit branch | `audit/sss-c2-campaign-completion` |
| Audit worktree | `/private/tmp/sss-c2-campaign-completion` |
| Retained Case 07 audit worktree | `/private/tmp/sss-case07-curriculum-audit` @ `76a9084`, clean, untouched |

All five game worktrees clean. Primary curriculum worktree clean. No generated PDF, screenshot, or role document
is tracked anywhere in the repository; the only tracked HTML under `sss/` is `content.html`.

### Preflight observations (not defects)

- **Campaign 1 Cases 01–03 carry no owner-approval record**, and Cases 01 and 03 are v1.1. This is correct frozen
  history: `validate_canonical_case_structure.py:221-226` expects approval records only for Campaign 1 Cases
  04–07. Campaign 1 predates the convention and must not be revised.
- **Case 03 pins an older game baseline** (`46b9387bca95736f164f905596e3dd8b13968661`) than its five siblings.
  Verified substantively accurate: `campaign_2_data.js` and `docs/campaign_2_science_sources.md` are
  byte-identical between that commit and `29c3b222`. The only delta is `index.html` (a tooltip scaling change).
  The pin is a provenance inconsistency, not an evidence inconsistency.

## 2. Six-case release inventory

All six are v1.0, `APPROVED_STABLE`, package status `APPROVED`, print `PASS`, each backed by exactly
`history/release-v1.0.json` + `history/CASE0N_OWNER_APPROVAL_v1.0.md`, each protected by a frozen Student,
Teacher and Answer Key DOM baseline that matches current markup.

| Case | ID | Title | Runtime | Student | Teacher | Answer | Accessible |
|---|---|---|---|---:|---:|---:|---:|
| 01 | `SSS-C2-CASE01` | Heavy Hands | `heavy_hands` | 5 | 8 | 4 | 8 |
| 02 | `SSS-C2-CASE02` | The Missing Dance | `missing_dance` | 5 | 8 | 4 | 8 |
| 03 | `SSS-C2-CASE03` | The Wrong Color of Light | `wrong_color_light` | 5 | 8 | 4 | 8 |
| 04 | `SSS-C2-CASE04` | The Silent Grove | `silent_grove` | 6 | 8 | 4 | 8 |
| 05 | `SSS-C2-CASE05` | Too Clean a Room | `too_clean_room` | 7 | 9 | 5 | 7 |
| 06 | `SSS-C2-CASE06` | The First Garden | `first_garden` | 5 | 8 | 5 | 7 |

Page counts verified to agree across **five independent authorities** for every case: rendered DOM, package
`rolePageStructure`, task-registry `roles`, release-record `rolePageCounts`, and the package README.

## 3. Per-case audit matrix

Legend: OK = no finding. Severity of the worst finding in that dimension is shown otherwise.

| Case | A identity/evidence | B cross-role parity | C answers | D teacher | E accessible | F standards | G visual/print | H release |
|---|---|---|---|---|---|---|---|---|
| 01 | **MAJOR** | **MAJOR** | **MAJOR** | **MAJOR** | MINOR | **MAJOR** | OK | **MAJOR** |
| 02 | MINOR | **BLOCKER** | **MAJOR** | **MAJOR** | **MAJOR** | **MAJOR** | OK | **MAJOR** |
| 03 | MINOR | **MAJOR** | MINOR | MINOR | OK | **MAJOR** | OK | DOC |
| 04 | MINOR | **MAJOR** | **MAJOR** | OK | **MAJOR** | **MAJOR** | OK | MINOR |
| 05 | MINOR | OK | MINOR | **MAJOR** | MINOR | OK | OK | DOC |
| 06 | **MAJOR** | **MAJOR** | MINOR | **MAJOR** | **MAJOR** | **MAJOR** | OK | **MAJOR** |

Case 05 is the campaign's reference implementation on cross-role parity, standards and release integrity, and its
Accessible edition is the model the other cases should have followed. Case 06 carries the largest cluster of
defects in the campaign, and **four of them share a single cause**: the owner-review revision `59005a8` was
applied to the learner pages, the README and the release record, but not to the Teacher Guide or the task
registry, leaving both describing a superseded figure and a superseded page structure.

## 4. Cross-role task-parity findings

Task **order and registry-identifier parity are exact** in every case: tasks appear once each, in ascending
order, with identical canonical ids across Student, Answer Key and Accessible. The defects are in *content*
parity, not sequence.

- **Case 02 Task 1 — BLOCKER.** Unusable as printed, described three incompatible ways. Student Table 1 is
  3 columns × 7 rows with **zero** response cells (the page's only response is `t1-trials`), yet the directions
  say "Marking a condition OK means you can stop investigating it." The Accessible directions say "In the last
  column of **Table 1a**, write OK … or ?" — the string `Table 1a` occurs **exactly once in the entire file**,
  in that sentence; the real table is `Table 1 · What the garden reports` and also has zero response cells. The
  Answer Key completes a **2 × 5** table (`Condition | Mark`) that merges the Student's seven rows and marks
  three "?" (Pollinators, Airflow, Periodic vibration). The Teacher Guide says "Task 1. Every row is OK except
  **the last two**: no pollinators and no periodic vibration" — two rows, contradicting the Answer Key's three.
- **Case 04 Task 2 — MAJOR.** The Accessible edition omits Table 4 (`What each log reports`) — its table set is
  2, 3, 5, 6, 7 versus the Student's 1–7 — while retaining the prompt "What both logs agree on, and what their
  three-day difference does not mean." The only log content on that Accessible page is the sentence naming Day
  −80 and Day −83. The Answer Key grades against four agreements ("the power fluctuation, the schedule change,
  the loss of signalling that followed, and no other change and no structural decline") that no Accessible
  student can see. Invisible to the existing validator, whose reference check only fires on *named* tables.
- **Case 03 Task 5 — MAJOR.** Student and Accessible print "total PAR alone **proves no effective spectrum**";
  Teacher and Answer Key print "total PAR alone **does not establish** an effective spectrum." The student-facing
  sentence inverts the packet's own reasoning rule, and the Answer Key grades against the other wording.
- **Case 01 Tasks 1, 5, 6 — MAJOR.** Answer Key rows depend on evidence in no learner edition: nutrient/light
  "verified" rows (also unsupported by the game), the raw gravity profile (radii, magnitudes, `0.00187 g`,
  `2.88966 RPM` — all deliberately withheld and confirmed 0 occurrences), and `±0.05 g` plus the endpoint values
  required to reject "calibrated too strong" at Task 6, which first appear at Task 8.
- **Case 02 Task 5 — MAJOR.** The 100–150 Hz Telluvian comparison, `28 dB`, the lyre-moth, "buzz pollination"
  and "poricidal" occur **0 times** in Student and Accessible, yet Task 5 and the CER exemplar require them.
- **Case 03 Task 4 / Case 04 Task 8 — MINOR.** Answer Key exemplars cite runtime-only facts (a 30%-higher photon
  flux; the grove being "culturally significant") that no printable role carries.
- **Case 06 Task 4 — MAJOR.** Student Table 6 carries only bare source labels — there is no reported-observation
  column, unlike Case 05's equivalent. The Answer Key nonetheless grades against Kess's mechanism (stated in no
  learner edition), `Section 14.7` (printed one page later, at Task 7) and `GC-2201` (printed nowhere). My own
  independent check confirms `GC-2201` occurs **0 times** in both learner editions. The README's claim that Task 4
  "receives a full five-source contribution-and-limit matrix" describes response cells, not evidence.
- **Case 06 Tasks 1 and 3 — MAJOR.** The Accessible edition drops the Student Table's record column entirely
  (2 columns versus 3), so no Accessible learner can tell which row was never tested except from the directions.
  Downstream, `Corrected years ago`, `toxicology` and `summit` occur **0 times** in that edition, leaving two of
  Task 3's three rejections unanswerable from the page.
- **Case 06 — MAJOR.** Student and Accessible table numbering diverges (the Student vocabulary table is numbered
  `Table 1`; Case 05 leaves its equivalent unnumbered), so four Teacher and Answer Key references — "Figure A and
  Table 3 report the same survey", "Table 4 supplies the piece students need", "Tables 1–7 are the case records" —
  misresolve for Accessible readers. Case 05's release record certifies `crossRoleReferenceIntegrity: PASS`;
  Case 06's record has no such entry and its validator has no equivalent assertion.
- **Cases 03 and 04 Task 1 — MINOR.** Both ask for a change/keep classification before the controlling evidence
  is printed. In Case 03 the Accessible edition supplies it and the Student edition does not — the differentiated
  edition is better evidenced than the base edition for the same task.

## 5. Answer-correctness findings

Independent recomputation found the **quantitative core sound**. Case 01's entire `a = ω²r` profile was
re-derived from scratch (ω = 2.88966 RPM → 2.1000012 g at 224.9 m; 2.0990675 g at 224.8 m; 2.1009349 g at
225.0 m; Δ = 0.0018675 g → 0.00187 g; Δa/a = 0.089%; spec band 2.05–2.15 g) and matches every printed figure at
the authored precision, including the deliberate mixed-precision policy and the 0.0018-vs-0.00187 rounding
relationship. Case 04's unreported-hour-block complement (0–6, 12–18, 18–19) is arithmetically correct, and its
reconciliation of the game's latent 18/6-versus-hours-19–24 ambiguity is careful and does not invent data.
Case 03's four-figure spectrum comparison correctly preserves two different blue-green band edges rather than
eliding them.

Two answers are **wrong or unsupported**:

- **Case 04 Task 4 — MAJOR.** The Answer Key asserts "Intensity has stayed at 100% of the standard grow setting
  throughout" and "intensity did not change." No printed record establishes this (only a *current* 100% value
  exists), and the game contradicts it: the caretaker says "We set the lights to maximum — **24 hours, full
  intensity**." Verified present in the `silent_grove` case data. The rejection survives on its other three
  clauses, but the key teaches a fabricated control.
- **Case 01 Task 1 — MAJOR.** "Nutrient supply — Y — verified against the cultivation standard" and "Grow-light
  spectrum — Y — calibrated to the homeworld standard" are supported by neither the packet nor the game. The
  game's only historical record is three crops varying soil and seed stock; water is never mentioned in the case.

### Systemic confirmation

I ran an independent evidence-availability sweep across all six cases, extracting every reported value and
distinctive proper noun from each Answer Key and testing for its presence in the learner editions. It reproduces
the agent findings exactly and independently: **Case 01** (`0.00187 g`, `2.0991 g`, `2.1009 g`, `224.8/224.9/225.0 m`,
`0.3%`, `80 m`, `300 m`, `GC-1445`), **Case 02** (`150 Hz`, `buzz pollination`, `lyre-moth`, `poricidal`,
`wingbeat`), **Case 06** (`GC-2201`). Cases 03, 04 and 05 are **clean** on this check.

## 6. Teacher-completeness findings

- **Case 01 — MAJOR.** The guide describes a Task 3 that no longer exists, in three places ("Task 3 needs one
  subtraction of four-decimal values"; a preparation note keyed to it; a ledger row "What Task 3 produces. Accept
  it, and require the explanation"). Commit `bf0ad45` removed all arithmetic from Task 3; the guide was not
  updated, and it now instructs teachers to require a number students cannot obtain — contradicting the same
  guide's own "the packet requires no calculation anywhere."
- **Case 01 — MAJOR.** One of four formal rubric dimensions ("Precision"), one measurable objective, and one
  success criterion cannot be scored from the printed packet, because the values they grade never reach learners.
- **Case 02 — MAJOR.** The guide references "Figure 2", which exists in no role; the only numbered figure is
  Figure 1. The same guide elsewhere says the four-settings block is "a labelled comparison rather than a figure."
- **Cases 01 and 02 — MINOR.** Annotated answers cover only Tasks 1, 3, 4 and 8; Tasks 2, 5, 6 and 7 have no
  teacher-side answer or acceptable range.
- **Case 05 — MAJOR (printable text corruption).** `teacher-guide-09` prints a bare `X` where a clause belongs:
  "Tasks 1–3 sit naturally in the first, Tasks 4–7 in the second. **X** so the explanation is written in one
  sitting rather than assembled in margins." Verified in the shipped markup. It has survived the original draft,
  owner review, a 101/101 case validator, a 28-page visual review and a physical print gate at 100% / Actual Size.
- **Case 06 — MAJOR ×3.** The Teacher Guide describes Figure A as drawn "along a **twelve-metre strip**" and
  as "**The strip** is drawn to show the reported pattern" — the shipped figure is a plan view with four
  `<circle>` elements and `aria-label="Plan view of surveyed ground…"`. It states "The CER occupies a full page in
  **both** learner editions" — the Student CER is combined with Task 7 under `combined-v1.0`. And it tells
  teachers the Accessible edition's "task numbers, **the evidence** and the diagnosis are identical", which the
  removed record column contradicts.
- **Case 06 — MAJOR.** The building-inspection analogy that the approval record binds to Task 1 is printed on
  page 2, *after* Task 1, in both learner editions. Case 05 places its rain-gauge analogy correctly, inside the
  page of the task it teaches.
- **Case 04 — OK, and the strongest guide in the campaign**: it defends its own analogy design, separates
  teacher-only vocabulary, and states its assessment boundary honestly.
- Science boundaries are preserved in every case. No guide generalises alien-organism biology to Earth, and each
  carries an explicit "claims to correct on sight" list.

## 7. Accessible-differentiation findings

Differentiation is **real and per-task** in all four audited cases — one task per page, rewritten register,
word banks, sentence frames, section-per-source decomposition, and a full-page CER preserved everywhere.

Defects:

- **Case 04 — MAJOR.** Removed essential evidence (Table 4) while retaining the prompt that needs it (§4).
- **Case 02 — MAJOR.** Similarity measured at **76.6%**, but `history/release-v1.0.json` claims the edition sits
  "inside the 43-68% band set by the approved cases." The validator only enforces ≤80%, so the overshoot passes
  silently while the release record asserts the opposite. Table 1, Table 2, Figure 1 with its full caption and
  extended description, the researcher's block quote and the entire four-settings block carry over verbatim.
- **Case 02 — MAJOR.** Differentiation is **inverted at Task 1**: the Accessible edition asks for seven
  classification judgements *plus* the Student's written response, from the same two dense tables.
- **Case 01 — MINOR.** The Accessible edition drops "neither toward the axis nor away from it," the clause that
  rules out a listed prohibited claim and is quoted back in the Answer Key CER exemplar. Its CER page also
  receives no extra scaffold on the hardest task in the packet.

- **Case 06 — MAJOR.** Removed essential evidence (§4): the Task 1 record column and the Task 3 rejection
  records. Structurally its Accessible edition is the campaign's most ambitious — the five-source matrix becomes
  five headed blocks, one source at a time — but it is the least self-sufficient learner document in the campaign.
- **Case 05 — the reference implementation.** One task per page, nine scaffold blocks, a word bank that keeps
  every rejection answerable from the page, and no essential evidence removed.

Measured similarity across the campaign: Case 01 67.7%, Case 02 76.6%, Case 03 60.1%, Case 04 67.8%,
Case 05 55.4%, **Case 06 51.0%** — the most differentiated edition in either campaign. Case 05's release record
and approval document both call Case 05 "the most differentiated Accessible edition in Campaign 2"; that
superlative was true when written and is now false.

## 8. Standards findings

Five standards claims are not supported by the tasks named to carry them. None was revised during this audit.

| Case | Standard | Claimed | Finding |
|---|---|---|---|
| 01 | MS-ETS1-3 | supporting | **MAJOR.** Justified by records GC-1208 and GC-1445, but `GC-1445`, `80 m` and `300 m` occur 0× in both learner editions. No student sees two design outcomes to analyse, and nothing asks for a combined solution. |
| 02 | MS-LS1-4 | direct | **MAJOR.** The specialised-plant-structure half is genuinely present; the **characteristic-animal-behaviour half is entirely absent** — `moth`, `wingbeat`, `bee`, `buzz` all 0× in learner editions. A student can earn full credit believing the missing event has no biological agent. |
| 02 | MS-LS2-2 | supporting | **MAJOR.** Topic-only. One organism pair, one setting, nothing predicting patterns, nothing spanning multiple ecosystems. |
| 02 | MS-ETS1-3 | supporting | **MAJOR.** The three hand-pollination trials are the *same* solution with three applicators, not several competing designs. |
| 03 | MS-PS4-2 | direct | **MAJOR.** No task models reflection, absorption or transmission through a material. Justified by wavelength vocabulary and by figures students read rather than build. |
| 04 | MS-LS1-5 | direct | **MAJOR.** The PE names *growth*; this case holds growth constant deliberately, and the Teacher Guide itself instructs teachers not to report growth evidence from the packet. |
| 06 | MS-LS2-2 | direct | **MAJOR.** The PE reads "across multiple **ecosystems**"; the packet has one restored terrace with two bed types. The named assessing task (Task 4) is a source contribution-and-limit matrix — an epistemics task — not the construction of an explanation, which lives in Task 6. |
| 06 | MS-ETS1-2 | supporting | **MINOR.** Mapped to Task 3, which evaluates competing *explanations*, not competing *design solutions*. Case 05 anchors the same conditional claim correctly to two actual solutions. |
| 04 | MS-ETS1-1 | direct | **MINOR.** Rests partly on an "impacts on people" expectation the Student task never sets — and Case 03 rates the structurally identical Task 8 as *supporting*. One of the two ratings should move. |

Conservatively-hedged claims (Case 01 MS-ETS1-2, Case 02 MS-PS4-1, Case 03 MS-ETS1-2, Case 04 MS-ETS1-2) are
**correct and honest**, each explicitly withheld unless the class performs the missing practice. No case claims a
mathematics standard, and that withdrawal is mechanically enforced.

## 9. Visual and print findings

**No visual or print defect was found in any Campaign 2 case.** Verified mechanically across all six:

- Every figure carries a caption, an extended description, and a pattern fill; **zero** curves, polylines or
  polygons in any figure; no duplicate figure letters or table numbers within any role; no colour-dependent
  legend wording anywhere.
- Page-identity contracts are exact in all six: first/continuation headers correct, footers correct, Student
  identification rows only on page 1 of Student and Accessible, and no formal "Role:" field in any learner
  edition.
- Browser matrix confirms page fit, fixed Letter geometry (816 × 1056 CSS-px pages, 720 × 960 frames), grayscale
  states and print isolation for all 13 cases. **Zero JavaScript errors** across 24 role loads.

One campaign-wide *pattern* worth recording (not a defect, and not remediable without reopening five approved
packages): Student CER pages in Cases 01–05 carry **300–530 px** of unused reserve, because the Student CER uses
a fixed `min-height: 2.55in` and the Student content area is not a flex column. Case 06's combined CER + Task 7
page under `data-student-cer-page="combined-v1.0"` is the only Student CER page that fills its page (19 px
reserve). Measured reserve per page, all roles, is recorded in §12 of the working notes.

## 10. Game-to-curriculum evidence crosswalk

Every case's identity, five formal clues, correct diagnosis and rejected alternatives were traced to
`campaign_2_data.js` and `docs/campaign_2_science_sources.md`. Identity fields, clue tags and required routes
match the runtime exactly in all audited cases. Numeric transcription is faithful throughout — inequalities
(`<5%`, `<0.01 mGy/day`), ranges (`40–80 ppb`, `460–540 nm`, `approximately four to six metres`), qualifiers
("about", "trace levels only", "near 124 Hz") and modeled-versus-measured status are preserved.

Curriculum claims are, as designed, systematically **weaker** than the runtime. The exceptions found:

| Case | Curriculum claim | Canonical source | Category |
|---|---|---|---|
| 01 | "soil, nutrients, light, water … each changed without effect" | Game records only soil (Crop 2) and seed stock (Crop 3); water never mentioned | **Stronger — MAJOR** |
| 01 | GC-1445 reused as radius evidence | Game: "No misalignment **(low gravitropic precision)** … Gradient sensitivity is species-dependent" | **Qualifier dropped — MAJOR** |
| 04 | "Intensity has stayed at 100% … throughout" | Game: "We set the lights to maximum — 24 hours, full intensity" | **Contradicted — MAJOR** |
| 01 | "The archive says the bed-scale difference is negligible" | It is the botanist who says it, twice; the archive does not | Misattributed — MINOR |
| 01 | "Nominal; no vibration and no wobble reported" | Game says only "Ring Status: NOMINAL" | Invented absence — MINOR |
| 03 | "an approximation from an incomplete weighting model" | Game says only "~14 µmol/m²/s (starvation level)" | Invented provenance — MINOR |
| 04 | Distractor reworded to "scrubbers are filtering the compounds out" | Game: "chemical filtering has **drifted out of range**" | Reworded — MINOR |
| 02 | "the plant is vigorous and healthy" (present tense) | "Vigorous growth" is Month 1 only; Month 3 is "No successful bloom since week 5" | Overstated — MINOR |

**Obsolete design-document language** was correctly excluded in every case; the shipped runtime and the science
register won every conflict. **Internal clue tags** never leak into printable content. **Game-side issues found,
out of scope, no curriculum impact:** `missing_dance.callHomeHints.low` refers to Miran-sel as "she" while every
other reference uses they/them; the Case 03 OMS-4 output categories as reported sum to >100%, which the packet
reproduces faithfully and contains with a "do not sum" caution.

## 11. Release-integrity findings

Correct in all six cases: package `sourceHashes` match on-disk SHA-256 for all four sources; release-record
hashes match the package; `history/` contains exactly the two canonical records; no generated artifacts tracked;
approval date, owner, version, status and page counts agree across package, task registry, registry entry,
release record, approval record and README; all frozen DOM baselines match current markup.

Defects:

- **Cases 01 and 02 — MAJOR.** `canonicalSourceApprovalCommit` **does not contain the source it certifies.**
  Case 01 pins `864156f0…` and records `taskRegistry` = `7d92bac9…`, but that file at that commit hashes
  `485076fa…`; the real release commit is `a419591`. Case 02 pins `16c53a4b…` recording `949beba1…`, but that
  file there hashes `be69ff59…`; the real release commit is `b453457`. Content, presentation and layout-overrides
  do match at both pinned commits — only the lifecycle-stamped task registry does not. The validators compare
  record↔package but never record↔commit, so both pass.
- **Cases 01, 02 and 04 — MINOR.** Accepted-validation figures in the release and approval records were stale on
  the day they were written: Case 01 records `69/69` and `static 432/432` where its own release commit message
  says `74/74` / `436/436`; Case 02 records `63/63` / `468/468` against `68/68` / `472/472`; Case 04 records
  `75/75` where the validator committed in the same commit reports `82/82`. A reviewer reproducing the approval
  numbers will fail to.
- **Case 01 vs Case 02 — MINOR.** The two release records disagree about the same suite: Case 01's says
  `case01Scoped: 69/69`; Case 02's says `case01Scoped: 74/74 (unchanged, byte-identical)`. 74 is correct.
- **All six — DOCUMENTATION-ONLY.** `release-v1.0.json.sourceHashes` omits `layoutOverrides`, which the package
  does pin. A layout-overrides edit would break the package hash but leave the release record silently valid.
- **Case 02 — MINOR.** `figureProvenance` declares `fig-factors`, which exists in no role.
- **Case 06 — MAJOR.** `task-registry.js` `figureProvenance` — designated "the ledger of record" by the package
  README — still describes the superseded figure: "One **twelve-metre strip** on which the surveyed compounds are
  abundant from 0 to 5 metres…". The validator checks `figureProvenance` only for id-set equality and `kind`
  prefix, never the `shows` text against the rendered figure.
- **Case 06 — MINOR.** Recorded validation counts are understated at the commit they describe: the records say
  `148/148` and `static 576/576`; the released tree produces `153/153` and `580/580`.
- **Cases 01–05 versus 06 — DOCUMENTATION-ONLY.** The package `location` field means different things: Cases
  01–05 store the runtime *investigation name*, Case 06 stores the runtime *location*. Each validator encodes its
  own convention, so both pass and the divergence is invisible.
- **Case 04 — DOCUMENTATION-ONLY.** `migrationNotes` carries a Case 03 copy-paste ("keeps its runtime case number
  and is not renumbered as Campaign 2 Case 01").

## 12. Shared editor and validation findings

No approved case content is involved in any item below.

- **MAJOR — a released case is silently untested.** `browser-harness.html:270-271`: `accessibleEligibleCounts`
  and `studentEligibleCounts` each list **12 of 13** cases; `SSS-C1-CASE07` is absent from both. The loop
  iterates the map, so Case 07 receives zero resize-eligibility, layout-panel and invalid-default coverage.
  Its real values are Accessible 23 eligible / 12 locked, Student 11 / 24.
- **MAJOR — unreachable check.** `browser-harness.html:1152` (outer guard) and `:1159` (nested) carry different
  rosters. `SSS-C1-CASE06` appears in the inner roster but not the outer one, so the SAA-insignia grayscale
  assertion at `:1160` is dead code for that case.
- **MAJOR — grayscale palette covers 7 of 13.** The `:1152` roster excludes `SSS-C1-CASE01`, `SSS-C1-CASE02`,
  `SSS-C1-CASE06`, `SSS-C2-CASE04`, `SSS-C2-CASE05` and `SSS-C2-CASE06`. No global backstop exists — the three
  newest approved Campaign 2 cases have no grayscale palette assertion at all.
- **MAJOR — structural validation is Campaign 1 only.** `validate_canonical_case_structure.py:13` sets
  `CAMPAIGN = ROOT / "sss/campaign-1"` and `:141` hard-codes the seven-case roster. It reports `"cases": 7`
  against a 13-case registry. Campaign 2 coverage is complete today only because each `validate_caseNN_campaign2.py`
  re-implements it by hand; a fourteenth case would receive **zero** shared structural coverage. Fixing it is a
  single coupled edit — `case_key = case.name[:7]` at `:245` collides `campaign-1/case-01` with
  `campaign-2/case-01`, and `:311` carries a Campaign-1-Case-01-specific assertion that would misfire.
- **MAJOR — four repository documents state that Campaign 2 is unproduced.** `README.md:5,9`;
  `apps/curriculum-editor/README.md:3,5,7`; `CURRENT_PROJECT_STATE.md:40-47` (release table omits Campaign 2
  Cases 01, 02, 04, 05, 06) and `:51` ("The remaining Campaign 2 cases are unproduced"). Also
  `CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md:66` and `REPOSITORY_CURRICULUM_LIBRARY_ARCHITECTURE.md:38` say "all 40
  case/role/presentation states"; the matrix is now 104.
- **MINOR — stale wording.** `validate_static.py:335` still says "plus the unreleased Campaign 2 case";
  `browser-harness.html:1091` labels Cases 04–06 "legacy protected components".
- **MAINTENANCE-DEBT — hand-maintained magic totals.** `13` in `validate_case05`/`case06` (a campaign-wide
  invariant asserted redundantly by case-scoped validators); `104` and `52` matrix totals; the literal
  seven/six campaign counts. All correct today; all rot on the next case.
- **MAINTENANCE-DEBT — `run_pdf_tests.py` is absent from the root README validation workflow**, although it is a
  real regression suite and is named in the per-case READMEs.
- **OK-BY-DESIGN.** Draft-lifecycle branches in `validate_static.py:357-360,403,482` and
  `validate_canonical_case_structure.py:229-236` are currently unreachable but schema-faithful and needed the
  moment a case is drafted. The `unreleased` draft exemptions added during Case 06 production were correctly
  removed at release; none survives.

**Validator chaining.** `validate_static.py` chains eight subprocesses — canonical structure, layout overrides,
the six Campaign 2 case validators, and the authoring-service tests. `run_browser_tests.py` and
`run_pdf_tests.py` are manual by design (they require Chrome).

## 13. Cleanup-audit root cause

`shared/validation/validate_repository_cleanup_audit.py` crashes with `FileNotFoundError` on
`shared/implementation/CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json`.

**Root cause: the validator is a retired, baseline-anchored migration-era control that reads retired historical
inputs from the working tree.** Evidence:

1. **Five inputs are missing, not one.** `CLEANUP_OWNER_REVIEW_CHECKLIST_v1.md` (never committed at any commit),
   `CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json`, `phase2-protected-artifacts.v1.json`,
   `CURRICULUM_EDITOR_CUTOVER_v1.json`, `CUTOVER_VALIDATION_RESULTS.json`. The last four existed at the audit
   baseline `66b4d5514d55aa4ce9972bea46227d7362d10ce3` and were deleted in `34cbe28`.
2. **The deletions were owner-authorised.** The frozen cleanup plan lists all four as RETAIN, but
   `CANONICAL_CASE_STRUCTURE_MIGRATION_v1.md` records that "the 2026-08-01 owner decision authorizes the cleanup
   and **supersedes that earlier conservative proposal wherever they conflict**"; its
   `supersession.recordsPreservedUnmodified` deliberately preserves only the four snapshot documents; and
   `CANONICAL_CASE_STRUCTURE_OWNER_APPROVAL_v1.md` closes "This approval … **does not restore any retired or
   generated artifact**." The migration's `validatorRetirement[1]` names this exact workflow as retired:
   "Phase 2 protected-inventory, reconciliation, package builder, binding audit, and cutover validator."
3. **It cannot pass even if every input were restored.** It is a frozen no-change assertion against a baseline
   that no longer describes the repository: `:157` requires 477 tracked files (HEAD tracks 223); `:185` requires
   that no baseline file was deleted, moved or modified (the approved migration deleted 377 paths); `:296-299`
   require Case 04 to be `NOT_STARTED` in three manifests that no longer exist.
4. **It is fully orphaned.** Nothing executes it; the only live reference is its own self-listing at `:34`. The
   root README validation workflow excludes it, and a prior audit already classified it "Retired legacy-cleanup
   audit utility | NOT CURRENT / not counted."

**Resolution: option (b)/(d) — the validator references retired artifacts and should itself be retired.** The
missing files must **not** be restored. Forensic recovery, if ever wanted, is
`git show 34cbe28^:shared/implementation/CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json`.

**Not applied in this audit**, because Phase 6 is gated behind the remediation rule (§15).

## 14. Defect list by severity

### Blocker (1)

| ID | Case | Where | Defect |
|---|---|---|---|
| B-1 | 02 | Task 1, all four roles | Unusable as printed and described three incompatible ways (§4). |

### Major (23)

| ID | Case | Where | Defect |
|---|---|---|---|
| M-1 | 01 | Registry, Teacher p1 | "nutrients, light, water … changed without effect" unsupported by the game |
| M-2 | 01 | Answer Key Task 1 | Two fabricated Y rows |
| M-3 | 01 | Teacher p4, AK p4 | GC-1445 species qualifier dropped, then reused as radius evidence |
| M-4 | 01 | Answer Key Task 5 | Requires radii/magnitudes/RPM withheld from learners |
| M-5 | 01 | Answer Key Task 7 | CER exemplar not producible from any learner edition |
| M-6 | 01 | Answer Key Task 6 | Rejection needs ±0.05 g and endpoints unavailable at that task |
| M-7 | 01 | Teacher pp. 3, 6 | Describes a Task 3 subtraction that no longer exists (3 places) |
| M-8 | 01 | Teacher pp. 1, 8 | Rubric dimension, objective and success criterion unachievable |
| M-9 | 01 | Standards | MS-ETS1-3 unsupported |
| M-10 | 01 | Release record | `canonicalSourceApprovalCommit` does not contain the certified task registry |
| M-11 | 02 | Teacher p7 | References a non-existent "Figure 2" |
| M-12 | 02 | Task 5, AK Task 7 | 100–150 Hz, lyre-moth, buzz pollination, poricidal — 0× in learner editions |
| M-13 | 02 | Accessible | Similarity 76.6%; release record claims "inside the 43-68% band" |
| M-14 | 02 | Accessible Task 1 | Differentiation inverted — asks for more than the Student edition |
| M-15 | 02 | Standards | MS-LS1-4 animal-behaviour half absent |
| M-16 | 02 | Standards | MS-LS2-2 topic-only |
| M-17 | 02 | Standards | MS-ETS1-3 — one solution, not several |
| M-18 | 02 | Release record | Same pinned-commit hash mismatch as Case 01 |
| M-19 | 03 | Student + Accessible Task 5 | "total PAR alone proves no effective spectrum" — inverted |
| M-20 | 03 | Standards | MS-PS4-2 direct not supported |
| M-21 | 04 | Accessible Task 2 | Table 4 removed; prompt and Answer Key still require it |
| M-22 | 04 | Answer Key Task 4 | Intensity control unsupported and contradicted by the game |
| M-23 | 04 | Standards | MS-LS1-5 direct contradicted by the packet's own boundary note |

| M-24 | 05 | Teacher p9 | Bare `X` replaces a clause in printable text |
| M-25 | 06 | Figure A + ledger | "about three metres" repurposed as a surveyed patch-edge offset, against the packet's own precision ledger |
| M-26 | 06 | Both learner editions | Table numbering diverges; four Teacher/Answer-Key references misresolve for Accessible |
| M-27 | 06 | Task 4 | No printed source statements for three of five sources; AK requires `GC-2201`, printed nowhere |
| M-28 | 06 | Accessible Tasks 1, 3 | Record column removed; two of three rejections unanswerable from the page |
| M-29 | 06 | Teacher pp. 3, 8 | Describes Figure A as a "twelve-metre strip"; shipped figure is a plan view |
| M-30 | 06 | Teacher p5 | "The CER occupies a full page in both learner editions" — Student CER is `combined-v1.0` |
| M-31 | 06 | Teacher p2 | Tells teachers the Accessible evidence is identical; it is not |
| M-32 | 06 | Both learner editions | The analogy bound to Task 1 is printed after Task 1 |
| M-33 | 06 | `task-registry.js` | `figureProvenance` — the declared ledger of record — describes the superseded strip |
| M-34 | 06 | Standards | MS-LS2-2 direct: "across multiple ecosystems" absent; named task is a source-limits matrix |

Plus five shared-infrastructure majors (§12), which touch no case package.

**Cause concentration.** M-25, M-26, M-29, M-30 and M-33 all trace to the single owner-review revision
`59005a8`, which was propagated to the learner pages, the README and the release record but not to the Teacher
Guide or the task registry. A revision-propagation checklist covering all four roles plus the registry would have
caught the whole cluster.

### Minor (24) and documentation-only (7)

Recorded in §§4–11. Summary: Case 01 A-3, A-4, A-5 (a 2 m-radius/2 m-across arithmetic error propagated to five
files), C-3, C-4, D-3, D-4, E-1, E-2; Case 02 A-1, A-2, B-4, D-2, D-3, H-2; Case 03 A-1, A-2, B-2, B-3, D-1
(four text errors including one in an Accessible direction), T8 criterion 2; Case 04 A-3, B-5, B-6, C-2, F-3,
H-2. Documentation-only: Case 03's unexplained older pin; the `layoutOverrides` hash absent from all six release
records; Case 04's `migrationNotes` copy-paste; SAA-versus-Federation branding across Campaign 2; stale accepted
validation counts; the game-side pronoun slip.

## 15. Remediation plan

**The remediation rule applies.** Approved packages carry substantive content, answer, Teacher, Accessible and
standards defects, so **no approved case was modified**, and Phase 6 campaign-level maintenance was **not
performed**. The following is the plan, not a record of work done.

**Reopening any case invalidates, for that case:** `case-package.json.sourceHashes` (content and/or
task-registry), `history/release-v1.0.json.sourceHashes`, the Student/Teacher/Answer entry in
`NON_ACCESSIBLE_BASELINE_HASHES` in `validate_static.py`, and the print attestation in
`CASE0N_OWNER_APPROVAL_v1.0.md` — a content change to any learner edition requires a fresh physical print test.
Case-scoped assertion totals and the release record's accepted-validation figures would also need re-recording.

Recommended sequencing:

0. **Case 06's revision-propagation cluster is the cheapest large win.** M-25, M-26, M-29, M-30, M-33 are all
   Teacher-Guide or registry text, plus one figure annotation and one table-numbering decision. Only the figure
   annotation and the table renumbering touch a learner edition and therefore require a re-print; the rest are
   Teacher/registry-only and do not.
1. **Case 02 blocker first.** Decide the intended Task 1 design (add a mark column to Table 1 in both learner
   editions, or convert it to a stand-alone response block), then reconcile the Answer Key table shape and the
   Teacher's "last two" note to it, and fix the dead `Table 1a` reference. Requires re-print of Student and
   Accessible.
2. **Evidence-availability majors** (M-2, M-4, M-5, M-6, M-12, M-21, M-22): for each, either print the missing
   evidence in the learner editions or rewrite the Answer Key exemplar to the evidence students actually hold.
   The second option is cheaper and, for Case 01, is the option consistent with the deliberate design that keeps
   the raw gravity profile out of learner editions.
3. **Single-sentence corrections** (M-19 Case 03 wording, M-1/M-3 Case 01 sourcing, M-11 Figure 2, M-7/M-8
   Case 01 Teacher): low-risk text edits, but each still re-hashes its package.
4. **Standards downgrades** (M-9, M-15, M-16, M-17, M-20, M-23 and the Case 03/04 MS-ETS1-1 inconsistency):
   documentation-level within the packages; owner should decide whether to downgrade to supporting or to add the
   missing assessed content.
5. **Release-record corrections** (M-10, M-18 pinned commits; stale validation counts; the missing
   `layoutOverrides` hash): correctable without touching printable content, therefore without a re-print.
6. **Shared infrastructure** (§12) and the **cleanup-audit retirement** (§13): independent of every package
   defect and safe to authorise separately.

## 16. Owner decisions required

1. **Authorise reopening approved packages.** Cases 01–04 require it; Cases 05–06 pending the final audit stream.
   Each reopened learner edition needs a new physical print attestation.
2. **Standards policy.** Downgrade the six overclaimed standards, or extend the packets to assess them. This
   also resolves the Case 03/04 MS-ETS1-1 inconsistency on structurally identical tasks.
3. **Release-record correction policy.** Whether to correct historically inaccurate `canonicalSourceApprovalCommit`
   pins and stale validation counts in place, or to append corrections.
4. **Whether to authorise the shared-infrastructure and cleanup-audit work now**, ahead of package remediation,
   since it is independent and unblocks honest reporting of repository state.
5. **Figure-numbering convention.** Cases 01–03 use "Figure 1/2"; Cases 04–06 use "Figure A/B" and enforce it
   per case. No governing style-guide rule exists. Codify one for HHH, and decide whether Campaign 2 tolerates
   the split permanently.

## 17. Campaign-completion recommendation

**Do not close Campaign 2.** The campaign is complete as *production* — six released cases, consistent identity,
faithful numerics, clean release mechanics, and a validation estate that passes 580/580 static, 2161/2161
browser, 316/316 PDF across all thirteen registered cases. It is not complete as *quality*: one blocker makes a
released Task 1 unusable, and **thirty-four major defects** sit inside approved packages — including two answer
keys that teach claims the canonical game source does not support or contradicts, a bare `X` that reached print
through a physical print gate, and a Teacher Guide that describes a figure and a page structure the case no
longer has.

The validation estate did not catch any of them, which is the more important finding. Every defect above is
invisible to the current suites because they check structure, hashes, precision and prohibited claims — not
whether an Answer Key can be produced from the evidence a student actually holds. **Recommended follow-up
regardless of remediation choices: add a cross-role evidence-availability check** asserting that every value and
proper noun an Answer Key exemplar relies on appears in the corresponding learner edition. That single check
would have caught M-2, M-4, M-5, M-6, M-12, M-21, M-22 and M-27 — eight of the thirty-four. Two further cheap
checks would cover most of the rest: a **cross-role reference resolver** (does every "Table N"/"Figure X" named by
any role resolve to that content *in the role the reader holds*), which catches M-26 and Case 04's M-21; and a
**revision-propagation check** asserting that figure captions, `figureProvenance.shows`, and Teacher descriptions
of page structure agree with the rendered markup, which catches M-29, M-30 and M-33.

Case 05 should be treated as the campaign's reference implementation when remediating the others: it is the only
case clean on cross-role parity, standards and release integrity simultaneously, and its Accessible edition is the
only one that keeps every rejection answerable from the page.
