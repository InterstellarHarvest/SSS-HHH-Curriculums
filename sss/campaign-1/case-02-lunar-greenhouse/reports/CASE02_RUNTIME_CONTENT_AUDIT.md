# Case 02 Runtime Content Audit — Lunar Greenhouse

**Case:** SSS Campaign 1, Case 02  
**Audit date:** 2026-07-24  
**Game baseline:** `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`  
**Status:** VALIDATION BUILD

## 1. Runtime source of truth

The playable Case 02 source of truth is:

1. top-level `index.html`, which loads the canonical data files;
2. top-level `space_sprout_sleuth_data.js`;
3. the case object with `id: "lunar"`.

Nested resource copies, design notes, exports, and backups are historical/supporting material and are not curriculum truth when they differ from the playable top-level runtime.

## 2. Playable case identity

- **Runtime name:** Lunar Greenhouse
- **Location:** Shackleton Crater, lunar south pole
- **Crop:** Cherry tomato
- **Phenomenon:** Plants are vigorous and flower normally, but no fruit forms; flowers later drop.
- **Required source count:** Four
- **Purposeful direct-route reading estimate:** approximately 515 words
- **Purposeful gameplay window:** about 8–12 minutes direct; 14–18 minutes with mechanism exploration

## 3. Formal evidence and direct routes

| Runtime source | Direct route | Formal clue | Curriculum interpretation |
|---|---|---|---|
| Botanist Chen | `start → problem_main` | `FLOWERS_NO_FRUIT` | Healthy flowers drop without fruit; this is the reproductive symptom. |
| Lunar-GH Sensor Array | `start → airflow` | `LOW_AIRFLOW` | Air movement is nearly absent while primary growth conditions are nominal. |
| Tomato Specimen Row | `start → flowers → pollen_close` | `POLLEN_UNDISTURBED` | Mature pollen remains on the anthers; stigmas are clean; no insects are present. |
| Greenhouse Design Docs | `start → crop_protocols` | `NO_POLLINATION_PLAN` | Pollination was left unresolved; no animal, manual, or mechanical system was implemented. |

The optional stem-shaking interaction and hand/mechanical-pollination records are useful mechanism tests but are not required for academic completion.

## 4. Diagnosis options

| Runtime option | Audit disposition |
|---|---|
| Lunar regolith is toxic to fruit development. | Distractor; broad toxicity conflicts with healthy roots, leaves, stems, moisture, and nutrients. |
| The light spectrum lacks ultraviolet light needed for fruiting. | Distractor; normal flowering and the direct pollen observation weaken it. |
| No pollination is occurring because pollen is not effectively released/transferred. | Correct. |
| Carbon dioxide is too high for tomatoes. | Distractor; the case treats the reading as compatible with growth and it does not explain pollen remaining on anthers. |

## 5. Verified mechanism

The last clearly working event is production of viable pollen in healthy flowers. The first failed event is effective physical agitation/pollen release. Because pollen is not released and does not reach the receptive stigma, pollen germination, pollen-tube growth, fertilization, and fruit set cannot proceed normally.

The curriculum therefore diagnoses a **missing process action**, not merely “no bees.” Tomato flowers can contain both reproductive structures, but effective pollen movement is still required.

## 6. Compatibility and qualification decisions

### Preserved from the game

- Four formal evidence channels and clue identities
- Correct diagnosis and implemented distractors
- Flower-without-fruit symptom
- Nearly still habitat, no insects, and omitted pollination plan
- Direct agitation as a mechanism test

### Qualified in the curriculum

- The game’s exact airflow and vibration-frequency numbers are treated as local fictional/design data, not universal engineering recommendations.
- The fictional `NASA Technical Brief TB-2019-AG` is not represented as a real source.
- Brush transfer, vibration, airflow, and insect activity are not collapsed into one universal method; they are possible ways to achieve species-appropriate pollen release/transfer.
- Pollination is explicitly separated from fertilization and fruit set.
- The mechanism is taught as tomato/greenhouse science and is not generalized to every flowering crop.

## 7. Instructional identity decision

- **Student identity:** Process Modeler
- **Central task:** Reproductive-process model
- **First failed step:** Physical agitation/pollen release
- **Primary evidence-processing move:** Trace dependency through the sequence and identify the earliest broken event
- **CER focus:** Explain why undisturbed pollen, still air, and the missing plan support pollination failure better than the three distractors

This follows the approved audit recommendation and deliberately does not reuse Case 01’s four-source evidence matrix as the central worksheet structure.

## 8. Runtime audit conclusion

The current playable Case 02 content is compatible with a scientifically defensible lesson after the qualifications above. No game-code change is required to author this curriculum build. The curriculum remains pinned to game commit `2a6e8a7` until a later game revision is separately audited.
