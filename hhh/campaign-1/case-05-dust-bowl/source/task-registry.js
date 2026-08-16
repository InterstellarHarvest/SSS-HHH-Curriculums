window.HHH_CASE05_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C1-CASE05",
  "runtimeId": "L5",
  "instructionalType": "CORE_CASE",
  "title": "The Dust Bowl",
  "displayLabel": "5 - The Dust Bowl",
  "version": "0.1",
  "status": "APPROVED_STABLE",
  "ownerReviewStatus": "OWNER_REVIEW_PASS",
  "editorShell": "1.0",
  "gameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
  "auditBaseline": "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md",
  "staticContentInventory": "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json",
  "blueprint": "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
  "roles": {
    "student": 10,
    "teacher": 8,
    "answer": 6,
    "accessible": 17
  },
  "culminatingProduct": "Qualified multi-causal historical and environmental explanation. The learner must name what arrived and what was already true, show how the two together produced wind erosion at the scale the region saw, state what the conservation response did and what the evidence in this packet cannot settle about the end of the dust, and then apply the same test to an unfamiliar human-environment claim. Canonical CER is deliberately not used: a single claim would collapse the interaction the case exists to teach, and the Blueprint names a qualified multi-causal explanation as this case's product. See the Teacher Guide reasoning architecture.",
  "causalFrame": {
    "id": "dust-bowl-interaction-v1.0",
    "rule": "Every role represents the Dust Bowl through four labelled causal roles plus one feedback relation. No role may be dropped, and no single role may be presented as the whole cause.",
    "roles": [
      {
        "id": "condition",
        "label": "CONDITION",
        "gloss": "what arrived",
        "subject": "the drought of the 1930s",
        "requiredStatus": "contributing cause",
        "why": "The drought is a real, documented, severe cause. Naming it a condition places it; it does not demote it. HHH-GAME-C1L5-002 exists because the runtime level's rhetoric can be heard as making the drought irrelevant, and this slot is the structural answer to that."
      },
      {
        "id": "vulnerability",
        "label": "VULNERABILITY",
        "gloss": "what the land was already like",
        "subject": "prairie sod broken for cropland, leaving bare and rootless soil between crops",
        "requiredStatus": "contributing cause",
        "why": "Land-use change is a real cause and is what made the same weather produce a different outcome. It is never presented as a sufficient sole cause, and it is never presented as the moral fault of individual farmers."
      },
      {
        "id": "mechanism",
        "label": "MECHANISM",
        "gloss": "how the soil actually left",
        "subject": "wind erosion: saltation, surface creep and suspension acting on loose dry soil with no cover",
        "requiredStatus": "requires both the condition and the vulnerability",
        "why": "The mechanism is the hinge of the whole case. Wind erosion needs dry loose soil and it needs the surface uncovered. Neither cause reaches the outcome without the other."
      },
      {
        "id": "response",
        "label": "RESPONSE",
        "gloss": "what was done about it",
        "subject": "conservation practice and the Soil Conservation Act of 27 April 1935",
        "requiredStatus": "addressed part of the system",
        "why": "The response acted on the vulnerability, not on the drought. It is never presented as an instantaneous or single-cause cure, because the rains also returned at the end of the decade and this packet cannot separate the two."
      }
    ],
    "feedback": {
      "id": "degradation-amplifies-drought",
      "from": "mechanism",
      "to": "condition",
      "statement": "Reduced vegetation cover and the dust the bare ground supplied fed back into the drought and made it worse.",
      "source": "degradation-model",
      "status": "modeled",
      "why": "Cook, Miller and Seager (2009) report that sea-surface forcing alone does not reproduce the observed drought and that adding land degradation is needed to do so. The relation is a model result and is labelled as one everywhere it appears."
    },
    "removalTest": {
      "rule": "Both removal answers must be available to the learner and both must be modelled in the Answer Key.",
      "removeCondition": "Without the drought the soil stays moist enough to hold together, and bare fields do not blow at that scale.",
      "removeVulnerability": "Without the plough-up the sod holds the soil through the dry years, which is exactly what the unploughed fence strip did."
    }
  },
  "tasks": [
    {
      "id": "C05-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Case Vocabulary",
      "description": "Apply the six case terms to the things and actions they name rather than copying definitions.",
      "instructionalPurpose": "Establish the six terms the case is unreadable without. Two of them, sod and topsoil, are the difference between what was removed and what was lost, and a learner who separates them has already met the distinction Tasks 4 and 5 assess.",
      "provenance": [
        "Curriculum-authored definitions",
        "Established soil science on wind erosion and soil horizons"
      ],
      "responseType": "six exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared six-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-dust-bowl-01",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-dust-bowl-01"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C05-T2",
      "number": "2",
      "semanticLabel": "FIRST READING",
      "icon": "ph-diagnosis",
      "title": "Record a First Explanation",
      "description": "Write down why you think the soil left this field, and name one thing you would have to find out before trusting that answer.",
      "instructionalPurpose": "Provisional interpretation recorded from the reconstructed scene alone, before the drought record and the survey evidence arrive. Most learners write either the drought or the plough, which are the two single-cause answers the whole case exists to complicate. The learner overturns their own answer at Task 5 rather than being corrected here.",
      "provenance": [
        "Game reconstruction of the southern plains in 1935",
        "Curriculum-authored prompt"
      ],
      "responseType": "two short constructed responses",
      "answerScope": "One provisional explanation of why the soil left and one named check that would have to come from outside the reconstructed scene.",
      "pagePlacement": {
        "student": "student-dust-bowl-03",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-dust-bowl-06"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C05-T3",
      "number": "3",
      "semanticLabel": "PLACE AND WEATHER",
      "icon": "ph-globe",
      "title": "Locate the Plains and Read the Drought",
      "description": "Use the region diagram and the drought record to say where this happened, how long the drought ran and how far it reached, then say why a drought alone is not yet the whole explanation.",
      "instructionalPurpose": "Family H3 sourced region diagram plus the instrumental drought record. This task exists so that the drought is established as real, long and severe before land use is mentioned at all. A learner who leaves this case believing the drought was a detail has been taught the opposite of the history, and this is the structural guard against it. Part C opens the interaction question without answering it.",
      "provenance": [
        "NOAA National Centers for Environmental Information, A Historical Perspective on Drought",
        "Soil Conservation Service erosion surveys as reported by Coppess 2019",
        "Curriculum-created region diagram"
      ],
      "responseType": "three marked placements plus two short constructed responses",
      "answerScope": "The states of the worst-hit core, the span and peak extent of the drought from the record, and a statement of what a drought on its own does not yet explain.",
      "pagePlacement": {
        "student": "student-dust-bowl-04",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-dust-bowl-08"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C05-T4",
      "number": "4",
      "semanticLabel": "THE SOIL SYSTEM",
      "icon": "ph-flow",
      "title": "Trace How Soil Leaves a Field",
      "description": "Complete the two open stages of the erosion diagram, say which condition the ploughing changed and which the drought changed, then read the core readings for what they do and do not establish.",
      "instructionalPurpose": "Family H8 soil and erosion system, and the load-bearing task of the case. Part B is the interaction made mechanical rather than rhetorical: the four conditions wind erosion needs are printed, and the learner assigns one to land use and one to the weather, so neither cause can be dropped. Part C is the audit boundary made assessable: the core readings say how much less, and a learner who writes that nothing can live below the lost topsoil has gone past the evidence in front of them.",
      "provenance": [
        "Jasa 2018, University of Nebraska-Lincoln Extension, on saltation, surface creep, suspension and the conditions wind erosion requires",
        "Game reconstruction of the gully core readings at the integrated game baseline",
        "Curriculum-created erosion system figure"
      ],
      "responseType": "two organizer stages, two condition placements and two short constructed responses",
      "answerScope": "The two open transport stages, one condition assigned to land use, one condition assigned to the drought, what the core readings establish about the subsoil, and one conclusion those readings do not support.",
      "pagePlacement": {
        "student": "student-dust-bowl-05",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-02",
        "accessible": "accessible-dust-bowl-10"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C05-T5",
      "number": "5",
      "semanticLabel": "THE CONTROL",
      "icon": "ph-scales",
      "title": "Read the Fence Line",
      "description": "Complete the comparison between the ploughed field and the unploughed strip beside it, then say what one fence line does and does not establish.",
      "instructionalPurpose": "The case's controlled comparison and the strongest single piece of evidence the runtime level supplies. Same soil, same sky, the same dry years, one difference. Part A makes the learner write the same drought into both columns, which is what makes the comparison a control rather than a slogan. Part B is where the case refuses to overreach: a fence line establishes that cover changed the outcome on that ground; it does not establish the region, and it does not establish that the drought was irrelevant. Source C is what carries the claim to regional scale.",
      "provenance": [
        "Game reconstruction of the fence line at the integrated game baseline",
        "Soil Conservation Service erosion surveys as reported by Coppess 2019",
        "Curriculum-created comparison"
      ],
      "responseType": "eight to ten comparison cells plus two short constructed responses",
      "answerScope": "Cover, roots, the drought each side received, and what the wind did on each side; then one statement of what the comparison establishes and one of what it cannot establish without further evidence.",
      "pagePlacement": {
        "student": "student-dust-bowl-06",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-03",
        "accessible": "accessible-dust-bowl-11"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C05-T6",
      "number": "6",
      "semanticLabel": "MULTIPLE CAUSATION",
      "icon": "ph-nodes",
      "title": "Build the Causation Map",
      "description": "Place eight factors in the four causal roles, then run the two removal tests and name one thing the map does not explain.",
      "instructionalPurpose": "Family H5 multiple-causation map and the organizer the culminating product is written from. The four roles are the case's answer to the audit finding: drought occupies a labelled slot, so it cannot quietly disappear, and land use occupies a different one, so it cannot quietly become the whole cause. Part B is the interaction test — remove either side and the dust does not follow — and Part C is the map's own limit, because a map of why soil blew does not explain who left the plains. The feedback relation is SUPPLIED on the map in both learner editions and is graded in neither: it is a modelled result reported by one source rather than something a learner can derive from the packet, and asking for it would have made the Accessible edition demand work the Student edition never asks for.",
      "provenance": [
        "NOAA National Centers for Environmental Information on the drought",
        "Cook, Miller and Seager 2009 on sea-surface forcing and land degradation",
        "Soil Conservation Service erosion surveys as reported by Coppess 2019",
        "The Soil Conservation Act of 27 April 1935",
        "Mullins, Okie Migrations, Oklahoma Historical Society",
        "Curriculum-created causation map"
      ],
      "responseType": "eight marked placements plus two short constructed responses",
      "answerScope": "Two factors in each of the four roles; both removal answers; and one named limit of the map drawn from the migration record. The Accessible edition places six factors rather than eight, because two are pre-placed under a declared adaptation, and it collects the two removal answers as two steps where the Student edition collects them in one field - a presentation split, not a change in what is demanded. Neither edition is asked for the feedback relation, which is printed on the map in both.",
      "suppliedNotAssessed": [
        {
          "id": "feedback-relation",
          "what": "The modelled feedback running from the mechanism back to the condition.",
          "printedIn": ["student", "accessible"],
          "gradedIn": [],
          "why": "A model result from a single source rather than an inference this packet supports, printed identically in both learner editions. It carries no response control in either edition and earns no Answer Key credit."
        }
      ],
      "pagePlacement": {
        "student": "student-dust-bowl-07",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-04",
        "accessible": "accessible-dust-bowl-13"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C05-T7",
      "number": "7",
      "semanticLabel": "POLICY SEQUENCE",
      "icon": "ph-flow",
      "title": "Order the Response",
      "description": "Put the four middle entries of the conservation sequence in order, then explain why this timeline cannot show that the law by itself stopped the dust.",
      "instructionalPurpose": "Family H11 policy and response sequence. The first and last entries are fixed, and the last one is the point: the rains returned at the end of the decade as well. A learner who reads the storms stopping as proof that the Act worked has made exactly the mistake the sequence is drawn to catch, and the same reasoning that refuses a single cause for the disaster has to refuse a single cause for its end.",
      "provenance": [
        "The Soil Conservation Act of 27 April 1935, ch. 85, 49 Stat. 163",
        "USDA Natural Resources Conservation Service and USDA Farmers.gov on Bennett and the founding of the Soil Conservation Service",
        "NOAA National Centers for Environmental Information on the span of the drought",
        "Curriculum-created policy sequence"
      ],
      "responseType": "four ordered placements plus one short constructed response",
      "answerScope": "The four middle entries in date order, and an explanation naming the second thing that changed at the end of the decade and why the timeline cannot separate the two.",
      "pagePlacement": {
        "student": "student-dust-bowl-08",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-05",
        "accessible": "accessible-dust-bowl-15"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C05-T8",
      "number": "8",
      "semanticLabel": "COMPETING CLAIMS",
      "icon": "ph-diagnosis",
      "title": "Weigh Five Claims",
      "description": "Mark five claims about the Dust Bowl against the evidence in this packet, then say what would settle the one you could not decide.",
      "instructionalPurpose": "Competing interpretations with three marks rather than two. Claim 2 is the drought-only account the runtime level rejects, Claim 3 is the land-use-only account the runtime level's rhetoric can produce in a learner, and Claim 4 is the biological-zero reading of the core. Claim 5 is undecidable from this packet on purpose and is not a manufactured puzzle: the conservation programme and the return of the rains arrive together at the end of the decade, and nothing printed here separates them.",
      "provenance": [
        "The fence-line comparison and the core readings from the game reconstruction",
        "NOAA National Centers for Environmental Information on the drought",
        "Cook, Miller and Seager 2009",
        "Worster 1979 and Cunfer 2005 on how much weight to give each factor",
        "Curriculum-created claims"
      ],
      "responseType": "five marked judgments plus one short constructed response",
      "answerScope": "One supported claim, three contradicted claims, one claim this packet cannot decide, and a named kind of evidence that would move the undecided claim.",
      "pagePlacement": {
        "student": "student-dust-bowl-09",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-05",
        "accessible": "accessible-dust-bowl-16"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C05-T9",
      "number": "9",
      "semanticLabel": "QUALIFIED EXPLANATION",
      "icon": "ph-wrench",
      "title": "Explain the Dust Bowl",
      "description": "Write the case's explanation using the four causal roles and specific sourced evidence, say what the response settled and what it did not, then apply the same test to a new claim.",
      "instructionalPurpose": "Culminating product for the case: a qualified multi-causal historical and environmental explanation. Part D carries the transfer function of the Core Case spine inside the culminating task rather than as a separate tenth task, because the operation being transferred is the same operation Parts A to C assess and a standalone transfer task would have re-measured it on a fresh page for no additional information.",
      "provenance": [
        "Curriculum-authored prompt",
        "Blueprint culminating-product policy",
        "Blueprint transfer and exit policy"
      ],
      "responseType": "extended constructed response with four required parts",
      "answerScope": "The condition and the vulnerability with sourced evidence for each, the mechanism and why it needed both, what the response addressed and what this packet cannot establish about the end of the dust, and two things that would have to be found out about an unfamiliar human-environment claim.",
      "pagePlacement": {
        "student": "student-dust-bowl-10",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-06",
        "accessible": "accessible-dust-bowl-17"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    }
  ],
  "vocabulary": [
    "contour plowing",
    "drought",
    "erosion",
    "shelterbelt",
    "sod",
    "topsoil"
  ],
  "caseSources": [
    {
      "id": "archive-plains",
      "displayLabel": "The Archive's scenes on the plains and in the hearing room",
      "creator": "Hunger, Harvest, & History Campaign 1 Level 5",
      "period": "scenes set in 1935",
      "sourceType": "reconstruction",
      "sourceOrigin": "game reconstruction of a historical setting",
      "evidentiaryStatus": "reconstructed",
      "limitationClass": "reconstruction",
      "contribution": "The lived shape of the case and its single best piece of reasoning: a farmer who broke the sod for wheat the way everyone did; field soil that runs through the fingers with no roots and no crumb structure; a strip of unploughed grass along a fence that kept its soil through the same dry years; a gully wall where a topsoil band that should run many inches deep is worn to about one; core readings for the ground beneath it; and a soil scientist in Washington naming the practices that keep land covered.",
      "limitation": "No person in it is a real person and no line of its dialogue is testimony. Its regional figures are stated inside the fiction and are not measurements this packet can rest on. Its own summing-up presses the point that the drought only pulled the trigger, which is a rhetorical emphasis rather than a finding, and this packet keeps the drought in a named causal role instead.",
      "gameCorrespondence": "C1 L5 sources farmer, sample_soil, examine_evidence, survey_land, examine_strata, sample_core, survey_region, bennett, review_testimony and query_archive at the integrated game baseline.",
      "fallbackCorrespondence": "Dossier card A on Student page 2 and Accessible page 2."
    },
    {
      "id": "drought-record",
      "displayLabel": "The instrumental drought record",
      "creator": "NOAA National Centers for Environmental Information, A Historical Perspective on Drought",
      "period": "July 1928 to May 1942",
      "sourceType": "national climate record",
      "sourceOrigin": "real modern government scientific record",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "That the drought was real, long and continental. NCEI records the 1930s drought as running between July 1928 and May 1942, calls it the most expansive at its peak, states that at its peak it covered at least 60 per cent of the Lower 48 States, and gives the average longest unbroken stretch at individual locations as 38.4 months, peaking in March 1935 - the spring this case is set in.",
      "limitation": "It measures the weather and nothing else. It cannot say why one field blew away and the field on the other side of a fence did not, it says nothing about what was planted or ploughed, and NCEI makes no statement on this page about what caused the drought.",
      "gameCorrespondence": "The level's premise that the rains have failed. The game gives no dates or extent for the drought; this source supplies both.",
      "fallbackCorrespondence": "Dossier card B on Student page 2 and Accessible page 2, and the drought bar in the Task 3 region diagram.",
      "rights": "NOAA NCEI news article. Public-domain United States Government work; summarised, not reproduced."
    },
    {
      "id": "erosion-surveys",
      "displayLabel": "What was ploughed, and what the erosion surveys found",
      "creator": "Coppess, J., The Conservation Question, Part 2: Lessons Written in Dust, farmdoc daily (9):200, Department of Agricultural and Consumer Economics, University of Illinois, 24 October 2019, reporting Soil Conservation Service survey figures and the 1936 Great Plains Committee report",
      "period": "1880 to 1938",
      "sourceType": "scholarly synthesis reporting contemporary government surveys",
      "sourceOrigin": "real modern institutional and scholarly source",
      "evidentiaryStatus": "documented",
      "limitationClass": "reported-at-second-hand",
      "contribution": "Scale, on both sides of the case. On the land-use side: 104 million acres of native sod ploughed under between initial settlement in 1880 and 1900, 20 million more by 1925 and 5 million more by 1930; and roughly 40 million acres ploughed in the southern and parts of the central Great Plains by 1929. On the damage side: a Soil Conservation Service survey in 1934 finding that 65 per cent of Great Plains acreage had suffered wind-erosion damage and that 15 per cent was severely eroded, and by 1938 that 80 per cent of the southern Great Plains had been affected with 40 per cent seriously affected. The 1936 Great Plains Committee recommended that about 15 million acres be taken out of production.",
      "limitation": "These are survey assessments reported at second hand, not measurements this packet has inspected. The damage categories are the agency's own and the boundaries between them are judgements. A survey of how much land was damaged cannot by itself apportion the damage between the weather and the ploughing.",
      "gameCorrespondence": "The level's in-world regional survey, which states a comparable order of magnitude inside the fiction. This source is where the figure actually comes from.",
      "fallbackCorrespondence": "Dossier card C on Student page 2 and Accessible page 3."
    },
    {
      "id": "wind-erosion-science",
      "displayLabel": "How wind moves soil, and what it needs in order to",
      "creator": "Jasa, P., Practices to Reduce Wind Erosion, CropWatch, University of Nebraska-Lincoln Extension, 11 May 2018",
      "period": "established soil science; no period",
      "sourceType": "established science",
      "sourceOrigin": "real modern institutional and scientific source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "The mechanism, in three named modes and four named conditions. Large particles move by saltation, rolling along the surface and detaching more soil particles; smaller particles move by surface creep; the smallest move by suspension and form the dust clouds in the sky. Wind erosion occurs where the soil is loose, dry and finely granulated; where the surface is reasonably smooth and vegetative cover is nonexistent or sparse; where there are large fields with no obstructions to reduce the force of the wind; and where the wind is strong enough to start soil moving. The potential for wind erosion is reduced any time the soil surface is covered.",
      "limitation": "It states what wind erosion requires. It does not date anything, it names no place, and it cannot say how much soil left the southern plains in the 1930s or who was responsible. It is the mechanism only.",
      "gameCorrespondence": "The level's soil analysis, which reports the same surface state - no roots, collapsed structure, wind-portable grains - inside the fiction without naming the transport modes.",
      "fallbackCorrespondence": "The Task 4 erosion system figure on Student page 5 and Accessible page 9, which prints the three modes and the four conditions."
    },
    {
      "id": "conservation-act",
      "displayLabel": "The Soil Conservation Act of 1935",
      "creator": "Act of April 27, 1935, ch. 85, 49 Stat. 163, codified at 16 U.S.C. 590a",
      "period": "approved 27 April 1935",
      "sourceType": "statute",
      "sourceOrigin": "real historical primary source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "A real document from the spring this case is set in, and the exact words Congress chose. It recognises that the wastage of soil and moisture resources on farm, grazing and forest lands of the Nation, resulting from soil erosion, is a menace to the national welfare; it makes the control and prevention of soil erosion a permanent federal policy; and it authorises the Secretary of Agriculture to carry out preventive measures including, but not limited to, engineering operations, methods of cultivation, the growing of vegetation, and changes in use of land.",
      "limitation": "A statute records what Congress enacted. It does not record what changed in any field, it measures no erosion, it names no farm, and it is not evidence that the law is what ended the dust storms. The Act acts on land use; it does not act on the weather.",
      "gameCorrespondence": "The level's forward archive, which reports the Act passing weeks after the testimony. This source is the Act itself.",
      "fallbackCorrespondence": "Dossier card E on Student page 3 and Accessible page 4, and entry 3 of the Task 7 policy sequence.",
      "rights": "United States statute and United States Code. Public record; quoted in part and not reproduced in full."
    },
    {
      "id": "degradation-model",
      "displayLabel": "A model that puts the weather and the land together",
      "creator": "Cook, B. I., Miller, R. L. and Seager, R., Amplification of the North American Dust Bowl drought through human-induced land degradation, Proceedings of the National Academy of Sciences 106, 4997-5001 (2009), doi:10.1073/pnas.0810200106",
      "period": "modelling the 1930s; published 2009",
      "sourceType": "peer-reviewed climate modelling study",
      "sourceOrigin": "real modern scientific source",
      "evidentiaryStatus": "modeled",
      "limitationClass": "model",
      "contribution": "The interaction itself, as a scientific result rather than as a slogan. General circulation models forced by 1930s sea-surface temperatures alone produce a drought, but one centred in southwestern North America and without the observed warming across the middle of the continent. The authors report that including forcing from human land degradation - represented as reduced vegetation cover and soil dust aerosol from crop failure - in addition to the anomalous sea-surface temperatures is necessary to reproduce the anomalous features of the Dust Bowl drought, and that human-induced land degradation is likely to have not only contributed to the dust storms of the 1930s but also amplified the drought.",
      "limitation": "It is a model, not a measurement of the 1930s. It does not observe any field, it does not record what any farmer did, and it cannot apportion blame between people. What it establishes is that the ocean-driven drought on its own does not reproduce what happened, which is a statement about two causes and not about one.",
      "supportingReferences": [
        {
          "label": "Schubert, S. D., Suarez, M. J., Pegion, P. J., Koster, R. D. and Bacmeister, J. T., On the Cause of the 1930s Dust Bowl, Science 303, 1855-1859 (2004)",
          "role": "corroboration that the drought itself had an ocean cause independent of anything done on the land",
          "states": "that model results indicate the drought was caused by anomalous tropical sea-surface temperatures during that decade, and that interactions between the atmosphere and the land surface increased its severity",
          "limitation": "also a modelling study, and it is cited here for the origin of the drought rather than for the land-degradation result",
          "printedIn": "Teacher source ledger only; it supplies no learner-facing evidence of its own and is therefore a supporting reference under this source rather than a canonical source in its own right"
        }
      ],
      "gameCorrespondence": "None. The level offers the interaction as a verdict; no scene in it models anything.",
      "fallbackCorrespondence": "Dossier card F on Student page 3 and Accessible page 4, and the feedback relation in the Task 6 causation map.",
      "rights": "PNAS 106, 4997-5001 (2009). doi:10.1073/pnas.0810200106. Cited and summarised, not reproduced."
    },
    {
      "id": "historians-disagree",
      "displayLabel": "Two historians, weighing the same two causes differently",
      "creator": "Worster, D., Dust Bowl: The Southern Plains in the 1930s, Oxford University Press, 1979; and Cunfer, G., On the Great Plains: Agriculture and Environment, Texas A&M University Press, 2005",
      "period": "the 1930s, argued about in 1979 and in 2005",
      "sourceType": "scholarly historical accounts in disagreement",
      "sourceOrigin": "real modern scholarly sources",
      "evidentiaryStatus": "debated",
      "limitationClass": "debate",
      "contribution": "That the weighting is a live question among historians, not a settled sum. Worster argues that the disaster was made by a land-use system that broke the sod for market wheat, and that the dust followed from that choice. Cunfer, working from county-level agricultural census data and mapping across 450 counties in ten states, argues that land use on the Plains was more stable than that account implies, that about two-thirds of the Great Plains remained in unploughed native vegetation, and that drought and heat account for the dust better than the amount of ploughing does.",
      "limitation": "Two published historians disagreeing is evidence that the question is open, not evidence for either answer. They use different units of analysis - one region and one decade against 450 counties and 130 years - and nothing in this packet decides between them. Neither of them argues that the drought did not matter, and neither argues that land use did not matter; they disagree about weight.",
      "gameCorrespondence": "None. The level presents one settled verdict and no disagreement.",
      "fallbackCorrespondence": "Dossier card G on Student page 3 and Accessible page 5."
    },
    {
      "id": "migration-record",
      "displayLabel": "Who actually left, and why",
      "creator": "Mullins, W. H., Okie Migrations, The Encyclopedia of Oklahoma History and Culture, Oklahoma Historical Society",
      "period": "the 1930s",
      "sourceType": "reference encyclopedia entry by a named historian",
      "sourceOrigin": "real modern institutional and scholarly source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "The single most useful check on overreach in this case. Far more migrants left southeastern Oklahoma than the Dust Bowl region of northwestern Oklahoma and the Panhandle. Net migration loss from Oklahoma across the 1930s may have been as many as 440,000 people. Between 1931 and 1933, 10 per cent of Oklahoma farmers lost their land to foreclosure; more than 60 per cent of Oklahoma farmers were tenants; mechanisation was consolidating small farms into larger ones; and payments for taking land out of production often resulted in landowners removing tenants' land from cultivation.",
      "limitation": "It establishes that the migration cannot be read off a dust map. It does not measure how much any one of those pressures contributed, and it is an encyclopedia entry rather than the underlying study.",
      "supportingReferences": [
        {
          "label": "Gregory, J. N., American Exodus: The Dust Bowl Migration and Okie Culture in California, Oxford University Press, 1989",
          "role": "the standard scholarly study behind the encyclopedia entry's account of where the migrants came from",
          "states": "that the great majority of the southwestern migrants to California did not come from the Dust Bowl counties",
          "limitation": "cited here at the level the encyclopedia entry supports; this packet does not quote a figure from it",
          "printedIn": "Teacher source ledger only; the learner editions carry the encyclopedia entry"
        }
      ],
      "gameCorrespondence": "The level's optional survey line about families driving west, which the scene itself cannot establish anything about.",
      "fallbackCorrespondence": "Dossier card G on Student page 3 and Accessible page 5, used by Task 6 Part C."
    },
    {
      "id": "region-diagram",
      "displayLabel": "The region diagram",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching schematic and is not a projection",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "limitationClass": "model",
      "contribution": "It puts the worst-hit core in the right relationship to the wider drought, so that the difference between the region that blew and the far larger region that was dry can be seen rather than asserted. The core it marks is the one the sources describe: the panhandles of Texas and Oklahoma with adjacent parts of New Mexico, Colorado and Kansas.",
      "limitation": "It is a schematic of relative position, not a map. It is not a projection, it is not to scale, it draws no boundary that any survey drew, and no distance or area may be read off it. It shows where, roughly; it does not show how much.",
      "gameCorrespondence": "The level's two locations, Oklahoma and Washington, which fix no geography beyond their names.",
      "fallbackCorrespondence": "Task 3 figure on Student page 4 and Accessible page 7."
    },
    {
      "id": "erosion-figure",
      "displayLabel": "The erosion system figure",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching model",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "limitationClass": "model",
      "contribution": "It sets the soil profile beside the transport sequence, so that what was lost and how it left can be reasoned about together. Its four printed conditions are the established requirements for wind erosion, and printing them is what lets a learner assign one to the weather and one to the land use instead of arguing about which cause is bigger.",
      "limitation": "A drawing made to explain an order and a set of requirements. Nothing on it is to scale; no depth, particle size, wind speed or rate is measurable from it. The profile panel is a generalised one and is not a survey of any particular gully.",
      "gameCorrespondence": "The level's gully wall and core, which give the profile without the transport mechanism.",
      "fallbackCorrespondence": "Task 4 figure on Student page 5 and Accessible page 9."
    },
    {
      "id": "causation-figure",
      "displayLabel": "The causation map",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching organizer",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "limitationClass": "model",
      "contribution": "It gives the four causal roles equal printed weight and holds the feedback relation as a separate, separately labelled arrow, so that the interaction can be organised without any arrow implying a measured strength.",
      "limitation": "No arrow on it carries a weight, a percentage or a rank, because no source in this packet supplies one, and the figure says so in print. It organises causes; it does not measure them. It explains why soil blew, and it does not explain who left the plains.",
      "gameCorrespondence": "None. The level presents its causation as a paragraph.",
      "fallbackCorrespondence": "Task 6 figure on Student page 7 and Accessible page 13."
    },
    {
      "id": "policy-figure",
      "displayLabel": "The policy and response sequence",
      "creator": "Curriculum-original figure authored for this case",
      "period": "1933 to 1941",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "limitationClass": "model",
      "contribution": "It puts the response in order and, by fixing the last entry, puts the return of the rains on the same timeline as the conservation programme. That adjacency is the argument: two things changed at the end of the decade, and a sequence can show both without claiming which one did the work.",
      "limitation": "An ordering, not an evaluation. It shows what followed what; it does not show what caused what, and it supplies no measurement of how much erosion any practice prevented.",
      "gameCorrespondence": "The level's forward archive, which reports the Act and the practices spreading but not the drought ending.",
      "fallbackCorrespondence": "Task 7 figure on Student page 8 and Accessible page 15."
    }
  ],
  "subsoilBoundary": {
    "rule": "Severe topsoil loss, low organic matter, low fertility, greatly reduced biological activity and greatly reduced crop suitability are the case's claims about the exposed subsoil. Biological or agronomic zero is not.",
    "requiredFraming": "bounded-comparative",
    "approvedQualifiers": [
      "a trace",
      "trace",
      "far below",
      "well below",
      "a fraction of",
      "much less than",
      "greatly reduced",
      "severely reduced",
      "severely degraded",
      "sharply lower",
      "lower than",
      "poor in",
      "starved",
      "too little to carry a crop",
      "far too little"
    ],
    "prohibitedFramings": [
      "biologically dead",
      "dead soil",
      "dead ground",
      "lifeless",
      "sterile",
      "no microbial life",
      "no living things",
      "nothing lives",
      "nothing can live",
      "nothing will grow",
      "will grow nothing",
      "grows nothing",
      "cannot grow anything",
      "devoid of life",
      "zero organic matter",
      "no organic matter",
      "no life at all",
      "completely dead"
    ],
    "prohibitedConceptClasses": {
      "rule": "These two classes are the enforced contract. A proposition whose subject is the protected subsoil fails if it carries either class, WITHOUT needing any second life-or-growth token: in 'the subsoil is dead' the predicate already is the biological claim. The first candidate's guard required subject AND a separate life token AND an absolute, which is why seven direct characterizations escaped it.",
      "selfSufficient": true,
      "biologicalZero": {
        "meaning": "Asserts that life, biological activity or organic matter is absent from the protected layer, rather than reduced.",
        "patterns": [
          "\\bdead\\b(?!\\s+(?:field|fields|crop|crops|plant|plants|grass|animal|animals|wood|weight|end|reckoning|heat|centre|center))",
          "\\blifeless\\b",
          "\\bsterile\\b|\\bsterilis\\w*\\b|\\bsteriliz\\w*\\b",
          "\\bdevoid\\b",
          "\\bbarren of life\\b",
          "\\bempty of life\\b",
          "\\bno\\s+(?:life|living|micro\\w*|organisms?|biology|biological\\s+activity|organic\\s+matter|organic\\s+carbon)\\b",
          "\\bnothing\\s+(?:at all|whatsoever)?\\s*(?:is\\s+|was\\s+)?(?:alive|living|lives|live|survives|survive|remains|remain)\\b",
          "\\bnothing\\s+(?:at all|whatsoever)?\\s*(?:can|will|could|would|has|have|had)\\s+(?:ever\\s+)?(?:live|lived|survive|survived|remain|remained)\\b",
          "\\bnot\\s+(?:a|an|one)\\s+(?:single\\s+)?(?:\\w+\\s+){0,2}?(?:living\\s+thing|thing|organism|organisms|microbe|microbes|microorganism|bacterium|bacteria|creature|root)s?\\b",
          "\\bno\\s+single\\s+(?:\\w+\\s+){0,2}?(?:living\\s+thing|thing|organism|organisms|microbe|microbes|microorganism|bacterium|bacteria|creature|root)s?\\b",
          "\\bnot\\s+(?:a|an|one)?\\s*(?:single\\s+)?traces?\\s+of\\s+(?:life|living)\\b",
          "\\bnot\\s+(?:a|an|one)\\s+(?:single\\s+)?(?:\\w+\\s+){0,2}?(?:survives?|remains?|lives?|is\\s+alive)\\b",
          "\\bzero\\s+(?:life|living|organic|microbial|biological)\\b",
          "\\bwithout\\s+(?:any\\s+)?(?:life|living|microbial|biological)\\b",
          "\\bno\\s+longer\\s+alive\\b",
          "\\b(?:life|living|microbial|biological|microbes?|organisms?)\\w*\\s+(?:\\w+\\s+){0,2}?(?:is|are|was|were)\\s+(?:completely\\s+|entirely\\s+|totally\\s+|wholly\\s+)?absent\\b",
          "\\b(?:completely|entirely|totally|wholly)\\s+absent\\b"
        ]
      },
      "universalGrowthZero": {
        "meaning": "Asserts that the protected layer can grow nothing at all, rather than that it is greatly reduced in crop suitability.",
        "arityNote": "The modal and the adverb are INDEPENDENTLY optional. An earlier compilation put them in one alternation, so it accepted a modal or an ever but not both. The same lesson applies to the intensifier slot and to the verb form: every slot is its own optional group, and the verb is a declared lexeme family rather than a spelling stem.",
        "growthVerbFamily": ["grow", "grows", "growing", "grew", "grown"],
        "growthVerbRule": "The prohibited class is semantic, not spelling-stem-specific. Matching on grow\\w* silently excluded grew and grown, so 'nothing grew in the subsoil' and 'nothing has ever grown' were outside the guard. The family is declared here and compiled into every construction that needs a growth verb.",
        "intensifiers": ["at all", "whatsoever"],
        "intensifierRule": "A bounded, closed set placed immediately after 'nothing'. Ordinary English puts an intensifier there and nowhere else in these constructions, so the slot is one optional group rather than a filler-word run.",
        "supportObjects": ["growth", "life", "plants", "plant", "crops", "crop", "vegetation"],
        "patterns": [
          "\\bnothing\\s+(?:at all|whatsoever)?\\s*(?:can|will|could|would|shall|may|has|have|had|is|was)?\\s*(?:ever\\s+)?(?:have\\s+|has\\s+|had\\s+|been\\s+|going\\s+to\\s+)?(?:grow|grows|growing|grew|grown)\\b",
          "\\bnothing\\s+(?:at all|whatsoever)?\\s*(?:has|have|had)\\s+(?:ever\\s+)?(?:grown|grew)\\b",
          "\\b(?:grow|grows|grew|grown)\\s+nothing\\b",
          "\\bcan\\s?not\\s+grow\\s+anything\\b|\\bcannot\\s+grow\\s+anything\\b",
          "\\bwill\\s+not\\s+grow\\s+anything\\b|\\bwon't\\s+grow\\s+anything\\b",
          "\\bcan\\s?not\\s+support\\s+(?:any|a|an|the|one|a single)?\\s*(?:growth|life|plants?|crops?|vegetation)\\b|\\bcannot\\s+support\\s+(?:any|a|an|the|one|a single)?\\s*(?:growth|life|plants?|crops?|vegetation)\\b",
          "\\bnever\\s+(?:again\\s+)?support\\s+(?:any|a|an|the|one|a single)?\\s*(?:growth|life|plants?|crops?|vegetation)\\b",
          "\\b(?:can|will|could|would|shall|may)\\s?not\\s+(?:ever\\s+)?(?:grow|grows|growing|grew|grown)\\b",
          "\\bnever\\s+(?:again\\s+)?(?:grow|grows|growing|grew|grown)\\b",
          "\\bunable\\s+to\\s+(?:grow|support)\\w*\\b",
          "\\bincapable\\s+of\\s+(?:growing|supporting)\\b",
          "\\b(?:no|not\\s+(?:a|one))\\s+(?:crop|plant|seed|thing)s?\\s+(?:can|will|could|would)?\\s*(?:ever\\s+)?(?:grow|grows|grew|grown)\\b"
        ]
      }
    },
    "boundaryCorpus": {
      "rule": "Shipped with the contract rather than held privately in the validator, so a mutation to the registry moves the tests with it and the corpus can never drift from the boundary it exercises. Every sentence binds the protected subject explicitly, because a sentence without one tests nothing: subject scoping is part of the accepted architecture.",
      "nonSubsoilDeadRole": "The nonSubsoilDead group is the standing proof that subject scoping works: ordinary surface and crop uses of the word dead - a dead field, a dead wheat crop, dead grass - are not subsoil claims and must never be treated as violations. That coverage existed implicitly before the bounded whitelist was retired and was lost with it; it is now explicit and registry-owned, so it cannot disappear again as a side effect of unrelated work.",
      "mustPassRole": "REPRESENTATIVE REGRESSION PROBES, NOT A WHITELIST. The must-pass sentences exist to prove the zero classifier does not overmatch truthful prose. They confer no authority: prose does not need to appear here, or to resemble anything here, in order to pass. Authored wording this corpus has never seen is expected to pass, and does.",
      "mustFailZero": {
        "reviewerEscapes": [
          "The subsoil is dead.",
          "Beneath the topsoil the ground is dead.",
          "Below the topsoil lies dead ground.",
          "The subsoil is dead soil.",
          "Beneath the topsoil the ground is completely dead.",
          "The subsoil is sterile.",
          "Beneath the topsoil nothing is alive."
        ],
        "modalAdverbArity": [
          "Nothing will ever grow in the subsoil.",
          "Nothing can ever grow in the subsoil.",
          "Nothing could ever grow below the topsoil.",
          "Nothing would ever grow beneath the topsoil.",
          "Nothing ever grows in this subsoil.",
          "Nothing can grow in the lower soil layer."
        ],
        "modalAdverbArityFresh": [
          "Nothing will ever grow beneath the topsoil again.",
          "Nothing could grow in the subsoil now.",
          "Nothing would grow below the topsoil even with rain.",
          "Nothing is ever going to grow in the subsoil.",
          "The subsoil can never again grow a crop.",
          "Below the topsoil no plant will ever grow.",
          "Beneath the topsoil no seeds can grow.",
          "The subsoil will not ever grow wheat."
        ],
        "quantifierGrammar": [
          "Not one microbe survives below the topsoil.",
          "Not one organism survives in the subsoil.",
          "Below the topsoil not one living thing remains.",
          "There is not one microbe alive in the subsoil.",
          "Not one living organism remains beneath the topsoil."
        ],
        "quantifierGrammarFresh": [
          "Not one bacterium is left in the subsoil.",
          "Beneath the topsoil not one root survives.",
          "Not one single microbe lives below the topsoil.",
          "In the subsoil not one creature remains.",
          "Below the topsoil there is not a single living thing.",
          "Not one tiny organism survives in the subsoil.",
          "Beneath the topsoil not one trace of life is left.",
          "The subsoil holds not one living microorganism."
        ],
        "neverSupport": [
          "The subsoil can never support growth.",
          "The subsoil can never support any growth.",
          "The subsoil will never support growth.",
          "The subsoil could never support life.",
          "Beneath the topsoil the ground would never support plants.",
          "The lower soil layer can never support crops."
        ],
        "neverSupportFresh": [
          "The subsoil can never again support a crop.",
          "Below the topsoil the ground will never support vegetation.",
          "The lower layer could never support any plants.",
          "Beneath the topsoil the soil would never support life again.",
          "The subsoil may never support crops.",
          "The exposed lower layer shall never support growth.",
          "Under the topsoil the ground can never support any life.",
          "The gully floor will never again support vegetation.",
          "The mineral layer can never support a single crop.",
          "Beneath the topsoil nothing there could never support growth."
        ],
        "nothingIntensifier": [
          "Nothing at all can grow in the subsoil.",
          "Nothing whatsoever will grow beneath the topsoil.",
          "Nothing at all lives below the topsoil.",
          "Nothing whatsoever can live in the lower soil layer.",
          "Nothing at all could grow in this subsoil.",
          "Nothing whatsoever survives in the subsoil."
        ],
        "nothingIntensifierFresh": [
          "Nothing at all will grow in the subsoil now.",
          "Nothing whatsoever grows beneath the topsoil.",
          "Nothing at all remains alive below the topsoil.",
          "Nothing whatsoever is alive in the subsoil.",
          "Nothing at all can live beneath the topsoil.",
          "Nothing whatsoever could survive in the lower soil layer.",
          "In the subsoil nothing at all survives.",
          "Below the topsoil nothing whatsoever remains.",
          "Nothing at all has ever lived in the subsoil.",
          "Nothing whatsoever would grow beneath the topsoil."
        ],
        "growInflection": [
          "Nothing grew in the subsoil.",
          "Nothing ever grew below the topsoil.",
          "Nothing has ever grown in the subsoil.",
          "Nothing had ever grown beneath the topsoil.",
          "Nothing whatsoever has grown in the lower soil layer."
        ],
        "growInflectionFresh": [
          "Nothing has grown in the subsoil since the topsoil left.",
          "Beneath the topsoil nothing grew after that.",
          "Nothing at all grew below the topsoil.",
          "In the subsoil nothing has ever grown.",
          "Nothing had grown beneath the topsoil for years.",
          "Below the topsoil nothing whatsoever grew.",
          "Nothing ever grew again in the lower soil layer.",
          "The subsoil grew nothing.",
          "Nothing at all has grown in the exposed lower layer.",
          "Beneath the topsoil nothing would ever have grown."
        ],
        "layerSubjectScope": [
          "The lower layer is sterile.",
          "The lower soil layer is dead.",
          "The exposed layer contains no life.",
          "The exposed soil layer will grow nothing.",
          "The exposed lower layer is biologically dead.",
          "The exposed lower soil layer can never support growth."
        ],
        "noSingleQuantifier": [
          "No single living organism remains below the topsoil.",
          "No single organism survives in the subsoil.",
          "No single microbe remains beneath the topsoil.",
          "No single living thing survives in the lower soil layer.",
          "The subsoil contains no single living organism.",
          "Below the topsoil no single microbe remains."
        ],
        "noSingleQuantifierFresh": [
          "No single microbial organism is left in the subsoil.",
          "Beneath the topsoil no single creature survives.",
          "In the exposed lower layer no single bacterium remains.",
          "The gully floor holds no single living thing.",
          "Under the topsoil no single root survives.",
          "No single living microbe remains in the subsoil.",
          "Below the topsoil there is no single organism left.",
          "The mineral layer contains no single microbe."
        ],
        "mixedZeroFirst": [
          "The subsoil can never support growth, though fertility is low.",
          "Nothing at all can grow in the subsoil, where fertility is low.",
          "Nothing whatsoever will grow beneath the topsoil, although activity is weak.",
          "Nothing ever grew in the subsoil, where organic matter is scarce.",
          "The lower soil layer can never support plants, though its fertility is low.",
          "Nothing at all lives below the topsoil, where organic matter is scarce.",
          "Nothing has ever grown in the subsoil, although its structure is poor.",
          "The subsoil is sterile, but it still holds a small amount of mineral matter.",
          "Nothing whatsoever survives in the subsoil, though some structure remains.",
          "Below the topsoil nothing grew, even where fertility had only dropped a little."
        ],
        "mixedSafeFirst": [
          "Fertility below the topsoil is low, and the subsoil can never support growth.",
          "Organic matter beneath the topsoil is scarce, so nothing at all can grow there.",
          "Although activity in the subsoil is weak, nothing whatsoever will grow in it.",
          "The subsoil holds a small amount of mineral matter, but nothing has ever grown in it.",
          "Crop suitability in the lower soil layer is limited, and it can never support crops.",
          "Fertility under the topsoil has dropped a long way, and nothing grew there afterwards.",
          "Growing a crop beneath the topsoil would be hard, and in fact nothing whatsoever lives there.",
          "The subsoil is somewhat reduced in fertility, yet nothing at all could grow in it."
        ],
        "mixedClause": [
          "The subsoil is sterile even though fertility is low.",
          "No microbes live below the topsoil, where organic matter is scarce.",
          "Nothing will ever grow in the subsoil, although its structure is poor.",
          "The ground beneath the topsoil is dead, with low fertility.",
          "Not one organism survives in the subsoil, even though crop suitability is limited."
        ],
        "mixedClauseFresh": [
          "Microbial life in the subsoil is completely absent, although fertility is low.",
          "Below the topsoil the layer is lifeless, though some structure is weak rather than gone.",
          "The subsoil has scarce organic matter and not one surviving microbe.",
          "Beneath the topsoil biological activity is limited and nothing can ever grow.",
          "The subsoil is degraded, poor, thin - and devoid of life."
        ]
      },
      "mustPassSafeProse": {
        "required": [
          "The subsoil has low fertility.",
          "Biological activity in the subsoil is weak.",
          "Organic matter below the topsoil is scarce.",
          "Microbial life in the subsoil is limited.",
          "Fertility in the layer below the topsoil is minimal.",
          "Living activity beneath the topsoil is slight.",
          "Crop growth in the degraded subsoil is difficult.",
          "Crop suitability in the subsoil is low.",
          "Microbial activity in the subsoil is far below healthy topsoil.",
          "The subsoil has sparse living activity.",
          "The remaining subsoil is severely degraded.",
          "The layer below the topsoil can support some growth, but poorly."
        ],
        "fresh": [
          "The subsoil holds only a trace of organic matter.",
          "Beneath the topsoil the microbial biomass is a fraction of what it was.",
          "Below the topsoil the organic carbon is down to a trace.",
          "The subsoil is starved of the organic matter a crop depends on.",
          "Biological activity in the subsoil is much lower than in living topsoil.",
          "The subsoil's structure has broken down and its fertility is poor.",
          "Beneath the topsoil the living community is thin.",
          "Crop suitability below the topsoil is greatly reduced.",
          "The subsoil is impoverished compared with the band above it.",
          "Below the topsoil there is too little organic matter to carry a crop.",
          "A seed in the subsoil would struggle for anchor and for feeding.",
          "Beneath the topsoil the biological activity is far below the living-topsoil range.",
          "The subsoil is depleted, and what growth it supports is marginal.",
          "Living activity in the subsoil is diminished rather than gone."
        ],
        "reviewerFalsePositives": [
          "The subsoil holds a small amount of biological activity.",
          "Under the topsoil fertility has dropped a long way.",
          "Beneath the topsoil growing a crop would be hard without help.",
          "Under the topsoil the biological activity has fallen sharply."
        ],
        "freshSafeProse": [
          "The subsoil supports only limited crop growth.",
          "Some organisms remain in the subsoil.",
          "A few microbes remain below the topsoil.",
          "Growth in the subsoil is possible but difficult.",
          "The subsoil is not very fertile.",
          "Fertility beneath the topsoil is somewhat reduced.",
          "Under the topsoil the organic matter has dropped away.",
          "Beneath the topsoil the living community has thinned out.",
          "The subsoil would need years of cover before it carried a crop again.",
          "Below the topsoil there is still some biological activity, just far less of it.",
          "The subsoil can support hardy plants, though not a wheat crop.",
          "Beneath the topsoil the soil has lost most of what a seed feeds on.",
          "Under the topsoil what is left is mineral, with a little organic matter mixed in.",
          "The exposed lower layer would grow a cover crop only with help."
        ],
        "bareLayerSubjectScope": [
          "The layer is degraded but not empty of life.",
          "The layer is difficult to farm.",
          "The layer contains some organisms.",
          "The layer has low fertility."
        ],
        "nonSubsoilDead": [
          "The soil analysis, at the edge of the dead field.",
          "The dead field is bare.",
          "The wheat crop is dead.",
          "Dead grass lies on the surface.",
          "Nothing grew on the dead field that year."
        ]
      }
    },
    "prohibitedFramingsRole": "DIAGNOSTIC REGISTER, RECONCILED. The eighteen phrases below are the wordings this boundary exists to refuse. They are not themselves the matcher - a phrase list cannot be completed - but the validator asserts that every one of them is caught by the concept classes above when bound to a protected subject. That reconciliation is what stops the declared contract and the enforced contract from drifting apart, which is exactly what had happened in the first candidate: these eighteen entries were declared and the validator referenced them zero times.",
    "requiredQualification": "Both learner editions must carry at least one printed reading, marked data-subsoil-reading, that says how much less rather than none. This is a POSITIVE requirement on one authored node per edition, not a vocabulary test applied to prose: approvedQualifierTerms below governs that node and nothing else. Task 4 Part C and Task 8 Claim 4 assess the boundary directly.",
    "gameResolution": "HHH-GAME-C1L5-001 is RESOLVED_VERIFIED at the integrated game baseline. The zero-life and zero-growth absolutes the Phase 1 audit rejected were replaced in the game before this package was authored, and this package neither reproduces the old wording nor relies on the game for the boundary: the readings it prints are bounded comparatives and the boundary is taught as an assessed task rather than carried as a disclaimer.",
    "internalIdentifierRule": "The runtime clue identifier for the core source is a non-player-facing internal string and was deliberately left unchanged in the game. It is prohibited from every role of this package, along with every other runtime clue tag, node id and route."
  },
  "droughtQualification": {
    "rule": "The drought is a contributing cause of the Dust Bowl in every role. It may be placed, weighed, and distinguished from the vulnerability that made it destructive. It may not be removed, dismissed, or described as irrelevant.",
    "causalRole": "condition",
    "documentedFacts": [
      "the 1930s drought ran between July 1928 and May 1942",
      "at its peak it covered at least 60 per cent of the Lower 48 States",
      "the average longest unbroken stretch at individual locations was 38.4 months, peaking in March 1935"
    ],
    "prohibitedFramings": [
      "the drought did not cause",
      "the drought was not a cause",
      "the drought was irrelevant",
      "the drought had nothing to do with",
      "the drought made no difference",
      "nothing to do with the weather",
      "the weather was not to blame",
      "it was not the drought"
    ],
    "requiredQualification": "No role may assert that the drought was not a cause of the Dust Bowl. Where the packet reports that emphasis from the runtime level, or offers it to a learner as a claim to be judged, the passage is a registered exemption and is marked as one.",
    "gameDependency": "HHH-GAME-C1L5-002 remains CURRICULUM_QUALIFICATION_REQUIRED. It is discharged structurally: the drought holds a named slot in the causal frame carried by every role, Task 3 establishes it before land use is mentioned, Task 4 Part B assigns it a named condition of the mechanism, Task 6 Part B requires the learner to say what happens without it, and Task 8 Claim 3 makes the denial itself a claim to be refused."
  },
  "landUseQualification": {
    "rule": "Land-use change is a contributing cause and is never a sufficient sole cause. The case explains a practice and a system, not the character of the people who farmed.",
    "causalRole": "vulnerability",
    "soleCauseMarkers": [
      "alone", "only", "solely", "nothing but", "entirely", "wholly",
      "the whole cause", "the sole cause", "all by itself", "by itself",
      "the only reason", "nothing else"
    ],
    "prohibitedFramings": [
      "the plough alone caused the Dust Bowl",
      "the ploughing alone explains it",
      "farmers caused the Dust Bowl",
      "the plow alone caused the Dust Bowl",
      "bad farming caused the Dust Bowl",
      "greedy farmers caused the Dust Bowl",
      "it was entirely the farmers"
    ],
    "blameRule": "The packet follows the runtime level's own better instinct here: the fault named is in the practice and the system that rewarded it, not in the individual behind the plough. The Teacher Guide states this explicitly and the rubric does not credit a moral verdict about farmers as historical reasoning.",
    "uniformityRule": "The packet does not imply that every Great Plains farmer behaved identically. Cunfer's finding that about two-thirds of the Great Plains remained in unploughed native vegetation is printed in both learner editions for exactly this reason."
  },
  "policyQualification": {
    "rule": "The conservation response addressed the vulnerability. It is never presented as an instantaneous cure, as the single cause of the end of the dust storms, or as acting on the drought.",
    "confound": "The federal conservation programme spread across the later 1930s and the rains returned to the plains at the end of the decade. Nothing printed in this packet separates their contributions.",
    "prohibitedFramings": [
      "the Soil Conservation Act ended the Dust Bowl",
      "conservation ended the Dust Bowl",
      "the law stopped the dust storms",
      "the Act stopped the dust",
      "conservation solved the problem",
      "the shelterbelts ended the drought",
      "soil conservation cured the plains"
    ],
    "requiredQualification": "Task 7 Part B and Task 8 Claim 5 both assess this. The Answer Key marks Claim 5 as undecidable from this packet and says why. Any role that states the response ended the disaster must be a registered exemption naming it as a claim under test or as a misconception.",
    "printedConfoundRequired": true,
    "printedConfoundRule": "Both learner editions must print the return of the rains on the same sequence as the conservation programme, so that the confound is visible evidence rather than a teacher's footnote."
  },
  "sourceStatusContract": {
    "rule": "Every learner-facing evidence object carries a printed STATUS line bound to a canonical source in this registry, and the game reconstruction is labelled reconstructed in every role in which it appears.",
    "statusVocabulary": ["documented", "reconstructed", "modeled", "debated"],
    "reconstructionNoticeRequired": ["student", "accessible"],
    "reconstructionNoticeRule": "Page 1 of both learner editions carries the reconstruction and causation notice, which states that the Archive's scenes were written for the game and that the case has more than one cause.",
    "prohibitedRuntimeIdentifiers": [
      "grass_plowed", "no_root_structure", "grass_control",
      "profile_stripped", "dead_soil", "conservation_answer",
      "political_contest", "soil_act", "dust_bowl_farm", "eroded_gully",
      "committee_room", "sample_core", "examine_strata", "survey_region",
      "review_testimony", "query_archive", "sample_soil", "examine_evidence",
      "survey_land", "clueTag", "revealsClue", "bonusInsight", "lockHint",
      "anchorPoint", "taaCommsHints", "resolveLabel"
    ],
    "prohibitedRuntimeIdentifierRule": "No runtime clue tag, source key, location id, node name or route may appear in any role. The core source's internal clue identifier is specifically named in the audit resolution as non-player-facing and must not become learner-facing terminology. The list holds only identifier-shaped strings: the runtime's two remaining clue tags that are ordinary English words, `extent` and `scale`, are deliberately excluded, because forbidding them would forbid the words themselves and the guard would stop protecting anything."
  },
  "claimJudgments": {
    "markScheme": {
      "Y": "the evidence in this packet supports it",
      "N": "the evidence in this packet goes against it",
      "?": "this packet cannot decide it"
    },
    "claims": [
      { "number": "1", "layer": "mechanism", "mark": "Y" },
      { "number": "2", "layer": "causation", "mark": "N" },
      { "number": "3", "layer": "causation", "mark": "N" },
      { "number": "4", "layer": "soil", "mark": "N" },
      { "number": "5", "layer": "response", "mark": "?" }
    ]
  },
  "chronology": [
    { "year": "1880-1930", "lane": "land", "entry": "Native sod is ploughed across the Great Plains: 104 million acres between 1880 and 1900, 20 million more by 1925 and 5 million more by 1930.", "source": "erosion-surveys" },
    { "year": "1928", "lane": "weather", "entry": "The drought the record treats as one long event begins in July.", "source": "drought-record" },
    { "year": "1933", "lane": "response", "entry": "A federal Soil Erosion Service is created as a temporary agency.", "source": "conservation-act", "fixedPosition": "first" },
    { "year": "1934", "lane": "land", "entry": "A Soil Conservation Service survey finds 65 per cent of Great Plains acreage wind-eroded and 15 per cent severely eroded.", "source": "erosion-surveys" },
    { "year": "1935", "lane": "response", "entry": "Hugh Hammond Bennett testifies to Congress for a soil conservation bill in the spring, while dust blown from the plains reaches Washington.", "source": "conservation-act", "dateStatus": "debated-detail" },
    { "year": "1935", "lane": "response", "entry": "On 27 April the Soil Conservation Act becomes law and makes a permanent conservation service part of the Department of Agriculture.", "source": "conservation-act" },
    { "year": "1935-1942", "lane": "response", "entry": "A federal tree-planting programme runs across a belt of the plains states.", "source": "conservation-act", "quantityStatus": "published-totals-differ" },
    { "year": "later 1930s", "lane": "response", "entry": "Local conservation districts form and cover, residue, contour ploughing and windbreaks spread across the region.", "source": "conservation-act" },
    { "year": "1938", "lane": "land", "entry": "Survey figures put 80 per cent of the southern Great Plains as affected by wind erosion, 40 per cent seriously.", "source": "erosion-surveys" },
    { "year": "1939-1941", "lane": "weather", "entry": "The rains return to the plains; the record ends the drought in May 1942.", "source": "drought-record", "fixedPosition": "last" }
  ],
  "unsettledDetails": [
    {
      "id": "bennett-testimony-date",
      "subject": "the exact date of Bennett's decisive testimony, and how far he timed it to the storm",
      "status": "debated / uncertain",
      "whatIsDocumented": "That Bennett testified in support of soil-conservation legislation in the spring of 1935, that dust blown from the plains reached Washington more than once that spring, and that the Soil Conservation Act was approved on 27 April 1935.",
      "whatIsNot": "Published accounts give different dates for the decisive appearance and differ on how far the arrival of the dust was arranged rather than fortunate. USDA's own retelling says he stalled until the dust darkened the sky; other accounts note that plains dust had already reached Washington earlier that spring while hearings were under way.",
      "rule": "No role prints an exact date for the testimony as settled. The year and the date of the Act are printed as documented, because they are. The Teacher Guide records the disagreement.",
      "printedIn": ["teacher"]
    },
    {
      "id": "shelterbelt-total",
      "subject": "the total number of trees planted by the federal shelterbelt programme",
      "status": "published totals differ",
      "whatIsDocumented": "That a federal tree-planting programme ran from 1935 to 1942 across a belt of the plains states.",
      "whatIsNot": "Published totals for the number of trees planted differ substantially between accounts.",
      "rule": "No role prints a total. The programme is printed by its dates and its purpose.",
      "printedIn": ["teacher"]
    }
  ],
  "editionResponseContract": {
    "rule": "Every learner response control in either edition belongs to exactly one assessed subpart, and every subpart declares what each edition is obliged to produce. Parity is checked against these canonical obligations rather than against prose, so an Accessible edition cannot acquire a required response the Student edition never asks for.",
    "whyItExists": "The first Case 05 candidate did exactly that: the Accessible edition asked for the feedback relation as its Part B while the Student edition was given the same relation on the map. That is a fifth, undeclared, demand-INCREASING adaptation, and no text-level check caught it. Comparing declared obligations per subpart does.",
    "differenceClasses": {
      "parity": "Both editions produce the same number of responses for the same obligation.",
      "declared-reduction": "The Accessible edition produces fewer, under a registered entry in accessibleAdaptations. This is a scored difference and must be disclosed to the teacher and the key.",
      "chunking": "The Accessible edition splits one Student field into several, or merges none, with an identical assessed obligation. Support under the Accessible Adaptation Contract; not a scored difference, because nothing more is demanded.",
      "accessible-only": "PROHIBITED. A required Accessible response with no Student counterpart is a demand increase and fails validation."
    },
    "subparts": [
      { "task": "C05-T1", "id": "vocabulary-placements", "obligation": "Place six exact-match terms.", "student": ["t1-term-1","t1-term-2","t1-term-3","t1-term-4","t1-term-5","t1-term-6"], "accessible": ["a1-term-1","a1-term-2","a1-term-3","a1-term-4","a1-term-5","a1-term-6"], "differenceClass": "parity" },
      { "task": "C05-T2", "id": "first-explanation", "obligation": "One provisional explanation and one named check.", "student": ["t2-first","t2-check"], "accessible": ["a2-first","a2-check"], "differenceClass": "parity" },
      { "task": "C05-T3", "id": "band-placements", "obligation": "Place three statements against the three bands.", "student": ["t3-band-1","t3-band-2","t3-band-3"], "accessible": ["a3-band-1","a3-band-2","a3-band-3"], "differenceClass": "parity" },
      { "task": "C05-T3", "id": "drought-span", "obligation": "State the drought's span and the longest unbroken stretch.", "student": ["t3-span"], "accessible": ["a3-span"], "differenceClass": "parity" },
      { "task": "C05-T3", "id": "scale-gap", "obligation": "Explain why the drought record alone does not explain the soil loss.", "student": ["t3-gap"], "accessible": ["a3-gap"], "differenceClass": "parity" },
      { "task": "C05-T4", "id": "transport-stages", "obligation": "Complete the two open transport stages.", "student": ["t4-stage-2","t4-stage-4"], "accessible": ["a4-stage-2","a4-stage-4"], "differenceClass": "parity" },
      { "task": "C05-T4", "id": "condition-assignment", "obligation": "Assign one wind-erosion condition to land use and a different one to the drought.", "student": ["t4-cond-landuse","t4-cond-drought"], "accessible": ["a4-cond-landuse","a4-cond-drought"], "differenceClass": "parity" },
      { "task": "C05-T4", "id": "subsoil-boundary", "obligation": "State what the core readings do and do not establish.", "student": ["t4-sub-does","t4-sub-not"], "accessible": ["a4-sub-does","a4-sub-not"], "differenceClass": "parity" },
      { "task": "C05-T5", "id": "comparison-cells", "obligation": "Complete the fence-line comparison.", "student": ["t5-cover-field","t5-cover-strip","t5-roots-field","t5-roots-strip","t5-dry-field","t5-dry-strip","t5-soil-field","t5-soil-strip","t5-wind-field","t5-wind-strip"], "accessible": ["a5-roots-field","a5-roots-strip","a5-dry-field","a5-dry-strip","a5-soil-field","a5-soil-strip","a5-wind-field","a5-wind-strip"], "differenceClass": "declared-reduction", "governedBy": "t5-modelled-cover-row" },
      { "task": "C05-T5", "id": "control-establishes", "obligation": "State what the comparison establishes.", "student": ["t5-establishes"], "accessible": ["a5-establishes"], "differenceClass": "parity" },
      { "task": "C05-T5", "id": "control-limits", "obligation": "State what it cannot establish and the regional check needed.", "student": ["t5-limits"], "accessible": ["a5-limits"], "differenceClass": "parity" },
      { "task": "C05-T6", "id": "factor-placements", "obligation": "Place the factor cards in the four causal roles.", "student": ["t6-cond-1","t6-cond-2","t6-vuln-1","t6-vuln-2","t6-mech-1","t6-mech-2","t6-resp-1","t6-resp-2"], "accessible": ["a6-cond-2","a6-vuln-1","a6-vuln-2","a6-mech-1","a6-mech-2","a6-resp-2"], "differenceClass": "declared-reduction", "governedBy": "t6-preplaced-factors" },
      { "task": "C05-T6", "id": "removal-test", "obligation": "Answer both removal tests: what happens to the dust without the condition, and without the vulnerability.", "student": ["t6-remove"], "accessible": ["a6-remove-cond","a6-remove-vuln"], "differenceClass": "chunking", "chunkingNote": "One Student field collects both halves; the Accessible edition asks for them as two steps. The assessed obligation is identical and the Answer Key models both halves for both editions." },
      { "task": "C05-T6", "id": "map-limit", "obligation": "Name one thing the map does not explain, using the migration record.", "student": ["t6-limit"], "accessible": ["a6-limit"], "differenceClass": "parity" },
      { "task": "C05-T7", "id": "sequence-order", "obligation": "Order the four middle entries.", "student": ["t7-slot-2","t7-slot-3","t7-slot-4","t7-slot-5"], "accessible": ["a7-slot-2","a7-slot-3","a7-slot-4","a7-slot-5"], "differenceClass": "parity", "supportNote": "The Accessible rail repeats each slot's date under t7-fixed-ends. That changes the route, not the number of responses, so it is not a field-count difference." },
      { "task": "C05-T7", "id": "policy-confound", "obligation": "Explain why the timeline cannot credit the Act alone.", "student": ["t7-confound"], "accessible": ["a7-confound"], "differenceClass": "parity" },
      { "task": "C05-T8", "id": "claim-marks", "obligation": "Mark five claims Y, N or question mark.", "student": ["t8-mark-1","t8-mark-2","t8-mark-3","t8-mark-4","t8-mark-5"], "accessible": ["a8-mark-1","a8-mark-2","a8-mark-3","a8-mark-4","a8-mark-5"], "differenceClass": "parity", "supportNote": "The Accessible claims carry source pointers under t8-source-pointers. That names where to look, not what to write, and changes no response count." },
      { "task": "C05-T8", "id": "settle-undecided", "obligation": "Name evidence that would settle the undecided claim.", "student": ["t8-settle"], "accessible": ["a8-settle"], "differenceClass": "parity" },
      { "task": "C05-T9", "id": "culminating-explanation", "obligation": "Write the four-part qualified multi-causal explanation.", "student": ["t9-explanation"], "accessible": ["a9-explanation"], "differenceClass": "parity" }
    ],
    "identityFields": { "student": ["student-name","student-date","student-class"], "accessible": ["a-name","a-date","a-class"] }
  },
  "accessibleAdaptations": [
    {
      "id": "t5-modelled-cover-row",
      "task": "C05-T5",
      "what": "The first comparison row, cover, is supplied complete on both sides as a worked model.",
      "effect": "The Accessible learner completes four rows and eight cells independently; the Student learner completes five rows and ten cells.",
      "whyNotALeak": "The row that carries the reasoning is the drought row, where the learner has to write the same dry years into both columns, and that row is the learner's. The modelled row shows what a filled cell looks like.",
      "declaredIn": ["accessible", "teacher", "answer"]
    },
    {
      "id": "t6-preplaced-factors",
      "task": "C05-T6",
      "what": "Two of the eight factor cards are pre-placed in the map as worked models, one in the condition role and one in the response role.",
      "effect": "The Accessible learner places six factors independently rather than eight. Both removal answers and the limit of the map remain entirely the learner's, and are the same two assessed parts the Student edition requires.",
      "whyNotALeak": "One card is placed in each of two different roles, so no role is completed for the learner and the condition-against-vulnerability judgement the task assesses is untouched.",
      "declaredIn": ["accessible", "teacher", "answer"]
    },
    {
      "id": "t7-fixed-ends",
      "task": "C05-T7",
      "what": "The first and last entries of the policy sequence are fixed in both editions; the Accessible edition additionally supplies the four middle entries as dated cards rather than undated ones.",
      "effect": "Ordering becomes a matching operation rather than a recall operation for the Accessible learner. Part B, which is the assessed reasoning, is unchanged.",
      "whyNotALeak": "Part B asks what the timeline cannot show. Knowing the dates does not answer it.",
      "declaredIn": ["accessible", "teacher", "answer"]
    },
    {
      "id": "t8-source-pointers",
      "task": "C05-T8",
      "what": "Each claim carries a printed pointer to the source that bears on it.",
      "effect": "The Accessible learner is told where to look and is never told what to write.",
      "whyNotALeak": "The pointer names a source. The mark is still a judgement about what that source establishes.",
      "declaredIn": ["accessible", "teacher"]
    }
  ],
  "semanticInvariants": {
    "scanScope": {
      "roles": ["student", "teacher", "answer", "accessible"],
      "unit": "sentence",
      "rule": "Every sentence in every role is scanned, together with the accessibility text of every figure, unless the node carries a registered exemption id. Exemption is granted only by the closed contract below: markup cannot self-authorize, and every registered exemption declares its roles, its selector and its expected count.",
      "exemptionAttribute": "data-semantic-exemption",
      "designNote": "These guards are deliberately narrow. Each protects one curricular boundary by policing a closed class of absolute or sole-cause language bound to a named subject, plus a positive structural requirement that the correct framing is actually present. None of them attempts to recognise every English paraphrase of a wrong idea, and none of them depends on enumerating synonyms for an ordinary verb."
    },
    "exemptions": [
      {
        "id": "claim-under-test-learner",
        "roles": ["student", "accessible"],
        "selector": ".account-item[data-semantic-exemption=\"claim-under-test-learner\"]",
        "purpose": "Task 8 claims are propositions offered to the learner for judgment, not assertions of the packet.",
        "allowedConcepts": ["subsoil", "drought", "landuse", "policy"]
      },
      {
        "id": "claim-under-test-key",
        "roles": ["answer"],
        "selector": "[data-semantic-exemption=\"claim-under-test-key\"]",
        "purpose": "The Answer Key restates each competing claim beside the mark that decides it.",
        "allowedConcepts": ["subsoil", "drought", "landuse", "policy"]
      },
      {
        "id": "teacher-misconception",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"teacher-misconception\"]",
        "purpose": "The Teacher misconceptions table and the prose warnings name an error in order to reject it.",
        "allowedConcepts": ["subsoil", "drought", "landuse", "policy"]
      },
      {
        "id": "teacher-rubric-floor",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"teacher-rubric-floor\"]",
        "purpose": "Rubric descriptors that quote the disqualifying answer in order to place a floor under it.",
        "allowedConcepts": ["subsoil", "drought", "landuse", "policy"]
      },
      {
        "id": "answer-key-floor",
        "roles": ["answer"],
        "selector": "[data-semantic-exemption=\"answer-key-floor\"]",
        "purpose": "Answer Key floors that quote the answer they refuse to accept at any level.",
        "allowedConcepts": ["subsoil", "drought", "landuse", "policy"]
      },
      {
        "id": "game-wording-reported",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"game-wording-reported\"]",
        "purpose": "Places where the runtime level's own emphasis is reported so the teacher can qualify it after play.",
        "allowedConcepts": ["drought"]
      },
      {
        "id": "learner-refutation-prompt",
        "roles": ["student", "accessible"],
        "selector": "[data-semantic-exemption=\"learner-refutation-prompt\"]",
        "purpose": "Prompts that quote a wrong reading and ask the learner to refuse it using the printed evidence.",
        "allowedConcepts": ["subsoil", "drought", "policy"]
      },
      {
        "id": "boundary-notice",
        "roles": ["student", "accessible"],
        "selector": "[data-causation-boundary][data-semantic-exemption=\"boundary-notice\"]",
        "purpose": "The page-1 notice names the overcorrection in order to warn a learner away from it. It is the one place in a learner edition that has to say the wrong thing out loud.",
        "allowedConcepts": ["drought", "landuse"]
      },
      {
        "id": "audit-wording-reported",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"audit-wording-reported\"]",
        "purpose": "Passages that name the wording the Phase 1 audit rejected, in order to record that it was rejected and corrected.",
        "allowedConcepts": ["subsoil"]
      },
      {
        "id": "vocabulary-term-list",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"vocabulary-term-list\"]",
        "purpose": "An enumeration of the case vocabulary is a term list, not a claim about any term in it.",
        "allowedConcepts": ["subsoil", "drought", "landuse", "policy"]
      }
    ],
    "structuralExemptSelectors": [
      { "selector": ".word-bank", "why": "a word bank is a list of terms offered for placement; it asserts nothing about any of them" },
      { "selector": ".factor-bank", "why": "the Task 6 factor bank is a list of cards to be sorted; a card states a fact about one factor and makes no causal claim about the whole" }
    ],
    "subsoil": {
      "policy": "FAIL_CLOSED_ON_ZERO_CLASSES",
      "enforcedRoles": ["student", "teacher", "answer", "accessible"],
      "enforcedRolesRule": "Both rules apply in all four roles. The declared scope once read 'a learner or key role' while the implementation already covered Teacher as well; the wording was the thing that was wrong, and it has been corrected to match. Teacher prose that names the prohibited claim in order to reject it passes through the registered exemption mechanism, not through a narrower scope.",
      "policyRule": "A non-exempt sentence naming a subsoil subject together with a life-or-growth predicate must carry an approved bounded qualifier. An absolute term from the closed list below fails outright. The prohibited class here is genuinely closed - absolutes are a small finite class in English, unlike synonyms for an ordinary verb - which is why this guard converges where an open blacklist would not.",
      "subjectTerms": [
        "subsoil", "sub-soil", "the ground below", "the ground beneath",
        "below the topsoil", "beneath the topsoil", "under the topsoil",
        "what is left below", "the pale sand", "the sand below",
        "the mineral layer", "the layer below", "the lower layer",
        "the lower soil layer", "the exposed lower layer", "the core",
        "the gully floor"
      ],
      "subjectPatterns": [
        "\\bsub-?soil\\b",
        "\\b(?:below|beneath|under|underneath)\\b[^.]{0,40}?\\btopsoil\\b",
        "\\bthe ground (?:below|beneath|underneath)\\b",
        "\\bthe (?:pale |mineral |starved |exposed )?(?:sand|layer|soil layer) below\\b",
        "\\bthe\\s+(?=(?:exposed|lower|soil)\\b)(?:exposed\\s+)?(?:lower\\s+)?(?:soil\\s+)?layer\\b",
        "\\bthe mineral layer\\b",
        "\\bgully floor\\b"
      ],
      "subjectModifierRule": "The layer pattern requires AT LEAST ONE modifier - exposed, lower or soil - enforced by a lookahead rather than by making every group optional. With all three optional the pattern silently reduced to bare 'the layer', which is not the protected subsoil subject at all, and it began rejecting the truthful sentence 'the layer is degraded but not empty of life'. The fix belongs in the subject scope, not in the negation vocabulary: widening negations would have hidden an over-broad subject instead of correcting it.",
      "subjectPatternRule": "The protected subject is declared HERE, not in the validator. It used to be a module-level regex constant in the test file - a second authority of exactly the kind this contract exists to prevent - and it silently excluded ordinary names for the same layer, so 'nothing can grow in the lower soil layer' fell outside the guard entirely. subjectTerms above stays as the readable register; subjectPatterns is what compiles.",
      "predicateTerms": [
        "life", "living", "lives", "live", "alive", "biological", "biology",
        "microbial", "microbes", "organism", "organisms", "activity",
        "grow", "grows", "grown", "growing", "growth", "crop", "crops",
        "organic matter", "organic carbon", "fertility", "fertile"
      ],
      "absoluteTermsRemoved": "The hand-maintained absolute list that used to sit here is gone. It was a second authority beside subsoilBoundary.prohibitedFramings and the two could drift apart silently - they had. The enforced matcher is now built from subsoilBoundary.prohibitedConceptClasses, and that block is the only authority.",
      "approvedQualifierTerms": [
        "a trace", "trace", "traces", "far below", "well below", "below the range",
        "a fraction", "fraction of", "much less", "far less", "greatly reduced",
        "severely reduced", "severely degraded", "sharply lower", "lower than",
        "poor in", "starved", "too little", "far too little", "not enough",
        "how much less", "reduced", "diminished", "depleted", "thin", "little left"
      ],
      "retiredBoundedGate": "A blocking rule once required any life-or-growth claim about the protected layer to contain a listed comparative adjective, and a finite family list decided which. It was retired by PMO decision after repeated review rounds proved it could not converge: there are indefinitely many truthful ways to say a layer holds less, and each round found more safe prose it rejected - a small amount, has dropped, hard without help, has fallen sharply. Safety was never coming from that list. It comes from the zero classes, which are closed and enforceable. Truthful prose is no longer required to prove itself by vocabulary; it is protected instead by the must-pass regression corpus, which demonstrates the zero classifier does not overmatch.",
      "negationTerms": [
        "not dead", "is not dead", "are not dead", "not lifeless", "not sterile",
        "does not mean nothing", "do not mean nothing", "not that nothing",
        "rather than none", "not none", "says how much less", "not zero",
        "goes past the evidence", "beyond what the readings", "the readings do not say",
        "cannot be read as", "is wrong", "are wrong", "incorrect", "not accepted",
        "do not establish", "does not establish", "not establish",
        "do not measure", "does not measure", "is not none", "not zero",
        "gone further than", "not dead", "degraded, not"
      ],
      "positiveRequirement": {
        "rule": "Both learner editions must print at least one bounded reading of the subsoil, and Task 4 Part C must be present in both, so that the boundary is taught rather than merely policed.",
        "requiredAttribute": "data-subsoil-reading",
        "requiredRoles": ["student", "accessible", "answer"],
        "minimumPerRole": 1
      },
      "rules": [
        "ZERO-CLASS, AND IT IS THE WHOLE BLOCKING CONTRACT: a proposition naming a subsoil subject together with any biological-zero or universal-growth-zero concept fails. No second life-or-growth token is required, because the concept classes already carry that meaning. It clears only through a registered exemption or an explicit clearing term.",
        "NO SAFE-VOCABULARY REQUIREMENT: a proposition that carries no prohibited zero concept passes. It does not have to contain a listed comparative adjective, and it is never failed for describing the layer in wording this contract has not seen before.",
        "SUBJECT SCOPE: the rule applies only to the protected subject - the subsoil, the ground below or beneath the topsoil, and the exposed lower layer. The adjective dead applied to anything else, including a dead field at the surface, is outside this contract and is not a violation of it."
      ]
    },
    "drought": {
      "policy": "FAIL_CLOSED_ON_DENIAL_PLUS_STRUCTURAL_PRESENCE",
      "policyRule": "Two guards, one negative and one positive. The negative one polices a closed class: denials that the drought was a cause. The positive one is structural and is the one that actually carries the audit requirement - every role must place the drought in the condition role of the causal frame, and the culminating prompt and the rubric must require it.",
      "subjectTerms": ["drought", "the dry years", "the rains failed", "lack of rain", "the weather", "rainfall"],
      "denialPattern": "\\b(?:drought|dry years|weather|rains?)\\b[^.]{0,60}?\\b(?:did not|didn't|does not|was not|were not|wasn't|weren't|had nothing|has nothing|no part|not a cause|not the cause|irrelevant|made no difference|no difference|not to blame|nothing to do)",
      "denialRule": "A sentence matching the denial pattern asserts that the drought was not a cause. It fails unless it is a registered exemption - a claim offered for judgment, a misconception being named, or the runtime level's emphasis being reported so a teacher can qualify it - or unless it carries a clearing term below.",
      "negationTerms": [
        "on its own", "alone does not", "alone cannot", "alone is not",
        "by itself", "does not show", "do not show", "did not show",
        "neither says", "neither argues", "not yet", "is wrong", "are wrong",
        "incorrect", "not accepted", "cannot be credited", "two causes",
        "one of two", "still a cause", "remains a cause", "has drawn the opposite",
        "without the drought", "without the dry years", "had there been no drought"
      ],
      "negationRule": "A statement of INSUFFICIENCY is not a denial, and neither is a COUNTERFACTUAL REMOVAL. 'The drought on its own does not explain the soil loss' is the correct history and the thing this case teaches; 'the drought was not a cause' is the error. The clearing terms above separate the two, so the guard polices denial rather than qualification. 'Without the drought the soil stays damp enough to hold together' is the removal test Task 6 Part B assesses: it is the strongest possible affirmation that the drought was a cause, and a guard that failed it would be punishing the packet for teaching the thing the audit asked for.",
      "positiveRequirement": {
        "rule": "Every role must carry the drought in the condition role of the causal frame, identified in markup rather than inferred from prose.",
        "requiredAttribute": "data-causal-role",
        "requiredValue": "condition",
        "requiredRoles": ["student", "teacher", "answer", "accessible"],
        "minimumPerRole": 1,
        "subjectMustMatch": "drought"
      },
      "figureParityRule": "The causation map's accessibility text must name the drought in the condition role, so that a reader using the text rather than the drawing meets the same four-role frame."
    },
    "landuse": {
      "policy": "FAIL_CLOSED_ON_SOLE_CAUSE",
      "policyRule": "A sentence that names a land-use subject, a sole-cause marker and a Dust Bowl outcome asserts that land use was the whole cause. It fails unless registered. The marker class is closed and small; this guard does not attempt to police every way of overstating a cause, only the explicit sole-cause construction the audit warns about.",
      "subjectTerms": [
        "plough", "plow", "ploughing", "plowing", "ploughed", "plowed",
        "farming", "farmers", "the farmer", "land use", "land-use",
        "breaking the sod", "broke the sod", "sod", "wheat", "cultivation"
      ],
      "soleCauseTerms": [
        "alone", "only", "solely", "nothing but", "entirely", "wholly",
        "the whole cause", "the sole cause", "all by itself", "by itself",
        "on its own", "the only reason", "the only cause", "nothing else", "purely"
      ],
      "outcomeTerms": [
        "dust bowl", "the dust", "the disaster", "the catastrophe",
        "the storms", "dust storms", "the soil blew", "the erosion",
        "what happened"
      ],
      "negationTerms": [
        "not alone", "not the only", "not the whole", "not solely",
        "more than one", "both", "together with", "as well as",
        "did not act alone", "no single cause", "not by itself", "is wrong", "are wrong"
      ],
      "positiveRequirement": {
        "rule": "Every role must carry the land-use factor in the vulnerability role of the causal frame, so that it is present as one named cause among four rather than as the case's verdict.",
        "requiredAttribute": "data-causal-role",
        "requiredValue": "vulnerability",
        "requiredRoles": ["student", "teacher", "answer", "accessible"],
        "minimumPerRole": 1
      },
      "blameRule": "No role may attribute the Dust Bowl to the character, intelligence or morals of the farmers. The Teacher Guide states the distinction between a practice and a person, and the rubric does not credit a moral verdict as historical reasoning."
    },
    "policy": {
      "policy": "FAIL_CLOSED_ON_SINGLE_CAUSE_CURE",
      "policyRule": "A sentence naming a conservation-response subject together with a termination predicate asserts that the response ended the disaster. It fails unless registered as a claim under test, a misconception, or an explicitly refused reading.",
      "subjectTerms": [
        "soil conservation act", "the act", "the law", "conservation",
        "the service", "soil conservation service", "shelterbelt", "shelterbelts",
        "contour plowing", "contour ploughing", "the programme", "the program",
        "the response", "windbreaks", "cover crops"
      ],
      "terminationTerms": [
        "ended", "end the", "ends the", "to an end", "stopped", "stop the",
        "stops the", "put an end", "brought an end", "finished", "cured", "cure",
        "solved", "solve the", "saved the plains", "eliminated", "wiped out",
        "made it stop"
      ],
      "terminationTermsNote": "The verbs 'fixed' and 'fix' were deliberately removed from this class. They collide with ordinary English about a diagram - an entry FIXED as the last on a rail - and 'cured' and 'solved' already cover the claim the guard exists to catch. A guard that fires on its own documentation stops being read.",
      "negationTerms": [
        "cannot say", "cannot show", "does not show", "do not show", "cannot separate",
        "cannot tell", "not proof", "is not evidence", "also returned",
        "at the same time", "both changed", "this packet cannot",
        "does not settle", "cannot decide", "undecided", "is wrong", "are wrong",
        "not accepted", "would need"
      ],
      "positiveRequirement": {
        "rule": "Both learner editions must print the return of the rains on the same sequence as the conservation programme, identified in markup, so the confound is visible evidence.",
        "requiredAttribute": "data-policy-confound",
        "requiredRoles": ["student", "accessible", "answer", "teacher"],
        "minimumPerRole": 1
      }
    },
    "sourceStatus": {
      "policy": "STRUCTURAL",
      "policyRule": "Structural rather than lexical. Every learner-facing evidence object must declare a canonical source id and print a STATUS line whose leading word is one of the four status words the registry declares; the game reconstruction must print reconstructed in every role that carries it; and no runtime identifier may appear anywhere.",
      "statusVocabulary": ["documented", "reconstructed", "modeled", "debated"],
      "boundAttribute": "data-source-id",
      "reconstructionSourceId": "archive-plains",
      "reconstructionRequiredStatusWord": "reconstructed",
      "prohibitedIdentifierSource": "sourceStatusContract.prohibitedRuntimeIdentifiers",
      "figureParityRule": "Every figure that is itself a status-bearing source prints its STATUS line above the drawing and names its canonical source id, and its accessibility text carries the same status word."
    }
  },
  "figureAccessibilityContract": {
    "rule": "Critical figure accessibility text carries the same distinctions the visible figure carries. It is checked against canonical registry metadata, not against one hard-coded sentence.",
    "figures": [
      {
        "id": "causation-map",
        "selector": "[data-causation-contract]",
        "roles": ["student", "accessible"],
        "requiresAllCausalRoles": true,
        "requiresFeedbackRelation": true,
        "requiresNoWeightStatement": true,
        "prohibitedPatterns": [
          { "id": "ranked-arrows", "regex": "(?:main|primary|chief|biggest|largest|strongest|real)\\s+cause", "why": "the map assigns no rank and no source in this packet supplies one" },
          { "id": "percentage-weighting", "regex": "\\d{1,3}\\s*(?:%|per cent|percent)\\s+(?:of\\s+)?(?:the\\s+)?(?:cause|blame|responsibility)", "why": "no source apportions the causes numerically" }
        ]
      },
      {
        "id": "erosion-system",
        "selector": "[data-erosion-contract]",
        "roles": ["student", "accessible"],
        "requiresBoundedSubsoilReading": true,
        "requiresAllTransportModes": ["saltation", "creep", "suspension"],
        "requiresAllConditions": 4,
        "prohibitedPatterns": [
          { "id": "absolute-subsoil-aria", "regex": "(?:dead|lifeless|sterile|no life|nothing (?:can )?(?:live|grow))", "why": "the accessibility text must carry the same bounded comparatives the visible readings carry" }
        ]
      },
      {
        "id": "policy-sequence",
        "selector": "[data-sequence-contract]",
        "roles": ["student", "accessible"],
        "requiresRainReturnEntry": true,
        "prohibitedPatterns": [
          { "id": "act-ended-it", "regex": "(?:act|law|conservation|service)[^.]{0,40}(?:ended|stopped|cured|solved)[^.]{0,30}(?:dust|drought|disaster)", "why": "the sequence orders events and does not evaluate them" }
        ]
      },
      {
        "id": "region-diagram",
        "selector": "[data-region-contract]",
        "roles": ["student", "accessible"],
        "requiresSchematicDisclaimer": true,
        "prohibitedPatterns": [
          { "id": "false-precision", "regex": "(?:exactly|precisely)\\s+\\d", "why": "a schematic of relative position supports no exact quantity" }
        ]
      }
    ]
  },
  "standards": {
    "directlyAssessed": [
      "C3 D2.His.14.6-8",
      "CCSS RH.6-8.1",
      "CCSS RH.6-8.7"
    ],
    "supporting": [
      "C3 D2.His.1.6-8",
      "C3 D3.2.6-8",
      "CCSS RH.6-8.9",
      "CCSS WHST.6-8.2"
    ],
    "contextual": [
      "NGSS MS-ESS3-1",
      "NGSS MS-ESS2-4"
    ],
    "ngss": "Both NGSS references are contextual only. Tasks 4 and 6 do reason about a surface process and about human impact on an Earth system, but the assessed product is a qualified multi-causal historical explanation with source qualification, not a science or engineering practice, and no investigation, model construction or data analysis of the kind those performance expectations describe is performed. No NGSS alignment is claimed as directly assessed."
  }
};
