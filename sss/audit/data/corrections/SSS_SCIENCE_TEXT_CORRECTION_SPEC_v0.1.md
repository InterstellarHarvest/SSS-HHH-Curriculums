# Space Sprout Sleuth — Science and Historical Text Correction Specification

**Version:** 0.1  
**Game baseline:** `Space-Sprout-Sleuth` `main` at commit `9f07e00`  
**Prepared:** 2026-07-22  
**Purpose:** Exact, narrow replacement text for student-facing statements identified during the curriculum audit. This is not a request for another code audit or refactor.

## Scope rules

- Make only the text changes listed here.
- Keep internal clue IDs, flags, `goto` destinations, diagnosis IDs, and progression logic unchanged unless explicitly stated.
- Do not alter scoring, campaign structure, case numbering, or unrelated dialogue.
- Preserve the story solution while calibrating Earth-science claims.
- Where the story biology is fictional, say so clearly in the explanation without weakening the in-universe evidence.

---

# 1. Campaign 1, Case 1 — ISS microgravity wording and Veggie history

## 1.1 Microgravity wording

### File and locations

`space_sprout_sleuth_data.js`

- approximately line 471 — `cases[0].sources.sensors.nodes.gravity.text`
- approximately line 519 — `cases[0].sources.sensors.nodes.env_factors.text`
- approximately line 874 — `cases[0].clues[1].text`
- `cases[0].sources.crew.nodes.gravitropism_discussion.options[0].label`
- `cases[0].clues[3].learned`

### Replace the gravity sensor text with

```js
text: "═══ GRAVITATIONAL DATA ═══\n\nEnvironment: MICROGRAVITY\nApparent weight: NEAR ZERO\n\nNote: Standard for a Low Earth Orbit facility. The station and everything inside it are continuously falling around Earth, so the usual gravity cue is too weak to guide plant orientation."
```

### In `env_factors.text`, replace

```text
1. Gravitational acceleration: 0.00 g
```

with

```text
1. Environment: microgravity / apparent weightlessness
```

### In the formal sensor clue, replace

```text
⚠️ Gravitational acceleration: 0.00 g.
```

with

```text
⚠️ Environment: microgravity — the normal downward orientation cue is greatly reduced.
```

### Replace the crew option label

```text
Exactly. No gravity means no orientation signal.
```

with

```text
Exactly. In microgravity, the usual gravity cue is too weak to guide orientation.
```

### Replace the clue summary

```text
Plants use gravity to orient roots. No gravity = no orientation.
```

with

```text
Plants normally use gravity to orient roots. In microgravity, statoliths do not settle normally, so roots lose a reliable “down” cue.
```

## 1.2 Veggie fun fact

### Location

Approximately line 937 — `cases[0].explanation.funFact`

### Replace with

```js
funFact: "NASA's Veggie system began operating on the ISS in 2014. In August 2015, Kjell Lindgren harvested red romaine lettuce and shared it with Scott Kelly and Kimiya Yui — the first time a station-grown crop was officially served to the crew. An earlier Veg-01 crop had been returned to Earth for analysis."
```

### Rationale

This distinguishes the earlier research harvest from the first crop officially eaten aboard the station and avoids crediting the achievement to one astronaut.

---

# 2. Campaign 1, Case 2 — bee experiment fun fact

## Location

Approximately line 1523 — `cases[1].explanation.funFact`

## Replace with

```js
funFact: "NASA flew worker honeybees in a short microgravity flight study on STS-3 in 1982. In 1984, a student experiment carried about 3,300 honeybees aboard STS-41C. The bees initially collided with the enclosure walls, but adapted their flight during the week-long mission and built honeycomb in orbit."
```

### Rationale

The documented experiments involved honeybees in 1982 and 1984, not a 1990s bumblebee habitat trial.

---

# 3. Campaign 1, Case 3 — Mars spectrum mechanism and green-light fun fact

The case should still teach that total PAR can appear adequate while the spectrum is biologically unsuitable. The false part is the claim that Martian dust plus a 12 m borosilicate guide selectively removes red while transmitting blue. Martian dust can strongly reduce total light and, during documented storms, allowed red through while filtering much of the green and blue.

Use a **wrong replacement filter at the surface collector** as the red-loss mechanism. This preserves the evidence chain and solution without requiring a redesign.

