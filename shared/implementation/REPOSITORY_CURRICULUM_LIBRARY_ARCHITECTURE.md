# Repository Curriculum Library Architecture

## Current production architecture

```text
shared canonical editor shell
+ case content/configuration
→ self-contained case master
→ independent role HTML outputs
```

The shared shell is a build-time source, not a runtime web dependency. Each generated case master embeds the shell assets and remains portable. Page identity and recurring component geometry come from the shared `curriculum-components.css`; case CSS is limited to case-specific tokens, figures, and role layouts.

Case instructional content is not stored inside the shared shell. Task titles, semantic labels, role counts, output paths, and case metadata remain case configuration.

Beginning with Case 03, the registry and future viewer are HTML-only. They point to the portable master and independent role HTML files and never require or expose a PDF counterpart. Approved Case 01/02 PDFs remain historical artifacts outside the future viewer contract.

## Future repository-level curriculum library

```text
case registry
→ campaign/case/role selector
→ opens the relevant case master or role output
```

The repository viewer should read `case-registry.v1.json`, populate selectors, and open the selected path. It must not concatenate every case into one monolithic HTML document.

The registry supports both SSS and HHH curricula. A curriculum or campaign may exist with no published cases yet. Adding a case means adding one registry entry that points to its independent master and role outputs.

The registry-level production policy is machine-readable: new production is `HTML_ONLY`, effective from `SSS-C1-CASE03`, and PDF paths are not allowed in registry entries.

## Boundaries for this pass

This architecture defines the registry and shell contracts but does not build the full viewer or the multi-campaign curriculum library.
