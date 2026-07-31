# SSS Campaign 1 Case 03 - Mars Habitat

- Curriculum version: v1.0
- Student identity: Data Analyst
- Core science: light spectrum versus total intensity
- Game baseline: `c6c17be57880b365793fdf99ff4ad09b62ecacce`
- Shared editor shell: v1.0
- Artifact policy: HTML_ONLY
- Status: APPROVED STABLE
- Approval date: 2026-07-31
- Owner physical print test: PASS — Nate / Owner

Case 03 is assembled from `shared/implementation/editor-shell/v1.0/` plus its case configuration, CSS, and instructional content. The shared shell uses the approved Case 02 editable master as the literal toolbar/editor reference and the approved Case 01/02 printable worksheet identity. The build creates exactly six canonical production artifacts:

- one self-contained portable editable-master HTML;
- independent Student, Teacher, Answer Key, Accessible, and Grayscale HTML outputs.

Do not hand-edit generated HTML. Do not generate or store PDFs during routine production.

```bash
python3 validation-artifacts/build_case03_html.py
python3 shared/validation/validate_editor_shell_contract.py \
  --config sss/campaign-1/case-03-mars-habitat/source/editor/case03-editor-config.json \
  --master sss/campaign-1/case-03-mars-habitat/master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html
python3 validation-artifacts/validate_case03_editor_shell.py
python3 validation-artifacts/render_case03_browser_review.py
python3 validation-artifacts/validate_case03_v1.py
```

The browser action remains labeled **Print / Save PDF**. It is an optional end-user convenience, not a production artifact pipeline. Browser PDF export does not guarantee an accessible PDF; any PDF distributed, published, or archived requires separate accessibility verification.

The canonical SAA expansion is **Solar Agricultural Agency**. This is a follow-up correction after initial Case 03 commit `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`.

Case 03 completed every HTML-only automated, rendered-browser, and owner physical-print release gate and was approved stable on 2026-07-31. Printer and paper details were not recorded.