## 3.1 Light-pipe hardware description

### Location

Approximately line 1814 — `cases[2].sources.sensors.nodes.pipe_details.text`

### Replace with

```js
text: "FIBER OPTIC LIGHT PIPE DATA\n---------------------------\nCable type: Multi-strand full-spectrum silica\nLength: 12m (surface to hab floor)\nSurface collector filter:\n  Replacement unit installed 47 sols ago\n  Part number not recorded\n\nTotal transmission efficiency: 68%\nNote: Wavelength-specific transmission\n  requires full spectral analysis."
```

## 3.2 Spectral analysis

### Location

Approximately line 1821 — `cases[2].sources.sensors.nodes.spectral_analysis.text`

### Replace with

```js
text: "SPECTRAL ANALYSIS - LIGHT PIPES\n-------------------------------\nSurface intake vs hab output:\n\nBlue  (400-500nm): 92% transmission\nGreen (500-600nm): 88% transmission\nRed   (600-700nm): 31% transmission !!\nDeep red (700nm+): 12% transmission !!\n\n!! WARNING: Selective red rejection\nis occurring at the surface collector.\nLikely cause: wrong-model thermal\ncontrol filter or optical coating.\n\nMars dust lowers total transmission,\nbut does not explain blue and green\npassing while red is rejected.\n\nRed delivery: CRITICALLY INSUFFICIENT\nfor normal chlorophyll development."
```

## 3.3 Lighting documentation

### Location

`cases[2].sources.logs.nodes.lighting_docs.text`

### Replace with

```js
text: "LIGHTING SYSTEM DOCUMENTATION\n-----------------------------\nPrimary: Fiber optic light pipes\n  12m full-spectrum silica guides\n  Surface collector -> ceiling diffuser\n  Rated for full PAR transmission\n\nSurface collector includes a replaceable\nthermal-control filter.\nRequired model: FS-7 FULL SPECTRUM\n\nSupplemental: White LED panels (4000K)\n  Broad-spectrum, ~30% of total PAR\n\nCombined PAR: 280 umol/m2/s\nDesign note: 'PAR adequate for all\ncrop types in rotation.'\n\nSpectral analysis: NOT PERFORMED\n(PAR reading deemed sufficient)"
```

## 3.4 Technical-search node

### Location

Approximately line 2006 — `cases[2].sources.logs.nodes.fiber_optic_search.text`

### Replace with

```js
text: "SEARCH: 'COLLECTOR FILTER TRANSMISSION'\n----------------------------------\nTechnical brief: Spectral filters in\nsolar collection systems.\n\nCorrect filter — FS-7 FULL SPECTRUM:\n- Passes visible PAR from 400-700nm\n- Rejects excess infrared heat\n\nIncorrect filter — BP-4 BLUE PASS:\n- Passes blue and green wavelengths\n- Rejects most red and deep red\n- Intended for algae imaging systems\n\nMaintenance record:\n- Filter replaced 47 sols ago\n- Installed part number: NOT LOGGED\n\nRecommendation: Inspect collector,\nreplace with FS-7, and verify output\nwith a spectrometer before planting."
```

The node ID may remain `fiber_optic_search` to avoid unnecessary wiring changes.

## 3.5 Explanation body

### Location

`cases[2].explanation.body`

### Replace with

```js
body: "Plants do not just need “enough” light — they need a usable spectrum. In many flowering plants, the light-dependent enzyme protochlorophyllide oxidoreductase helps convert protochlorophyllide into chlorophyllide during chlorophyll production. New leaves are affected first when this pathway is disrupted because developing tissue must manufacture new chlorophyll.\n\nIn this habitat, the total PAR reading looked adequate because blue and green photons were still reaching the crop. A wrong replacement filter at the surface collector was selectively rejecting much of the red output, so the total-light number concealed a serious spectral deficit. Mars dust can reduce the amount of sunlight reaching a collector, but it would not explain this particular pattern of blue and green transmission with severe red loss.\n\nThe engineering lesson is to measure spectrum as well as total intensity. Space greenhouses also benefit from independently controlled, tunable LED backup rather than relying on one optical pathway."
```

## 3.6 Green-light fun fact

### Location

Approximately line 2108 — `cases[2].explanation.funFact`

### Replace with

