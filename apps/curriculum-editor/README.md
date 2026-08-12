# SSS/HHH Curriculum Editor

The repository-local Curriculum Editor is the canonical interface for the thirteen released SSS cases: Campaign 1 Cases 01–07 and Campaign 2 Cases 01–06. The editor discovers each case through the v2 registry, loads the native `source/case-package.json`, verifies package-controlled source hashes, and mounts worksheet-only content in an open Shadow DOM.

SSS Campaign 1 contains seven curriculum-sequenced cases. Case 06 is **First Contact Protocol** (runtime `alien1`), and Case 07 is **The Gift** (runtime `alien2`; former source-development label `Case 6b`) and the approved Campaign 1 culmination. Both first-contact cases entered the editor only as complete canonical packages.

SSS Campaign 2 contains six cases, all released at v1.1 as corrective reissues of their approved v1.0 releases. Case 03, **The Wrong Color of Light** (runtime `wrong_color_light`), was produced first and keeps its runtime case number.

Status: all thirteen registered SSS cases are `APPROVED_STABLE`. The library is campaign-scoped, so the Case menu lists exactly the cases registered under the selected campaign.

## Launch

Double-click **`Open Curriculum Editor.command`** at the repository root. It starts the local server (unless a Curriculum Editor is already serving), opens <http://127.0.0.1:8000/apps/curriculum-editor/> in your default browser, and stays responsible for the server it started. When the editor tab closes, the server notices the missing heartbeat and exits on its own, so nothing needs to be stopped manually. If port 8000 is occupied by something that is not the Curriculum Editor, the launcher reports that and leaves the other program untouched (`CURRICULUM_EDITOR_PORT` selects a different port).

The direct development command remains available as a fallback:

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/>. `file://` is unsupported because package resources are fetched independently. A directly launched server never exits on its own; stop it with Ctrl-C or the editor's Stop control.

### Server heartbeat, Restart, and Stop

While the editor page is open it posts a tiny heartbeat (an in-memory timestamp update only) to loopback `POST /__server/heartbeat` about every 5 seconds. A launcher-started server (`--auto-shutdown`) shuts down cleanly roughly 15 seconds after heartbeats stop — page reloads reconnect well inside that window — and a hidden background tab is given a longer allowance because browsers throttle its timers. A freshly launched server waits about 60 seconds for the first editor tab before giving up and exiting.

The Editor Status area shows a subordinate `Server` row with the connection state and two small controls. **Restart** cleanly restarts the same server process (the process re-executes itself in place, so the launcher keeps ownership and no other process is ever touched) and the page reconnects automatically once `/__health` answers again. **Stop** shuts the server down intentionally; relaunch with the `.command` file. If the connection drops unexpectedly the row shows a reconnecting state and retries without reloading the worksheet or discarding local responses. The row never appears in print output, editable copies, or worksheet exports, and it stays hidden entirely when the page is not served by a lifecycle-aware Curriculum Editor server. All `/__server/*` endpoints are loopback-only under the same request protection as the authoring endpoints.

## Roles and Grayscale

The only document roles are Student, Teacher, Answer Key, and Accessible. The library rail and portable editable-copy selector expose those four roles; the portable selector also includes an All Pages editing view.

Grayscale is an independent Boolean presentation toggle. It changes presentation tokens for the selected role without changing that role’s identity, page count, content, response geometry, semantic markup, or autosave namespace. Printing and worksheet export apply the current Grayscale state while retaining the role’s normal filename and identity.

Accessible editions load the shared `accessible-edition.css` production layer after case presentation styles. That layer supplies content-driven one-to-three-task pagination primitives, Accessible-specific response sizing, and the dedicated canonical CER page used by the editor, editable copies, worksheet exports, and print output. Accessible page counts are intentionally flexible; the other three roles retain their package-locked counts and geometry.

## Editing and exports

- **Edit Text** applies the central `instructional-text-v1` semantic contract to registered prompts, directions, instructional blocks, lists, headings, tables, model answers, and caption/description text in every role. Identity, pagination, response controls, response-height controls, source references, and structural/technical labels remain protected. Runtime-generated registrations are deterministic and travel with editable copies; approved package sources and hashes do not change.
- **Download Editable Copy** creates a self-contained HTML copy with all four roles, the editing toolbar, current edits/responses, and the current Grayscale state.
- **Download Worksheet** creates a self-contained HTML worksheet containing only the selected role, current edits/responses, and current Grayscale state. It has no toolbar or application chrome.
- **Print / Save PDF** builds a temporary same-origin print document for the selected role, waits for fonts and images, removes application chrome and page shadows, and opens the browser print dialog.
- **Clear Responses** affects only the selected role’s response fields.
- **Reset This Case** affects only the loaded case/version recovery state.

Generated HTML and PDFs are not written into the repository. A browser-created PDF requires separate accessibility verification before distribution.

## Source and recovery model

