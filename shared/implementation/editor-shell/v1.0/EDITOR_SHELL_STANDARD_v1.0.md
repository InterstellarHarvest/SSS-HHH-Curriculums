# Shared Editable-Master Shell v1.0

## Authority

This directory is the canonical source for the SSS/HHH editable-master authoring shell. Case-specific masters must not maintain independent copies as their source of truth.

The shell owns:

- toolbar markup and control order;
- editor, response-fill, margin, density, grayscale, guide, and boundary behavior;
- local autosave and portable HTML serialization;
- reset-to-embedded-source behavior;
- shared task-heading markup, typography, icons, and numbering rules;
- the Student, Accessible, and Answer Key CER variants of one canonical component;
- the canonical five-stage process model, sequence phrase bank, and optional-extension component;
- common page-identity and authoring-mode CSS.

Case packages own instructional content, task configuration, case-specific figures, case-specific layout CSS, and release metadata.

## HTML-only output policy

Beginning with Case 03, the canonical artifact set is the portable editable-master HTML plus independent Student, Teacher, Answer Key, Accessible, and Grayscale HTML files. The shared workflow does not generate, store, preflight, checksum, validate, or require PDFs.

The toolbar retains **Print / Save PDF** for browser printing and optional end-user export. That action does not guarantee an accessible PDF. A manually created PDF must not be distributed, published, or archived without separate accessibility verification. Physical print testing uses the browser print dialog at 100% / Actual Size.

## Assembly contract

```text
shared canonical editor shell
+ case content/configuration
→ self-contained case master
→ independent role HTML outputs
```

`assemble_editable_master.py` embeds the shared toolbar, page-identity/common-component CSS, editor CSS, CER CSS, icons, and runtime into the finished HTML. The output records shell version `1.0`, the contract SHA-256, and each embedded shell-asset SHA-256. A validator can therefore prove that a master matches the shared contract instead of trusting locally named classes.

The generated master has no runtime dependency on this directory. It remains portable as one HTML file.

## Literal editor reference

The toolbar HTML, toolbar CSS, runtime behavior, controls, labels, order, grouping, dimensions, and spacing are governed by the approved Case 02 master at `sss/campaign-1/case-02-lunar-greenhouse/master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html`. Shared-shell assembly preserves that implementation. Case-specific storage keys, download filename, and exported global name are the only runtime substitutions, preventing cross-case local-storage collisions without changing behavior.

The worksheet identity also follows the approved Case 01/02 `printable-v1.1` structures: full-width 2fr/1fr/.7fr identification fields, color SAA insignia, three-line Solar Agricultural Agency lockup, first-page accent rail/title geometry, and continuation-header geometry.

## Save model

Local autosave is recovery state only. `Download Current HTML` clones the live document, embeds the current instructional edits and responses in the clone, and serializes it as self-contained HTML.

When that downloaded copy opens with empty storage, its DOM becomes its embedded source. `Reset Source` therefore returns to the edits embedded in that downloaded copy.

## Case-source requirements

A case configuration must provide:

- a unique document key;
- title and metadata;
- roles and default toolbar state;
- exact task numbers, titles, semantic labels, and icon IDs;
- a case CSS source;
- an instructional-content fragment;
- master and role-output filenames.

Task-heading placeholders use `data-shell-task-heading="N"`. The assembler replaces them with the canonical heading component.

Standard Student, Teacher-reference, and Answer Key task titles render at **11.5 pt**. Accessible task titles render at **14 pt**. The technical label describes the task function (`REFERENCE`, `PREDICTION`, `DATA ANALYSIS`, `EXPLANATION`, and so on); it must not repeat the task number as `TASK 01`, `TASK 7`, or a similar label. The visible title owns the number exactly once in the form `N · Title`.

Every case page has one shared page-identity marker—`data-page-identity="first"` or `data-page-identity="continuation"`—and one `data-publication-footer`. The first page of each role uses the first-page identity; all later pages use the continuation identity. `curriculum-components.css` is the canonical CSS source for those structures and for recurring page, response, callout, table, and figure components.

Every response or note field uses `data-response` and a stable `data-persist-id`. Every instructional node that may be author-edited uses `data-editable` and a stable `data-persist-id`.

## Canonical CER component

The canonical Student component is identified by:

```html
<div class="canonical-cer" data-cer-contract="student-v1.0">
```

Its Claim, Evidence, and Reasoning boxes use the shared geometry in `cer.css`. `student-v1.0`, `accessible-v1.0`, and `answer-v1.0` preserve the same three-row structure, label blocks, borders, spacing, proportional row heights, and grayscale behavior. A CER is atomic in every role: all three rows share one canonical root, that root belongs to one `.page`, and its rendered bounds remain inside that page's frame. Accessible layouts may not split the component across pages. The shared `break-inside` protections support this rule but do not replace correct authored page structure. Answer Keys complete the right-hand response fields instead of substituting another layout.

## Five-stage process model

Recurring five-stage mechanisms use `data-process-contract="five-stage-v1.0"`, five `.canonical-process-stage` elements, and four `.canonical-process-arrow` connectors. Standard pages use the deterministic horizontal grid; Accessible pages use the vertical variant. Flex wrapping is prohibited. Geometry validation confirms equal stages, aligned connectors, no collisions, and no detached final stage.

## Sequence phrase bank

Recurring sequencing scaffolds use `data-phrase-bank-contract="sequence-v1.0"` on one `.canonical-phrase-bank` immediately after the model it supports. Its DOM order is label, instruction, then one unnumbered `.canonical-phrase-bank-items` list. Each `.canonical-phrase-bank-item` contains one source-controlled phrase. Case configuration owns the exact phrase source, fixed display order, and role scope; runtime reshuffling is prohibited. Student, Accessible, Grayscale, and any layout-parity Answer Key bank use identical wording and order. The bank and its supported task must share one authored page, while the model remains a separate atomic component with all stages and connectors intact.

## Figure provenance and optional extensions

Student-facing figure provenance is one compact caption. Production commentary boxes such as `SOURCE STATUS` and `GAME-PROVIDED COMPARISON` are prohibited on Student and Accessible pages. Fuller source distinctions belong in Teacher analysis, rights records, metadata, and reports.

Optional extensions use `data-optional-extension="canonical-v1.0"` and the Case 01 neutral callout/icon family. They appear only after all required tasks when usable surplus space remains; they are never required for grading.

Open-response tasks are stacked full-width by default. Two tasks may share a row only when both components are genuinely compact, the prompts remain comfortably readable, each writing area remains adequate, and the pairing does not create visual crowding. Surplus page height should first increase useful writing/model space and deliberate vertical separation rather than remain as a large blank lower-page area.

## Older cases

Case 01 is the functional reference that informed this shell. Approved Case 01 and Case 02 PDFs are retained only as historical release artifacts. They are not regenerated, and maintained HTML does not require a new PDF counterpart.