```js
funFact: "Many indoor farm fixtures emphasize red and blue because chlorophyll absorbs those wavelengths strongly, but green light is not wasted. It penetrates deeper into leaves and crop canopies and can support photosynthesis in tissues that surface-absorbed red and blue light do not reach as effectively."
```

---

# 4. Campaign 1, Case 4 — continuous illumination in the Spirulina reactor

The correct diagnosis should be **reactor-specific photoinhibition caused by uncontrolled continuous exposure**, not a universal claim that *Arthrospira/Limnospira* requires darkness. Continuous cultivation can work when light intensity, cell density, mixing, and dilution are controlled.

Keep the existing internal clue ID `DARK_PERIOD_REQUIRED` to avoid unnecessary code changes.

## 4.1 Repeated option labels

Replace both occurrences of:

```text
The setup manual says dark periods are essential.
```

and the occurrence of:

```text
The manual says dark periods are essential.
```

with:

```text
The manual says this reactor needs a recovery interval or lower controlled light.
```

## 4.2 Crew reasoning nodes

### `repair_insight.text`

Replace with:

```js
text: "Repair systems? So the light is not just providing energy — under these conditions it is causing damage faster than the cells can compensate. A scheduled dark or low-light interval would cut the photon load long enough for the culture to recover."
```

### `dark_needed.text`

Replace with:

```js
text: "Of course. For this reactor, the scheduled dark period was the simplest way to keep the daily light dose within its validated range. Without independent control, continuous corridor lighting pushes damage faster than repair until the culture collapses. Then the survivors rebuild and the cycle repeats."
```

### `ros_explanation.text`

Replace with:

```js
text: "ROS — reactive oxygen species generated during photosynthesis. The reactor was stable under 16/8 and began crashing after the switch to uncontrolled 24/0 exposure. That does not mean every spirulina culture requires night, but it does mean this reactor's current light regime exceeds what it can safely process."
```

### `dark_period_insight.text`

Replace with:

```js
text: "The manual says this reactor was validated at 12–16 hours of light per day at its current mixing rate and culture density. Continuous operation requires independent intensity control and different operating conditions. We have been running 24/0 from the corridor lights with no control at all."
```

### `no_dark_insight.text`

Replace with:

```js
text: "24/0 with no independent control. Every time Roth runs the corridor lights around the clock, the reactor receives an excessive daily light dose. Restoring the old schedule is the quickest safe fix; independent dimming and better process control would be the longer-term solution."
```

## 4.3 Sensor cross-reference

### `photoperiod_crossref.text`

Replace with:

```js
text: "+----------------------------------+\n|  CROSS-REFERENCE ANALYSIS        |\n+----------------------------------+\n\nValidated reactor schedule:\n  12-16h light / day at current\n  mixing and culture density\nActual: 24h uncontrolled light\nDeviation: +8 to +12h exposure\n\nManual warns: under THIS reactor's\ncurrent operating conditions,\ncontinuous illumination can cause\nphotooxidative stress and collapse.\n\nActual collapse onset: 7 days.\nWithin predicted range."
```

## 4.4 Setup-manual nodes

### Approximately line 2523 — `photoperiod_entry.text`

Replace with:

```js
text: "+----------------------------------+\n|  BIOREACTOR SETUP MANUAL v2.4    |\n|  Section 4.2: Light Management   |\n+----------------------------------+\n\nValidated operating schedule for\nthis reactor configuration:\n  12-16 hours light\n  8-12 hours dark or low-light\n\nOperating assumptions:\n  - Current culture density\n  - Current mixing rate\n  - PAR within validated range\n\nContinuous operation is possible\nonly with independent intensity,\nmixing, and density control.\n\n!! WARNING: Uncontrolled 24/0\nillumination in this configuration\ncan cause photooxidative stress\nand culture collapse."
```

### `dark_period_detail.text`

Replace with:

```js
text: "+----------------------------------+\n|  Section 4.2.1: Recovery Load    |\n|  Biological Rationale            |\n+----------------------------------+\n\nPhotosynthetic electron transport can\ngenerate reactive oxygen species (ROS),\nespecially when absorbed light exceeds\nthe culture's ability to use or dissipate\nthat energy.\n\nCells repair photosystems and run\nantioxidant pathways in both light and\ndark conditions. In this reactor, a dark\nor lower-light interval reduces the daily\nphoton load enough for repair to keep up.\n\nWithout intensity control, ROS damage\noutpaces recovery and the culture crashes."
```

