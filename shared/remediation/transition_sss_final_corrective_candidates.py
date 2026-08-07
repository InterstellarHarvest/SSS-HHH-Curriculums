#!/usr/bin/env python3
"""Transition all remediated SSS packages into formal corrective-release candidates.

The final unified audit changed canonical curriculum source after the prior releases
were approved. Those modified sources must not continue to advertise the old
released version. This script performs the repository's established corrective
release transition without touching any historical release or owner-approval file.

Rules:
- increment the two-component curriculum version by one minor component;
- package + central registry become DRAFT / owner review not started / print not run;
- remove current releaseHistory/historyRecord pointers only;
- preserve all prior history files byte-for-byte;
- update document/output version strings and current source hashes;
- update task-registry lifecycle metadata only where that registry already has it;
- preserve gameCommit, auditCommit, science ledgers, task content and runtime IDs.

Idempotent: once a case is at the target candidate version/state, re-running makes
no additional change.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "shared/implementation/case-registry.v2.json"
OWNER = "Nate / Owner"

VERSION_MAP = {
    "SSS-C1-CASE01": ("1.1", "1.2"),
    "SSS-C1-CASE02": ("1.0", "1.1"),
    "SSS-C1-CASE03": ("1.1", "1.2"),
    "SSS-C1-CASE04": ("1.0", "1.1"),
    "SSS-C1-CASE05": ("1.0", "1.1"),
    "SSS-C1-CASE06": ("1.0", "1.1"),
    "SSS-C1-CASE07": ("1.0", "1.1"),
    "SSS-C2-CASE01": ("1.1", "1.2"),
    "SSS-C2-CASE02": ("1.1", "1.2"),
    "SSS-C2-CASE03": ("1.1", "1.2"),
    "SSS-C2-CASE04": ("1.1", "1.2"),
    "SSS-C2-CASE05": ("1.1", "1.2"),
    "SSS-C2-CASE06": ("1.1", "1.2"),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_task_registry(path: Path) -> tuple[str, dict]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\s*window\.([A-Z0-9_]+)\s*=\s*", text)
    if not m:
        raise ValueError(f"Unsupported task-registry assignment in {path}")
    global_name = m.group(1)
    payload = re.sub(r"^\s*window\.[A-Z0-9_]+\s*=\s*", "", text).rstrip().removesuffix(";")
    return global_name, json.loads(payload)


def write_task_registry(path: Path, global_name: str, data: dict) -> None:
    path.write_text(f"window.{global_name} = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n", encoding="utf-8")


def replace_version(value: str, old: str, new: str) -> str:
    return value.replace(f"v{old}", f"v{new}").replace(f":{old}:", f":{new}:").replace(f" {old} ", f" {new} ")


def candidate_approval() -> dict:
    return {"owner": OWNER, "status": "OWNER_REVIEW_NOT_STARTED", "printStatus": "NOT_RUN"}


def flatten_sss_entries(registry: dict) -> list[dict]:
    for curriculum in registry["curricula"]:
        if curriculum["id"] == "SSS":
            return [case for campaign in curriculum["campaigns"] for case in campaign["cases"]]
    return []


def transition_case(entry: dict) -> list[str]:
    case_id = entry["id"]
    old, new = VERSION_MAP[case_id]
    package_path = ROOT / entry["editorPackage"]
    case_root = package_path.parent.parent
    package = json.loads(package_path.read_text(encoding="utf-8"))
    task_path = ROOT / package["taskRegistry"]["source"]
    global_name, task = load_task_registry(task_path)
    ops: list[str] = []

    current_version = package.get("version")
    if current_version not in {old, new}:
        raise ValueError(f"{case_id}: expected released {old} or candidate {new}, found {current_version}")

    # Task registries from early C1 predate lifecycle metadata. Change them only
    # when they already declare lifecycle/version state.
    task_changed = False
    if "version" in task:
        if task.get("version") != new:
            if task.get("version") not in {old, new}:
                raise ValueError(f"{case_id}: task registry version {task.get('version')} is outside transition")
            task["version"] = new
            task_changed = True
        if task.get("status") != "DRAFT":
            task["status"] = "DRAFT"
            task_changed = True
        if task.get("correctiveOf") != old:
            task["correctiveOf"] = old
            task_changed = True
        for key in ("approvalDate", "approvedBy", "mergeStatus", "releaseHistory"):
            if key in task:
                task.pop(key)
                task_changed = True
        if task.get("ownerReviewStatus") != "OWNER_REVIEW_NOT_STARTED":
            task["ownerReviewStatus"] = "OWNER_REVIEW_NOT_STARTED"
            task_changed = True
        if task.get("printStatus") != "NOT_RUN":
            task["printStatus"] = "NOT_RUN"
            task_changed = True
    if task_changed:
        write_task_registry(task_path, global_name, task)
        ops.append("task registry -> corrective DRAFT lifecycle")

    if package.get("version") != new:
        package["version"] = new
        ops.append(f"package version {old} -> {new}")
    if package.get("status") != "DRAFT":
        package["status"] = "DRAFT"
        ops.append("package status -> DRAFT")
    if package.get("approval") != candidate_approval():
        package["approval"] = candidate_approval()
        ops.append("package owner/print gate reset")
    if "releaseHistory" in package:
        package.pop("releaseHistory")
        ops.append("removed current releaseHistory pointer")

    package["documentKey"] = replace_version(package["documentKey"], old, new)
    for key, filename in list(package["outputs"].items()):
        package["outputs"][key] = replace_version(filename, old, new)
    for key in ("documentTitle", "loadAnnouncement"):
        package["accessibility"][key] = replace_version(package["accessibility"][key], old, new)

    source_root = case_root / "source"
    source_files = {
        "content": source_root / "content.html",
        "presentation": source_root / "presentation.css",
        "taskRegistry": source_root / "task-registry.js",
        "layoutOverrides": source_root / "layout-overrides.json",
        "icons": source_root / "icons.svg",
    }
    for key in list(package["sourceHashes"]):
        path = source_files.get(key)
        if path and path.is_file():
            package["sourceHashes"][key] = digest(path)
    package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if entry.get("version") != new:
        entry["version"] = new
        ops.append("central registry version updated")
    entry["status"] = "DRAFT"
    entry["packageStatus"] = "DRAFT"
    entry["approval"] = candidate_approval()
    entry.pop("historyRecord", None)

    # The script must never touch history. Presence of the released record is a
    # precondition proving this is a correction of a genuine prior release.
    released = case_root / "history" / f"release-v{old}.json"
    if not released.is_file():
        raise FileNotFoundError(f"{case_id}: missing retained release-v{old}.json")
    return ops


def main() -> int:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    entries = flatten_sss_entries(registry)
    if {entry["id"] for entry in entries} != set(VERSION_MAP):
        raise SystemExit("Registered SSS case roster does not match the 13-case transition map")

    changed = 0
    for entry in entries:
        before = json.dumps(entry, sort_keys=True)
        ops = transition_case(entry)
        after = json.dumps(entry, sort_keys=True)
        changed += int(before != after or bool(ops))
        print(f"{entry['id']}: {'; '.join(ops) if ops else 'already candidate'}")

    REGISTRY_PATH.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"SSS corrective candidate transition complete: {changed} case(s) changed or reconfirmed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
