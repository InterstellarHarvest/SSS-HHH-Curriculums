#!/usr/bin/env python3
"""Validate the HHH production-activation contract.

Scope: the HHH curriculum object inside the shared case registry, the planned
15-unit topology the approved Blueprint locks, and the HHH game-remediation
dependency tracker. This validator owns the planned-entry rules that the
operational validators (`validate_canonical_case_structure.py`,
`validate_release_integrity.py`) deliberately skip: registry entries without an
``editorPackage`` are planned reservations, and this is where their shape is
enforced.

It stays reusable after package production begins: an entry that gains an
``editorPackage`` is checked for canonical-package existence and registry/package
identity and instructional-type parity instead of being rejected. The optional
``--expect-editor-ready N`` argument pins the number of operational HHH entries,
so the activation commit itself can assert that it created no HHH package
(``--expect-editor-ready 0``) without freezing that state into the validator.

Usage:
    python3 shared/validation/validate_hhh_activation.py [--expect-editor-ready N]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "shared/implementation/case-registry.v2.json"
TRACKER = ROOT / "hhh/production/data/HHH_GAME_REMEDIATION_DEPENDENCY_TRACKER_v1.0.json"

CANONICAL_TITLE = "Hunger, Harvest, & History"
INSTRUCTIONAL_TYPES = {"ORIENTATION", "CORE_CASE", "SYNTHESIS", "CAPSTONE"}

# The Blueprint-locked 15-unit sequence: (campaign, id, displayOrder, displayLabel,
# title, instructionalType). Section 5 and 19.3 of HHH_CURRICULUM_BLUEPRINT_v1.0.md.
EXPECTED_UNITS = [
    ("campaign-1", "HHH-C1-CASE00", 1, "Archive Orientation", "Temporal Agricultural Archive Facility", "ORIENTATION"),
    ("campaign-1", "HHH-C1-CASE01", 2, "1 - The Fertile Crescent", "The Fertile Crescent", "CORE_CASE"),
    ("campaign-1", "HHH-C1-CASE02", 3, "2 - Sumer", "Sumer", "CORE_CASE"),
    ("campaign-1", "HHH-C1-CASE03", 4, "3 - County Cork", "County Cork", "CORE_CASE"),
    ("campaign-1", "HHH-C1-CASE04", 5, "4 - Karlsruhe", "Karlsruhe", "CORE_CASE"),
    ("campaign-1", "HHH-C1-CASE05", 6, "5 - The Dust Bowl", "The Dust Bowl", "CORE_CASE"),
    ("campaign-1", "HHH-C1-CASE06", 7, "6 - The Vertical Farm", "The Vertical Farm", "CORE_CASE"),
    ("campaign-1", "HHH-C1-SYNTHESIS", 8, "Campaign 1 Synthesis", "The Temporal Agricultural Archive", "SYNTHESIS"),
    ("campaign-2", "HHH-C2-CASE07", 9, "7 - The Audit", "The Audit", "CORE_CASE"),
    ("campaign-2", "HHH-C2-CASE08", 10, "8 - The Floating Gardens", "The Floating Gardens", "CORE_CASE"),
    ("campaign-2", "HHH-C2-CASE09", 11, "9 - The Seeds They Kept", "The Seeds They Kept", "CORE_CASE"),
    ("campaign-2", "HHH-C2-CASE10", 12, "10 - The Quiet Billion", "The Quiet Billion", "CORE_CASE"),
    ("campaign-2", "HHH-C2-CASE11", 13, "11 - The Bloom That Needed Poison", "The Bloom That Needed Poison", "CORE_CASE"),
    ("campaign-2", "HHH-C2-CASE12", 14, "12 - The Living Record", "The Living Record", "CORE_CASE"),
    ("campaign-2", "HHH-C2-CAPSTONE", 15, "Program Capstone", "The Source", "CAPSTONE"),
]
SPECIAL_UNIT_TYPES = {
    "HHH-C1-CASE00": "ORIENTATION",
    "HHH-C1-SYNTHESIS": "SYNTHESIS",
    "HHH-C2-CAPSTONE": "CAPSTONE",
}
PLANNED_LIFECYCLE = {
    "version": "0.1",
    "status": "DRAFT",
    "editorShell": "1.0",
    "centralWorkflow": "CANONICAL",
    "packageStatus": "DRAFT",
}
PLANNED_APPROVAL = {
    "owner": "Nate / Owner",
    "status": "OWNER_REVIEW_NOT_STARTED",
    "printStatus": "NOT_RUN",
}

# Authoritative baselines the tracker must name. Section 21 of the Blueprint and
# Section 1 of the Phase 1 audit.
TRACKER_AUTHORITY = {
    "phase1Audit": "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md",
    "staticContentInventory": "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json",
    "auditedGameCommit": "9b8545ed6ecf98b337326390400076e36789e056",
    "blueprint": "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
    "activationBaselineCommit": "d47003c34650a465aea81dbc2da5b5fc9dc4cd47",
}

# The complete audit-§6 game-dependency census: finding ID -> (curriculum unit,
# dependency class). Independently verified field-for-field against the committed
# Phase 1 audit. The tracker must carry exactly these 21 — no additions, no losses.
EXPECTED_DEPENDENCIES = {
    "HHH-GAME-C1L1-001": ("HHH-C1-CASE01", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
    "HHH-GAME-C1L1-002": ("HHH-C1-CASE01", "NONBLOCKING_POLISH"),
    "HHH-GAME-C1L2-001": ("HHH-C1-CASE02", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
    "HHH-GAME-C1L2-002": ("HHH-C1-CASE02", "CURRICULUM_QUALIFICATION_REQUIRED"),
    "HHH-GAME-C1L2-003": ("HHH-C1-CASE02", "NONBLOCKING_POLISH"),
    "HHH-GAME-C1L3-001": ("HHH-C1-CASE03", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
    "HHH-GAME-C1L4-001": ("HHH-C1-CASE04", "NONBLOCKING_POLISH"),
    "HHH-GAME-C1L4-002": ("HHH-C1-CASE04", "CURRICULUM_QUALIFICATION_REQUIRED"),
    "HHH-GAME-C1L5-001": ("HHH-C1-CASE05", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
    "HHH-GAME-C1L5-002": ("HHH-C1-CASE05", "CURRICULUM_QUALIFICATION_REQUIRED"),
    "HHH-GAME-C1L6-001": ("HHH-C1-CASE06", "CURRICULUM_QUALIFICATION_REQUIRED"),
    "HHH-GAME-C2L0-001": ("HHH-C2-CASE07", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
    "HHH-GAME-C2L1-001": ("HHH-C2-CASE08", "CURRICULUM_QUALIFICATION_REQUIRED"),
    "HHH-IMP-C2L2-001": ("HHH-C2-CASE09", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
    "HHH-GAME-C2L2-001": ("HHH-C2-CASE09", "CURRICULUM_QUALIFICATION_REQUIRED"),
    "HHH-GAME-C2L3-001": ("HHH-C2-CASE10", "CURRICULUM_QUALIFICATION_REQUIRED"),
    "HHH-GAME-C2L4-001": ("HHH-C2-CASE11", "CURRICULUM_QUALIFICATION_REQUIRED"),
    "HHH-DOC-C2L4-001": ("HHH-C2-CASE11", "NONBLOCKING_POLISH"),
    "HHH-GAME-C2L5-001": ("HHH-C2-CASE12", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
    "HHH-GAME-C2L5-002": ("HHH-C2-CASE12", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
    "HHH-GAME-C2L6-001": ("HHH-C2-CAPSTONE", "GAME_REMEDIATION_BLOCKS_FINALIZATION"),
}
EXPECTED_CLASS_TOTALS = {
    "GAME_REMEDIATION_BLOCKS_FINALIZATION": 9,
    "CURRICULUM_QUALIFICATION_REQUIRED": 8,
    "NONBLOCKING_POLISH": 4,
}
# Finalization-blocking coverage, derived from the census above.
REQUIRED_BLOCKING = {finding_id: unit for finding_id, (unit, dependency_class) in EXPECTED_DEPENDENCIES.items()
                     if dependency_class == "GAME_REMEDIATION_BLOCKS_FINALIZATION"}
# Blueprint decision findings closed by the approved Blueprint, not by activation.
EXPECTED_BLUEPRINT_CLOSURES = {"HHH-DEC-001", "HHH-DEC-002", "HHH-DEC-003", "HHH-DEC-004"}
RESOLUTION_FIELDS = ("resolvedGameCommit", "resolutionEvidence", "verificationDate", "verifier", "verificationStatus")
OPEN_STATUS = "OPEN_AT_AUDITED_GAME_BASELINE"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expect-editor-ready", type=int, default=None, metavar="N",
                        help="require exactly N HHH entries to declare an editorPackage "
                             "(0 asserts the activation state: no HHH package exists yet)")
    args = parser.parse_args()

    failures: list[str] = []

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    hhh = next((c for c in registry.get("curricula", []) if c.get("id") == "HHH"), None)
    if hhh is None:
        failures.append("registry declares no HHH curriculum")
        return report(failures, 0)

    if hhh.get("title") != CANONICAL_TITLE:
        failures.append(f"HHH curriculum title must be {CANONICAL_TITLE!r}; found {hhh.get('title')!r}")

    campaigns = hhh.get("campaigns", [])
    if [c.get("id") for c in campaigns] != ["campaign-1", "campaign-2"]:
        failures.append(f"HHH must hold exactly campaign-1 and campaign-2; found {[c.get('id') for c in campaigns]}")

    entries = [(campaign.get("id"), case) for campaign in campaigns for case in campaign.get("cases", [])]
    actual = [(campaign_id, e.get("id"), e.get("displayOrder"), e.get("displayLabel"), e.get("title"), e.get("instructionalType"))
              for campaign_id, e in entries]
    if actual != EXPECTED_UNITS:
        for got, want in zip(actual + [None] * (len(EXPECTED_UNITS) - len(actual)), EXPECTED_UNITS):
            if got != want:
                failures.append(f"HHH unit sequence mismatch: expected {want}, found {got}")
        if len(actual) > len(EXPECTED_UNITS):
            failures.append(f"HHH declares {len(actual)} units; the locked topology has exactly {len(EXPECTED_UNITS)}")

    by_id = {e.get("id"): (campaign_id, e) for campaign_id, e in entries}
    for campaign_id, e in entries:
        unit_id = e.get("id")
        label = str(e.get("displayLabel", ""))
        if "CASE13" in str(unit_id) or label.startswith("13 -"):
            failures.append(f"{unit_id}: there is no Core Case 13 in the locked topology")
        expected_special = SPECIAL_UNIT_TYPES.get(unit_id)
        if expected_special and e.get("instructionalType") != expected_special:
            failures.append(f"{unit_id}: special unit must be {expected_special}; found {e.get('instructionalType')}")
        if expected_special is None and e.get("instructionalType") != "CORE_CASE":
            failures.append(f"{unit_id}: numbered Core Case must be CORE_CASE; found {e.get('instructionalType')}")
        if e.get("instructionalType") not in INSTRUCTIONAL_TYPES:
            failures.append(f"{unit_id}: every HHH entry requires a valid instructionalType")

        if "editorPackage" not in e:
            # Planned reservation: unreleased lifecycle metadata, no package, no history.
            if "historyRecord" in e:
                failures.append(f"{unit_id}: planned entry must not declare a historyRecord")
            for field, expected in PLANNED_LIFECYCLE.items():
                if e.get(field) != expected:
                    failures.append(f"{unit_id}: planned entry {field} must be {expected!r}; found {e.get(field)!r}")
            if e.get("approval") != PLANNED_APPROVAL:
                failures.append(f"{unit_id}: planned entry approval must be {PLANNED_APPROVAL}; found {e.get('approval')}")
        else:
            package_path = ROOT / e["editorPackage"]
            if not str(e["editorPackage"]).startswith(f"hhh/{campaign_id}/"):
                failures.append(f"{unit_id}: editorPackage must live under hhh/{campaign_id}/: {e['editorPackage']}")
            if not package_path.is_file():
                failures.append(f"{unit_id}: declared editorPackage does not exist: {e['editorPackage']}")
                continue
            try:
                package = json.loads(package_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as error:
                failures.append(f"{unit_id}: declared editorPackage is not readable JSON: {error}")
                continue
            if package.get("id") != unit_id:
                failures.append(f"{unit_id}: package identity mismatch: {package.get('id')}")
            if package.get("curriculum") != "HHH":
                failures.append(f"{unit_id}: package curriculum must be HHH; found {package.get('curriculum')}")
            if package.get("instructionalType") != e.get("instructionalType"):
                failures.append(f"{unit_id}: registry/package instructional type mismatch: "
                                f"{e.get('instructionalType')} vs {package.get('instructionalType')}")

    editor_ready = [e.get("id") for _, e in entries if "editorPackage" in e]
    if args.expect_editor_ready is not None and len(editor_ready) != args.expect_editor_ready:
        failures.append(f"expected exactly {args.expect_editor_ready} editor-ready HHH entr(y/ies); found {len(editor_ready)}: {editor_ready}")

    # No unregistered HHH package directory: every case-package.json under hhh/ must be
    # named by a registry entry, and every unit directory under an HHH campaign folder
    # must belong to a registered operational entry.
    registered_packages = {e["editorPackage"] for _, e in entries if "editorPackage" in e}
    for package_file in sorted((ROOT / "hhh").rglob("case-package.json")):
        relative = package_file.relative_to(ROOT).as_posix()
        if relative not in registered_packages:
            failures.append(f"unregistered HHH package exists on disk: {relative}")
    registered_unit_dirs = {(ROOT / path).parent.parent for path in registered_packages}
    for campaign_dir in sorted((ROOT / "hhh").glob("campaign-*")):
        for unit_dir in sorted(path for path in campaign_dir.iterdir() if path.is_dir()):
            if unit_dir not in registered_unit_dirs:
                failures.append(f"HHH unit directory has no registered operational entry: {unit_dir.relative_to(ROOT).as_posix()}")

    # --- remediation dependency tracker -------------------------------------------
    if not TRACKER.is_file():
        failures.append(f"remediation dependency tracker is missing: {TRACKER.relative_to(ROOT).as_posix()}")
        return report(failures, len(editor_ready))
    try:
        tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        failures.append(f"remediation dependency tracker is not readable JSON: {error}")
        return report(failures, len(editor_ready))

    authority = tracker.get("authority", {})
    for field, expected in TRACKER_AUTHORITY.items():
        if authority.get(field) != expected:
            failures.append(f"tracker authority.{field} must be {expected!r}; found {authority.get(field)!r}")

    dependencies = tracker.get("gameDependencies", [])
    by_finding: dict[str, list[dict]] = {}
    for item in dependencies:
        by_finding.setdefault(str(item.get("findingId")), []).append(item)

    # Complete census: exactly the 21 audit-§6 game dependencies, each exactly once,
    # each mapped to its unit and class. Missing and extra IDs are both failures.
    if len(dependencies) != len(EXPECTED_DEPENDENCIES):
        failures.append(f"tracker must hold exactly {len(EXPECTED_DEPENDENCIES)} game dependencies; found {len(dependencies)}")
    missing = sorted(set(EXPECTED_DEPENDENCIES) - set(by_finding))
    extra = sorted(set(by_finding) - set(EXPECTED_DEPENDENCIES))
    if missing:
        failures.append(f"tracker lost audited game dependencies: {missing}")
    if extra:
        failures.append(f"tracker holds dependency IDs the audit register does not: {extra}")
    for finding_id, (unit_id, dependency_class) in EXPECTED_DEPENDENCIES.items():
        matches = by_finding.get(finding_id, [])
        if len(matches) != 1:
            if matches:
                failures.append(f"tracker must record {finding_id} exactly once; found {len(matches)}")
            continue
        item = matches[0]
        if item.get("curriculumUnit") != unit_id:
            failures.append(f"{finding_id}: must map to {unit_id}; tracker maps it to {item.get('curriculumUnit')}")
        if item.get("dependencyClass") != dependency_class:
            failures.append(f"{finding_id}: must be classed {dependency_class}; tracker classes it {item.get('dependencyClass')}")
    actual_totals: dict[str, int] = {}
    for item in dependencies:
        actual_totals[str(item.get("dependencyClass"))] = actual_totals.get(str(item.get("dependencyClass")), 0) + 1
    if actual_totals != EXPECTED_CLASS_TOTALS:
        failures.append(f"tracker class totals must be {EXPECTED_CLASS_TOTALS}; found {actual_totals}")

    for item in dependencies:
        finding_id = item.get("findingId")
        if item.get("curriculumUnit") not in by_id:
            failures.append(f"{finding_id}: tracker names an unknown curriculum unit: {item.get('curriculumUnit')}")
        if item.get("dependencyClass") not in {"GAME_REMEDIATION_BLOCKS_FINALIZATION", "CURRICULUM_QUALIFICATION_REQUIRED", "NONBLOCKING_POLISH"}:
            failures.append(f"{finding_id}: invalid dependencyClass {item.get('dependencyClass')}")
        resolution = item.get("resolution", {})
        missing = [field for field in RESOLUTION_FIELDS if field not in resolution]
        if missing:
            failures.append(f"{finding_id}: resolution record is missing nullable fields: {missing}")
        if item.get("status") == OPEN_STATUS:
            filled = [field for field in RESOLUTION_FIELDS if resolution.get(field) is not None]
            if filled:
                failures.append(f"{finding_id}: open dependency must keep null resolution fields; found {filled}")
        else:
            # A game dependency may leave the open state only with a complete, inspected
            # resolution — and never by pointing at the commit the audit already rejected.
            empty = [field for field in RESOLUTION_FIELDS if resolution.get(field) in (None, "")]
            if empty:
                failures.append(f"{finding_id}: non-open dependency lacks completed resolution fields: {empty}")
            if resolution.get("resolvedGameCommit") == TRACKER_AUTHORITY["auditedGameCommit"]:
                failures.append(f"{finding_id}: resolvedGameCommit is the audited baseline itself; that is not a remediation")
        if args.expect_editor_ready == 0 and item.get("status") != OPEN_STATUS:
            failures.append(f"{finding_id}: no game dependency may be marked resolved at activation; found status {item.get('status')}")

    resolved_at_activation = {str(item.get("findingId")) for item in tracker.get("sharedSystemFindings", [])
                              if str(item.get("status", "")).startswith("RESOLVED")}
    if resolved_at_activation != {"HHH-SYS-001", "HHH-SYS-002"}:
        failures.append(f"activation resolves exactly HHH-SYS-001 and HHH-SYS-002; tracker resolves {sorted(resolved_at_activation)}")

    blueprint_closures = {str(item.get("findingId")): str(item.get("status"))
                          for item in tracker.get("blueprintDecisionFindings", [])}
    if set(blueprint_closures) != EXPECTED_BLUEPRINT_CLOSURES:
        failures.append(f"tracker must carry exactly the four Blueprint decision findings {sorted(EXPECTED_BLUEPRINT_CLOSURES)}; found {sorted(blueprint_closures)}")
    for finding_id, status in blueprint_closures.items():
        if status != "CLOSED_BY_APPROVED_BLUEPRINT":
            failures.append(f"{finding_id}: Blueprint decision finding must be CLOSED_BY_APPROVED_BLUEPRINT; found {status}")

    return report(failures, len(editor_ready))


def report(failures: list[str], editor_ready: int) -> int:
    payload = {
        "validator": "hhh-activation-v1",
        "status": "PASS" if not failures else "FAIL",
        "units": len(EXPECTED_UNITS),
        "editorReadyEntries": editor_ready,
        "trackedGameDependencies": len(EXPECTED_DEPENDENCIES),
        "requiredBlockingFindings": len(REQUIRED_BLOCKING),
        "failures": failures,
    }
    print(json.dumps(payload, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