### `continuous_light.text`

Replace with:

```js
text: "+----------------------------------+\n|  SEARCH: continuous light        |\n|  3 results                       |\n+----------------------------------+\n\nResult 1 - Setup Manual 4.2:\n\"Continuous operation requires\nindependent light and process control.\nDo not expose this configuration to\nuncontrolled 24/0 corridor lighting.\"\n\nResult 2 - Maintenance Log Day 8:\n\"Scheduled recovery interval:\n2200-0600. Automated blackout confirmed.\"\n\nResult 3 - Cmdr Order #4471:\n\"Effective Day 121: all hab\nlighting to 24/0 continuous.\nNo exceptions.\""
```

### `photooxidative_search.text`

Replace with:

```js
text: "+----------------------------------+\n|  SEARCH: photooxidative stress   |\n|  2 results                       |\n+----------------------------------+\n\nResult 1 - Setup Manual 4.2.1:\n\"When absorbed light exceeds carbon\nfixation, mixing, and protective capacity,\nROS damage can outpace repair. Reduce\nintensity or add a recovery interval.\"\n\nResult 2 - Troubleshooting Guide:\n\"If culture shows photooxidative\ndamage, FIRST compare total daily\nlight exposure with validated settings.\""
```

## 4.5 Formal log clue

### `cases[3].clues[3].text`

Replace with:

```js
text: "Bioreactor setup manual: \"This reactor configuration was validated at 12–16 hours of light per day with a scheduled dark or low-light recovery interval. Continuous operation requires independent intensity, mixing, and culture-density control.\"\n\n⚠️ WARNING: Uncontrolled 24/0 illumination can cause photooxidative stress and culture collapse."
```

### `cases[3].clues[3].learned`

Replace with:

```js
learned: "The reactor manual warns that uncontrolled 24/0 exposure exceeds this system's validated operating range."
```

## 4.6 Correct diagnosis

### Approximately line 2636 — `cases[3].diagnoses[1].label`

Replace with:

```js
label: "Uncontrolled 24-hour lighting is causing recurrent photoinhibition in this reactor. Restore the validated light/recovery schedule now and add independent intensity control."
```

## 4.7 Explanation

### Title

Replace with:

```js
title: "The Dark Side of Light: Why Bioreactors Need Light Control"
```

### Body

Replace with:

```js
body: "Photosynthesis captures light energy, but more light is not automatically better. When a culture absorbs photons faster than it can use or safely dissipate the energy, photosynthetic electron transport can generate reactive oxygen species and damage pigments, proteins, and membranes. Whether continuous illumination works depends on the organism and on reactor conditions such as photon flux, cell density, mixing, nutrient supply, temperature, and dilution rate.\n\nThis spirulina reactor had operated safely on a validated 16/8 schedule. When the shared corridor lighting changed to 24/0, the reactor had no independent dimming or blackout control. Its daily photon dose rose sharply, photooxidative damage outpaced recovery, and the culture entered a crash-and-regrowth cycle. Restoring the old schedule is the fastest remedy; the better engineering fix is independent control of light intensity and reactor conditions.\n\nThe lesson for space-habitat design is not that every photosynthetic organism requires night. It is that biological life-support equipment needs its own validated environmental controls rather than inheriting settings chosen for human convenience."
```

### Fun fact

Replace with:

```js
funFact: "Long-duration continuous cultivation of Limnospira has been demonstrated in a controlled air-lift photobioreactor developed for regenerative space life support. In that system, photoinhibition depended on light level and culture density and was reversible when illumination was reduced."
```

---

# 5. Campaign 1, Case 5 — ISS versus Moon radiation protection

## Location

Approximately line 3193 — `cases[4].explanation.body`

## Replace the opening paragraph with

```text
Earth's magnetic field and thick atmosphere shield surface life from much of the space-radiation environment. The ISS remains in low Earth orbit inside Earth's magnetosphere, and its structure adds further shielding. The Moon is different: it has almost no atmosphere and no global magnetic field, so lunar habitats require their own local shielding. The Moon passes through parts of Earth's magnetotail for a few days during some orbits, but that protection is partial and intermittent. Europa, meanwhile, orbits inside Jupiter's intense radiation environment. Even beneath ice, interactions between energetic particles and shielding materials can produce secondary radiation that must be considered in habitat design.
```

