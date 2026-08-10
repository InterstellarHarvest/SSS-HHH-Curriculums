# SSS Final Visual Modernization Plan v1.0

**Status:** `APPROVED-BASELINE-BOUND · PRODUCTION-IN-PROGRESS`  
**Prepared:** 2026-08-07  
**Correctness authority:** `5844b56fd10e4be068dc9049f6a743cd473de805`  
**Working branch:** `visual/sss-final-modernization`  
**Scope:** SSS Campaign 1 Cases 01–07 and Campaign 2 Cases 01–06  
**PDF/physical print:** `OWNER-MANUAL` — excluded from automated production and validation

## 1. Phase boundary

The correctness/remediation phase is closed. This plan does not reopen curriculum content,
Teacher pagination, Accessible adaptation, Answer Key reconciliation, lifecycle, or release
baseline decisions. Visual changes must preserve all accepted prompts, task order, response
controls and persistence IDs, scientific conclusions and qualifications, package structure,
fixed Letter geometry, and the owner-accepted eight-page C1 Case 01 and nine-page C2 Case 01
Teacher Editions.

Only a new regression introduced by this branch may reopen a correctness question.

## 2. Repository and branch verification

Verification on 2026-08-07 established:

| Ref | SHA | Disposition |
|---|---|---|
| accepted correctness candidate | `5844b56fd10e4be068dc9049f6a743cd473de805` | exists locally |
| `origin/remediate/sss-final-system` | `5844b56fd10e4be068dc9049f6a743cd473de805` | exact match; no later commits |
| `origin/main` | `f7a24423f802a095aa149f923d05475ba2837599` | untouched |
| visual worktree start | `5844b56fd10e4be068dc9049f6a743cd473de805` | clean |

The visual branch is isolated in a separate worktree. It must remain a descendant of the
accepted correctness candidate. No rebase, amend, force-push, direct main merge, or rewrite
of PR #1 history is permitted. Production commits are organized by plan, shared/family
foundation, family implementation, and final cross-case regression. Main integration requires
separate owner authorization.

Rendered-gate history is preserved rather than overwritten: `2a04e14` passed 2293/2293 and is
the last accepted browser checkpoint; `71e555d` was rejected at 2291/2293 because C2C3 page fit
regressed and the new C1C3/C2C4 selectors produced no rendered treatment. The remediation after
that rejection added five computed-style browser assertions. Its first candidate, `8e27e61`, was
also rejected because its C1C3 visual-CSS start constant did not match the real multiline comment,
blocking the default editor boot before case assertions ran. The successor uses explicit extraction
sentinels and a deterministic check that the JavaScript constants delimit the real CSS payload. Its
browser acceptance target remains 2298/2298. The accepted mechanism pilot `a9dfecf` subsequently
passed 2300/2300. The first Mars expansion candidate, `7ec465e`, was rejected at 2295/2302 because
its visual chain enlarged C1C3 Student page 3 by 7 px; all new mechanism assertions passed, but the
page-fit failure cascaded into seven harness failures. Its successor preserves the approved 2.25 in
stage-writing height and compacts only the new Student-page status rail and vertical margins. That
successor passed 2302/2302 and the application tolerance but was held because its sole target page
still rounded to `scrollHeight 937 > clientHeight 936`, with only 0.531 px of geometric overflow.
Candidate `b429fb4` was rejected at 2302/2303: reducing the process margin was a rendered no-op
because both adjacent margins collapsed to larger neighboring values, and its strict-fit assertion
was mistakenly placed in the C1C2 block, where the Mars page did not exist. The next successor
reduces the dominant Student-page phrase-bank top margin from 6 px to 2 px, retains the paired 1 px
process margin, relocates the executable assertion into the C1C3 block and strengthens the focused
validator to check that structural placement. Candidate `a960018` proved the page fit at 2302/2303
with `936 <= 936` and 3.47 px of geometric reserve, but was rejected because relocating the block
also moved C1C2's terminal Student/normal state reset into C1C3. The next successor restores that
terminal C1C2 reset while retaining C1C3's independent initialization, with a focused structural
check for both block-local resets. Candidate `c532ac5` passed the complete 2303/2303 browser
harness twice with zero application JavaScript errors, retained strict `936 <= 936` fit and
3.47 px of geometric bottom reserve, passed the 25/25 mechanism and 36/36 telemetry focused
validators, and was accepted and pushed at
`c532ac5246a72ef4b9f06d985b3d5c60be92cfde`. The Mars expansion is therefore promoted to
`VERIFIED-FAMILY`. The ISS Family 2 expansion at `ceb632d` subsequently passed the complete
2306/2306 browser harness twice with zero application JavaScript errors, retained strict 884/884
fit on Student page 2, Accessible page 3 and Answer Key page 2, and passed the 35/35 mechanism and
36/36 telemetry validators. Normal and grayscale manual inspection found no overflow, clipping or
collision. The Earth status arrow wraps beneath `SETTLED · CUE` in the narrow rail but remains fully
visible and exact; this accepted cosmetic line break does not reopen the candidate. `C1C1-VIS01`
is therefore `VERIFIED-FAMILY`. The next Family 2 candidate is `C1C4-VIS02`: the existing Hayes
six-stage snake and Accessible vertical sequence receive direct `REPEAT TO STAGE 1` closure rails,
stage-state labels and grayscale-independent border/pattern states without changing worksheet
content, response identities, phrase banks or package-controlled source hashes. It remains
`IMPLEMENTED-CANDIDATE` until the 2309-assertion rendered gate confirms both presentation modes and
strict page fit. A green source-token validator alone cannot promote a visual candidate.
Candidate `f14355b` was rejected deterministically at 2307/2309: the new Answer Key assertion read
each stage number and body as fused DOM text even though the approved stage bodies were exact, and
the Accessible Stage 5 connector's circular border crossed its existing `↓ then repeat` label in
normal and grayscale. The corrective successor reads the stage body element directly, gives only
that labeled connector a padded 3 px rounded-rectangle border, and makes the rendered contract
require the label's radius, padding and internal fit. No worksheet content or package-controlled
source changes. Corrective candidate `d5b6c02` then passed the complete 2309/2309 browser harness
twice with zero application JavaScript errors, retained strict 936/936 fit on Student page 3,
Accessible page 5 and Answer Key page 3 in both modes, and passed the 44/44 mechanism validator.
Manual inspection confirmed that the labeled Accessible connector no longer collided with its
border. `C1C4-VIS02` is therefore `VERIFIED-FAMILY`. The next Family 2 candidate is `C1C5-VIS01`:
Europa's existing seven-stage Student, Accessible and Answer Key pathway receives direct evidence-
status labels and grayscale-independent border/pattern states without changing worksheet content,
response identities, approved Accessible prefills, phrase banks or package-controlled source hashes.
Candidate `df1ec0c` passed the complete 2312/2312 browser harness twice with zero application
JavaScript errors and retained strict 936/936 fit on Student page 3, Accessible page 5 and Answer
Key page 3 in both modes. Its sole static failure was a capitalization mismatch in a historical
handoff sentence; documentation-only successor `dcb2d91` restored that accepted literal and passed
the 52/52 mechanism validator without changing any rendered or package-controlled source.
`C1C5-VIS01` is therefore `VERIFIED-FAMILY`. The next Family 2 candidate is `C1C6-VIS02`: First
Contact's existing four-stage Student, Accessible and Answer Key coordination model receives a
bounded system rail, direct state markers, labeled transitions and grayscale-independent
border/pattern states without changing worksheet content, response identities, phrase banks or
package-controlled source hashes. Candidate `c9534e4` passed the complete 2315/2315 browser
harness twice with zero application JavaScript errors and retained strict 936/936 fit on Student
page 2, Accessible page 3 and Answer Key page 2 in both modes. Its sole static failure was a new
literal that did not match either approved correlation caveat; validator-only successor `11a0871`
required both approved source statements and passed the 60/60 mechanism validator without changing
worksheet content, presentation or browser behavior. `C1C6-VIS02` is therefore `VERIFIED-FAMILY`.
The final Campaign 1 Family 2 candidate is `C1C7-VIS02`: The Gift's existing six-stage Student,
Accessible, Teacher and Answer Key source-to-symbiosis models receive a bounded biological-system
rail, direct stage markers, emphasized supply/status controls and grayscale-independent
border/pattern states without changing worksheet content, response identities, approved Accessible
prefills, phrase banks or package-controlled source hashes. Candidate `70da06a` passed the complete
2318/2318 browser harness twice with zero application JavaScript errors, retained strict 936/936
fit and fixed 816 × 1056 geometry on Student page 3, Accessible page 4, Teacher page 4 and Answer
Key page 3 in both modes, and passed the 68/68 mechanism validator. Manual inspection identified
one real Accessible paint-order defect: all five vertical connector glyphs were occluded by the
following stage. Corrective successor `812d5c3` lifted only those five Case 07 Accessible connector
badges, added computed-style and static regression coverage, and then passed the complete 2318/2318
browser harness twice, the 68/68 mechanism validator and normal/grayscale manual inspection with
all five circled down-arrow glyphs visible. Worksheet sources, package metadata, page counts,
response controls and release baselines remained unchanged. `C1C7-VIS02` is therefore
`VERIFIED-FAMILY`.

Campaign 1's Family 2 cohort is closed: all seven Campaign 1 mechanism/pathway findings are
verified. Campaign 2's four Family 2 findings are also verified, so the complete 11-finding
mechanism/pathway family is closed. The formal visual-modernization inventory now stands at 20 of
36 completed findings, with 16 remaining.

`C2C2-VIS02` modernizes The Missing Dance's frozen Student Task 6 page 5, Answer Key Task 6 page 3
and Accessible Task 6 page 6 as one exact five-stage failure path. Candidate `132161a` passed the
complete 2321/2321 browser harness twice with zero application JavaScript errors and retained
strict 936/936 fit, fixed 816 × 1056 geometry, existing page counts, all four fully visible
Accessible connector glyphs, the two blank Student and two blank Accessible response identities,
and the completed Answer Key in normal and grayscale. Its sole static failure was a handoff line
wrap that split a required lifecycle literal. Documentation/validator successor `aa4eeac`
normalized handoff whitespace, passed the 76/76 mechanism validator, and changed no implementation
or curriculum source. The missing vibration event, near-124-Hz insufficiency and Earth-bee-versus-
airborne-coupling boundaries remained exact. `C2C2-VIS02` is therefore `VERIFIED-FAMILY`.

