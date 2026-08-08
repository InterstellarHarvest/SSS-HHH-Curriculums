# SSS Visual Modernization Desktop Browser Handoff v1.0

Use this handoff with local Codex or Claude on a machine with installed Google Chrome.
This is a read-only validation run. Do not edit sources, regenerate release baselines, run PDF
automation, or reopen correctness findings.

## Current validation target — C1C1 gravity-sensing cutaways

The current branch tip advances `C1C1-VIS01` to `IMPLEMENTED-CANDIDATE`. It opts ISS Greenhouse
into the extracted shared-visual layer and adds narrow deterministic SVG cutaway rails to the
existing Student Task 5 page 2, Accessible Task 5 page 3 and Answer Key Task 5 page 2 pathways.
The Earth rail shows settled statoliths, one stable downward cue and downward root growth; the
microgravity rail shows dispersed statoliths, no single stable cue and a curved root path. Direct
status text, solid/double borders and a dashed unreliable-cue marker preserve meaning in
grayscale. No package-controlled content or presentation source, response ID, approved prefill,
word-bank term, page count, source hash or release baseline changes.

The accepted executable baseline is 2303/2303. This candidate adds three browser assertions:
one strict page-fit assertion covering all three touched pages and one computed-style/content
assertion in each of normal and grayscale presentation. Its acceptance target is therefore
**2306/2306 PASS with 0 application JavaScript errors**. The focused mechanism validator target
is **35/35 PASS**; telemetry remains **36/36 PASS**.

## Recorded outcome — 2026-08-08

The C1C3 Mars mechanism expansion is `VERIFIED-FAMILY` at
`c532ac5246a72ef4b9f06d985b3d5c60be92cfde`. The browser harness passed 2303/2303 twice with
zero application JavaScript errors. The strict-fit assertion measured `scrollHeight 936 <=
clientHeight 936` and 3.47 px of geometric bottom reserve. The mechanism validator passed 25/25,
the telemetry validator passed 36/36, normal and grayscale inspection passed, and the accepted
C1C2 rendering remained unchanged. The branch was pushed by normal fast-forward. This recorded
outcome satisfies the acceptance rule below; the expansion is no longer an
`IMPLEMENTED-CANDIDATE`.

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

   The current executable browser target is **2306/2306 PASS with 0 JavaScript errors**. The
   accepted branch state before this candidate produces 2303/2303. The C1C1 expansion adds one
   strict-fit assertion for Student page 2, Accessible page 3 and Answer Key page 2 plus two
   normal/grayscale computed-style assertions. Those assertions require two deterministic SVG
   rails in every synchronized edition, `SETTLED · CUE ↓` versus `NO STABLE CUE` direct status,
   solid versus double left borders, exact response identities and approved Accessible prefills.
   They also require the Answer Key's two complete pathways to remain exact.

   Historical context: the accepted mechanism-family pilot `a9dfecf` produces 2300/2300. The
   later C1C3 expansion added two computed-style assertions, one for normal and one for grayscale
   presentation, covering the five-stage spectral-loss chain in Student, Teacher, Answer Key and
   Accessible roles.
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
   exact Student page. Candidate `a960018` achieved that fit (`936 <= 936`, 3.47 px reserve) but was
   rejected at 2302/2303 because relocating the assertion also moved C1C2's terminal Student/normal
   state reset. This successor restores the reset at the end of C1C2 while retaining the independent
   reset at the start of C1C3.
   Confirm that the default editor, C1C2 and C1C3 load before reporting case results. Report any
   drop by assertion name and case/role/presentation state. Do not change expected values.
3. Start the editor with `python3 apps/curriculum-editor/serve.py`, open the printed-page preview
   in Chrome, and inspect the current C1 Case 01 expansion in both normal and grayscale modes:

   - C1C1 Student p2, Task 5 matched Earth/microgravity cutaways and four blank fields;
   - C1C1 Answer Key p2, Task 5 matched completed cutaways;
   - C1C1 Accessible p3, Task 5 matched cutaways with only the approved Earth-side prefills.

   The full harness must also keep the accepted C1 Case 02 and C1 Case 03 mechanism assertions
   green. Their reference pages are:

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
   - C1C1 contains two SVG cutaway rails in every synchronized edition: yes/no;
   - Earth shows settled statoliths, a stable downward cue and downward root outcome: yes/no;
   - Microgravity shows dispersed statoliths, no single stable cue and curved root outcome: yes/no;
   - C1C1 direct statuses remain `SETTLED · CUE ↓` and `NO STABLE CUE`: yes/no;
   - C1C1 Student retains four blank fields with the original response IDs: yes/no;
   - C1C1 Accessible retains `settle` and `downward` only as its approved Earth prefills: yes/no;
   - C1C1 Answer Key retains both exact completed pathways and the accuracy note: yes/no;
   - C1C1 card states remain distinguishable without color: yes/no;
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

Expected focused results: **35/35 mechanism PASS** and **36/36 telemetry PASS**. Return a concise
run report with the exact branch SHA, commands, totals, and any failing page/state. Do not produce
or inspect PDFs.

## Acceptance rule

The C1C1 expansion may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2306/2306 with zero application JavaScript errors and the three touched pages have strict
`scrollHeight <= clientHeight` fit with no overflow, clipping or label/cutaway collision in normal
and grayscale presentation. The three new assertions must confirm the two SVG rails, direct status,
solid/double state distinction, exact Student/Accessible response identities and contents, complete
Answer Key pathways and unchanged approved page geometry. The accepted C1C2/C1C3 mechanism and
telemetry assertions must remain green.

The earlier C1C3 expansion could advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reached
2303/2303 with zero JavaScript errors and every listed page had no overflow, clipping or connector/
status collision in normal and grayscale presentation. Its two assertions confirm the
computed five-stage chain, direct labels, border states, response identity/content and horizontal/
vertical variants. The accepted C1C2 mechanism and telemetry computed-style assertions must remain
green. C1C3 Student page 3 must also satisfy strict `scrollHeight <= clientHeight` and retain at
least 3 px of real geometric bottom reserve. The recorded outcome above satisfies every condition.
