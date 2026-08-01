# SSS Campaign 1 Case 03 - Mars Habitat

- Current approved version: v1.1
- Student identity: Data Analyst
- Core science: light spectrum versus total intensity
- Game baseline: `c6c17be57880b365793fdf99ff4ad09b62ecacce`
- Shared editor shell: v1.0
- Artifact policy: HTML_ONLY
- Status: APPROVED STABLE
- Owner browser/physical print gate: PASS
- Approval: Nate / Owner · 2026-07-31 · 100% / Actual Size

Case 03 v1.0 remains the byte-identical approved historical release. Its master hash is `c97a880f0be0c58848c0d8a7394ce75925aff26f3fb542dc4d63cca25a9b6bce`; its five role outputs, release manifest, approval evidence, checksum records, reports, and owner print record are preserved.

Case 03 v1.1 is the current approved stable successor and the central Curriculum Editor Phase 1 golden reference. Accessible Task 7 keeps Claim, Evidence, and Reasoning in one canonical CER root on Accessible page 6. Tasks 8–9 occupy page 7, increasing Accessible from six to seven pages without shrinking accessible text or writing areas. Task 6 includes the approved fixed-order phrase bank. Student, Teacher, Answer Key, and Grayscale retain four, eight, four, and four pages respectively.

The v1.1 build creates six self-contained approved HTML artifacts:

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

See `CASE03_V1_1_CHANGELOG.md`, `CASE03_V1_1_RELEASE_MANIFEST.json`, `reports/CASE03_V1_1_VALIDATION_REPORT.md`, and `published/OWNER_PRINT_BROWSER_CHECKLIST_v1.1.md` for the final approval record. Printer and paper were not recorded. No PDF was required or authorized.