`C2C3-VIS03` modernizes Wrong Color of Light's related Task 6 mechanism and Task 8 specification
panels without merging their tasks or pages. Candidate `79a7c80` passed the complete 2324/2324
browser harness twice with zero application JavaScript errors, the 85/85 focused mechanism
validator and normal/grayscale inspection of all six touched pages. It retained strict 936/936
fit, fixed 816 × 1056 geometry, Student 5 / Answer Key 4 / Accessible 8 page counts, all response
geometry and blank learner fields, and the exact completed Answer Key. The five direct Task 6
states and four connectors remained fully visible, while Task 8 retained the related spectrum,
intensity, constraint and monitored-trial grammar. Total PAR 280 remained adequate; every discrete
spectral value and band remained exact; response outside 460–540 nm remained unspecified; and the
recovery statement remained a trial prediction rather than a result. Worksheet content, case
presentation, package metadata, source hashes and release baselines remained unchanged.
`C2C3-VIS03` is therefore `VERIFIED-FAMILY`.

`C2C5-VIS03` modernizes Too Clean a Room's species-specific signal-to-product mechanism paired with
its separate high-level trial workflow. The frozen
five-stage Student and Accessible models now share direct `SHIELDED READING` → `SIGNAL TOO LOW` →
`PATHWAY QUIESCENT` → `PRODUCT NOT MADE` → `OBSERVED DECLINE` states; Accessible becomes the
standard in-flow vertical rail without changing its approved Stage 3 scaffold. The separate Task 7
table now presents the existing authorization, comparison, measurement, containment, staging and
stop requirements as six ordered safety gates, while the five existing learner responses and
completed Answer Key remain exact. No worksheet source, case presentation, package metadata,
response identity, layout override, page count or release baseline changes. Held candidate
`41a83e9fa1bea3864a3008571a604c5c637512c6` reached 2321/2327 twice: Accessible Task 5 page 5
overflowed by 93 px and four Task 7 label borders were targeted in the wrong sibling direction.
Ordinary corrective successor `7be2f428dfe41a3247794662ca9d1f4ef5362d2e` compacts only
vertical-rail and surrounding panel chrome while preserving full-width 48 px source response
minimums, and retargets the frozen direct-label order. It passed the complete 2327/2327 browser
harness twice with zero application JavaScript errors, the 94/94 focused mechanism validator and
normal/grayscale inspection of all six touched pages. All pages retained strict 936/936 fit, fixed
816 × 1056 geometry, Student 7 / Answer Key 5 / Accessible 7 page counts and zero content-boundary
spill. The four Accessible Task 5 connectors were reduced locally from 15 px to 11 px to preserve
fit; all remained clearly visible, circled, in flow and topmost, with no response-space reduction.
All five mechanism states, six safety gates, blank learner fields, completed Answer Key rows and
scientific/safety boundaries remained exact. `C2C5-VIS03` is therefore `VERIFIED-FAMILY`.

`C2C6-VIS02` modernizes The First Garden's frozen Task 5 candidate pathway across Student page 5,
Accessible page 5 and Answer Key page 4. The existing five stages now carry the direct states
`CONSTRUCTION HISTORY` → `POSSIBLE PARTNER LOSS` → `FEWER PARTNERSHIPS` →
`LESS ASSISTED ACQUISITION` → `SURVEYED PATTERN`, while one persistent
`CANDIDATE · NOT ESTABLISHED` rail remains visible across the whole explanation. Student remains
horizontal; Accessible becomes the established in-flow vertical rail; and the Answer Key's three
completed rows receive the matching dashed, dotted and double state treatment. The two fixed
endpoints, three blank fields in each learner edition, exact edition-specific phrase banks, both
blank model-limit responses and the verbatim completed Answer Key remain unchanged. No worksheet
content, case presentation, package metadata, persistence identity, layout override, page count,
source hash or release baseline changes. Candidate
`d8886b539e328fd3e9dcb9cdaa1bd4e16aaf6a54` passed the complete 2330/2330 Mac/Chrome browser
harness twice with zero application JavaScript errors, the 103/103 focused mechanism validator,
the 36/36 telemetry validator and the Case 06 layout-override validator. Normal and grayscale
inspection confirmed strict 936/936 fit, fixed 816 × 1056 geometry, unchanged Student 6 / Answer
Key 5 / Accessible 7 page counts and zero content-boundary spill on all three touched pages. All
four 15 × 15 Accessible connectors remained visible, circled, in flow and topmost; all eight
learner fields retained their source-controlled geometry and blank state; and the candidate,
survey and ecological-safety boundaries remained exact. `C2C6-VIS02` is therefore
`VERIFIED-FAMILY`, closing Family 2.

`C1C4-VIS01` begins Family 3 by modernizing Hayes Orbital Station's frozen Task 2 relative-event
organizer on Student page 1, Accessible page 2 and Answer Key page 1. The five existing positions
now read as one `SAA INCIDENT LOG · RELATIVE SEQUENCE` with the direct event-type states
`BASELINE` → `CHANGE` → `FIRST FAILURE` → `REPEAT` → `RECOVERY`. Student and Answer Key remain
horizontal with four right-arrow connectors. Accessible remains one in-flow vertical reading
sequence and gains four grayscale-safe down-arrow connectors without adding response controls.
All five Student fields, all five Accessible fields, both exact event banks and the completed
Answer Key sequence remain unchanged. The visual spacing is deliberately equal: no mission days,
proportional distances or new timing precision are introduced. No worksheet content, case
presentation, layout override, package metadata, task registry, page count, persistence identity,
source hash or release baseline changes. Candidate
`d5ffe37c0db952fb74c51c961d5b58bb405f01ea` passed the complete 2333/2333 Mac/Chrome browser
harness twice with zero application JavaScript errors, the 17/17 focused timeline validator, the
103/103 mechanism validator, the 36/36 telemetry validator and the Case 04 layout-override
validator. Normal and grayscale inspection confirmed strict 936/936 fit, fixed 816 × 1056
geometry, unchanged Student 4 / Answer Key 4 / Accessible 7 page counts and zero content-boundary
spill on all three touched pages. All connectors, state labels, patterns and borders remained
visible and collision-free; all ten learner fields retained their source-controlled geometry and
blank state; and the relative-timing, reactor-specific and correlation boundaries remained exact.
`C1C4-VIS01` is therefore `VERIFIED-FAMILY`, the first accepted Family 3 finding.

`C1C6-VIS01` is the second accepted Family 3 finding. It modernizes First Contact Protocol's
frozen Task 3 timing strips on Student page 2 and Accessible page 2 as one compact reported-event
telemetry grammar. Both learner displays retain the exact `72.4 hours ago` docking event, the
exact `72.1 hours ago` last-signal event and the exact 18-minute interval. Student also retains the qualitative
first post-docking cycle observation and its separate connector. The case-scoped shared layer adds
the persistent rail `SAA EVENT TELEMETRY · REPORTED ORDER · NOT TO SCALE`, the direct states
`DOCKING EVENT`, `LAST SIGNAL` and `FIRST-CYCLE OBSERVATION`, distinct border/pattern states and an
interval capsule. It adds no axis, tick, curve, scaled distance, new timing value, learner response
or causal conclusion. Larger “hours ago” remains earlier; 0.3 hours remains exactly 18 minutes;
timing remains correlation rather than proof; and the approved converging evidence remains
necessary. No worksheet content, case presentation, layout override, package metadata, task
registry, page count, persistence identity, source hash or release baseline changes. Candidate
`66a3d1b76077201cbd438f2b70b64e4a1380d7a2` passed the complete 2336/2336 Mac/Chrome browser
harness twice with zero application JavaScript errors, the 30/30 focused timeline validator, the
103/103 mechanism validator, the 36/36 telemetry validator and the Case 06 layout-override
validator. Normal and grayscale inspection confirmed strict 936/936 fit, fixed 816 × 1056
geometry, unchanged Student 5 / Accessible 7 page counts and zero content-boundary spill on both
touched pages. Every event and connector remained contained, topmost and collision-free; the
rail, direct state labels, border order and grayscale-independent patterns remained exact; and the
ordinal timing, correlation, converging-evidence and fictional-organism boundaries remained
intact. `C1C6-VIS01` is therefore `VERIFIED-FAMILY`, the second accepted Family 3 finding.

`C2C4-VIS01` is the third accepted Family 3 finding. It modernizes The Silent Grove's frozen Task
3 same-total sleep-pattern teaching figures on Student page 3 and Accessible page 3 without
changing their inline SVG or the adjacent ship-record telemetry table. Mia retains one unbroken
8-hour block; Sam retains eight separate one-hour blocks; both retain the exact 8-hour total, the
0–24 hour scale and the exact `0`, `6`, `12`, `18`, `24` ticks. The case-scoped shared layer adds
the persistent rail `SAA TEACHING EXAMPLE · SAME TOTAL / DIFFERENT PATTERN · NOT GROVE DATA`, a
stronger figure frame and grayscale-independent solid-versus-dashed block edges. It preserves the
semantic title, caption, extended description, all six learner responses and every source
disclaimer. It adds no case measurement, curve, biological inference or new action. No worksheet
content, case presentation, layout override, package metadata, task registry, page count,
persistence identity, source hash or release baseline changes.

Candidate `73e8496393f5f29d90abf0e805e4f43c90ca26f9` passed the complete 2339/2339
Mac/Chrome browser harness twice with zero application JavaScript errors, the 44/44 focused
timeline validator, the 103/103 mechanism validator, the 36/36 telemetry validator and the Case
04 layout-override validator. Normal and grayscale inspection confirmed strict 936/936 fit, fixed
816 × 1056 geometry, unchanged Student 6 / Accessible 8 page counts and zero content-boundary
spill on both touched pages. The status rail remained clear of the figure header; the exact SVG
geometry, hatch, solid/dashed edges, semantic relationships and all six blank learner responses
remained intact; and the separate six-row Table 5 ship record remained unchanged. The
teaching-example, not-grove-data, discrete-block and no-biological-claim boundaries remained
exact. `C2C4-VIS01` is therefore `VERIFIED-FAMILY`, completing Family 3.

`C1C5-VIS02` is the first accepted Family 4 evidence-convergence finding. It recomposes Europa Bunker's
frozen Task 3 Student table, Accessible cards and completed Answer Key exemplars through one
case-scoped EC1 presentation grammar. Crew, Sensors, Plants and Logs remain four independent
channels with the direct states `REPEATED PATTERN`, `EXPOSURE`, `BIO EVIDENCE` and
`PROTECTION LIMIT`, distinct solid/double/dashed/dotted borders and grayscale-independent
patterns. All four channels feed the qualified synthesis
`QUALIFIED CONVERGENCE · RADIATION BEST-SUPPORTED · NO SINGLE CLUE PROVES CAUSE`. Student retains
its four blank `t3-*` contribution fields; Accessible retains its four blank `a3-*` fields; and
the Answer Key retains all four exact completed exemplars. The shared layer changes no worksheet
wording, response identity, package-controlled source, page count or release record.

