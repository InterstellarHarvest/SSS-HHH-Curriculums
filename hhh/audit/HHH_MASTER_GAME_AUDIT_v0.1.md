# HHH Master Game Audit — Phase 1

**Document:** `HHH_MASTER_GAME_AUDIT_v0.1`  
**Audit date:** 2026-08-11  
**Scope:** read-only game-content, historical/scientific accuracy, evidence architecture, implementation integrity, and curriculum readiness  
**Final disposition:** `AUDIT_COMPLETE — GAME_REMEDIATION_REQUIRED`

> This audit does **not** modify the HHH game, curriculum repository, registry, or case packages. It records current runtime truth, external historical/scientific verification, and curriculum-planning implications. SSS remains frozen and is used only as a methodological/reference baseline.

## 1. Authority and exact baselines

| Authority | Authorized | Live remote verified | Audit use |
|---|---|---|---|
| Curriculum `InterstellarHarvest/SSS-HHH-Curriculums` | `f61b77a63020254c8729d63c9960492cff0dc948` | `f61b77a63020254c8729d63c9960492cff0dc948` | governing curriculum/shared contracts |
| HHH game `InterstellarHarvest/Hunger-Harvest-History` | `9b8545ed6ecf98b337326390400076e36789e056` | `9b8545ed6ecf98b337326390400076e36789e056` | shipped runtime authority |
| Local game audit checkout | `9b8545ed6ecf98b337326390400076e36789e056` | n/a | read-only static/runtime analysis |

**Baseline verdict:** no divergence. The live remote `main` tips still agree with both owner-authorized SHAs. The audit did not silently adopt a newer baseline.

### Authority order applied

**Game truth:** shipped runtime at authorized SHA → current README/docs that accurately describe runtime → current design/handoff intent → older plans/demos only as historical intent evidence.

**Curriculum-production truth:** governing shared contracts at curriculum SHA → Curriculum Bible v1.3 → Visual Style Guide + amendments → implementation schemas/registry/editor/validators → final SSS audit/remediation lessons → older SSS records only as rationale/history.

## 2. Sources inspected

### HHH shipped/runtime sources

- `index.html` — present; `CLAUDE.md` is local/supporting material and is not elevated above shipped runtime.
- `hhh_data.js` — present; `CLAUDE.md` is local/supporting material and is not elevated above shipped runtime.
- `hhh_campaign_2_data.js` — present; `CLAUDE.md` is local/supporting material and is not elevated above shipped runtime.
- `README.md` — present; `CLAUDE.md` is local/supporting material and is not elevated above shipped runtime.
- `CLAUDE.md` — present; `CLAUDE.md` is local/supporting material and is not elevated above shipped runtime.
- Supporting HHH intent/history: `resources/HHH_DESIGN_BIBLE.md`, `resources/HHH_HANDOFF.md`, `resources/HHH_IMPLEMENTATION_PLAN.md`, Campaign 2 design/implementation material, review/re-review records, and gameplay/evidence harnesses where relevant.

### Governing curriculum/shared sources

- `AGENTS.md`
- `shared/curriculum-bible/SSS_HHH_CURRICULUM_BIBLE_v1.3.md`
- `shared/implementation/SSS_TO_HHH_PRODUCTION_LESSONS_v1.0.md`
- `shared/implementation/SSS_HHH_TEACHER_EDITION_CONTRACT_v1.0.md`
- `shared/implementation/SSS_HHH_ACCESSIBLE_ADAPTATION_CONTRACT_v1.0.md`
- `shared/visual-style-guide/VISUAL_STYLE_GUIDE_v1.0.md` and controlling amendments
- `shared/implementation/case-package.schema.v2.json`, `case-registry.schema.v2.json`, `case-registry.v2.json`, `case-release-history.schema.v1.json`, `layout-overrides.schema.v1.json`
- `sss/audit/SSS_MASTER_AUDIT_v1.0.md`, `sss/audit/data/SSS_STATIC_CONTENT_INVENTORY_v1.0.json`, `sss/blueprint/SSS_CURRICULUM_BLUEPRINT_v1.0.md` — **method references only**, not HHH content templates.

### External verification

Substantive real-world claims were checked against academic, government, archival, institutional, or primary/near-primary sources where practical. The external bibliography is in §13. Source uncertainty is preserved rather than “corrected” into false certainty.

## 3. Executive audit disposition

All 15 shipped levels were audited before curriculum sequencing was recommended. The game is structurally playable at the authorized baseline: every completion-required chain is reachable, normal cases have a resolvable final record/diagnosis, and the three special levels (C1 L0, C1 L7, C2 L6) intentionally use nonstandard completion mechanics. No dead completion route or baseline conflict blocks the program.

However, **curriculum-affecting remediation is required before affected case production**. The most material issues are:

- C1 L1 compresses a protracted cereal-domestication process into a precise 9700 BCE reconstructed individual/event without enough source-status qualification.
- C1 L3 universalizes Irish Lumper dependence and collapses famine causation too aggressively.
- C1 L5 states that exposed subsoil has “no microbial life” and “will grow nothing.”
- C2 L0 turns “too clean” into an overgeneralized document-forensics rule.
- C2 L5 presents broad common-mycorrhizal-network water/nutrient/signal sharing as settled and overstates direct fossil chronology.
- C2 L2 has a concrete runtime data-semantics defect: an `insight:true` clue is mandatory because it gates the next location.

These corrections do **not** invalidate HHH’s overall level architecture or prevent Blueprint work. The evidence is sufficient to establish HHH-specific curriculum architecture while game remediation proceeds; worksheets for affected cases should not be finalized against the current problematic wording.

## 4. Aggregate runtime inventory

| Campaign | Runtime level | Runtime title | Date/period | Location | Sources | Required | Insight/optional | Approx. direct-route words | Completion |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| C1 | 0 | Temporal Agricultural Archive Facility | 2387 | TAA Orientation | 4 | 4 | 0 | 449 | special |
| C1 | 1 | The Fertile Crescent | 9,700 BCE | a river valley | 4 | 4 | 0 | 504 | standard final record/diagnosis |
| C1 | 2 | Sumer | ~2000 BCE | the southern floodplain | 10 | 5 | 5 | 684 | standard final record/diagnosis |
| C1 | 3 | County Cork | 1845 | the Irish countryside | 9 | 5 | 4 | 773 | standard final record/diagnosis |
| C1 | 4 | Karlsruhe | 1909 | Fritz Haber's laboratory | 6 | 5 | 1 | 778 | standard final record/diagnosis |
| C1 | 5 | The Dust Bowl | 1935 | Oklahoma & Washington, DC | 10 | 5 | 5 | 701 | standard final record/diagnosis |
| C1 | 6 | The Vertical Farm | 2041 | A commercial vertical farm | 10 | 5 | 5 | 836 | standard final record/diagnosis |
| C1 | 7 | The Temporal Agricultural Archive | 2387 | home, at the end of the thread | 4 | 2 | 2 | 463 | special |
| C2 | 0 | The Audit | 2387 | TAA Facility | 4 | 4 | 0 | 545 | standard final record/diagnosis |
| C2 | 1 | The Floating Gardens | 1487 | Tenochtitlan | 7 | 4 | 3 | 460 | standard final record/diagnosis |
| C2 | 2 | The Seeds They Kept | 1941 | Leningrad | 6 | 5 + 1 gate-required insight | 1 tagged / 0 operationally optional | 587 | standard final record/diagnosis |
| C2 | 3 | The Quiet Billion | 1968 | Mexico | 6 | 4 | 2 | 516 | standard final record/diagnosis |
| C2 | 4 | The Bloom That Needed Poison | 2301 | Concord space | 6 | 4 | 2 | 484 | standard final record/diagnosis |
| C2 | 5 | The Living Record | 2387 | First Garden, Earth | 6 | 5 | 1 | 782 | standard final record/diagnosis |
| C2 | 6 | The Source | 2389 | Concord space, the ARS Chamber | 7 | 5 | 2 | 724 | special |

**Reading-burden method:** approximate word counts are the summed shortest dialogue/reveal paths required to expose the direct evidence set, not classroom timed-reading estimates. Completionist play is longer. C2 L2 is adjusted upward to include `siege_witnessed` because that clue is structurally mandatory despite `insight:true`.

### Runtime integrity summary

- All 15 configured levels are present at the authorized baseline.
- Location gates are satisfiable in sequence; no required clue is stranded behind an impossible route.
- Normal cases require all non-insight clue tags before the final resolution UI becomes valid.
- C1 L0 uses a special “Initialize Thread” orientation gate; C1 L7 uses finale stabilization; C2 L6 uses confrontation plus a three-way final archival/value choice.
- C1 L7’s companion source is dynamically selected at runtime; a static parser can report a false `NO_START`/unrevealed-clue warning for the generic companion placeholder. Manual runtime/source inspection shows that this is intentional dynamic construction, not a dead route.
- C2 L2 is the one material clue-classification/gating inconsistency: `siege_witnessed` is labeled insight/optional in the source object but is required to unlock `seed_vault`.

## 5. Per-level audit

### C1 Level 0 — TAA Orientation

**Runtime identity:** `L0` · `Temporal Agricultural Archive Facility` · 2387 · TAA Orientation  
**Runtime source:** `hhh_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `READY_WITH_BOUNDARY_NOTE`

#### A. Runtime / completion integrity

- Sources: **4**; runtime-required non-insight clues: **4**; runtime-insight clues: **0**.
- Location gates: `briefing_chamber` (open); `thread_console` ← `briefed`.
- Completion: Special orientation completion: collect all four required orientation clues, return to the thread console/anchor, then initialize the thread; no ordinary historical diagnosis.
- Approximate direct-route reading burden: **449 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `briefing_chamber` / `nova` | Required; `briefed` | Nova: the human record is fraying. | `start → preview_oolian → chose → brief_premise → brief_task` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `briefing_chamber` / `zelketh` | Required; `met_zelketh` | Zel'keth: the 'deep current' of their network carries signals across time. | `start → deep_current` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `briefing_chamber` / `taa_records` | Required; `read_records` | Archive: the human chain runs from the first planted seed to humanity's journey to the stars. | `start → entry_begin` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `thread_console` / `scan_resonance` | Required; `resonance_scanned` | Resonance map locked: first fray point is a river-valley crescent, roughly 9,700 BCE. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> Initialize the thread.

#### C. Historical/scientific truth and source-status boundary

Entire setting and institution are fictional; only the archival reasoning vocabulary should be treated as real-world transferable practice.

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Distinguish archive procedure, record status, and source handling from the fictional institutional story that frames the game.
- **Principal reasoning operation:** provenance/source-status orientation.
- **What students genuinely reason about:** Students must decide what different record types can establish and understand that an archive preserves claims rather than automatically guaranteeing their truth.
- **Likely stumbling point:** Treating the fictional TAA, Concord, Zhel’ii, or resonance/thread technology as real historical authority.
- **Candidate evidence-processing structure:** archive orientation / source-status sorting.
- **Useful vocabulary:** archive, record, provenance, corroboration, source status, accession.
- **Candidate source/provenance task:** Classify an in-game testimony, archive record, and scan by what each can and cannot establish.
- **Chronology/map/data opportunity:** A simple provenance/source-type diagram; no historical geographic map is needed.
- **Possible synthesis/explanation product:** Short archive-procedure explanation rather than a diagnosis.
- **Plausible transfer/exit question:** Given a newly discovered record, what would you verify before treating it as reliable evidence?
- **No-game fallback:** A compact TAA orientation dossier reproducing the four required source texts with explicit FICTIONAL CONTEXT labeling.
- **Standalone lesson:** CONDITIONAL — useful as a short program orientation, not strong enough for a full historical case by itself.
- **Accessibility concern:** High lore density and unfamiliar institutional/species names before students have historical context.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D3.1.6-8 (source gathering/evaluation, if explicitly built into task); CCSS RH.6-8.1
- **Supporting:** CCSS RH.6-8.6
- **Contextual:** none proposed at audit stage.

### C1 Level 1 — Fertile Crescent / Early Grain Domestication

**Runtime identity:** `L1` · `The Fertile Crescent` · 9,700 BCE · a river valley  
**Runtime source:** `hhh_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `GAME_REMEDIATION_REQUIRED`

#### A. Runtime / completion integrity

