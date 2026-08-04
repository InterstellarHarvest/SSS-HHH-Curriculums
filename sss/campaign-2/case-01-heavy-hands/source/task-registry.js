window.SSS_C2_CASE01_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C2-CASE01",
  "title": "Heavy Hands",
  "version": "1.0",
  "status": "DRAFT",
  "approvalDate": null,
  "approvedBy": null,
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "mergeStatus": "NOT_READY",
  "editorShell": "1.0",
  "gameCommit": "29c3b222c53f51de11a3aa83e896a6d0ef6fb490",
  "runtimeCaseId": "heavy_hands",
  "runtimeInvestigationName": "Vressk Centrifuge Habitat",
  "runtimeLocation": "Kepler-442b Orbit",
  "runtimeSubtitle": "Vressk Territory",
  "roles": {
    "student": 5,
    "teacher": 8,
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
      "description": "Separate the variables the botanist already changed across three crops from the one condition never changed, and state why a correct midpoint reading still leaves the problem open.",
      "keyed": true
    },
    {
      "id": "C2-C01-T2",
      "number": "2",
      "semanticLabel": "DATA ANALYSIS",
      "icon": "ph-scales",
      "title": "Read the Gravity Profile",
      "description": "Read the three reported radii and their acceleration magnitudes exactly, record the reported difference at full precision, and state what the profile reports about direction.",
      "keyed": true
    },
    {
      "id": "C2-C01-T3",
      "number": "3",
      "semanticLabel": "MATHEMATICAL REASONING",
      "icon": "ph-scales",
      "title": "Use a = ω²r Across the Bed",
      "description": "Apply the given relationship at one fixed rotation rate to show the two ends of the bed cannot share one magnitude, then compare a difference of rounded endpoints with the directly reported difference.",
      "keyed": true
    },
    {
      "id": "C2-C01-T4",
      "number": "4",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-nodes",
      "title": "Explain the Size Pattern",
      "description": "Use the observation that larger tubers deform more to connect radial span to the magnitude difference a single organ samples, and state why that pattern discriminates among the candidate causes.",
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
      "establishes": "Primary roots point outward toward the ring wall, the correct down direction, while swelling tubers buckle sideways and break the soil surface; soil, nutrients, light, water, and seed stock were each changed without effect across three crops.",
      "cannotEstablishAlone": "Does not identify the acceleration gradient, because the botanist measured only the midpoint."
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
      "ringStatus": "nominal, no vibration and no wobble reported"
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
      {"record": "GC-1445", "crop": "Oolian kelp", "radiusM": 300, "outcome": "no misalignment reported", "resolution": "none required"}
    ]
  },
  "sourceStatus": {
    "establishedEarthScienceComparison": "In a rotating frame the apparent acceleration follows a = ω²r, so at one rotation rate the magnitude grows with distance from the axis; for a chosen target magnitude a larger radius allows a lower rotation rate. Earth plants orient growth using gravity-sensing tissue, including statolith-bearing cells.",
    "caseSpecificEvidence": "The habitat radius, rotation rate, bed depth, the three reported acceleration magnitudes and their difference, the gorlroot growth-control response, the Vressk cultivation records, and the two Concord centrifuge precedents.",
    "numbers": "game-provided measurements",
    "figures": "curriculum-original"
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
      "id": "fig-scale",
      "kind": "curriculum-original inline SVG",
      "shows": "The three reported magnitudes as discrete marked points on an expanded scale that does not start at zero, with the expansion stated in the caption.",
      "prohibited": "No connecting curve, no interpolated values between the marked points, and no implication that the scale begins at zero."
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
    "Do not convert the archive's 'negligible' bed-scale difference on a planet into a number; none is reported.",
    "Do not require any student calculation that needs the angular speed in radians per second; the runtime reports the rotation rate in RPM only.",
    "Do not invent a deformation quantity. The specimen record reports only that deformation increases with tuber diameter.",
    "Keep the gorlroot growth-control response as case evidence rather than established Earth plant biology."
  ]
};
