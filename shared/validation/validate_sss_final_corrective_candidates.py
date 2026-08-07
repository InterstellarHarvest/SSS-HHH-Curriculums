#!/usr/bin/env python3
"""Validate the thirteen post-audit SSS corrective-release candidates.

This validator is intentionally candidate-specific. It proves that modified source
no longer masquerades as the previous approved release while every prior release
and owner-approval record remains untouched.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FROZEN_MAIN = "f7a24423f802a095aa149f923d05475ba2837599"
REGISTRY_PATH = ROOT / "shared/implementation/case-registry.v2.json"
OWNER = "Nate / Owner"
VERSION_MAP = {
    "SSS-C1-CASE01": ("1.1", "1.2"), "SSS-C1-CASE02": ("1.0", "1.1"),
    "SSS-C1-CASE03": ("1.1", "1.2"), "SSS-C1-CASE04": ("1.0", "1.1"),
    "SSS-C1-CASE05": ("1.0", "1.1"), "SSS-C1-CASE06": ("1.0", "1.1"),
    "SSS-C1-CASE07": ("1.0", "1.1"), "SSS-C2-CASE01": ("1.1", "1.2"),
    "SSS-C2-CASE02": ("1.1", "1.2"), "SSS-C2-CASE03": ("1.1", "1.2"),
    "SSS-C2-CASE04": ("1.1", "1.2"), "SSS-C2-CASE05": ("1.1", "1.2"),
    "SSS-C2-CASE06": ("1.1", "1.2"),
}

sys.path.insert(0, str(ROOT / "shared/validation"))
from corrective_release_lifecycle import history_findings  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def task_registry(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    payload = re.sub(r"^\s*window\.[A-Z0-9_]+\s*=\s*", "", text).rstrip().removesuffix(";")
    return json.loads(payload)


def approval() -> dict:
    return {"owner": OWNER, "status": "OWNER_REVIEW_NOT_STARTED", "printStatus": "NOT_RUN"}


def flatten(registry: dict) -> list[dict]:
    return [
        case for curriculum in registry["curricula"] if curriculum["id"] == "SSS"
        for campaign in curriculum["campaigns"] for case in campaign["cases"]
    ]


def check(errors: list[str], condition: bool, label: str, detail: object = "") -> None:
    if not condition:
        errors.append(f"FAIL: {label}{' — ' + str(detail) if detail else ''}")


def main() -> int:
    errors: list[str] = []
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    entries = flatten(registry)
    check(errors, {e["id"] for e in entries} == set(VERSION_MAP), "central registry contains exactly the 13 final-audit SSS cases")

    # Historical records are immutable across the entire remediation branch.
    diff = subprocess.run(
        ["git", "diff", "--name-only", FROZEN_MAIN, "HEAD", "--", "sss/campaign-1/*/history", "sss/campaign-2/*/history"],
        cwd=ROOT, text=True, capture_output=True,
    )
    history_changes = [line for line in diff.stdout.splitlines() if line.strip()]
    check(errors, diff.returncode == 0 and not history_changes,
          "no historical release/owner-approval file changed from frozen main", history_changes)

    for entry in entries:
        case_id = entry["id"]
        old, new = VERSION_MAP[case_id]
        package_path = ROOT / entry["editorPackage"]
        package = json.loads(package_path.read_text(encoding="utf-8"))
        case_root = package_path.parent.parent
        task_path = ROOT / package["taskRegistry"]["source"]
        task = task_registry(task_path)

        check(errors, entry["version"] == package["version"] == new,
              f"{case_id} registry/package candidate version is {new}", (entry["version"], package["version"]))
        check(errors, entry["status"] == package["status"] == "DRAFT",
              f"{case_id} registry/package lifecycle is DRAFT")
        check(errors, entry["packageStatus"] == "DRAFT", f"{case_id} central packageStatus is DRAFT")
        check(errors, entry["approval"] == package["approval"] == approval(),
              f"{case_id} owner and print gates are reset", (entry["approval"], package["approval"]))
        check(errors, "historyRecord" not in entry and "releaseHistory" not in package,
              f"{case_id} candidate declares no current release pointer")
        check(errors, "date" not in entry["approval"] and "date" not in package["approval"],
              f"{case_id} candidate has no unearned approval date")

        # Every name/string exposed by the package that embeds a curriculum version
        # should now identify the candidate, not the superseded release.
        check(errors, f":{new}:" in package["documentKey"], f"{case_id} documentKey names candidate version", package["documentKey"])
        check(errors, all(f"v{new}" in value for value in package["outputs"].values()),
              f"{case_id} output names identify candidate version", package["outputs"])
        check(errors, f"v{new}" in package["accessibility"]["documentTitle"]
              and f"v{new}" in package["accessibility"]["loadAnnouncement"],
              f"{case_id} accessibility identity names candidate version")

        source_root = case_root / "source"
        mapping = {
            "content": source_root / "content.html", "presentation": source_root / "presentation.css",
            "taskRegistry": source_root / "task-registry.js", "layoutOverrides": source_root / "layout-overrides.json",
            "icons": source_root / "icons.svg",
        }
        actual = {key: digest(mapping[key]) for key in package["sourceHashes"] if key in mapping and mapping[key].is_file()}
        check(errors, all(package["sourceHashes"].get(k) == v for k, v in actual.items()),
              f"{case_id} sourceHashes certify current candidate source")

        if "version" in task:
            check(errors, task.get("version") == new and task.get("status") == "DRAFT",
                  f"{case_id} task registry identifies candidate lifecycle", (task.get("version"), task.get("status")))
            check(errors, task.get("correctiveOf") == old,
                  f"{case_id} task registry records correctiveOf {old}", task.get("correctiveOf"))
            check(errors, task.get("ownerReviewStatus") == "OWNER_REVIEW_NOT_STARTED"
                  and task.get("printStatus") == "NOT_RUN",
                  f"{case_id} task-registry review/print gates reset")
            check(errors, not any(k in task for k in ("approvalDate", "approvedBy", "mergeStatus", "releaseHistory")),
                  f"{case_id} task registry carries no unearned release-promotion fields")

        lifecycle = history_findings(case_root, case_id, package, task)
        check(errors, not lifecycle, f"{case_id} satisfies shared corrective-release lifecycle", lifecycle)
        check(errors, (case_root / "history" / f"release-v{old}.json").is_file(),
              f"{case_id} retains approved release-v{old}.json")

        candidate_history = list((case_root / "history").glob(f"release-v{new}.json"))
        check(errors, not candidate_history,
              f"{case_id} has no release record for unapproved candidate v{new}", candidate_history)

    print("SSS final corrective-candidate lifecycle validation")
    print(f"Cases inspected: {len(entries)}")
    for error in errors:
        print(error)
    print(f"Result: {len(errors)} failure(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
