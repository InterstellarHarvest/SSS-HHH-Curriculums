window.SSS_CASE06_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C1-CASE06",
  "runtimeId": "alien1",
  "title": "First Contact Protocol",
  "version": "1.0",
  "status": "OWNER_GATE_OPEN",
  "ownerReviewStatus": "OWNER_REVIEW_PASS",
  "mergeStatus": "NOT_READY_TO_MERGE",
  "editorShell": "1.0",
  "gameCommit": "d723fb9b8085905a6048575a2cb3bb0fce1d312b",
  "roles": {
    "student": 5,
    "teacher": 8,
    "answer": 5,
    "accessible": 7
  },
  "tasks": [
    {
      "number": "1",
      "semanticLabel": "INITIAL THINKING",
      "icon": "ph-book",
      "title": "Predict What Changed at Docking",
      "description": "Make an initial prediction and identify information needed to test it.",
      "keyed": true
    },
    {
      "number": "2",
      "semanticLabel": "EVIDENCE CLASSIFICATION",
      "icon": "ph-scales",
      "title": "Separate Observation from Interpretation",
      "description": "Classify case statements and explain why an interpretation requires several observations.",
      "keyed": true
    },
    {
      "number": "3",
      "semanticLabel": "EVIDENCE SYNTHESIS",
      "icon": "ph-nodes",
      "title": "Connect the Four Evidence Sources",
      "description": "Explain what the liaison, interface array, cultivar inspection, and botanical archive contribute.",
      "keyed": true
    },
    {
      "number": "4",
      "semanticLabel": "SYSTEMS MODEL",
      "icon": "ph-flow",
      "title": "Model the Broken Coordination System",
      "description": "Map atmosphere, signal persistence, network response, and partnership outcome.",
      "keyed": true
    },
    {
      "number": "5",
      "semanticLabel": "DIAGNOSIS COMPARISON",
      "icon": "ph-diagnosis",
      "title": "Compare and Reject Competing Diagnoses",
      "description": "Test the best diagnosis and three distractors against converging evidence.",
      "keyed": true
    },
    {
      "number": "6",
      "semanticLabel": "SAFE INTERVENTION",
      "icon": "ph-wrench",
      "title": "Recommend a Monitored Signal-Safe Response",
      "description": "Compare responses using biological, engineering, and human-safety criteria and constraints.",
      "keyed": true
    },
    {
      "number": "7",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Explain the Diagnosis with CER",
      "description": "Write a qualified explanation using evidence from more than one source.",
      "keyed": true
    },
    {
      "number": "8",
      "semanticLabel": "TRANSFER AND EXIT",
      "icon": "ph-ticket",
      "title": "Transfer the Systems Reasoning",
      "description": "Apply the interaction model to a new fictional system and state the independent exit conclusion.",
      "keyed": true
    }
  ],
  "vocabulary": [
    "Chemical signal",
    "Dormancy",
    "Interpretation",
    "Observation",
    "Symbiosis",
    "Volatile compound"
  ],
  "formalClues": [
    "SYMBIOSIS_BROKEN",
    "HUMAN_SCRUBBERS_ACTIVE",
    "NETWORK_DORMANT",
    "VOC_SIGNALING"
  ],
  "requiredRoutes": [
    "crew.start->symbiosis_detail",
    "sensors.start->atmosphere",
    "plants.start->network",
    "logs.start->network_comm"
  ],
  "correctDiagnosis": "human atmospheric processing filtered the volatile signal compounds, triggering network dormancy and loss of symbiosis coordination",
  "incorrectAlternatives": [
    "physical docking damage",
    "atmospheric drift during the journey",
    "incompatibility among the three organisms"
  ],
  "timingLedger": {
    "dockingHoursAgo": 72.4,
    "lastSignalHoursAgo": 72.1,
    "differenceHours": 0.3,
    "differenceMinutes": 18,
    "qualification": "Correlation supports the investigation but does not alone establish causation."
  },
  "mechanism": [
    "human-standard atmospheric processing engages at docking",
    "unrecognized volatile Zhel'ii signal compounds are removed from the shared atmosphere",
    "network signals fail to persist",
    "the fictional network enters a resource-conserving dormancy response",
    "root and canopy functions continue at reduced efficiency without coordination",
    "nutrient transfer and partnership-level function break down"
  ],
  "interventionBoundary": "Use monitored atmospheric isolation or selective docking-section treatment that preserves identified signals while maintaining human life-support safeguards; never disable all atmospheric processing.",
  "case07Boundary": "GERMINATION-CASCADE, germination-pod evidence, and the resolution of The Gift are excluded from Case 06.",
  "prohibitedClaims": [
    "the alien system proves a universal Earth principle",
    "plants hear or intentionally converse",
    "forests are a single superorganism or internet",
    "mother trees broadly or intentionally feed offspring",
    "forest-wide resource sharing is settled science",
    "all atmospheric processing should be disabled",
    "correlation alone proves causation",
    "GERMINATION-CASCADE resolves Case 06"
  ],
  "sourceStatus": {
    "runtimeEvidence": "fictional in-game measurement and narrative evidence at frozen game commit",
    "alienBiology": "fictional Zhel'ii biology",
    "earthScience": "qualified context for chemical signaling and symbiosis",
    "engineering": "plausible selective-control extrapolation",
    "figures": "curriculum-original explanatory models"
  }
};
