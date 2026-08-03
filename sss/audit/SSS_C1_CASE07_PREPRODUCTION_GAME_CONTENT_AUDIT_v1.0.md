# SSS Campaign 1 Case 07 — Pre-Production Game-Content Audit and Worksheet Crosswalk

**Version:** 1.0

**Audit date:** 2026-08-03

**Status:** Phase 1 complete; proposed frozen game baseline; curriculum production not begun

**Curriculum identity:** Campaign 1, Case 07 — The Gift

**Runtime identity:** alien2

**Traceability alias:** former source-development label Case 6b

## 1. Authority, scope, and protected baselines

This record implements the owner handoff for a pre-production audit only. It does not create, register, render, release, or imply release of a Case 07 curriculum package.

| Item | Audited value |
|---|---|
| Curriculum pre-audit local main | 7b41416b925bf78fb91cf30377e13421cb68650b |
| Curriculum pre-audit origin/main | 7b41416b925bf78fb91cf30377e13421cb68650b |
| Game pre-correction local main | d723fb9b8085905a6048575a2cb3bb0fce1d312b |
| Game pre-correction origin/main | d723fb9b8085905a6048575a2cb3bb0fce1d312b |
| Game post-correction commit | 530758235522ce110695a23feacea065ed370d08 |
| Proposed frozen Case 07 game baseline | 530758235522ce110695a23feacea065ed370d08 |
| Remote advancement beyond handoff | None in either repository |
| Compatibility determination | Exact match; no baseline conflict |

Cases 01–05 remain released core cases. Case 06 remains APPROVED_STABLE, synchronized, and frozen to game commit d723fb9b8085905a6048575a2cb3bb0fce1d312b. Its classroom sources, approval record, and release history were not changed.

### Governing curriculum sources consulted

- shared/curriculum-bible/SSS_HHH_CURRICULUM_BIBLE_v1.3.md and its retained predecessors
- shared/visual-style-guide/VISUAL_STYLE_GUIDE_v1.0.md and approved amendments, including Balanced Page Fill and Vertical Rhythm v1.0.2, Content Ordering and Accessible Flow v1.0.2, and Printable Page Identity v1.0.4
- shared/implementation/REPOSITORY_CURRICULUM_LIBRARY_ARCHITECTURE.md
- shared/implementation/CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md
- current case-package, registry, release-history, task-registry, and layout-override contracts
- sss/blueprint/SSS_CURRICULUM_BLUEPRINT_v1.0.md
- sss/audit/SSS_MASTER_AUDIT_v1.0.md
- approved Cases 01–06, with Cases 05–06 used as the latest native production and release-control references
- Case 06 owner approval, compact release record, task registry, and frozen classroom sources
- current Curriculum Editor and repository validation suites

The governing blueprint locks the Case 07 task identity as a compact Campaign 1 culmination: evidence synthesis, a systems diagram, missing-trigger CER, comparison to an earlier case, and an independent exit ticket. The audit preserves that design.

## 2. Runtime source of truth

### Controlling files

| File | Control |
|---|---|
| Space-Sprout-Sleuth/space_sprout_sleuth_data.js | Case 07 identity, location, briefing, four evidence sources, dialogue graph, flags, clue tags and summaries, diagnoses, hints, intervention options and scores, rank-up text, explanation, and authored victory text |
| Space-Sprout-Sleuth/index.html | clue acquisition and prerequisite evaluation, diagnosis gate and scoring, solution-choice persistence, resume behavior, unlock rules, rank progression, final-case narrative handoff, Campaign 1 completion, and Campaign 2 unlock messaging |
| Space-Sprout-Sleuth/tests/case07_content.test.js | deterministic content graph, reachability, science-language, arithmetic, timing, and intervention regression coverage |
| Space-Sprout-Sleuth/tests/case07_runtime_flow.test.js | deterministic unlock, diagnosis, resume, solution persistence, victory, rank, and campaign-transition regression coverage |

### Confirmed identity and placement

- Title: The Gift.
- Location: SAA Xenobiology Lab.
- Subtitle: L2 Station Hayes — Secure Cultivation Wing.
- Runtime ID: alien2.
- Former source label: Case 6b; corrected source comment now identifies Case 07 and retains the alias.
- Campaign position: seventh and final Campaign 1 runtime case.
- Four player-facing interactions: Consult Liaison, Scan Biomonitors, Examine Specimen, Decode Archives.

### Controlling flow

1. index.html:isCaseUnlocked(6) now requires a completed alien1 entry. A bare currentCase value cannot bypass Case 06.
2. The investigation engine starts each source at its start node, filters options by requirements, records visited nodes and flags, and awards revealsClue tags.
3. The Diagnose control remains blocked while cluesFound is less than caseData.clues.length. For Case 07, all four formal clues are therefore mandatory.
4. Only the germination_compound diagnosis is marked correct. Three distractors route to specific corrective hints and a score penalty.
5. Correct diagnosis records completion, then opens the three-option solutionChoice. Every option occurs after the four-clue diagnosis gate; synthesis also retains an explicit GERMINATION_COMPOUND requirement.
6. The chosen intervention is saved even when its bonus is zero. Resume returns a diagnosed case to the intervention screen if no option was chosen, or to the explanation after a choice; it no longer increments beyond the final case.
7. Explanation leads to the authored podAwakening and zelkethClosing sequence, then finishFinalCase. The final rank advances from Chief Sprout Sleuth to Xenobotanist, and showVictory persists campaign1Complete.
8. Campaign 1 victory displays an incoming-transmission notice that unlocks the existing game-side Campaign 2 entry. It does not claim that Campaign 2 curriculum exists.

