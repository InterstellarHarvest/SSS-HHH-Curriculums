# SSS Visual Modernization Desktop Browser Handoff v1.0

Use this handoff with local Codex or Claude on a machine with installed Google Chrome.
Correctness remediation is closed. Do not edit worksheet sources, regenerate release baselines,
run PDF automation, or reopen accepted correctness findings.

## Current validation target — C2C2 vibration-release failure path

The isolated `visual/sss-final-modernization` branch is accepted and pushed through closeout commit
`340428094e22598109e0d404f56c037448148437`. The current successor advances `C2C2-VIS02` for The
Missing Dance to `IMPLEMENTED-CANDIDATE`; it must remain unpushed until the browser gate passes.
The accepted executable baseline is **2318/2318 PASS with 0 application JavaScript errors**, and
the accepted focused mechanism baseline is **68/68 PASS**.

The candidate uses the existing five-stage models on Student Task 6 page 5, Answer Key Task 6 page
3 and Accessible Task 6 page 6. It marks the exact path as `SEALED SYSTEM` → `MISSING EVENT` →
`POLLEN RETAINED` → `BUDS ABORT` → `NO FRUIT`, while keeping the two Student and two Accessible
response fields blank and preserving the completed Answer Key. Student and Answer Key remain
horizontal. Accessible becomes a true in-flow vertical rail with four circled down-arrow glyphs.
Solid, dashed, double and dotted borders plus distinct hatch states preserve the causal state
differences in grayscale.

No worksheet content, case presentation, package metadata, response identity, page count, source
hash or release baseline changed. The scientific boundary remains exact: the strongest release
near 124 Hz is insufficient without amplitude, duration and coupling, and an Earth bee gripping a
flower is not the same route as the fictional airborne oscillation coupling into lyreflower tissue.

This candidate adds one strict fit/page-count/geometry assertion across all three pages and both
modes, plus one computed-style/content assertion in normal and one in grayscale. Its acceptance
target is therefore **2321/2321 PASS with 0 application JavaScript errors**. The focused mechanism
validator target is **76/76 PASS**. The formal inventory remains **16 of 36 completed**, with
**20 remaining**, until this candidate is accepted.

## Recorded late-case outcomes — 2026-08-08

### C1C5-VIS01 — Europa radiation-to-growth pathway

`C1C5-VIS01` is `VERIFIED-FAMILY` at
`dcb2d91565769d7bd907b491359ef695a805f784`. Candidate `df1ec0c` passed the complete 2312/2312
browser harness twice with zero application JavaScript errors and retained strict
`scrollHeight 936 <= clientHeight 936` fit on Student page 3, Answer Key page 3 and Accessible page
5 in normal and grayscale. Documentation-only successor `dcb2d91` restored the accepted lifecycle
literal and passed the 52/52 mechanism validator. All seven evidence states, six connectors,
learner fields, phrase banks and the completed Answer Key sequence remained exact. Manual
inspection found no clipping or collision and preserved the distinctions among modeled secondary
radiation, possible exposure and biological evidence consistent with damage.

### C1C6-VIS02 — First Contact coordination-system model

`C1C6-VIS02` is `VERIFIED-FAMILY` at
`11a0871d293d4294c72040b0ec9f9e79574704c2`. Candidate `c9534e4` passed the complete 2315/2315
browser harness twice with zero application JavaScript errors and retained strict
`scrollHeight 936 <= clientHeight 936` fit on Student page 2, Answer Key page 2 and Accessible page
3 in normal and grayscale. Validator-only successor `11a0871` replaced a never-present literal
with both approved correlation caveats and passed the 60/60 mechanism validator without changing
worksheet content or presentation. All four states, three labeled transitions, learner fields,
matching phrase banks and the completed Answer Key sequence remained exact. Manual inspection
found no clipping or collision and preserved the fictional-system and correlation boundaries.

### C1C7-VIS02 — The Gift biological-systems schematic

`C1C7-VIS02` is `VERIFIED-FAMILY` at
`812d5c35d21a3d1e2314e4993faac188b1441c8d`. Candidate `70da06a` passed the complete 2318/2318
browser harness twice with zero application JavaScript errors, the 68/68 mechanism validator and
strict `scrollHeight 936 <= clientHeight 936` fit on Student page 3, Answer Key page 3, Teacher page
4 and Accessible page 4 in normal and grayscale. Manual inspection then found that the following
Accessible stages painted over all five vertical connector glyphs. Corrective successor `812d5c3`
added one Case 07 Accessible `z-index: 1` declaration plus computed-style and static regression
coverage. It passed the complete 2318/2318 browser harness twice, the 68/68 mechanism validator and
manual inspection in both modes. All five circled down-arrow connectors were fully visible, with
computed z-index `1 | 1 | 1 | 1 | 1`, no clipping, overlap or collision, fixed 816 × 1056 geometry,
and unchanged Student 6, Answer Key 6, Teacher 8 and Accessible 8 page counts.

