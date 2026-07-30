window.SSS_CASE03_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C1-CASE03",
  "title": "Mars Habitat",
  "version": "1.0",
  "status": "VALIDATION BUILD",
  "gameCommit": "2a6e8a7bb75c8c96f26f9ebfe7523668107ab712",
  "roles": {
    "student": 4,
    "teacher": 8,
    "answer": 4,
    "accessible": 6,
    "grayscale": 4
  },
  "tasks": [
    {
      "number": "1",
      "title": "Define the measurement",
      "description": "Explain what PPFD/PAR quantity tells you and what it does not reveal about spectral distribution.",
      "keyed": true
    },
    {
      "number": "2",
      "title": "Read the spectral-transmission data",
      "description": "Use the game-provided wavelength-band transmission values to identify the weakest band within 400-700 nm.",
      "keyed": true
    },
    {
      "number": "3",
      "title": "Compare quantity and quality",
      "description": "Compare the adequate total PPFD reading with uneven wavelength transmission and reject the low-total-light explanation.",
      "keyed": true
    },
    {
      "number": "4",
      "title": "Connect the symptom pattern",
      "description": "Use old-versus-new leaf evidence to identify a failure in new chlorophyll formation.",
      "keyed": true
    },
    {
      "number": "5",
      "title": "Select and reject diagnoses",
      "description": "Choose the diagnosis that fits all evidence and reject one tempting alternative.",
      "keyed": true
    },
    {
      "number": "6",
      "title": "Model the mechanism",
      "description": "Complete the chain from the wrong collector filter to bleached new growth.",
      "keyed": true
    },
    {
      "number": "7",
      "title": "Write the case conclusion",
      "description": "Write a concise Claim-Evidence-Reasoning explanation.",
      "keyed": true
    },
    {
      "number": "8",
      "title": "Transfer the analysis",
      "description": "Explain why increasing brightness without correcting spectrum may fail.",
      "keyed": true
    },
    {
      "number": "9",
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
  }
};
