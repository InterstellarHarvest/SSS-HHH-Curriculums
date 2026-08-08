# SSS Visual Modernization Desktop Browser Handoff v1.0

Use this handoff with local Codex or Claude on a machine with installed Google Chrome.
This is a read-only validation run. Do not edit sources, regenerate release baselines, run PDF
automation, or reopen correctness findings.

## Current validation target — C1C7 biological-systems schematic

The current branch tip advances `C1C7-VIS02` to `IMPLEMENTED-CANDIDATE`. It opts The Gift into the
shared-visual layer and applies a bounded biological-system treatment to the existing Student Task 4
page 3, Accessible Task 4 page 4, Teacher reference page 4 and Answer Key Task 4 page 3 models.

The six exact stages and five original connectors remain in their existing horizontal and Accessible
vertical reading order. The existing stage headings directly mark `MATURE NETWORK`, `INCIDENTAL
CUE`, `CARRIER AND PATH`, `POD RECEPTORS`, `COMMITMENT`, and `YOUNG SYMBIOSIS`; the twelve learner
stage/status controls and the approved Accessible Stage 1 source/status prefills remain unchanged.
Solid, dotted, double and dashed borders plus hatch states remain distinguishable in grayscale. No
worksheet content, presentation source, response ID, status value, phrase-bank term, page count,
source hash or release baseline changes.

The accepted executable baseline is 2315/2315. This candidate adds one strict page-fit/geometry
assertion covering all four touched pages in both modes and one computed-style/content assertion
in each of normal and grayscale presentation. Its acceptance target is therefore
**2318/2318 PASS with 0 application JavaScript errors**. The focused mechanism validator target is
**68/68 PASS**.

## Recorded outcome — 2026-08-08

The C1C6 First Contact coordination-system model is `VERIFIED-FAMILY` at
`11a0871d293d4294c72040b0ec9f9e79574704c2`. The browser harness passed 2315/2315 twice with zero
application JavaScript errors. Student page 2, Answer Key page 2 and Accessible page 3 retained
strict `scrollHeight 936 <= clientHeight 936` fit in normal and grayscale presentation. The
mechanism validator passed 60/60. All four direct states, three labeled transitions, exact Student
and Accessible field identities/contents, matching phrase banks and the complete Answer Key
sequence were preserved. Manual inspection found no clipping or collision and retained the
fictional-system boundary. The branch was pushed by normal fast-forward. This recorded outcome
satisfies every condition; C1C6 is no longer an `IMPLEMENTED-CANDIDATE`.

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

   - browser harness: **2318/2318 PASS**;
   - application JavaScript errors: **0**;
   - mechanism validator: **68/68 PASS**;
   - whitespace: clean.

3. Start the editor with `python3 apps/curriculum-editor/serve.py` and inspect only these pages in
   normal and grayscale presentation:

   - C1C7 Student Task 4 page 3;
   - C1C7 Answer Key Task 4 page 3;
   - C1C7 Teacher reference page 4;
   - C1C7 Accessible Task 4 page 4.

4. Report for those pages:

   - overflow warning visible: yes/no;
   - clipping or stage-marker/status/connector collision: yes/no;
   - strict `scrollHeight <= clientHeight`: exact values;
   - fixed page box remains 816 × 1056 and page counts remain Student 6, Answer Key 6, Teacher 8,
     Accessible 8: yes/no;
   - six ordered stages and five original connectors remain: yes/no;
   - horizontal connector order remains `→ | → | → | → | →`: yes/no;
   - Accessible connector order remains `↓ | ↓ | ↓ | ↓ | ↓`: yes/no;
   - learner stage headings remain `MATURE NETWORK | INCIDENTAL CUE | CARRIER AND PATH | POD
     RECEPTORS | COMMITMENT | YOUNG SYMBIOSIS`: yes/no;
   - Student retains all six blank `t4-*` stage fields and all six blank `t4-status-*` controls:
     yes/no;
   - Accessible retains its approved Stage 1 source and `X — MISSING` status prefills while its
     other ten Task 4 controls remain blank and vertical: yes/no;
   - Answer Key and Teacher reference retain their exact six-stage completed models: yes/no;
   - the Student and Accessible phrase banks remain exact and identical: yes/no;
   - the Answer Key retains the mature-source/path unavailability exemplar and downstream
     represented-but-blocked distinction: yes/no;
   - the system remains explicitly fictional and the supported path remains under 3 m: yes/no;
   - no safe dose or complete molecular-structure claim appears: yes/no;
   - pre-commitment reversibility remains distinct from irreversible commitment: yes/no;
   - solid/dotted/double/dashed borders and hatch states remain distinguishable without color:
     yes/no;
   - browser-console JavaScript errors: exact count and text.

Do not run telemetry, repository-wide, legacy mutation, PDF, or unrelated checks. If every check
passes, push the candidate as a normal fast-forward and return the concise report. If anything
fails, hold unpushed and report the exact assertion, role, mode and measurements.

## Acceptance rule

`C1C7-VIS02` may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2318/2318 with zero application JavaScript errors, the focused mechanism validator reaches 68/68,
and the four touched pages retain strict fit, fixed geometry and their existing page counts in
normal and grayscale. The three new assertions must confirm the six-stage order, five connectors,
direct stage markers, grayscale-independent border/pattern states, exact learner response/status
identities and contents, and complete Answer Key and Teacher sequences. Manual inspection must find
no clipping or collision and must preserve the fictional-system, supported-path, safe-dose/structure
and commitment/reversibility limits.
