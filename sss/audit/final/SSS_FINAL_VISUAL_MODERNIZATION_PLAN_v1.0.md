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

## 3. Exact inventory reconciliation

The current remediation register contains exactly **36 findings classified
`DEFERRED-VISUAL`**:

- **35 numbered `VIS` figure/diagram/data-display candidates** — exactly reconciled to the
  discovery catalog; none is missing and none is duplicated.
- **1 numbered grayscale finding, `C1C1-GS01`**.

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
the full non-PDF browser regression against **2292/2292 PASS and 0 JavaScript errors**.

## 5. Grayscale-system work

| Finding / item | Case | Current state | Modernization | Method | Constraints and validation | Status |
|---|---|---|---|---|---|---|
| `C1C1-GS01` | C1 Case 01 — ISS Greenhouse | Grayscale variables change, but neutral/optional callouts retain tint and `.callout-success` uses hard-coded `#e9f3ed`. | Neutralize rendered callout surfaces in grayscale while retaining border/value hierarchy; update the inherited-tint browser expectation only after the rendered count reaches zero. | deterministic CSS | Do not rewrite dormant tokens without maintenance value; verify all four roles, color and grayscale, page geometry, contrast, and zero tint. | `PLANNED · FORMAL FINDING` |
| tracked status §5.3 | C1 Case 02 — Lunar Greenhouse | Rendered grayscale passes; some declared palette tokens are dormant and not neutralized. | Trace token reachability; neutralize only tokens that can reach printable components or consolidate them into governed grayscale values. | deterministic CSS audit | Must not turn a passing rendered state into blanket low-contrast gray; zero new tinted rendered surfaces. | `PLANNED · UNNUMBERED BACKLOG ITEM` |
| tracked status §5.3 | C1 Case 06 — First Contact Protocol | Grayscale override exists, but the accepted handoff records token/fill coverage as visual backlog. | Audit all printable fills against the override set and close any reachable gap using Cool Mission Gray hierarchy. | deterministic CSS audit | Preserve timing/model/data distinction with value, border, label and pattern; no color-only meaning. | `PLANNED · UNNUMBERED BACKLOG ITEM` |

## 6. Candidate production matrix — Campaign 1

