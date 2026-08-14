window.HHH_CASE04_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "HHH-C1-CASE04",
  "runtimeId": "L4",
  "instructionalType": "CORE_CASE",
  "title": "Karlsruhe",
  "displayLabel": "4 - Karlsruhe",
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
    "accessible": 14
  },
  "culminatingProduct": "Historical-technological explanation that states the balance problem the chemistry set, says what each of pressure, temperature, catalyst and recycle contributes, distinguishes what Haber's laboratory established from what Bosch and BASF had to solve, and explains why the workable process cannot be credited to one step or one kind of work. Canonical CER is deliberately not used; the product is an explanation of a technology, not a claim-evidence-reasoning argument, and forcing CER would collapse the attribution reasoning into a single claim. See the Teacher Guide reasoning architecture.",
  "tasks": [
    {
      "id": "C04-T1",
      "number": "1",
      "semanticLabel": "CASE VOCABULARY",
      "icon": "ph-book",
      "title": "Build the Case Vocabulary",
      "description": "Apply the six case terms to the things and actions they name rather than copying definitions.",
      "instructionalPurpose": "Establish the six terms the case is unreadable without. The catalyst statement carries the equilibrium boundary in its own wording, so a learner who places it correctly has already met the distinction Task 4 and Task 7 assess.",
      "provenance": [
        "Curriculum-authored definitions",
        "Established chemistry of the ammonia equilibrium"
      ],
      "responseType": "six exact-match term placements",
      "answerScope": "One term per statement, drawn from the shared six-term bank with no decoys.",
      "pagePlacement": {
        "student": "student-karlsruhe-01",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-karlsruhe-01"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C04-T2",
      "number": "2",
      "semanticLabel": "FIRST READING",
      "icon": "ph-diagnosis",
      "title": "Record a First Explanation",
      "description": "Write down why you think the bench experiment gives so little ammonia, and name one thing you would have to find out before trusting that answer.",
      "instructionalPurpose": "Provisional interpretation recorded before the tradeoff evidence arrives. Most learners write either 'the apparatus is leaking' or 'he needs more heat', which are the two wrong diagnoses the game itself offers. The case is built so the learner overturns their own answer at Task 3 rather than being corrected.",
      "provenance": [
        "Game reconstruction of the bench at Karlsruhe",
        "Curriculum-authored prompt"
      ],
      "responseType": "two short constructed responses",
      "answerScope": "One provisional explanation of the small yield and one named check that would have to come from outside the bench scene.",
      "pagePlacement": {
        "student": "student-karlsruhe-03",
        "teacher": "teacher-guide-03",
        "answer": "answer-key-01",
        "accessible": "accessible-karlsruhe-05"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C04-T3",
      "number": "3",
      "semanticLabel": "THE TRADEOFF",
      "icon": "ph-scales",
      "title": "Read the Two Tradeoffs",
      "description": "Use the tradeoff panel to say which way pressure and temperature each push, then say what the operating temperature is a compromise between and how hot it actually is.",
      "instructionalPurpose": "Family H8 tradeoff visualisation and the load-bearing qualification task of the whole case. Part C is the audit requirement made assessable: a learner who writes that the process runs at a gentle or moderate warmth has not met the standard, because the printed temperature ruler puts the operating range above the melting point of lead. The panel gives directions and anchored values only; it draws no invented curve.",
      "provenance": [
        "Haber and Le Rossignol, US Patent 1,202,995",
        "Appl 1997 on modern operating conditions",
        "Travis 2015 on Haber's laboratory conditions",
        "Established chemistry of the ammonia equilibrium",
        "Royal Society of Chemistry melting-point value for lead",
        "Curriculum-created tradeoff panel"
      ],
      "responseType": "two marked directions plus two short constructed responses",
      "answerScope": "The direction pressure pushes the balance, the direction temperature pushes the balance, what the operating temperature is a compromise between, and a statement of how hot that compromise actually is using a value from the ruler.",
      "pagePlacement": {
        "student": "student-karlsruhe-04",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-02",
        "accessible": "accessible-karlsruhe-06"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C04-T4",
      "number": "4",
      "semanticLabel": "THE WORKING LOOP",
      "icon": "ph-flow",
      "title": "Complete the Process Loop",
      "description": "Fill the missing stages of the loop, then say in one line each what the catalyst contributes and what the recycle contributes.",
      "instructionalPurpose": "Family H8 process and system diagram. Part B is the catalyst boundary: a catalyst changes how fast the balance is reached and does not change where the balance sits, and an answer that has the catalyst producing more ammonia at the balance is not accepted. Part C establishes that no single pass converts the feed, which is why the loop exists at all.",
      "provenance": [
        "Haber and Le Rossignol, US Patent 1,202,995, on passing unreacted gas over the catalyst again",
        "Appl 1997 on the recycle concept and the promoted iron catalyst",
        "Established chemistry on catalysts and the position of equilibrium",
        "Curriculum-created process figure"
      ],
      "responseType": "three organizer stages plus two short constructed responses",
      "answerScope": "The compression stage, the separation of ammonia, the return of unreacted gas, one statement of what the catalyst does and does not do, and one statement of why the leftover gas is worth sending round again.",
      "pagePlacement": {
        "student": "student-karlsruhe-05",
        "teacher": "teacher-guide-04",
        "answer": "answer-key-03",
        "accessible": "accessible-karlsruhe-08"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C04-T5",
      "number": "5",
      "semanticLabel": "WHOSE WORK",
      "icon": "ph-nodes",
      "title": "Sort the Work and Put It in Order",
      "description": "Use the technology sequence to place four pieces of work with the people who did them, and explain why the laboratory result was not yet a working process.",
      "instructionalPurpose": "Family H11 technology sequence and the historical attribution operation. The three lanes are drawn at equal weight on purpose: a learner reading the figure should be unable to conclude that the plant engineers merely copied the bench. Part B is the assessed reasoning and is the hinge of the culminating product.",
      "provenance": [
        "Travis 2015 on the laboratory, the catalyst search and the converter",
        "Appl 1997 on the scale-up and the Oppau plant",
        "Haber and Le Rossignol, US Patent 1,202,995, for the filing date and the named inventors",
        "BASF corporate chronology for the company's own account",
        "Curriculum-created technology sequence"
      ],
      "responseType": "four marked placements plus one explanation",
      "answerScope": "Four pieces of work matched to Haber, Le Rossignol, Mittasch and Bosch, and an explanation naming at least one specific thing that still had to be solved after the demonstration worked.",
      "pagePlacement": {
        "student": "student-karlsruhe-06",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-04",
        "accessible": "accessible-karlsruhe-10"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C04-T6",
      "number": "6",
      "semanticLabel": "SOURCE STATUS",
      "icon": "ph-book",
      "title": "Decide What Each Source Can Show",
      "description": "For each of the five kinds of evidence in this case, name its status and state what it contributes and what it cannot establish on its own.",
      "instructionalPurpose": "Family H4 contribution-and-limitation matrix across five different evidentiary statuses. Row one against row two is the pair the case exists to separate: a scene written for a game and a patent filed in 1909 are not the same kind of thing. Row three carries a real disagreement between two published historians about a date, and row four an estimate that is not a count.",
      "provenance": [
        "Game reconstruction at the integrated game baseline",
        "Haber and Le Rossignol, US Patent 1,202,995",
        "Travis 2015 and Appl 1997, which date the decisive demonstration differently",
        "Erisman and others 2008 for the population estimate",
        "Curriculum-created matrix and process figure"
      ],
      "responseType": "five-row status, contribution and limitation matrix",
      "answerScope": "Fifteen bounded cells; the five rows must carry five different statuses and five different limits.",
      "pagePlacement": {
        "student": "student-karlsruhe-07",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-04",
        "accessible": "accessible-karlsruhe-12"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C04-T7",
      "number": "7",
      "semanticLabel": "COMPETING CLAIMS",
      "icon": "ph-diagnosis",
      "title": "Weigh Five Claims",
      "description": "Mark five claims about the process and the people against the evidence in this packet, then say what would be needed to settle the one you could not decide.",
      "instructionalPurpose": "Competing interpretations with three marks rather than two. Claim 2 is the catalyst-shifts-equilibrium error, Claim 3 the coldest-is-best error and Claim 4 the attribution collapse. Claim 5 is undecidable here on purpose and is a real disagreement in the published record rather than a manufactured one: the packet carries two historians giving different dates for the same demonstration, and it carries the reason neither can be preferred from this evidence.",
      "provenance": [
        "Established chemistry on catalysts, pressure and temperature",
        "Travis 2015 and Appl 1997 on the demonstration date",
        "Travis 2015 and Appl 1997 on the scale-up work",
        "Curriculum-created claims"
      ],
      "responseType": "five marked judgments plus one short constructed response",
      "answerScope": "One supported claim, three contradicted claims, one claim this packet cannot decide, and a named kind of evidence that would move the undecided claim.",
      "pagePlacement": {
        "student": "student-karlsruhe-07",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-05",
        "accessible": "accessible-karlsruhe-13"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    },
    {
      "id": "C04-T8",
      "number": "8",
      "semanticLabel": "TECHNOLOGICAL EXPLANATION",
      "icon": "ph-wrench",
      "title": "Explain What Made the Process Workable",
      "description": "Write the case's explanation, using the four choices, the two kinds of work, and specific sourced evidence — then apply the same test to a new announcement.",
      "instructionalPurpose": "Culminating product for the case: a historical-technological explanation. Part D carries the transfer function of the Core Case spine inside the culminating task rather than as a separate ninth task, because the operation being transferred — that a laboratory result is not yet a technology — is the same operation Parts A to C assess, and a standalone transfer task would have re-measured it on a fresh page for no additional information.",
      "provenance": [
        "Curriculum-authored prompt",
        "Blueprint culminating-product policy",
        "Blueprint transfer and exit policy"
      ],
      "responseType": "extended constructed response with four required parts",
      "answerScope": "The balance problem and why more heat does not solve it, what each of the four choices contributes with temperature named as a compromise, what Haber's laboratory established against what Bosch and BASF solved with one named engineering problem, and two questions that would have to be answered about an unfamiliar laboratory result.",
      "pagePlacement": {
        "student": "student-karlsruhe-08",
        "teacher": "teacher-guide-05",
        "answer": "answer-key-06",
        "accessible": "accessible-karlsruhe-14"
      },
      "editions": ["student", "teacher", "answer", "accessible"],
      "keyed": true
    }
  ],
  "vocabulary": [
    "catalyst",
    "compromise",
    "equilibrium",
    "recycle",
    "scale up",
    "yield"
  ],
  "caseSources": [
    {
      "id": "archive-bench",
      "displayLabel": "The Archive's scenes at the bench and in the office",
      "creator": "Hunger, Harvest, & History Campaign 1 Level 4",
      "period": "scene set in 1909",
      "sourceType": "reconstruction",
      "sourceOrigin": "game reconstruction of a historical setting",
      "evidentiaryStatus": "reconstructed",
      "limitationClass": "reconstruction",
      "contribution": "A watchable model of the problem: a sound vessel whose outflow is almost all unreacted gas, a reaction that balances instead of failing, a chemist caught between a yield he cannot reach and a speed he cannot use, trays of metals set in the path of the gas, and a notebook margin where the answer turns out to be to stop throwing the leftover gas away.",
      "limitation": "No person in it is a real person and no notebook in it is a real notebook. Its dialogue was written for the game and is not surviving testimony. It fixes no date, no pressure and no temperature, its summaries describe the operating temperature as merely warm, and one of its field-note summaries contains a transcription error in the word for modelling. Its closing archive states a figure about the modern world that the scene itself cannot establish.",
      "gameCorrespondence": "C1 L4 sources examine_apparatus, measure_readings, run_analysis, haber, review_notebooks and query_archive.",
      "fallbackCorrespondence": "Dossier card A on Student page 2 and Accessible page 2."
    },
    {
      "id": "haber-patent",
      "displayLabel": "The ammonia patent of Haber and Le Rossignol, filed 1909",
      "creator": "Fritz Haber and Robert Le Rossignol, both of Karlsruhe; assigned to Badische Anilin & Soda Fabrik, Ludwigshafen-on-the-Rhine",
      "period": "filed 13 August 1909; granted 31 October 1916",
      "sourceType": "patent specification",
      "sourceOrigin": "real historical primary source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "A real document from the year of the demonstration, naming two inventors rather than one. It states that the process must be carried out continuously under pressure, that it can be operated at a pressure of 150 atmospheres, that higher pressure increases the ammonia concentration, that the catalyst is worked between 500 and 1000 degrees Celsius, and that gases from which the ammonia has been removed are passed over the catalyst again.",
      "limitation": "A patent records what its inventors claimed and wished to protect. It is not a measurement of how a plant performed, it does not say what happened on any particular day, and it describes nothing of the steel, the compressors or the catalyst that industrial production would later require.",
      "gameCorrespondence": "None. The game presents no real historical document.",
      "fallbackCorrespondence": "Dossier card B on Student page 2 and Accessible page 2.",
      "rights": "United States Patent 1,202,995. Published patent specifications are public records; the packet paraphrases and does not reproduce the specification."
    },
    {
      "id": "travis-2015",
      "displayLabel": "Travis on the laboratory, the catalyst search and the converter",
      "creator": "Anthony S. Travis, Sidney M. Edelstein Centre for the History and Philosophy of Science, Technology and Medicine, the Hebrew University of Jerusalem; the Seventh Wheeler Lecture, Royal Society of Chemistry, 22 October 2014, published as RSC Historical Group Occasional Papers No 7, April 2015",
      "period": "1900 to 1918",
      "sourceType": "scholarly historical account",
      "sourceOrigin": "real modern secondary and scholarly source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "The named people and the sequence. Haber calculated that about eight per cent ammonia could be reached at 600 degrees and 200 atmospheres. Robert Le Rossignol built the steel apparatus and the compressor and invented the valve that held the pressure, and designed the complete apparatus. Manganese, iron, chromium and nickel gave little; osmium and uranium worked, and about 100 grams of osmium, probably most of the world supply, was bought. Alwin Mittasch screened catalysts until promoted iron proved ideal in 1910. Bosch and Franz Lappe found that hydrogen was diffusing into the steel and embrittling it, and answered it in February 1911 with a double-walled converter vented through small holes. Production at Oppau began on 9 September 1913 at about twenty tonnes a day, soon about thirty.",
      "limitation": "A historian's reconstruction from records, not the records themselves. On the date of the decisive demonstration this account is explicitly cautious, giving 1 July 1909 as one version of events, and it does not settle the question against the other published date.",
      "gameCorrespondence": "The osmium and uranium the reconstructed Haber names, and his not yet knowing why iron failed.",
      "fallbackCorrespondence": "Dossier card C on Student page 2 and Accessible page 3, and the technology sequence in Task 5."
    },
    {
      "id": "appl-1997",
      "displayLabel": "Appl on the process, the equilibrium and the plant",
      "creator": "Max Appl, for the 50th Anniversary of the IFA Technical Conference, Sevilla, 25 to 26 September 1997, International Fertilizer Industry Association",
      "period": "1900 to 1997",
      "sourceType": "technical and historical review",
      "sourceOrigin": "real modern institutional and technical source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "The process as an industry states it. The reaction reduces the volume of gas and gives off heat, so the ammonia at the balance is higher at high pressure and at low temperature. The amount formed in a single pass is far too small to be worth producing, which is why Haber recycled the unconverted gas. Early in 1909 finely divided osmium gave about eight per cent ammonia at 175 bar and 600 degrees. Mittasch tested more than 2,500 formulas in 6,500 runs by 1910. Test reactors ruptured after only eighty hours. Modern plants run an iron catalyst at 400 to 500 degrees, above 100 bar, and 87 per cent of ammonia production goes to fertilizer.",
      "limitation": "A technical conference review written for industry, summarising rather than reproducing the laboratory record. It dates the successful BASF demonstration to April 1909, which is not the date the other scholarly account in this packet gives.",
      "gameCorrespondence": "The level's balance reading, its pressure model, its thermal model and its recycling note.",
      "fallbackCorrespondence": "Dossier card D on Student page 3 and Accessible page 3, and the process loop in Task 4."
    },
    {
      "id": "equilibrium-science",
      "displayLabel": "What the balance does, and what a catalyst does to it",
      "creator": "Chemistry LibreTexts, The Haber Process; corroborated by Appl 1997; melting point and atmospheric abundance from the Royal Society of Chemistry periodic table",
      "period": "established chemistry; no period",
      "sourceType": "established science",
      "sourceOrigin": "real modern institutional and scientific source",
      "evidentiaryStatus": "documented",
      "limitationClass": "observation",
      "contribution": "Nitrogen and hydrogen combine reversibly into ammonia, giving off about 92 kilojoules for every two moles of ammonia formed. Four molecules of gas go in and two come out, so raising the pressure moves the balance toward ammonia. Lowering the temperature also moves the balance toward ammonia, and slows the reaction down. A catalyst has no effect on where the balance sits; it makes the reaction reach that balance fast enough to be worth running. About fifteen parts in a hundred convert on a single pass, and with the leftover gas recycled the overall conversion is about ninety-eight parts in a hundred. Nitrogen is 78 per cent of air by volume, and lead melts at 327 degrees Celsius.",
      "limitation": "It says which way each change pushes. It does not say what a plant costs, what steel will hold, how much pressure is worth buying, or which compromise any company should choose. Those are engineering and economic questions and this source does not answer them.",
      "gameCorrespondence": "The level's balance reading, its four-parts-to-two-parts pressure query and its cold and hot thermal models.",
      "fallbackCorrespondence": "Dossier card E on Student page 3 and Accessible page 4, and the tradeoff panel in Task 3."
    },
    {
      "id": "erisman-2008",
      "displayLabel": "How many people this reaction feeds",
      "creator": "J. W. Erisman, M. A. Sutton, J. Galloway, Z. Klimont and W. Winiwarter, Nature Geoscience 1, 636 to 639, 2008",
      "period": "estimates for 2000 and 2008",
      "sourceType": "peer-reviewed estimate",
      "sourceOrigin": "real modern scientific source",
      "evidentiaryStatus": "estimated",
      "limitationClass": "estimate",
      "contribution": "An estimate that 44 per cent of the world's population in 2000, and 48 per cent in 2008, depended on food grown with synthetic nitrogen fertilizer. Independent estimates by other researchers cluster near one half.",
      "limitation": "An estimate, not a count. Nobody has weighed the food any person ate against the fertilizer that grew it. The researchers say plainly that separating the effect of fertilizer from every other reason harvests grew is difficult, and different methods give different figures around one half.",
      "gameCorrespondence": "The level's optional archive claim about the nitrogen in a living human body, which the game itself cannot establish.",
      "fallbackCorrespondence": "Dossier card F on Student page 3 and Accessible page 4.",
      "rights": "Nature Geoscience 1, 636-639 (2008). doi:10.1038/ngeo325. Cited, not reproduced."
    },
    {
      "id": "process-figure",
      "displayLabel": "The process loop",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching model and depicts no particular plant",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "limitationClass": "model",
      "contribution": "It puts the stages in the order the sources give them and closes the loop, so that the reason for the recycle can be reasoned about rather than asserted. Every arrow on it is a movement of gas that a source describes.",
      "limitation": "It is a drawing made to explain an order, not a plant drawing. Nothing on it is to scale. It shows no vessel sizes, no pipe diameters, no heat exchange duties and no costs, and it is not evidence that any particular plant was built this way.",
      "gameCorrespondence": "None. The level presents the stages as separate discoveries rather than as a loop.",
      "fallbackCorrespondence": "Task 4 figure on Student page 5 and Accessible page 8."
    },
    {
      "id": "tradeoff-panel",
      "displayLabel": "The tradeoff panel and the temperature ruler",
      "creator": "Curriculum-original figure authored for this case",
      "period": "no period; the figure is a teaching model",
      "sourceType": "teaching model",
      "sourceOrigin": "curriculum-original schematic",
      "evidentiaryStatus": "modeled",
      "limitationClass": "model",
      "contribution": "It shows the direction each change pushes, and it places the operating temperature on a ruler against fixed points a reader already knows, so that the word compromise cannot be read as ordinary warmth.",
      "limitation": "It carries directions and anchored values only. It draws no curve and plots no measured yield, because no source in this packet supplies the values a curve would need. It cannot be used to read off how much ammonia any temperature or pressure would give.",
      "gameCorrespondence": "The level's pressure model and thermal model, which give directions without values.",
      "fallbackCorrespondence": "Task 3 figure on Student page 4 and Accessible page 6."
    }
  ],
  "temperatureQualification": {
    "rule": "The operating temperature is a compromise between the share of ammonia the balance allows and the speed at which the reaction reaches it. It is never presented as ordinary warmth.",
    "requiredFraming": "compromise",
    "prohibitedFramings": [
      "gentle warmth",
      "merely warm",
      "mildly warm",
      "lukewarm",
      "room temperature",
      "warm but not hot",
      "moderate warmth"
    ],
    "anchorValues": {
      "leadMelts": { "celsius": 327, "qualifier": "about", "source": "Royal Society of Chemistry", "label": "lead melts" },
      "modernPlant": { "celsius": [400, 500], "qualifier": "about", "source": "Appl 1997", "label": "modern plants run here" },
      "haberBench": { "celsius": 600, "qualifier": "about", "source": "Travis 2015; Appl 1997", "label": "Haber's laboratory result" },
      "patentRange": { "celsius": [500, 1000], "qualifier": "stated", "source": "US Patent 1,202,995", "label": "the range the patent claims for the catalyst" }
    },
    "requiredQualification": "Every role must state that the operating temperature is a compromise, and both learner editions must carry at least one anchored value showing that the compromise is hundreds of degrees Celsius and hotter than the melting point of lead."
  },
  "catalystBoundary": {
    "correct": "A catalyst gives the reaction a faster route by lowering the energy barrier, so the balance is reached quickly enough to be worth running. It is not used up in the overall reaction.",
    "prohibitedClaims": [
      "the catalyst shifts the equilibrium toward ammonia",
      "the catalyst moves the balance",
      "the catalyst increases the yield at equilibrium",
      "the catalyst changes the position of the equilibrium",
      "the catalyst makes more ammonia possible at the balance"
    ],
    "requiredQualification": "No role may state or accept that the catalyst changes where the balance sits. Wording about the catalyst producing more ammonia is acceptable only where it plainly refers to production in a practical operating time."
  },
  "attributionBoundary": {
    "haber": "Directed the laboratory work that showed the synthesis could be made to run, calculated the conditions it needed, and introduced the principle of recycling the unconverted gas. Named first on the patent.",
    "leRossignol": "Built the steel apparatus and the compression that made the demonstration physically possible, and invented the valve that held the pressure. Named with Haber as co-inventor on the patent, and usually left out of the process's name.",
    "mittasch": "Ran the BASF catalyst search that replaced osmium, which was too rare to buy, with promoted iron that could be made in quantity.",
    "bosch": "Led the BASF engineering that turned a bench result into a plant: steel that would not be destroyed by hydrogen, compressors of a kind not previously built, and the works at Oppau.",
    "prohibitedClaims": [
      "Haber alone created the industrial process",
      "Haber invented the Haber process and factories simply copied it",
      "Bosch merely copied Haber's laboratory apparatus",
      "the factory was a scaled-up copy of the bench",
      "Haber's laboratory work alone made ammonia available to farmers"
    ],
    "requiredQualification": "Every role must keep laboratory demonstration and industrial engineering distinct, must credit both, and must not present either as the whole of the achievement."
  },
  "demonstrationDateBoundary": {
    "certifiedYear": "1909",
    "status": "debated / uncertain",
    "positions": [
      { "date": "1 July 1909", "source": "Travis 2015", "qualifier": "given explicitly as one version of events, with liquefied ammonia appearing the following day after a seal failed" },
      { "date": "April 1909", "source": "Appl 1997", "qualifier": "given without qualification" }
    ],
    "rule": "The year 1909 is printed as documented. No exact date is printed as settled in any role. The disagreement is the evidence for Task 6 row three and Task 7 Claim 5.",
    "settlementEvidence": "Only a dated contemporary record — a laboratory notebook entry, a BASF internal report, correspondence, or a travel or expense record placing the BASF party at Karlsruhe — could settle it."
  },
  "recycleBoundary": {
    "singlePass": { "value": 15, "units": "parts converted per hundred fed, approximate", "status": "reported", "source": "Chemistry LibreTexts, corroborated qualitatively by Appl 1997" },
    "overallWithRecycle": { "value": 98, "units": "parts converted per hundred fed, approximate", "status": "reported", "source": "Chemistry LibreTexts" },
    "prohibitedClaims": [
      "one pass converts all the gas",
      "recycling makes a single pass complete",
      "the recycle increases the share converted in one pass"
    ],
    "requiredQualification": "Recycling changes what the whole plant achieves over many passes. It does not change what one pass does."
  },
  "claimJudgments": {
    "markScheme": {
      "Y": "the evidence in this packet supports it",
      "N": "the evidence in this packet goes against it",
      "?": "this packet cannot decide it"
    },
    "claims": [
      { "number": "1", "layer": "mechanism", "mark": "Y" },
      { "number": "2", "layer": "mechanism", "mark": "N" },
      { "number": "3", "layer": "mechanism", "mark": "N" },
      { "number": "4", "layer": "attribution", "mark": "N" },
      { "number": "5", "layer": "record", "mark": "?" }
    ]
  },
  "chronology": [
    { "year": "1908", "lane": "laboratory", "entry": "BASF and Haber agree to pursue the direct combination of nitrogen and hydrogen.", "source": "travis-2015" },
    { "year": "1909", "lane": "laboratory", "entry": "The Karlsruhe demonstration, with Le Rossignol's apparatus and an osmium catalyst: about eight per cent ammonia at roughly 600 degrees and about 175 to 200 atmospheres. Published accounts differ on the exact date.", "source": "travis-2015; appl-1997" },
    { "year": "1909", "lane": "laboratory", "entry": "Haber and Le Rossignol file the ammonia patent on 13 August, assigned to BASF.", "source": "haber-patent" },
    { "year": "1910", "lane": "catalyst", "entry": "Mittasch's screening at BASF finds promoted iron, after thousands of tests.", "source": "travis-2015; appl-1997" },
    { "year": "1911", "lane": "plant", "entry": "Bosch and Lappe answer the hydrogen embrittlement of the steel with a double-walled converter, in February.", "source": "travis-2015" },
    { "year": "1913", "lane": "plant", "entry": "Oppau begins production on 9 September, at about twenty tonnes a day, soon about thirty.", "source": "travis-2015; appl-1997" },
    { "year": "1916", "lane": "laboratory", "entry": "The Haber and Le Rossignol patent is granted on 31 October.", "source": "haber-patent" }
  ],
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
      "NGSS MS-PS1-2",
      "NGSS MS-ETS1-1"
    ],
    "ngss": "Both NGSS references are contextual only. Tasks 3 and 4 do reason about a chemical reaction and about criteria and constraints on a designed process, but the assessed product is a historical-technological explanation with source qualification, not a science or engineering practice, and no laboratory investigation or design test is performed. No NGSS alignment is claimed as directly assessed."
  }
};
