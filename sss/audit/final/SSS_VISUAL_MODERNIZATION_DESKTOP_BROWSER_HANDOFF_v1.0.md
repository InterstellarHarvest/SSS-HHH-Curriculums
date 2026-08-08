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

   The current executable browser target is **2298/2298 PASS with 0 JavaScript errors**. The
   accepted correctness commit produces 2293/2293; this branch adds five computed-style assertions
   for the visual-delivery defects exposed by the `71e555d` desktop run. Report any drop by
   assertion name and case/role/presentation state. Do not change expected values.
3. Start the editor with `python3 apps/curriculum-editor/serve.py`, open the printed-page preview
   in Chrome, and inspect these telemetry-family candidates in both normal and grayscale modes:

   - C1 Case 03 optical scan: Student p1, Teacher p4, Answer Key p2, Accessible p2;
   - C1 Case 03 quantity-versus-spectrum: Student p2, Answer Key p1, Accessible p3;
   - C2 Case 01: Teacher p4;
   - C2 Case 03: Student pp2–3 and Accessible pp2–3;
   - C2 Case 04 within-cycle record: Student p3, Accessible p3, and the Answer Key p1 summary;
   - C2 Case 05: Student pp2–3 and Accessible pp2–3;
   - C2 Case 06: Student p2 and Accessible p2.

4. For every inspected page, report:

   - overflow warning visible: yes/no;
   - clipping or label collision: yes/no;
   - caption or extended-description clipping: yes/no;
   - figure-status chip collision in C1C3/C2C3: yes/no;
   - C1C3 dual-channel badges visibly state `QUANTITY ≠ DISTRIBUTION` and `UNEVEN`: yes/no;
   - C2C4 light/dark patterns and reported/unreported border states remain distinct without a
     connecting curve: yes/no;
   - grayscale patterns and direct labels distinguish every category: yes/no;
   - page geometry changed from the declared role/page: yes/no;
   - browser-console JavaScript errors: exact count and text.

5. Run the focused deterministic check and whitespace check:

   ```bash
   python3 shared/validation/validate_sss_visual_telemetry_family.py
   git diff --check
   ```

Expected focused result: **35/35 PASS**. Return a concise run report with the exact branch SHA,
commands, totals, and any failing page/state. Do not produce or inspect PDFs.

## Acceptance rule

The family pilot may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2298/2298 with zero JavaScript errors and every listed page has no overflow, clipping, or status
collision in normal and grayscale presentation. The five new browser assertions must confirm the
C1C3 pseudo-content, C2C3 compact computed padding/page fit, and C2C4 computed pattern/border states.
