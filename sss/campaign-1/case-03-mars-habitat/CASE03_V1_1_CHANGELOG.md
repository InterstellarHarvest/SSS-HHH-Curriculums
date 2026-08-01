# Case 03 v1.1 approved-stable changelog

## Status

- Release state: `APPROVED_STABLE`
- Artifact policy: HTML only
- Owner browser/physical-print gate: **PASS**
- Approval: Nate / Owner · 2026-07-31 · 100% / Actual Size
- Printer: Not recorded
- Paper: Not recorded
- Successor reason: Accessible CER atomicity and Task 6 phrase-bank correction

## Preserved historical release

Case 03 v1.0 remains the approved historical release. Its master, five role outputs, release manifest, checksum evidence, reports, and owner print record are unchanged. The approved v1.0 master SHA-256 remains `c97a880f0be0c58848c0d8a7394ce75925aff26f3fb542dc4d63cca25a9b6bce`.

## v1.1 corrections

Accessible Task 7 no longer spans pages or uses two partial CER roots. Accessible page 5 contains Task 6, page 6 contains the complete Task 7 Claim/Evidence/Reasoning component in one canonical root, and page 7 contains Tasks 8–9 plus the optional extension. The Accessible role therefore increases from six to seven pages. Student, Teacher, Answer Key, and Grayscale retain their v1.0 page composition.

Task 6 now places a shared `sequence-v1.0` phrase bank directly after the complete five-stage model in Student, Answer Key, Accessible, and Grayscale output. The four phrases are extracted verbatim from controlled Answer Key Stages 2–5 and displayed in the fixed source-stage order 4, 2, 5, 3. Teacher guidance now makes explicit that students sequence the supplied phrases rather than independently generate all mechanism wording.

No instructional science, task title, answer sequence, evidence, response identifier, or assessment intent changed.

## Migration and parity

`validation-artifacts/build_case03_v1_1.py` verifies the approved v1.0 master hash before extracting its worksheet DOM and case CSS, applies the owner-authorized Accessible reflow and Task 6 phrase-bank scaffold, and generates the v1.1 controlled sources, master, five role outputs, package, manifest, and checksums deterministically. The central editor loads the extracted worksheet-only presentation into an open Shadow DOM; neither complete master nor its embedded toolbar/runtime is loaded by the application.

The v1.1 master is the current approved stable Case 03 master and golden Curriculum Editor Phase 1 reference. Automated validation compares all 27 role-profile pages for structure, page assignment, geometry, computed presentation, and rendered pixels, and separately checks current-role export parity, CER containment, phrase-bank parity, and zero overflow.

## Approval

Nate / Owner approved Case 03 v1.1 and Curriculum Editor Phase 1 on 2026-07-31. Browser physical-print review passed at 100% / Actual Size; printer and paper were not recorded. No PDF was required or authorized. The feature branch is ready for merge review, but the embedded editors remain preserved pending additive Case 01/02 migration and Phase 2 cutover.
