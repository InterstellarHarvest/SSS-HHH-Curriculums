# SSS Visual Modernization Desktop Browser Handoff v1.0

Use this handoff with local Codex or Claude on a machine with installed Google Chrome.
This is a read-only validation run. Do not edit sources, regenerate release baselines, run PDF
automation, or reopen correctness findings.

## Current validation target — C1C4 closed reactor fault loop

The current branch tip advances `C1C4-VIS02` to `IMPLEMENTED-CANDIDATE`. It opts Hayes Orbital
Station into the shared-visual layer and turns the existing Student Task 5 page 3, Accessible
Task 5 page 5 and Answer Key Task 5 page 3 process models into an immediate closed fault loop.
The existing two-row snake and Accessible vertical reading order remain intact. A direct
`REPEAT TO STAGE 1` rail closes Stage 6 back to Stage 1; the horizontal Student/Answer models add
the direct states `EXPOSURE`, `LOAD`, `DAMAGE`, `DECLINE`, `REBUILD`, and `RECURRENCE`. Solid,
double and dashed borders plus hatch states preserve meaning in grayscale. No package-controlled
content or presentation source, response ID, approved Accessible prefill, phrase-bank term, page
count, source hash or release baseline changes.

The accepted executable baseline is 2306/2306. This candidate adds three browser assertions:
one strict page-fit assertion covering all three touched pages in both modes and one computed-
style/content assertion in each of normal and grayscale presentation. Its acceptance target is
therefore **2309/2309 PASS with 0 application JavaScript errors**. The focused mechanism validator
target is **44/44 PASS**; telemetry remains **36/36 PASS**.

Candidate `f14355b` was held unpushed after two identical 2307/2309 runs. Its only computed-style
failure was a harness extraction defect: Answer Key stage numbers and bodies were read as fused DOM
text although all six approved body strings were exact. Manual inspection also found the circular
border crossing the Accessible connector's existing `↓ then repeat` label. This corrective
successor reads each body element directly, changes only that labeled connector to a padded 3 px
rounded rectangle, and requires its computed radius, padding and internal fit in both modes. The
acceptance target remains 2309/2309; no expected content, worksheet source or baseline changed.

## Recorded outcome — 2026-08-08

The C1C1 ISS gravity-sensing expansion is `VERIFIED-FAMILY` at
`ceb632dadb9461cae81086021b0727c2a2efad6a`. The browser harness passed 2306/2306 twice with zero
application JavaScript errors. Student page 2, Answer Key page 2 and Accessible page 3 each
measured strict `scrollHeight 884 <= clientHeight 884` fit in normal and grayscale presentation.
The mechanism validator passed 35/35, telemetry passed 36/36, both deterministic cutaway rails and
all original response identities/prefills remained exact, and accepted C1C2/C1C3 assertions stayed
green. The Earth status arrow wraps beneath `SETTLED · CUE` in the narrow rail but is fully visible,
unclipped and exact; the accepted cosmetic line break requires no product correction. The branch
was pushed by normal fast-forward. This recorded outcome satisfies the acceptance rule below;
C1C1 is no longer an `IMPLEMENTED-CANDIDATE`.

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

   The current executable browser target is **2309/2309 PASS with 0 JavaScript errors**. The
   accepted branch state before this candidate produces 2306/2306. The C1C4 expansion adds one
   strict-fit assertion for Student page 3, Accessible page 5 and Answer Key page 3 in both modes,
   plus two normal/grayscale computed-style assertions. Those assertions require six ordered
   stages, five existing connectors, a direct `REPEAT TO STAGE 1` link, horizontal direct-state
   labels, solid/double/dashed borders, exact response identities and the approved Accessible
   Stage 2 prefill. They also require the Answer Key's six exact completed stages to remain exact.
   The labeled Accessible `↓ then repeat` connector must have a computed corner radius no greater
   than 4 px, at least 4 px left/right padding, and `scrollWidth <= clientWidth` plus
   `scrollHeight <= clientHeight`; its border must not cross the label.

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
   Confirm that the default editor, C1C1, C1C2 and C1C3 load before reporting case results. Report any
   drop by assertion name and case/role/presentation state. Do not change expected values.
3. Start the editor with `python3 apps/curriculum-editor/serve.py`, open the printed-page preview
   in Chrome, and inspect the current C1 Case 04 expansion in both normal and grayscale modes:

   - C1C4 Student p3, Task 5 two-row closed loop with five blank fields;
   - C1C4 Answer Key p3, Task 5 completed two-row closed loop;
   - C1C4 Accessible p5, Task 5 vertical loop with only the approved Stage 2 prefill.

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
   - C1C4 contains six ordered stages and five connectors in every synchronized edition: yes/no;
   - direct `REPEAT TO STAGE 1` closure is visible and connected to the Stage 6 recurrence: yes/no;
   - horizontal direct states remain `EXPOSURE`, `LOAD`, `DAMAGE`, `DECLINE`, `REBUILD`, and
     `RECURRENCE`: yes/no;
   - C1C4 Student retains five blank fields with the original response IDs: yes/no;
   - C1C4 Accessible remains vertical and retains only its approved Stage 2 prefill: yes/no;
   - C1C4 Answer Key retains all six exact completed stages: yes/no;
   - Answer commentary retains the qualitative-only boundary and prohibits invented density,
     photon-total and mission-day values: yes/no;
   - C1C4 loop states remain distinguishable without color: yes/no;
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

Expected focused results: **44/44 mechanism PASS** and **36/36 telemetry PASS**. Return a concise
run report with the exact branch SHA, commands, totals, and any failing page/state. Do not produce
or inspect PDFs.

## Acceptance rule

The C1C4 expansion may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2309/2309 with zero application JavaScript errors and the three touched pages have strict
`scrollHeight <= clientHeight` fit with no overflow, clipping or repeat-label/connector collision in
normal and grayscale presentation. The three new assertions must confirm the six-stage order, five
existing connectors, direct loop closure, horizontal state labels, border/pattern distinctions,
exact Student/Accessible response identities and contents, complete Answer Key sequence and
unchanged approved page geometry. The accepted C1C1/C1C2/C1C3 mechanism and telemetry assertions
must remain green.

The earlier C1C1 expansion could advance from `IMPLEMENTED-CANDIDATE` only when the browser harness
reached 2306/2306 with zero application JavaScript errors and its three touched pages retained
strict 884/884 fit with no overflow, clipping or label/cutaway collision in normal and grayscale.
Its three assertions confirmed the two SVG rails, direct status, solid/double distinction, exact
Student/Accessible fields and contents, complete Answer Key pathways and unchanged geometry. The
recorded outcome above satisfies every condition.

The earlier C1C3 expansion could advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reached
2303/2303 with zero JavaScript errors and every listed page had no overflow, clipping or connector/
status collision in normal and grayscale presentation. Its two assertions confirm the
computed five-stage chain, direct labels, border states, response identity/content and horizontal/
vertical variants. The accepted C1C2 mechanism and telemetry computed-style assertions must remain
green. C1C3 Student page 3 must also satisfy strict `scrollHeight <= clientHeight` and retain at
least 3 px of real geometric bottom reserve. The recorded outcome above satisfies every condition.