Candidate `70375daa5bebe7dea127c0b8f6f6e0aeece48fc9` passed the complete 2342/2342
Mac/Chrome browser harness twice with zero application JavaScript errors, the 30/30 focused
evidence-convergence validator, the 44/44 timeline validator, the 103/103 mechanism validator, the
36/36 telemetry validator and the Case 05 layout-override validator. Normal and grayscale
inspection confirmed strict 936/936 fit, fixed 816 × 1056 geometry, unchanged Student 4 / Answer
Key 4 / Accessible 7 page counts, full map/card containment and zero overflow, spill, clipping,
collision or crowding across all six target views. The synthesis rail remained at least 24.63 px
clear of every channel heading, status, evidence sentence and response border. All eight learner
fields remained blank, visible, unclipped and at their accepted dimensions; the Answer Key retained
all four exact exemplars. Every exposure, biological-evidence, modeled-secondary-radiation,
protection-limit, threshold and single-clue boundary remained exact. `C1C5-VIS02` is therefore
`VERIFIED-FAMILY`, the first accepted Family 4 finding.

`C1C7-VIS01` is the second accepted Family 4 evidence-convergence finding and completes the
family. Candidate `39325dcd1639c40e17aac435c599e17ecaffc3df` preserves The Gift's frozen Task 2
Student table, Accessible cards and completed Answer Key table as the source of truth. Liaison,
Biomonitors, Specimen and Archives stay independent channels with the direct
states `SOURCE / RANGE`, `MATCH / TRACE GAP`, `VIABLE / RESPONSIVE` and `MECHANISM RECORD`,
distinct solid/double/dashed/dotted borders and grayscale-independent patterns. The shared,
Case-07-scoped EC1 treatment separates the exact diagnostic
`PRIMARY TARGETS MATCH · TRACE CONTEXT INCOMPLETE` into primary-condition and trace-context
summaries, then converges only on
`QUALIFIED QUESTION · WHICH MISSING CONTEXT MATTERS? · 99.7% ≠ COMPLETE · SETS DIFFER / NO RATIO`.
It preserves all ten blank learner responses, all eight completed Answer Key contribution/limit
cells, the exact trace-comparison and convergence exemplars, and Student 6 / Answer Key 6 /
Accessible 8 page counts. It changes no worksheet content, case presentation, layout override,
package metadata, task registry, persistence identity, source hash, Teacher content or release
record.

The external Mac/Chrome gate passed under a candidate-specific differential acceptance. The
accepted prerequisite `9934febfe255778b29b84955a1f65371e74fa8d0` registered 2341/2341 PASS;
the candidate registered 2344/2344 PASS twice with zero application JavaScript errors, proving the
exact intended +3 assertion delta and passing all three new Case 07 contracts. This does not create
a general Mac/Linux rebaseline: Linux continues to register the canonical 2345 assertions, with
the candidate at 2314/2345 because of the 31 established platform/font/screenshot-smoke
exceptions. All three Case 07 contracts pass in both environments.

Normal and grayscale inspection of Student page 2, Answer Key page 2 and Accessible page 2
confirmed fixed 816 × 1056 geometry, strict `scrollHeight 936 == clientHeight 936` fit, exact
Student 6 / Answer Key 6 / Accessible 8 page counts, contained channels and diagnostic gates,
legible solid/double/dashed/dotted patterned states, all ten blank and unclipped learner fields,
all eight exact Answer Key cells, both exact exemplars and the 99.7%-not-complete and
sets-differ/no-ratio boundaries. No view had overflow, spill, clipping, collision or crowding.
The focused evidence-convergence validator passed 60/60, timeline 44/44, mechanism 103/103,
telemetry 36/36 and the Case 07 layout-override validator passed. `C1C7-VIS01` is therefore
`VERIFIED-FAMILY`, completing Family 4.

`C1C4-VIS03` is the accepted Family 5 engineering-control-loop finding and completes the family.
Candidate `4b0ef8bafd8f633b49e248a511bda13e554887e7` preserves Hayes Orbital Station's frozen
Student page 4, Answer Key page 3 reference and Accessible page 7 control structures as the
semantic source of truth. The shared Case-04-scoped CL1 treatment identifies the four
existing nodes as `SENSOR`, `COMPARATOR / CONTROLLER`, `INDEPENDENT ACTUATOR` and
`REACTOR / VERIFICATION`; labels the existing forward relationships `MEASURES`, `COMMANDS` and
`ADJUSTS`; and adds the explicit return rail
`PERFORMANCE FEEDBACK · CULTURE RESPONSE → SENSOR / COMPARATOR`. Solid, double, dashed and
dotted node borders plus independent hatch states preserve the role distinctions in grayscale.
The source labels and descriptions remain present, including the Answer Key's completed sensor,
controller, actuator and feedback wording.

The implementation changes no worksheet source, case presentation, layout override, package
metadata, task registry, page count, persistence identity, Teacher content, release record or
accepted-family implementation. Student retains blank fields `t7a | t7b` at 356 × 196.8 px;
Accessible retains blank fields `a7 | a7-longterm` at 720 × 148.8 px and 720 × 65.27 px. The
immediate response remains restoration of the validated recovery interval, while the long-term
response remains independent intensity/schedule control with actual-exposure and culture-response
monitoring. The diagram introduces no setpoint and does not generalize this reactor's failure to
all continuous cultivation.

The external Mac/Chrome gate passed under a candidate-specific differential acceptance. On the
same Mac, accepted prerequisite `e3abde0f0a05c3481bf6d03a7ca22c52c520d9ec` registered
2344/2344 PASS. Candidate Run 1 and Candidate Run 2 each registered 2347/2347 PASS with zero
application JavaScript errors, proving the exact intended +3 assertion delta and passing all
three new Case 04 contracts. This does not create a general platform policy or change the
canonical 2348-assertion registration. Linux reports 2317/2348 because of the 31 established
platform/font/screenshot-smoke exceptions, with all three Case 04 contracts passing.

Independent normal and grayscale inspection of Student page 4, Answer Key page 3 and Accessible
page 7 confirmed fixed 816 × 1056 geometry, strict `scrollHeight 936 == clientHeight 936` fit,
exact Student 4 / Answer Key 4 / Accessible 7 page counts, contained nodes and rails, readable
labels, four distinct border/pattern states, blank unclipped learner fields and no overflow, spill,
clipping, collision or crowding. The Answer Key retained the completed control model, validated
recovery interval, independent control, monitored response, current mixing/density validation and
reactor-specific continuous-cultivation boundary; no operating setpoint was invented. The focused
control validator passed 30/30, timeline 44/44, mechanism 103/103, evidence convergence 60/60,
telemetry 36/36 and the Case 04 layout-override validator passed. `C1C4-VIS03` is therefore
`VERIFIED-FAMILY`, completing Family 5.

`C1C5-VIS03` is the accepted first standalone Family 6 specification/verification finding.
Candidate `22ab529c388ee4f33be97ce3150fc5b5c49cba0b` preserves Europa Bunker's frozen final
Student page 4, Answer Key page 4 and Accessible page 7 as the semantic source of truth. Task 7
remains the engineering-problem definition and Task 8 remains the immediate/durable
recommendation; the shared Case-05-scoped SV1 treatment simply joins them into one visible
requirements-to-verification grammar. The existing Need, Criteria, Constraints and Verification
states use solid, double, dotted and dashed borders with independent hatch patterns. The existing
immediate and durable responses form the labeled
`ACTION PATH · CAUTIOUS NOW → DURABLE DESIGN`, and the existing justification/test response is
identified as the `MONITORING GATE`. The Answer Key carries the parallel
`ACCEPTED RESPONSE PATH · ACTION → DESIGN → VERIFY` treatment.

The implementation changes no worksheet source, case presentation, layout override, package
metadata, task registry, page count, response text, persistence identity, Teacher content, source
hash, release/history record or accepted-family implementation. Student retains seven blank fields:
`t7-need | t7-criteria | t7-constraints | t7-verify | t8-immediate | t8-durable | t8-justify`.
Accessible retains the parallel seven blank fields ending in `a8-test`. The Answer Key retains
the exact accepted Need/Criteria/Constraints/Verification and immediate/durable/justification
exemplars. No crop-safe threshold, shielding percentage, guaranteed solution or completed in-game
fix is added.

The external Mac/Chrome gate passed under a candidate-specific differential acceptance. On the
same Mac, accepted prerequisite `3b19fcbcf7cabec08aadf303b41eb8168604c931` registered
2347/2347 PASS. Candidate Run 1 and Candidate Run 2 each registered 2350/2350 PASS with zero
application JavaScript errors. The candidate delta is exactly +3, both candidate runs have
identical assertion-name sets, no inherited assertion was removed and all three new Case 05
contracts registered and passed. This does not create a general platform policy or change the
canonical 2351-assertion registration. Linux reports 2320/2351 because of the 31 established
platform/font/screenshot-smoke exceptions, with all three Case 05 contracts passing.

Independent normal and grayscale inspection of Student page 4, Answer Key page 4 and Accessible
page 7 confirmed fixed 816 × 1056 geometry, strict `scrollHeight 936 == clientHeight 936` fit,
exact Student 4 / Answer Key 4 / Accessible 7 page counts, contained panels, distinct
border/pattern states, all fourteen blank unclipped learner fields and no overflow, spill,
clipping, collision or crowding. The Answer Key retained crop-specific monitoring, microscopy,
growth-stage and repeated-trial verification; separate crew and crop criteria; modeled secondary
radiation; the unverified-safety qualifier; and the prohibition on invented numerical safe levels,
guaranteed success and an in-game `apply the fix` step. The focused specification validator passed
35/35, control 30/30, timeline 44/44, mechanism 103/103, evidence convergence 60/60, telemetry
36/36 and the Case 05 layout-override validator passed. `C1C5-VIS03` is therefore
`VERIFIED-FAMILY`. Family 6 now has two of four assignments verified, including the previously
accepted hybrid `C2C3-VIS03`; the unique-finding inventory counts that hybrid only once.