Leave the seedling-sensitivity and solution paragraph unchanged unless a later specialist radiation review is requested.

---

# 6. Campaign 2, Case 3 — pigment and spectral-match wording

The alien organism may remain blue-green adapted, but red light should be described as **poorly matched or inefficient**, not categorically unusable. For Earth parallels, use chlorophyll a/c and fucoxanthin for brown algae and diatoms. The zhal-kelp may retain fictional additional pigments.

## 6.1 Crew dialogue

### Approximately line 1432 — `cant_use_red.text`

Replace with:

```js
text: "'It is not that the kelp cannot use any red light. Its light-harvesting system is simply optimized for the blue-green photons that dominate its native water. A red-heavy lamp delivers far less usable energy than its total brightness suggests. The kelp has chlorophyll a and c plus blue-green accessory pigments; red contributes, but inefficiently compared with the spectrum it evolved under.'"
```

### Approximately line 1488 — `spectrum_insight.text`

Replace with:

```js
text: "'62% red.' Tei-sal's patches flash. 'There it is. Most of the output is concentrated where the kelp captures energy least efficiently. Another 18% is blue — partly useful. Less than 5% is in its strongest blue-green range. The dome is not literally dark, but its usable photon supply is far below what the total PAR number implies.'"
```

### `realization.text`

Replace with:

```js
text: "'So you see it now. The lights are not broken. The kelp is not broken. The specification was incomplete. Earth crop lights emphasize wavelengths suited to terrestrial plant pigments. Deep-water algae use different light-harvesting complexes, including chlorophyll c and accessory pigments that capture blue-green light efficiently. A spectrum optimized for one organism can be a poor energy match for another.'"
```

## 6.2 Database entry

### Approximately line 1765 — `chlorophyll_variants.text`

Replace with:

```js
text: "——— LIGHT-HARVESTING PIGMENTS — CONCORD SURVEY ———\n\nChlorophyll a + b (terrestrial plants,\nmost Earth crops):\n  Strong absorption in blue and red.\n  Common grow-light design: red-blue\n  emphasis with broader-spectrum fill.\n\nChlorophyll a + c with accessory pigments\n(brown algae, diatoms, Oolian analogues):\n  Strong blue-green light harvesting.\n  Red contribution: possible but less\n  efficient in this species.\n  Recommended zhal-kelp spectrum:\n  blue-green dominant with balanced fill.\n\n⚠ ADVISORY: Total photon flux alone is\nnot enough. Spectral requirements must\nbe specified for the actual organism."
```

## 6.3 Formal database clue

### Approximately line 1863 — `cases[2].clues[4].learned`

Replace with:

```js
learned: "Zhal-kelp uses a blue-green-optimized light-harvesting system. A red-heavy Earth crop spectrum provides much less usable energy than the total PAR reading suggests."
```

## 6.4 Diagnosis

### Approximately line 1870 — correct diagnosis label

Replace with:

```js
label: "The Earth grow lights are red-heavy and poorly matched to zhal-kelp's blue-green-optimized pigments. The dome is bright, but the kelp receives too few efficiently absorbed photons."
```

## 6.5 Explanation

### Approximately line 1897 — body

Replace with:

```js
body: "Photosynthesis is not powered by one universal pigment recipe. Light-harvesting systems vary among organisms because they evolved under different spectra.\n\nTerrestrial crop plants use chlorophyll a and b and commonly absorb blue and red light strongly. Many grow lights therefore emphasize those regions, often with broader-spectrum light included as well.\n\nBrown algae and diatoms use chlorophyll a and c with accessory pigments such as fucoxanthin that expand strong light harvesting into the blue-green region. Water removes longer red wavelengths more rapidly than blue-green wavelengths, although the exact spectrum depends on depth, particles, and dissolved material. The fictional zhal-kelp is even more strongly adapted to the blue-green light of its native habitat.\n\nThe new dome delivered plenty of total photons, but most were concentrated in a region the kelp used inefficiently. The habitat was not literally dark; it was spectrally mismatched. This is why biological specifications must include spectrum, not merely total intensity."
```