- Sources: **4**; runtime-required non-insight clues: **4**; runtime-insight clues: **0**.
- Location gates: `grain_field` (open); `storage_pit` ← `nonshatter_trait`; `settlement_edge` ← `seed_selection`.
- Completion: Standard evidence gate: all 4 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **504 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `grain_field` / `woman` | Required; `replanting_seen` | She deliberately replants only the grain heads that held their seed instead of shattering, season after season. | `start → observe → replant_reveal` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `grain_field` / `handle_grain` | Required; `nonshatter_trait` | In these grain heads they does not shatter, so the seed stays fixed on the stalk instead of scattering to sow itself. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `storage_pit` / `examine_stores` | Required; `seed_selection` | She sets aside only the non-shattering heads as next year's seed. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `settlement_edge` / `neighbor` | Required; `knowledge_spreading` | A visitor leaves carrying the kept seed — the practice crosses to the next settlement. | `start → examine → share` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> She is deliberately selecting her crop: each harvest she sets aside the seed heads that held onto their grain and replants those, so generation by generation she has bred a wheat that depends on her hands to sow it.

**Distractors / false records:**
- The sturdy-headed grain happened to thrive on its own near her camp, and the plant essentially domesticated itself without any real choice on her part.
- An outsider arrived and taught her the whole method of farming at once.

#### C. Historical/scientific truth and source-status boundary

The woman, dialogue, and exact event are reconstructed/fictionalized; the non-shattering domestication pattern is archaeobotanically documented but gradual.

**Relevant finding IDs:** `HHH-GAME-C1L1-001`, `HHH-GAME-C1L1-002`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Explain cereal domestication as a cumulative selection process produced by repeated human harvesting, seed saving, and replanting, while distinguishing cultivation from later morphological domestication.
- **Principal reasoning operation:** chronology + cause/change over time + inference from archaeobotanical traits.
- **What students genuinely reason about:** Students must connect harvesting/replanting behavior to selection pressure and decide what non-shattering remains do—and do not—prove about a specific moment or person.
- **Likely stumbling point:** Reading domestication as a single intentional invention at exactly 9700 BCE rather than a long, geographically varied process.
- **Candidate evidence-processing structure:** chronology + evidence chain + documented/reconstructed status comparison.
- **Useful vocabulary:** domestication, cultivation, selection, non-shattering, rachis, wild type.
- **Candidate source/provenance task:** Compare the game vignette with archaeobotanical evidence; mark which parts are documented population-level evidence and which are narrative reconstruction.
- **Chronology/map/data opportunity:** Sourced Fertile Crescent map plus a broad archaeological timeline/range; do not plot a fabricated exact “first domestication” point.
- **Possible synthesis/explanation product:** Historical explanation of how repeated human choices create selection pressure over generations.
- **Plausible transfer/exit question:** What evidence would distinguish early cultivation from a population that had already become morphologically domesticated?
- **No-game fallback:** Evidence cards using archaeobotanical shattering/non-shattering data and a clearly labeled reconstructed harvesting vignette.
- **Standalone lesson:** YES after game-text/reconstruction remediation.
- **Accessibility concern:** Chronology spans millennia; the game’s single-person narrative can overpower the slower process unless source status is explicit.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D2.His.1.6-8; C3 D2.His.2.6-8; CCSS RH.6-8.7
- **Supporting:** C3 D3.2.6-8; CCSS WHST.6-8.2
- **Contextual:** none proposed at audit stage.

### C1 Level 2 — Sumer / Irrigation and Salinization

**Runtime identity:** `L2` · `Sumer` · ~2000 BCE · the southern floodplain  
**Runtime source:** `hhh_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `GAME_REMEDIATION_REQUIRED`

#### A. Runtime / completion integrity

- Sources: **10**; runtime-required non-insight clues: **5**; runtime-insight clues: **5**.
- Location gates: `irrigated_fields` (open); `river_bank` ← `salt_crust`; `scribes_room` ← `river_comparison`.
- Completion: Standard evidence gate: all 5 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **684 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `irrigated_fields` / `overseer` | Required; `irrigation_practice` | The overseer floods the fields from the channels again and again, and crops the land every season without the old fallow res. | `start → method_intro → drainage` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `irrigated_fields` / `sample_soil` | Required; `salt_crust` | The pale crust scabbing the dying plots is salt drawn up to the surface and left behind as the standing water evaporates in the sun. | `start → survey` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `irrigated_fields` / `trace_channels` | Required; `no_drainage` | Every channel feeds water onto the fields and not one drains it off again. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `irrigated_fields` / `examine_crops` | Insight/optional; `crops_examined` | The wheat dies in the same salted ground the barley still stands. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `river_bank` / `river_worker` | Required; `river_comparison` | Where the river and the marsh keep the water moving, the ground stays sweet as the current carries the salt away. | `start → soil → compare` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `river_bank` / `sample_water` | Insight/optional; `water_sampled` | The river water carries only a faint trace of salt, and never stops moving, so it never gets the chance to leave that salt behind the way the trapped fields do. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `river_bank` / `examine_plants` | Insight/optional; `plants_examined` | The reeds and levee plants grow thick and green in black, sweet soil. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `scribes_room` / `read_records` | Required; `scribe_record` | The temple tallies track the harvest falling year on year and the salt-tolerant barley quietly replacing the failing wheat. | `start → cause` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `scribes_room` / `examine_room` | Insight/optional; `room_examined` | The room has turned its mind to the gods, not the soil. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `scribes_room` / `query_archive` | Insight/optional; `archive_queried` | The TAA Archive names what the scribes can't: salinization. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The fields are salting themselves.

**Distractors / false records:**
- The gods truly have withdrawn their favour — or, in plainer terms, the rivers' flood has been failing and the fields are simply starved of water.
- A blight or pest is spreading through the crop, the way disease moved through the wild grain upstream.

#### C. Historical/scientific truth and source-status boundary

Irrigation salinization is real and historically important; exact overseer/scribe dialogue is reconstructed, and the extent of salinity’s role in state/economic decline is debated.

**Relevant finding IDs:** `HHH-GAME-C1L2-001`, `HHH-GAME-C1L2-002`, `HHH-GAME-C1L2-003`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Explain how irrigation, shallow groundwater, inadequate drainage, and evaporation can contribute to soil salinization while evaluating the limits of using salinity as a single explanation for broad historical decline.
- **Principal reasoning operation:** cause and consequence + systems reasoning + source comparison.
- **What students genuinely reason about:** Students must combine field observations, hydrology, comparison evidence, and written records; no single clue independently establishes the whole causal chain.
- **Likely stumbling point:** Assuming more irrigation always helps, or treating salinization as the sole cause of Sumerian political/economic change.
- **Candidate evidence-processing structure:** cause-effect systems diagram + evidence/source comparison.
- **Useful vocabulary:** irrigation, salinization, water table, drainage, evaporation, fallow, alluvial plain.
- **Candidate source/provenance task:** Compare physical evidence with the in-game scribe record and identify where the record’s explanation diverges from the inferred physical mechanism.
- **Chronology/map/data opportunity:** Sourced lower-Mesopotamia map/canal context plus deterministic water-table → evaporation → salt accumulation schematic.
- **Possible synthesis/explanation product:** Qualified causal explanation of field salinization, explicitly separated from claims about civilization-wide collapse.
- **Plausible transfer/exit question:** What additional evidence would be needed to distinguish salinization from other causes of a crop shift or settlement decline?
- **No-game fallback:** No-game packet with field profile, irrigation/drainage schematic, crop-tolerance comparison, and translated/secondary source excerpts with status labels.
- **Standalone lesson:** YES after the truncated required clue is corrected; broader decline language requires qualification.
- **Accessibility concern:** Several sources mix physical process and historical interpretation; students need a visible “local field mechanism vs. broader historical claim” distinction.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D2.His.14.6-8; C3 D3.2.6-8; CCSS RH.6-8.1
- **Supporting:** CCSS RH.6-8.7; CCSS WHST.6-8.2
- **Contextual:** NGSS Earth/human-impact systems as supporting context only unless explicitly assessed

### C1 Level 3 — Ireland 1845 / Blight and Famine

**Runtime identity:** `L3` · `County Cork` · 1845 · the Irish countryside  
**Runtime source:** `hhh_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `GAME_REMEDIATION_REQUIRED`

#### A. Runtime / completion integrity

- Sources: **9**; runtime-required non-insight clues: **5**; runtime-insight clues: **4**.
- Location gates: `potato_field` (open); `cottage_interior` ← `blight_agent`; `the_road` ← `sole_food`.
- Completion: Standard evidence gate: all 5 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **773 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `potato_field` / `farmer` | Required; `sudden_collapse` | The crop stood green and sound a week ago; he woke to a stench and a field gone black overnight. | `start → speed → recap` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `potato_field` / `blight` | Required; `blight_agent` | On the cool underside of the dying leaves grows a fine white down, fruiting along the lesion edges. | `start → device` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `potato_field` / `survey_field` | Required; `monoculture` | Every plant in the field is the one variety: the Lumper, grown from cuttings of cuttings until each is the twin of the last. | `start → resist` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `potato_field` / `sample_soil` | Insight/optional; `soil_clear` | The ground itself is sound: good dirt, no exhaustion, no poison, no salt. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `cottage_interior` / `woman` | Required; `sole_food` | The family lives on the potato and almost nothing else. | `start → diet → now` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `cottage_interior` / `records` | Insight/optional; `exports_continue` | The estate ledger and the parish book tell two halves of one truth: the potato has failed and the first hunger is setting in — while the same season's grain, butter, and… | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `the_road` / `traveler` | Required; `spreading` | The same rot stands in every field from here to the coast — the next parish, the next county, the far side of the island, all in the one season. | `start → reach → record` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `the_road` / `survey_region` | Insight/optional; `oomycete` | The regional scan maps the spread onto the weather: the organism rides cool, wet wind, fruiting in damp and stalling in drought, leaping farm to farm on rain and breeze. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `the_road` / `examine_evidence` | Insight/optional; `displacement` | The verge is strewn with the leavings of flight — a dropped pot, a child's shoe, the cold ash of roadside fires, cart-ruts worn deep by traffic all going one way. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> A living organism — a water-mould, later named Phytophthora infestans — is killing the potato, spreading on wind and rain from one identical Lumper to the next.

**Distractors / false records:**
- It is a judgment on the land — or, in plainer terms, the soil has finally failed after too many years of the same crop worked too hard.
- It is simply the cold, wet season rotting the crop in the wet ground — bad weather, nothing more.

#### C. Historical/scientific truth and source-status boundary

The pathogen is documented science; the game characters are reconstructed. Famine causation is social, political, economic, and biological, not a one-variable diagnosis.

**Relevant finding IDs:** `HHH-GAME-C1L3-001`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Evaluate why potato late blight became a famine by integrating plant disease, crop dependence, poverty/land systems, food access, exports, relief, and historical context rather than treating one factor as sufficient.
- **Principal reasoning operation:** multiple causation + contextualization + corroboration.
- **What students genuinely reason about:** Students must distinguish a biological crop failure trigger from the social and political conditions that turned crop loss into mass hunger.
- **Likely stumbling point:** “Blight alone caused the famine” or the opposite simplification that every Irish field was one genetically identical Lumper and no other food existed.
- **Candidate evidence-processing structure:** multi-causal evidence map / source contribution-and-limitation matrix.
- **Useful vocabulary:** late blight, oomycete, Phytophthora infestans, Lumper, clonal propagation, subsistence, tenant farming.
- **Candidate source/provenance task:** Separate pathogen evidence from evidence about dependence, food movement, and social conditions; state what each source cannot establish alone.
- **Chronology/map/data opportunity:** Sourced Ireland map showing regional context plus a 1845–1852 chronology; any export or crop data must be sourced and dated.
- **Possible synthesis/explanation product:** Multi-causal historical explanation that identifies the pathogen as crop-failure mechanism without reducing famine mortality to biology alone.
- **Plausible transfer/exit question:** What evidence would you need to distinguish “crop failure” from “famine” as historical explanations?
- **No-game fallback:** Primary/secondary evidence dossier with blight evidence, dependence statistics, land/relief context, and export records; no invented peasant dialogue as primary source.
- **Standalone lesson:** YES after universalizing game language is corrected and teacher context is locked.
- **Accessibility concern:** Emotionally heavy content, many causal layers, and potential misconception that a single “correct diagnosis” is the full historical explanation.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D2.His.14.6-8; C3 D3.1.6-8; C3 D3.2.6-8; CCSS RH.6-8.1
- **Supporting:** CCSS RH.6-8.9; CCSS WHST.6-8.1
- **Contextual:** Plant-pathology science supports the history task but need not be a direct NGSS alignment

### C1 Level 4 — Karlsruhe 1909 / Haber Process

