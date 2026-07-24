# SSS/HHH v1.0 Editable Master Production Handoff

**Foundation implementation:** `sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html`

## 1. Purpose

Case 01 proves that the approved v1.0 visual system can operate as a real editable, fillable, printable curriculum master rather than only as a template gallery.

Later SSS and HHH cases should reuse the framework contracts below and replace only case content, institutional identity variables, and role-specific page composition.

## 2. Shared framework code

### 2.1 Core CSS variables

Retain a single `:root` production token block.

#### Geometry

- `--page-w`
- `--page-h`
- `--margin`
- `--gutter`
- `--density`
- `--radius`

#### Shared neutral system

- `--ink`
- `--muted`
- `--line`
- `--line-light`
- `--paper`
- `--screen`
- `--neutral-field`

#### Institutional and semantic colors

SSS maps the institutional variables to Orbital Cyan and Botanical Green. HHH should map the same component variables to Archive Amber and Record Cyan rather than forking component geometry.

Keep semantic caution, critical, success, and neutral meanings consistent across both curricula.

#### Type scale

- `--hero` / `--hero-lh`
- `--title` / `--title-lh`
- `--section` / `--section-lh`
- `--deck` / `--deck-lh`
- `--body` / `--body-lh`
- `--small` / `--small-lh`
- `--caption` / `--caption-lh`
- `--micro` / `--micro-lh`

Do not solve overflow by silently lowering these values case by case.

### 2.2 Page shell

Every page uses:

```html
<section class="page role-…" data-role="…" data-page-id="…" role="region" aria-labelledby="…">
  <div class="overflow-warning" aria-live="polite">PAGE OVERFLOW</div>
  <div class="page-frame">
    <!-- first Student/Accessible page: identification row, then title block; otherwise title block or continuation header -->
    <div class="content-area">…</div>
    <footer class="publication-footer">…</footer>
  </div>
</section>
```

The fixed page boundary is non-negotiable. Overflow warnings are screen-only and must never print.

### 2.3 Student identification before first-page identity

For Student and Accessible outputs, page 1 begins with `.student-id` before `.mission-title-block`.

Required order:

1. Name
2. Date
3. Period

Contract:

- the row is the first printable element inside `.page-frame`;
- it appears only on page 1 of each Student or Accessible role;
- it is absent from continuation pages, Teacher pages, and Answer Key pages;
- stable `data-field` values and accessible names are required;
- the row must remain usable in print, fillable mode, grayscale, and keyboard navigation.

Recommended shell:

```html
<div class="page-frame">
  <div class="student-id" aria-label="Student identification">…</div>
  <header class="mission-title-block">…</header>
  <div class="content-area">…</div>
  <footer class="publication-footer">…</footer>
</div>
```

### 2.4 First-page identity

Use `.mission-title-block` once at the start of each independent output role. In Student and Accessible roles, it follows the first-page identification row. Teacher and Answer Key roles begin directly with the Mission Title Block.

Variables:

- institution;
- document role;
- case/chapter title;
- campaign/setting/topic subtitle;
- insignia path;
- publication-status mark.

Do not place commit, publication date, repository path, page count, Name, Date, or Period in the prominent title hierarchy.

### 2.5 Continuation identity

Use `.continuation-header` for subsequent pages.

Include:

- compact institution mark;
- case or document title;
- role;
- “Continued” where useful.

### 2.6 Publication footer

Use `.publication-footer` with:

- document code;
- curriculum/master version;
- game/source compatibility baseline;
- publication date;
- filled status text;
- role-specific page number and total.

Keep these values data-driven when the production pipeline is extracted from the single-file prototype.

Production provenance (commit hash, source-master version, migration date, repository path, checksums, internal filenames) stays in these footer and metadata channels, migration and validation reports, decision records, and Git history — not in ordinary Teacher-page body sections. See `TEACHER_PRODUCTION_METADATA_VISIBILITY_v1.0.1.md`.

### Exact-match word-bank contract

