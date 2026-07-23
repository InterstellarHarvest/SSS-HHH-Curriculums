# Space Sprout Sleuth — Master Content and Curriculum Audit

**Version:** 0.3 — final audit analysis, exact science-edit specification, final NGSS map, and curriculum naming conventions  
**Authoritative game baseline:** `Space-Sprout-Sleuth` `main` at commit `9f07e00`; content analysis uses the uploaded source snapshot plus the owner-confirmed fixes in that commit  
**Audit date:** 2026-07-22  
**Status:** Final analytical audit pass complete. The repository architecture, all 13 cases, evidence routes, classroom timing, misconceptions, science verification, exact correction text, NGSS alignment, assessment opportunities, and curriculum naming conventions are documented. Version 1.0 will be issued after the approved game-text corrections are committed and reconciled.

## Version 0.3 change log

- Produced an exact, implementation-ready science and historical correction specification for the game text.
- Verified the remaining historical, spaceflight, plant-lighting, radiation, fungal, and mycorrhizal claims against primary or authoritative sources.
- Updated the mycorrhizal mapping finding to include the June 2026 *Science* global density and biomass study.
- Finalized the NGSS table with SEP, DCI, CCC, assessed product, and alignment limitations.
- Established stable curriculum labels for both campaigns and all cases without requiring game renaming.
- Determined that the machine-readable v0.2 inventory remains current because no case architecture changed in this pass.
- Defined the final reconciliation step required before audit v1.0.

## Version 0.2 change log

- Adopted commit `9f07e00` as the canonical implementation baseline.
- Closed the three dead dialogue destinations, help/runtime contradiction, and Europa mood-property mismatch.
- Mapped direct clue routes and evidence depth for all 13 cases.
- Estimated purposeful gameplay windows from implemented text rather than raw repository size.
- Documented every implemented diagnosis distractor and its instructional use.
- Assigned a distinct evidence-processing task, CER frame, exit ticket, and candidate NGSS alignment to every case.
- Completed primary/authoritative source verification for the serious science concerns.
- Identified which findings require game-text edits versus teacher qualification only.

---

## 1. Executive assessment

Space Sprout Sleuth is already structured around a legitimate evidence-based learning loop. The player does not merely receive science facts. In each case, the player gathers information from multiple sources, compares competing explanations, identifies a causal mechanism, selects a diagnosis, receives corrective feedback, and reads a scientific explanation. That structure is unusually well suited to an embedded classroom worksheet because it naturally supports evidence logging, elimination of alternatives, cause-and-effect reasoning, and Claim–Evidence–Reasoning (CER).

The uploaded project contains enough source material to audit all student-facing content across both SSS campaigns. The top-level runtime loads two canonical data files:

- `space_sprout_sleuth_data.js` — Campaign 1, seven playable cases
- `campaign_2_data.js` — Campaign 2, six playable cases
- `index.html` — shared engine, tutorial/help text, scoring, progression, campaign transitions, diagnosis screens, and victory screens

Across both campaigns, the current source contains:

| Measure | Campaign 1 | Campaign 2 | Total |
|---|---:|---:|---:|
| Playable cases | 7 | 6 | 13 |
| Investigation sources | 28 | 30 | 58 |
| Required clue records | 28 | 30 | 58 |
| Dialogue/information nodes | 403 | 307 | 710 |
| Player options | 1,025 | 687 | 1,712 |
| Approximate authored words represented in case data* | 26,850 | 22,490 | 49,340 |

\*The raw word estimate includes dialogue, choices, clue summaries, diagnosis text, hints, and explanations; it therefore includes some duplicated or optional content and is not a playthrough word count.

### Bottom-line findings

1. **The instructional skeleton is strong.** Every standard case has a four- or five-part evidence chain culminating in a diagnosis.
2. **The science progression is intentionally recursive.** Campaign 2 revisits Campaign 1 ideas in harder or inverted contexts.
3. **The curriculum should be embedded during play.** A detached post-game worksheet would waste the strongest part of the design: students already have to collect and reconcile evidence.
4. **The game is not yet classroom-safe without teacher notes.** Several claims need careful qualification, and at least two cases appear to contain science that is overstated or potentially incorrect.
5. **The three broken Campaign 2 dialogue links, diagnosis-help contradiction, and Europa mood-property mismatch were resolved in commit `9f07e00`.** They remain documented for traceability but are no longer open classroom blockers.
6. **The intended 20-minute gameplay target is plausible for every case through a purposeful evidence route, but not through completionist play.** Direct-route reading loads range from roughly 515 to 1,099 words before worksheet writing; navigation and optional cross-checks can expand that considerably.
7. **Formal clue collection is intentionally easy; scientific interpretation is where the curriculum must add rigor.** In most sources, the required clue sits one obvious choice beyond the entry node. The worksheet must therefore ask students to connect, weigh, and explain evidence rather than merely prove that they clicked it.
8. **The materials should grade reasoning, not game performance.** The current score combines diagnosis accuracy, rapport, optional insights, and exhaustive node visitation; that score should never become the academic grade.

---

## 2. Working classroom constraints

The audit uses the following owner-approved constraints:

- Audience begins at middle school and extends through adults/general audiences.
- Primary curricular homes are environmental science and STEM.
- NGSS is the standards anchor.
- A complete case lesson must fit within 60 minutes, including startup, instructions, approximately 20 minutes of gameplay, worksheet completion, and closure.
- Each chapter should ordinarily function as a self-contained lesson.
- Students may work together but every task must be independently completable.
- No student should be penalized for preferring to work alone.
- Gameplay skill and game score do not determine the academic grade.
- Every case should include a CER component and an exit ticket.
- Materials should emphasize scientific reasoning, evidence collection, completion, vocabulary, and a concise written explanation.
- Student materials should use a hybrid classroom/in-universe visual style, print well in grayscale, and eventually exist as paper, fillable PDF, and Google Docs versions.
- Directions should be chunked and compatible with text-to-speech.
- Important scientific claims require sourcing.
- Established science, plausible extrapolation, and fiction must be clearly distinguished.
- Only serious scientific problems should trigger recommendations for changes to the game.

---

## 3. Canonical source hierarchy

### 3.1 Files used as canonical

The current `index.html` directly loads:

```html
<script src="space_sprout_sleuth_data.js"></script>
<script src="campaign_2_data.js"></script>
```

Therefore the audit treats the following order as authoritative:

1. Top-level `index.html`
2. Top-level `space_sprout_sleuth_data.js`
3. Top-level `campaign_2_data.js`
4. Current design documents under `resources/`
5. Implementation plans under `resources/`
6. Backups and demo files only as historical or intent evidence

### 3.2 Duplicate source copies

The archive also contains copies under `resources/campaign_2/` and backup files. They are not byte-identical to the top-level runtime files. The data differences are primarily asset-path adjustments, while the nested `index.html` is substantially older. These copies must not be mixed into the curriculum extraction.

**Curriculum rule:** quote and map student-facing content from the top-level files unless a clearly documented runtime bug makes the intended design relevant.

### 3.3 Case source ranges

#### Campaign 1 — `space_sprout_sleuth_data.js`

| Runtime case | ID | Approximate source start |
|---|---|---:|
| 1 | `iss` | line 68 |
| 2 | `lunar` | line 943 |
| 3 | `mars` | line 1529 |
| 4 | `orbital` | line 2114 |
| 5 | `europa` | line 2664 |
| 6 | `alien1` | line 3200 |
| 7 / design “6b” | `alien2` | line 3884 |

#### Campaign 2 — `campaign_2_data.js`

| Runtime case | ID | Approximate source start |
|---|---|---:|
| 1 | `heavy_hands` | line 220 |
| 2 | `missing_dance` | line 814 |
| 3 | `wrong_color_light` | line 1351 |
| 4 | `silent_grove` | line 1913 |
| 5 | `too_clean_room` | line 2475 |
| 6 | `first_garden` | line 3038 |

---

## 4. How the game teaches

### 4.1 Core investigation model

Campaign 1 normally presents four evidence channels:

1. Crew interview
2. Sensor readings
3. Plant examination
4. Mission or research logs

Campaign 2 adds a fifth channel:

5. Federation Database

The final Campaign 2 case intentionally changes the model: four character interviews plus the database replace the standard crew/sensors/plants/logs arrangement. This is educationally useful because it changes source type and forces students to distinguish testimony, interpretation, policy, and reference evidence.

### 4.2 Evidence structure

Each case has one formal clue per source. Finding all formal clues unlocks the diagnosis screen under the current implementation. Optional nodes can:

- reveal contextual facts;
- unlock questions in other sources;
- improve or damage rapport;
- provide bonus insights;
- set flags;
- expose misconceptions;
- offer humor or characterization.

The formal clue records are concise and are already close to worksheet-ready evidence statements. They should not simply be copied into blanks, however. A better worksheet asks students to classify, interpret, or connect them.

### 4.3 Diagnosis model

Every case supplies four competing diagnoses with exactly one marked correct. Wrong choices return a targeted hint and a score penalty. Correct choices lead to a scientific explanation and fun fact. Some later cases add a solution/policy choice after the diagnosis.

This supports a strong classroom distinction:

- **Diagnosis:** What is causing the failure?
- **Evidence:** Which observations support that diagnosis?
- **Mechanism:** Why would that cause the observed pattern?
- **Solution:** What should be changed?
- **Policy or trade-off:** What wider action should follow?

### 4.4 Scoring model

The current game score begins at 100 points and adds or subtracts points for:

- all formal clues found;
- wrong diagnoses;
- cross-source bonus insights;
- maintaining rapport;
- visiting every node in a source;
- selected solution choices.

This is good game feedback but poor academic grading data. In particular, “visit every node” rewards completionist clicking rather than efficient scientific reasoning. The teacher materials should explicitly state that game points are motivational only.

### 4.5 Readability screening

A rough Flesch–Kincaid screening of the authored case text places most total dialogue near grades 7–9, while several core explanations rise into grades 10–12 because of technical vocabulary and sentence length. This is acceptable for the stated middle-school-through-adult audience only when the worksheet chunks the language and teachers have short vocabulary supports available.

The most demanding core explanation screens are currently:

- Campaign 1 Case 4 — spirulina/light stress
- Campaign 1 Case 5 — radiation and DNA damage
- Campaign 2 Case 5 — hormesis and DNA-repair pathways

Text-to-speech compatibility is realistic because the source is real text rather than text embedded in images.

---

## 5. Campaign architecture

## Campaign 1 — Solar Agricultural Authority

Campaign 1 establishes five core space-agriculture principles, then applies ecosystem communication and germination signaling in a two-part first-contact ending.

| Sequence | Case | Main concept | Reasoning pattern |
|---:|---|---|---|
| 1 | ISS Greenhouse Module | Gravitropism in microgravity | Identify the missing environmental cue |
| 2 | Lunar Greenhouse | Pollination in a sealed system | Identify a missing biological process |
| 3 | Mars Habitat | Light quality and chlorophyll production | Separate light quantity from spectral quality |
| 4 | Hayes Orbital Station | Continuous light and algal stress | Link a system change to a delayed crash pattern |
| 5 | Europa Outpost | Radiation damage in seedlings | Eliminate controlled variables and infer an invisible hazard |
| 6 | First Contact Protocol | Chemical signaling in a symbiosis | Recognize human technology as the disturbance |
| 7 / “6b” | The Gift | Chemical germination cue | Infer the missing living-context trigger |

## Campaign 2 — Distant Soils / Federation Field Cases

The runtime title calls Campaign 2 **Distant Soils**, while the data object calls it **Federation Field Cases**. The campaign revisits earlier concepts in alien, systems, cultural, and policy contexts.