`C2C1-VIS03` is the accepted second standalone Family 6 specification/verification finding.
Corrected candidate `4d181aa796591249bb4f989e091c646b22b3a3e8` preserves Heavy Hands Student page 5, Answer Key page 4
and Accessible page 8 as the semantic source of truth. The existing Task 8 sequence remains
midpoint-only rule → missing across-bed criterion and reported constraint → compare two reported
proposals → choose → monitored trial → stop/revise. The strictly Case-01-scoped shared treatment
labels that path `POINT RULE → ACROSS-BED TEST`, identifies the proposal table as
`COMPARE AGAINST CRITERION` and marks the existing choice response as `DECISION GATE`. Independent
hatch states and inset rails distinguish the rule, criterion, constraint, proposal, verification
and stop states without adding a learner action. The four proposal checks remain the only
content-derived response widths; the cross-platform browser usability floor is 108 px, below the
independently observed 109.38 px Mac width, so no response dimension changes. Each of the ten Task
8 response labels has 6 px of left clearance so its inset rail cannot paint beneath the first
glyph.

The accepted implementation changes no worksheet source, case presentation, layout override, package metadata,
task registry, response text, persistence identity, page count, Teacher content, source hash,
release/history record or accepted-family implementation. Student retains blank fields
`t8-criterion | t8-constraint | t8-o1 | t8-o2 | t8-choice | t8-trial | t8-stop`; Accessible
retains the parallel seven `a8-*` fields. The Answer Key retains its exact five-paragraph exemplar,
including the trial-justified tolerance boundary, the statement that neither proposal may promise
recovery, the unchanged-control trial, the stop/revise rule and the case-bounded marking note.

The first implementation commit, `473722443e0d6e03e3e7edf1c855cf68e7c8fbc8`, failed its
external Mac/Chrome gate at **2351/2353** twice with zero JavaScript errors. Both normal and
grayscale Heavy Hands assertions failed because `a8-o1` and `a8-o2` measured 109.38 px against the
110 px floor; independent inspection also found all ten new inset label rails painted beneath the
first glyph. Accepted prerequisite `b95563f…` passed 2350/2350 on that Mac, so the candidate added
three registered assertions but only one passing assertion. No differential exception applies to
new failing contracts. The corrective successor preserves `4737224…` as immutable evidence.

The external Mac/Chrome gate passed under a candidate-specific differential acceptance. On the
same Mac, accepted prerequisite `b95563f181c0d442d40784bbe1a45d1794cfb256` registered
2350/2350 PASS. Corrected candidate Run 1 and Run 2 each registered 2353/2353 PASS with zero
application JavaScript errors. The candidate delta is exactly +3 registered and +3 passed, both
runs have identical assertion-name sets, no inherited assertion was removed or broken and all
three new Heavy Hands contracts passed. This does not create a general platform policy or change
the canonical 2354-assertion registration.

Linux Chromium registers the intended three new browser assertions and reports **2323/2354** with
zero application JavaScript errors: exactly the 31 established platform/font/screenshot-smoke
exceptions and no candidate-specific failure. All three new contracts pass. Six-view normal and
grayscale inspection confirms fixed 816 × 1056 geometry, strict
`scrollHeight 936 == clientHeight 936` fit, exact Student 5 / Answer Key 4 / Accessible 8 page
counts, no overflow/spill/clipping/collision/crowding and preserved field dimensions. Earlier
local reserve measurements were 24.27 / 73.41 / 193.22 px; an independent content-area method
reported 39.59 / 150.05 / 211.36 px. Because the metric was not defined, neither numeric series is
an acceptance gate; exact fit, positive clearance and no crowding govern. The focused
specification validator passed 70/70, control 30/30, timeline 44/44, mechanism 103/103, evidence
convergence 60/60, telemetry 36/36 and the Case 01 layout-override validator passed.
`C2C1-VIS03` is therefore `VERIFIED-FAMILY`. Family 6 now has three of four assignments verified,
including hybrid `C2C3-VIS03`, counted once in the unique-finding inventory.

`C2C4-VIS03` is the accepted fourth and final Family 6 specification/verification finding.
Candidate `84333922c4e1e7cd7c7b4de248243c5ddd0c9ad2` preserves Silent Grove's frozen Student page 6,
Answer Key page 4 and Accessible page 8 as the semantic
source of truth. The shared Case-04-scoped SV1 treatment exposes the existing progression as
`EVIDENCE → SPECIFY → VERIFY`; the existing Table 7 is labeled
`MINIMUM ≠ PREFERRED DESIGN`. The three table rows retain their exact evidence roles and use
dashed, double and dotted states for recorded minimum, two-year schedule and reversibility
record. The four existing learner responses use dashed / double / dotted / solid states for the
dark-hour criterion, cycle-stability criterion, constraint and monitored trial/stop rule. The
Answer Key mirrors those four states and keeps its fifth uncertainty note distinct.

The accepted implementation changes no worksheet source, case presentation, layout override, package metadata,
task registry, page count, response text, persistence identity, Teacher content, source hash,
release/history record or accepted-family implementation. Student retains four blank fields:
`t8-criterion-1 | t8-criterion-2 | t8-constraint | t8-test`. Accessible retains the parallel four
blank fields. The Answer Key retains the exact accepted five-paragraph exemplar. Five hours
remains the recorded trial minimum rather than the preferred design; six hours remains the
schedule with a two-year successful record in this grove; 40–80 ppb remains a range; and recovery
remains an unreplicated prediction rather than a guaranteed result.

The external Mac/Chrome gate passed under a candidate-specific differential acceptance. On the
same Mac, accepted prerequisite `199d5d289947fe8402d6563067afa7d47be60cfb` registered
2353/2353 PASS. Candidate Run 1 and Run 2 each registered 2356/2356 PASS with zero application
JavaScript errors. The candidate delta is exactly +3 registered and +3 passed, both runs have
identical assertion-name sets, no inherited assertion was removed or broken, no assertion passing
at the prerequisite now fails and all three new Silent Grove contracts passed. This does not
create a general platform policy or change the canonical 2357-assertion registration.

The finished Linux Chromium 149 run registers the canonical total of 2357 assertions and
reports 2326/2357 because of the same 31 established platform/font/screenshot-smoke exceptions.
All three new Case 04 assertions pass and application JavaScript errors remain zero. The candidate
adds one six-state strict-fit contract plus normal and grayscale semantic/geometry contracts.
Normal and grayscale inspection confirms fixed 816 × 1056 pages, exact
`scrollHeight 936 == clientHeight 936`, Student 6 / Answer Key 4 / Accessible 8 page counts,
contained panels, distinct border/pattern states, blank usable learner fields and no overflow,
spill, clipping, collision or crowding. All eight learner fields matched the Linux reference
dimensions exactly during independent Mac inspection. The focused specification validator passed
105/105, control 30/30, timeline 44/44, mechanism 103/103, evidence convergence 60/60, telemetry
36/36 and the Case 04 layout-override validator passed. `C2C4-VIS03` is therefore
`VERIFIED-FAMILY`, completing Family 6 at four of four assignments.

`C1C6-VIS03` is the accepted first standalone Family 8 intervention-comparison finding. Candidate
`8d6a51a58a18f1f4db51d7a25ea58317f1962408` preserves First Contact Protocol's frozen Student page 3,
Answer Key page 3 and Accessible page 5 as the semantic source of truth. The strictly Case-06-
scoped shared treatment exposes the existing Task 6 sequence as
`COMPARE → SELECT → MONITOR`. Its three existing options retain their exact order and receive
`UNSAFE`, `NO CHANGE` and `CONTROLLED TEST` states with double, dotted and solid borders plus
independent hatch patterns. The existing life-support note remains a distinct safety gate; the
recommendation and monitoring fields remain separate solid and dashed rails. The Answer Key
mirrors the same option states and both response gates.

The accepted implementation changes no worksheet source, case presentation, layout override, package metadata,
task registry, response wording or dimensions, persistence identity, page count, Teacher content,
source hash, release/history record or accepted-family implementation. Student retains five blank
fields: `t6-disable | t6-unchanged | t6-selective | t6-recommend | t6-monitor`. Accessible retains
the parallel five fields and only its already accepted unsafe-option scaffold. Disabling all
atmospheric processing remains unsafe; unchanged operation remains inconsistent with the supported
signal-loss diagnosis; and isolation or selective preservation remains a reversible, limited-scale,
monitored test rather than a completed treatment or guaranteed recovery. Pressure,
breathable-gas control and contaminant protection remain active constraints.

The external Mac/Google Chrome gate passed under a candidate-specific differential acceptance. On
the same Mac, accepted prerequisite `dab27208c6fa352a506fbf6a80a7b3071fcad286` registered
2356/2356 PASS. Candidate Run 1 and Candidate Run 2 each registered 2359/2359 PASS with zero
application JavaScript errors. The candidate delta is exactly +3 registered and +3 passed, both
runs have identical assertion-name sets, no inherited assertion was removed or broken, no
assertion passing at the prerequisite now fails and all three new First Contact contracts passed.
This does not create a general platform policy or change the canonical 2360-assertion registration.

The finished Linux Chromium 143 run registers the canonical total of 2360 assertions and
reports **2329/2360** because of the same 31 established platform/font/screenshot-smoke exceptions.
All three new Case 06 assertions pass and application JavaScript errors remain zero. The candidate
adds one six-view strict-fit contract plus normal and grayscale semantic/geometry contracts.
Normal and grayscale inspection confirms fixed 816 × 1056 pages, exact
`scrollHeight 936 == clientHeight 936`, Student 5 / Answer Key 5 / Accessible 7 page counts,
contained option panels, distinct border/pattern states, blank usable learner fields and no
overflow, spill, clipping, collision or crowding. All ten learner fields matched the Linux
reference dimensions exactly during independent Mac inspection. The focused intervention/trial
validator passed 63/63, specification 105/105, control 30/30, timeline 44/44, mechanism 103/103,
evidence convergence 60/60, telemetry 36/36 and the Case 06 layout-override validator passed.
`C1C6-VIS03` is therefore `VERIFIED-FAMILY`. Family 8 now has two of five assignments verified:
accepted hybrid `C2C5-VIS03`, already counted once in the unique inventory, and accepted standalone
`C1C6-VIS03`.