**Runtime identity:** `L4` · `Karlsruhe` · 1909 · Fritz Haber's laboratory  
**Runtime source:** `hhh_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `READY_AFTER_POLISH_AND_QUALIFICATION`

#### A. Runtime / completion integrity

- Sources: **6**; runtime-required non-insight clues: **5**; runtime-insight clues: **1**.
- Location gates: `reactor_chamber` (open); `habers_office` ← `equilibrium_stall`.
- Completion: Standard evidence gate: all 5 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **778 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `reactor_chamber` / `examine_apparatus` | Required; `equilibrium_stall` | The apparatus is sound — the high-pressure vessel holds, the seals are tight, nothing is leaking. | `start → device` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `reactor_chamber` / `measure_readings` | Required; `pressure_yield` | The pressure tells the story the bench can't reach. | `start → climb` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `reactor_chamber` / `run_analysis` | Required; `heat_paradox` | The reaction gives off heat as it makes ammonia. | `start → hot` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `habers_office` / `haber` | Required; `catalyst_rate` | Haber is caught between cold yield and hot speed, and has been trying to break the bind not with heat but with a catalyst: a substance that hurries the reaction along without… | `start → bind → catalyst` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `habers_office` / `review_notebooks` | Required; `recycle_yield` | The notebooks are columns of disappointment — every run yields only a few parts in a hundred, whatever the setting. | `start → margin` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `habers_office` / `query_archive` | Insight/optional; `fertilizer_future` | Within a few years Carl Bosch turns this bench into industry, and in time the trickle of ammonia becomes an ocean of fertilizer. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The reaction is reversible and sheds heat as it works, so it settles at a balance with only a trace of ammonia — and forcing it hotter, the obvious move, only drives it further back.

**Distractors / false records:**
- The apparatus is at fault — there is a leak in the high-pressure vessel, and the ammonia is escaping before it can ever be collected.
- He is simply not pushing hard enough — drive the temperature far higher and the reaction will be forced to completion, the way heat hurries any sluggish process along.

#### C. Historical/scientific truth and source-status boundary

Haber’s laboratory synthesis and Bosch’s industrial high-pressure engineering are distinct contributions. “Moderate” temperature is a compromise relative to the reaction, not an everyday low temperature.

**Relevant finding IDs:** `HHH-GAME-C1L4-001`, `HHH-GAME-C1L4-002`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Explain the pressure/temperature/catalyst/recycle tradeoffs that made ammonia synthesis workable and place Haber’s laboratory result and Bosch’s industrial scale-up in correct historical relationship.
- **Principal reasoning operation:** technological change + mechanism/tradeoff reasoning.
- **What students genuinely reason about:** Students must distinguish equilibrium effects from reaction-rate effects and use multiple conditions together rather than retrieve one “magic” variable.
- **Likely stumbling point:** Believing a catalyst shifts equilibrium or that simply maximizing temperature produces the highest ammonia equilibrium yield.
- **Candidate evidence-processing structure:** condition–mechanism–effect matrix / process-flow analysis.
- **Useful vocabulary:** ammonia, equilibrium, catalyst, pressure, yield, reaction rate, recycle.
- **Candidate source/provenance task:** Compare lab observations, Haber testimony/notebook evidence, and later historical reference on industrialization; identify which evidence supports chemistry versus historical attribution.
- **Chronology/map/data opportunity:** Deterministic Haber-process flow with pressure/temperature/catalyst/recycle labels; optional sourced 1908–1913 timeline.
- **Possible synthesis/explanation product:** Explain why a compromise operating condition plus high pressure, catalyst, and recycling works better than “just make it hotter.”
- **Plausible transfer/exit question:** Which changes affect equilibrium position, which affect rate, and which improve overall process yield without changing equilibrium?
- **No-game fallback:** No-game lab evidence sheet with controlled qualitative equilibrium/rate data and a short Haber/Bosch historical source set.
- **Standalone lesson:** YES, though it is science-heavy and needs careful middle-school framing.
- **Accessibility concern:** Dense technical vocabulary and abstract equilibrium/rate distinction; diagrams should reduce rather than add cognitive load.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** CCSS RH.6-8.7; CCSS RH.6-8.1
- **Supporting:** C3 D2.His.2.6-8; CCSS WHST.6-8.2
- **Contextual:** NGSS chemical-reaction/engineering concepts are supporting; do not claim a middle-school PE if equilibrium is not directly assessed

### C1 Level 5 — Dust Bowl 1935

**Runtime identity:** `L5` · `The Dust Bowl` · 1935 · Oklahoma & Washington, DC  
**Runtime source:** `hhh_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `GAME_REMEDIATION_REQUIRED`

#### A. Runtime / completion integrity

- Sources: **10**; runtime-required non-insight clues: **5**; runtime-insight clues: **5**.
- Location gates: `dust_bowl_farm` (open); `eroded_gully` ← `no_root_structure`; `committee_room` ← `profile_stripped`.
- Completion: Standard evidence gate: all 5 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **701 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `dust_bowl_farm` / `farmer` | Required; `grass_plowed` | The farmer broke the native prairie sod and sowed it all to wheat in the boom years, fence to fence, the way everyone did. | `start → plough` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `dust_bowl_farm` / `sample_soil` | Required; `no_root_structure` | The field soil is fine as flour and just as loose. | `start → reading` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `dust_bowl_farm` / `examine_evidence` | Required; `grass_control` | Along the fence line a narrow strip of native grass was never plowed, and it has kept its soil through the same drought that stripped the field bare beside it. | `start → compare` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `dust_bowl_farm` / `survey_land` | Insight/optional; `extent` | From a rise you can see how far the ruin runs. | `start → extent` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `eroded_gully` / `examine_strata` | Required; `profile_stripped` | The cut wall of the gully reads like a ruined book: a dark band of topsoil that should run many inches deep is worn to barely one, and below it only pale,… | `start → topsoil` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `eroded_gully` / `sample_core` | Insight/optional; `dead_soil` | A core driven through the gully floor confirms the wound runs deeper than the eye: beneath the last residual topsoil, the subsoil is biologically dead — no organic matter, no microbial life,… | `start → verdict` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `eroded_gully` / `survey_region` | Insight/optional; `scale` | A regional dust survey puts numbers to the catastrophe: erosion like this gully repeated across a hundred million acres, tens of thousands of farms abandoned, soil from these plains falling on cities… | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `committee_room` / `bennett` | Required; `conservation_answer` | Bennett has the answer and the patience to land it: the land can be saved by never leaving it bare — keeping crop residue and grass cover, plowing along the contours, planting… | `start → case → answer` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `committee_room` / `review_testimony` | Insight/optional; `political_contest` | Bennett's testimony draft and the papers beside it show the fight he's walking into: land and agricultural interests have spent years insisting the soil is an endless resource and the dusters a… | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `committee_room` / `query_archive` | Insight/optional; `soil_act` | The forward thread is bright, for once: weeks after this testimony Congress passes the Soil Conservation Act and builds a permanent service to carry the work nationwide — contour plowing, terracing, cover… | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The Dust Bowl is not simply a drought.

**Distractors / false records:**
- This is only a drought — a natural disaster, an act of God.
- The soil is simply worn out — too many seasons of wheat have used up its richness.

#### C. Historical/scientific truth and source-status boundary

Drought and land use both matter. Subsoil can have lower organic matter, fertility, roots, and microbial biomass without being literally biologically dead.

**Relevant finding IDs:** `HHH-GAME-C1L5-001`, `HHH-GAME-C1L5-002`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Explain the Dust Bowl as an interaction among drought, removal of prairie cover, soil erosion, land use, and conservation/policy responses.
- **Principal reasoning operation:** multiple cause/consequence + human-environment systems + policy response.
- **What students genuinely reason about:** Students must compare damaged and protected land, connect root structure to erosion, and distinguish contributing causes from overly simple “drought only” or “soil nutrients only” explanations.
- **Likely stumbling point:** Treating drought as irrelevant because the game rejects a drought-only diagnosis, or treating exposed subsoil as literally sterile/devoid of life.
- **Candidate evidence-processing structure:** before/after land-cover comparison + causal chain + policy/source corroboration.
- **Useful vocabulary:** topsoil, erosion, prairie sod, drought, shelterbelt, contour farming, soil conservation.
- **Candidate source/provenance task:** Compare farmer testimony, soil-profile evidence, control vegetation, and Bennett/policy records; identify which sources support mechanism and which support response.
- **Chronology/map/data opportunity:** Sourced Dust Bowl region map; deterministic soil-profile/erosion comparison; optional 1933–1935 policy chronology.
- **Possible synthesis/explanation product:** Qualified explanation: severe drought interacted with exposed, erosion-prone soils created by land-use practices; conservation reduced vulnerability.
- **Plausible transfer/exit question:** Why can the same drought produce different erosion outcomes on intact grassland and recently plowed soil?
- **No-game fallback:** Photo/map/soil-profile/policy dossier using USDA/NRCS sources and clear source dates.
- **Standalone lesson:** YES after biological-zero claims are corrected.
- **Accessibility concern:** Strong rhetoric can turn a systems explanation into a moral blame story; students need explicit distinction between contributing conditions and individual culpability.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D2.His.14.6-8; CCSS RH.6-8.7; CCSS RH.6-8.1
- **Supporting:** C3 D2.His.2.6-8; CCSS WHST.6-8.2
- **Contextual:** NGSS Earth-surface/human-impact systems supporting context

### C1 Level 6 — Vertical Farm 2041

**Runtime identity:** `L6` · `The Vertical Farm` · 2041 · A commercial vertical farm  
**Runtime source:** `hhh_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `READY_WITH_TEACHER_QUALIFICATION`

#### A. Runtime / completion integrity

- Sources: **10**; runtime-required non-insight clues: **5**; runtime-insight clues: **5**.
- Location gates: `failed_farm_floor` (open); `control_room` ← `ammonia_burn`; `press_briefing` ← `consortium_crash`.
- Completion: Standard evidence gate: all 5 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **836 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `failed_farm_floor` / `farm_researcher` | Required; `starved_while_fed` | The researcher has documented the failure floor by floor: the crops showed nitrogen starvation and caustic root burn at once — yet the feed system never stopped dosing nutrient. | `start → symptom → reveal` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `failed_farm_floor` / `examine_crops` | Required; `ammonia_burn` | The dead crops carry a contradiction that resolves into a single cause: nitrogen starvation and ammonia burn together. | `start → reading` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `failed_farm_floor` / `scan_systems` | Insight/optional; `systems_running` | A full scan of the facility's machinery comes back clean: pumps, dosers, climate, circulation, sensors — every mechanical system operational, no faults. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `failed_farm_floor` / `survey_floor` | Insight/optional; `facility_scale` | Seen whole, the floor is vast — ten storeys of soilless fields meant to feed a city, lit and circulating and immaculate, and entirely dead. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `control_room` / `systems_engineer` | Required; `hardware_to_spec` | The engineer walks you through the operational history: dosing to the gram, pumps at pressure, temperature held, every setpoint he designed met to the final hour. | `start → logs` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `control_room` / `query_systems` | Required; `consortium_crash` | The system logged its living loop as well as its machinery, and the two traces tell the whole story: the microbial consortium in the biofilter held steady for fifty-eight days, then collapsed… | `start → microbes → reveal` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `control_room` / `review_records` | Insight/optional; `trigger_event` | The maintenance log holds the trigger, buried under 'within tolerance': in the days before the collapse a sanitizer flush, a pH dip, a warm spell from a cycling chiller — none of… | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `press_briefing` / `facility_spokesperson` | Required; `false_verdict` | The spokesperson will tell the cameras the failure was human error — a flawed nutrient-cycling design, a named engineer, tighter oversight to come — because it is the version investors can act… | `start → finding` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `press_briefing` / `query_archive` | Insight/optional; `regulatory_stakes` | The forward trace lays two futures side by side. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `press_briefing` / `press_records` | Insight/optional; `public_record` | The media archive runs the whole arc: the ribbon-cutting eighteen months ago — 'The Farm That Feeds the City,' a mayor, schoolchildren with seedlings — to the timelapse of the building browning… | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The farm was not killed by human error or by any failure of its machinery.

**Distractors / false records:**
- The failure was human error: the nutrient-cycling system was flawed as it was designed, and the engineer who built it is to blame.
- The nutrient solution was simply wrong — the formula was mis-mixed or a key nutrient ran dry, and the crops starved of nitrogen.

#### C. Historical/scientific truth and source-status boundary

2041 facility and institutional events are fictional. Nitrification is real; the game simplifies microbial diversity and nitrogen uptake/toxicity chemistry.

**Relevant finding IDs:** `HHH-GAME-C1L6-001`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Distinguish hardware performance from failure of a biological nitrogen-cycling subsystem and evaluate how an institution can misattribute a complex system failure.
- **Principal reasoning operation:** systems causation + evidence audit + accountability.
- **What students genuinely reason about:** Students must combine plant symptoms, chemistry, engineering logs, microbial evidence, and public claims to reject both “hardware broke” and “recipe was simply wrong.”
- **Likely stumbling point:** Assuming “all hardware in spec” means the whole farm is healthy; treating nitrate as the only plant-usable nitrogen form or the microbial consortium as exactly two universal species.
- **Candidate evidence-processing structure:** systems trace comparison + competing explanations + source/audit table.
- **Useful vocabulary:** nitrification, biofilter, microbial consortium, ammonium, ammonia, nitrite, nitrate, system boundary.
- **Candidate source/provenance task:** Compare machine logs with biological/chemical evidence and the public verdict; ask what each source measures and what it leaves invisible.
- **Chronology/map/data opportunity:** Deterministic nitrogen-cycle control-loop schematic and time/event log; fictional values must be labeled as fictional case data.
- **Possible synthesis/explanation product:** Explain how a living subsystem can fail while engineered hardware remains within specification.
- **Plausible transfer/exit question:** What monitoring would detect biological nitrification failure before visible crop collapse?
- **No-game fallback:** Fiction-labeled vertical-farm dossier with system diagram, chemistry trend cards, and public-record comparison.
- **Standalone lesson:** YES as a fictional future systems-history case with science qualifications.
- **Accessibility concern:** Dense systems vocabulary and multiple nitrogen forms; accessible edition should prestructure the pathway rather than require repeated free writing.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D3.2.6-8; CCSS RH.6-8.7
- **Supporting:** C3 D2.His.14.6-8; CCSS WHST.6-8.2
- **Contextual:** NGSS ecosystem/nitrogen-cycle and engineering systems concepts supporting only

### C1 Level 7 — Home / Campaign 1 Finale

**Runtime identity:** `L7` · `The Temporal Agricultural Archive` · 2387 · home, at the end of the thread  
**Runtime source:** `hhh_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `READY_AS_SYNTHESIS_NOT_CORE_CASE`

