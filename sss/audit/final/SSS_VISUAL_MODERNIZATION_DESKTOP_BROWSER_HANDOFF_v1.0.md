# SSS Visual Modernization Desktop Browser Handoff v1.0

Use this handoff with local Codex or Claude on a machine with installed Google Chrome.
This is a read-only validation run. Do not edit sources, regenerate release baselines, run PDF
automation, or reopen correctness findings.

## Current validation target — C1C6 coordination-system model

The current branch tip advances `C1C6-VIS02` to `IMPLEMENTED-CANDIDATE`. It opts First Contact
Protocol into the shared-visual layer and applies a bounded system-rail treatment to the existing
Student Task 4 page 2, Accessible Task 4 page 3 and Answer Key Task 4 page 2 models.

The four exact stages and three original connectors remain in their existing horizontal and
Accessible vertical reading order. Direct states identify `PROCESSING`, `SIGNAL OFF`, `FICTIONAL
RESPONSE`, and `COORDINATION OFF`; transition labels remain `REMOVES`, `TRIGGERS`, and `DISRUPTS`.
Solid, dotted, dashed and double borders plus hatch states remain distinguishable in grayscale.
No worksheet content, presentation source, response ID, phrase-bank term, page count, source hash
or release baseline changes.

The accepted executable baseline is 2312/2312. This candidate adds one strict page-fit/geometry
assertion covering all three touched pages in both modes and one computed-style/content assertion
in each of normal and grayscale presentation. Its acceptance target is therefore
**2315/2315 PASS with 0 application JavaScript errors**. The focused mechanism validator target is
**60/60 PASS**.

## Recorded outcome — 2026-08-08

The C1C5 Europa radiation-to-growth pathway is `VERIFIED-FAMILY` at
`dcb2d91565769d7bd907b491359ef695a805f784`. The browser harness passed 2312/2312 twice with zero
application JavaScript errors. Student page 3, Answer Key page 3 and Accessible page 5 retained
strict `scrollHeight 936 <= clientHeight 936` fit in normal and grayscale presentation. The
mechanism validator passed 52/52. All seven direct evidence states, six original connectors, exact
Student and Accessible field identities and contents, and the complete Answer Key sequence were
preserved. Manual inspection found no clipping or collision and retained the distinctions between
modeled secondary radiation, possible exposure and biological evidence consistent with damage.
The branch was pushed by normal fast-forward. This recorded outcome satisfies every condition;
C1C5 is no longer an `IMPLEMENTED-CANDIDATE`.

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

   - browser harness: **2315/2315 PASS**;
   - application JavaScript errors: **0**;
   - mechanism validator: **60/60 PASS**;
   - whitespace: clean.

3. Start the editor with `python3 apps/curriculum-editor/serve.py` and inspect only these pages in
   normal and grayscale presentation:

   - C1C6 Student Task 4 page 2;
   - C1C6 Answer Key Task 4 page 2;
   - C1C6 Accessible Task 4 page 3.

4. Report for those pages:

   - overflow warning visible: yes/no;
   - clipping or state/connector-label collision: yes/no;
   - strict `scrollHeight <= clientHeight`: exact values;
   - fixed page box remains 816 × 1056 and page counts remain Student 5, Answer Key 5,
     Accessible 7: yes/no;
   - four ordered stages and three original connectors remain: yes/no;
   - horizontal connector order remains `→ | → | →`: yes/no;
   - Accessible connector order remains `↓ | ↓ | ↓`: yes/no;
   - direct states remain `PROCESSING | SIGNAL OFF | FICTIONAL RESPONSE | COORDINATION OFF`: yes/no;
   - transition labels remain `REMOVES | TRIGGERS | DISRUPTS`: yes/no;
   - Student retains blank `t4-atmosphere`, `t4-signal`, `t4-network`, and `t4-partnership`
     fields: yes/no;
   - Accessible retains blank `a4-atmosphere`, `a4-signal`, `a4-network`, and `a4-partnership`
     fields in vertical order: yes/no;
   - Answer Key retains all four exact completed stages: yes/no;
   - the phrase bank remains exact and identical between Student and Accessible: yes/no;
   - the fictional network response remains explicitly distinct from an Earth-organism claim:
     yes/no;
   - timing remains supporting correlation rather than proof: yes/no;
   - solid/dotted/dashed/double borders and hatch states remain distinguishable without color:
     yes/no;
   - browser-console JavaScript errors: exact count and text.

Do not run telemetry, repository-wide, legacy mutation, PDF, or unrelated checks. If every check
passes, push the candidate as a normal fast-forward and return the concise report. If anything
fails, hold unpushed and report the exact assertion, role, mode and measurements.

## Acceptance rule

`C1C6-VIS02` may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2315/2315 with zero application JavaScript errors, the focused mechanism validator reaches 60/60,
and the three touched pages retain strict fit, fixed geometry and their existing page counts in
normal and grayscale. The three new assertions must confirm the four-stage order, three connectors,
direct state and transition labels, grayscale-independent border/pattern states, exact Student and
Accessible response identities/contents, and complete Answer Key sequence. Manual inspection must
find no clipping or collision and must preserve the fictional-system and correlation limits.
