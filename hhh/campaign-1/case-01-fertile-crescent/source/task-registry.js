window.HHH_CASE01_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C1-CASE01",
  "runtimeId": "L1",
  "instructionalType": "CORE_CASE",
  "title": "The Fertile Crescent",
  "displayLabel": "1 - The Fertile Crescent",
  "version": "0.1",
  "status": "APPROVED_STABLE",
  "ownerReviewStatus": "OWNER_REVIEW_PASS",
  "editorShell": "1.0",
  "gameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
  "auditBaseline": "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md",
  "staticContentInventory": "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json",
  "blueprint": "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
  "roles": {
    "student": 7,
    "teacher": 7,
    "answer": 4,
    "accessible": 9
  },
  "culminatingProduct": "Qualified historical explanation of cumulative selection across generations. Canonical CER is deliberately not used; see the Teacher Guide reasoning architecture.",
  "tasks": [
    {
      "id": "C01-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Domestication Vocabulary",
      "description": "Apply the six case terms to the actions and states they name rather than copying definitions.",
      "instructionalPurpose": "Establish the six terms the rest of the case reasons with, including the cultivation and domestication pair the case turns on.",
      "provenance": [
        "Curriculum-authored definitions",
        "Audit-recorded case vocabulary set"
      ],
      "responseType": "six exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared six-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-crescent-01",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-crescent-01"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C01-T2",
      "number": "2",
      "semanticLabel": "FIRST READING",
      "icon": "ph-diagnosis",
      "title": "Make a First Reading of the Field",
      "description": "State what the reconstructed scene shows and name one thing you would need before treating it as history.",
      "instructionalPurpose": "Provisional interpretation before the evidence arrives; establishes a starting point without revealing the case resolution.",
      "provenance": [
        "Game reconstruction of an early harvesting practice",
        "Curriculum-authored prompt"
      ],
      "responseType": "two short constructed responses",
      "answerScope": "One observation from the reconstruction and one named kind of evidence that would have to be found elsewhere.",
      "pagePlacement": {
        "student": "student-crescent-02",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-crescent-02"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C01-T3",
      "number": "3",
      "semanticLabel": "CHRONOLOGY TIMELINE",
      "icon": "ph-flow",
      "title": "Place the Scene on the Evidence Timeline",
      "description": "Place the reconstructed scene on a dated timeline of archaeobotanical evidence and say what that placement rules out.",
      "instructionalPurpose": "Family H2 chronology. A single calibrated timeline carries five overlapping evidence bars, so no row order implies sequence. The scene date, 9,700 BCE, sits inside bar A (about 9,750-8,750 BCE), the cultivation window, and centuries to millennia before domesticated-type grain becomes common anywhere.",
      "provenance": [
        "Arranz-Otaegui et al. 2016 regional chronology, calibrated (bands A, B, C, E)",
        "Allaby et al. 2017 calibrated-BC selection-rate analysis (band D)",
        "Curriculum-created timeline"
      ],
      "responseType": "one marked placement plus two short constructed responses",
      "answerScope": "The scene placed in the cultivation bar, one pair of bars read for how domestication developed over time, and one bar used to refute a single-date domestication claim.",
      "pagePlacement": {
        "student": "student-crescent-03",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-crescent-04"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C01-T4",
      "number": "4",
      "semanticLabel": "SOURCE STATUS",
      "icon": "ph-scales",
      "title": "Decide What Each Source Can Carry",
      "description": "For each of the four case sources, name its status and state what it can and cannot establish on its own.",
      "instructionalPurpose": "Family H4 contribution-and-limitation matrix across four different source statuses; the reconstruction must not receive the same status as the excavated evidence.",
      "provenance": [
        "Game reconstruction",
        "Archaeobotanical evidence",
        "Modern scholarly interpretation",
        "Curriculum-created matrix"
      ],
      "responseType": "four-row status, contribution and limitation matrix",
      "answerScope": "Twelve bounded cells; the reconstruction, the excavated remains, the site chronology and the scholarly interpretation must not share one status or one limit.",
      "pagePlacement": {
        "student": "student-crescent-04",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-02",
        "accessible": "accessible-crescent-05"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C01-T5",
      "number": "5",
      "semanticLabel": "SELECTION TRACE",
      "icon": "ph-wrench",
      "title": "Trace the Trait Across Generations",
      "description": "Complete the generation trace and explain why repeating the practice changes how common the trait is.",
      "instructionalPurpose": "The cumulative-selection mechanism: a trait that cannot spread in the wild spreads inside a human practice because the practice does the sowing.",
      "provenance": [
        "Purugganan and Fuller 2009 selection account",
        "Curriculum-created generation trace"
      ],
      "responseType": "three organizer stages plus one explanation",
      "answerScope": "What is kept, what is sown, what changes in the next crop, and why the frequency rises only while people keep replanting.",
      "pagePlacement": {
        "student": "student-crescent-05",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-03",
        "accessible": "accessible-crescent-06"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C01-T6",
      "number": "6",
      "semanticLabel": "COMPETING ACCOUNTS",
      "icon": "ph-nodes",
      "title": "Weigh Three Accounts of the Change",
      "description": "Judge three accounts against the evidence, then say what the disagreement about speed means for your confidence.",
      "instructionalPurpose": "Competing interpretation. Rejects both the single-inventor account and the no-human-role account, and makes the live scholarly disagreement about rate visible rather than hidden.",
      "provenance": [
        "Fuller 2007 rate analysis",
        "Purugganan and Fuller 2009 model expectations and the two-to-four-thousand-year fixation figure",
        "Allaby et al. 2017 measured selection coefficients",
        "Curriculum-created accounts"
      ],
      "responseType": "three marked judgments plus two short constructed responses",
      "answerScope": "Three supported or unsupported marks, one evidence-based rejection, and one statement about what the unresolved question of speed does and does not unsettle.",
      "pagePlacement": {
        "student": "student-crescent-06",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-03",
        "accessible": "accessible-crescent-07"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C01-T7",
      "number": "7",
      "semanticLabel": "HISTORICAL EXPLANATION",
      "icon": "ph-book",
      "title": "Write the Qualified Explanation",
      "description": "Explain how repeated human choices changed a crop across generations, using specific evidence and keeping the qualifications.",
      "instructionalPurpose": "Culminating product for the case: a qualified historical explanation of cumulative selection, not a Claim-Evidence-Reasoning argument.",
      "provenance": [
        "Curriculum-authored prompt",
        "Blueprint culminating-product policy"
      ],
      "responseType": "extended constructed response with four required parts",
      "answerScope": "Practice and mechanism, two named sources with their statuses, one thing the evidence cannot establish, and the cultivation-to-domestication distinction placed in time.",
      "pagePlacement": {
        "student": "student-crescent-07",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-04",
        "accessible": "accessible-crescent-08"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C01-T8",
      "number": "8",
      "semanticLabel": "TRANSFER EXIT",
      "icon": "ph-ticket",
      "title": "Test a New Claim",
      "description": "Apply the case reasoning to a dig report the unit never presented and say what would settle it.",
      "instructionalPurpose": "Transfer rather than recall: the exit uses a site the case never supplied and asks for the cultivation and domestication distinction in a new setting.",
      "provenance": [
        "Fuller 2007 arable-weed indicator",
        "Curriculum-authored transfer prompt"
      ],
      "responseType": "short constructed response in two parts",
      "answerScope": "What the report supports so far and what further evidence would separate cultivation from morphological domestication.",
      "pagePlacement": {
        "student": "student-crescent-07",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-04",
        "accessible": "accessible-crescent-09"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    }
  ],
  "vocabulary": [
    "cultivation",
    "domestication",
    "non-shattering",
    "rachis",
    "selection",
    "wild type"
  ],
  "caseSources": [
    {
      "displayLabel": "The Archive's reconstructed field",
      "sourceType": "reconstruction",
      "sourceOrigin": "game reconstruction of a historical practice",
      "evidentiaryStatus": "reconstructed",
      "limitationClass": "reconstruction"
    },
    {
      "displayLabel": "Charred grain remains from excavated sites",
      "sourceType": "archaeobotanical evidence",
      "sourceOrigin": "archaeological or archaeobotanical evidence",
      "evidentiaryStatus": "documented / observed",
      "limitationClass": "observation"
    },
    {
      "displayLabel": "Site-by-site chronology of domesticated-type grain",
      "sourceType": "quantitative synthesis",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "inferred",
      "limitationClass": "inference"
    },
    {
      "displayLabel": "Scholarly interpretation of how the change happened",
      "sourceType": "interpretation",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "debated / uncertain",
      "limitationClass": "interpretation"
    }
  ],
  "chronologyScale": {
    "system": "calibrated calendar dates",
    "model": "overlapping-evidence-windows",
    "modelNote": "The rail is five dated evidence windows drawn from different regions, crops and studies, not five consecutive eras. Bands B, D and E cover partly the same centuries. Band D is a selection-rate window rather than a regional threshold. Both learner editions must disclose this above the rail.",
    "timelineBars": {
      "A": { "range": "about 9,750-8,750 BCE / about 11,700-10,700 cal BP", "kind": "regional-cultivation", "source": "Arranz-Otaegui et al. 2016" },
      "B": { "range": "about 8,750-8,250 BCE / about 10,700-10,200 cal BP", "kind": "regional-threshold", "source": "Arranz-Otaegui et al. 2016" },
      "C": { "range": "about 400-1,000 years later than band B", "kind": "regional-threshold", "source": "Arranz-Otaegui et al. 2016" },
      "D": { "range": "about 8,500-7,500 BCE", "kind": "selection-rate", "overlaps": ["B", "E"], "source": "Allaby et al. 2017, reported in calibrated BC" },
      "E": { "range": "about 8,250-6,350 BCE / about 10,200-8,300 cal BP", "kind": "regional-threshold", "source": "Arranz-Otaegui et al. 2016" }
    },
    "sceneDate": "9,700 BCE",
    "sceneBand": "A",
    "excludedFromRail": "Tanno and Willcox 2006 report noncalibrated radiocarbon years BP. Their numerical dates are deliberately not placed on the rail and are never converted to BCE. The paper is used for the counted wild-to-domesticated trend only.",
    "evidenceCounts": {
      "tanno-willcox-2006": { "examined": 9844, "identifiable": 804, "note": "9,844 spikelets examined; 804 identifiable well enough to classify as wild or domesticated type. The trend claim belongs to the 804, never to the 9,844." }
    },
    "caseSourceStatuses": {
      "reconstructed": "the Archive's scene and the Archivist's in-scene observations",
      "documented": "the Background block on how the grain works, and the counted charred grain"
    }
  },
  "reconstructionBoundary": [
    "the woman and her words",
    "the single field and the single season",
    "9,700 BCE as scene setting rather than a dated find",
    "the neighbour who carries the seed away"
  ],
  "standards": {
    "directlyAssessed": [
      "C3 D2.His.1.6-8",
      "C3 D2.His.2.6-8",
      "CCSS RH.6-8.7"
    ],
    "supporting": [
      "C3 D3.2.6-8",
      "CCSS RH.6-8.8",
      "CCSS WHST.6-8.2"
    ],
    "contextual": [
      "NGSS MS-LS4-5"
    ],
    "ngss": "MS-LS4-5 is contextual only. The case reasons about how a human practice changed the frequency of a trait, but the assessed product is a historical explanation with source qualification, not a science or engineering practice, so no NGSS alignment is claimed as directly assessed."
  }
};
