# Curriculum Editor Legacy Workflow Inventory v1

**Status:** APPROVED · OWNER REVIEW PASS · repository cleanup NOT STARTED

This record identifies the case-owned editor/runtime material retained after the central-editor cutover. Nothing in this inventory is deleted, rewritten, regenerated, or reclassified as an active authoring entry point during cutover.

## Classification rule

- **Approved release snapshot:** frozen approved HTML artifact.
- **Historical provenance:** retained evidence of a prior implementation or release path.
- **Compatibility runtime:** embedded editor or portable role runtime that may still execute, but is not the canonical active workflow.
- **Validation dependency:** read by an accepted or historical regression path.
- **Candidate for later cleanup:** may be evaluated only in the separately authorized cleanup phase.
- **Must retain permanently:** immutable release/provenance artifact; not a cleanup candidate.

## Totals

The machine-readable companion inventories 44 retained items:

| Type | Items | Cutover disposition |
|---|---:|---|
| Embedded-editor masters | 7 | Retain permanently; compatibility-only |
| Portable role runtimes | 20 | Retain permanently as approved current/historical release snapshots |
| Validation fixture | 1 | Retain now; later cleanup review permitted |
| Historical Case 03 case-owned sources | 3 | Retain now; later cleanup review permitted |
| Legacy build/validation tools | 13 | Retain now; later cleanup review permitted |

The seven masters are the complete Case 01 v0.2, v0.3, v1.0, and v1.1 files; Case 02 v1.0; and Case 03 v1.0 and v1.1. The 20 role runtimes are the five current Case 01 outputs, five current Case 02 outputs, and both five-role Case 03 v1.0/v1.1 release sets. Approved HTML remains byte-identical even where it contains an editor toolbar, script, or portable response/print runtime.

## Cleanup boundary

Candidate status is not deletion approval. A later cleanup phase must re-check validation reachability, release provenance, package references, and owner requirements before changing any candidate. Approved masters and role snapshots are permanently excluded from cleanup. The central editor, shared shell, current case packages, and package-controlled current content/presentation/task/assets are active architecture and are not legacy inventory items.
