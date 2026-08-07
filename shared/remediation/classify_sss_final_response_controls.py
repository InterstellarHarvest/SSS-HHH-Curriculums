#!/usr/bin/env python3
"""Classify response controls introduced by the final SSS remediation.

The editor's layout contract requires every Student/Accessible response to be
explicitly resizable or locked. The final audit added compact persisted
mark/status/final-choice controls plus one new long-form Hayes Accessible field.

Policy:
- compact B/R, X/status, and final diagnosis controls are locked;
- Hayes Accessible Task 7 long-term independent control is resizable with the
  same bounds as its immediate-action sibling;
- no existing area or override is changed;
- package layoutOverrides hashes are refreshed.

Idempotent.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "shared/implementation/case-registry.v2.json"

LOCKS = {
    "SSS-C1-CASE03": {
        "accessible": [(f"a-t5-mark-{i}", "status") for i in range(1, 5)],
        "student": [(f"s-t5-mark-{i}", "status") for i in range(1, 5)],
    },
    "SSS-C1-CASE04": {
        "accessible": [(f"a-t4-mark-{i}", "status") for i in range(1, 5)],
        "student": [(f"s-t4-mark-{i}", "status") for i in range(1, 5)],
    },
    "SSS-C1-CASE05": {
        "accessible": [("a4-best", "classification")],
        "student": [("t4-best", "classification")],
    },
    "SSS-C1-CASE06": {
        "accessible": [("a5-best", "classification")],
        "student": [("t5-best", "classification")],
    },
    "SSS-C1-CASE07": {
        "accessible": [(f"a4-status-{i}", "status") for i in range(1, 7)] + [("a5-best", "classification")],
        "student": [(f"t4-status-{i}", "status") for i in range(1, 7)] + [("t5-best", "classification")],
    },
}

HAYES_AREA = {
    "id": "SSS-C1-CASE04:accessible:t7:a7-longterm",
    "persistId": "a7-longterm",
    "pageId": "accessible-mission-07",
    "taskId": 7,
    "label": "Long-term independent control",
    "minPx": 32,
    "maxPx": 900,
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packages() -> dict[str, Path]:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    found = {}
    for curriculum in registry["curricula"]:
        if curriculum.get("id") != "SSS":
            continue
        for campaign in curriculum["campaigns"]:
            for case in campaign["cases"]:
                found[case["id"]] = ROOT / case["editorPackage"]
    return found


def ensure_locked(target: dict, persist_id: str, reason: str) -> bool:
    locked = target["lockedAreas"]
    existing = next((item for item in locked if item.get("persistId") == persist_id), None)
    if existing:
        if existing.get("reason") != reason:
            raise ValueError(f"{persist_id} already locked with {existing.get('reason')}, expected {reason}")
        return False
    if any(area.get("persistId") == persist_id for area in target["areas"]):
        raise ValueError(f"{persist_id} is already resize-eligible and cannot also be locked")
    locked.append({"persistId": persist_id, "reason": reason})
    return True


def ensure_hayes_area(data: dict) -> bool:
    if any(item.get("persistId") == "a7-longterm" for item in data["lockedAreas"]):
        raise ValueError("Hayes a7-longterm is locked but must be resize-eligible")
    existing = next((area for area in data["areas"] if area.get("persistId") == "a7-longterm"), None)
    if existing:
        if existing != HAYES_AREA:
            raise ValueError(f"Hayes a7-longterm area differs from final contract: {existing}")
        return False
    data["areas"].append(dict(HAYES_AREA))
    return True


def main() -> int:
    package_map = packages()
    changed_cases = 0
    for case_id, editions in LOCKS.items():
        package_path = package_map[case_id]
        package = json.loads(package_path.read_text(encoding="utf-8"))
        layout_path = ROOT / package["layoutOverrides"]["source"]
        data = json.loads(layout_path.read_text(encoding="utf-8"))
        changed = False

        for persist_id, reason in editions.get("accessible", []):
            changed |= ensure_locked(data, persist_id, reason)
        student = data["student"]
        for persist_id, reason in editions.get("student", []):
            changed |= ensure_locked(student, persist_id, reason)

        if case_id == "SSS-C1-CASE04":
            changed |= ensure_hayes_area(data)

        if changed:
            layout_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            package["sourceHashes"]["layoutOverrides"] = digest(layout_path)
            package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            changed_cases += 1
            print(f"{case_id}: layout contract updated")
        else:
            print(f"{case_id}: layout contract already current")

    print(f"Final response-control classification complete: {changed_cases} case(s) changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