| Sequence | Case | Callback | Added complexity |
|---:|---|---|---|
| 1 | Vressk Centrifuge Habitat | Gravitropism | Artificial-gravity gradient and species-specific adaptation |
| 2 | Ares Botanical Garden | Pollination | Vibration/acoustic triggering plus cultural information barriers |
| 3 | Oolian Mariculture Dome | Light spectrum | Different pigments make Earth grow lights inappropriate |
| 4 | Zhel’ii Diaspora Grove | Photoperiod + VOC signaling | Two prior principles must be combined |
| 5 | Concord Botanical Vault | Radiation | The hazard is inverted into a required input; policy choice follows |
| 6 | The First Garden | Mycorrhizal ecology | Restoration science, testimony, legal precedent, and policy reform |

### Campaign-level educational progression

Campaign 1 asks, “Which environmental requirement is missing or harmful?”

Campaign 2 increasingly asks, “Whose assumptions define the environment, and what happens when a universal standard ignores species-specific biology?”

That is a genuine increase in systems thinking. Campaign 2 is not merely a harder fact quiz; it introduces policy, culture, evidence quality, institutional assumptions, and transfer of prior learning.

---

# 6. Case-by-case preliminary curriculum audit

The following dossiers describe the implemented case, not yet the final lesson plan.

## C1-1 — ISS Greenhouse Module

**Story problem:** Lettuce remains alive but roots form tangled balls and shoots orient poorly in microgravity.

**Formal evidence chain:**

- Crew: roots do not orient downward.
- Sensors: gravitational acceleration is 0.00 g.
- Plant examination: roots curl into tangled mats; stems grow at odd angles.
- Logs: plants normally use gravitropism; alternative physical or light cues are recommended.

**Correct diagnosis:** Microgravity disrupts gravitropism, so plants need alternative orientation and root-zone guidance.

**Core reasoning:** Match an abnormal plant pattern to the one environmental variable that differs fundamentally from Earth.

**Instructional strengths:**

- Clean introductory case with one dominant cause.
- All four evidence types contribute different pieces.
- Wrong answers are directly contradicted by evidence.
- Strong introduction to controlled variables and environmental cues.

**Likely misconceptions:**

- “Plants cannot grow in space at all.”
- “Roots always grow toward water, so gravity is irrelevant.”
- Confusing gravitropism with phototropism.
- Treating microgravity as literally no gravity rather than a free-fall environment.

**Preliminary NGSS fit:** Strong SEP alignment to analyzing evidence and constructing an explanation; possible engineering extension through MS-ETS1-1/2 rather than claiming a direct life-science PE.

**Best student task identity:** **Evidence triage.** Students sort observations into “supports gravitropism diagnosis,” “rules out another cause,” or “background information.”

**CER focus:** How does the evidence show that loss of a directional gravity cue—not nutrient or genetic failure—is causing the root pattern?

**Class-period fit:** Excellent pilot lesson. The shortest evidence routes are compact, and the concept can be understood without a long prerequisite reading.

**Science status:** Core concept is established. Teacher notes should clarify that the ISS is a microgravity/free-fall environment and that Veggie pillows primarily manage water, nutrients, and air distribution; light provides an orientation cue above the plants.

---

## C1-2 — Lunar Greenhouse

**Story problem:** Healthy tomato plants flower but never set fruit.

**Formal evidence chain:**

- Crew: flowers drop after several days without fruiting.
- Sensors: airflow is nearly zero while other environmental measures are acceptable.
- Plant examination: pollen remains undisturbed on the anthers; stigmas are clean.
- Logs: the greenhouse never implemented a pollination plan.

**Correct diagnosis:** Physical pollen transfer is not occurring in the sealed greenhouse.

**Core reasoning:** Distinguish healthy vegetative growth and flowering from the separate reproductive process required for fruit set.

**Instructional strengths:**

- Observable cause-and-effect chain.
- Direct connection to greenhouse agriculture on Earth.
- Provides an authentic engineering-design opening: fan, vibration tool, manual pollination, or managed pollinator.

**Likely misconceptions:**

- “Self-pollinating” means no pollen movement is required.
- Flowers automatically become fruit.
- More fertilizer or light solves every crop problem.

**Preliminary NGSS fit:** MS-LS2-4 and MS-LS2-5 are possible supporting links when discussing changed biological components and design solutions; MS-ETS1-2 is a natural fit for comparing pollination solutions.

**Best student task identity:** **Cause-and-effect flow diagram.** Flower → pollen release/transfer → stigma → fertilization → fruit set.

**CER focus:** Why is missing pollen movement a better explanation than soil, light, or CO₂?

**Class-period fit:** Very strong. A short demonstration or teacher video of tomato vibration/buzz pollination could fit within the 60-minute ceiling.

**Science status:** The core tomato vibration claim is established. Teacher materials should avoid implying all self-pollinating plants require the same method.

---

## C1-3 — Mars Habitat

**Story problem:** New potato growth is pale or white while older leaves remain greener; nutrient increases do not help.

**Formal evidence chain:**

- Crew: new growth fails first and nutrients did not solve it.
- Sensors: light arrives through long fiber-optic pipes plus white LEDs.
- Plant examination: new tissue is structurally normal but fails to develop chlorophyll.
- Logs: a light-dependent chlorophyll-biosynthesis step requires suitable wavelengths.

**Correct diagnosis:** The light system is filtering out red wavelengths needed for chlorophyll biosynthesis.

**Core reasoning:** Separate total photon quantity (PAR) from spectral composition, then connect the age pattern to pigment production in new tissue.

**Instructional strengths:**

- Strong “quantity versus quality” misconception challenge.
- Students must use pattern location—new versus old tissue—not merely notice yellow leaves.
- Provides a clear sensor-data interpretation opportunity.

**Likely misconceptions:**

- Any chlorosis must be nitrogen or iron deficiency.
- PAR alone proves a light system is suitable.
- Green light is wholly useless to plants.

**Preliminary NGSS fit:** MS-LS1-6 is relevant to photosynthesis conceptually, but the game’s biochemical detail exceeds the middle-school assessment boundary. MS-ETS1-2 is stronger for evaluating lighting fixes.

**Best student task identity:** **Data comparison.** Students compare total PAR, spectral profile, leaf age, and nutrient response, then identify which variable explains all observations.

**CER focus:** Why can a plant receive “enough light” by a PAR meter and still fail to produce healthy new leaves?

**Class-period fit:** Good if the worksheet supplies a simple spectrum graphic rather than requiring students to parse every biochemical term.

**Serious science review flag:** The chlorophyll pathway’s light dependence is real, but the implemented physical explanation may be backwards or unsupported. The game states that 12 m of borosilicate fiber and Martian dust transmit blue well while severely attenuating red. Ordinary silica/glass transmission and Martian dust behavior do not obviously support that pattern; NASA descriptions often show Martian dust filtering out green/blue while red light reaches the surface. This case needs a technical source or a revised failure mechanism before it becomes a formal classroom lesson. A safer mechanism might be an intentionally misconfigured luminaire, a red-blocking filter/coating, or a measured spectral defect rather than a generic property of long glass fibers and Mars dust.

---

## C1-4 — Hayes Orbital Station

**Story problem:** A spirulina bioreactor repeatedly crashes after station lighting changes from a 16/8 cycle to continuous illumination.

**Formal evidence chain:**

- Crew: crashes began soon after the lighting schedule changed.
- Sensors: the reactor receives 24-hour light with no independent dark cycle.
- Examination: culture shows light-stress damage rather than infection.
- Logs: the operational manual states that a dark period is essential.

**Correct diagnosis:** Continuous lighting causes photodamage, and the culture needs a dark period for repair.

**Core reasoning:** Use temporal correlation, controlled alternatives, tissue evidence, and system documentation to identify a delayed consequence of an operational change.

**Instructional strengths:**

- Excellent timeline reasoning.
- Strong opportunity to distinguish correlation from mechanism.
- Teaches that “more input” does not always produce more output.

**Likely misconceptions:**

- Photosynthetic organisms benefit indefinitely from more light.
- Dark reactions occur only in darkness.
- Any cloudy culture must be contaminated.

**Preliminary NGSS fit:** MS-LS1-6 and systems/cause-and-effect practices are relevant; engineering standards can support redesign of the lighting controls.

**Best student task identity:** **Failure timeline and variable isolation.** Students identify what changed, when the failures began, and which evidence distinguishes light stress from infection.

**CER focus:** How does the timing and damage pattern support light stress over nutrient, CO₂, or contamination explanations?

**Class-period fit:** Structurally strong, but only after the core science is corrected or carefully reframed.

**Serious science review flag:** The current text overstates the requirement for darkness in spirulina/Arthrospira cultivation. Published continuous-culture and continuous-illumination studies show Arthrospira can grow successfully under continuous light when intensity, density, mixing, and reactor design are controlled. Photoinhibition is real, but “continuous light kills the culture” and “dark period is essential” are not defensible as general principles. The case can be preserved by making the cause **excess continuous irradiance without adequate mixing/light management**, a failed reactor-specific control specification, or a particular strain’s validated operating limit. This is a major correction candidate.

---

## C1-5 — Europa Outpost

**Story problem:** Wheat repeatedly germinates, grows a few centimeters, then develops damage and dies despite changes to other growing conditions.

**Formal evidence chain:**

- Crew: multiple trials fail at the same developmental stage.
- Sensors: radiation remains elevated.
- Plant examination: rapidly dividing tissues show patterns consistent with DNA replication damage.
- Logs: shielding assessment was incomplete and secondary particle exposure remained possible.

**Correct diagnosis:** Residual radiation causes DNA damage in rapidly dividing seedling tissue.

**Core reasoning:** Repeated failure under varied conditions narrows the cause to a persistent environmental factor; tissue location connects that factor to a mechanism.

**Instructional strengths:**

- Strong elimination of alternatives.
- Useful invisible-hazard case.
- Good connection between cell division and vulnerability.
- Naturally supports risk-assessment and engineering trade-offs.

**Likely misconceptions:**

- Radiation makes organisms instantly radioactive.
- All plant cells divide at the same rate.
- Any amount of ice or polyethylene makes radiation negligible.

**Preliminary NGSS fit:** MS-ETS1-1/2 for shielding design; cause-and-effect and structure/function practices; direct radiation biology is more high-school than middle-school content.

**Best student task identity:** **Risk matrix.** Students rank evidence by reliability and compare possible mitigation strategies.

**CER focus:** Why does repeated death at growing tips support radiation-induced DNA damage rather than low gravity, water contamination, or light intensity?

**Class-period fit:** Good with a concise teacher explanation of ionizing radiation and rapidly dividing cells.

**Science status:** Europa’s external radiation environment is unquestionably intense. The exact interior dose, shield composition, and “secondary neutron cascade” details are scenario-specific and should be labeled extrapolation unless a design calculation supports them. The teacher guide should not imply that lunar surface habitats receive meaningful protection merely from being near Earth’s magnetosphere.

---

## C1-6 — First Contact Protocol

**Story problem:** A three-organism alien food symbiosis loses coordination after docking with a human station.

**Formal evidence chain:**

- Zel’keth: the network organism became dormant several days after docking.
- Sensors: human scrubbers remove nearly all atmospheric volatile compounds.
- Organism examination: signal structures are closed in controlled dormancy, not physically damaged.
- Archive: the network communicates through volatile compounds and shuts down when signals fail to persist.

**Correct diagnosis:** Human atmospheric scrubbers remove the symbiosis’s communication compounds.

**Core reasoning:** Identify the intervention introduced at the exact time of failure and recognize that a technology considered “clean” can remove biologically necessary signals.

**Instructional strengths:**