#### A. Runtime / completion integrity

- Sources: **4**; runtime-required non-insight clues: **2**; runtime-insight clues: **2**.
- Location gates: `briefing_chamber_return` (open); `grove_viewing` ← `nova_speaks_of_it`.
- Completion: Special finale stabilization: collect two required finale clues, return to grove anchor, stabilize/close the record; no ordinary diagnosis.
- Approximate direct-route reading burden: **463 words** by the audit measurement method.
- Static analyzer issues for the generic `companion` source are a known false positive caused by dynamic companion construction; manual inspection overrides the parser warning.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `briefing_chamber_return` / `nova` | Required; `nova_speaks_of_it` | Nova: the chain held, every link. | `start → held → the_plant` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `briefing_chamber_return` / `companion` | Insight/optional; `companion_present` | (runtime source has no static learned summary; dynamic content) | `dynamic/runtime branch` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `briefing_chamber_return` / `taa_archive` | Insight/optional; `chain_intact` | Archive: the human chain is whole — six moments from the first chosen seed to a grove between the stars, every link stabilized. | `start` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `grove_viewing` / `observe_grove` | Required; `witnessed_growth` | You witnessed it: a small new growth in the grove, grown from the connection between species — answering nothing in any record. | `start → closer` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** special orientation/finale action rather than a standard diagnosis.

#### C. Historical/scientific truth and source-status boundary

Entire finale setting is fictional; historical claims should be sourced back to the earlier cases rather than to finale dialogue.

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Synthesize the idea that agricultural knowledge accumulates through preserved records and human choices across the campaign.
- **Principal reasoning operation:** cross-case synthesis + continuity/change.
- **What students genuinely reason about:** The value is retrospective: students connect earlier cases into a long chain rather than solve a new independent historical problem.
- **Likely stumbling point:** Treating finale lore as new historical evidence or expecting another diagnosis when runtime intentionally removes one.
- **Candidate evidence-processing structure:** campaign synthesis / continuity map / reflection.
- **Useful vocabulary:** continuity, change, record, stewardship, historical memory.
- **Candidate source/provenance task:** Trace one idea or practice from two earlier cases and explain how the finale reframes it.
- **Chronology/map/data opportunity:** Cross-case chronology/continuity rail; no fabricated historical source is needed.
- **Possible synthesis/explanation product:** Short synthesis argument about what is gained by preserving agricultural records.
- **Plausible transfer/exit question:** Which earlier case most changed what later societies could know or do, and what evidence supports that judgment?
- **No-game fallback:** Campaign evidence recap cards plus finale excerpt.
- **Standalone lesson:** NO — strongest as a Campaign 1 debrief/synthesis, not an independent case.
- **Accessibility concern:** Depends on prior story and case memory; provide thumbnails/brief evidence recaps rather than require recall.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D2.His.2.6-8; CCSS WHST.6-8.1
- **Supporting:** CCSS RH.6-8.1
- **Contextual:** none proposed at audit stage.

### C2 Level 0 — Archive Audit / Forged Record

**Runtime identity:** `C2L0` · `The Audit` · 2387 · TAA Facility  
**Runtime source:** `hhh_campaign_2_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `GAME_REMEDIATION_REQUIRED`

#### A. Runtime / completion integrity

- Sources: **4**; runtime-required non-insight clues: **4**; runtime-insight clues: **0**.
- Location gates: `briefing_chamber` (open); `thread_console` ← `audit_briefed`.
- Completion: Standard evidence gate: all 4 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **545 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `briefing_chamber` / `nova` | Required; `audit_briefed` | Nova: the audit found a second corruption layer beneath your own repairs. | `start → findings → deliberate → task` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `briefing_chamber` / `zelketh` | Required; `audit_current` | Zel'keth: the flagged nodes are not random — every one sits where agricultural knowledge crossed a boundary. | `start → pattern` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `briefing_chamber` / `audit_log` | Required; `audit_logged` | Audit log: the buried layer reads non-random and expert — five nodes, one hand. | `disfavoredStart → start → signature` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `thread_console` / `memo_pair` | Required; `memo_examined` | The memo pair: the genuine report keeps your amendments — a re-logged timestamp, a crossed-out coordinate. | `disfavoredStart → start → compare` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> Copy B — the working report: a re-logged timestamp, a corrected grain count, one crossed-out coordinate.

**Distractors / false records:**
- Copy A — the pristine report: no amendments, immaculate custody, your signature clean on every page.
- Neither — both copies are forgeries, planted to discredit the audit itself.

#### C. Historical/scientific truth and source-status boundary

Mabillon/diplomatics are real; the TAA audit and memo pair are fictional. Cleanliness/corrections are clues at most, not authenticity tests by themselves.

**Relevant finding IDs:** `HHH-GAME-C2L0-001`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Evaluate authenticity by comparing provenance, transmission, discrepancies, and corroboration rather than treating surface neatness as proof of forgery.
- **Principal reasoning operation:** source criticism + provenance + corroboration.
- **What students genuinely reason about:** Students must decide between records using a chain of evidence; the central historical skill is validating a record, not copying a suspicious feature.
- **Likely stumbling point:** Believing one “too clean” document is automatically forged or that working records must always contain corrections.
- **Candidate evidence-processing structure:** record comparison + provenance chain + authenticity argument.
- **Useful vocabulary:** diplomatics, provenance, authenticity, integrity, transmission, corroboration.
- **Candidate source/provenance task:** Compare audit testimony, logging metadata, and two record copies; identify independent indicators and rank their evidentiary weight.
- **Chronology/map/data opportunity:** Provenance relationship diagram with documented/inferred labels and exact change log.
- **Possible synthesis/explanation product:** Argument for which record is better supported, with explicit statement that no single cosmetic feature proves authenticity.
- **Plausible transfer/exit question:** What additional evidence would most increase or decrease confidence that a suspicious record is authentic?
- **No-game fallback:** Four-record dossier reproducing the game’s audit log/memo comparison, plus a short real-world diplomatics/provenance reference.
- **Standalone lesson:** YES after the “too clean” heuristic is corrected.
- **Accessibility concern:** Students may overfocus on formatting differences; organizer should force multiple-source corroboration.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D3.1.6-8; C3 D3.2.6-8; CCSS RH.6-8.6; CCSS RH.6-8.9
- **Supporting:** CCSS WHST.6-8.1
- **Contextual:** none proposed at audit stage.

### C2 Level 1 — Tenochtitlan / Chinampas

**Runtime identity:** `C2L1` · `The Floating Gardens` · 1487 · Tenochtitlan  
**Runtime source:** `hhh_campaign_2_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `READY_WITH_TEACHER_QUALIFICATION`

#### A. Runtime / completion integrity

- Sources: **7**; runtime-required non-insight clues: **4**; runtime-insight clues: **3**.
- Location gates: `chinampa_field` (open); `lake_causeway` ← `gardens_thriving`; `codex_house` ← `salinity_engineered`.
- Completion: Standard evidence gate: all 4 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **460 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `chinampa_field` / `farmer` | Required; `gardens_thriving` | Xochitl: the plots yield several harvests a year and never rest — canal mud re-laid each season feeds them continuously. | `start → yields` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `chinampa_field` / `soil` | Required; `soil_alive` | The plot soil is layered lake mud and green matter, actively cycling nutrients. | `start → probe` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `lake_causeway` / `waterworks` | Required; `salinity_engineered` | The lake is managed: a long dike and gated sluices hold the brackish eastern water apart from the spring-fed west. | `start → overlay` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `lake_causeway` / `canoes` | Insight/optional; `surplus_seen` | Insight: an unbroken stream of canoes hauls produce toward the city markets — the surplus of a system that feeds a capital, not one collapsing. | `start` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `codex_house` / `codex` | Required; `harvest_counted` | The harvest codex: plot-by-plot, season-by-season counts, generations deep — the same named gardens, yielding steadily, in an unbroken painted record. | `start → crossref` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `codex_house` / `keeper` | Insight/optional; `keeper_heard` | Insight: the tlacuilo counts every harvest three times — field, canoe, and market — and paints only what agrees. | `start → method` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `codex_house` / `collapse_record` | Insight/optional; `collapse_read` | Insight: the collapse account is beautifully made and cites nothing — no plot names, no seasons, no keepers. | `disfavoredStart → start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The Harvest Codex — named plots, counted seasons, generations of tallies from the same living gardens, still rising.

**Distractors / false records:**
- The Collapse Account — salt crept into the plots, the canals fouled, and the gardens farmed the valley to death.
- The Untouched Lake — the valley’s waters never suffered at all; the gardens were simply perfect, forever.

#### C. Historical/scientific truth and source-status boundary

Chinampas are historical; exact 1487 characters, codex entries, and TAA interactions are game reconstructions. “Floating gardens” is a conventional but potentially misleading label.

**Relevant finding IDs:** `HHH-GAME-C2L1-001`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Explain chinampas as an engineered wetland/raised-field agricultural system integrating canals, soil renewal, intensive cultivation, and hydrologic management, while evaluating the source status of the game’s records.
- **Principal reasoning operation:** geographic reasoning + systems/contextualization + source limitation.
- **What students genuinely reason about:** Students must integrate soil, waterworks, harvest records, and testimony rather than treat “floating gardens” as a literal construction description.
- **Likely stumbling point:** Imagining chinampas as floating rafts or treating the game’s codex/keeper dialogue as literal surviving Aztec primary records.
- **Candidate evidence-processing structure:** sourced map + agroecosystem diagram + source-status comparison.
- **Useful vocabulary:** chinampa, raised field, canal, dike/causeway, salinity, intensive agriculture, agrobiodiversity.
- **Candidate source/provenance task:** Compare physical-system evidence with the in-game codex and oral testimony; flag what requires external historical corroboration.
- **Chronology/map/data opportunity:** Sourced Basin of Mexico/Tenochtitlan map and chinampa cross-section; clearly label reconstructed features.
- **Possible synthesis/explanation product:** Explain how chinampas manage water/soil and support intensive production without calling them literal floating islands unless the source uses that conventional nickname.
- **Plausible transfer/exit question:** Which physical feature addresses water, soil fertility, or salinity, and what source would verify that historical use?
- **No-game fallback:** FAO/archaeological secondary-source excerpts, sourced map, and a clearly reconstructed chinampa schematic.
- **Standalone lesson:** YES with Teacher qualification on terminology/source status.
- **Accessibility concern:** Spatial system is easier with a cross-section and map; avoid dense prose-only treatment.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D2.His.1.6-8; C3 D3.2.6-8; CCSS RH.6-8.7
- **Supporting:** CCSS RH.6-8.9; CCSS WHST.6-8.2
- **Contextual:** none proposed at audit stage.

### C2 Level 2 — Leningrad / Seed Bank

**Runtime identity:** `C2L2` · `The Seeds They Kept` · 1941 · Leningrad  
**Runtime source:** `hhh_campaign_2_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `GAME_REMEDIATION_REQUIRED`

