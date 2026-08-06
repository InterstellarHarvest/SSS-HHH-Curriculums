# Campaign 2 Case 03 v1.1 Owner Approval

Owner: **Nate / Owner**

Date: **2026-08-06**

Title: **The Wrong Color of Light**

Curriculum: **SSS · Campaign 2 · Case 03**

Runtime ID: **wrong_color_light**

Release status: **APPROVED_STABLE**

Review status: **OWNER_REVIEW_PASS**

Merge status: **READY_TO_MERGE**

Corrective of: **1.0**

## Release gates

- On-screen content and visual review: **PASS**
- Generated PDF review: **PASS**
- Physical print at 100% / Actual Size: **PASS**

All three gates were re-run for v1.1. A content change to any learner edition
invalidates the v1.0 print attestation, so this release does not inherit it.

## What this corrective release corrects

The Campaign 2 completion audit
(`sss/audit/SSS_C2_CAMPAIGN_COMPLETION_AUDIT_v1.0.md`) found five defects inside
the approved v1.0 package. All five are corrected here.

- **Corrected total-PAR reasoning.** The Student and Accessible editions printed
  "total PAR alone **proves no** effective spectrum" while the Teacher Guide and
  Answer Key printed "total PAR alone **does not establish** an effective
  spectrum". The learner sentence inverted the packet's own reasoning rule, and
  the Answer Key graded against the other wording. Both learner occurrences now
  carry the canonical sentence. The rule is additionally stated in full in a
  marked `data-reasoning-rule` block in each learner edition: total PAR counts
  every photon in the reported range; that total alone does not establish
  whether the spectrum matches the response measured for zhal-kelp; and
  lamp-output evidence and biological-response evidence are compared separately.
  All four roles now express one rule, and no role states its inverse.
- **Corrected evidence availability.** Task 1 asked learners to classify what
  changed and what was held constant before the Student edition printed the
  record that settles it — the Accessible edition supplied it and the Student
  edition did not. Both editions now carry a marked Week 0 change record naming
  all four classified conditions, on the page of the task that grades them. The
  Answer Key's Task 4 rejection reasoned from a 30%-higher installed photon flux
  carried by no printable role (it is Tei-sal's `wrong_guess_intensity` runtime
  dialogue); the clause was unnecessary and is removed, leaving the rejection on
  the 280 µmol/m²/s total in Table 1 and the old-dome control at 100% in
  Table 3. Task 8's intensity criterion graded against "the level the old dome
  delivered", which the packet never prints, and now names the 280 µmol/m²/s
  learners hold. Every graded claim is answerable from the printed packet.
- **Corrected approximate-value provenance.** The curriculum described the
  approximate `~14 µmol/m²/s` effective-PAR value as "an approximation from an
  incomplete weighting model". The canonical game source states the value and
  says nothing about how it was obtained. The invented provenance is removed
  from the Teacher Guide and the task registry. The value stays Teacher-facing
  and approximate, is never presented as exact or as a complete action-spectrum
  calculation, and is never used in student work.
- **Standards changes.** `MS-PS4-2` is **withdrawn** as a direct standard and is
  not replaced. No task develops or uses a model of light reflected, absorbed or
  transmitted through a material; students read reported wavelength bands and
  lamp-output figures, and wavelength vocabulary and figure reading alone do not
  assess that performance expectation. The Teacher Guide records the withdrawal
  and its reason so the claim cannot silently return. `MS-LS1-6` remains
  **direct** and now names Tasks 6 and 7 as the assessing tasks, fed by Tasks 2,
  3 and 5. `MS-ETS1-1` remains **supporting** and records why it is not direct.
  `MS-ETS1-2` remains **conditional**, keeps its existing limitation unchanged,
  and now names Task 8. No mathematics standard is claimed.
- **Accessible corrections.** The inverted Task 5 sentence is corrected; the
  Week 0 change record is stated one short sentence per held condition, in the
  edition's own register; a plain-language Reasoning rule callout is added where
  total PAR is introduced; and the direction "responds most strongly **in at**
  this site" is repaired. No scaffold was reduced, the edition was not reflowed
  toward the Student edition, one task per page is retained, and the diagnosis
  is still withheld until after evidence analysis.
