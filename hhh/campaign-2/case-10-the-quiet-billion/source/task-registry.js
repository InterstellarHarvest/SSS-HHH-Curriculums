window.HHH_CASE10_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C2-CASE10",
  "runtimeId": "C2L3",
  "instructionalType": "CORE_CASE",
  "title": "The Quiet Billion",
  "displayLabel": "10 - The Quiet Billion",
  "version": "0.1",
  "status": "DRAFT",
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
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
  "learningGoal": "Evaluate competing Green Revolution claims by interpreting quantitative wheat evidence, separating reconstructed game evidence from documented history, and explaining how improved wheat varieties contributed to production gains within a larger system of agronomy, inputs, institutions and policy — without treating one statistic or the phrase “saved a billion lives” as proof of a single cause.",
  "guidingQuestion": "How should historians explain the 1960s wheat gains when the numbers rose, improved varieties mattered, several conditions changed at once, and both the strongest success story and the strongest failure story claim more than the evidence can prove?",
  "culminatingProduct": "Qualified Historical Finding — a five-part product. The learner states what the evidence supports, uses at least one quantitative India value or trend with its units and scope, uses at least one additional documented source, identifies other contributing conditions and states something the evidence does not prove, and identifies the additional evidence that would better isolate the varietal effect or connect agricultural production to hunger and human welfare. Canonical CER is deliberately not used; see cerDecision.",
  "conceptualDistinction": "Production, yield, hunger, welfare and a counterfactual count of lives saved are five different things. A correct agricultural mechanism or a real yield increase does not by itself settle questions of hunger, distribution, environment, policy or human welfare, and no source in this package measures how much of the gain came from the variety.",
  "cerDecision": {
    "id": "case10-cer-declined-v1.0",
    "decision": "DECLINED",
    "blueprintProduct": "qualified evidence-based historical argument about the contribution of improved varieties within a larger input/institutional system (Blueprint, Core Case 10)",
    "rationale": "The Blueprint permits canonical CER only where its structure genuinely supports the case, and names a qualified evidence-based historical argument as this case's culminating product. Case 10 separately assesses six obligations — quantitative interpretation, source-status discipline, competing interpretation, multi-causal qualification, evidentiary limitation and next-evidence reasoning — and a claim/evidence/reasoning sequence would flatten them into one. The three that would be lost are precisely the three the case exists for: the causal qualification, the explicit statement of what the evidence does not prove, and the identification of the evidence that would be needed next. The Qualified Historical Finding keeps five obligations separately visible and separately scored.",
    "precedent": "HHH Campaign 1 Core Case 06 declined canonical CER for its systems and evidence-audit explanation on the Blueprint ground, Campaign 2 Core Case 07 followed it for its provenance and authenticity judgment, Core Case 08 for its engineered-landscape explanation and Core Case 09 for its collection continuity judgment. This case follows that established precedent rather than inventing a new one.",
    "enforcement": "No role renders the shared canonical CER component, and no role declares a CER contract.",
    "prohibitedSelectors": [
      "[data-cer-contract]",
      ".canonical-cer",
      ".cer-stack"
    ]
  },
  "sourceStatusContract": {
    "rule": "Every learner-facing evidence object declares its status in markup (data-evidence-layer) and in printed text (a SOURCE STATUS line), and no role converts reconstructed game evidence into a claim about the real Green Revolution or a documented source into evidence that a game record is genuine.",
    "bands": [
      {
        "id": "reconstructed",
        "label": "RECONSTRUCTED GAME EVIDENCE",
        "attribute": "reconstructed",
        "statusMarker": "reconstructed game evidence",
        "covers": [
          "the recovered Borlaug record and the Archive's annotation of it, including the Archive's filing claim",
          "the two wheats and the Archive's trait scan of them",
          "the pedigree records and the Archive's cross-reference",
          "Dr. Rao and everything he says, including his field-yield figure",
          "the Failure Report, its claims and its paperwork",
          "every date, count, name, measurement, reading and quotation belonging to any of the above"
        ],
        "rule": "Evidence written for the game. It may be reasoned about, compared and tested inside the case. It may never be cited as a fact about the real Mexican programme, the real Indian harvests, any real person, or any real number."
      },
      {
        "id": "documented",
        "label": "DOCUMENTED",
        "attribute": "documented",
        "statusMarker": "documented",
        "covers": [
          "the Government of India wheat record for the crop years 1964-65 to 1969-70",
          "Norman Borlaug's Nobel lecture of 11 December 1970, used as a primary participant source",
          "CIMMYT's account of the transmission of the Norin 10 dwarfing",
          "Pingali's 2012 retrospective in the Proceedings of the National Academy of Sciences"
        ],
        "rule": "Real published sources, cited to a real government, laureate, research centre or journal. Each establishes claims about the real Green Revolution within its own stated bounds. None is ever evidence that any event or record in the game is genuine."
      },
      {
        "id": "curriculum-model",
        "label": "CURRICULUM-ORIGINAL FIGURE",
        "attribute": "curriculum-model",
        "statusMarker": "curriculum-original figure",
        "covers": [
          "the India wheat record figure",
          "the transmission route figure",
          "the production package figure"
        ],
        "rule": "Drawn for this packet from the documented sources by deterministic HTML and CSS. A figure organises evidence and is not itself evidence; each figure prints its basis and its status."
      }
    ],
    "statusVocabulary": [
      "reconstructed game evidence",
      "documented",
      "curriculum-original figure"
    ],
    "layerAttribute": "data-evidence-layer",
    "layerValues": [
      "reconstructed",
      "documented",
      "curriculum-model"
    ],
    "noticeRequired": [
      "student",
      "accessible"
    ],
    "noticeSelector": "[data-source-status-notice]",
    "nonMergerRule": "Reconstructed game evidence can support a judgment about the game's record. It cannot establish a real historical claim. Documented historical evidence can support claims about the Green Revolution. It cannot prove that a game record is genuine. Both learner editions carry this rule on page 1.",
    "titleBoundaryRule": "The title comes from the game. Treat “a billion lives” as a claim that would require a stated method and counterfactual, not as a measurement supplied by this packet. Both learner editions carry this sentence on page 1, and no task asks a learner to calculate, repeat, validate or endorse a numerical lives-saved figure.",
    "titleBoundarySelector": "[data-title-boundary]",
    "nonMergerSelector": "[data-non-merger-rule]",
    "fictionalDataRule": "Every deterministic invented value sits inside a node carrying data-fictional-data, and every such node sits inside a reconstructed evidence object.",
    "gameClaimRule": "A learner or teacher page may quote a claim made inside the game in order to test it. Every such quotation outside a reconstructed evidence object is wrapped in a node carrying data-game-claim, sits inside a task marked data-tests-game-claim, and is excused from the game-layer semantic classes only while it is so marked.",
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
      "locationFx",
      "spritesheet",
      "bonusInsight",
      "archiveFigure",
      "menuName",
      "rankUpText",
      "ranksUp",
      "funFact",
      "briefing",
      "trials_succeeded",
      "lodging_resistance",
      "pedigree_verified",
      "real_yields",
      "forgery_read",
      "harvest_scale",
      "trial_plots",
      "research_station",
      "deployment_field",
      "bannerLocation",
      "resolveNag",
      "patternInterject"
    ],
    "prohibitedRuntimeIdentifierRule": "Runtime implementation identifiers are never learner-facing or teacher-facing content. None of these strings appears in any printable role.",
    "enforcedRoles": [
      "student",
      "teacher",
      "answer",
      "accessible"
    ]
  },
  "runtimeDependency": {
    "id": "case10-runtime-dependency-v1.0",
    "findingId": "HHH-GAME-C2L3-001",
    "dependencyClass": "CURRICULUM_QUALIFICATION_REQUIRED",
    "dependencyStatus": "OPEN_AT_AUDITED_GAME_BASELINE",
    "auditedGameCommit": "9b8545ed6ecf98b337326390400076e36789e056",
    "currentGameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
    "gameModificationRequired": false,
    "verifiedSemantics": "The current game main is three commits after the audited baseline and the intervening remediation affects other levels; C2 L3 carries no substantive post-audit change. The level has four operationally required evidence clues and two insight-flagged sources, one of which is the Failure Report. This package does not modify the game, does not reopen the game audit and does not initiate game remediation.",
    "requiredStrandCount": 4,
    "insightStrandCount": 2,
    "rule": "Case 10 carries only HHH-GAME-C2L3-001, a curriculum qualification. The game may remain unchanged, and this package leaves the shared remediation tracker untouched.",
    "qualificationFindingId": "HHH-GAME-C2L3-001",
    "qualificationClass": "CURRICULUM_QUALIFICATION_REQUIRED",
    "qualificationStatus": "OPEN_AT_AUDITED_GAME_BASELINE",
    "qualificationRule": "The audit found the core semi-dwarf, lodging and rust story sound, but held that exact field-yield claims and any “one seed saved a billion” shorthand must not replace broader irrigation, fertiliser and institutional context. The packet carries that qualification in every role: every game figure is printed inside a reconstructed card and marked as invented, the title's claim is refused as a measurement on learner page 1, and the production package is taught as an interacting system in a figure, a task and the Teacher Guide."
  },
  "historicalQualification": {
    "id": "case10-historical-qualification-v1.0",
    "findingId": "HHH-GAME-C2L3-001",
    "rule": "Improved semi-dwarf wheat was an important contributor to large productivity and production gains, but the realised gains occurred through an interacting system including agronomy, fertiliser, irrigation and water management, research, seed multiplication and distribution, extension, credit and pricing, institutions and policy. The packet teaches that conclusion and refuses both extremes.",
    "rejectedOverclaim": "The new wheat alone caused the Green Revolution and therefore proves that one breeder, one seed or one innovation saved a billion lives.",
    "rejectedOvercorrection": "Because the Green Revolution involved environmental, distributional or social costs, the wheat gains were unreal or historically worthless.",
    "refusedSimplifications": [
      "that the new seed alone caused the wheat gains",
      "that any counted number of lives saved is an established historical fact",
      "that a rise in total production is the same as a rise in yield",
      "that semi-dwarfing or short straw is what produces rust resistance",
      "that a document's paperwork settles its authenticity in either direction"
    ],
    "measureRule": "Production, yield, hunger, welfare and a counterfactual count of lives saved are five different things. Yield is production per unit of area. A rise in total production can come from greater yield per hectare, greater planted area, or both. Moving from any one of the five to the next is a separate claim requiring separate evidence.",
    "traitRule": "Semi-dwarfing, short stiff straw and lodging resistance are one trait family; rust resistance is another. Successful varieties combined multiple useful traits because breeders selected for them; dwarfing does not biologically cause rust resistance, and a tall wheat can be rust-resistant.",
    "printedRule": "Production, yield, hunger, welfare and a counterfactual count of lives saved are five different things",
    "requiredPrintedStatements": [
      "The title comes from the game",
      "a claim that would require a stated method and counterfactual",
      "It cannot establish a real historical claim",
      "It cannot prove that a game record is genuine",
      "Production, yield, hunger, welfare and a counterfactual count of lives saved are five different things",
      "Two separate traits",
      "neither trait produces the other",
      "not based solely on the use of Mexican dwarf varieties",
      "No contributor here produced the result alone",
      "1,103",
      "16.54",
      "51.1%",
      "16.63"
    ],
    "requiredPrintedStatementRoles": [
      "student",
      "accessible"
    ],
    "positiveRequirements": [
      {
        "id": "record-figure-present",
        "selector": "[data-quant-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the quantitative record figure, with production and yield drawn as two separate graphs."
      },
      {
        "id": "route-figure-present",
        "selector": "[data-route-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the transmission route figure."
      },
      {
        "id": "package-figure-present",
        "selector": "[data-package-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the production package figure."
      },
      {
        "id": "package-rule-printed",
        "selector": "[data-package-rule='no-measured-share']",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print, inside the package figure, that no contributor produced the result alone and that no share is claimed."
      },
      {
        "id": "route-rule-printed",
        "selector": "[data-route-rule='not-a-map']",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print, inside the route figure, that it is a route and not a map of 1968 borders."
      },
      {
        "id": "title-boundary-printed",
        "selector": "[data-title-boundary]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print the title boundary on page 1."
      },
      {
        "id": "non-merger-printed",
        "selector": "[data-non-merger-rule]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print the non-merger rule on page 1."
      },
      {
        "id": "layer-table-printed",
        "selector": "[data-evidence-layer-table]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the three-layer can-establish / cannot-establish table."
      },
      {
        "id": "claim-test-printed",
        "selector": "[data-claim-test]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the four-test organiser that keeps the Failure Report inside the game."
      },
      {
        "id": "interpretations-printed",
        "selector": "[data-interpretations]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the three competing interpretations with a supports and an overreach column."
      },
      {
        "id": "finding-printed",
        "selector": "[data-qualified-finding]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the five-part Qualified Historical Finding."
      },
      {
        "id": "measure-boundary-printed",
        "selector": "[data-measure-boundary]",
        "roles": [
          "teacher"
        ],
        "rule": "The Teacher Guide prints the five-measures boundary as its own block."
      },
      {
        "id": "trait-boundary-printed",
        "selector": "[data-trait-boundary]",
        "roles": [
          "teacher"
        ],
        "rule": "The Teacher Guide prints the semi-dwarfing versus rust-resistance boundary as its own block."
      },
      {
        "id": "answer-key-floor-printed",
        "selector": "[data-answer-key-floor]",
        "roles": [
          "answer"
        ],
        "rule": "The Answer Key states the claims that are refused at every level."
      },
      {
        "id": "answer-key-measure-exemplar",
        "selector": "[data-measure-exemplar]",
        "roles": [
          "answer"
        ],
        "rule": "The Answer Key's Task 4 exemplar distinguishes production, yield, area and irrigation explicitly."
      },
      {
        "id": "answer-key-two-layer-verdict",
        "selector": "[data-two-layer-verdict]",
        "roles": [
          "answer"
        ],
        "rule": "The Answer Key's Task 7 exemplar separates the in-game verdict from the historical interpretation."
      },
      {
        "id": "answer-key-finding-exemplar",
        "selector": "[data-qualified-finding-exemplar]",
        "roles": [
          "answer"
        ],
        "rule": "The Answer Key models all five obligations of the finding."
      }
    ],
    "prohibitedFramings": {
      "rule": "Five CLOSED negative classes, each anchored to a named subject register and each requiring an affirmative, unnegated predicate. A proposition violates a class only when the class's subject is present in the same proposition and one of its patterns matches, and, for a class that declares unlessPatterns, when none of those qualifiers is present in the same proposition. Propositions inside a reconstructed evidence object, or inside a marked in-game quotation, are the game layer and are excused from the two classes the game itself asserts. This is a bounded guard against five known high-risk misconceptions. It is not, and does not claim to be, a general semantic detector: an unseen paraphrase can pass it, and manual cross-role review remains required.",
      "livesSavedAsMeasurement": {
        "why": "A counted number of lives saved, fed or rescued asserted as documented history rather than as a claim.",
        "subjectPatterns": [
          "\\bbillion\\b"
        ],
        "patterns": [
          "\\b(?:saved|fed|rescued)\\b(?:[^.!?]{0,20})\\b(?:a|one|about a|nearly a|almost a|roughly a)?\\s*billion\\b",
          "\\b(?:a|one) billion (?:lives|people)\\b[^.!?]{0,24}\\b(?:were|was|hung on|depended on|rested on|saved|fed)\\b",
          "\\bbillion (?:lives|people)\\b[^.!?]{0,16}\\b(?:saved|fed|rescued)\\b"
        ],
        "unlessPatterns": [
          "\\b(?:claims?|claimed|would require|not a measurement|does not|do not|cannot|no source|counts no|method|counterfactual|refuses?|refused|not keyed|would need|the game's phrase)\\b"
        ],
        "layerExempt": true
      },
      "seedAloneCausation": {
        "why": "The variety, seed or wheat asserted as the sole cause of the agricultural gains.",
        "subjectPatterns": [
          "\\b(?:seed|variety|varieties|wheat|semi-?dwarf\\w*|breeder|innovation)\\b"
        ],
        "patterns": [
          "\\b(?:seed|variety|varieties|wheat|semi-?dwarf\\w*)\\b\\s+(?:alone|by itself|on its own)\\b[^.!?]{0,30}\\b(?:caused|causes|explains?|produced|produces|created|creates|drove|delivered|made|accounts for|is why)\\b",
          "\\b(?:the )?(?:sole|only) (?:cause|reason|explanation|factor)\\b[^.!?]{0,30}\\b(?:was|is|were|are)\\b[^.!?]{0,24}\\b(?:the )?(?:seed|variety|varieties|wheat|semi-?dwarf\\w*)\\b",
          "\\b(?:seed|variety|varieties|wheat|semi-?dwarf\\w*)\\b[^.!?]{0,24}\\b(?:was|were|is|are)\\b[^.!?]{0,12}\\bthe (?:sole|only) (?:cause|reason|explanation|factor)\\b",
          "\\b(?:one|a single) (?:seed|variety|breeder|innovation)\\b[^.!?]{0,30}\\b(?:caused|causes|explains?|produced|created|drove|transformed)\\b"
        ],
        "unlessPatterns": [
          "\\b(?:not|never|no longer|cannot|do not credit|is not|was not|were not|refuses?|refused|denies|denied|myth|wrong|false|overreach\\w*|rather than)\\b"
        ],
        "layerExempt": true
      },
      "productionIsYield": {
        "why": "Total production and yield per unit area treated as the same measure, or a production rise asserted as a yield rise.",
        "subjectPatterns": [
          "\\b(?:production|yield|harvest\\w*|tonnes)\\b"
        ],
        "patterns": [
          "\\b(?:production|the harvest|total production|the total harvest)\\b[^.!?]{0,20}\\b(?:is|are|means|equals|is the same as|was the same as)\\b[^.!?]{0,12}\\byield\\b",
          "\\byield\\b[^.!?]{0,20}\\b(?:is|means|equals|is the same as|was the same as)\\b[^.!?]{0,16}\\b(?:production|the total harvest|total production)\\b",
          "\\b(?:a|the) (?:rise|increase) in (?:total )?production\\b[^.!?]{0,24}\\b(?:is|means|shows|is the same as)\\b[^.!?]{0,24}\\b(?:a |the )?(?:rise|increase) in yield\\b",
          "\\bproduction\\b[^.!?]{0,14}\\b(?:went up|rose|increased)\\b[^.!?]{0,10}\\bso\\b[^.!?]{0,20}\\byield\\b[^.!?]{0,20}\\b(?:went up|rose|increased)\\b"
        ],
        "unlessPatterns": [
          "\\b(?:multiplied by|times|divided by|per unit|per hectare|not the same|are different|two different|five different|separately|rather than)\\b"
        ]
      },
      "dwarfingCausesRust": {
        "why": "Semi-dwarfing, short straw or lodging resistance asserted as the cause of rust or disease resistance.",
        "subjectPatterns": [
          "\\b(?:semi-?dwarf\\w*|dwarfing|dwarf|short(?:er)? straw|short)\\b"
        ],
        "patterns": [
          "\\b(?:semi-?dwarf\\w*|dwarfing|the short straw|short(?:er)? straw|making (?:the|it) (?:wheat )?short)\\b[^.!?]{0,30}\\b(?:causes?|caused|gave|gives|produces?|produced|creates?|created|makes? it|made it|is what|is why)\\b[^.!?]{0,24}\\b(?:stem-?rust|rust|disease)[- ]?resistan\\w*\\b",
          "\\b(?:stem-?rust|rust|disease)[- ]?resistance\\b[^.!?]{0,24}\\b(?:comes from|came from|results from|resulted from|is caused by|was caused by|is produced by|because of)\\b[^.!?]{0,24}\\b(?:semi-?dwarf\\w*|dwarfing|the short straw|short(?:er)? straw)\\b",
          "\\b(?:semi-?dwarf\\w*|dwarfing|the short straw|short(?:er)? straw|making (?:the|it) (?:wheat )?short)\\b[^.!?]{0,30}\\b(?:causes?|caused|gave|gives|makes? it|made it|is what|is why)\\b[^.!?]{0,20}\\bresistant to (?:stem )?rust\\b"
        ],
        "unlessPatterns": [
          "\\b(?:not|never|no|cannot|do not|does not|neither|separate|two goals|two traits|three separate)\\b"
        ]
      },
      "productionEndsHunger": {
        "why": "Agricultural production or yield asserted to have directly ended hunger, famine or malnutrition, or to have produced welfare.",
        "subjectPatterns": [
          "\\b(?:production|harvests?|wheat|food|yields?|green revolution|hunger|famine|starvation|malnutrition)\\b"
        ],
        "patterns": [
          "\\b(?:the )?(?:green revolution|new wheat|higher (?:yields?|production)|the harvests?|more (?:wheat|food|grain))\\b[^.!?]{0,30}\\b(?:ended|eliminated|solved|abolished|wiped out|stopped|cured)\\b[^.!?]{0,16}\\b(?:hunger|famine|starvation|malnutrition|poverty)\\b",
          "\\b(?:hunger|famine|starvation|malnutrition)\\b[^.!?]{0,16}\\b(?:was|were)\\b[^.!?]{0,12}\\b(?:ended|eliminated|solved|abolished|wiped out)\\b[^.!?]{0,24}\\bby (?:the )?(?:green revolution|new wheat|higher yields?|more (?:wheat|food))\\b",
          "\\b(?:more (?:wheat|food|grain)|higher (?:yields?|production)|the harvests?)\\b[^.!?]{0,16}\\b(?:means?|meant|proves?|shows?)\\b[^.!?]{0,16}\\b(?:hunger|famine|starvation)\\b[^.!?]{0,16}\\b(?:ended|is over|was over|gone)\\b"
        ],
        "unlessPatterns": [
          "\\b(?:not|never|no|cannot|does not|do not|persisted|remains?|remained|uneven|exception|is not|was not)\\b"
        ]
      }
    },
    "negativeControls": {
      "livesSavedAsMeasurement": [
        "The new wheat saved a billion lives.",
        "Borlaug fed a billion people.",
        "A billion lives were saved by the semi-dwarf varieties.",
        "A billion lives hung on the wheat."
      ],
      "seedAloneCausation": [
        "The new seed alone caused the wheat gains.",
        "The variety by itself explains the whole rise.",
        "The sole cause of the transformation was the wheat.",
        "One breeder transformed the food supply of the world."
      ],
      "productionIsYield": [
        "Production is yield.",
        "A rise in total production is the same as a rise in yield.",
        "Production went up, so yield went up by the same amount.",
        "Yield means total production."
      ],
      "dwarfingCausesRust": [
        "Making the wheat short is what made it rust-resistant.",
        "Semi-dwarfing gave the wheat its rust resistance.",
        "The short straw is what made it resistant to rust.",
        "Rust resistance comes from the dwarfing genes."
      ],
      "productionEndsHunger": [
        "The green revolution ended hunger.",
        "More wheat means hunger ended.",
        "Higher yields eliminated famine.",
        "Starvation was eliminated by the new wheat."
      ]
    },
    "positiveControls": [
      "The title comes from the game.",
      "A billion lives is a claim that would require a stated method and counterfactual.",
      "No source in this packet counts lives.",
      "Improved semi-dwarf wheat was an important contributor to the production gains.",
      "The gains came from an interacting system of varieties, fertiliser, water, agronomy, institutions and policy.",
      "Borlaug says the increase was not based solely on the use of Mexican dwarf varieties.",
      "Production is yield multiplied by area, which is why the two percentages are different.",
      "Production, yield, hunger, welfare and a counterfactual count of lives saved are five different things.",
      "Wheat production rose from 11.39 to 16.54 million tonnes while yield rose from 887 to 1,103 kilograms per hectare.",
      "The area sown rose and the irrigated share of the wheat area fell in the same crop year.",
      "Short stiff straw answers lodging and rust resistance answers a fungus.",
      "Breeders combined semi-dwarf, rust resistant and photoperiod insensitive traits in one variety.",
      "A tall wheat can be rust-resistant.",
      "Calorie availability rose, but micronutrient malnutrition persisted.",
      "Sub-Saharan Africa is the exception to the global trend.",
      "The green revolution has won a temporary success and has given man a breathing space.",
      "The record shows that production rose, and it does not say how much of that rise the new wheat caused.",
      "A correct mechanism is not a measured share."
    ]
  },
  "quantitativeRecord": {
    "id": "case10-india-record-v1.0",
    "selector": "[data-quant-contract]",
    "roles": [
      "student",
      "accessible"
    ],
    "source": "india-wheat-record",
    "rule": "The exact published six-year Government of India wheat series, printed in full in both learner editions. Production and yield are drawn as two separate graphs on two separate printed scales; area sown and the irrigated share of the wheat area are printed in an accompanying table. Every bar prints its own value, so the figure is readable without colour. No value is approximated, rounded or generated visually.",
    "units": {
      "area": "million hectares",
      "production": "million tonnes",
      "yield": "kilograms per hectare",
      "irrigatedShare": "per cent of the wheat area"
    },
    "series": [
      {
        "cropYear": "1964-65",
        "area": "13.42",
        "production": "12.26",
        "yield": "913",
        "irrigatedShare": "36.8%"
      },
      {
        "cropYear": "1965-66",
        "area": "12.57",
        "production": "10.40",
        "yield": "827",
        "irrigatedShare": "43.1%"
      },
      {
        "cropYear": "1966-67",
        "area": "12.84",
        "production": "11.39",
        "yield": "887",
        "irrigatedShare": "48.0%"
      },
      {
        "cropYear": "1967-68",
        "area": "14.99",
        "production": "16.54",
        "yield": "1,103",
        "irrigatedShare": "43.4%"
      },
      {
        "cropYear": "1968-69",
        "area": "15.96",
        "production": "18.65",
        "yield": "1,169",
        "irrigatedShare": "49.8%"
      },
      {
        "cropYear": "1969-70",
        "area": "16.63",
        "production": "20.09",
        "yield": "1,208",
        "irrigatedShare": "51.1%"
      }
    ],
    "internalConsistency": "Area multiplied by yield reproduces production to within published rounding in all six crop years, which is the arithmetic identity the case teaches and an independent check on the transcription.",
    "measuresRequiredVisible": [
      "production",
      "yield",
      "area",
      "irrigatedShare"
    ],
    "twoGraphRule": "Production and yield are never drawn on one shared value axis. Each column declares its own unit and its own scale, and the figure prints an instruction not to compare a bar in one column with a bar in the other.",
    "requiredPrintedText": [
      "PRODUCTION",
      "YIELD",
      "scale 0 to 22",
      "scale 0 to 1,300",
      "12.26",
      "10.40",
      "11.39",
      "16.54",
      "18.65",
      "20.09",
      "913",
      "827",
      "887",
      "1,103",
      "1,169",
      "1,208",
      "13.42",
      "12.57",
      "12.84",
      "14.99",
      "15.96",
      "16.63",
      "36.8%",
      "43.1%",
      "48.0%",
      "43.4%",
      "49.8%",
      "51.1%",
      "Area sown",
      "Irrigated share of the wheat area"
    ],
    "requiresCaptionTerms": [
      "BASED ON",
      "GOVERNMENT OF INDIA",
      "EXACT PUBLISHED VALUES",
      "TWO SEPARATE SCALES"
    ],
    "requiresAltConcepts": [
      "two separate bar graphs",
      "production",
      "million tonnes",
      "yield",
      "kilograms per hectare",
      "the two scales are different",
      "area sown",
      "irrigated share"
    ],
    "prohibitedPatterns": [
      {
        "id": "single-shared-axis",
        "regex": "\\b(?:shared|single|one) (?:axis|scale)\\b",
        "why": "The two measures are drawn on two separate scales and the figure must not claim otherwise."
      },
      {
        "id": "lives-in-the-figure",
        "regex": "\\blives\\b",
        "why": "The quantitative record reports crops, not lives, and its accessibility text may not introduce one."
      },
      {
        "id": "causal-attribution",
        "regex": "\\b(?:because of the (?:new )?(?:seed|variety)|caused by the (?:new )?(?:seed|variety))\\b",
        "why": "The record attributes nothing to any cause and its accessibility text may not do so either."
      }
    ]
  },
  "transmissionRoute": {
    "id": "case10-route-v1.0",
    "selector": "[data-route-contract]",
    "roles": [
      "student",
      "accessible"
    ],
    "rule": "A deterministic four-stage route showing the documented movement of the dwarfing trait and the breeding material, from Japan through the United States and Mexico to India and West Pakistan. Every stage is certified by Source H or Source G. It is drawn as a route and not as a map, and it prints that it does not represent the political geography of 1968.",
    "stages": [
      {
        "id": "japan",
        "label": "JAPAN",
        "when": "1935",
        "certifiedBy": "cimmyt-history"
      },
      {
        "id": "united-states",
        "label": "UNITED STATES",
        "when": "late 1940s",
        "certifiedBy": "cimmyt-history"
      },
      {
        "id": "mexico",
        "label": "MEXICO",
        "when": "1953-1962",
        "certifiedBy": "cimmyt-history"
      },
      {
        "id": "south-asia",
        "label": "INDIA & WEST PAKISTAN",
        "when": "1963-1968",
        "certifiedBy": "borlaug-nobel-lecture"
      }
    ],
    "linkLabels": [
      "S. D. Salmon (USDA) carries samples home",
      "Borlaug writes to Vogel for seed carrying the dwarfing genes",
      "seed shipped for on-farm testing, then in bulk"
    ],
    "requiredPrintedText": [
      "JAPAN",
      "UNITED STATES",
      "MEXICO",
      "INDIA & WEST PAKISTAN",
      "Norin 10",
      "Rht1",
      "Rht2",
      "Vogel",
      "Salmon",
      "Pitic 62",
      "Penjamo 62",
      "only after agronomy practices are changed"
    ],
    "requiredRule": "This is a route, not a map",
    "requiresCaptionTerms": [
      "BASED ON",
      "CIMMYT",
      "BORLAUG NOBEL LECTURE 1970",
      "NOT A MAP TO SCALE"
    ],
    "requiresAltConcepts": [
      "japan",
      "1935",
      "norin 10",
      "united states",
      "vogel",
      "mexico",
      "1953",
      "india and west pakistan",
      "only after agronomy practices are changed",
      "route and not a map"
    ],
    "prohibitedPatterns": [
      {
        "id": "modern-borders",
        "regex": "\\b(?:modern|current|present-day) (?:border|borders|map)\\b(?![^.!?]{0,40}\\bnot\\b)",
        "why": "The figure explicitly refuses to represent modern political borders as 1968 geography."
      },
      {
        "id": "hero-person",
        "regex": "\\b(?:borlaug|vogel|salmon|inazuka)\\b[^.!?]{0,24}\\b(?:alone|single-handedly|by himself)\\b",
        "why": "The route names institutions and public programmes as well as people, and refuses hero-person simplification."
      },
      {
        "id": "lives-in-the-route",
        "regex": "\\blives\\b",
        "why": "The route figure reports the movement of breeding material, not a humanitarian total."
      }
    ]
  },
  "productionPackage": {
    "id": "case10-package-v1.0",
    "selector": "[data-package-contract]",
    "roles": [
      "student",
      "accessible"
    ],
    "rule": "Six interacting contributors converging on one outcome, each printing its own connector word from the controlled set. The figure states in print that no contributor produced the result alone and that it claims no share or weighting.",
    "nodes": [
      {
        "id": "varieties",
        "label": "IMPROVED VARIETIES",
        "verb": "contributed to"
      },
      {
        "id": "fertiliser",
        "label": "FERTILISER",
        "verb": "worked with"
      },
      {
        "id": "water",
        "label": "IRRIGATION & WATER MANAGEMENT",
        "verb": "enabled"
      },
      {
        "id": "agronomy",
        "label": "AGRONOMY",
        "verb": "enabled"
      },
      {
        "id": "research",
        "label": "RESEARCH, SEED MULTIPLICATION, DISTRIBUTION & EXTENSION",
        "verb": "contributed to"
      },
      {
        "id": "policy",
        "label": "CREDIT, PRICING, INSTITUTIONS & POLICY",
        "verb": "worked with"
      }
    ],
    "outcome": "HIGHER REALISED WHEAT PRODUCTIVITY AND PRODUCTION",
    "allowedConnectorVerbs": [
      "contributed to",
      "enabled",
      "worked with"
    ],
    "prohibitedConnectorVerbs": [
      "caused entirely",
      "proved",
      "alone produced",
      "single-handedly produced"
    ],
    "requiredRule": "No contributor here produced the result alone",
    "requiresCaptionTerms": [
      "BASED ON",
      "BORLAUG NOBEL LECTURE 1970",
      "CIMMYT",
      "PINGALI 2012",
      "NO SHARE OR WEIGHTING IS CLAIMED"
    ],
    "requiresAltConcepts": [
      "improved varieties",
      "fertiliser",
      "irrigation and water management",
      "agronomy",
      "research, seed multiplication, distribution and extension",
      "credit, pricing, institutions and policy",
      "higher realised wheat productivity and production",
      "no contributor here produced the result alone",
      "a correct mechanism is not a measured share"
    ],
    "prohibitedPatterns": [
      {
        "id": "measured-share",
        "regex": "\\b\\d+\\s?(?:%|per cent|percent)\\b",
        "why": "No share of the gain is measured or claimed anywhere in this figure."
      },
      {
        "id": "sole-cause",
        "regex": "\\b(?:caused entirely|alone produced|single-handedly)\\b",
        "why": "The figure exists to refuse sole-cause language."
      }
    ]
  },
  "claimTest": {
    "id": "case10-claim-test-v1.0",
    "selector": "[data-claim-test]",
    "roles": [
      "student",
      "accessible"
    ],
    "rule": "Four tests the game's own evidence can run on the Failure Report. The task is confined to Sources A to D, and the report's paperwork is excluded as a test in both directions: an immaculate chain of custody does not prove a document genuine, and a flaw in it would not prove one forged.",
    "tests": [
      {
        "id": "trial-result",
        "label": "TRIAL RESULT",
        "checkedAgainst": "two-wheats"
      },
      {
        "id": "lineage-record",
        "label": "LINEAGE AND HARVEST RECORD",
        "checkedAgainst": "pedigree-records"
      },
      {
        "id": "field-outcome",
        "label": "FIELD OUTCOME",
        "checkedAgainst": "rao-testimony"
      },
      {
        "id": "corroboration",
        "label": "CORROBORATION",
        "checkedAgainst": "borlaug-record"
      }
    ],
    "printedRule": "Real letterhead, a reviewer's initials that trace to a real reviewer and an immaculate chain of custody are not proof that a report is genuine",
    "requiredPrintedText": [
      "TRIAL RESULT",
      "LINEAGE AND HARVEST RECORD",
      "FIELD OUTCOME",
      "CORROBORATION",
      "Sources A to D only",
      "Neither is one of the four tests"
    ],
    "insideGameOnly": true,
    "claimsSuppliedInBothEditions": true
  },
  "interpretations": {
    "id": "case10-interpretations-v1.0",
    "selector": "[data-interpretations]",
    "roles": [
      "student",
      "accessible"
    ],
    "rule": "Three positions on the same evidence, each with a supports column and an overreach column. This is historical claim and counterclaim reasoning, not a disguised multiple-choice item: every position, including the two that are wrong, has valid evidence the learner is required to find.",
    "positions": [
      {
        "id": "failed",
        "label": "A",
        "summary": "The wheat failed",
        "bestSupported": false
      },
      {
        "id": "wheat-alone",
        "label": "B",
        "summary": "The wheat alone explains it",
        "bestSupported": false
      },
      {
        "id": "system",
        "label": "C",
        "summary": "A large contribution inside a system",
        "bestSupported": true
      }
    ],
    "bestSupported": "system",
    "requiredPrintedText": [
      "Valid evidence that supports it",
      "Where it overreaches",
      "Best supported"
    ]
  },
  "sourceCertification": {
    "id": "case10-source-certification-v1.0",
    "rule": "Case-local certification, bounded to the claims each source actually supports. The Phase 1 Master Game Audit is not modified. The audit's certified pointer for this level, H15, is recorded as reused but is not relied on for any printed claim: every Nobel-derived claim in this package rests on the text of the 1970 lecture itself, which the PMO authorised as Source B of the locked estate. No historical claim outside these bounds appears in the package.",
    "pmoEstateMapping": [
      {
        "pmoSourceId": "A",
        "caseSourceId": "india-wheat-record",
        "printedLabel": "F"
      },
      {
        "pmoSourceId": "B",
        "caseSourceId": "borlaug-nobel-lecture",
        "printedLabel": "G"
      },
      {
        "pmoSourceId": "C",
        "caseSourceId": "cimmyt-history",
        "printedLabel": "H"
      },
      {
        "pmoSourceId": "D",
        "caseSourceId": "pingali-retrospective",
        "printedLabel": "I"
      }
    ],
    "auditReused": [
      {
        "auditId": "H15",
        "caseSourceId": "borlaug-nobel-lecture",
        "note": "The Phase 1 audit certified the Nobel Prize “Norman Borlaug — Facts” page for this level. No audit record is modified by this package. That page is not relied on for any printed claim: the PMO's locked estate names the 1970 Nobel Lecture itself, which was read in full for this candidate and is bounded claim by claim below."
      }
    ],
    "caseCertified": [
      {
        "caseSourceId": "india-wheat-record",
        "pmoSourceId": "A",
        "citation": "Government of India, official agricultural statistics for wheat, crop years 1964-65 to 1969-70: area sown, production, yield and irrigated share of the wheat area.",
        "supports": [
          "the annual area sown in million hectares for each of the six crop years: 13.42, 12.57, 12.84, 14.99, 15.96, 16.63",
          "the annual production in million tonnes for each of the six crop years: 12.26, 10.40, 11.39, 16.54, 18.65, 20.09",
          "the annual yield in kilograms per hectare for each of the six crop years: 913, 827, 887, 1,103, 1,169, 1,208",
          "the irrigated share of the wheat area for each of the six crop years: 36.8%, 43.1%, 48.0%, 43.4%, 49.8%, 51.1%",
          "that area, production and yield are three different measures of the same crop year",
          "that the irrigation share of the wheat area changed during the same period"
        ],
        "doesNotSupport": [
          "what fraction of the gains came from genetics or from any other single contributor",
          "how many lives were saved, fed or affected",
          "hunger reduction by itself",
          "welfare effects by itself",
          "any one-cause explanation of the Green Revolution",
          "any event, person, record or reading in the game's case"
        ]
      },
      {
        "caseSourceId": "borlaug-nobel-lecture",
        "pmoSourceId": "B",
        "citation": "Norman E. Borlaug, Nobel Lecture, “The Green Revolution, Peace, and Humanity”, delivered 11 December 1970 (Nobel Peace Prize 1970).",
        "sourceClass": "PRIMARY PARTICIPANT SOURCE",
        "supports": [
          "the Mexican wheat work, and Mexico's pre-programme national average wheat yield of 750 kilos per hectare",
          "that as fertiliser use raised yields to about four and a half thousand kilos per hectare, lodging, glossed in the lecture as “falling over of the plant”, began to limit further increases",
          "that a search was made for a source of genetic dwarfness and that “Norin 10, an extremely dwarf wheat from Japan, proved to be a suitable source”",
          "that crosses and re-crosses began in 1954 and that the dwarf Mexican wheats were first distributed in Mexico in 1961",
          "the four properties he names together in the varieties: high genetic yield potential, short straw, a strong and efficient response to heavy doses of fertilisers, and a broad spectrum of disease resistance",
          "that “this rapid increase in wheat production was not based solely on the use of Mexican dwarf varieties” but involved the transfer of a whole new production technology",
          "the crop-production campaign strategy resting on government economic policy assuring the farmer a fair price, the availability of the necessary inputs — seed, fertilizers, insecticides, weed killers and machinery — and the credit with which to buy them",
          "the seed movement: 350 tons to Pakistan and 250 tons to India in 1965 for wide-scale on-farm testing, 18,000 tons imported by India in 1966 and 42,000 tons by Pakistan a year later",
          "that “there are no miracles in agricultural production” and no miracle variety",
          "that the great increase in production had so far been in irrigated areas, and that not all cereal farmers even in irrigated areas had adopted or benefited from the new seed and technology",
          "that “the green revolution has won a temporary success in man's war against hunger and deprivation; it has given man a breathing space”",
          "that the original dwarf wheats imported from Mexico carried a wider spectrum of disease resistance than the local Indian types they replaced, and that resistance is a breeding objective distinct from short straw"
        ],
        "doesNotSupport": [
          "a neutral, omniscient or retrospective assessment: it is a participant's own account, delivered in 1970",
          "any measured share of the gains attributable to the varieties",
          "any count of lives saved, fed or rescued",
          "any national crop statistic outside what the lecture itself states",
          "any event, person, record or reading in the game's case",
          "every retrospective causal claim it makes, which it does not independently prove"
        ]
      },
      {
        "caseSourceId": "cimmyt-history",
        "pmoSourceId": "C",
        "citation": "CIMMYT (International Maize and Wheat Improvement Center), “From east Asia to south Asia, via Mexico: how one gene changed the course of history”, cimmyt.org.",
        "supports": [
          "that in 1935 Gonjoro Inazuka crossed a semi-dwarf Japanese wheat landrace with two American varieties, producing Norin 10",
          "that Norin 10 reduced wheat plant height from about 150 cm to 60-110 cm, through the reduced-height genes Rht1 and Rht2",
          "that S. D. Salmon of the USDA took samples of Norin 10 back to the United States, and that in the late 1940s Orville Vogel at Washington State University used them to produce semi-dwarf winter wheats, of which Gaines was the first",
          "that Borlaug's team in Mexico were working on lodging and rust resistance as two problems, that he wrote to Vogel for seed containing the Norin 10 dwarfing genes, that crossing began in 1953, that the first attempt failed, and that the result after crosses and re-crosses was a short, stiff-strawed spring wheat less likely to lodge",
          "that within seven years average wheat yields in Mexico had doubled, that Pitic 62 and Penjamo 62 were released by 1962, and that Sonora 64 and Lerma Rojo 64 followed and went to India and Pakistan",
          "that the Green Revolution was begun by combining three separate traits — semi-dwarf, rust resistant and photoperiod insensitive — and that one of the pictured parent crosses, Chapingo 53, was a tall variety resistant to stem rust",
          "that trials in India and Pakistan produced high yields “but only after agronomy practices were changed”, and that without those changes the Green Revolution would never have taken off",
          "that in 1967 Pakistan imported about 42,000 tons of semi-dwarf wheat seed from Mexico, Turkey 22,000 tons and India 18,000 tons"
        ],
        "doesNotSupport": [
          "that semi-dwarfing and rust resistance are the same trait, or that either produces the other",
          "the popular “saved hundreds of millions from starvation” framing in its own headline, which is not used or certified here",
          "any national harvest statistic",
          "any count of lives saved",
          "any event, person, record or reading in the game's case"
        ]
      },
      {
        "caseSourceId": "pingali-retrospective",
        "pmoSourceId": "D",
        "citation": "Prabhu L. Pingali, “Green Revolution: Impacts, limits, and the path ahead”, Proceedings of the National Academy of Sciences, 2012, 109(31):12302-12308, DOI 10.1073/pnas.0912953109.",
        "supports": [
          "that over about fifty years the production of cereal crops in the developing world tripled with only about a 30 per cent increase in land area cultivated, while populations had more than doubled",
          "that “much of the success was caused by the combination of high rates of investment in crop research, infrastructure, and market development and appropriate policy support”",
          "that between 1960 and 2000 yields for all developing countries rose 208 per cent for wheat",
          "that productivity gains from crop germplasm improvement alone are estimated to have averaged about 1.0 per cent per annum for wheat across all regions",
          "that fertiliser, irrigation and to a certain extent pesticides were critical components of the intervention, and that Asia had already invested significantly in irrigation infrastructure at the start of the period",
          "that adoption was uneven: modern varieties covered 82 per cent of the area planted in Asian countries and 27 per cent in Africa by 1998, that sub-Saharan Africa continues to be the exception to the global trend, and that women farmers and female-headed households gained proportionally less",
          "that calorie availability rose while dietary diversity decreased for many poor people and micronutrient malnutrition persisted",
          "that environmental impacts were mixed, with intensification sparing land from conversion alongside unintended consequences in water use, soil degradation and chemical runoff, which the article attributes to the policy environment that promoted over-use of inputs rather than to the technology itself",
          "the reported estimate that without the international and national crop germplasm improvement efforts, food production in developing countries would have been almost 20 per cent lower"
        ],
        "doesNotSupport": [
          "any count of lives saved, which the article does not supply",
          "any share of India's 1960s wheat rise attributable to the variety: the germplasm figure is an estimate across all developing countries and all wheat",
          "any claim beyond what the article states, its figures being estimates with stated methods",
          "any event, person, record or reading in the game's case"
        ]
      }
    ],
    "noFurtherClaims": "No historical, biographical, chronological, quantitative or institutional claim appears in this package that is not on one of the lists above. If a later revision needs one, that is a source-certification dependency for the PMO, not an authoring decision.",
    "openVarianceForPmo": "Two variances are recorded rather than resolved by the implementation. First, a currently published Government of India area table gives slightly different back-numbers for wheat area in these crop years than the PMO's locked series; the locked series is implemented exactly and the variance is reported to the PMO. Second, the Nobel lecture and CIMMYT date India's large seed purchase to 1966 and 1967 respectively; the packet prints the lecture's chronology and the Teacher Guide records the difference as a limitation."
  },
  "noGameRoute": {
    "rule": "Campaign 2 has no teacher level selector, no direct-launch mode, no injected state and no developer shortcut, and none will be built. Every assessed piece of evidence therefore exists in the learner packet, and the dossier is the stable assessment record in both routes.",
    "dossier": [
      "borlaug-record",
      "two-wheats",
      "pedigree-records",
      "rao-testimony",
      "failure-report"
    ],
    "requiredStrands": [
      {
        "id": "breeder-record",
        "source": "borlaug-record",
        "what": "reconstructed recovered record of the breeder and the Archive's annotation",
        "runtimeStatus": "required"
      },
      {
        "id": "lodging-evidence",
        "source": "two-wheats",
        "what": "reconstructed comparative trait evidence of lodging and standing",
        "runtimeStatus": "required"
      },
      {
        "id": "pedigree-provenance",
        "source": "pedigree-records",
        "what": "reconstructed pedigree and harvest cross-reference",
        "runtimeStatus": "required"
      },
      {
        "id": "field-yield-testimony",
        "source": "rao-testimony",
        "what": "reconstructed deployment testimony and field-yield claim",
        "runtimeStatus": "required"
      },
      {
        "id": "failure-report",
        "source": "failure-report",
        "what": "the reconstructed competing record the case exists to test",
        "runtimeStatus": "runtime-optional, curriculum-assessed"
      }
    ],
    "assessedStrandCount": 5,
    "requiredInRoles": [
      "student",
      "accessible"
    ],
    "gameRouteIsOptional": true,
    "optionalRuntimeSourceNotAssessed": {
      "id": "harvest-scale-survey",
      "what": "the level's optional survey of the harvest running to the horizon",
      "rule": "Deliberately not assessed and deliberately not reproduced. No task refers to it, no rubric criterion depends on it, and the Teacher Guide states that it is not assessed."
    },
    "optionalButAssessedRule": "The Failure Report is an optional insight source in normal gameplay, and a class can finish the level without seeing it. Because this curriculum assesses it, the packet reproduces it in full in both learner editions, and no learner's ability to complete Task 6 depends on discovering it during play.",
    "prohibited": [
      "reproducing runtime correct-answer flags",
      "reproducing runtime candidate-record labels or their hints",
      "reproducing the level's resolution text as learner evidence",
      "reproducing runtime clue identifiers, node identifiers or control labels",
      "reproducing any invented quotation the game attributes to Norman Borlaug, a real historical person",
      "requiring an unprinted line of gameplay for any assessed item"
    ],
    "teacherMustProvide": [
      "normal game route",
      "complete no-game route",
      "a mapping from each gameplay evidence object to its printed dossier card without ranking the routes",
      "an explicit statement that the optional horizon survey is not assessed"
    ]
  },
  "tasks": [
    {
      "id": "C10-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Case Vocabulary",
      "description": "Apply the nine terms the case cannot be performed without to the measures, objects and relationships they name.",
      "instructionalPurpose": "Establish only the nine terms the reasoning needs, with their definitions printed. The load-bearing term is yield, because Task 4 turns on its being a per-hectare measure rather than a total; baseline, denominator and causation are the terms the claim test and the finding are written in. No exact-match word bank is used and none is authorised: the definitions are on the page, so the activity is application rather than constrained recall.",
      "provenance": [
        "Curriculum-authored working definitions",
        "Terminology as used in the certified documented estate"
      ],
      "responseType": "seven applied term placements",
      "answerScope": "One term per statement, applied to a thing in this case, with the nine definitions printed above.",
      "pagePlacement": {
        "student": "student-billion-01",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-billion-02"
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
      "id": "C10-T2",
      "number": "2",
      "semanticLabel": "CLAIM TEST",
      "icon": "ph-diagnosis",
      "title": "Set the Claim Test",
      "description": "State what you would need before treating the claim that a billion lives were saved as a measured historical fact.",
      "instructionalPurpose": "Provisional thinking, taken after the reconstructed case records and deliberately before the documented sources arrive. It records what a learner already thinks a measurement requires. Because it is a starting point rather than a judgment, it is deliberately non-keyable, and the packet does not reveal a preferred answer anywhere near it.",
      "provenance": [
        "The reconstructed case records",
        "Curriculum-authored prompt"
      ],
      "responseType": "three short constructed responses",
      "answerScope": "Any honest and specific requirement, and any honest sign of estimation. There is no correct answer and none is keyed.",
      "pagePlacement": {
        "student": "student-billion-03",
        "teacher": "teacher-guide-03",
        "answer": null,
        "accessible": "accessible-billion-04"
      },
      "editions": [
        "student",
        "teacher",
        "accessible"
      ],
      "keyed": false,
      "nonKeyableReason": "The task asks what a learner would require before believing a claim, before the case has shown them what a stated method and counterfactual look like. Keying it would convert a record of provisional thinking into a hidden multiple-choice item and would penalise the very gap the sequence is built to expose. The Teacher Guide carries the guidance for reading it diagnostically."
    },
    {
      "id": "C10-T3",
      "number": "3",
      "semanticLabel": "EVIDENCE LAYERS",
      "icon": "ph-scales",
      "title": "Keep the Evidence Layers Separate",
      "description": "Say what reconstructed game evidence, documented sources and curriculum figures can each establish, and what each cannot.",
      "instructionalPurpose": "Not a classification drill: the three layers are named on the page, and what the learner produces is one can-establish and one cannot-establish relationship for each, plus the boundary stated in both directions. The boundary is the case's structural rule: a verdict on the Failure Report settles nothing historical, and a documented source settles nothing about the Failure Report.",
      "provenance": [
        "The printed source-status notice",
        "Every source card's own SOURCE STATUS line"
      ],
      "responseType": "six matrix cells and one boundary statement",
      "answerScope": "Any genuine capacity and any genuine limit for each layer, and a boundary sentence that runs in both directions.",
      "pagePlacement": {
        "student": "student-billion-05",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-billion-06"
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
      "id": "C10-T4",
      "number": "4",
      "semanticLabel": "QUANTITATIVE RECORD",
      "icon": "ph-ticket",
      "title": "Read the Numbers Carefully",
      "description": "Read the six-year India wheat record and separate production, yield, planted area and irrigation as four different measures.",
      "instructionalPurpose": "The major quantitative task and the load-bearing one. The learner reads four values off the record, shows the difference between a production figure and a yield figure using one crop year, names two other conditions that changed, and says why the record cannot apportion the rise. No arithmetic is required: the reasoning matters more than calculating a percentage, and no denominator, counterfactual or causal share is invented anywhere.",
      "provenance": [
        "Source F, the Government of India wheat record",
        "Figure 1, drawn from it"
      ],
      "responseType": "four compact reads and three short constructed responses",
      "answerScope": "Exact values as printed, and reasoning that keeps production, yield, area and irrigation distinct.",
      "pagePlacement": {
        "student": "student-billion-05",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-billion-07"
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
      "id": "C10-T5",
      "number": "5",
      "semanticLabel": "ROUTE AND PACKAGE",
      "icon": "ph-flow",
      "title": "Trace the Wheat and the Package",
      "description": "Trace the movement of the dwarfing trait between countries, and place the improved variety inside the wider production system.",
      "instructionalPurpose": "Two halves that must be taught together: the transmission of breeding knowledge and material, and the input package that made the varieties productive at scale. Varietal improvement mattered and is credited; it did not act alone, and the figure and the task both refuse hero-person simplification by naming farmers, breeders, agronomists, institutions and public policy where the sources support them.",
      "provenance": [
        "Source G, Borlaug's Nobel lecture",
        "Source H, CIMMYT",
        "Figures 2 and 3, drawn from them"
      ],
      "responseType": "four route stages, three contributor statements and one explanation",
      "answerScope": "Each route stage says what that place added; each contributor carries a function; the explanation uses the term input package.",
      "pagePlacement": {
        "student": "student-billion-06",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-billion-08"
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
      "id": "C10-T6",
      "number": "6",
      "semanticLabel": "TEST THE REPORT",
      "icon": "ph-wrench",
      "title": "Test the Failure Report",
      "description": "Test the game's Failure Report against the game's own evidence, on four things other than its paperwork.",
      "instructionalPurpose": "Entirely inside the reconstructed investigation. The report is an optional insight source in play, so the packet prints it in full and no learner needs to have found it. The trap is its provenance: the chain of custody is immaculate, and the packet refuses that reading in print in both directions. No documented source is used to prove the fictional report forged.",
      "provenance": [
        "Sources A to D, reconstructed",
        "Source E, the reconstructed report under test"
      ],
      "responseType": "four evidence cells, one verdict and one explanation",
      "answerScope": "Each cell pairs the report's printed claim with contrary evidence from Sources A to D; the verdict is an in-game verdict only.",
      "pagePlacement": {
        "student": "student-billion-07",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-billion-09"
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
      "id": "C10-T7",
      "number": "7",
      "semanticLabel": "COMPETING INTERPRETATIONS",
      "icon": "ph-nodes",
      "title": "Test the Competing Interpretations",
      "description": "Weigh three interpretations of the same evidence, naming the valid evidence and the overreach in each.",
      "instructionalPurpose": "Historical claim and counterclaim reasoning. Every position, including the two that are wrong, is required to have its valid evidence found, because naming the true part of a wrong claim is what makes the overreach visible. Interpretation C is the strongest supported, and its own risk — a qualification so heavy that it stops crediting the varieties — is named in the key.",
      "provenance": [
        "The whole printed estate",
        "Figures 1 to 3"
      ],
      "responseType": "six matrix cells, one bounded choice and one justification",
      "answerScope": "Any defensible valid-evidence entry from the printed estate; the overreach in B must name both the sole-cause error and the counted lives.",
      "pagePlacement": {
        "student": "student-billion-07",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-billion-09"
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
      "id": "C10-T8",
      "number": "8",
      "semanticLabel": "QUALIFIED FINDING",
      "icon": "ph-scales",
      "title": "Write a Qualified Historical Finding",
      "description": "Write a five-part historical finding with quantitative evidence, a second documented source, a causal qualification, a stated limitation and the next evidence needed.",
      "instructionalPurpose": "The culminating product, and deliberately not a canonical CER. Five obligations are visibly separate and separately scored: the finding, the quantitative evidence with units and scope, a second documented source, the causal qualification together with an explicit limitation, and the evidence that would be needed next. No exemplar states a number of lives saved as measured fact, and the key refuses any finding that does.",
      "provenance": [
        "The documented estate, Sources F to I",
        "Figures 1 to 3"
      ],
      "responseType": "six constructed responses under five numbered obligations",
      "answerScope": "A finding the evidence carries, one India value with units and scope, one further documented source, contributing conditions and one explicit limit, and a next-evidence claim.",
      "pagePlacement": {
        "student": "student-billion-08",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-04",
        "accessible": "accessible-billion-10"
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
  "timedRoute": {
    "id": "case10-core-route-v1.0",
    "assessedCoreMinutes": 60,
    "rule": "The assessed core route is sixty minutes of task time, at the minutes printed against each task in the Teacher procedure. Around it the packet needs about twenty minutes of launch, reading and close, which the procedure lists as unnumbered steps. The Teacher Guide states that gameplay is not inserted into the sixty minutes and that a class taking the game route should play in a separate period.",
    "taskMinutes": {
      "1": 5,
      "2": 4,
      "3": 5,
      "4": 10,
      "5": 8,
      "6": 8,
      "7": 8,
      "8": 12
    },
    "surroundingMinutes": {
      "launch": 3,
      "read-reconstructed": 8,
      "read-documented": 6,
      "close": 3
    }
  },
  "vocabulary": [
    "baseline",
    "causation",
    "denominator",
    "Green Revolution",
    "input package",
    "lodging",
    "pedigree",
    "semi-dwarf",
    "yield"
  ],
  "vocabularyBankDecision": "No exact-match word bank is used, and none is authorised by the design lock. The nine definitions are printed on the learner page as a glossary the learner keeps using all lesson, so Task 1 requires applying a term to a thing in this case rather than generating a term from memory. The EXACT_MATCH_WORD_BANKS amendment governs constrained fill-in-the-blank recall activities; this task is not one, and inventing a bank here would have added a decoy-free list beside a glossary that already prints the same words.",
  "caseSources": [
    {
      "id": "borlaug-record",
      "displayLabel": "A · The recovered Borlaug record",
      "evidenceLayer": "reconstructed",
      "contribution": "Inside the case: what the wheat was bred for, why a well-fed tall wheat lodges, that the short straw stood in the plots season after season, and the Archive's own filing claim about a billion lives.",
      "limitation": "Any fact about the real Norman Borlaug, any real trial result, and above all any count of lives. The filing claim is a claim, not a measurement.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3",
      "evidenceStrand": "breeder-record"
    },
    {
      "id": "two-wheats",
      "displayLabel": "B · The two wheats",
      "evidenceLayer": "reconstructed",
      "contribution": "Inside the case: the same heavy head standing on short stiff straw and flat on tall straw under an identical load, with the two traits named separately.",
      "limitation": "The condition of any real plot, any real stem measurement, and any claim that one of the two traits produces the other.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3",
      "evidenceStrand": "lodging-evidence"
    },
    {
      "id": "pedigree-records",
      "displayLabel": "C · The pedigree records",
      "evidenceLayer": "reconstructed",
      "contribution": "Inside the case: an unbroken dated lineage from the dwarf parent to distributed seed, and rising recorded yields across seasons in two regions.",
      "limitation": "What any real register or harvest book contains, and any real national harvest figure.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3",
      "evidenceStrand": "pedigree-provenance"
    },
    {
      "id": "rao-testimony",
      "displayLabel": "D · Dr. Rao, the deployment agronomist",
      "evidenceLayer": "reconstructed",
      "contribution": "Inside the case: a field account that the new wheat delivered and held through the season, and how the farmers were convinced.",
      "limitation": "Anything about a real agronomist, farm, farmer or harvest. His field-yield figure is invented and is not a measurement.",
      "fallbackCorrespondence": "Student page 3 · Accessible page 4",
      "evidenceStrand": "field-yield-testimony"
    },
    {
      "id": "failure-report",
      "displayLabel": "E · The Failure Report",
      "evidenceLayer": "reconstructed",
      "contribution": "The competing claim the case exists to test, its recommendation that the seed stock be destroyed, and the flawless paperwork that is not a test.",
      "limitation": "Anything about the real programme, and its own authenticity, which its provenance cannot settle in either direction.",
      "fallbackCorrespondence": "Student page 3 · Accessible page 4",
      "evidenceStrand": "failure-report"
    },
    {
      "id": "india-wheat-record",
      "displayLabel": "F · The India wheat record, 1964-65 to 1969-70",
      "evidenceLayer": "documented",
      "contribution": "Six crop years of area sown, production, yield and irrigated share, exactly as published, and the fact that these are four different measures.",
      "limitation": "Why anything changed. It attributes nothing to any cause, and reports nothing about hunger, welfare or lives.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 5"
    },
    {
      "id": "borlaug-nobel-lecture",
      "displayLabel": "G · Borlaug's Nobel lecture, 11 December 1970",
      "evidenceLayer": "documented",
      "contribution": "Lodging as the barrier, Norin 10 as the dwarfing source, the seed movement, the whole production technology, the price-input-credit strategy, and his own refusal of the miracle reading.",
      "limitation": "A neutral retrospective judgment, any measured share of the gains, and any count of lives. He is a participant with a case to make.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 5"
    },
    {
      "id": "cimmyt-history",
      "displayLabel": "H · CIMMYT on where the dwarfing came from",
      "evidenceLayer": "documented",
      "contribution": "Norin 10's origin and its reduced-height genes, the Salmon to Vogel to Borlaug transmission, the released varieties, and the three separate traits combined by breeding.",
      "limitation": "Anything about the game, any national harvest statistic, any count of lives, and any claim that dwarfing produces rust resistance.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 5"
    },
    {
      "id": "pingali-retrospective",
      "displayLabel": "I · A retrospective, forty years later",
      "evidenceLayer": "documented",
      "contribution": "The scale of the productivity change, the research-infrastructure-market-policy combination, unevenness by region and by gender, and nutritional and environmental limits.",
      "limitation": "Anything about the game, any count of lives, and any share of India's 1960s rise attributable to the variety.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 6"
    },
    {
      "id": "india-record-figure",
      "displayLabel": "Figure 1 · the India wheat record",
      "evidenceLayer": "curriculum-model",
      "contribution": "The six-year record arranged as two separate graphs on two separate scales, with the land-and-water strip beneath, so that four measures can be read together.",
      "limitation": "Nothing. A figure that organises evidence is not evidence, and this one prints the source it was drawn from.",
      "fallbackCorrespondence": "Student page 5 · Accessible page 7"
    },
    {
      "id": "route-figure",
      "displayLabel": "Figure 2 · the wheat crosses borders",
      "evidenceLayer": "curriculum-model",
      "contribution": "The documented transmission route in four stages, with each link labelled by who or what carried the material across it.",
      "limitation": "Nothing. It is a route and not a map, and it represents no political geography.",
      "fallbackCorrespondence": "Student page 6 · Accessible page 8"
    },
    {
      "id": "package-figure",
      "displayLabel": "Figure 3 · the production package",
      "evidenceLayer": "curriculum-model",
      "contribution": "Six contributors converging on one outcome, each with its own connector word from the controlled set.",
      "limitation": "Nothing, and in particular no share or weighting. A correct mechanism is not a measured share.",
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
    "culminationParityRule": "All five obligations of the Qualified Historical Finding are parity subparts in both editions. The Accessible edition changes the route — sentence openers, bullets accepted — and reduces nothing.",
    "subparts": [
      {
        "task": "C10-T1",
        "id": "vocabulary",
        "obligation": "Apply all seven terms.",
        "student": [
          "t1-term-1",
          "t1-term-2",
          "t1-term-3",
          "t1-term-4",
          "t1-term-5",
          "t1-term-6",
          "t1-term-7"
        ],
        "accessible": [
          "a1-term-1",
          "a1-term-2",
          "a1-term-3",
          "a1-term-4",
          "a1-term-5",
          "a1-term-6",
          "a1-term-7"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T2",
        "id": "claim-requirement-1",
        "obligation": "Name one thing required before the claim could be called measured.",
        "student": [
          "t2-need-1"
        ],
        "accessible": [
          "a2-need-1"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T2",
        "id": "claim-requirement-2",
        "obligation": "Name a second, different requirement.",
        "student": [
          "t2-need-2"
        ],
        "accessible": [
          "a2-need-2"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T2",
        "id": "estimation-sign",
        "obligation": "Name one missing element that would show the number was estimated.",
        "student": [
          "t2-missing"
        ],
        "accessible": [
          "a2-missing"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T3",
        "id": "layer-reconstructed",
        "obligation": "Say what reconstructed game evidence can and cannot establish.",
        "student": [
          "t3-r1-can",
          "t3-r1-cannot"
        ],
        "accessible": [
          "a3-r1-can",
          "a3-r1-cannot"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T3",
        "id": "layer-documented",
        "obligation": "Say what documented sources can and cannot establish.",
        "student": [
          "t3-r2-can",
          "t3-r2-cannot"
        ],
        "accessible": [
          "a3-r2-can",
          "a3-r2-cannot"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T3",
        "id": "layer-figure",
        "obligation": "Say what a curriculum-original figure can and cannot establish.",
        "student": [
          "t3-r3-can",
          "t3-r3-cannot"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t3-figure-row-modelled"
      },
      {
        "task": "C10-T3",
        "id": "layer-boundary",
        "obligation": "State the boundary between the two evidence layers in both directions.",
        "student": [
          "t3-boundary"
        ],
        "accessible": [
          "a3-boundary"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T4",
        "id": "read-lowest",
        "obligation": "Name the crop year with the lowest production.",
        "student": [
          "t4-low-year"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t4-first-read-modelled"
      },
      {
        "task": "C10-T4",
        "id": "read-jump",
        "obligation": "Name the crop year in which production rose most.",
        "student": [
          "t4-jump-year"
        ],
        "accessible": [
          "a4-jump-year"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T4",
        "id": "read-area",
        "obligation": "Say what the area sown did between 1966-67 and 1967-68.",
        "student": [
          "t4-area"
        ],
        "accessible": [
          "a4-area"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T4",
        "id": "read-irrigation",
        "obligation": "Say what the irrigated share did between 1966-67 and 1967-68.",
        "student": [
          "t4-irrigation"
        ],
        "accessible": [
          "a4-irrigation"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T4",
        "id": "two-measures",
        "obligation": "Show the difference between a production figure and a yield figure.",
        "student": [
          "t4-measures"
        ],
        "accessible": [
          "a4-measures"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T4",
        "id": "other-conditions",
        "obligation": "Name two conditions other than the variety that changed, with where each is visible.",
        "student": [
          "t4-conditions"
        ],
        "accessible": [
          "a4-conditions"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T4",
        "id": "no-apportionment",
        "obligation": "Say why the record cannot say how much of the rise the new wheat caused.",
        "student": [
          "t4-cause"
        ],
        "accessible": [
          "a4-cause"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T5",
        "id": "route-stages",
        "obligation": "Say what each stage of the route added.",
        "student": [
          "t5-route-japan",
          "t5-route-us",
          "t5-route-mexico",
          "t5-route-southasia"
        ],
        "accessible": [
          "a5-route-mexico"
        ],
        "differenceClass": "declared-reduction",
        "governedBy": "t5-route-mostly-supplied"
      },
      {
        "task": "C10-T5",
        "id": "package-contributors",
        "obligation": "Name three contributors other than the variety, with what each did.",
        "student": [
          "t5-part-1",
          "t5-part-2",
          "t5-part-3"
        ],
        "accessible": [
          "a5-part-1",
          "a5-part-2",
          "a5-part-3"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T5",
        "id": "seed-not-alone",
        "obligation": "Explain, using the term input package, why the seed alone is not the explanation.",
        "student": [
          "t5-why"
        ],
        "accessible": [
          "a5-why"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T6",
        "id": "test-trial-result",
        "obligation": "State what the game's evidence shows under the trial-result test.",
        "student": [
          "t6-r1-shows"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t6-modelled-comparison"
      },
      {
        "task": "C10-T6",
        "id": "test-lineage",
        "obligation": "State what the game's evidence shows under the lineage and harvest-record test.",
        "student": [
          "t6-r2-shows"
        ],
        "accessible": [
          "a6-r2-shows"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T6",
        "id": "test-field",
        "obligation": "State what the game's evidence shows under the field-outcome test.",
        "student": [
          "t6-r3-shows"
        ],
        "accessible": [
          "a6-r3-shows"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T6",
        "id": "test-corroboration",
        "obligation": "State what the game's evidence shows under the corroboration test.",
        "student": [
          "t6-r4-shows"
        ],
        "accessible": [
          "a6-r4-shows"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T6",
        "id": "verdict",
        "obligation": "Reach a verdict on the report inside the game.",
        "student": [
          "t6-verdict"
        ],
        "accessible": [
          "a6-verdict"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T6",
        "id": "paperwork",
        "obligation": "Say why the report's paperwork is not one of the tests.",
        "student": [
          "t6-paperwork"
        ],
        "accessible": [
          "a6-paperwork"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T7",
        "id": "position-failed",
        "obligation": "Weigh interpretation A: valid evidence and overreach.",
        "student": [
          "t7-a-supports",
          "t7-a-overreach"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t7-first-position-modelled"
      },
      {
        "task": "C10-T7",
        "id": "position-wheat-alone",
        "obligation": "Weigh interpretation B: valid evidence and overreach.",
        "student": [
          "t7-b-supports",
          "t7-b-overreach"
        ],
        "accessible": [
          "a7-b-supports",
          "a7-b-overreach"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T7",
        "id": "position-system",
        "obligation": "Weigh interpretation C: valid evidence and overreach.",
        "student": [
          "t7-c-supports",
          "t7-c-overreach"
        ],
        "accessible": [
          "a7-c-supports",
          "a7-c-overreach"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T7",
        "id": "best-supported",
        "obligation": "Choose the best-supported interpretation.",
        "student": [
          "t7-best"
        ],
        "accessible": [
          "a7-best"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T7",
        "id": "best-supported-why",
        "obligation": "Justify the choice, naming a source.",
        "student": [
          "t7-why"
        ],
        "accessible": [
          "a7-why"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T8",
        "id": "finding",
        "obligation": "State what the evidence supports about the part improved varieties played.",
        "student": [
          "t8-finding"
        ],
        "accessible": [
          "a8-finding"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T8",
        "id": "quantitative-evidence",
        "obligation": "Use one India value or trend with its units and scope.",
        "student": [
          "t8-quant"
        ],
        "accessible": [
          "a8-quant"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T8",
        "id": "second-source",
        "obligation": "Use one additional documented source and say what it adds.",
        "student": [
          "t8-second-source"
        ],
        "accessible": [
          "a8-second-source"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T8",
        "id": "causal-qualification",
        "obligation": "Identify other contributing conditions and why that matters.",
        "student": [
          "t8-qualification"
        ],
        "accessible": [
          "a8-qualification"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T8",
        "id": "limitation",
        "obligation": "State something the evidence does not prove.",
        "student": [
          "t8-limitation"
        ],
        "accessible": [
          "a8-limitation"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C10-T8",
        "id": "next-evidence",
        "obligation": "Identify the additional evidence that would be needed next.",
        "student": [
          "t8-next"
        ],
        "accessible": [
          "a8-next"
        ],
        "differenceClass": "parity"
      }
    ]
  },
  "accessibleAdaptations": [
    {
      "id": "t3-figure-row-modelled",
      "task": "C10-T3",
      "what": "The curriculum-original figure row of the three-layer table is supplied complete in both cells as a worked example.",
      "effect": "Accessible completes four matrix cells; Student completes six. The boundary sentence is answered independently in both.",
      "whyNotALeak": "The figure row is the one the source-status notice has already stated in full on page 1: a figure organises evidence and is not itself evidence. The two rows that carry the case — what reconstructed game evidence can do and what documented sources can do — are worked independently in both editions, as is the boundary sentence.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t4-first-read-modelled",
      "task": "C10-T4",
      "what": "The first of the four reads, the crop year with the lowest production, is supplied as a worked example, and each remaining prompt names the row or column it needs.",
      "effect": "Accessible completes three reads; Student completes four. All three written parts are independent in both.",
      "whyNotALeak": "The worked example models how to read a bar column and nothing more, and the value it gives is not used by any later part. The reasoning the task assesses — that production and yield are different measures, that other conditions changed, and that the record cannot apportion the rise — is answered independently in both editions, on identical data with identical units.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t5-route-mostly-supplied",
      "task": "C10-T5",
      "what": "Three of the four route stages — Japan, the United States, and India and West Pakistan — are supplied as GIVEN; Mexico is answered.",
      "effect": "Accessible completes one route stage; Student completes four. The three package contributors and the input-package explanation are independent in both.",
      "whyNotALeak": "The route stages are printed in full in Figure 2 in both editions, so supplying three of them removes transcription rather than reasoning. Mexico is the stage that is kept because it is where the trait was converted into a usable variety, and the reasoning the task assesses — that the variety worked inside a package — is carried by Parts B and C, which are identical obligations.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t6-modelled-comparison",
      "task": "C10-T6",
      "what": "One complete claim-versus-evidence comparison, the trial-result test, is modelled in full.",
      "effect": "Accessible completes three evidence cells; Student completes four. The verdict and the paperwork response are identical obligations in both.",
      "whyNotALeak": "The modelled row shows the move the task assesses — set the report's printed claim beside the game's own contrary evidence — on the one test whose evidence is a physical comparison the learner has already read twice. The three remaining tests, the verdict and the refusal of the paperwork as a test are answered independently in both editions.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t7-first-position-modelled",
      "task": "C10-T7",
      "what": "Interpretation A is worked in both its cells as a model of the move: valid evidence first, then overreach.",
      "effect": "Accessible completes four matrix cells; Student completes six. The choice and the justification are identical obligations in both.",
      "whyNotALeak": "Interpretation A is the one the learner has already refuted in Task 6, so modelling it shows the form of the answer without giving away either of the two interpretations the case turns on. Interpretations B and C — including the overreach that names both the sole-cause error and the counted lives — are worked independently in both editions.",
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
      "rule": "Every printable proposition in every role is scanned against the five closed negative classes. Internal punctuation is not a safety boundary.",
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
          "livesSavedAsMeasurement",
          "seedAloneCausation",
          "productionIsYield",
          "dwarfingCausesRust",
          "productionEndsHunger"
        ]
      },
      {
        "id": "answer-key-floor",
        "roles": [
          "answer"
        ],
        "purpose": "The Answer Key must be able to state the wording it refuses at every level.",
        "allowedConcepts": [
          "livesSavedAsMeasurement",
          "seedAloneCausation",
          "productionIsYield",
          "dwarfingCausesRust",
          "productionEndsHunger"
        ]
      },
      {
        "id": "answer-key-tested-claim",
        "roles": [
          "answer"
        ],
        "purpose": "The Answer Key must be able to name a competing interpretation in order to weigh and reject it.",
        "allowedConcepts": [
          "livesSavedAsMeasurement",
          "seedAloneCausation"
        ]
      }
    ],
    "structuralExemptSelectors": [
      {
        "selector": "[data-evidence-layer='reconstructed']",
        "allowedConcepts": [
          "livesSavedAsMeasurement",
          "seedAloneCausation"
        ],
        "why": "A reconstructed evidence object is the game layer. The Archive files the case under a claim about a billion lives, and the card has to print what the game says in order for the learner to test it; the card's own status line is what keeps it from being read as history. The layer is NOT excused from the production-versus-yield, trait-causation or production-ends-hunger classes, because the game asserts none of those and the packet must not introduce them anywhere."
      },
      {
        "selector": "[data-game-claim]",
        "allowedConcepts": [
          "livesSavedAsMeasurement",
          "seedAloneCausation"
        ],
        "why": "A marked in-game quotation inside a task that tests it. Quoting a claim in order to test it is not asserting it, and the marker is what makes the quotation legible as a quotation to the validator as well as to the learner."
      }
    ]
  },
  "figureContract": {
    "rule": "Three figures, all deterministic HTML and CSS with no generative art, each carrying a printed SOURCE STATUS line and a printed basis line, and each carrying accessibility text held to the same factual contracts as the visible drawing. No imagery of any kind is used anywhere in this package apart from the shared institutional insignia.",
    "figures": [
      {
        "id": "india-record",
        "selector": "[data-quant-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "H7 quantitative evidence, two aligned graphs on separate scales",
        "requiresPrintedText": [
          "PRODUCTION",
          "YIELD",
          "scale 0 to 22",
          "scale 0 to 1,300",
          "12.26",
          "10.40",
          "11.39",
          "16.54",
          "18.65",
          "20.09",
          "913",
          "827",
          "887",
          "1,103",
          "1,169",
          "1,208",
          "13.42",
          "12.57",
          "12.84",
          "14.99",
          "15.96",
          "16.63",
          "36.8%",
          "43.1%",
          "48.0%",
          "43.4%",
          "49.8%",
          "51.1%",
          "Area sown",
          "Irrigated share of the wheat area"
        ],
        "requiresCaptionTerms": [
          "BASED ON",
          "GOVERNMENT OF INDIA",
          "EXACT PUBLISHED VALUES",
          "TWO SEPARATE SCALES"
        ],
        "requiresAltConcepts": [
          "two separate bar graphs",
          "production",
          "million tonnes",
          "yield",
          "kilograms per hectare",
          "the two scales are different",
          "area sown",
          "irrigated share"
        ],
        "prohibitedPatterns": [
          {
            "id": "single-shared-axis",
            "regex": "\\b(?:shared|single|one) (?:axis|scale)\\b",
            "why": "The two measures are drawn on two separate scales and the figure must not claim otherwise."
          },
          {
            "id": "lives-in-the-figure",
            "regex": "\\blives\\b",
            "why": "The quantitative record reports crops, not lives, and its accessibility text may not introduce one."
          },
          {
            "id": "causal-attribution",
            "regex": "\\b(?:because of the (?:new )?(?:seed|variety)|caused by the (?:new )?(?:seed|variety))\\b",
            "why": "The record attributes nothing to any cause and its accessibility text may not do so either."
          }
        ]
      },
      {
        "id": "route",
        "selector": "[data-route-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "H3 sourced route",
        "requiresPrintedText": [
          "JAPAN",
          "UNITED STATES",
          "MEXICO",
          "INDIA & WEST PAKISTAN",
          "Norin 10",
          "Rht1",
          "Rht2",
          "Vogel",
          "Salmon",
          "Pitic 62",
          "Penjamo 62",
          "only after agronomy practices are changed"
        ],
        "requiresCaptionTerms": [
          "BASED ON",
          "CIMMYT",
          "BORLAUG NOBEL LECTURE 1970",
          "NOT A MAP TO SCALE"
        ],
        "requiresAltConcepts": [
          "japan",
          "1935",
          "norin 10",
          "united states",
          "vogel",
          "mexico",
          "1953",
          "india and west pakistan",
          "only after agronomy practices are changed",
          "route and not a map"
        ],
        "requiresRouteRule": "This is a route, not a map",
        "prohibitedPatterns": [
          {
            "id": "modern-borders",
            "regex": "\\b(?:modern|current|present-day) (?:border|borders|map)\\b(?![^.!?]{0,40}\\bnot\\b)",
            "why": "The figure explicitly refuses to represent modern political borders as 1968 geography."
          },
          {
            "id": "hero-person",
            "regex": "\\b(?:borlaug|vogel|salmon|inazuka)\\b[^.!?]{0,24}\\b(?:alone|single-handedly|by himself)\\b",
            "why": "The route names institutions and public programmes as well as people, and refuses hero-person simplification."
          },
          {
            "id": "lives-in-the-route",
            "regex": "\\blives\\b",
            "why": "The route figure reports the movement of breeding material, not a humanitarian total."
          }
        ]
      },
      {
        "id": "package",
        "selector": "[data-package-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "H1 contributing-system model",
        "requiresPrintedText": [
          "IMPROVED VARIETIES",
          "FERTILISER",
          "IRRIGATION & WATER MANAGEMENT",
          "AGRONOMY",
          "RESEARCH, SEED MULTIPLICATION, DISTRIBUTION & EXTENSION",
          "CREDIT, PRICING, INSTITUTIONS & POLICY",
          "HIGHER REALISED WHEAT PRODUCTIVITY AND PRODUCTION"
        ],
        "requiresCaptionTerms": [
          "BASED ON",
          "BORLAUG NOBEL LECTURE 1970",
          "CIMMYT",
          "PINGALI 2012",
          "NO SHARE OR WEIGHTING IS CLAIMED"
        ],
        "requiresAltConcepts": [
          "improved varieties",
          "fertiliser",
          "irrigation and water management",
          "agronomy",
          "research, seed multiplication, distribution and extension",
          "credit, pricing, institutions and policy",
          "higher realised wheat productivity and production",
          "no contributor here produced the result alone",
          "a correct mechanism is not a measured share"
        ],
        "requiresPackageRule": "No contributor here produced the result alone",
        "prohibitedPatterns": [
          {
            "id": "measured-share",
            "regex": "\\b\\d+\\s?(?:%|per cent|percent)\\b",
            "why": "No share of the gain is measured or claimed anywhere in this figure."
          },
          {
            "id": "sole-cause",
            "regex": "\\b(?:caused entirely|alone produced|single-handedly)\\b",
            "why": "The figure exists to refuse sole-cause language."
          }
        ]
      }
    ],
    "grayscaleRule": "Nothing in any figure is carried by colour alone. Every bar prints its own value, every route stage prints its place and its date, every package node prints its connector word, and the border weights that distinguish the yield bars, the final route stage and the outcome node are geometry."
  },
  "standards": {
    "directlyAssessed": [
      "C3 D2.His.14.6-8",
      "C3 D3.3.6-8",
      "C3 D3.4.6-8",
      "C3 D4.1.6-8",
      "CCSS RH.6-8.7",
      "CCSS WHST.6-8.1"
    ],
    "supporting": [
      "C3 D3.2.6-8",
      "CCSS RH.6-8.8"
    ],
    "contextual": [],
    "ngss": "No NGSS performance expectation is claimed at any status, and no contextual standard is claimed either. Plant breeding, lodging and disease resistance are the content the case uses; no task asks a learner to construct a scientific explanation, develop or use a model of a natural system, or analyse scientific data. The tasks measure multiple causation, source usefulness and limits, claim construction from quantitative evidence, and written argument.",
    "rationale": "Task-first alignment under the PMO partition, and deliberately short. D2.His.14 is measured by Task 5's multiple-cause explanation and Task 8's multi-causal finding; D3.3 by Task 3's can-establish and cannot-establish cells and by Task 6's in-game evidence test; D3.4 by Task 4's development of claims from the quantitative record and by Task 7's weighing of three interpretations against the same evidence; D4.1 by Task 8's written argument with an explicit qualification, a stated limitation and a next-evidence claim. RH.6-8.7 is measured by the integration of the three figures and the quantitative record with the written sources in Tasks 4, 5 and 8; WHST.6-8.1 by Task 8's argument with its required counter-consideration. D3.2 is supporting because Tasks 3, 6 and 7 evaluate each source's usefulness against the question being asked without performing a standalone source evaluation. RH.6-8.8 is supporting because Task 6 distinguishes a report's claims from the evidence behind them and Task 7 separates supported evidence from overreach, exercised on a bounded printed set rather than on continuous text. The contextual list is empty on purpose: the case makes no science-standard claim of any kind."
  }
};