- Strong systems thinking.
- Excellent perspective shift: human infrastructure is the disturbance.
- Good bridge from plant biology to environmental management and unintended consequences.
- Supports distinction between an observation and an assumption.

**Likely misconceptions:**

- All airborne organic compounds are pollution.
- Symbiosis means only two organisms.
- An ecosystem is merely a collection of independent organisms.

**Preliminary NGSS fit:** MS-LS2-3 and MS-LS2-4 are strong conceptual candidates; MS-ETS1-2 supports scrubber redesign.

**Best student task identity:** **Systems map.** Students draw organism-to-organism signals and show where the scrubber breaks the feedback loop.

**CER focus:** Why does the timing, sensor record, and dormant anatomy support signal removal rather than physical damage or incompatibility?

**Class-period fit:** Longer than the core cases but workable if the worksheet limits students to the four formal evidence routes.

**Science status:** The alien biology is clearly speculative. The Earth analogy must be handled carefully. Common mycorrhizal networks exist, but popular claims that “mother trees” broadly feed seedlings and that forests operate as intentional communication superorganisms are scientifically contested and often overstated. Teacher materials should label the alien VOC system as fiction inspired by real plant/fungal chemical signaling, not as a direct copy of settled “wood wide web” science.

---

## C1-7 / design Case 6b — The Gift

**Story problem:** An alien genesis pod remains dormant even after the human lab reproduces all measurable physical conditions.

**Formal evidence chain:**

- Zel’keth: pods are traditionally placed near mature networks.
- Sensors: physical atmospheric measures match, but living volatile compounds are absent.
- Pod examination: receptors appear to be waiting for a specific chemical trigger.
- Archive: a mature network produces the germination compound.

**Correct diagnosis:** The pod requires a chemical signal from an established living network before germination.

**Core reasoning:** Recognize that duplicating physical conditions is not the same as reproducing a living ecological context.

**Instructional strengths:**

- Strong culmination of the first-contact sequence.
- Encourages inference from tradition, sensor absence, anatomy, and archive evidence.
- Solution choices allow comparison of natural transfer, sample transfer, and synthesis.

**Likely misconceptions:**

- Germination is controlled only by water, temperature, oxygen, and light.
- Recreating average atmospheric chemistry recreates an ecosystem.
- A laboratory can reproduce a biological system merely by matching measured variables.

**Preliminary NGSS fit:** MS-LS2-3/4 conceptually; MS-ETS1-2 for evaluating delivery options.

**Best student task identity:** **Missing-variable investigation.** Students separate what the lab matched from what it failed to reproduce.

**CER focus:** Why is a network-derived germination signal the best explanation for the pod’s dormancy?

**Class-period fit:** Text-heavy. It is better suited as the Campaign 1 culmination than as an ordinary worksheet case, provided the task remains compact.

**Canon decision needed later:** Design documentation says the player-facing label should be “Case 6b,” while the current runtime’s sequential label function displays it as Case 7. Curriculum files cannot be finalized until the owner chooses the classroom-facing label.

---

## C2-1 — Vressk Centrifuge Habitat

**Story problem:** Gorlroot tubers in a rotating habitat grow outward/upward instead of into the soil despite the system reading 2.1 g.

**Formal evidence chain:**

- Crew: tubers are misdirected.
- Sensors: artificial gravity varies slightly across soil-bed radius/depth.
- Plant examination: growth aligns toward the ring wall rather than the expected soil direction.
- Archive: traditional practice assumes a uniform planetary field.
- Database: similar short-radius centrifuges caused species-specific orientation failures.

**Correct diagnosis:** The centrifugal gravity field changes with radius, and the crop’s orientation system is adapted to a more uniform planetary field.

**Core reasoning:** Recognize that a single “2.1 g” value does not fully describe a field across a system.

**Instructional strengths:**

- Excellent transfer from the introductory gravitropism case.
- Encourages students to question averaged measurements.
- Strong engineering design possibilities involving radius, bed depth, and orientation.

**Likely misconceptions:**

- Artificial gravity is identical everywhere in a rotating habitat.
- Correct average magnitude guarantees correct biological response.
- More gravity is always the problem.

**Preliminary NGSS fit:** Strong MS-ETS1-1/2; possible force/motion enrichment beyond the core environmental-science focus.

**Best student task identity:** **Gradient diagram.** Students annotate force direction and magnitude across the bed and explain why one sensor value is inadequate.

**CER focus:** Why does the gradient explanation fit the direction of tuber growth better than excessive gravity, soil chemistry, or bed depth alone?

**Science status:** Centrifugal acceleration varies with radius; the alien species response is extrapolation and should be labeled as such.

---

## C2-2 — Ares Botanical Garden

**Story problem:** An alien lyreflower forms buds and mature pollen but buds abort and manual pollen transfer fails.

**Formal evidence chain:**

- Crew: “the dance” is culturally important but difficult to discuss.
- Sensors: the sealed garden has essentially no relevant acoustic stimulus.
- Plant examination: mature pollen remains trapped in specialized anthers.
- Logs: manual pollination failed.
- Database: the species requires a specific vibration/acoustic trigger.

**Correct diagnosis:** A tuned vibration is required to release pollen; contact alone is insufficient.

**Core reasoning:** Use failed intervention evidence to distinguish pollen transfer from pollen release.

**Instructional strengths:**

- Directly revises the Campaign 1 solution.
- Demonstrates that a strategy valid for one species may fail for another.
- Adds cultural communication as an evidence-access issue without making culture itself the cause.

**Likely misconceptions:**

- Hand pollination is universally effective.
- Sound affects plants only metaphorically.
- Cultural reluctance means the witness is unreliable.

**Preliminary NGSS fit:** MS-LS2-4 and MS-ETS1-2; engineering task can compare vibration devices.

**Best student task identity:** **Failed-solution analysis.** Students explain why the attempted fix failed and what new evidence changes the design.

**CER focus:** Why does trapped mature pollen plus failed hand transfer support vibration-triggered release?

**Science status:** Earth buzz pollination is established; the exact alien resonance is fiction.

---

## C2-3 — Oolian Mariculture Dome

**Story problem:** Alien kelp begins dying when a new dome adopts red-heavy Earth grow lights.

**Formal evidence chain:**

- Crew: decline began with the new lighting system.
- Sensors: lamps are red-heavy with little blue-green output.
- Plant examination: pigments are tuned to different wavelengths.
- Archive: the species evolved under deep-ocean blue-green light.
- Database: chlorophyll c and accessory pigments differ from terrestrial crop assumptions.

**Correct diagnosis:** The Earth-designed light spectrum is functionally dim for the kelp’s pigment system.

**Core reasoning:** Apply the principle that usable light depends on an organism’s pigments and evolutionary environment.

**Instructional strengths:**

- Strong inversion of the Mars case.
- Useful distinction between human product quality and biological suitability.
- Good trade/policy context without requiring group debate.

**Likely misconceptions:**

- Red and blue terrestrial grow lights are optimal for every photosynthetic organism.
- Total intensity alone determines photosynthesis.
- “Different chlorophyll” means no shared photosynthetic biology.

**Preliminary NGSS fit:** MS-LS1-6 conceptually and MS-ETS1-2 for light-system redesign.

**Best student task identity:** **Action-spectrum match.** Students match lamp output to pigment absorption and identify the mismatch.

**CER focus:** Why can high-quality Earth grow lights still be biologically inappropriate for this organism?

**Science status:** The alien species is fictional, while chlorophyll c and accessory pigments in marine algae are real. Teacher notes should avoid claiming these organisms use no red light at all; the issue is relative effectiveness and available spectrum.

---

## C2-4 — Zhel’ii Diaspora Grove

**Story problem:** A descendant grove remains alive but stops producing its communication compounds after caretakers switch to continuous light.

**Formal evidence chain:**

- Crew: the network has fallen silent.
- Sensors: lighting is 24/0 and volatile signaling is absent.
- Examination: the organisms remain alive and structurally healthy.
- Logs: silence began after the schedule change.
- Database: signaling is circadian-linked and requires periodic darkness.

**Correct diagnosis:** Continuous light prevents the network’s circadian signaling cycle from resetting.

**Core reasoning:** Combine two earlier principles—chemical signaling and photoperiod/circadian regulation.

**Instructional strengths:**

- Best explicit transfer case in the game.
- Requires students to integrate evidence rather than apply one memorized fact.
- Strong opportunity to distinguish organism health from ecosystem function.

**Likely misconceptions:**

- If an organism looks alive, its ecological function is intact.
- Continuous light always improves growth.
- Circadian rhythms are limited to animals.

**Preliminary NGSS fit:** MS-LS2-3/4 and systems thinking; the alien mechanism remains fictional.

**Best student task identity:** **Two-concept synthesis.** Students create a chain linking light schedule → internal clock → VOC production → network coordination.

**CER focus:** Why does the evidence require both circadian regulation and chemical signaling to explain the silence?

**Science status:** Alien-specific mechanism is speculative. It should not inherit the overbroad claim from C1-4 that all spirulina require a dark period.

---

## C2-5 — Concord Botanical Vault

**Story problem:** A medicinal alien bloom remains intact but stops producing useful compounds inside a perfectly shielded vault.

**Formal evidence chain:**

- Crew: compound production collapsed after transplantation.
- Sensors: radiation is effectively zero.
- Examination: DNA-repair pathway is inactive; target compounds lie downstream.
- Archive: the homeworld has high background radiation.
- Database: the species is described as requiring low-level radiation.

**Correct diagnosis:** Shielding removed the stimulus that activates the plant’s repair/production pathway.

**Core reasoning:** Invert the assumption that minimizing a hazard is always optimal, then trace a mechanistic pathway.

**Instructional strengths:**

- Strongest policy-assumption case.
- Good distinction between universal standards and species-specific needs.
- Solution choice introduces immediate repair, policy reform, and technological substitution.

**Likely misconceptions:**

- Radiation is always beneficial at low doses.
- Hormesis is a universally accepted rule.
- Chernobyl fungi are proven to photosynthesize ionizing radiation like plants use light.

**Preliminary NGSS fit:** MS-ETS1-2 and argument from evidence; detailed radiation metabolism is beyond typical middle-school expectations.

**Best student task identity:** **Assumption audit.** Students identify the hidden policy assumption, the evidence that contradicts it, and the risks of each proposed solution.

**CER focus:** Why does a zero-radiation environment explain low compound production better than soil chemistry, temperature, or transplant shock?

**Class-period fit:** Conceptually challenging but manageable with a one-paragraph science note.

**Serious science review flag:** Radiation hormesis remains scientifically disputed as a general principle, and published fungal studies show enhanced growth/metabolic effects under radiation—not established obligate dependence or a settled photosynthesis-like energy pathway. The alien plant may be fictional and radiation-dependent, but the Earth analogy must be rewritten as tentative inspiration. The phrase “some Earth fungi require radiation” should not appear as established fact. The use of cesium-137 sources also requires safety/context framing in teacher materials and may be an unnecessarily distracting implementation detail.

---

## C2-6 — The First Garden

**Story problem:** A restored garden has chemically healthy patches that remain disconnected and fail to function as one system; the biological repair is restricted by Concord rules.

**Formal evidence chain:**

- Nova: decades of conventional restoration produced patchy success.
- Vorn-Shael: chemical compounds remain isolated rather than moving across zones.
- Kess: a mycorrhizal network is the missing biological connection.
- Ilreth-Mar: regulation prohibits cross-zone biological inoculation.
- Database: precedent may allow an exemption and support policy reform.

**Correct diagnosis:** The fungal/root network destroyed by contamination was never restored, leaving healthy patches ecologically disconnected.

**Core reasoning:** Integrate historical testimony, chemical observations, ecological mechanism, regulation, and legal precedent.

