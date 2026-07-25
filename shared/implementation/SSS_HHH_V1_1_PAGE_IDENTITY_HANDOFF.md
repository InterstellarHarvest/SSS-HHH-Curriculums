# SSS/HHH v1.1 Universal Page Identity Handoff

This addendum implements `UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md` without redesigning lesson content or publishing behavior.

## Required structural classes

First page:

```html
<header class="mission-title-block" data-header-contract="universal-v1.1">
  <div class="mission-rail" aria-hidden="true"></div>
  <div class="mission-title-copy">
    <h1 class="hero-title">Case title</h1>
    <p class="mission-subtitle">Campaign · Case · Location</p>
  </div>
  <div class="identity-mark">
    <!-- insignia -->
    <div class="identity-copy">
      <div class="institution">Institution name</div>
      <div class="document-role">Document role</div>
    </div>
  </div>
</header>
```

Continuation page:

```html
<header class="continuation-header" data-header-contract="universal-v1.1">
  <div class="continuation-copy">
    <h1>Case title</h1>
    <div class="continuation-role">Document role · Continued</div>
  </div>
  <div class="continuation-identity">
    <!-- insignia -->
    <div class="institution">Institution name</div>
  </div>
</header>
```

Footer:

```html
<footer class="publication-footer" data-footer-contract="universal-v1.1">
  <span>Document role N of total</span>
</footer>
```

## Role labels

- `Student Mission`
- `Teacher Guide`
- `Answer Key`
- `Accessible Mission`

## Validation assertions

A v1.1 validator must reject:

- a visible top accent rule;
- an internal document code in a printable banner or footer;
- a visible master/curriculum version, game baseline, date, approval state, or validation state;
- page-specific continuation titles within one role;
- a footer using `Page N of total` or `1/2` rather than the role-plus-`N of total` contract;
- the insignia/institution on the left side of a continuation header;
- the case title/role on the right side of a continuation header.

All previous role isolation, persistence, reset, portable-download, accessibility, grayscale, and overflow requirements remain unchanged.

## Compact header geometry correction

The universal v1.1 banner uses a 26 pt primary title and 9 pt subtitle. Identification-to-banner and banner-to-content spacing remain compact. The institutional name is rendered as three fixed, left-aligned lines beside the insignia: Solar / Agricultural / Agency. Continuation headers use the same lockup on the right.

## Delta overlay rule

Follow-up ZIP overlays include only files changed by the follow-up. Do not repeat unchanged assets such as case diagrams, source documents, or historical masters. The handoff must identify the prior overlay that the delta expects.
