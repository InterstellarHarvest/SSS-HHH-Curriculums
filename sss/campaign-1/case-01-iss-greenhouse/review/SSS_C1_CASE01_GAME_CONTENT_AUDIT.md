# SSS Campaign 1, Case 01 — Game-Content Audit

**Audited curriculum artifact:** `sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`
**Consulted prior version:** `…/SSS_C1_CASE01_EDITABLE_MASTER_v0.3.html`
**Game repository:** `Space Sprout Sleuth` (GitHub org `InterstellarHarvest`)
**Audit type:** Investigation was read-only; the game, config, assets, and tests were not modified. After the crosswalk, at reviewer request, four confirmed corrections were applied to the curriculum packet (`…MASTER_v1.0.html`) — see the "Applied to v1.0" entries in §13/§14. No other files were changed; the report itself is the only additional file produced.
**Audit date:** 2026-07-23 (URL/OSDR verification and packet corrections same day)
**Auditor:** Automated repository crosswalk; external URL and OSDR-API verification performed (see §12.2 and §18)

---

## 1. Executive Summary

Campaign 1, Case 01 of the curriculum packet is **strongly compatible** with the current playable game. The packet's central mission question, four-source evidence structure, four diagnosis options, correct diagnosis, statolith/gravitropism mechanism, and proposed engineering interventions all map cleanly onto the game data at the packet's recorded baseline — and that baseline commit (`2a6e8a7`) **is the current game HEAD**, so the packet was written against the live runtime.

No **Critical** discrepancies were found: the packet teaches the diagnosis the game encodes as `isCorrect: true`, it does not describe nonexistent gameplay, and its task sequence follows the game's actual investigate → diagnose flow (which the engine hard-gates behind collecting all four clues).

The findings were minor-to-moderate and mostly editorial or verification-scoped, and the four correction-type items have already been **applied to the packet** in this pass (no lesson content changed):

- **Two reviewer-confirmed classroom-clarity edits** — ✅ applied: (a) the Teacher table's **"Water problem"** is now labeled an additional *discussion* distractor, not one of the four selectable in-game diagnoses (DISC-01); (b) a teacher note now states the **engineering response (Task 8) is worksheet-only** — Campaign 1 has no in-game "apply the fix" screen (DISC-06).
- **One citation fix** — ✅ applied: source #5 was mis-attributed to "Nakamura et al. (2020)"; the paper (PMID 31963631, correct title and year) is by **Ditengou, Teale & Palme**, now corrected (DISC-08).
- **One cosmetic label fix** — ✅ applied: source #2 "(SpaceX-13)" → "(Space-13)" to match NASA's page (DISC-09; the "· Hardware" label on source #4 was kept by design). OSD-38 was confirmed via the OSDR metadata API — all eight printed links are verified.
- Optional polish left for the author: pre-game vocabulary reveal of the mechanism (DISC-02, playtest judgment); add "amyloplast" to the statolith definition (DISC-03); name the player "Dr. Nova" (DISC-04).

**Standards/science-source status (updated):** the earlier "external verification" gate for standards and science claims is **closed** — the Master Audit v1.0 verified the science claims against authoritative sources and set Case 01's MS-ETS1-1/2 *supporting* framing (gravitropism is not a standalone middle-school PE), and the Blueprint v1.0 adopted that as approved architecture (§12.1). The only external item was URL resolution/title matching, which this audit **completed**: all eight printed URLs resolve (§12.2).

The packet is self-labeled **"VALIDATION BUILD"** and its own migration/blocker docs state that *"game compatibility baseline `2a6e8a7` was preserved but not re-tested against game source."* This audit closes that gap on the content side and finds the baseline still valid.

**Final verdict: Compatible with minor curriculum corrections.** (See §Final Verdict.)

---

## 2. Repositories, Branches, and Commits Reviewed

| Repository | Branch | HEAD (short) | State | Role |
|---|---|---|---|---|
| `Space Sprout Sleuth` | `main` | `2a6e8a7` | Clean working tree; up to date with `origin/main` | **Game — runtime source of truth** |
| `SSS-HHH-Curriculums` | `main` | `8d6d31d` | Curriculum repo | Contains the audited packet |

Game HEAD full SHA: `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`
Immediately prior game commit: `9f07e00` ("Fix C2 Case 6 dialogue targets…"); `2a6e8a7` = "Calibrate science/history text per curriculum audit correction spec v0.1".

**Notable:** the audited packet file (`…MASTER_v1.0.html`) is **untracked** in the curriculum repo (not yet committed). The packet's own metadata records `sss-game-baseline = 2a6e8a7`, which equals the current game HEAD. The science-text correction spec at `sss/audit/data/corrections/SSS_SCIENCE_TEXT_CORRECTION_SPEC_v0.1.md` names game baseline `9f07e00`; the game commit `2a6e8a7` is the application of that spec, so the corrected text is live.

---

## 3. Runtime Source-of-Truth Determination

The game runs from a single-file HTML engine that loads two plain-JS data files:

- `index.html` → `<script src="space_sprout_sleuth_data.js">` (Campaign 1) then `<script src="campaign_2_data.js">` (Campaign 2) — `index.html:2686-2687`.

Campaign 1, Case 01 is the **first** case object in `space_sprout_sleuth_data.js`:

- `GAME_DATA.cases[0]`, `id: "iss"`, `name: "ISS Greenhouse Module"` — `space_sprout_sleuth_data.js:66-68`. The object spans lines **66–440** (next case `"lunar"` begins at line 443).

**Non-runtime / legacy files that must NOT be used as source of truth** (they differ from the loaded files and are not referenced by the root `index.html`):

- `resources/campaign_2/space_sprout_sleuth_data.js` — a divergent copy (`diff` = differs).
- `resources/space_sprout_sleuth_data_backup.js` — backup (differs).
- `resources/index_backup.html`, `resources/campaign_2/index.html` — legacy engines.