**Instructional strengths:**

- Strong campaign culmination.
- Students must evaluate source roles rather than just read four instruments.
- Connects restoration ecology to policy and institutional design.
- Solution options allow individual written argument without requiring a group project.

**Likely misconceptions:**

- Correct soil chemistry guarantees a functioning ecosystem.
- Fungal inoculation is always beneficial and risk-free.
- Any common mycorrhizal network broadly transfers resources among plants in a cooperative “internet.”

**Preliminary NGSS fit:** MS-LS2-3, MS-LS2-4, MS-LS2-5, and MS-ETS1-2 are the strongest campaign-level fit.

**Best student task identity:** **Evidence-and-policy recommendation.** Students separate the scientific diagnosis from the legal response, then defend one action under stated criteria.

**CER focus:** Why is ecological disconnection a better explanation than pH, irrigation, or invasive species?

**Science status:** Mycorrhizal symbioses and restoration inoculation are real, but the broad “wood wide web” resource-sharing narrative is contested. The curriculum must distinguish established fungal-root symbiosis from debated claims about large-scale tree-to-tree support and intentional communication.

**Resolved runtime defects:** The three evidence-gated dead dialogue destinations originally found in this case were repaired in commit `9f07e00`:

- `vorn_shael.active_transport` now routes to `kess_correlation`;
- the two gated options in `ilreth_mar.start` now route to `biosafety_overview` and `exemption_history`.

The owner reports that both data files pass syntax checks and the game boots headlessly without console or page errors after the fix.

---

# 7. Cross-case instructional findings

## 7.1 The formal clue architecture is curriculum-ready

Each case already provides exactly one formal clue from each evidence channel. A student mission sheet can therefore use a consistent evidence table without making every activity identical.

Recommended recurring columns:

| Source | Observation or record | What it rules out | What it suggests | Reliability/limitations |
|---|---|---|---|---|

The final response area can then vary by case: diagram, ranked evidence, model, recommendation, or CER.

## 7.2 Campaign 2 successfully spirals prior learning

The clearest concept pairs are:

- C1 gravitropism → C2 centrifugal-gravity gradient
- C1 missing pollination → C2 specialized vibration trigger
- C1 spectrum mismatch → C2 different pigment system
- C1 continuous-light case + first-contact signaling → C2 circadian signaling
- C1 radiation damage → C2 fictional radiation dependence
- C1 first-contact network → C2 ecological restoration network

This should be made visible in teacher materials but not necessarily announced to students before investigation.

## 7.3 Case tasks should vary by scientific practice

A single repeated worksheet format would flatten the game. Recommended primary task identities are:

| Case | Primary task |
|---|---|
| C1-1 | Evidence triage |
| C1-2 | Cause-and-effect chain |
| C1-3 | Spectral/data comparison |
| C1-4 | Timeline and variable isolation |
| C1-5 | Risk assessment |
| C1-6 | Systems map |
| C1-7 | Missing-variable investigation and culmination |
| C2-1 | Gradient model |
| C2-2 | Failed-solution analysis |
| C2-3 | Action-spectrum match |
| C2-4 | Two-concept synthesis |
| C2-5 | Assumption/policy audit |
| C2-6 | Evidence-based restoration recommendation |

Every case can still end in CER, but the evidence-processing task should change.

## 7.4 The game’s score should be hidden from academic assessment

Students can diagnose correctly with all required evidence but receive different scores due to personality choices, optional exploration, or exhaustive clicking. Teacher rubrics should score:

- accurate evidence capture;
- reasoning linking evidence to mechanism;
- appropriate vocabulary;
- elimination of alternatives;
- clarity of CER;
- completion of exit ticket.

## 7.5 Twenty minutes of gameplay requires an “instructional path”

The authored content is much larger than a 20-minute target. Direct shortest routes to the formal clues are reasonably compact, but students may explore hundreds of optional nodes. The teacher guide should provide one of the following without spoiling the diagnosis:

- a 20-minute timer with permission to prioritize one source at a time;
- a checkpoint list naming the four/five evidence channels;
- a teacher bypass or clue-access procedure for students who get stuck;
- a save/resume fallback;
- optional exploration clearly separated from required evidence.

The curriculum must never require exhaustive node visitation.

## 7.6 CER is authentic here

The diagnosis itself supplies the **claim**. The formal clues supply candidate **evidence**. The missing instructional layer is **reasoning**—the scientific mechanism explaining why those observations support the diagnosis. Therefore each worksheet should avoid asking students merely to rewrite the diagnosis and clues. It should require one concise mechanism statement.

---

---

# 8. Resolved implementation findings and remaining non-blockers

## 8.1 Resolved in canonical commit `9f07e00`

- Three dead dialogue destinations in Campaign 2 Case 6 were repaired.
- The help panel and tutorial tip now match the implemented all-clues diagnosis gate.
- Campaign 1 Europa now uses the engine-supported `startMood` property.
- The owner reports successful syntax checks and a headless boot with no console/page errors.

These items remain in v0.1 as an historical discovery record. They are closed in v0.2 and should not be sent back for another agent audit.

## 8.2 Deliberately not treated as bugs

- Campaign 2 naming differences remain a future canonical/style decision.
- Runtime Case 7 versus design-document Case 6b remains a curriculum naming decision.
- Completionist scoring remains game design; academic grading will ignore it.
- No validator or expanded test framework is required for this curriculum project unless game development later creates a separate need.

# 9. Required-route and classroom timing audit

## 9.1 Main conclusion

Every case has a viable purposeful route that fits the owner’s approximately 20-minute gameplay target. The formal clue architecture itself is shallow: nearly every clue is found one obvious selection beyond a source’s entry node, with only a few requiring two steps. This is good for accessibility and classroom reliability, but it means clue collection alone is not a rigorous learning product. Rigor must come from comparing sources, ruling out alternatives, modeling the mechanism, and writing the CER.

The word estimates below include the briefing, direct-route node text, diagnosis choices, and final explanation. They do **not** include optional dialogue, time spent navigating, rereading, worksheet writing, or incorrect diagnosis feedback. They are planning estimates rather than promises about individual students.

| Case | Sources | Approx. direct-route words | Purposeful gameplay window | Best evidence-processing task |
|---|---:|---:|---|---|
| C1-1 — ISS Greenhouse Module | 4 | 541 | 8–12 min direct; 15–20 min with one cross-check per source | Evidence triage: identify which observations are symptoms, which are controlled variables, and which identify the missing cue. |
| C1-2 — Lunar Greenhouse | 4 | 515 | 8–12 min direct; 14–18 min with mechanical-pollination exploration | Reproductive-process flowchart: flower → pollen release/movement → stigma contact → fruit set; mark the missing step. |
| C1-3 — Mars Habitat | 4 | 609 | 9–13 min direct; 15–20 min with spectral cross-checks | Spectrum comparison: separate total photon flux, wavelength distribution, pigment response, and observed tissue pattern. |
| C1-4 — Hayes Orbital Station | 4 | 579 | 9–13 min direct; 15–20 min with timeline cross-checks | Timeline and variable isolation: distinguish the independent system change, delayed response, cellular damage, and downstream sensor fluctuations. |
| C1-5 — Europa Outpost | 4 | 529 | 8–12 min direct; 15–20 min with evidence-convergence dialogue | Risk-convergence matrix: hazard evidence, biological effect, failed protection, and eliminated alternatives. |
| C1-6 — First Contact Protocol | 4 | 977 | 13–17 min direct; 18–22 min with story/rapport exploration | Systems-interruption map: scrubber input → removed compounds → failed coordination → dormancy. |
| C1-7 — The Gift | 4 | 928 | 13–17 min direct; 18–22 min with solution-choice discussion | Missing-variable investigation plus solution comparison. |
| C2-1 — Vressk Centrifuge Habitat | 5 | 842 | 12–16 min direct; 17–20 min with species/cross-check dialogue | Gradient model: sketch direction and relative magnitude at the top and bottom of the bed; annotate biological response. |
| C2-2 — Ares Botanical Garden | 5 | 901 | 12–16 min direct; 17–20 min with failed-solution analysis | Failed-solution analysis: what was tried, what assumption it made, why it failed, and what mechanism the replacement must produce. |
| C2-3 — Oolian Mariculture Dome | 5 | 853 | 12–16 min direct; 17–20 min with action-spectrum comparison | Action-spectrum matching: overlay available wavelengths with relative pigment absorption and identify the weakest overlap. |
| C2-4 — Zhel’ii Diaspora Grove | 5 | 1,009 | 13–17 min direct; 18–22 min with callback synthesis | Two-concept synthesis: create a chain linking schedule, internal timing, compound production, and network behavior. |
| C2-5 — Concord Botanical Vault | 5 | 998 | 13–17 min direct; 18–22 min with policy/solution choice | Assumption and policy audit: identify the policy assumption, evidence that violates it, proposed exception, and safety constraints. |
| C2-6 — The First Garden | 5 | 1,099 | 14–18 min direct; 20+ min if the full Kess memory/rapport path is required | Evidence-based restoration recommendation with separate science, intervention, regulation, risk, and uncertainty boxes. |

## 9.2 Practical classroom implication

- Students should be told to obtain one formal clue from every available source before diagnosing.
- Teacher materials should name the source categories, not the correct node choices.
- Optional cross-checks should be encouraged when time remains but never required for completion.
- The worksheet should record interpretation, not copied dialogue. A student who finds all clues but cannot explain the mechanism has not yet demonstrated the learning objective.
- The two Campaign 1 first-contact cases and most Campaign 2 cases have higher reading loads; text-to-speech and chunked response boxes are especially important there.

# 10. Case-by-case required-route and instructional dossiers

## C1-1 — ISS Greenhouse Module

**Approximate direct-route reading load:** 541 words  
**Likely gameplay window:** 8–12 min direct; 15–20 min with one cross-check per source  
**Primary student practice:** Evidence triage: identify which observations are symptoms, which are controlled variables, and which identify the missing cue.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → problem_main` | Ask what the problem is. | Roots fail to orient downward. |
| Sensors | `start → gravity` | Display gravity data. | The habitat is in microgravity. |
| Plants | `start → roots` | Examine the roots. | Roots form tangled mats; shoots orient poorly. |
| Logs | `start → gravitropism_entry` | Search gravitropism. | Gravity normally supplies a directional cue. |

**Best optional cross-check:** Return to Kim after collecting sensor, plant, and log evidence; her gated responses explicitly connect zero gravity, root morphology, and the historical record.

**Implemented distractors:** nutrient burn, incorrect photoperiod, genetically defective seed stock.

**Likely student stumbling point:** Students may equate microgravity with “no forces” or assume roots simply grow toward water. The case also uses “zero g,” which should be corrected to microgravity/apparent weightlessness.

**CER frame:** Claim which environmental cue is missing; cite the gravity reading and root pattern; explain gravitropism and why physical/light guides could substitute.

**Exit ticket:** Why can a plant remain alive in microgravity while still growing in a disorganized way?

**NGSS candidates:** SEP: Constructing Explanations; CCC: Cause and Effect; MS-ETS1-1 (supporting, if students define guide criteria).

**Science disposition:** Core mechanism is sound. Edit “zero g” language and correct the Veggie first-harvest fun fact.

---

## C1-2 — Lunar Greenhouse

**Approximate direct-route reading load:** 515 words  
**Likely gameplay window:** 8–12 min direct; 14–18 min with mechanical-pollination exploration  
**Primary student practice:** Reproductive-process flowchart: flower → pollen release/movement → stigma contact → fruit set; mark the missing step.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → problem_main` | Ask for the observed pattern. | Healthy flowers drop without fruit. |
| Sensors | `start → airflow` | Display air circulation. | Air movement is nearly absent. |
| Plants | `start → flowers → pollen_close` | Inspect flowers, then pollen. | Mature pollen remains undisturbed. |
| Logs | `start → crop_protocols` | Open crop protocols. | No pollination plan was implemented. |