The six ordered stages, five original connectors, learner response/status controls, approved
Accessible Stage 1 prefills, identical learner phrase banks, completed Answer Key and Teacher
models, fictional-system boundary, under-3-m path, safe-dose/structure limitation and
commitment/reversibility distinction all remained exact. No worksheet source, package metadata,
release baseline or accepted content changed.

## Campaign 1 Family 2 closeout register

| Finding | Accepted implementation | Recorded state |
|---|---|---|
| `C1C1-VIS01` | `ceb632d` | `VERIFIED-FAMILY` |
| `C1C2-VIS01` | `a9dfecf` | `VERIFIED-FAMILY-PILOT` |
| `C1C3-VIS03` | `c532ac5` | `VERIFIED-FAMILY` |
| `C1C4-VIS02` | `d5b6c02` | `VERIFIED-FAMILY` |
| `C1C5-VIS01` | `dcb2d91` | `VERIFIED-FAMILY` |
| `C1C6-VIS02` | `11a0871` | `VERIFIED-FAMILY` |
| `C1C7-VIS02` | `812d5c3` | `VERIFIED-FAMILY` |

The accepted Mars expansion at `c532ac5` reached 2303/2303 with zero JavaScript errors and retained
3.47 px of geometric reserve. Together with the six other accepted rows above, this closes the
Campaign 1 mechanism cohort. These lifecycle records do not merge the visual branch to `main`,
declare the overall 11-item Family 2 complete, or reopen frozen curriculum and release decisions.

## Prompt

You are validating the isolated `visual/sss-final-modernization` branch of
`InterstellarHarvest/SSS-HHH-Curriculums`. Correctness remediation and the Campaign 2 release are
frozen.

1. Verify the working tree is clean at the supplied candidate on
   `visual/sss-final-modernization`. Do not reset, rebase, amend, squash, force-push, update frozen
   release baselines, or edit any file.

2. Run only:

   ```bash
   python3 apps/curriculum-editor/tests/run_browser_tests.py \
     --chrome "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

   python3 shared/validation/validate_sss_visual_mechanism_family.py
   git diff --check
   ```

   Expected:

   - browser harness: **2321/2321 PASS**;
   - application JavaScript errors: **0**;
   - mechanism validator: **76/76 PASS**;
   - whitespace: clean.

3. Start the editor with `python3 apps/curriculum-editor/serve.py` and inspect only these pages in
   normal and grayscale presentation:

   - C2C2 Student Task 6 page 5;
   - C2C2 Answer Key Task 6 page 3;
   - C2C2 Accessible Task 6 page 6.

4. Report for those pages:

   - overflow warning visible: yes/no;
   - clipping, collision, hidden connector or status-label overlap: yes/no;
   - strict `scrollHeight <= clientHeight`: exact values;
   - fixed page box remains 816 × 1056 and page counts remain Student 6, Answer Key 4 and
     Accessible 8: yes/no;
   - five ordered stages and four connectors remain: yes/no;
   - Student and Answer Key connector order remains `→ | → | → | →`: yes/no;
   - Accessible shows four completely visible circled `↓` connectors in the vertical flow: yes/no;
   - direct state order is `SEALED SYSTEM | MISSING EVENT | POLLEN RETAINED | BUDS ABORT | NO
     FRUIT`: yes/no;
   - border order is `solid | dashed | double | dotted | double` and all hatch states remain
     visible without color: yes/no;
   - Student retains blank `t6-m3` and `t6-m4`; Accessible retains blank `a6-m3` and `a6-m4`:
     yes/no;
   - Answer Key retains the exact completed five-stage model: yes/no;
   - Stage 2 remains an absent vibration event rather than a missing substance, closed pore or
     broken structure: yes/no;
   - near 124 Hz remains insufficient without amplitude, duration and coupling: yes/no;
   - Earth bee gripping remains distinct from fictional airborne coupling: yes/no;
   - browser-console JavaScript errors: exact count and text.

Do not run telemetry, repository-wide, legacy mutation, PDF, or unrelated checks. If every check
passes, push the candidate as a normal fast-forward and return the concise report. If anything
fails, hold unpushed and report the exact assertion, role, mode and measurements.

## Acceptance rule

`C2C2-VIS02` may advance from `IMPLEMENTED-CANDIDATE` only when the browser harness reaches
2321/2321 with zero application JavaScript errors, the focused mechanism validator reaches 76/76,
and all three touched pages retain strict fit, fixed geometry and existing page counts in normal
and grayscale. Manual inspection must confirm the vertical Accessible connectors and every status
label are completely visible, fields and completed content are unchanged, the distinctions survive
grayscale, and the frequency/coupling/Earth-comparison boundaries remain intact. Until then,
`C2C3-VIS03`, `C2C5-VIS03` and `C2C6-VIS02` remain the only other open Family 2 findings.
