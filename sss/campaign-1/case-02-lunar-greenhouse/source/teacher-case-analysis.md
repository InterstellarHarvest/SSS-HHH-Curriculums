# Teacher Case Analysis — Lunar Greenhouse

**Status:** VALIDATION BUILD

## Story problem

At Shackleton Crater, vigorous cherry tomato plants produce normal-looking flowers for weeks, but flowers drop without fruit development.

## Scientific phenomenon

A designed environment supports vegetative growth but omits a critical reproductive operation. The case asks students to locate the first broken link in a sequence rather than merely name a missing animal.

## Exact runtime source of truth

The playable case is the `lunar` object in top-level `space_sprout_sleuth_data.js`, loaded by top-level `index.html`, at game commit `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`. Nested resource copies and backups are not curriculum sources.

## Formal evidence sources

| Source | Formal clue | Instructional role |
|---|---|---|
| Botanist Chen | `FLOWERS_NO_FRUIT` | Defines the reproductive symptom: healthy flowers drop without fruit. |
| Lunar-GH Sensor Array | `LOW_AIRFLOW` | Shows nearly absent air movement while primary growth measures are nominal. |
| Tomato Specimen Row | `POLLEN_UNDISTURBED` | Locates the bottleneck: mature pollen remains on anthers and stigmas are clean. |
| Greenhouse Design Docs | `NO_POLLINATION_PLAN` | Identifies a systems-design omission: no pollination strategy or equipment. |

## Essential versus optional evidence

Essential evidence is the undisturbed pollen, the missing pollination plan, the still-air condition, and the flower-without-fruit pattern. Optional gated conversations, hand-pollination records, and the stem-shaking action strengthen the mechanism by showing that agitation releases pollen. They are useful cross-checks but may not be required for academic completion.

## Correct mechanism

The last clearly working step is production of viable pollen in healthy flowers. The first failed step is effective physical agitation/pollen release. Without release, pollen does not reach the receptive stigma; later pollen-tube growth, fertilization, and fruit set cannot proceed.

## Implemented diagnosis options

1. Lunar regolith is toxic to fruit development — wrong.
2. Missing ultraviolet light prevents fruiting — wrong.
3. No pollination is occurring because pollen is not effectively released/transferred — correct.
4. Carbon dioxide is too high — wrong.

## Why distractors are tempting

- **Regolith toxicity** sounds plausible in a lunar setting, but healthy roots, stems, leaves, and nominal nutrients argue against a broad toxicity failure.
- **Ultraviolet deficiency** sounds technical, but flowering is normal and the game states full-spectrum lighting includes ultraviolet components.
- **High carbon dioxide** can sound harmful, but the case sensor treats the reading as compatible with growth; it does not explain pollen remaining on anthers.

## Instructional opportunities

- Separate reproductive sequence from general plant health.
- Distinguish pollination, fertilization, and fruit set.
- Show how a direct intervention can test a causal model.
- Teach that controlled systems must intentionally replace ecosystem services.
- Prepare for Campaign 2 Case 02, which complicates the solution by making a species require a tuned release trigger.

## Science qualifications

The game’s core mechanism is sound for greenhouse tomato instruction, but its exact airflow and vibration numbers should not be taught as universal thresholds. The curriculum uses them only as fictional/local design data. Brush transfer and vibration are distinct techniques; the case diagnosis is best expressed as missing effective pollen release and stigma contact, not “no bees.”

## Science-status labels

- **Established:** flower structures and the pollination-to-fruit sequence; agitation-assisted greenhouse tomato pollination.
- **Plausible extrapolation:** deliberate mechanical/manual support in an off-world habitat.
- **Fictional:** location, characters, readings, logs, and equipment history.
- **Context-dependent:** exact environmental limits and best engineering method.
