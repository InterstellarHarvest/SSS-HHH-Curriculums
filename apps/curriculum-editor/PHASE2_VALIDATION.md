# Curriculum Editor Phase 2 Validation Handoff

**Status:** VALIDATION_BUILD

**Owner gate:** OWNER_GATE_OPEN

**Physical-print gate:** PHYSICAL_PRINT_GATE_OPEN

This branch additively migrates the owner-authorized current maintained HTML for Case 01 v1.1 and Case 02 v1.0 into the Phase 1 central editor. It does not create a curriculum release, accept Phase 2, perform cutover, remove embedded editors, clean up history, or create/modify PDFs.

## Golden baselines and packages

| Case | Golden maintained master SHA-256 | Package | Role pages |
|---|---|---|---|
| Case 01 v1.1 | `737239b53ae5af3f25cbaf037d0c9882f50d9e7e8d26b3d03408e469ced6b56f` | `sss/campaign-1/case-01-iss-greenhouse/source/editor-package/case-package.v1.1.json` | Student 3 · Teacher 7 · Answer 3 · Accessible 6 · Student Grayscale 3 |
| Case 02 v1.0 | `4e5d03a62cba494ae09604194f69578b4c4bcceeeca1f9d53d818109e132fd0d` | `sss/campaign-1/case-02-lunar-greenhouse/source/editor-package/case-package.v1.0.json` | Student 3 · Teacher 7 · Answer 3 · Accessible 5 · Student Grayscale 3 |

The generic deterministic builder is `shared/implementation/build_phase2_case_packages.py`. It fails closed on either golden, task registry, or controlled-source hash change and emits 10 deterministic files. The package schema records the maintained golden, pre-maintenance historical hash, reconciliation record, maintenance revision, owner authorization, and open gates.

## Automated results

| Validation | Case 01 | Case 02 | Combined |
|---|---:|---:|---:|
| Structure | 22/22 | 21/21 | 43/43 |
| Task/page assignment | 22/22 | 21/21 | 43/43 |
| Geometry (0.25 px) | 1758/1758 | 1800/1800 | 3558/3558 |
| Computed presentation | 6988/6988 | 7158/7158 | 14146/14146 |
| Rendered pixels (accepted Phase 1 tolerance) | 22/22 | 21/21 | 43/43 |
| Component integrity/atomicity | 219/219 | 224/224 | 443/443 |
| Current maintained role HTML | 5/5 | 5/5 | 10/10 |
| Current-role exports | 5/5 | 5/5 | 10/10 |
| Complete portable export pages | 19/19 | 18/18 | 37/37 |
| Role profiles reporting Pages fit | 5/5 | 5/5 | 10/10 |

The expanded browser/cross-case suite passes 267/267 assertions, including every accepted Phase 1 browser assertion and all 15 isolated print profiles. The Phase 2 static suite passes 69/69; the nested accepted Phase 1 static suite passes 103/103. Reconciliation passes 121/121, deterministic extraction 10/10, and the protected ledger 116/116. Both master and editor browser logs contain zero JavaScript errors.

The clean-print DOM assertions require exact counts for Case 01 (3/7/3/6/3), Case 02 (3/7/3/5/3), and Case 03 (4/8/4/7/4), in Student/Teacher/Answer Key/Accessible/Student Grayscale order. They also require one intact first-page title/institutional identity, intact continuation identity on every later page, no blank printable fragments, no application chrome or authoring state, preserved current edits/responses, unchanged page geometry, and no Page shadow.

## Protected history

`shared/implementation/phase2-protected-artifacts.v1.json` freezes 110 Case 01/02 artifacts at reconciliation commit `63364fb4e6bc6f7639b861d9ae570f49e5d224ff`: 5 masters, 10 current role HTML files, 23 controlled sources/assets, 3 manifests, 49 validation/owner/master/reconciliation records, and 20 historical PDFs. The validator also rejects undeclared/new PDFs. All protected bytes and all PDFs remain unchanged; no PDF was generated.

Case 03 v1.0/v1.1 protection and Phase 1 behavior remain covered by the accepted 103-assertion static suite, the expanded browser suite, and the unchanged Phase 1 parity artifacts.

## Owner review materials

- Case 01 screenshots/contact sheets: `tests/screenshots/parity-phase2/sss-c1-case01/`
- Case 01 parity JSON/report/checklist: `sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/phase2/`
- Case 02 screenshots/contact sheets: `tests/screenshots/parity-phase2/sss-c1-case02/`
- Case 02 parity JSON/report/checklist: `sss/campaign-1/case-02-lunar-greenhouse/validation-artifacts/phase2/`
- Binding-rule audit: `tests/PHASE2_BINDING_RULE_AUDIT.md`

The owner review must cover both the current maintained standalone HTML and its exact central-editor rendering. For every role, use the clean Print / Save PDF path and confirm browser print preview at 100% / Actual Size, exact expected page count, no blank fragments or application chrome, intact first-page and continuation identity, unchanged geometry/content pagination, and no Page shadow. Then complete browser physical printing at 100% / Actual Size. Until the owner records that decision, current maintained Case 01/02 standalone artifacts remain canonical and the central editor remains a validation representation.

## Reproduction

```bash
python3 shared/validation/validate_phase2_reconciliation.py
python3 shared/validation/validate_phase2_protected_inventory.py
python3 shared/implementation/build_phase2_case_packages.py --check
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/validate_phase2_static.py
python3 apps/curriculum-editor/tests/run_browser_tests.py
/private/tmp/curriculum-editor-parity-venv/bin/python3 apps/curriculum-editor/tests/validate_phase2_parity.py
```
