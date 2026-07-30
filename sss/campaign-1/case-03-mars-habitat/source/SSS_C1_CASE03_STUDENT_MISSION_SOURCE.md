# Mars Habitat - Student Mission Source

**Case:** SSS-C1-CASE03  
**Student identity:** Data Analyst  
**Status:** VALIDATION BUILD  
**Game baseline:** `c6c17be57880b365793fdf99ff4ad09b62ecacce`

## Mission question
How can the habitat receive an adequate total amount of light while the potato plants still fail to form normal green new growth?

## Current runtime data
- Combined PPFD: **280 umol m-2 s-1**, reported as adequate/nominal.
- Primary delivery: **12 m multi-strand full-spectrum silica light pipes** from a surface collector to the habitat.
- Supplemental light: **4000 K white LEDs**, approximately **30% of total PAR**; game text describes red output as weak and deep-red output as minimal.
- Aggregate pipe transmission efficiency: **68%**.
- Surface-collector filter was replaced **47 sols ago**; part number was not recorded.
- Spectral analysis, surface intake versus habitat output: blue 400-500 nm **92% transmission**; green 500-600 nm **88%**; red 600-700 nm **31%**; deep red 700 nm+ **12%**.
- Archive identifies the required filter as **FS-7 FULL SPECTRUM** and the incorrect **BP-4 BLUE PASS** filter as passing blue/green while rejecting most red/deep red.
- New growth is pale yellow to white; older lower leaves retain green; roots are healthy; iron and nitrogen additions did not help.

## Canonical tasks
| No. | Exact task title | Required student action |
|---|---|---|
| 1 | Define the measurement | Explain what PPFD/PAR quantity tells you and what it does not reveal about spectral distribution. |
| 2 | Read the spectral-transmission data | Use the game-provided wavelength-band transmission values to identify the weakest band within 400-700 nm. |
| 3 | Compare quantity and quality | Compare the adequate total PPFD reading with uneven wavelength transmission and reject the low-total-light explanation. |
| 4 | Connect the symptom pattern | Use old-versus-new leaf evidence to identify a failure in new chlorophyll formation. |
| 5 | Select and reject diagnoses | Choose the diagnosis that fits all evidence and reject one tempting alternative. |
| 6 | Model the mechanism | Complete the chain from the wrong collector filter to bleached new growth. |
| 7 | Write the case conclusion | Write a concise Claim-Evidence-Reasoning explanation. |
| 8 | Transfer the analysis | Explain why increasing brightness without correcting spectrum may fail. |
| 9 | Exit ticket | State the first two measurements you would compare in a new lighting failure. |

## Correct diagnosis
The light delivery system is filtering out red wavelengths needed for chlorophyll biosynthesis.

## Science-status boundary
PPFD definitions, wavelength-dependent plant responses, and the light-driven POR reaction are authoritative science. The Mars hardware, filter models, exact transmission percentages, symptom timing, and diagnosis are game-specific controlled content. No unreported points, smooth spectral curve, or universal filter performance is inferred.