`C1C7-VIS03` is the accepted second standalone Family 8 intervention-comparison finding. Corrective
candidate `917908cc6da875d33c953601f2ed565b53939dc5` preserves The Gift's frozen Student page 5, Answer Key
page 5 and Accessible page 7 as the semantic source of truth. The strictly Case-07-scoped shared
treatment exposes the existing Task 7 sequence as `EVIDENCE → CONTROL → MONITOR`. The three
existing routes retain their exact order. Student matrix rows and Accessible route cards receive
`SUPPORTED`, `QUALIFIED` and `RESEARCH ONLY` states with solid, dashed and double borders plus
independent patterns. The existing +10, +5 and +0 story ranks remain visible but typographically
subordinate to evidence, controls and uncertainty. Recommendation, monitoring/stopping and
prediction/challenge fields remain separate solid, dashed and dotted rails. The Answer Key mirrors
the same three response gates.

The accepted implementation changes no worksheet source, case presentation, layout override, package metadata,
task registry, response wording or dimensions, persistence identity, page count, Teacher content,
source hash, release/history record or accepted-family implementation. Student retains three blank
fields: `t7-recommend | t7-monitor | t7-predict`. Accessible retains the parallel three fields and
only its already accepted monitoring/stopping scaffold. The sealed natural-plume route remains the
best-supported immediate route; verified extraction remains defensible only when its added
uncertainties are controlled; and validated synthesis remains a longer research program rather
than a safe immediate action. The evidence supplies no safe numerical dose, exposure is stoppable
only before commitment, and the predicted first responses and stabilization remain modeled story
outcomes rather than replicated trials.

The first implementation commit, `d97fd466057ad1c9bab7d33d5666cc946416586c`, failed its first
external Mac/Google Chrome 150 gate deterministically at **2360/2362** on both runs with zero
application JavaScript errors. The strict-fit/page-count/geometry assertion passed. The normal and
grayscale semantic assertions failed only because their browser oracles expected spaces that a
`<br/>` does not contribute to `textContent` and expected `Task 7` text that exists only in
`aria-label` attributes rather than visible page `textContent`. Every other captured sub-condition
passed. Accepted prerequisite `e7e1b58…` passed 2359/2359 on the same Mac, so the failed candidate
added three registered assertions but only one passing assertion. These are new DOM-structure
oracle defects, not the inherited one-registration differential and not product-rendering defects.
The corrective successor preserves `d97fd46…` as immutable evidence and changes only those two
harness expectations plus the focused validator and active lifecycle records that govern them.

The external Mac/Google Chrome gate passed under a candidate-specific differential acceptance. On
the same Mac, accepted prerequisite `e7e1b58f61899b0e53de5b7f07cba205fdb7797b` registered
2359/2359 PASS. Corrective candidate Run 1 and Run 2 each registered 2362/2362 PASS with zero
application JavaScript errors. The candidate delta is exactly +3 registered and +3 passed, both
runs have identical assertion-name sets, all three new The Gift contracts passed, no inherited
assertion was removed or broken and no assertion passing at the prerequisite now fails. Both
previously failing DOM-oracle assertions now pass. This disposition applies only to corrective
candidate `917908c…`; it does not create a general platform policy or change the canonical
2363-assertion registration. Failed first implementation `d97fd46…` remains immutable evidence in
the accepted lineage and is not itself granted visual acceptance.

The candidate adds exactly three browser assertions: one six-view strict-fit contract plus normal
and grayscale semantic/geometry contracts. Independent normal and grayscale inspection of Student
page 5, Answer Key page 5 and Accessible page 7 confirmed fixed 816 × 1056 geometry, exact
`scrollHeight 936 == clientHeight 936` fit, Student 6 / Answer Key 6 / Accessible 8 page counts,
contained route panels and response rails, distinct border/pattern states, blank usable learner
fields except the accepted Accessible monitoring scaffold, three unchanged Answer Key exemplars,
and no overflow, spill, clipping, collision or crowding. The focused intervention/trial validator
passed 125/125; specification 105/105; control 30/30; timeline 44/44; mechanism 103/103; evidence
convergence 60/60; telemetry 36/36; and the Case 07 layout-override validator passed.
`C1C7-VIS03` is therefore `VERIFIED-FAMILY`. Family 8 now has three of five assignments verified:
accepted hybrid `C2C5-VIS03`, already counted once in the unique inventory, accepted standalone
`C1C6-VIS03` and accepted corrective standalone `C1C7-VIS03`.

`C2C1-VIS01` is the implemented but unaccepted Family 7 pilot. It preserves Heavy Hands' frozen
Student Task 4 page 3 and Accessible Task 4 page 4 SVGs as the semantic source of truth. Those two
figures already contain the same 20 cm bed boundary, the qualitative small / medium / large size
sequence, three independent patterns, the explicit no-deformation-quantity limit, an accessible
SVG title and a non-color extended description. The strictly Case-01-scoped shared treatment
repositions those existing marks as matched radial-bed cutaway panels. Equal dashed bed sections
retain one common depth while the contained patterned tuber marks increase in both width and
radial span. The generated status reads `RADIAL BED CUTAWAY · NOT TO SCALE`.

The candidate changes no worksheet source, case presentation, layout override, package metadata,
task registry, response wording or dimensions, persistence identity, page count, Teacher content,
source hash, release/history record or accepted-family implementation. Student fields
`t4-span | t4-rules-out` and Accessible fields `a4-span | a4-rules-out` remain blank and
source-controlled. The specimen record remains bounded to gorlroot in this habitat: the tuber
starts aligned with the outward primary roots, curves sideways across the row rather than toward
or away from the axis, and deformation increases qualitatively with diameter. No organ dimension,
deformation amount, cross-species rule or scale relationship is introduced.

The candidate adds exactly three browser assertions: one four-view strict-fit/page-count/geometry
contract plus normal and grayscale semantic/geometry contracts. Canonical project registration is
therefore expected to become 2366. The focused contracts require fixed 816 × 1056 pages, unchanged
Student 5 / Accessible 8 page counts, equal bed boundaries, strictly increasing contained tuber
spans, three independent source patterns, exact direct labels, the qualitative/not-to-scale state,
the 20 cm boundary and the no-deformation-quantity limitation. This production environment makes
no executable-browser, rendered-fit or manual-inspection claim. Until the complete external
browser harness passes twice and both pages are inspected in normal and grayscale,
C2C1-VIS01 does not advance the accepted **31 of 36 completed / 5 of 36 remaining** inventory.
Family 7 remains zero of two accepted assignments; this pilot remains `IMPLEMENTED-CANDIDATE`.

## 3. Exact inventory reconciliation

The current remediation register contains exactly **36 findings classified
`DEFERRED-VISUAL`**:

- **35 numbered `VIS` figure/diagram/data-display candidates** — exactly reconciled to the
  discovery catalog; none is missing and none is duplicated.
- **1 numbered grayscale finding, `C1C1-GS01`**.

Accepted progress after The Gift intervention-comparison closeout is **31 of 36 completed**
and **5 of 36 remaining**. Family 1 contributes 9 completed findings, Family 2 contributes all 11
of its verified findings, Family 3 contributes all 3 of its verified findings, Family 4 contributes
both of its verified findings and Family 5 contributes its sole verified finding. Family 6 is
complete at four of four assignments: hybrid `C2C3-VIS03`, already counted once among Family 2's
unique findings, and accepted standalone findings `C1C5-VIS03`, `C2C1-VIS03` and `C2C4-VIS03`.
Family 8 has three of five assignments verified: hybrid `C2C5-VIS03`, already counted once among
Family 2's unique findings, accepted standalone `C1C6-VIS03` and accepted corrective standalone
`C1C7-VIS03`.

Accepted progress after the First Contact intervention-comparison closeout is **30 of 36 completed**
and **6 of 36 remaining**.

Accepted progress after the Silent Grove specification/verification closeout is **29 of 36 completed**
and **7 of 36 remaining**.

At the preceding Heavy Hands specification/verification closeout, accepted progress was 28 of 36
completed and 8 of 36 remaining.

At the preceding Europa specification/verification closeout, accepted progress was 27 of 36
completed and 9 of 36 remaining.

At the preceding Hayes engineering-control-loop closeout, accepted progress was 26 of 36 completed
and 10 of 36 remaining.

At the preceding The Gift evidence-convergence closeout, accepted progress was 25 of 36 completed
and 11 of 36 remaining.

At the preceding Europa evidence-convergence closeout, accepted progress was 24 of 36 completed
and 12 of 36 remaining.

At the preceding Silent Grove sleep-pattern closeout, accepted progress was 23 of 36 completed and
13 of 36 remaining.

At the preceding First Contact timing-telemetry closeout, accepted progress was 22 of 36 completed
and 14 of 36 remaining.

At the preceding Hayes incident-log closeout, accepted progress was 21 of 36 completed and 15 of
36 remaining.

At the preceding Family 2 closeout, accepted progress was 20 of 36 completed and 16 of 36 remaining.

The final remediation status also carries token/fill maintenance notes for C1 Case 02 and
C1 Case 06. Those two notes are tracked in §5 as visual-system work items but are not invented
finding IDs and do not change the formal count of 36.

Inventory separation:

| Work type | Formal findings | Additional tracked items | Production treatment |
|---|---:|---:|---|
| figure / diagram / data display | 35 | 0 | deterministic HTML/CSS/SVG; illustrative work only where authorized |
| grayscale system | 1 | 2 | rendered-surface correction plus bounded token/fill coverage cleanup |
| shared visual system | 0 | primitive set below | implementation dependency, not a new finding |
| informational only | 0 | audit cautions embedded below | constraints, not new graphics |

## 4. Notation and common requirements

Edition abbreviations: **S** Student, **A** Accessible, **T** Teacher, **AK** Answer Key.
Page references use the current role page IDs/counts at the accepted baseline. “Parallel” means
the same graphic or grammar is synchronized where the current content repeats; it does not mean
adding a figure to every role.

Common footprint requirement for every row: retain the existing role page count, page ID, fixed
8.5 × 11 geometry, task order, and response-area utility. Reduce visual chrome before changing
layout. A significant architecture/page-count change is owner-gated.

Common validation for every row: focused package validation; no overflow/clipping; legible labels;
logical DOM order and alt/extended description where applicable; grayscale-independent meaning;
unchanged response IDs/fill persistence; synchronized keyed exemplar where the learner completes
the visual; zero JavaScript errors; `git diff --check`. Family completion additionally requires
the full non-PDF browser regression against the current accepted executable baseline of **2324/2324 PASS
and 0 JavaScript errors**. The accepted correctness commit produces 2293/2293; five telemetry
assertions verify computed visual delivery, pseudo-content, table patterns/state borders and the
dense telemetry cascade, two accepted mechanism-pilot assertions verify the horizontal dependency
rail, Answer Key interruption state and Accessible vertical rail, two Mars expansion assertions
verify the C1C3 spectral-loss chain in normal and grayscale, one strict-fit assertion requires real
bottom reserve on the dense C1C3 Student mechanism page, three accepted ISS assertions verify
the gravity cutaways in both modes plus strict fit across the three synchronized editions, and
three accepted Hayes assertions verify its direct repeat loop, connector treatment and strict fit.

