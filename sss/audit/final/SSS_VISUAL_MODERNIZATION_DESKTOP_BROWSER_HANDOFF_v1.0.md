# SSS Visual Modernization Desktop Browser Handoff v1.0

Use this handoff with local Codex or Claude on a machine with installed Google Chrome.
This is a read-only validation run. Do not edit sources, regenerate release baselines, run PDF
automation, or reopen correctness findings.

## Prompt

You are validating the isolated `visual/sss-final-modernization` branch of
`InterstellarHarvest/SSS-HHH-Curriculums`. The accepted correctness base is
`5844b56fd10e4be068dc9049f6a743cd473de805`. Correctness remediation is closed.

1. Fetch origin and verify that the working tree is clean on
   `visual/sss-final-modernization`. Do not reset, rebase, amend, force-push, or update any frozen
   release baseline.
2. Run:

   ```bash
   python3 apps/curriculum-editor/tests/run_browser_tests.py \
     --chrome "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
   ```

   The current executable browser target is **2303/2303 PASS with 0 JavaScript errors**. The
   accepted mechanism-family pilot `a9dfecf` produces 2300/2300. This expansion adds two
   computed-style assertions, one for normal and one for grayscale presentation, covering the
   C1C3 five-stage spectral-loss chain in Student, Teacher, Answer Key and Accessible roles.
   Candidate `7ec465e` was rejected at 2295/2302 solely because C1C3 Student page 3 exceeded its
   content area by 7 px. This successor compacts only the added Student-page mechanism chrome;
   it does not reduce the approved Task 5 response or 2.25 in process-stage writing height.
   Candidate `7ed27eb` subsequently passed 2302/2302 and reported `Pages fit`, but was held because
   the target content area still rounded to `scrollHeight 937 > clientHeight 936` and had no usable
   reserve. Candidate `b429fb4` was rejected at 2302/2303 because its margin reduction collapsed
   against larger neighboring margins and its new assertion was mistakenly placed in the C1C2
   block, where it returned a null Mars-page measurement. This successor reduces the dominant
   C1C3 Student phrase-bank top margin from 6 px to 2 px and moves the assertion into the C1C3 block.
   The assertion requires strict integer fit and at least 3 px of geometric bottom reserve on that
   exact Student page.
   Confirm that the default editor, C1C2 and C1C3 load before reporting case results. Report any
   drop by assertion name and case/role/presentation state. Do not change expected values.
3. Start the editor with `python3 apps/curriculum-editor/serve.py`, open the printed-page preview
   in Chrome, and inspect the accepted C1 Case 02 pilot and the C1 Case 03 expansion in both normal
   and grayscale modes:

   - Student p1, Task 3 horizontal six-stage dependency rail;
   - Answer Key p1, Task 3 completed six-stage rail and Step 2 interruption state;
   - Accessible p2, Task 3 vertical six-stage dependency rail.
   - C1C3 Student p3, Task 6 horizontal five-stage spectral-loss chain;
   - C1C3 Teacher p5 and Answer Key p3 completed five-stage chains;
   - C1C3 Accessible p5 vertical five-stage chain.

4. For every inspected page, report:

   - overflow warning visible: yes/no;
   - clipping or label collision: yes/no;
   - caption or extended-description clipping: yes/no;
   - Student/Answer horizontal rail contains six stages and five connectors: yes/no;
   - Student rail remains blank and writable: yes/no;
   - Answer Key order remains exact and Step 2 alone is `FAILED STEP`: yes/no;
   - Answer Key Steps 3–6 remain `DOWNSTREAM BLOCKED`: yes/no;
   - Accessible rail contains six vertical fields with only the approved first/final prefills:
     yes/no;
   - C1C3 contains five stages and four connectors in every role: yes/no;
   - C1C3 direct stage labels remain `INTAKE`, `FILTER`, `BAND LOSS`, `CHLOROPHYLL`, `OUTCOME`:
     yes/no;
   - C1C3 Student stages 2–5 remain blank and writable: yes/no;
   - C1C3 Teacher/Answer chains retain the exact approved sequence: yes/no;
   - C1C3 Accessible remains vertical with only the approved Step 2 prefill: yes/no;
   - C1C3 Student phrase-bank top margin is 2 px and the process status rail remains .2 in: yes/no;
   - border, pattern and direct status remain distinguishable in grayscale: yes/no;
   - page geometry changed from the declared role/page: yes/no;
   - browser-console JavaScript errors: exact count and text.

5. Run the focused deterministic check and whitespace check:

   ```bash
   python3 shared/validation/validate_sss_visual_mechanism_family.py
   python3 shared/validation/validate_sss_visual_telemetry_family.py
   git diff --check
   ```

Expected focused results: **24/24 mechanism PASS** and **36/36 telemetry PASS**. Return a concise
run report with the exact branch SHA, commands, totals, and any failing page/state. Do not produce
or inspect PDFs.

## Acceptance rule

The C1C3 expansion may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2303/2303 with zero JavaScript errors and every listed page has no overflow, clipping or connector/
status collision in normal and grayscale presentation. The two new assertions must confirm the
computed five-stage chain, direct labels, border states, response identity/content and horizontal/
vertical variants. The accepted C1C2 mechanism and telemetry computed-style assertions must remain
green. C1C3 Student page 3 must also satisfy strict `scrollHeight <= clientHeight` and retain at
least 3 px of real geometric bottom reserve.
