# SSS Campaign 1 Case 03 - Mars Habitat

- Curriculum version: v1.0
- Student identity: Data Analyst
- Core science: light spectrum versus total intensity
- Game baseline: `c6c17be57880b365793fdf99ff4ad09b62ecacce`
- Curriculum baseline: `e524d333f28a1515571f038e3ed494d87aa812d3`
- Printable Page Identity: v1.0.4
- Balanced Page Fill and Vertical Rhythm: v1.0.2
- Shared editor shell: v1.0
- Status: VALIDATION BUILD
- Automated validation: PASS
- Owner physical 100%-scale print test: OPEN

The portable editable master is assembled from `shared/implementation/editor-shell/v1.0/` plus `source/editor/case03-editor-config.json`, `case03.css`, and `case03-content.html`. Run `python validation-artifacts/build_case03_html.py` to rebuild the master and five independent role HTML outputs. Do not hand-edit generated HTML.

This editor-shell maintenance pass is HTML-only. It does not regenerate the five existing PDFs, change their page counts, or close the owner physical-print gate.

Contract validation:

```bash
python shared/validation/validate_editor_shell_contract.py \
  --config sss/campaign-1/case-03-mars-habitat/source/editor/case03-editor-config.json \
  --master sss/campaign-1/case-03-mars-habitat/master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html
python sss/campaign-1/case-03-mars-habitat/validation-artifacts/validate_case03_editor_shell.py
```

## Institutional identity
The canonical SAA expansion for this validation build is **Solar Agricultural Agency** under the owner-directed follow-up correction after initial Case 03 commit `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`.
