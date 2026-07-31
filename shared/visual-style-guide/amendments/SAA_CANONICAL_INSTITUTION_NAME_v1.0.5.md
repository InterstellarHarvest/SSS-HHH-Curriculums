# SAA Canonical Institution Name - v1.0.5

**Status:** Approved owner-directed shared correction  
**Scope:** Space Sprout Sleuth game lore, SSS curriculum materials, shared SSS identity assets, templates, manifests, validators, and future cases  
**Effective with:** Follow-up correction after SSS Campaign 1, Case 03 commit `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`

## 1. Canonical name

The one canonical expansion of **SAA** is:

> **Solar Agricultural Agency**

Use the abbreviation **SAA** after the full name has been established where appropriate.

## 2. Rejected variants

Current production material must not use any of the following as an SAA expansion:

- Solar Agricultural Authority
- Space Agricultural Authority
- Space Agricultural Agency
- Solar Agriculture Agency
- Space Agriculture Authority

These forms may appear only inside clearly identified migration reports, historical records, or validator forbidden-term lists.

## 3. Supersession

This correction supersedes the institution-name wording in Section 5.1 of `VISUAL_STYLE_GUIDE_v1.0.md` and any prior game or curriculum text that expands SAA differently. It changes nomenclature only. It does not alter the institutional visual system, insignia, mission-document structure, curriculum architecture, gameplay, science content, or assessment system.

## 4. Required application

### Game repository

Update the canonical full name in:

- title and menu UI;
- lore and dialogue;
- README and current specifications;
- current campaign files and duplicated runtime bundles;
- accessible labels and metadata;
- current asset-generation descriptions that identify the institution.

Do not rename the `SAA` abbreviation, code identifiers, save keys, asset paths, CSS classes, or data structures merely because the displayed full name changes.

### Curriculum repository

Update or verify the canonical full name in:

- the shared Visual Style Guide and quick references;
- SAA insignia alt text and institutional lockups;
- editable masters and generated role outputs;
- controlled Markdown sources when the full name is written;
- manifests, templates, publishing scripts, and validators;
- all future SSS cases.

Approved Case 01 v1.1 and Case 02 v1.0 already use **Solar Agricultural Agency** in their printable identity and do not require a content revision solely for this correction.

## 5. Case 03 application

Case 03 remains version `v1.0` and status `VALIDATION BUILD`, with its physical-print gate `OPEN`. This is a follow-up canonical terminology correction after Case 03 was first committed to `main` at `378f4d873a8fcc46b91af3fb0b552650c2ddeea7`; it does not recreate, replace, or rewrite that initial publication commit. The corrected master, standalone HTML, alt text, lockups, print checklist, reports, manifest, HTML checksums, and validation assertions use **Solar Agricultural Agency**.

The later HTML-only production decision in `HTML_ONLY_PRODUCTION_AND_MANUAL_PDF_ACCESSIBILITY_v1.0.6.md` supersedes this amendment's former Case 03 PDF implementation references. Case 03 no longer stores or validates PDFs.

## 6. Validation rule

Current Student, Teacher, Answer Key, Accessible, and Grayscale outputs must:

1. contain `Solar Agricultural Agency` in the institutional identity;
2. show the three-line lockup `Solar / Agricultural / Agency`;
3. use `Solar Agricultural Agency insignia` in accessible labels where the full name is needed;
4. reject every variant listed in Section 2;
5. retain `SAA` for abbreviations and implementation identifiers.
