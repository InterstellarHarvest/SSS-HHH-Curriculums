# Case 01 v1.0 — Validation Artifacts

Post-edit layout/publishing regression evidence for `master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`.

**Context:** The original v1.0 validation (see `../master/SSS_C1_CASE01_V1_VALIDATION_REPORT.md`) referenced a `validation-artifacts/validation-results.json` and a Playwright script that were never committed. After the game-content audit applied four small text corrections to the packet, this folder was created to store the **post-edit** rerun so the packet, the audit report, the validation report, and the checksum all describe the same final build.

## Contents

| File | What it is |
|---|---|
| `revalidate_packet.mjs` | Repeatable headless-Chromium harness. Drives the packet's own role `<select>`, grayscale/print-preview toggles, and overflow logic; measures per-role page counts and overflow; checks fill/persistence across a real reload; generates the Teacher PDF. |
| `revalidation-results.json` | Machine-readable output of the rerun (all roles PASS, zero overflow, no JS errors). |
| `teacher_v1.0_revalidated.pdf` | Teacher role rendered to PDF post-edit — 7 pages. Regression evidence only, **not** a published deliverable. |
| `CHECKSUMS.txt` | SHA-256 of the edited `SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html` under test. |

## How to rerun

```
NODE=~/.nvm/versions/node/v20.20.2/bin/node
"$NODE" revalidate_packet.mjs \
  "../master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html" \
  "$(pwd)"
```

## Result summary (2026-07-23)

Student 3 · Teacher 7 · Answer Key 3 · Accessible 6 · All 19 pages — every role zero overflow, grayscale and print preview clean, persistence restores after reload, Teacher PDF 7 pages, no console/page errors. Matches the pre-edit baseline; the two added Teacher notes caused no overflow or pagination change.

These are review evidence, not permanent curriculum-source files, unless the repository adopts a validation-artifact policy.
