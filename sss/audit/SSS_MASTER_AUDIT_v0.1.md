# Space Sprout Sleuth — Master Content and Curriculum Audit

**Version:** 0.1 — repository architecture, content inventory, static integrity, and preliminary instructional analysis  
**Authoritative game snapshot:** uploaded `sss.zip`, top-level runtime files, corresponding to the repository `main` branch supplied by the project owner  
**Audit date:** 2026-07-22  
**Status:** First substantial audit pass. This document establishes what is present, how it functions, what can support curriculum, and which issues require deeper scientific or instructional review. It is not yet the final lesson-plan package.

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
5. **There are three confirmed broken dialogue links in the final Campaign 2 case.** These can create runtime failures after students unlock specific evidence.
6. **The tutorial contradicts the implemented diagnosis rule.** It tells players they may diagnose early, while the runtime refuses to open diagnosis until every clue has been collected.
7. **The intended 20-minute gameplay target is plausible for direct evidence routes, but not for completionist play.** Full dialogue trees are large, and the scoring system rewards exhaustive exploration.
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

**Confirmed runtime defects:** Three visible dialogue options point to node IDs that do not exist:

- `vorn_shael.active_transport` → `mycorrhizal_confirm` (`campaign_2_data.js` around line 3270)
- `ilreth_mar.start` → `regulation_direct` (around line 3472)
- `ilreth_mar.start` → `exemption_question` (around line 3473)

These options are evidence-gated, so they may not appear during a superficial test. Once the requirements are met, clicking them can attempt to render an undefined node. This should be fixed before classroom deployment or worksheet checkpoints might direct students into a broken path.

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

# 8. Confirmed implementation and content issues

## Critical — fix before classroom use

### 8.1 Broken dialogue targets in Campaign 2 Case 6

Three gated options reference missing nodes, as detailed in the case dossier above. These can break a student’s investigation after they have done the correct evidence work.

## High instructional priority

### 8.2 Tutorial contradicts diagnosis gating

The help screen says players may press Diagnose early and that guessing without all clues still works (`index.html` around line 2082). The actual click handler refuses diagnosis until all formal clues are found and displays “Need more evidence!” (`index.html` around lines 6281–6301).

This matters educationally because teachers and worksheets need to know whether diagnosis is an open claim students may revise or a locked final step. The current implementation makes it a locked step. Either the help text or the code should change.

### 8.3 Case numbering disagreement

The bonus-content design says the second first-contact case should be displayed as “Case 6b.” The runtime function returns sequential integers, displaying it as Case 7. This affects worksheet filenames, teacher directions, and campaign pacing.

### 8.4 Campaign 2 name disagreement

- Runtime title: **Space Sprout Sleuth: Distant Soils**
- Data object: **Federation Field Cases**
- Victory wording: **Federation Mission Complete**

This is not a gameplay bug, but the curriculum needs one official campaign title with alternatives recorded as subtitles if desired.

## Medium priority

### 8.5 Europa crew mood property typo

Campaign 1 Europa uses `moodStart` where the engine reads `startMood`. The default is also zero, so it currently has no visible effect, but it is a schema inconsistency that could matter if the intended start mood changes.

### 8.6 Help text is Campaign-1-specific

The help screen describes four sources, while Campaign 2 uses five and its final case uses a different source structure. Campaign 2 teacher quick-start materials must describe the changed evidence model even if the game help remains unchanged.

### 8.7 Full-completion scoring conflicts with classroom efficiency

The “thoroughness” score awards points only when all nodes in a source have been visited. That is incompatible with a 20-minute targeted play window and may encourage students to click every option rather than reason efficiently.

---

# 9. Preliminary serious-science triage

This is a screening pass, not the final source-by-source science review.

| Case | Status | Audit judgment |
|---|---|---|
| C1-1 Gravitropism | Mostly sound | Clarify microgravity/free fall and the role of plant pillows versus light orientation. |
| C1-2 Pollination | Sound | Appropriate generalization for tomatoes; species-specific caveat needed. |
| C1-3 Mars light pipes | Major review | Biochemistry is plausible, but the claimed red-selective transmission loss from borosilicate/Mars dust needs evidence or revision. |
| C1-4 Spirulina continuous light | Major correction | Continuous illumination is not inherently lethal or universally incompatible with Arthrospira culture. Reframe around intensity/reactor-specific photoinhibition. |
| C1-5 Europa radiation | Plausible extrapolation | External hazard is sound; exact dose/shielding scenario needs labeling as modeled fiction. |
| C1-6/7 network signaling | Fiction with contested analogy | VOC signaling is plausible fiction; “mother tree/wood wide web” claims require qualification. |
| C2-1 artificial gravity | Plausible extrapolation | Physics is real; alien biological sensitivity is fictional. |
| C2-2 buzz trigger | Sound analogy + fiction | Earth vibration pollination is real; alien frequency dependence is fictional. |
| C2-3 pigment spectrum | Mostly sound analogy | Avoid absolute claims that red light is wholly unusable. |
| C2-4 circadian VOC network | Fiction | Internally consistent, but must not rely on the inaccurate universal dark-period claim from C1-4. |
| C2-5 radiation dependence | Major qualification | Radiation-enhanced fungal growth has evidence; obligate dependence and settled “radiosynthesis” claims do not. |
| C2-6 mycorrhizal restoration | Major qualification | Symbiosis is real; broad cooperative resource-sharing/mother-tree claims are disputed. |

