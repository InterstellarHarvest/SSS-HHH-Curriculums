# Case 03 Runtime Content Audit

**Game commit:** `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`  
**Controlling files:** repository-root `space_sprout_sleuth_data.js` (`id: "mars"`) controls mission text, evidence, numerical values, diagnosis choices, correct diagnosis, and explanation. Repository-root `index.html` is the shared engine that loads and renders the case data.  
**Status:** VERIFIED AGAINST CURRENT MAIN

## Mission problem
Potatoes grow normally for about three weeks; newest leaves then become washed out, followed by top-canopy yellowing and nearly white new growth.

## Evidence channels
Crew, Sensors, Plants, and Logs/Archive. The playable sequence moves from adequate total PAR to wavelength-resolved sensor analysis, plant pigment evidence, and collector-filter maintenance records.

## Exact current values
- 12 m full-spectrum silica light pipe.
- 4000 K white LEDs, approximately 30% of total PAR; red weak, deep red minimal.
- Combined PAR/PPFD: 280 umol m-2 s-1, nominal/adequate.
- Aggregate light-pipe transmission: 68%.
- Collector filter replacement: 47 sols ago; part number not recorded.
- Surface intake to habitat output: blue 92%, green 88%, red 31%, deep red 12% transmission.
- Required filter FS-7 FULL SPECTRUM; incorrect BP-4 BLUE PASS passes blue/green and rejects most red/deep red.
- Environmental context: 20 C, CO2 1200 ppm, UV index 0.1.

## Diagnosis options
Perchlorates; high CO2; Mars-sol photoperiod; correct diagnosis: `The light delivery system is filtering out red wavelengths needed for chlorophyll biosynthesis.`

## Mechanism and sequence
Adequate total PPFD -> spectral analysis shows selective red/deep-red rejection -> maintenance/archive evidence identifies likely wrong collector filter -> plant evidence shows failure concentrated in new pigment formation -> diagnosis.

## Important correction from the first interrupted build
The uploaded local ZIP contained older Case 03 content with 8/12/45/65 loss values and a borosilicate/dust explanation. Current GitHub main at the verified game commit contains 92/88/31/12 transmission values and the wrong-filter mechanism. The validation build uses only current-main content.