The package’s `content.html`, `presentation.css`, `task-registry.js`, `layout-overrides.json`, and referenced assets are canonical. The central shell applies `protected-printable-components.css` after case presentation so identification rows, title and continuation headers, institutional identity, footers, and CER keep one printable contract. New packages opt into the shared component layer and may not redefine protected selectors. Complete editable documents and role documents are assembled on demand. Historical generated artifacts, when they existed, remain recoverable through `history/release-vX.json`; native-only releases record that no former generated artifacts exist.

## Student and Accessible vertical response-area authoring

Each SSS or HHH package declares `source/layout-overrides.json` using `layout-overrides.schema.v1.json`. The original top-level `areas`, `lockedAreas`, and `overrides` keys remain the canonical Accessible registry. The `student` member uses the same three-part contract for Student. Every response in both editions must be explicitly allowlisted or locked. Validation rejects omissions, duplicates, role/page/task drift, Student compact-table eligibility, CER eligibility, and protected short/status/classification/criterion/constraint fields. Both sparse override maps contain only owner-applied heights; an empty map changes no worksheet geometry.

In Student or Accessible Edit Text mode, eligible fields receive vertical-only pointer and keyboard handles. Values snap to 4px, respect declared bounds, and receive live page-fit/footer safety validation. Minima preserve each field's released usable baseline on the 4px grid (28px for two released 31px fields, 32px for ordinary multi-line fields, and 64px only where the released design/plan geometry supports it). The declared 900px ceiling is generous, while the live dynamic maximum and final overflow validation enforce the actual page-safe limit. Pending changes are browser drafts isolated by repository/worktree identity, case, edition, and the content/presentation/layout source hashes. Undo, redo, Reset Area, Reset Page, stale-draft inspect/export/discard, and **Export Layout Changes** do not write repository files. Normal editable-copy, worksheet, print, and PDF pathways omit authoring controls and unapproved draft heights.

The layout drawer always states the current permanence level. A resize is labeled **Browser draft** until Apply to Source succeeds; ordinary exports ignore it. After a successful canonical reload, the drawer reports **Written to source** and reminds the owner that a Git commit and push are still required. Pending-table response labels jump to and briefly highlight the exact editable area. When page-fit validation reports one or more affected pages, both page-fit statuses become keyboard-operable jump controls for the first affected page. Jump highlights are editor-only and are removed from every export path.

The editor remembers the selected case, edition, existing presentation controls, and the Student/Accessible layout-drawer expansion preference. **Edit Text is intentionally never persisted**: a normal reload or case change starts with authoring mode off. The controlled reload immediately following Apply to Source keeps Edit Text open long enough to show the written-to-source result and any remaining browser draft.

**Apply to Source** shows the exact selected changes and requires confirmation. The loopback service accepts only registered Student or Accessible allowlist IDs with matching source-hash preconditions. It independently revalidates role, case, page, task, locator uniqueness, CER ancestry, bounds, and source hashes. It rejects Teacher/Answer Key targets, wrong-role IDs, locked or unknown IDs, unexpected fields, and all client filesystem paths. It atomically writes only the selected case's sparse layout file and required package hash, runs focused validation, and rolls both files back on failure. Successful changes intentionally remain uncommitted for owner inspection.

### Owner Apply-to-Source workflow

1. Open the intended case and choose Student or Accessible, enable **Edit Text**, and resize one eligible area.
2. Inspect **Pending Layout Changes**, including page/task identity, source and proposed heights, and page/footer validation.
3. Select only the approved valid change, choose **Apply to Source**, inspect the exact confirmation list, and confirm.
4. Allow the editor to reload; confirm the approved height is now canonical and no longer appears as a pending browser draft.
5. Run `git diff --check` and inspect `git diff -- source/layout-overrides.json source/case-package.json`; only the selected case's sparse override and layout-override package hash may change.
6. Run the validation commands below and visually review the affected page at normal and 75% preview scale, including worksheet export and Print / Save PDF.
7. Commit the two intentional source changes only after review passes.
8. Integrate the reviewed commit and synchronize `main` through the repository's normal release workflow.

## Validation

```bash
python3 shared/validation/validate_canonical_case_structure.py
python3 shared/validation/validate_release_integrity.py
python3 shared/validation/validate_layout_overrides.py
python3 apps/curriculum-editor/tests/validate_static.py
python3 apps/curriculum-editor/tests/test_authoring_service.py
python3 apps/curriculum-editor/tests/test_server_lifecycle.py
python3 apps/curriculum-editor/tests/run_browser_tests.py
python3 apps/curriculum-editor/tests/run_pdf_tests.py
```

The browser suite covers all registered case/role/presentation states, Student and Accessible resize controls and draft isolation, 75%-scale pointer conversion, role and case switching, Grayscale persistence, response/edit isolation, editable-copy and worksheet exports, isolated print documents, keyboard access, announcements, page fit, protected-component and CER geometry, Accessible task density and overlap checks, identities, and JavaScript errors. Static validation rejects protected selectors in new case presentation stylesheets. Screenshots are temporary; reproduce visual evidence with `run_browser_tests.py`.

The server binds to `127.0.0.1` by default. Static reads remain repository-root scoped; its authoring endpoints are loopback-only and the apply endpoint has the strict contract described above. Packages are trusted repository content; downloaded editable HTML contains JavaScript and should be treated accordingly.