### Primary-source anchors used in this screening

- NASA, **Growing Plants in Space**, on Veggie plant pillows and light orientation.
- Heyes & Hunter (2005), **Making light work of enzyme catalysis: protochlorophyllide oxidoreductase**, DOI: 10.1016/j.tibs.2005.09.001.
- Gabruk & Mysliwa-Kurdziel and related POR literature on the light-dependent chlorophyllide step.
- Lehto et al. / MELiSSA continuous-culture work on *Limnospira/Arthrospira* photobioreactors; continuous illumination can be used, with photoinhibition depending on irradiance and culture conditions.
- NASA/JPL Europa Clipper materials on Europa’s intense radiation environment.
- Dadachova et al. (2007), **Ionizing radiation changes the electronic properties of melanin and enhances the growth of melanized fungi**, DOI: 10.1371/journal.pone.0000457.
- Henriksson et al. (2023), **Re-examining the evidence for the mother tree hypothesis**, DOI: 10.1111/nph.18935.
- Karst et al. (2023), **Positive citation bias and overinterpreted results lead to misinformation on common mycorrhizal networks in forests**, DOI: 10.1038/s41559-023-02035-7.

---

# 10. Preliminary NGSS strategy

The game aligns most strongly to **Science and Engineering Practices**, particularly:

- analyzing and interpreting information/data;
- constructing explanations;
- engaging in argument from evidence;
- defining problems;
- evaluating design solutions;
- developing systems models.

Likely middle-school performance expectations to use selectively—not to claim wholesale for every case—include:

- **MS-LS1-6:** construct an explanation based on evidence for the role of photosynthesis in matter and energy flow;
- **MS-LS2-3:** develop a model of matter cycling and energy flow among living and nonliving ecosystem parts;
- **MS-LS2-4:** construct an evidence-supported argument that changes to physical or biological ecosystem components affect populations;
- **MS-LS2-5:** evaluate competing solutions for maintaining biodiversity and ecosystem services;
- **MS-ETS1-1:** define criteria and constraints for a design problem;
- **MS-ETS1-2:** evaluate competing design solutions systematically;
- **MS-ETS1-3:** analyze test data to compare solutions.

The curriculum should not claim that merely playing a case fully satisfies a performance expectation. Each lesson must include the actual student product required by the standard: model, explanation, argument, data analysis, or solution evaluation.

A particularly important NGSS boundary: MS-LS1-6 emphasizes photosynthesis but does not require middle-school students to master detailed biochemical reaction pathways. The Mars lesson should therefore use the POR pathway as enrichment/context rather than the central assessed fact.

---

# 11. Recommended 60-minute lesson frame

This remains provisional until the detailed dialogue audit is complete.

| Time | Activity |
|---:|---|
| 0–5 min | Phenomenon/mission launch and one prediction |
| 5–8 min | Controls and evidence-log directions |
| 8–28 min | Gameplay and embedded evidence recording |
| 28–38 min | Case-specific evidence-processing task |
| 38–48 min | CER response |
| 48–55 min | Brief teacher debrief or source/video/reading snippet |
| 55–60 min | Individual exit ticket |

The supplemental reading or video should not automatically be required in every lesson. Most cases already contain enough content; external media should be used only where it corrects, visualizes, or contextualizes a concept that the game cannot efficiently show.

---

# 12. Recommended campaign culminations

## Campaign 1 culmination

Use **The Gift** as an applied missing-variable case rather than adding a separate multi-day project. Students complete a one-period “Xenobotanist Certification” sheet that asks them to:

1. identify which variables the lab successfully reproduced;
2. identify the missing biological signal;
3. select and defend one solution;
4. compare this case to one earlier environmental-cue case;
5. complete a concise CER.

## Campaign 2 culmination

Use **The First Garden** as an evidence-and-policy synthesis. Each student independently writes a short recommendation separating:

- scientific diagnosis;
- proposed ecological repair;
- regulatory route;
- risks and constraints;
- evidence from at least three source types.

## Final SSS synthesis

After both campaigns, students diagnose two or three short unseen scenarios. Each scenario should deliberately combine or invert earlier ideas. This can function as the post-assessment and final SSS certification within one class period.

---

# 13. What the next audit pass must do

The next pass remains inside the **SSS audit phase** and should be conducted at **High thinking**. It must:

1. Read every dialogue tree node case by case.
2. Map required versus optional paths.
3. Identify every cross-source dependency.
4. Record distractors and misconception dialogue.
5. Estimate realistic play time rather than raw content size.
6. Identify evidence that is easy to miss or confusingly worded.
7. Validate all formal clues against the actual node text that reveals them.
8. Complete the serious-science verification with primary sources.
9. Produce a final NGSS candidate map without overstating alignment.
10. Recommend only high-value code changes that materially improve classroom use.

After those tasks, the audit can be considered complete and the project can move to the Curriculum Blueprint. Before that phase transition, the recommended thinking level should be reviewed with the owner as requested.

---

## Appendix A — Static graph validation results

All case data parsed successfully as JavaScript. Every case has exactly one correct diagnosis and every formal clue is revealed by at least one node.

Dynamic “annoyed” and “locked” nodes are not ordinary dialogue targets; the engine enters them based on mood/source state, so their structural isolation is expected.

The only confirmed missing `goto` targets are the three in Campaign 2 Case 6 described above.

## Appendix B — Source-content totals by case

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

