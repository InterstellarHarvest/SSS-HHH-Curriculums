# Teacher Production-Metadata Visibility

**Amendment:** v1.0.1  
**Applies to:** SSS and HHH ordinary teacher-facing classroom documents  
**Status:** Locked clarification

## Decision

Ordinary Teacher pages must not include a visible body section devoted to internal compatibility or production lineage.

The following do not appear as ordinary Teacher-page body content:

- source-master version;
- migration date;
- repository path;
- internal filename;
- commit hash;
- validation history;
- checksum;
- build provenance;
- implementation notes intended for maintainers.

A visible body block such as this is prohibited in ordinary Teacher materials:

```text
COMPATIBILITY
Source baseline

Curriculum source master v0.3 · Compatible with SSS commit 2a6e8a7 ·
v1.0 visual-system migration prepared 2026-07-23.
```

## Where production metadata belongs

Keep internal production information in:

- HTML `<meta>` elements;
- the quiet publication footer;
- migration reports;
- validation reports;
- amendment and decision records;
- Git history;
- release manifests;
- repository documentation intended for maintainers.

A concise compatible game release or commit may remain in the publication footer, for example:

```text
SSS-C1-01-TCH · Curriculum v1.0 · Game baseline 2a6e8a7 · Published 2026-XX-XX
```

## Documents covered

This rule applies by default to:

- Teacher Quick Start;
- Formal Lesson Plan;
- Teacher Case Analysis;
- Answer Key;
- Teacher reference pages;
- scoring tools;
- source/reference pages;
- ordinary technical fallback pages included in a classroom packet.

## Exception

A separate technical deployment, administrator, release-management, or compatibility document may present version details prominently when those details are operationally necessary.

That exception does not justify placing internal provenance blocks inside ordinary classroom-facing Teacher packets.

## Page-space principle

Teacher-page body space should support instruction, facilitation, assessment, references, notes, or classroom fallback. It should not be consumed by repository-maintenance information already preserved elsewhere.
