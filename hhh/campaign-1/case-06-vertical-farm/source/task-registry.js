window.HHH_CASE06_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C1-CASE06",
  "runtimeId": "L6",
  "instructionalType": "CORE_CASE",
  "title": "The Vertical Farm",
  "displayLabel": "6 - The Vertical Farm",
  "version": "0.1",
  "status": "VALIDATION_BUILD",
  "ownerReviewStatus": "OWNER_REVIEW_NOT_STARTED",
  "editorShell": "1.0",
  "gameCommit": "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
  "auditBaseline": "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md",
  "staticContentInventory": "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json",
  "blueprint": "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
  "roles": {
    "student": 11,
    "teacher": 10,
    "answer": 6,
    "accessible": 17
  },
  "culminatingProduct": "Systems and evidence-audit explanation. The learner must name which subsystem failed and the evidence for it, state what the engineering records do and do not establish, say what the public record claimed and what accountability the evidence actually supports, and then apply the same audit to an unfamiliar automated-system failure. Canonical CER is deliberately not used: the product requires two findings that a single claim cannot hold at once - that a biological subsystem failed, and that the record which named the cause was wrong about it - and the Blueprint names a systems/evidence-audit explanation as this case's product rather than a claim-evidence-reasoning frame. See the Teacher Guide reasoning architecture.",
  "twoLayerTruth": {
    "id": "vertical-farm-two-layer-v1.0",
    "mandate": "Blueprint section 12. Mandatory for this case.",
    "rule": "Every learner-facing evidence object declares which layer it belongs to, in markup and in printed text, and no role ever converts a Layer 1 figure, date, actor or measurement into a Layer 2 claim about the real world.",
    "layers": [
      {
        "id": "fictional",
        "label": "FICTIONAL CASE EVIDENCE",
        "attribute": "fictional",
        "statusMarker": "fictional / hypothetical",
        "covers": [
          "the 2041 facility and everything in it",
          "the failed crops and the floors they stood on",
          "the engineering and dosing logs",
          "the microbial-consortium monitoring trace",
          "the maintenance chronology and its three logged events",
          "the company's public statement and the named engineer",
          "the media archive and the forward regulatory trace",
          "every date, day number, duration and quantity belonging to the facility"
        ],
        "rule": "Named as evidence about a case that did not happen. It may be reasoned about, ordered, compared and audited. It may never be cited as evidence about the real world."
      },
      {
        "id": "real",
        "label": "REAL-WORLD SCIENCE",
        "attribute": "real",
        "statusMarker": "documented",
        "covers": [
          "nitrification as a microbial process",
          "the ammonia and ammonium forms and the pH dependence between them",
          "nitrite and nitrate",
          "the diversity of nitrifying microorganisms, including ammonia-oxidising archaea and comammox Nitrospira",
          "plant uptake of inorganic nitrogen",
          "the variability of ammonium tolerance between plant species and cultivars"
        ],
        "rule": "Real published science, cited to a real source. It explains how the fictional system was supposed to work. It is never evidence that the fictional system existed."
      },
      {
        "id": "curriculum-model",
        "label": "CURRICULUM DIAGRAM",
        "attribute": "curriculum-model",
        "statusMarker": "modeled",
        "covers": [
          "the system-boundary figure",
          "the nitrogen-pathway figure",
          "the chronology figure",
          "the record-audit matrix",
          "the public-record comparison"
        ],
        "rule": "Drawn for this packet. A diagram that organises evidence is not itself evidence, and every figure says so in print."
      }
    ],
    "nonMergerRule": "A correct conclusion about the 2041 facility proves nothing about the real world, and a real scientific finding proves nothing about the 2041 facility. Both learner editions carry this sentence on page 1, and Task 9 Part A requires the learner to name the layer of every piece of evidence they use.",
    "enforcedRoles": ["student", "teacher", "answer", "accessible"]
  },
  "systemsFrame": {
    "id": "vertical-farm-systems-v1.0",
    "rule": "Every role represents the facility as one loop containing two kinds of part, plus the monitoring that watched only one of them. No role may present the loop as wholly engineered, and no role may present the biology as an add-on to the machinery.",
    "zones": [
      {
        "id": "engineered",
        "label": "ENGINEERED",
        "gloss": "the parts that are machines",
        "members": ["pumps and circulation", "dosing units", "grow lights and climate control", "water-quality sensors and alarms", "plumbing and tanks"],
        "requiredStatus": "performed to specification throughout",
        "why": "The engineering held. That is the finding the whole case turns on, and it is why blaming a machine or the person who designed one does not fit the evidence."
      },
      {
        "id": "living",
        "label": "LIVING",
        "gloss": "the parts that are alive",
        "members": ["the crops in the trays", "the nitrifying consortium in the biofilter"],
        "requiredStatus": "one living part failed, and the other died of it",
        "why": "A sealed nutrient loop of this design does a chemical conversion that no pump performs. That conversion is done by organisms, and organisms can die while the machinery around them keeps running."
      },
      {
        "id": "monitoring",
        "label": "WATCHED",
        "gloss": "what the alarms could see",
        "members": ["pump pressure", "dose delivered", "temperature", "total nutrient concentration"],
        "requiredStatus": "watched the engineered zone; did not watch the living one",
        "why": "The monitoring gap is the mechanism of the misattribution. Instruments that only measure the machinery will only ever report that the machinery is fine."
      }
    ],
    "boundaryRule": "The learner draws the boundary in Task 3 before meeting any evidence about what failed. The distinction has to be available before the case can be audited, or the audit collapses into hindsight."
  },
  "tasks": [
    {
      "id": "C06-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Case Vocabulary",
      "description": "Apply the seven case terms to the things and processes they name rather than copying definitions.",
      "instructionalPurpose": "Establish the seven terms the case is unreadable without. Three of them - ammonium, nitrite and nitrate - are three different substances that a learner will otherwise hear as three spellings of the word nitrogen, and Task 4 assesses exactly that distinction. The term system boundary is placed here deliberately: it is the abstraction Task 3 asks the learner to draw.",
      "provenance": [
        "Curriculum-authored definitions",
        "Established microbiology and plant nutrition as cited in the real-world source estate"
      ],
      "responseType": "seven exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared seven-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-vertical-farm-01",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-01",
        "accessible": "accessible-vertical-farm-02"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C06-T2",
      "number": "2",
      "semanticLabel": "FIRST AUDIT QUESTION",
      "icon": "ph-diagnosis",
      "title": "Record a First Audit Question",
      "description": "State what the inquiry has concluded, say whether the case file so far supports it, then write the single question you would ask first to test that conclusion.",
      "instructionalPurpose": "Provisional judgment recorded from the fictional case file alone, before any real-world science arrives. An evidence audit begins with a question, not with an answer, and this task is where the learner's own question gets written down so it can be compared with the audit they actually run. Most learners write a question about the machines, which is exactly the question the inquiry already asked and the reason it reached the wrong verdict.",
      "provenance": [
        "The Archive's fictional record of the 2041 facility",
        "Curriculum-authored prompt"
      ],
      "responseType": "two short constructed responses",
      "answerScope": "One statement of the inquiry's conclusion and whether the case file supports it, and one first audit question with a reason.",
      "pagePlacement": {
        "student": "student-vertical-farm-03",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-01",
        "accessible": "accessible-vertical-farm-05"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C06-T3",
      "number": "3",
      "semanticLabel": "SYSTEM BOUNDARY",
      "icon": "ph-globe",
      "title": "Draw the System Boundary",
      "description": "Sort four parts of the farm into the engineered zone and the living zone, say which zone the facility's alarms watched, then explain how every machine can be running correctly while the farm dies.",
      "instructionalPurpose": "Family H8, and the structural move the whole case depends on. A loop that contains living components is not a machine with plants in it, and a learner who has not drawn that line will read hardware to spec as proof of health. Part C is the case's central proposition stated as a question the learner has to answer before any failure evidence is on the page - which is why this task comes before the pathway, the chronology and the audit.",
      "provenance": [
        "The Archive's fictional record of the 2041 facility",
        "Real recirculating-system design as documented in the biofilter-community study",
        "Curriculum-created system-boundary figure"
      ],
      "responseType": "four marked placements plus two short constructed responses",
      "answerScope": "Each of four components assigned to the engineered or the living zone, the zone the monitoring watched, and an explanation of how full mechanical compliance and system failure can be true at the same time.",
      "pagePlacement": {
        "student": "student-vertical-farm-05",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-02",
        "accessible": "accessible-vertical-farm-08"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C06-T4",
      "number": "4",
      "semanticLabel": "NITROGEN PATHWAY",
      "icon": "ph-flow",
      "title": "Trace the Nitrogen Pathway",
      "description": "Complete the two open stages of the nitrogen pathway, name which form of nitrogen scorched the roots and which one the crops ran short of, then say which step of the pathway is not a machine.",
      "instructionalPurpose": "Family H8 and the load-bearing science task. The pathway makes the case's contradiction mechanical rather than rhetorical: nitrogen was abundant and the crops starved, which is only possible if the forms are different substances with different fates. Part C is where the systems reasoning and the chemistry meet - the conversion between the forms is the one step in the whole loop that no pump performs, and a learner who can name it can explain the failure without naming a villain.",
      "provenance": [
        "US EPA CADDIS on ammonia, ammonium and nitrification",
        "Hachiya and Sakakibara 2017 on plant uptake of nitrate and ammonium",
        "The Archive's fictional record of the 2041 facility for the case's own readings",
        "Curriculum-created pathway figure"
      ],
      "responseType": "two organizer stages, two form identifications and one short constructed response",
      "answerScope": "The two open conversion stages, the form that burned the roots, the form the crops could not get enough of, and a statement of which step is biological and what the dosing records could not have detected.",
      "pagePlacement": {
        "student": "student-vertical-farm-06",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-02",
        "accessible": "accessible-vertical-farm-09"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C06-T5",
      "number": "5",
      "semanticLabel": "EVENT CHRONOLOGY",
      "icon": "ph-flow",
      "title": "Order the Failure",
      "description": "Put the four middle entries of the facility's chronology in order, say what the order establishes about what failed first, then explain why the chronology cannot establish which logged event caused the collapse.",
      "instructionalPurpose": "Family H2 event log. Sequence is the strongest single piece of reasoning the fictional record supplies: the biology fails, then the chemistry moves, then the crops die, and nothing in the machinery changes at any point. Part C is the case's uncertainty requirement made assessable. Three maintenance events are logged in the days before the collapse and the record cannot separate them, so a learner who names one as the cause has read a sequence as a proof.",
      "provenance": [
        "The Archive's fictional consortium trace and maintenance chronology",
        "Curriculum-created chronology figure"
      ],
      "responseType": "four ordered placements plus two short constructed responses",
      "answerScope": "The four middle entries in order, a statement of which subsystem failed first and how the order shows it, and an explanation of why no single logged event can be named as the trigger from this record.",
      "pagePlacement": {
        "student": "student-vertical-farm-07",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-03",
        "accessible": "accessible-vertical-farm-11"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C06-T6",
      "number": "6",
      "semanticLabel": "EVIDENCE AUDIT",
      "icon": "ph-scales",
      "title": "Audit the Records",
      "description": "For each of five records, write what it measures and what it cannot show, then name the two records that together rule out a hardware failure and say why neither does it alone.",
      "instructionalPurpose": "Family H9 and the disciplinary core of the case. Every record in this packet is honest and every record is partial, and the failure of the inquiry was not that anyone lied but that the record with the most authority measured the wrong zone. Part B is the convergence requirement: a single record never settles this case, and a learner who can name which pair does the work has performed an evidence audit rather than picked a favourite source.",
      "provenance": [
        "The Archive's fictional engineering logs, consortium trace, crop evidence, maintenance log and public statement",
        "Blueprint contribution-and-limitation rule",
        "Curriculum-created audit matrix"
      ],
      "responseType": "ten matrix cells plus one short constructed response",
      "answerScope": "What each of five records measures and what it leaves invisible, and a named pair of records that together exclude a mechanical failure with a reason why one alone cannot.",
      "pagePlacement": {
        "student": "student-vertical-farm-08",
        "teacher": "teacher-guide-06",
        "answer": "answer-key-03",
        "accessible": "accessible-vertical-farm-13"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C06-T7",
      "number": "7",
      "semanticLabel": "COMPETING ACCOUNTS",
      "icon": "ph-diagnosis",
      "title": "Weigh Five Accounts",
      "description": "Mark five accounts of the failure against the evidence in this packet, then say what would settle the one you could not decide.",
      "instructionalPurpose": "Competing explanations with three marks rather than two. Account 2 is the inquiry's verdict, Account 3 is the runtime level's second distractor, and Account 4 is the science qualification made assessable rather than announced: the packet's own real-world sources show that a nitrifying community is not universally two named species, so a learner who has read them can refuse that account on evidence. Account 5 is undecidable from this packet on purpose and is not a manufactured puzzle - three candidate triggers are logged within three days of each other and nothing printed here separates them.",
      "provenance": [
        "The Archive's fictional case file",
        "Daims and colleagues 2015 and van Kessel and colleagues 2015 on complete nitrification",
        "Bartelme, McLellan and Newton 2017 on the nitrifying community of a working biofilter",
        "Curriculum-created accounts"
      ],
      "responseType": "five marked judgments plus one short constructed response",
      "answerScope": "One supported account, three contradicted accounts, one account this packet cannot decide, and a named kind of evidence that would move the undecided one.",
      "pagePlacement": {
        "student": "student-vertical-farm-09",
        "teacher": "teacher-guide-06",
        "answer": "answer-key-04",
        "accessible": "accessible-vertical-farm-14"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C06-T8",
      "number": "8",
      "semanticLabel": "PUBLIC RECORD",
      "icon": "ph-nodes",
      "title": "Audit the Public Record",
      "description": "Mark three claims from the company's public statement against the evidence, state what the evidence establishes about the named engineer, then name one institutional question the evidence leaves open.",
      "instructionalPurpose": "The accountability boundary, and the task this case exists for as much as for the chemistry. Part B is the exoneration the evidence actually supports and it is bounded: the records clear the engineer of the failure the statement describes, which is not the same as establishing that nothing could have been done differently by anyone. Part C is the other half and it is required, because a case that ends at the machinery worked has taught a learner that a complex failure with no individual culprit is a failure with no accountability at all. The evidence in this packet does support institutional questions - about what was monitored, about what was commissioned, about what a public statement is for - and Part C makes the learner name one and cite the record that raised it.",
      "provenance": [
        "The Archive's fictional public statement, media archive and forward regulatory trace",
        "The fictional engineering logs and consortium trace",
        "Curriculum-created public-record comparison"
      ],
      "responseType": "three marked judgments plus two short constructed responses",
      "answerScope": "Each of three public claims marked against the packet's evidence, a bounded statement of what the evidence establishes about the named engineer, and one open institutional question with the record that raised it.",
      "pagePlacement": {
        "student": "student-vertical-farm-10",
        "teacher": "teacher-guide-06",
        "answer": "answer-key-05",
        "accessible": "accessible-vertical-farm-15"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C06-T9",
      "number": "9",
      "semanticLabel": "SYSTEMS EXPLANATION",
      "icon": "ph-wrench",
      "title": "Explain the Failure",
      "description": "Write the case's explanation using the system boundary and specific labelled evidence, state what the engineering records do and do not establish, say what accountability the evidence supports, then apply the same audit to a new claim.",
      "instructionalPurpose": "Culminating product for the case: a systems and evidence-audit explanation. Part A requires the learner to label the layer of every piece of evidence they use, which is where the two-layer truth policy stops being a notice and becomes an assessed obligation. Part D carries the transfer function of the Core Case spine inside the culminating task rather than as a separate tenth task, because the operation being transferred is the same audit Parts A to C perform and a standalone transfer task would have re-measured it on a fresh page for no additional information.",
      "provenance": [
        "Curriculum-authored prompt",
        "Blueprint culminating-product policy",
        "Blueprint two-layer truth policy",
        "Blueprint transfer and exit policy"
      ],
      "responseType": "extended constructed response with four required parts",
      "answerScope": "What failed and the labelled evidence for it, what the engineering records do and do not establish, what the public record claimed against what accountability the evidence supports, and two questions to ask about an unfamiliar automated-system failure.",
      "pagePlacement": {
        "student": "student-vertical-farm-11",
        "teacher": "teacher-guide-06",
        "answer": "answer-key-06",
        "accessible": "accessible-vertical-farm-17"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    }
  ],
  "vocabulary": [
    "ammonium",
    "biofilter",
    "microbial consortium",
    "nitrate",
    "nitrification",
    "nitrite",
    "system boundary"
  ],
  "caseSources": [
    {
      "id": "facility-record",
      "displayLabel": "The Archive's record of the 2041 facility",
      "creator": "Hunger, Harvest, & History Campaign 1 Level 6",
      "period": "a fictional 2041",
      "sourceType": "in-world archive record",
      "sourceOrigin": "fictional in-world archive record",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "limitationClass": "observation",
      "contribution": "The case itself: a ten-storey closed-loop farm built to grow food for a city without soil or sky, dead floor by floor while its lights stayed on; crops showing nitrogen starvation and caustic root burn at the same time; a full scan reporting every mechanical system operational with no faults; and the scale of the thing, which is why the verdict mattered to more than one man.",
      "limitation": "Nothing in it happened. There is no such facility, no such year of operation and no such failure, and none of its people are people. It is the case to be audited, not evidence about any real farm, any real company or any real technology. Its own summing-up is a verdict rather than a finding, and this packet asks the learner to audit it rather than to adopt it.",
      "gameCorrespondence": "C1 L6 sources farm_researcher, examine_crops, scan_systems and survey_floor at the current game baseline.",
      "fallbackCorrespondence": "Dossier card A on Student page 2 and Accessible page 3."
    },
    {
      "id": "engineering-log",
      "displayLabel": "The facility's engineering record, and the engineer's account of it",
      "creator": "Hunger, Harvest, & History Campaign 1 Level 6",
      "period": "a fictional 2041",
      "sourceType": "in-world instrument output and testimony",
      "sourceOrigin": "fictional in-world instrument output",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "limitationClass": "record",
      "contribution": "The negative finding the case turns on, stated inside the fiction: nutrient metered to the gram, pumps at pressure, temperature held, every designed setpoint met to the final hour. The engineer's own reading of it is the case in one sentence - that they built beautiful hardware around a living community and then only ever watched the hardware.",
      "limitation": "A machine log records what the machine did and what the machine was built to measure. It cannot report a condition it has no instrument for, and it is silent about the living part of the loop for exactly that reason. Its silence is not evidence of health. The engineer's account is also an interested account: he is the person the statement is about.",
      "gameCorrespondence": "C1 L6 source systems_engineer at the current game baseline.",
      "fallbackCorrespondence": "Dossier card B on Student page 2 and Accessible page 3, and row 1 of the Task 6 audit matrix."
    },
    {
      "id": "consortium-trace",
      "displayLabel": "The biological monitoring trace",
      "creator": "Hunger, Harvest, & History Campaign 1 Level 6",
      "period": "a fictional 2041",
      "sourceType": "in-world instrument output",
      "sourceOrigin": "fictional in-world instrument output",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "limitationClass": "observation",
      "contribution": "The one record in the fictional case that watched the living zone, and the only reason the true cause is recoverable at all. Inside the fiction it holds the consortium steady for fifty-eight days, collapsing across about seventy-two hours and then flat; and from that point ammonia climbing while nitrate falls, with the crops beginning to die only afterwards.",
      "limitation": "Every figure in it is fictional case data and none of it is a measurement of anything. Inside the fiction it establishes a sequence and not a mechanism: it records that the consortium collapsed, not why, and it identifies no organism, no species and no cause of death. It also cannot be checked against anything, because the case supplies no second biological record.",
      "gameCorrespondence": "C1 L6 source query_systems at the current game baseline.",
      "fallbackCorrespondence": "Dossier card C on Student page 2 and Accessible page 4, and the Task 5 chronology figure."
    },
    {
      "id": "maintenance-chronology",
      "displayLabel": "The maintenance log",
      "creator": "Hunger, Harvest, & History Campaign 1 Level 6",
      "period": "a fictional 2041",
      "sourceType": "in-world operational record",
      "sourceOrigin": "fictional in-world archive record",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "limitationClass": "record",
      "contribution": "Three logged events in the days before the collapse, each filed within tolerance: a sanitiser flush, a dip in pH and a warm spell from a cycling chiller. It is the case's account of why an engineering alarm can be honest and useless at once - the thresholds were set for the machinery, and conditions well inside them are not necessarily well inside what a microbial community can survive.",
      "limitation": "It is the source of the case's central uncertainty and must not be read past. Three candidate events fall within three days of each other, the log records no biological measurement at all, and nothing in this packet establishes which of them - or which combination, or whether any of them - collapsed the consortium. A logged event before a failure is a candidate, not a cause.",
      "gameCorrespondence": "C1 L6 source review_records at the current game baseline.",
      "fallbackCorrespondence": "Dossier card D on Student page 3 and Accessible page 4, and entry Q of the Task 5 chronology."
    },
    {
      "id": "public-statement",
      "displayLabel": "The company's public statement, the media archive and the forward trace",
      "creator": "Hunger, Harvest, & History Campaign 1 Level 6",
      "period": "a fictional 2041",
      "sourceType": "in-world public statement and media record",
      "sourceOrigin": "fictional in-world testimony",
      "evidentiaryStatus": "fictional / hypothetical",
      "evidenceLayer": "fictional",
      "limitationClass": "testimony",
      "contribution": "The record the case exists to audit. A spokesperson attributes the failure to human error in the nutrient-cycling design, names an engineer, and promises tighter oversight of the engineering; the media archive runs the arc from ribbon-cutting to the building browning from the inside; and the forward trace sets out what follows from sealing the record either way.",
      "limitation": "A public statement is evidence of what an institution said, and of nothing else. It is not an investigation, it reports no measurement, and inside the fiction it is chosen for what an industry can absorb rather than for what the records show. The forward trace is a projection inside a fiction and is not a prediction about anything. Reading this source as the answer is the error the case is built to catch; reading it as worthless is the opposite error, because what an institution chose to say is itself a finding.",
      "gameCorrespondence": "C1 L6 sources facility_spokesperson, query_archive and press_records at the current game baseline.",
      "fallbackCorrespondence": "Dossier card E on Student page 3 and Accessible page 4, and the Task 8 comparison figure."
    },
    {
      "id": "epa-ammonia",
      "displayLabel": "What ammonia is in water, and what nitrification does to it",
      "creator": "United States Environmental Protection Agency, CADDIS Volume 2: Ammonia, epa.gov/caddis/ammonia, page updated 22 January 2026",
      "period": "established science; no period",
      "sourceType": "government scientific reference",
      "sourceOrigin": "real modern government scientific record",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "real",
      "limitationClass": "observation",
      "contribution": "The chemistry the case depends on, from a federal scientific authority. Ammonia nitrogen includes both the ionized form, ammonium (NH4+), and the unionized form, ammonia (NH3). An increase in pH favors formation of the more toxic unionized form (NH3), while a decrease favors the ionized (NH4+) form; temperature also affects the toxicity of ammonia to aquatic life. And nitrification is defined there as the oxidation of ammonia to nitrite (NO2-) and nitrate (NO3-), carried out as bacteria and other microbes oxidize ammonia into nitrite and nitrate.",
      "limitation": "It is written about surface waters and the aquatic animals in them. Its toxicity statements are about aquatic life - it explains that unionized ammonia is very toxic to aquatic animals, particularly fish, because it can readily diffuse across gill membranes - and it supplies no threshold for any crop plant and no statement about hydroponic or recirculating agriculture. It establishes the forms and the pH relationship. It does not establish what concentration harms lettuce.",
      "gameCorrespondence": "None. The runtime level names ammonia, nitrite and nitrate inside its own story; this source is where the real chemistry comes from.",
      "fallbackCorrespondence": "Dossier card F on Student page 4 and Accessible page 6, and the chemistry panel of the Task 4 pathway figure.",
      "rights": "United States Environmental Protection Agency web resource. Public-domain United States Government work; summarised and quoted in part, not reproduced."
    },
    {
      "id": "comammox-discovery",
      "displayLabel": "The discovery that one organism can do the whole job",
      "creator": "Daims, H., Lebedeva, E. V., Pjevac, P., Han, P., Herbold, C., Albertsen, M., Jehmlich, N., Palatinszky, M., Vierheilig, J., Bulaev, A., Kirkegaard, R. H., von Bergen, M., Rattei, T., Bendinger, B., Nielsen, P. H. and Wagner, M., Complete nitrification by Nitrospira bacteria, Nature 528(7583), 504-509 (2015), doi:10.1038/nature16461; and van Kessel, M. A. H. J., Speth, D. R., Albertsen, M., Nielsen, P. H., Op den Camp, H. J. M., Kartal, B., Jetten, M. S. M. and Lucker, S., Complete nitrification by a single microorganism, Nature 528(7583), 555-559 (2015), doi:10.1038/nature16459",
      "period": "published 2015",
      "sourceType": "peer-reviewed primary research, two independent papers",
      "sourceOrigin": "real modern scientific source",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "real",
      "limitationClass": "observation",
      "contribution": "The reason the two-species story cannot be taught as a universal rule. Two groups reported independently, in the same issue of the same journal, the enrichment and characterisation of Nitrospira that encode all the enzymes needed to catalyse complete nitrification - ammonia all the way to nitrate in one organism - a phenotype named comammox. Until then the two oxidation steps had always been observed in two separate microorganisms in a cross-feeding interaction, and the split had puzzled microbiologists for decades. Phylogenetic analysis in those papers indicates comammox Nitrospira occur in a range of environments.",
      "limitation": "Two enrichment cultures, from a deep oil-exploration well and from an aquaculture recirculation system, characterised in the laboratory. They establish that complete nitrification by one organism happens; they do not establish how much of the nitrification in any particular system it accounts for, and they do not make comammox the new universal answer in place of the old one. What they retire is the word always.",
      "gameCorrespondence": "None. The runtime level's closing note names two partner microbes as the real-world case; these are the papers that show that framing is a simplification.",
      "fallbackCorrespondence": "Dossier card G on Student page 4 and Accessible page 6, sharing that card with the biofilter-community study.",
      "rights": "Nature 528 (2015). Cited and summarised, not reproduced."
    },
    {
      "id": "biofilter-community",
      "displayLabel": "Who actually turned out to be doing the work in a real biofilter",
      "creator": "Bartelme, R. P., McLellan, S. L. and Newton, R. J., Freshwater Recirculating Aquaculture System Operations Drive Biofilter Bacterial Community Shifts around a Stable Nitrifying Consortium of Ammonia-Oxidizing Archaea and Comammox Nitrospira, Frontiers in Microbiology 8, article 101 (2017), doi:10.3389/fmicb.2017.00101",
      "period": "published 2017",
      "sourceType": "peer-reviewed primary research",
      "sourceOrigin": "real modern scientific source",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "real",
      "limitationClass": "observation",
      "contribution": "The single most useful check on overreach in this case, because it measures a real working version of the fictional system. The authors sampled the fluidized-sand biofilter of a commercial-scale freshwater recirculating aquaculture system raising yellow perch. They note that in recirculating-system process engineering, designers typically cite the principle nitrifying taxa as Nitrosomonas species for ammonia oxidation and Nitrobacter species for nitrite oxidation. What they found was not that: ammonia-oxidizing archaea dominated, present at roughly six hundred thousand times the abundance of Nitrosomonas, and comammox Nitrospira carried the most abundant ammonia-oxidising gene. Comammox and nitrite-oxidising Nitrospira co-existed at relatively equivalent and stable abundances, and the dominant nitrifying organisms changed little in composition or abundance over time while the rest of the bacterial community shifted with normal operations.",
      "limitation": "One biofilter, one system, one time series, in aquaculture rather than in crop production. It cannot establish what lives in any other biofilter, and it is not a claim that archaea dominate everywhere. What it does establish is that the organisms a designer expects and the organisms actually doing the work in a running system were, in this measured case, not the same - which is why a curriculum may not teach the expected pair as the universal fact.",
      "gameCorrespondence": "None. The runtime level's biofilter is fictional; this is a measurement of a real one.",
      "fallbackCorrespondence": "Dossier card G on Student page 4 and Accessible page 6, sharing that card with the comammox discovery, and Account 4 of Task 7.",
      "rights": "Frontiers in Microbiology 8:101 (2017). Open access; cited and summarised, not reproduced."
    },
    {
      "id": "plant-nitrogen-uptake",
      "displayLabel": "Which forms of nitrogen a plant can actually take up",
      "creator": "Hachiya, T. and Sakakibara, H., Interactions between nitrate and ammonium in their uptake, allocation, assimilation, and signaling in plants, Journal of Experimental Botany 68(10), 2501-2512 (2017), doi:10.1093/jxb/erw449",
      "period": "published 2017",
      "sourceType": "peer-reviewed review",
      "sourceOrigin": "real modern scholarly source",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "real",
      "limitationClass": "observation",
      "contribution": "The correction that keeps this case honest. Plants acquire inorganic nitrogen mainly in the form of nitrate and ammonium - both of them, through separate transporters - and the review reports that mixtures of the two are beneficial for growth compared with either alone. Nitrate is the major form in most aerated soils and ammonium is prevalent in acidic or water-saturated ones.",
      "limitation": "A review of plant physiology, largely in soil and laboratory systems. It describes what plants can take up; it does not describe any particular growing system, it sets no concentration for any crop, and it is not a statement about what happened in any farm.",
      "gameCorrespondence": "None. The runtime level speaks of nitrate as the form the plants can finally drink; this source is why that must not become the claim that nitrate is the only usable form.",
      "fallbackCorrespondence": "Dossier card H on Student page 4 and Accessible page 7, sharing that card with the ammonium-tolerance review, and the Task 4 pathway figure boundary note.",
      "rights": "Journal of Experimental Botany 68 (2017). Cited and summarised, not reproduced."
    },
    {
      "id": "ammonium-tolerance",
      "displayLabel": "How much ammonium is too much, and why there is no single answer",
      "creator": "Esteban, R., Ariz, I., Cruz, C. and Moran, J. F., Review: Mechanisms of ammonium toxicity and the quest for tolerance, Plant Science 248, 92-101 (2016), doi:10.1016/j.plantsci.2016.04.008",
      "period": "published 2016",
      "sourceType": "peer-reviewed review",
      "sourceOrigin": "real modern scholarly source",
      "evidentiaryStatus": "documented",
      "evidenceLayer": "real",
      "limitationClass": "observation",
      "contribution": "The reason this packet prints no toxicity number. Ammonium stress affects virtually every plant species, but the degree of stress it generates is variable: the review reports high intraspecific and interspecific variability in response to ammonium nutrition, with some species and genotypes showing a preference for ammonium and others extreme sensitivity, and it reports that the threshold for ammonium toxicity depends on the species, the ecotype and even the cultivar, and on the growing conditions.",
      "limitation": "It establishes that no universal threshold exists, which is a statement about the absence of a number rather than a number. It cannot be used to say how much ammonium harmed any particular crop, and it does not describe recirculating hydroponic production.",
      "gameCorrespondence": "None. The runtime level says ammonia burned the roots without stating a level; this source is why no level is supplied here either.",
      "fallbackCorrespondence": "Dossier card H on Student page 4 and Accessible page 7, sharing that card with the plant-uptake review, and the Teacher science-qualification note.",
      "rights": "Plant Science 248 (2016). Cited and summarised, not reproduced."
    },
    {
      "id": "boundary-figure",
      "displayLabel": "The system-boundary figure",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching schematic",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "limitationClass": "model",
      "contribution": "It puts the engineered parts and the living parts inside one loop and draws the monitoring as a separate band across only one of them, so the gap between what the system was and what the system watched can be seen rather than asserted.",
      "limitation": "A schematic of membership, not a plan. It is not a drawing of any facility, nothing on it is to scale, no pipe route, flow rate, tank volume or floor layout may be read from it, and it does not represent the design of any real recirculating system.",
      "gameCorrespondence": "The level's three locations, which fix no system architecture beyond their names.",
      "fallbackCorrespondence": "Task 3 figure on Student page 5 and Accessible page 8."
    },
    {
      "id": "pathway-figure",
      "displayLabel": "The nitrogen pathway figure",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching model",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "limitationClass": "model",
      "contribution": "It sets the four stages of the loop beside the control panel that doses it, so that the one step performed by organisms rather than by machinery can be located, and so that a learner can see that a device measuring total nutrient would read the same whether the conversion was happening or not.",
      "limitation": "A drawing made to explain an order and a division of labour. No rate, concentration, residence time or organism is measurable from it. It shows the two-step conversion because that is the framing the real sources describe as conventional, and it prints alongside them that a single organism can perform both steps and that the community doing the work is not a fixed pair.",
      "gameCorrespondence": "The level's account of the loop, which gives the chemistry as narration without separating the biological step.",
      "fallbackCorrespondence": "Task 4 figure on Student page 6 and Accessible page 9."
    },
    {
      "id": "chronology-figure",
      "displayLabel": "The chronology figure",
      "creator": "Curriculum-original figure authored for this case",
      "period": "a fictional 2041; the figure is a teaching organizer",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "limitationClass": "model",
      "contribution": "It puts the biological trace, the maintenance events, the chemistry and the crop deaths on one timeline, with the engineering rail running unbroken beneath all of them, so that what changed and what did not can be read in one look.",
      "limitation": "An ordering of fictional case data, and every date and day number on it is fictional case data and is labelled as such. It shows what followed what inside a story; it does not show what caused what, and the three logged events it carries are candidates for a trigger and are printed as candidates.",
      "gameCorrespondence": "The level's consortium trace and maintenance log, which give the same sequence as narration without a timeline.",
      "fallbackCorrespondence": "Task 5 figure on Student page 7 and Accessible page 10."
    },
    {
      "id": "audit-matrix",
      "displayLabel": "The record-audit matrix",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching organizer",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "limitationClass": "model",
      "contribution": "It gives every record in the case the same two columns - what it measures, and what it cannot show - so that no record's authority comes from its format, and so that the difference between an honest record and a sufficient one has somewhere to be written down.",
      "limitation": "An organizer, not an evaluation. It ranks no record above another, it assigns no reliability score, and nothing on it says which record is right. It sets out what each one can carry.",
      "gameCorrespondence": "None. The level presents its sources one at a time and never side by side.",
      "fallbackCorrespondence": "Task 6 matrix on Student page 8 and Accessible pages 12 and 13."
    },
    {
      "id": "verdict-comparison",
      "displayLabel": "The public-record comparison",
      "creator": "Curriculum-original figure authored for this case",
      "period": "a fictional 2041; the figure is a teaching organizer",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "evidenceLayer": "curriculum-model",
      "limitationClass": "model",
      "contribution": "It sets the three claims of the fictional public statement against the packet's own evidence, claim by claim, and holds a third column open for the questions the evidence raises but does not answer, so that clearing a named person and closing an institutional question do not become the same act.",
      "limitation": "A comparison of a fictional statement with fictional and real evidence. It decides nothing about any real company, any real regulator or any real technology, and its third column is a set of questions rather than a set of findings.",
      "gameCorrespondence": "The level's spokesperson and forward archive, which are presented as scenes rather than as a comparison.",
      "fallbackCorrespondence": "Task 8 figure on Student page 10 and Accessible page 15. Parts B and C of the task continue overleaf."
    }
  ],
  "scienceQualification": {
    "findingId": "HHH-GAME-C1L6-001",
    "dependencyClass": "CURRICULUM_QUALIFICATION_REQUIRED",
    "rule": "The runtime level's nitrogen model is usable as fictional case data. It is not usable as a statement about real microbiology or real plant nutrition, and this packet corrects it in print rather than editing the game.",
    "gameDependency": "HHH-GAME-C1L6-001 is discharged as design rather than as disclaimer. The two-species claim becomes Task 7 Account 4, which a learner refuses using the packet's own real sources. The nitrate-only reading is refused inside the Task 4 figure, where the boundary note prints that plants take up both nitrate and ammonium. No toxicity number is printed anywhere, because the real source says the threshold varies by species, ecotype and cultivar.",
    "boundaries": [
      {
        "id": "consortium-composition",
        "gameModel": "The runtime level presents the nitrifying consortium as two named partner microbes, Nitrosomonas and Nitrospira.",
        "realWorld": "Nitrification is real and is conventionally described in two steps, but the organisms are not a fixed universal pair. Ammonia-oxidising archaea as well as bacteria carry out the first step; comammox Nitrospira can carry out both steps in one organism; and in the one real biofilter measured in this packet's source estate, archaea and comammox Nitrospira dominated while Nitrosomonas was present at a tiny fraction of their abundance.",
        "curriculumTreatment": "The pathway figure prints the two-step conversion as the conventional framing and prints beside it that one organism can do both steps and that the community is not a fixed pair. Task 7 Account 4 makes the universal two-species claim an account to be refused on evidence.",
        "supportingSources": ["comammox-discovery", "biofilter-community"],
        "assessedIn": ["C06-T7"]
      },
      {
        "id": "plant-usable-forms",
        "gameModel": "The runtime level speaks of nitrate as the form the plants can finally drink, which can be heard as nitrate being the only usable form.",
        "realWorld": "Plants acquire inorganic nitrogen mainly as nitrate and as ammonium, through separate transporters, and mixtures of the two are reported to be better for growth than either alone.",
        "curriculumTreatment": "Every role states that plants take up both forms. The case's own contradiction is preserved without the false claim: in the fictional facility the nitrogen was present as ammonium and ammonia at levels the fictional crops could not tolerate while the nitrate they were being grown on was gone, which is a statement about that fictional system and not about what plants can use.",
        "supportingSources": ["plant-nitrogen-uptake", "epa-ammonia"],
        "assessedIn": ["C06-T4"]
      },
      {
        "id": "toxicity-threshold",
        "gameModel": "The runtime level says ammonia burned the roots and supplies no level, which invites a learner or a teacher to supply one.",
        "realWorld": "The threshold for ammonium toxicity depends on the species, the ecotype and even the cultivar, and on growing conditions; sensitivity varies widely and some species prefer ammonium. EPA's ammonia toxicity statements are about aquatic animals and pH-dependent speciation, not about crop plants.",
        "curriculumTreatment": "No role prints a concentration, a threshold or a lethal level for any plant. The chemistry that is printed is the speciation relationship - that raising pH shifts the balance toward the more toxic unionized ammonia - attributed to EPA and scoped to what EPA actually says.",
        "supportingSources": ["ammonium-tolerance", "epa-ammonia"],
        "assessedIn": []
      },
      {
        "id": "ammonia-ammonium-distinction",
        "gameModel": "The runtime level uses ammonia and ammonium loosely and sometimes interchangeably.",
        "realWorld": "Ammonia nitrogen includes both the ionized form ammonium (NH4+) and the unionized form ammonia (NH3); pH shifts the balance between them and the unionized form is the more toxic one.",
        "curriculumTreatment": "Both terms are printed with their formulas in every learner edition, the pH relationship is printed with them, and the vocabulary task assesses ammonium as a term in its own right rather than as a synonym for nitrogen.",
        "supportingSources": ["epa-ammonia"],
        "assessedIn": ["C06-T1", "C06-T4"]
      }
    ],
    "prohibitedFramings": {
      "rule": "Closed classes only. Each is a small, finite family of ways to state a universal that the real sources contradict, bound to a named subject. No open synonym family is policed anywhere in this contract.",
      "universalTwoSpecies": {
        "meaning": "Asserts that a nitrifying consortium is always, everywhere, exactly two species or two named organisms.",
        "subjectPatterns": [
          "\\bconsorti\\w*\\b",
          "\\bnitrif\\w*\\b",
          "\\bbiofilter\\w*\\b",
          "\\bnitrosomonas\\b",
          "\\bnitrospira\\b",
          "\\bnitrobacter\\b"
        ],
        "patterns": [
          "\\b(?:always|universally|invariably)\\s+(?:consists?|comprises?|contains?|is|are|made\\s+up)\\b",
          "\\b(?:is|are)\\s+(?:always|universally|invariably)\\s+(?:exactly\\s+)?two\\b",
          "\\bexactly\\s+two\\s+(?:species|organisms?|microbes?|bacteri\\w+|partners?|kinds?|types?)\\b",
          "\\b(?:consists?|comprises?|is\\s+made\\s+up)\\s+of\\s+(?:exactly\\s+|just\\s+|only\\s+)?two\\s+(?:species|organisms?|microbes?|bacteri\\w+|partners?)\\b",
          "\\bonly\\s+two\\s+(?:species|organisms?|microbes?|bacteri\\w+|partners?)\\b",
          "\\bthe\\s+two\\s+(?:species|organisms?|microbes?|bacteri\\w+)\\s+that\\s+(?:always|universally)\\b",
          "\\b(?:every|all|any)\\s+(?:nitrifying\\s+)?(?:consorti\\w*|biofilters?)\\s+(?:has|have|contains?|holds?|uses?)\\s+(?:the\\s+same\\s+)?two\\b"
        ]
      },
      "nitrateOnly": {
        "meaning": "Asserts that nitrate is the only form of nitrogen a plant can take up or use.",
        "subjectPatterns": [
          "\\bplants?\\b",
          "\\bcrops?\\b",
          "\\broots?\\b"
        ],
        "patterns": [
          "\\bnitrate\\s+is\\s+the\\s+only\\b",
          "\\bthe\\s+only\\s+(?:form|kind|type)\\s+of\\s+nitrogen\\s+(?:that\\s+)?(?:plants?|crops?|roots?)\\s+(?:can|could)\\b",
          "\\bonly\\s+(?:take\\s+up|absorb|use|drink)\\s+nitrate\\b",
          "\\bcan\\s?not\\s+(?:take\\s+up|absorb|use)\\s+ammoni\\w+\\b",
          "\\bcannot\\s+(?:take\\s+up|absorb|use)\\s+ammoni\\w+\\b",
          "\\bunable\\s+to\\s+(?:take\\s+up|absorb|use)\\s+ammoni\\w+\\b",
          "\\bno\\s+plant\\s+can\\s+(?:take\\s+up|absorb|use)\\s+ammoni\\w+\\b"
        ]
      },
      "universalToxicityThreshold": {
        "meaning": "Prints a numeric ammonia or ammonium level as a general threshold at which plants are harmed.",
        "patterns": [
          "\\b\\d+(?:\\.\\d+)?\\s*(?:ppm|mg\\s*/\\s*l|mg\\s+per\\s+litre|mg\\s+per\\s+liter|milligrams?\\s+per\\s+lit\\w+)\\s+(?:of\\s+)?(?:ammoni\\w+|nh3|nh4)\\b",
          "\\b(?:ammoni\\w+|nh3|nh4\\+?)\\s+(?:above|over|beyond|exceeding|at)\\s+\\d+(?:\\.\\d+)?\\s*(?:ppm|mg\\s*/\\s*l)\\b",
          "\\b\\d+(?:\\.\\d+)?\\s*(?:ppm|mg\\s*/\\s*l)\\s+(?:is|are|becomes?)\\s+(?:toxic|lethal|fatal|harmful)\\b"
        ]
      },
      "noAccountability": {
        "meaning": "Asserts that because no machine broke and no individual caused the failure, no responsibility of any kind arises.",
        "patterns": [
          "\\bno\\s?one\\s+(?:was|is)\\s+(?:responsible|to\\s+blame|at\\s+fault|accountable)\\b",
          "\\bnobody\\s+(?:was|is)\\s+(?:responsible|to\\s+blame|at\\s+fault|accountable)\\b",
          "\\bthere\\s+(?:is|was)\\s+no\\s+(?:accountability|responsibility|blame|fault)\\b",
          "\\bno\\s?one\\s+(?:could|can)\\s+have\\s+(?:done|prevented)\\s+anything\\b",
          "\\bnothing\\s+(?:could|can)\\s+have\\s+been\\s+done\\b",
          "\\bno\\s+(?:institution|company|organisation|organization)\\s+(?:is|was)\\s+(?:responsible|accountable|at\\s+fault)\\b"
        ]
      },
      "verdictAdopted": {
        "meaning": "States the fictional public statement's verdict as an established finding of this packet.",
        "patterns": [
          "\\bthe\\s+engineer\\s+(?:caused|was\\s+responsible\\s+for|is\\s+responsible\\s+for|is\\s+to\\s+blame\\s+for)\\s+(?:the\\s+)?(?:failure|collapse|deaths?|disaster)\\b",
          "\\bhuman\\s+error\\s+(?:caused|was\\s+the\\s+cause\\s+of|explains)\\s+(?:the\\s+)?(?:failure|collapse|disaster)\\b",
          "\\b(?:the\\s+)?(?:failure|collapse)\\s+was\\s+caused\\s+by\\s+human\\s+error\\b",
          "\\bthe\\s+(?:design|nutrient-cycling\\s+design)\\s+was\\s+flawed\\b"
        ]
      }
    },
    "positiveRequirements": [
      {
        "id": "diversity-printed",
        "rule": "Both learner editions print that the nitrifying community is not a fixed pair of species, with the real source named.",
        "roles": ["student", "accessible"],
        "selector": "[data-science-qualification=\"consortium-composition\"]"
      },
      {
        "id": "both-forms-printed",
        "rule": "Both learner editions print that plants take up both nitrate and ammonium.",
        "roles": ["student", "accessible"],
        "selector": "[data-science-qualification=\"plant-usable-forms\"]"
      },
      {
        "id": "speciation-printed",
        "rule": "Both learner editions print the ammonia and ammonium forms with their formulas and the pH relationship between them.",
        "roles": ["student", "accessible"],
        "selector": "[data-science-qualification=\"ammonia-ammonium-distinction\"]"
      },
      {
        "id": "no-threshold-declared",
        "rule": "Every role states that no single toxicity threshold is printed and why.",
        "roles": ["teacher", "answer"],
        "selector": "[data-science-qualification=\"toxicity-threshold\"]"
      }
    ]
  },
  "accountabilityBoundary": {
    "id": "vertical-farm-accountability-v1.0",
    "rule": "The evidence clears the named engineer of the failure the public statement describes. It does not establish that a complex failure with no individual culprit raises no institutional question. Both halves are required in every role, and Task 8 assesses both.",
    "establishedByEvidence": [
      "The engineering records show the machinery met its designed setpoints through the failure.",
      "The biological trace shows the living subsystem failed before the chemistry moved and before the crops died.",
      "The public statement's account - a flawed nutrient-cycling design - is not supported by any record in this packet."
    ],
    "notEstablishedByEvidence": [
      "That the sanitiser flush, the pH dip or the warm spell caused the collapse.",
      "That the collapse could not have been detected earlier by any means.",
      "That no person or body could have chosen differently about what to monitor or how to commission a living subsystem.",
      "That the institution's choice of public account was reasonable."
    ],
    "openInstitutionalQuestions": [
      "Why did the monitoring that triggered alarms watch only the engineered zone?",
      "Why were three events lethal to a microbial community filed as within tolerance?",
      "Was the living part of the loop commissioned and verified with the same care as the steel?",
      "What is a public statement for, when the investigation it reports has not been done?"
    ],
    "requiredFraming": "two-sided",
    "assessedIn": ["C06-T8", "C06-T9"]
  },
  "sourceStatusContract": {
    "rule": "Every learner-facing evidence object carries a printed STATUS line bound to a canonical source in this registry, and every such object declares its truth layer in markup as well as in print.",
    "statusVocabulary": [
      "fictional / hypothetical",
      "documented",
      "modeled"
    ],
    "layerAttribute": "data-evidence-layer",
    "layerValues": ["fictional", "real", "curriculum-model"],
    "twoLayerNoticeRequired": ["student", "accessible"],
    "twoLayerNoticeRule": "Page 1 of both learner editions carries the two-layer truth notice, which states that the 2041 facility is invented, that the science is real, and that neither one is evidence for the other.",
    "fictionalDataRule": "Every deterministic figure, date, day number or duration belonging to the fictional case sits inside a node carrying data-fictional-data, and every figure that displays such values prints the words FICTIONAL CASE DATA.",
    "prohibitedRuntimeIdentifiers": [
      "failed_farm_floor",
      "control_room",
      "press_briefing",
      "farm_researcher",
      "examine_crops",
      "scan_systems",
      "survey_floor",
      "systems_engineer",
      "query_systems",
      "review_records",
      "facility_spokesperson",
      "query_archive",
      "press_records",
      "starved_while_fed",
      "ammonia_burn",
      "systems_running",
      "facility_scale",
      "hardware_to_spec",
      "consortium_crash",
      "trigger_event",
      "false_verdict",
      "regulatory_stakes",
      "public_record",
      "clueTag",
      "revealsClue",
      "bonusInsight",
      "taaCommsHints",
      "resolveLabel",
      "resolveNag",
      "locationFx",
      "ledFlicker"
    ],
    "prohibitedRuntimeIdentifierRule": "No runtime clue tag, source key, location id, node name or route may appear in any role. The list holds only identifier-shaped strings, so that forbidding them forbids nothing a learner would ever legitimately write."
  },
  "claimJudgments": {
    "markScheme": {
      "Y": "the evidence in this packet supports it",
      "N": "the evidence in this packet goes against it",
      "?": "this packet cannot decide it"
    },
    "claims": [
      { "number": "1", "layer": "systems", "mark": "Y" },
      { "number": "2", "layer": "accountability", "mark": "N" },
      { "number": "3", "layer": "chemistry", "mark": "N" },
      { "number": "4", "layer": "microbiology", "mark": "N" },
      { "number": "5", "layer": "trigger", "mark": "?" }
    ],
    "statementClaims": [
      { "number": "1", "subject": "the machinery was at fault", "mark": "N" },
      { "number": "2", "subject": "the named engineer's design caused it", "mark": "N" },
      { "number": "3", "subject": "tighter engineering oversight will prevent a repeat", "mark": "?" }
    ]
  },
  "chronology": [
    { "id": "fixed-first", "label": "Day 1", "what": "The facility opens its second growing cycle. Every system is commissioned and signed off.", "fixed": true, "layer": "fictional" },
    { "id": "P", "label": "Day 58", "what": "The biological trace shows the consortium steady, as it has been since commissioning.", "order": 1, "layer": "fictional" },
    { "id": "Q", "label": "Days 59 to 61", "what": "Three maintenance events are logged, each filed within tolerance: a sanitiser flush, a dip in pH, and a warm spell from a cycling chiller.", "order": 2, "layer": "fictional" },
    { "id": "R", "label": "Days 61 to 63", "what": "The consortium trace falls across about seventy-two hours and then runs flat.", "order": 3, "layer": "fictional" },
    { "id": "S", "label": "From day 64", "what": "Ammonia rises and nitrate falls. The dosing hardware meters nutrient on schedule and logs no fault.", "order": 4, "layer": "fictional" },
    { "id": "fixed-last", "label": "From day 70", "what": "The crops brown floor by floor. Three weeks later the inquiry closes on human error.", "fixed": true, "layer": "fictional" }
  ],
  "unsettledDetails": [
    {
      "id": "collapse-trigger",
      "subject": "which logged event, if any, collapsed the consortium",
      "status": "undecidable from this packet",
      "whatIsDocumented": "Inside the fiction: that three events were logged in the three days before the trace fell, that all three were filed within tolerance, and that the trace fell afterwards.",
      "whatIsNot": "Which one, whether any of them, or whether some combination. The fictional record holds no biological measurement between the events and the collapse, and no control.",
      "rule": "No role names a trigger as established. Task 5 Part C and Task 7 Account 5 both make the uncertainty the assessed object.",
      "printedIn": ["student", "teacher", "answer", "accessible"]
    },
    {
      "id": "consortium-species",
      "subject": "which organisms made up the fictional facility's consortium",
      "status": "not established, and not establishable",
      "whatIsDocumented": "That the fictional trace recorded a collapse in the biological activity of the biofilter.",
      "whatIsNot": "Any species, any count, any composition. The fictional record names none, and the real sources in this packet show that a designer's expected pair and a working biofilter's actual community can differ by orders of magnitude.",
      "rule": "No role states what the fictional consortium was made of. Task 7 Account 4 makes the universal two-species claim an account to be refused.",
      "printedIn": ["student", "teacher", "answer", "accessible"]
    },
    {
      "id": "detection-counterfactual",
      "subject": "whether better monitoring would have saved the crop",
      "status": "not established",
      "whatIsDocumented": "That the monitoring in place watched the engineered zone and reported no fault throughout.",
      "whatIsNot": "That biological monitoring would have caught the collapse in time, or that any particular intervention would have worked. The packet supports the question, not the answer.",
      "rule": "Task 8 Part C asks for an open institutional question and does not accept a counterfactual stated as a finding.",
      "printedIn": ["teacher", "answer"]
    }
  ],
  "editionResponseContract": {
    "rule": "Every learner response control in either edition belongs to exactly one assessed subpart, and every subpart declares what each edition is obliged to produce. Parity is checked against these canonical obligations rather than against prose, so an Accessible edition cannot acquire a required response the Student edition never asks for.",
    "whyItExists": "Carried forward from Case 05, where the first candidate's Accessible edition asked for a relation as its own assessed part while the Student edition was given that relation on the figure - an undeclared, demand-increasing adaptation that no text-level check caught. Comparing declared obligations per subpart does catch it.",
    "differenceClasses": {
      "parity": "Both editions produce the same number of responses for the same obligation.",
      "declared-reduction": "The Accessible edition produces fewer, under a registered entry in accessibleAdaptations. This is a scored difference and must be disclosed to the teacher and the key.",
      "chunking": "The Accessible edition splits one Student field into several, with an identical assessed obligation. Support under the Accessible Adaptation Contract; not a scored difference, because nothing more is demanded.",
      "accessible-only": "PROHIBITED. A required Accessible response with no Student counterpart is a demand increase and fails validation."
    },
    "identityFields": {
      "student": ["student-name", "student-date", "student-class"],
      "accessible": ["a-name", "a-date", "a-class"]
    },
    "subparts": [
      {
        "task": "C06-T1",
        "id": "vocabulary-placements",
        "obligation": "Place seven exact-match terms.",
        "student": ["t1-term-1", "t1-term-2", "t1-term-3", "t1-term-4", "t1-term-5", "t1-term-6", "t1-term-7"],
        "accessible": ["a1-term-1", "a1-term-2", "a1-term-3", "a1-term-4", "a1-term-5", "a1-term-6", "a1-term-7"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T2",
        "id": "inquiry-reading",
        "obligation": "State the inquiry's conclusion and whether the case file so far supports it.",
        "student": ["t2-verdict"],
        "accessible": ["a2-verdict"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T2",
        "id": "first-question",
        "obligation": "Write one first audit question with a reason.",
        "student": ["t2-question"],
        "accessible": ["a2-question"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T3",
        "id": "zone-placements",
        "obligation": "Assign four components to the engineered or the living zone.",
        "student": ["t3-zone-1", "t3-zone-2", "t3-zone-3", "t3-zone-4"],
        "accessible": ["a3-zone-1", "a3-zone-2", "a3-zone-3", "a3-zone-4"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T3",
        "id": "monitoring-zone",
        "obligation": "Name the zone the facility's alarms watched.",
        "student": ["t3-watched"],
        "accessible": ["a3-watched"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T3",
        "id": "boundary-reasoning",
        "obligation": "Explain how every machine can run correctly while the farm dies.",
        "student": ["t3-gap"],
        "accessible": ["a3-gap"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T4",
        "id": "pathway-stages",
        "obligation": "Complete the open conversion stages of the nitrogen pathway.",
        "student": ["t4-stage-2", "t4-stage-3"],
        "accessible": ["a4-stage-3"],
        "differenceClass": "declared-reduction",
        "governedBy": "t4-modelled-stage"
      },
      {
        "task": "C06-T4",
        "id": "nitrogen-forms",
        "obligation": "Name the form that burned the roots and the form the crops ran short of.",
        "student": ["t4-toxic", "t4-usable"],
        "accessible": ["a4-toxic", "a4-usable"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T4",
        "id": "living-step",
        "obligation": "Name the step that is not a machine and say what the dosing records could not detect.",
        "student": ["t4-living-step"],
        "accessible": ["a4-living-step"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T5",
        "id": "chronology-order",
        "obligation": "Order the four middle entries of the chronology.",
        "student": ["t5-order-1", "t5-order-2", "t5-order-3", "t5-order-4"],
        "accessible": ["a5-order-1", "a5-order-2", "a5-order-3", "a5-order-4"],
        "differenceClass": "parity",
        "supportNote": "The Accessible cards carry their day labels under t5-dated-cards. That names where each card sits on the timeline, not what the order establishes, and changes no response count."
      },
      {
        "task": "C06-T5",
        "id": "sequence-finding",
        "obligation": "State which subsystem failed first and how the order shows it.",
        "student": ["t5-first"],
        "accessible": ["a5-first"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T5",
        "id": "trigger-limit",
        "obligation": "Explain why the chronology cannot establish which logged event caused the collapse.",
        "student": ["t5-trigger"],
        "accessible": ["a5-trigger"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T6",
        "id": "audit-cells",
        "obligation": "State what each record measures and what it cannot show.",
        "student": ["t6-r1-measures", "t6-r1-blind", "t6-r2-measures", "t6-r2-blind", "t6-r3-measures", "t6-r3-blind", "t6-r4-measures", "t6-r4-blind", "t6-r5-measures", "t6-r5-blind"],
        "accessible": ["a6-r2-measures", "a6-r2-blind", "a6-r3-measures", "a6-r3-blind", "a6-r4-measures", "a6-r4-blind", "a6-r5-measures", "a6-r5-blind"],
        "differenceClass": "declared-reduction",
        "governedBy": "t6-modelled-row"
      },
      {
        "task": "C06-T6",
        "id": "convergence",
        "obligation": "Name the two records that together rule out a hardware failure and say why neither does it alone.",
        "student": ["t6-converge"],
        "accessible": ["a6-converge"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T7",
        "id": "account-marks",
        "obligation": "Mark five accounts Y, N or question mark.",
        "student": ["t7-mark-1", "t7-mark-2", "t7-mark-3", "t7-mark-4", "t7-mark-5"],
        "accessible": ["a7-mark-1", "a7-mark-2", "a7-mark-3", "a7-mark-4", "a7-mark-5"],
        "differenceClass": "parity",
        "supportNote": "The Accessible accounts carry source pointers under t7-source-pointers. That names where to look, not what to write, and changes no response count."
      },
      {
        "task": "C06-T7",
        "id": "settle-undecided",
        "obligation": "Name evidence that would settle the undecided account.",
        "student": ["t7-settle"],
        "accessible": ["a7-settle"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T8",
        "id": "statement-marks",
        "obligation": "Mark the three public claims against the packet's evidence.",
        "student": ["t8-claim-1", "t8-claim-2", "t8-claim-3"],
        "accessible": ["a8-claim-1", "a8-claim-2", "a8-claim-3"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T8",
        "id": "engineer-finding",
        "obligation": "State what the evidence establishes about the named engineer.",
        "student": ["t8-engineer"],
        "accessible": ["a8-engineer"],
        "differenceClass": "parity"
      },
      {
        "task": "C06-T8",
        "id": "open-question",
        "obligation": "Name one institutional question the evidence leaves open, and the record that raised it.",
        "student": ["t8-open"],
        "accessible": ["a8-open-question", "a8-open-record"],
        "differenceClass": "chunking",
        "chunkingNote": "One Student field collects the question and the record it came from; the Accessible edition asks for them as two steps. The assessed obligation is identical and the Answer Key models both halves for both editions."
      },
      {
        "task": "C06-T9",
        "id": "culminating-explanation",
        "obligation": "Write the four-part systems and evidence-audit explanation.",
        "student": ["t9-explanation"],
        "accessible": ["a9-explanation"],
        "differenceClass": "parity"
      }
    ]
  },
  "accessibleAdaptations": [
    {
      "id": "t4-modelled-stage",
      "task": "C06-T4",
      "what": "The first open conversion stage of the pathway is supplied complete as a worked model.",
      "effect": "The Accessible learner completes one open stage independently; the Student learner completes two.",
      "whyNotALeak": "The two stages are the same operation performed twice - naming a conversion and the kind of thing that performs it. Showing one worked does not answer the other, and Parts B and C, which carry the assessed chemistry and the assessed systems reasoning, are untouched.",
      "declaredIn": ["accessible", "teacher", "answer"]
    },
    {
      "id": "t6-modelled-row",
      "task": "C06-T6",
      "what": "The first record row of the audit matrix, the dosing and pump logs, is supplied complete in both cells as a worked model.",
      "effect": "The Accessible learner completes four rows and eight cells independently; the Student learner completes five rows and ten cells.",
      "whyNotALeak": "The modelled row shows what a filled pair of cells looks like. The record that carries the case's reasoning is the biological trace, and that row is the learner's in both editions, as are the crop evidence, the maintenance log and the public statement.",
      "declaredIn": ["accessible", "teacher", "answer"]
    },
    {
      "id": "t5-dated-cards",
      "task": "C06-T5",
      "what": "The four chronology cards carry their day labels in the Accessible edition; in the Student edition the labels are printed on the timeline rail instead of on the cards.",
      "effect": "Ordering becomes a matching operation rather than a reconstruction. Parts B and C, which are the assessed reasoning, are unchanged.",
      "whyNotALeak": "Part B asks what the order establishes and Part C asks what it cannot establish. Knowing the day numbers answers neither.",
      "declaredIn": ["accessible", "teacher", "answer"]
    },
    {
      "id": "t7-source-pointers",
      "task": "C06-T7",
      "what": "Each of the five accounts carries a printed pointer to the source or sources that bear on it.",
      "effect": "The Accessible learner is told where to look and is never told what to write.",
      "whyNotALeak": "The pointer names a source. The mark is still a judgement about what that source establishes, and Account 5 remains undecidable with its pointer in place.",
      "declaredIn": ["accessible", "teacher"]
    }
  ],
  "semanticInvariants": {
    "scanScope": {
      "roles": ["student", "teacher", "answer", "accessible"],
      "unit": "sentence",
      "rule": "Every sentence in every role is scanned, together with the accessibility text of every figure, unless the node carries a registered exemption id. Exemption is granted only by the closed contract below: markup cannot self-authorize, and every registered exemption declares its roles and its purpose.",
      "exemptionAttribute": "data-semantic-exemption",
      "designNote": "These guards are deliberately narrow. Each protects one curricular boundary by policing a closed class of universal, absolute or verdict-adopting language bound to a named subject, plus a positive structural requirement that the correct framing is actually present. None of them attempts to recognise every English paraphrase of a wrong idea, and none of them depends on enumerating synonyms for an ordinary verb. Case 05's zero-boundary guard was needed because the runtime level itself carried the absolute; nothing comparable exists here, so nothing comparable is built."
    },
    "exemptions": [
      {
        "id": "account-under-test-learner",
        "roles": ["student", "accessible"],
        "purpose": "Task 7 accounts are propositions offered to the learner for judgment, not assertions of the packet.",
        "allowedConcepts": ["universalTwoSpecies", "nitrateOnly", "verdictAdopted", "noAccountability"]
      },
      {
        "id": "account-under-test-key",
        "roles": ["answer"],
        "purpose": "The Answer Key restates each competing account beside the mark that decides it.",
        "allowedConcepts": ["universalTwoSpecies", "nitrateOnly", "verdictAdopted", "noAccountability"]
      },
      {
        "id": "public-statement-quoted",
        "roles": ["student", "teacher", "answer", "accessible"],
        "purpose": "The fictional public statement has to be printed in its own words in order to be audited. Every such node also sits inside a fictional-layer evidence object.",
        "allowedConcepts": ["verdictAdopted"]
      },
      {
        "id": "teacher-misconception",
        "roles": ["teacher"],
        "purpose": "The Teacher misconceptions table and the prose warnings name an error in order to reject it.",
        "allowedConcepts": ["universalTwoSpecies", "nitrateOnly", "verdictAdopted", "noAccountability", "universalToxicityThreshold"]
      },
      {
        "id": "teacher-rubric-floor",
        "roles": ["teacher"],
        "purpose": "Rubric descriptors that quote the disqualifying answer in order to place a floor under it.",
        "allowedConcepts": ["universalTwoSpecies", "nitrateOnly", "verdictAdopted", "noAccountability"]
      },
      {
        "id": "answer-key-floor",
        "roles": ["answer"],
        "purpose": "Answer Key floors that quote the answer they refuse to accept at any level.",
        "allowedConcepts": ["universalTwoSpecies", "nitrateOnly", "verdictAdopted", "noAccountability"]
      },
      {
        "id": "game-wording-reported",
        "roles": ["teacher"],
        "purpose": "Places where the runtime level's own simplification is reported so the teacher can qualify it after play.",
        "allowedConcepts": ["universalTwoSpecies", "nitrateOnly"]
      },
      {
        "id": "learner-refutation-prompt",
        "roles": ["student", "accessible"],
        "purpose": "Prompts that quote a wrong reading and ask the learner to refuse it using the printed evidence.",
        "allowedConcepts": ["verdictAdopted", "noAccountability"]
      },
      {
        "id": "accountability-notice",
        "roles": ["student", "accessible"],
        "purpose": "The Task 8 framing names the no-accountability overcorrection in order to warn a learner away from it. It is the one place in a learner edition that has to say the wrong thing out loud.",
        "allowedConcepts": ["noAccountability"]
      },
      {
        "id": "vocabulary-term-list",
        "roles": ["teacher"],
        "purpose": "An enumeration of the case vocabulary is a term list, not a claim about any term in it.",
        "allowedConcepts": ["universalTwoSpecies", "nitrateOnly"]
      }
    ],
    "structuralExemptSelectors": [
      { "selector": ".word-bank", "why": "a word bank is a list of terms and asserts nothing about any of them" },
      { "selector": ".source-table", "why": "the Teacher source ledger reports what each source states, including what the fictional statement claims, under its own printed status column" }
    ]
  },
  "figureAccessibilityContract": {
    "rule": "Critical figure accessibility text carries the same distinctions the visible figure carries. It is checked against canonical registry metadata, not against one hard-coded sentence.",
    "figures": [
      {
        "id": "system-boundary",
        "selector": "[data-boundary-contract]",
        "roles": ["student", "accessible"],
        "requiresAllZones": true,
        "requiresMonitoringGap": true,
        "requiresSchematicDisclaimer": true,
        "prohibitedPatterns": [
          {
            "id": "facility-as-real",
            "regex": "(?:the\\s+world's\\s+first|actually\\s+built|really\\s+exists?|a\\s+real\\s+facility)",
            "why": "the facility is fictional and the accessibility text must not present it as an existing building"
          }
        ]
      },
      {
        "id": "nitrogen-pathway",
        "selector": "[data-pathway-contract]",
        "roles": ["student", "accessible"],
        "requiresAllForms": ["ammonium", "ammonia", "nitrite", "nitrate"],
        "requiresBothUsableForms": true,
        "requiresDiversityNote": true,
        "prohibitedPatterns": [
          {
            "id": "nitrate-only-aria",
            "regex": "(?:only\\s+form\\s+of\\s+nitrogen|nitrate\\s+is\\s+the\\s+only)",
            "why": "the accessibility text must carry the same both-forms boundary the visible figure carries"
          },
          {
            "id": "two-species-aria",
            "regex": "(?:always\\s+two|exactly\\s+two\\s+species)",
            "why": "the accessibility text must not restate the universal the figure exists to qualify"
          }
        ]
      },
      {
        "id": "chronology",
        "selector": "[data-chronology-contract]",
        "roles": ["student", "accessible"],
        "requiresFictionalDataLabel": true,
        "requiresEngineeringRail": true,
        "prohibitedPatterns": [
          {
            "id": "trigger-as-cause",
            "regex": "(?:the\\s+flush|the\\s+sanitiser\\s+flush|the\\s+ph\\s+dip|the\\s+warm\\s+spell)[^.]{0,40}(?:caused|killed|collapsed)",
            "why": "the chronology names candidates and the packet establishes no trigger"
          }
        ]
      },
      {
        "id": "record-audit",
        "selector": "[data-audit-contract]",
        "roles": ["student", "accessible"],
        "requiresAccessibilityText": false,
        "accessibilityNote": "This figure is a data table, not a drawing. It carries its own semantics through its caption, its column headers and a scoped row header on every record, so it is checked for those rather than for a prose alt text. Wrapping a navigable table in role=img would replace a structure a screen-reader user can move around in with a paragraph they cannot.",
        "requiresAllRecords": 5,
        "requiresBothColumns": true,
        "prohibitedPatterns": [
          {
            "id": "ranked-records",
            "regex": "(?:most\\s+reliable|least\\s+reliable|best\\s+source|worst\\s+source)",
            "why": "the matrix sets out what each record can carry and ranks none of them"
          }
        ]
      },
      {
        "id": "public-record",
        "selector": "[data-verdict-contract]",
        "roles": ["student", "accessible"],
        "requiresOpenQuestionColumn": true,
        "requiresBothAccountabilityHalves": true,
        "prohibitedPatterns": [
          {
            "id": "no-accountability-aria",
            "regex": "(?:no\\s?one\\s+(?:was|is)\\s+(?:responsible|to\\s+blame)|nobody\\s+(?:was|is)\\s+(?:responsible|to\\s+blame))",
            "why": "clearing a named person is not the same as closing every institutional question, and the accessibility text must carry both halves"
          }
        ]
      }
    ]
  },
  "standards": {
    "directlyAssessed": [
      "C3 D3.2.6-8",
      "CCSS RH.6-8.7",
      "CCSS RH.6-8.8"
    ],
    "supporting": [
      "C3 D2.His.14.6-8",
      "C3 D4.1.6-8",
      "CCSS RH.6-8.1",
      "CCSS WHST.6-8.2"
    ],
    "contextual": [
      "NGSS MS-LS2-3",
      "NGSS MS-ETS1-1"
    ],
    "ngss": "Both NGSS references are contextual only. Tasks 3, 4 and 5 do reason about the cycling of matter through a system that contains living components, and Task 8 does reason about how a designed system's monitoring defined what could be noticed. But the assessed product is an evidence audit of competing records and an accountability judgment about a public statement, not a science or engineering practice: no learner develops a model from data, designs or tests a solution, or defines an engineering problem against criteria and constraints in the way those performance expectations describe. The real science in this packet is supplied to the learner as sourced reading and is used to qualify a fictional model, which is source reasoning rather than science practice. No NGSS alignment is claimed as directly assessed.",
    "rationale": "C3 D3.2.6-8 is the case's directly assessed home because Task 6 is a five-record contribution-and-limitation audit and Task 8 evaluates a public claim against the evidence behind it. CCSS RH.6-8.7 is directly assessed because five curriculum figures are read against the written sources at Tasks 3, 4, 5, 6 and 8. CCSS RH.6-8.8 is directly assessed because distinguishing a claim from the evidence that supports it is the entire operation of Tasks 7 and 8. The Phase 1 planning candidate C3 D3.2.6-8 is confirmed and promoted; the planning candidate CCSS RH.6-8.7 is confirmed; C3 D2.His.14.6-8 is demoted to supporting because this case's causation reasoning is about a technical system rather than about historical causation, and CCSS WHST.6-8.2 remains supporting because Task 9 is scored for reasoning rather than for craft."
  }
};
