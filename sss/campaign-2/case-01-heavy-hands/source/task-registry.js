window.SSS_C2_CASE01_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C2-CASE01",
  "title": "Heavy Hands",
  "version": "1.1",
  "status": "OWNER_GATE_OPEN",
  "correctiveOf": "1.0",
  "ownerReviewStatus": "OWNER_REVIEW_IN_PROGRESS",
  "printStatus": "NOT_RUN",
  "editorShell": "1.0",
  "gameCommit": "29c3b222c53f51de11a3aa83e896a6d0ef6fb490",
  "runtimeCaseId": "heavy_hands",
  "runtimeInvestigationName": "Vressk Centrifuge Habitat",
  "runtimeLocation": "Kepler-442b Orbit",
  "runtimeSubtitle": "Vressk Territory",
  "roles": {
    "student": 5,
    "teacher": 9,
    "answer": 4,
    "accessible": 8
  },
  "tasks": [
    {
      "id": "C2-C01-T1",
      "number": "1",
      "semanticLabel": "REFERENCE",
      "icon": "ph-book",
      "title": "Frame What Has Already Been Tested",
      "description": "Separate the two conditions the botanist actually changed across three plantings from the conditions merely reported at a present value, record that a present reading is not a completed test, and state why a correct midpoint reading still leaves the problem open.",
      "keyed": true
    },
    {
      "id": "C2-C01-T2",
      "number": "2",
      "semanticLabel": "WARM-UP",
      "icon": "ph-book",
      "title": "Ride the Merry-Go-Round",
      "description": "Use a merry-go-round with invented, friendly values to establish that the pull grows with distance from the centre, and that anything long enough to span several positions feels more than one value at once.",
      "keyed": true
    },
    {
      "id": "C2-C01-T3",
      "number": "3",
      "semanticLabel": "INVESTIGATION",
      "icon": "ph-nodes",
      "title": "Think Like the Investigator",
      "description": "Take the botanist's correct single-point reading and decide what to ask next, where else to measure, and what the habitat rule failed to say.",
      "keyed": true
    },
    {
      "id": "C2-C01-T4",
      "number": "4",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-nodes",
      "title": "Why the Biggest Tubers Bend Most",
      "description": "Use the observation that larger tubers deform more to connect how much of the bed an organ spans to how much difference it feels, and state why that pattern discriminates among the candidate causes.",
      "keyed": true
    },
    {
      "id": "C2-C01-T5",
      "number": "5",
      "semanticLabel": "EVIDENCE SYNTHESIS",
      "icon": "ph-nodes",
      "title": "Connect the Five Evidence Sources",
      "description": "Give every formal evidence source an instructional role by stating its contribution to the diagnosis and its limit if used alone.",
      "keyed": true
    },
    {
      "id": "C2-C01-T6",
      "number": "6",
      "semanticLabel": "DIAGNOSIS",
      "icon": "ph-diagnosis",
      "title": "Diagnose and Reject Alternatives",
      "description": "Select the best-supported diagnosis, reject the three alternatives with evidence, and complete the condition-mechanism-effect model.",
      "keyed": true
    },
    {
      "id": "C2-C01-T7",
      "number": "7",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Explain the Diagnosis with CER",
      "description": "Write a Claim-Evidence-Reasoning explanation using evidence from more than one source and preserving the boundary between established Earth science and case-specific evidence.",
      "keyed": true
    },
    {
      "id": "C2-C01-T8",
      "number": "8",
      "semanticLabel": "ENGINEERING DESIGN",
      "icon": "ph-wrench",
      "title": "Write the Missing Habitat Specification",
      "description": "Write the across-bed criterion the original specification omitted, compare a larger ring against a thinner bed using the same criteria and the stated constraint, and define a monitored trial with a stop-and-revise rule.",
      "keyed": true
    }
  ],
  "formalClues": [
    "GORLROOT_UPWARD",
    "GRAVITY_GRADIENT",
    "TUBERS_MISALIGNED",
    "GORLROOT_NEEDS_UNIFORM_G",
    "CENTRIFUGAL_GRADIENT_KNOWN"
  ],
  "clueTaskCoverage": {
    "GORLROOT_UPWARD": [1, 5],
    "GRAVITY_GRADIENT": [2, 3, 5],
    "TUBERS_MISALIGNED": [4, 5, 6],
    "GORLROOT_NEEDS_UNIFORM_G": [1, 5, 6],
    "CENTRIFUGAL_GRADIENT_KNOWN": [5, 8]
  },
  "requiredRoutes": [
    "crew.start->problem_main",
    "sensors.start->gravity_profile",
    "plants.start->tuber_orientation",
    "logs.start->gorlroot_cultivation",
    "database.start->centrifugal_gradient"
  ],
  "sourceLedger": [
    {
      "source": "Vressk Botanist",
      "clue": "GORLROOT_UPWARD",
      "establishes": "Primary roots point outward toward the ring wall, the correct down direction, while swelling tubers buckle sideways and break the soil surface; soil was reformulated for Crop 2 and new seed stock used for Crop 3, each without effect; nutrients, light and water are reported at present values that were never varied between plantings.",
      "cannotEstablishAlone": "Does not identify the acceleration gradient, because the botanist measured only the midpoint. A condition reported at a present value has not been tested and is not ruled out."
    },
    {
      "source": "Centrifuge Sensor Array",
      "clue": "GRAVITY_GRADIENT",
      "establishes": "At one stable rotation rate the reported outward magnitude rises across the radial depth of the bed, and the direction is reported as radially outward at all three sampled radii.",
      "cannotEstablishAlone": "Does not show that any organism responds to a difference that small."
    },
    {
      "source": "Gorlroot Specimen",
      "clue": "TUBERS_MISALIGNED",
      "establishes": "Deformation increases with tuber diameter rather than pointing toward or away from the axis, so the response tracks how much radial depth an organ spans.",
      "cannotEstablishAlone": "Does not by itself establish which environmental variable produces the pattern."
    },
    {
      "source": "Vressk Botanical Archive",
      "clue": "GORLROOT_NEEDS_UNIFORM_G",
      "establishes": "Every Vressk cultivation record assumes a planetary field, gorlroot had never been grown off-world before this installation, and the habitat specification bounds the midpoint magnitude only.",
      "cannotEstablishAlone": "Does not measure what the habitat actually delivers across the bed."
    },
    {
      "source": "Federation Database",
      "clue": "CENTRIFUGAL_GRADIENT_KNOWN",
      "establishes": "Concord engineering records state that magnitude increases with distance from the axis, that a midpoint-only specification can hide a difference across a deep bed, and that two earlier centrifuge crops responded differently to the same design question.",
      "cannotEstablishAlone": "Does not establish that this habitat and this crop reproduce the recorded precedent without site measurements."
    }
  ],
  "historicalControls": [
    {
      "condition": "Soil mineral formulation",
      "changedBetweenPlantings": true,
      "canonicalSource": "Centrifuge Sensor Array historical log; Vressk Botanist",
      "canonicalEvidence": "Crop 2 (day 46–90): soil reformulated to the Vress mineral profile. Same result, day 10.",
      "learnerVisible": true,
      "answerKeyMark": "Y",
      "ruledOut": false
    },
    {
      "condition": "Seed stock",
      "changedBetweenPlantings": true,
      "canonicalSource": "Centrifuge Sensor Array historical log; Vressk Botanist",
      "canonicalEvidence": "Crop 3 (day 91–now): new seed stock. Misalignment day 11.",
      "learnerVisible": true,
      "answerKeyMark": "Y",
      "ruledOut": false
    },
    {
      "condition": "Nutrient supply",
      "changedBetweenPlantings": false,
      "reportedAsPresentCondition": true,
      "canonicalSource": "Vressk Botanist",
      "canonicalEvidence": "\"Nutrients: precise.\" A present condition, not an intervention in any planting.",
      "learnerVisible": true,
      "answerKeyMark": "N",
      "ruledOut": false
    },
    {
      "condition": "Grow-light spectrum",
      "changedBetweenPlantings": false,
      "reportedAsPresentCondition": true,
      "canonicalSource": "Vressk Botanist",
      "canonicalEvidence": "\"Light: calibrated to Vress-standard grow spectrum.\" A present condition, not an intervention in any planting.",
      "learnerVisible": true,
      "answerKeyMark": "N",
      "ruledOut": false
    },
    {
      "condition": "Water supply",
      "changedBetweenPlantings": false,
      "reportedAsPresentCondition": true,
      "canonicalSource": "Vressk Botanist",
      "canonicalEvidence": "\"Water: clean.\" A present condition. It is not a tested historical variable and no Table 2 row asks about it.",
      "learnerVisible": true,
      "answerKeyMark": null,
      "ruledOut": false
    },
    {
      "condition": "Ring radius and rotation rate",
      "changedBetweenPlantings": false,
      "reportedAsPresentCondition": true,
      "canonicalSource": "Centrifuge Sensor Array; Vressk Botanical Archive",
      "canonicalEvidence": "Rotation reported stable and the midpoint calibrated once. Never changed across the three plantings, and only ever measured at the midpoint.",
      "learnerVisible": true,
      "answerKeyMark": "N",
      "ruledOut": false
    }
  ],
  "controlsPolicy": "No role may state or imply that nutrients, light, water, vibration or wobble were changed, tested, verified or ruled out. The game reports nutrients, light and water as present conditions only, and reports no vibration or wobble from the botanist rather than from the sensor array's Ring Status: NOMINAL. A present reading is never evidence that a condition did not contribute.",
  "standards": [
    {
      "code": "MS-LS1-5",
      "claim": "direct",
      "assessingTasks": [1, 7],
      "learnerEvidence": [
        "Table 1 — Crop 3 planted from new seed stock, deformation returning on day 11 (the varied genetic factor)",
        "Table 2 — ring radius and rotation rate recorded as never changed (the unvaried environmental factor)",
        "Task 7 CER — an evidence-based explanation of the growth outcome that uses both"
      ]
    },
    {
      "code": "MS-ETS1-1",
      "claim": "direct",
      "assessingTasks": [8],
      "learnerEvidence": [
        "Task 8 response — the across-bed criterion the specification left out",
        "Task 8 response — one constraint reported in this case",
        "Table 7 — the reported constraints on each proposal"
      ]
    },
    {
      "code": "MS-ETS1-2",
      "claim": "supporting",
      "conditional": true,
      "assessingTasks": [8],
      "limitation": "Claim only if the class systematically compares the larger ring against the thinner bed using the same criterion and the same constraint. Table 7 sets the comparison up; the packet as written does not force it."
    }
  ],
  "withdrawnStandards": [
    {
      "code": "MS-ETS1-3",
      "claimedIn": "1.0",
      "withdrawnIn": "1.1",
      "reason": "Justified by Concord records GC-1208 and GC-1445, which are Teacher-facing and appear in no learner edition. No task asks students to analyse data from several design solutions or to combine the best characteristics into a new solution. No standard replaces it."
    },
    {
      "code": "mathematics",
      "reason": "The packet requires no calculation anywhere, and no task asks for arithmetic with any reported value."
    }
  ],
  "learnerEvidencePolicy": {
    "rule": "Every graded Answer Key expectation and every clause of the CER exemplar must be producible from the Student edition alone and, independently, from the Accessible edition alone. A value first printed at a later task may not be required to answer an earlier one.",
    "suppliedToLearners": ["2.10 g", "±0.05 g", "20 cm", "600 m", "GC-1208", "Day 10", "Day 11", "Day 12"],
    "withheldFromLearners": ["0.00187", "2.0991", "2.1009", "224.8", "224.9", "225.0", "2.88966", "0.3%", "80 m", "300 m", "GC-1445", "0.0018", "a = ω²r"],
    "teacherOnly": [
      "The three sampled radii and their magnitudes, the directly reported across-bed difference, and the rotation rate",
      "The rounded-endpoint subtraction and the reason the directly reported difference keeps a fifth digit",
      "The two Concord centrifuge records GC-1208 and GC-1445 and their radii",
      "The 0.3% soil match and the tabulated atmosphere, temperature and humidity readings"
    ],
    "note": "Learners meet the acceleration relationship through the labelled merry-go-round and through the qualitative three-place result on Student page 2 and Accessible page 3. That is deliberate and is the reason the raw profile stays in the Teacher Guide."
  },
  "numericalLedger": {
    "relationship": "a = ω²r",
    "standardGravityMps2": 9.80665,
    "rotationRpm": "2.88966",
    "rotationStability": "±0.00001",
    "bedDepthM": 0.2,
    "bedDepthCm": 20,
    "profile": [
      {"position": "Bed top (surface side)", "radiusM": "224.8", "accelerationG": "2.0991", "direction": "outward"},
      {"position": "Bed midpoint (calibration point)", "radiusM": "224.9", "accelerationG": "2.10", "direction": "outward"},
      {"position": "Bed base (ring-wall side)", "radiusM": "225.0", "accelerationG": "2.1009", "direction": "outward"}
    ],
    "reportedDifferenceG": "0.00187",
    "differenceOfRoundedEndpointsG": "0.0018",
    "roundingNote": "Subtracting the two four-decimal endpoint values gives 0.0018 g. The array reports the difference directly as 0.00187 g. The directly reported difference carries more digits because it is not built from two rounded numbers. The two values do not conflict.",
    "specification": {
      "text": "2.10 g ±0.05 g at midpoint",
      "boundsMidpointOnly": true,
      "acrossBedToleranceSpecified": false
    },
    "habitatConditions": {
      "temperatureC": 22.4,
      "humidityPercent": 68,
      "oxygenPercent": 21.0,
      "carbonDioxidePpm": 800,
      "nitrogenPercent": 78.2,
      "pressureAtm": 1.08,
      "ringStatus": "Ring Status: NOMINAL (sensor array). The botanist separately reports the RPM steady with no vibration and no wobble; the array reports no such absence."
    },
    "cultivationStandard": {
      "gravity": "2.1 g uniform planetary field",
      "pH": "6.2–6.8",
      "temperatureC": "18–24",
      "humidityPercent": "60–75",
      "soilMatch": "within 0.3% of Vress surface regolith"
    },
    "crops": [
      {"crop": "Crop 1", "days": "0–45", "changed": "none (baseline planting)", "onsetDay": 12},
      {"crop": "Crop 2", "days": "46–90", "changed": "soil reformulated", "onsetDay": 10},
      {"crop": "Crop 3", "days": "91–now", "changed": "new seed stock", "onsetDay": 11}
    ],
    "precedents": [
      {"record": "GC-1208", "crop": "Telluvian root-vine", "radiusM": 80, "outcome": "misalignment matching this case", "resolution": "radius extended to 600 m"},
      {"record": "GC-1445", "crop": "Oolian kelp", "radiusM": 300, "outcome": "no misalignment reported, with the record's qualifier: low gravitropic precision", "qualifier": "low gravitropic precision", "conclusion": "gradient sensitivity is species-dependent", "resolution": "none required", "role": "Teacher-facing counter-example only. Not evidence that a 300 m radius prevents misalignment, and not evidence about gorlroot."}
    ]
  },
  "sourceStatus": {
    "establishedEarthScienceComparison": "In a rotating frame the apparent acceleration follows a = ω²r, so at one rotation rate the magnitude grows with distance from the axis; for a chosen target magnitude a larger radius allows a lower rotation rate. Earth plants orient growth using gravity-sensing tissue, including statolith-bearing cells.",
    "caseSpecificEvidence": "The habitat radius, rotation rate, bed depth, the three reported acceleration magnitudes and their difference, the gorlroot growth-control response, the Vressk cultivation records, and the two Concord centrifuge precedents.",
    "numbers": "game-provided measurements",
    "figures": "curriculum-original",
    "teachingAnalogy": "Task 2 uses a merry-go-round with three riders and invented pull values of 2, 5 and 8. Those values teach the relationship only. They are labelled in the printable content as not being measurements from the habitat, and they never appear as case evidence."
  },
  "correctDiagnosis": "At one rotation rate the outward acceleration magnitude increases across the radial depth of the bed, and the gorlroot growth-control system responds to that difference across a swelling tuber by growing its two sides unequally, which curves the tuber sideways.",
  "incorrectAlternatives": [
    "the centrifuge is calibrated too strong, so the crop is above 2.1 g",
    "the soil nutrients do not match the homeworld composition",
    "the soil bed is too shallow for the root system"
  ],
  "prohibitedClaims": [
    "down points in different directions across the bed",
    "the direction of the apparent gravity reverses between the bed top and the bed base",
    "the acceleration vector rotates across the bed",
    "the habitat is calibrated too strong",
    "the midpoint calibration is wrong",
    "the tubers grow upward",
    "the tubers point toward the rotation axis",
    "Earth plants detect a difference this small",
    "all plants sense acceleration gradients",
    "the Coriolis effect causes the deformation",
    "centrifugal gravity is not real gravity",
    "a larger ring is guaranteed to fix the problem",
    "the reported difference is the detection threshold for gravity sensing",
    "the two reported difference values contradict each other",
    "negligible means zero",
    "one measurement alone proves the diagnosis",
    "correlation alone proves causation"
  ],
  "figureProvenance": [
    {
      "id": "fig-profile",
      "kind": "curriculum-original inline SVG",
      "shows": "A radial section of the soil bed with the three sampled radii labelled, each carrying an outward arrow of the same direction and its own reported magnitude.",
      "prohibited": "No arrow may point in a different direction from the others, no continuous field is drawn, and no unreported radius is labelled."
    },
    {
      "id": "fig-span",
      "kind": "curriculum-original inline SVG",
      "shows": "Three tuber outlines of increasing diameter against the same radial depth scale, showing how much of the bed depth each one spans.",
      "prohibited": "No numeric deformation value is shown, because none is reported; the comparison stays qualitative and patterned rather than colour-coded."
    }
  ],
  "productionCautions": [
    "Direction is reported as outward at every sampled radius. Never describe the difference as a change of direction, a tilt of the field, or a rotation of down.",
    "Preserve the reported precision: 2.0991 g and 2.1009 g at four decimals, 0.00187 g at five, 2.88966 RPM at five.",
    "Do not present 0.0018 g and 0.00187 g as conflicting; the first is a difference of rounded endpoints and the second is reported directly.",
    "The 'negligible' bed-scale judgement belongs to the botanist, not to the archive. Attribute it to the botanist, and do not convert it into a number; none is reported.",
    "The packet requires no calculation. a = ω²r is named once so students know the relationship exists; it is never evaluated, and no task asks for arithmetic with the reported values.",
    "The rounding relationship between 0.0018 g and 0.00187 g is Teacher-facing only, offered as an optional extension. Do not promote it into a student task; it is interesting enough to displace the biology.",
    "The habitat's reported magnitudes differ by less than a tenth of one percent because a 0.2 m bed sits in a 224.9 m radius. That is unavoidable: a ring with a classroom-friendly spread would need a radius of about 2 m, roughly 4 m across, and would have to spin near 30 RPM. Learners therefore meet the relationship through the labelled merry-go-round analogy, and the reported values appear as reference evidence rather than as arithmetic.",
    "Do not invent a deformation quantity. The specimen record reports only that deformation increases with tuber diameter.",
    "Keep the gorlroot growth-control response as case evidence rather than established Earth plant biology."
  ]
};
