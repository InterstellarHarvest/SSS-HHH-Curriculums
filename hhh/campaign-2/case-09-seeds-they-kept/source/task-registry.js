window.HHH_CASE09_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C2-CASE09",
  "runtimeId": "C2L2",
  "instructionalType": "CORE_CASE",
  "title": "The Seeds They Kept",
  "displayLabel": "9 - The Seeds They Kept",
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
  "learningGoal": "Explain why preserving crop genetic diversity during the Siege of Leningrad mattered and use chronology, provenance, collection continuity, and corroboration to evaluate what the evidence can establish about the collection's survival.",
  "guidingQuestion": "How can historians tell whether a collection survived a crisis as the same continuing collection, and what can each source actually prove?",
  "culminatingProduct": "Collection Continuity Judgment — a four-part provenance and continuity product. The learner states what the historical evidence supports about the collection's preservation and continuity, names the evidence that provides the strongest links in that chain, states what testimony or reconstructed evidence cannot establish, and explains why maintaining crop genetic diversity mattered beyond the immediate siege. Canonical CER is deliberately not used; see cerDecision.",
  "conceptualDistinction": "Collection continuity does not require physical immobility or perfect survival. A defensible continuity chain may include movement, reproduction, partial loss, emergency conservation, changing custodianship and post-crisis regeneration, when provenance supports the connection.",
  "cerDecision": {
    "id": "case09-cer-declined-v1.0",
    "decision": "DECLINED",
    "blueprintProduct": "evidence-based provenance/continuity explanation (Blueprint, Core Case 09)",
    "rationale": "The Blueprint permits canonical CER only where its structure genuinely supports the case, and names an evidence-based provenance and continuity explanation as this case's culminating product. A CER frame would force one claim to the front and subordinate everything else to it, and this case assesses four separate obligations that cannot be collapsed into claim, evidence and reasoning without losing one of them: a judgment about continuity, the identification of the strongest links in a provenance chain, an explicit statement of what testimony and reconstructed evidence cannot establish, and a separate explanation of why crop genetic diversity mattered beyond the siege. The Collection Continuity Judgment keeps the four as separately scored parts, and the Answer Key must distinguish the in-world verdict from the defensible real-history conclusion, which a single CER claim could not do.",
    "precedent": "HHH Campaign 1 Core Case 06 declined canonical CER for its systems and evidence-audit explanation on the Blueprint ground, Campaign 2 Core Case 07 followed it for its provenance and authenticity judgment, and Core Case 08 for its engineered-landscape explanation. This case follows that established precedent rather than inventing a new one.",
    "enforcement": "No role renders the shared canonical CER component, and no role declares a CER contract.",
    "prohibitedSelectors": [
      "[data-cer-contract]",
      ".canonical-cer",
      ".cer-stack"
    ]
  },
  "sourceStatusContract": {
    "rule": "Every learner-facing evidence object declares its status in markup (data-evidence-layer) and in printed text (a SOURCE STATUS line), and no role converts reconstructed game evidence into a claim about 1941 to 1946 or a documented source into evidence that a game event happened.",
    "bands": [
      {
        "id": "reconstructed",
        "label": "RECONSTRUCTED GAME EVIDENCE",
        "attribute": "reconstructed",
        "statusMarker": "reconstructed game evidence",
        "covers": [
          "the besieged street and the ration notice",
          "Dr. Morozov and everything he says",
          "the Archive's preservation scan of the collection",
          "the Archive's accession-ledger cross-reference",
          "the recovered Vavilov presentation and the Archive's annotation of it",
          "the Consumption Report",
          "every date, count, name, seal, signature and reading belonging to any of the above"
        ],
        "rule": "Evidence written for the game. It may be reasoned about, compared and tested inside the case. It may never be cited as a fact about the real Institute, the real siege or the real collection."
      },
      {
        "id": "documented",
        "label": "DOCUMENTED",
        "attribute": "documented",
        "statusMarker": "documented",
        "covers": [
          "the Crop Trust account of Vavilov, the collection and the siege",
          "Loskutov's archival account of the Institute's wartime work, published in the Institute's own journal",
          "the Institute's own statement of its present identity"
        ],
        "rule": "Real published documentation, cited to a real institution or journal. It establishes what happened to the real collection and the people who kept it. It is never evidence that any event in the game happened."
      },
      {
        "id": "curriculum-model",
        "label": "CURRICULUM-ORIGINAL SCHEMATIC",
        "attribute": "curriculum-model",
        "statusMarker": "curriculum-original schematic",
        "covers": [
          "the chronology figure",
          "the collection-continuity chain figure"
        ],
        "rule": "Drawn for this packet from the documented sources. A figure that organises evidence is not itself evidence, and each figure prints its basis and its status."
      }
    ],
    "statusVocabulary": [
      "reconstructed game evidence",
      "documented",
      "curriculum-original schematic"
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
    "nonMergerRule": "Reconstructed game evidence can support reasoning inside the case. It cannot establish what happened to the real collection. A documented source can establish what happened to the real collection. It cannot prove any event in the game. Both learner editions carry this rule on page 1.",
    "fictionalDataRule": "Every deterministic invented value sits inside a node carrying data-fictional-data, and every such node sits inside a reconstructed evidence object.",
    "gameClaimRule": "A learner or teacher page may quote a claim made inside the game in order to test it. Every such quotation outside a reconstructed evidence object is wrapped in a node carrying data-game-claim, sits inside a task that tests it, and is excused from the historical-claim guards only while it is so marked.",
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
      "ranksUp",
      "rankUpText",
      "besieged_street",
      "seed_vault",
      "institute_office",
      "siege_witnessed",
      "keeper_testimony",
      "collection_intact",
      "accessions_continuous",
      "vavilov_fate",
      "report_read"
    ],
    "prohibitedRuntimeIdentifierRule": "No printable page in any role may display a runtime implementation identifier. The list is identifier-shaped by construction so that it can never accidentally forbid ordinary English.",
    "enforcedRoles": [
      "student",
      "teacher",
      "answer",
      "accessible"
    ]
  },
  "runtimeDependency": {
    "id": "case09-runtime-dependency-v1.0",
    "findingId": "HHH-IMP-C2L2-001",
    "dependencyClass": "GAME_REMEDIATION_BLOCKS_FINALIZATION",
    "dependencyStatus": "RESOLVED_VERIFIED",
    "auditedGameCommit": "9b8545ed6ecf98b337326390400076e36789e056",
    "resolvedGameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
    "verifiedSemantics": "At the resolved game commit the level has six operationally required evidence clues and no insight-flagged source. The street evidence is required rather than optional: the insight flag was removed from its source while the node-level bonus scoring was retained. The vault unlocks on the street evidence and the office unlocks on the keeper's testimony, so the intended street-first route is now structurally honest.",
    "requiredStrandCount": 6,
    "requiredStrands": [
      {
        "id": "siege-context",
        "source": "besieged-street",
        "what": "reconstructed siege context — the street and the ration notice",
        "runtimeStatus": "required; formerly insight-flagged, corrected at the resolved commit"
      },
      {
        "id": "keeper-testimony",
        "source": "keeper-testimony",
        "what": "reconstructed testimony of the surviving keeper"
      },
      {
        "id": "collection-condition",
        "source": "preservation-scan",
        "what": "reconstructed examination of the collection's physical condition"
      },
      {
        "id": "accession-continuity",
        "source": "accession-ledger",
        "what": "reconstructed accession-ledger cross-reference"
      },
      {
        "id": "vavilov-fate",
        "source": "vavilov-record",
        "what": "reconstructed recovered record and annotation of Vavilov's fate"
      },
      {
        "id": "consumption-report",
        "source": "consumption-report",
        "what": "the reconstructed competing record the case exists to test"
      }
    ],
    "rule": "This package does not modify the game and does not recreate the former optional-clue reading of the street evidence. The shared remediation tracker already records the resolution, and this package leaves the tracker untouched.",
    "qualificationFindingId": "HHH-GAME-C2L2-001",
    "qualificationClass": "CURRICULUM_QUALIFICATION_REQUIRED",
    "qualificationStatus": "OPEN_AT_AUDITED_GAME_BASELINE",
    "qualificationRule": "Published accounts disagree on the number and category of Institute staff who died protecting the collection, and Vavilov himself had been arrested before the siege. The packet uses sourced, qualified count language and separates Vavilov's fate from the staff's wartime actions in every role."
  },
  "historicalQualification": {
    "id": "case09-historical-qualification-v1.0",
    "findingId": "HHH-GAME-C2L2-001",
    "rule": "The collection remained substantially continuous through documented custodianship and conservation even though preserving it involved movement, reproduction, partial loss and later regeneration. The packet teaches that conclusion, and refuses both the game's simplification and its opposite.",
    "refusedSimplifications": [
      "that the entire collection never left one room",
      "that nothing was lost",
      "that Vavilov personally guarded the collection during the siege",
      "that one exact staff-death count is universally settled",
      "that a materially clean document is thereby proved forged"
    ],
    "deathCountRule": "The one archival account this packet certifies counts more than twenty specialists and scientists lost to the siege, names many of them with the cause recorded in their personal files, and records that the first autumn alone cost more than thirty researchers to bombing, starvation and the front. Other published accounts count differently. Every count in every role is qualified by its source.",
    "vavilovRule": "Vavilov was arrested in 1940, before the siege, and died in incarceration in Saratov on 26 January 1943. He was never at the besieged Institute. The staff who kept the collection were his colleagues and successors, named in the documented record.",
    "printedRule": "Collection continuity does not require physical immobility or perfect survival",
    "requiredPrintedStatements": [
      "Collection continuity does not require physical immobility or perfect survival",
      "arrested in 1940",
      "26 January 1943",
      "8 September 1941",
      "more than twenty",
      "about 40,000 accessions",
      "not one of them is proof that the report is forged",
      "cannot establish what happened to the real collection",
      "cannot prove any event in the game"
    ],
    "requiredPrintedStatementRoles": [
      "student",
      "accessible"
    ],
    "positiveRequirements": [
      {
        "id": "chronology-figure-present",
        "selector": "[data-chronology-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the two-strand chronology that keeps Vavilov's timeline apart from the siege."
      },
      {
        "id": "continuity-chain-present",
        "selector": "[data-continuity-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the provenance and continuity chain, with movement, reproduction and loss drawn as links rather than hidden."
      },
      {
        "id": "continuity-rule-printed",
        "selector": "[data-continuity-rule='not-immobility']",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions print, inside the continuity figure, that continuity does not require physical immobility or perfect survival."
      },
      {
        "id": "report-test-organiser-printed",
        "selector": "[data-claim-test]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the four-test organiser that keeps the Consumption Report inside the game and tests it by more than its appearance."
      },
      {
        "id": "judgment-product-printed",
        "selector": "[data-continuity-judgment]",
        "roles": [
          "student",
          "accessible"
        ],
        "rule": "Both learner editions carry the four-part Collection Continuity Judgment."
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
        "id": "answer-key-two-layer-verdict",
        "selector": "[data-two-layer-verdict]",
        "roles": [
          "answer"
        ],
        "rule": "The Answer Key's Task 7 exemplar distinguishes the in-world verdict from the defensible real-history conclusion."
      }
    ],
    "prohibitedFramings": {
      "rule": "Four CLOSED negative classes, each anchored to a named subject register and each requiring an affirmative, unnegated predicate. A proposition violates a class only when the class's subject is present in the same proposition and one of its patterns matches, and, for a class that declares unlessPatterns, when none of those qualifiers is present in the same proposition. Propositions inside a reconstructed evidence object, or inside a marked in-game quotation, are the game layer and are excused from the two historical-claim classes. This is a bounded guard against four known high-risk misconceptions. It is not, and does not claim to be, a general semantic detector: an unseen paraphrase can pass it, and manual cross-role review remains required.",
      "vavilovPresentAtSiege": {
        "why": "Vavilov personally present at, guarding, or witnessing the Institute during the siege.",
        "subjectPatterns": [
          "\\bvavilov\\b"
        ],
        "patterns": [
          "\\bvavilov\\b(?:\\s+(?:himself|personally))?(?:(?!\\b(?:not|never|no longer|nowhere|impossible)\\b)[^.!?]){0,30}\\b(?:was|is|stayed|remained|worked|lived|served|present)\\b(?:(?!\\b(?:not|never|no longer|nowhere|impossible)\\b)[^.!?]){0,30}\\b(?:at|in|inside)\\b\\s+(?:the\\s+)?(?:besieged\\s+)?(?:institute|vault|building|leningrad)\\b",
          "\\bvavilov\\b(?:\\s+(?:himself|personally))?\\s+(?:guarded|protected|defended|kept|saved|preserved|watched over|starved beside|witnessed)\\b(?!\\s+(?:nothing|no\\b))[^.!?]{0,40}\\b(?:the collection|the seeds|the vault|the staff|the institute|the work)\\b",
          "\\b(?:director|professor)\\s+vavilov\\b[^.!?]{0,30}\\b(?:signed|countersigned|authorised|authorized|witnessed|supervised|ordered)\\b(?!\\s+(?:nothing|no\\b))[^.!?]{0,40}\\b(?:194[1-4]|the siege|the blockade|on site|at the institute)\\b"
        ]
      },
      "nothingMovedAsHistory": {
        "why": "The real collection stated to have stayed physically immobile: never left the room, building or city.",
        "subjectPatterns": [
          "\\b(?:the collection|the seeds?|the accessions|the whole collection|the entire collection|the seed collection|vavilov's collection|nothing|none of it|not one accession|not a single accession)\\b"
        ],
        "patterns": [
          "\\b(?:the collection|the seeds?|the accessions|the whole collection|the entire collection|the seed collection|vavilov's collection)\\b[^.!?]{0,30}(?<!not )(?<!never )\\b(?:never left|never moved|did not move|was never moved|stayed in|remained in)\\b[^.!?]{0,12}\\b(?:the room|one room|the building|the institute|leningrad|place|the same room|the vault)\\b",
          "\\b(?:nothing|none of it|not one accession|not a single accession)\\b[^.!?]{0,20}\\b(?:left|moved|was moved|was evacuated|was taken)\\b[^.!?]{0,20}\\b(?:the room|the building|the institute|leningrad|the city)\\b"
        ],
        "unlessPatterns": [
          "\\b(?:the (?:game|scan|report|ledger|keeper)|inside the game|game evidence|reconstructed|do not credit|is not history|not history|claims? that|reads:|line that|says that)\\b"
        ],
        "layerExempt": true
      },
      "zeroLossAsHistory": {
        "why": "The real collection stated to have survived with no loss at all.",
        "subjectPatterns": [
          "\\b(?:the collection|the seeds?|the accessions|every accession|all the accessions|the whole collection|the entire collection|nothing|no accession|not one accession)\\b"
        ],
        "patterns": [
          "\\bnothing\\b[^.!?]{0,12}\\b(?:was lost|was destroyed|died|perished)\\b(?![^.!?]*\\b(?:inside the game|the game says|the scan says|in the game|game evidence)\\b)",
          "\\b(?:no accession|not one accession|not a single accession|no losses?)\\b[^.!?]{0,24}\\b(?:was lost|were lost|lost|at all|whatever)\\b",
          "\\b(?:every accession|all the accessions|all of the accessions|the whole collection|the entire collection)\\b[^.!?]{0,24}\\b(?:survived|came through|was saved|were saved|remained)\\b(?!\\s+(?:only|partly|in part))[^.!?]{0,20}\\b(?:untouched|intact|unharmed|whole|without loss|completely|entirely)\\b",
          "\\b(?:the collection|the seeds?|the accessions)\\b[^.!?]{0,30}\\b(?:survived|came through|was preserved|were preserved)\\b[^.!?]{0,16}\\b(?:without (?:any )?loss|with no loss|with nothing lost|perfectly|in full|complete and untouched)\\b"
        ],
        "unlessPatterns": [
          "\\b(?:the (?:game|scan|report|ledger|keeper)|inside the game|game evidence|reconstructed|do not credit|is not history|not history|claims? that|reads:|line that|says that)\\b"
        ],
        "layerExempt": true
      },
      "cleanProvesForged": {
        "why": "A materially clean, neat or perfect document declared forged because of that appearance alone.",
        "subjectPatterns": [
          "\\b(?:clean|neat|perfect|perfection|tidy|flawless|typed)\\b"
        ],
        "patterns": [
          "\\b(?:clean|neat|perfect|tidy|flawless|too clean|too neat|too perfect)\\b[^.!?]{0,40}\\b(?:so|therefore|which means|means|proves|shows|is why)\\b(?!\\s+(?:nothing|it is not|not))[^.!?]{0,30}\\b(?:forged|a forgery|fake|faked|false|not genuine)\\b",
          "\\b(?:forged|a forgery|fake|faked|false)\\b[^.!?]{0,24}\\bbecause\\b[^.!?]{0,30}\\b(?:clean|neat|perfect|tidy|flawless|typed)\\b",
          "\\b(?:perfection|neatness|cleanness|tidiness)\\b[^.!?]{0,20}\\b(?:is|was)\\b(?!\\s+(?:not|never|no))[^.!?]{0,12}\\b(?:proof|the proof|enough)\\b"
        ]
      },
      "settledDeathCount": {
        "why": "A specific number of staff deaths stated as settled fact with no qualifying source or count language in the same proposition.",
        "subjectPatterns": [
          "\\b(?:staff|scientists|employees|keepers|researchers|specialists|people|workers|curators)\\b"
        ],
        "patterns": [
          "\\b(?:exactly|precisely)\\s+(?:\\d+|nine|ten|eleven|twelve|twenty|thirty|forty)\\b[^.!?]{0,30}\\b(?:staff|scientists|employees|keepers|researchers|specialists|people|workers|curators)\\b[^.!?]{0,24}\\b(?:died|starved|perished|lost their lives)\\b",
          "\\b(?:\\d+|nine|ten|eleven|twelve|twenty|thirty|forty)\\s+(?:of (?:the |its )?)?(?:staff|scientists|employees|keepers|researchers|specialists|people|workers|curators)\\b[^.!?]{0,24}\\b(?:died|starved|perished|lost their lives)\\b"
        ],
        "unlessPatterns": [
          "\\b(?:more than|at least|about|around|roughly|over|some|several|many)\\b",
          "\\b(?:according to|counts|count|account|accounts|names|reports|recorded|record|archiv|source|published)\\b",
          "\\b(?:differ|disagree|vary|qualif|uncertain|disputed|unsettled)\\b"
        ]
      }
    },
    "negativeControls": {
      "vavilovPresentAtSiege": [
        "Vavilov guarded the collection during the siege.",
        "Vavilov was at the Institute through the blockade.",
        "Vavilov remained in Leningrad through the winter of 1941.",
        "Director Vavilov witnessed the staff's work at the Institute in 1942.",
        "Vavilov stayed in Leningrad during the siege.",
        "Vavilov himself protected the seeds."
      ],
      "nothingMovedAsHistory": [
        "The collection never left the room.",
        "The seeds never moved from the building.",
        "Nothing left the Institute during the siege.",
        "The whole collection stayed in one room through the war."
      ],
      "zeroLossAsHistory": [
        "Nothing was lost.",
        "Every accession survived the siege untouched.",
        "No accession was lost at all.",
        "The collection survived without any loss."
      ],
      "cleanProvesForged": [
        "The report is too clean, so it is forged.",
        "It is a forgery because it is so neat.",
        "Perfect typing proves it is fake.",
        "Its perfection is proof."
      ],
      "settledDeathCount": [
        "Nine staff died guarding the collection.",
        "Twelve scientists starved to death in the vault.",
        "Exactly 28 employees died of hunger."
      ]
    },
    "positiveControls": [
      "Vavilov was arrested in 1940 and was never at the besieged Institute.",
      "Vavilov built the collection expedition by expedition.",
      "Any record placing Vavilov at the Institute during the siege is impossible.",
      "The people Vavilov trained guarded the collection.",
      "Vavilov did not guard the collection during the siege; he was in prison.",
      "Collection continuity does not require physical immobility or perfect survival.",
      "The collection remained substantially continuous despite losses.",
      "Not every accession survived.",
      "Part of the collection was evacuated to Krasnoufimsk and part stayed in Leningrad.",
      "About 40,000 accessions were lost over the war, according to Loskutov's account.",
      "Inside the game, the scan reports that nothing was eaten.",
      "A clean document can be genuine.",
      "Its perfection is a reason to look closer, not a verdict.",
      "The report fails because the countersignature is impossible, not because it is neat.",
      "Loskutov's account counts more than twenty specialists and scientists who died.",
      "Published accounts give different numbers of staff who died.",
      "Staff died of hunger at their desks beside the seeds they would not eat.",
      "The collection was divided, sealed, partly flown out, replanted and checked, and it is still the same collection."
    ]
  },
  "chronologyBoundary": {
    "id": "case09-chronology-v1.0",
    "selector": "[data-chronology-contract]",
    "roles": [
      "student",
      "accessible"
    ],
    "strands": [
      {
        "id": "vavilov",
        "label": "VAVILOV"
      },
      {
        "id": "institute",
        "label": "INSTITUTE"
      }
    ],
    "rule": "Two strands on one axis, every row dated from a certified documented source, every row printing its strand word. The arrest row precedes the siege row in the document order, the death row is marked as happening in Saratov, and no row places Vavilov in Leningrad after 1940.",
    "requiredRows": [
      {
        "year": "1887",
        "strand": "vavilov",
        "certifiedBy": "crop-trust-vavilov",
        "event": "born in Moscow"
      },
      {
        "year": "1916–1933",
        "strand": "vavilov",
        "certifiedBy": "crop-trust-vavilov",
        "event": "collecting expeditions on five continents; more than 250,000 samples gathered"
      },
      {
        "year": "1940",
        "strand": "vavilov",
        "certifiedBy": "crop-trust-vavilov",
        "event": "arrested during a collecting expedition in western Ukraine"
      },
      {
        "year": "1941",
        "strand": "institute",
        "certifiedBy": "loskutov-wartime",
        "event": "22 June invasion; 25–27 August rail evacuation fails; 8 September the siege ring closes"
      },
      {
        "year": "1941–42",
        "strand": "institute",
        "certifiedBy": "loskutov-wartime",
        "event": "collection divided and sealed inside the building; part flown to Krasnoufimsk; staff die of hunger at their posts"
      },
      {
        "year": "1942–43",
        "strand": "institute",
        "certifiedBy": "loskutov-wartime",
        "event": "staff evacuated over Lake Ladoga with seed; potatoes and cereals re-sown in suburban fields under fire"
      },
      {
        "year": "1943",
        "strand": "vavilov",
        "certifiedBy": "crop-trust-vavilov",
        "event": "26 January: dies in incarceration in Saratov"
      },
      {
        "year": "1944",
        "strand": "institute",
        "certifiedBy": "loskutov-wartime",
        "event": "siege lifted; first staff return from Krasnoufimsk in February"
      },
      {
        "year": "1946",
        "strand": "institute",
        "certifiedBy": "loskutov-wartime",
        "event": "whole collection checked; emergency regeneration programme"
      }
    ],
    "requiredPrintedText": [
      "VAVILOV",
      "INSTITUTE",
      "1940",
      "8 September 1941",
      "26 January 1943",
      "Saratov",
      "Krasnoufimsk",
      "1946"
    ],
    "requiresCaptionTerms": [
      "BASED ON",
      "CROP TRUST",
      "LOSKUTOV",
      "NOT TO SCALE"
    ],
    "requiresAltConcepts": [
      "two strands",
      "1940",
      "arrested",
      "8 September 1941",
      "26 January 1943",
      "Saratov",
      "Krasnoufimsk",
      "1946"
    ],
    "prohibitedPatterns": [
      {
        "id": "august-1940-as-documented",
        "regex": "\\baugust\\s+1940\\b",
        "why": "The month of the arrest is the game's annotation, not a claim the certified documented estate supports; the documented timeline says 1940."
      },
      {
        "id": "exact-siege-length-days",
        "regex": "\\b(?:87[0-9]|88[0-9]|89[0-9]|900|90[1-9])\\s+days\\b(?![^.!?]*\\bcrop trust\\b)",
        "why": "The 900-day figure is printed only as the Crop Trust's own conventional description."
      }
    ]
  },
  "continuityChain": {
    "id": "case09-continuity-v1.0",
    "selector": "[data-continuity-contract]",
    "roles": [
      "student",
      "accessible"
    ],
    "rule": "A deterministic provenance and continuity chain drawn only from the certified documented estate. It makes visible pre-crisis collection identity, wartime preservation, transfer and reproduction, partial loss, and post-crisis verification and regeneration, and it states in print that continuity does not require immobility or perfect survival. The game's reconstructed simplicity is not reproduced as history anywhere in the figure.",
    "nodes": [
      {
        "id": "pre-crisis",
        "label": "PRE-CRISIS COLLECTION",
        "status": "documented",
        "certifiedBy": [
          "crop-trust-vavilov",
          "loskutov-wartime"
        ]
      },
      {
        "id": "failed-evacuation",
        "label": "FAILED RAIL EVACUATION",
        "status": "documented",
        "certifiedBy": [
          "loskutov-wartime"
        ]
      },
      {
        "id": "divided-sealed",
        "label": "DIVIDED AND SEALED",
        "status": "documented",
        "certifiedBy": [
          "loskutov-wartime"
        ]
      },
      {
        "id": "partial-evacuation",
        "label": "PARTIAL EVACUATION",
        "status": "documented",
        "certifiedBy": [
          "loskutov-wartime"
        ]
      },
      {
        "id": "reproduction",
        "label": "REPRODUCTION UNDER SIEGE",
        "status": "documented",
        "certifiedBy": [
          "loskutov-wartime"
        ]
      },
      {
        "id": "losses",
        "label": "LOSSES",
        "status": "documented",
        "certifiedBy": [
          "loskutov-wartime"
        ]
      },
      {
        "id": "check-regeneration",
        "label": "CHECK AND REGENERATION",
        "status": "documented",
        "certifiedBy": [
          "loskutov-wartime"
        ]
      },
      {
        "id": "continuing",
        "label": "CONTINUING COLLECTION",
        "status": "documented",
        "certifiedBy": [
          "loskutov-wartime",
          "vir-institute"
        ]
      }
    ],
    "linkLabels": [
      "same accessions, re-inventoried",
      "documented custodians",
      "duplicates flown out",
      "reproduced from the same accessions",
      "recorded, not hidden",
      "regenerated from surviving seed",
      "preserved in"
    ],
    "requiredPrintedText": [
      "PRE-CRISIS COLLECTION",
      "FAILED RAIL EVACUATION",
      "DIVIDED AND SEALED",
      "PARTIAL EVACUATION",
      "REPRODUCTION UNDER SIEGE",
      "LOSSES",
      "CHECK AND REGENERATION",
      "CONTINUING COLLECTION",
      "Krasnoufimsk",
      "about 40,000 accessions"
    ],
    "requiredRule": "Collection continuity does not require physical immobility or perfect survival",
    "requiresCaptionTerms": [
      "BASED ON",
      "LOSKUTOV",
      "CROP TRUST",
      "RECONSTRUCTION",
      "NOT TO SCALE"
    ],
    "requiresAltConcepts": [
      "pre-crisis collection",
      "failed rail evacuation",
      "divided and sealed",
      "partial evacuation",
      "reproduction under siege",
      "losses",
      "check and regeneration",
      "continuing collection",
      "does not require physical immobility or perfect survival"
    ],
    "prohibitedPatterns": [
      {
        "id": "never-left-as-history",
        "regex": "\\bnever left\\b",
        "why": "The figure draws movement; its text and accessibility description may not state the game's immobility claim as history."
      },
      {
        "id": "zero-loss",
        "regex": "\\b(?:nothing was lost|no losses|without loss|no accession was lost)\\b",
        "why": "The figure carries a LOSSES node because the documented record does."
      },
      {
        "id": "numeric-confidence",
        "regex": "\\b\\d+\\s?(?:%|per cent|percent)\\b",
        "why": "No numerical confidence value is supported anywhere in this case."
      }
    ]
  },
  "claimTest": {
    "id": "case09-claim-test-v1.0",
    "selector": "[data-claim-test]",
    "roles": [
      "student",
      "accessible"
    ],
    "rule": "The Consumption Report stays inside the reconstructed game layer. The organiser tests it by four things the game's own evidence can check — chronology, the collection's condition, the accession record and corroboration — and prints that appearance alone is not one of them.",
    "tests": [
      {
        "id": "chronology",
        "label": "CHRONOLOGY",
        "claim": "witnessed on site by Director N. I. Vavilov during the siege winter",
        "checkedAgainst": "vavilov-record"
      },
      {
        "id": "condition",
        "label": "COLLECTION CONDITION",
        "claim": "the rice, tubers and grain stores were consumed between December 1941 and March 1942",
        "checkedAgainst": "preservation-scan"
      },
      {
        "id": "record",
        "label": "ACCESSION RECORD",
        "claim": "the post-war bank was restocked from outside sources",
        "checkedAgainst": "accession-ledger"
      },
      {
        "id": "corroboration",
        "label": "CORROBORATION",
        "claim": "the staff consumed the collection under emergency authorisation",
        "checkedAgainst": "keeper-testimony"
      }
    ],
    "printedRule": "Its clean finish is a reason to look closer. It is not one of the four tests, and it is not proof.",
    "requiredPrintedText": [
      "CHRONOLOGY",
      "COLLECTION CONDITION",
      "ACCESSION RECORD",
      "CORROBORATION",
      "not one of them is proof that the report is forged"
    ],
    "insideGameOnly": true
  },
  "sourceCertification": {
    "id": "case09-source-certification-v1.0",
    "rule": "Case-local certification, bounded to the claims each source actually supports. The Phase 1 Master Game Audit is not modified: sources H13 and H14 are reused as the audit certified them, and the one source added here carries a case-local identifier and case-local bounds. No historical claim outside these bounds appears in the package.",
    "auditReused": [
      {
        "auditId": "H13",
        "caseSourceId": "vir-institute",
        "note": "Reused as the Phase 1 audit certified it. No audit record is modified by this package. As consulted for this candidate on 2026-08-20 the page carried the Institute's present name and status and the notice that it is under construction; it is therefore used for institutional identity only, and every siege-period claim rests on the other two sources."
      },
      {
        "auditId": "H14",
        "caseSourceId": "crop-trust-vavilov",
        "note": "Reused exactly as the Phase 1 audit certified it. No audit record is modified by this package."
      }
    ],
    "caseCertified": [
      {
        "caseSourceId": "crop-trust-vavilov",
        "auditId": "H14",
        "citation": "Crop Trust, “Nikolai Vavilov: The Father of Genebanks”, croptrust.org/news-events/news/nikolai-vavilov-the-father-of-genebanks/",
        "supports": [
          "Vavilov born on 25 November 1887 in Moscow",
          "115 research expeditions to 64 countries on five continents, the first in 1916 and the last in 1933",
          "publication of the theory of the centres of origin of cultivated plants in 1926",
          "a collection of more than 250,000 seed samples, the world's largest repository of crop diversity",
          "arrest in 1940 during a collecting expedition in western Ukraine, and the charge of being a traitor and a spy",
          "a death sentence commuted to twenty years' imprisonment",
          "death in incarceration in Saratov on 26 January 1943, the cause being starvation",
          "the 900-day siege of Leningrad, during which the Institute's staff refused to eat the seeds even as they starved to death",
          "genebanks, collecting expeditions and the use of plant genetic resources in breeding as standard parts of the food system today"
        ],
        "doesNotSupport": [
          "the month of the arrest",
          "any count of staff who died",
          "any named member of the wartime staff",
          "the movement, division, evacuation or reproduction of the collection during the war",
          "any event, person, record or reading in the game's case"
        ]
      },
      {
        "caseSourceId": "loskutov-wartime",
        "citation": "I. G. Loskutov, “Wartime activities of the Vavilov Institute”, Proceedings on Applied Botany, Genetics and Breeding, 2021, 182(2):151–162, DOI 10.30901/2227-8834-2021-2-151-162",
        "supports": [
          "the invasion beginning on 22 June 1941, and the government's pre-encirclement decision to evacuate the Institute, which failed",
          "the evacuation of staff and collection scheduled for 25 August 1941; the last railway cut on 27 August; the siege ring completely closed on 8 September 1941, when the staff returned to the city and the loaded freight car remained on a siding",
          "the division of the returned collection into two lots kept in different parts of the building to avoid destruction during bombing, the tying of boxes into packs, the relocation into sealed rooms, and the inventory and layout made when the relocation was completed",
          "the potato collection harvested unripe at Pavlovsk under fire and brought into the city with army transport, and the collections at Pavlovsk and Pushkin urgently evacuated to Leningrad at the end of August 1941",
          "the sealing of storerooms and the potato basement, keys held by a named superintendent, a 24-hour watch, weekly checks of the boxes, and daily checks of the seals",
          "famine beginning in the city in November 1941, with the Institute's employees among its first victims, and the daily bread ration in the winter of 1941–42 of 125 grams mixed half with bran",
          "named staff who died of hunger and exhaustion at their posts with the cause recorded in their personal files, among them the head of the rice section who died in his office in January 1942 beside several thousand packages of rice seed, and the keeper of the oat collection who died in the room where it was stored",
          "that the staff did not use the grain and seeds of the rice, pea, maize and wheat accessions to relieve their hunger",
          "more than thirty researchers lost in the first autumn of the siege to bombing, dystrophy and the front; more than twenty experts and scientists whose deaths the article attributes to the preservation effort; three employees who died on the evacuation journey carrying seed packages",
          "partial evacuation: a portion of the potato collection flown to Krasnoufimsk on 5 November 1941; staff evacuated over Lake Ladoga from 17 February 1942 carrying seed; about 40,000 seed packages and a full duplicate set of potato accessions flown out in March 1942; more than 100,000 accessions kept at Krasnoufimsk during the siege",
          "the need to reproduce living accessions: the potato collection of about 6,000 accessions planted in suburban state-farm fields each of the three siege seasons, and about 200 cereal varieties re-sown on 250 square metres in 1942 under fire",
          "seed germination reduced by damp and cold across three siege winters, and the 1943 regeneration sowing of about 200 early-ripening varieties on about 3.5 hectares, cultivated with shovels",
          "losses: only one potato cultivar lost from the Leningrad basement; some accessions from subtropical and highland areas losing their germination; several Chilean varieties and wild species lost and later revived in the Urals from other stations and from the seed repository; small thefts in the spring of 1942; about 40,000 accessions lost over the war by the Extraordinary State Commission's reckoning, including collections captured at Pushkin and fruit collections lost at Pavlovsk; about 30,000 accessions of essential-oil, medicinal, tobacco, tea and novel crops handed to other institutes after the war and lost there",
          "the first group of staff returning from Krasnoufimsk to Leningrad in February 1944 to prepare seed for shipment to the stations for reproduction; the thorough check of the collection's state in 1946 and the emergency regeneration plan for accessions of critically low viability, implemented with every station and breeding centre involved",
          "the Institute's own summary that its staff preserved the unique global collection collected by Vavilov and his associates and continued their work in the postwar period",
          "the Institute's present name, the N. I. Vavilov All-Russian Institute of Plant Genetic Resources"
        ],
        "doesNotSupport": [
          "Dr. Morozov as a historical person or eyewitness",
          "the Consumption Report, which is a fiction written for the game",
          "the Archive's preservation scan, its seal readings or its aging profile",
          "the game's specific accession ledger, its register numbers or its cross-reference",
          "the claim that every relevant accession remained untouched in one room",
          "a claim that there were zero losses",
          "a single universally settled staff-death count",
          "any quotation attributed to Vavilov, and any runtime dialogue",
          "any exact forensic result produced in the game",
          "the month of Vavilov's arrest, or the date the siege was lifted beyond the February 1944 return"
        ]
      },
      {
        "caseSourceId": "vir-institute",
        "auditId": "H13",
        "citation": "N. I. Vavilov All-Russian Institute of Plant Genetic Resources (VIR), “About institute”, vir.nw.ru/en/about-institute/",
        "supports": [
          "the Institute's present name, the N. I. Vavilov All-Russian Institute of Plant Genetic Resources (VIR)",
          "its present status as a Federal Research Center",
          "that the Institute continues to exist and to hold a plant genetic resources collection today"
        ],
        "doesNotSupport": [
          "any siege-period event, count or date",
          "any event in the game",
          "any figure for the collection's present size"
        ]
      }
    ],
    "noFurtherClaims": "No historical, biographical, chronological, quantitative or institutional claim appears in this package that is not on one of the lists above. If a later revision needs one, that is a source-certification dependency for the PMO, not an authoring decision."
  },
  "noGameRoute": {
    "rule": "Campaign 2 has no teacher level selector, no direct-launch mode, no injected state and no developer shortcut, and none will be built. Every assessed piece of evidence therefore exists in the learner packet, and the dossier is the stable assessment record in both routes.",
    "dossier": [
      "besieged-street",
      "keeper-testimony",
      "preservation-scan",
      "accession-ledger",
      "vavilov-record",
      "consumption-report"
    ],
    "requiredStrands": [
      {
        "id": "siege-context",
        "source": "besieged-street",
        "what": "reconstructed siege context"
      },
      {
        "id": "keeper-testimony",
        "source": "keeper-testimony",
        "what": "reconstructed keeper testimony"
      },
      {
        "id": "collection-condition",
        "source": "preservation-scan",
        "what": "reconstructed collection-condition evidence"
      },
      {
        "id": "accession-continuity",
        "source": "accession-ledger",
        "what": "reconstructed accession-continuity evidence"
      },
      {
        "id": "vavilov-fate",
        "source": "vavilov-record",
        "what": "reconstructed recovered-record evidence of Vavilov's fate"
      },
      {
        "id": "consumption-report",
        "source": "consumption-report",
        "what": "the reconstructed competing record under test"
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
      "reproducing the invented quotation attributed to Vavilov in the game",
      "requiring an unprinted line of gameplay for any assessed item"
    ],
    "teacherMustProvide": [
      "normal game route",
      "complete no-game route",
      "a mapping from each gameplay evidence object to its printed dossier card without ranking the routes"
    ]
  },
  "tasks": [
    {
      "id": "C09-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Case Vocabulary",
      "description": "Apply the seven terms the case cannot be performed without to the things and relationships they name.",
      "instructionalPurpose": "Establish only the seven terms the reasoning needs. The load-bearing pair is accession and collection continuity: an accession is the unit the ledger counts and the regeneration programme renews, and continuity is the property of the whole collection that Tasks 4 and 7 ask the learner to judge. The bank is exact-match because four of the terms are technical vocabulary a learner cannot be expected to generate from memory; the activity genuinely requires constrained exact recall.",
      "provenance": [
        "Curriculum-authored working definitions",
        "Terminology as used in the certified documented estate"
      ],
      "responseType": "seven exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared seven-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-seeds-01",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-seeds-02"
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
      "id": "C09-T2",
      "number": "2",
      "semanticLabel": "CONTINUITY TEST",
      "icon": "ph-diagnosis",
      "title": "Set a Continuity Test",
      "description": "State what evidence you would look for to decide whether a collection after a crisis is the same continuing collection as before it, rather than one rebuilt from scratch.",
      "instructionalPurpose": "Provisional thinking, taken after the reconstructed case records and deliberately before the documented sources arrive. It records where a learner starts and what they think continuity would look like. Because it is a starting point rather than a judgment, it is deliberately non-keyable, and the packet does not reveal the answer anywhere near it.",
      "provenance": [
        "The reconstructed case records",
        "Curriculum-authored prompt"
      ],
      "responseType": "two short constructed responses",
      "answerScope": "Any honest and specific kind of evidence, and any honest sign of rebuilding. There is no correct answer and none is keyed.",
      "pagePlacement": {
        "student": "student-seeds-03",
        "teacher": "teacher-guide-03",
        "answer": null,
        "accessible": "accessible-seeds-05"
      },
      "editions": [
        "student",
        "teacher",
        "accessible"
      ],
      "keyed": false,
      "nonKeyableReason": "The task asks what a learner would look for before the case has shown them what continuity evidence looks like. Keying it would convert a record of provisional thinking into a hidden multiple-choice item and would penalise the very gap the sequence is built to expose. The Teacher Guide carries the guidance for reading it diagnostically."
    },
    {
      "id": "C09-T3",
      "number": "3",
      "semanticLabel": "TWO TIMELINES",
      "icon": "ph-flow",
      "title": "Separate Vavilov's Timeline from the Siege",
      "description": "Read a two-strand chronology to place Vavilov's arrest and death on one strand and the Institute's siege on the other, and say what that separation establishes.",
      "instructionalPurpose": "The H2 operation, performed so that it becomes impossible to conflate Vavilov with the staff who kept the collection in Leningrad. Part A fixes the two dates the whole case turns on; Part B asks where Vavilov was during the siege winter; Part C asks who was actually keeping the collection and what they did; Part D asks the learner to separate the two in one sentence of their own. Every date on the figure is from a certified documented source, and the range runs through 1946 because the documented record of regeneration does.",
      "provenance": [
        "The Crop Trust account of Vavilov's life, arrest and death",
        "Loskutov's archival account of the Institute's wartime work",
        "Curriculum-original chronology figure"
      ],
      "responseType": "two compact dated responses and three short constructed responses",
      "answerScope": "The arrest year and the siege-closure date; Vavilov's documented whereabouts; the documented keepers and one documented action; one sentence separating the two.",
      "pagePlacement": {
        "student": "student-seeds-05",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-seeds-07"
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
      "id": "C09-T4",
      "number": "4",
      "semanticLabel": "CONTINUITY CHAIN",
      "icon": "ph-nodes",
      "title": "Trace the Collection Through Crisis",
      "description": "Complete a five-box continuity chain from the pre-crisis collection to the continuing collection, and explain which links preserved identity through movement, reproduction and loss.",
      "instructionalPurpose": "The H1 operation and the load-bearing task of the case. The figure draws movement, reproduction and loss as links in the chain rather than as breaks in it, and prints the rule the case exists to teach: continuity does not require physical immobility or perfect survival. Part A makes the learner name what the collection was, what stayed the same across three changes, and what it is now; Part B asks why those changes do not break continuity; Part C sets the game's immobility claim beside the documented record without letting either layer settle the other.",
      "provenance": [
        "Loskutov's archival account of the Institute's wartime work",
        "The Crop Trust account of the collection",
        "Curriculum-original continuity chain"
      ],
      "responseType": "five compact chain boxes and two short constructed responses",
      "answerScope": "What the collection was before; what preserved identity through the move, the reproduction and the loss; what it is after; why change is not a break; the documented contrast with the game's claim.",
      "pagePlacement": {
        "student": "student-seeds-06",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-seeds-08"
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
      "id": "C09-T5",
      "number": "5",
      "semanticLabel": "SOURCE COMPARISON",
      "icon": "ph-scales",
      "title": "Compare What the Sources Can Establish",
      "description": "For each of four sources, classify its status, state what it supports, state what it cannot establish, and say how it corroborates or qualifies another source.",
      "instructionalPurpose": "The H4 operation, and the place the central source-status distinction becomes explicit. The four rows are deliberately not equivalent: testimony written for the game can support reasoning inside the case and prove nothing outside it; the game's forensic and record evidence can settle the game's question and nothing else; the game's recovered record happens to agree with the documented record, which is corroboration running from the document to the claim and never the other way; and the documented record establishes the real history and nothing whatever about the game. The fourth column forces genuine source reasoning rather than clue transcription.",
      "provenance": [
        "All six reconstructed case records",
        "The three documented source cards, G, H and I"
      ],
      "responseType": "four compact status classifications and twelve matrix fields",
      "answerScope": "A correct status, a genuine contribution, a genuine limit and a genuine corroboration-or-qualification for each of the four rows.",
      "pagePlacement": {
        "student": "student-seeds-07",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-seeds-09"
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
      "id": "C09-T6",
      "number": "6",
      "semanticLabel": "TEST THE REPORT",
      "icon": "ph-wrench",
      "title": "Test the Consumption Report",
      "description": "Inside the game only, state what the Consumption Report claims under each of four tests and what the game's own evidence shows, reach a verdict, and say why appearance alone is not a test.",
      "instructionalPurpose": "The competing-record operation, kept explicitly inside the reconstructed layer. Four tests — chronology, collection condition, accession record and corroboration — each check one of the report's claims against one of the game's evidence objects. The organiser prints that the report's clean finish is a reason to look closer and not one of the four tests, because the misconception the Phase 1 audit flagged for this campaign is that neatness proves forgery.",
      "provenance": [
        "The six reconstructed case records",
        "Curriculum-authored organiser"
      ],
      "responseType": "eight organiser fields, one compact verdict and one short constructed response",
      "answerScope": "The report's claim and the game's contrary evidence under each test; a verdict; a statement that appearance is not one of the tests.",
      "pagePlacement": {
        "student": "student-seeds-07",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-seeds-09"
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
      "id": "C09-T7",
      "number": "7",
      "semanticLabel": "CONTINUITY JUDGMENT",
      "icon": "ph-scales",
      "title": "Make a Collection Continuity Judgment",
      "description": "Write a four-part Collection Continuity Judgment: what the historical evidence supports, the strongest links, what testimony and reconstructed evidence cannot establish, and why crop genetic diversity mattered beyond the siege.",
      "instructionalPurpose": "The culminating provenance and continuity product, and a judgment rather than a canonical CER. Four parts, each separately scored, so that neither the qualification nor the wider significance can be lost inside a confident paragraph. The Answer Key models the distinction between the verdict the game's evidence supports inside the case and the conclusion the documented record supports about the real collection.",
      "provenance": [
        "The three documented source cards, G, H and I",
        "Both curriculum figures",
        "The reconstructed dossier, for the in-world verdict only"
      ],
      "responseType": "one short judgment, one medium evidence response, one short qualification and one short significance response",
      "answerScope": "A qualified continuity judgment; the strongest documented links named; one thing testimony or reconstructed evidence cannot establish; why crop genetic diversity mattered beyond the siege.",
      "pagePlacement": {
        "student": "student-seeds-08",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-seeds-10"
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
      "id": "C09-T8",
      "number": "8",
      "semanticLabel": "TRANSFER EXIT",
      "icon": "ph-ticket",
      "title": "Transfer the Method",
      "description": "Name the evidence that would best demonstrate that a collection after a crisis is continuous with the pre-crisis collection rather than rebuilt from scratch, and explain why by method rather than by this case.",
      "instructionalPurpose": "Transfer, and deliberately about no particular collection. The prompt is the Phase 1 transfer concept in its own words. A learner who retells Leningrad has visibly failed to transfer, and the prompt says so before they start. The method is provenance and continuity reasoning: records that carry the same identities across the crisis, custodians who can be named, and regeneration that can be traced to the accessions it renewed.",
      "provenance": [
        "Curriculum-authored transfer prompt",
        "The method established across Tasks 3 to 7"
      ],
      "responseType": "two short judgments and one constructed explanation",
      "answerScope": "Two kinds of evidence that show continuity rather than replacement, each justified by method.",
      "pagePlacement": {
        "student": "student-seeds-08",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-04",
        "accessible": "accessible-seeds-10"
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
    "accession",
    "collection continuity",
    "ex situ conservation",
    "germplasm",
    "provenance",
    "seed bank",
    "siege"
  ],
  "vocabularyBankDecision": "Exact-match word bank used. Four of the seven terms are technical vocabulary a middle-school learner cannot be expected to generate from memory, so the activity genuinely requires constrained exact recall; the bank holds exactly the seven answers, one per statement, with no decoys, and the statements are printed in a fixed non-alphabetical order.",
  "caseSources": [
    {
      "id": "besieged-street",
      "displayLabel": "A · The besieged street",
      "creator": "The street outside the Institute, as the Archive reconstructs it (written for the game)",
      "period": "winter 1941 (reconstructed)",
      "sourceType": "in-world examination",
      "sourceOrigin": "reconstructed game examination",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "siege-context",
      "contribution": "Establishes, inside the case, what the word siege means on the ground: a silent bread queue, a ration notice cut again to a slice and a half, and artillery in the distance, a few streets from a building full of seed that no one ate.",
      "limitation": "Cannot establish any real ration, any real queue or any real day. It is a scene written for the game to set the stakes of the case, and it is not testimony that survives from 1941.",
      "gameCorrespondence": "Campaign 2, Level 2 — the street the investigator arrives on, which must be taken in before the vault opens.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3"
    },
    {
      "id": "keeper-testimony",
      "displayLabel": "B · Dr. Morozov, the surviving keeper",
      "creator": "Dr. Morozov, a keeper at the Institute (written for the game)",
      "period": "after the siege (reconstructed)",
      "sourceType": "in-world testimony",
      "sourceOrigin": "reconstructed game testimony",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "keeper-testimony",
      "contribution": "Establishes, inside the case, the keeper's account: the staff kept working, cataloguing, drying and testing germination in the cold; they did not eat the collection; a colleague died at his desk in January beside the rice, and the rice was still there in the morning; and a seed is not food, because a seed potato is every harvest from now on.",
      "limitation": "Cannot establish anything about a real person, a real death or a real count. Dr. Morozov was written for the game; he is not a surviving historical witness, and his account is not testimony that survives from the siege. The detail he gives about a colleague and the rice matches a documented death, which means the game drew on the record, not that the keeper is real.",
      "gameCorrespondence": "Campaign 2, Level 2 — the conversation with the keeper in the vault.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3"
    },
    {
      "id": "preservation-scan",
      "displayLabel": "C · The Archive's preservation scan",
      "creator": "The Archive's examination of the sampled shelves (written for the game)",
      "period": "after the siege (reconstructed)",
      "sourceType": "in-world examination",
      "sourceOrigin": "reconstructed game examination",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "collection-condition",
      "contribution": "Establishes, inside the case, the physical condition of the sampled collection: pre-war seals intact with no re-sealing, counts matching the catalogue of record, an aging profile continuous and in place through the siege winters, and no evidence of consumption.",
      "limitation": "Cannot establish the condition of any real shelf. The reading was invented with the case. Its closing line, that the seed never left the room, is the game's simplification of a history in which the real collection was divided, partly flown out, replanted and checked; the documented record is Source H, and the scan is not evidence about it.",
      "gameCorrespondence": "Campaign 2, Level 2 — the examination of the collection in the vault and the scan it offers.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 3"
    },
    {
      "id": "accession-ledger",
      "displayLabel": "D · The accession ledger and its cross-reference",
      "creator": "The Institute's accession ledger and the Archive's cross-reference of it (written for the game)",
      "period": "1940 to 1946 registers (reconstructed)",
      "sourceType": "in-world record",
      "sourceOrigin": "reconstructed game record",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "accession-continuity",
      "contribution": "Establishes, inside the case, a ledger dated straight through the siege winters with the handwriting thinning but never stopping, accession numbers continuous from the 1940 register to the 1946 register, no renumbering of the kind a re-collected bank would show, and the same custodians through 1942 with successors after.",
      "limitation": "Cannot establish what any real VIR register contains. It is an invented record, and its numbers, its hands and its cross-reference were written for the game. It is not a real accession record and the packet never presents it as one.",
      "gameCorrespondence": "Campaign 2, Level 2 — the ledger read in the office and the cross-reference run on it.",
      "fallbackCorrespondence": "Student page 2 · Accessible page 4"
    },
    {
      "id": "vavilov-record",
      "displayLabel": "E · The recovered Vavilov record",
      "creator": "A recovered presentation by N. I. Vavilov, with the Archive's annotation of his fate (written for the game)",
      "period": "presentation undated; annotation covers 1940 to 1943 (reconstructed)",
      "sourceType": "in-world recovered record and annotation",
      "sourceOrigin": "reconstructed game record",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "vavilov-fate",
      "contribution": "Establishes, inside the case, the Archive's annotation: Vavilov arrested in August 1940, before the siege began; imprisoned at Saratov; dead in prison in January 1943; not present at the besieged Institute in 1941 to 1942. It is the evidence the game uses to break the report's countersignature.",
      "limitation": "Cannot establish anything about the real Vavilov. The recovered presentation and its annotation were written for the game, and the words the game gives him are invented. That the annotation's dates agree with the documented record is corroboration running from Source G to the game's claim, never the other way.",
      "gameCorrespondence": "Campaign 2, Level 2 — the recovered record played in the office and the annotation pulled from it.",
      "fallbackCorrespondence": "Student page 3 · Accessible page 4"
    },
    {
      "id": "consumption-report",
      "displayLabel": "F · The Consumption Report",
      "creator": "A typed report found in the office (written for the game)",
      "period": "claims to cover December 1941 to March 1942 (reconstructed)",
      "sourceType": "in-world record",
      "sourceOrigin": "reconstructed game record",
      "evidentiaryStatus": "reconstructed",
      "evidenceLayer": "reconstructed",
      "evidenceStrand": "consumption-report",
      "contribution": "Supplies the claim the case exists to test: that under emergency authorisation the staff consumed the collections between December 1941 and March 1942, that the post-war bank was restocked from outside sources, and that the report was witnessed on site by Director N. I. Vavilov. Supplies also what can be seen in it: correct paper, correct typeface, aging ink, and a finish with no trace of the winter it claims to describe.",
      "limitation": "Cannot establish anything about the real Institute. It is an invented document, and everything inside the game that can test it is invented too. Its clean finish is a reason to look closer and is not one of the tests that break it.",
      "gameCorrespondence": "Campaign 2, Level 2 — the report read in the office, the competing record the investigator must reject.",
      "fallbackCorrespondence": "Student page 3 · Accessible page 4"
    },
    {
      "id": "crop-trust-vavilov",
      "displayLabel": "G · Vavilov, the collection and the siege",
      "creator": "Crop Trust, “Nikolai Vavilov: The Father of Genebanks”, croptrust.org",
      "period": "published account; covers 1887 to 1943",
      "sourceType": "international crop-conservation organisation's published account",
      "sourceOrigin": "real modern institutional documentation",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "documented",
      "contribution": "Vavilov's life and fate: born 1887; 115 expeditions to 64 countries on five continents between 1916 and 1933; the centres-of-origin theory of 1926; more than 250,000 seed samples, the world's largest repository of crop diversity; arrest in 1940 during a collecting expedition in western Ukraine; a death sentence commuted to twenty years; death in incarceration in Saratov on 26 January 1943, of starvation. And the siege: 900 days, during which the Institute's staff refused to eat the seeds even as they starved to death.",
      "limitation": "Gives no month for the arrest, no count of staff who died, no names of the wartime staff, and nothing about how the collection was moved, divided, evacuated or reproduced. It establishes nothing whatever about the game's case.",
      "gameCorrespondence": "No runtime counterpart. The game's recovered record is a fiction; this source is where the documented dates come from.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 5",
      "rights": "Crop Trust web resource. Cited and summarised, not reproduced."
    },
    {
      "id": "loskutov-wartime",
      "displayLabel": "H · The Institute's own wartime record",
      "creator": "I. G. Loskutov, “Wartime activities of the Vavilov Institute”, Proceedings on Applied Botany, Genetics and Breeding, 2021, 182(2):151–162, from the Institute's archives",
      "period": "published 2021; covers 1941 to 1946",
      "sourceType": "peer-reviewed archival history in the Institute's own journal",
      "sourceOrigin": "real published archival research",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "documented",
      "contribution": "What actually happened to the collection: a failed rail evacuation in August 1941; the collection divided into two lots, tied into packs and sealed in rooms inside the building, with an inventory made; part of the potato collection flown to Krasnoufimsk in November 1941; staff evacuated over Lake Ladoga from February 1942 carrying seed, and about 40,000 packages and a duplicate potato set flown out in March; more than 100,000 accessions kept at Krasnoufimsk; potatoes and about 200 cereal varieties re-sown in suburban fields under fire in 1942 and 1943 to renew their viability; named staff who died of hunger and exhaustion at their posts, more than twenty by the article's own count, among them the head of the rice section who died in his office beside thousands of packages of rice; losses of about 40,000 accessions over the war; the first staff back from Krasnoufimsk in February 1944; and a full check of the collection in 1946 with an emergency regeneration programme carried through.",
      "limitation": "Establishes nothing about the game's case, its keeper, its scan, its ledger or its report. It gives the arrest only as the event before a named director took office, not its month, and it gives the lifting of the siege only through the February 1944 return. Its count of the dead is one archival account's count; other published accounts count differently.",
      "gameCorrespondence": "No runtime counterpart. The level narrates intact seals and an unbroken ledger; this source is where the documented movement, reproduction, loss and regeneration come from.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 6",
      "rights": "Open-access journal article. Cited and summarised, not reproduced."
    },
    {
      "id": "vir-institute",
      "displayLabel": "I · The Institute today",
      "creator": "N. I. Vavilov All-Russian Institute of Plant Genetic Resources (VIR), vir.nw.ru",
      "period": "current",
      "sourceType": "institutional self-description",
      "sourceOrigin": "real modern institutional documentation",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "documented",
      "contribution": "The Institute's present name and status: the N. I. Vavilov All-Russian Institute of Plant Genetic Resources, a Federal Research Center, still holding a plant genetic resources collection today.",
      "limitation": "Establishes the institution's present identity and nothing about the siege. As consulted for this packet the page carried no siege narrative, no count and no date, and this packet does not borrow one from it.",
      "gameCorrespondence": "No runtime counterpart.",
      "fallbackCorrespondence": "Student page 4 · Accessible page 6",
      "rights": "Institutional web resource. Cited, not reproduced."
    },
    {
      "id": "chronology-figure",
      "displayLabel": "Figure — two timelines on one axis",
      "creator": "Curriculum",
      "period": "not applicable",
      "sourceType": "deterministic HTML and CSS schematic",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "contribution": "Sets Vavilov's strand beside the Institute's strand on one axis from 1887 to 1946, every row dated from Source G or Source H and every row printing its strand word, so that the arrest of 1940 visibly precedes the closing of the siege ring on 8 September 1941 and the death of 26 January 1943 visibly happens in Saratov while the Institute's staff are in Leningrad and Krasnoufimsk.",
      "limitation": "A schematic of order. Its intervals are not to scale, it draws no event the two documented sources do not date, and it is not the evidence; Sources G and H are.",
      "gameCorrespondence": "No runtime counterpart. Drawn for this packet from the documented sources.",
      "fallbackCorrespondence": "Student page 5 · Accessible page 7"
    },
    {
      "id": "continuity-figure",
      "displayLabel": "Figure — the collection-continuity chain",
      "creator": "Curriculum",
      "period": "not applicable",
      "sourceType": "deterministic HTML and CSS schematic",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "contribution": "Draws the documented collection as a chain of eight linked nodes from the pre-crisis collection to the continuing one, with the failed evacuation, the division and sealing, the partial evacuation to Krasnoufimsk, the reproduction under siege, the losses and the post-siege check and regeneration all drawn as links, each link labelled with what preserved identity across it, and prints that continuity does not require physical immobility or perfect survival.",
      "limitation": "A schematic of relationships. Nothing on it is to scale, no count may be read from it beyond the ones it prints from Source H, and it is not the evidence; Source H is.",
      "gameCorrespondence": "No runtime counterpart. The level narrates seed that never left the room; this figure is built from the documented record instead.",
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
        "task": "C09-T1",
        "id": "vocabulary",
        "obligation": "Place all seven terms.",
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
        "task": "C09-T2",
        "id": "continuity-evidence",
        "obligation": "Name one kind of evidence you would look for to decide whether a collection is continuous.",
        "student": [
          "t2-evidence"
        ],
        "accessible": [
          "a2-evidence"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T2",
        "id": "rebuilt-sign",
        "obligation": "Name one sign that would tell you the collection had been rebuilt instead.",
        "student": [
          "t2-rebuilt"
        ],
        "accessible": [
          "a2-rebuilt"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T3",
        "id": "two-dates",
        "obligation": "Give the year of Vavilov's arrest and the date the siege ring closed.",
        "student": [
          "t3-arrest",
          "t3-siege"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t3-dates-supplied"
      },
      {
        "task": "C09-T3",
        "id": "vavilov-whereabouts",
        "obligation": "Say where Vavilov was during the siege winter and what that establishes.",
        "student": [
          "t3-where"
        ],
        "accessible": [
          "a3-where"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T3",
        "id": "documented-keepers",
        "obligation": "Say who kept the collection in Leningrad and name one documented thing they did.",
        "student": [
          "t3-keepers"
        ],
        "accessible": [
          "a3-keepers"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T3",
        "id": "separate-sentence",
        "obligation": "Separate Vavilov from the siege staff in one sentence.",
        "student": [
          "t3-separate"
        ],
        "accessible": [
          "a3-separate"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T4",
        "id": "chain-ends",
        "obligation": "Name what the collection was before the crisis and what it is after.",
        "student": [
          "t4-node-1",
          "t4-node-5"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t4-ends-supplied"
      },
      {
        "task": "C09-T4",
        "id": "chain-links",
        "obligation": "For the move, the reproduction and the loss, say what preserved the collection's identity.",
        "student": [
          "t4-node-2",
          "t4-node-3",
          "t4-node-4"
        ],
        "accessible": [
          "a4-node-2",
          "a4-node-3",
          "a4-node-4"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T4",
        "id": "change-not-break",
        "obligation": "Explain why movement, reproduction and partial loss do not break continuity.",
        "student": [
          "t4-why"
        ],
        "accessible": [
          "a4-why"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T4",
        "id": "scan-contrast",
        "obligation": "Set the game's immobility claim beside the documented record without letting either settle the other.",
        "student": [
          "t4-scan"
        ],
        "accessible": [
          "a4-scan"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T5",
        "id": "status-classification",
        "obligation": "Classify the status of each of the four sources.",
        "student": [
          "t5-r1-status",
          "t5-r2-status",
          "t5-r3-status",
          "t5-r4-status"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t5-status-prelabeled"
      },
      {
        "task": "C09-T5",
        "id": "row-keeper",
        "obligation": "Weigh the keeper's testimony.",
        "student": [
          "t5-r1-supports",
          "t5-r1-cannot",
          "t5-r1-corrob"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t5-modelled-row"
      },
      {
        "task": "C09-T5",
        "id": "row-scan-ledger",
        "obligation": "Weigh the Archive's scan and ledger cross-reference.",
        "student": [
          "t5-r2-supports",
          "t5-r2-cannot",
          "t5-r2-corrob"
        ],
        "accessible": [
          "a5-r2-supports",
          "a5-r2-cannot",
          "a5-r2-corrob"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T5",
        "id": "row-vavilov-record",
        "obligation": "Weigh the recovered Vavilov record.",
        "student": [
          "t5-r3-supports",
          "t5-r3-cannot",
          "t5-r3-corrob"
        ],
        "accessible": [
          "a5-r3-supports",
          "a5-r3-cannot",
          "a5-r3-corrob"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T5",
        "id": "row-documented",
        "obligation": "Weigh the documented record.",
        "student": [
          "t5-r4-supports",
          "t5-r4-cannot",
          "t5-r4-corrob"
        ],
        "accessible": [
          "a5-r4-supports",
          "a5-r4-cannot",
          "a5-r4-corrob"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T6",
        "id": "report-claims",
        "obligation": "State the report's claim under each of the four tests.",
        "student": [
          "t6-r1-claim",
          "t6-r2-claim",
          "t6-r3-claim",
          "t6-r4-claim"
        ],
        "accessible": [],
        "differenceClass": "declared-reduction",
        "governedBy": "t6-claims-supplied"
      },
      {
        "task": "C09-T6",
        "id": "game-evidence",
        "obligation": "State what the game's evidence shows under each of the four tests.",
        "student": [
          "t6-r1-shows",
          "t6-r2-shows",
          "t6-r3-shows",
          "t6-r4-shows"
        ],
        "accessible": [
          "a6-r1-shows",
          "a6-r2-shows",
          "a6-r3-shows",
          "a6-r4-shows"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T6",
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
        "task": "C09-T6",
        "id": "appearance",
        "obligation": "Say why the report's clean finish is not one of the tests.",
        "student": [
          "t6-appearance"
        ],
        "accessible": [
          "a6-appearance"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T7",
        "id": "judgment",
        "obligation": "State what the historical evidence supports about preservation and continuity.",
        "student": [
          "t7-judgment"
        ],
        "accessible": [
          "a7-judgment"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T7",
        "id": "strongest-evidence",
        "obligation": "Name the evidence that provides the strongest links in the chain.",
        "student": [
          "t7-evidence"
        ],
        "accessible": [
          "a7-evidence"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T7",
        "id": "qualification",
        "obligation": "State what testimony or reconstructed evidence cannot establish.",
        "student": [
          "t7-limit"
        ],
        "accessible": [
          "a7-limit"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T7",
        "id": "why-it-mattered",
        "obligation": "Explain why maintaining crop genetic diversity mattered beyond the siege.",
        "student": [
          "t7-why"
        ],
        "accessible": [
          "a7-why"
        ],
        "differenceClass": "parity"
      },
      {
        "task": "C09-T8",
        "id": "transfer-evidence",
        "obligation": "Name the evidence that would best show continuity rather than rebuilding.",
        "student": [
          "t8-evidence-1",
          "t8-evidence-2"
        ],
        "accessible": [
          "a8-choice"
        ],
        "differenceClass": "declared-reduction",
        "governedBy": "t8-bounded-choice"
      },
      {
        "task": "C09-T8",
        "id": "transfer-explanation",
        "obligation": "Explain the choice by method rather than by this case.",
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
      "id": "t3-dates-supplied",
      "task": "C09-T3",
      "what": "Part A is supplied complete as a worked example: the arrest year and the siege-closure date are read off the figure for the learner.",
      "effect": "Accessible answers three parts of Task 3; Student answers four.",
      "whyNotALeak": "The two dates are printed on the figure in both editions, so supplying them removes transcription rather than reasoning. The separation the task assesses — where Vavilov was, who actually kept the collection, and one sentence keeping the two apart — is answered independently in both editions.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t4-ends-supplied",
      "task": "C09-T4",
      "what": "The first and last boxes of the continuity chain — the pre-crisis collection and the continuing collection — are supplied as GIVEN.",
      "effect": "Accessible completes three chain boxes; Student completes five.",
      "whyNotALeak": "The ends of the chain are the two nodes the figure already names in full. The three middle boxes, which ask what preserved identity through the move, the reproduction and the loss, are the reasoning the task assesses, and they are answered independently in both editions, as are Parts B and C.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t5-status-prelabeled",
      "task": "C09-T5",
      "what": "The status of each of the four sources is printed in the matrix rather than classified by the learner.",
      "effect": "Four compact classifications are removed from the Accessible matrix.",
      "whyNotALeak": "Every source card already prints its SOURCE STATUS line in both editions, so the classification is a transcription the learner has performed nine times by the time the matrix arrives. The three judgment columns in every remaining row are untouched.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t5-modelled-row",
      "task": "C09-T5",
      "what": "The keeper-testimony row is supplied complete in all three judgment cells as a worked example.",
      "effect": "Accessible completes nine matrix fields; Student completes sixteen.",
      "whyNotALeak": "The modelled row is the one the source-status notice has already stated in full: testimony written for the game supports reasoning inside the case and proves nothing outside it. The three rows that carry the evidentiary reasoning the case turns on — the game's forensic and record evidence, the recovered record that the documented record corroborates, and the documented record itself — are worked independently in both editions.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t6-claims-supplied",
      "task": "C09-T6",
      "what": "The report's claim under each of the four tests is printed in the organiser rather than copied out by the learner.",
      "effect": "Accessible completes four evidence fields, a verdict and an appearance response; Student also writes the four claims.",
      "whyNotALeak": "The claims are on the report's card in both editions, so supplying them removes copying. What the game's evidence shows under each test, the verdict, and the statement that appearance is not a test are the reasoning, and they are answered independently in both editions.",
      "declaredIn": [
        "teacher",
        "answer"
      ]
    },
    {
      "id": "t8-bounded-choice",
      "task": "C09-T8",
      "what": "The two open evidence judgments are offered as one bounded choice from four printed kinds of evidence, followed by the same open explanation.",
      "effect": "Accessible records one choice and one explanation; Student writes two kinds of evidence and one explanation.",
      "whyNotALeak": "Two of the four options are sound and two are weaker than they look, so the choice still requires the judgment the task assesses, and the explanation that justifies it by method is identical in both editions.",
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
      "rule": "Every printable proposition in every role is scanned against the four closed negative classes. Internal punctuation is not a safety boundary.",
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
          "vavilovPresentAtSiege",
          "nothingMovedAsHistory",
          "zeroLossAsHistory",
          "cleanProvesForged",
          "settledDeathCount"
        ]
      },
      {
        "id": "answer-key-floor",
        "roles": [
          "answer"
        ],
        "purpose": "The Answer Key must be able to state the wording it refuses at every level.",
        "allowedConcepts": [
          "vavilovPresentAtSiege",
          "nothingMovedAsHistory",
          "zeroLossAsHistory",
          "cleanProvesForged",
          "settledDeathCount"
        ]
      }
    ],
    "structuralExemptSelectors": [
      {
        "selector": "[data-evidence-layer='reconstructed']",
        "allowedConcepts": [
          "nothingMovedAsHistory",
          "zeroLossAsHistory",
          "vavilovPresentAtSiege"
        ],
        "why": "A reconstructed evidence object is the game layer. The game's scan says the seed never left the room and the game's report claims a countersignature by Vavilov; the card has to print what the game says in order for the learner to test it, and the card's own status line is what keeps it from being read as history."
      },
      {
        "selector": "[data-game-claim]",
        "allowedConcepts": [
          "nothingMovedAsHistory",
          "zeroLossAsHistory",
          "vavilovPresentAtSiege"
        ],
        "why": "A marked in-game quotation inside a task that tests it. Quoting a claim in order to test it is not asserting it, and the marker is what makes the quotation legible as a quotation to the validator as well as to the learner."
      }
    ]
  },
  "figureContract": {
    "rule": "Both figures are deterministic HTML and CSS, carry a printed SOURCE STATUS line and a printed basis line, and carry accessibility text held to the same factual contracts as the visible drawing. No imagery of any kind is used anywhere in this package apart from the shared institutional insignia.",
    "figures": [
      {
        "id": "two-timelines",
        "selector": "[data-chronology-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "H2 chronology, two strands on one axis",
        "requiresPrintedText": [
          "VAVILOV",
          "INSTITUTE",
          "1940",
          "8 September 1941",
          "26 January 1943",
          "Saratov",
          "Krasnoufimsk",
          "1946"
        ],
        "requiresCaptionTerms": [
          "BASED ON",
          "CROP TRUST",
          "LOSKUTOV",
          "NOT TO SCALE"
        ],
        "requiresAltConcepts": [
          "two strands",
          "1940",
          "arrested",
          "8 September 1941",
          "26 January 1943",
          "Saratov",
          "Krasnoufimsk",
          "1946"
        ],
        "prohibitedPatterns": [
          {
            "id": "august-1940-as-documented",
            "regex": "\\baugust\\s+1940\\b",
            "why": "The month of the arrest is the game's annotation, not a claim the certified documented estate supports."
          },
          {
            "id": "vavilov-in-leningrad-after-1940",
            "regex": "\\bvavilov\\b[^.!?]{0,40}\\b(?:in leningrad|at the institute)\\b[^.!?]{0,20}\\b(?:194[1-4])\\b",
            "why": "The figure exists to keep Vavilov off the Institute's strand after 1940."
          }
        ]
      },
      {
        "id": "continuity-chain",
        "selector": "[data-continuity-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "family": "H1 accession and provenance chain",
        "requiresPrintedText": [
          "PRE-CRISIS COLLECTION",
          "FAILED RAIL EVACUATION",
          "DIVIDED AND SEALED",
          "PARTIAL EVACUATION",
          "REPRODUCTION UNDER SIEGE",
          "LOSSES",
          "CHECK AND REGENERATION",
          "CONTINUING COLLECTION"
        ],
        "requiresCaptionTerms": [
          "BASED ON",
          "LOSKUTOV",
          "CROP TRUST",
          "RECONSTRUCTION",
          "NOT TO SCALE"
        ],
        "requiresContinuityRule": "does not require physical immobility or perfect survival",
        "requiresAltConcepts": [
          "pre-crisis collection",
          "failed rail evacuation",
          "divided and sealed",
          "partial evacuation",
          "reproduction under siege",
          "losses",
          "check and regeneration",
          "continuing collection",
          "does not require physical immobility or perfect survival"
        ],
        "prohibitedPatterns": [
          {
            "id": "never-left-as-history",
            "regex": "\\bnever left\\b",
            "why": "The figure draws movement; its accessibility text may not state the game's immobility claim as history."
          },
          {
            "id": "zero-loss",
            "regex": "\\b(?:nothing was lost|no losses|without loss|no accession was lost)\\b",
            "why": "The figure carries a LOSSES node because the documented record does."
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
      "C3 D2.His.1.6-8",
      "C3 D2.His.2.6-8",
      "C3 D3.1.6-8",
      "C3 D3.2.6-8",
      "CCSS RH.6-8.1",
      "CCSS RH.6-8.7",
      "CCSS WHST.6-8.1"
    ],
    "supporting": [
      "CCSS RH.6-8.9",
      "CCSS WHST.6-8.2"
    ],
    "contextual": [
      "crop genetic diversity / germplasm / ex situ conservation"
    ],
    "ngss": "No NGSS performance expectation is claimed at any status. The case touches crop genetic diversity, germplasm and ex situ conservation, and those are held as contextual science content rather than as a science standard, because no task asks a learner to construct a scientific explanation, develop or use a model of a natural system, or analyse data. The tasks measure chronological reasoning, source evaluation, provenance and continuity reasoning, and argument from evidence.",
    "rationale": "Task-first alignment under the PMO partition. D2.His.1 is measured by Task 3's two-strand chronology and by Task 4's placement of events in a chain; D2.His.2 by Task 4's reasoning about continuity and change across the crisis; D3.1 by Task 5's status classification and by Task 3's and Task 4's use of documented sources; D3.2 by Task 5's contribution-and-limitation columns and Task 6's corroboration test; RH.6-8.1 by the citation of specific documented evidence in Tasks 4, 5 and 7; RH.6-8.7 by the integration of the two figures with the written sources in Tasks 3, 4 and 7; WHST.6-8.1 by Task 7's four-part judgment, which is an argument from evidence with an explicit qualification. RH.6-8.9 is supporting because Tasks 5 and 6 set reconstructed testimony beside documented archival research and require the learner to say what each can carry, which practises the relationship a primary-versus-secondary analysis rests on without performing it. WHST.6-8.2 is supporting because Task 4 Part B and Task 7 Part D are short explanatory products scored for reasoning rather than craft. The contextual entry names the science content the case uses and claims no performance expectation for it."
  }
};
