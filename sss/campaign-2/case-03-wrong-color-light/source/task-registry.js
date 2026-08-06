window.SSS_C2_CASE03_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C2-CASE03",
  "title": "The Wrong Color of Light",
  "version": "1.1",
  "status": "OWNER_GATE_OPEN",
  "ownerReviewStatus": "OWNER_REVIEW_IN_PROGRESS",
  "printStatus": "NOT_RUN",
  "correctiveOf": "1.0",
  "editorShell": "1.0",
  "gameCommit": "29c3b222c53f51de11a3aa83e896a6d0ef6fb490",
  "runtimeCaseId": "wrong_color_light",
  "runtimeInvestigationName": "Oolian Mariculture Dome",
  "runtimeLocation": "Trench Shelf IV",
  "runtimeSubtitle": "Kepler-186f (Ocean)",
  "roles": {
    "student": 5,
    "teacher": 8,
    "answer": 4,
    "accessible": 8
  },
  "tasks": [
    {
      "id": "C2-C03-T1",
      "number": "1",
      "semanticLabel": "REFERENCE",
      "icon": "ph-book",
      "title": "Frame What Changed",
      "description": "Separate the one variable that changed at Week 0 from the conditions the two domes held constant, and state why timing alone cannot identify a cause.",
      "keyed": true
    },
    {
      "id": "C2-C03-T2",
      "number": "2",
      "semanticLabel": "DATA ANALYSIS",
      "icon": "ph-scales",
      "title": "Read the GRO-9 Spectrum",
      "description": "Read the reported output categories and the separate total PAR value exactly, preserving inequalities and inferring no intermediate values.",
      "keyed": true
    },
    {
      "id": "C2-C03-T3",
      "number": "3",
      "semanticLabel": "DATA ANALYSIS",
      "icon": "ph-scales",
      "title": "Compare Lamp Output with Zhal-Kelp Response",
      "description": "Compare the installed lamp output with the recorded strongest-response band and write a qualified mismatch statement without inventing a curve or an overlap figure.",
      "keyed": true
    },
    {
      "id": "C2-C03-T4",
      "number": "4",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-nodes",
      "title": "Use the Timeline and Controls",
      "description": "Use the growth timeline, the dome conditions, and the old-dome control to weaken the water-chemistry and low-total-light explanations.",
      "keyed": true
    },
    {
      "id": "C2-C03-T5",
      "number": "5",
      "semanticLabel": "EVIDENCE SYNTHESIS",
      "icon": "ph-nodes",
      "title": "Connect the Five Evidence Sources",
      "description": "Give every formal evidence source an instructional role by stating its contribution to the diagnosis and its limit if used alone.",
      "keyed": true
    },
    {
      "id": "C2-C03-T6",
      "number": "6",
      "semanticLabel": "DIAGNOSIS",
      "icon": "ph-diagnosis",
      "title": "Diagnose and Reject Alternatives",
      "description": "Select the best-supported diagnosis, reject the alternatives with evidence, and complete the condition-mechanism-effect model.",
      "keyed": true
    },
    {
      "id": "C2-C03-T7",
      "number": "7",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Explain the Diagnosis with CER",
      "description": "Write a Claim-Evidence-Reasoning explanation using evidence from more than one source and preserving the boundary between established Earth science and case-specific evidence.",
      "keyed": true
    },
    {
      "id": "C2-C03-T8",
      "number": "8",
      "semanticLabel": "ENGINEERING DESIGN",
      "icon": "ph-wrench",
      "title": "Write a Better Lighting Specification",
      "description": "Define species-specific spectral and intensity criteria, one constraint, a monitored trial, and a stop-and-revise rule.",
      "keyed": true
    }
  ],
  "formalClues": [
    "KELP_DYING_NEW_DOME",
    "LIGHT_SPECTRUM_RED_HEAVY",
    "PIGMENT_MISMATCH",
    "KELP_EVOLVED_DEEP_OCEAN_LIGHT",
    "CHLOROPHYLL_C_BLUE_GREEN"
  ],
  "clueTaskCoverage": {
    "KELP_DYING_NEW_DOME": [1, 4, 5],
    "LIGHT_SPECTRUM_RED_HEAVY": [2, 3, 5],
    "PIGMENT_MISMATCH": [5, 6],
    "KELP_EVOLVED_DEEP_OCEAN_LIGHT": [3, 5],
    "CHLOROPHYLL_C_BLUE_GREEN": [5, 6]
  },
  "requiredRoutes": [
    "crew.start->problem_main",
    "sensors.start->spectral_analysis",
    "plants.start->magnification",
    "logs.start->kelp_profile",
    "database.start->chlorophyll_variants"
  ],
  "sourceLedger": [
    {
      "source": "Aquaculturist Tei-sal",
      "clue": "KELP_DYING_NEW_DOME",
      "establishes": "Decline begins after the switch from Oolian to Earth-manufactured fixtures; the old dome controls water, temperature, salinity, and species.",
      "cannotEstablishAlone": "Does not identify spectrum as the mechanism."
    },
    {
      "source": "Dome Sensor Array",
      "clue": "LIGHT_SPECTRUM_RED_HEAVY",
      "establishes": "GRO-9 is red-heavy, total PAR is adequate, and reported output in the recorded strongest-response band is under 5%.",
      "cannotEstablishAlone": "Does not prove that all other wavelengths are unused or that plant and water evidence is irrelevant."
    },
    {
      "source": "Zhal-Kelp Specimen",
      "clue": "PIGMENT_MISMATCH",
      "establishes": "Photosynthetic structures are present and intact; the pigment profile is measured to harvest blue-green wavelengths efficiently.",
      "cannotEstablishAlone": "Does not independently prove that light is the only causal variable."
    },
    {
      "source": "Oolian Aquaculture Records",
      "clue": "KELP_EVOLVED_DEEP_OCEAN_LIGHT",
      "establishes": "Site-specific habitat record reports blue-green-dominant light with little red at surveyed beds at 40-120 m; strongest measured response is 460-540 nm.",
      "cannotEstablishAlone": "Does not establish a universal Earth-algae depth profile or a universal kelp action spectrum."
    },
    {
      "source": "Federation Database",
      "clue": "CHLOROPHYLL_C_BLUE_GREEN",
      "establishes": "Brown algae use chlorophyll a and c with accessory pigments such as fucoxanthin; total PAR alone does not establish an effective spectrum.",
      "cannotEstablishAlone": "Does not turn the alien measurements into established Earth biology."
    }
  ],
  "numericalLedger": {
    "unit": "umol m-2 s-1",
    "totalPar": 280,
    "totalParStatus": "reported adequate",
    "gro9": {
      "redPercent": 62,
      "redBandNm": [620, 680],
      "bluePercent": 18,
      "blueBandNm": [440, 490],
      "broadPercent": 15,
      "blueGreenPercent": "<5",
      "blueGreenBandNm": [490, 560],
      "reportedOutputInResponseBand": "<5%"
    },
    "oms4": {
      "blueGreenPercent": 78,
      "blueGreenBandNm": [460, 540],
      "bluePercent": 12,
      "blueBandNm": [440, 460],
      "broadPercent": 10,
      "redPercent": "<1"
    },
    "zhalKelp": {
      "strongestMeasuredResponseNm": [460, 540],
      "recordedHabitatDepthM": [40, 120],
      "habitatSpectrum": "predominantly blue-green with little red at the recorded beds"
    },
    "domeConditions": {
      "waterTemperatureC": 4.2,
      "salinityPpt": 34.8,
      "pressureAtm": 12.4,
      "pH": 8.1,
      "dissolvedOxygenMgPerL": 7.2,
      "nutrients": "within Oolian mariculture specification",
      "heavyMetals": "below detection"
    },
    "timeline": {
      "week0": "GRO-9 replaces OMS-4",
      "week1": "Blade-tip yellowing detected",
      "week2": "Yellowing spreads to mid-blade",
      "week3": "Growth rate drops 60%",
      "week6": "Growth rate at 15% of nominal",
      "oldDomeControlPercent": 100
    },
    "excludedFromStudentWork": {
      "approximateEffectivePar": 14,
      "reason": "The runtime reports this value as approximate and does not report how it was obtained. It is not an exact organism-level action-spectrum result and is never used in student calculations."
    }
  },
  "sourceStatus": {
    "establishedEarthScienceComparison": "Brown algae use chlorophyll a and c with accessory pigments such as fucoxanthin; photosynthetic systems differ in wavelength response; water and dissolved or suspended material filter spectra.",
    "caseSpecificEvidence": "Zhal-kelp accessory pigments, the 460-540 nm strongest measured response band, the site habitat profile, and the comparative efficiency values.",
    "numbers": "game-provided measurements",
    "figures": "curriculum-original"
  },
  "correctDiagnosis": "The installed red-heavy lamps are a poor match for the zhal-kelp response measured at this site, so captured energy is much lower than the total brightness suggests.",
  "incorrectAlternatives": [
    "the Earth-manufactured lights are defective",
    "total intensity is too low",
    "water chemistry drifted out of range"
  ],
  "prohibitedClaims": [
    "kelp cannot use red light",
    "red light is absolutely unused",
    "red photons pass through all kelp unused",
    "red light is equivalent to darkness",
    "all brown algae share one action spectrum",
    "the 460-540 nm band is the only usable range",
    "one spectral percentage alone proves the diagnosis",
    "the approximate 14 umol/m2/s value is exact effective PAR",
    "the predicted recovery within days is a guaranteed experimental result",
    "below detection equals zero",
    "correlation alone proves causation"
  ],
  "figureProvenance": [
    {
      "id": "fig-gro9",
      "kind": "curriculum-original inline SVG",
      "shows": "Four reported GRO-9 output categories as discrete patterned bars with direct values.",
      "prohibited": "No continuous spectrum, no interpolated categories, no colour-only encoding."
    },
    {
      "id": "fig-band",
      "kind": "curriculum-original inline SVG",
      "shows": "The 460-540 nm strongest measured response band against the GRO-9 reported bands on a wavelength scale.",
      "prohibited": "No action-spectrum curve, no zero baseline, no claim that response outside the band is zero."
    }
  ],
  "productionCautions": [
    "Do not geometrically infer spectral overlap from the reported category bins.",
    "Do not require any student calculation using the approximate effective-PAR estimate.",
    "Do not sum or interpolate unreported values.",
    "Preserve <5% and <1% as inequalities.",
    "Do not treat below detection as zero."
  ]
};
