window.SSS_C2_CASE04_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C2-CASE04",
  "title": "The Silent Grove",
  "version": "1.0",
  "status": "DRAFT",
  "approvalDate": null,
  "approvedBy": null,
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "mergeStatus": "NOT_READY",
  "editorShell": "1.0",
  "gameCommit": "29c3b222c53f51de11a3aa83e896a6d0ef6fb490",
  "runtimeCaseId": "silent_grove",
  "runtimeInvestigationName": "Zhel'ii Diaspora Grove",
  "runtimeLocation": "Drift Vessel Thal-Oren",
  "runtimeSubtitle": "Inter-system Transit",
  "roles": {
    "student": 6,
    "teacher": 8,
    "answer": 4,
    "accessible": 8
  },
  "tasks": [
    {
      "id": "C2-C04-T1",
      "number": "1",
      "semanticLabel": "REFERENCE",
      "icon": "ph-book",
      "title": "Separate What Changed from What Held",
      "description": "Separate the one condition that changed on Day −90 from the conditions two independent ship logs show were held, and state why a sequence in time is not yet a cause.",
      "keyed": true
    },
    {
      "id": "C2-C04-T2",
      "number": "2",
      "semanticLabel": "DATA ANALYSIS",
      "icon": "ph-scales",
      "title": "Read the Change Record and the Signalling Readings",
      "description": "Read the schedule record, the signalling readings, and the two change logs exactly, preserving the reported range and the reporting-threshold status of the 0.0 ppb reading.",
      "keyed": true
    },
    {
      "id": "C2-C04-T3",
      "number": "3",
      "semanticLabel": "DATA ANALYSIS",
      "icon": "ph-scales",
      "title": "Read the Daily Signalling Profile",
      "description": "Read the within-cycle record, explain what a daily total cannot show, and identify the hour blocks the records do not report and may not be filled in.",
      "keyed": true
    },
    {
      "id": "C2-C04-T4",
      "number": "4",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-nodes",
      "title": "Weaken the Competing Explanations",
      "description": "Use the grove readings, the examination record, and the habitat record to weaken the filtration, light-damage, and transit-stress explanations with evidence.",
      "keyed": true
    },
    {
      "id": "C2-C04-T5",
      "number": "5",
      "semanticLabel": "EVIDENCE SYNTHESIS",
      "icon": "ph-nodes",
      "title": "Connect the Five Evidence Sources",
      "description": "Give every formal evidence source an instructional role by stating its contribution to the diagnosis and its limit if used alone.",
      "keyed": true
    },
    {
      "id": "C2-C04-T6",
      "number": "6",
      "semanticLabel": "DIAGNOSIS",
      "icon": "ph-diagnosis",
      "title": "Diagnose and Model the Mechanism",
      "description": "Select the best-supported diagnosis, reject the alternatives with evidence, and complete the condition-mechanism-effect model.",
      "keyed": true
    },
    {
      "id": "C2-C04-T7",
      "number": "7",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Explain the Diagnosis with CER",
      "description": "Write a Claim-Evidence-Reasoning explanation using evidence from more than one source and preserving the boundary between established Earth chronobiology and records made for this grove.",
      "keyed": true
    },
    {
      "id": "C2-C04-T8",
      "number": "8",
      "semanticLabel": "ENGINEERING DESIGN",
      "icon": "ph-wrench",
      "title": "Specify a Dark Period and a Monitored Trial",
      "description": "Define dark-hour and cycle-stability criteria, justify the chosen value against the recorded minimum, name one constraint, and set a monitored trial with a stop-and-revise rule.",
      "keyed": true
    }
  ],
  "formalClues": [
    "NETWORK_FALLEN_SILENT",
    "CONTINUOUS_LIGHT_24H",
    "SIGNALING_COMPOUNDS_ABSENT",
    "LIGHT_SCHEDULE_CHANGED",
    "CIRCADIAN_SIGNALING_NEEDS_DARK"
  ],
  "clueTaskCoverage": {
    "NETWORK_FALLEN_SILENT": [
      1,
      5
    ],
    "CONTINUOUS_LIGHT_24H": [
      2,
      5,
      6
    ],
    "SIGNALING_COMPOUNDS_ABSENT": [
      4,
      5,
      6
    ],
    "LIGHT_SCHEDULE_CHANGED": [
      1,
      2,
      3,
      5
    ],
    "CIRCADIAN_SIGNALING_NEEDS_DARK": [
      3,
      5,
      8
    ]
  },
  "requiredRoutes": [
    "crew.start->timeline",
    "sensors.start->light_data",
    "plants.start->signal_structures",
    "logs.start->light_history",
    "database.start->circadian_data"
  ],
  "sourceLedger": [
    {
      "source": "Caretaker Vess-lor",
      "clue": "NETWORK_FALLEN_SILENT",
      "establishes": "A two-year healthy baseline aboard this ship, and a gradual fade over about a week rather than a sudden loss.",
      "cannotEstablishAlone": "An account of what the caretakers changed is not a measurement of what the change did."
    },
    {
      "source": "Grove Sensor Array",
      "clue": "CONTINUOUS_LIGHT_24H",
      "establishes": "The schedule now runs 24.0 h on and 0.0 h off with no dark period, and output reads 0.0 ppb at the reporting threshold against an expected 40-80 ppb cycling range.",
      "cannotEstablishAlone": "A reading at the threshold shows that no signal is measurable; it does not show why production stopped."
    },
    {
      "source": "Genesis Pod Offspring",
      "clue": "SIGNALING_COMPOUNDS_ABSENT",
      "establishes": "The release structures are closed rather than damaged, the receiver is intact, and the vine reflex is normal, so the machinery is capable and idle.",
      "cannotEstablishAlone": "An intact structure does not identify which condition switched the function off."
    },
    {
      "source": "Ship Caretaker Logs",
      "clue": "LIGHT_SCHEDULE_CHANGED",
      "establishes": "The Day -90 change from 18/6 to 24/0 and the two-year within-cycle pattern of a peak in hours 19-24 and a minimum in hours 6-12.",
      "cannotEstablishAlone": "The within-cycle pattern is a record of this grove under one schedule, not a general rule."
    },
    {
      "source": "Federation Database",
      "clue": "CIRCADIAN_SIGNALING_NEEDS_DARK",
      "establishes": "The Earth comparison that clocks can be entrained by light-dark cycles with species-dependent responses to continuous light, and this grove's recorded minimum of at least five dark hours.",
      "cannotEstablishAlone": "Established Earth science does not turn records made for this grove into general biology."
    }
  ],
  "numericalLedger": {
    "schedule": {
      "currentOnHours": 24.0,
      "currentOffHours": 0.0,
      "currentDarkPeriod": "none",
      "currentIntensityPercent": 100,
      "previousOnHours": 18.0,
      "previousOffHours": 6.0,
      "scheduleChangedOnDay": -90,
      "habitatDayHours": 19,
      "habitatNightHours": 7
    },
    "signalling": {
      "unit": "ppb",
      "trailing24hOutput": "0.0",
      "trailingWeekOutput": "0.0",
      "outputStatus": "no signal at the reporting threshold",
      "lastRecordedSignalDaysAgo": 87,
      "expectedHealthyRange": [
        40,
        80
      ],
      "expectedHealthyStatus": "cycling",
      "peakHours": [
        19,
        24
      ],
      "minimumHours": [
        6,
        12
      ],
      "unreportedHourBlocks": [
        [
          0,
          6
        ],
        [
          12,
          18
        ],
        [
          18,
          19
        ]
      ],
      "cyclingRecordDurationYears": 2
    },
    "groveConditions": {
      "temperatureC": 24.1,
      "humidityPercent": 88,
      "oxygenPercent": 22.4,
      "carbonDioxidePpm": 1200,
      "nitrogenPercent": 76.8,
      "scrubberStatus": "active, within the Zhel'ii target range",
      "compoundFiltration": "set to preserve"
    },
    "changeRecords": {
      "sensorChangeLog": {
        "-93": "power fluctuation, mild photosynthetic stress",
        "-90": "schedule changed to 24.0 h on / 0.0 h off",
        "-87": "first drop in signalling output noted",
        "-83": "output falls below the measurable threshold",
        "-80": "complete silence"
      },
      "caretakerLog": {
        "-93": "power fluctuation recorded",
        "-90": "same schedule change recorded",
        "-83": "signalling ceases entirely; complete silence, no structural decline"
      },
      "recordDivergence": "The two logs give different days for the start of complete silence, -80 and -83. The difference is between records and is never reconciled, averaged, or treated as a second cause."
    },
    "habitatRecord": {
      "validatedMinimumDarkHours": 5,
      "suppressionWindowDays": [
        7,
        10
      ],
      "reversibilityWindowMonths": 6,
      "scheduleWithTwoYearRecordDarkHours": 6
    }
  },
  "sourceStatus": {
    "establishedEarthScienceComparison": "Biological clocks can be entrained by recurring environmental cycles including light-dark transitions, and responses to continuous light differ among species, with both injury and tolerance reported.",
    "caseSpecificEvidence": "This grove's two-year cycling record and its peak and minimum hour blocks, the 40-80 ppb healthy range, the recorded five-hour minimum dark interval, the 7-10 day suppression window, and the six-month reversibility figure.",
    "numbers": "game-provided measurements",
    "figures": "curriculum-original"
  },
  "correctDiagnosis": "Removing the recurring dark interval removed the timing cue that this grove's recorded signalling cycle is entrained to, so measured output fell to the reporting threshold while the three organisms stayed structurally healthy.",
  "incorrectAlternatives": [
    "the chemical scrubbers are filtering the signalling compounds out of the air",
    "the light intensity is high enough to damage the grove's photosynthetic tissue",
    "the ship's transit environment is stressing the grove"
  ],
  "prohibitedClaims": [
    "all plants need darkness",
    "every plant needs a night to reset its clock",
    "darkness is a nutrient",
    "0.0 ppb means no molecules are present",
    "the signalling output is exactly zero",
    "the grove will sing again once the dark period is restored",
    "signalling is guaranteed to return within a day or two",
    "continuous light always harms plants",
    "the organisms decided or chose to stop signalling",
    "all chemical signalling between organisms is circadian",
    "the clock thinks it is always midday",
    "five dark hours is the requirement for this or any grove",
    "the caretakers damaged the grove",
    "the average healthy output is 60 ppb",
    "the grove was singing as an acoustic measurement",
    "correlation alone proves causation"
  ],
  "figureProvenance": [
    {
      "id": "fig-timeline",
      "kind": "curriculum-original inline SVG",
      "shows": "The days each ship log actually records, with each log's own silence-onset day marked by its own fill pattern.",
      "prohibited": "No interpolation between logged days, no reconciled single onset date, no colour-only encoding."
    },
    {
      "id": "fig-profile",
      "kind": "curriculum-original inline SVG",
      "shows": "Reported lighting and reported signalling as discrete hour blocks for the previous and current schedules, with unreported blocks labelled as unreported.",
      "prohibited": "No continuous curve, no connecting line between blocks, no value for an unreported hour, no zero baseline."
    }
  ],
  "productionCautions": [
    "Keep 40-80 ppb as a range; never report a midpoint.",
    "Report 0.0 ppb as a reading at the instrument's reporting threshold, never as an absolute absence.",
    "Do not read or draw a value for any hour block the records mark as not separately reported.",
    "Do not average or reconcile the two logs' different silence-onset days.",
    "Do not convert the recorded five-hour minimum into the specification value; the schedule with a two-year record used six dark hours.",
    "Do not generalise this grove's dark-interval requirement to plants as a whole."
  ]
};
