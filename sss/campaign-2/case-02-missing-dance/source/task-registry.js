window.SSS_C2_CASE02_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C2-CASE02",
  "title": "The Missing Dance",
  "version": "1.0",
  "status": "DRAFT",
  "approvalDate": null,
  "approvedBy": null,
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "mergeStatus": "NOT_READY",
  "editorShell": "1.0",
  "gameCommit": "29c3b222c53f51de11a3aa83e896a6d0ef6fb490",
  "runtimeCaseId": "missing_dance",
  "runtimeInvestigationName": "Ares Botanical Garden",
  "runtimeLocation": "Olympia District",
  "runtimeSubtitle": "Mars",
  "roles": {
    "student": 5,
    "teacher": 8,
    "answer": 4,
    "accessible": 8
  },
  "tasks": [
    {
      "id": "C2-C02-T1",
      "number": "1",
      "semanticLabel": "REFERENCE",
      "icon": "ph-book",
      "title": "Rule Things Out",
      "description": "Cross off the conditions the garden reports as normal and the interventions already tried, then explain why three failed pollination trials are useful evidence rather than a dead end.",
      "keyed": true
    },
    {
      "id": "C2-C02-T2",
      "number": "2",
      "semanticLabel": "WARM-UP",
      "icon": "ph-book",
      "title": "Shake, Don't Touch",
      "description": "Use a salt-shaker comparison with invented values to establish that some containers release their contents only when shaken hard enough and long enough, not when merely touched.",
      "keyed": true
    },
    {
      "id": "C2-C02-T3",
      "number": "3",
      "semanticLabel": "OBSERVATION",
      "icon": "ph-scales",
      "title": "Look Inside the Flower",
      "description": "Read the specimen record to establish that the pollen is present, viable and retained, and that the cone's pores are already open, so nothing is blocked or missing.",
      "keyed": true
    },
    {
      "id": "C2-C02-T4",
      "number": "4",
      "semanticLabel": "INVESTIGATION",
      "icon": "ph-nodes",
      "title": "Ask Without Asking",
      "description": "Work out how to reach a conclusion when a knowledgeable source cannot share it, by deciding what to establish independently and which source could establish it.",
      "keyed": true
    },
    {
      "id": "C2-C02-T5",
      "number": "5",
      "semanticLabel": "EVIDENCE SYNTHESIS",
      "icon": "ph-nodes",
      "title": "Connect the Five Evidence Sources",
      "description": "Give every formal evidence source an instructional role by stating its contribution to the diagnosis and its limit if used alone.",
      "keyed": true
    },
    {
      "id": "C2-C02-T6",
      "number": "6",
      "semanticLabel": "DIAGNOSIS",
      "icon": "ph-diagnosis",
      "title": "Diagnose and Reject Alternatives",
      "description": "Select the best-supported diagnosis, reject the three alternatives with evidence, and complete the condition-mechanism-effect model.",
      "keyed": true
    },
    {
      "id": "C2-C02-T7",
      "number": "7",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Explain the Diagnosis with CER",
      "description": "Write a Claim-Evidence-Reasoning explanation using evidence from more than one source and preserving the boundary between established Earth science and case-specific evidence.",
      "keyed": true
    },
    {
      "id": "C2-C02-T8",
      "number": "8",
      "semanticLabel": "ENGINEERING DESIGN",
      "icon": "ph-wrench",
      "title": "Specify a Safe Trial",
      "description": "Name the four settings a vibration trial must vary rather than assuming one number, define what to measure, set a damage limit, and write a stop-and-revise rule.",
      "keyed": true
    }
  ],
  "formalClues": [
    "LYREFLOWER_BUDS_ABORT",
    "NO_ACOUSTIC_TRIGGER",
    "POLLEN_RETAINED",
    "HAND_POLLINATION_FAILED",
    "BUZZ_POLLINATION_ACOUSTIC"
  ],
  "clueTaskCoverage": {
    "LYREFLOWER_BUDS_ABORT": [1, 4],
    "NO_ACOUSTIC_TRIGGER": [1, 5, 6],
    "POLLEN_RETAINED": [3, 5, 6],
    "HAND_POLLINATION_FAILED": [1, 5, 6],
    "BUZZ_POLLINATION_ACOUSTIC": [4, 5, 8]
  },
  "requiredRoutes": [
    "crew.start->cultural_barrier",
    "sensors.start->acoustic_scan",
    "plants.start->anther_exam",
    "logs.start->pollination_log",
    "database.start->buzz_pollination"
  ],
  "sourceLedger": [
    {
      "source": "Researcher Miran-sel",
      "clue": "LYREFLOWER_BUDS_ABORT",
      "establishes": "Buds form correctly and then abort before opening while the plant stays healthy in every other respect, and a knowledgeable source can confirm a conclusion reached independently but cannot state it first.",
      "cannotEstablishAlone": "Does not supply the mechanism, because the cultural constraint prevents the researcher from naming it."
    },
    {
      "source": "Garden Sensor Array",
      "clue": "NO_ACOUSTIC_TRIGGER",
      "establishes": "The sealed garden reports no periodic vibration and a flat 20-200 Hz scan, where comparable Telluvian gardens report periodic signals in the 100-150 Hz range; every other condition reads nominal.",
      "cannotEstablishAlone": "Does not show that this particular plant depends on such a signal."
    },
    {
      "source": "Lyreflower Specimen",
      "clue": "POLLEN_RETAINED",
      "establishes": "The anther cone is poricidal with pores already present, the pollen inside is mature and dense, and ordinary contact releases almost none of it.",
      "cannotEstablishAlone": "Does not identify which stimulus would release it."
    },
    {
      "source": "Garden Records",
      "clue": "HAND_POLLINATION_FAILED",
      "establishes": "Three hand-pollination trials with viable pollen and a receptive stigma produced no fruit set, and every horticultural variable was already optimised without improvement.",
      "cannotEstablishAlone": "Does not explain why direct contact was insufficient."
    },
    {
      "source": "Federation Database",
      "clue": "BUZZ_POLLINATION_ACOUSTIC",
      "establishes": "In established Earth science, buzz-pollinating bees vibrate poricidal flowers so pollen leaves through pores already present, with release depending on frequency, amplitude, duration and coupling; the case record reports the lyreflower's strongest release near the lyre-moth's 124 Hz wingbeat when amplitude and duration are sufficient.",
      "cannotEstablishAlone": "Does not establish that this garden is the failure point without the site measurements."
    }
  ],
  "numericalLedger": {
    "acoustic": {
      "ambientNoiseDb": 28,
      "ambientNoiseSource": "HVAC hum only",
      "periodicSignals": "none detected",
      "scanRangeHz": [20, 200],
      "scanResult": "flat, no peaks",
      "soilLevelVibration": "below threshold",
      "telluvianGardenReferenceHz": [100, 150]
    },
    "pollination": {
      "pollinatorsPresent": "none, sealed facility",
      "airflowMetresPerSecond": 0.0,
      "handPollinationAttempts": 3,
      "handPollinationSuccesses": 0,
      "pollenViabilityPercent": 98,
      "stigmaReceptivity": "confirmed receptive"
    },
    "environment": {
      "airTemperatureC": 22.1,
      "humidityPercent": 62,
      "lightCycle": "14h/10h",
      "soilPh": 6.8,
      "oxygenPercent": 21.0,
      "carbonDioxidePpm": 420,
      "nitrogenPercent": 78.1,
      "pressureAtm": 1.01,
      "substrate": "imported Telluvian mineral substrate"
    },
    "timeline": [
      {"period": "Month 1", "observation": "Continuous bloom, vigorous growth"},
      {"period": "Week 3", "observation": "Hand-pollination trial 1, brush applicator, no fruit set"},
      {"period": "Week 4", "observation": "Hand-pollination trial 2, calibrated applicator, no fruit set"},
      {"period": "Week 5", "observation": "Hand-pollination trial 3, viability confirmed, no fruit set"},
      {"period": "Month 2", "observation": "Buds abort before opening, bloom rate declining"},
      {"period": "Month 3", "observation": "No successful bloom since week 5"}
    ],
    "strongestResponseHz": 124,
    "strongestResponseQualifier": "strongest response near this value, and only when amplitude and duration are also sufficient",
    "trialVariables": ["frequency", "amplitude", "duration", "coupling and placement"]
  },
  "sourceStatus": {
    "establishedEarthScienceComparison": "Poricidal anthers have pores that are already present. In buzz pollination a bee grasps the flower and vibrates it mechanically, so pollen is expelled through those existing pores. Release depends on frequency, amplitude, duration and coupling rather than one universal frequency. Floral buzzing occurs across several bee taxa and honeybees do not perform it. Growers can assist tomato pollination with commercial vibrating tools, and managed bumblebee colonies are another greenhouse option.",
    "caseSpecificEvidence": "The lyreflower's flexible cone, the lyre-moth's hovering wingbeat, the airborne coupling route, the strongest measured response near 124 Hz, and every garden measurement in this case.",
    "numbers": "game-provided measurements",
    "figures": "curriculum-original",
    "teachingAnalogy": "Task 2 uses a salt shaker with invented counts of grains released by touching, by one shake and by ten shakes. Those values teach the relationship only. They are labelled in the printable content as not being measurements from the garden, and they never appear as case evidence."
  },
  "correctDiagnosis": "The lyreflower needs vibration coupled into its anther cone that is strong enough and sustained enough to shake pollen out through the pores already present, with the strongest reported response near the lyre-moth's 124 Hz wingbeat. The sealed garden supplies no such vibration, so pollen stays in the cone and the buds abort.",
  "incorrectAlternatives": [
    "the pollinator species is simply absent, so staff need to transfer pollen by hand",
    "the light cycle is wrong for Telluvian flowering",
    "the imported substrate is missing a trace element"
  ],
  "prohibitedClaims": [
    "124 Hz is a magic frequency that guarantees pollen release",
    "frequency alone determines whether pollen is released",
    "all buzz-pollinated flowers respond at the same frequency",
    "Earth flowers respond most strongly at 124 Hz",
    "honeybees perform buzz pollination",
    "only bumblebees perform buzz pollination",
    "the pores open when the flower is vibrated",
    "the pores are sealed until the right sound arrives",
    "playing a sound in the room is enough to release the pollen",
    "the flower hears or listens for the moth",
    "hand pollination always works for any flower",
    "the researcher was keeping a secret",
    "a calibrated exciter is guaranteed to restore fruit set",
    "the plant is unhealthy or diseased",
    "correlation alone proves causation"
  ],
  "figureProvenance": [
    {
      "id": "fig-cone",
      "kind": "curriculum-original inline SVG",
      "shows": "A cut-away of the anther cone with the pores already present along its surface and mature pollen retained inside.",
      "prohibited": "No pore may be drawn as closed, sealed or opening; nothing may imply the pollen is blocked rather than retained."
    },
    {
      "id": "fig-factors",
      "kind": "curriculum-original inline SVG",
      "shows": "The four settings that together determine release - frequency, amplitude, duration, and coupling - as four equally weighted labelled panels.",
      "prohibited": "No response curve, no frequency axis, and no visual that singles out one setting as sufficient on its own."
    }
  ],
  "productionCautions": [
    "The pores are already present. Never write that they open, unseal or are blocked; the pollen is retained, not trapped by a closed structure.",
    "Never present 124 Hz as sufficient on its own. Every mention must sit beside amplitude, duration and coupling.",
    "Keep the 124 Hz value as a case measurement for this species. It is not an Earth figure and not a universal one.",
    "Honeybees do not perform floral buzzing, and floral buzzing is not limited to bumblebees. State neither incorrectly.",
    "The researcher's constraint is cultural, and the case says explicitly that it is not secrecy. Present it as a professional boundary to work within, never as obstruction.",
    "Airborne coupling is the route recorded for this species. Earth bees grasp the flower directly, so do not merge the two mechanisms.",
    "The remedy is a monitored trial. Do not describe any exciter setting as guaranteed, and keep a damage limit attached to it."
  ]
};
