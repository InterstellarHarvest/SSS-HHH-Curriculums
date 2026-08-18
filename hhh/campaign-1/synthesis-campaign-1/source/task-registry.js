window.HHH_C1_SYNTHESIS_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C1-SYNTHESIS",
  "runtimeId": "L7",
  "instructionalType": "SYNTHESIS",
  "title": "The Temporal Agricultural Archive",
  "displayLabel": "Campaign 1 Synthesis",
  "version": "0.1",
  "status": "VALIDATION_BUILD",
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "editorShell": "1.0",
  "gameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
  "auditBaseline": "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md",
  "staticContentInventory": "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json",
  "blueprint": "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
  "roles": {
    "student": 7,
    "teacher": 7,
    "answer": 5,
    "accessible": 11
  },
  "unitKind": {
    "instructionalType": "SYNTHESIS",
    "rule": "This unit is the Campaign 1 Synthesis. It is not a numbered Core Case, it is not Case 07, and no role may present it as one. Campaign 2 Core Case 07 - The Audit - is a separate later unit.",
    "prohibitedIdentities": [
      "CORE_CASE",
      "Case 07",
      "Case 7",
      "HHH-C2-CASE07"
    ],
    "displayLabel": "Campaign 1 Synthesis",
    "contextualSubtitle": "Campaign 1 Synthesis · The Long Yield",
    "subtitleProvenance": "The Long Yield is the runtime tagline of Campaign 1 Level 7 and the title of its finale card. It is carried forward as the unit's contextual subtitle rather than invented for the packet."
  },
  "learningGoal": "Students will use evidence from Campaign 1 to trace continuity and change in agricultural knowledge, systems, and record preservation across time, explaining how knowledge was preserved, transferred, tested, or revised and why a correct local mechanism may still be insufficient to explain a broader historical outcome.",
  "guidingQuestion": "How does agricultural knowledge change as people preserve, transfer, test, and revise it—and why does the historical record matter?",
  "culminatingProduct": "Historical continuity/change synthesis across Campaign 1. The learner must name one continuity and one change, support both with specific evidence from at least two earlier cases, carry at least one source-status, evidence-limit or causal qualification, and explain why preservation and historical memory matter. Canonical CER is deliberately not used: the product has several load-bearing parts that a single claim cannot hold at once, and the Blueprint names a continuity/change synthesis rather than a claim-evidence-reasoning argument as this unit's product. See cerDecision.",
  "cerDecision": {
    "used": false,
    "rule": "The canonical Claim/Evidence/Reasoning component is not rendered in any role of this unit, and no role prints a CLAIM / EVIDENCE / REASONING structure.",
    "why": "The Blueprint's culminating-product policy names continuity/change synthesis (§9.5) for cross-case reasoning about what changed, what persisted and why, and names CER (§9.6) only where its structure genuinely supports the case. The Archive Synthesis carries a continuity, a change, evidence from two or more cases, a qualification and a statement about historical memory. A CER frame would have to elect one of those as the claim and demote the rest to support, which is precisely the flattening this unit exists to refuse. Evidence and reasoning remain assessed - through the Archive Synthesis and through rubric criteria 2 and 4 - rather than through a CER component.",
    "prohibitedSelectors": [
      ".canonical-cer",
      "[data-cer-contract]",
      ".cer-stack",
      ".canonical-cer-box",
      ".canonical-cer-label"
    ]
  },
  "tasks": [
    {
      "id": "SYN-T1",
      "number": "1",
      "semanticLabel": "CAMPAIGN RECORD",
      "icon": "ph-book",
      "title": "Read the Campaign Record",
      "description": "Read the six evidence recap cards for Campaign 1 Cases 01 to 06 and keep them to hand; every later task is answered from them.",
      "instructionalPurpose": "This task exists to remove perfect-memory dependence. A campaign synthesis that asks a learner to recall six investigations they may have finished weeks ago assesses memory rather than historical reasoning. The six cards carry the setting, the change, one or two certified evidence points, what that evidence supports, what it does not establish alone, its source status and its archive thread - which is exactly the material Tasks 2 to 6 require and nothing more. It is reference and orientation, and it is deliberately not keyed.",
      "responseType": "reference; no response is collected",
      "answerScope": "None. Task 1 is orientation and is not keyed.",
      "evidencePointers": [
        "recap-01",
        "recap-02",
        "recap-03",
        "recap-04",
        "recap-05",
        "recap-06"
      ],
      "pagePlacement": {
        "student": "student-synthesis-01",
        "teacher": "teacher-guide-03",
        "accessible": "accessible-synthesis-01"
      },
      "editions": [
        "student",
        "teacher",
        "accessible"
      ],
      "keyed": false
    },
    {
      "id": "SYN-T2",
      "number": "2",
      "semanticLabel": "CROSS-CASE CHRONOLOGY",
      "icon": "ph-flow",
      "title": "Trace the Long Yield",
      "description": "Use the cross-case chronology rail to name one meaningful continuity and one meaningful change across Campaign 1, each with the cases it rests on.",
      "instructionalPurpose": "Family H2 and H6. The rail supplies the dates and the case identities so that the reasoning operation is comparison rather than recall. A continuity and a change are the two halves of the same historical judgment: a learner who can only find change reads the campaign as a march of progress, and a learner who can only find continuity misses that anything happened. Both must name the cases they rest on, because a continuity asserted without cases is a slogan.",
      "responseType": "two short constructed responses, each with a case citation",
      "answerScope": "One meaningful continuity with the cases it rests on, and one meaningful change with the cases it rests on.",
      "evidencePointers": [
        "chronology-rail"
      ],
      "pagePlacement": {
        "student": "student-synthesis-03",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-synthesis-05"
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
      "id": "SYN-T3",
      "number": "3",
      "semanticLabel": "CONTINUITY AND CHANGE",
      "icon": "ph-scales",
      "title": "Compare Continuity and Change",
      "description": "Choose one case from Cases 01 to 03 and one from Cases 04 to 06, then compare them on knowledge or practice, what was preserved or transferred, what changed, and an important consequence - with specific evidence and one qualification.",
      "instructionalPurpose": "Family H6, and the task the whole unit turns on. The early/late split is structural: it guarantees the comparison crosses a genuine span of time rather than pairing two adjacent cases, and it does so without prescribing which pair. Six separate written comparisons would be repetition rather than reasoning, so the depth goes into one pair. The final two rows are what stop the organizer from becoming a worksheet of assertions - the evidence row makes the comparison answerable to the record, and the qualification row makes it honest about the record's limits.",
      "responseType": "two case selections plus a ten-field comparison organizer",
      "answerScope": "One early case and one late case; for each, the agricultural knowledge, practice or system, what was preserved or transferred, what changed, and an important consequence; then specific supporting evidence drawn from both cases and one important qualification or evidence limit.",
      "evidencePointers": [
        "recap-01",
        "recap-02",
        "recap-03",
        "recap-04",
        "recap-05",
        "recap-06"
      ],
      "pagePlacement": {
        "student": "student-synthesis-04",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-synthesis-06"
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
      "id": "SYN-T4",
      "number": "4",
      "semanticLabel": "MECHANISM AND EXPLANATION",
      "icon": "ph-diagnosis",
      "title": "Test the Limits of a Correct Mechanism",
      "description": "Choose two of Cases 02, 03, 05 and 06, and for each organize the local mechanism, what it explains, what it does not explain alone, and the additional context or evidence needed.",
      "instructionalPurpose": "The recurring Campaign 1 lesson, made explicit: a correct local mechanism is not automatically a complete explanation of a broader historical outcome. Every one of the four supplied cases has a mechanism that is genuinely correct at its own scale and genuinely insufficient at the scale of the historical outcome - salt in a field against the decline of a society, a pathogen against a mortality figure, wind erosion against a decade, a failed subsystem against a public verdict. Cases 01 and 04 are deliberately excluded rather than forced into the frame for symmetry: Case 01's change is cumulative rather than mechanism-and-outcome, and Case 04's reasoning is about attribution across kinds of work rather than about a mechanism falling short.",
      "responseType": "two case selections plus two four-field mechanism organizers",
      "answerScope": "For each of two chosen cases: the local mechanism, what it explains, what it does not explain alone, and what additional context or evidence would be needed.",
      "evidencePointers": [
        "recap-02",
        "recap-03",
        "recap-05",
        "recap-06"
      ],
      "pagePlacement": {
        "student": "student-synthesis-05",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-03",
        "accessible": "accessible-synthesis-08"
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
      "id": "SYN-T5",
      "number": "5",
      "semanticLabel": "ARCHIVE SYNTHESIS",
      "icon": "ph-nodes",
      "title": "Write the Archive Synthesis",
      "description": "Write the campaign synthesis: one continuity, one change, specific evidence from at least two cases, at least one qualification, and why preservation and historical memory matter.",
      "instructionalPurpose": "The culminating product. It is a historical continuity/change synthesis, not a claim-evidence-reasoning argument, and the difference is deliberate: the learner is explaining how agricultural knowledge moved across twelve thousand years and what the record made possible, which is an explanation with several load-bearing parts rather than one claim with support beneath it. The qualification requirement is the unit's spine - every case in Campaign 1 has a boundary its evidence cannot cross, and a synthesis that reports six findings without one of those boundaries has learned the content and missed the discipline.",
      "responseType": "one extended constructed response of roughly two compact paragraphs",
      "answerScope": "One continuity; one change; specific evidence from at least two cases; at least one source-status, evidence-limit or causal qualification; and an explanation of why preservation and historical memory matter. Roughly six to eight substantive sentences. Sentence count is not itself scored.",
      "evidencePointers": [
        "chronology-rail",
        "recap-01",
        "recap-02",
        "recap-03",
        "recap-04",
        "recap-05",
        "recap-06"
      ],
      "pagePlacement": {
        "student": "student-synthesis-06",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-04",
        "accessible": "accessible-synthesis-10"
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
      "id": "SYN-T6",
      "number": "6",
      "semanticLabel": "PRESERVATION TRANSFER",
      "icon": "ph-ticket",
      "title": "What Should the Archive Preserve?",
      "description": "Choose one Campaign 1 case and explain what later readers could misunderstand if one critical piece of evidence, qualification, or source relationship disappeared from the record.",
      "instructionalPurpose": "Transfer, and the exit. It turns Archive Orientation's methodological rule - preservation does not equal historical verification - into a counterfactual the learner has to run for themselves. Naming what would be lost requires knowing what a specific piece of evidence was carrying, which is a harder and more diagnostic question than naming what the evidence shows. It is also where a learner who has treated the qualifications as decoration is most visible, because a missing qualification is exactly the kind of loss that leaves a confident and wrong record behind.",
      "responseType": "one case selection plus one short constructed response",
      "answerScope": "One Campaign 1 case, the specific piece of evidence, qualification or source relationship that disappears, and what later readers could then misunderstand.",
      "evidencePointers": [
        "recap-01",
        "recap-02",
        "recap-03",
        "recap-04",
        "recap-05",
        "recap-06"
      ],
      "pagePlacement": {
        "student": "student-synthesis-07",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-05",
        "accessible": "accessible-synthesis-11"
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
  "caseRecaps": [
    {
      "id": "recap-01",
      "case": "HHH-C1-CASE01",
      "label": "Case 01",
      "title": "The Fertile Crescent",
      "setting": "Southwest Asia · the scene is set about 9,700 BCE",
      "span": "about 9,750 – 6,350 BCE",
      "archiveThread": "PRESERVE",
      "archiveThreadGloss": "knowledge carried forward by saving and replanting seed",
      "change": "People cultivated grain that was still the wild kind for centuries. Domestication — a lasting change across the whole plant population — arrived much later, and it arrived cumulatively, over many generations and many regions.",
      "evidence": [
        "Charred grain from four excavated sites in northern Syria and southeastern Turkey: 9,844 spikelets examined; 804 identifiable well enough to sort into wild type or domesticated type. In those 804, early deposits are almost entirely wild type and later ones hold more and more non-shattering grain.",
        "A site-by-site chronology: people are cultivating wild-type grain from about 9,750 BCE, and non-shattering grain only passes a tenth of the chaff around 8,750–8,250 BCE in southern Syria — and as late as about 6,350 BCE in other regions."
      ],
      "supports": "That the change was cumulative and slow. Repeated harvesting, seed saving and replanting acted as selection, keeping alive a trait that could not survive without people, and the trait spread across generations rather than in a season.",
      "doesNotEstablishAlone": "It identifies no first person, no first field and no starting date, and the change did not run on one clock. Cultivation is not domestication: people were growing grain on purpose long before the plant population changed.",
      "sourceStatus": "Charred grain: documented / observed. The multi-site chronology: inferred. How the change happened: debated. The Archive’s field scene, the woman and her words: reconstructed.",
      "railEntry": "Repeated selection, seed saving and replanting. Domesticated-type grain appears at different times in different regions."
    },
    {
      "id": "recap-02",
      "case": "HHH-C1-CASE02",
      "label": "Case 02",
      "title": "Sumer",
      "setting": "The southern Mesopotamian plain · the scene is set about 2000 BCE",
      "span": "scene set about 2000 BCE",
      "archiveThread": "RECORD",
      "archiveThreadGloss": "a record naming a cause the ground does not support",
      "change": "Irrigation without drainage, on a flat plain with a shallow water table, can raise the salt in a field until crops suffer.",
      "evidence": [
        "The mechanism (FAO): irrigation water carries dissolved salt; a water table within a few metres of the surface delivers salt upward; evaporation removes the water and not the salt; only downward flow with drainage carries salt away.",
        "Measured salt tolerance (FAO, after Maas and Grattan 1999): barley keeps full grain yield to 8.0 dS/m and wheat to 6.0 dS/m. These are modern measurements on modern varieties, and both grains are less tolerant while germinating."
      ],
      "supports": "The field-scale salinization mechanism: where water leaves and salt does not, salt accumulates, and a more tolerant grain outlasts a less tolerant one in the same ground.",
      "doesNotEstablishAlone": "How much soil salt contributed to the wider decline of southern Mesopotamian society is argued among scholars, and this evidence does not settle it. The barley-replacing-wheat reading of the tablets (Jacobsen and Adams 1958) was challenged by Powell (1985), and administrative tablets are not agricultural statistics. Other pressures are argued for the same centuries.",
      "sourceStatus": "The mechanism and the tolerance values: documented. The reading of the tablets: debated / uncertain. The soil cross-sections: modeled. The Archive’s scenes at the fields and the scribes’ room: reconstructed.",
      "railEntry": "Irrigation without drainage on a flat plain. Salt accumulates where the water leaves and the salt does not."
    },
    {
      "id": "recap-03",
      "case": "HHH-C1-CASE03",
      "label": "Case 03",
      "title": "County Cork",
      "setting": "Ireland · County Cork · the scene is set in 1845",
      "span": "1845 – 1852",
      "archiveThread": "RESPOND",
      "archiveThreadGloss": "what a record of relief does and does not show",
      "change": "Phytophthora infestans — late blight — destroyed the potato crop. About a million people died, and the deaths followed from that failure meeting conditions that were already in place.",
      "evidence": [
        "The same blight in two countries (Ronsijn and Vanhaute): Belgium lost almost 90% of its potato harvest in 1845; Ireland lost about 30% that year and over 75% in 1846. Belgium recorded over 40,000 famine-related deaths and mortality 30–40% above normal; Ireland’s mortality ran at about three times normal and about a million people died.",
        "Nicholas Cummins, a magistrate of Cork, travelled to Skibbereen in December 1846 and wrote to the Duke of Wellington about what he found. The letter was published in The Times on 24 December 1846."
      ],
      "supports": "That the pathogen explains the crop failure, and that the size of the crop loss did not set the size of the death toll — Belgium lost far more of its harvest and lost far fewer of its people.",
      "doesNotEstablishAlone": "It does not rank the conditions that made the difference. Deep dependence among the poorest, land and labour arrangements that left households without money or security, unequal access to the food that remained, and the scale and timing of relief all contributed. Blight alone did not cause the famine, and no single condition — biological or political — was the whole cause.",
      "sourceStatus": "The blight science, the comparison and the Cummins letter: documented. The argument about food exports: debated / uncertain. The causes map: modeled. The Archive’s scenes at the field, the cottage and the road: reconstructed.",
      "railEntry": "Late blight destroys the potato crop. About a million deaths follow from the failure meeting conditions already in place."
    },
    {
      "id": "recap-04",
      "case": "HHH-C1-CASE04",
      "label": "Case 04",
      "title": "Karlsruhe",
      "setting": "Karlsruhe and Oppau, Germany",
      "span": "1908 – 1913",
      "archiveThread": "TRANSFER",
      "archiveThreadGloss": "from a bench result to a working plant, and the record of who did what",
      "change": "Nitrogen was taken from the air and combined into ammonia — first as a laboratory demonstration, and then, several distinct problems later, as an industrial process.",
      "evidence": [
        "The 1909 Karlsruhe demonstration, with the apparatus Le Rossignol designed and an osmium catalyst. Published accounts differ on the exact date: Travis (2015) gives 1 July 1909, Appl (1997) gives April 1909. The year is documented; no exact date is settled.",
        "The dated sequence that followed: Haber and Le Rossignol file the ammonia patent on 13 August 1909; Mittasch’s screening at BASF finds promoted iron in 1910; Bosch and Lappe answer the hydrogen embrittlement of the steel with a double-walled converter in February 1911; Oppau begins production on 9 September 1913."
      ],
      "supports": "That a laboratory result is not an industrial process. Making it workable took a catalyst that could be made in quantity, steel that survived hydrogen at pressure, and the recycling of unconverted gas.",
      "doesNotEstablishAlone": "It does not license crediting one person. Haber directed the laboratory programme and introduced the recycle principle; Le Rossignol designed the ammonia apparatus and invented the high-pressure valve; Mittasch found the catalyst; Bosch diagnosed the steel failure and led the works. Laboratory demonstration and industrial engineering are distinct, and both are credited.",
      "sourceStatus": "The patent, Travis and Appl: documented. The exact demonstration date: debated / uncertain. The process loop and the tradeoff panel: modeled. The Archive’s scenes at the bench: reconstructed.",
      "railEntry": "Ammonia synthesis moves from a laboratory demonstration at Karlsruhe to production at Oppau."
    },
    {
      "id": "recap-05",
      "case": "HHH-C1-CASE05",
      "label": "Case 05",
      "title": "The Dust Bowl",
      "setting": "The southern Great Plains of the United States",
      "span": "the 1930s · drought July 1928 – May 1942",
      "archiveThread": "RESPOND",
      "archiveThreadGloss": "a response that acted on one cause and not the other",
      "change": "Soil left the land at regional scale, and a conservation programme followed.",
      "evidence": [
        "The instrumental drought record: the 1930s drought ran between July 1928 and May 1942; at its peak it covered at least 60% of the Lower 48 States; the average longest unbroken stretch at individual locations was 38.4 months, peaking in March 1935.",
        "What the land was already like, and what was done: prairie sod was broken for cropland, leaving bare rootless soil between crops — while about two-thirds of the Great Plains remained in unploughed native vegetation. The Soil Conservation Act was signed on 27 April 1935."
      ],
      "supports": "That the drought (what arrived) and the broken sod (what the land was already like) together produced wind erosion at the scale the region saw. Wind erosion needs loose dry soil and an uncovered surface: neither cause reaches the outcome without the other.",
      "doesNotEstablishAlone": "Weather alone is wrong, and so is the claim that the weather was irrelevant. The plough alone is wrong too. And the conservation programme spread across the later 1930s while the rains also returned at the end of the decade — nothing in this evidence separates their contributions.",
      "sourceStatus": "The drought record, the erosion surveys and the Act: documented. The land-degradation feedback (Cook, Miller and Seager 2009): modeled. How two historians weigh the same two causes: debated. The Archive’s scenes on the plains: reconstructed.",
      "railEntry": "Drought meets broken sod. Wind erosion at regional scale, and a conservation response that acted on the land."
    },
    {
      "id": "recap-06",
      "case": "HHH-C1-CASE06",
      "label": "Case 06",
      "title": "The Vertical Farm",
      "setting": "A commercial vertical farm, 2041 — fictional",
      "span": "2041 — fictional",
      "archiveThread": "PRESERVE",
      "archiveThreadGloss": "what a record leaves out becomes what later readers cannot know",
      "change": "In a sealed indoor growing loop, every machine met the specification it was designed to meet, and the crop died anyway.",
      "evidence": [
        "FICTIONAL CASE EVIDENCE The engineered part of the loop met its setpoints throughout. Biological activity in the biofilter held steady, then fell over about 72 hours and ran flat; ammonia rose and nitrate fell; the crops began to die only after that. The company’s public statement blamed a flawed nutrient-cycling design and named an engineer.",
        "REAL-WORLD SCIENCE Nitrification is a real microbial process: ammonia and ammonium are oxidised to nitrite and then to nitrate. The organisms are not a fixed pair — ammonia-oxidising archaea as well as bacteria carry out the first step, and comammox Nitrospira can carry out both steps in one organism (Daims et al. 2015; van Kessel et al. 2015). Plants take up inorganic nitrogen mainly as nitrate and ammonium (Hachiya and Sakakibara 2017)."
      ],
      "supports": "Within the invented case: that the living part of the loop failed while the engineered part met specification, and that the monitoring watched only the engineered part.",
      "doesNotEstablishAlone": "Nothing about the real world. Getting the 2041 case right proves nothing about the real world, and a real scientific finding proves nothing about 2041. The invented record also does not establish which logged event collapsed the microbes.",
      "sourceStatus": "Two layers, and they never merge. The 2041 facility, its logs, its dates and its public statement are fictional / hypothetical — the Archive invented all of it. The nitrification science and the plant-uptake science are documented real-world findings from real published sources.",
      "railEntry": "A sealed indoor loop. The engineered part meets specification; the living part fails. Fictional."
    }
  ],
  "recapContract": {
    "id": "synthesis-recap-v1.0",
    "rule": "All six Campaign 1 Core Cases appear as evidence recaps in both learner editions. Each recap prints its setting and time, the historical or system change, one or two certified evidence points, what that evidence supports, what it does not establish alone, its source status, and its archive thread. No recap is given an explanatory formula that would create false equivalence with another.",
    "requiredFields": [
      "setting",
      "change",
      "evidence",
      "supports",
      "doesNotEstablishAlone",
      "sourceStatus",
      "archiveThread"
    ],
    "enforcedRoles": [
      "student",
      "accessible"
    ],
    "noNewEvidenceRule": "Every factual statement in every recap is carried forward from the released Case 01 to 06 packages and their certified sources. This unit introduces no new external factual claim and launches no new research.",
    "orientationContribution": {
      "unit": "HHH-C1-CASE00",
      "rule": "Archive Orientation is not one of the six Core Case evidence selections. Its methodological rule is carried forward instead: preservation does not equal historical verification.",
      "appliesTo": [
        "source-status treatment in every recap",
        "SYN-T6"
      ]
    }
  },
  "chronology": [
    {
      "case": "HHH-C1-CASE01",
      "label": "Case 01",
      "title": "The Fertile Crescent",
      "when": "about 9,750 – 6,350 BCE",
      "entry": "Repeated selection, seed saving and replanting. Domesticated-type grain appears at different times in different regions."
    },
    {
      "case": "HHH-C1-CASE02",
      "label": "Case 02",
      "title": "Sumer",
      "when": "scene set about 2000 BCE",
      "entry": "Irrigation without drainage on a flat plain. Salt accumulates where the water leaves and the salt does not."
    },
    {
      "case": "HHH-C1-CASE03",
      "label": "Case 03",
      "title": "County Cork",
      "when": "1845 – 1852",
      "entry": "Late blight destroys the potato crop. About a million deaths follow from the failure meeting conditions already in place."
    },
    {
      "case": "HHH-C1-CASE04",
      "label": "Case 04",
      "title": "Karlsruhe",
      "when": "1908 – 1913",
      "entry": "Ammonia synthesis moves from a laboratory demonstration at Karlsruhe to production at Oppau."
    },
    {
      "case": "HHH-C1-CASE05",
      "label": "Case 05",
      "title": "The Dust Bowl",
      "when": "the 1930s · drought July 1928 – May 1942",
      "entry": "Drought meets broken sod. Wind erosion at regional scale, and a conservation response that acted on the land."
    },
    {
      "case": "HHH-C1-CASE06",
      "label": "Case 06",
      "title": "The Vertical Farm",
      "when": "2041 — fictional",
      "entry": "A sealed indoor loop. The engineered part meets specification; the living part fails. Fictional."
    }
  ],
  "chronologyScale": {
    "system": "cross-case timeline with nonuniform spans, not a single continuous-scale timeline",
    "rule": "The rail places six investigations in order and supplies their dates and identities so that no task depends on recall. The spans are of different kinds and different precisions - a set of overlapping archaeological evidence windows, a scene date, a famine period, a five-year industrial sequence, a decade with an instrumental drought record, and a fictional year - and both learner editions disclose that above the rail.",
    "disclosure": "These six spans are not measured the same way. Case 01's range is a set of overlapping evidence windows from different regions, crops and studies, not one continuous event. Case 02's date is the setting of a reconstructed scene. Case 06's year belongs to an invented case.",
    "case01Note": "Case 01's span is given as the range of its dated evidence windows, about 9,750 to 6,350 BCE. Those windows overlap and come from different regions and studies. The unit does not place Case 01 on a single date."
  },
  "limitCases": [
    {
      "case": "HHH-C1-CASE02",
      "label": "Case 02",
      "title": "Sumer",
      "localMechanism": "Irrigation without drainage on a flat plain with a shallow water table raises the salt in a field until crops suffer.",
      "pointer": "Recap card 02"
    },
    {
      "case": "HHH-C1-CASE03",
      "label": "Case 03",
      "title": "County Cork",
      "localMechanism": "Phytophthora infestans — late blight — destroys a potato crop in the field.",
      "pointer": "Recap card 03"
    },
    {
      "case": "HHH-C1-CASE05",
      "label": "Case 05",
      "title": "The Dust Bowl",
      "localMechanism": "Wind erosion moves loose dry soil that has no cover on it.",
      "pointer": "Recap card 05"
    },
    {
      "case": "HHH-C1-CASE06",
      "label": "Case 06",
      "title": "The Vertical Farm",
      "localMechanism": "In the invented 2041 case, the living part of the loop stopped converting ammonia while the machinery kept dosing it.",
      "pointer": "Recap card 06"
    }
  ],
  "mechanismLimitContract": {
    "id": "synthesis-mechanism-limit-v1.0",
    "rule": "Task 4 offers exactly Cases 02, 03, 05 and 06 and no others. The learner selects two and organizes each as local mechanism → what it explains → what it does not explain alone → additional context or evidence needed.",
    "allowedCases": [
      "HHH-C1-CASE02",
      "HHH-C1-CASE03",
      "HHH-C1-CASE05",
      "HHH-C1-CASE06"
    ],
    "excludedCases": [
      "HHH-C1-CASE01",
      "HHH-C1-CASE04"
    ],
    "exclusionReason": "Case 01's reasoning is cumulative change across generations rather than a mechanism that falls short of an outcome, and Case 04's is attribution across distinct kinds of work. Forcing either into the mechanism/broader-outcome frame for symmetry would teach a false shape.",
    "requiredStages": [
      "local-mechanism",
      "explains",
      "does-not-explain-alone",
      "additional-context"
    ],
    "enforcedRoles": [
      "student",
      "accessible"
    ]
  },
  "comparisonContract": {
    "id": "synthesis-continuity-change-v1.0",
    "rule": "Task 3 requires one case selected from Cases 01 to 03 and one from Cases 04 to 06. The comparison covers agricultural knowledge, practice or system; what was preserved or transferred; what changed; and an important consequence - for each selected case - then specific supporting evidence and one important qualification or evidence limit across the pair.",
    "earlyCases": [
      "HHH-C1-CASE01",
      "HHH-C1-CASE02",
      "HHH-C1-CASE03"
    ],
    "lateCases": [
      "HHH-C1-CASE04",
      "HHH-C1-CASE05",
      "HHH-C1-CASE06"
    ],
    "requiredRows": [
      "knowledge-practice-system",
      "preserved-or-transferred",
      "what-changed",
      "consequence",
      "supporting-evidence",
      "qualification"
    ],
    "enforcedRoles": [
      "student",
      "accessible"
    ],
    "why": "Six separate written comparisons would be repetition. One pair crossing a genuine span of time is the reasoning target."
  },
  "gameFramingBoundary": {
    "id": "synthesis-l7-framing-v1.0",
    "runtimeLevel": "C1 L7",
    "rule": "Campaign 1 Level 7 is framing material, not a historical evidence base. The finale excerpt is printed once per learner edition, inside a node marked data-game-framing, visibly identified as fictional in-world framing. No role cites Nova's testimony, the grove observation or any Archive finale statement as evidence for a real-world historical claim.",
    "excerptSource": "The Long Yield finale card, C1 L7, at game commit d9fc16baf272cb543c29cbd0c06ec85efad60be8.",
    "containment": "The excerpt text appears only inside [data-game-framing] nodes. No Answer Key exemplar may rest on a [data-game-framing] node.",
    "gamePlayRequired": false,
    "noGameFallback": "Complete. Six cross-case evidence recaps, the chronology rail and every supplied pointer carry Tasks 2 to 6 with no gameplay at all. The finale excerpt is optional framing and no task depends on it.",
    "auditDisposition": "READY_AS_SYNTHESIS_NOT_CORE_CASE",
    "gameDependencies": "None. The Phase 1 audit's game-dependency census records no finding against C1 L7."
  },
  "sourceStatusContract": {
    "id": "synthesis-source-status-v1.0",
    "rule": "Every recap prints the status of the evidence it carries, in words. Statuses are never upgraded: modeled is never printed as observed, reconstructed never as documented, debated never as settled, and fictional never as real history.",
    "statuses": [
      "documented",
      "observed",
      "measured",
      "reported",
      "inferred",
      "reconstructed",
      "modeled",
      "debated / uncertain",
      "fictional / hypothetical"
    ],
    "orientationRule": "Preservation does not equal historical verification. A record surviving is not the same as a record being checked.",
    "enforcedRoles": [
      "student",
      "teacher",
      "answer",
      "accessible"
    ]
  },
  "twoLayerTruth": {
    "id": "synthesis-two-layer-v1.0",
    "mandate": "Blueprint section 12, carried forward from Core Case 06. Mandatory wherever Case 06 evidence appears in this unit.",
    "rule": "The Case 06 recap declares both layers in markup and in printed text. Layer 1 - the 2041 facility, its logs, its dates, its public statement - is fictional and is marked FICTIONAL CASE EVIDENCE. Layer 2 - nitrification, the diversity of nitrifying organisms, plant uptake of inorganic nitrogen - is real published science and is marked REAL-WORLD SCIENCE.",
    "nonMergerRule": "Getting the 2041 case right proves nothing about the real world, and a real scientific finding proves nothing about 2041.",
    "requiredChips": [
      "FICTIONAL CASE EVIDENCE",
      "REAL-WORLD SCIENCE"
    ],
    "enforcedRoles": [
      "student",
      "teacher",
      "answer",
      "accessible"
    ],
    "prohibitedConversion": "No role converts a fictional 2041 event, figure, date or actor into a documented historical claim, and no role presents the invented case as future history."
  },
  "vocabulary": [
    {
      "term": "change",
      "definition": "Something that is different after a period of time than it was before."
    },
    {
      "term": "consequence",
      "definition": "What follows from a change, for people or for land."
    },
    {
      "term": "continuity",
      "definition": "Something that stays recognisably the same across a period of time."
    },
    {
      "term": "historical memory",
      "definition": "What later people can know about earlier people, and how they came to know it."
    },
    {
      "term": "preservation",
      "definition": "Keeping something — a seed, a practice, a record — so that it is still there later."
    },
    {
      "term": "provenance",
      "definition": "Where a record came from, and the hands it passed through to reach us."
    },
    {
      "term": "source status",
      "definition": "What kind of evidence something is: documented, reconstructed, inferred, modeled, debated, or fictional."
    },
    {
      "term": "transfer",
      "definition": "Knowledge or practice moving from one person, place, or setting to another."
    }
  ],
  "memoryIndependenceContract": {
    "id": "synthesis-memory-independence-v1.0",
    "rule": "No task in either learner edition requires recall of a Campaign 1 case. Every task carries a printed pointer to the recap card or rail entry that answers it, and every date and case identity a task needs is supplied on the page or on a page the pointer names.",
    "enforcedRoles": [
      "student",
      "accessible"
    ],
    "checkedAgainst": "tasks[].evidencePointers"
  },
  "accessibleAdaptations": [
    {
      "id": "a-chunked-recaps",
      "task": "1",
      "what": "The six recap cards are set at the Accessible type size, one or two to a page, with each of the seven required fields introduced by its own labelled line rather than run together in prose.",
      "effect": "Visual-search and reading burden drop. No evidence point and no qualification is removed."
    },
    {
      "id": "a-rail-supplied",
      "task": "2",
      "what": "The chronology rail prints the case number, the title and the date span on every row, at the Accessible type size.",
      "effect": "Dates and case identities are supplied rather than recalled. The comparison itself is unchanged."
    },
    {
      "id": "a-t2-frames",
      "task": "2",
      "what": "Both responses carry a sentence opener naming the shape of the answer, including blanks for the case numbers.",
      "effect": "Sentence-starting burden drops. Neither frame contains a continuity or a change."
    },
    {
      "id": "a-t3-frames",
      "task": "3",
      "what": "Every organizer cell carries a sentence frame, and the two selection rows print the permitted case numbers as options.",
      "effect": "Organization and sentence-starting burden drop. No cell is prefilled with an assessed conclusion."
    },
    {
      "id": "a-t3-short-phrases",
      "task": "3",
      "what": "The four per-case cells accept a short evidence phrase rather than a full sentence, stated in the directions.",
      "effect": "Repeated writing drops while the four distinct judgments remain."
    },
    {
      "id": "a-t4-pointers",
      "task": "4",
      "what": "Each permitted case in the choice list names the recap card and the exact line on it that bears on the task.",
      "effect": "Cross-page evidence search is removed. The judgment about where the mechanism stops is not."
    },
    {
      "id": "a-t4-frames",
      "task": "4",
      "what": "All four stages of both mechanism organizers carry a plain-language hint and a sentence frame, and stages 1 and 2 accept short phrases.",
      "effect": "Writing and organization burden drop. No stage is prefilled, and the does-not-explain-alone stage is never supplied."
    },
    {
      "id": "a-t4-contrast-strip",
      "task": "4",
      "what": "A printed two-column strip models the distinction between what a mechanism explains and what it does not explain alone, worked on Case 04.",
      "effect": "The distinction the task assesses is modelled on a case the learner may not choose, so the model cannot be copied into an answer."
    },
    {
      "id": "a-t5-bullets",
      "task": "5",
      "what": "The synthesis may be written as bullet points, and five labelled prompts with sentence openers stand above the response area.",
      "effect": "Extended prose is not a barrier to demonstrating the reasoning. All five requirements remain."
    },
    {
      "id": "a-t6-two-steps",
      "task": "6",
      "what": "Task 6 is collected as two steps - what disappears, then what a later reader could misunderstand - where the Student edition collects both in one field.",
      "effect": "Chunking only. The obligation is identical and the Answer Key models both halves for both editions."
    }
  ],
  "editionResponseContract": {
    "id": "synthesis-edition-parity-v1.0",
    "rule": "Every assessed Accessible response has a Student counterpart. No Accessible-only obligation exists, and no Accessible task carries more open response controls than its Student counterpart except where a declared chunking adaptation splits one field into two.",
    "declaredChunking": [
      "a-t6-two-steps"
    ],
    "declaredReductions": [
      "a-t3-short-phrases",
      "a-t4-frames"
    ]
  },
  "semanticInvariants": {
    "note": "DIAGNOSTIC REGISTER RECONCILED WITH POSITIVE STRUCTURE. Each negative class below is closed - a finite set of wordings the released Cases 01 to 06 already registered as prohibited, or a small finite set bound to a named subject. None polices an open synonym family and none polices an ordinary verb. Every class is paired with a positive structural requirement, because a guard that only forbade a sentence would be satisfied by a packet that said nothing at all.",
    "classes": [
      {
        "id": "cultivationIsDomestication",
        "subject": "HHH-C1-CASE01",
        "meaning": "Collapses cultivation into domestication.",
        "prohibited": [
          "cultivation is domestication",
          "cultivation means domestication",
          "cultivating is domesticating",
          "cultivation and domestication are the same",
          "domestication began when people began cultivating",
          "domestication started when people started cultivating"
        ],
        "positive": "The Case 01 recap must print that cultivation is not domestication and that people grew wild-type grain long before the plant population changed."
      },
      {
        "id": "salinityAsWholeCause",
        "subject": "HHH-C1-CASE02",
        "meaning": "Turns the field-scale salinization mechanism into a complete explanation of Sumerian historical decline.",
        "prohibited": [
          "the first agricultural crisis of human making",
          "salinity caused the fall of Sumer",
          "a people undone by its own water",
          "salt was the reason power moved north"
        ],
        "positive": "The Case 02 recap must print that how much soil salt contributed to the wider decline is argued among scholars and is not settled here."
      },
      {
        "id": "blightAlone",
        "subject": "HHH-C1-CASE03",
        "meaning": "Treats the pathogen, or any single condition, as a sufficient explanation of famine mortality.",
        "prohibited": [
          "blight alone caused the famine",
          "the whole country lived on the potato",
          "nothing else was grown to fall back on",
          "the potato famine was simply a natural disaster",
          "every field in Ireland was the same plant repeated"
        ],
        "positive": "The Case 03 recap must print that more than one condition contributed and that this evidence does not rank them."
      },
      {
        "id": "soloAttribution",
        "subject": "HHH-C1-CASE04",
        "meaning": "Credits the industrial process to one person or collapses laboratory demonstration into industrial engineering.",
        "prohibited": [
          "Haber alone created the industrial process",
          "Haber invented the Haber process and factories simply copied it",
          "Bosch merely copied Haber's laboratory apparatus",
          "the factory was a scaled-up copy of the bench",
          "Haber's laboratory work alone made ammonia available to farmers"
        ],
        "positive": "The Case 04 recap must print that laboratory demonstration and industrial engineering are distinct and must name more than one contributor."
      },
      {
        "id": "weatherIrrelevant",
        "subject": "HHH-C1-CASE05",
        "meaning": "Asserts that the drought was not a cause of the Dust Bowl.",
        "prohibited": [
          "the drought was not a cause",
          "the drought did not cause",
          "the drought was irrelevant",
          "the drought had nothing to do with",
          "the weather was not to blame",
          "nothing to do with the weather"
        ],
        "positive": "The Case 05 recap must print the drought as a contributing cause and must print that the two causes together produced the outcome."
      },
      {
        "id": "ploughAlone",
        "subject": "HHH-C1-CASE05",
        "meaning": "Presents land-use change as a sufficient sole cause, or blames individual farmers.",
        "prohibited": [
          "the plough alone caused the Dust Bowl",
          "the plow alone caused the Dust Bowl",
          "the ploughing alone explains it",
          "farmers caused the Dust Bowl",
          "bad farming caused the Dust Bowl",
          "greedy farmers caused the Dust Bowl"
        ],
        "positive": "The Case 05 recap must print that about two-thirds of the Great Plains remained in unploughed native vegetation."
      },
      {
        "id": "fictionAsHistory",
        "subject": "HHH-C1-CASE06",
        "meaning": "Converts the invented 2041 vertical farm into documented history.",
        "prohibited": [
          "the vertical farm really happened",
          "the vertical farm actually happened",
          "a real vertical farm",
          "documented future history",
          "the 2041 failure is a historical fact",
          "when the vertical farm failed in 2041",
          "the real 2041 facility"
        ],
        "positive": "The Case 06 recap must carry both layer chips, must print that the facility is fictional, and must print the non-merger rule."
      },
      {
        "id": "case07Identity",
        "subject": "HHH-C1-SYNTHESIS",
        "meaning": "Presents this unit as a numbered Core Case, or as Case 07.",
        "prohibited": [
          "Case 07",
          "Case 7",
          "CASE07",
          "Core Case 07",
          "Core Case 7"
        ],
        "positive": "Every role prints the display label Campaign 1 Synthesis, and the package instructional type is SYNTHESIS."
      },
      {
        "id": "progressNarrative",
        "subject": "HHH-C1-SYNTHESIS",
        "meaning": "Asserts that historical change is always improvement.",
        "prohibited": [
          "history always moves forward",
          "farming always got better",
          "each case is better than the one before",
          "agriculture has only improved",
          "change always means progress"
        ],
        "positive": "The Teacher misconceptions table must name the belief that historical change always means progress, and the unit must print at least one change with a harmful consequence."
      }
    ],
    "exemptions": [
      {
        "id": "teacher-misconception-register",
        "roles": [
          "teacher"
        ],
        "classes": [
          "cultivationIsDomestication",
          "salinityAsWholeCause",
          "blightAlone",
          "soloAttribution",
          "weatherIrrelevant",
          "ploughAlone",
          "fictionAsHistory",
          "progressNarrative",
          "case07Identity"
        ],
        "why": "The Teacher misconceptions table must be able to state a misconception in order to name it. Every excused node states the belief and its correction on the same row."
      },
      {
        "id": "answer-key-floor",
        "roles": [
          "answer"
        ],
        "classes": [
          "blightAlone",
          "weatherIrrelevant",
          "ploughAlone",
          "fictionAsHistory",
          "progressNarrative",
          "salinityAsWholeCause",
          "soloAttribution",
          "cultivationIsDomestication"
        ],
        "why": "The Answer Key states the wordings that do not earn credit. Every excused node is a scoring floor and says so."
      }
    ],
    "exemptionRule": "A node is excused only by naming a registered exemption id that resolves, for its role, to the class it would otherwise violate. Markup cannot self-authorize, and adding an attribute cannot make an unregistered sentence disappear."
  },
  "figureAccessibilityContract": {
    "rule": "Every curriculum figure carries a text alternative that states what the figure shows and what it is not. No figure carries information by colour alone.",
    "figures": [
      {
        "id": "recap-cards",
        "selector": "[data-recap-case]",
        "roles": [
          "student",
          "accessible"
        ],
        "alt": "Six evidence recap cards, one for each Campaign 1 Core Case, each printing its setting, the change, its evidence, what the evidence supports, what it does not establish alone, its source status and its archive thread."
      },
      {
        "id": "chronology-rail",
        "selector": "[data-chronology-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "alt": "A rail of six rows in campaign order, each naming the case, its date span and what the campaign records. The spans are of different kinds and precisions and the rail says so above itself."
      },
      {
        "id": "comparison-organizer",
        "selector": "[data-comparison-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "alt": "A two-column organizer, one column for the selected early case and one for the selected late case, with four rows of comparison and two full-width rows for evidence and qualification."
      },
      {
        "id": "mechanism-organizer",
        "selector": "[data-mechanism-contract]",
        "roles": [
          "student",
          "accessible"
        ],
        "alt": "Two four-stage organizers running local mechanism, what it explains, what it does not explain alone, and additional context or evidence needed."
      },
      {
        "id": "source-status-key",
        "selector": "[data-source-status-key]",
        "roles": [
          "student",
          "accessible"
        ],
        "alt": "A key naming the evidence statuses used across the campaign, in words, with the Archive rule that preservation does not equal historical verification."
      }
    ]
  },
  "standards": {
    "directlyAssessed": [
      "C3 D2.His.2.6-8",
      "C3 D2.His.1.6-8",
      "C3 D2.His.14.6-8",
      "CCSS RH.6-8.1",
      "CCSS WHST.6-8.2"
    ],
    "supporting": [
      "C3 D3.2.6-8",
      "CCSS RH.6-8.9"
    ],
    "contextual": [],
    "ngss": "No NGSS Performance Expectation is claimed, directly or contextually. The unit reasons about agricultural and environmental systems, but every assessed product is a historical continuity/change judgment supported by documentary and source-status reasoning. No learner develops a model from data, plans an investigation, or designs a solution against criteria and constraints, and the scientific material is supplied as sourced reading carried forward from the released cases rather than practised.",
    "d41": "C3 D4.1.6-8 is deliberately not claimed. The culminating product is an explanatory synthesis, not a formal evidence-based argument with a claim and counterclaims. If a later revision converts Task 5 into an argument, D4.1 becomes claimable; at this architecture it is not.",
    "rationale": "C3 D2.His.2.6-8 is the primary home: Tasks 2, 3 and 5 all require the learner to classify developments across Campaign 1 as continuity or as change. C3 D2.His.1.6-8 is directly assessed because Task 2 and Task 3 connect developments in six separate investigations to a broader campaign-wide context. C3 D2.His.14.6-8 is directly assessed because Task 4 is a multiple-cause judgment in its entirety - a correct local mechanism set against the broader outcome it cannot explain alone - and Task 3's consequence row assesses effects. CCSS RH.6-8.1 is directly assessed because Tasks 3, 4, 5 and 6 all require specific evidence cited from the recap cards, which are secondary summaries of certified primary and scholarly sources. CCSS WHST.6-8.2 is directly assessed at Task 5, which is an informative/explanatory text conveying the campaign's ideas through selection and organization of evidence. C3 D3.2.6-8 is supporting rather than directly assessed: the learner uses source status throughout and reasons about it directly at Task 6, but no task asks for a credibility verdict on a named source. CCSS RH.6-8.9 is supporting: the recaps set documented, reconstructed, inferred, modeled, debated and fictional material about the same events beside one another, and Task 4's additional-context stage requires the learner to say what other evidence would be needed, but no task assesses a formal two-source relationship analysis."
  }
};