### Complete interaction and state inventory

Every authored Case 07 node was inspected:

- crew: start, proximity_detail, canopy_reach, wake_up_call, solution_hint, proximity_option_early, network_signal_idea, earth_parallel_6b, isolated_germination, too_clean, add_compounds, trigger_discussion, compound_discussion, solution_proximity, solution_extract, solution_synthesize, wrong_damage, exit_neutral, exit_positive.
- sensors: start, pod_status, micro_stimuli, atmosphere, voc_gap, trigger_search, comparison, mature_growth_diff, distance_problem, replicate_compound, exit_neutral.
- plants: start, chambers, what_signal, chemical_trigger, membrane, receptors, earth_comparison, talk_to_pod, exit_neutral.
- logs: start, cultivation, germination, signal_chemistry, triggers, proximity_search, earth_parallels, exit_neutral.

The inspected source flags are zelketh_admitted_ignorance, zelketh_canopy_insight, zelketh_willing_to_help, zelketh_mother_tree_concept, zelketh_isolation_insight, zelketh_clean_air_again, zelketh_knows_compound, discussed_proximity_solution, discussed_extract_solution, discussed_synthesize_solution, saw_pod_status, pod_has_chemical_receptors, understood_voc_gap, saw_comparison, saw_proximity_data, examined_chambers, understood_chemical_trigger, examined_membrane, examined_receptors, earth_seed_comparison, talked_to_pod, read_cultivation, read_signal_chemistry, read_trigger_mechanism, read_proximity_requirements, and read_earth_parallels_6b. They record optional traversal but do not add hidden mandatory evidence.

Controlling completion state consists of caseState.cluesFound, nodesVisited, flags, wrongGuesses, diagnosed, and solutionIdx; completedCases uses caseId alien2; campaign completion uses campaign1Complete. Diagnosis IDs are germination_compound, wrong_light, transfer_damage, and human_microbes. Intervention IDs are proximity, extract, and synthesize.

## 3. Complete clue and reachability map

All four formal clues are essential because the global diagnosis gate requires all declared clues. There are no optional formal clues. Supporting nodes and flags are optional and ungraded.

| Source / interaction | Displayed route | Prerequisite | Award / internal tag | Status | Downstream use | Fallback route | Result / correction |
|---|---|---|---|---|---|---|---|
| Liaison / crew | Why near established growth specifically? → proximity_detail | None | Nearby mature growth is the historic operating context / PROXIMITY_REQUIRED | Essential | Opens range comparison; supports mature-network source and delivery reasoning | Have you ever germinated a pod away from mature growth? → isolated_germination | Reachable. Fallback reveal added so a second ordinary path awards the clue. |
| Biomonitors / sensors | Scan: Atmospheric analysis → atmosphere | None | Primary targets match; 12 of 847+ trace identifiers remain / MISSING_VOCS | Essential | Establishes matched-versus-missing comparison; weakens light and microbe distractors | Environmental comparison with Zhel'ora → comparison | Reachable. Comparison was made a second reveal route. Legacy internal tag retained for save compatibility; displayed wording now says trace biological compounds, not that the 890 Da cue is an ordinary VOC. |
| Specimen / plants | Look for receptor structures → receptors | None | Viable pod has dense cue-responsive membrane receptors / WAITING_FOR_TRIGGER | Essential | Distinguishes dormancy from death; links ligand to response | Examine chambers → What signal are they waiting for? → what_signal | Reachable. Two reveal nodes preserved. |
| Archives / logs | Search: Germination biology → germination | None | Archive identifies mature-network cue and receptor gate / GERMINATION_COMPOUND | Essential | Supports diagnosis and all intervention analysis | Search: Signal chemistry → signal_chemistry | Reachable. Signal-chemistry node was made a second reveal route. |

### Reachability totals

- Formal clues: 4 essential, 0 optional.
- Reachable: 4 of 4.
- Unreachable: 0.
- Reveal sites: 8 total, two per formal clue.
- Broken gotos: 0 across every Case 07 option.
- Unknown clue prerequisites: 0.
- Developer shortcuts required: 0.
- Diagnosis before all evidence: blocked by the four-clue gate.
- Premature solution reveal: corrected. The early docking option now requires GERMINATION_COMPOUND, and earlier “wake-up call” dialogue is framed as a hypothesis pending receptor and archive evidence.
- Softlock: corrected. A save after diagnosis resumes the unresolved choice or explanation instead of calling nextCase and moving beyond the final array element.
- Hint/recovery behavior: the Diagnose button reports “Need more evidence”; each mandatory clue has an ordinary second reveal route; wrong diagnoses return the player to investigation with evidence-specific feedback.

