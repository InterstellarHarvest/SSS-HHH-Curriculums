# Case 03 v1.1 validation-build changelog

## Status

- Release state: `VALIDATION_BUILD`
- Artifact policy: HTML only
- Owner browser/physical-print gate: **OPEN**
- Successor reason: Accessible CER atomicity correction

## Preserved historical release

Case 03 v1.0 remains the approved historical release. Its master, five role outputs, release manifest, checksum evidence, reports, and owner print record are unchanged. The approved v1.0 master SHA-256 remains `c97a880f0be0c58848c0d8a7394ce75925aff26f3fb542dc4d63cca25a9b6bce`.

## v1.1 correction

Accessible Task 7 no longer spans pages or uses two partial CER roots. Accessible page 5 contains Task 6, page 6 contains the complete Task 7 Claim/Evidence/Reasoning component in one canonical root, and page 7 contains Tasks 8–9 plus the optional extension. The Accessible role therefore increases from six to seven pages. Student, Teacher, Answer Key, and Grayscale retain their v1.0 page composition.

No instructional science, task title, answer, evidence, response identifier, or assessment intent changed.

## Migration and parity

`validation-artifacts/build_case03_v1_1.py` verifies the approved v1.0 master hash before extracting its worksheet DOM and case CSS, applies only the owner-authorized Accessible reflow, and generates the v1.1 controlled sources, master, five role outputs, package, manifest, and checksums deterministically. The central editor loads the extracted worksheet-only presentation into an open Shadow DOM; neither complete master nor its embedded toolbar/runtime is loaded by the application.

The v1.1 master is the golden migration reference. Automated validation compares all 27 role-profile pages for structure, page assignment, geometry, computed presentation, and rendered pixels, and separately checks current-role export parity and CER containment. Owner approval remains required before v1.1 can become approved stable.
