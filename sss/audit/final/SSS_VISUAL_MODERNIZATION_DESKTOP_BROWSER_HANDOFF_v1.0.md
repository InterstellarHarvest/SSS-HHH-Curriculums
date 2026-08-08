# SSS Visual Modernization Desktop Browser Handoff v1.0

Use this handoff with local Codex or Claude on a machine with installed Google Chrome.
This is a read-only validation run. Do not edit sources, regenerate release baselines, run PDF
automation, or reopen correctness findings.

## Current validation target — C1C5 radiation-to-growth pathway

The current branch tip advances `C1C5-VIS01` to `IMPLEMENTED-CANDIDATE`. It opts Europa Bunker
into the shared-visual layer and applies a qualified evidence-status treatment to the existing
Student Task 5 page 3, Accessible Task 5 page 5 and Answer Key Task 5 page 3 pathway models.

The seven exact stages and six original connectors remain in their existing horizontal snake and
Accessible vertical reading order. Direct states identify `ENVIRONMENT`, `MODELED`, `EXPOSURE`,
`LIMIT ≠ DAMAGE`, `BIO EVIDENCE`, `GROWTH`, and `CONVERGENCE`. Solid, dotted, double and dashed
borders plus hatch states remain distinguishable in grayscale. No worksheet content, presentation
source, response ID, approved Accessible prefill, phrase-bank term, page count, source hash or
release baseline changes.

The accepted executable baseline is 2309/2309. This candidate adds one strict page-fit/geometry
assertion covering all three touched pages in both modes and one computed-style/content assertion
in each of normal and grayscale presentation. Its acceptance target is therefore
**2312/2312 PASS with 0 application JavaScript errors**. The focused mechanism validator target is
**52/52 PASS**.

## Recorded outcome — 2026-08-08

The C1C4 Hayes closed fault loop is `VERIFIED-FAMILY` at
`d5b6c028d51649843170d2b7b84b20cf73db3ed9`. The browser harness passed 2309/2309 twice with zero
application JavaScript errors. Student page 3, Answer Key page 3 and Accessible page 5 retained
strict `scrollHeight 936 <= clientHeight 936` fit in normal and grayscale presentation. The
mechanism validator passed 44/44. The corrected Answer Key body extraction matched all six exact
stages, and the Accessible `↓ then repeat` connector rendered as a padded 3 px rounded rectangle
without border/label collision. The branch was pushed by normal fast-forward. This recorded
outcome satisfies every condition; C1C4 is no longer an `IMPLEMENTED-CANDIDATE`.

Earlier accepted family evidence remains recorded in the modernization plan.
The earlier C1C3 expansion could advance from `IMPLEMENTED-CANDIDATE` only after the harness reached
2303/2303 with zero JavaScript errors and the dense Student mechanism page retained 3.47 px reserve.
The recorded outcome above satisfies every condition.

## Prompt

You are validating the isolated `visual/sss-final-modernization` branch of
`InterstellarHarvest/SSS-HHH-Curriculums`. Correctness remediation is closed.

1. Verify the working tree is clean at the supplied candidate on
   `visual/sss-final-modernization`. Do not reset, rebase, amend, force-push, update frozen release
   baselines, edit expected values, or open a PR.

2. Run only:

   ```bash
   python3 apps/curriculum-editor/tests/run_browser_tests.py \
     --chrome "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

   python3 shared/validation/validate_sss_visual_mechanism_family.py
   git diff --check
   ```

   Expected:

   - browser harness: **2312/2312 PASS**;
   - application JavaScript errors: **0**;
   - mechanism validator: **52/52 PASS**;
   - whitespace: clean.

3. Start the editor with `python3 apps/curriculum-editor/serve.py` and inspect only these pages in
   normal and grayscale presentation:

   - C1C5 Student Task 5 page 3;
   - C1C5 Answer Key Task 5 page 3;
   - C1C5 Accessible Task 5 page 5.

4. Report for those pages:

   - overflow warning visible: yes/no;
   - clipping or status/connector collision: yes/no;
   - strict `scrollHeight <= clientHeight`: exact values;
   - fixed page box remains 816 × 1056 and page counts remain Student 4, Answer Key 4,
     Accessible 7: yes/no;
   - seven ordered stages and six original connectors remain: yes/no;
   - horizontal connector order remains `→ | → | → | ↓ | ← | ←`: yes/no;
   - Accessible connector order remains six downward arrows: yes/no;
   - direct states remain `ENVIRONMENT | MODELED | EXPOSURE | LIMIT ≠ DAMAGE | BIO EVIDENCE |
     GROWTH | CONVERGENCE`: yes/no;
   - Student retains blank `t5-2` through `t5-7` fields: yes/no;
   - Accessible remains vertical with only Stage 2 `interactions may produce modeled secondary
     radiation` and Stage 4 `exposure is possible, but exposure alone does not prove damage`
     prefilled: yes/no;
   - Answer Key retains all seven exact completed stages: yes/no;
   - modeled secondary radiation remains conditional rather than measured: yes/no;
   - exposure remains distinct from biological damage: yes/no;
   - meristem abnormalities remain evidence consistent with damage rather than proof of an exact
     molecular mechanism: yes/no;
   - no exact radiation quantity, crop-safe threshold or guaranteed shielding claim appears:
     yes/no;
   - solid/dotted/double/dashed borders and hatch states remain distinguishable without color:
     yes/no;
   - browser-console JavaScript errors: exact count and text.

Do not run telemetry, repository-wide, legacy mutation, PDF, or unrelated checks. If every check
passes, push the candidate as a normal fast-forward and return the concise report. If anything
fails, hold unpushed and report the exact assertion, role, mode and measurements.

## Acceptance rule

`C1C5-VIS01` may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2312/2312 with zero application JavaScript errors, the focused mechanism validator reaches 52/52,
and the three touched pages retain strict fit, fixed geometry and their existing page counts in
normal and grayscale. The three new assertions must confirm the seven-stage order, six connectors,
direct evidence-status labels, grayscale-independent border/pattern states, exact Student and
Accessible response identities/contents, and complete Answer Key sequence. Manual inspection must
find no clipping or collision and must preserve the modeled/exposure/damage qualifications.
