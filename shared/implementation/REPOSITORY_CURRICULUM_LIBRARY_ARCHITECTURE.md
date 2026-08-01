# Repository Curriculum Library Architecture

**Cutover status:** APPROVED · OWNER REVIEW PASS · READY TO MERGE

## Current production architecture

```text
central Curriculum Editor
+ shared canonical editor shell
+ registered current case package
→ customized portable complete HTML
→ customized current-role HTML
→ clean isolated-role browser printing
```

For SSS Campaign 1 Cases 01–03, the central Curriculum Editor is the canonical active interface and each registered current package is the canonical active editable production source. Launch with `python3 apps/curriculum-editor/serve.py`, then open <http://127.0.0.1:8000/apps/curriculum-editor/>. Versions are not selected in the primary case menu. The action order is **Print / Save PDF**, **Download Editable Copy**, **Download Worksheet**, **Clear Responses**, and **Reset This Case**; the editable copy includes all roles and the toolbar, while the worksheet contains only the selected role without editing controls.

The shared shell remains the canonical implementation of editor controls and recurring presentation behavior. Portable complete exports embed the shell assets. Page identity and recurring component geometry come from the shared `curriculum-components.css`; case CSS is limited to case-specific tokens, figures, and role layouts.

Case instructional content is not stored inside the shared shell. Task titles, semantic labels, role counts, output paths, and case metadata remain case configuration.

The registry retains approved master and role paths for release discovery and verification, but those files are immutable approved release snapshots rather than ongoing editable sources. Embedded case-owned editors are deprecated compatibility implementations. Historical PDFs remain retained outside the active workflow, and browser-created PDFs require separate accessibility review.

## Registry-backed central library

```text
case registry
→ campaign/case/role selector
→ loads the current approved package
→ central editor/export/print workflow
```

The central editor reads `case-registry.v1.json`, preserves exact case order and labels, and loads the selected current package. It does not concatenate every case into one monolithic worksheet or execute an approved standalone master.

The registry supports both SSS and HHH curricula. A curriculum or campaign may exist with no published cases yet. Each cut-over case records editor shell, package, workflow/snapshot/compatibility statuses, manifest reference, retained master and role paths, and current hashes.

The registry-level production policy is machine-readable: new production is `HTML_ONLY`, effective from `SSS-C1-CASE03`, and PDF paths are not allowed in registry entries.

## Cutover boundaries

Approved snapshots are not rewritten to remove their embedded runtime. Repository cleanup is `NOT_STARTED`, Case 04 is `NOT_STARTED`, and no files are deleted in this cutover.
