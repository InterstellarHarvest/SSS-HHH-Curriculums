# SSS Campaign 1 Case 03 - Mars Habitat

- Current validation version: v1.1
- Student identity: Data Analyst
- Core science: light spectrum versus total intensity
- Game baseline: `c6c17be57880b365793fdf99ff4ad09b62ecacce`
- Shared editor shell: v1.0
- Artifact policy: HTML_ONLY
- Status: VALIDATION BUILD
- Owner browser/physical print gate: OPEN

Case 03 v1.0 remains the byte-identical approved historical release. Its master hash is `c97a880f0be0c58848c0d8a7394ce75925aff26f3fb542dc4d63cca25a9b6bce`; its five role outputs, release manifest, approval evidence, checksum records, reports, and owner print record are preserved.

Case 03 v1.1 is a corrected successor validation build. Accessible Task 7 now keeps Claim, Evidence, and Reasoning in one canonical CER root on Accessible page 6. Tasks 8–9 move to page 7, increasing Accessible from six to seven pages without shrinking accessible text or writing areas. Student, Teacher, Answer Key, and Grayscale page composition is unchanged.

The v1.1 build creates six self-contained HTML validation artifacts:

- one self-contained portable editable-master HTML;
- independent Student, Teacher, Answer Key, Accessible, and Grayscale HTML outputs.

Do not hand-edit generated HTML. Do not generate or store PDFs.

```bash
python3 validation-artifacts/build_case03_v1_1.py --check
python3 ../../../apps/curriculum-editor/tests/validate_static.py
python3 ../../../apps/curriculum-editor/tests/run_browser_tests.py
python3 ../../../apps/curriculum-editor/tests/validate_v1_1_parity.py
```

The browser action remains labeled **Print / Save PDF**. It is an optional end-user convenience, not a production artifact pipeline. Browser PDF export does not guarantee an accessible PDF; any PDF distributed, published, or archived requires separate accessibility verification.

The canonical SAA expansion is **Solar Agricultural Agency**. This is a follow-up correction after initial Case 03 commit `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`.

See `CASE03_V1_1_CHANGELOG.md` and `CASE03_V1_1_RELEASE_MANIFEST.json` for the successor record. v1.1 must not be marked approved stable until owner browser and physical-print review passes.