## 5. Grayscale-system work

| Finding / item | Case | Current state | Modernization | Method | Constraints and validation | Status |
|---|---|---|---|---|---|---|
| `C1C1-GS01` | C1 Case 01 — ISS Greenhouse | Grayscale variables change, but neutral/optional callouts retain tint and `.callout-success` uses hard-coded `#e9f3ed`. | Neutralize rendered callout surfaces in grayscale while retaining border/value hierarchy; update the inherited-tint browser expectation only after the rendered count reaches zero. | deterministic CSS | Do not rewrite dormant tokens without maintenance value; verify all four roles, color and grayscale, page geometry, contrast, and zero tint. | `PLANNED · FORMAL FINDING` |
| tracked status §5.3 | C1 Case 02 — Lunar Greenhouse | Rendered grayscale passes; some declared palette tokens are dormant and not neutralized. | Trace token reachability; neutralize only tokens that can reach printable components or consolidate them into governed grayscale values. | deterministic CSS audit | Must not turn a passing rendered state into blanket low-contrast gray; zero new tinted rendered surfaces. | `PLANNED · UNNUMBERED BACKLOG ITEM` |
| tracked status §5.3 | C1 Case 06 — First Contact Protocol | Grayscale override exists, but the accepted handoff records token/fill coverage as visual backlog. | Audit all printable fills against the override set and close any reachable gap using Cool Mission Gray hierarchy. | deterministic CSS audit | Preserve timing/model/data distinction with value, border, label and pattern; no color-only meaning. | `PLANNED · UNNUMBERED BACKLOG ITEM` |

## 6. Candidate production matrix — Campaign 1

| Finding | Case; editions; task/page | Current visual and problem | Family | Proposed modernization and method | Footprint / synchronization | Science/data constraints | Dependency and validation | Status |
|---|---|---|---|---|---|---|---|---|
| `C1C1-VIS01` | ISS Greenhouse; S T5 p2, A T5 p3, AK T5 p2 | Two plain comparison cards; the gravity-sensing relationship is text-heavy and visually basic. | 2 · Causal mechanism/pathway | Matched statocyte/root cutaways with settled/unsettled statolith states, direction cue, and root outcome; deterministic SVG + existing writable phrase fields. | Same footprint; synchronize S/A/AK blanks and completed exemplar; T wording only. | Do not imply roots become random or respond only to gravity; fictional case context vs established gravitropism remains explicit. | primitives P1–P6; mechanism and fill-persistence tests | `VERIFIED-FAMILY · 35/35 FAMILY STATIC PASS · 2306/2306 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 884/884 · ceb632d ACCEPTED` |
| `C1C2-VIS01` | Lunar Greenhouse; S T3 p1, A T3 p2, AK T3 p1 | Conventional six-box flow; A uses a separate plain vertical list. | 2 · Causal mechanism/pathway | Reproductive telemetry rail: anther/pollen → physical agitation → stigma → pollen tube → fertilization → fruit, with numbered nodes and failure/interruption status; deterministic HTML/CSS/SVG. | Preserve six exact bank entries and fields; horizontal S/AK and vertical A remain one grammar. | Pores/structures downstream may remain capable; failed Step 2 interrupts rather than destroys them. | P1–P6; exact-bank parity; AK failure-state check | `VERIFIED-FAMILY-PILOT · 14/14 PILOT STATIC PASS · 2300/2300 BROWSER PASS · 0 JS ERRORS` |
| `C1C3-VIS01` | Mars Habitat; S T2 p1, A T2 p2, T reference p4, AK T2 p1 | Accurate ordinary four-bar transmission graph repeated across roles. | 1 · Technical telemetry/data | Four-channel optical-transmission scan with direct percentages, patterned rails, and low-transmission flags; deterministic SVG. | Preserve current figure height and table backup; synchronize all existing instances. | Four discrete bands only; no continuous spectrum or interpolated values; retain 92%, 88%, 31%, 12%. | P1–P5, D1; numeric DOM assertions and extended description | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C1C3-VIS02` | Mars Habitat; S T3 p2, A T3 p3, AK T3 p1 | Boxed “280 adequate” plus repeated mini bars; comparison is correct but visually ordinary. | 1 · Technical telemetry/data | Dual-channel diagnostic: photon quantity 280 PPFD `ADEQUATE` vs four-rail spectrum `UNEVEN`, with `Quantity ≠ Distribution`; deterministic HTML/SVG. | Same footprint; synchronize S/A and concise AK treatment. | PPFD quantity must not be presented as spectral adequacy; preserve units and exact discrete values. | C1C3-VIS01 rail primitive; numeric/parity checks | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C1C3-VIS03` | Mars Habitat; S T6 p3, A T6 p5, AK T6 p3 | Generic five-stage rectangles. | 2 · Causal mechanism/pathway | Technical glyph chain: collector → wrong BP-4 filter → selective loss → disrupted new chlorophyll production → pale new growth; deterministic HTML/SVG. | Preserve five-stage exact-match bank, blank stages and vertical A variant. | Do not claim an unsupported universal chlorophyll mechanism; retain case wording and corrected 700 nm boundary. | mechanism primitive; bank/order/persistence checks | `VERIFIED-FAMILY · 25/25 FAMILY STATIC PASS · 2303/2303 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 3.47px RESERVE · c532ac5 ACCEPTED` |
| `C1C4-VIS01` | Hayes Orbital Station; S T2 p1, A T2 p2, AK T2 p1 | Five numbered blanks connected by plain arrows. | 3 · Timeline/event log | SAA incident log with verified relative-event slots and event-type markers; deterministic HTML/CSS. | Same five writable positions; A stays vertical; AK completes identical log. | Relative timing only; do not invent mission days or proportional spacing. | P1–P5, TL1; exact event-bank/parity checks | `VERIFIED-FAMILY · 17/17 TIMELINE STATIC PASS · 2333/2333 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · d5ffe37 ACCEPTED` |
| `C1C4-VIS02` | Hayes Orbital Station; S T5 p3, A T5 p5, AK T5 p3 | Six-stage snake layout; reading direction requires prose. | 2 · Causal mechanism/pathway | Immediate closed fault loop with directional connectors and explicit repeat link. | Preserve six exact stages/fields and A vertical reading order. | Qualitative recurrence; no invented light dose, density or crash interval beyond reported 6–8 days. | loop variant of mechanism primitive; connector/read-order tests | `VERIFIED-FAMILY · 44/44 FAMILY STATIC PASS · 2309/2309 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · d5b6c02 ACCEPTED` |
| `C1C4-VIS03` | Hayes Orbital Station; S T7 p4, A T7 p7, AK T7 p4 | Four equal text boxes in a linear row. | 5 · Engineering control loop | Sensor → comparator → independent actuator → reactor, with performance feedback to verification; deterministic SVG/HTML. | Keep two learner response fields and current page; complete AK treatment without new graded actions. | Independent light control and monitored response; do not generalize continuous-light failure to all cultures. | P1–P6, CL1; feedback-label and response tests | `VERIFIED-FAMILY · 30/30 CONTROL STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 4b0ef8b ACCEPTED` |
| `C1C5-VIS01` | Europa Bunker; S T5 p3, A T5 p5, AK T5 p3 | Seven-stage snake of text boxes. | 2 · Causal mechanism/pathway | Qualified hazard pathway visually separating environment, modeled interaction, exposure evidence, evidence limit, biological evidence, growth consequence and convergence; deterministic HTML/SVG. | Preserve seven exact bank entries and current blanks; A vertical; AK complete. | Modeled secondary radiation ≠ measured; exposure ≠ damage; abnormalities are consistent with damage; no exact quantities. | mechanism/status primitives; phrase, qualifier and persistence tests | `VERIFIED-FAMILY · 52/52 FAMILY STATIC PASS · 2312/2312 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · dcb2d91 ACCEPTED` |
| `C1C5-VIS02` | Europa Bunker; S T3 p2, A T3 p3, AK T3 p2 | Four-row source table; convergence remains implicit. | 4 · Evidence-convergence map | Four labeled channels—Crew, Sensors, Plants, Logs—feeding a qualified “best-supported” diagnosis node while retaining contribution writing areas. | Recompose within table footprint; preserve all contribution fields and AK exemplars. | No single clue proves radiation; sensor exposure and biological evidence stay distinct. | P1–P6, EC1; field-count, AK and causal-language checks | `VERIFIED-FAMILY · 30/30 FAMILY STATIC PASS · 2342/2342 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 70375da ACCEPTED` |
| `C1C5-VIS03` | Europa Bunker; S T8 p4, A T8 p7, AK T8 p4 | Need/criteria/constraints/verification organizer with ordinary panels. | 6 · Specification/verification | Compact mission requirements panel with Need, Criteria, Constraints, Verification and monitoring gate; deterministic HTML/CSS. | Preserve every existing writable field and page; sync AK completion. | No crop-safe threshold or guaranteed shielding solution may be invented. | P1–P5, SV1; field/parity and qualifier checks | `VERIFIED-FAMILY · 35/35 SPECIFICATION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 22ab529 ACCEPTED` |
| `C1C6-VIS01` | First Contact Protocol; S T3 p2, A T3 p2; T/AK reference where present | Small three-block timing strip embedded with evidence. | 3 · Timeline/event log | Compact event/telemetry strip: docking at 72.4 h ago → 18 min → last signal at 72.1 h ago. | No new response control; preserve evidence-card footprint and all repeated values. | Larger “hours ago” is earlier; 0.3 h = 18 min; timing is correlation, not proof. | TL1; exact-text/numeric and page-fit assertions | `VERIFIED-FAMILY · 30/30 TIMELINE STATIC PASS · 2336/2336 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 66a3d1b ACCEPTED` |
| `C1C6-VIS02` | First Contact Protocol; S T4 p2, A T4 p3, AK T4 p2 | Four generic stage cards. | 2 · Causal mechanism/pathway | Bounded four-channel systems model: atmosphere → signal persistence → fictional network response → partnership outcome, with labeled transitions and state markers. | Preserve exact phrase bank and response IDs; horizontal S/AK, vertical A. | Earth signalling context must remain distinct from fictional volatile/network dormancy system. | mechanism/system-boundary primitive; exact-bank, fiction-status and persistence checks | `VERIFIED-FAMILY · 60/60 FAMILY STATIC PASS · 2315/2315 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 11a0871 ACCEPTED` |
| `C1C6-VIS03` | First Contact Protocol; S T6 p3, A T6 p5, AK T6 p3 | Three-row intervention table. | 8 · Intervention comparison/trial workflow | Decision panel distinguishing unsafe shutdown, no change, and reversible selective treatment; include evidence fit, safety constraint and monitor rail. | Preserve recommendation and monitoring fields; identical option order across S/A/AK. | Do not imply disabling life support is safe; preserve pressure, breathable-gas and contaminant controls. | P1–P5, IC1; option/parity and response tests | `VERIFIED-FAMILY · 63/63 INTERVENTION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 8d6a51a ACCEPTED` |
| `C1C7-VIS01` | The Gift; S T2 p2, A T2 p2, AK T2 p2 | Primary-condition and trace-context information is tabular; `99.7%` visually dominates. | 4 · Evidence-convergence/diagnostic map | Matched diagnostic channels separating “primary targets match” from “trace biological context incomplete”, converging only on a qualified question. | Preserve evidence/limit writing areas and AK exemplar; no page-count change. | 99.7% is not complete ecosystem similarity; 12 and 847+ identifier sets differ and cannot be divided. | EC1 + comparison primitive; prohibited-inference checks | `VERIFIED-FAMILY · 60/60 FAMILY STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 39325dc ACCEPTED` |
| `C1C7-VIS02` | The Gift; S T4 p3, A T4 p4, T reference p4, AK T4 p3 | Six-stage generic chain with status fields. | 2 · Causal mechanism/pathway | Biological systems schematic: mature source → incidental cue → carrier/path → receptors → commitment → young symbiosis, with supply/status markers. | Preserve six phrases, every status/X control and AK completed statuses; horizontal/vertical variants. | Fictional system; under-3-m supported path; no safe dose/structure claim; commitment/reversibility distinction retained. | mechanism + status primitive; exact subpart, persistence and fiction checks | `VERIFIED-FAMILY · 68/68 FAMILY STATIC PASS · 2318/2318 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 812d5c3 ACCEPTED` |
| `C1C7-VIS03` | The Gift; S T7 p5, A T7 p7, AK T7 p5 | Dense intervention matrix; story rank competes with evidence. | 8 · Intervention comparison/trial workflow | Three-route decision/monitoring matrix with explicit evidence fit, controls, reversibility/commitment, monitoring and uncertainty hierarchy. | Preserve route choice, evidence, monitor/stop and prediction fields; points remain subordinate story ranks. | Story scores are not scientific results; no inferred dose, purity, synthesis or safety. | IC1; response/AK parity and label hierarchy checks | `VERIFIED-FAMILY · 125/125 INTERVENTION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 917908c ACCEPTED` |