### Fun fact

Replace with:

```js
funFact: "Brown algae such as giant kelp use chlorophyll a and c together with fucoxanthin, an accessory pigment that helps capture blue-green light. Kelp forests still occur in relatively shallow, sunlit coastal water because even well-adapted pigments cannot photosynthesize where too little light remains."
```

---

# 7. Campaign 2, Case 5 — fictional radiation dependence versus Earth evidence

Keep the karreth bloom's radiation-triggered pathway as fictional alien biology. Stop defining this as an established Earth meaning of “radiation hormesis,” and stop stating that Chernobyl fungi perform confirmed radiation-powered photosynthesis.

The internal clue ID `HORMESIS_OBLIGATE_RADIATION` may remain unchanged.

## 7.1 Crew option and response

### Replace option label

```text
Concord records describe obligate radiation dependence. Hormesis.
```

with

```text
Concord records describe an obligate radiation-triggered pathway.
```

### Replace `database_insight.text`

```js
text: "'The Concord documented this.' Kel-tor closes their eyes briefly. 'An obligate radiation-triggered pathway — rare, species-specific, and nothing like the response of ordinary organisms. And they still built a vault with zero background radiation for a species whose medicinal pathway requires that trigger.' A long silence. 'At least the record exists. Your report will have citations.'"
```

## 7.2 Database category entry

### Approximately line 2850 — `database.nodes.hormesis.text`

Replace with:

```js
text: "——— OBLIGATE RADIATION-TRIGGERED METABOLISM ———\n\nConcord classification: a rare, fictional\nbiological system in which a low-level\nionizing-radiation signal activates a\nspecies-specific metabolic pathway.\n\nKnown Concord examples: 5, including\nthe karreth bloom. The exact mechanisms\nare species-specific and should not be\ngeneralized to other organisms.\n\nKarreth mechanism: low-level DNA damage\nactivates a repair cascade whose byproducts\ninclude essential karrethins. Removing the\ntrigger shuts down that pathway.\n\n⚠ ADVISORY: This Concord category is not\nequivalent to a general claim that low-dose\nradiation benefits Earth organisms."
```

## 7.3 Karreth database entry

### Approximately line 2860 — replace the Earth-parallel paragraph only

Replace:

```text
Earth parallel: Certain fungi (Cladosporium sphaerospermum) growing inside the Chernobyl reactor use melanin to convert ionizing radiation into metabolic energy via radiosynthesis.
```

with:

```text
Earth comparison: Laboratory studies have found that ionizing radiation can alter the electron-transfer properties of melanin and can enhance growth or metabolic activity in some melanized fungi under particular conditions. Researchers have proposed a possible energy-capture role, but this is not established as radiation-powered photosynthesis and the fungi are not known to require radiation.
```

## 7.4 Rhessi entry

Replace the bullet:

```text
- Melanin-analogue in integument converts ionizing radiation to supplemental metabolic energy
```

with:

```text
- Melanin-analogue in integument is radioprotective and may contribute to species-specific energy handling
```

Replace:

```text
Full radiation dependence is debated; partial dependence is documented.
```

with:

```text
Within the fictional Concord record, partial dependence is documented for this species; it should not be treated as an Earth biological generalization.
```

## 7.5 Formal clue summary

### Approximately line 2957

Replace with:

```js
learned: "Concord records report that the fictional karreth bloom requires a low-level radiation trigger for the repair pathway that produces karrethins."
```

## 7.6 Explanation

### Title

Replace with:

```js
title: "When a Hazard Becomes a Biological Trigger"
```

### Approximately line 3021 — body

Replace with:

```js
body: "Ionizing radiation is usually biologically damaging because it can break molecules, generate reactive species, and damage DNA. The karreth bloom is fictional alien biology built around an unusual exception: on its high-radiation homeworld, a low-level radiation signal became integrated into a repair pathway that also produces karrethins. Remove the signal, and the valuable pathway switches off.\n\nThis should not be read as a claim that Earth organisms generally benefit from or require ionizing radiation. On Earth, melanin is well established as radioprotective in fungi. Laboratory experiments have also reported increased growth or metabolic activity in some melanized fungi under particular high-radiation conditions and changes in melanin's electron-transfer properties. Those findings led researchers to propose possible radiation-energy capture, but the mechanism and ecological importance remain under study and are not equivalent to ordinary photosynthesis.\n\nThe case's established lesson is an engineering and policy lesson: a universal safety standard can fail when it ignores species-specific requirements. The radiation-dependent karreth pathway itself remains clearly labeled science fiction."
```

