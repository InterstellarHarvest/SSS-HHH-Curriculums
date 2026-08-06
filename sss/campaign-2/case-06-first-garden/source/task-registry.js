window.SSS_C2_CASE06_TASK_REGISTRY = {
  "schemaVersion": 1,
  "case": "SSS-C2-CASE06",
  "title": "The First Garden",
  "version": "1.0",
  "status": "APPROVED_STABLE",
  "approvalDate": "2026-08-05",
  "approvedBy": "Nate / Owner",
  "ownerReviewStatus": "OWNER_REVIEW_PASS",
  "mergeStatus": "READY_TO_MERGE",
  "editorShell": "1.0",
  "gameCommit": "29c3b222c53f51de11a3aa83e896a6d0ef6fb490",
  "runtimeCaseId": "first_garden",
  "runtimeInvestigationName": "The First Garden",
  "runtimeLocation": "Restored Terrace",
  "runtimeSubtitle": "Earth",
  "runtimeBonusCase": true,
  "runtimeCampaignPosition": 6,
  "runtimeUnlockCondition": "Hidden from level select until all five main Campaign 2 cases are complete; the runtime then labels it case 6 of 6.",
  "roles": {
    "student": 5,
    "teacher": 8,
    "answer": 5,
    "accessible": 7
  },
  "tasks": [
    {
      "id": "C2-C06-T1",
      "number": "1",
      "semanticLabel": "REFERENCE",
      "icon": "ph-book",
      "title": "Sort What Was Tested from What Was Never Tested",
      "description": "Separate the eight parts of the soil that forty years of restoration examined from the one part no panel ever examined, and explain why a set of clean results is not evidence that nothing is wrong.",
      "keyed": true
    },
    {
      "id": "C2-C06-T2",
      "number": "2",
      "semanticLabel": "PATTERN ANALYSIS",
      "icon": "ph-scales",
      "title": "Read the Pattern in the Site Survey",
      "description": "Describe what the chemical survey found inside a surveyed patch and what it found between patches, and explain why a chemical survey cannot identify the organism or prove an absence on its own.",
      "keyed": true
    },
    {
      "id": "C2-C06-T3",
      "number": "3",
      "semanticLabel": "EVIDENCE",
      "icon": "ph-diagnosis",
      "title": "Weigh the Explanations",
      "description": "Use the construction history of the two kinds of bed to select the best-supported candidate cause, and write the record that rules out each of the three rejected explanations.",
      "keyed": true
    },
    {
      "id": "C2-C06-T4",
      "number": "4",
      "semanticLabel": "EVIDENCE SYNTHESIS",
      "icon": "ph-nodes",
      "title": "Show Where the Five Sources Converge",
      "description": "State what each of the five sources establishes and what it cannot establish alone, then write one sentence for what the five together support and what they still leave untested.",
      "keyed": true
    },
    {
      "id": "C2-C06-T5",
      "number": "5",
      "semanticLabel": "MECHANISM",
      "icon": "ph-flow",
      "title": "Model the Candidate Pathway",
      "description": "Complete the condition-mechanism-effect model in causal order using the word bank, then name one thing the completed model does not establish.",
      "keyed": true
    },
    {
      "id": "C2-C06-T6",
      "number": "6",
      "semanticLabel": "EXPLANATION",
      "icon": "ph-cer",
      "title": "Explain the Diagnosis with CER",
      "description": "Write a Claim-Evidence-Reasoning explanation using evidence from more than one source, keeping the candidate cause framed as a candidate, and naming at least one thing the evidence does not establish.",
      "keyed": true
    },
    {
      "id": "C2-C06-T7",
      "number": "7",
      "semanticLabel": "ENGINEERING DESIGN",
      "icon": "ph-wrench",
      "title": "Specify the Screened, Approved Trial",
      "description": "Define what the trial must compare and why it needs untreated control plots, name one constraint, and justify why approval and screening still apply to a transfer in which the fungi and the soil both come from Earth.",
      "keyed": true
    }
  ],
  "formalClues": [
    "RESTORATION_HISTORY",
    "CHEMICAL_DISCONNECTION",
    "MYCORRHIZAL_NETWORK",
    "CONCORD_REGULATION",
    "DATABASE_PRECEDENT"
  ],
  "clueTaskCoverage": {
    "RESTORATION_HISTORY": [1, 3, 4],
    "CHEMICAL_DISCONNECTION": [2, 3, 4, 5],
    "MYCORRHIZAL_NETWORK": [4, 5, 6],
    "CONCORD_REGULATION": [4, 7],
    "DATABASE_PRECEDENT": [4, 7]
  },
  "requiredRoutes": [
    "nova.start->problem",
    "vorn_shael.start->chemical_reading",
    "kess.start->direct_ask",
    "ilreth_mar.start->role",
    "database.start->exemptions"
  ],
  "sourceLedger": [
    {
      "source": "Dr. Nova",
      "clue": "RESTORATION_HISTORY",
      "establishes": "Forty years of remediation across three generations, that the original beds were established from mature garden soil while the expansion beds were built from clean remediated substrate, that both receive identical amendments, water, compost and seed, and that every conventional gardening fix has already been tried and ruled out.",
      "cannotEstablishAlone": "She measured no living community. Eliminating the conventional fixes narrows the field but does not identify what remains, and the thriving beds were never sampled either."
    },
    {
      "source": "Delegate Vorn-Shael",
      "clue": "CHEMICAL_DISCONNECTION",
      "establishes": "Phosphorus, nitrogen, carbon chains and signalling compounds are present inside circular patches of approximately four to six metres in diameter and at trace levels only between them, the boundaries are sharp despite adequate matrix diffusion, and the measured transport signature is reduced.",
      "cannotEstablishAlone": "Chemistry establishes a distribution. It identifies no organism and cannot prove that any particular organism is absent, which the delegate states directly and repeats when pressed."
    },
    {
      "source": "Delegate Kess",
      "clue": "MYCORRHIZAL_NETWORK",
      "establishes": "That fungal hyphae colonise compatible roots, receive plant carbon, and can improve acquisition of phosphorus, nitrogen or water, and that one fungal individual may colonise more than one root.",
      "cannotEstablishAlone": "The account is a reconstructed and fragmentary ancestral memory from a species that abandoned soil cultivation three thousand years ago. It describes a mechanism, not any organism in this garden."
    },
    {
      "source": "Delegate Ilreth-Mar",
      "clue": "CONCORD_REGULATION",
      "establishes": "That Section 14.7 classifies cross-zone transfer of living biological material as a contamination risk requiring prior Concord approval, and that this summit site is a designated zone.",
      "cannotEstablishAlone": "It is a constraint on the response, not evidence about the cause. It contributes no biology and identifies nothing in the soil."
    },
    {
      "source": "Federation Database",
      "clue": "DATABASE_PRECEDENT",
      "establishes": "The Earth mycorrhizal record, the text of Section 14.7 and its acknowledged ambiguity for within-world transfers, and the GC-2201 within-species agricultural exemption precedent.",
      "cannotEstablishAlone": "It reports general findings and precedent and explicitly declines to generalise to any particular site. It measures nothing in this garden."
    }
  ],
  "numericalLedger": {
    "surveyedPattern": {
      "patchDiameter": "approximately four to six metres",
      "patchDiameterStatus": "reported as a range for circular patches; not an average and not a single measured patch",
      "betweenPatches": "trace levels only",
      "betweenPatchesStatus": "the compounds are detected between patches; never write zero, absent, or none",
      "adjacentSeparation": "about three metres",
      "adjacentSeparationStatus": "the described distance between thriving and failing ground; not a surveyed boundary offset",
      "boundary": "sharp, despite adequate matrix diffusion",
      "transportSignature": "reduced against the delegate's homeworld reference",
      "compounds": "phosphorus, nitrogen, carbon chains, and signalling compounds — auxins, cytokinins, strigolactones"
    },
    "restorationHistory": {
      "remediationPeriod": "forty years",
      "generations": "three",
      "composting": "twenty years",
      "coverCropping": "six species rotations",
      "originalBeds": "established from mature garden soil",
      "expansionBeds": "built from scratch: clean remediated substrate with amendments",
      "toxicology": "every toxicology panel comes back clear"
    },
    "regulation": {
      "section": "Section 14.7",
      "sectionStatus": "a review requirement, not a prohibition",
      "precedentGranted": "GC-2201",
      "precedentPending": "GC-2445",
      "memberSpeciesCiting": "3"
    },
    "globalContext": {
      "hyphalLength": "about 110 quadrillion kilometres of hyphae in Earth's topsoils",
      "carbonAllocation": "about 13.12 gigatons of CO2-equivalent carbon each year",
      "status": "published global estimates from the runtime fact panel, not measurements of this garden; the carbon figure is an annual flux and not stored carbon. Neither figure is used in any student-facing task."
    },
    "note": "This case reports no time series, no dated events, and no calculation. There is nothing to plot as a trend and nothing to compute."
  },
  "sourceStatus": {
    "establishedEarthScience": "Many land plants associate with mycorrhizal fungi. Hyphae extend beyond the root, receive carbon from the plant, and can help particular hosts acquire phosphorus, nitrogen or water. A single fungal individual may colonise more than one root, which is what a common mycorrhizal network is. Experiments sometimes detect movement of carbon, nutrients, water or signalling compounds along shared pathways, but magnitude, direction, and whether a receiving plant benefits vary with fungus, plant, soil and experimental design. Industrial disturbance can damage soil fungal communities as well as soil chemistry.",
    "establishedEarthScienceBoundary": "The evidence does not support a universal cooperative network, does not establish that mature trees preferentially feed related seedlings, and does not support treating a forest as one organism. Inoculation can fail and can cause harm, and effects have been observed beyond directly inoculated plants, which is why monitoring for spread is required.",
    "caseSpecificEvidence": "The garden, the forty-year restoration, the two kinds of bed, the surveyed chemical distribution, the patch dimensions, the four delegates, the biosafety regulation and the exemption precedents are records made for this case.",
    "modeledEvidence": "The global estimates of topsoil hyphal length and of annual plant-carbon allocation to mycorrhizal mycelium are published global estimates rather than measurements of this garden, and the carbon figure is an annual flux rather than stored carbon. Neither appears in any student-facing task.",
    "caseInference": "That failed or incomplete re-establishment of compatible mycorrhizal partners caused the patch pattern is the best-supported candidate cause from a construction-history contrast, a surveyed distribution, and a set of eliminated alternatives. It is not an established mechanism, which is why the packet ends in a screened, approved, controlled trial rather than a treatment.",
    "engineeringExtrapolation": "The trial requirements in Task 7 — approval, organism identification, provenance and pathogen screening, host-compatibility checks, replicated untreated controls, monitoring for spread, and staged expansion — follow the runtime's own decision boundary and ordinary practice for introducing living material, not from any measurement in the case.",
    "numbers": "Every printed value is reproduced exactly as its record reports it. The patch diameter keeps 'approximately' and stays a range, the separation keeps 'about', 'trace levels only' is never written as zero or absent, and no value is calculated from another.",
    "figures": "Figure A is curriculum-original. It draws the surveyed pattern along a twelve-metre strip using the survey's own distances, with hatched ground where the compounds are abundant and dotted ground where they fall to trace levels. Its caption and extended description both state that it shows the reported pattern and is not a map of the garden.",
    "teachingAnalogy": "The building-inspection example carries the scope-of-testing idea without using any garden value, contains no numbers at all, and prints a visible line stating that it is not a garden record."
  },
  "correctDiagnosis": "Failed or incomplete re-establishment of compatible mycorrhizal partners in the beds built from clean remediated substrate is the best-supported candidate cause of the garden's patch pattern. The organisms present in both kinds of bed must still be identified and tested against untreated controls before causation is claimed.",
  "incorrectAlternatives": [
    "Soil pH imbalance from residual concrete leaching into the restored beds.",
    "Inconsistent irrigation creating drought stress in the struggling zones.",
    "Invasive organisms carried in by the Concord delegates' ships are disrupting local biology."
  ],
  "prohibitedClaims": [
    "Describing the soil as a wood wide web, an underground internet, a superorganism, or one cooperative mind.",
    "Claiming that mature trees preferentially feed their own seedlings through a fungal network.",
    "Claiming that a forest behaves as a single cooperative organism.",
    "Stating the mycorrhizal explanation as a proven mechanism rather than a candidate cause to be tested.",
    "Declaring that compatible fungi are certainly absent, or that the network was never restored.",
    "Claiming that inoculation is a guaranteed cure, or promising that the garden will recover.",
    "Promising a recovery time before a monitored trial has produced evidence.",
    "Proposing transfer of living soil or fungi without organism identification, provenance and pathogen screening, host-compatibility checks, approval, controls and monitoring.",
    "Claiming that a within-world transfer carries no ecological risk because both zones are on Earth.",
    "Claiming that urgency removes the review requirement, or that Section 14.7 may simply be ignored.",
    "Claiming that nutrients or signals always move through shared fungal pathways, or that a receiving plant always benefits.",
    "Treating clean chemistry and toxicology panels as proof that the soil biology is intact.",
    "Claiming that the chemical survey proves which organism is missing.",
    "Claiming that all land plants require mycorrhizal fungi.",
    "Presenting the global hyphal-length or carbon-allocation estimates as measurements made at this garden.",
    "Presenting annual carbon allocation to mycorrhizal mycelium as permanent carbon storage.",
    "Attributing intention to the fungi or the plants, as though they decided, chose, or wanted to share.",
    "Naming a commercial inoculant product, supplier, or a specific species to add.",
    "Generalising this garden's result to any other restoration site as a certainty.",
    "Claiming that the restoration team was incompetent or that the soil tests were wrong."
  ],
  "figureProvenance": [
    {
      "id": "fig-patches-student",
      "kind": "curriculum-original case record figure",
      "shows": "One twelve-metre strip on which the surveyed compounds are abundant from 0 to 5 metres, fall to trace levels only from 5 to 8 metres, and are abundant again from 8 metres, with the survey's reported patch diameter of about 4-6 metres and separation of about 3 metres labelled directly.",
      "prohibited": "It must never be read as a map of the garden or used to infer where any particular bed sits, and the trace-level ground must never be described as empty or as containing none of the compounds."
    },
    {
      "id": "fig-patches-accessible",
      "kind": "curriculum-original case record figure",
      "shows": "The Accessible edition of the same surveyed strip, with identical distances, identical zones and identical fill patterns.",
      "prohibited": "It must never be read as a map of the garden or used to infer where any particular bed sits, and the trace-level ground must never be described as empty or as containing none of the compounds."
    }
  ],
  "productionCautions": [
    "The design document for this case describes the mechanism as the 'wood wide web' and as a network that 'was never fully restored', and its draft diagnosis text states the connections were never restored as fact. The shipped runtime supersedes both, and the game's own content suite asserts against that wording. The packet follows the runtime: a candidate cause, framed as a hypothesis, tested by a controlled trial.",
    "The internal clue tag reads MYCORRHIZAL_NETWORK, and the design documents reference Suzanne Simard's mother-tree work. Neither the tag nor the mother-tree claim appears in the printable packet, and the mother-tree claim is listed as a prohibited claim because the approved science-source register records it as not established.",
    "No printable role may name an organism, product, or supplier to add to the soil. Task 7 states on the page that those decisions belong to the team that identifies and screens the organisms.",
    "The phrase 'trace levels only' must always travel intact. Reducing it to zero or to absent converts a detection into an absence and is the central misconception of the case.",
    "This case reports no time series and no dated events, so the packet contains no timeline and no trend figure. Adding either would require inventing data the runtime does not supply.",
    "This case contains no calculation. No mathematics standard is claimed, and none should be added on the strength of the patch dimensions.",
    "MS-LS2-3 is recorded as supporting rather than direct. The performance expectation names cycling of matter and flow of energy, and this case supplies no cycling or energy-flow measurements; the evidence is a spatial distribution and a construction history."
  ]
};