## 4. Evidence map

| Evidence category | Exact reachable runtime evidence | Status and justified inference | Stronger inference not justified |
|---|---|---|---|
| Mission problem | briefing | A contained, viable alien pod does not germinate after known primary targets are reproduced. | “Every biologically relevant condition matches.” |
| Conditions already matched | sensors.atmosphere; sensors.comparison | Primary gas targets, temperature, humidity, light spectrum, and pressure are within stated fictional tolerances. | The chamber recreates a living ecosystem or every unknown variable. |
| Viable rather than dead | sensors.pod_status; sensors.micro_stimuli; plants.chambers | Intact, primed structures respond to controlled stimuli. | Viability proves that germination must begin spontaneously. |
| Dormant or waiting | plants.receptors; plants.what_signal; clue WAITING_FOR_TRIGGER | Dense outward receptors and primed chambers support a cue-gated dormant state. | Receptor shape alone identifies a ligand, safe dose, or alien evolutionary history. |
| Primary atmosphere match | sensors.atmosphere | A 99.7% primary-condition similarity index explicitly excludes trace compounds. | A composite similarity score proves complete environmental identity. |
| Trace compounds do not match | sensors.atmosphere; sensors.comparison; sensors.voc_gap | The lab has 12 residual identifiers while the living cultivation area has 847+; the residual set does not match. | Every absent trace compound matters, or absence alone identifies the germination cue. |
| Proximity | crew.proximity_detail; sensors.mature_growth_diff; logs.cultivation; logs.proximity_search | Historic success occurs within 1–3 m along shared airflow; measured cue falls below threshold past 3 m. | Proximity itself proves nutrient transfer, kin recognition, or intentional communication. |
| Receptor evidence | sensors.micro_stimuli; plants.receptors | Selective response supports a ligand-trigger mechanism. | Preliminary binding response gives connectivity, stereochemistry, formulation, or safety. |
| Archive mechanism | logs.germination; logs.signal_chemistry; logs.triggers | Fictional records identify an incidental mature-network signaling byproduct interpreted by pod receptors as a cue. | The compound is deliberately “speaking” to pods or represents Earth plant behavior. |
| Missing variable | convergence of MISSING_VOCS, WAITING_FOR_TRIGGER, GERMINATION_COMPOUND | The best-supported missing variable is the specific cue, not the whole trace mixture. | One sensor line alone proves diagnosis. |
| Mature-network source | crew plus logs.signal_chemistry | Healthy mature growth is the verified natural source in the fictional archive. | An Earth “mother tree” analogy proves the source or mechanism. |
| Prior Case 06 connection | briefing; crew.too_clean; approved Case 06 evidence | Case 06 showed that human atmospheric processing can remove Zhel'ii signal compounds; Case 07 asks what an independently built lab never reproduced. | The two rooms have identical filtration histories or the same biological outcome. |
| Predicted germination | logs.triggers; intervention responses; victory.podAwakening | Sustained above-threshold exposure precedes receptor activation, commitment, chamber opening, and linked young-symbiosis development. | The response is instantaneous, universally safe, or reversible after commitment. |

## 5. Culminating reasoning chain

| Link | Reachable evidence and node | Weight | Justified inference | Boundary / status |
|---|---|---|---|---|
| Matched measured conditions | sensors.atmosphere; sensors.comparison | Essential | Known primary physical targets are not the differentiating variable. | Fictional game measurement. Does not mean a complete ecosystem was recreated. |
| → viable but dormant organism | sensors.pod_status plus plants.chambers/receptors | Essential | Lack of germination is better described as dormancy than death or transfer destruction. | Fictional anatomy and response. “Viable” does not reveal the missing cue by itself. |
| → missing trace biological signal | sensors.atmosphere/comparison plus MISSING_VOCS | Essential | The living chemical context is a productive missing-variable category. | Fictional measurement. The broad absence does not identify the active molecule. |
| → receptor/trigger evidence | plants.receptors/what_signal and sensors.micro_stimuli | Essential | A selective receptor-mediated cue is plausible and testable. | Fictional mechanism; response alone does not establish complete structure or dose. |
| → mature-network source | logs.germination/signal_chemistry plus crew.proximity_detail | Essential | The archive identifies the mature network as the natural source of the cue. | Fictional archive fact; Earth analogy is not proof. Case 06 supports plausibility of a Zhel'ii atmospheric signaling dependency. |
| → justified intervention | solutionChoice after all four clues | Essential culmination | Compare delivery routes using evidence fit, containment, verification, uncertainty, reversibility, and consent. | Speculative engineering extrapolation inside a fictional scenario. |
| → predicted germination response | logs.triggers plus selected response and victory | Supporting outcome | Above-threshold exposure predicts receptor activation, commitment, visible glow, chamber opening, and stabilization. | Fictional prediction and narrated outcome; timing is scenario evidence. |

## 6. Diagnosis and distractor map

The engine requires all four formal clues before any diagnosis may be submitted.

