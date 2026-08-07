window.SSS_CASE03_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C1-CASE03",
  "title": "Mars Habitat",
  "version": "1.2",
  "status": "DRAFT",
  "editorShell": "1.0",
  "gameCommit": "c6c17be57880b365793fdf99ff4ad09b62ecacce",
  "roles": {
    "student": 4,
    "teacher": 8,
    "answer": 4,
    "accessible": 7
  },
  "tasks": [
    {
      "number": "1",
      "semanticLabel": "REFERENCE",
      "icon": "ph-book",
      "title": "Define the measurement",
      "description": "Explain what PPFD/PAR quantity tells you and what it does not reveal about spectral distribution.",
      "keyed": true
    },
    {
      "number": "2",
      "semanticLabel": "DATA ANALYSIS",
      "icon": "ph-scales",
      "title": "Read the spectral-transmission data",
      "description": "Use the game-provided wavelength-band transmission values to identify the weakest band within 400-700 nm.",
      "keyed": true
    },
    {
      "number": "3",
      "semanticLabel": "DATA ANALYSIS",
      "icon": "ph-scales",
      "title": "Compare quantity and quality",
      "description": "Compare the adequate total PPFD reading with uneven wavelength transmission and reject the low-total-light explanation.",
      "keyed": true
    },
    {
      "number": "4",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-nodes",
      "title": "Connect the symptom pattern",
      "description": "Use old-versus-new leaf evidence to identify a failure in new chlorophyll formation.",
      "keyed": true
    },
    {
      "number": "5",
      "semanticLabel": "DIAGNOSIS",
      "icon": "ph-diagnosis",
      "title": "Select and reject diagnoses",
      "description": "Choose the diagnosis that fits all evidence and reject one tempting alternative.",
      "keyed": true
    },
    {
      "number": "6",
      "semanticLabel": "MECHANISM MODEL",
      "icon": "ph-flow",
      "title": "Model the mechanism",
      "description": "Complete the chain from the wrong collector filter to bleached new growth.",
      "keyed": true
    },
    {
      "number": "7",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Claim-Evidence-Reasoning",
      "description": "Write a concise Claim-Evidence-Reasoning explanation.",
      "keyed": true
    },
    {
      "number": "8",
      "semanticLabel": "TRANSFER CHECK",
      "icon": "ph-wrench",
      "title": "Transfer the analysis",
      "description": "Explain why increasing brightness without correcting spectrum may fail.",
      "keyed": true
    },
    {
      "number": "9",
      "semanticLabel": "EXIT TICKET",
      "icon": "ph-ticket",
      "title": "Exit ticket",
      "description": "State the first two measurements you would compare in a new lighting failure.",
      "keyed": true
    }
  ],
  "data": {
    "combinedPpfd": 280,
    "unit": "umol m-2 s-1",
    "pipeLengthM": 12,
    "aggregateTransmissionPercent": 68,
    "filterReplacementSolsAgo": 47,
    "transmissionPercent": {
      "blue": 92,
      "green": 88,
      "red": 31,
      "deepRed": 12
    },
    "requiredFilter": "FS-7 FULL SPECTRUM",
    "incorrectFilter": "BP-4 BLUE PASS"
  },
  "correctDiagnosis": "The light delivery system is filtering out red wavelengths needed for chlorophyll biosynthesis.",
  "prohibitedClaims": [
    "increased brightness alone always solves a spectrum problem",
    "plants only use red light",
    "green light is useless",
    "dust alone explains selective red rejection"
  ],
  "sourceStatus": {
    "science": "authoritative/general",
    "numbers": "game-specific",
    "figures": "curriculum-original"
  },
  "correctiveOf": "1.1",
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "printStatus": "NOT_RUN"
};
