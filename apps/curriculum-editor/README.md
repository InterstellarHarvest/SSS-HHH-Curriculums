# SSS/HHH Curriculum Editor — Phase 1

This repository-local browser application loads the current Case 03 editor package and combines it with shared editor-shell sources. It does not open, iframe, rewrite, or execute the approved Case 03 master.

## Launch

From the repository root:

```bash
python3 apps/curriculum-editor/serve.py
```

Open <http://127.0.0.1:8000/apps/curriculum-editor/>. Stop the server with `Ctrl-C`.

The server is required. `file://` is not a supported production path because the application fetches the registry, package, content, shared shell, styles, icons, and task registry as separate repository resources.

## Phase 1 workflow

1. Choose Curriculum → Campaign → Case → Role in the library rail. The rail contains the four instructional roles: Student, Teacher, Answer Key, and Accessible. Phase 1 exposes only the current registered Case 03 package.
2. Use **Fill responses** for response fields or **Edit text** for explicitly marked instructional nodes.
3. Changes autosave to local browser storage under the package's unique case/version/document key.
4. Use **Download Current HTML** for a self-contained editable worksheet containing every role.
5. Use **Download Current Role** for a self-contained file containing only the selected role.

Grayscale is a toolbar presentation modifier, not a library role. It remains on when switching among instructional roles and never changes the selected role or page set. Student with Grayscale enabled maps to the canonical Grayscale Mission output name. Other roles retain their own output identity while exporting with grayscale presentation. Grayscale uses token overrides and keeps `Student Mission` identity in the canonical Student Grayscale footer.

The central toolbar omits the duplicate Role selector because the library rail is authoritative. A complete portable HTML export restores the shared-shell Role selector because that file has no library rail.

**Clear Current Role** removes response and note fields only from the selected source role. **Reset Source** clears the package autosave, restores package content, and restores toolbar defaults. In a downloaded complete HTML file, Reset Source preserves the instructional edits embedded in that file and clears response recovery work, matching shared-shell v1.0 behavior.

## Portable output and printing

Both download actions inline the shared CSS, Case 03 CSS, Phosphor icon sprite, page content, figures, insignia, current edits, current responses, configuration, and portable runtime. They do not overwrite repository files.

The **Print / Save PDF** button invokes the browser print dialog. Browser PDF export does not guarantee PDF accessibility. Any PDF distributed, published, or archived requires separate accessibility verification. This application does not create, validate, preflight, checksum, or store PDFs.

## Validation

Static/package validation requires Python and Beautiful Soup 4:

```bash
python3 apps/curriculum-editor/tests/validate_static.py
```

Browser validation uses the installed Google Chrome executable directly and creates only temporary profiles/screenshots:

```bash
python3 apps/curriculum-editor/tests/run_browser_tests.py
```

To use a different Chrome-compatible executable:

```bash
python3 apps/curriculum-editor/tests/run_browser_tests.py --chrome /path/to/chrome
```

The static suite validates registry/package schemas, references, negative failure modes, task and component contracts, accessibility structure, release hashes, and the no-PDF rule. The browser suite validates controls, roles, page counts, editing, autosave/reload, role isolation, layout controls, print-preview events, zero overflow, portable serialization, Reset Source, current-role export, and browser rendering.

The current owner-review capture is [curriculum-editor-wide-desktop.png](tests/screenshots/curriculum-editor-wide-desktop.png) at 1440×1200.

## Security and local-file assumptions

- The server binds to `127.0.0.1` by default and serves repository files read-only through Python's static handler. Do not bind it to an external interface on an untrusted network.
- Case packages are trusted repository code/content. The app rejects scripts, styles, links, and iframes inside instructional content fragments, but package CSS and the portable runtime are still executable presentation assets controlled by repository owners.
- Local storage is recovery state, not a durable database or synchronization service. Downloaded HTML is the portable handoff format.
- Downloaded HTML contains JavaScript for local editing and printing. Treat customized files from unknown sources as untrusted files.
- No authentication, cloud service, backend database, or external runtime API is used.

## Known Phase 1 limitations

- Only the current registered Case 03 version is editor-compatible.
- Historical-version browsing and a prominent version selector are intentionally absent.
- Case 01 and Case 02 remain on their approved historical master/output implementations.
- Autosave is browser-profile and origin specific; it does not synchronize between devices or browsers.
- Browser print behavior and physical results remain browser/driver dependent and require owner review at 100% / Actual Size.
- HTML accessibility is validated; manually created PDFs require their own accessibility review.

See [CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md](../../shared/implementation/CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md) for the contract, load sequence, accessibility model, and Phase 2 migration plan.
