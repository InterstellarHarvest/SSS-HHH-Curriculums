window.HHH_CASE07_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C2-CASE07",
  "runtimeId": "C2L0",
  "instructionalType": "CORE_CASE",
  "title": "The Audit",
  "displayLabel": "7 - The Audit",
  "version": "0.1",
  "status": "APPROVED_STABLE",
  "ownerReviewStatus": "OWNER_REVIEW_PASS",
  "editorShell": "1.0",
  "gameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
  "auditBaseline": "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md",
  "staticContentInventory": "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json",
  "blueprint": "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
  "roles": {
    "student": 8,
    "teacher": 7,
    "answer": 4,
    "accessible": 10
  },
  "learningGoal": "Evaluate which competing record is better supported as authentic by tracing provenance and transmission, comparing discrepancies, and corroborating independent evidence—without treating neatness or corrections as proof.",
  "guidingQuestion": "Which report is better supported as authentic, and how does the chain of evidence justify that judgment?",
  "culminatingProduct": "Record Validation Memorandum — a provenance and authenticity judgment. The learner names the better-supported record, supplies two evidentiary links from different sources, explains how those links fit together, names one tempting clue that does not prove the finding by itself, and states a remaining limit. Canonical CER is deliberately not used; see cerDecision.",
  "cerDecision": {
    "id": "case07-cer-declined-v1.0",
    "decision": "DECLINED",
    "blueprintProduct": "provenance/authenticity judgment (Blueprint section 9.3)",
    "rationale": "The Blueprint permits canonical CER only when its structure genuinely supports the case, and names a provenance/authenticity judgment as this case's culminating product. A CER frame would force the learner to elect one claim and demote everything else to support, and this case assesses the opposite operation: the relationship between records, what each source can and cannot establish, the corroboration between an amended page and an independently recorded custody event, and a named clue that must be refused rather than used. The Record Validation Memorandum keeps all five of those as separate, separately scored obligations.",
    "precedent": "HHH Campaign 1 Core Case 06 declined canonical CER for its systems and evidence-audit explanation on the same Blueprint ground: the product carried findings a single claim could not hold at once. This case follows that precedent rather than inventing a new one.",
    "enforcement": "No role renders the shared canonical CER component, and no role declares a CER contract.",
    "prohibitedSelectors": [
      "[data-cer-contract]",
      ".canonical-cer",
      ".cer-stack"
    ]
  },
  "sourceStatusContract": {
    "rule": "Every learner-facing evidence object declares its status in markup (data-evidence-layer) and in printed text (a STATUS line), and no role converts an invented TAA record into a claim about the real world or a real archival principle into evidence that the TAA case happened.",
    "bands": [
      {
        "id": "fictional",
        "label": "FICTIONAL CASE EVIDENCE",
        "attribute": "fictional",
        "statusMarker": "fictional case evidence",
        "covers": [
          "the Temporal Agricultural Archive and everyone in it",
          "the audit and its findings",
          "the two competing copies of the field report",
          "both recorded custody histories and every entry in them",
          "the recall, the re-filing and the reason recorded with them",
          "every count, name and date belonging to any of the above"
        ],
        "rule": "Evidence about a case that did not happen. It may be reasoned about, compared and judged. It may never be cited as a fact about the real world."
      },
      {
        "id": "real",
        "label": "DOCUMENTED",
        "attribute": "real",
        "statusMarker": "documented",
        "covers": [
          "diplomatics as the name and definition of the discipline",
          "the identification of Mabillon's De Re Diplomatica (1681) in the SAA dictionary entry",
          "the description of diplomatics as weighing context with internal and external characteristics",
          "the four properties of a trustworthy record: reliability, authenticity, integrity, usability",
          "the multi-factor authenticity rule that follows from them"
        ],
        "rule": "Real archival practice, cited to a real published reference source. It explains how records are judged. It is never evidence that the TAA case happened."
      },
      {
        "id": "curriculum-model",
        "label": "CURRICULUM-ORIGINAL SCHEMATIC",
        "attribute": "curriculum-model",
        "statusMarker": "curriculum-original schematic",
        "covers": [
          "the multi-factor authenticity framework figure",
          "the two-copy provenance and custody comparison figure",
          "the evidence-weight organiser figure"
        ],
        "rule": "Drawn for this packet. A diagram that organises evidence is not itself evidence, and every figure says so in print."
      }
    ],
    "statusVocabulary": [
      "fictional case evidence",
      "documented",
      "curriculum-original schematic"
    ],
    "layerAttribute": "data-evidence-layer",
    "layerValues": [
      "fictional",
      "real",
      "curriculum-model"
    ],
    "noticeRequired": [
      "student",
      "accessible"
    ],
    "noticeSelector": "[data-source-status-notice]",
    "nonMergerRule": "Getting the TAA case right proves nothing about the real world, and a real archival principle proves nothing about the TAA. Both learner editions carry this sentence on page 1.",
    "fictionalDataRule": "Every deterministic invented value sits inside a node carrying data-fictional-data, and every such node sits inside a fictional or curriculum-model evidence object.",
    "prohibitedRuntimeIdentifiers": [
      "clueTag",
      "revealsClue",
      "endsConversation",
      "disfavoredStart",
      "goto",
      "nodes",
      "diagnoses",
      "isCorrect",
      "evidenceType",
      "blindspotFor",
      "anchorPoint",
      "lockHint",
      "taaCommsHints",
      "resolveLabel",
      "diagnosisPrompt",
      "livingBg",
      "spritesheet",
      "audit_briefed",
      "audit_current",
      "audit_logged",
      "memo_examined",
      "briefing_chamber",
      "thread_console",
      "memo_pair",
      "audit_log"
    ],
    "prohibitedRuntimeIdentifierRule": "No printable page in any role may display a runtime implementation identifier. The list is identifier-shaped by construction so that it can never accidentally forbid ordinary English.",
    "enforcedRoles": [
      "student",
      "teacher",
      "answer",
      "accessible"
    ]
  },
  "authenticityRule": {
    "id": "case07-authenticity-v1.0",
    "findingId": "HHH-GAME-C2L0-001",
    "dependencyClass": "GAME_REMEDIATION_BLOCKS_FINALIZATION",
    "dependencyStatus": "RESOLVED_VERIFIED",
    "resolvedGameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
    "rule": "Authenticity is evaluated through multiple factors such as materials, handwriting, provenance, custody, and corroboration. Unexplained neatness may prompt questions. No single surface feature proves authenticity or forgery. A clean working document can be genuine. A forgery can imitate corrections.",
    "families": [
      "materials",
      "handwriting",
      "provenance",
      "custody",
      "corroboration"
    ],
    "printedRule": "No single surface feature proves authenticity or forgery.",
    "requiredPrintedStatements": [
      "No single surface feature proves authenticity or forgery.",
      "A clean record can be authentic",
      "a forged record can imitate corrections",
      "Unexplained neatness may prompt closer examination"
    ],
    "requiredPrintedStatementRoles": [
      "student",
      "accessible"
    ],
    "gameNote": "The game dependency is closed. The remediated Campaign 2 Level 0 closing note already states the multi-factor rule, and the curriculum neither reopens it nor propagates the retired heuristic.",
    "positiveRequirements": [
      {
        "id": "multi-factor-rule-printed",
        "selector": "[data-authenticity-rule='multi-factor']",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print the multi-factor rule and the two consequences that follow from it."
      },
      {
        "id": "authenticity-framework-figure",
        "selector": "[data-authenticity-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the five-family framework figure with the rule printed inside it."
      },
      {
        "id": "surface-not-decisive-printed",
        "selector": "[data-authenticity-rule='surface-not-decisive']",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "The matched comparison visibly states that surface characteristics alone do not settle it."
      },
      {
        "id": "answer-key-floor-printed",
        "selector": "[data-authenticity-rule='answer-key-floor']",
        "roles": [
          "answer"
        ],
        "rule": "The Answer Key states the single-factor floors that are refused at every level."
      }
    ],
    "prohibitedFramings": {
      "rule": "Five CLOSED negative classes, each anchored to a named subject register. A proposition violates a class only when the class's subject is present in the same proposition and one of its patterns matches. This is a bounded guard against one known high-risk misconception. It is not, and does not claim to be, a general semantic detector: an unseen paraphrase can pass it, and manual cross-role review remains required.",
      "neatProvesForged": {
        "why": "A clean, pristine or unamended record proves or means the record is forged.",
        "subjectPatterns": [
          "\\b(?:clean|pristine|neat|immaculate|flawless|spotless|unamended|uncorrected|seamless|neatness|tidiness)\\b"
        ],
        "patterns": [
          "\\b(?:clean|pristine|neat|immaculate|flawless|spotless|unamended|uncorrected|seamless|neatness|tidiness)\\b[^.!?]{0,90}\\b(?:proves?|proved|proving|means?|meant|shows?|showed|establishes|established|confirms?|confirmed|guarantees?|is proof|are proof)\\b[^.!?]{0,60}\\b(?:forged|forgery|forgeries|fake|faked|false|falsified|inauthentic|not genuine|not authentic)\\b",
          "\\b(?:forged|forgery|forgeries|fake|faked|false|falsified|inauthentic|not genuine|not authentic)\\b[^.!?]{0,60}\\b(?:because|since)\\b[^.!?]{0,45}\\b(?:(?:clean|pristine|neat|immaculate|flawless|spotless|unamended|uncorrected|seamless|neatness|tidiness)|no corrections|no amendments)\\b"
        ]
      },
      "correctionsProveAuthentic": {
        "why": "Corrections or amendments prove or mean the record is genuine.",
        "subjectPatterns": [
          "\\b(?:corrections?|amendments?|crossings?[- ]out|crossed[- ]out|struck[- ]through|scratched[- ]out)\\b"
        ],
        "patterns": [
          "\\b(?:corrections?|amendments?|crossings?[- ]out|crossed[- ]out|struck[- ]through|scratched[- ]out)\\b[^.!?]{0,90}\\b(?:proves?|proved|proving|means?|meant|shows?|showed|establishes|established|confirms?|confirmed|guarantees?|is proof|are proof)\\b[^.!?]{0,60}\\b(?:authentic|authenticity|genuine|genuineness|the real one|not forged|not a forgery)\\b",
          "\\b(?:authentic|genuine|the real one)\\b[^.!?]{0,60}\\b(?:because|since)\\b[^.!?]{0,50}\\b(?:it has corrections|of the corrections|of its corrections|it is amended|it has amendments|of the amendments|it was corrected)\\b"
        ]
      },
      "messyIsGenuine": {
        "why": "A messy or working record is automatically genuine.",
        "subjectPatterns": [
          "\\b(?:messy|messier|untidy|scruffy|rough|scratched|amended|working)\\b[^.!?]{0,40}\\b(?:record|copy|document|report|draft)s?\\b",
          "\\b(?:always|automatically|necessarily|by definition)\\b"
        ],
        "patterns": [
          "\\b(?:messy|messier|untidy|scruffy|rough|scratched|amended|working)\\b[^.!?]{0,40}\\b(?:record|copy|document|report|draft)s?\\b[^.!?]{0,50}\\b(?:is|are|must be|will be)\\b[^.!?]{0,25}\\b(?:always|automatically|necessarily|by definition|therefore)\\b[^.!?]{0,30}\\b(?:genuine|authentic|real|true)\\b",
          "\\b(?:always|automatically|necessarily|by definition)\\b[^.!?]{0,30}\\b(?:genuine|authentic|real)\\b[^.!?]{0,60}\\b(?:because|since|if)\\b[^.!?]{0,45}\\b(?:messy|untidy|amended|corrected|scratched|has corrections)\\b"
        ]
      },
      "noCorrectionsProveForgery": {
        "why": "The absence of corrections proves the record is a forgery.",
        "subjectPatterns": [
          "\\b(?:no|without|absence of|lack of|zero)\\b[^.!?]{0,30}\\b(?:corrections?|amendments?)\\b"
        ],
        "patterns": [
          "\\b(?:no|without|absence of|lack of|zero)\\b[^.!?]{0,30}\\b(?:corrections?|amendments?)\\b[^.!?]{0,70}\\b(?:proves?|proved|proving|means?|meant|shows?|showed|establishes|established|confirms?|confirmed|guarantees?|is proof|are proof)\\b[^.!?]{0,60}\\b(?:forged|forgery|forgeries|fake|faked|false|falsified|inauthentic|not genuine|not authentic)\\b"
        ]
      },
      "visibleCorrectionsProveAuthenticity": {
        "why": "Visible or present corrections prove authenticity.",
        "subjectPatterns": [
          "\\b(?:visible|present|presence of)\\b[^.!?]{0,30}\\b(?:corrections?|amendments?)\\b",
          "\\b(?:corrections?|amendments?)\\b[^.!?]{0,25}\\b(?:are|is)\\b[^.!?]{0,20}\\bproof\\b"
        ],
        "patterns": [
          "\\b(?:visible|present|presence of)\\b[^.!?]{0,30}\\b(?:corrections?|amendments?)\\b[^.!?]{0,70}\\b(?:proves?|proved|proving|establishes|established|confirms?|confirmed|guarantees?|means?)\\b[^.!?]{0,50}\\b(?:authenticity|authentic|genuineness|genuine)\\b",
          "\\b(?:corrections?|amendments?)\\b[^.!?]{0,25}\\b(?:are|is)\\b[^.!?]{0,20}\\bproof\\b[^.!?]{0,45}\\b(?:authenticity|authentic|genuineness|genuine)\\b"
        ]
      }
    },
    "negativeControls": {
      "neatProvesForged": [
        "Copy A is clean, which proves it is a forgery.",
        "A pristine record means the document is fake.",
        "Unexplained neatness shows that a record is forged.",
        "The report is a forgery because it is too clean."
      ],
      "correctionsProveAuthentic": [
        "The corrections prove the report is genuine.",
        "Amendments show that a record is authentic.",
        "A crossed-out coordinate means the copy is the real one.",
        "Copy B is genuine because of its corrections."
      ],
      "messyIsGenuine": [
        "A messy working record is always genuine.",
        "An amended report is automatically the real one.",
        "A record is automatically genuine if it is messy."
      ],
      "noCorrectionsProveForgery": [
        "No corrections at all proves the record is a forgery.",
        "The absence of amendments shows the copy is fake.",
        "A copy with no corrections is proof of forgery."
      ],
      "visibleCorrectionsProveAuthenticity": [
        "Visible corrections prove authenticity.",
        "The presence of amendments establishes the genuineness of the report.",
        "Corrections are proof of authenticity."
      ]
    },
    "positiveControls": [
      "Unexplained neatness may prompt closer examination.",
      "Corrections can be one clue when they match a documented record history.",
      "A clean record can be authentic.",
      "A forged record can imitate corrections.",
      "No single surface feature proves authenticity or forgery.",
      "Copy B is the better-supported record because its custody trail and its page agree, and an independent log licenses the trail.",
      "The corrections are one clue among several, and they carry weight only because a separate record explains them.",
      "Nothing on either page settles this on its own.",
      "The working archive held the amended copy, and the primary shelf held the unamended one.",
      "An absence of recorded events is not the same as an absence of events."
    ]
  },
  "provenanceTrails": {
    "id": "case07-provenance-v1.0",
    "rule": "Both trails are drawn from the recorded custody history and from nothing else. No creation or provenance event is invented to complete a pattern, and the head of both trails is drawn as an explicit NOT RECORDED node in every role that shows the figure.",
    "copies": [
      {
        "id": "copy-a",
        "label": "Copy A",
        "heldAt": "the primary shelf",
        "recordedSteps": [
          "intake",
          "catalogue",
          "shelf"
        ],
        "recordedStepCount": 3,
        "amendments": [],
        "noteOnFile": null,
        "surface": "No amendments. Every entry complete, every coordinate exact, the named author's signature clean on every page."
      },
      {
        "id": "copy-b",
        "label": "Copy B",
        "heldAt": "the working archive",
        "recordedSteps": [
          "intake",
          "catalogue",
          "recalled",
          "re-filed",
          "shelf"
        ],
        "recordedStepCount": 5,
        "amendments": [
          "a timestamp struck through and re-logged",
          "a margin note correcting a grain count",
          "one coordinate crossed out"
        ],
        "noteOnFile": "The recall was made mid-mission, at the named author's own request, to correct the grain count.",
        "surface": "Amended. A struck-through timestamp, a corrected grain count, one crossed-out coordinate, the named author's signature on every page."
      }
    ],
    "differingLinks": [
      "recalled",
      "re-filed"
    ],
    "unrecordedEvents": [
      "the making of either copy — both trails begin at intake",
      "where or when either copy was written",
      "by whose hand either copy was written, as opposed to who is named on it"
    ],
    "corroborationPair": {
      "onThePage": "a margin note correcting a grain count, on Copy B",
      "inTheRecord": "a recall entry whose recorded reason was to correct a grain count",
      "why": "The page and the custody trail were produced at different times by different processes and say the same thing. That agreement, not the existence of the correction, is what carries weight."
    },
    "intendedJudgment": "Copy B is better supported as authentic.",
    "prohibitedJudgmentRoute": "Copy B has corrections, therefore it is authentic. Refused at every level: it would reach the same answer about a forgery that had been given corrections on purpose."
  },
  "evidenceWeighting": {
    "id": "case07-weighting-v1.0",
    "rule": "Evidentiary roles are qualitative kinds, not scores. No numerical weighting, ranking value or confidence percentage appears anywhere in this package.",
    "roles": [
      {
        "id": "context",
        "label": "CONTEXT",
        "gloss": "Tells you what kind of case this is. It frames the question and does not answer it.",
        "sources": [
          "audit-briefing",
          "audit-pattern"
        ]
      },
      {
        "id": "corroborating",
        "label": "CORROBORATING EVIDENCE",
        "gloss": "An independent record that can agree or disagree with another record. Its own custody must be sound first.",
        "sources": [
          "audit-log"
        ]
      },
      {
        "id": "direct-record",
        "label": "DIRECT RECORD EVIDENCE",
        "gloss": "The records under judgment themselves, together with their recorded transmission.",
        "sources": [
          "memo-pair"
        ]
      }
    ],
    "notEquallyProbative": "The four sources are not equally probative and Task 5 requires the learner to say so. The two participant accounts establish case context and pattern; the audit log and the memo pair with its custody history carry the record-authentication weight.",
    "acceptedAlternative": "A learner who argues the audit log into DIRECT RECORD EVIDENCE, on the ground that it is itself a record whose custody is verified, has made a defensible move and the key credits it. Putting either participant account into a record role is not creditable."
  },
  "noGameRoute": {
    "rule": "Campaign 2 has no teacher level selector, no direct-launch mode, no injected state and no developer shortcut, and none will be built. Every assessed piece of evidence therefore exists in the learner packet, and the dossier is the stable assessment record in both routes.",
    "dossier": [
      "audit-briefing",
      "audit-pattern",
      "audit-log",
      "memo-pair"
    ],
    "requiredInRoles": [
      "student",
      "accessible"
    ],
    "gameRouteIsOptional": true,
    "prohibited": [
      "reproducing runtime correct-answer flags",
      "reproducing hints that name the answer",
      "reproducing the level's resolution text as learner evidence",
      "requiring an unprinted line of gameplay for any assessed item"
    ],
    "teacherMustProvide": [
      "normal game route",
      "complete no-game route"
    ]
  },
  "tasks": [
    {
      "id": "C07-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Case Vocabulary",
      "description": "Apply the six terms the case cannot be performed without to the things and relationships they name.",
      "instructionalPurpose": "Establish only the six terms the reasoning needs. The load-bearing pair is provenance and chain of custody: a learner who holds them as synonyms reads the two trails in Task 4 as the same kind of fact and cannot say what the extra links mean.",
      "provenance": [
        "Curriculum-authored working definitions",
        "Real archival terminology as defined in the certified reference estate"
      ],
      "responseType": "six exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared six-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-audit-01",
        "teacher": "teacher-guide-02",
        "answer": "answer-key-01",
        "accessible": "accessible-audit-02"
      },
      "editions": [
        "student",
        "teacher",
        "answer",
        "accessible"
      ],
      "keyed": true
    },
    {
      "id": "C07-T2",
      "number": "2",
      "semanticLabel": "AUTHENTICITY TEST",
      "icon": "ph-diagnosis",
      "title": "Set an Authenticity Test",
      "description": "State what kinds of evidence you would verify before accepting one of two competing copies as authentic, and why one of them tells you more than the page does.",
      "instructionalPurpose": "Provisional thinking, taken before the method arrives and before the learner has been led toward either copy. Most classes name a feature of the page itself, which is the useful mistake: Task 3 then shows why the page cannot carry the decision. Because the task records a starting point rather than a judgment, it is deliberately non-keyable.",
      "provenance": [
        "The Archive's invented record of the flagged pair",
        "Curriculum-authored prompt"
      ],
      "responseType": "two short constructed responses",
      "answerScope": "Any honest and specific test. There is no correct answer and none is keyed.",
      "pagePlacement": {
        "student": "student-audit-03",
        "teacher": "teacher-guide-03",
        "answer": null,
        "accessible": "accessible-audit-05"
      },
      "editions": [
        "student",
        "teacher",
        "accessible"
      ],
      "keyed": false,
      "nonKeyableReason": "The task asks what the learner would verify before the case has shown them how. Keying it would convert a record of provisional thinking into a hidden multiple-choice item and would penalise the very mistake the sequence is built to expose. The Teacher Guide carries the guidance for reading it."
    },
    {
      "id": "C07-T3",
      "number": "3",
      "semanticLabel": "CLUE AND PROOF",
      "icon": "ph-scales",
      "title": "Separate a Clue from Proof",
      "description": "Sort six observations about the two copies by what each one can carry: a question, evidence once corroborated, or nothing either way.",
      "instructionalPurpose": "The explicit misconception barrier, and the load-bearing task of the case. Item 1 addresses neatness and item 2 addresses corrections; both are marked Q, so neither can be read as deciding anything. Items 5 and 6 are features both copies share, which is a different reason for carrying no weight. Part B is the paragraph that has to exist before the culminating memorandum can be trusted.",
      "provenance": [
        "The Archive's invented record of the flagged pair",
        "The certified real-world authenticity rule"
      ],
      "responseType": "six closed classifications plus one short constructed response",
      "answerScope": "One mark per item from the printed three-value key, and one explanation covering both halves of the rule.",
      "pagePlacement": {
        "student": "student-audit-04",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-audit-06"
      },
      "editions": [
        "student",
        "teacher",
        "answer",
        "accessible"
      ],
      "keyed": true
    },
    {
      "id": "C07-T4",
      "number": "4",
      "semanticLabel": "PROVENANCE TRAIL",
      "icon": "ph-flow",
      "title": "Trace Each Copy's Provenance",
      "description": "Compare the two recorded custody trails, name the links one has and the other does not, and say what neither trail records.",
      "instructionalPurpose": "The provenance operation, performed on records that stop. The figure draws only steps the records contain and marks the head of both trails as unrecorded, so a learner who invents a creation event to complete the pattern has done the opposite of the skill. Part C is where corroboration first appears: a reason recorded at the time, matching an amendment on the page.",
      "provenance": [
        "The Archive's invented custody histories",
        "Curriculum-original schematic"
      ],
      "responseType": "two compact counts and three short constructed responses",
      "answerScope": "Exact counts, the two extra links named, the recorded reason with its significance, and one thing neither trail reaches.",
      "pagePlacement": {
        "student": "student-audit-05",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-audit-07"
      },
      "editions": [
        "student",
        "teacher",
        "answer",
        "accessible"
      ],
      "keyed": true
    },
    {
      "id": "C07-T5",
      "number": "5",
      "semanticLabel": "EVIDENCE WEIGHT",
      "icon": "ph-scales",
      "title": "Weigh the Four Evidence Sources",
      "description": "For each of the four sources, state what it establishes, what it cannot establish alone, and its evidentiary role.",
      "instructionalPurpose": "The signature HHH contribution-and-limitation operation, extended with a qualitative evidentiary role. The four sources are deliberately not equally probative: two participant accounts frame the case, an independent log with verified custody corroborates, and the records under judgment carry their own transmission. No numerical score exists anywhere in the case.",
      "provenance": [
        "The four invented case sources",
        "Curriculum-original schematic"
      ],
      "responseType": "twelve matrix fields, four of them closed role classifications",
      "answerScope": "Establishes and cannot-establish for each source, plus one role from the printed three-value set.",
      "pagePlacement": {
        "student": "student-audit-06",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-audit-08"
      },
      "editions": [
        "student",
        "teacher",
        "answer",
        "accessible"
      ],
      "keyed": true
    },
    {
      "id": "C07-T6",
      "number": "6",
      "semanticLabel": "COMPETING RECORDS",
      "icon": "ph-nodes",
      "title": "Compare the Competing Records",
      "description": "Set the two copies against each other on surface characteristics, amendments, recorded custody and transmission, and corroborating information, then name what remains uncertain.",
      "instructionalPurpose": "The matched comparison. The surface row is given rather than asked for, and the task states in print that surface characteristics alone do not settle the comparison — the row is on the table because a learner has to look at it, not because looking decides anything. The uncertainty field is required, not optional.",
      "provenance": [
        "The Archive's invented record of the flagged pair",
        "The invented audit log"
      ],
      "responseType": "six matrix fields plus one short constructed response",
      "answerScope": "Both copies on three dimensions, plus one genuine open question the packet does not settle.",
      "pagePlacement": {
        "student": "student-audit-07",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-audit-09"
      },
      "editions": [
        "student",
        "teacher",
        "answer",
        "accessible"
      ],
      "keyed": true
    },
    {
      "id": "C07-T7",
      "number": "7",
      "semanticLabel": "VALIDATION MEMORANDUM",
      "icon": "ph-wrench",
      "title": "Validate the Better-Supported Record",
      "description": "Write a Record Validation Memorandum naming the better-supported record, with two evidence links from different sources, an explanation of how they fit, one tempting clue that does not prove it, and a stated limit.",
      "instructionalPurpose": "The culminating historical-reasoning product, and a provenance/authenticity judgment rather than a canonical CER. Six parts, each separately scored, so that the multi-factor requirement cannot be satisfied by one confident sentence. Part E is the structural refusal: the learner must name a clue that looks like proof and say why it is not.",
      "provenance": [
        "All four invented case sources",
        "The certified real-world authenticity rule"
      ],
      "responseType": "one closed finding plus five constructed responses",
      "answerScope": "Copy B, supported by at least two independent evidentiary links, with a refused clue and a stated limit.",
      "pagePlacement": {
        "student": "student-audit-08",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-audit-10"
      },
      "editions": [
        "student",
        "teacher",
        "answer",
        "accessible"
      ],
      "keyed": true
    },
    {
      "id": "C07-T8",
      "number": "8",
      "semanticLabel": "TRANSFER EXIT",
      "icon": "ph-ticket",
      "title": "Test What Would Change Your Confidence",
      "description": "For an unfamiliar flagged record, name the additional evidence that would most increase and most decrease confidence in its authenticity, and explain both.",
      "instructionalPurpose": "Transfer, and deliberately about a record no source in the packet mentions. The prompt forbids naming either copy, so a learner who retells the case result has visibly failed to transfer. The Accessible bounded set includes the author-recollection option precisely because it is the trap that survives the case.",
      "provenance": [
        "Curriculum-authored transfer scenario",
        "The certified real-world authenticity rule"
      ],
      "responseType": "two short judgments plus one constructed explanation",
      "answerScope": "Any independent corroboration for the increase and any unexplained custody break for the decrease, each justified by method rather than by this case.",
      "pagePlacement": {
        "student": "student-audit-08",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-04",
        "accessible": "accessible-audit-10"
      },
      "editions": [
        "student",
        "teacher",
        "answer",
        "accessible"
      ],
      "keyed": true
    }
  ],
  "vocabulary": [
    "authenticity",
    "chain of custody",
    "corroboration",
    "integrity",
    "provenance",
    "transmission"
  ],
  "caseSources": [
    {
      "id": "audit-briefing",
      "displayLabel": "A · The audit briefing",
      "creator": "Dr Nova, TAA (invented)",
      "period": "2387 (invented)",
      "sourceType": "in-world testimony",
      "sourceOrigin": "fictional in-world testimony",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "evidentiaryRole": "CONTEXT",
      "contribution": "Establishes that a re-scan found a planted second layer beneath repaired records, that the planted records are complete and professionally made, and that two copies of one field report both name the same author.",
      "limitation": "Cannot establish which copy is genuine. It is a participant's account of the case, not of either page, and it names no feature of either document.",
      "gameCorrespondence": "Campaign 2, Level 0 — the audit briefing taken in the Briefing Chamber.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3"
    },
    {
      "id": "audit-pattern",
      "displayLabel": "B · The pattern across the flagged records",
      "creator": "Zel'keth, TAA (invented)",
      "period": "2387 (invented)",
      "sourceType": "in-world testimony",
      "sourceOrigin": "fictional in-world testimony",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "evidentiaryRole": "CONTEXT",
      "contribution": "Establishes that the insertions are non-random and sit at points where knowledge about growing food passed from one set of hands to another, so the flagged records were chosen rather than damaged.",
      "limitation": "Cannot establish which of two particular copies is the inserted one. A pattern across an archive is not a finding about a single page, and treating it as one is a named misconception.",
      "gameCorrespondence": "Campaign 2, Level 0 — the second archivist's account of the flagged pattern.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3"
    },
    {
      "id": "audit-log",
      "displayLabel": "C · The TAA audit log",
      "creator": "TAA Records (invented)",
      "period": "2387 (invented)",
      "sourceType": "in-world institutional record",
      "sourceOrigin": "fictional in-world archive record",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "evidentiaryRole": "CORROBORATING EVIDENCE",
      "contribution": "Establishes that the forger is expert, so a forgery in this case is complete and internally consistent; that the buried layer surfaced only when each record was set against recorded custody; and that the log's own custody is verified end to end, which is the condition on which it can be used to check anything else.",
      "limitation": "Cannot establish which of the two copies is the forged one. It describes the operation and the method, not either page.",
      "gameCorrespondence": "Campaign 2, Level 0 — the audit log read in the Briefing Chamber, including its method note.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 4"
    },
    {
      "id": "memo-pair",
      "displayLabel": "D · The competing memo pair and their custody histories",
      "creator": "TAA Thread Console (invented)",
      "period": "2387 (invented)",
      "sourceType": "in-world record pair with transmission history",
      "sourceOrigin": "fictional in-world archive record",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "evidentiaryRole": "DIRECT RECORD EVIDENCE",
      "contribution": "Establishes what each page carries, what each trail records, and that Copy B's trail holds a recall and a re-filing with a reason recorded at the time which matches an amendment visible on Copy B's page.",
      "limitation": "Cannot establish where or when either copy was made; both trails begin at intake. Nor can it establish that a short trail is complete rather than merely uneventful.",
      "gameCorrespondence": "Campaign 2, Level 0 — the memo pair examined at the Thread Console, with its custody comparison.",
      "fallbackCorrespondence": "Student page 3 · Accessible page 4"
    },
    {
      "id": "diplomatics-reference",
      "displayLabel": "The real discipline behind this case",
      "creator": "Society of American Archivists; U.S. National Archives and Records Administration",
      "period": "current reference sources",
      "sourceType": "reference definition and institutional guidance",
      "sourceOrigin": "real modern reference source",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "real",
      "evidentiaryRole": "METHOD",
      "contribution": "Supplies the name and definition of diplomatics, the identification of Mabillon's De Re Diplomatica (1681) in the SAA entry, the description of the work as weighing context with internal and external characteristics, and the four properties of a trustworthy record from which the multi-factor authenticity rule follows.",
      "limitation": "Establishes nothing whatever about the TAA. It is method rather than evidence, and neither source sets a test that could be applied to a single document by inspection.",
      "gameCorrespondence": "Corresponds to the remediated closing note of Campaign 2, Level 0, which states the same multi-factor rule.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 5"
    },
    {
      "id": "authenticity-figure",
      "displayLabel": "Figure — the multi-factor authenticity framework",
      "creator": "Curriculum",
      "period": "not applicable",
      "sourceType": "deterministic HTML and CSS schematic",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "evidentiaryRole": "ORGANISER",
      "contribution": "Shows five families of evidence converging on one authenticity judgment and prints the governing rule inside the figure.",
      "limitation": "Organises a method. It is not evidence about Copy A, Copy B or anything else, and it says so in print.",
      "gameCorrespondence": "No runtime counterpart. Drawn for this packet from the certified real-world reference.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 6"
    },
    {
      "id": "provenance-figure",
      "displayLabel": "Figure — the two-copy provenance and custody comparison",
      "creator": "Curriculum",
      "period": "not applicable",
      "sourceType": "deterministic HTML and CSS schematic",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "evidentiaryRole": "ORGANISER",
      "contribution": "Draws both recorded custody trails, marks the two links Copy B's trail has and Copy A's does not, and prints the reason recorded with the recall.",
      "limitation": "Draws only steps the records contain. The head of both trails is dashed and labelled NOT RECORDED, so the figure cannot be read as a claim about how either copy was made.",
      "gameCorrespondence": "Redrawn from the custody comparison shown at the Thread Console in Campaign 2, Level 0.",
      "fallbackCorrespondence": "Student page 5 · Accessible page 7"
    },
    {
      "id": "weight-figure",
      "displayLabel": "Figure — the evidence-weight organiser",
      "creator": "Curriculum",
      "period": "not applicable",
      "sourceType": "deterministic HTML and CSS schematic",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "evidentiaryRole": "ORGANISER",
      "contribution": "Names the three evidentiary roles the case uses and says which sources sit in each.",
      "limitation": "Qualitative. No number appears in it, no confidence value is implied, and two sources in the same band are not therefore equal.",
      "gameCorrespondence": "No runtime counterpart. Drawn for this packet.",
      "fallbackCorrespondence": "Student page 6 · Accessible page 8"
    }
  ],
  "editionResponseContract": {
    "rule": "Every assessed Accessible response has a Student counterpart. A subpart may hold fewer Accessible responses only under a registered adaptation, and may hold more only as a declared chunking split of one Student obligation.",
    "whyItExists": "Accessibility is measured here as a change of route rather than a change of demand, and the only way to prove that mechanically is to bind every persistent response on both editions to a named obligation.",
    "differenceClasses": {
      "parity": "Identical obligation and identical response count.",
      "declared-reduction": "Fewer Accessible responses, governed by a registered adaptation.",
      "chunking": "One Student obligation collected in more than one Accessible field. Never an increase in demand.",
      "accessible-only": "PROHIBITED. An Accessible response with no Student counterpart is a demand increase."
    },
    "identityFields": {
      "student": [
        "student-name",
        "student-date",
        "student-class"
      ],
      "accessible": [
        "a-name",
        "a-date",
        "a-class"
      ]
    },
    "subparts": [
      {
        "task": "C07-T1",
        "id": "vocabulary",
        "obligation": "Place all six terms.",
        "student": [
          "t1-term-1",
          "t1-term-2",
          "t1-term-3",
          "t1-term-4",
          "t1-term-5",
          "t1-term-6"
        ],
        "accessible": [
          "a1-term-1",
          "a1-term-2",
          "a1-term-3",
          "a1-term-4",
          "a1-term-5",
          "a1-term-6"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T2",
        "id": "evidence-to-check",
        "obligation": "Name the kinds of evidence you would verify first.",
        "student": [
          "t2-evidence"
        ],
        "accessible": [
          "a2-choice-1",
          "a2-choice-2"
        ],
        "differenceClass": "chunking",
        "chunkingNote": "One open listing of two kinds becomes two bounded slots, one per kind. The obligation is the same two judgments; only open recall becomes selection."
      },
      {
        "task": "C07-T2",
        "id": "test-reason",
        "obligation": "Say why one of them tells you more than the page.",
        "student": [
          "t2-reason"
        ],
        "accessible": [
          "a2-reason"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T3",
        "id": "clue-marks",
        "obligation": "Classify each observation by what it can carry.",
        "student": [
          "t3-mark-1",
          "t3-mark-2",
          "t3-mark-3",
          "t3-mark-4",
          "t3-mark-5",
          "t3-mark-6"
        ],
        "accessible": [
          "a3-mark-1",
          "a3-mark-2",
          "a3-mark-4",
          "a3-mark-5",
          "a3-mark-6"
        ],
        "differenceClass": "declared-reduction",
        "governedBy": "t3-modelled-judgment"
      },
      {
        "task": "C07-T3",
        "id": "clue-explanation",
        "obligation": "Explain why neither surface item settles authenticity.",
        "student": [
          "t3-explain"
        ],
        "accessible": [
          "a3-explain"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T4",
        "id": "trail-counts",
        "obligation": "Count the recorded custody entries on each trail.",
        "student": [
          "t4-count-a",
          "t4-count-b"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t4-supplied-totals"
      },
      {
        "task": "C07-T4",
        "id": "differing-links",
        "obligation": "Name the two steps one trail has and the other does not.",
        "student": [
          "t4-extra"
        ],
        "accessible": [
          "a4-extra"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T4",
        "id": "recorded-reason",
        "obligation": "State the recorded reason and why a recorded reason does more work.",
        "student": [
          "t4-meaning"
        ],
        "accessible": [
          "a4-meaning"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T4",
        "id": "unrecorded",
        "obligation": "Name something neither trail records.",
        "student": [
          "t4-unrecorded"
        ],
        "accessible": [
          "a4-unrecorded"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T5",
        "id": "weight-row-briefing",
        "obligation": "Weigh the audit briefing.",
        "student": [
          "t5-r1-est",
          "t5-r1-cannot",
          "t5-r1-role"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t5-modelled-row"
      },
      {
        "task": "C07-T5",
        "id": "weight-row-pattern",
        "obligation": "Weigh the pattern across the flagged records.",
        "student": [
          "t5-r2-est",
          "t5-r2-cannot",
          "t5-r2-role"
        ],
        "accessible": [
          "a5-r2-cannot",
          "a5-r2-role"
        ],
        "differenceClass": "declared-reduction",
        "governedBy": "t5-prefilled-row"
      },
      {
        "task": "C07-T5",
        "id": "weight-row-log",
        "obligation": "Weigh the audit log.",
        "student": [
          "t5-r3-est",
          "t5-r3-cannot",
          "t5-r3-role"
        ],
        "accessible": [
          "a5-r3-est",
          "a5-r3-cannot",
          "a5-r3-role"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T5",
        "id": "weight-row-memo",
        "obligation": "Weigh the memo pair and its custody histories.",
        "student": [
          "t5-r4-est",
          "t5-r4-cannot",
          "t5-r4-role"
        ],
        "accessible": [
          "a5-r4-est",
          "a5-r4-cannot",
          "a5-r4-role"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T6",
        "id": "compare-amendments",
        "obligation": "Compare the specific amendments on both copies.",
        "student": [
          "t6-amend-a",
          "t6-amend-b"
        ],
        "accessible": [
          "a6-amend-a",
          "a6-amend-b"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T6",
        "id": "compare-custody",
        "obligation": "Compare the recorded custody and transmission of both copies.",
        "student": [
          "t6-custody-a",
          "t6-custody-b"
        ],
        "accessible": [
          "a6-custody-a",
          "a6-custody-b"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T6",
        "id": "compare-corroboration",
        "obligation": "Compare what independently agrees with each copy.",
        "student": [
          "t6-corrob-a",
          "t6-corrob-b"
        ],
        "accessible": [
          "a6-corrob-a",
          "a6-corrob-b"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T6",
        "id": "compare-uncertain",
        "obligation": "Name what the packet does not settle about the two copies.",
        "student": [
          "t6-uncertain"
        ],
        "accessible": [
          "a6-uncertain"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T7",
        "id": "memo-finding",
        "obligation": "Name the better-supported record.",
        "student": [
          "t7-finding"
        ],
        "accessible": [
          "a7-finding"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T7",
        "id": "memo-links",
        "obligation": "Supply two evidentiary links from different sources.",
        "student": [
          "t7-link-1",
          "t7-link-2"
        ],
        "accessible": [
          "a7-link-1",
          "a7-link-2"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T7",
        "id": "memo-why",
        "obligation": "Explain how the two links fit together.",
        "student": [
          "t7-why"
        ],
        "accessible": [
          "a7-why"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T7",
        "id": "memo-clue",
        "obligation": "Name a clue that looks like proof and say why it is not.",
        "student": [
          "t7-clue"
        ],
        "accessible": [
          "a7-clue"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T7",
        "id": "memo-limit",
        "obligation": "State a limit on the finding.",
        "student": [
          "t7-limit"
        ],
        "accessible": [
          "a7-limit"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T8",
        "id": "transfer-judgments",
        "obligation": "Name evidence that would most raise and most lower confidence.",
        "student": [
          "t8-increase",
          "t8-decrease"
        ],
        "accessible": [
          "a8-increase",
          "a8-decrease"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C07-T8",
        "id": "transfer-explanation",
        "obligation": "Explain both judgments by method rather than by this case.",
        "student": [
          "t8-why"
        ],
        "accessible": [
          "a8-why"
        ],
        "differenceClass": "parity"
      }
    ]
  },
  "accessibleAdaptations": [
    {
      "id": "t3-modelled-judgment",
      "task": "C07-T3",
      "what": "Item 3 is supplied complete as a worked example, with the reason for its mark printed beside it.",
      "effect": "Accessible marks five items; Student marks six.",
      "whyNotALeak": "Item 3 is a corroboration item. The neatness item and the corrections item, which are the misconception barrier, are both still judged independently.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t4-supplied-totals",
      "task": "C07-T4",
      "what": "Both recorded custody totals are printed on the provenance figure.",
      "effect": "Accessible is not asked to count; Student completes two compact counts.",
      "whyNotALeak": "Counting is transcription. The reasoning target — which links differ, what the recorded reason does, and what neither trail reaches — is unchanged and fully independent.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t5-modelled-row",
      "task": "C07-T5",
      "what": "The audit-briefing row is supplied complete in all three cells as a worked example.",
      "effect": "Accessible completes eight matrix fields; Student completes twelve.",
      "whyNotALeak": "The modelled row is a CONTEXT source. The two sources that carry the record-authentication weight are worked independently in both editions.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t5-prefilled-row",
      "task": "C07-T5",
      "what": "The pattern row's first cell is supplied; its limitation and its role are not.",
      "effect": "Part of one repeated row is removed; the judgment in that row is preserved.",
      "whyNotALeak": "What the pattern establishes is stated on the source card itself. What it cannot establish, and what role that gives it, is the reasoning and is still required.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    }
  ],
  "semanticInvariants": {
    "scanScope": {
      "roles": [
        "student",
        "teacher",
        "answer",
        "accessible"
      ],
      "unit": "proposition, split on terminal punctuation only",
      "rule": "Every printable proposition in every role is scanned against the five closed authenticity classes. Internal punctuation is not a safety boundary.",
      "exemptionAttribute": "data-semantic-exemption",
      "designNote": "Exemption is a closed contract. A node is excused only by naming a registered exemption id that resolves for its own role; markup cannot self-authorize, and an invented attribute value excuses nothing."
    },
    "exemptions": [
      {
        "id": "teacher-misconception",
        "roles": [
          "teacher"
        ],
        "purpose": "Teacher pages must be able to quote the misconception in order to name it and refuse it.",
        "allowedConcepts": [
          "neatProvesForged",
          "correctionsProveAuthentic",
          "messyIsGenuine",
          "noCorrectionsProveForgery",
          "visibleCorrectionsProveAuthenticity"
        ]
      },
      {
        "id": "answer-key-floor",
        "roles": [
          "answer"
        ],
        "purpose": "The Answer Key must be able to state the wording it refuses at every level.",
        "allowedConcepts": [
          "neatProvesForged",
          "correctionsProveAuthentic",
          "messyIsGenuine",
          "noCorrectionsProveForgery",
          "visibleCorrectionsProveAuthenticity"
        ]
      }
    ],
    "structuralExemptSelectors": []
  },
  "figureContract": {
    "rule": "Every figure is deterministic HTML and CSS, carries a printed STATUS line, and carries accessibility text held to the same factual contracts as the visible drawing. No generated imagery is used anywhere in this package.",
    "figures": [
      {
        "id": "authenticity-framework",
        "selector": "[data-authenticity-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "multi-factor authenticity framework",
        "requiresFamilies": [
          "MATERIALS",
          "HANDWRITING",
          "PROVENANCE",
          "CUSTODY",
          "CORROBORATION"
        ],
        "requiresPrintedRule": "No single surface feature proves authenticity or forgery.",
        "requiresSchematicDisclaimer": true,
        "prohibitedPatterns": [
          {
            "id": "single-factor-verdict",
            "regex": "\\b(?:clean|neat|pristine)\\b[^.!?]{0,60}\\b(?:proves?|means?)\\b[^.!?]{0,40}\\b(?:forged|fake)\\b",
            "why": "The figure exists to refuse the single-factor verdict; its accessibility text may not state one."
          },
          {
            "id": "numeric-confidence",
            "regex": "\\b\\d+\\s?(?:%|per cent|percent)\\b",
            "why": "No numerical confidence value is supported anywhere in this case."
          }
        ]
      },
      {
        "id": "provenance-comparison",
        "selector": "[data-provenance-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "H1 source/provenance chain",
        "requiresUnrecordedHead": true,
        "requiresBothTrails": true,
        "prohibitedPatterns": [
          {
            "id": "invented-creation-event",
            "regex": "\\b(?:written|created|copied|made)\\s+(?:on|at|in)\\s+\\d",
            "why": "Neither trail records the making of either copy; a dated creation event would be invented."
          },
          {
            "id": "numeric-confidence",
            "regex": "\\b\\d+\\s?(?:%|per cent|percent)\\b",
            "why": "No numerical confidence value is supported anywhere in this case."
          }
        ]
      },
      {
        "id": "evidence-weight",
        "selector": "[data-weight-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "qualitative evidentiary-role organiser",
        "requiresRoles": [
          "CONTEXT",
          "CORROBORATING EVIDENCE",
          "DIRECT RECORD EVIDENCE"
        ],
        "requiresNoScore": true,
        "prohibitedPatterns": [
          {
            "id": "numeric-weight",
            "regex": "\\b(?:weight|score|confidence|rating)\\s*(?:of\\s*)?\\d",
            "why": "The organiser is qualitative; a numeric weight would fabricate precision the case does not have."
          },
          {
            "id": "numeric-confidence",
            "regex": "\\b\\d+\\s?(?:%|per cent|percent)\\b",
            "why": "No numerical confidence value is supported anywhere in this case."
          }
        ]
      }
    ]
  },
  "standards": {
    "directlyAssessed": [
      "C3 D3.1.6-8",
      "C3 D3.2.6-8",
      "CCSS RH.6-8.6"
    ],
    "supporting": [
      "CCSS WHST.6-8.1",
      "CCSS RH.6-8.9"
    ],
    "contextual": [],
    "ngss": "No NGSS alignment is claimed at any status. This case contains no science content; it assesses source criticism, provenance and corroboration. Attaching a science performance expectation to it would be a false claim about what the tasks measure.",
    "rationale": "Task-first alignment. The three directly assessed claims each name the task that measures them and the limit on the claim: the sources are supplied rather than researched, all four case sources are invented, and the texts are curriculum-written rather than excerpted. Two claims are supporting: the written argument in Task 7, which is scored for reasoning rather than for craft, and the record-to-record comparison in Tasks 6 and 7, which practises the relationship a primary-versus-secondary analysis rests on without assessing that analysis itself. The list is deliberately short; nothing is claimed merely because the topic touches it."
  }
};