| Finding | Case; editions; task/page | Current visual and problem | Family | Proposed modernization and method | Footprint / synchronization | Science/data constraints | Dependency and validation | Status |
|---|---|---|---|---|---|---|---|---|
| `C1C1-VIS01` | ISS Greenhouse; S T5 p2, A T5 p3, AK T5 p2 | Two plain comparison cards; the gravity-sensing relationship is text-heavy and visually basic. | 2 · Causal mechanism/pathway | Matched statocyte/root cutaways with settled/unsettled statolith states, direction cue, and root outcome; deterministic SVG + existing writable phrase fields. | Same footprint; synchronize S/A/AK blanks and completed exemplar; T wording only. | Do not imply roots become random or respond only to gravity; fictional case context vs established gravitropism remains explicit. | primitives P1–P6; mechanism and fill-persistence tests | `PLANNED` |
| `C1C2-VIS01` | Lunar Greenhouse; S T3 p1, A T3 p2, AK T3 p1 | Conventional six-box flow; A uses a separate plain vertical list. | 2 · Causal mechanism/pathway | Reproductive telemetry rail: anther/pollen → physical agitation → stigma → pollen tube → fertilization → fruit, with numbered nodes and failure/interruption status; deterministic HTML/CSS/SVG. | Preserve six exact bank entries and fields; horizontal S/AK and vertical A remain one grammar. | Pores/structures downstream may remain capable; failed Step 2 interrupts rather than destroys them. | P1–P6; exact-bank parity; AK failure-state check | `PLANNED` |
| `C1C3-VIS01` | Mars Habitat; S T2 p1, A T2 p2, T reference p4, AK T2 p1 | Accurate ordinary four-bar transmission graph repeated across roles. | 1 · Technical telemetry/data | Four-channel optical-transmission scan with direct percentages, patterned rails, and low-transmission flags; deterministic SVG. | Preserve current figure height and table backup; synchronize all existing instances. | Four discrete bands only; no continuous spectrum or interpolated values; retain 92%, 88%, 31%, 12%. | P1–P5, D1; numeric DOM assertions and extended description | `PLANNED · FAMILY PILOT` |
| `C1C3-VIS02` | Mars Habitat; S T3 p2, A T3 p3, AK T3 p1 | Boxed “280 adequate” plus repeated mini bars; comparison is correct but visually ordinary. | 1 · Technical telemetry/data | Dual-channel diagnostic: photon quantity 280 PPFD `ADEQUATE` vs four-rail spectrum `UNEVEN`, with `Quantity ≠ Distribution`; deterministic HTML/SVG. | Same footprint; synchronize S/A and concise AK treatment. | PPFD quantity must not be presented as spectral adequacy; preserve units and exact discrete values. | C1C3-VIS01 rail primitive; numeric/parity checks | `PLANNED` |
| `C1C3-VIS03` | Mars Habitat; S T6 p3, A T6 p5, AK T6 p3 | Generic five-stage rectangles. | 2 · Causal mechanism/pathway | Technical glyph chain: collector → wrong BP-4 filter → selective loss → disrupted new chlorophyll production → pale new growth; deterministic HTML/SVG. | Preserve five-stage exact-match bank, blank stages and vertical A variant. | Do not claim an unsupported universal chlorophyll mechanism; retain case wording and corrected 700 nm boundary. | mechanism primitive; bank/order/persistence checks | `PLANNED` |
| `C1C4-VIS01` | Hayes Orbital Station; S T2 p1, A T2 p2, AK T2 p1 | Five numbered blanks connected by plain arrows. | 3 · Timeline/event log | SAA incident log with verified relative-event slots and event-type markers; deterministic HTML/CSS. | Same five writable positions; A stays vertical; AK completes identical log. | Relative timing only; do not invent mission days or proportional spacing. | P1–P5, TL1; exact event-bank/parity checks | `PLANNED` |
| `C1C4-VIS02` | Hayes Orbital Station; S T5 p3, A T5 p5, AK T5 p3 | Six-stage snake layout; reading direction requires prose. | 2 · Causal mechanism/pathway | Immediate closed fault loop with directional connectors and explicit repeat link. | Preserve six exact stages/fields and A vertical reading order. | Qualitative recurrence; no invented light dose, density or crash interval beyond reported 6–8 days. | loop variant of mechanism primitive; connector/read-order tests | `PLANNED` |
| `C1C4-VIS03` | Hayes Orbital Station; S T7 p4, A T7 p7, AK T7 p4 | Four equal text boxes in a linear row. | 5 · Engineering control loop | Sensor → comparator → independent actuator → reactor, with performance feedback to verification; deterministic SVG/HTML. | Keep two learner response fields and current page; complete AK treatment without new graded actions. | Independent light control and monitored response; do not generalize continuous-light failure to all cultures. | P1–P6, CL1; feedback-label and response tests | `PLANNED` |
| `C1C5-VIS01` | Europa Bunker; S T5 p3, A T5 p5, AK T5 p3 | Seven-stage snake of text boxes. | 2 · Causal mechanism/pathway | Qualified hazard pathway visually separating environment, modeled interaction, exposure evidence, evidence limit, biological evidence, growth consequence and convergence; deterministic HTML/SVG. | Preserve seven exact bank entries and current blanks; A vertical; AK complete. | Modeled secondary radiation ≠ measured; exposure ≠ damage; abnormalities are consistent with damage; no exact quantities. | mechanism/status primitives; phrase, qualifier and persistence tests | `PLANNED` |
| `C1C5-VIS02` | Europa Bunker; S T3 p2, A T3 p3, AK T3 p2 | Four-row source table; convergence remains implicit. | 4 · Evidence-convergence map | Four labeled channels—Crew, Sensors, Plants, Logs—feeding a qualified “best-supported” diagnosis node while retaining contribution writing areas. | Recompose within table footprint; preserve all contribution fields and AK exemplars. | No single clue proves radiation; sensor exposure and biological evidence stay distinct. | P1–P6, EC1; field-count, AK and causal-language checks | `PLANNED` |
| `C1C5-VIS03` | Europa Bunker; S T8 p4, A T8 p7, AK T8 p4 | Need/criteria/constraints/verification organizer with ordinary panels. | 6 · Specification/verification | Compact mission requirements panel with Need, Criteria, Constraints, Verification and monitoring gate; deterministic HTML/CSS. | Preserve every existing writable field and page; sync AK completion. | No crop-safe threshold or guaranteed shielding solution may be invented. | P1–P5, SV1; field/parity and qualifier checks | `PLANNED` |
| `C1C6-VIS01` | First Contact Protocol; S T3 p2, A T3 p2; T/AK reference where present | Small three-block timing strip embedded with evidence. | 3 · Timeline/event log | Compact event/telemetry strip: docking at 72.4 h ago → 18 min → last signal at 72.1 h ago. | No new response control; preserve evidence-card footprint and all repeated values. | Larger “hours ago” is earlier; 0.3 h = 18 min; timing is correlation, not proof. | TL1; exact-text/numeric and page-fit assertions | `PLANNED` |
| `C1C6-VIS02` | First Contact Protocol; S T4 p2, A T4 p3, AK T4 p2 | Four generic stage cards. | 2 · Causal mechanism/pathway | Bounded four-channel systems model: atmosphere → signal persistence → fictional network response → partnership outcome, with labeled transitions and state markers. | Preserve exact phrase bank and response IDs; horizontal S/AK, vertical A. | Earth signalling context must remain distinct from fictional volatile/network dormancy system. | mechanism/system-boundary primitive; exact-bank, fiction-status and persistence checks | `PLANNED` |
| `C1C6-VIS03` | First Contact Protocol; S T6 p3, A T6 p5, AK T6 p3 | Three-row intervention table. | 8 · Intervention comparison/trial workflow | Decision panel distinguishing unsafe shutdown, no change, and reversible selective treatment; include evidence fit, safety constraint and monitor rail. | Preserve recommendation and monitoring fields; identical option order across S/A/AK. | Do not imply disabling life support is safe; preserve pressure, breathable-gas and contaminant controls. | P1–P5, IC1; option/parity and response tests | `PLANNED` |
| `C1C7-VIS01` | The Gift; S T2 p2, A T2 p2, AK T2 p2 | Primary-condition and trace-context information is tabular; `99.7%` visually dominates. | 4 · Evidence-convergence/diagnostic map | Matched diagnostic channels separating “primary targets match” from “trace biological context incomplete”, converging only on a qualified question. | Preserve evidence/limit writing areas and AK exemplar; no page-count change. | 99.7% is not complete ecosystem similarity; 12 and 847+ identifier sets differ and cannot be divided. | EC1 + comparison primitive; prohibited-inference checks | `PLANNED` |
| `C1C7-VIS02` | The Gift; S T4 p3, A T4 p4, T reference p4, AK T4 p3 | Six-stage generic chain with status fields. | 2 · Causal mechanism/pathway | Biological systems schematic: mature source → incidental cue → carrier/path → receptors → commitment → young symbiosis, with supply/status markers. | Preserve six phrases, every status/X control and AK completed statuses; horizontal/vertical variants. | Fictional system; under-3-m supported path; no safe dose/structure claim; commitment/reversibility distinction retained. | mechanism + status primitive; exact subpart, persistence and fiction checks | `PLANNED` |
| `C1C7-VIS03` | The Gift; S T7 p5, A T7 p7, AK T7 p5 | Dense intervention matrix; story rank competes with evidence. | 8 · Intervention comparison/trial workflow | Three-route decision/monitoring matrix with explicit evidence fit, controls, reversibility/commitment, monitoring and uncertainty hierarchy. | Preserve route choice, evidence, monitor/stop and prediction fields; points remain subordinate story ranks. | Story scores are not scientific results; no inferred dose, purity, synthesis or safety. | IC1; response/AK parity and label hierarchy checks | `PLANNED` |

