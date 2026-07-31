# Shared Editable-Master Shell v1.0

## Authority

This directory is the canonical source for the SSS/HHH editable-master authoring shell. Case-specific masters must not maintain independent copies as their source of truth.

The shell owns:

- toolbar markup and control order;
- editor, response-fill, margin, density, grayscale, guide, and boundary behavior;
- local autosave and portable HTML serialization;
- reset-to-embedded-source behavior;
- shared task-heading markup, typography, icons, and numbering rules;
- the Student CER component;
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

## Save model

Local autosave is recovery state only. `Download Edited Master HTML` clones the live document, embeds the current instructional edits and responses in the clone, gives the clone a distinct document key, and serializes it as self-contained HTML.

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

Every case page has one shared page-identity marker—`data-page-identity="first"` or `data-page-identity="continuation"`—and one `data-publication-footer`. The first page of each role uses the first-page identity; all later pages use the continuation identity. `curriculum-components.css` is the canonical CSS source for those structures and for recurring page, response, callout, table, and figure components.

Every response or note field uses `data-response` and a stable `data-persist-id`. Every instructional node that may be author-edited uses `data-editable` and a stable `data-persist-id`.

## Student CER component

The canonical Student component is identified by:

```html
<div class="canonical-cer" data-cer-contract="student-v1.0">
```

Its Claim, Evidence, and Reasoning boxes use the shared geometry in `cer.css`. Accessible layouts may use a split-page accessible variant when required, but the standard Student and Grayscale sheets use the full-width `student-v1.0` contract.

## Older cases

Case 01 is the functional reference that informed this shell. Approved Case 01 and Case 02 PDFs are retained only as historical release artifacts. They are not regenerated, and maintained HTML does not require a new PDF counterpart.