#### A. Runtime / completion integrity

- Sources: **6**; runtime-required non-insight clues: **5**; runtime-insight clues: **1**.
- **Important exception:** `siege_witnessed` is tagged `insight:true` but gates `seed_vault`; effective direct play therefore requires it. This is a semantics/authoring defect even though the route remains playable.
- Location gates: `besieged_street` (open); `seed_vault` ← `siege_witnessed`; `institute_office` ← `keeper_testimony`.
- Completion: Standard evidence gate: all 5 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **587 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `besieged_street` / `street` | **Gate-required despite `insight:true`**; `siege_witnessed` | Insight: the city is starving — the bread ration is 125 grams. | `start` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `seed_vault` / `keeper` | Required; `keeper_testimony` | Dr. | `start → testimony` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `seed_vault` / `collection` | Required; `collection_intact` | The collection is intact: pre-war seals unbroken, counts matching the catalogue, seed aged in place through the siege winters. | `start → scan` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `institute_office` / `ledger` | Required; `accessions_continuous` | The ledger runs unbroken through the siege. | `start → crossref` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `institute_office` / `vavilov` | Required; `vavilov_fate` | The recovered record: Vavilov was arrested in August 1940 and died in prison in January 1943. | `start → fate` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `institute_office` / `report` | Required; `report_read` | The Consumption Report: typed, complete, materially perfect — staff 'consumed the collections under emergency authorization, witnessed by Director Vavilov at the Institute.' Its perfection, and that signature, are the tells. | `disfavoredStart → start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The Keeper's Record — the collection intact through the siege; the staff who starved rather than eat it, named and mourned.

**Distractors / false records:**
- The Rationed Collection — the staff ate some accessions to survive and preserved the rest.
- The Consumption Report — under emergency authorization, the collections were consumed; the post-war bank was rebuilt later.

#### C. Historical/scientific truth and source-status boundary

Siege, collection, Vavilov arrest/death, and preservation are historical. Individual dialogue is reconstructed; published counts of staff deaths vary by source/definition.

**Relevant finding IDs:** `HHH-IMP-C2L2-001`, `HHH-GAME-C2L2-001`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Explain why preserving crop genetic diversity during the Siege of Leningrad mattered and evaluate testimony, accession continuity, and later reports as evidence for what happened to the collection.
- **Principal reasoning operation:** provenance + continuity/change + ethical historical reasoning.
- **What students genuinely reason about:** Students must corroborate a dramatic story with collection continuity and records; heroic testimony alone cannot establish every count or detail.
- **Likely stumbling point:** Treating one legendary death count as universally settled, or assuming Vavilov himself was present during the siege.
- **Candidate evidence-processing structure:** siege timeline + accession/provenance chain + corroboration matrix.
- **Useful vocabulary:** accession, germplasm, seed bank, siege, ex situ conservation, provenance, collection continuity.
- **Candidate source/provenance task:** Use ledger continuity, collection examination, testimony, Vavilov’s fate, and post-event reporting to test competing archival claims.
- **Chronology/map/data opportunity:** 1940–1944 timeline distinguishing Vavilov’s arrest/death from siege events; provenance/collection continuity diagram.
- **Possible synthesis/explanation product:** Evidence-based explanation of how the collection was preserved and why exact heroic-story details require source qualification.
- **Plausible transfer/exit question:** What evidence best demonstrates that a collection after a crisis is continuous with the pre-crisis collection rather than rebuilt from scratch?
- **No-game fallback:** VIR/Crop Trust source excerpts, accession-chain diagram, siege timeline, and game testimony clearly labeled as reconstructed.
- **Standalone lesson:** YES after the `insight`/gate semantics defect is fixed or explicitly normalized.
- **Accessibility concern:** Emotional content and many record types; timeline should make Vavilov’s absence and staff actions distinct.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D3.1.6-8; C3 D3.2.6-8; CCSS RH.6-8.9
- **Supporting:** C3 D2.His.1.6-8; CCSS WHST.6-8.1
- **Contextual:** none proposed at audit stage.

### C2 Level 3 — Green Revolution / Mexico and South Asia

**Runtime identity:** `C2L3` · `The Quiet Billion` · 1968 · Mexico  
**Runtime source:** `hhh_campaign_2_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `READY_WITH_TEACHER_QUALIFICATION`

#### A. Runtime / completion integrity

- Sources: **6**; runtime-required non-insight clues: **4**; runtime-insight clues: **2**.
- Location gates: `trial_plots` (open); `research_station` ← `lodging_resistance`; `deployment_field` ← `pedigree_verified`.
- Completion: Standard evidence gate: all 4 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **516 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `trial_plots` / `borlaug` | Required; `trials_succeeded` | The recovered record: Borlaug bred the wheat SHORT on purpose — a stiff dwarf straw that stands under a heavy, well-fed head instead of falling. | `start → trait` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `trial_plots` / `wheat` | Required; `lodging_resistance` | The short-strawed wheat stands under the same heavy head that flattens the tall wheat beside it. | `start → scan` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `research_station` / `pedigree` | Required; `pedigree_verified` | The variety pedigree runs unbroken from the dwarf parent to the seed going out by the ton, every cross dated and the recorded yields RISE across seasons in both Mexico and South… | `start → crossref` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `research_station` / `report` | Insight/optional; `forgery_read` | Insight: the buried 'trial failure' report is professionally forged — real letterhead, yet it describes the wheat being abandoned, and recommends the seed stock be destroyed. | `disfavoredStart → start` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `deployment_field` / `agronomist` | Required; `real_yields` | Dr. | `start → yields` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `deployment_field` / `survey` | Insight/optional; `harvest_scale` | Insight: the new crop runs to the horizon in every direction — one variety, one height, heavy-headed, standing. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The Trial Record — the semi-dwarf varieties stood, resisted lodging and rust, and drove rising harvests across Mexico and South Asia.

**Distractors / false records:**
- The Failure Report — the semi-dwarf trials lodged and were quietly abandoned; the green revolution was a buried disaster.
- The Reckoning — the wheat worked, but the green revolution was an ecological and social catastrophe not worth keeping in the record.

#### C. Historical/scientific truth and source-status boundary

Borlaug, Mexican research, semi-dwarf wheat, and South Asian adoption are historical; exact game dialogue/yield numbers and forged record are constructed for gameplay.

**Relevant finding IDs:** `HHH-GAME-C2L3-001`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Evaluate Green Revolution claims using experimental results, pedigree, lodging/rust traits, yield evidence, and broader production context rather than accepting either triumphalist or wholly dismissive records.
- **Principal reasoning operation:** corroboration + quantitative evidence + cause/consequence + competing interpretation.
- **What students genuinely reason about:** Students must test a forged/oversimplified account against independent trial, pedigree, and field evidence and separate varietal effects from the larger technology/input system.
- **Likely stumbling point:** Reducing yield changes to one seed variety alone, or treating popular “saved a billion lives” language as a directly measurable case fact.
- **Candidate evidence-processing structure:** claim-evidence audit + before/after data interpretation + provenance check.
- **Useful vocabulary:** semi-dwarf, lodging, rust resistance, pedigree, yield, Green Revolution, input package.
- **Candidate source/provenance task:** Compare trial evidence, pedigree, field testimony/data, and the optional forged report; identify what each supports and what remains contextual.
- **Chronology/map/data opportunity:** Sourced Mexico → South Asia map, 1940s–1960s timeline, and sourced yield data where used.
- **Possible synthesis/explanation product:** Qualified explanation of how improved varieties contributed to yield gains alongside irrigation, fertilizer, agronomy, institutions, and policy.
- **Plausible transfer/exit question:** What additional evidence would separate the effect of the variety from fertilizer, irrigation, or policy changes?
- **No-game fallback:** Nobel/CIMMYT-style secondary sources plus sourced trial/yield excerpts and a labeled fictional forgery record.
- **Standalone lesson:** YES with contextual qualification.
- **Accessibility concern:** Quantitative and causal complexity; accessible edition should model one claim-evidence comparison and reduce repetitive rows.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D3.2.6-8; CCSS RH.6-8.7; CCSS RH.6-8.8
- **Supporting:** C3 D2.His.14.6-8; CCSS WHST.6-8.1
- **Contextual:** none proposed at audit stage.

### C2 Level 4 — Concord / Karreth Bloom

**Runtime identity:** `C2L4` · `The Bloom That Needed Poison` · 2301 · Concord space  
**Runtime source:** `hhh_campaign_2_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `READY_WITH_QUALIFICATION_AND_DOC_FIX`

#### A. Runtime / completion integrity

- Sources: **6**; runtime-required non-insight clues: **4**; runtime-insight clues: **2**.
- Location gates: `karreth_vault` (open); `transit_corridor` ← `vault_starved`; `regulation_office` ← `diagnosis_recovered`.
- Completion: Standard evidence gate: all 4 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **484 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `karreth_vault` / `bloom` | Required; `bloom_failing` | The karreth bloom is dying in a flawless vault. | `start → scan` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `karreth_vault` / `telemetry` | Required; `vault_starved` | The vault holds ambient radiation at ZERO — the Universal Shielding Protocol scrubs it flawlessly. | `start → crossref` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `transit_corridor` / `nova` | Required; `diagnosis_recovered` | A recovered archive of Dr. | `start → diagnosis` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `transit_corridor` / `viewport` | Insight/optional; `station_scale` | Insight: through the corridor viewport, the Concord station sprawls across deep space — docking arms, habitat rings, ships of a dozen species moving between them. | `start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `regulation_office` / `regulator` | Required; `protocol_ratified` | Regulator Vess administered the Universal Shielding Protocol — and states plainly that after the karreth was diagnosed, the Protocol was AMENDED to grant the bloom a formal exemption. | `start → amended` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `regulation_office` / `ratification` | Insight/optional; `ratification_examined` | Insight: the buried record is a formal ratification of the Universal Shielding Protocol as PERMANENT and universal — dated before the karreth diagnosis, and containing no exemption at all. | `disfavoredStart → start` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The Diagnosis Record — the bloom was starving under the universal Protocol; it was found to require radiation, and the Protocol was amended to grant a karreth bloom exemption.

**Distractors / false records:**
- The Ratification Record — the Universal Shielding Protocol was ratified permanent and universal before any diagnosis; no exemption was ever needed or made.
- The Falsified Exemption — the bloom's own keepers fabricated the radiation diagnosis to win themselves an exemption from Concord safety law.

#### C. Historical/scientific truth and source-status boundary

Karreth, Concord, and protocol history are fictional. Melanized-fungus radiation responses are real research, but “gamma radiation converted into usable metabolic energy” remains a hypothesis/interpretation rather than settled equivalent biology.

**Relevant finding IDs:** `HHH-DOC-C2L4-001`, `HHH-GAME-C2L4-001`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Practice archival/source reasoning in a clearly fictional case where a universal safety rule harms an organism with different requirements, while separating the fictional mechanism from real analogies about radiation-tolerant life.
- **Principal reasoning operation:** competing interpretation + policy revision + source-status reasoning.
- **What students genuinely reason about:** Students must use telemetry, recovered diagnosis, and ratification history to decide whether the policy record was amended and why.
- **Likely stumbling point:** Treating karreth biology as real Earth history or treating fungal “radiosynthesis” as a settled, direct analogue.
- **Candidate evidence-processing structure:** source-status matrix + policy chronology + competing-record evaluation.
- **Useful vocabulary:** protocol, ratification, exemption, symbiosis, ionizing radiation, source status, analogy.
- **Candidate source/provenance task:** Distinguish fictional direct evidence about karreth from real-world scientific analogy; evaluate policy records separately from biological claims.
- **Chronology/map/data opportunity:** Deterministic fictional protocol timeline plus explicitly FICTIONAL VISUALIZATION organism/system diagram.
- **Possible synthesis/explanation product:** Explain why the fictional protocol was revised using in-world evidence, then separately state the limits of Earth-life analogies.
- **Plausible transfer/exit question:** When can a real scientific analogy support interpretation of a fictional system, and when does it become overclaiming?
- **No-game fallback:** Fully fiction-labeled dossier with protocol records and a short real-source sidebar on melanized fungi/radiation tolerance.
- **Standalone lesson:** CONDITIONAL — strong source-reasoning lesson if fictional status is foregrounded.
- **Accessibility concern:** Two truth layers (in-world truth and real-world science) can blur; use explicit status labels on every source/figure.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D3.2.6-8; CCSS RH.6-8.8
- **Supporting:** C3 D2.His.14.6-8; CCSS WHST.6-8.1
- **Contextual:** Radiobiology is analogy/context, not direct historical evidence