For a constrained fill-in-the-blank activity, place `.word-bank` adjacent to the supported blanks.

```html
<div class="word-bank" aria-label="Word bank for Task 5">
  <span class="word-bank-label">WORD BANK</span>
  <span class="word-bank-terms">term or phrase · second term · third term</span>
</div>
```

Contract:

- the number of bank entries equals the number of blanks;
- every entry is used by the activity;
- no decoys, extras, or omissions;
- repeated answers are repeated;
- phrase answers remain intact;
- Standard and Accessible roles use the same bank;
- Answer Key wording matches exactly;
- the bank is not a response field and does not require persistence;
- keyboard and screen-reader users encounter the bank before or immediately after the supported blanks.

## 3. Shared component contracts

### 3.1 Technical Label Heading

```html
<h2 class="section-heading">
  <svg class="ph-icon" aria-hidden="true"><use href="#ph-…"></use></svg>
  <span>
    <span class="technical-label">STANDARDIZED FUNCTION</span>
    <span class="section-title">Human-readable heading</span>
  </span>
</h2>
```

Use an official Phosphor Regular symbol for recurring standardized functions. One-off subheadings may remain plain.

### 3.2 Callout

Use `.callout` with one icon, one technical label, and one semantic text block.

Variants should describe meaning, not decoration:

- institutional focus;
- confirmed/success;
- caution/inference;
- fictional context;
- critical boundary;
- optional extension.

Never rely on fill color alone.

### 3.3 Student response

```html
<div class="response-block …">
  <p class="response-prompt">…</p>
  <div class="response-guidance">…</div>
  <div class="response-area" data-response data-field="…" aria-label="…"></div>
</div>
```

Rules:

- prompt above the box;
- blank and unruled;
- short mono guidance;
- stable `data-field` identifier;
- accessible name;
- flex growth only when extra space improves usability.

### 3.4 CER

Use `.cer-stack` with three `.cer-block` children.

Minimum hierarchy:

- Claim shortest;
- Evidence taller;
- Reasoning tallest.

When the stack receives surplus page height, distribute additional height equally rather than allowing only Reasoning to absorb it.

### 3.5 Technical tables

Use `.tech-table` and include a `<caption>`. A caption may be visually hidden when the visible section heading already supplies the same label.

Avoid dense table text below the approved table scale. Repaginate or simplify the table structure instead.

### 3.6 Teacher and answer notes

Use `.teacher-note` for facilitation guidance inside the lesson flow.

Use `.notes-area` for genuine remaining-page planning or annotation space. Do not add a notes area merely to conceal poor pagination; it must be useful in the document role.

### 3.7 Answer blocks

Use `.answer-block` only inside the independent Answer Key role. Do not restore inline student-page answer toggles.

<!-- TASK_REFERENCE_PARITY_RULE_v1.0.1: HANDOFF -->
### 3.8 Student-task reference parity

The standard Student role owns numbered task identifiers and visible task titles.

- Answer Key headings for keyed work repeat the Student number and title exactly.
- Non-keyable tasks are omitted silently; later Answer Key sections keep the original Student numbering.
- Teacher-facing prose or tables that direct a teacher to a specific worksheet task include the same number and title.
- General teacher sections remain unnumbered when they are not cross-references.
- Technical labels may distinguish `MODEL RESPONSE`, `REJECTED ALTERNATIVE`, `SCORING GUIDANCE`, or similar teacher functions, but they do not replace the shared numbered title.
- Accessible editions retain the same numbered titles as the standard Student edition.
- A direct Teacher reference to a specific Student task is rendered in bold as `<strong class="task-reference">N · Title</strong>` (shared CSS `.task-reference { font-weight: 700; }`); only the reference is bolded. See `TEACHER_TASK_REFERENCE_EMPHASIS_v1.0.1.md`.

## 4. Role architecture

Required role values:

- `student`
- `teacher`
- `answer`
- `accessible`
- `all`

The body owns the active role:

```html
<body data-role="student">
```