**Best optional cross-check:** After the pollen clue, read the hand/mechanical pollination log entries or try the gated stem-shaking interaction. These turn the solution into a testable mechanism rather than a vocabulary answer.

**Implemented distractors:** toxic lunar regolith, missing ultraviolet light, excess carbon dioxide.

**Likely student stumbling point:** Students may think “self-pollinating” means no pollen movement is needed, or assume every flowering crop uses the same mechanism.

**CER frame:** Claim that pollination failure caused the missing fruit; cite undisturbed pollen, low airflow, and absent pollination plan; explain why healthy flowers alone are insufficient.

**Exit ticket:** Why did extra nutrients or healthier leaves fail to solve this case?

**NGSS candidates:** SEP: Constructing Explanations; CCC: Structure and Function; MS-ETS1-2 (compare fans, vibration, or manual approaches).

**Science disposition:** Core tomato-pollination mechanism is sound. Replace the unsupported 1990s bumblebee fun fact with NASA’s documented honeybee experiments (1982/1984).

---

## C1-3 — Mars Habitat

**Approximate direct-route reading load:** 609 words  
**Likely gameplay window:** 9–13 min direct; 15–20 min with spectral cross-checks  
**Primary student practice:** Spectrum comparison: separate total photon flux, wavelength distribution, pigment response, and observed tissue pattern.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → problem_main` | Ask about the crop decline. | New growth yellows first and ignores nutrient additions. |
| Sensors | `start → lighting_data` | Display lighting-system data. | Light arrives through surface pipes plus white LEDs. |
| Plants | `start → upper_leaves` | Examine new leaves. | New tissue fails to develop chlorophyll. |
| Logs | `start → spectrum_search → red_wavelength_detail` | Search spectrum requirements, then details. | The record attributes chlorophyll formation to needed wavelengths. |

**Best optional cross-check:** Use the gated spectral analysis and fiber-optic search to compare total PAR with wavelength distribution. This is the case’s strongest conceptual move: quantity is not quality.

**Implemented distractors:** perchlorate/root poisoning, excess carbon dioxide, Martian-sol photoperiod disruption.

**Likely student stumbling point:** The current mechanism teaches a real spectrum concept through a likely false engineering cause: Martian dust is described as preferentially removing red light, while NASA observations show dust storms transmitting red while strongly suppressing green and blue.

**CER frame:** Claim that a spectrum mismatch—not total light or nutrients—caused the symptom; cite new-growth bleaching and the measured delivery system; explain why adequate PAR can still be biologically inadequate.

**Exit ticket:** What is the difference between “enough light” and “the right light”?

**NGSS candidates:** SEP: Analyzing and Interpreting Data; CCC: Energy and Matter; MS-LS1-6 (supporting context only); MS-ETS1-2.

**Science disposition:** Major game-text edit required. Preserve the spectrum lesson but replace the Mars-dust/borosilicate red-loss mechanism with a measured equipment fault, filter/coating problem, or failed red LED channel. Soften the claim that green light is wasted.

---

## C1-4 — Hayes Orbital Station

**Approximate direct-route reading load:** 579 words  
**Likely gameplay window:** 9–13 min direct; 15–20 min with timeline cross-checks  
**Primary student practice:** Timeline and variable isolation: distinguish the independent system change, delayed response, cellular damage, and downstream sensor fluctuations.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → problem_main → lighting_change` | Ask what happened and what changed. | Crashes began after the station switched to 24/0 light. |
| Sensors | `start → light_data` | Display light exposure. | The reactor receives continuous corridor lighting. |
| Culture | `start → microscope` | Inspect under a microscope. | Cells show photooxidative stress rather than infection. |
| Logs | `start → photoperiod_entry` | Search light requirements. | The manual asserts a required dark period. |

**Best optional cross-check:** Build the change/crash timeline, then read the continuous-light and photooxidative-stress entries. The temporal sequence is stronger evidence than the manual’s overbroad biological claim.

**Implemented distractors:** nutrient contamination, inconsistent carbon dioxide, microbial infection.

**Likely student stumbling point:** Students may learn the false universal rule that Spirulina necessarily dies without darkness. Continuous cultivation and illumination can work; damage depends on irradiance, culture density, mixing, temperature, and reactor control.

**CER frame:** Claim that the lighting change exceeded the reactor/culture’s safe operating conditions; cite the change timeline and microscopy; explain photoinhibition/photooxidative stress without declaring darkness universally essential.

**Exit ticket:** Why is the CO₂ fluctuation better treated as an effect of the crash than its original cause?

**NGSS candidates:** SEP: Analyzing and Interpreting Data; CCC: Cause and Effect; MS-ETS1-2.

**Science disposition:** Major game-text edit required. Reframe from “continuous light always causes collapse” to reactor-specific excessive continuous irradiance/insufficient light control; restoring a controlled cycle is one valid engineering fix, not a universal biological law.

---

## C1-5 — Europa Outpost

**Approximate direct-route reading load:** 529 words  
**Likely gameplay window:** 8–12 min direct; 15–20 min with evidence-convergence dialogue  
**Primary student practice:** Risk-convergence matrix: hazard evidence, biological effect, failed protection, and eliminated alternatives.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → problem_main` | Ask what has remained consistent. | Every seed batch follows the same failure pattern. |
| Sensors | `start → radiation_detail` | Display radiation monitoring. | The growth bay has an elevated ionizing-radiation reading. |
| Plants | `start → microscope` | Inspect seedlings microscopically. | Rapidly dividing tissues show damage consistent with DNA injury. |
| Logs | `start → construction_log` | Review shielding specifications. | Shielding was not assessed for crop tolerance. |

**Best optional cross-check:** The crew tree contains multiple pairwise and full-picture responses. Returning after two or three clues gives students explicit practice combining independent lines of evidence.

**Implemented distractors:** low gravity, mineral-contaminated water, excessive LED intensity.

**Likely student stumbling point:** The specific fictional dose can look more certain than it is, and the explanation incorrectly groups lunar bases with the ISS as protected by Earth’s magnetosphere.

**CER frame:** Claim that inadequate radiation shielding caused repeated seedling failure; cite the radiation reading, DNA-damage pattern, and unvalidated shielding; explain why reproducing the result across seed batches points away from genetics.

**Exit ticket:** Why is the construction log necessary if the sensor and microscope already point to radiation?

**NGSS candidates:** SEP: Argument from Evidence; CCC: Cause and Effect; MS-ETS1-1; MS-ETS1-2.

**Science disposition:** Core radiation-risk principle is sound. Label the Europa dose and secondary-particle scenario as modeled fiction. Correct the Moon comparison: the ISS receives substantial geomagnetic protection; the lunar surface is largely exposed.

---

## C1-6 — First Contact Protocol

**Approximate direct-route reading load:** 977 words  
**Likely gameplay window:** 13–17 min direct; 18–22 min with story/rapport exploration  
**Primary student practice:** Systems-interruption map: scrubber input → removed compounds → failed coordination → dormancy.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → symbiosis_detail` | Ask about the “three-who-are-one.” | The organism depends on coordinated symbiosis. |
| Sensors | `start → atmosphere` | Analyze atmospheric composition. | Human scrubbers remove trace volatile compounds. |
| Organism | `start → network` | Inspect network structures. | The network is intact but dormant. |
| Logs | `start → network_comm` | Search communication records. | The system coordinates through volatile signals. |

**Best optional cross-check:** Ask what changed at docking, then cross-reference the filtered compounds. This cleanly links a human engineering system to an unintended biological consequence.

**Implemented distractors:** physical docking damage, long-term atmospheric drift, symbiont incompatibility.

**Likely student stumbling point:** Students may anthropomorphize chemical signaling or interpret an alien mechanism as direct evidence that Earth plants consciously communicate.

**CER frame:** Claim that atmospheric scrubbing disrupted the symbiosis; cite intact anatomy, missing volatiles, and docking timing; explain why “cleaner” air can be harmful to a different biological system.

**Exit ticket:** Which part of the human habitat worked exactly as designed—and still caused the failure?

**NGSS candidates:** SEP: Developing and Using Models; CCC: Systems and System Models; MS-LS2-4 (analogy, not literal alien evidence); MS-ETS1-2.

**Science disposition:** Treat the alien network as fiction inspired by real VOC signaling and symbiosis. Teacher materials must distinguish chemical responses from intentional language or established “plant conversation.”

---

## C1-7 — The Gift

**Approximate direct-route reading load:** 928 words  
**Likely gameplay window:** 13–17 min direct; 18–22 min with solution-choice discussion  
**Primary student practice:** Missing-variable investigation plus solution comparison.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → proximity_detail` | Ask why the pod must be near mature growth. | Established networks supply a missing context. |
| Sensors | `start → atmosphere` | Scan atmospheric composition. | The isolation chamber lacks trace VOCs. |
| Pod | `start → receptors` | Inspect receptor structures. | The viable pod is waiting for a chemical trigger. |
| Logs | `start → germination` | Search germination biology. | A mature network releases the needed trigger compound. |

**Best optional cross-check:** Compare extraction, synthesis, and living-network placement. This makes the case a compact culmination about mechanism, evidence, risk, and intervention.

**Implemented distractors:** wrong light wavelength, transfer damage, inhibitory human microbes.

**Likely student stumbling point:** Students may collapse “a molecule can trigger germination” into “all seeds need nearby mature plants.” The implemented biology is alien fiction.

**CER frame:** Claim that the pod requires a chemical germination cue; cite receptor readiness, missing VOCs, and archive evidence; explain why viability without germination indicates dormancy rather than damage.

**Exit ticket:** What evidence proves that the pod is waiting rather than dead?

**NGSS candidates:** SEP: Constructing Explanations and Designing Solutions; CCC: Structure and Function; MS-ETS1-2.

**Science disposition:** Keep as clearly labeled alien fiction. Use Earth VOC/germination research only as inspiration, noting that biological volatiles can stimulate or inhibit responses depending on organism and compound.

---

## C2-1 — Vressk Centrifuge Habitat

**Approximate direct-route reading load:** 842 words  
**Likely gameplay window:** 12–16 min direct; 17–20 min with species/cross-check dialogue  
**Primary student practice:** Gradient model: sketch direction and relative magnitude at the top and bottom of the bed; annotate biological response.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → problem_main` | Ask what the crop is doing. | Tubers grow toward the ring wall. |
| Sensors | `start → gravity_profile` | Run the gravity profile. | Acceleration changes across bed depth. |
| Plants | `start → root_inspection` | Inspect roots/tubers. | Organs align with the local vector rather than intended rows. |
| Logs | `start → gorlroot_cultivation` | Read species requirements. | The crop is adapted to a uniform native field. |
| Database | `start → centrifugal_gradient` | Read centrifugal-gradient entry. | Rotating habitats inherently produce radial gradients. |

**Best optional cross-check:** Return to the Vressk botanist with each evidence type. The gated responses convert a physics fact into a species-specific design failure.

**Implemented distractors:** average gravity too strong, wrong nutrients, shallow soil alone.

**Likely student stumbling point:** Students may focus on the displayed average g and miss spatial variation. The case should not require formal algebra unless adapted for older learners.

**CER frame:** Claim that nonuniform centrifugal acceleration caused the pattern; cite the profile and organ orientation; explain why matching average 2.1g is insufficient.

**Exit ticket:** How can a system be “calibrated correctly” and still provide the wrong environment?