All findings below cite `space_sprout_sleuth_data.js` (root) and `index.html` (root) at HEAD `2a6e8a7`.

**Dynamic content:** Case 01 content is fully static (no procedural generation). Case scoring, clue-gating, and rank are computed at runtime in `index.html` but from fixed data; nothing in Case 01 is generated in a way that cannot be verified from the two text files.

---

## 4. Overall Compatibility Verdict

**Compatible with minor curriculum corrections.** The packet and game agree on case identity, mission question, symptoms, nominal conditions, the four evidence sources, the four diagnosis options, the correct diagnosis, the statolith mechanism, and the intervention menu. The recorded baseline matches the live runtime. The standards/science architecture is settled upstream (Master Audit v1.0 + Blueprint v1.0, §12.1), and the external URL/title check is **complete** — all eight printed links resolve and OSD-38 is confirmed (§12.2). The four resulting corrections have been applied to the packet (§13/§14); no external verification remains open.

---

## 5. Task 1–9 Gameplay Mapping

Engine flow (verified in `index.html`): the player investigates four action stations (`crew`, `sensors`, `plants`, `logs`), each revealing one required clue; the **Diagnose button is hard-gated** — clicking it before all clues are found triggers a "Need more evidence!" message and screen shake (`index.html:6281-6306`), and only opens the diagnosis screen when `cluesFound.length >= clues.length` (`index.html:3879-3880`, `4247`). After a correct diagnosis the game shows the `explanation` and `rankUpText`. **Campaign 1 has no in-game "choose a solution/intervention" step** (there is no `solutions:` array in `cases[0]`; the solution-selection UI at `index.html:4388` is a Campaign 2 feature).

| Task | Student asked to… | Corresponding game experience | Intended timing | Info available then? | Notes / flags |
|---|---|---|---|---|---|
| **1 · Vocabulary (REFERENCE)** | Read terms: gravitropism, microgravity, statocyte, statolith, phototropism | Terms surface in-game via `logs.gravitropism_entry` and `sensors.gravitropism_query` (`data.js:240-241, 511-515`) | **Before** play | N/A (reference) | Pre-teaches the mechanism/answer vocabulary → see §6/§13 reveal flag. Match, but sequencing judgment. |
| **2 · Initial thinking (PREDICTION)** | Predict what evidence distinguishes a resource vs. orientation problem | No game step; primes investigation. Teacher: "do not confirm the diagnosis" | **Before** play | N/A | Correct pre-game framing. **No issue.** |
| **3 · Investigate four sources (EVIDENCE TASK)** | Record observations from Crew / Sensors / Plants / Logs; tag O vs I | Player visits the four stations; each reveals one clue (`data.js:352-405`) | **During** play | Yes — all four sources live from case start | Exact 1:1 with the game's four clues. **No issue.** |
| **4 · Test competing explanations (CAUSE TEST)** | Mark support/reject + one reason for four explanations | The four map to the game's four diagnosis options (`data.js:407-431`) | **During / checkpoint** | Yes, once clues found | Student list matches game options exactly; Teacher table adds "Water problem" (see §6/§13). |
| **5 · Build the mechanism (MECHANISM MODEL)** | Fill statolith settle/no-settle → root direction cards | Game states the mechanism in `logs.gravitropism_entry` (`data.js:241`) and clue `GRAVITROPISM_MISSING.learned` (`data.js:403`) | **During / after** | Yes (from logs clue) | Packet omits auxin (game includes it) — appropriately optional. **No issue.** |
| **6 · Diagnose + reject alternative (DIAGNOSIS)** | State cause in own words; reject the tempting alternative | Player selects 1 of 4 on the gated Diagnose screen (`index.html:4247-4276`) | **After** play (post-unlock) | Yes | Directly encoded. **No issue.** |
| **7 · CER (EXPLANATION)** | Claim / Evidence / Reasoning | Post-diagnosis the game shows the `explanation` narrative (`data.js:435-439`) | **After** play | Yes | Model CER cites the exact four in-game sources. **No issue.** |
| **8 · Supply an orientation cue (ENGINEERING RESPONSE)** | Choose/design root channels, moisture gradient, shoot light + root guide, or rotating chamber; give one criterion + one constraint | Interventions are **discussed** in `logs.solutions_search` (`data.js:259`) and `sensors.gravity_simulation` (`data.js:498`), but **not selectable in Campaign 1** | **After** play (paper design) | Yes (from logs) | Packet correctly treats this as a worksheet design task, not an in-game action. See §9. **No issue**, but teachers should know there is no in-game "fix" step. |
| **9 · Exit ticket (TRANSFER CHECK)** | Predict which symptom (roots vs pale leaves) improves first with root channels; optional extension comparing a root guide vs rotating chamber | Transfer/extension beyond scripted content; consistent with game's "not available on ISS" framing of centrifuges (`data.js:498, 259`) | **After** play | Yes | **No issue.** |

**Sequencing verdict:** the worksheet order (predict → investigate → eliminate → mechanism → diagnose → CER → engineer → transfer) matches the game's enforced investigate-then-diagnose gate. No task requires information the game withholds at that point. The only sequencing concern is the pre-game vocabulary reveal (Task 1) — see §13, DISC-02.

---

## 6. Evidence and Clue Crosswalk

The game defines exactly four required clues (`space_sprout_sleuth_data.js:352-405`); all four must be collected before diagnosis unlocks. The packet's four-source evidence structure is a 1:1 match.