### Approximately line 3022 — fun fact

Replace with:

```js
funFact: "Melanized fungi can be unusually radiation resistant. A 2007 laboratory study found that ionizing radiation changed melanin's electronic properties and enhanced growth or metabolic activity in several melanized fungi under specific conditions. The authors described energy capture as an intriguing possibility, not a confirmed form of fungal photosynthesis."
```

---

# 8. Campaign 2, Case 6 — evidence-calibrated mycorrhizal claims

Keep plant–fungus mutualism and the possibility that missing mycorrhizal partners limit restoration. Remove claims that forests universally operate as a cooperative organism, that mature trees reliably feed seedlings, or that warning signals are settled and general. Present inoculation as a controlled restoration trial rather than a guaranteed single fix.

## 8.1 Kess dialogue

### Approximately line 3393 — `function_fragment.text`

Replace with:

```js
text: "'What do they do...' The lights cycle through warm amber — the memory surfacing. 'Fungal hyphae extend beyond individual roots. They help plants acquire phosphorus, nitrogen, and water in exchange for plant carbon. One fungal individual can sometimes connect multiple roots, so substances and signals may move through shared pathways — but the direction and benefit depend on the species and conditions. The soil is not one cooperative mind. It is a network of negotiated partnerships.'"
```

## 8.2 Correct diagnosis label

### Approximately line 3767

Replace with:

```js
label: "Loss of compatible mycorrhizal partners — the restored soil chemistry is suitable, but the fungal-root partnerships needed for efficient nutrient acquisition and connected growth were not re-established. A controlled inoculation trial is warranted."
```

## 8.3 Solution prompt

### Approximately line 3791

Replace with:

```js
prompt: "Your diagnosis is supported — the restored beds appear to be missing compatible mycorrhizal partners after the industrial damage. A controlled inoculation trial using soil or cultured fungi from the healthy original beds is the best-supported next step, with monitoring to test whether connectivity and plant performance improve. But Concord biosafety regulations technically forbid the transfer. How do you proceed?"
```

Where solution responses say the garden begins healing immediately or certainly, soften them to indicate the monitored trial begins and early indicators improve. Preserve the ethical/policy distinction among the three choices.

Recommended minimal wording changes:

- Formal option: replace “The inoculation begins” with “The monitored inoculation trial begins.”
- Immediate option: replace “The garden begins healing that afternoon” with “The inoculation trial begins that afternoon; recovery will be measured over the coming weeks.”
- Reform option may remain focused on policy but should not imply that policy reform alone proves ecological success.

## 8.4 Explanation title

Replace with:

```js
title: "Mycorrhizae: Underground Partnerships in Ecosystems"
```

## 8.5 Explanation body

### Approximately line 3824

Replace with:

```js
body: "Many land plants form partnerships with mycorrhizal fungi. The fungi grow fine hyphae through soil, receive carbon compounds from plants, and help their plant partners obtain resources such as phosphorus, nitrogen, and water. A single fungal individual can colonize more than one root system, creating a common mycorrhizal network.\n\nExperiments show that carbon, nutrients, water, and signaling compounds can sometimes move among organisms associated with these networks. What those movements mean ecologically is still debated. The amount transferred, the direction of transfer, and whether a receiving plant benefits vary with fungal species, plant species, soil conditions, competition, and experimental design. Current evidence does not support a universal claim that mature 'mother trees' preferentially feed seedlings or that forests behave as one cooperative organism.\n\nIndustrial disturbance can damage soil fungal communities as well as soil chemistry. Restoration may therefore need to rebuild biological partnerships, but inoculation is not a guaranteed one-step cure. Fungal identity, host compatibility, soil conditions, contamination risk, and monitoring all matter. In this fictional case, the evidence makes missing compatible mycorrhizal partners a plausible limiting factor, so a controlled inoculation trial is the scientifically responsible next step."
```

## 8.6 Fun fact

### Approximately line 3825

Replace with:

