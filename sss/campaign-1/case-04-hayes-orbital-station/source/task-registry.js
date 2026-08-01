window.SSS_CASE04_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C1-CASE04",
  "runtimeId": "orbital",
  "title": "Hayes Orbital Station",
  "version": "0.1",
  "status": "DRAFT",
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "editorShell": "1.0",
  "gameCommit": "2bfdb0aadf6ce33b6664cd104b11a891cb55efaf",
  "roles": {
    "student": 4,
    "teacher": 7,
    "answer": 4,
    "accessible": 6
  },
  "tasks": [
    {
      "number": "1",
      "semanticLabel": "INITIAL THINKING",
      "icon": "ph-scales",
      "title": "Initial Thinking — Identify the Variable",
      "description": "Identify the environmental variable that changed immediately before the repeating reactor failures.",
      "keyed": true
    },
    {
      "number": "2",
      "semanticLabel": "TIMELINE ANALYSIS",
      "icon": "ph-nodes",
      "title": "Build the Change-to-Crash Timeline",
      "description": "Arrange the verified relative events from stable operation through repeated crash and recovery.",
      "keyed": true
    },
    {
      "number": "3",
      "semanticLabel": "EVIDENCE ANALYSIS",
      "icon": "ph-scales",
      "title": "Isolate Variables and Test Alternatives",
      "description": "Sort changed, stable, symptom, and mechanism evidence and test competing explanations.",
      "keyed": true
    },
    {
      "number": "4",
      "semanticLabel": "DIAGNOSIS",
      "icon": "ph-diagnosis",
      "title": "Diagnose the Reactor Failure",
      "description": "Select the diagnosis that fits the timeline and mechanism evidence rather than correlation alone.",
      "keyed": true
    },
    {
      "number": "5",
      "semanticLabel": "PROCESS MODEL",
      "icon": "ph-flow",
      "title": "Model the Repeating Crash Cycle",
      "description": "Complete the reactor-specific causal cycle from uncontrolled exposure to recovery and recurrence.",
      "keyed": true
    },
    {
      "number": "6",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Explain the Failure with CER",
      "description": "Write an atomic Claim-Evidence-Reasoning explanation using timeline and mechanism evidence.",
      "keyed": true
    },
    {
      "number": "7",
      "semanticLabel": "ENGINEERING DECISION",
      "icon": "ph-wrench",
      "title": "Design Independent Reactor Controls",
      "description": "Choose immediate and longer-term light controls while keeping continuous cultivation conditionally possible.",
      "keyed": true
    },
    {
      "number": "8",
      "semanticLabel": "EXIT TICKET",
      "icon": "ph-ticket",
      "title": "Exit Ticket — Cause or Effect?",
      "description": "Classify a gas-exchange change as a cause or an effect and justify the classification.",
      "keyed": true
    }
  ],
  "vocabulary": [
    "Daily light dose",
    "Photobioreactor",
    "Photoinhibition",
    "Photooxidative stress",
    "Process control"
  ],
  "correctDiagnosis": "Uncontrolled 24/0 corridor lighting exceeded this reactor configuration's validated operating range, causing recurrent photoinhibition and photooxidative damage.",
  "mechanism": [
    "uncontrolled 24/0 exposure",
    "excessive daily light dose under current operating conditions",
    "photodamage outpaces repair",
    "culture productivity and gas exchange fall",
    "survivors rebuild",
    "unchanged exposure causes another crash"
  ],
  "prohibitedClaims": [
    "all spirulina universally require night",
    "continuous cultivation is impossible",
    "dark reactions require darkness",
    "spirulina is a plant",
    "correlation alone establishes the mechanism"
  ],
  "sourceStatus": {
    "science": "qualified reactor-specific mechanism",
    "sequence": "game-verified relative timeline",
    "figures": "curriculum-original qualitative models"
  }
};