| Option | Apparent support | Contradicting evidence | Required clues | Expected feedback and runtime outcome | Correction |
|---|---|---|---|---|---|
| The viable pod is dormant because its receptors have not received the mature network’s specific germination cue. | Primary targets match; pod is viable; trace context is missing; dense receptors await a cue; archive names the mature-network source. | No audited evidence contradicts it. | All four through global gate | Correct; records completion and opens intervention comparison. | Label tightened to distinguish observation, mechanism, and source. |
| Artificial light lacks a critical wavelength. | Light can regulate germination in some Earth species. | Runtime says light spectrum is within fictional target tolerance; chemical receptors, trace-gap evidence, and archive mechanism converge elsewhere. | All four through global gate | Incorrect; hint identifies the matched-light and molecule evidence; −20 points. | Removed stale 99.1% claim and used the actual tolerance framing. |
| Transfer damaged the pod. | Transfer is a plausible initial concern. | Integrity is 100%; chambers are primed; membrane responses support viability. | All four through global gate | Incorrect; hint returns player to viability evidence; −20 points. | No logic change needed. |
| Human microbes inhibit germination. | A novel lab could raise contamination concerns. | Chamber is contained; no microbe evidence is supplied; receptor and archive evidence identify an absent cue rather than an inhibitor. | All four through global gate | Incorrect; hint directs attention to absence and mechanism; −20 points. | No logic change needed; containment framing strengthened elsewhere. |

Distractors remain plausible as hypotheses but rejectable from supplied evidence. No distractor is defeated solely by an Earth analogy.

## 7. Intervention comparison

All choices occur after all four clues have been collected and the correct diagnosis selected.

| Intervention | Evidence and mechanism | Benefit | Risks / uncertainty / verification | Reversibility and authorization | Score and justification |
|---|---|---|---|---|---|
| Sealed natural-plume transfer from Zhel'ora at the xenobiology port | Uses the verified natural source, less-than-3-m line, and archive threshold. | Best match to known source and transport; avoids isolating or inventing the molecule. | Must exclude cells and unexpected co-transported compounds, verify cue identity/concentration, monitor leakage and cross-contamination. | Flow can stop before commitment; station biosafety and Zhel'ii representatives authorize. | +10, Contained Cooperative Test. Best supported, not “best” by sentiment. |
| Capture and microdose an authentic fraction | Uses an authentic source but separates material from its living context. | Does not require moving the vessel as close; supports controlled concentration measurement. | Adds purity, co-extraction, dose, storage, and sampling uncertainty; requires closed capture, cell screening, staged dosing, and monitoring. | Exposure is staged before commitment; explicit Zhel'ii consent. | +5, Verified Extraction. Defensible but riskier than direct contained transfer. |
| Develop a validated synthetic candidate | Could reproduce the cue after complete identity and formulation work. | May reduce future collection if successfully validated. | Formula alone is insufficient; connectivity, stereochemistry, carrier, concentration, receptor response, and authentic-standard comparison are required. Longest and least certain immediate route. | Contained pre-pod testing and joint authorization required; staged microdose before commitment. | +0. Defensible only after additional study; correctly ranked lowest for the immediate case. |

The runtime does not model separate failure branches after a player chooses an intervention. Its relative scores and narrative consequences now communicate the evidence and risk ranking. A later worksheet may ask students to defend a different choice if they explicitly address its additional controls; it must not represent the three routes as equally established.

## 8. Predicted response sequence

1. A verified cue is delivered above the fictional receptor threshold along a controlled airflow path.
2. Receptors activate; exposure remains stoppable during the pre-commitment stage.
3. The pod crosses an irreversible commitment checkpoint.
4. Internal membranes dissolve.
5. The network precursor activates first and links the canopy and root precursors.
6. Canopy unfolds and roots enter the validated medium.
7. The young symbiosis stabilizes over the archived post-commitment interval.

The runtime shows the first glow after 2, 3, or 4 cycles depending on route; these are narrative outcomes, not evidence that all choices have equal confidence or safety.

## 9. Scientific accuracy and consistency

### Classification of audited claims