- Three further printable text errors are repaired: a doubled "and and" in the
  Teacher success criteria, a truncated Answer Key rubric clause, and a doubled
  superlative in both extended descriptions.

## Preserved without change

- **Figures.** Figure 1's discrete GRO-9 output bars and Figure 2's separate
  measured 460–540 nm response band are unchanged, with their captions,
  extended descriptions, pattern fills, direct labels, category-boundary
  cautions, and the distinction between lamp output and biological response.
  Neither draws a continuous action-spectrum curve or a zero baseline, and both
  remain legible in grayscale with no colour-dependent wording.
- **Page counts and geometry.** Student Mission 5 pages, Teacher Guide 8 pages,
  Answer Key 4 pages, Accessible Mission 8 pages — unchanged from v1.0. Every
  page fits; no role overflows. Fixed Letter geometry of 816 × 1056 CSS-pixel
  pages with 720 × 960 CSS-pixel frames: PASS for all four roles. Response areas
  and resize eligibility are unchanged, so the layout-override contracts are
  byte-identical.
- **Instructional shape.** Eight tasks in the approved order with exact
  identifiers across Student, Answer Key and Accessible; the correct diagnosis,
  its three rejected alternatives, the five formal clues and their routes; the
  combined Student CER and lighting-specification workspace on Student page 5;
  and the Accessible dedicated CER page with its shared subtitle.
- **Science protections.** All prohibited-claim guards are retained and
  demonstrated by mutation: no claim that kelp universally cannot use red light,
  no equivalence between red light and darkness, no claim that `<5%` alone
  proves the diagnosis, no zero-response claim outside the measured band, no
  universal brown-algae action spectrum, no smooth response curve, no exact
  effective-PAR calculation from the packet's category data, no summing of
  output categories whose definitions do not align, no below-detection-as-zero,
  no correlation-as-causation, and no repeated reminders that the scenario is
  fictional.

## v1.0 historical preservation

- `history/release-v1.0.json` and `history/CASE03_OWNER_APPROVAL_v1.0.md` are
  retained **byte-identical**. Neither was edited to describe v1.1.
- v1.0 is represented inside `history/release-v1.1.json` as the canonical prior
  approved release, with its own approval date, approval commit, source hashes,
  DOM baselines, page counts and recovery command.
- v1.0's game pin `46b9387bca95736f164f905596e3dd8b13968661` is **preserved as
  written**. v1.1 pins the current authorized baseline
  `29c3b222c53f51de11a3aa83e896a6d0ef6fb490`; the audit verified
  `campaign_2_data.js` and `docs/campaign_2_science_sources.md` are
  byte-identical between the two commits, so the repin changes no evidence.
- v1.0 is superseded, not withdrawn. It was a genuine approved release with its
  own owner review, PDF review and physical print pass.
- Frozen Student, Teacher and Answer Key DOM baselines were regenerated for
  v1.1, and all three differ from v1.0's, so approved-baseline enforcement
  cannot be satisfied by the superseded v1.0 markup.

## Accepted validation

- Case 03 scoped: **107/107**
- Case 03 mutations: **22/22** — each mutation names and trips the specific
  protection it targets rather than a hash or frozen-baseline check
- Corrective-release lifecycle: **25/25**
- Campaign 2 Case 01 **74/74**, Case 02 **108/108**, Case 04 **82/82**,
  Case 05 **101/101**, Case 06 **153/153**
- Full static validation: **596/596**
- Browser matrix: **2161/2161**, zero JavaScript errors
- PDF validation: **316/316**
- Layout overrides: **PASS** across 13 registered cases
- Canonical case structure: **PASS**
- Authoring-service tests: **13/13**
- `git diff --check`: clean

## Artifact policy

`NO_GENERATED_ARTIFACTS_COMMITTED`: Campaign 2 Case 03 was produced natively
under the canonical source model at v1.0 and reissued the same way at v1.1. No
master, published role HTML, PDF, screenshot, browser profile, or generated
release file was committed at either version.

The owner approves Campaign 2 Case 03 v1.1 as the corrective release. This
approval records the classroom-material and physical-print gates for v1.1 and
authorizes integration into curriculum main. It supersedes v1.0 for classroom
use and does not alter, withdraw or reinterpret the v1.0 approval record.
