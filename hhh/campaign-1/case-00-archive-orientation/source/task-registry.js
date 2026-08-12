window.HHH_CASE00_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C1-CASE00",
  "runtimeId": "L0",
  "instructionalType": "ORIENTATION",
  "title": "Temporal Agricultural Archive Facility",
  "displayLabel": "Archive Orientation",
  "version": "0.1",
  "status": "VALIDATION_BUILD",
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "editorShell": "1.0",
  "gameCommit": "9b8545ed6ecf98b337326390400076e36789e056",
  "auditBaseline": "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md",
  "staticContentInventory": "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json",
  "blueprint": "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
  "roles": {
    "student": 4,
    "teacher": 7,
    "answer": 3,
    "accessible": 5
  },
  "culminatingProduct": "Short archive-procedure and source-status explanation. Canonical CER is deliberately not used; see the Teacher Guide reasoning architecture.",
  "tasks": [
    {
      "id": "C00-T1",
      "number": "1",
      "semanticLabel": "ARCHIVE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Archive Vocabulary",
      "description": "Apply the six archival terms to the actions they name rather than copying definitions.",
      "instructionalPurpose": "Establish the transferable archival vocabulary the rest of the unit reasons with.",
      "provenance": [
        "Curriculum-authored definitions",
        "Blueprint-specified vocabulary set"
      ],
      "responseType": "six exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared six-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-orientation-01",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-orientation-01"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C00-T2",
      "number": "2",
      "semanticLabel": "PROVENANCE CHAIN",
      "icon": "ph-flow",
      "title": "Trace a Record from Accession to Interpretation",
      "description": "Complete a four-link provenance chain and identify where a claim can gain weight it has not earned.",
      "instructionalPurpose": "Family H1 source/provenance chain: creation, accession, transmission, interpretation.",
      "provenance": [
        "Curriculum-created model",
        "Blueprint Family H1"
      ],
      "responseType": "two organizer stages plus one short explanation",
      "answerScope": "What accession adds, what transmission can change, and one named link where unearned weight can enter.",
      "pagePlacement": {
        "student": "student-orientation-02",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-orientation-02"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C00-T3",
      "number": "3",
      "semanticLabel": "SOURCE STATUS",
      "icon": "ph-scales",
      "title": "Sort the Orientation Sources by Status",
      "description": "For each of the four orientation sources, state what it can establish and what it cannot establish alone.",
      "instructionalPurpose": "Contribution-and-limitation reasoning across the three source-limitation classes recorded in the Phase 1 audit.",
      "provenance": [
        "Fictional in-world testimony",
        "Fictional in-world archive record",
        "Fictional in-world instrument output",
        "Audit-recorded limitation classes"
      ],
      "responseType": "four-row contribution and limitation matrix",
      "answerScope": "Eight bounded cells; testimony, archive record, and instrument output must not receive the same limitation.",
      "pagePlacement": {
        "student": "student-orientation-03",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-orientation-03"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C00-T4",
      "number": "4",
      "semanticLabel": "FICTION BOUNDARY",
      "icon": "ph-nodes",
      "title": "Separate the Preserved Claim from Verified History",
      "description": "Mark which named elements are fictional framing and which ideas transfer, then separate an in-world claim from a real-world claim.",
      "instructionalPurpose": "Two-layer truth policy: the fictional setting is named explicitly and never merged with real-world evidence.",
      "provenance": [
        "Blueprint fiction boundary",
        "Curriculum-created model"
      ],
      "responseType": "six marked classifications plus two short explanations",
      "answerScope": "Four fictional elements and two transferable ideas, plus one preserved in-world claim and one transferable practice.",
      "pagePlacement": {
        "student": "student-orientation-03",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-02",
        "accessible": "accessible-orientation-04"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C00-T5",
      "number": "5",
      "semanticLabel": "ARCHIVE PROCEDURE",
      "icon": "ph-wrench",
      "title": "Write the Archive Procedure",
      "description": "Write the procedure for taking in a new record and deciding what weight it can carry.",
      "instructionalPurpose": "Culminating product for the unit: a short archive-procedure and source-status explanation.",
      "provenance": [
        "Curriculum-authored procedure",
        "Blueprint culminating-product policy"
      ],
      "responseType": "extended constructed response",
      "answerScope": "An ordered procedure using at least four of the six terms, ending in a weight decision rather than a truth verdict.",
      "pagePlacement": {
        "student": "student-orientation-04",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-03",
        "accessible": "accessible-orientation-05"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C00-T6",
      "number": "6",
      "semanticLabel": "TRANSFER EXIT",
      "icon": "ph-ticket",
      "title": "Verify a Newly Discovered Record",
      "description": "Apply the procedure to a record from outside the unit and justify each verification step.",
      "instructionalPurpose": "Transfer rather than recall: the exit uses a record the unit never presented.",
      "provenance": [
        "Curriculum-authored transfer prompt"
      ],
      "responseType": "short constructed response",
      "answerScope": "Two verification checks with a reason for each; naming the archive's own conclusion is not sufficient.",
      "pagePlacement": {
        "student": "student-orientation-04",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-03",
        "accessible": "accessible-orientation-05"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    }
  ],
  "vocabulary": [
    "accession",
    "archive",
    "corroboration",
    "provenance",
    "record",
    "source status"
  ],
  "orientationSources": [
    {
      "displayLabel": "Speak to Nova",
      "place": "Briefing Chamber",
      "sourceType": "conversation",
      "sourceOrigin": "fictional in-world testimony",
      "evidentiaryStatus": "fictional / hypothetical",
      "limitationClass": "testimony"
    },
    {
      "displayLabel": "Hear Zel'keth",
      "place": "Briefing Chamber",
      "sourceType": "conversation",
      "sourceOrigin": "fictional in-world testimony",
      "evidentiaryStatus": "fictional / hypothetical",
      "limitationClass": "testimony"
    },
    {
      "displayLabel": "Read TAA Records",
      "place": "Briefing Chamber",
      "sourceType": "archive",
      "sourceOrigin": "fictional in-world archive record",
      "evidentiaryStatus": "fictional / hypothetical",
      "limitationClass": "record"
    },
    {
      "displayLabel": "Scan Resonance Map",
      "place": "Thread Console",
      "sourceType": "terminal",
      "sourceOrigin": "fictional in-world instrument output",
      "evidentiaryStatus": "fictional / hypothetical",
      "limitationClass": "observation"
    }
  ],
  "fictionBoundary": [
    "Temporal Agricultural Archive",
    "Concord",
    "Zhel'ii",
    "resonance threading and the thread"
  ],
  "standards": {
    "directlyAssessed": [
      "C3 D3.1.6-8",
      "CCSS RH.6-8.1"
    ],
    "supporting": [
      "C3 D3.2.6-8",
      "CCSS RH.6-8.6"
    ],
    "contextual": [],
    "ngss": "No NGSS alignment is claimed. This unit assesses historical source handling, not a science or engineering practice."
  }
};
