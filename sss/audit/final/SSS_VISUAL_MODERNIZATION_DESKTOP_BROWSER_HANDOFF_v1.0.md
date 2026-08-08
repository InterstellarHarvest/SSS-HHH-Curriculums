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

   The current executable browser target is **2300/2300 PASS with 0 JavaScript errors**. The
   accepted telemetry-family baseline `bee63f5` produces 2298/2298. This mechanism pilot adds two
   computed-style assertions, one for normal and one for grayscale presentation, covering the
   horizontal dependency rail, the Answer Key interruption state and the Accessible vertical rail.
   Confirm that the default editor, C1C2 and C1C3 load before reporting case results. Report any
   drop by assertion name and case/role/presentation state. Do not change expected values.
3. Start the editor with `python3 apps/curriculum-editor/serve.py`, open the printed-page preview
   in Chrome, and inspect the C1 Case 02 mechanism pilot in both normal and grayscale modes:

   - Student p1, Task 3 horizontal six-stage dependency rail;
   - Answer Key p1, Task 3 completed six-stage rail and Step 2 interruption state;
   - Accessible p2, Task 3 vertical six-stage dependency rail.

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
   - border, pattern and direct status remain distinguishable in grayscale: yes/no;
   - page geometry changed from the declared role/page: yes/no;
   - browser-console JavaScript errors: exact count and text.

5. Run the focused deterministic check and whitespace check:

   ```bash
   python3 shared/validation/validate_sss_visual_mechanism_family.py
   python3 shared/validation/validate_sss_visual_telemetry_family.py
   git diff --check
   ```

Expected focused results: **14/14 mechanism PASS** and **36/36 telemetry PASS**. Return a concise
run report with the exact branch SHA, commands, totals, and any failing page/state. Do not produce
or inspect PDFs.

## Acceptance rule

The mechanism pilot may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2300/2300 with zero JavaScript errors and every listed page has no overflow, clipping or connector/
status collision in normal and grayscale presentation. The two new assertions must confirm the
computed horizontal and vertical rails plus the completed Step 2 interruption state. The five
accepted telemetry computed-style assertions must remain green.