| Runtime claim area | Pre-audit classification | Post-correction classification | Decision |
|---|---|---|---|
| A viable seed may remain dormant under otherwise favorable conditions | Accurate but requires species-specific qualification | Accurate as written | Explanation now lists interacting cues without universalizing them. |
| Fire, smoke, heat, cold, light, water, oxygen, scarification, and gut passage | Misleading categorical examples in places | Accurate but qualified | Responses vary by species, state, animal, dose, and environment; fire and digestion do not guarantee benefit. |
| Karrikins can stimulate responsive seeds | Not used accurately | Accurate but qualified | Fun fact notes low-dose stimulation and possible smoke inhibition. |
| Conditioned Striga can respond to host strigolactones | Absent | Accurate but qualified | Added as a receptor-mediated Earth analogue, with ligand/state/context limits. |
| Orchid–fungus dependence | Overly broad | Accurate but qualified | Nature dependence, partner variation, and asymbiotic laboratory exceptions are explicit. |
| Legume–rhizobium relationship | Incorrectly implied as a germination requirement | Accurate as written | Reframed as Nod-factor signaling during later root infection/nodulation. |
| Mycorrhizal networks and “mother trees” | Settled, universal, intentional, and kin-preference language | Qualified / debated | Network existence and some resource movement are distinguished from unsupported universal seedling dependence or preferential kin feeding. |
| “Family voice” | At times literalized as biology | Fictional and clearly framed | Retained as Zhel'ii metaphor for receptor binding, never as Earth plant intention. |
| Zhel'ii cue and receptor gate | Fictional but inconsistently framed | Fictional and clearly framed | The cue is an incidental mature-network signaling byproduct interpreted by pod receptors. |
| 890 Da airborne “volatile” | Fictional but inadequately framed | Fictional and clearly framed | Described as transported in fictional aerosol carrier droplets and explicitly not an ordinary Earth plant VOC. |
| Formula enables synthesis | Unsupported and unsafe | Qualified speculative engineering | Formula alone is rejected; complete structure, stereochemistry, carrier, authentic comparison, response, dose, and authorization are required. |
| Signal reaches through walls | Internally inconsistent | Internally consistent | Closed corridors and bulkheads have no shared airflow; a sealed short transfer line supplies a supported route. |
| Matching atmosphere recreates ecosystem | Misleading | Accurate boundary | The 99.7% composite explicitly excludes trace compounds and does not claim ecosystem equivalence. |
| Unknown alien sample handling | Unsafe / incomplete | Qualified speculative engineering | Containment, identity, dose, cells, cross-contamination, reversibility, monitoring, and two-party authorization are explicit. |

### Numerical and unit verification

| Quantity | Independent calculation | Result |
|---|---|---|
| Formula mass for C47H63N5O8S2 | 47(12.011) + 63(1.0080) + 5(14.007) + 8(15.999) + 2(32.06) | 564.517 + 63.504 + 70.035 + 127.992 + 64.120 = 890.168 Da; displayed 890.17 Da is correct. Old 862.15 and 847 amu values removed. |
| Trace coverage | 12 ÷ 847 × 100 | 1.416765…%; 1.4% is correct to one decimal. The denominator is shown. |
| Trace-category ledger | at least 340 + approximately 290 + approximately 217 | 847 as an approximate lower ledger; consistent with 847+ identifiers, not an exact compositional proof. |
| Temperature difference | 18.4 °C − 18.2 °C | +0.2 °C. |
| Humidity difference | 71% − 72% | −1 percentage point, not −1%. |
| Natural range | above threshold at 0–3 m; below at 3–5 m; absent beyond 10 m | Current approximately 40 m separation with closed corridors is outside the route; a sealed line less than 3 m is coherent. All values are fictional measurements. |
| Cycle conversion | 1 cycle ≈ 6 Earth hours | 2–4 cycles = 12–24 h; 4–6 cycles = 24–36 h; intervention responses at 2/3/4 cycles = 12/18/24 h. |
| Victory timing | first response 12–24 h, followed by 24–36 h stabilization | Consistent with archive and intervention wording. |

The molecular mass calculation uses 2024 CIAAW abridged standard atomic weights. “Da” is appropriate for a molecular mass expressed relative to the unified atomic mass scale; the formula and mass remain invented game data.

### Suspected issues not present after tracing

- The runtime did not make any formal clue optional: all four were already mandatory by engine design.
- The correct diagnosis was already unique and the three distractors were structurally intact.
- WAITING_FOR_TRIGGER already had two reveal nodes.
- The authored location already matched SAA Xenobiology Lab aboard Hayes Station.
- The game already contained an intentional Campaign 2 game unlock; the defect was not the unlock’s existence but the incomplete final Case 07 handoff.
- No Case 07 curriculum registry or release entry existed.

### Authoritative claim-to-source map

All web sources below were accessed 2026-08-03. Earth sources qualify analogies; none validates the fictional Zhel'ii mechanism.