### C2 Level 5 — First Garden / Mycorrhizal Record

**Runtime identity:** `C2L5` · `The Living Record` · 2387 · First Garden, Earth  
**Runtime source:** `hhh_campaign_2_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `GAME_REMEDIATION_REQUIRED`

#### A. Runtime / completion integrity

- Sources: **6**; runtime-required non-insight clues: **5**; runtime-insight clues: **1**.
- Location gates: `terraced_garden` (open); `soil_zone` ← `garden_ailing`; `summit_pavilion` ← `network_severed`.
- Completion: Standard evidence gate: all 5 non-insight required clues → return to anchor → choose among 3 final records/diagnoses (1 runtime-correct).
- Approximate direct-route reading burden: **782 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `terraced_garden` / `nova` | Required; `garden_ailing` | Dr. | `start → ailing` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `soil_zone` / `mycorrhizal` | Required; `network_severed` | A TAA scan of the terrace edge finds the cause the surface hides. | `start → scan` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `soil_zone` / `kess` | Required; `fungal_named` | Delegate Kess — a preserved mind of a species that left soil-farming a thousand generations ago but carries a fragmented ancestral sense for it, kept alive in a sensing-vessel whose filaments read… | `start → names` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `summit_pavilion` / `shael` | Required; `chemistry_islands` | Delegate Vorn-Shael — a chemist, pure observation. | `start → maps` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `summit_pavilion` / `liverecord` | Required; `live_forgery` | The summit display shows the record forming in real time — and a second version overwriting it as you watch. | `disfavoredStart → start` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |
| `summit_pavilion` / `ilreth` | Insight/optional; `skeptic_convinced` | Insight: Delegate Ilreth-Mar came to the summit a reform skeptic — to observe and, they expected, to record that cross-species knowledge-sharing does not work. | `start` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |

**Runtime final reasoning:** the correct resolution must integrate the required evidence, not reproduce one clue. Runtime-correct choice:

> The Living Diagnosis — the mycorrhizal network was severed between the terraces; cross-zone inoculation from mature ground restores it; three species read it together and the garden can heal.

**Distractors / false records:**
- The Inconclusive Summit — the delegates’ alien methods proved incompatible with Earth soil; no fix was found; the garden’s decline is natural and beyond cross-species help.
- A Routine Revision — nothing is being erased; the record is simply updating itself as new data arrives, the ordinary way any live document corrects in real time.

#### C. Historical/scientific truth and source-status boundary

First Garden and its severing/inoculation event are fictional. Mycorrhizal symbiosis is established; common-network resource/signal transfer exists in some systems but broad forest-wide claims are actively debated. Direct fossil evidence is ~407 Ma, not a precise 450-Ma observation.

**Relevant finding IDs:** `HHH-GAME-C2L5-001`, `HHH-GAME-C2L5-002`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Evaluate a biological/historical claim by separating direct observation of mycorrhizal symbiosis, fossil evidence, inferred network function, debated common-mycorrhizal-network claims, and the fictional First Garden mechanism.
- **Principal reasoning operation:** source contribution/limitation + contested interpretation + documented/inferred/fictional status.
- **What students genuinely reason about:** Students must decide which claims are directly observed, which are supported in some systems, which remain contested/generalized, and which exist only inside the game.
- **Likely stumbling point:** Treating the popular “wood-wide web” idea—one network moving water, nutrients, and warning signals among essentially all plants—as a settled universal mechanism.
- **Candidate evidence-processing structure:** documented/inferred/fictional status table + evidence-convergence/limitation analysis.
- **Useful vocabulary:** mycorrhiza, hyphae, symbiosis, arbuscular mycorrhiza, common mycorrhizal network, inference, fossil evidence.
- **Candidate source/provenance task:** Compare the game scan/testimony/chemistry with peer-reviewed sources that disagree about how broadly CMN transfer claims can be generalized.
- **Chronology/map/data opportunity:** Evidence-status convergence diagram: established symbiosis → fossil evidence → contested network-transfer claims → fictional First Garden mechanism.
- **Possible synthesis/explanation product:** Qualified claim distinguishing “mycorrhizal symbiosis is ancient and widespread” from stronger interplant sharing/signaling claims.
- **Plausible transfer/exit question:** Which statement is directly documented, which is inferred, and what new evidence would be required to support the strongest network claim?
- **No-game fallback:** Peer-reviewed pro/con CMN excerpts, 407-Ma fossil source, and fully FICTIONAL CONTEXT game evidence packet.
- **Standalone lesson:** YES after game science is corrected/qualified; potentially one of the strongest HHH source-status lessons.
- **Accessibility concern:** Requires students to hold several confidence/status categories at once; use explicit labels and reduce repeated prose.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D3.2.6-8; CCSS RH.6-8.8; CCSS RH.6-8.9
- **Supporting:** CCSS WHST.6-8.1
- **Contextual:** Life-science symbiosis/evolution supports the source-reasoning task

### C2 Level 6 — ARS Chamber / Campaign 2 Finale

**Runtime identity:** `C2L6` · `The Source` · 2389 · Concord space, the ARS Chamber  
**Runtime source:** `hhh_campaign_2_data.js` @ `9b8545ed6ecf98b337326390400076e36789e056`  
**Audit disposition:** `MINOR_GAME_UPDATE_AND_OWNER_CASE_DECISION_REQUIRED`

#### A. Runtime / completion integrity

- Sources: **7**; runtime-required non-insight clues: **5**; runtime-insight clues: **2**.
- Location gates: `archive_return` (open); `thread_console` ← `trace_followed`; `ars_chamber` ← `study_identified`.
- Completion: Special confrontation: collect five required clues, return to ARS Chamber, confront source, then choose one of three value/record outcomes; no academically unique “correct” moral choice.
- Approximate direct-route reading burden: **724 words** by the audit measurement method.

#### B. Evidence architecture

| Location / source | Runtime status | Evidence contribution | Direct reveal route | What it cannot establish alone |
|---|---|---|---|---|
| `archive_return` / `nova` | Required; `trace_followed` | Dr. | `start → trace` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `archive_return` / `zelketh` | Insight/optional; `concord_shadow` | Zel'keth's counsel: whatever is at the end of the trace operates INSIDE Concord officialdom — chartered, funded, procedurally clean. | `start → inside` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `thread_console` / `trace_scan` | Required; `reachback_mapped` | The write-path, mapped. | `start → scan` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `thread_console` / `charter_query` | Required; `study_identified` | The credentials resolve. | `start → charter` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `ars_chamber` / `evidence_dais` | Required; `works_assembled` | The Study's own display: all five forgeries, hung in holographic array beside the severed thread-diagrams of the chain — Tenochtitlan, Leningrad, the Green Revolution, the karreth vault, the First Garden. | `start → works` | In-game record/provenance evidence; chronology or transmission still requires authenticity/context corroboration. |
| `ars_chamber` / `ars_delegate` | Required; `thesis_heard` | The Study's delegate, in their own words: cross-species agricultural exchange is an existential hazard — when biospheres teach each other to farm, they contaminate each other, and the long arc ends in… | `start → thesis → conviction` | In-game testimony/perspective; cannot alone establish system-wide prevalence, authenticity, motive, or causation. |
| `ars_chamber` / `viewport` | Insight/optional; `quarantine_seen` | Virel, seen with your own eyes: a quarantined world, ninety years silent, its farmlands dead of a blight that crossed during an early cross-species seed exchange. | `start → virel` | In-game observation/analysis of a local case state; cannot by itself establish broader historical generalization or external real-world truth. |

**Runtime final reasoning:** no single factual diagnosis. The confrontation deliberately presents three final archival/value choices; curriculum assessment must score evidence use and reasoning rather than keying one moral answer.

#### C. Historical/scientific truth and source-status boundary

ARS, Virel, Concord politics, and all three choices are fictional. The Svalbard analogy is real but its sample count is time-sensitive.

**Relevant finding IDs:** `HHH-GAME-C2L6-001`

#### D. Curriculum-readiness planning evidence

- **Strongest central learning goal:** Synthesize provenance, evidence, uncertainty, and archive ethics when competing interpretations cannot be reduced to a single academically correct moral verdict.
- **Principal reasoning operation:** cross-case synthesis + argumentation + archive ethics + competing values.
- **What students genuinely reason about:** Students must assemble prior evidence, represent the opposing thesis fairly, and justify a record-keeping decision without pretending one moral choice is factually mandated.
- **Likely stumbling point:** Treating one of the three finale choices as the teacher’s “correct answer,” or confusing fictional conspiracy evidence with real archival history.
- **Candidate evidence-processing structure:** capstone argument / competing-values deliberation / evidence ledger.
- **Useful vocabulary:** archive ethics, disclosure, quarantine, stewardship, provenance, uncertainty, public record.
- **Candidate source/provenance task:** Trace the final thesis back to earlier case records and identify which claims are established in-world, contested in-world, or purely value judgments.
- **Chronology/map/data opportunity:** Cross-campaign evidence/provenance map; optional decision matrix that keeps evidence separate from values.
- **Possible synthesis/explanation product:** Evidence-based capstone argument with no single keyed moral verdict; scoring should assess use of evidence, counterargument, and source precision.
- **Plausible transfer/exit question:** When an archive cannot settle a contested policy question, what does it still owe future users of the record?
- **No-game fallback:** Assembled cross-case dossier plus finale excerpts and an explicit rubric that scores reasoning rather than choice.
- **Standalone lesson:** NO as a normal case; CONDITIONAL as a formal capstone after prior cases.
- **Accessibility concern:** Very high prior-knowledge burden; provide case recaps and avoid requiring memory of lore names to demonstrate historical reasoning.

#### E. Candidate standards homes — planning only

- **Directly Assessed:** C3 D4.1.6-8; CCSS WHST.6-8.1
- **Supporting:** C3 D3.2.6-8; CCSS RH.6-8.1
- **Contextual:** none proposed at audit stage.

## 6. Historical/scientific and game-text findings register

| ID | Register class | Severity | Finding | Exact location / evidence | Recommended disposition |
|---|---|---|---|---|---|
| HHH-SYS-001 | Shared-system/readiness | Moderate | Curriculum registry display title is stale: `History's Harvest` rather than canonical *Hunger, Harvest, & History*. | `shared/implementation/case-registry.v2.json` @ curriculum SHA | Correct before first HHH package registration/release; does not block Blueprint. |
| HHH-SYS-002 | Shared-system/readiness | Expected pre-production gap | HHH registry entry has `campaigns: []`; no HHH campaign/case packages are registered yet. | same registry | Populate only after Blueprint/case architecture is approved; not a defect in the game. |
| HHH-IMP-C2L2-001 | Game correction before affected case | Major implementation semantics | `siege_witnessed` is marked `insight:true` but `seed_vault` requires that clue, making an “optional” insight structurally mandatory. | `hhh_campaign_2_data.js:834–858` | Either mark the clue required or remove the gate; keep intended street-first flow explicit and test completion semantics. |
| HHH-DOC-C2L4-001 | Nonblocking polish / documentation | Moderate | README describes Campaign 2 as including “radiation hormesis,” while shipped C2 L4 is the fictional karreth-bloom/protocol case. | `README.md:54` vs shipped C2 L4 | Synchronize README to runtime before curriculum extraction. |
| HHH-GAME-C1L1-001 | Game correction before affected case | Major historical precision | Exact 9700 BCE vignette presents a single deliberate non-shattering selection event as the beginning of domestication; current archaeobotany supports a long, mosaic process and later gradual rise of non-shattering traits. | C1 L1 runtime + [H1] | Reframe as reconstructed/composite early cultivation/selection scene; avoid claiming a documented first individual/event at 9700 BCE. |
| HHH-GAME-C1L1-002 | Nonblocking polish | Minor | Grammar defect: “In these grain heads they does not shatter…” | `hhh_data.js:490` | Correct grammar before any curriculum quotation. |
| HHH-GAME-C1L2-001 | Game correction before affected case | Major textual integrity | Required clue summary is truncated: “without the old fallow res.” | `hhh_data.js:695` | Restore intended phrase/sentence before case production. |
| HHH-GAME-C1L2-002 | Teacher qualification / optional game softening | Moderate | Salinization mechanism is credible, but wording that implies a uniquely first human-made agricultural crisis or broad decline from one cause overstates historical certainty. | C1 L2 + [H2] | Keep local mechanism; qualify broader historical causation and debated crop-shift interpretation. |
| HHH-GAME-C1L2-003 | Nonblocking polish | Minor | Scribe clue contains broken syntax around “Yet, wrote the cause down…” | C1 L2 `scribe_record` learned text | Repair prose before direct reuse. |
| HHH-GAME-C1L3-001 | Game correction before affected case | Major historical distortion risk | Correct diagnosis/explanation universalizes dependence: “whole country,” “every field was the same plant repeated,” and “nothing else grown to fall back on.” | `hhh_data.js:1067,1070,1076` + [H3][H4] | Retain severe Lumper/dependence vulnerability but remove universals; separate crop disease from famine’s social/political/economic causes. |
| HHH-GAME-C1L4-001 | Nonblocking polish | Minor | Required pressure clue contains typo “Mdeled up…” | `hhh_data.js:1488` | Correct to “Modeled” (or intended wording). |
| HHH-GAME-C1L4-002 | Teacher qualification | Moderate | Temperature wording can sound “gentle/merely warm” despite Haber conditions near ~500 °C; lab Haber and industrial Bosch roles also require distinction. | C1 L4 + [H5][H6] | Use “compromise temperature for this equilibrium/rate tradeoff”; distinguish Haber laboratory synthesis from Bosch scale-up. |
| HHH-GAME-C1L5-001 | Game correction before affected case | Major scientific overstatement | Required/optional evidence describes subsoil as “lifeless,” “will grow nothing,” “biologically dead — no organic matter, no microbial life.” | `hhh_data.js:1861,1885–1890` + [H8] | Replace zero-life/zero-growth language with severe topsoil loss, low organic matter/fertility/biological activity, and greatly reduced crop suitability. |
| HHH-GAME-C1L5-002 | Teacher qualification / optional game softening | Moderate | Correct diagnosis rhetorically opposes drought too strongly; the historical mechanism is drought interacting with exposed/erodible land, not “drought irrelevant.” | C1 L5 + [H7] | Teach interaction of drought + land cover/land use + wind erosion + policy response. |
| HHH-GAME-C1L6-001 | Teacher qualification | Moderate science simplification | Nitrification and microbial-biofilter failure are sound as a model, but the game simplifies microbial diversity and plant nitrogen use/toxicity chemistry. | C1 L6 + [H9] | Keep as fictional systems case; qualify consortium composition and ammonium/ammonia/nitrate language. |
| HHH-GAME-C2L0-001 | Game correction before affected case | Major historical-method overstatement | Fun fact says modern examiners treat “too clean” as a warning because genuine working records accumulate corrections and forgeries rarely do. | `hhh_campaign_2_data.js:439` + [H10][H11] | Replace with multi-factor authenticity rule: unexplained neatness can prompt questions, but form/corrections alone do not prove authenticity or forgery. |
| HHH-GAME-C2L1-001 | Teacher qualification | Moderate terminology/source-status | “Floating Gardens” can be read literally; game codex/keeper testimony is reconstructed rather than a literal surviving 1487 source. | C2 L1 + [H12] | Use “chinampas/raised-field wetland agriculture”; explain conventional “floating gardens” label and mark reconstructed game sources. |
| HHH-GAME-C2L2-001 | Teacher qualification | Minor/Moderate source precision | Popular accounts disagree on exact number/category of institute staff who died protecting the collection; Vavilov himself had been arrested before the siege. | C2 L2 + [H13][H14] | Use sourced, qualified count language; distinguish Vavilov’s fate from siege staff actions. |
| HHH-GAME-C2L3-001 | Teacher qualification | Moderate historical causation | Core semidwarf/lodging/rust story is sound, but exact field-yield claims and any “one seed saved a billion” shorthand should not replace broader irrigation/fertilizer/institutional context. | C2 L3 + [H15] | Treat exact game figures as game evidence unless externally sourced; contextualize Green Revolution as a package of varieties, agronomy, inputs, institutions, and policy. |
| HHH-GAME-C2L4-001 | Teacher qualification / optional game softening | Moderate science precision | Fun fact says melanized fungus “appears to use melanin to convert gamma radiation into usable energy,” which risks presenting “radiosynthesis” as established mechanism. | `hhh_campaign_2_data.js:1690` + [H16] | Describe radiation-associated melanin effects/growth as research evidence and energy-harvesting interpretation/hypothesis, not a settled direct analogue to karreth. |
| HHH-GAME-C2L5-001 | Game correction before affected case | Major scientific precision | Required evidence and explanation assert one mycorrhizal web carries water, nutrients, and chemical signals among plants across the whole slope, and dialogue generalizes this to “every healthy garden.” | `hhh_campaign_2_data.js:1849,1860,1890,2055` + [H17][H18] | Separate fictional First Garden network behavior from established mycorrhizal symbiosis; explicitly label broad interplant transfer/signaling claims as system-dependent/debated. |
| HHH-GAME-C2L5-002 | Game correction before affected case | Moderate chronology/source-status | Fun fact frames “450 million years ago” plant–fungus partnership as if directly fossil-documented; fine-detail arbuscular-mycorrhizal fossil evidence is ~407 Ma, while older origins are inference. | `hhh_campaign_2_data.js:2056` + [H19] | Distinguish direct fossil evidence (~407 Ma) from broader evolutionary inference about earlier land-plant symbioses. |
| HHH-GAME-C2L6-001 | Game correction before affected case | Minor time-sensitive factual drift | Svalbard fun fact says “over 1.2 million” samples; still technically true but stale and likely to age poorly. Official total reached 1,401,285 in June 2026. | `hhh_campaign_2_data.js:2531` + [H20][H21] | Use “more than 1.4 million as of June 2026” with date, or future-proof as “more than one million.” |
| HHH-DEC-001 | Curriculum design decision | Owner/Blueprint | HHH needs a governing synthesis/argument rule: shared Claim–Evidence–Reasoning can be used, but not every HHH lesson should imitate SSS scientific diagnosis/CER structure. | Curriculum Bible + HHH identity rules | Blueprint should define HHH historical argument products and when canonical CER is appropriate. |
| HHH-DEC-002 | Curriculum design decision | Owner/Blueprint | Decide whether C2 L6 is a formal numbered curriculum case or an optional culminating capstone. | Cross-campaign audit | Recommendation: 12 core cases; C2 L6 as capstone unless owner wants 13 formal cases. |
| HHH-DEC-003 | Curriculum design decision | Owner/Blueprint | Decide formal placement of heavily fictional C2 L4 and mixed-fiction C2 L5. | Cross-campaign audit | Recommendation: retain both if source-status reasoning is explicit; C2 L5 must be scientifically remediated first. |
| HHH-DEC-004 | Curriculum design decision / access | Owner/Blueprint | Campaign 2 classroom independence needs a defined no-game/direct-launch strategy because game progression is narratively gated by prior campaign state. | Runtime/menu behavior + shared fallback contract | Blueprint should require complete no-game evidence fallback and define approved classroom launch/save-state method if direct play is expected. |