## 7. Candidate production matrix — Campaign 2

| Finding | Case; editions; task/page | Current visual and problem | Family | Proposed modernization and method | Footprint / synchronization | Science/data constraints | Dependency and validation | Status |
|---|---|---|---|---|---|---|---|---|
| `C2C1-VIS01` | Heavy Hands; S T4 p3, A T4 p4 | Three simple tuber panels and span bars. | 7 · Biological/structural cutaway | Matched radial-bed cross-sections showing a small/medium/large organ spanning more of the same 20 cm bed depth; deterministic SVG. | Replace existing figure only; retain table/text support and exact height. | Qualitative size dependence only; no deformation amounts or invented organ dimensions. | P1–P6, CU1; not-to-scale/alt and no-new-number check | `IMPLEMENTED-CANDIDATE` |
| `C2C1-VIS02` | Heavy Hands; T reference p4 | Three-point radial profile is a basic Teacher-only schematic. | 1 · Technical telemetry/data | Centrifuge telemetry profile with three reported radii, outward direction arrows and direct exact magnitudes. | Teacher-only replacement; no learner workload/page changes. | Direction outward at all points; magnitude increases with radius; retain exact reported values and rounding note; no interpolation. | D1; exact-value/rounding and page-fit checks | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C2C1-VIS03` | Heavy Hands; S T8 p5, A T8 p8, AK T8 p4 | Missing criterion and two design responses are mainly prose/table. | 6 · Specification/verification | Requirement flow: midpoint-only rule → missing across-bed criterion → two proposals → monitored verification. | Preserve criterion, constraint and comparison fields; synchronize AK. | Do not invent tolerance; GC-1445 is not universal; present readings are not completed tests. | SV1; field/parity and no-new-number checks | `VERIFIED-FAMILY · 70/70 SPECIFICATION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 4d181aa ACCEPTED` |
| `C2C2-VIS01` | The Missing Dance; S T3 p3, A T3 p3 | Accurate but basic poricidal-cone SVG. | 7 · Biological/structural cutaway | Cleaner technical botanical cross-section with cut plane, open pores and mature retained pollen directly labeled. | Same figure footprint and text/table backup; no new learner action. | Pores already present, not blocked/sealed; 98% viable pollen retained; Earth buzz pollination distinct from fictional coupling. | CU1; direct-label/alt and prohibited-claim checks | `PLANNED` |
| `C2C2-VIS02` | The Missing Dance; S T6 p5, A T6 p6, AK T6 p3 | Generic condition/mechanism/effect stage model. | 2 · Causal mechanism/pathway | Failure path: sealed garden → no coupled vibration → pollen retained → buds abort → no fruit, with explicit missing-event node. | Preserve existing diagnosis, rejection and two model-stage fields; sync AK. | Near 124 Hz is insufficient without amplitude, duration and coupling; do not equate bee gripping with airborne coupling. | mechanism primitive; field/parity and boundary checks | `VERIFIED-FAMILY · 76/76 FAMILY STATIC PASS · 2321/2321 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · aa4eeac ACCEPTED` |
| `C2C2-VIS03` | The Missing Dance; S T8 p6, A T8 p8, AK T8 p4 | Four setting prompts followed by trial prose. | 8 · Intervention comparison/trial workflow | Four-control engineering panel—frequency, amplitude, duration, coupling—feeding release measurement, damage limit and stop rule. | Preserve all setting and trial fields; keep high-level monitored-test footprint. | 124 Hz is “near strongest release,” not a universal or sufficient prescription; no invented amplitude/duration. | IC1/SV1; exact qualifier and response tests | `PLANNED` |
| `C2C3-VIS01` | Wrong Color of Light; S T2 p2, A T2 p2 | Accurate discrete bars with correct labels but limited telemetry hierarchy. | 1 · Technical telemetry/data | GRO-9 discrete spectral-output diagnostic with four category rails and explicit category/inequality encoding. | Replace existing repeated figure at same height; table remains accessible backup. | Red 62% at 620–680; blue 18% at 440–490; broad 15%; blue-green <5% at 490–560; no interpolation/continuous curve. | D1; exact bins, inequality, DOM table and alt checks | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C2C3-VIS02` | Wrong Color of Light; S T3 p3, A T3 p3 | Accurate band overlay but measurement/status hierarchy can be clearer. | 1 · Technical telemetry/data | Measurement-overlay panel: discrete fixture bands against the 460–540 nm strongest-response band, with “outside unspecified ≠ zero.” | Same footprint and backup table; sync S/A. | Do not imply continuous response, geometric overlap calculation, or zero response outside band. | D1 overlay variant; prohibited-curve and inequality checks | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C2C3-VIS03` | Wrong Color of Light; S T6 p4 + T8 p5, A T6 p6 + T8 p8, AK T6 p3 + T8 p4 | Generic five-stage mechanism and separate prose procurement task. | 2 + 6 · Mechanism/specification | Shared spectral-match grammar connects poor match → lower captured energy → reduced growth/pigment replacement, then spectrum criterion + intensity criterion + monitored validation. | Do not merge tasks or pages; use related panels across existing footprints and preserve all fields. | Total PAR 280 remains adequate; response outside 460–540 unspecified; prediction remains a trial hypothesis. | mechanism + SV1; cross-task consistency and full field tests | `VERIFIED-FAMILY · 85/85 FAMILY STATIC PASS · 2324/2324 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 79a7c80 ACCEPTED` |
| `C2C4-VIS01` | Silent Grove; S T3 p3, A T3 p3 | Correct but plain same-total sleep-pattern teaching example. | 3 · Timeline/event log | Cleaner discrete 24-hour comparison with identical totals, distinct block patterns and an unmistakable “teaching example—not grove data” band. | Replace existing figure only; no new action or data. | Example values are illustrative, not grove measurements; no curve or biological claim. | TL1; status-label/alt and no-case-data confusion check | `VERIFIED-FAMILY · 44/44 TIMELINE STATIC PASS · 2339/2339 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 73e8496 ACCEPTED` |
| `C2C4-VIS02` | Silent Grove; S T3 p3, A T3 p3, AK T3 p1 where summarized | The exact within-cycle record is a conventional table with little visual distinction among light, dark, reported and unreported blocks. | 1 · Technical telemetry/data | Preserve the semantic table as a discrete 24-hour telemetry panel; distinguish light/dark schedule blocks and reported/unreported signal states through pattern, border weight and direct text, with no connecting curve. | Restyle the existing S/A Table 5 in place; retain all six rows, exact table semantics and the concise AK explanation. | Current 24/0; previous 18/6; healthy 40–80 ppb; current 0.0 ppb is threshold result; unreported blocks stay missing. | D1 timeline hybrid; exact-value/missing-data checks | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C2C4-VIS03` | Silent Grove; S T8 p6, A T8 p8, AK T8 p4 | Schedule requirements and monitored trial are prose/table led. | 6 · Specification/verification | Specification panel separating minimum evidence, six-hour historical schedule, stability criterion, power constraint, monitoring and stop rule. | Preserve all design fields and accepted response space; synchronize AK. | Five-hour minimum ≠ preferred design; successful schedule has six dark hours; 40–80 remains a range; no guaranteed recovery. | SV1; cross-edition acceptance and numeric checks | `VERIFIED-FAMILY · 105/105 SPECIFICATION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 8433392 ACCEPTED` |
| `C2C5-VIS01` | Too Clean a Room; S T2 p2, A T2 p2 | Accurate whole-mm rain-gauge analogy is visually basic. | 1 · Technical telemetry/data | Instrument-resolution figure with two sub-threshold inputs yielding the same reported bin and an explicit “teaching example—not vault data” status. | Replace figure at same height; preserve questions/table. | Detection bound analogy only; vault `<0.01 mGy/day` is not literal zero or exactly 0.01. | D1 instrument variant; inequality/status and alt checks | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C2C5-VIS02` | Too Clean a Room; S T3 p3, A T3 p3 | Accurate six discrete bars with limited production-monitor hierarchy. | 1 · Technical telemetry/data | Six-month SAA production-monitor display with direct values and no interpolation. | Replace existing repeated figure at same footprint; table remains. | Six discrete monthly values only; draw nothing between months; preserve baseline definition. | D1; exact-value/DOM and no-line checks | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C2C5-VIS03` | Too Clean a Room; S T5 p5 + T7 p7, A T5 p5 + T7 p7, AK T5 p4 + T7 p5 | Generic pathway and separate dense trial-requirements table. | 2 + 8 · Mechanism/trial workflow | Species-specific signal → pathway → product panel paired with high-level authorization → control → dosimetry/production → staged trial → stop workflow. | Keep tasks/pages separate; preserve diagnosis fields, pathway blanks and all trial requirements. | `<0.01 mGy/day` bound; homeworld ~8.4 and Rhessi ~12 are different contexts; mGy ≠ sievert; two conditions do not form a curve; non-operational only. | mechanism + IC1; unit, context, safety and response checks | `VERIFIED-FAMILY · 94/94 FAMILY STATIC PASS · 2327/2327 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · 7be2f42 ACCEPTED` |
| `C2C6-VIS01` | The First Garden; S T2 p2, A T2 p2 | Accurate simple plan-view patch diagram. | 1 · Technical telemetry/data | SAA soil-survey diagnostic with discrete abundance zones, sharp boundary and trace inter-patch ground. | Replace existing figure only; same caption/table backup and height. | Approximately 4–6 m remains a range; trace ≠ absent; pattern is not a map/not to scale; no patch spacing invented. | D1 spatial variant; range/status/alt checks | `VERIFIED-FAMILY · 36/36 FAMILY STATIC PASS · 2298/2298 BROWSER PASS` |
| `C2C6-VIS02` | The First Garden; S T5 p5, A T5 p5, AK T5 p4 | Generic five-stage pathway. | 2 · Causal mechanism/pathway | Candidate pathway with an explicit persistent `CANDIDATE · NOT ESTABLISHED` status rail from construction history through possible partnership loss to surveyed pattern. | Preserve fixed stages, three blanks, exact bank and model-limit response; sync AK. | Best-supported candidate only; no wood-wide-web/mother-tree/guaranteed-inoculation claims. | mechanism/status primitive; bank, qualifier and persistence checks | `VERIFIED-FAMILY · 103/103 FAMILY STATIC PASS · 2330/2330 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 · d8886b5 ACCEPTED` |
| `C2C6-VIS03` | The First Garden; S T7 p6, A T7 p7, AK T7 p5, T support p4 | Trial requirements are a long table; decision sequence is implicit. | 8 · Intervention comparison/trial workflow | Screened ecological workflow: identify → screen → approve → replicated treated + untreated plots → monitor colonization/performance/spread → conditional expansion. | Preserve all requirement fields and no-product/no-species instruction; synchronize AK and Teacher explanation. | Do not name treatment/product/organism; within-world transfer is not risk-free; no guaranteed cure; expand only if evidence supports. | IC1; safety-language, field/parity and conditionality checks | `PLANNED` |