**NGSS candidates:** SEP: Developing and Using Models; CCC: Scale, Proportion, and Quantity; MS-ETS1-1; MS-ETS1-2.

**Science disposition:** The rotational gradient is real; species sensitivity and exact design tolerances are fictional. Treat large habitat-dimension claims as fictional engineering context unless separately sourced.

---

## C2-2 — Ares Botanical Garden

**Approximate direct-route reading load:** 901 words  
**Likely gameplay window:** 12–16 min direct; 17–20 min with failed-solution analysis  
**Primary student practice:** Failed-solution analysis: what was tried, what assumption it made, why it failed, and what mechanism the replacement must produce.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → cultural_barrier` | Ask what the botanist suspects. | Buds abort and crucial knowledge was not shared clearly. |
| Sensors | `start → acoustic_scan` | Scan acoustic conditions. | The expected vibration is absent. |
| Plants | `start → anther_exam` | Inspect anthers. | Mature pollen remains trapped. |
| Logs | `start → pollination_log` | Review prior attempts. | Contact-based hand pollination already failed. |
| Database | `start → buzz_pollination` | Read vibration-pollination entry. | Pollen release requires mechanical vibration. |

**Best optional cross-check:** Use the hand-pollination failure as explicit disconfirming evidence. This teaches that a plausible solution can fail because it targets the wrong mechanism.

**Implemented distractors:** ordinary hand pollination, wrong photoperiod, trace nutrient deficiency.

**Likely student stumbling point:** Students may treat frequency as a magic number rather than one part of vibration amplitude, coupling, duration, and flower structure.

**CER frame:** Claim that an acoustic/mechanical trigger is missing; cite trapped pollen, absent vibration, and failed hand transfer; explain buzz pollination.

**Exit ticket:** What did the failed hand-pollination attempt teach that a successful attempt could not?

**NGSS candidates:** SEP: Evaluating Design Solutions; CCC: Structure and Function; MS-ETS1-2.

**Science disposition:** Earth buzz pollination is well established. The Telluvian organism, exact frequency, and cultural history are fictional; avoid implying frequency alone determines release.

---

## C2-3 — Oolian Mariculture Dome

**Approximate direct-route reading load:** 853 words  
**Likely gameplay window:** 12–16 min direct; 17–20 min with action-spectrum comparison  
**Primary student practice:** Action-spectrum matching: overlay available wavelengths with relative pigment absorption and identify the weakest overlap.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → problem_main` | Ask what changed. | Kelp declined only in the new Earth-lit dome. |
| Sensors | `start → spectral_analysis` | Inspect spectrum. | The system is heavily red-weighted. |
| Kelp | `start → magnification` | Inspect pigments/tissue. | Pigments are adapted to blue-green-rich conditions. |
| Logs | `start → kelp_profile` | Read evolutionary habitat. | The organism evolved in spectrally filtered deep water. |
| Database | `start → chlorophyll_variants` | Compare pigment systems. | Different antenna pigments capture different spectral regions. |

**Best optional cross-check:** Compare old and new domes as a natural control. The “defective light” distractor becomes useful for separating equipment function from biological suitability.

**Implemented distractors:** defective lamps, insufficient total intensity, water chemistry drift.

**Likely student stumbling point:** The current correct diagnosis says the kelp cannot use red light and the dome is functionally dark. Real brown algae still use chlorophyll a and transfer energy from chlorophyll c/fucoxanthin; the mismatch should be relative, not absolute.

**CER frame:** Claim that the lamp spectrum is poorly matched to the organism; cite the spectrum, pigment profile, and old-dome comparison; explain adaptation to available light.

**Exit ticket:** Why are the lights neither broken nor appropriate?

**NGSS candidates:** SEP: Analyzing and Interpreting Data; CCC: Energy and Matter; MS-LS1-6 (supporting); MS-ETS1-2.

**Science disposition:** Minor-to-moderate wording edit. Preserve the pigment lesson but replace absolutes (“cannot use red,” “effectively dark”) with low efficiency/poor spectral match.

---

## C2-4 — Zhel’ii Diaspora Grove

