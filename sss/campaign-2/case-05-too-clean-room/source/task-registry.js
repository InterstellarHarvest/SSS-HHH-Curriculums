window.SSS_C2_CASE05_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C2-CASE05",
  "title": "Too Clean a Room",
  "version": "1.2",
  "status": "APPROVED_STABLE",
  "correctiveOf": "1.1",
  "approvalDate": "2026-08-10",
  "approvedBy": "Nate / Owner",
  "ownerReviewStatus": "OWNER_REVIEW_PASS",
  "mergeStatus": "READY_TO_MERGE",
  "editorShell": "1.0",
  "gameCommit": "29c3b222c53f51de11a3aa83e896a6d0ef6fb490",
  "runtimeCaseId": "too_clean_room",
  "runtimeInvestigationName": "Concord Botanical Vault",
  "runtimeLocation": "Lagrange Point 5",
  "runtimeSubtitle": "Concord Neutral Zone",
  "roles": {
    "student": 7,
    "teacher": 9,
    "answer": 5,
    "accessible": 7
  },
  "tasks": [
    {
      "id": "C2-C05-T1",
      "number": "1",
      "semanticLabel": "REFERENCE",
      "icon": "ph-book",
      "title": "Sort What Was Specified from What Was Not",
      "description": "Separate the five vault conditions monitored against a karreth specification from the one condition the vault controlled but never wrote a biological specification for, and explain why an all-optimal report is not evidence that nothing is wrong.",
      "keyed": true
    },
    {
      "id": "C2-C05-T2",
      "number": "2",
      "semanticLabel": "DATA ANALYSIS",
      "icon": "ph-scales",
      "title": "What a Reading Can and Cannot Tell You",
      "description": "Use a whole-millimetre rain gauge to judge what a reading at a detection limit bounds, then separate absorbed dose in milligray from equivalent dose in sievert and a site record from a modeled average.",
      "keyed": true
    },
    {
      "id": "C2-C05-T3",
      "number": "3",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-nodes",
      "title": "Read the Decline and the Failed Adjustments",
      "description": "Identify the month production first falls below baseline, explain how a condition present from the first day can produce a decline that only appears later, and use five adjustments that produced no change as evidence.",
      "keyed": true
    },
    {
      "id": "C2-C05-T4",
      "number": "4",
      "semanticLabel": "EVIDENCE SYNTHESIS",
      "icon": "ph-ticket",
      "title": "Connect the Five Evidence Sources",
      "description": "State what each of the five sources contributes to the diagnosis and what it could not establish alone, then write one sentence for what the five together support.",
      "keyed": true
    },
    {
      "id": "C2-C05-T5",
      "number": "5",
      "semanticLabel": "DIAGNOSIS",
      "icon": "ph-diagnosis",
      "title": "Diagnose, Reject the Alternatives, and Model the Mechanism",
      "description": "Select the best-supported diagnosis, write the evidence that rules out each of the three alternatives, and complete the condition-mechanism-effect model in causal order.",
      "keyed": true
    },
    {
      "id": "C2-C05-T6",
      "number": "6",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Explain the Diagnosis with CER",
      "description": "Write a Claim-Evidence-Reasoning explanation using evidence from more than one source, keeping the boundary between established Earth radiation science and records made for this vault, and naming at least one thing the evidence does not establish.",
      "keyed": true
    },
    {
      "id": "C2-C05-T7",
      "number": "7",
      "semanticLabel": "ENGINEERING DESIGN",
      "icon": "ph-wrench",
      "title": "Specify a Monitored Trial and Recommend a Response",
      "description": "Define what the approved trial must measure and why it needs a chamber receiving no added exposure, name one constraint, justify finding a minimum effective exposure rather than copying the homeworld value, and recommend a response with a reason.",
      "keyed": true
    }
  ],
  "formalClues": [
    "BLOOMS_INERT",
    "RADIATION_ZERO",
    "DNA_REPAIR_PATHWAY_INACTIVE",
    "KARRETH_HOMEWORLD_HIGH_RAD",
    "HORMESIS_OBLIGATE_RADIATION"
  ],
  "clueTaskCoverage": {
    "BLOOMS_INERT": [
      1,
      3,
      4
    ],
    "RADIATION_ZERO": [
      1,
      2,
      4,
      5
    ],
    "DNA_REPAIR_PATHWAY_INACTIVE": [
      3,
      4,
      5
    ],
    "KARRETH_HOMEWORLD_HIGH_RAD": [
      2,
      4,
      5,
      7
    ],
    "HORMESIS_OBLIGATE_RADIATION": [
      4,
      5,
      6
    ]
  },
  "requiredRoutes": [
    "crew.start->what_tried",
    "sensors.start->radiation_data",
    "plants.start->tissue_analysis",
    "logs.start->homeworld",
    "database.start->hormesis"
  ],
  "sourceLedger": [
    {
      "source": "Vault Admin Kel-tor",
      "clue": "BLOOMS_INERT",
      "establishes": "The transplant timeline, that production has declined 94% since month three, and that every variable within the administrator's authority has been adjusted without effect.",
      "cannotEstablishAlone": "It is a statement of experience and suspicion. It measures nothing, and the administrator holds a hypothesis of their own."
    },
    {
      "source": "Vault Sensor Array",
      "clue": "RADIATION_ZERO",
      "establishes": "Every specified condition reads inside the karreth range, and absorbed dose at plant tissue reads below the monitor's 0.01 mGy/day detection limit.",
      "cannotEstablishAlone": "It reports an absence bounded by an instrument limit, not a biological requirement. On its own it is a clean report."
    },
    {
      "source": "Karreth Bloom Specimen",
      "clue": "DNA_REPAIR_PATHWAY_INACTIVE",
      "establishes": "Cell structure, membranes, organelles and nutrient uptake are normal, and the biosynthetic pathway is present but quiescent.",
      "cannotEstablishAlone": "It locates the failure as regulatory rather than structural. It does not identify what caused the pathway to stop."
    },
    {
      "source": "Karreth Transplant Records",
      "clue": "KARRETH_HOMEWORLD_HIGH_RAD",
      "establishes": "The homeworld site record of about 8.4 mGy/day absorbed by plant tissue in a mixed photon field, and that the shielding was recorded as far exceeding native conditions with no concern raised.",
      "cannotEstablishAlone": "A difference between two sites is not a cause, and a single surveyed site does not establish an optimum."
    },
    {
      "source": "Federation Database",
      "clue": "HORMESIS_OBLIGATE_RADIATION",
      "establishes": "A species-specific Concord category in which a low-level ionizing-radiation signal activates a repair cascade whose products include the medicinal compounds.",
      "cannotEstablishAlone": "It describes a category and states that its mechanisms are species-specific. It does not measure this bloom and does not generalize."
    }
  ],
  "numericalLedger": {
    "vaultEnvironment": {
      "temperature": "22.0 °C",
      "temperatureSpecification": "20–25 °C",
      "humidity": "55%",
      "humiditySpecification": "50–60%",
      "light": "14 h on / 10 h off",
      "lightSpecification": "12–16 h",
      "nutrients": "karreth mineral profile v4",
      "atmosphere": "standard Concord mix",
      "matchTolerance": "within 2%"
    },
    "dose": {
      "vaultReading": "<0.01 mGy/day",
      "vaultReadingStatus": "instrument reading at the monitor's detection limit; a bound, not zero and not 0.01",
      "homeworldSiteRecord": "about 8.4 mGy/day",
      "homeworldStatus": "site record for absorbed dose at plant tissue in a mixed photon field; not an optimum",
      "rhessiHabitat": "about 12 mGy/day",
      "rhessiStatus": "modeled average for a different species; not a direct reading",
      "unit": "absorbed dose in milligray per day; equivalent and effective dose in sievert are not used and cannot be derived from these values"
    },
    "production": {
      "month1": "100%",
      "month2": "100%",
      "month3": "68%",
      "month4": "31%",
      "month5": "11%",
      "month6": "6%",
      "baseline": "month 1–2 baseline",
      "administratorStatement": "94%",
      "shape": "six reported monthly values; no value is reported between months"
    },
    "specifications": {
      "shielding": "Tier-1",
      "protocol": "Protocol v3.2",
      "nutrientProfile": "profile v4",
      "transplantAge": "six months",
      "normalPeriod": "two months",
      "concordExamples": "5"
    },
    "teachingExample": {
      "gaugeResolution": "1 mm",
      "gaugeReading": "0 mm",
      "night1": "0.2 mm",
      "night2": "0.8 mm",
      "scaleMaximum": "5 mm",
      "status": "rain-gauge teaching example only; these values are not vault measurements and appear nowhere else in the packet"
    }
  },
  "sourceStatus": {
    "establishedEarthScience": "Ionizing radiation can break molecules, generate reactive species, and damage DNA. Absorbed dose is energy per unit mass, measured in gray; equivalent and effective dose in sievert add radiation and tissue weighting factors and are not interchangeable with absorbed dose. A reading below an instrument's detection limit bounds a value rather than measuring zero. Melanin is radioprotective in fungi.",
    "establishedEarthScienceComparison": "A 2007 laboratory study reported that ionizing radiation changed melanin's electronic properties and enhanced growth or metabolic activity in several melanized fungi under specific conditions, and proposed energy capture as a possibility. It does not establish radiation-powered photosynthesis, and it does not show that any fungus requires ionizing radiation.",
    "caseSpecificEvidence": "The karreth bloom, its compounds, the repair-linked pathway, the vault environmental record, the monthly production record, the vault dose reading, the homeworld site record, and Concord shielding policy are records made for this case.",
    "modeledEvidence": "The Rhessi habitat figure of about 12 mGy/day is a modeled average for a different species, offered as a comparison and carrying less weight than the surveyed site record.",
    "caseInference": "That the reduced exposure caused the pathway to become quiescent is the best-supported explanation from a two-condition contrast, a timeline, and a set of null results. It is not a demonstrated mechanism, which is why the packet ends in a controlled trial rather than a fix.",
    "engineeringExtrapolation": "The trial requirements in Task 7 — specialist authorization, a non-exposed control, dosimetry, retained shielding and interlocks, staged exposure, and written stop criteria — follow ordinary practice for work with a hazard rather than from any measurement in the case.",
    "numbers": "Every printed value is reproduced exactly as its record reports it. The vault dose keeps its inequality, the two comparison doses keep 'about', the six monthly percentages are never interpolated, and no value is converted between dose quantities.",
    "figures": "Both figures are curriculum-original. Figure A is a teaching example and says so in its caption; Figure B is the vault production record drawn as six discrete bars with nothing between them.",
    "teachingAnalogy": "The rain-gauge example carries the detection-limit idea without using any vault value, and prints a visible line stating that it is not a vault instrument."
  },
  "standards": [
    {
      "code": "MS-ETS1-1",
      "claim": "direct",
      "assessingTask": 7,
      "assessedPractice": "Asking Questions and Defining Problems — defining the criteria and constraints of a design problem with sufficient precision to guide a solution.",
      "learnerEvidence": "Table 7 prints the six requirements of the approved trial in both learner editions. Task 7 asks for two criteria, one constraint, the reason a staged trial must find a minimum rather than copy the homeworld value, and a recommendation with a reason.",
      "impactsOnPeople": "The briefing states in both learner editions that the compound treats a disease affecting several Concord species and that supplies are running out; Table 7 prints the authorization and retained-containment requirements that protect the people who would work near any exposure.",
      "limitation": "Students specify the trial. They do not build, run, or optimise a solution, and they never name a radiation source, device, or operating setting."
    },
    {
      "code": "MS-LS1-5",
      "claim": "supporting",
      "assessingTask": 6,
      "assessedPractice": "Constructing Explanations — an evidence-based explanation of how an environmental condition influences an organism.",
      "learnerEvidence": "Task 6 is a full-page Claim-Evidence-Reasoning explanation in both learner editions, drawing on the dose values in Table 2, the production record in Table 3 and Figure B, the null results in Table 4, and the five sources in Table 5.",
      "limitation": "The performance expectation names growth. The records here hold growth and tissue health unaffected; the affected output is a compound produced by a regulated biosynthetic pathway, which falls outside this standard's assessment boundary. The practice half is claimed; the performance expectation is not, and this claim is never reported as direct assessment."
    },
    {
      "code": "MS-ETS1-2",
      "claim": "conditional",
      "assessingTask": 7,
      "assessedPractice": "Evaluating competing design solutions against a shared set of criteria.",
      "learnerEvidence": "Task 7 names two real solutions — repair this vault only, or also add a species-specific validation step to Protocol v3.2 — so a class that compares them systematically has two genuine design solutions to evaluate.",
      "limitation": "Claim this only if the class systematically compares the two solutions using one shared set of criteria. The packet as written asks for a recommendation with a reason, which is not a systematic comparison, so the claim is conditional and is stated as conditional in the Teacher Guide."
    }
  ],
  "standardsPolicy": "Exactly three performance expectations are claimed, one as direct assessment and two with their limitations stated. No mathematics standard is claimed. No printable role reports a supporting or conditional claim as direct assessment.",
  "learnerEvidencePolicy": {
    "principle": "Every fact the Answer Key or the CER exemplar grades against, or accepts, must be printed in both learner editions on or before the page of the task that requires it.",
    "suppliedToBothLearnerEditions": [
      "The six vault conditions, their readings and their karreth specifications, and that Protocol v3.2 states no specification for ionizing radiation (Table 1, Task 1).",
      "The three dose values with their status — a reading at the detection limit, a surveyed site record, and a modeled average for a different species (Table 2, Task 2).",
      "The six reported monthly production values (Figure B and Table 3, Task 3).",
      "The five adjustments and their recorded null outcomes (Table 4, Task 3).",
      "The five sources and the observation each reports, including that cell structure and nutrient uptake are normal and the pathway is present but quiescent (Table 5, Task 4).",
      "The four diagnosis options in the same order (Table 6, Task 5).",
      "The six requirements of the approved trial (Table 7, Task 7).",
      "That the compound treats a disease affecting several Concord species and that supplies are running out (briefing, page 1)."
    ],
    "teacherOnly": [
      "Equivalent and effective dose, and the sievert quantities.",
      "Dose rate as a named term.",
      "The word 'control' before Task 7 introduces the idea.",
      "The melanin and 2007 melanized-fungi laboratory comparison.",
      "The internal hormesis clue tag."
    ],
    "withheldFromEveryRole": [
      "Any isotope, radiation source, device, or operating setting.",
      "Any absorbed dose restated in sievert, and any human risk figure.",
      "Any production value for a month the record does not report.",
      "Any staff exposure limit, specimen count, or other constraint no learner edition prints."
    ]
  },
  "correctDiagnosis": "The vault's shielding reduced absorbed dose at plant tissue below the level the species record associates with activity in the karreth repair-linked pathway, and that pathway — which produces the medicinal compounds downstream — became quiescent while the plant itself stayed healthy.",
  "incorrectAlternatives": [
    "The bloom is missing a trace element from its native soil that the vault's nutrient mix does not include.",
    "Ambient humidity or temperature is slightly off from karreth homeworld conditions.",
    "The bloom is experiencing delayed transplant shock and needs more time to acclimate."
  ],
  "prohibitedClaims": [
    "Describing ionizing radiation as a nutrient, food, or fuel for the bloom or for any plant.",
    "Claiming that plants in general need, require, or benefit from ionizing radiation.",
    "Claiming that low-dose ionizing radiation is beneficial or healthy for people.",
    "Claiming that ionizing radiation is generally good for Earth organisms.",
    "Claiming that DNA damage is beneficial, or that the case shows damage is harmless.",
    "Claiming that melanized fungi perform radiation-powered photosynthesis, or that radiosynthesis is established.",
    "Claiming that the melanized-fungi laboratory work shows any fungus requires ionizing radiation.",
    "Claiming that more exposure would produce more compound, or that a higher dose is better.",
    "Asserting that the bloom will recover, or that production will return, as a certainty.",
    "Treating the vault reading as absolute zero, as an absence of radiation, or as exactly 0.01 mGy/day.",
    "Presenting about 8.4 mGy/day as the optimal, required, or target exposure for the bloom.",
    "Presenting the modeled Rhessi figure of about 12 mGy/day as a direct measurement.",
    "Converting or restating absorbed dose in milligray as equivalent or effective dose in sievert, or as a human risk figure.",
    "Claiming the evidence establishes a dose-response curve or a response function from two dose conditions.",
    "Generalizing the karreth result to Earth plants, to other Concord species, or to humans.",
    "Attributing intention to the bloom, as though it decided, chose, or wanted to stop producing.",
    "Naming an isotope, a radiation source, a device, or an operating setting for any intervention.",
    "Claiming that radiation shielding is harmful, or that building the vault's shielding was itself the error rather than the missing species-specific review."
  ],
  "figureProvenance": [
    {
      "id": "fig-gauge-student",
      "kind": "curriculum-original teaching example",
      "shows": "Two rainfalls of 0.2 mm and 0.8 mm that both report as 0 mm on a gauge marked in whole millimetres, as discrete blocks inside a marked band.",
      "prohibited": "It must never be read as vault data, and its millimetre values must not appear outside the analogy block."
    },
    {
      "id": "fig-gauge-accessible",
      "kind": "curriculum-original teaching example",
      "shows": "The Accessible edition of the same rain-gauge comparison, with identical values and the same discrete blocks.",
      "prohibited": "It must never be read as vault data, and its millimetre values must not appear outside the analogy block."
    },
    {
      "id": "fig-production-student",
      "kind": "curriculum-original case record figure",
      "shows": "Six discrete bars giving karrethin production for months 1 to 6 as 100%, 100%, 68%, 31%, 11% and 6% of the month 1–2 baseline.",
      "prohibited": "No curve, trend line, or connector may join the bars, because the record reports one value per month and nothing between them."
    },
    {
      "id": "fig-production-accessible",
      "kind": "curriculum-original case record figure",
      "shows": "The Accessible edition of the same six monthly production bars, with identical values.",
      "prohibited": "No curve, trend line, or connector may join the bars, because the record reports one value per month and nothing between them."
    }
  ],
  "productionCautions": [
    "The design document for this case calls the mechanism 'radiation as nutrient' and proposes installing calibrated radiation sources. The shipped runtime supersedes both. The packet follows the runtime: a species-specific radiation-responsive pathway, and a licensed, shielded, monitored trial with controls and stop criteria.",
    "The internal clue tag and the database menu key both read 'hormesis', but the record they open is titled obligate radiation-triggered metabolism and carries an advisory that it is not a general claim about low-dose radiation. The word hormesis appears nowhere in the printable packet.",
    "No printable role may prescribe an isotope, a radiation source, a device, or an operating setting. Task 7 states on the page that those decisions belong to the qualified radiation-protection and radiological-engineering team.",
    "The vault dose reading must always travel with its detection-limit status. Stripping the inequality turns a bound into a measurement of zero, which is the central misconception of the case.",
    "The Rhessi comparison is modeled and belongs to a different species. It may support a comparison and must never be used as a measured value for the bloom.",
    "MS-LS1-5 is recorded as supporting rather than direct. The performance expectation names growth, and the records show growth and tissue health were unaffected; the affected output is a compound, and the mechanism is a regulated pathway that falls outside the standard's assessment boundary."
  ],
  "printStatus": "PASS"
};
