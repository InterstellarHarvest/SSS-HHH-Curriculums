# Repository Curriculum Library Architecture

Status: shared production architecture for current and future SSS/HHH cases.

## Discovery and production

```text
case-registry.v2.json
→ source/case-package.json
→ source/content.html
→ source/presentation.css
→ source/task-registry.js
→ source/layout-overrides.json
→ referenced source/assets
→ shared protected printable components
→ central Curriculum Editor
→ temporary editable/role/print documents
```

The registry contains only current operational discovery and lifecycle metadata. Historical artifact paths and hashes live in each approved case’s compact release record when such artifacts existed. Native-only releases explicitly record that no former generated artifacts exist. An unreleased native case has no release record.

The package-controlled sources are canonical. The central editor provides editing, response entry, allowlisted Accessible-only vertical response sizing, display state, four-role switching, clean printing, editable-copy export, and selected-role worksheet export. Generated documents and rendered validation evidence are temporary and are not committed.

## Role model

Student, Teacher, Answer Key, and Accessible are the only roles. Grayscale is a Boolean presentation state applied independently to each role. It does not create another output profile, page-count category, stored document, or filename.

## Required case layout

Every current and future SSS or HHH case uses `README.md` and canonical files directly under `source/`, including a hashed `layout-overrides.json` eligibility/sparse-override contract. Compact records under `history/` are required only at `APPROVED_STABLE`. An `assets/` directory exists only when the active package references its files. Case folders do not contain publishing, master, report, review, or validation-output directories.

## History and recovery

The current tree is intentionally lean. Previous complete documents, role files, PDFs, reports, and validation evidence remain available through Git without rewriting history. A release record either supplies the approved/recovery commit, former paths, hashes, accepted totals, and recovery template, or explicitly marks a native release with no former generated artifacts.

## Validation

Shared static validation reads canonical sources directly. Browser validation assembles role/export/print documents in memory, uses temporary browser profiles and screenshots, validates all 40 case/role/presentation states, and discards outputs. Validation must leave the worktree unchanged.