### Register interpretation

- **Blocker before Blueprint:** none. The authority and structure are stable enough to define HHH architecture.
- **Game corrections before affected case production:** C1 L1, C1 L2, C1 L3, C1 L5, C2 L0, C2 L2 implementation semantics, C2 L5, and the time-sensitive C2 L6 fact; smaller wording fixes should ride the same controlled remediation phase.
- **Teacher qualification only / curriculum boundary:** Sumer broader causation, Haber/Bosch attribution and temperature language, C1 L6 nitrification simplification, chinampa terminology/reconstruction, Leningrad count precision, Green Revolution context, C2 L4 radiation analogy, and all fictional/future source-status boundaries.
- **Curriculum design decisions:** HHH argument/CER rule, C2 L6 case-vs-capstone status, placement of fictional cases, and approved Campaign 2 classroom/no-game access strategy.
- **Shared-system/readiness:** stale HHH registry title and empty HHH campaigns list; expected to be resolved as case architecture becomes official, not patched during this audit.

## 7. Shared curriculum-production requirements that carry into HHH

The shared system should be reused **without forcing HHH into SSS scientific-diagnosis structure**. The following are controlling production lessons from the Curriculum Bible, Teacher/Accessible contracts, visual system, and SSS closeout:

- Student → Teacher task traceability; exact Student task numbers/titles control cross-role references.
- Field-complete Answer Key exemplars for every keyable subpart; “answers vary” is supplemental, never a substitute.
- Student and Accessible authored together. Accessible must reduce repeated workload/organizational burden while preserving the central historical reasoning goal.
- Every mark/select/rank/classify action must be digitally operable and persistent; every persistent response must be layout-classified.
- No runtime IDs, debug identifiers, repository paths, hashes, or production lineage in classroom-facing body content.
- One shared seven-function Teacher architecture and shared rubric architecture, populated with HHH-specific historical content.
- Source-status precision is central to HHH: documented, reproduced/adapted, inferred/reconstructed, debated, and fictional must be visibly distinct.
- Correctness and evidence architecture first; visual modernization follows separately. Exact maps, timelines, quantitative displays, and provenance relationships should be deterministic and sourced.
- Canonical production remains registered package-source HTML only: Student, Teacher, Answer Key, Accessible; Grayscale is a presentation state, not a fifth role.
- Printable identity, student identification row, balanced page fill, accessible continuous flow, Teacher metadata visibility, and task-reference emphasis amendments remain controlling.

### HHH-specific adaptation that the Blueprint should lock

HHH’s recurring student reasoning should be allowed to use chronology, provenance, source contribution/limitation, corroboration, contextualization, cause/consequence, continuity/change, competing interpretations, documented-vs-reconstructed status, geographic evidence, technology/agriculture change, and claim evaluation. A shared Claim–Evidence–Reasoning component can remain available when the product is genuinely an evidence-based historical claim, but **a scientific diagnosis or identical CER routine should not be imposed on every HHH case**.

## 8. Cross-campaign architecture

### Progression of historical reasoning

**Campaign 1** begins with archive procedure, then moves through cumulative selection/domestication, environmental systems and salinity, multi-causal famine, chemical/industrial technological change, land-use/conservation policy, a future biological-engineering system failure, and finally campaign synthesis.

**Campaign 2** raises the source-reasoning demand: authenticity/provenance, engineered historical landscapes, preservation of genetic records under siege, contested/forged Green Revolution records, a fully fictional protocol case requiring source-status discipline, a mixed real/debated/fictional mycorrhizal case, and an archive-ethics capstone with no uniquely correct moral verdict.

### Progression of agricultural concepts

Selection/domestication → water/soil management → crop genetic vulnerability → synthetic nitrogen → erosion/conservation → microbial nutrient cycling → archival authenticity → intensive wetland agriculture → crop-diversity preservation → varietal improvement/intensification → cross-species ecological requirements → mycorrhizal symbiosis/network claims → long-term stewardship of agricultural knowledge.

### Repeated concepts and callbacks

- Agricultural knowledge is cumulative, but records can be incomplete, reconstructed, politically framed, or forged.
- Diversity repeatedly functions as resilience: crop genetic diversity, ecosystem diversity, and diversity of evidence/methods.
- “One mechanism explains everything” is repeatedly unsafe; HHH should explicitly teach local mechanism vs. broader historical causation.
- Campaign 2 deliberately calls back to prior preservation/transfer themes and asks students to audit records rather than merely accept them.

### Campaign 2 independent usability

Pedagogically, C2 L0–L5 can be made independently usable because each has a self-contained evidence problem. Mechanically/narratively, Campaign 2 belongs after Campaign 1 in the game state. Therefore every C2 curriculum package should have a complete no-game evidence fallback, and the Blueprint should define an approved classroom direct-launch/save-state procedure if teachers are expected to play C2 cases out of campaign order.

### Fictional/future cases

C1 L6, C2 L4, C2 L5, and C2 L6 are not automatically disqualified. Their value is strongest when **fictional status is a reasoning feature rather than camouflage**: students can compare real principles, debated interpretations, and in-world claims. C2 L5 is especially promising after remediation because it can make documented vs. inferred vs. debated vs. fictional status the central historical/scientific literacy skill.

## 9. Game level count vs. recommended curriculum case count

**GAME LEVEL COUNT: 15**

**RECOMMENDED CURRICULUM CASE COUNT: 12 core cases**

Recommended default architecture:

1. C1 L0 — **Archive Orientation** (shared opener, not numbered core case)
2. Core Case 01 — C1 L1 Fertile Crescent / early grain domestication
3. Core Case 02 — C1 L2 Sumer / irrigation salinization
4. Core Case 03 — C1 L3 Ireland / blight and famine
5. Core Case 04 — C1 L4 Haber process
6. Core Case 05 — C1 L5 Dust Bowl
7. Core Case 06 — C1 L6 Vertical Farm 2041
8. C1 L7 — **Campaign 1 Synthesis / Debrief** (not numbered core case)
9. Core Case 07 — C2 L0 Archive Audit
10. Core Case 08 — C2 L1 Chinampas
11. Core Case 09 — C2 L2 Leningrad seed bank
12. Core Case 10 — C2 L3 Green Revolution
13. Core Case 11 — C2 L4 Karreth / protocol record
14. Core Case 12 — C2 L5 First Garden / mycorrhizal record
15. C2 L6 — **Campaign 2 / Program Capstone** (recommended non-core capstone unless owner promotes it to formal Case 13)

### Why the counts differ

C1 L0 teaches procedures and lore but does not contain enough independent historical content for a full case. C1 L7 is a retrospective finale that depends on earlier case memory. C2 L6 is pedagogically substantial but its final decision is an archive-ethics synthesis rather than a new historical investigation; it works better as a capstone unless the owner wants a formally numbered argumentation case. This recommendation follows the completed audit rather than assuming prologues/finales are excluded in advance.

### Alternate sequence option

If source literacy should precede all historical cases, the C2 L0 Archive Audit could be adapted into an early non-spoiler **Source Authenticity Mini-Lab** before Core Case 01, while its story-specific version remains in Campaign 2. That would require careful separation from game spoilers and should be a Blueprint decision, not silently reordered production.

## 10. Standards possibilities — program level

The strongest HHH homes are historical inquiry and disciplinary literacy. Candidate alignments must be chosen task-by-task; topic presence alone is not alignment.

- **C3 directly assessed candidates:** D3.1.6-8 / D3.2.6-8 for gathering/evaluating sources; D2.His.1.6-8 for contextual connections; D2.His.2.6-8 for continuity/change; D2.His.14.6-8 for multiple causes/effects; D4.1.6-8 for evidence-based argumentation where the final task genuinely requires it.
- **CCSS History/Social Studies directly/supporting:** RH.6-8.1, RH.6-8.2, RH.6-8.6, RH.6-8.7, RH.6-8.8, RH.6-8.9; WHST.6-8.1 and WHST.6-8.2 as appropriate.
- **NGSS:** use only when a case actually assesses a science/engineering practice or disciplinary idea. Sumer, Haber, Dust Bowl, Vertical Farm, and First Garden have genuine science content, but an HHH worksheet focused on source reasoning should label NGSS as supporting/contextual rather than fabricate direct performance-expectation alignment.

## 11. Owner decisions required for Blueprint

1. **HHH argument/CER policy.** Approve a historical-argument rule that permits canonical CER when appropriate but also allows source-analysis, chronology, provenance, comparison, and historical explanation products without a forced SSS-style diagnosis.
2. **C2 L6 status.** Recommended: capstone outside the 12 core numbered cases. Alternative: promote to formal Case 13 with a rubric that does not key one moral choice.
3. **Fictional case policy.** Recommended: keep C2 L4 and C2 L5 in the core sequence because they are strong source-status/interpretation lessons, provided their fictional and debated-science boundaries are explicit and C2 L5 is remediated.
4. **Campaign 2 classroom access.** Define approved direct-play/save-state behavior or rely on no-game evidence fallback for out-of-order classroom use.

These decisions should be resolved **in the Blueprint**, not before the Blueprint can begin.

## 12. PM handoff

- **Verified curriculum SHA:** `f61b77a63020254c8729d63c9960492cff0dc948` — authorized SHA and live remote `main` agree.
- **Verified HHH game SHA:** `9b8545ed6ecf98b337326390400076e36789e056` — authorized SHA, live remote `main`, and local audit checkout agree.
- **Audit status:** `AUDIT_COMPLETE — GAME_REMEDIATION_REQUIRED`.
- **Levels audited:** 15/15 shipped levels (Campaign 1 levels 0–7; Campaign 2 levels 0–6).
- **Baseline/source blockers:** none.
- **Material game corrections recommended before affected case production:** C1 L1 chronology/reconstruction framing; C1 L2 truncated required clue; C1 L3 universalizing famine/dependence wording; C1 L5 zero-life subsoil claims; C2 L0 “too clean” authenticity heuristic; C2 L2 insight/gate semantics; C2 L5 CMN/fossil-status claims; plus smaller prose/documentation/currentness corrections.
- **Owner/Blueprint decisions:** HHH argument/CER policy; C2 L6 formal-case status; fictional-case placement; Campaign 2 classroom launch/fallback strategy.
- **Recommended curriculum architecture:** 12 core cases + C1 orientation + C1 synthesis + C2 program capstone. Alternate: 13 formal cases if C2 L6 is promoted.
- **Proceed to HHH Curriculum Blueprint?** **YES.** The audit evidence is sufficient to define the HHH Blueprint and remediation plan. Do not finalize affected worksheets against unremediated game wording.

## 13. External verification bibliography

- **[H1] Allaby et al., “Geographic mosaics and changing rates of cereal domestication,” Philosophical Transactions B (2017).** https://pmc.ncbi.nlm.nih.gov/articles/PMC5665816/ — Supports a protracted, geographically variable cereal domestication process; wild-type shattering dominates before ~9500 BCE and non-shattering increases later.
- **[H2] Altaweel et al., “New insights on the role of environmental dynamics shaping southern Mesopotamia,” IRAQ (2019).** https://www.cambridge.org/core/journals/iraq/article/new-insights-on-the-role-of-environmental-dynamics-shaping-southern-mesopotamia-from-the-preubaid-to-the-early-islamic-period/F7084E4BF1171D8B77021B286BFE300C — Reviews salinization evidence and explicitly notes scholarly criticism of simple crop-shift/salinization interpretations.
- **[H3] Coomber, Saville & Ristaino, “Evolution of Phytophthora infestans on its potato host since the Irish potato famine,” Nature Communications (2024).** https://www.nature.com/articles/s41467-024-50749-4 — Confirms P. infestans as the oomycete responsible for potato late blight associated with the famine.
- **[H4] UK Parliament, “The great famine.”** https://www.parliament.uk/about/living-heritage/evolutionofparliament/legislativescrutiny/parliamentandireland/overview/the-great-famine/ — Notes dependence of about a third of the population on potatoes and continued food exports; useful for avoiding “nothing else existed” language.
- **[H5] Nobel Prize, “Fritz Haber – Facts” and 1918 presentation material.** https://www.nobelprize.org/prizes/chemistry/1918/haber/facts/ — Authoritative summary of Haber’s ammonia synthesis and controlled temperature/pressure/catalyst conditions.
- **[H6] Nobel Prize, “Carl Bosch – Facts.”** https://www.nobelprize.org/prizes/chemistry/1931/bosch/facts/ — Separates Bosch’s industrial high-pressure engineering from Haber’s laboratory synthesis.
- **[H7] USDA NRCS, “NRCS History.”** https://www.nrcs.usda.gov/about/history/brief-history-nrcs — Documents drought/erosion context, Bennett’s advocacy, 1935 storms, and the Soil Conservation Act.
- **[H8] USDA NRCS, “Soil Health” / “State Soils.”** https://www.nrcs.usda.gov/conservation-basics/soil/soil-health — Supports describing soil as biologically active and variable rather than treating exposed subsoil as literally devoid of microbial life.
- **[H9] US EPA, “Nitrogen Stabilizer Products that Must Be Registered under FIFRA.”** https://www.epa.gov/pesticide-registration/nitrogen-stabilizer-products-must-be-registered-under-fifra — Summarizes ammonium/ammonia → nitrite → nitrate nitrification and identifies ammonium and nitrate as major inorganic nitrogen forms.
- **[H10] Society of American Archivists Dictionary, “diplomatics.”** https://dictionary.archivists.org/entry/diplomatics.html — Defines diplomatics and identifies Mabillon’s De Re Diplomatica (1681) while emphasizing context/internal/external characteristics rather than a “too clean” rule.
- **[H11] U.S. National Archives, “NARA Guidance on Managing Web Records” / trustworthy records.** https://www.archives.gov/records-mgmt/policy/managing-web-records.html — Defines reliability, authenticity, integrity, and usability; supports multi-factor authenticity reasoning.
- **[H12] FAO, “Chinampas Agricultural System in Mexico City, Mexico.”** https://www.fao.org/giahs/giahs-around-the-world/mexico-chinampas-agricultural-system/en — Describes chinampas as wetland raised-field/artificial-island agriculture with canals, sediment/organic inputs, and high productivity.
- **[H13] Vavilov Institute (VIR), institute/history and siege remembrance material.** https://www.vir.nw.ru/en/about-institute/ — Primary institutional context for the Vavilov collection; paired with VIR siege records where available.
- **[H14] Crop Trust, “Nikolai Vavilov: The Father of Genebanks.”** https://www.croptrust.org/news-events/news/nikolai-vavilov-the-father-of-genebanks/ — Secondary authoritative crop-conservation account of Vavilov, the collection, siege preservation, and Vavilov’s 1943 death in prison.
- **[H15] Nobel Prize, “Norman Borlaug – Facts.”** https://www.nobelprize.org/prizes/peace/1970/borlaug/facts/ — Summarizes Mexico work, dwarf wheat, 1956 self-sufficiency, and introduction into India/Pakistan in the mid-1960s.
- **[H16] Dadachova et al., “Ionizing Radiation Changes the Electronic Properties of Melanin and Enhances the Growth of Melanized Fungi,” PLOS ONE (2007).** https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0000457 — Supports radiation-associated changes/growth in melanized fungi; does not justify presenting a complete gamma-to-metabolic-energy pathway as settled fact.
- **[H17] Karst, Jones & Hoeksema, “Positive citation bias and overinterpreted results lead to misinformation on common mycorrhizal networks in forests,” Nature Ecology & Evolution (2023).** https://www.nature.com/articles/s41559-023-01986-1 — Finds several broad popular CMN claims insufficiently supported and emphasizes alternative explanations.
- **[H18] Selosse et al., “Mycoheterotrophy in the wood-wide web,” Nature Plants (2024).** https://www.nature.com/articles/s41477-024-01677-0 — Provides an important counter-perspective: resource transfer through CMNs is real in particular systems; the literature should not be simplified to either “all sharing proven” or “networks do nothing.”
- **[H19] Strullu-Derrien et al., “An arbuscular mycorrhiza from the 407-million-year-old Windyfield Chert,” New Phytologist (2026).** https://pubmed.ncbi.nlm.nih.gov/41222019/ — Direct fossil evidence of arbuscular-mycorrhiza-like structures at ~407 Ma; useful for separating fossil evidence from older evolutionary inference.
- **[H20] Svalbard Global Seed Vault, 18 June 2026 deposit update.** https://www.seedvault.no/2026/06/18/svalbard-global-seed-vault-crosses-major-milestone-1-4-million-seed-samples-secured/ — Current official total: 1,401,285 seed samples after the June 2026 deposit.
- **[H21] Crop Trust, “Svalbard Global Seed Vault” program history.** https://www.croptrust.org/what-we-do/programs/svalbard-global-seed-vault/ — Documents ICARDA’s 2015 first-ever withdrawal and regeneration in Lebanon and Morocco.
- **[H22] Common Core State Standards Initiative, History/Social Studies Grades 6–8.** https://www.thecorestandards.org/ELA-Literacy/RH/6-8/ — Reference for candidate RH.6-8 literacy standards.

## 14. Audit-method notes and limitations

- Runtime counts/reachability were derived from the authorized JavaScript data and `index.html` completion logic using a read-only Node/static harness, then manually checked where static analysis could be fooled by dynamic construction.
- “Direct-route words” are comparative burden estimates, not exact student reading-time predictions and not completionist totals.
- Game dialogue, TAA scans, future/alien records, and reconstructed historical characters are **not** automatically real primary sources merely because the runtime labels them testimony/archive/forensics. Curriculum source status must be independently declared.
- Historical verification deliberately avoids manufacturing precise motives, dates, counts, or quotes when sources support only ranges, interpretations, or reconstructed narratives.
- This audit does not redesign HHH worksheets. Candidate tasks/standards are readiness evidence for the Blueprint phase only.

---

**FINAL DISPOSITION: `AUDIT_COMPLETE — GAME_REMEDIATION_REQUIRED`**

Blueprint work may proceed. Affected case production must respect the remediation/qualification findings above.