## 8. Reusable visual grammar and smallest primitive set

No new family is required. The 35 candidates fit the eight established families. Hybrid rows
combine two established families without creating a ninth.

| Family | Findings | Count | Shared grammar |
|---|---|---:|---|
| 1 · Technical telemetry / data display | C1C3-VIS01–02; C2C1-VIS02; C2C3-VIS01–02; C2C4-VIS02; C2C5-VIS01–02; C2C6-VIS01 | 9 | framed data viewport, exact direct labels, discrete rails/bars/bins, unit/status band, no invented interpolation |
| 2 · Causal mechanism / pathway | C1C1-VIS01; C1C2-VIS01; C1C3-VIS03; C1C4-VIS02; C1C5-VIS01; C1C6-VIS02; C1C7-VIS02; C2C2-VIS02; C2C3-VIS03; C2C5-VIS03; C2C6-VIS02 | 11 | numbered/status nodes, labeled connectors, horizontal and Accessible vertical variants, evidence-status rail |
| 3 · Timeline / event log | C1C4-VIS01; C1C6-VIS01; C2C4-VIS01 | 3 | single direction, discrete event nodes, relative/illustrative status, no false proportionality |
| 4 · Evidence-convergence map | C1C5-VIS02; C1C7-VIS01 | 2 | independent source channels, contribution/limit separation, qualified convergence node |
| 5 · Engineering control loop | C1C4-VIS03 | 1 | sensor, comparator, actuator, process, labeled feedback |
| 6 · Specification / verification panel | C1C5-VIS03; C2C1-VIS03; C2C3-VIS03; C2C4-VIS03 | 4 | need/criterion/constraint/verification/stop hierarchy |
| 7 · Biological / structural cutaway | C2C1-VIS01; C2C2-VIS01 | 2 | flat section, cut-plane cue, direct anatomy labels, pattern/scale status |
| 8 · Intervention comparison / trial workflow | C1C6-VIS03; C1C7-VIS03; C2C2-VIS03; C2C5-VIS03; C2C6-VIS03 | 5 | options or gated steps, evidence fit, controls, monitoring, stop/conditional decision |

Counts total 37 family assignments because two hybrid findings (`C2C3-VIS03` and
`C2C5-VIS03`) intentionally use two established families; the unique finding count remains 35.

Smallest reusable primitive/component set:

- **P1 Figure shell:** thin technical frame, 3 px radius, white surface, governed padding.
- **P2 Metadata/status band:** concise caption, source/evidence/scale status in JetBrains Mono.
- **P3 Line system:** primary/secondary/accent weights; observed solid, inferred dashed,
  fictional/hypothetical dotted with text.
- **P4 Direct label:** short label, optional light leader, minimum print size.
- **P5 Status chip:** text + shape/pattern; never color only.
- **P6 Connector:** orthogonal default, compact arrowhead, explicit relationship verb where needed.
- **D1 Discrete data rail/bar/bin:** exact DOM text value, pattern fallback, no generated raster.
- **TL1 Event node/rail:** fixed reading direction and explicit relative/illustrative status.
- **EC1 Convergence channel:** source → contribution/limit → qualified synthesis.
- **CL1 Control node/feedback connector.**
- **SV1 Requirement row/gate:** criterion, constraint, verification, stop/decision.
- **CU1 Cutaway region/leader.**
- **IC1 Trial/option card:** evidence fit, control, measurement, stop/conditional next step.

Implementation should reuse class contracts and SVG conventions, not create a framework that
forces every case through one renderer. A unique deterministic SVG may remain local when its
geometry is genuinely unique.

## 9. Synchronized-edition policy

When S, A and AK contain the same learner-completed model, one semantic structure governs:

- identical stage count, terms, relationship meaning and response IDs;
- horizontal standard/AK layout may pair with a vertical Accessible layout;
- AK visibly completes every learner visual/status subpart;
- Teacher content receives a duplicate figure only when the accepted source already contains
  one or when it materially improves facilitation without changing pagination;
- quantitative figures retain a text/table backup and exact DOM values;
- a non-keyable explanatory figure need not be added to AK solely for decorative parity.

## 10. Production order

1. Commit this accepted-baseline-bound plan.
2. Establish P1–P6 and D1 through the high-leverage deterministic telemetry pilots
   `C1C3-VIS01` and `C2C3-VIS01`; validate exact values, inequalities, grayscale and page fit.
3. Complete Family 1 across C1C3, C2C1, C2C3, C2C4, C2C5 and C2C6.
4. Establish the horizontal/Accessible-vertical mechanism grammar and complete Family 2.
5. Complete timeline/event logs, then evidence convergence and the control loop.
6. Complete specification and intervention/trial panels using shared gate/monitor primitives.
7. Complete the two deterministic structural cutaways.
8. Resolve C1C1-GS01 and the two tracked grayscale token/fill items as a system pass.
9. Run cross-case visual consistency review and the full non-PDF regression.

This order maximizes shared leverage while testing the strictest data-discipline cases early.

## 11. Validation cadence

Focused development:

- source-hash/package integrity for each changed package;
- case-scoped static validators and relevant mutation suite;
- browser page-fit and figure-placement checks for changed role/page/grayscale states;
- exact values, units, inequalities, ranges and qualifiers asserted from DOM text;
- response/fill persistence when a learner-completed model is touched;
- Student/Accessible/AK subpart parity;
- `git diff --check`.

Family gate:

- every changed case in color and grayscale;
- no overflow, clipping, figure-label collision or hidden caption/description;
- no JavaScript errors;
- lifecycle-neutral load announcements unchanged;
- owner-accepted Teacher page geometry unchanged;
- visual family consistency checklist.

Periodic/final system gate:

- corrective-aware canonical structure;
- release integrity as applicable to corrective candidates;
- layout overrides;
- quality contract v3;
- accessibility contract v2;
- lifecycle tests and corrective-candidate contract;
- full browser harness: current accepted executable baseline **2324/2324 PASS, 0 JavaScript errors**;
- `git diff --check`.

Frozen-release assertions remain `RELEASE-BASELINE-PENDING`; they are not re-pinned here.
No automated PDF generation, comparison, debugging or gate is part of this plan.
When the production container has no installed Chrome, use the read-only run/report prompt in
`SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md`; it does not authorize baseline edits.

## 12. Owner decisions

**No owner decision is required at the planning gate.** The proposed work uses the approved
visual language, existing eight-family taxonomy, deterministic methods and current worksheet
footprints.

Stop and request an owner decision only if implementation proves that a candidate requires a
materially new visual language, curriculum/science change, substantial architecture or page-count
change, new lore, reversal of an accepted correctness decision, or a long-term asset dependency.

## 13. HHH inheritance

HHH should inherit the primitive contracts and family patterns, not SSS case-specific content.
Reusable outputs from this phase are:

- a deterministic figure shell/status/caption contract;
- grayscale-safe exact-data rails and discrete records;
- horizontal and Accessible-vertical mechanism/pathway structures;
- relative event-log treatment;
- qualified evidence convergence;
- engineering control-loop notation;
- specification/verification and monitored-trial gates;
- flat cutaway conventions;
- validation rules for data precision, evidence status, cross-edition visual parity and fixed
  geometry.

These are additions to the existing shared Visual Style Guide, not a replacement visual system.