| Packet source | Packet wording (paraphrase) | Game clue tag & source | Game wording (paraphrase / cite) | How encountered | Status | Fidelity |
|---|---|---|---|---|---|---|
| **Crew** | "Roots do not grow down; changing resources did not help" | `ROOTS_DIRECTIONLESS` via `crew` (Astronaut Kim) | "The lettuce just doesn't seem to know which way is down… roots always find their way into the soil. Up here? They go every which way." `learned: "Roots are not orienting downward."` (`data.js:362-364`) | Talk to Kim | **Required** | Accurate |
| **Sensors** | "Microgravity is the major unusual condition; nutrients, water, temperature, humidity, lighting nominal" | `ZERO_GRAVITY` via `sensors` (ISS-GH Sensor Array) | "…⚠️ Environment: microgravity — the normal downward orientation cue is greatly reduced." `learned: "The module is in microgravity — zero g."` (`data.js:375-377`) | Query terminal | **Required** | Accurate (corrected-spec wording) |
| **Plants** | "Dense tangles, poor anchoring, unusual stem angles" | `ROOT_TANGLE` via `plants` (Lettuce Specimen Tray) | "The roots have formed dense, tangled mats around the seed pillow… stems are growing at odd angles…" (`data.js:388-390`) | Examine plants | **Required** | Accurate |
| **Mission logs** | "Gravitropism/statolith mechanism and possible replacement cues" | `GRAVITROPISM_MISSING` via `logs` (Mission Log Archive) | "…Without gravity vector, roots default to random growth. Recommend installing directional light guides or physical root channels…" `learned:` statoliths do not settle normally → roots lose a reliable 'down' cue (`data.js:401-403`) | Review logs | **Required** | Accurate |

**Deeper (optional / decorative) game evidence the packet does not use — correctly, as these are not required clues:**

- **CO₂ 410 ppm, O₂ 21%, pressure 101.3 kPa** — nominal, `sensors.env_readings` (`data.js:475` region). Decorative/eliminative.
- **Airflow** "fan-driven (no convection)" and **radiation** "elevated (shielded)" — `sensors.env_factors` (`data.js:519`). Decorative/eliminative.
- **Nutrient panel** (N 150 / P 50 / K 200 / Ca 180 / Mg 50 / pH 6.0) — nominal, `sensors.nutrients`.
- **Light** LED full-spectrum, 16h/8h, PAR 250 µmol/m²/s, R660/B450 — nominal, `sensors.light`.
- **Growing medium** arcillite "plant pillow" with wicking — `plants.medium`.
- **Cross-expedition crew pattern** (Chen/Patel/Santos/Kim) rejecting the defective-seed hypothesis — `logs.crew_observations`, `logs.crew_pattern`.
- **Statolith deep mechanism** (auxin, differential elongation) — `logs.gravitropism_entry` (`data.js:241`).

**Reveal-timing check:** the packet does not reveal any required clue's content ahead of the game *within the evidence tasks* — the Student/Accessible evidence tables ship blank. However, Task 1 vocabulary pre-defines the *mechanism terms* (gravitropism, statolith) — see §13 DISC-02.

**Omission check for the intended conclusion:** the four packet sources are exactly the four the game requires for diagnosis. No evidence needed for the intended conclusion is omitted. **No issue.**

---

## 7. Competing Explanations Crosswalk

Game diagnosis options (`space_sprout_sleuth_data.js:407-431`):

| Game option `id` | Game label (paraphrase) | `isCorrect` | Game hint on wrong pick |
|---|---|---|---|
| `gravity` | Microgravity disrupts gravitropism; roots can't sense "down"; need physical guides/directional light | **true** | — |
| `nutrients` | Nutrient solution too concentrated, burning roots | false | "Sensor data shows nutrients are nominal…" |
| `light` | Light cycle wrong for lettuce | false | "16/8 is a standard photoperiod…" |
| `seeds` | Seed stock has a genetic defect | false | "This same seed variety grows perfectly on Earth…" |

| Explanation | Student edition | Answer Key | Teacher distractor table | Game | Assessment |
|---|---|---|---|---|---|
| Nutrient damage | "Nutrient solution is damaging roots" | "weakened: readings nominal" | "Nutrient burn — nominal solution; directional tangling a poor match" | `nutrients` (false) + nominal sensor data | **Match** |
| Wrong light cycle | "The light cycle is wrong" | "weakened: schedule/intensity nominal" | "Wrong light cycle — 16/8 & PAR nominal" | `light` (false) + nominal light node | **Match** |
| Defective seeds | "The seed stock is defective" | "weakened: repeated environment-linked pattern" | "Defective seeds — pattern repeats with environment & prior plantings" | `seeds` (false) + cross-expedition pattern (`logs.crew_pattern`) | **Match** |
| Microgravity (correct) | "Microgravity disrupts orientation" | "supported: matches all four sources & mechanism" | (not listed — it is the answer) | `gravity` (true) | **Match** |
| **Water problem** | — | — | **"Water problem — delivery works; uniform wicking may reduce a cue but does not best explain the case"** | **Not a selectable diagnosis;** in-game dialogue discusses uniform wicking reducing a moisture cue (`plants.moisture_confirmed`, `data.js:159-161`) | **Extra (Teacher-only).** See DISC-01 |

