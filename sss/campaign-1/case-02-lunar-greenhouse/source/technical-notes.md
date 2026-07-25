# Technical Notes and Gameplay Fallback — Lunar Greenhouse

**Status:** VALIDATION BUILD

## Compatibility baseline

- Game repository: `InterstellarHarvest/Space-Sprout-Sleuth`
- Compatible game commit: `2a6e8a7bb75c8c96f26f9ebfe7523668107ab712`
- Runtime file: top-level `space_sprout_sleuth_data.js`
- Runtime object: `id: "lunar"`
- Engine entry point: top-level `index.html`

## Purposeful route

1. **Crew:** `start → problem_main`
2. **Sensors:** `start → airflow`
3. **Plants:** `start → flowers → pollen_close`
4. **Logs:** `start → crop_protocols`

Optional mechanism checks include the hand/mechanical-pollination records and the gated stem-shaking interaction.

## Evidence-summary fallback

Use this briefing if the game is unavailable or a student cannot complete navigation. Do not reveal which diagnosis is correct until the student has processed the evidence.

### Case briefing

A sealed lunar greenhouse contains vigorous cherry tomato plants. The plants have healthy roots, stems, leaves, and many normal-looking flowers. After three weeks, no fruit has formed, and older flowers drop.

### Evidence A — Crew observation

The same cultivar fruits reliably in other controlled environments. In this greenhouse, flowers open on schedule, remain for several days, then drop without the ovary swelling.

### Evidence B — Sensor report

Water, nutrients, temperature, humidity, carbon dioxide, and lighting are reported as suitable for plant growth. Air movement is nearly absent. No dedicated circulation fans are installed.

### Evidence C — Plant examination

Flowers contain abundant, apparently viable pollen. Pollen remains undisturbed on the anthers. Receptive stigmas appear clean. No insects are present. Gently agitating a flower releases a visible cloud of pollen.

### Evidence D — Design record

The crop-management plan lists pollination as “to be determined.” No animal, manual, or mechanical pollination method was installed or scheduled.

### Diagnosis options

- Lunar regolith is toxic to fruit development.
- The light spectrum lacks ultraviolet light needed for fruiting.
- No effective pollen release and transfer is occurring.
- Carbon dioxide is too high for tomatoes.

Students complete the standard Tasks 3–9 with this evidence. The academic target and rubric remain unchanged.

## Browser and data behavior

The editable master stores changes in browser local storage only. It does not upload student data. Teachers should use Download Current HTML or Print / Save PDF before clearing browser data. The Reset Source control deletes local packet state and restores the original validation build.

## Accessibility

- Use the Accessible role for larger type, linearized process modeling, and expanded response areas.
- The original process schematic has a complete text equivalent.
- All controls and response fields have programmatic labels and keyboard focus.
- Role switching must not clear responses or reset margin/settings state.

## Production clarifications from owner review

- Vocabulary lists are alphabetized rather than arranged in discovery or process order.
- A word bank used to fill a sequence is deliberately shuffled; it must not reveal the correct sequence.
- Student and Accessible directions do not discuss whether a response is graded for correctness. Assessment handling belongs in Teacher materials.
- Accessible pages use continuous task flow. Related tasks share a page when the larger type and response areas still fit without overflow; a task is not forced onto its own page merely because it is numbered separately.

## Science qualification

The game contains case-specific airflow and vibration numbers. They are preserved in the runtime audit but intentionally omitted from the Student model and design criteria because they are not universal thresholds. Teachers should assess mechanism-based design, not recall of those numbers.

## Shared v1.0.2 production clarification

The Case 02 ordering and pagination corrections are no longer case-only conventions. They are governed project-wide by `shared/visual-style-guide/amendments/CONTENT_ORDERING_AND_ACCESSIBLE_FLOW_v1.0.2.md` and are listed as controlling in Curriculum Bible v1.3. Future cases must preserve alphabetical vocabulary, fixed shuffled sequence banks, nonredundant directions, Teacher-only grading-policy notes, and continuous-flow Accessible pagination.

## Header parity contract

Case 02 uses the approved Case 01 v1.0 Mission Title Block and continuation-header anatomy across all roles. The prominent title displays `CASE 02 · LUNAR GREENHOUSE`; `SSS-C1-CASE02`, curriculum version, game baseline, and provenance remain in metadata and footers. Continuation pages use the institutional line plus a page-specific title rather than repeating the generic case name in a split banner.

The controlling shared rule is `MISSION_TITLE_AND_CONTINUATION_HEADER_PARITY_v1.0.3.md`.

## v1.1 universal printable page identity

The current master is `SSS_C1_CASE02_EDITABLE_MASTER_v1.1.html`. The v1.0 master remains unchanged for provenance.

- First pages use the left accent rail, title/location copy on the left, and insignia/institution/role block on the right.
- Continuation pages use the case title and generic role-plus-Continued label on the left and the insignia/institution on the right.
- Printable footers contain only the document role and `N of total`.
- Production status, version, baseline, date, and document code are metadata-only.
- Routine test PDFs are temporary and are not stored in `published/`.
