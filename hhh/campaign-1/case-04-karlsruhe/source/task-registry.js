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
      "contribution": "The named people and the sequence, each at the strength this source states. Haber opted for an apparatus of steel and calculated an estimated eight per cent equilibrium yield at 600 degrees and 200 atmospheres; the high-pressure work was then assigned to Robert Le Rossignol, who carried it out and introduced improvements throughout. Le Rossignol designed the complete ammonia apparatus - the arrangement through which the compressed gases passed to the steel converter, were cooled, and had the ammonia liquefied and separated from the unreacted gas - and his own first major contribution was the valve that withstood the pressure and controlled the flow of hot gases. The custom-made steel apparatus used a novel 200-atmosphere compressor newly acquired by Haber, and the help of the laboratory technician Friedrich Kirchenbauer was critical. Manganese, iron, chromium and nickel gave little; osmium and uranium carbide worked, and about 100 grams of osmium, probably most of the world supply, was bought. Alwin Mittasch screened catalysts until promoted iron proved ideal in 1910. Bosch used his metallographic training to establish that hydrogen was diffusing into the steel and embrittling it by decarbonization, and, aided by chief engineer Franz Lappe, answered it in February 1911 with a double-walled converter vented through small holes. Production at Oppau began on 9 September 1913 at about twenty tonnes a day, soon about thirty.",
      "limitation": "A historian's reconstruction from records, not the records themselves. On the date of the decisive demonstration this account is explicitly cautious, giving 1 July 1909 as one version of events, and it does not settle the question against the other published date.",
      "supportingReferences": [
        {
          "label": "BASF corporate chronology, entry for 1913",
          "role": "corroboration of the attribution split, from the industrial party itself",
          "states": "that a BASF team headed by Carl Bosch worked from 1908 on realising ammonia synthesis at industrial scale, starting from the laboratory procedures of Haber, and describes it as cooperation between academia and industry",
          "limitation": "a company's account of its own history, written for the public; it credits its own team and is not an independent measure",
          "printedIn": "Teacher source ledger only; it supplies no learner-facing evidence and is therefore a supporting reference under this source rather than a canonical source of its own"
        }
      ],
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
      "contribution": "The process as an industry states it. The reaction reduces the volume of gas and gives off heat, so the ammonia at the balance is higher at high pressure and at low temperature. The amount formed in a single pass is far too small to be worth producing, which is why Haber recycled the unconverted gas. Early in 1909 finely divided osmium was found to yield about 8 volume per cent ammonia at 175 bar and 600 degrees - an obtained result, and stated in bar, which is not the same statement as the 200-atmosphere figure Haber had calculated beforehand. Mittasch tested more than 2,500 formulas in 6,500 runs by 1910. Test reactors ruptured after only eighty hours. Modern plants run an iron catalyst at 400 to 500 degrees, above 100 bar, and 87 per cent of ammonia production goes to fertilizer.",
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
      "contribution": "Nitrogen and hydrogen combine reversibly into ammonia, giving off about 92 kilojoules for every two moles of ammonia formed. Four molecules of gas go in and two come out, so raising the pressure moves the balance toward ammonia. Lowering the temperature also moves the balance toward ammonia, and slows the reaction down. A catalyst has no effect on where the balance sits; it makes the reaction reach that balance fast enough to be worth running. This source also reports worked operating figures for a typical plant - about fifteen parts in a hundred converting on a single pass, and about ninety-eight parts in a hundred overall once the leftover gas is recycled - and states in the same breath that the pressure varies from one manufacturing plant to another and that the single-pass figure also varies from plant to plant. They are reported example figures, not constants of the process. Nitrogen is 78 per cent of air by volume, and lead melts at 327 degrees Celsius.",
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
    "haber": "Directed the laboratory programme: opted for an apparatus of steel, calculated the conditions the reaction would need, acquired the 200-atmosphere compressor the work depended on, and introduced the principle of recycling the unconverted gas. Named first on the patent.",
    "leRossignol": "Was assigned the high-pressure experimental work and carried it out, improving the process throughout. Designed the complete ammonia apparatus - the arrangement through which the compressed gases passed to the converter, were cooled, and had the ammonia liquefied and separated - and invented the valve that withstood the pressure and controlled the flow of hot gases. Named with Haber as co-inventor on the patent, and usually left out of the process's name.",
    "kirchenbauer": "Laboratory technician whose help the source calls critical to the enterprise. Named in the Teacher Guide only.",
    "mittasch": "Ran the BASF catalyst search that replaced osmium, which was too rare to buy, with promoted iron that could be made in quantity.",
    "bosch": "Led the BASF engineering that turned a bench result into a plant. Used his metallographic training to establish why the high-pressure steel was failing, and led the works at Oppau.",
    "lappe": "Chief engineer who aided Bosch on the pilot-plant design and on the double-walled converter of February 1911.",
    "sourceStrengthRules": [
      "The 200-atmosphere compressor was newly acquired by Haber. It may not be described as built, made or invented by Le Rossignol.",
      "The choice of a steel apparatus is Haber's. Le Rossignol designed the apparatus arrangement and invented the valve.",
      "Le Rossignol designed the complete ammonia apparatus; he is not described as having built the compressor.",
      "The diagnosis of hydrogen embrittlement is Bosch's. Lappe aided the solution and is not credited with the diagnosis.",
      "No single person may be credited with both diagnosing and solving the high-pressure materials problem alone."
    ],
    "prohibitedClaims": [
      "Haber alone created the industrial process",
      "Haber invented the Haber process and factories simply copied it",
      "Bosch merely copied Haber's laboratory apparatus",
      "the factory was a scaled-up copy of the bench",
      "Haber's laboratory work alone made ammonia available to farmers",
      "Le Rossignol built the compressor",
      "Le Rossignol built the complete apparatus"
    ],
    "requiredQualification": "Every role must keep laboratory demonstration and industrial engineering distinct, must credit both, must not present either as the whole of the achievement, and must not credit any contributor beyond the strength the cited source supports."
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
    "singlePass": { "value": 15, "units": "parts converted per hundred fed", "qualifier": "about", "status": "reported example", "source": "Chemistry LibreTexts, The Haber Process", "variability": "the source states that this figure also varies from plant to plant" },
    "overallWithRecycle": { "value": 98, "units": "parts converted per hundred fed", "qualifier": "about", "status": "reported example", "source": "Chemistry LibreTexts, The Haber Process", "variability": "quoted for the same worked plant; operating pressure is stated to vary from one manufacturing plant to another" },
    "printedQualificationRequired": true,
    "printedQualificationRule": "Wherever either figure is printed in a learner edition it must be marked as a reported example for a typical plant that varies from plant to plant, never as a constant of the process. The conceptual point - that one pass leaves most of the feed unreacted, and that recycling raises what the whole plant converts - is what is assessed.",
    "prohibitedClaims": [
      "one pass converts all the gas",
      "recycling makes a single pass complete",
      "the recycle increases the share converted in one pass",
      "the Haber process always converts 15% per pass",
      "every plant converts 98% after recycling"
    ],
    "requiredQualification": "Recycling changes what the whole plant achieves over many passes. It does not change what one pass does. The two figures are reported examples, not universal constants."
  },
  "semanticInvariants": {
    "scanScope": {
      "roles": ["student", "teacher", "answer", "accessible"],
      "unit": "sentence",
      "rule": "Every sentence in every role is scanned unless the node carries a registered exemption id. Exemption is granted only by the closed contract below: markup cannot self-authorize.",
      "exemptionAttribute": "data-semantic-exemption"
    },
    "exemptions": [
      {
        "id": "claim-under-test-learner",
        "roles": ["student", "accessible"],
        "selector": ".account-item[data-semantic-exemption=\"claim-under-test-learner\"]",
        "expectedCount": 10,
        "purpose": "Task 7 competing claims are propositions offered to the learner for judgment, not assertions of the packet.",
        "allowedConcepts": ["catalyst", "temperature", "attribution", "recycle"]
      },
      {
        "id": "claim-under-test-key",
        "roles": ["answer"],
        "selector": ".claims-key tbody tr[data-semantic-exemption=\"claim-under-test-key\"]",
        "expectedCount": 5,
        "purpose": "The Answer Key restates each competing claim beside the mark that decides it.",
        "allowedConcepts": ["catalyst", "temperature", "attribution", "recycle"]
      },
      {
        "id": "teacher-misconception",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"teacher-misconception\"]",
        "expectedCount": 10,
        "purpose": "The Teacher misconceptions table and the prose warnings name an error in order to reject it.",
        "allowedConcepts": ["catalyst", "temperature", "attribution", "recycle"]
      },
      {
        "id": "teacher-rubric-floor",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"teacher-rubric-floor\"]",
        "expectedCount": 4,
        "purpose": "Rubric descriptors that quote the disqualifying answer in order to place a floor under it.",
        "allowedConcepts": ["catalyst", "temperature", "attribution", "recycle"]
      },
      {
        "id": "answer-key-floor",
        "roles": ["answer"],
        "selector": "[data-semantic-exemption=\"answer-key-floor\"]",
        "expectedCount": 5,
        "purpose": "Answer Key floors that quote the answer they refuse to accept at any level.",
        "allowedConcepts": ["catalyst", "temperature", "attribution", "recycle"]
      },
      {
        "id": "game-wording-quoted",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"game-wording-quoted\"]",
        "expectedCount": 3,
        "purpose": "Places where the runtime level's own faulty wording is reported so the teacher can correct it.",
        "allowedConcepts": ["temperature"]
      },
      {
        "id": "learner-refutation-prompt",
        "roles": ["student", "accessible"],
        "selector": "[data-semantic-exemption=\"learner-refutation-prompt\"]",
        "expectedCount": 2,
        "purpose": "Task 3 Part D quotes a wrong belief and asks the learner to refute it with a value.",
        "allowedConcepts": ["temperature"]
      },
      {
        "id": "scoring-quoted-wording",
        "roles": ["answer"],
        "selector": "[data-semantic-exemption=\"scoring-quoted-wording\"]",
        "expectedCount": 1,
        "purpose": "Scoring guidance quoting a learner phrasing in order to bound when it is acceptable.",
        "allowedConcepts": ["catalyst"]
      },
      {
        "id": "vocabulary-term-list",
        "roles": ["teacher"],
        "selector": "[data-semantic-exemption=\"vocabulary-term-list\"]",
        "expectedCount": 1,
        "purpose": "An enumeration of the case vocabulary is a term list, not a claim about any term in it.",
        "allowedConcepts": ["catalyst", "temperature", "attribution", "recycle"]
      }
    ],
    "structuralExemptSelectors": [
      { "selector": ".word-bank", "why": "a word bank is a list of terms offered for placement; it asserts nothing about any of them" }
    ],
    "catalyst": {
      "role": "rate and pathway",
      "equilibriumPositionEffect": "NONE",
      "protectedProposition": "A catalyst may change the rate, the pathway, or the time taken to approach the final state. It may not change the amount, proportion, concentration, composition or yield established by the equilibrium state under the same conditions.",
      "subjectTerms": [
        "catalyst", "catalysts", "catalytic", "catalytic surface", "catalyst material",
        "iron catalyst", "promoted iron", "osmium", "uranium"
      ],
      "namesInEvidence": ["osmium", "uranium", "promoted iron", "iron catalyst"],
      "namesInEvidenceRule": "Every catalyst this package actually names in learner evidence must resolve to the catalyst subject concept. Osmium was silently dropped from the subject list during an earlier hardening pass and three misconceptions escaped; a guard now reconciles this list against subjectTerms so the same regression cannot recur.",
      "productTerms": ["ammonia", "product", "mixture", "yield"],
      "chemicalAliases": {
        "ammonia": ["NH3", "NH\u2083", "NH<sub>3</sub>", "NH 3"],
        "rule": "The normaliser folds every rendering of the ammonia formula - ASCII, Unicode subscript, and the HTML markup as the browser extracts it - onto the ammonia product concept, so a misconception cannot hide behind notation."
      },
      "finalStateStrongTerms": [
        "equilibrium", "balance", "at rest", "come to rest", "settle", "settle down",
        "settled", "settling", "resting", "stop changing", "no longer changing",
        "steady", "end state", "final state", "equilibrium mixture",
        "once the reaction", "after the reaction", "when the reaction",
        "once it stops", "when it stops", "once everything"
      ],
      "finalStateContextualTerms": [
        "final", "finally", "finished", "resulting", "remaining", "remains",
        "left", "ends", "ends up", "end up", "ended", "present", "outcome",
        "in the end", "afterwards", "result", "results"
      ],
      "mixtureContextTerms": [
        "mixture", "composition", "gas", "gases", "vessel", "reactor", "share",
        "proportion", "fraction", "amount", "ammonia", "product", "yield", "reaction"
      ],
      "finalStateRule": "A strong term denotes the settled state on its own. A contextual term - finished, resulting, left, present - counts only when the sentence also names a mixture or reaction context, so ordinary uses such as finishing a building programme cannot satisfy it.",
      "increaseRelationTerms": [
        "increase", "increases", "increased", "increasing", "raise", "raises", "raised", "raising",
        "boost", "boosts", "boosted", "boosting", "more", "extra", "richer", "rich",
        "larger", "bigger", "greater", "higher", "improve", "improves", "improved",
        "change", "changes", "changed", "changing", "shift", "shifts", "shifted", "shifting",
        "move", "moves", "moved", "moving", "tip", "tips", "tipped", "favour", "favours",
        "alter", "alters", "altering", "push", "pushes", "pushing",
        "enrich", "enriches", "enriching", "drive", "drives", "driving",
        "steer", "steers", "nudge", "nudges", "lift", "lifts", "lifting",
        "produce more", "make more", "give more", "leaves more", "leave more", "adds to"
      ],
      "resultReportMarkers": ["bar", "atm", "atmospheres", "by volume", "vol", "degrees", "grams", "per cent"],
      "functionVerbTerms": [
        "helps", "help", "lets", "let", "allows", "allow", "enables", "enable",
        "makes", "make", "produces", "produce", "gives", "give", "works by", "does the work"
      ],
      "permittedRateTerms": [
        "faster", "fast", "quick", "quickly", "quicker", "speed", "speeds", "rate", "sooner",
        "time", "route", "pathway", "path", "barrier", "activation", "approach", "reach",
        "reaches", "reached", "practical", "working time", "in practice"
      ],
      "negationTerms": [
        "no effect on", "does not change", "do not change", "without changing",
        "does not move", "without moving", "does not shift", "without shifting",
        "not change where", "never changes", "cannot change", "not the position",
        "without altering", "does not alter", "not by moving", "rather than moving",
        "without raising", "does not raise", "not balance", "not the balance",
        "rate, not", "not where the balance", "never moves the balance", "not how much",
        "not the final", "not the amount", "not the share", "not the composition",
        "does not decide", "not the yield", "did not change", "did not move",
        "did not alter", "does not affect", "did not affect", "no effect"
      ],
      "negationPattern": "\\b(?:not|never|without)\\b[^.]{0,40}\\b(?:chang|mov|shift|alter|rais|increas|affect|effect|tip|push|boost|enrich|improv)",
      "policy": "FAIL_CLOSED",
      "policyRule": "A non-exempt sentence naming a canonical catalyst subject together with a product concept must resolve to an approved catalyst function, a registered descriptive claim, or a registered evaluative exemption. Anything else fails. Correctness therefore does not depend on recognising the verb that carries the wrong relationship, so no future synonym for 'increase' can evade it.",
      "approvedFunctions": [
        {
          "id": "rate",
          "why": "the catalyst changes how fast the reaction gets there",
          "terms": [
            "speed", "speeds", "speeded", "sped", "speeding", "faster", "fast enough",
            "quick", "quickly", "quicker", "rate", "rates", "reaction time", "sooner",
            "in hours", "practical time", "working time", "in practice", "how fast",
            "how long", "how soon", "time the gases", "waiting time", "shortens the wait"
          ]
        },
        {
          "id": "pathway",
          "why": "the catalyst offers another or lower-energy route",
          "terms": [
            "pathway", "path", "route", "activation", "energy barrier", "barrier",
            "lower-energy", "lower energy", "energy hill", "easier route", "easier path"
          ]
        },
        {
          "id": "no-shift",
          "why": "the catalyst explicitly does not move the equilibrium position or the settled amount",
          "requires": "bound-invariant",
          "requiresRule": "A no-shift assertion must identify WHAT stays invariant. A condition qualifier names what was held constant, not what stayed unchanged in the product, so it cannot satisfy no-shift on its own. The patterns below bind an invariance word to an invariant object within a bounded distance.",
          "insufficientAloneTerms": [
            "same conditions", "same pressure and temperature", "identical conditions",
            "everything else held constant", "conditions are unchanged", "held constant",
            "same operating conditions", "all else equal"
          ],
          "boundPatterns": [
            "(?:equilibrium|settled|final|balance)\\s+(?:\\w+\\s+){0,2}(?:position|composition|share|amount|fraction|mixture|endpoint|point)\\s+(?:\\w+\\s+){0,4}(?:unchanged|untouched|exactly as it was|as it was|stays the same|stay the same|remains the same|remain the same|the same)",
            "(?:same|unchanged|identical|untouched)\\s+(?:\\w+\\s+){0,2}(?:equilibrium|composition|share|amount|fraction|endpoint|position|settled)",
            "(?:does not|do not|did not|cannot|can not|never|without)\\s+(?:\\w+\\s+){0,3}(?:chang\\w*|mov\\w*|shift\\w*|alter\\w*|affect\\w*|rais\\w*|increas\\w*)\\s+(?:\\w+\\s+){0,4}(?:equilibrium|balance|composition|share|amount|position|settled|endpoint|final)",
            "(?:no effect on|no say in)\\s+(?:\\w+\\s+){0,4}(?:equilibrium|balance|composition|share|amount|position|settled|where)",
            "with or without\\s+(?:\\w+\\s+){0,6}(?:same|unchanged)",
            "(?:equilibrium|settled|balance)\\s+(?:\\w+\\s+){0,3}(?:stays|stay|stayed|remains|remain|remained)\\s+(?:exactly\\s+)?(?:the same|unchanged|as it was|put)",
            "(?:equilibrium|balance|composition|share|amount|settled|endpoint)[^.]{0,90}?(?:does not|do not|did not|cannot|can not|never)\\s+(?:\\w+\\s+){0,3}(?:chang\\w*|mov\\w*|shift\\w*|alter\\w*|affect\\w*)"
          ]
        }
      ],
      "approvedFunctionRule": "Bare approval words such as helps, lets, allows or works are deliberately absent. 'The catalyst helps make ammonia' underspecifies the function and fails.",
      "registeredDescriptiveClaimsNote": "Fingerprints are computed over the PROPOSITION as the catalyst parser now bounds it. When internal punctuation stopped severing propositions, six of these fingerprints changed mechanically and four further propositions surfaced that colons and semicolons had previously hidden from the gate. Each is a non-causal historical, certification or pedagogical statement; none asserts anything about what a catalyst does to the amount of ammonia. One earlier registration, the Teacher central-resolution summary, now resolves as an approved rate function and has been removed rather than kept as a stale entry.",
      "registeredDescriptiveClaims": [
        {
          "id": "patent-recycle-learner",
          "roles": ["student", "accessible"],
          "expectedCount": 2,
          "fingerprint": "4800faa689c3283f",
          "purpose": "The patent's own recycle statement: it describes where the gas is routed, not what the catalyst does to the amount of ammonia.",
          "sourceCorrespondence": "haber-patent"
        },
        {
          "id": "patent-certification-teacher",
          "roles": ["teacher"],
          "expectedCount": 1,
          "fingerprint": "ea72ea3613e5bcf7",
          "purpose": "The Teacher source ledger row listing what the 1909 patent certifies. A semicolon-separated certification list in which catalyst and ammonia co-occur incidentally.",
          "sourceCorrespondence": "haber-patent"
        },
        {
          "id": "patent-recycle-answer",
          "roles": ["answer"],
          "expectedCount": 1,
          "fingerprint": "616ec83cb7e69730",
          "purpose": "The Answer Key exemplar for Task 4 stage 6, citing the patent's recycle statement.",
          "sourceCorrespondence": "haber-patent"
        },
        {
          "id": "osmium-obtained-student",
          "roles": ["student"],
          "expectedCount": 1,
          "fingerprint": "f44e25881c65fc2f",
          "purpose": "Appl's historical result: osmium was found to give about 8 volume per cent ammonia at 175 bar and 600 degrees. A dated measurement, not a claim about equilibrium.",
          "sourceCorrespondence": "appl-1997"
        },
        {
          "id": "osmium-obtained-accessible",
          "roles": ["accessible"],
          "expectedCount": 1,
          "fingerprint": "20ebe9bad89e1cee",
          "purpose": "The same Appl historical result in the Accessible dossier.",
          "sourceCorrespondence": "appl-1997"
        },
        {
          "id": "appl-certification-teacher",
          "roles": ["teacher"],
          "expectedCount": 1,
          "fingerprint": "fbf398d226b0a86c",
          "purpose": "The Teacher source ledger row listing what Appl certifies, including the osmium result. Surfaced by the parser change; a certification list, not a causal claim.",
          "sourceCorrespondence": "appl-1997"
        },
        {
          "id": "sequence-demonstration-student",
          "roles": ["student"],
          "expectedCount": 2,
          "fingerprint": "585033cd40e6f18a",
          "purpose": "The Student technology-sequence cell for the 1909 demonstration, naming the osmium catalyst and the ammonia obtained. Surfaced by the parser change, which stopped a colon from severing it. Counted twice because the row and the cell are both leaf text blocks.",
          "sourceCorrespondence": "appl-1997"
        },
        {
          "id": "sequence-demonstration-accessible",
          "roles": ["accessible"],
          "expectedCount": 2,
          "fingerprint": "a0f8e9d588f2bc41",
          "purpose": "The Accessible technology-sequence entry for the same demonstration.",
          "sourceCorrespondence": "appl-1997"
        },
        {
          "id": "synthesis-conditions-answer",
          "roles": ["answer"],
          "expectedCount": 1,
          "fingerprint": "f96ec63a94b0ae50",
          "purpose": "The Answer Key statement that under pressure, with a catalyst and with recycling, nitrogen and hydrogen will give ammonia. States that the synthesis runs, not that the catalyst raises the settled amount.",
          "sourceCorrespondence": "haber-patent"
        },
        {
          "id": "success-criteria-teacher",
          "roles": ["teacher"],
          "expectedCount": 1,
          "fingerprint": "5c22502e42c8cfa0",
          "purpose": "The Teacher success criteria, a semicolon list of what learners should be able to say. Pedagogical description; the catalyst clause states that learners must refuse what a catalyst does not do.",
          "sourceCorrespondence": "equilibrium-science"
        }
      ],
      "registeredDescriptiveClaimRule": "Identity is a fingerprint of the normalised sentence, not an HTML attribute, so classroom markup carries no authority to exempt itself and content.html stays byte-identical. Reconciled both ways: every registered fingerprint must resolve in its declared roles at its declared count, and every catalyst-and-product sentence in the package must be an approved function, a registered fingerprint, or a registered evaluative exemption.",
      "diagnosticOnlyRule": "The increase-relation and final-state families below are retained for diagnostics and for the more specific message they produce. The correctness gate no longer depends on them, so a missing synonym degrades the error text rather than opening a hole.",
      "rules": [
        "NEGATIVE RELATION: a sentence naming the catalyst, a product term, an increase relation and a final-state term asserts that the catalyst changes the settled amount. The word equilibrium is not required for the contradiction to count.",
        "POSITIVE BOUNDARY: a learner sentence that assigns a function to the catalyst must resolve into a permitted role - rate, pathway, time to approach - or state that it does not change the equilibrium position. A bare function claim is insufficient."
      ]
    },
    "temperature": {
      "industrialTemperatureCharacterization": "compromise",
      "ordinaryWarmthCharacterization": "prohibited",
      "numericAnchorIsEvidenceNotWaiver": true,
      "requiredDirectionsInLearnerEvidence": ["equilibriumDirection", "rateDirection"],
      "subjectTerms": [
        "operating temperature", "compromise temperature", "the temperature",
        "reactor runs", "reactor operates", "runs at", "operates at", "operating at",
        "plants run", "plant runs", "plant operates", "process runs", "it runs at", "reactor"
      ],
      "subjectValuePattern": "\\b\\d{2,4}\\s*(?:°\\s*c|degrees)",
      "warmthTerms": [
        "warm", "warmth", "warmly", "mild", "mildly", "mildness", "gentle", "gently",
        "lukewarm", "tepid", "comfortable", "comfortably", "comfort", "cosy", "cozy",
        "balmy", "temperate", "mellow", "pleasant", "room temperature", "body temperature",
        "not especially hot", "not very hot", "not that hot", "not too hot", "hardly hot",
        "barely hot", "a little hot", "slightly hot", "no hotter than", "no fiercer than",
        "moderate setting", "moderate warmth", "merely moderate", "just moderate",
        "nothing extreme", "not extreme"
      ],
      "negationTerms": [
        "not ordinary warmth", "does not mean warm", "do not mean warm", "not merely warm",
        "not mildly warm", "rather than warm", "not gently warm", "never warm",
        "cannot be read as ordinary warmth", "cannot be read as warm", "is not gentle",
        "is wrong", "are wrong", "incorrect"
      ],
      "rule": "A numeric temperature makes a sentence a temperature sentence. Warmth or mildness language about the operating condition fails even when a high numeric value is present in the same sentence: the value is evidence that the mild characterisation is wrong, never a waiver. Only an explicit denial of the warmth reading clears it."
    },
    "attribution": {
      "laboratoryWorkIsNotIndustrialScaleUp": true,
      "industrialProcessMayNotBeDescribedAsCompleteBeforeScaleUp": true,
      "laboratorySubjectTerms": ["haber", "le rossignol", "laboratory", "bench"],
      "industrialSubjectTerms": ["bosch", "basf", "factory", "factories", "plant", "works", "industry"],
      "completionTerms": [
        "already", "finished", "finish", "completed", "complete", "solved", "solve",
        "fully developed", "made ready", "ready", "production-ready", "factory-ready",
        "had everything needed", "nothing left", "worked out the industrial",
        "sorted out", "settled the engineering"
      ],
      "industrialNounTerms": [
        "industrial", "industry", "factory", "factories", "plant-scale", "plant scale",
        "production-scale", "production scale", "scale-up", "scale up", "at scale",
        "engineering", "production", "works", "plant"
      ],
      "diminutiveTerms": ["simply", "merely", "only", "just", "no more than", "nothing more than"],
      "reproductionTerms": [
        "copied", "copy", "copies", "copying", "reproduced", "reproduce", "reproducing",
        "built", "build", "building", "constructed", "construct", "constructing",
        "replicated", "replicate", "followed", "follow"
      ],
      "negationTerms": [
        "not yet", "was not", "were not", "had not", "did not", "does not", "nothing about",
        "not complete", "not finished", "not solved", "still had to", "had to solve",
        "had to invent", "could not", "never"
      ],
      "rules": [
        "A sentence naming a laboratory actor, a completion term and an industrial noun asserts that the industrial engineering was finished before the scale-up. Word order and adjacency are irrelevant.",
        "A sentence naming an industrial actor, a diminutive and a reproduction term reduces the scale-up to copying."
      ]
    },
    "recycle": {
      "figuresAreReportedExamples": true,
      "figures": ["15", "98"],
      "qualificationTerms": [
        "reported", "example", "typical", "varies from plant to plant", "varies from one",
        "for one worked plant", "not a constant", "not constants", "a worked figure", "worked plant"
      ],
      "universalQuantifierTerms": [
        "every", "any", "all ", "always", "invariably", "universal", "universally",
        "in all cases", "without exception", "never varies", "regardless of plant"
      ],
      "plantContextTerms": [
        "plant", "plants", "factory", "factories", "works", "process", "manufacturing",
        "haber-bosch", "haber bosch", "ammonia plant"
      ],
      "rules": [
        "A learner block printing either figure as a share of conversion must carry a qualification term.",
        "UNIVERSALITY: a sentence printing either figure together with a universal quantifier and a plant or process context asserts the figure is what every plant does. The quantifier and the plant word need not be adjacent."
      ]
    }
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
    { "year": "1909", "lane": "laboratory",
      "entry": "The Karlsruhe demonstration, with the apparatus Le Rossignol designed and an osmium catalyst. Published accounts differ on the exact date.",
      "source": "travis-2015; appl-1997",
      "unitConflationProhibited": true,
      "conflationNote": "The two sources report about eight per cent under different conditions, in different units, with different epistemic status. They are two sourced facts about one milestone and must never be merged into a single 175 to 200 atmospheres condition.",
      "sourcedConditions": [
        {
          "id": "haber-calculated",
          "epistemicStatus": "calculated",
          "verbFamily": ["calculated", "predicted", "expected", "should be reachable"],
          "prohibitedVerbFamily": ["obtained", "achieved", "produced", "gave", "measured"],
          "ammonia": "about eight per cent",
          "temperature": { "value": 600, "unit": "degrees Celsius" },
          "pressure": { "value": 200, "unit": "atmospheres" },
          "note": "a prediction made before the experiments",
          "source": "travis-2015"
        },
        {
          "id": "osmium-obtained",
          "epistemicStatus": "obtained",
          "verbFamily": ["obtained", "gave", "yielded", "achieved", "was obtained"],
          "prohibitedVerbFamily": ["calculated", "predicted", "expected"],
          "ammonia": "about eight per cent by volume",
          "temperature": { "value": 600, "unit": "degrees Celsius" },
          "pressure": { "value": 175, "unit": "bar" },
          "note": "a result obtained with a finely divided osmium catalyst",
          "source": "appl-1997"
        }
      ] },
    { "year": "1909", "lane": "laboratory", "entry": "Haber and Le Rossignol file the ammonia patent on 13 August, assigned to BASF.", "source": "haber-patent" },
    { "year": "1910", "lane": "catalyst", "entry": "Mittasch's screening at BASF finds promoted iron, after thousands of tests.", "source": "travis-2015; appl-1997" },
    { "year": "1911", "lane": "plant", "entry": "Bosch and Lappe answer the hydrogen embrittlement of the steel with a double-walled converter, in February.", "source": "travis-2015" },
    { "year": "1913", "lane": "plant", "entry": "Oppau begins production on 9 September, at about twenty tonnes a day, soon about thirty.", "source": "travis-2015; appl-1997" },
    { "year": "1916", "lane": "laboratory", "entry": "The Haber and Le Rossignol patent is granted on 31 October.", "source": "haber-patent" }
  ],
  "figureAccessibilityContract": {
    "rule": "Critical figure accessibility text carries the same distinctions the visible figure carries. It is checked against canonical chronology metadata, not against one hard-coded sentence.",
    "figures": [
      {
        "id": "technology-sequence",
        "selector": "[data-sequence-contract]",
        "roles": ["student", "accessible"],
        "chronologyYear": "1909",
        "chronologyLane": "laboratory",
        "requiresSourcedConditionParity": true,
        "requiresRolePartity": true,
        "prohibitedPatterns": [
          { "id": "merged-pressure-range", "regex": "175\\s*(?:to|-|\\u2013|\\u2014)\\s*200", "why": "merges Appl's obtained 175 bar with Travis's calculated 200 atmospheres into one false condition" },
          { "id": "bar-atm-substitution", "regex": "175\\s*(?:atm|atmospheres)", "why": "Appl states 175 in bar; restating it in atmospheres performs an unmarked conversion" },
          { "id": "atm-bar-substitution", "regex": "200\\s*bar", "why": "Travis states 200 in atmospheres; restating it in bar performs an unmarked conversion" }
        ]
      }
    ],
    "attributionParity": {
      "rule": "Where the visible figure distinguishes who diagnosed a failure from who aided the solution, the accessibility text must make the same distinction.",
      "prohibitedPatterns": [
        { "id": "joint-embrittlement-diagnosis", "regex": "bosch and (?:franz )?lappe (?:answer|find|found|discover|discovered|establish|established|work out|worked out)", "why": "the diagnosis is Bosch's; Lappe aided the solution" }
      ]
    }
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
      "NGSS MS-PS1-2",
      "NGSS MS-ETS1-1"
    ],
    "ngss": "Both NGSS references are contextual only. Tasks 3 and 4 do reason about a chemical reaction and about criteria and constraints on a designed process, but the assessed product is a historical-technological explanation with source qualification, not a science or engineering practice, and no laboratory investigation or design test is performed. No NGSS alignment is claimed as directly assessed."
  }
};
