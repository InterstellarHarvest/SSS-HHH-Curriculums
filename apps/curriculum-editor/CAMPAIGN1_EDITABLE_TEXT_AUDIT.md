# Campaign 1 editable-text audit

Scope: released SSS Campaign 1 Cases 01–07 at baseline `2a70afb9c3897c9fe43bda3109cfb1103825df7f`. The audit changes no classroom wording, package source, package hash, lifecycle record, layout, page count, or response-height default.

## Root cause

`content.html` packages use `data-editable` plus a unique `data-persist-id` to register editable instructional text. Before this correction, `editor-app.js` and `portable-runtime.js` discovered only `[data-editable]`; package loading, Shadow DOM mounting, role switching, Grayscale, persistence, and export preserved registered targets correctly. The later package builds did not register equivalent semantic text consistently:

- Case 05: 11 Student registrations and none in Teacher, Answer Key, or Accessible.
- Case 06: one Student registration and none in the other roles.
- Case 07: one Student and one Accessible registration; none in Teacher or Answer Key.

Case 05 therefore follows the later sparse-registration pattern. The failure is not a schema-version, Shadow DOM, role-selection, hash, lifecycle, or response-height defect. Runtime evidence is covered by the 28-state browser matrix in `tests/browser-harness.html`.

## Before and after

Cells show registered visible editable-text targets as `before → after`. Counts document the reproduced behavior; regression assertions validate semantic categories and protected boundaries rather than using counts as the contract.

| Case | Student | Teacher | Answer Key | Accessible |
|---|---:|---:|---:|---:|
| 01 | 62 → 58 | 233 → 242 | 43 → 43 | 64 → 61 |
| 02 | 3 → 40 | 0 → 149 | 0 → 40 | 0 → 34 |
| 03 | 42 → 44 | 137 → 137 | 18 → 23 | 32 → 39 |
| 04 | 10 → 39 | 1 → 146 | 0 → 29 | 6 → 27 |
| 05 | 11 → 50 | 0 → 175 | 0 → 46 | 0 → 27 |
| 06 | 1 → 57 | 0 → 186 | 0 → 69 | 0 → 42 |
| 07 | 1 → 88 | 0 → 266 | 0 → 67 | 1 → 60 |

The decreases in three Case 01/03 learner cells are intentional: registrations that enclosed live response controls are no longer activated as editable-text parents, keeping response entry and response-height authoring structurally separate.

## Contract

Editable semantic categories are task prompts/directions, instructional paragraphs, lists and headings, instructional table copy, science notes, model-answer blocks, and figure captions or extended descriptions. Existing safe explicit registrations remain supported.

Protected categories are SAA and document identity, title/continuation headers, role names, Name/Date/Period structure, generated task identity, lifecycle or structural metadata, page numbers and footers, response labels and response controls, response-height controls, hidden captions, source URLs/reference ledgers, and decorative or technical model labels not explicitly registered.

Generated registrations are deterministic per page, receive the existing focus/outline affordance, use the existing case/version persistence namespace, and are serialized into editable copies. Grayscale changes presentation only. Stored and portable instructional HTML use the same allowlist sanitizer: safe emphasis/list markup and safe HTTP(S)/mailto links are retained; scripts, styles, embedded media, forms, event-handler attributes, and unsafe URL schemes are removed.

## Regression evidence

The browser harness covers every Case 01–07 role, semantic discovery, protected boundaries, focus and keyboard access, Grayscale invariance, response separation, response-height controls, reset/reload/role-switch persistence, role and portable exports, print isolation, unsafe HTML, fixed Letter geometry, overflow, and page counts. Existing static, canonical, layout, authoring-service, PDF, hash, accessibility, and content-regression validators remain authoritative.