**Approximate direct-route reading load:** 1,009 words  
**Likely gameplay window:** 13–17 min direct; 18–22 min with callback synthesis  
**Primary student practice:** Two-concept synthesis: create a chain linking schedule, internal timing, compound production, and network behavior.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → timeline` | Ask when signaling stopped. | Silence follows a recent management change. |
| Sensors | `start → light_data` | Inspect light schedule. | The grove receives 24/0 light. |
| Grove | `start → signal_structures` | Inspect structures. | Tissue is healthy but signal compounds are absent. |
| Logs | `start → health_timeline` | Compare the timeline. | The shift from 18/6 to 24/0 precedes silence. |
| Database | `start → circadian_data` | Read species rhythm data. | The fictional network requires darkness to activate/reset signaling. |

**Best optional cross-check:** Ask the caretaker about each clue after collection. The case is strongest when students explicitly combine the Campaign 1 lighting and signaling concepts.

**Implemented distractors:** atmospheric filtering drift, light-intensity bleaching, general transit stress.

**Likely student stumbling point:** Students may overgeneralize the alien requirement into “all plants perform their most important work at night” or “stomata close at night in every plant.”

**CER frame:** Claim that continuous light suppressed the fictional circadian signaling pathway; cite healthy tissue, absent compounds, and the timeline; explain why this is functional silence rather than damage.

**Exit ticket:** Which evidence shows that this case is about timing rather than too much energy?

**NGSS candidates:** SEP: Constructing Explanations; CCC: Patterns; CCC: Cause and Effect.

**Science disposition:** Keep as species-specific alien fiction. Teacher notes should explain that Earth circadian responses and continuous-light tolerance vary widely; nighttime examples are illustrative, not universal.

---

## C2-5 — Concord Botanical Vault

**Approximate direct-route reading load:** 998 words  
**Likely gameplay window:** 13–17 min direct; 18–22 min with policy/solution choice  
**Primary student practice:** Assumption and policy audit: identify the policy assumption, evidence that violates it, proposed exception, and safety constraints.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Crew | `start → keltor_suspicion` | Ask for the administrator’s theory. | Medicinal output fails despite a seemingly perfect vault. |
| Sensors | `start → radiation_data` | Read radiation data. | The chamber reports zero background radiation. |
| Bloom | `start → tissue_analysis` | Analyze tissue/pathway activity. | The DNA-repair-linked pathway is inactive. |
| Logs | `start → homeworld` | Read native environment. | The species evolved under high background radiation. |
| Database | `start → hormesis` | Read Concord entry. | The database asserts fictional obligate radiation dependence. |

**Best optional cross-check:** Compare a general safety policy with species-specific evidence. The case is an excellent assumption audit even if the Earth analogy is corrected.

**Implemented distractors:** trace nutrient deficiency, humidity/temperature mismatch, delayed transplant shock.

**Likely student stumbling point:** The current text presents radiation hormesis and fungal “radiosynthesis” as settled, direct analogues. Evidence exists for enhanced growth/metabolism in some melanized fungi under particular exposures, but the mechanism and generality are not equivalent to photosynthesis; human/plant hormesis is contested.

**CER frame:** Claim that the fictional species requires a low-level radiation-triggered pathway; cite zero exposure, inactive pathway, and native conditions; clearly separate story biology from the tentative Earth analogy.

**Exit ticket:** Why is “remove every hazard” not automatically a biologically neutral policy?

**NGSS candidates:** SEP: Argument from Evidence; CCC: Stability and Change; MS-ETS1-1; MS-ETS1-2.

**Science disposition:** Major qualification required. Label obligate radiation dependence as fiction. Rewrite the Earth parallel to say some experiments found radiation-enhanced growth/metabolism in melanized fungi under specific conditions; avoid stating established radiosynthesis or general radiation hormesis.

---

## C2-6 — The First Garden

**Approximate direct-route reading load:** 1,099 words  
**Likely gameplay window:** 14–18 min direct; 20+ min if the full Kess memory/rapport path is required  
**Primary student practice:** Evidence-based restoration recommendation with separate science, intervention, regulation, risk, and uncertainty boxes.

### Required evidence route

| Source | Direct node route | Student-facing action | Evidence contribution |
|---|---|---|---|
| Nova | `start → problem` | Ask what restoration has already tried. | Chemistry and conventional repairs have been exhausted. |
| Vorn-Shael | `start → chemical_reading` | Ask what the chemical pattern shows. | Useful compounds remain isolated in patches. |
| Ilreth-Mar | `start → role → biosafety_overview` | Ask role, then applicable protocol. | Cross-zone inoculation is restricted. |
| Database | `start → exemptions` | After regulation is known, search precedents. | An exemption route exists. |
| Kess | `start → database_assist` | Use the database-assisted prompt. | The missing biological connection is identified as mycorrhizal. |

**Best optional cross-check:** The richer path is Kess’s fragmented-memory sequence plus the database’s mycorrhizal and biosafety entries. The shortest current path can reveal the mycorrhizal clue through a “database entries” prompt after reading only the legal-precedent clue; teacher materials should direct students to the biology entry before accepting the conclusion.

**Implemented distractors:** residual pH imbalance, irrigation inconsistency, new invasive organisms.

**Likely student stumbling point:** The case turns a valid fungal-root mutualism into overly categorical claims about mature trees subsidizing seedlings, defense warnings, universal resource sharing, and inoculation as the single required restoration fix.

**CER frame:** Claim that missing fungal-root connectivity is a plausible limiting factor; cite isolated chemical patches and soil history; explain the proposed mechanism while acknowledging uncertainty and evaluating the exemption.

**Exit ticket:** Which part of the final recommendation is directly supported, which is inferred, and which remains uncertain?

**NGSS candidates:** SEP: Argument from Evidence; SEP: Evaluating Design Solutions; CCC: Systems and System Models; MS-LS2-3; MS-LS2-5; MS-ETS1-2.

**Science disposition:** Major qualification required. Keep mycorrhizal mutualism and fungal nutrient acquisition as established. Present plant-to-plant transfer/benefit as context-dependent and debated. Correct the carbon fun fact to 13.12 Gt CO₂e allocated to mycorrhizal mycelium annually—not 13 billion tons of stored carbon or a 2023 global map.

---


# 11. Serious-science verification and game-text disposition

The audit applies three labels:

- **Keep:** adequately accurate at the level required by the game.
- **Qualify in teacher materials:** the game may remain unchanged, but instruction must distinguish established science from extrapolation or fiction.
- **Edit game text:** a central or memorable statement is materially misleading enough to affect classroom learning.

| Case/content | Disposition | Verified judgment | Minimum corrective action |
|---|---|---|---|
| C1-1 microgravity/gravitropism | Minor edit | Plants can grow in microgravity when light, water, nutrients, air, and hardware are managed; gravity-related orientation changes, but “0.00 g” is not literally absence of gravity. | Use “microgravity/apparent weightlessness”; retain alternative cue/guide solution. |
| C1-1 Veggie fun fact | Edit game text | Veggie began in 2014; Steve Swanson harvested the first red-romaine crop for return and analysis. The first station-grown crop officially eaten was a second crop in August 2015 by Kimiya Yui, Kjell Lindgren, and Scott Kelly. | Replace sole attribution to Scott Kelly and distinguish first harvest from first eaten harvest. |
| C1-2 pollination | Keep | Tomato anthers release pollen through physical vibration; low air movement and no vibration/pollinator can prevent fruit set. | Keep core case; state that mechanisms vary among crops. |
| C1-2 bee fun fact | Edit game text | NASA documented worker honeybee flight in 1982 and a honeycomb-building/hive experiment in 1984—not a 1990s bumblebee habitat trial. | Replace species, decade, and claim with the documented honeybee experiment. |
| C1-3 Mars dust/light pipes | Edit game text | NASA observations during a Martian dust storm reported red light reaching the surface while little green and essentially no blue passed through. The game’s specific 12 m borosilicate loss table is unsourced and likely implausible as written. | Keep the spectrum-mismatch lesson but make the cause a verified equipment/filter/LED fault rather than generic Mars dust and glass. |
| C1-3 green light fun fact | Edit/soften | Green light is less absorbed near leaf surfaces but can drive photosynthesis and penetrate deeper into leaves/canopies; it is not merely wasted. | Replace “smart growers skip it” with a balanced statement about red, blue, and green roles. |
| C1-4 Spirulina and darkness | Edit game text | Long-term continuous *Limnospira/Arthrospira* cultivation is feasible. Photoinhibition depends on photon flux, cell density, mixing, and reactor conditions, and can be reversible. | Reframe as reactor-specific continuous overexposure/poor control, not a universal essential dark period. |
| C1-5 radiation injury | Keep with fiction label | Simulated space radiation can reduce seed viability and alter seedling development in dose- and ion-dependent ways. | Keep core hazard; label exact Europa dose and particle scenario as modeled fiction. |
| C1-5 Moon/ISS protection comparison | Edit game text | The ISS benefits from low-Earth-orbit geomagnetic protection. The Moon has almost no atmosphere and no global magnetic field; it receives only intermittent/partial shielding when passing through Earth’s magnetosphere. | Do not group lunar bases with ISS protection. |
| C1-6/7 VOC signaling | Qualify | Biological VOCs can affect organisms and plant/fungal physiology, but responses vary and should not be portrayed as intentional speech. | Keep alien mechanism as fiction inspired by real chemical signaling. |
| C2-1 centrifugal gradient | Keep with fiction label | In a rotating habitat, apparent acceleration varies with radius. NASA uses centrifuges to create partial/artificial gravity for biological research. | Keep physics; label alien tolerance and architectural numbers as fiction unless sourced. |
| C2-2 buzz pollination | Keep with fiction label | Vibrations transmit through flowers and can eject pollen from poricidal anthers; amplitude, frequency, coupling, and duration matter. | Keep Earth analogy; label alien exact trigger as fiction. |
| C2-3 pigment mismatch | Minor edit | Brown algae/diatoms use chlorophyll a/c and fucoxanthin complexes that transfer absorbed energy. Spectral adaptation is real, but red light is not simply unusable. | Change absolute “functionally dark” wording to poor match/reduced efficiency. |
| C2-4 circadian signaling | Qualify | Circadian timing is real, but continuous-light injury and nighttime metabolism vary among species. The Zhel’ii dark-triggered VOC pathway is fictional. | Keep case as species-specific fiction; remove universal Earth claims. |
| C2-5 radiation hormesis/radiosynthesis | Edit game text | Some experiments report enhanced growth or metabolism in melanized fungi under ionizing radiation, and melanin is radioprotective. The “radiosynthesis” interpretation and broad radiation hormesis claims are not settled or universal. | Explicitly label obligate radiation dependence as fiction; describe the fungal analogy as limited and under study. |
| C2-6 mycorrhizal networks | Edit game text | Mycorrhizal root–fungus mutualism and nutrient exchange are established. Common networks can exist, but generalized claims that mature trees preferentially subsidize seedlings or reliably send warnings are contested and context-dependent. | Replace categorical cooperation claims with evidence-calibrated language and uncertainty. |
| C2-6 carbon fun fact | Edit game text | A 2023 synthesis estimated 13.12 Gt CO₂e fixed by plants is allocated at least temporarily to mycorrhizal mycelium per year. That is a flux/allocation estimate, not 13 billion tons of carbon stored, and the paper was not the first global fungal map. | Correct units, meaning, and attribution. |

## 11.1 Priority order for eventual game-text revisions

1. C1-3 Mars spectral-loss mechanism.
2. C1-4 universal Spirulina dark-period claim.
3. C2-5 settled hormesis/radiosynthesis language.
4. C2-6 categorical “wood wide web” and restoration claims.
5. C1-5 Moon magnetosphere comparison.
6. C1-1 and C1-2 historical fun facts.
7. C2-3 and C1-3 absolute statements about usable/green light.

These should be addressed through a later **exact replacement-text specification**, not through another broad agent audit.


# 12. Final NGSS alignment map

NGSS alignment belongs to the **student product around gameplay**, not to game completion alone. The game supplies a phenomenon, information sources, competing explanations, and design constraints. The lesson must require students to use an identified Science and Engineering Practice with appropriate disciplinary ideas and a crosscutting concept.

| Case | SEP emphasized | DCI/component used | CCC | Assessed student product | PE relationship and limitation |
|---|---|---|---|---|---|
| C1-1 ISS Greenhouse | Constructing Explanations; Defining Problems | ETS1.A/B; plant structure/function as supporting science | Cause and Effect | Evidence-based diagnosis plus criteria for an alternative root-orientation system | Supports MS-ETS1-1/2. Gravitropism itself is not a standalone middle-school PE. |
| C1-2 Lunar Greenhouse | Developing and Using Models; Evaluating Solutions | LS1.A structure/function; ETS1.B | Structure and Function | Pollination process model and comparison of fan, vibration, or manual solutions | Strongest as MS-ETS1-2 support; do not claim a full reproduction PE from one tomato case. |
| C1-3 Mars Habitat | Analyzing and Interpreting Data; Constructing Explanations | LS1.C photosynthetic energy capture; ETS1.B | Energy and Matter; Cause and Effect | Spectrum comparison, elimination of total-intensity explanation, and corrected optical-system recommendation | Supports MS-LS1-6 and MS-ETS1-2. NGSS explicitly excludes detailed biochemical mechanisms of photosynthesis from MS-LS1-6 assessment. |
| C1-4 Hayes Orbital Station | Analyzing Data; Designing Solutions | ETS1.B/C; biological system regulation as supporting science | Cause and Effect; Stability and Change | Timeline correlation and independent bioreactor-control redesign | Supports MS-ETS1-2. Do not assess the false generalization that all photosynthetic organisms require darkness. |
| C1-5 Europa Outpost | Engaging in Argument from Evidence; Defining Problems | ETS1.A/B; DNA damage as supporting content | Cause and Effect; Systems and System Models | Radiation-cause argument and shielding criteria/constraints | Supports MS-ETS1-1/2. Exact dose, shielding percentages, and Europa facility are modeled fiction. |
| C1-6 First Contact Protocol | Developing and Using Models | LS2.C ecosystem dynamics as analogy; ETS1.B | Systems and System Models | Model linking atmospheric change, signaling loss, and symbiosis failure | Can support MS-LS2-4 practice/component work, but alien evidence cannot serve as empirical proof about Earth ecosystems. |
| C1-7 The Gift | Constructing Explanations; Evaluating Solutions | ETS1.B | Systems and System Models; Cause and Effect | Missing-variable synthesis and justified germination intervention | Supports MS-ETS1-2. The receptor and germination chemistry are fictional. |
| C2-1 Vressk Centrifuge Habitat | Developing and Using Models; Defining Problems | ETS1.A/B; gravity/rotation concepts as supporting physical science | Scale, Proportion, and Quantity; Systems | Radial-gradient model and revised habitat criteria | Supports MS-ETS1-1/2; may connect to MS-ESS1-2 conceptually. Formal rotational mathematics should be optional for middle school. |
| C2-2 Ares Botanical Garden | Evaluating Design Solutions | LS1.A structure/function; ETS1.B | Structure and Function | Failure analysis comparing contact, airflow, and vibration-coupled pollination solutions | Supports MS-ETS1-2. Alien floral trigger remains fiction; Earth buzz pollination supplies the analogy. |
| C2-3 Oolian Mariculture Dome | Analyzing Data; Constructing Explanations | LS1.C photosynthetic energy capture; ETS1.B | Energy and Matter | Action-spectrum/spectral-match analysis and lamp redesign | Supports MS-LS1-6 and MS-ETS1-2. Assess spectrum and energy capture, not memorization of alien pigment names. |
| C2-4 Zhel’ii Diaspora Grove | Constructing Explanations from Multiple Sources | Circadian regulation as supporting life science; no strong direct MS DCI | Patterns; Cause and Effect | Timeline model linking schedule change, signal-compound output, and network silence | Best claimed at SEP/CCC level. The species-specific dark-triggered VOC pathway is fiction. |
| C2-5 Concord Botanical Vault | Engaging in Argument from Evidence; Evaluating Solutions | ETS1.A/B | Stability and Change; Cause and Effect | Species-specific policy assumption audit and constrained solution comparison | Supports MS-ETS1-1/2. Radiation dependence is fictional, so the assessed target is evidence use and policy design. |
| C2-6 The First Garden | Developing Models; Argument from Evidence; Evaluating Solutions | LS2.B matter transfer; LS2.C ecosystem dynamics; ETS1.B | Systems and System Models; Energy and Matter | Qualified mycorrhizal model plus monitored restoration and policy recommendation | Can support MS-LS2-3, MS-LS2-5, and MS-ETS1-2 only if the product models matter flow, compares solutions, and explicitly includes scientific uncertainty. |

## 12.1 Campaign-level assessment alignment

- **Pre-assessment:** Students interpret an unfamiliar plant-failure scenario, separate observations from possible causes, and identify missing evidence.
- **Campaign 1 culmination — The Gift:** Students construct a multi-source explanation and evaluate a biologically appropriate intervention.
- **Campaign 2 culmination — The First Garden:** Students evaluate a restoration solution under scientific uncertainty, biosafety constraints, and policy trade-offs.
- **Final SSS post-assessment:** Students diagnose two or three unseen short scenarios, explain causal mechanisms, reject plausible distractors, and identify a limitation in the evidence.

## 12.2 Standards-claim rule

A lesson may state “aligned to” a full performance expectation only when its assessed student product actually performs the PE. Otherwise use language such as:

- “supports components of…”
- “uses the SEP/CCC associated with…”
- “provides context for…”
- “does not by itself fulfill the complete PE.”

Official references:

- MS-LS1-6: https://www.nextgenscience.org/pe/ms-ls1-6-molecules-organisms-structures-and-processes
- MS-LS2-3: https://www.nextgenscience.org/pe/ms-ls2-3-ecosystems-interactions-energy-and-dynamics
- MS-LS2-5: https://www.nextgenscience.org/pe/ms-ls2-5-ecosystems-interactions-energy-and-dynamics
- MS-ETS1: https://www.nextgenscience.org/msets1-engineering-design


# 13. Confirmed 60-minute instructional architecture

| Time | Activity | Required student product |
|---:|---|---|
| 0–5 min | Mission launch and individual prediction | One initial hypothesis or “evidence needed” statement |
| 5–8 min | Controls, source categories, and evidence-log directions | Student identifies the available evidence channels |
| 8–28 min | Purposeful gameplay | One concise evidence entry per formal source; optional cross-checks as time permits |
| 28–38 min | Case-specific processing task | Diagram, timeline, comparison, model, or solution matrix |
| 38–48 min | CER | One claim, selected evidence, and mechanism-based reasoning |
| 48–55 min | Teacher debrief or short source/media context | Correction/qualification of fiction and scientific simplifications |
| 55–60 min | Individual exit ticket | One transferable concept or uncertainty statement |

For the heavier reading cases, the teacher may allow gameplay to continue to minute 30 and compress the debrief. External videos/readings should be optional unless they perform a necessary correction that the game itself does not yet contain.


# 14. Campaign and final culmination disposition

## Campaign 1

Use **The Gift** as the campaign culmination rather than adding a separate large project. Its missing-variable problem asks students to combine viability evidence, receptor structure, atmospheric chemistry, and prior signaling ideas. The student product should remain one-period and individual.

## Campaign 2

Use **The First Garden** as the campaign culmination, but the worksheet must explicitly separate:

1. established Earth science;
2. evidence inside the fictional case;
3. inferred mechanism;
4. proposed restoration action;
5. policy route and constraints;
6. scientific uncertainty.

## Final SSS synthesis

Use a one-period post-assessment with two or three short unseen cases. At least one should invert an earlier assumption—for example, a hazard that is actually within tolerance, or adequate light quantity with the wrong spectrum. Students should not need to build a multiday presentation or group project.


# 15. Cross-case conclusions from Pass 2

## 15.1 Clue acquisition and learning are not the same thing

The formal clue system reliably prevents students from diagnosing without visiting every source. It does not, by itself, require them to explain why the sources agree. The curriculum’s central value is therefore to convert **collected clues** into **warranted conclusions**.

## 15.2 The best recurring student move is evidence classification

Across the game, evidence usually falls into four functional categories:

- **symptom/pattern** — what is happening;
- **environmental or system condition** — what differs;
- **mechanism evidence** — how the condition affects biology;
- **history/design record** — why the condition exists or why protection failed.

The consistent mission-sheet template should preserve these categories while the case-specific processing task changes.

## 15.3 Campaign 2’s real advance is assumption testing

Campaign 1 mostly identifies a missing or harmful requirement. Campaign 2 asks whether human/Earth/Concord standards are valid for a different organism. This supports stronger work on model limitations, cultural knowledge, policy constraints, and species-specific design.

## 15.4 The game’s optional dialogue is valuable but cannot be mandatory

Gated cross-checks often contain the clearest reasoning language. Requiring all of them would break the 20-minute target. Teacher guides should identify one “best optional cross-check” per case and treat all other exploration as enrichment.

## 15.5 Campaign 2 Case 6 needs a curriculum-side evidence safeguard

The shortest implemented route can reach the Kess mycorrhizal clue through a database-assisted option after the student has obtained the legal-precedent clue, even if the student did not read the database’s mycorrhizal biology entry. This is not a runtime failure. The mission sheet should require one biology note from the mycorrhizal database entry before students recommend inoculation.

## 15.6 Academic grading remains independent from game score

A common rubric can score evidence accuracy, mechanism reasoning, vocabulary used in context, elimination of alternatives, CER quality, and exit-ticket transfer. Rapport choices, rank, optional nodes, and speed should remain ungraded.


# 16. Canonical curriculum naming and numbering

The game uses several labels for narrative and organizational purposes. The curriculum should not force a game rename. Use the following stable labels in filenames, teacher directions, and student materials:

## Campaign 1

**Curriculum label:** `Campaign 1 — Solar Agricultural Authority`

| Curriculum number | Runtime ID | Student-facing case name |
|---:|---|---|
| 1 | `iss` | ISS Greenhouse Module |
| 2 | `lunar` | Lunar Greenhouse |
| 3 | `mars` | Mars Habitat |
| 4 | `orbital` | Hayes Orbital Station |
| 5 | `europa` | Europa Outpost |
| 6 | `alien1` | First Contact Protocol |
| 7 | `alien2` | The Gift |

The source comment “Case 6b” is a development-history label only. The runtime presents a distinct seventh playable case. Curriculum files should therefore use **Case 7**.

## Campaign 2

**Curriculum label:** `Campaign 2 — Distant Soils: Federation Field Cases`

This preserves both implemented identities:

- `Distant Soils` is the narrative campaign/title-screen identity.
- `Federation Field Cases` is the campaign data and organizational identity.

| Curriculum number | Runtime ID | Student-facing case name |
|---:|---|---|
| 1 | `heavy_hands` | Vressk Centrifuge Habitat |
| 2 | `missing_dance` | Ares Botanical Garden |
| 3 | `wrong_color_light` | Oolian Mariculture Dome |
| 4 | `silent_grove` | Zhel’ii Diaspora Grove |
| 5 | `too_clean_room` | Concord Botanical Vault |
| 6 | `first_garden` | The First Garden |

Teacher materials may use design codenames such as “The Missing Dance” in notes, but student filenames and pacing documents should use the implemented case names above.

# 17. Exact correction specification

The implementation-ready correction package is stored separately as:

`SSS_SCIENCE_TEXT_CORRECTION_SPEC_v0.1.md`

It contains exact replacement text for:

1. microgravity and Veggie-history wording;
2. NASA bee-history wording;
3. the Mars spectral-loss mechanism and green-light statement;
4. the Spirulina continuous-light mechanism;
5. ISS-versus-Moon radiation protection;
6. chlorophyll-c/fucoxanthin and spectral-match wording;
7. fictional karreth radiation dependence versus Earth fungal evidence;
8. evidence-calibrated mycorrhizal restoration claims and the updated 2026 global fungal map.

The specification intentionally avoids new tests, validators, refactors, scoring changes, or unrelated content work.

# 18. Final audit disposition

The analytical audit is complete. No additional broad repository audit is warranted.

Before issuing **v1.0**, complete only these steps:

1. Apply the approved text replacements from the correction specification.
2. Record the resulting SSS commit hash.
3. Re-run a syntax check and one boot/play-path check for the edited cases.
4. Reconcile this audit against the committed strings.
5. Mark all approved science findings resolved or intentionally teacher-qualified.

The static-content inventory remains at **v0.2** because this pass did not change the case structure, evidence counts, nodes, options, or route analysis. Creating an identical v0.3 JSON file would add version noise without new machine-readable information.

**Thinking setting:** remain on **High** until the science edits are committed and audit v1.0 is reconciled. Immediately before beginning the Curriculum Blueprint, change Sol to **Medium** and obtain owner confirmation.


## Appendix A — Content totals by case

| Campaign | Case ID | Sources | Clues | Nodes | Options | Approx. raw authored words |
|---|---|---:|---:|---:|---:|---:|
| C1 | `iss` | 4 | 4 | 91 | 231 | 4,241 |
| C1 | `lunar` | 4 | 4 | 55 | 133 | 2,867 |
| C1 | `mars` | 4 | 4 | 55 | 135 | 3,039 |
| C1 | `orbital` | 4 | 4 | 49 | 112 | 2,801 |
| C1 | `europa` | 4 | 4 | 48 | 123 | 2,813 |
| C1 | `alien1` | 4 | 4 | 58 | 163 | 5,650 |
| C1 | `alien2` | 4 | 4 | 47 | 128 | 5,439 |
| C2 | `heavy_hands` | 5 | 5 | 52 | 119 | 3,111 |
| C2 | `missing_dance` | 5 | 5 | 44 | 101 | 3,018 |
| C2 | `wrong_color_light` | 5 | 5 | 48 | 105 | 3,301 |
| C2 | `silent_grove` | 5 | 5 | 46 | 107 | 3,593 |
| C2 | `too_clean_room` | 5 | 5 | 44 | 104 | 3,892 |
| C2 | `first_garden` | 5 | 5 | 73 | 151 | 5,575 |

## Appendix B — Static integrity disposition

The uploaded data snapshot parsed successfully, each case contains exactly one correct diagnosis, and every formal clue has at least one revealing node. The three missing destinations identified in v0.1 were corrected in canonical commit `9f07e00`. Dynamic mood-state nodes that are structurally isolated from ordinary `goto` links are expected engine entry points rather than automatically broken content.


## Appendix C — Primary and authoritative science references used in v0.2

### Space plant growth, Veggie, and gravity

- NASA, “Plant Biology Program”: https://science.nasa.gov/biological-physical/focus-areas/plant-biology/focus-areas/
- NASA, “Station Science 101: Plant Research”: https://www.nasa.gov/missions/station/ways-the-international-space-station-helps-us-study-plant-growth-in-space/
- NASA, “Veggie Plant Growth System Activated on International Space Station”: https://www.nasa.gov/missions/station/veggie-plant-growth-system-activated-on-international-space-station/
- NASA NTRS, “Veggie ISS Validation Test Results and Produce Consumption”: https://ntrs.nasa.gov/citations/20150021302
- NASA, “Cosmonauts Complete Russian Spacewalk” (first official station-grown crop tasting): https://www.nasa.gov/blogs/spacestation/2015/08/10/cosmonauts-complete-russian-spacewalk/

### Pollination

- NASA NTRS, “Insect Flight Observation at Zero Gravity” (1982): https://ntrs.nasa.gov/citations/19830025642
- NASA Spaceflight Q&A, honeybee/honeycomb experiment (1984): https://robotics.nasa.gov/spaceflight-qa/
- Vallejo-Marín et al., “Biomechanical properties of a buzz-pollinated flower”: https://pubmed.ncbi.nlm.nih.gov/33047057/
- “Buzz pollination: investigations of pollen expulsion…”: https://pubmed.ncbi.nlm.nih.gov/39837481/

### Light, pigments, and chlorophyll

- NASA/JPL, “Duluth After Dust Storm”: https://www.jpl.nasa.gov/images/pia22330-duluth-after-dust-storm/
- Vedalankar & Tripathy, “Light dependent protochlorophyllide oxidoreductase”: https://pubmed.ncbi.nlm.nih.gov/38846463/
- Terashima et al., “Green light drives leaf photosynthesis…”: https://pubmed.ncbi.nlm.nih.gov/19246458/
- Alberte et al., chlorophyll a/c and fucoxanthin complexes: https://pubmed.ncbi.nlm.nih.gov/7016188/
- Akimoto et al., energy transfer in fucoxanthin–chlorophyll a/c complexes: https://pubmed.ncbi.nlm.nih.gov/24530875/

### Continuous illumination and Spirulina/Limnospira

- “Dynamics of long-term continuous culture of Limnospira indica…”: https://pubmed.ncbi.nlm.nih.gov/34342154/
- Velez-Ramirez et al., “Plants under continuous light”: https://pubmed.ncbi.nlm.nih.gov/21396878/

### Radiation

- NASA NTRS, “Impact of Space Radiation on Plant Seeds”: https://ntrs.nasa.gov/citations/20210000732
- NASA Science, “Weather on the Moon”: https://science.nasa.gov/moon/weather-on-the-moon/
- NASA Science, “Solar Wind on the Moon”: https://science.nasa.gov/moon/solar-wind/
- Dadachova et al., “Ionizing radiation changes the electronic properties of melanin…”: https://pubmed.ncbi.nlm.nih.gov/17520016/
- Pacelli et al., melanin and fungal radioprotection: https://pubmed.ncbi.nlm.nih.gov/28127878/

### Mycorrhizae and fungal networks

- Figueiredo et al., review of common mycorrhizal networks: https://pubmed.ncbi.nlm.nih.gov/37744156/
- Karst et al., “Positive citation bias and overinterpreted results…”: https://www.nature.com/articles/s41559-023-01986-1
- Henriksson et al., “Re-examining the evidence for the mother tree hypothesis”: https://pubmed.ncbi.nlm.nih.gov/37149889/
- Hawkins et al., “Mycorrhizal mycelium as a global carbon pool”: https://doi.org/10.1016/j.cub.2023.02.027
- Inamdar et al., “Fungal Volatile Organic Compounds”: https://pubmed.ncbi.nlm.nih.gov/32905756/

### Standards

- NGSS MS-LS1-6: https://www.nextgenscience.org/pe/ms-ls1-6-molecules-organisms-structures-and-processes
- NGSS MS-LS2: https://www.nextgenscience.org/dci-arrangement/ms-ls2-ecosystems-interactions-energy-and-dynamics
- NGSS MS-ETS1: https://www.nextgenscience.org/msets1-engineering-design

