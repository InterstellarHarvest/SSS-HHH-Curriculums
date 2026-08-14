window.HHH_CASE03_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C1-CASE03",
  "runtimeId": "L3",
  "instructionalType": "CORE_CASE",
  "title": "County Cork",
  "displayLabel": "3 - County Cork",
  "version": "0.1",
  "status": "VALIDATION_BUILD",
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "editorShell": "1.0",
  "gameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
  "auditBaseline": "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md",
  "staticContentInventory": "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json",
  "blueprint": "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
  "roles": {
    "student": 8,
    "teacher": 7,
    "answer": 6,
    "accessible": 13
  },
  "culminatingProduct": "Multi-causal historical explanation that names the biological trigger, identifies more than one historically supported condition, explains how at least two of them interacted, and states what the evidence cannot settle. Canonical CER is deliberately not used; see the Teacher Guide reasoning architecture.",
  "tasks": [
    {
      "id": "C03-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Case Vocabulary",
      "description": "Apply the six case terms to the things, people and actions they name rather than copying definitions.",
      "instructionalPurpose": "Establish the six terms the case is unreadable without, and set up the blight-against-famine opposition the whole case turns on without revealing how the gap between them is closed.",
      "provenance": [
        "Curriculum-authored definitions",
        "Audit-recorded case vocabulary set"
      ],
      "responseType": "six exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared six-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-cork-01",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-cork-01"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C03-T2",
      "number": "2",
      "semanticLabel": "FIRST READING",
      "icon": "ph-diagnosis",
      "title": "Record a First Explanation",
      "description": "Write down the explanation you already hold, and name one thing you would have to find out before trusting it.",
      "instructionalPurpose": "Provisional interpretation recorded before the evidence arrives. Most learners write a single-cause answer here, and the case is designed so they revise it themselves at Task 4 rather than being corrected.",
      "provenance": [
        "Game reconstruction of a ruined potato field",
        "Curriculum-authored prompt"
      ],
      "responseType": "two short constructed responses",
      "answerScope": "One provisional explanation of the deaths and one named check that would have to come from outside the scene.",
      "pagePlacement": {
        "student": "student-cork-03",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-cork-05"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C03-T3",
      "number": "3",
      "semanticLabel": "WHEN AND WHERE",
      "icon": "ph-flow",
      "title": "Put the Failures in Order",
      "description": "Read the timeline and the place diagram, then say which year was worst and what the repeat failures meant for a family with no store of food.",
      "instructionalPurpose": "Family H2 chronology and Family H3 place figure. Establishes that this was not one bad harvest but a run of them, which is the condition that turns a hungry season into a demographic catastrophe, and fixes the case in a named county rather than a vague Ireland.",
      "provenance": [
        "Ronsijn and Vanhaute crop-loss figures for 1845 and 1846",
        "Gray chronology of relief measures",
        "Curriculum-created timeline and place figure"
      ],
      "responseType": "one marked selection plus two short constructed responses",
      "answerScope": "The worst crop year read from the timeline, one consequence of failure repeating for a household that eats what it grows, and the county the case is set in read from the place figure.",
      "pagePlacement": {
        "student": "student-cork-03",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-02",
        "accessible": "accessible-cork-06"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C03-T4",
      "number": "4",
      "semanticLabel": "THE TRIGGER",
      "icon": "ph-wrench",
      "title": "Trace the Blight, Then Test It",
      "description": "Complete the middle of the path from spore to ruined field, then use the two-country comparison to say what the blight does and does not explain.",
      "instructionalPurpose": "The hinge of the case. Part A teaches the documented biological mechanism properly. Part B is a real historical control: the same pathogen struck Belgium in the same year and destroyed a larger share of its potato crop, and Belgian famine mortality was a fraction of Ireland's. That comparison, not a disclaimer, is what refutes the blight as a sufficient explanation.",
      "provenance": [
        "University of Minnesota Extension late blight guidance",
        "Coomber, Saville and Ristaino 2024 on Phytophthora infestans",
        "Ronsijn and Vanhaute comparative crop-loss and mortality figures",
        "Curriculum-created stage path and comparison panel"
      ],
      "responseType": "three organizer stages plus one explanation",
      "answerScope": "The spore landing and infecting, the sporulation and re-release, the tuber rot, and an explanation using the Belgium comparison to show that the size of the crop loss does not by itself set the size of the death toll.",
      "pagePlacement": {
        "student": "student-cork-04",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-02",
        "accessible": "accessible-cork-07"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C03-T5",
      "number": "5",
      "semanticLabel": "SOURCE STATUS",
      "icon": "ph-scales",
      "title": "Decide What Each Source Can Show",
      "description": "For each of the five kinds of evidence in this case, name its status and state what it contributes and what it cannot establish on its own.",
      "instructionalPurpose": "Family H4 contribution-and-limitation matrix across five different evidentiary statuses. Rows one and two are the pair the case exists to separate: written-for-the-game dialogue and a real published eyewitness letter are not the same kind of thing, and no learner may treat them as one.",
      "provenance": [
        "Game reconstruction at the integrated game baseline",
        "Cummins letter, The Times, 24 December 1846",
        "Bourke 1976 and Kinealy on the food-export record",
        "Curriculum-created matrix"
      ],
      "responseType": "five-row status, contribution and limitation matrix",
      "answerScope": "Fifteen bounded cells; the five rows must carry five different statuses and five different limits.",
      "pagePlacement": {
        "student": "student-cork-05",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-03",
        "accessible": "accessible-cork-09"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C03-T6",
      "number": "6",
      "semanticLabel": "HOW THE CAUSES MEET",
      "icon": "ph-nodes",
      "title": "Work the Causes Map",
      "description": "Use the causes map to explain how two conditions made each other worse, and why the map needs more boxes than the blight.",
      "instructionalPurpose": "Family H5 multiple-causation map, and the operation the whole case is built to teach. Listing causes is not multiple causation; interaction is. Part A assesses interaction between two named conditions and Part B assesses why the trigger alone is insufficient, using the Task 4 comparison as evidence rather than assertion.",
      "provenance": [
        "O'Keeffe and Reilly on dependence, cottier tenure and land",
        "Kinealy and Bourke on food leaving Ireland",
        "Gray and O'Keeffe on relief timing and the Gregory clause",
        "Curriculum-created causes map"
      ],
      "responseType": "two marked condition selections plus two explanations",
      "answerScope": "Two named conditions from the map, an explanation of how one made the other worse, and an explanation of what an account keeping only the blight box would fail to explain.",
      "pagePlacement": {
        "student": "student-cork-06",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-04",
        "accessible": "accessible-cork-10"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C03-T7",
      "number": "7",
      "semanticLabel": "COMPETING CLAIMS",
      "icon": "ph-diagnosis",
      "title": "Weigh Five Claims",
      "description": "Mark five claims about the famine against the evidence in this packet, then say what would be needed to settle the one you could not decide.",
      "instructionalPurpose": "Competing interpretations with three marks rather than two. Claim 4 is the export claim, and it is undecidable here on purpose: the packet carries both published positions and the reason the official trade returns cannot settle between them. A learner who marks it Y or N has taken a side the evidence does not support.",
      "provenance": [
        "Bourke 1976 grain-trade tabulation",
        "Kinealy on the limits of the official returns",
        "Gray on relief timing and its consequences",
        "Curriculum-created claims"
      ],
      "responseType": "five marked judgments plus one short constructed response",
      "answerScope": "Two supported claims, two contradicted claims, one claim this packet cannot decide, and a named kind of evidence that would move the undecided claim.",
      "pagePlacement": {
        "student": "student-cork-07",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-05",
        "accessible": "accessible-cork-11"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C03-T8",
      "number": "8",
      "semanticLabel": "MULTI-CAUSAL EXPLANATION",
      "icon": "ph-book",
      "title": "Explain How a Crop Failure Became a Famine",
      "description": "Write the case's explanation, using specific sourced evidence, at least two conditions, one interaction, and one stated limit.",
      "instructionalPurpose": "Culminating product for the case: a multi-causal historical explanation. A correct account of the pathogen followed by a list of other factors is not proficient; the explanation must show conditions acting on each other and must say what the evidence does not settle.",
      "provenance": [
        "Curriculum-authored prompt",
        "Blueprint culminating-product policy"
      ],
      "responseType": "extended constructed response with four required parts",
      "answerScope": "What the blight did and what it explains, two conditions with named sourced evidence, one explained interaction between conditions, and one thing the evidence cannot settle followed by a closing sentence pitched at the right strength.",
      "pagePlacement": {
        "student": "student-cork-08",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-06",
        "accessible": "accessible-cork-12"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C03-T9",
      "number": "9",
      "semanticLabel": "NEW SITUATION",
      "icon": "ph-ticket",
      "title": "Tell a Crop Failure from a Famine",
      "description": "Read a made-up report of a crop failure somewhere else, and name what you would have to find out before you could say whether it became a famine.",
      "instructionalPurpose": "Transfer rather than recall. The report is invented and labelled as such, so no dossier card answers it and the case's own conclusion cannot be restated in place of reasoning. It measures whether the learner has acquired the operation itself: that a crop failure is a question about plants and a famine is a question about people, food access and response.",
      "provenance": [
        "Curriculum-authored transfer report",
        "Blueprint transfer and exit policy"
      ],
      "responseType": "short constructed response in two parts",
      "answerScope": "Two things that would have to be found out, each with a reason tied to the difference between crop failure and famine, and one of them chosen as the most informative with a justification.",
      "pagePlacement": {
        "student": "student-cork-08",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-06",
        "accessible": "accessible-cork-13"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    }
  ],
  "vocabulary": [
    "blight",
    "clone",
    "cottier",
    "export",
    "famine",
    "relief"
  ],
  "caseSources": [
    {
      "id": "archive-scenes",
      "displayLabel": "The Archive's scenes at the field, the cottage and the road",
      "creator": "Hunger, Harvest, & History Campaign 1 Level 3",
      "period": "scene set in 1845",
      "sourceType": "reconstruction",
      "sourceOrigin": "game reconstruction of a historical setting",
      "evidentiaryStatus": "reconstructed",
      "limitationClass": "reconstruction",
      "contribution": "A watchable model of one blighted field, one household's food, and one road out: the speed of the collapse, the sameness of the crop, what a family had left when the potato went, and the estate and parish books recording the potato gone on one page and grain, butter and cattle consigned to the ports on the other.",
      "limitation": "No person in it is a real person and no ledger in it is a real ledger. Its dialogue was written for the game and is not surviving testimony. It fixes no date, no parish and no count, and one traveller's report of what lies beyond the next parish cannot establish how far anything actually reached.",
      "gameCorrespondence": "C1 L3 sources farmer, blight, survey_field, sample_soil, woman, records, traveler, survey_region, examine_evidence.",
      "fallbackCorrespondence": "Dossier cards A, B and C on Student page 2 and Accessible page 2."
    },
    {
      "id": "cummins-letter",
      "displayLabel": "Nicholas Cummins's letter from Skibbereen, December 1846",
      "creator": "Nicholas Cummins, magistrate of Cork; published in The Times, 24 December 1846",
      "period": "written 15-17 December 1846; published 24 December 1846",
      "sourceType": "published eyewitness account",
      "sourceOrigin": "real historical primary source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "A real, named, dated account by a magistrate who travelled to Skibbereen in West Cork in December 1846 and wrote to the Duke of Wellington about what he found, sending copies to the newspapers. It establishes that severe starvation in County Cork was seen, reported and publicly known at the time.",
      "limitation": "One man, one district, a few days. It was written to move a government to act, so it selects what would move them. It counts nobody, measures nothing, and cannot establish how conditions in Skibbereen compared with the rest of Ireland.",
      "gameCorrespondence": "None. The game presents no real historical document.",
      "fallbackCorrespondence": "Dossier card D on Student page 2 and Accessible page 3."
    },
    {
      "id": "blight-science",
      "displayLabel": "What late blight is and what it does to a potato crop",
      "creator": "University of Minnesota Extension; Coomber, Saville and Ristaino, Nature Communications, 2024",
      "period": "modern plant pathology; the historic lineage sampled from 1845 onward",
      "sourceType": "established science",
      "sourceOrigin": "real modern institutional and scientific source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "Phytophthora infestans is an oomycete, a water mould, not a true fungus. Spores land on wet leaves, the organism grows into the living tissue, dark blotches spread, a fine white growth fruits on the underside in damp air and releases more spores to wind and rain, and spores washed into the soil rot the tubers. It thrives in cool damp weather and stalls in hot dry weather, and one lesion can make thousands of spores in under five days.",
      "limitation": "It explains what happens to a potato plant. It says nothing about who owned the field, what else the household could eat, or what anyone did next, and it cannot explain why the same organism produced a catastrophe in one country and a hard year in another.",
      "gameCorrespondence": "The level's blight examination, its regional scan naming the organism a water-mould and an oomycete, and its closing record.",
      "fallbackCorrespondence": "Background block on Student page 2 and Accessible page 3, and the stage path in Task 4."
    },
    {
      "id": "potato-dependence",
      "displayLabel": "What the poorest households in Ireland lived on",
      "creator": "Helene O'Keeffe, University College Cork, for the RTE Great Irish Famine series, giving the County Cork acreage figure after John Feehan in the Atlas of the Great Irish Famine; Ciaran Reilly, Maynooth University",
      "period": "conditions of the 1830s and early 1840s",
      "sourceType": "scholarly summary of documented conditions",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "By the 1830s about a third of the population depended on the potato for about ninety per cent of what it ate, most heavily in Munster, Connacht and west Leinster. An agricultural labourer in the west ate ten to fourteen pounds of potatoes a day. One acre of lazy beds could yield almost six tonnes, enough to feed a family for close to a year. County Cork alone had a quarter of a million acres under potatoes.",
      "limitation": "These are proportions and averages for classes and regions, not a count of any parish or family. They establish that dependence was deep and unevenly spread; they do not establish that everyone in Ireland ate only potatoes, and other food was grown throughout.",
      "gameCorrespondence": "The woman's account of what the family lives on and what is left when the potato fails.",
      "fallbackCorrespondence": "Dossier card E on Student page 2 and Accessible page 4."
    },
    {
      "id": "lumper-and-variety",
      "displayLabel": "The Lumper, and what growing one variety did and did not do",
      "creator": "Cormac O Grada, History Ireland",
      "period": "the Lumper introduced from Scotland in the 1800s; blight from 1845",
      "sourceType": "scholarly interpretation",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "documented",
      "limitationClass": "interpretation",
      "contribution": "The Lumper spread because it yielded heavily on poor ground and was reliable, though it was watery and low in dry matter. Potatoes are grown from pieces of tuber, so a field of one variety is a field of clones. Where the poorest grew nothing else, one failure took the whole year's food at once.",
      "limitation": "Variety choice is not the whole story: every potato variety commonly sown in Ireland at the time also succumbed to the blight. Growing a different variety would not by itself have saved the crop. What uniformity removed was any chance of a plant the disease passed over, and what dependence removed was anything to fall back on.",
      "gameCorrespondence": "The level's field survey, which finds one variety repeated and no plant standing clear of the rot.",
      "fallbackCorrespondence": "Dossier card E on Student page 2 and Accessible page 4, and the variety note in Task 4 on Student page 4 and Accessible page 7."
    },
    {
      "id": "land-and-labour",
      "displayLabel": "How the poorest held their land and paid for it",
      "creator": "Ciaran Reilly, Maynooth University; Helene O'Keeffe, University College Cork",
      "period": "the early 1840s",
      "sourceType": "scholarly summary of documented conditions",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "The cottier class numbered more than three million people in the early 1840s. A cottier held a cabin and a potato plot and paid for them mostly in labour, commonly about two hundred days a year, under an unwritten agreement that could be ended at a moment's notice. Cottiers rarely handled cash and were persistently in debt. In 1841 nearly half of rural families lived in single-room mud-walled cabins.",
      "limitation": "It describes arrangements and orders of magnitude, not the terms of any particular tenancy. It shows why a household with no money and no security had no way to buy food once its own crop was gone; it does not by itself show what any landlord or agent chose to do.",
      "gameCorrespondence": "The woman's account of the oats going to the agent for the rent and the pig already gone the same way.",
      "fallbackCorrespondence": "Dossier card F on Student page 2 and Accessible page 4."
    },
    {
      "id": "food-exports",
      "displayLabel": "The food that left Ireland, and the argument about it",
      "creator": "P. M. Austin Bourke, Irish Historical Studies, 1976; Christine Kinealy, History Ireland",
      "period": "1846 to 1850; the sharpest dispute concerns the winter of 1846-47",
      "sourceType": "competing scholarly readings of trade records",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "debated / uncertain",
      "limitationClass": "interpretation",
      "contribution": "Food kept leaving Ireland while people starved. Almost four thousand vessels carried food from Ireland to British ports in 1847, and more than three million live animals were exported between 1846 and 1850, along with grain, butter, fish and vegetables. Bourke's tabulation of the official grain returns found that by 1847 grain imports exceeded grain exports.",
      "limitation": "The vessel figure counts ship movements, not the quantity or calorific value of what was carried. The two positions are not settled. Kinealy holds that the official returns are flawed, under-represent what left, cover grain rather than the whole food trade, and cannot gauge calorie losses, and that imports only became significant after the spring of 1847, leaving a gap over the winter of 1846-47. Nothing in this packet weighs the food that left against the food that was needed, so it cannot show that retaining exports would by itself have prevented the famine, and it cannot show that exports made no difference either.",
      "gameCorrespondence": "The estate ledger and parish register, which record the potato gone on one side and the season's grain, butter and cattle consigned to the ports on the other.",
      "fallbackCorrespondence": "The food that left panel, Source G, on Student page 2 and Accessible page 5."
    },
    {
      "id": "relief-chronology",
      "displayLabel": "What was done, and when",
      "creator": "Peter Gray, Queen's University Belfast; Helene O'Keeffe, University College Cork",
      "period": "autumn 1845 to 1849",
      "sourceType": "scholarly chronology of government measures",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "A dated sequence: a Relief Commission in autumn 1845; a hundred thousand pounds of Indian corn bought in early 1846 and shipped to Cork; public works employing over 700,000 people at their March 1847 peak; soup kitchens feeding over three million people by July 1847; the soup kitchens closed from August 1847; the Poor Law Extension Act of June 1847 moving the cost onto Irish rates and, through the Gregory clause, refusing relief to anyone holding more than a quarter of an acre. Evictions rose sharply after 1847.",
      "limitation": "A chronology of measures is not a measurement of their effect. It records what was set up and when it stopped; it does not count who was saved or lost by any single decision, and the historians who assembled it say so.",
      "gameCorrespondence": "None. The level ends in 1845, before any of these measures existed.",
      "fallbackCorrespondence": "Relief strand of the Task 3 timeline on Student page 3 and Accessible page 6."
    },
    {
      "id": "european-comparison",
      "displayLabel": "The same blight in two countries, 1845 to 1847",
      "creator": "Wouter Ronsijn and Eric Vanhaute, Ghent University, for the RTE Great Irish Famine series",
      "period": "1845 to 1847",
      "sourceType": "comparative historical evidence",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "The blight was first seen near Courtrai in Belgium in June 1845 and reached the whole of Ireland by mid-September. Belgium lost almost ninety per cent of its potato harvest in 1845; Ireland lost about thirty per cent that year and over three quarters in 1846. Belgium and Prussia each recorded over forty thousand famine-related deaths and mortality thirty to forty per cent above normal, while Ireland's mortality ran at about three times normal and about a million people died.",
      "limitation": "It compares national figures, not households, and it does not itself explain the difference. Using the comparison to decide which conditions mattered in Ireland is a reasoned inference drawn from the numbers, not something the numbers state.",
      "gameCorrespondence": "None. The level shows one country.",
      "fallbackCorrespondence": "Two-country comparison panel in Task 4 on Student page 4 and Accessible page 8."
    },
    {
      "id": "causes-map",
      "displayLabel": "The causes map",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching model and depicts no dated record",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "limitationClass": "model",
      "contribution": "It separates the trigger from the conditions and puts four historically supported conditions between the crop failure and the death toll, so that interaction can be reasoned about and written down rather than merely asserted.",
      "limitation": "It is a drawing made to organise an argument, not evidence. Every arrow on it means contributed to and nothing more. It carries no weights, and no source in this packet ranks the four conditions against each other or measures how much any of them added.",
      "gameCorrespondence": "None. The level presents one closing account rather than a map.",
      "fallbackCorrespondence": "Task 6 figure on Student page 6 and Accessible page 10."
    }
  ],
  "causationBoundary": {
    "trigger": "Late blight caused catastrophic potato crop failures in Ireland from 1845. This packet supports that, and the biology is documented science.",
    "famineCausation": "The death toll followed from the crop failure interacting with deep dependence among the poorest, land and labour arrangements that left them without money or security, unequal access to the food that remained, and the scale and timing of relief. This packet supports that more than one condition contributed. It does not rank them.",
    "prohibitedClaims": [
      "the whole country lived on the potato",
      "every field in Ireland was the same plant repeated",
      "nothing else was grown to fall back on",
      "blight alone caused the famine",
      "the potato famine was simply a natural disaster",
      "Ireland exported enough food to feed everyone, so exports alone caused the famine"
    ],
    "requiredQualification": "Every role must keep the biological trigger and the wider famine causation apart, must present more than one contributing condition, and must not present any single condition, biological or political, as the whole cause."
  },
  "observationExtent": {
    "scopeSourceId": "archive-scenes",
    "appliesTo": "learner blocks marked data-traveller-evidence, inside the reconstructed Archive scenes",
    "rule": "A reconstructed traveller may report only the extent actually observed on the journey. Reconstructed testimony cannot establish nationwide or system-wide disease extent. Documented sources may establish national extent, and the Task 3 timeline does; this bound applies to the game reconstruction alone.",
    "journeyBound": "four days",
    "requiredQualifier": "not a survey of Ireland",
    "prohibitedExtentConclusions": [
      "every parish in Ireland",
      "every field in Ireland",
      "the whole country",
      "the whole island",
      "the whole of Ireland",
      "all of Ireland",
      "the entire country",
      "nationwide",
      "system-wide",
      "throughout Ireland"
    ]
  },
  "cropLossComparison": {
    "units": "per cent of the national potato harvest lost",
    "status": "documented / reported",
    "source": "Ronsijn and Vanhaute, RTE Great Irish Famine series, after the comparative European literature",
    "measure": "Share of the potato harvest lost to late blight",
    "values": {
      "belgium1845": { "lossPercent": 90, "qualifier": "almost", "label": "Belgium, 1845" },
      "ireland1845": { "lossPercent": 30, "qualifier": "about", "label": "Ireland, 1845" },
      "ireland1846": { "lossPercent": 75, "qualifier": "over", "label": "Ireland, 1846" }
    },
    "mortality": {
      "belgium": "over 40,000 famine-related deaths; mortality 30 to 40 per cent above normal",
      "ireland": "about 1,000,000 deaths; mortality about three times normal"
    },
    "boundary": "National shares reported by historians, not measurements of any field or parish. The comparison shows that the size of the crop loss did not set the size of the death toll; it does not by itself say which conditions did."
  },
  "claimJudgments": {
    "markScheme": {
      "Y": "the evidence in this packet supports it",
      "N": "the evidence in this packet goes against it",
      "?": "this packet cannot decide it"
    },
    "claims": [
      { "number": "1", "layer": "trigger", "mark": "Y" },
      { "number": "2", "layer": "trigger", "mark": "N" },
      { "number": "3", "layer": "condition", "mark": "Y" },
      { "number": "4", "layer": "condition", "mark": "?" },
      { "number": "5", "layer": "condition", "mark": "N" }
    ]
  },
  "standards": {
    "directlyAssessed": [
      "C3 D2.His.14.6-8",
      "C3 D3.2.6-8",
      "CCSS RH.6-8.1",
      "CCSS RH.6-8.7"
    ],
    "supporting": [
      "C3 D2.His.1.6-8",
      "CCSS RH.6-8.9",
      "CCSS WHST.6-8.2"
    ],
    "contextual": [
      "NGSS MS-LS2-4"
    ],
    "ngss": "MS-LS2-4 is contextual only. Task 4 does describe a pathogen disrupting a cultivated population, but the assessed product is a multi-causal historical explanation with source qualification, not a science or engineering practice, so no NGSS alignment is claimed as directly assessed."
  }
};