Page visibility is controlled by role classes. Changing roles must update only the role field in state; it must not reconstruct or reset the state object.

“All Pages” is an implementation-audit view, not a packet intended for ordinary distribution.

## 5. JavaScript foundation

### 5.1 Persistent state object

Persist one state object containing:

- role;
- margin;
- density;
- edit mode;
- fill mode;
- grayscale;
- print preview;
- margin guides.

Use one `applyState()` path so controls, DOM classes, editable states, status text, and overflow checks cannot drift.

### 5.2 Persistent content

Assign a stable `data-persist-id` to every `[data-editable]` and `[data-response]` node.

Prefer explicit `data-field` values for response areas because those identifiers should survive ordinary content reordering.

Save content on input. Load content after stable IDs are assigned.

### 5.3 Edit and fill behavior

- Edit mode enables instructional text and response fields.
- Fillable Student mode enables response fields without opening instructional text.
- Inactive editable regions use `tabindex="-1"`.
- Active fields use `tabindex="0"` and visible focus styling.

### 5.4 Overflow behavior

Check only visible pages. Hidden role pages have zero layout dimensions and must never be diagnosed as overflowing.

Check:

- page frame scroll width/height;
- content area scroll width/height.

The warning is diagnostic. It must not auto-shrink type or content.

### 5.5 Print behavior

Do not mutate role before printing. The current role already determines page visibility.

`beforeprint` should run overflow checking. Screen controls and warnings must be excluded by print CSS.

### 5.6 Grayscale behavior

Do not apply `filter: grayscale()` to the whole page or workspace. Chromium may rasterize the exported PDF.

Use grayscale token overrides for:

- text;
- rules;
- fills;
- status colors.

Filter only artwork that cannot be recolored through CSS variables.

## 6. Accessible-edition contract

The Accessible role is a parallel edition, not a zoomed screenshot of the standard packet.

It may:

- increase type;
- reduce density;
- use more pages;
- simplify multi-column layouts;
- enlarge writing and drawing areas;
- support alternate response modes.

It must preserve:

- case identity;
- numbered task order;
- science/history expectations;
- evidence relationships;
- assessment target;
- source and compatibility metadata.

The HTML edition should remain the primary accessible digital artifact unless a tagged-PDF pipeline is added.

## 7. SSS versus HHH variables

Shared geometry and component logic should remain identical.

Change the recurring institutional structures:

| SSS | HHH |
|---|---|
| Solar Agricultural Authority | Temporal Agricultural Archive |
| `shared/assets/insignia/saa.svg` | `shared/assets/insignia/taa.svg` |
| Mission/system status language | Accession/source-status language |
| Mechanism and diagnosis | Provenance and interpretation |
| Engineering recommendation | Historical interpretation |
| Orbital Cyan / Botanical Green | Archive Amber / Record Cyan |

Do not fork borders, page geometry, response-box rules, or type scales merely to make the curricula look more different.

## 8. Case-production workflow

For each later case:

1. Inventory the real source master before editing.
2. Separate content defects from framework defects.
3. Map source content into role page sets.
4. Apply the shared page shell and components.
5. Repaginate rather than reduce approved type.
6. Build the accessible role in parallel, not after release.
7. Confirm Name / Date / Period is topmost on only the first Student and Accessible page.
8. Validate Student, Teacher, Answer, Accessible, Grayscale, Print Preview, and All Pages.
9. Test role-state preservation and saved content restoration.
10. Render PDFs and inspect every page.
11. Complete a physical 100% print test.
12. Keep status as Validation or Review until all release gates pass.

## 9. Recommended extraction after Case 02

Case 01 is intentionally a self-contained HTML proof. After one additional SSS case demonstrates that the component contracts generalize, extract:

- shared CSS tokens and components;
- shared Phosphor symbol sprite;
- shared publishing toolbar;
- shared state/persistence module;
- shared overflow test;
- shared role-print test harness.

Do not extract Case 01 vocabulary, prompts, tables, answers, or timing into framework code.
