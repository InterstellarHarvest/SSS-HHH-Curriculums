window.SSS_C2_CASE04_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C2-CASE04",
  "title": "The Silent Grove",
  "version": "1.1",
  "status": "OWNER_GATE_OPEN",
  "correctiveOf": "1.0",
  "owner": "Nate / Owner",
  "ownerReviewStatus": "OWNER_REVIEW_IN_PROGRESS",
  "printStatus": "NOT_RUN",
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
      "title": "What a Reading Can and Cannot Tell You",
      "description": "Use two everyday examples — a scale that reads zero and two witnesses who disagree — to judge what a threshold reading, a reported range, and two differing records can and cannot support, then apply all three to the grove.",
      "keyed": true
    },
    {
      "id": "C2-C04-T3",
      "number": "3",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-nodes",
      "title": "Find the Pattern a Total Hides",
      "description": "Use a same-total, different-pattern sleep example to explain why a daily total can hide timing, then apply it to the grove's two-year signalling cycle and the loss of its dark hours.",
      "keyed": true
    },
    {
      "id": "C2-C04-T4",
      "number": "4",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-nodes",
      "title": "Weaken the Competing Explanations",
      "description": "Use the grove readings, the examination record, and the recorded transit history to weaken the filtration-drift, light-damage, and transit-stress explanations with evidence.",
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
    "figures": "curriculum-original",
    "teachingAnalogy": "Task 2 uses a kitchen scale that reads 0 kg for an envelope and two witnesses, Rosa and Theo, who record a rain shower stopping at 4:00 and 4:10. Task 3 uses Mia and Sam, who each sleep 8 hours a day in different patterns. Those examples teach the ideas only. They are labelled in the printable content as not being grove measurements, they carry lettered table numbers rather than the numbered case tables, and their values never appear as case evidence."
  },
  "alternativeSourceFidelity": {
    "rule": "A rejected alternative must keep the causal direction the runtime states. A claim that a system has drifted out of its calibrated range is not the same claim as a system operating as set, and the packet's rejection evidence answers the former.",
    "runtimeLabel": "The atmospheric chemical filtering has drifted out of range despite the crew's monitoring.",
    "curriculumWording": "The chemical scrubbers have drifted out of their target range and are removing the signalling compounds from the air.",
    "rejectionEvidence": "Table 3 reports the chemical scrubbers active and within the Zhel'ii target range and compound filtration set to preserve; Table 6 reports the compounds not produced rather than removed."
  },
  "standards": [
    {
      "code": "MS-LS1-5",
      "claim": "supporting",
      "bounded": true,
      "assessingTasks": [7],
      "assessedPractice": "Constructing a written evidence-based explanation of how a local environmental condition influences an organism. The practice half only.",
      "learnerEvidence": [
        "Table 5 — the two-year within-cycle record, peak in hours 19–24 and minimum in hours 6–12 (Student page 3, Accessible page 3)",
        "Table 4 — the Day −90 schedule change and no other environmental variable changed (Student page 2, Accessible page 2)",
        "Table 6 — the examination record showing the organisms structurally intact (Student page 4, Accessible page 4)"
      ],
      "limitation": "The performance expectation names growth and genetic factors. This case holds growth constant deliberately, the affected output is a signalling compound, and no genetic factor is investigated. Claim the explanation practice, not the performance expectation."
    },
    {
      "code": "MS-ETS1-1",
      "claim": "supporting",
      "assessingTasks": [8],
      "assessedPractice": "Writing two criteria for a schedule specification and naming one constraint reported in the case.",
      "learnerEvidence": [
        "Task 8 response — Criterion 1, dark hours per cycle, justified against the recorded five-hour minimum",
        "Task 8 response — Criterion 2, cycle stability",
        "Table 7 — the validated dark interval, the schedule with a two-year record, and the six-month reversibility window (Student page 6, Accessible page 8)",
        "Table 4 — the Day −93 power fluctuation, available as a reported constraint (Student page 2, Accessible page 2)"
      ],
      "limitation": "Supporting, not direct. The Student task does not ask students to account for impacts on people, and the runtime's cultural-significance record appears in no learner edition. Campaign 2 Case 03 rates its structurally similar final specification task as supporting."
    },
    {
      "code": "MS-ETS1-2",
      "claim": "supporting",
      "conditional": true,
      "assessingTasks": [8],
      "limitation": "Claim only if the class systematically compares restoring the six-hour schedule against adopting the five-hour recorded minimum using the same criteria and constraints. The packet as written asks for one specification with a justification, which is not a systematic comparison."
    }
  ],
  "withdrawnStandards": [
    {
      "code": "MS-LS1-5",
      "claimedIn": "1.0",
      "claimedAs": "direct",
      "withdrawnIn": "1.1",
      "retainedAs": "supporting",
      "reason": "The performance expectation concerns environmental and genetic factors affecting organism growth. This case deliberately holds growth constant and uses a signalling and function outcome instead, and the packet's own assessment boundary instructs teachers not to report growth evidence from it. A boundary note cannot turn a mismatched performance expectation into a direct standard. No standard replaces the direct claim."
    },
    {
      "code": "MS-ETS1-1",
      "claimedIn": "1.0",
      "claimedAs": "direct",
      "withdrawnIn": "1.1",
      "retainedAs": "supporting",
      "reason": "The v1.0 justification rested partly on Task 8 accounting for impacts on the people who live with the grove. The Student task sets no such expectation, and the cultural-significance record that would support it is runtime-only. Task 8 was not enlarged in order to preserve the direct rating."
    },
    {
      "code": "mathematics",
      "reason": "The packet requires no calculation anywhere; the reasoning is comparative and temporal."
    }
  ],
  "learnerEvidencePolicy": {
    "rule": "Every graded Answer Key expectation and every clause of the CER exemplar must be producible from the Student edition alone and, independently, from the Accessible edition alone, using evidence printed on or before the page of the task that assesses it.",
    "suppliedToLearners": [
      "Day −93", "Day −90", "Day −83", "Day −80",
      "power fluctuation", "no other", "no structural decline", "measurable threshold",
      "24.0 h on / 0.0 h off", "18 h on / 6 h off", "0.0 ppb", "40–80 ppb",
      "five dark hours", "six dark hours", "six months", "Hours 19–24", "Hours 6–12",
      "target range", "set to preserve", "structurally sound", "entrained"
    ],
    "withheldFromLearners": [
      "culturally significant", "sacred", "the grove's historical light intensity before Day −90"
    ],
    "teacherOnly": [
      "The runtime record that the grove is culturally significant to the Thal-Oren community — discussion context only, never a graded requirement",
      "The 7–10 day suppression window, which is printed at Task 8 and therefore may not be required by the Task 7 CER exemplar"
    ],
    "note": "Task 1 classification evidence is repeated as a compact change record on the page of Task 1 in both learner editions. The Accessible edition carries a condensed Table 4 on the Task 2 page rather than the Student's five-row day-by-day table."
  },
  "correctDiagnosis": "Removing the recurring dark interval removed the timing cue that this grove's recorded signalling cycle is entrained to, so measured output fell to the reporting threshold while the three organisms stayed structurally healthy.",
  "incorrectAlternatives": [
    "the chemical scrubbers have drifted out of their target range and are filtering the signalling compounds out of the air",
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
    "intensity has stayed at 100% throughout",
    "the light intensity did not change",
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
    "Do not generalise this grove's dark-interval requirement to plants as a whole.",
    "Report the 100% intensity reading as a current value only. The records do not report the intensity before Day -90, so no role may state that intensity stayed the same or never changed.",
    "Keep the filtration alternative's causal direction: the runtime states that chemical filtering has drifted out of range, not that a correctly set system is removing the compounds."
  ]
};
