# Curriculum Editor Architecture v1.0

Status: shared production architecture for SSS and HHH packages.

Application: `apps/curriculum-editor/`

Registry: `shared/implementation/case-registry.v2.json`
Package schema: `shared/implementation/case-package.schema.v2.json`
Student/Accessible layout schema: `shared/implementation/layout-overrides.schema.v1.json`

## Runtime boundary

The central application owns library navigation, toolbar orchestration, editing state, autosave, page-fit reporting, Shadow DOM isolation, export assembly, and isolated printing. Shared shell files own recurring controls and component styles. Each case package owns identity, lifecycle and approval summary, worksheet content, presentation CSS, task definitions, referenced assets, four role page counts, output filename templates, defaults, accessibility metadata, and source hashes. An `APPROVED_STABLE` package also owns a release-history record; an unreleased native package must not declare one.

Packages never depend on stored complete documents or role outputs.

## Load sequence

1. Fetch and validate registry schema v2.
2. Load the selected `source/case-package.json`.
3. Require exactly Student, Teacher, Answer Key, and Accessible roles.
4. Fetch declared shell, content, presentation, task, Student/Accessible layout, and asset paths plus the central protected printable-component stylesheet.
5. Verify package source hashes.
6. Reject runtime/style/iframe elements in the worksheet fragment and validate stable persistence IDs.
7. Mount the worksheet in an open Shadow DOM, apply protected printable-component styles after case presentation, and restore case/version-scoped browser recovery state.
8. Announce the case, version, role, and Grayscale state.

## Student and Accessible layout authoring boundary

Every future SSS and HHH case package declares one hashed `source/layout-overrides.json`. The file keeps the released Accessible registry at the top level and adds a Student registry under `student`; each separates explicit eligibility metadata, explicit protected-response classifications, and a sparse map of approved pixel heights. Eligibility uses stable case/edition/task/response IDs and is restricted to substantial responses. Every Student and Accessible response must be either eligible or locked with a reason; omissions fail validation. Teacher, Answer Key, CER, compact table/label/classification/status, single-line, and criterion/constraint fields are never inferred as eligible.

Vertical authoring controls exist only in the central editor and only while Student + Edit Text or Accessible + Edit Text is active. Teacher and Answer Key never receive handles. Controls preserve width, page assignment, order, page count, and pagination; snap to 4px; enforce declared bounds; convert pointer movement through the rendered preview scale; and evaluate fixed-Letter page/frame/footer safety. Browser drafts, selections, Undo/Redo history, and pending lists are partitioned by repository/worktree identity, case, edition, and all three source hashes. Hash changes make a draft stale; stale drafts may be inspected, exported, or discarded, but never silently rebased.

Approved heights flow through the same source contract into the editor, editable copies, worksheet exports, isolated print documents, and browser PDF output. Pending browser heights do not. Authoring handles and metadata are stripped from every ordinary export.

The smallest privileged boundary is the loopback service in `authoring_service.py`. It resolves case paths only from the canonical registry/package, rejects client paths and unexpected JSON fields, verifies source hashes and recognized Student/Accessible allowlist IDs, and parses source HTML to revalidate exact role/page/task/locator ownership and reject CER targets independently. It atomically updates only the selected edition's sparse override and package hash, then runs focused validation with rollback on failure. It never commits, pushes, or changes lifecycle approval.

The owner workflow is intentionally source-controlled: resize; inspect the pending change and page validation; Apply to Source with exact confirmation; reload and confirm canonical persistence; inspect the exact two-file Git diff; run focused/full validation plus normal/75%-scale visual and export review; commit; then integrate and synchronize `main`. No implementation or fixture test may populate a real case override map.

## Role and presentation state

Role and Grayscale are independent state values. Switching roles preserves the Grayscale Boolean. Applying Grayscale changes presentation tokens on the isolated worksheet root; it does not change `data-role`, visible pages, content, response IDs, semantic structure, or storage keys. Whole-page raster filtering is prohibited.

## Serialization

Download Editable Copy clones all four roles, current values, toolbar, presentation state, and portable runtime into a self-contained document. Download Worksheet filters to the selected role, keeps that role’s normal filename and identity, applies the current presentation state, and omits editing/application chrome.

The portable runtime uses the same four-role model. The complete copy provides those roles plus an All Pages editing view. It does not define an additional role or output for presentation state.

## Printing

Print / Save PDF assembles a temporary same-origin document containing only the selected role. It preserves edits, responses, margins, density, guides, and current Grayscale state; removes toolbar, rail, status, authoring attributes, overflow warnings, and page shadows; waits for fonts/images; then invokes the isolated window’s print dialog. Temporary documents are removed afterward.

PDFs are neither generated by repository tooling nor committed. Browser-created PDFs require separate accessibility verification.

## State and accessibility

State and content keys include the package document key, so cases and versions remain isolated. Clear Responses affects selected-role responses only. Reset This Case restores only the current case/version.

Hidden roles leave the accessibility tree. Response fields retain accessible names, active editing remains keyboard reachable, and load/save/page-fit/error channels use accessible status announcements. Presentation state never changes document semantics.

## Validation model

- `shared/validation/validate_canonical_case_structure.py` enforces the lean case layout, referenced assets, four-role model, and absence of stored outputs, for every registered case in every campaign.
- `shared/validation/validate_release_integrity.py` proves that every approved release's `canonicalSourceApprovalCommit` contains the exact source blobs its record certifies, and that a corrective release's retained prior records are unmodified since the commit that wrote them.
- `apps/curriculum-editor/tests/validate_static.py` validates both schemas, package/source hashes, page counts, task/CER/process/figure/table contracts, protected-selector isolation, release history, and runtime serialization rules.
- `apps/curriculum-editor/tests/run_pdf_tests.py` generates the registry-derived case-edition print documents and validates them. It is a real regression suite and part of the canonical validation workflow; like the browser suite it is run manually because it requires installed Google Chrome.
- `apps/curriculum-editor/tests/run_browser_tests.py` runs the browser harness against all registry-derived case/role/presentation states -- 104 across the thirteen registered cases -- plus protected-component geometry, switching, persistence, exports, printing, keyboard access, announcements, and zero JavaScript errors.
- `shared/validation/validate_layout_overrides.py` validates complete eligible-or-locked coverage, all locators, Student/Accessible page/task ownership, Student compact-table exclusion, CER and protected compact-field exclusion, snap/bounds, sparse overrides, and package hashes.
- `apps/curriculum-editor/tests/test_authoring_service.py` uses disposable repositories for Student and Accessible round-trip persistence, exact two-file writes, package-hash synchronization, source conflicts, path/edition/role/ID/locked/CER/bounds rejection, and validation rollback.

The browser runner uses only temporary directories for profiles and screenshots. A full run must leave the tracked tree unchanged.

## Recovery boundary

Previous complete documents, role outputs, PDFs, and parity evidence are not present in the current tree. When such artifacts existed, their former paths and hashes are preserved in case history and remain recoverable with `git show <commit>:<path>`. A native-only release records that no former generated artifacts exist.
