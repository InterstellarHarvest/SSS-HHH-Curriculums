window.HHH_CASE08_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C2-CASE08",
  "runtimeId": "C2L1",
  "instructionalType": "CORE_CASE",
  "title": "The Floating Gardens",
  "displayLabel": "8 - The Floating Gardens",
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
  "learningGoal": "Explain chinampas as an engineered wetland/raised-field agricultural system integrating canals, soil renewal, intensive cultivation and hydrologic management, while evaluating what each class of source can and cannot establish about it.",
  "guidingQuestion": "How did the chinampa system work as an engineered landscape, and what can each kind of source actually establish about it?",
  "culminatingProduct": "Engineered Landscape Explanation — a geographic and historical systems explanation with source qualification. The learner states accurately what a chinampa is, supplies two evidentiary links from different real-world sources or figures, connects the geographic setting to agricultural function, states one thing a named source cannot establish, and then explains in a short synthesis how field construction, canals, soil renewal, intensive cultivation and basin-scale water management work on one another. Canonical CER is deliberately not used; see cerDecision.",
  "cerDecision": {
    "id": "case08-cer-declined-v1.0",
    "decision": "DECLINED",
    "blueprintProduct": "geographic/historical systems explanation with source qualification (Blueprint, Core Case 08)",
    "rationale": "The Blueprint permits canonical CER only where its structure genuinely supports the case, and names a geographic and historical systems explanation with source qualification as this case's culminating product. A CER frame would force the learner to elect one claim and demote everything else to support, and this case assesses the opposite operation: an accurate definition, two independent sourced links, a relationship between a landscape and the farming it made possible, an explicit statement of what a named source cannot establish, and a synthesis in which no single part of the system is the claim because each part only works through the others. The Engineered Landscape Explanation keeps all six of those as separate, separately scored obligations.",
    "precedent": "HHH Campaign 1 Core Case 06 declined canonical CER for its systems and evidence-audit explanation on the same Blueprint ground, and Campaign 2 Core Case 07 followed it for its provenance and authenticity judgment. This case follows that established precedent rather than inventing a new one.",
    "enforcement": "No role renders the shared canonical CER component, and no role declares a CER contract.",
    "prohibitedSelectors": [
      "[data-cer-contract]",
      ".canonical-cer",
      ".cer-stack"
    ]
  },
  "sourceStatusContract": {
    "rule": "Every learner-facing evidence object declares its status in markup (data-evidence-layer) and in printed text (a SOURCE STATUS line), and no role converts reconstructed game evidence into a claim about 1487 or a real-world source into evidence that a game event happened.",
    "bands": [
      {
        "id": "reconstructed",
        "label": "RECONSTRUCTED GAME EVIDENCE",
        "attribute": "reconstructed",
        "statusMarker": "reconstructed game evidence",
        "covers": [
          "the farmer at the plots and everything she reports",
          "the plot-soil reading",
          "the survey of the lake works",
          "the harvest count and the method described for making it",
          "the buried collapse account",
          "every count, name, date and reading belonging to any of the above"
        ],
        "rule": "Evidence written for the game. It may be reasoned about, compared and tested inside the case. It may never be cited as a fact about 1487 or about anything else in the real world."
      },
      {
        "id": "documented",
        "label": "DOCUMENTED",
        "attribute": "documented",
        "statusMarker": "documented",
        "covers": [
          "the FAO documentation of the chinampa agricultural system",
          "the INAH reporting of chinampa archaeology in the Basin of Mexico",
          "the INAH record of pre-Hispanic hydraulic works in the basin"
        ],
        "rule": "Real published documentation, cited to a real institution. It establishes the system and its material history. It is never evidence that any event in the game happened."
      },
      {
        "id": "historical-map",
        "label": "HISTORICAL MAP",
        "attribute": "historical-map",
        "statusMarker": "historical map",
        "covers": [
          "the plan of Tenochtitlan published at Nuremberg in 1524 and held by the Library of Congress",
          "its provenance, publication date, orientation and the geography its catalogue record describes"
        ],
        "rule": "A real printed historical map. It establishes geographic relationships and its own provenance. It is not a survey, and it is not a picture of the city in 1487."
      },
      {
        "id": "curriculum-model",
        "label": "CURRICULUM-ORIGINAL SCHEMATIC",
        "attribute": "curriculum-model",
        "statusMarker": "curriculum-original schematic",
        "covers": [
          "the adapted lake-city plan figure",
          "the two-scale chinampa system figure"
        ],
        "rule": "Drawn for this packet. A figure that organises evidence is not itself evidence, and each figure prints its adaptation status, its source and the fact that it is not to scale."
      }
    ],
    "statusVocabulary": [
      "reconstructed game evidence",
      "documented",
      "historical map",
      "curriculum-original schematic"
    ],
    "layerAttribute": "data-evidence-layer",
    "layerValues": [
      "reconstructed",
      "documented",
      "historical-map",
      "curriculum-model"
    ],
    "noticeRequired": [
      "student",
      "accessible"
    ],
    "noticeSelector": "[data-source-status-notice]",
    "nonMergerRule": "Reconstructed game evidence can support reasoning inside the case. It cannot establish what happened in 1487. A real-world source can document the system. It cannot prove any event in the game. Both learner editions carry this rule on page 1.",
    "fictionalDataRule": "Every deterministic invented value sits inside a node carrying data-fictional-data, and every such node sits inside a reconstructed evidence object.",
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
      "ranksUp",
      "rankUpText",
      "chinampa_field",
      "lake_causeway",
      "codex_house",
      "gardens_thriving",
      "soil_alive",
      "salinity_engineered",
      "harvest_counted",
      "keeper_heard",
      "collapse_read",
      "surplus_seen"
    ],
    "prohibitedRuntimeIdentifierRule": "No printable page in any role may display a runtime implementation identifier. The list is identifier-shaped by construction so that it can never accidentally forbid ordinary English.",
    "enforcedRoles": [
      "student",
      "teacher",
      "answer",
      "accessible"
    ]
  },
  "terminologyQualification": {
    "id": "case08-terminology-v1.0",
    "findingId": "HHH-GAME-C2L1-001",
    "dependencyClass": "CURRICULUM_QUALIFICATION_REQUIRED",
    "dependencyStatus": "OPEN_AT_AUDITED_GAME_BASELINE",
    "auditedGameCommit": "9b8545ed6ecf98b337326390400076e36789e056",
    "gameNote": "This is a teacher-qualification dependency, not a blocking one. No game remediation is required for Case 08 and this package requests none: the runtime title stays as it is, and the curriculum carries the qualification the audit asked for. This package changes nothing in the shared remediation tracker.",
    "rule": "“Floating gardens” is the runtime title and a conventional English nickname. Chinampas are raised fields: ground built up in shallow water from lake sediment, branches and decaying vegetation, on a staked structure set into the lake bottom, with canals on either side. The nickname is taught as a name; the construction is taught as the thing.",
    "sourceWordingNote": "The certified FAO summary itself opens with the phrase “floating artificial islands”. The packet reports that wording rather than hiding it, and sets it beside the construction steps in the same document, which describe a staked structure filled with two layers of soil. Where a source's shorthand and a source's detail disagree, the detail is what it documents.",
    "overcorrectionNote": "The opposite error is refused as firmly. Nothing in this package says or implies that the lake system was perfect or incapable of environmental change. INAH records a severe flood in 1604 and four later rebuildings of the same causeway, and the packet prints that.",
    "printedRule": "The field is built up from the lake bottom",
    "requiredPrintedStatements": [
      "“Floating gardens” is a conventional nickname",
      "Chinampas are raised fields built up in shallow water from lake sediment, branches and decaying vegetation",
      "The plan was published in 1524 and depicts the city about 1520",
      "It is not a picture of the city in 1487",
      "reconstructed game evidence can support reasoning inside the case",
      "The field is built up from the lake bottom"
    ],
    "requiredPrintedStatementRoles": [
      "student",
      "accessible"
    ],
    "positiveRequirements": [
      {
        "id": "nickname-qualification-printed",
        "selector": "[data-terminology-rule='nickname']",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print the nickname qualification beside the documented construction steps."
      },
      {
        "id": "not-floating-rule-printed",
        "selector": "[data-terminology-rule='not-floating']",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print, inside the system figure, that the field is built up from the lake bottom."
      },
      {
        "id": "system-figure-present",
        "selector": "[data-system-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the two-scale system figure with the lake bottom drawn under the field."
      },
      {
        "id": "map-limit-printed",
        "selector": "[data-map-limit='not-1487']",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print the map's date, provenance and the statement that it is not a picture of 1487."
      },
      {
        "id": "two-layer-organiser-printed",
        "selector": "[data-layer-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the two-layer organiser that keeps the game layer and the documented layer apart."
      },
      {
        "id": "answer-key-floor-printed",
        "selector": "[data-answer-key-floor]",
        "roles": [
          "answer"
        ],
        "rule": "The Answer Key states the claims that are refused at every level."
      }
    ],
    "prohibitedFramings": {
      "rule": "Three CLOSED negative classes, each anchored to a named subject register and each requiring an affirmative, unnegated predicate. A proposition violates a class only when the class's subject is present in the same proposition and one of its patterns matches. This is a bounded guard against three known high-risk misconceptions. It is not, and does not claim to be, a general semantic detector: an unseen paraphrase can pass it, and manual cross-role review remains required.",
      "chinampasFloat": {
        "why": "Chinampas literally float, drift, or are free-floating rafts.",
        "subjectPatterns": [
          "\\b(?:chinampas?|raised fields?|floating gardens?|the (?:plots|gardens|fields))\\b"
        ],
        "patterns": [
          "\\b(?:chinampas?|raised fields?|the (?:plots|gardens|fields))\\b[^.!?]{0,50}\\b(?:are|were|is|was)\\b(?!\\s+(?:not|never))[^.!?]{0,40}\\b(?:free[- ]?floating|floating rafts?|rafts? that float|unanchored|untethered|not attached to the lake ?bed|not attached to the bottom)\\b",
          "\\b(?:chinampas?|raised fields?|the (?:plots|gardens|fields))\\b[^.!?]{0,40}(?<!not )(?<!never )\\b(?:float|floats|floated|drift|drifts|drifted)\\b[^.!?]{0,30}\\b(?:on|upon|across|around|over)\\b[^.!?]{0,25}\\b(?:the\\s+)?(?:lake|water|canals?|surface)\\b",
          "\\b(?:floating gardens?|chinampas?)\\b[^.!?]{0,50}\\b(?:really|actually|literally|genuinely|in fact)\\b[^.!?]{0,35}(?<!not )(?<!never )\\b(?:float|floated|floating|drift|drifted)\\b",
          "\\b(?:chinampas?|raised fields?)\\b[^.!?]{0,30}\\b(?:were|are|was|is)\\b(?!\\s+(?:not|never))\\s*(?:just |simply |basically |merely )?(?:a |an )?rafts?\\b"
        ]
      },
      "reconstructionAsPrimary": {
        "why": "Reconstructed game characters, readings or records are presented as surviving 1487 evidence.",
        "subjectPatterns": [
          "\\b(?:xochitl|the harvest count|the collapse account|the plot soil|the lake works|reconstructed game evidence|the game)\\b"
        ],
        "patterns": [
          "\\b(?:xochitl|the harvest count|the collapse account|the plot soil|the lake works|reconstructed game evidence)\\b[^.!?]{0,40}\\b(?:is|are|was|were)\\b(?!\\s+(?:not|never))[^.!?]{0,35}\\b(?:surviving|primary|original|authentic|genuine|actual)\\b[^.!?]{0,25}\\b(?:source|record|document|testimony|evidence|account)\\b",
          "\\b(?:xochitl|the harvest count|the collapse account|reconstructed game evidence)\\b[^.!?]{0,40}(?<!not )(?<!never )\\b(?:survives?|survived|has survived)\\b[^.!?]{0,30}\\b1487\\b",
          "\\bthe game\\b[^.!?]{0,40}\\b(?:shows?|showed|says?|said|tells? us)\\b(?!\\s+(?:nothing|us nothing))[^.!?]{0,45}\\b(?:so|therefore|which means)\\b[^.!?]{0,45}\\b(?:1487|history|really happened|it happened)\\b"
        ]
      },
      "mapAsExactSnapshot": {
        "why": "The 1524 published plan is described as an exact map, survey or snapshot of 1487.",
        "subjectPatterns": [
          "\\b(?:plan|map)\\b"
        ],
        "patterns": [
          "\\b(?:plan|map)\\b[^.!?]{0,45}\\b(?:is|shows?|depicts?|records?|gives?)\\b(?!\\s+(?:not|never|no\\b))[^.!?]{0,35}\\b(?:exact(?:ly)?|precise(?:ly)?|accurate(?:ly)?)\\b[^.!?]{0,35}\\b1487\\b",
          "\\b(?:plan|map)\\b[^.!?]{0,45}\\b(?:is|was)\\b(?!\\s+(?:not|never))[^.!?]{0,25}\\b1487\\b\\s*(?:aerial\\s+)?(?:snapshot|survey|photograph|map|picture)\\b",
          "\\b(?:plan|map)\\b[^.!?]{0,45}\\b(?:was|is)\\b(?!\\s+(?:not|never))[^.!?]{0,30}\\b(?:drawn|made|surveyed|produced|printed|published)\\b[^.!?]{0,20}\\bin 1487\\b",
          "\\b(?:plan|map)\\b[^.!?]{0,45}\\b(?:shows?|depicts?|records?)\\b(?!\\s+(?:not|never))[^.!?]{0,30}\\b(?:the city|the gardens|tenochtitlan|it)\\b[^.!?]{0,20}\\bin 1487\\b"
        ]
      }
    },
    "negativeControls": {
      "chinampasFloat": [
        "Chinampas were floating rafts.",
        "The chinampas floated on the lake.",
        "The gardens drifted across the water.",
        "Chinampas are free-floating islands.",
        "The floating gardens really floated.",
        "Chinampas were simply rafts."
      ],
      "reconstructionAsPrimary": [
        "The harvest count is a surviving primary source from 1487.",
        "Xochitl is an authentic historical record.",
        "The collapse account is an original document.",
        "The harvest count survives from 1487.",
        "The game shows the gardens working, so that is what 1487 was like."
      ],
      "mapAsExactSnapshot": [
        "The map shows the exact layout of the city in 1487.",
        "The 1524 plan is a 1487 aerial survey.",
        "The plan was drawn in 1487.",
        "This map is a precise record of the city in 1487.",
        "The 1524 map shows the city in 1487."
      ]
    },
    "positiveControls": [
      "“Floating gardens” is a conventional nickname.",
      "Chinampas are raised fields constructed in wetlands.",
      "The game reconstructs a plausible scene for investigation.",
      "The 1524 published map can provide geographic evidence while still having limits.",
      "Historical evidence supports chinampa agriculture without proving every detail of the game scene.",
      "Chinampas are raised fields built up in shallow water from lake sediment, branches and decaying vegetation.",
      "The FAO summary also describes the system as floating artificial islands.",
      "The field is built up from the lake bottom.",
      "The plan was published in 1524 and depicts the city about 1520.",
      "It is not a picture of the city in 1487.",
      "The harvest count is reconstructed game evidence.",
      "Chinampas are not floating rafts.",
      "The chinampas did not float on the lake.",
      "The plan is not a picture of 1487.",
      "Archaeology establishes that chinampas and canals were built and used.",
      "The lake system was managed rather than immune."
    ]
  },
  "systemModel": {
    "id": "case08-system-v1.0",
    "rule": "The two-scale figure is drawn only from claims the certified real-world estate supports. Every component at field scale comes from the FAO documentation; the dike at basin scale comes from the INAH record. The game's reconstructed east-and-west hydrology arrangement is NOT reproduced as documented history anywhere in this package.",
    "fieldScale": {
      "label": "PANEL A · FIELD SCALE",
      "components": [
        "CANAL",
        "CULTIVATED SURFACE",
        "ORGANIC-MATTER LAYER",
        "LAKE-SEDIMENT LAYER",
        "STAKED STRUCTURE",
        "LAKE BOTTOM"
      ],
      "stabilisingVegetation": {
        "component": "ahuejote willow along both edges",
        "certifiedBy": "fao-chinampas",
        "why": "Included because the certified source states it directly: the perimeter is staked out with cut branches and stakes of ahuejote, a native willow, and rows of ahuejote along the edges perform several functions in the system."
      },
      "canalDepth": "about 1.5 m",
      "renewalStatement": "Sediment and aquatic vegetation are lifted from the canal floor onto the plot."
    },
    "basinScale": {
      "label": "PANEL B · BASIN SCALE",
      "components": [
        "CHINAMPA ZONE",
        "OPEN LAKE",
        "DIKE",
        "THE REST OF THE LAKE"
      ],
      "restraint": "The basin panel names a built barrier and the waters it separates, and stops there. It assigns no compass direction to any part of the lake, states no salinity for any part of it, and draws no gate schedule, because the certified INAH record supports none of those."
    },
    "joiningStatement": "The canal in Panel A is one thread of the water in Panel B.",
    "notFloatingStatement": "The field is built up from the lake bottom. It does not float.",
    "requiredStatusTerms": [
      "CURRICULUM-ORIGINAL SCHEMATIC",
      "BASED ON",
      "RECONSTRUCTION",
      "NOT TO SCALE"
    ],
    "prohibitedClaims": [
      "the game's east-and-west lake arrangement stated as documented history",
      "any measurement readable from the figure",
      "any count of chinampas, canals, causeways or people"
    ]
  },
  "evidenceLayers": {
    "id": "case08-layers-v1.0",
    "selector": "[data-layer-contract]",
    "roles": [
      "student",
      "accessible"
    ],
    "rule": "Task 6 is drawn as two named bands that are answered separately. The learner may not use reconstructed evidence to settle a question about the real world, or a real-world source to settle a question about the game's case.",
    "bands": [
      {
        "id": "inside",
        "label": "INSIDE THE GAME",
        "sources": [
          "field-testimony",
          "plot-soil",
          "lake-works",
          "harvest-record",
          "collapse-account"
        ]
      },
      {
        "id": "outside",
        "label": "OUTSIDE THE GAME",
        "sources": [
          "loc-plan",
          "fao-chinampas",
          "inah-record"
        ]
      }
    ],
    "printedRule": "The two layers do not join.",
    "refusedMove": "The game says so, therefore history says so.",
    "separateResponsesRequired": true
  },
  "sourceCertification": {
    "id": "case08-source-certification-v1.0",
    "rule": "Case-local certification, bounded to the claims each source actually supports. The Phase 1 Master Game Audit is not modified: source H12 is reused as the audit certified it, and the three sources added here carry case-local identifiers and case-local bounds. No claim outside these bounds appears in the package.",
    "auditReused": [
      {
        "auditId": "H12",
        "caseSourceId": "fao-chinampas",
        "note": "Reused exactly as the Phase 1 audit certified it. No audit record is modified by this package."
      }
    ],
    "caseCertified": [
      {
        "caseSourceId": "fao-chinampas",
        "auditId": "H12",
        "citation": "Food and Agriculture Organization of the United Nations, Globally Important Agricultural Heritage Systems, “Chinampas Agricultural System in Mexico City, Mexico”, fao.org/giahs/giahs-around-the-world/mexico-chinampas-agricultural-system/en",
        "supports": [
          "chinampas as a kind of wetland raised-field agriculture, in small islands in strips",
          "construction from sediments of the lake bottom, branches and decaying vegetation",
          "the construction sequence: staking the perimeter with ahuejote branches and stakes, building a structure around the stakes, then filling with two layers of soil, one of organic matter and one of sludge",
          "rows of ahuejote, a native willow, performing several functions in the system",
          "a web of channels forming part of the irrigation system, averaging about 1.5 m deep",
          "channels between 4 and 6 m average width used for transport by canoe",
          "channels carrying away excess rainy-season water and working as vessels of regulation",
          "soil fertility secured by constant organic-matter inputs, in particular aquatic vegetation",
          "an intensive farming method enabling cultivation throughout the year, with high productivity",
          "continuity of the system today in the lake area of Xochimilco",
          "designation as a Globally Important Agricultural Heritage System in 2017",
          "that the same summary also uses the conventional phrase “floating artificial islands”"
        ],
        "doesNotSupport": [
          "any statement about a particular year, and in particular about 1487",
          "any event, person or record in the game's case",
          "any archaeological date",
          "any claim that the fields floated, which the same document's construction steps contradict"
        ]
      },
      {
        "caseSourceId": "inah-record",
        "strand": "archaeology",
        "citation": "Instituto Nacional de Antropología e Historia, bulletin of 9 January 2024, “El sistema chinampero de la Cuenca de México, en la nueva edición de Arqueología Mexicana”, on Arqueología Mexicana no. 184, “Las chinampas de la Cuenca de México”, inah.gob.mx",
        "supports": [
          "chinampas as a practice much older than the Mexica period",
          "the earliest chinampas located in the Basin of Mexico belonging to the Early Postclassic, 900 to 1200 CE, at Xaltocan",
          "adoption of the practice by peoples settled around the basin's lakes",
          "continuity of the practice today in Tláhuac and Xochimilco",
          "an INAH salvage excavation of 2015 in the Cuauhtémoc borough identifying remains of chinampas and canals in use between 1300 and 1521 CE",
          "the association of those remains with a Mexica district of ancient México-Tenochtitlan",
          "crops recorded from archaeobotanical and sediment study of such contexts: maize, squash, chia, chile, amaranth, purslane, tomatillo and nopal"
        ],
        "doesNotSupport": [
          "any testimony, dialogue or named individual",
          "the date of any particular plot",
          "any event in the game's case",
          "any yield, area or population figure"
        ]
      },
      {
        "caseSourceId": "inah-record",
        "strand": "hydraulic works",
        "citation": "Instituto Nacional de Antropología e Historia, “El Albarradón de San Cristóbal”, Zona de Monumentos Históricos, Ecatepec, Estado de México, lugares.inah.gob.mx",
        "supports": [
          "pre-Hispanic hydraulic infrastructure in the Basin of Mexico",
          "a dike built as part of the works against flooding at Tenochtitlan, to separate the waters within Lake Texcoco and reduce the chance of the city flooding",
          "attribution of the work to a joint effort of the Mexica ruler Moctezuma Ilhuicamina and Nezahualcóyotl of Texcoco",
          "destruction of the causeway on Cortés's orders",
          "reconstruction after a severe flood in 1604, and renewal, rebuilding, restoration and reinforcement in 1675, 1692, 1743 and 1856"
        ],
        "doesNotSupport": [
          "which part of the lake held which water at any particular date",
          "the game's reconstructed east-and-west hydrology arrangement, which this source is expressly NOT used to certify",
          "any salinity measurement",
          "a date for any part of the pre-Hispanic work",
          "that the structure standing today is a preserved pre-Hispanic one; it is much rebuilt"
        ]
      },
      {
        "caseSourceId": "loc-plan",
        "citation": "Library of Congress, “Second Letter of Hernán Cortés”, Nuremberg: F. Peypus, 1524; translated into Latin by Petrus Savorgnanus; digitised copy from the Edward E. Ayer collection, The Newberry Library; loc.gov/item/2021667098",
        "supports": [
          "publication at Nuremberg by F. Peypus in 1524, in the first Latin edition of Cortés's second letter",
          "that the printing contains the first published plan of Tenochtitlan, labelled Temixtitan on the map",
          "that Cortés's letter is dated 30 October 1520 and the plan depicts the city in that year",
          "that Tenochtitlan was founded in the fourteenth century on an island in the salt lake of Texcoco",
          "that wide causeways connect the island city to the shores of the lake",
          "that the plan is oriented with west at the top",
          "that Cortés and his army attacked and destroyed the city in May 1521"
        ],
        "doesNotSupport": [
          "the city or its farmland in 1487",
          "any count, direction or length of causeways",
          "any agricultural detail",
          "any claim that the plan is a survey, an aerial view or a measured map"
        ],
        "rights": "The Library of Congress states that it is unaware of any copyright or other restrictions in this collection. No image from the item is reproduced in this package; the Task 3 figure is a curriculum redrawing of the relationships the Library's own catalogue record describes, and it is labelled ADAPTED FROM and RECONSTRUCTION accordingly."
      }
    ],
    "noFurtherClaims": "No historical, agricultural, hydrological, chronological, quantitative or archaeological claim appears in this package that is not on one of the lists above. If a later revision needs one, that is a source-certification dependency for the PMO, not an authoring decision."
  },
  "noGameRoute": {
    "rule": "Campaign 2 has no teacher level selector, no direct-launch mode, no injected state and no developer shortcut, and none will be built. Every assessed piece of evidence therefore exists in the learner packet, and the dossier is the stable assessment record in both routes.",
    "dossier": [
      "field-testimony",
      "plot-soil",
      "lake-works",
      "harvest-record",
      "collapse-account"
    ],
    "requiredStrands": [
      {
        "id": "cultivation",
        "source": "field-testimony",
        "what": "reconstructed farmer and cultivation evidence"
      },
      {
        "id": "soil",
        "source": "plot-soil",
        "what": "reconstructed soil evidence"
      },
      {
        "id": "waterworks",
        "source": "lake-works",
        "what": "reconstructed waterworks evidence"
      },
      {
        "id": "harvest-record",
        "source": "harvest-record",
        "what": "reconstructed harvest-record evidence"
      }
    ],
    "additionalIncluded": [
      {
        "id": "collapse-account",
        "why": "Included because Task 6 tests it by name. It is the claim the case exists to examine, and the task cannot be worked without it."
      }
    ],
    "requiredInRoles": [
      "student",
      "accessible"
    ],
    "gameRouteIsOptional": true,
    "prohibited": [
      "reproducing runtime correct-answer flags",
      "reproducing runtime candidate-record labels or their hints",
      "reproducing the level's resolution text as learner evidence",
      "reproducing runtime clue identifiers, node identifiers or control labels",
      "requiring an unprinted line of gameplay for any assessed item"
    ],
    "teacherMustProvide": [
      "normal game route",
      "complete no-game route"
    ]
  },
  "tasks": [
    {
      "id": "C08-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Case Vocabulary",
      "description": "Apply the six terms the case cannot be performed without to the things and relationships they name.",
      "instructionalPurpose": "Establish only the six terms the reasoning needs. The load-bearing pair is raised field and chinampa: the first is the general kind and the second is the particular case of it built in this basin. A learner who holds them as synonyms cannot answer Task 8, which is about a raised-field system somewhere else.",
      "provenance": [
        "Curriculum-authored working definitions",
        "Terminology as used in the certified real-world estate"
      ],
      "responseType": "six exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared six-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-gardens-01",
        "teacher": "teacher-guide-02",
        "answer": "answer-key-01",
        "accessible": "accessible-gardens-02"
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
      "id": "C08-T2",
      "number": "2",
      "semanticLabel": "GEOGRAPHIC TEST",
      "icon": "ph-diagnosis",
      "title": "Set a Geographic Test",
      "description": "Name one kind of water evidence and one kind of soil or land evidence you would look for to judge whether the lake-farming system was working.",
      "instructionalPurpose": "Provisional thinking, taken after the reconstructed case records and deliberately before the sources that explain the system arrive. It records where a learner starts. Because it is a starting point rather than a judgment, it is deliberately non-keyable.",
      "provenance": [
        "The reconstructed case records",
        "Curriculum-authored prompt"
      ],
      "responseType": "two short constructed responses",
      "answerScope": "Any honest and specific kind of evidence, one about water and one about soil or land. There is no correct answer and none is keyed.",
      "pagePlacement": {
        "student": "student-gardens-03",
        "teacher": "teacher-guide-03",
        "answer": null,
        "accessible": "accessible-gardens-05"
      },
      "editions": [
        "student",
        "teacher",
        "accessible"
      ],
      "keyed": false,
      "nonKeyableReason": "The task asks what a learner would look for before the case has shown them how the system works. Keying it would convert a record of provisional thinking into a hidden multiple-choice item and would penalise the very gap the sequence is built to expose. The Teacher Guide carries the guidance for reading it diagnostically."
    },
    {
      "id": "C08-T3",
      "number": "3",
      "semanticLabel": "SOURCED MAP",
      "icon": "ph-map",
      "title": "Read the Lake-City Map",
      "description": "Read a sourced historical map for the relationship between the city, the lake and the land, use it as geographic evidence, and state one limitation of it.",
      "instructionalPurpose": "The H3 operation, performed on a real published map rather than an invented locator. The learner extracts the island-lake-causeway relationship, uses it as evidence for why farming here took the form it did, and then says what the map cannot carry. Part D is the load-bearing part: a map published in 1524 depicting about 1520 is not evidence about 1487, and the packet says so in print before the task asks.",
      "provenance": [
        "The Library of Congress record of the 1524 published plan",
        "Curriculum-original adaptation of that plan"
      ],
      "responseType": "three short constructed responses and one medium constructed response",
      "answerScope": "The setting, the connection to land, one geographic reason drawn from the map and one other source, and one genuine limitation.",
      "pagePlacement": {
        "student": "student-gardens-05",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-gardens-07"
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
      "id": "C08-T4",
      "number": "4",
      "semanticLabel": "SYSTEM AT TWO SCALES",
      "icon": "ph-flow",
      "title": "Trace the Chinampa System at Two Scales",
      "description": "Explain how field construction, canals, soil renewal and basin-scale water management work on one another, at the scale of one field and at the scale of the lake.",
      "instructionalPurpose": "The H8 operation and the load-bearing task of the case. The figure draws the lake bottom under the field and the canals on either side of it, so that the misconception the runtime title invites cannot survive Part A. The four parts ask for relationships rather than labels, and Part D is where the two scales are joined.",
      "provenance": [
        "The certified FAO documentation of the system",
        "The certified INAH record of the basin's hydraulic works",
        "Curriculum-original schematic"
      ],
      "responseType": "four short constructed responses",
      "answerScope": "Construction and what holds the field in place; more than one function of the canals; soil renewal and repeated cropping; the basin scale reaching the plot.",
      "pagePlacement": {
        "student": "student-gardens-06",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-gardens-08"
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
      "id": "C08-T5",
      "number": "5",
      "semanticLabel": "SOURCE COMPARISON",
      "icon": "ph-scales",
      "title": "Compare What the Sources Can Establish",
      "description": "For each of four kinds of source, state what it contributes and what it cannot establish alone.",
      "instructionalPurpose": "The H4 operation, and the place the central source-status distinction becomes explicit. The four classes are deliberately not equivalent: a reconstruction can support reasoning inside the game and prove nothing outside it; current documentation can establish the system and its continuity but no event; archaeology can establish material presence and use but supply no words; a historical map can establish geographic relationships but is not a survey of the year in question.",
      "provenance": [
        "All five reconstructed case records",
        "The three certified real-world sources"
      ],
      "responseType": "eight matrix fields",
      "answerScope": "A genuine contribution and a genuine limit for each of the four source classes.",
      "pagePlacement": {
        "student": "student-gardens-07",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-gardens-09"
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
      "id": "C08-T6",
      "number": "6",
      "semanticLabel": "TWO EVIDENCE LAYERS",
      "icon": "ph-nodes",
      "title": "Test the Buried Collapse Claim",
      "description": "Test the reconstructed collapse account inside the game, and state separately what the real-world sources do and do not establish.",
      "instructionalPurpose": "The structural refusal of the merger. Two named bands, answered separately, so that a learner cannot reach an inside-the-game verdict by borrowing a real source, or a real-world conclusion by borrowing an invented record. The outside band is also where the overcorrection is refused: the real sources do not establish that the basin's water was ever free of trouble.",
      "provenance": [
        "The five reconstructed case records",
        "The three certified real-world sources"
      ],
      "responseType": "two constructed responses, one per evidence layer",
      "answerScope": "One layer answered from Sources A to E only, and one from Sources F to H only.",
      "pagePlacement": {
        "student": "student-gardens-07",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-gardens-09"
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
      "id": "C08-T7",
      "number": "7",
      "semanticLabel": "LANDSCAPE EXPLANATION",
      "icon": "ph-wrench",
      "title": "Explain the Engineered Landscape",
      "description": "Write an Engineered Landscape Explanation with an accurate definition, two links from different real-world sources, a geographic connection, one source qualification and a synthesis of the whole system.",
      "instructionalPurpose": "The culminating historical and geographic reasoning product, and a systems explanation with source qualification rather than a canonical CER. Six parts, each separately scored, so that neither the definition nor the qualification can be lost inside a confident paragraph. Part E is the structural obligation the Blueprint names: the learner must state something a named source cannot establish.",
      "provenance": [
        "The three certified real-world sources",
        "Both curriculum figures"
      ],
      "responseType": "five short constructed responses and one medium synthesis",
      "answerScope": "An accurate chinampa definition, two evidentiary links from different real-world sources or figures, a geographic connection, one explicit source qualification, and a synthesis of how the parts work together.",
      "pagePlacement": {
        "student": "student-gardens-08",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-gardens-10"
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
      "id": "C08-T8",
      "number": "8",
      "semanticLabel": "TRANSFER EXIT",
      "icon": "ph-ticket",
      "title": "Transfer the Method",
      "description": "For an unfamiliar reconstructed report about another wetland system, name one physical-landscape check and one source or provenance check you would make before accepting it.",
      "instructionalPurpose": "Transfer, and deliberately about somewhere the packet never mentions. The unfamiliar report repeats both traps at once: it calls the fields floating gardens and it blames salinity. A learner who retells Tenochtitlan has visibly failed to transfer, and the prompt says so before they start.",
      "provenance": [
        "Curriculum-authored transfer scenario",
        "The method established across Tasks 3 to 7"
      ],
      "responseType": "two short judgments and one constructed explanation",
      "answerScope": "One check that would be made in the landscape and one that would be made on the source, each justified by method rather than by this case.",
      "pagePlacement": {
        "student": "student-gardens-08",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-04",
        "accessible": "accessible-gardens-10"
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
    "canal",
    "chinampa",
    "dike",
    "intensive agriculture",
    "raised field",
    "salinity"
  ],
  "caseSources": [
    {
      "id": "field-testimony",
      "displayLabel": "A · The farmer at the plots",
      "creator": "Xochitl, a farmer at the chinampa plots (written for the game)",
      "period": "1487 (reconstructed)",
      "sourceType": "in-world testimony",
      "sourceOrigin": "reconstructed game testimony",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "cultivation",
      "contribution": "Establishes, inside the case, that the plots yield several harvests a year and are never rested, that maize, beans, squash and amaranth follow one another on the same ground, that new mud is lifted from the canal floor onto the plot each season, and that the plot is older than living memory.",
      "limitation": "Cannot establish anything about a real plot, a real yield or a real year. It is a character's account written for the game, and it is not testimony that survives from 1487.",
      "gameCorrespondence": "Campaign 2, Level 1 — the farmer's account taken at the chinampa plots.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3"
    },
    {
      "id": "plot-soil",
      "displayLabel": "B · The plot soil",
      "creator": "Field survey of the plot soil (written for the game)",
      "period": "1487 (reconstructed)",
      "sourceType": "in-world examination",
      "sourceOrigin": "reconstructed game examination",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "soil",
      "contribution": "Establishes, inside the case, that the plot soil is layered lake mud and decaying green matter, that its nutrient cycle is active and continuously replenished, and that no salt crust is present.",
      "limitation": "Cannot establish any real measurement of any real soil. The reading was invented with the case, and it describes one reconstructed plot.",
      "gameCorrespondence": "Campaign 2, Level 1 — the examination of the plot soil.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3"
    },
    {
      "id": "lake-works",
      "displayLabel": "C · The lake works",
      "creator": "Survey of the lake works from the causeway (written for the game)",
      "period": "1487 (reconstructed)",
      "sourceType": "in-world examination",
      "sourceOrigin": "reconstructed game examination",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "waterworks",
      "contribution": "Establishes, inside the case, that the lake is managed rather than simply present: an earthwork crosses the open water, it is pierced by gates, a crew works them, and the water on the garden side is held apart from the brackish water beyond.",
      "limitation": "Cannot establish the layout of the real basin, or which real water lay on which side of any real barrier. The certified INAH record describes a dike separating the waters of Lake Texcoco and does not say which part held which; this package does not either.",
      "gameCorrespondence": "Campaign 2, Level 1 — the survey of the lake works from the causeway.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3"
    },
    {
      "id": "harvest-record",
      "displayLabel": "D · The harvest count",
      "creator": "The painted harvest ledger and the method described for making it (written for the game)",
      "period": "1487 (reconstructed)",
      "sourceType": "in-world record",
      "sourceOrigin": "reconstructed game record",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "harvest-record",
      "contribution": "Establishes, inside the case, a painted screenfold of named plots and counted seasons running generations deep with yields steady to rising, and a method that required three independent counts to agree before anything was painted.",
      "limitation": "Cannot establish that any such record survives, or what a surviving one would say. It is not a surviving primary source and the packet never presents it as one.",
      "gameCorrespondence": "Campaign 2, Level 1 — the harvest record read in the record house.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 4"
    },
    {
      "id": "collapse-account",
      "displayLabel": "E · The buried collapse account",
      "creator": "The buried account (written for the game)",
      "period": "1487 (reconstructed)",
      "sourceType": "in-world record",
      "sourceOrigin": "reconstructed game record",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "contested-claim",
      "contribution": "Supplies the claim the case exists to test — salt in the plots, fouled canals, a valley exhausted — together with the one thing visible in the document itself: it names no plot, no season and no keeper, while every other record in the case names its plots.",
      "limitation": "Cannot establish anything about the real basin. It is an invented claim, and everything inside the game that could test it is invented too.",
      "gameCorrespondence": "Campaign 2, Level 1 — the buried account read in the record house.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 4"
    },
    {
      "id": "loc-plan",
      "displayLabel": "F · The 1524 published plan of the lake city",
      "creator": "Library of Congress, “Second Letter of Hernán Cortés”, Nuremberg: F. Peypus, 1524; digitised copy from the Edward E. Ayer collection, The Newberry Library; loc.gov/item/2021667098",
      "period": "published 1524; the plan depicts the city in 1520",
      "sourceType": "printed historical map in a published letter",
      "sourceOrigin": "real historical map",
      "evidentiaryStatus": "historical map",
      "evidenceLayer": "historical-map",
      "contribution": "The first published plan of Tenochtitlan, with its own provenance, date and orientation, and the geography its catalogue record describes: a city founded in the fourteenth century on an island in the salt lake of Texcoco, with wide causeways connecting the island city to the shores.",
      "limitation": "Cannot establish the city or its farmland in 1487. It was published in 1524, depicts the city about 1520, is oriented with west at the top, and was printed in Europe in a book by the commander whose army attacked and destroyed the city in 1521. It is not a survey and carries no agricultural detail.",
      "gameCorrespondence": "No runtime counterpart. The game supplies no map.",
      "fallbackCorrespondence": "Student page 3 · Accessible page 5",
      "rights": "The Library of Congress states it is unaware of any copyright or other restrictions in this collection. Cited and paraphrased; no image is reproduced in this package."
    },
    {
      "id": "fao-chinampas",
      "displayLabel": "G · How the system is built and worked",
      "creator": "Food and Agriculture Organization of the United Nations, Globally Important Agricultural Heritage Systems, “Chinampas Agricultural System in Mexico City, Mexico”, fao.org/giahs",
      "period": "current documentation; designated 2017",
      "sourceType": "intergovernmental heritage-system documentation",
      "sourceOrigin": "real modern institutional documentation",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "documented",
      "contribution": "The physical system: wetland raised fields built from lake-bottom sediment, branches and decaying vegetation; the staking, structure and two soil layers; the ahuejote willow; the channel network, its average 1.5 m depth and 4 to 6 m working width; organic-matter renewal from aquatic vegetation; intensive year-round cultivation; the channels as flood regulation; and present continuity in the lake area of Xochimilco.",
      "limitation": "Establishes nothing about any particular year and nothing whatever about the game's case. It also opens with the conventional phrase “floating artificial islands”, which its own construction steps correct; the packet prints both and teaches the construction.",
      "gameCorrespondence": "No runtime counterpart. The level narrates canal mud and continuous cropping; this source is where the documented system comes from.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 6",
      "rights": "FAO web resource. Cited and summarised, not reproduced."
    },
    {
      "id": "inah-record",
      "displayLabel": "H · What has been dug up, and what was built to hold the water",
      "creator": "Instituto Nacional de Antropología e Historia: bulletin of 9 January 2024 on Arqueología Mexicana no. 184, “Las chinampas de la Cuenca de México”, inah.gob.mx; and “El Albarradón de San Cristóbal”, lugares.inah.gob.mx",
      "period": "reporting current; the evidence reported spans 900 CE to 1856",
      "sourceType": "national institute archaeological reporting and heritage-site record",
      "sourceOrigin": "real modern institutional documentation",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "documented",
      "contribution": "Material depth and scale: chinampas in the Basin of Mexico from the Early Postclassic, 900 to 1200 CE, at Xaltocan; a 2015 salvage excavation identifying remains of chinampas and canals in use between 1300 and 1521 CE in a Mexica district of ancient México-Tenochtitlan; the crops recovered from such contexts; pre-Hispanic hydraulic works including a dike built to separate the waters within Lake Texcoco and reduce flooding at Tenochtitlan; and the record of destruction, flood and repeated rebuilding from 1604 to 1856.",
      "limitation": "Supplies nobody's words, confirms no event in the game, dates no individual plot, and does not say which part of the lake held which water. It is expressly not used to certify the game's reconstructed east-and-west arrangement.",
      "gameCorrespondence": "No runtime counterpart. The level narrates a dike and gates; this source is where the documented hydraulic works come from.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 6",
      "rights": "INAH web resources. Cited and summarised, not reproduced."
    },
    {
      "id": "lakecity-figure",
      "displayLabel": "Figure — the lake-city plan, adapted",
      "creator": "Curriculum",
      "period": "not applicable",
      "sourceType": "deterministic HTML and CSS schematic",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "contribution": "Redraws the relationships the Library's record of the 1524 plan describes: an island city in a lake, causeways running out to the shores, and settlements ringing the water.",
      "limitation": "An adaptation, and it says so in print. It claims no number, direction or length for the causeways, no distance, shape or size for anything, and no orientation — the source's own west-at-the-top orientation is stated rather than imitated. It is not to scale and it is not the evidence; Source F is.",
      "gameCorrespondence": "No runtime counterpart. Drawn for this packet from the certified historical map.",
      "fallbackCorrespondence": "Student page 5 · Accessible page 7"
    },
    {
      "id": "system-figure",
      "displayLabel": "Figure — the chinampa system at two scales",
      "creator": "Curriculum",
      "period": "not applicable",
      "sourceType": "deterministic HTML and CSS schematic",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "contribution": "Sets one field beside the basin it sits in: at field scale the canals, the staked structure, the two soil layers, the cultivated surface, the willow and the lake bottom under all of it, with the renewal arrow from the canal floor to the plot; at basin scale the chinampa zone, the open lake, the dike and the water beyond it.",
      "limitation": "A schematic of relationships. Nothing on it is to scale, no measurement may be read from it, it draws no real place, and it assigns no compass direction or salinity to any part of the lake.",
      "gameCorrespondence": "No runtime counterpart. The level narrates the system; this figure is built from the certified real-world estate instead.",
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
        "task": "C08-T1",
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
        "task": "C08-T2",
        "id": "water-evidence",
        "obligation": "Name one kind of water evidence you would look for.",
        "student": [
          "t2-water"
        ],
        "accessible": [
          "a2-water"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T2",
        "id": "land-evidence",
        "obligation": "Name one kind of soil or land evidence you would look for.",
        "student": [
          "t2-soil"
        ],
        "accessible": [
          "a2-soil"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T3",
        "id": "map-setting",
        "obligation": "Say where the city stands and what surrounds it.",
        "student": [
          "t3-setting"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t3-supplied-setting"
      },
      {
        "task": "C08-T3",
        "id": "map-connection",
        "obligation": "Say how the plan shows the city connected to the land.",
        "student": [
          "t3-connection"
        ],
        "accessible": [
          "a3-connection"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T3",
        "id": "map-geography",
        "obligation": "Use the map and one other source to say why the setting mattered for farming.",
        "student": [
          "t3-geography"
        ],
        "accessible": [
          "a3-geography"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T3",
        "id": "map-limit",
        "obligation": "State one limitation of the map as evidence about 1487.",
        "student": [
          "t3-limit"
        ],
        "accessible": [
          "a3-limit"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T4",
        "id": "field-construction",
        "obligation": "Explain how a chinampa is built and what holds it in place.",
        "student": [
          "t4-build"
        ],
        "accessible": [
          "a4-build"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T4",
        "id": "canal-functions",
        "obligation": "Explain more than one thing the canals do in the system.",
        "student": [
          "t4-canals"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t4-modelled-relationship"
      },
      {
        "task": "C08-T4",
        "id": "soil-renewal",
        "obligation": "Explain how soil renewal supports repeated cultivation.",
        "student": [
          "t4-renewal"
        ],
        "accessible": [
          "a4-renewal"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T4",
        "id": "basin-scale",
        "obligation": "Explain how basin-scale water management reaches one plot.",
        "student": [
          "t4-basin"
        ],
        "accessible": [
          "a4-basin"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T5",
        "id": "row-reconstructed",
        "obligation": "Weigh the reconstructed game evidence.",
        "student": [
          "t5-r1-contrib",
          "t5-r1-cannot"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t5-modelled-row"
      },
      {
        "task": "C08-T5",
        "id": "row-fao",
        "obligation": "Weigh the FAO documentation.",
        "student": [
          "t5-r2-contrib",
          "t5-r2-cannot"
        ],
        "accessible": [
          "a5-r2-cannot"
        ],
        "differenceClass": "declared-reduction",
        "governedBy": "t5-prefilled-cell"
      },
      {
        "task": "C08-T5",
        "id": "row-inah",
        "obligation": "Weigh the INAH archaeology and water works.",
        "student": [
          "t5-r3-contrib",
          "t5-r3-cannot"
        ],
        "accessible": [
          "a5-r3-contrib",
          "a5-r3-cannot"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T5",
        "id": "row-map",
        "obligation": "Weigh the 1524 published plan.",
        "student": [
          "t5-r4-contrib",
          "t5-r4-cannot"
        ],
        "accessible": [
          "a5-r4-contrib",
          "a5-r4-cannot"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T6",
        "id": "inside-layer",
        "obligation": "Test the collapse account against the reconstructed evidence only.",
        "student": [
          "t6-inside"
        ],
        "accessible": [
          "a6-inside"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T6",
        "id": "outside-layer",
        "obligation": "State what the real-world sources do and do not establish.",
        "student": [
          "t6-outside"
        ],
        "accessible": [
          "a6-outside"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T7",
        "id": "definition",
        "obligation": "State accurately what a chinampa is.",
        "student": [
          "t7-definition"
        ],
        "accessible": [
          "a7-definition"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T7",
        "id": "evidence-links",
        "obligation": "Supply two evidentiary links from different real-world sources or figures.",
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
        "task": "C08-T7",
        "id": "geography-function",
        "obligation": "Connect the geographic setting to the agricultural function.",
        "student": [
          "t7-geography"
        ],
        "accessible": [
          "a7-geography"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T7",
        "id": "source-qualification",
        "obligation": "State one thing a named source cannot establish.",
        "student": [
          "t7-qualification"
        ],
        "accessible": [
          "a7-qualification"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T7",
        "id": "system-synthesis",
        "obligation": "Explain how the parts of the system work together.",
        "student": [
          "t7-synthesis"
        ],
        "accessible": [
          "a7-synthesis"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T8",
        "id": "transfer-checks",
        "obligation": "Name one physical-landscape check and one source or provenance check.",
        "student": [
          "t8-physical",
          "t8-source"
        ],
        "accessible": [
          "a8-physical",
          "a8-source"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C08-T8",
        "id": "transfer-explanation",
        "obligation": "Explain both checks by method rather than by this case.",
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
      "id": "t3-supplied-setting",
      "task": "C08-T3",
      "what": "Part A is supplied complete as a worked example: the island-in-a-lake setting is named for the learner.",
      "effect": "Accessible answers three parts of Task 3; Student answers four.",
      "whyNotALeak": "Naming the setting is the orientation step. The map-reading requirement is untouched: the learner still has to say how the city is connected to the land, still has to use the map as geographic evidence for why farming took this form, and still has to state a limitation of the map.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t4-modelled-relationship",
      "task": "C08-T4",
      "what": "Part B, the canal functions, is worked in full as a modelled relationship, with selected labels supplied on the figure.",
      "effect": "Accessible answers three parts of Task 4; Student answers four.",
      "whyNotALeak": "The modelled part is the one whose answer the figure already lists. The three relationships the case turns on — how the field is built and held, how soil renewal permits repeated cropping, and how the basin scale reaches the plot — are answered independently in both editions, and the modelled example is written to show what explaining a relationship looks like.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t5-modelled-row",
      "task": "C08-T5",
      "what": "The reconstructed-evidence row is supplied complete in both cells as a worked example.",
      "effect": "Accessible completes five matrix fields; Student completes eight.",
      "whyNotALeak": "The modelled row is the one the source-status notice on page 1 has already stated in full. The two rows that carry the real evidentiary reasoning — the archaeology and the historical map — are worked independently in both editions.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t5-prefilled-cell",
      "task": "C08-T5",
      "what": "The FAO row's contribution cell is supplied; its limitation is not.",
      "effect": "Part of one repeated row is removed; the judgment in that row is preserved.",
      "whyNotALeak": "What the FAO documentation contributes is stated on the source card itself, so supplying it removes transcription rather than reasoning. What it cannot establish is the judgment, and it is still required.",
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
      "rule": "Every printable proposition in every role is scanned against the three closed negative classes. Internal punctuation is not a safety boundary.",
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
          "chinampasFloat",
          "reconstructionAsPrimary",
          "mapAsExactSnapshot"
        ]
      },
      {
        "id": "answer-key-floor",
        "roles": [
          "answer"
        ],
        "purpose": "The Answer Key must be able to state the wording it refuses at every level.",
        "allowedConcepts": [
          "chinampasFloat",
          "reconstructionAsPrimary",
          "mapAsExactSnapshot"
        ]
      }
    ],
    "structuralExemptSelectors": []
  },
  "figureContract": {
    "rule": "Both figures are deterministic HTML and CSS, carry a printed SOURCE STATUS line and a printed adaptation or basis line, and carry accessibility text held to the same factual contracts as the visible drawing. No imagery of any kind is used anywhere in this package apart from the shared institutional insignia.",
    "figures": [
      {
        "id": "lake-city-plan",
        "selector": "[data-map-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "H3 sourced historical map, adapted",
        "requiresPrintedText": [
          "THE ISLAND CITY",
          "CAUSEWAYS",
          "LAKE",
          "LAKESHORE"
        ],
        "requiresCaptionTerms": [
          "ADAPTED FROM",
          "LIBRARY OF CONGRESS",
          "RECONSTRUCTION",
          "NOT TO SCALE"
        ],
        "requiresAdaptationNote": "not claimed by this drawing",
        "requiresOrientationNote": "oriented with west at the top",
        "prohibitedPatterns": [
          {
            "id": "invented-distance",
            "regex": "\\b\\d+\\s?(?:km|kilometres|kilometers|miles|leagues)\\b",
            "why": "The adaptation claims no distance; the plan supports none."
          },
          {
            "id": "exact-1487",
            "regex": "\\bexact\\b[^.!?]{0,30}\\b1487\\b",
            "why": "The plan is not an exact map of 1487 and its accessibility text may not say so."
          },
          {
            "id": "causeway-count",
            "regex": "\\b(?:three|four|five|six|3|4|5|6)\\s+causeways\\b",
            "why": "The certified record gives no number of causeways, so neither the drawing nor its alt text may."
          }
        ],
        "requiresAltConcepts": [
          "island city",
          "causeways",
          "lake",
          "lakeshore"
        ]
      },
      {
        "id": "chinampa-system",
        "selector": "[data-system-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "H8 agroecosystem cross-section at two scales",
        "requiresPrintedText": [
          "CANAL",
          "CULTIVATED SURFACE",
          "ORGANIC-MATTER LAYER",
          "LAKE-SEDIMENT LAYER",
          "STAKED STRUCTURE",
          "LAKE BOTTOM",
          "CHINAMPA ZONE",
          "OPEN LAKE",
          "DIKE"
        ],
        "requiresCaptionTerms": [
          "BASED ON",
          "RECONSTRUCTION",
          "NOT TO SCALE"
        ],
        "requiresScales": [
          "FIELD SCALE",
          "BASIN SCALE"
        ],
        "requiresNotFloatingStatement": "does not float",
        "prohibitedPatterns": [
          {
            "id": "floating-claim",
            "regex": "\\b(?:chinampas?|raised fields?|the (?:plots|gardens|fields))\\b[^.!?]{0,40}(?<!not )(?<!never )\\b(?:float|floats|floated|drift|drifts|drifted)\\b[^.!?]{0,30}\\b(?:on|upon|across|over)\\b",
            "why": "The figure exists to refuse the floating reading; its accessibility text may not state one."
          },
          {
            "id": "compass-claim",
            "regex": "\\b(?:east|west|north|south)(?:ern)?\\b[^.!?]{0,25}\\b(?:basin|water|side|reach)\\b",
            "why": "The certified INAH record assigns no compass direction to any part of the lake."
          },
          {
            "id": "numeric-confidence",
            "regex": "\\b\\d+\\s?(?:%|per cent|percent)\\b",
            "why": "No numerical confidence value is supported anywhere in this case."
          }
        ],
        "requiresAltConcepts": [
          "canal",
          "cultivated surface",
          "organic matter",
          "lake sediment",
          "staked structure",
          "lake bottom",
          "chinampa zone",
          "open lake",
          "dike"
        ]
      }
    ]
  },
  "standards": {
    "directlyAssessed": [
      "C3 D2.His.1.6-8",
      "C3 D3.2.6-8",
      "CCSS RH.6-8.7"
    ],
    "supporting": [
      "CCSS RH.6-8.9",
      "CCSS WHST.6-8.2"
    ],
    "contextual": [],
    "ngss": "No NGSS alignment is claimed at any status. The system this case describes is agricultural and hydrological, and a science performance expectation would be easy to reach for. No task asks a learner to construct a scientific explanation, develop or use a model of a natural system, or analyse data. The tasks measure geographic reasoning, systems description and source evaluation, and claiming a science standard for them would be a false claim about what is measured.",
    "rationale": "Task-first alignment. The three directly assessed claims each name the task that measures them and the limit on the claim: one system in one basin, an estate supplied rather than researched, one class of which is openly invented, and figures that are curriculum adaptations with printed status. RH.6-8.9 is deliberately held at supporting rather than promoted: the packet does place a plan published in 1524 beside present-day documentation, archaeological reporting and reconstructed evidence, but no task asks the learner to analyse the relationship between a primary and a secondary source on the same topic. Tasks 5 and 6 ask what each can and cannot carry, which practises the relationship that analysis rests on without performing it. WHST.6-8.2 is supporting because Task 7 is scored for reasoning rather than for craft. The list is deliberately short; nothing is claimed merely because the topic touches it."
  }
};