```js
funFact: "In 2026, researchers produced the first global map estimating the density of arbuscular mycorrhizal fungal networks, calculating about 110 quadrillion kilometers of living hyphae in Earth's topsoils. A separate 2023 synthesis estimated that plants allocate about 13.12 gigatons of CO₂-equivalent carbon to mycorrhizal mycelium each year — an annual carbon flux, not a measurement of permanent carbon storage."
```

---

# 9. No game-text changes required

The following should remain in the game and be handled through teacher notes:

- C1-5 exact Europa radiation dose and shielding architecture: modeled fiction.
- C1-6 and C1-7 alien VOC signaling and germination response: fiction inspired by real chemical signaling.
- C2-1 exact alien gravity tolerance and habitat dimensions: fiction built on correct rotating-habitat physics.
- C2-2 exact alien buzz-pollination trigger: fiction built on real poricidal-anther mechanics.
- C2-4 Zhel'ii darkness-triggered VOC network: explicitly species-specific fiction.
- The game score: motivational game feedback only, never the academic grade.

---

# 10. Verification sources

## NASA and spaceflight history

- NASA, first station-grown crop officially served to crew, 10 August 2015:  
  https://www.nasa.gov/blogs/spacestation/2015/08/10/cosmonauts-complete-russian-spacewalk/
- NASA NTRS, worker honeybee flight observation on STS-3 (1982):  
  https://ntrs.nasa.gov/citations/19830025642
- NASA Life Sciences Data Archive, 1984 honeycomb experiment results:  
  https://nlsp.nasa.gov/view/lsdapub/lsda_experiment/879ffe10-dc28-5966-9a09-54697852d631
- NASA, STS-41C history including the 3,300-honeybee student experiment:  
  https://www.nasa.gov/history/40-years-ago-sts-41c-the-solar-max-repair-mission/
- NASA/JPL, Martian dust allowing red while filtering most green and blue:  
  https://www.jpl.nasa.gov/images/pia22330-duluth-after-dust-storm/
- NASA, ISS inside Earth's magnetosphere versus lunar radiation exposure:  
  https://www.nasa.gov/science-research/heliophysics/real-martians-how-to-protect-astronauts-from-space-radiation-on-mars/  
  https://science.nasa.gov/moon/weather-on-the-moon/  
  https://science.nasa.gov/moon/solar-wind/

## Photosynthesis and photobioreactors

- Terashima et al. (2009), green light and deeper leaf photosynthesis:  
  https://pubmed.ncbi.nlm.nih.gov/19246458/
- Liu & van Iersel (2021), blue/green/red photosynthetic physiology:  
  https://pubmed.ncbi.nlm.nih.gov/33747002/
- Long-term continuous cultivation of *Limnospira indica*:  
  https://pubmed.ncbi.nlm.nih.gov/34342154/
- Alberte et al. (1981), chlorophyll a/c and fucoxanthin complexes:  
  https://pubmed.ncbi.nlm.nih.gov/7016188/

## Melanized fungi and radiation

- Dadachova et al. (2007), radiation, melanin, and fungal growth:  
  https://pubmed.ncbi.nlm.nih.gov/17520016/
- Dadachova & Casadevall (2008), review of proposed fungal radiation-energy utilization:  
  https://pubmed.ncbi.nlm.nih.gov/18848901/
- Dadachova et al. (2008), fungal melanin radioprotection:  
  https://pubmed.ncbi.nlm.nih.gov/18426412/

## Mycorrhizal networks and carbon

- Karst, Jones & Hoeksema (2023), overinterpretation of common-network claims:  
  https://www.nature.com/articles/s41559-023-01986-1
- Henriksson et al. (2023), re-examination of the mother-tree hypothesis:  
  https://pubmed.ncbi.nlm.nih.gov/37149889/
- Hawkins et al. (2023), 13.12 Gt CO₂e annual allocation estimate:  
  https://doi.org/10.1016/j.cub.2023.02.027
- Stewart et al. (2026), first global density/biomass map of arbuscular mycorrhizal fungal networks:  
  https://doi.org/10.1126/science.adu4373

---

# 11. Efficient implementation instruction

Apply only the replacements above. Syntax-check both data files, boot the game once, and confirm the edited cases still reveal all existing clues and reach their diagnoses. No new validator, test framework, refactor, or broad content audit is requested.