**Findings:**
- The four student/answer-key competing explanations are a verbatim conceptual match to the game's four diagnosis options — no invented hypothesis, none omitted, distractors scientifically consistent with the in-game hints. **No issue.**
- The Teacher table substitutes **"Water problem"** for microgravity (reasonable, since microgravity is the answer) — but "Water problem" is **not** an in-game diagnosis option. It is scientifically defensible (the game's own `plants.moisture_confirmed` notes uniform wicking removes a moisture gradient), so it functions as a legitimate teaching distractor, not a contradiction. Flagged **Minor** only because a teacher could imply it is selectable in the game. See DISC-01.
- No wording makes the correct answer "obviously correct too early" *within the competing-explanations task itself*; the earliness concern lives in Task 1 vocabulary (DISC-02).

---

## 8. Diagnosis and Answer-Key Review

**Game-established diagnosis (independent of the packet):** `cases[0].diagnoses[0]` is flagged `isCorrect: true` and reads: *"Microgravity is disrupting gravitropism — roots can't sense 'down' without gravity and need physical guides or directional light to orient properly."* The game `explanation` (`data.js:435-439`) reinforces this with the statocyte/statolith mechanism and the Veggie plant-pillow solution. This is **directly encoded by game logic**, not merely narrative.

| Packet element | Content (paraphrase) | Game support | Classification |
|---|---|---|---|
| Answer-Key model diagnosis | "Microgravity disrupted normal gravitropic orientation; without a stable settling direction for statoliths, roots lacked a reliable 'down' cue and formed tangled growth around the plant pillows" | Matches `diagnoses[0]` + `explanation` + `logs.gravitropism_entry` | **Directly encoded** |
| Model CER — Claim | "Problem caused by disrupted gravitropism in microgravity" | Same | **Directly encoded** |
| Model CER — Evidence (Kim / sensors microgravity / plant tangles / logs statolith) | Cites all four game sources by function | Each maps to a required clue (§6) | **Directly encoded** |
| Model CER — Reasoning (statoliths don't settle → unreliable signal; beats nutrient/light/seed) | Mirrors game hints on wrong options | `diagnoses[1-3].hint`; `logs.gravitropism_entry` | **Strongly implied → encoded** |
| Rejected alternative (nutrient burn) | "tempting because stunted/pale, but sensors nominal" | `diagnoses[1].hint` + `sensors.nutrients_confirmed` | **Directly encoded** |
| Accepted variants ("apparent weightlessness," "reduced reliable gravity cue"; auxin optional; rotating chamber/moisture gradient acceptable) | Reasonable scoring latitude | Consistent with `sensors.gravity_simulation`, `logs.solutions_search` | **One plausible interpretation, supported** |
| Exit-ticket answer (root channels help tangled roots first; pale leaves later) | Transfer inference | Consistent with mechanism; not scripted verbatim | **Strongly implied** |
| Misconception list (ISS still under gravity/free fall; roots use more than gravity; light is a shoot cue; plants can grow in space; pillows don't recreate gravity) | Five misconceptions | All consistent with game text (`sensors.gravity` free-fall wording; `logs.root_morph` hydro/thigmotropism; `stem_analysis`; `plants.medium`) | **Directly supported** |

**Answer-key accuracy verdict:** the packet's answer is **directly encoded by game logic** and its supporting evidence, reasoning, and misconception handling are consistent with — and in places more scientifically careful than — the game text (e.g., the packet's boundary note "do not teach roots are completely random" tempers the game's casual "random growth" phrasing; the game itself softens to "semi-random" at `logs.root_orientation`). **No issue.**

---

## 9. Engineering Intervention Review

**Game-side interventions** are presented only as *discussion* (Campaign 1 has no solution-selection step). Sources:

- `logs.solutions_search` (`data.js:259`): (1) **Physical guides** — rigid channels/mesh; root tips show thigmotropism; (2) **Directional light** — strong phototropic cue for stems, "Does not help root orientation"; (3) **Moisture gradients** — trigger hydrotropism, "Less reliable than gravitropism"; (4) **Centrifugal systems** — artificial gravity, "Not currently available on ISS."
- `logs.guide_notes` (`data.js:267`): NASA Ames prototype biodegradable-mesh "root channel" systems.
- `sensors.gravity_simulation` (`data.js:498`): "ISS Greenhouse Module is not equipped with centrifugal systems" → light/physical/moisture alternatives.

| Packet intervention (Task 8 / Answer Key) | Game counterpart | Tradeoff match? | Verdict |
|---|---|---|---|
| Root channels / mesh (Answer-Key model design) | `logs.solutions_search` #1 + `guide_notes` (NASA Ames mesh) | Yes — packet criterion "roots extend into medium not around surface," constraint "lightweight, permit water/oxygen flow"; game frames as most practical root fix | **Supported / encoded** |
| Directional light supports shoots, weaker for roots | `logs.solutions_search` #2 ("Does not help root orientation") | Yes — exact tradeoff | **Supported / encoded** |
| Moisture gradient | `logs.solutions_search` #3 | Yes — game notes "less reliable" | **Supported / encoded** |
| Rotating chamber (extension: "more closely replaces gravity" but harder on ISS) | `logs.solutions_search` #4 + `sensors.gravity_simulation` ("not equipped") | Yes — game says best substitute but unavailable on ISS | **Supported / encoded** |

**Findings:**
- Every proposed intervention is present in game dialogue with the same tradeoffs. **No issue.**
- The packet does **not** claim any intervention "succeeds"; it frames Task 8 as a paper design with criterion + constraint, matching the game's "these may *partially* substitute" hedging (`sensors.gravity_simulation`). **No issue.**
- **Fiction vs. real science** is handled: the packet's "Science status" panel labels root channels/moisture/rotating systems as *plausible engineering* and the emergency/crew/SAA as *fictional context*; the game's NASA Ames reference is real-adjacent. **No issue.**
- **Advisory (not a defect):** because Campaign 1 has no in-game solution picker, students never "select" a fix inside the game — Task 8 is entirely worksheet-side. The packet frames it correctly, but teachers expecting an in-game engineering step should be told there isn't one. Suitable for the "Items Requiring Human Playtesting" list.

---

## 10. Terminology and Lore Review

| Term (packet) | Game canonical | Cite | Verdict |
|---|---|---|---|
| **SAA = Solar Agricultural Authority** | Identical | `resources/SPACE_SPROUT_SLEUTH_SPEC_v2.md:52`; insignia `shared/assets/insignia/saa.svg`; in-dialogue "Thank goodness SAA sent someone" (`data.js:74`) | **Match — no SAA/TAA confusion** |
| Kim (crew, named only in Answer Key) | "Astronaut Kim" | `data.js:72` (`speaker: "Astronaut Kim"`) | **Match** |
| ISS Greenhouse Module / Low Earth Orbit / ISS | Identical | `data.js:67-69` | **Match** |
| Plant pillows | "plant pillow… arcillite (baked clay) with wicking" | `data.js:152` | **Match** |
| Veggie Plant Growth System | "Veggie growth chamber / Veggie hardware installed 2014" | briefing `data.js:70`; `logs.veggie_history` | **Match** |
| "Diagnose screen unlocks after clues collected" | Engine gate | `index.html:6281-6306`, `3879-3880` | **Match** |
| Ranks / score / speed | Ranks Trainee→Xenobotanist; +25 all-clues score | `data.js:54`; `index.html:3766-3769` | **Match** |
| Player identity | Packet keeps player generic; game names player **"Dr. Nova"** (interplanetary agronomist) | `SPEC_v2.md:52`; `index.html:3203` | **Minor** — packet could reference Dr. Nova but does not; not a conflict |

- **No HHH (Hunger, Harvest, History) material** appears in the SSS packet. **No issue.**
- **No TAA** (the Campaign-2 alien authority) appears — correct for Campaign 1. **No issue.**
- No obsolete character/location names, no earlier-build-only terms detected. **No issue.**
- **Lore boundary:** the packet does not over-claim beyond the game — SAA/crew/emergency are explicitly labeled fictional; real NASA facts (Veggie, Ames root channels) match the game. **No issue.**

---

## 11. Science-Claim Inventory

| # | Claim (packet) | Classification | Basis |
|---|---|---|---|
| S1 | Gravitropism = directional growth in response to gravity | **Directly supported by game** | `logs.gravitropism_entry` (`data.js:241`) |
| S2 | On Earth statoliths settle → consistent signal → roots grow downward | **Directly supported** | `data.js:241`, `explanation` (`data.js:437`) |
| S3 | In microgravity statoliths don't settle → unreliable direction cue → tangled roots | **Directly supported** | `data.js:241, 511-515`; clue `learned` (`data.js:403`) |
| S4 | Statocyte = gravity-sensing cell; statolith = dense starch-filled structure | **Directly supported** (packet omits game's term "amyloplast") | `data.js:241` ("statoliths (starch-filled amyloplasts)") — see DISC-03 |
| S5 | Microgravity ≠ absence of gravity; ISS in continuous free fall (apparent weightlessness) | **Directly supported** (corrected-spec text) | `sensors.gravity` (`data.js:~471`); correction spec §1.1 |
| S6 | Roots also respond to moisture, touch, chemicals (not only gravity; not "completely random") | **Directly supported** (packet refines game's "random" wording) | `logs.root_morph` (hydro/thigmotropism), `logs.root_orientation` ("semi-random") |
| S7 | Phototropism = directional growth toward light; light is a stronger shoot cue than root cue | **Directly supported** | `plants.stem_analysis` (`data.js:145`), `logs.solutions_search` #2 |
| S8 | Plants can grow in space with adapted systems; pillows manage media/fluids, not a gravity vector | **Directly supported** | `logs.veggie_history`; `plants.medium` |
| S9 | Auxin mediates gravitropic elongation (packet: optional/"unless taught separately") | **Curriculum enrichment / game-optional** | Game states auxin (`data.js:241`); packet de-emphasizes it |
| S10 | Root channels/moisture gradients/rotating chambers as orientation substitutes | **Game fiction-adjacent / plausible engineering** (packet-labeled) | `logs.solutions_search`; NASA Ames mesh (`logs.guide_notes`) |
| S11 | Environmental readings (nutrients, water, temp, humidity, light/PAR, 16/8) nominal | **Directly supported** | `sensors.*` nodes |
| S12 | Underlying real-world validity of the gravitropism/statolith model | **Real-world science — already verified upstream** (Master Audit v1.0 lines 21/36 verified serious science claims against authoritative sources; not reopened) | §12.1 |

No claim in the packet **contradicts** the game. The only divergences are the packet **omitting** the game's "amyloplast" (DISC-03) and **de-emphasizing** auxin — both defensible simplifications for a middle-school audience, and the packet's own boundary notes handle the "random roots"/"only gravity" oversimplifications more carefully than the game text does.

---

## 12. Standards and External Sources (verification status)

### 12.1 Science claims and NGSS/standards architecture — already resolved upstream (not reopened)

These were **not** left open by this audit; prior repository work settled them, and this audit confirms that settlement:

- **Science claims verified against authoritative sources.** `sss/audit/SSS_MASTER_AUDIT_v1.0.md` records: *"Verified the remaining historical, spaceflight, plant-lighting, radiation, fungal, and mycorrhizal claims against primary or authoritative sources"* (line 21) and *"Completed primary/authoritative source verification for the serious science concerns"* (line 36).
- **NGSS treatment for Case 01 is deliberate, not incidental.** The Master Audit establishes the exact framing this packet uses — *"possible engineering extension through MS-ETS1-1/2 rather than claiming a direct life-science PE"* (line 294) — with the standing warning that **gravitropism is not itself a standalone middle-school performance expectation** (Master Audit line 294; NGSS table finalized with SEP/DCI/CCC and alignment limitations, line 23).
- **The Blueprint adopted that framing as approved architecture.** `sss/blueprint/SSS_CURRICULUM_BLUEPRINT_v1.0.md` sets NGSS as the standards anchor (line 8) and locks Case 01 as gravitropism / "Pattern investigator" / design an alternative directional cue (line 451).

Consequently the earlier "engineering-only PE framing for life-science content" concern is **withdrawn as a resolved design decision, not a discrepancy.** The packet's "supports components of the standards; does not by itself fulfill an entire performance expectation" caveat matches the approved architecture. No standards re-alignment is required, and the science claims do not need a fresh authoritative-source pass.

### 12.2 Remaining external check — URL resolution and title match (COMPLETED in this audit)

The one narrow external item that genuinely remained was: do the exact URLs printed in the packet still resolve, and do their titles match what the packet calls them? Checked via live fetch on 2026-07-23 (results below). **All eight URLs resolve.**

| # | Packet label | URL | Resolves? | Title-match result |
|---|---|---|---|---|
| 1 | NASA *Growing Plants in Space* | nasa.gov/…/growing-plants-in-space/ | ✅ | **Exact** — page title "Growing Plants in Space" |
| 2 | NASA Ames *Plant Gravity Perception (SpaceX-13)* | nasa.gov/ames/…/plant-gravity-perception-spacex-13/ | ✅ | **Cosmetic mismatch** — on-page title reads "Plant Gravity Perception (**Space-13**)". The PGP experiment did fly on SpaceX CRS-13, so the packet's "SpaceX-13" is arguably clearer, but it does not match NASA's on-page label. *(Minor — DISC-09)* |
| 3 | NASA *Veggie Plant Growth System Activated on ISS* | nasa.gov/missions/station/veggie-plant-growth-system-activated-…/ | ✅ | **Match** — page spells out "International Space Station" where packet abbreviates "ISS" (trivial) |
| 4 | NASA Science *Plant Biology Program · Hardware* | science.nasa.gov/…/plant-biology/hardware/ | ✅ | **Cosmetic** — the /hardware/ URL loads, but the page `<title>` is "Plant Biology Program". Packet's "· Hardware" names the subpage, not the title. *(Minor — DISC-09)* |
| 5 | *Nakamura et al. (2020)* *Settling for Less: Do Statoliths Modulate Gravity Perception?* | pubmed.ncbi.nlm.nih.gov/31963631/ | ✅ | **Author error** — title ✅ and year (2020) ✅, but the authors are **Ditengou, Teale & Palme**, not "Nakamura et al." Nakamura is a *cited reference within* this paper. See **DISC-08**. *(Minor–Moderate)* |
| 6 | NASA OSDR *Arabidopsis Seedlings in Microgravity (OSD-38)* | osdr.nasa.gov/bio/repo/data/studies/OSD-38 | ✅ | **Confirmed** — the OSDR metadata API (`osdr.nasa.gov/osdr/data/osd/meta/38`) returns an *Arabidopsis thaliana* (Col-0) seedling **spaceflight vs. ground-control** multi-omic study. The packet's "Arabidopsis Seedlings in Microgravity" label is accurate. |
| 7 | NGSS MS-ETS1-1/-2 | nextgenscience.org | ✅ | **Match** — "Next Generation Science Standards" home; MS-ETS1 reachable via the standards search |
| 8 | *Game access URL* (Teacher p.1) | interstellarharvest.github.io/Space-Sprout-Sleuth/ | ✅ | **Match** — live game, title "Space Sprout Sleuth," SAA framing confirmed |

**Summary of the URL check:** one substantive fix (the Nakamura → Ditengou/Teale/Palme attribution, **DISC-08**, now applied); two cosmetic title-label items (#2 SpaceX-13 vs Space-13 — fixed; #4 "· Hardware" vs "Plant Biology Program" — kept by design; **DISC-09**); and #6 OSD-38 confirmed via the OSDR metadata API. Every link is live and every printed reference is now verified.

*(The game's fun-fact history — Veggie 2014; Aug 2015 Lindgren harvest shared with Kelly & Yui; Veg-01 returned to Earth — was set by correction spec v0.1 and falls under the Master Audit's completed source verification; not reopened here.)*

---

## 13. Discrepancy Register

| ID | Severity | Responsibility | Editions | Finding | Evidence |
|---|---|---|---|---|---|
| **DISC-01** | Minor | Curriculum | Teacher | **✅ APPLIED to v1.0.** Teacher distractor table adds **"Water problem"**, which is not one of the four selectable in-game diagnoses. A clarifying note now follows the distractor table stating the nutrient/light/seed distractors are the three selectable incorrect options and "Water problem" is a teacher discussion distractor only. | Packet Teacher p.5 (note added after distractor table) vs `data.js:407-431` |
| **DISC-02** | Moderate | Human playtest decision (+ Curriculum) | Student, Teacher, Accessible | Pre-game **vocabulary (Task 1)** defines *gravitropism/statocyte/statolith* and **Task 4** lists "Microgravity disrupts orientation" — together may telegraph the answer before investigation. Mirrors the game's own transparency (briefing + mission question already point at orientation), so this is a design judgment, not an error. | Packet Task 1 & Task 4 vs game briefing `data.js:70`, diagnoses `data.js:407-431` |
| **DISC-03** | Minor | Curriculum (optional) | Student, Teacher, Answer Key, Accessible | Packet vocabulary calls statoliths "dense starch-filled structure"; the game specifies "starch-filled **amyloplasts**." Packet is less precise but not wrong. | Packet vocab vs `data.js:241` |
| **DISC-04** | Minor | Curriculum (optional) | All | Player character **"Dr. Nova"** (named in-game) is not referenced in the packet, which keeps the player generic. No conflict; a naming opportunity. | `index.html:3203`, `SPEC_v2.md:52` |
| **DISC-05** | ~~Moderate~~ → **Resolved / narrowed** | External verification | Teacher, Student (source line) | **Superseded.** The standards codes and science claims are settled upstream (Master Audit v1.0 lines 21/36/294; Blueprint v1.0 lines 8/451) — the MS-ETS1-1/2 *supporting* framing (gravitropism not a standalone PE) is approved architecture, not a discrepancy. The only external item was URL resolution/title match, now **completed** (see §12.2, DISC-08/09). | §12.1, §12.2 |
| **DISC-06** | No issue (advisory) → **✅ APPLIED** | Human playtest decision / Curriculum | Teacher | **✅ APPLIED to v1.0.** Task 8 engineering response has **no in-game counterpart action** (Campaign 1 has no solution-selection step); it is worksheet-only. The Teacher "Plausible Engineering" panel now notes that students design this on the worksheet and that Campaign 1 has no in-game apply-the-fix step (solutions appear only as mission-log discussion). | No `solutions:` in `cases[0]`; C2-only UI `index.html:4388` |
| **DISC-08** | Minor–Moderate | Curriculum | Teacher (source list) | **✅ APPLIED to v1.0.** Source #5 was attributed to "Nakamura et al. (2020)"; the PubMed record (PMID 31963631, *"Settling for Less: Do Statoliths Modulate Gravity Perception?"*, 2020) is authored by **Ditengou, Teale & Palme**. Corrected in the source list (title/year unchanged; URL unchanged). | Live fetch of pubmed.ncbi.nlm.nih.gov/31963631/ (2026-07-23) |
| **DISC-09** | Minor | Curriculum | Teacher (source list) | **Partly applied.** #2 label corrected "(SpaceX-13)" → **"(Space-13)"** to match NASA's on-page title (URL slug unchanged, still resolves). #4 **left as-is by design:** "Plant Biology Program · Hardware" accurately names the /hardware/ subpage the URL points to, even though that page's generic `<title>` is just "Plant Biology Program." | Live fetch (2026-07-23), §12.2 |
| **DISC-07** | No issue | — | — | Verified matches: case identity, mission question, symptoms, nominal conditions, four evidence sources, four diagnosis options, correct diagnosis, statolith mechanism, intervention menu, SAA lore, recorded baseline = current HEAD. | §5–§11 |

No **Critical** or **Major** discrepancies were identified. The two reviewer-confirmed edits (DISC-01, DISC-06) are classroom-clarity fixes that do not change lesson content.

---

## 14. Recommended Curriculum Changes

**Blocking (none for game-compatibility).** No change is required to make the packet compatible with the game.

**✅ Applied to v1.0 in this pass:**
1. **DISC-01:** Added a note after the Teacher distractor table — the nutrient/light/seed distractors are the three selectable incorrect in-game options; "Water problem" is a teacher discussion distractor only.
2. **DISC-06:** Added to the Teacher "Plausible Engineering" panel that Task 8 is a worksheet design; Campaign 1 has no in-game apply-the-fix step (solutions appear only as mission-log discussion).
3. **DISC-08:** Corrected source #5 attribution "Nakamura et al. (2020)" → **Ditengou, Teale & Palme (2020)** (title/year/URL unchanged).
4. **DISC-09 (partial):** Corrected the "(SpaceX-13)" label to **"(Space-13)"** to match NASA's page (URL unchanged). Left "Plant Biology Program · Hardware" as-is — it accurately names the /hardware/ subpage the URL targets.

**Post-edit layout revalidation — ✅ PASS.** After these edits, the publishing/layout regression was rerun in headless Chromium against the edited file (SHA-256 `5ccac6bf…6eb83b`): Student 3 / Teacher 7 / Answer Key 3 / Accessible 6 / All 19 pages, **zero overflow in every role**, grayscale and print preview clean, edit/fill persistence restores after reload, Teacher PDF 7 pages, no JS errors. The two added Teacher notes (p.4 engineering panel, p.5 distractor table) did not change pagination or cause overflow. Evidence: `validation-artifacts/` (harness, results JSON, checksum, Teacher PDF); addendum in `master/SSS_C1_CASE01_V1_VALIDATION_REPORT.md` §10.

**Still open (judgment calls / not applied — left for the author):**
5. **DISC-02:** Consider moving the deeper mechanism vocabulary (statocyte/statolith) to a *post-investigation* reveal, or reframing Task 1 as a word-bank completed *during* investigation — or confirm via playtest that the current pre-teach doesn't collapse the inquiry. *(Pedagogical decision — not made unilaterally.)*
6. **DISC-03:** Optionally add "amyloplast" to the statolith definition for vertical alignment to high-school biology. *(Enrichment, not a correction.)*
7. **DISC-04:** Optionally reference the player role "Dr. Nova, Space Sprout Sleuth (SAA)" for immersion. *(Optional.)*
8. Flip **"VALIDATION BUILD"** to approved once the print/font/tagged-PDF production blockers in `…V1_BLOCKERS_AND_EXCEPTIONS.md` are cleared. *(The standards/science-source gate is closed — §12.1; all printed URLs including OSD-38 are verified — §12.2.)*

---

## 15. Recommended Game Changes

The game is the source of truth and needs no change for compatibility. Two optional low-priority polish items surfaced by the crosswalk:

1. **"Random" phrasing:** `logs.gravitropism_confirmed` and `sensors`/`plants` nodes describe roots defaulting to "random growth." The packet's science boundary note correctly cautions against teaching roots as "completely random." The game already softens to "semi-random" in `logs.root_orientation`; consider harmonizing the other nodes to "semi-random / lacking a consistent vector." *(Minor / Game / optional.)*
2. **Intervention parity (design consideration, not a defect):** Campaign 1's engineering content is dialogue-only while the packet asks students to design a fix. If future revisions want gameplay to mirror the worksheet's Task 8, a Campaign-1 solution-selection step (as exists in Campaign 2) would align the two — but this is a scope decision, not a discrepancy.

---

## 16. Items Requiring Human Playtesting

1. **Reveal calibration (DISC-02):** does pre-teaching gravitropism/statolith vocabulary before play let students shortcut the investigation? Observe whether they still gather evidence or jump straight to "microgravity."
2. **Diagnosis-gate experience:** confirm students reach the four clues and hit the "Need more evidence!" gate as intended; verify the worksheet's "diagnose after unlock" timing feels right in a 60-minute block.
3. **Engineering step expectation (DISC-06):** confirm teachers/students aren't looking for an in-game "apply the fix" action that doesn't exist.
4. **Fallback path:** validate the Teacher "no-game evidence digest" (p.7) yields the same investigation outcomes when tech fails.
5. **Physical print / fonts / tagged PDF:** the packet's own open blockers (`…V1_BLOCKERS_AND_EXCEPTIONS.md §1`) — print at 100%, offline font determinism, and PDF/UA tagging — remain human tasks.

---

## 17. Files Inspected

**Game repository `Space Sprout Sleuth` @ `2a6e8a7`:**
- `index.html` — engine; data-load order (`:2686-2687`), clue-gating & diagnosis flow (`:3766-3880`, `:4247-4276`, `:6281-6306`), player name (`:3203`).
- `space_sprout_sleuth_data.js` — **Case 01 = `cases[0]` lines 66–440**: briefing (`:70`), dialogue sources crew/sensors/plants/logs (`:71-349`), clues (`:352-405`), diagnoses (`:407-431`), rankUpText (`:433`), explanation/funFact (`:435-439`).
- `resources/SPACE_SPROUT_SLEUTH_SPEC_v2.md` — SAA definition & Case 01 port note (`:52`, `:120-207`).
- Confirmed non-runtime: `resources/campaign_2/space_sprout_sleuth_data.js`, `resources/space_sprout_sleuth_data_backup.js`, `resources/index_backup.html` (all differ from loaded files).

**Curriculum repository `SSS-HHH-Curriculums` @ `8d6d31d`:**
- `sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html` — **primary audited artifact** (untracked); all four editions (Student 3pp / Teacher 7pp / Answer Key 3pp / Accessible 6pp).
- `…/master/SSS_C1_CASE01_V1_MIGRATION_AUDIT.md`, `…_V1_BLOCKERS_AND_EXCEPTIONS.md` — migration scope, recorded baseline `2a6e8a7`, deferred-verification statements.
- `sss/audit/data/corrections/SSS_SCIENCE_TEXT_CORRECTION_SPEC_v0.1.md` — the science-text corrections applied to the game at commit `2a6e8a7`.
- `shared/curriculum-bible/…v1.2`, `shared/visual-style-guide/…v1.0`, `shared/assets/insignia/saa.svg` (referenced by migration; not re-audited for content here).

---

## 18. Limitations

- **External browsing (scoped):** the packet's eight printed URLs were fetched live and their titles compared (§12.2). OSD-38's public HTML page is a JS app whose title did not render to the generic fetcher, so it was instead confirmed through the OSDR metadata API (`osdr.nasa.gov/osdr/data/osd/meta/38`), which returned the Arabidopsis-seedling spaceflight study. Standards codes and real-world science validity were **not** re-verified here because they are already settled upstream (Master Audit v1.0 + Blueprint v1.0, §12.1); this audit relied on that prior verification rather than repeating it.
- **Static analysis only:** the game was not launched/playtested; engine behavior was inferred from `index.html` logic and data. Items needing live confirmation are in §16.
- **Editions:** the four role editions were extracted from one HTML file; repeated content across roles was treated as one curriculum claim unless wording differed materially (differences noted, e.g., Answer-Key-only "Kim," Teacher-only "Water problem").
- **Scope:** only Campaign 1, Case 01 was audited. Cross-references to other cases (e.g., the correction spec's Case 02 bee fun-fact) were noted only where they bore on Case 01's baseline.
- The audited packet is **untracked in git**; a future re-audit should pin it to a committed blob SHA for reproducibility.

---

## Final Verdict

### **Compatible with minor curriculum corrections.**

The packet teaches the diagnosis the game encodes as correct, uses the game's exact four-source evidence model and four diagnosis options, maps its nine tasks onto the game's enforced investigate-then-diagnose flow, and records a baseline commit that is the current game HEAD. No Critical or Major discrepancies exist.

**Changes that should block approval:** *(none are game-compatibility blockers; the standards/science-source gate is closed — §12.1, and every printed URL is verified — §12.2.)* The content-side corrections this audit surfaced have all been applied (see below). The only items left before lifting "VALIDATION BUILD" are the packet's own production blockers: physical print sample, offline-font determinism, and tagged accessible PDF (`…V1_BLOCKERS_AND_EXCEPTIONS.md`).

**✅ Applied to v1.0 in this pass (no lesson-content change):**
1. Teacher "Water problem" labeled as an additional discussion distractor, not a selectable in-game diagnosis (DISC-01).
2. Teacher note added that the engineering response is completed on the worksheet — Campaign 1 has no in-game "apply the fix" screen (DISC-06).
3. Source #5 attribution corrected "Nakamura et al." → **Ditengou, Teale & Palme (2020)** (DISC-08).
4. Source #2 label "(SpaceX-13)" → "(Space-13)" to match NASA's page (DISC-09, partial; URL unchanged).

**Nonblocking / optional (left for the author):**
1. "· Hardware" suffix on source #4 kept by design — it names the /hardware/ subpage the URL targets (DISC-09).
2. Reconsider or playtest the pre-game vocabulary reveal of the mechanism (DISC-02).
3. Optionally add "amyloplast" to the statolith definition (DISC-03).
4. Optionally name the player role "Dr. Nova" for immersion (DISC-04).
5. *(Game, optional)* harmonize "random" → "semi-random" root-growth wording (§15).

**External verification status — CLOSED.** Science claims and NGSS/standards architecture are verified/approved upstream (Master Audit v1.0 + Blueprint v1.0). All eight printed URLs were fetched and their titles matched; OSD-38 was confirmed via the OSDR metadata API (§12.2). Nothing external remains open.

*End of report.*