## 7. Candidate production matrix — Campaign 2

| Finding | Case; editions; task/page | Current visual and problem | Family | Proposed modernization and method | Footprint / synchronization | Science/data constraints | Dependency and validation | Status |
|---|---|---|---|---|---|---|---|---|
| `C2C1-VIS01` | Heavy Hands; S T4 p3, A T4 p4 | Three simple tuber panels and span bars. | 7 · Biological/structural cutaway | Matched radial-bed cross-sections showing a small/medium/large organ spanning more of the same 20 cm bed depth; deterministic SVG. | Replace existing figure only; retain table/text support and exact height. | Qualitative size dependence only; no deformation amounts or invented organ dimensions. | P1–P6, CU1; not-to-scale/alt and no-new-number check | `PLANNED` |
| `C2C1-VIS02` | Heavy Hands; T reference p4 | Three-point radial profile is a basic Teacher-only schematic. | 1 · Technical telemetry/data | Centrifuge telemetry profile with three reported radii, outward direction arrows and direct exact magnitudes. | Teacher-only replacement; no learner workload/page changes. | Direction outward at all points; magnitude increases with radius; retain exact reported values and rounding note; no interpolation. | D1; exact-value/rounding and page-fit checks | `PLANNED` |
| `C2C1-VIS03` | Heavy Hands; S T8 p5, A T8 p8, AK T8 p4 | Missing criterion and two design responses are mainly prose/table. | 6 · Specification/verification | Requirement flow: midpoint-only rule → missing across-bed criterion → two proposals → monitored verification. | Preserve criterion, constraint and comparison fields; synchronize AK. | Do not invent tolerance; GC-1445 is not universal; present readings are not completed tests. | SV1; field/parity and no-new-number checks | `PLANNED` |
| `C2C2-VIS01` | The Missing Dance; S T3 p3, A T3 p3 | Accurate but basic poricidal-cone SVG. | 7 · Biological/structural cutaway | Cleaner technical botanical cross-section with cut plane, open pores and mature retained pollen directly labeled. | Same figure footprint and text/table backup; no new learner action. | Pores already present, not blocked/sealed; 98% viable pollen retained; Earth buzz pollination distinct from fictional coupling. | CU1; direct-label/alt and prohibited-claim checks | `PLANNED` |
| `C2C2-VIS02` | The Missing Dance; S T6 p5, A T6 p6, AK T6 p3 | Generic condition/mechanism/effect stage model. | 2 · Causal mechanism/pathway | Failure path: sealed garden → no coupled vibration → pollen retained → buds abort → no fruit, with explicit missing-event node. | Preserve existing diagnosis, rejection and two model-stage fields; sync AK. | Near 124 Hz is insufficient without amplitude, duration and coupling; do not equate bee gripping with airborne coupling. | mechanism primitive; field/parity and boundary checks | `PLANNED` |
| `C2C2-VIS03` | The Missing Dance; S T8 p6, A T8 p8, AK T8 p4 | Four setting prompts followed by trial prose. | 8 · Intervention comparison/trial workflow | Four-control engineering panel—frequency, amplitude, duration, coupling—feeding release measurement, damage limit and stop rule. | Preserve all setting and trial fields; keep high-level monitored-test footprint. | 124 Hz is “near strongest release,” not a universal or sufficient prescription; no invented amplitude/duration. | IC1/SV1; exact qualifier and response tests | `PLANNED` |
| `C2C3-VIS01` | Wrong Color of Light; S T2 p2, A T2 p2 | Accurate discrete bars with correct labels but limited telemetry hierarchy. | 1 · Technical telemetry/data | GRO-9 discrete spectral-output diagnostic with four category rails and explicit category/inequality encoding. | Replace existing repeated figure at same height; table remains accessible backup. | Red 62% at 620–680; blue 18% at 440–490; broad 15%; blue-green <5% at 490–560; no interpolation/continuous curve. | D1; exact bins, inequality, DOM table and alt checks | `PLANNED · FAMILY PILOT` |
| `C2C3-VIS02` | Wrong Color of Light; S T3 p3, A T3 p3 | Accurate band overlay but measurement/status hierarchy can be clearer. | 1 · Technical telemetry/data | Measurement-overlay panel: discrete fixture bands against the 460–540 nm strongest-response band, with “outside unspecified ≠ zero.” | Same footprint and backup table; sync S/A. | Do not imply continuous response, geometric overlap calculation, or zero response outside band. | D1 overlay variant; prohibited-curve and inequality checks | `PLANNED` |
| `C2C3-VIS03` | Wrong Color of Light; S T6 p4 + T8 p5, A T6 p6 + T8 p8, AK T6 p3 + T8 p4 | Generic five-stage mechanism and separate prose procurement task. | 2 + 6 · Mechanism/specification | Shared spectral-match grammar connects poor match → lower captured energy → reduced growth/pigment replacement, then spectrum criterion + intensity criterion + monitored validation. | Do not merge tasks or pages; use related panels across existing footprints and preserve all fields. | Total PAR 280 remains adequate; response outside 460–540 unspecified; prediction remains a trial hypothesis. | mechanism + SV1; cross-task consistency and full field tests | `PLANNED` |
| `C2C4-VIS01` | Silent Grove; S T3 p3, A T3 p3 | Correct but plain same-total sleep-pattern teaching example. | 3 · Timeline/event log | Cleaner discrete 24-hour comparison with identical totals, distinct block patterns and an unmistakable “teaching example—not grove data” band. | Replace existing figure only; no new action or data. | Example values are illustrative, not grove measurements; no curve or biological claim. | TL1; status-label/alt and no-case-data confusion check | `PLANNED` |
| `C2C4-VIS02` | Silent Grove; S T2 p2, A T2 p2, AK T2 p1 where summarized | Current cycle evidence is spread across tables/text. | 1 · Technical telemetry/data | Discrete 24-hour light/dark and reported-signal record with unreported blocks explicitly marked; no connecting curve. | Fit beside/within current task evidence; preserve tables as accessible source. | Current 24/0; previous 18/6; healthy 40–80 ppb; current 0.0 ppb is threshold result; unreported blocks stay missing. | D1 timeline hybrid; exact-value/missing-data checks | `PLANNED` |
| `C2C4-VIS03` | Silent Grove; S T8 p6, A T8 p8, AK T8 p4 | Schedule requirements and monitored trial are prose/table led. | 6 · Specification/verification | Specification panel separating minimum evidence, six-hour historical schedule, stability criterion, power constraint, monitoring and stop rule. | Preserve all design fields and accepted response space; synchronize AK. | Five-hour minimum ≠ preferred design; successful schedule has six dark hours; 40–80 remains a range; no guaranteed recovery. | SV1; cross-edition acceptance and numeric checks | `PLANNED` |
| `C2C5-VIS01` | Too Clean a Room; S T2 p2, A T2 p2 | Accurate whole-mm rain-gauge analogy is visually basic. | 1 · Technical telemetry/data | Instrument-resolution figure with two sub-threshold inputs yielding the same reported bin and an explicit “teaching example—not vault data” status. | Replace figure at same height; preserve questions/table. | Detection bound analogy only; vault `<0.01 mGy/day` is not literal zero or exactly 0.01. | D1 instrument variant; inequality/status and alt checks | `PLANNED` |
| `C2C5-VIS02` | Too Clean a Room; S T3 p3, A T3 p3 | Accurate six discrete bars with limited production-monitor hierarchy. | 1 · Technical telemetry/data | Six-month SAA production-monitor display with direct values and no interpolation. | Replace existing repeated figure at same footprint; table remains. | Six discrete monthly values only; draw nothing between months; preserve baseline definition. | D1; exact-value/DOM and no-line checks | `PLANNED` |
| `C2C5-VIS03` | Too Clean a Room; S T5 p5 + T7 p7, A T5 p5 + T7 p7, AK T5 p4 + T7 p5 | Generic pathway and separate dense trial-requirements table. | 2 + 8 · Mechanism/trial workflow | Species-specific signal → pathway → product panel paired with high-level authorization → control → dosimetry/production → staged trial → stop workflow. | Keep tasks/pages separate; preserve diagnosis fields, pathway blanks and all trial requirements. | `<0.01 mGy/day` bound; homeworld ~8.4 and Rhessi ~12 are different contexts; mGy ≠ sievert; two conditions do not form a curve; non-operational only. | mechanism + IC1; unit, context, safety and response checks | `PLANNED` |
| `C2C6-VIS01` | The First Garden; S T2 p2, A T2 p2 | Accurate simple plan-view patch diagram. | 1 · Technical telemetry/data | SAA soil-survey diagnostic with discrete abundance zones, sharp boundary and trace inter-patch ground. | Replace existing figure only; same caption/table backup and height. | Approximately 4–6 m remains a range; trace ≠ absent; pattern is not a map/not to scale; no patch spacing invented. | D1 spatial variant; range/status/alt checks | `PLANNED` |
| `C2C6-VIS02` | The First Garden; S T5 p5, A T5 p5, AK T5 p4 | Generic five-stage pathway. | 2 · Causal mechanism/pathway | Candidate pathway with an explicit persistent `CANDIDATE · NOT ESTABLISHED` status rail from construction history through possible partnership loss to surveyed pattern. | Preserve fixed stages, three blanks, exact bank and model-limit response; sync AK. | Best-supported candidate only; no wood-wide-web/mother-tree/guaranteed-inoculation claims. | mechanism/status primitive; bank, qualifier and persistence checks | `PLANNED` |
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
- full browser harness: baseline **2292/2292 PASS, 0 JavaScript errors**;
- `git diff --check`.

Frozen-release assertions remain `RELEASE-BASELINE-PENDING`; they are not re-pinned here.
No automated PDF generation, comparison, debugging or gate is part of this plan.

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