| Source | Precise claim supported |
|---|---|
| Nonogaki, Bassel, and Bewley, [Germination—Still a Mystery](https://pmc.ncbi.nlm.nih.gov/articles/PMC3243337/) | Dormancy and germination are regulated states; favorable conditions and environmental signals interact, and no single cue is universal. |
| Nelson et al., Plant Physiology, [Karrikins Discovered in Smoke Trigger Arabidopsis Seed Germination by a Mechanism Requiring Gibberellic Acid Synthesis and Light](https://pmc.ncbi.nlm.nih.gov/articles/PMC2633839/) | Smoke-derived karrikins can stimulate responsive seeds through regulated biological pathways; response depends on seed state and other conditions. |
| [Fire-related cues break seed dormancy of more species in fire-prone than in fire-free ecosystems](https://academic.oup.com/aob/article/135/6/1059/7933536), Annals of Botany | Heat and smoke effects vary across species and exposure conditions; smoke can contain stimulatory and inhibitory compounds. |
| [Strigolactone perception and germination of the parasitic plant Striga](https://pmc.ncbi.nlm.nih.gov/articles/PMC9035408/) | Conditioned Striga seeds use host-derived strigolactone cues; receptor activity, ligand, concentration, and conditioning context matter. |
| Bouwmeester et al., [The role of strigolactones in host recognition by parasitic plants](https://pmc.ncbi.nlm.nih.gov/articles/PMC1256006/) | Host-derived strigolactones are chemically specific germination stimulants in parasitic plants. |
| [Asymbiotic seed germination and in vitro seedling development of orchids](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575117/) | Many orchids depend on compatible fungi in nature, while asymbiotic laboratory germination is possible and requirements vary. |
| [Orchid mycorrhizal associations](https://pmc.ncbi.nlm.nih.gov/articles/PMC8138444/) | Fungal partners can differ across germination, protocorm, seedling, and adult stages; orchid–fungus relationships are not one universal rule. |
| [Rhizobial infection and nodulation of legume roots](https://pmc.ncbi.nlm.nih.gov/articles/PMC419923/) | Nod-factor signaling acts on growing roots and root hairs during infection and nodulation, not as a general seed-germination requirement. |
| Karst, Jones, and Hoeksema, Nature Ecology & Evolution, [Positive citation bias and overinterpreted results lead to misinformation on common mycorrhizal networks in forests](https://www.nature.com/articles/s41559-023-01986-1) | Common mycorrhizal network claims require qualification; evidence is insufficient for widespread universal benefits or preferential mature-tree support of offspring. |
| [Effects of animal gut passage on seed fate](https://pmc.ncbi.nlm.nih.gov/articles/PMC11405292/) | Gut passage may improve, leave unchanged, damage, or destroy seeds depending on plant and animal species. |
| U.S. EPA, [Technical Overview of Volatile Organic Compounds](https://www.epa.gov/indoor-air-quality-iaq/technical-overview-volatile-organic-compounds) | VOC classification concerns volatility behavior such as vapor pressure and boiling point; formula or “organic” status alone does not establish airborne transport. |
| [Plant Volatiles: Recent Advances and Future Perspectives](https://pmc.ncbi.nlm.nih.gov/articles/PMC6272994/) | Ordinary plant volatiles are generally relatively low-mass compounds; a roughly 890 Da cue needs fictional transport qualification. |
| IUPAC, [Configuration and stereochemical specification](https://iupac.qmul.ac.uk/BlueBook/P9.html) | Molecular formula alone does not specify connectivity or stereochemical configuration. |
| CIAAW, [Abridged Standard Atomic Weights 2024](https://ciaaw.org/abridged-atomic-weights.htm) | Atomic weights used for the independent C47H63N5O8S2 mass calculation. |
| NASA/JPL, [Planetary Protection Mission Implementation](https://planetaryprotection.jpl.nasa.gov/mission-implementation) | Back-contamination planning supports containment, restricted exposure pathways, and controlled handling in the fictional engineering scenario. |

## 10. Exact game corrections

### space_sprout_sleuth_data.js

- Corrected the source label to Case 07 while preserving “formerly Case 6b” traceability.
- Qualified all Earth dormancy analogies and removed false universal claims about fire, digestion, orchids, legumes, seedlings, and “mother trees.”
- Separated observation, analogy, hypothesis, archive fact, fictional mechanism, and engineering inference.
- Defined the cue as an incidental signaling byproduct interpreted by pod receptors, not deliberate speech.
- Replaced ordinary-VOC framing for the 890 Da compound with explicitly fictional aerosol carrier droplets.
- Corrected formula mass to 890.17 Da, exposed the 12 ÷ 847 calculation, corrected temperature and humidity differences, and made timing conversions explicit.
- Removed transport through walls and supplied an open/shared or sealed airflow path with a less-than-3-m operating range.
- Added second reveal routes for PROXIMITY_REQUIRED, MISSING_VOCS, and GERMINATION_COMPOUND; WAITING_FOR_TRIGGER already had two.
- Gated the early docking discussion by GERMINATION_COMPOUND and recast earlier solution language as a hypothesis.
- Rebalanced and rewrote the three interventions to compare evidence, contamination, dose, verification, reversibility, containment, and consent.
- Preserved proximity as preferred (+10), changed verified extraction to intermediate (+5), and made fully validated synthesis the least-supported immediate option (+0).
- Rewrote clue summaries, diagnosis text, wrong-light hint, explanation, rank-up, and victory timing.

### index.html

- Tightened Case 07 unlock to completed Case 06 only.
- Persisted zero-bonus solution choices.
- Added a solved-case resume handoff that cannot skip the intervention or increment past the final case.
- Rendered both authored Case 07 victory fields.
- Added a final-case rank-up path to Xenobotanist before Campaign 1 results.
- Preserved Campaign 1 completion and the existing game-side Campaign 2 unlock message.

## 11. Focused game tests and results

| Command | Scope | Result |
|---|---|---|
| node tests/case07_content.test.js | Entire Case 07 node graph, four sources, clue routes and fallbacks, diagnoses, science boundaries, formula, percentage, units, distance, timing, interventions, unrelated-case count | PASS, 210 assertions, 0 failures, 0 skips, 0 warnings |
| node tests/case07_runtime_flow.test.js | Case 06 prerequisite, all-clue diagnosis gate, correct-diagnosis integrity, intervention persistence, resume, authored victory, final rank, campaign unlock | PASS, 20 assertions, 0 failures, 0 skips, 0 warnings |
| node tests/case06_timing.test.js | Existing Case 06 timing regression | PASS, 7 assertions, 0 failures, 0 skips, 0 warnings |
| for test_file in tests/*.test.js; do node "$test_file"; done | Full established game suite | PASS, 237 assertions, 0 failures, 0 skips, 0 warnings |
| sed -n '2316,2683p' index.html \| node --check && sed -n '2689,6588p' index.html \| node --check && node --check space_sprout_sleuth_data.js | Both inline runtime scripts and data-source syntax | PASS, 3 syntax checks, 0 failures |

## 12. Proposed worksheet crosswalk — planning only

### Provenance legend

- **C07 reachable:** reachable audited Case 07 game evidence.
- **C06 labeled:** explicitly labeled evidence from approved Case 06.
- **Background:** clearly labeled curriculum background, not a game clue.
- **Fictional inference:** explicitly labeled inference within the Zhel'ii scenario.
- **Curriculum model:** organizer or explanatory representation created by curriculum.

No student-facing formal identity is proposed. Any “missing-variable investigator” language is teacher-facing task identity only.

| Proposed task / prompt | Evidence demand | Provenance | Production boundary |
|---|---|---|---|
| Mission launch and initial hypothesis | Explain why “matched known conditions” is not yet a complete diagnosis; name one measurement still needed. | C07 reachable: briefing; Fictional inference | Do not reveal the compound or diagnosis in the launch. |
| Establish prior known conditions concisely | Record primary gas targets, 18.4 vs 18.2 °C, 71 vs 72% humidity, matched light and pressure; state the 99.7% index excludes trace compounds. | C07 reachable: sensors.atmosphere | Use a compact supplied-data block; do not make students copy a long console. |
| Four-channel evidence collection | For Liaison, Biomonitors, Specimen, and Archives, state what each source establishes and what it cannot establish alone. | C07 reachable: four formal routes and supporting nodes | Include all evidence needed if gameplay is unavailable; hide internal clue tags. |
| Matched-versus-missing comparison | Sort supplied conditions into matched, missing/different, and not-yet-known. Explain why 12 of 847+ is about 1.4%. | C07 reachable: atmosphere/comparison; Curriculum model: comparison organizer | Preserve “trace biological identifiers,” not “the lab has no chemicals.” |
| Viability versus active germination | Cite integrity, primed chambers, and receptor response to explain why dormant is better supported than dead. | C07 reachable: pod_status, chambers, receptors | Do not imply receptor shape alone identifies the ligand. |
| Case 06 comparison | Identify what Case 06 and Case 07 share and how their immediate problems differ: processing removed signals there; a new lab lacked the living source here. | C06 labeled; C07 reachable | Label every reused Case 06 datum; do not import Case 07 outcomes into Case 06. |
| Receptor–signal–response reasoning | Complete receptor + sustained cue → activation → commitment → chamber opening. Mark where stopping exposure remains possible. | C07 reachable: receptors, logs.triggers; Curriculum model | Clearly label the mechanism as fictional alien biology. |
| Mature-network source | Explain why proximity, range, airflow, and archive evidence identify mature growth as the natural source. | C07 reachable: proximity_detail, mature_growth_diff, cultivation, signal_chemistry | “Family voice” may appear only as a labeled metaphor. |
| Systems / causal model | Build: mature network → incidental cue in carrier → airflow/transfer path → pod receptors → germination sequence → young symbiosis. Add “human-built isolated lab” at the broken link. | C07 reachable; Curriculum model; Fictional inference | Do not add invented organs, thresholds, or Earth network claims. |
| Diagnosis and distractor elimination | Compare the correct cue diagnosis against light wavelength, transfer damage, and human microbes using evidence for and against each. | C07 reachable: diagnoses, hints, all formal evidence | Require all four sources; avoid “one clue proves it.” |
| Intervention comparison | Compare sealed natural plume, verified extraction, and validated synthesis for evidence fit, benefit, dose, contamination, verification, reversibility, and authorization. | C07 reachable: solutionChoice; Fictional inference | Do not present the routes as equally safe; allow a nonpreferred defense only with added controls. |
| Safe evidence-based decision | Recommend one intervention and specify monitoring, stopping rule, consent, and evidence that would support or weaken success. | C07 reachable; Fictional inference | No invented safe concentration or universal biosafety rule. |
| Predict observable response | Predict first receptor/glow response and later stabilization in sequence, using 1 cycle ≈ 6 h. Identify one observation that would challenge the prediction. | C07 reachable: logs.triggers, responses, victory | Preserve route-specific response times and post-commitment 24–36 h stabilization. |
| Full-page CER | Claim the missing environmental variable; cite more than one source; explain the causal chain from matched targets through receptor activation. | C07 reachable; C06 labeled if used; Curriculum model | Planned Student and Accessible CER must use the exact locked subtitle below. |
| Campaign 1 synthesis / transfer | Compare this case with one earlier Campaign 1 case: what changed when the investigator moved from checking a single condition to testing a system interaction? | C07 reachable; C06 labeled or another explicitly supplied earlier-case record; Curriculum model | Keep individually completable and one-period; no large project. |
| Independent exit ticket | “What evidence shows the pod is waiting rather than dead, and why is that evidence not enough by itself to identify the missing trigger?” | C07 reachable | Independent response; no word bank that supplies the conclusion. |

Locked CER subtitle for later production:

> You may write sentences or use bullet points. Use evidence from more than one source.

### Suggested assessment boundaries for later production

- Directly assess evidence convergence, causal/system modeling, diagnosis, and evaluation of solutions.
- Treat MS-ETS1-2 as a candidate direct alignment only if the eventual task supplies common criteria and constraints for comparing all three interventions.
- Treat Earth dormancy, symbiosis, VOC, and mycorrhizal content as supporting background and science-boundary guidance, not proof of the alien case.
- Do not grade rapport choices, rank, speed, optional supporting nodes, or choice of the highest-scoring intervention by itself.
- The later Answer Key must complete every field and provide a full Claim, Evidence, and Reasoning exemplar.

## 13. Unresolved cautions

No blocker remains for Phase 1. The following are production cautions, not missing runtime facts:

1. MISSING_VOCS remains a legacy internal clue tag for save compatibility. Student materials should display “trace biological compounds/identifiers” and reserve VOC for qualified Earth background.
2. The 99.7% value is a fictional composite instrument result with no published weighting formula. A worksheet may interpret it only as “primary measured targets are very similar,” not recalculate the composite.
3. The cue concentration threshold has categorical bands but no safe numerical dose. A worksheet must not invent one.
4. Intervention outcomes are authored narrative results, not replicated experiments. Students should compare expected evidence and uncertainty.
5. The game unlocks a Campaign 2 experience. This audit does not create or assert the existence of Campaign 2 curriculum production.
6. Later production must keep the central task compact enough for one period despite the culmination’s rich evidence.

## 14. Curriculum validation and preservation

The audit adds documentation only. The current package registry still discovers exactly Cases 01–06; no Case 07 package, source files, task registry, layout override, history, owner approval, worksheet, export, PDF, screenshot, or generated artifact exists.

| Command | Scope | Result |
|---|---|---|
| python3 shared/validation/validate_canonical_case_structure.py | Canonical layout, registry/package integrity, release-history references, hashes, and generated-artifact exclusion | PASS: 6 cases; 22 commit references, 25 artifact recoveries, and 25 hashes checked; 0 failures |
| python3 shared/validation/validate_layout_overrides.py | Student/Accessible eligibility, lock, and sparse-override contracts | PASS: 6 cases; Accessible 71 eligible / 103 locked; Student 45 eligible / 137 locked |
| python3 apps/curriculum-editor/tests/validate_static.py | Schemas, hashes, role/task/accessibility contracts, Case 01–06 regressions, cleanup rules, nested authoring checks | PASS: 287/287; 0 failures, 0 skips |
| python3 -m unittest apps/curriculum-editor/tests/test_authoring_service.py | Source-write allowlist, path security, rollback, hash conflict, CER protection | PASS: 13/13; 0 failures, 0 skips |
| python3 apps/curriculum-editor/tests/run_browser_tests.py | All 48 case/role/presentation states, exports, printing, persistence, page fit, JavaScript, screenshot smoke | PASS: 952/952; 0 failures, 0 skips; expected favicon request warning only |
| python3 apps/curriculum-editor/tests/run_pdf_tests.py | Temporary PDF export regression | PASS: 146/146; 0 failures, 0 skips |
| python3 shared/validation/validate_repository_cleanup_audit.py | Retired legacy-cleanup audit utility | NOT CURRENT / not counted: exits before assertions because removed CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json is absent on the controlling clean main. The command is not in the current README validation workflow and no production source was changed to revive it. |

### Released-source preservation fingerprints

Directory fingerprints are SHA-256 hashes of the sorted per-file SHA-256 ledger. They were identical before and after this documentation change:

| Released case | Fingerprint |
|---|---|
| Case 01 | 550681ef8724a8cf196c8d816e3114328e597ecaabf0a278c284415fddd65796 |
| Case 02 | f51118e2ebfdf424be32e2d01be541fc4129c0602320fc31dce0b7c350b1c35a |
| Case 03 | 6bef87cbe8f76e82afb4ee6d4e7fd55907216e4712c4ade5d42668515386eb7c |
| Case 04 | e47c5ac131da87d226b5ab18c69c6acd54711e247ac33f3d7b0566850687518a |
| Case 05 | 95b8c4c4359ae5f7dbca66d1a747bb2dadd24f13c760355281f7cdca481789ef |
| Case 06 | b5c3c43c01dd85119ef24eebc12beb26d74afdfb33331f9e9e9e49abeb290d9c |

Git path diff is the controlling preservation proof: it contains only this audit record and sss/audit/README.md. No path under sss/campaign-1 changed.

## 15. Phase boundary

**Curriculum production has not begun.** This phase creates no Case 07 directory, package manifest, worksheet content, presentation stylesheet, task registry, layout override, export, PDF, screenshot, release history, approval record, or registry entry. The next phase requires an explicit production start and should use game commit 530758235522ce110695a23feacea065ed370d08 unless the owner approves a newer compatible baseline.
