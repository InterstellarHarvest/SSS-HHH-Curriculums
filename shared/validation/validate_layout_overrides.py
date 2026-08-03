#!/usr/bin/env python3
"""Validate Student/Accessible response-area eligibility and sparse overrides."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "shared/implementation/case-registry.v2.json"
PROTECTED_COMPACT_TOKENS = ("criterion", "constraint", "classification", "status")
LOCK_REASONS = {
    "cer",
    "classification",
    "compact-answer",
    "constraint",
    "criterion",
    "fixed-organizer",
    "horizontal-reflow",
    "identity",
    "single-line",
    "status",
    "table-cell",
}
CER_CLASSES = {"canonical-cer", "canonical-cer-box", "cer-stack", "cer-box", "compact-cer"}


def has_cer_ancestor(node) -> bool:
    return any(parent.has_attr("data-cer-contract") or CER_CLASSES.intersection(parent.get("class", [])) for parent in node.parents)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_repo_path(raw: str, *, suffix: str) -> Path:
    if not raw or raw.startswith(("/", "~")) or "\\" in raw:
        raise ValueError(f"unsafe repository path: {raw!r}")
    candidate = (ROOT / raw).resolve()
    candidate.relative_to(ROOT.resolve())
    if not candidate.as_posix().endswith(suffix):
        raise ValueError(f"unexpected source target: {raw!r}")
    return candidate


def package_paths() -> dict[str, Path]:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    found: dict[str, Path] = {}
    for curriculum in registry["curricula"]:
        for campaign in curriculum["campaigns"]:
            for case in campaign["cases"]:
                if case.get("editorPackage"):
                    found[case["id"]] = safe_repo_path(case["editorPackage"], suffix="/source/case-package.json")
    return found


def validate_edition(case_id: str, soup: BeautifulSoup, edition: str, data: dict) -> list[str]:
    errors: list[str] = []
    if set(data) != {"edition", "areas", "lockedAreas", "overrides"}:
        return [f"{case_id}: {edition} layout registry has unexpected or missing fields"]
    if data.get("edition") != edition:
        errors.append(f"{case_id}: {edition} layout registry identity is invalid")
    id_pattern = re.compile(rf"^[A-Z0-9-]+:{edition}:t[0-9]+:[a-z0-9-]+$")
    areas: dict[str, dict] = {}
    persist_ids: set[str] = set()
    for index, area in enumerate(data.get("areas", [])):
        required = {"id", "persistId", "pageId", "taskId", "label", "minPx", "maxPx"}
        if not isinstance(area, dict) or set(area) != required:
            errors.append(f"{case_id}: area {index} has unexpected or missing fields")
            continue
        area_id = area["id"]
        if not isinstance(area_id, str) or not id_pattern.fullmatch(area_id) or not area_id.startswith(f"{case_id}:{edition}:t{area['taskId']}:"):
            errors.append(f"{case_id}: malformed stable area id {area_id!r}")
        if area_id in areas or area["persistId"] in persist_ids:
            errors.append(f"{case_id}: duplicate eligible area identity {area_id!r}")
        areas[area_id] = area
        persist_ids.add(area["persistId"])
        if not all(isinstance(area[key], int) and not isinstance(area[key], bool) for key in ("taskId", "minPx", "maxPx")):
            errors.append(f"{case_id}: non-integer area bounds/task for {area_id}")
            continue
        if area["minPx"] < 16 or area["maxPx"] <= area["minPx"] or area["minPx"] % 4 or area["maxPx"] % 4:
            errors.append(f"{case_id}: invalid 4px bounds for {area_id}")
        matches = soup.select(f'[data-persist-id="{area["persistId"]}"]')
        if len(matches) != 1:
            errors.append(f"{case_id}: {area_id} resolves to {len(matches)} source elements")
            continue
        node = matches[0]
        page = node.find_parent(class_="page")
        if not page or page.get("data-role") != edition or page.get("data-page-id") != area["pageId"]:
            errors.append(f"{case_id}: {area_id} is not on its declared {edition.title()} page")
        task = node.find_previous(lambda tag: tag.name in {"h2", "div"} and (tag.has_attr("data-task-id") or tag.has_attr("data-shell-task-heading")))
        task_number = task.get("data-task-id") if task and task.has_attr("data-task-id") else task.get("data-shell-task-heading") if task else None
        if task_number != str(area["taskId"]):
            errors.append(f"{case_id}: {area_id} is not in its declared task")
        if has_cer_ancestor(node):
            errors.append(f"{case_id}: CER response is forbidden from resize eligibility: {area_id}")
        compact_text = f'{area_id} {area["persistId"]} {area["label"]}'.lower()
        if any(token in compact_text for token in PROTECTED_COMPACT_TOKENS):
            errors.append(f"{case_id}: compact field is forbidden from resize eligibility: {area_id}")
        if not node.has_attr("data-response"):
            errors.append(f"{case_id}: eligible area is not a response field: {area_id}")
        if edition == "student" and node.find_parent(["td", "th"]):
            errors.append(f"{case_id}: compact Student table cell is forbidden from resize eligibility: {area_id}")
    locked_persist_ids: set[str] = set()
    for index, locked in enumerate(data.get("lockedAreas", [])):
        if not isinstance(locked, dict) or set(locked) != {"persistId", "reason"}:
            errors.append(f"{case_id}: locked area {index} has unexpected or missing fields")
            continue
        persist_id = locked["persistId"]
        reason = locked["reason"]
        if not isinstance(persist_id, str) or not re.fullmatch(r"[a-zA-Z0-9-]+", persist_id):
            errors.append(f"{case_id}: malformed locked response locator {persist_id!r}")
            continue
        if reason not in LOCK_REASONS:
            errors.append(f"{case_id}: unrecognized lock reason for {persist_id}: {reason!r}")
        if persist_id in locked_persist_ids:
            errors.append(f"{case_id}: duplicate locked response locator {persist_id}")
        if persist_id in persist_ids:
            errors.append(f"{case_id}: response is both eligible and locked: {persist_id}")
        locked_persist_ids.add(persist_id)
        matches = soup.select(f'[data-persist-id="{persist_id}"]')
        if len(matches) != 1:
            errors.append(f"{case_id}: locked response {persist_id} resolves to {len(matches)} source elements")
            continue
        node = matches[0]
        page = node.find_parent(class_="page")
        if not page or page.get("data-role") != edition or not node.has_attr("data-response"):
            errors.append(f"{case_id}: locked response {persist_id} is not a {edition.title()} response field")
        in_cer = has_cer_ancestor(node)
        if in_cer and reason != "cer":
            errors.append(f"{case_id}: CER response must use the cer lock reason: {persist_id}")
        if reason == "cer" and not in_cer:
            errors.append(f"{case_id}: non-CER response uses the cer lock reason: {persist_id}")
    response_nodes = soup.select(f'.page[data-role="{edition}"] [data-response]')
    source_persist_ids: list[str] = []
    for node in response_nodes:
        persist_id = node.get("data-persist-id")
        if not persist_id:
            errors.append(f"{case_id}: {edition.title()} response is missing data-persist-id")
            continue
        source_persist_ids.append(persist_id)
    duplicates = sorted({persist_id for persist_id in source_persist_ids if source_persist_ids.count(persist_id) > 1})
    for persist_id in duplicates:
        errors.append(f"{case_id}: duplicate {edition.title()} response locator in source: {persist_id}")
    source_set = set(source_persist_ids)
    classified = persist_ids | locked_persist_ids
    for persist_id in sorted(source_set - classified):
        errors.append(f"{case_id}: {edition.title()} response is not classified as eligible or locked: {persist_id}")
    for persist_id in sorted(classified - source_set):
        errors.append(f"{case_id}: classified response is absent from {edition.title()} source: {persist_id}")
    overrides = data.get("overrides")
    if not isinstance(overrides, dict):
        errors.append(f"{case_id}: overrides must be an object")
        return errors
    for area_id, override in overrides.items():
        area = areas.get(area_id)
        if area is None:
            errors.append(f"{case_id}: override uses an unknown area id: {area_id}")
            continue
        if not isinstance(override, dict) or set(override) != {"heightPx", "sourceHeightPx"}:
            errors.append(f"{case_id}: invalid sparse override fields for {area_id}")
            continue
        height = override["heightPx"]
        source = override["sourceHeightPx"]
        if not isinstance(height, int) or isinstance(height, bool) or height % 4 or not area["minPx"] <= height <= area["maxPx"]:
            errors.append(f"{case_id}: override height violates snap/bounds for {area_id}")
        if not isinstance(source, int) or isinstance(source, bool) or source < 16 or source > 2000:
            errors.append(f"{case_id}: invalid source height for {area_id}")
    return errors


def validate_case(case_id: str, package_path: Path) -> list[str]:
    errors: list[str] = []
    package = json.loads(package_path.read_text(encoding="utf-8"))
    if package.get("id") != case_id:
        return [f"{case_id}: package identity mismatch"]
    contract = package.get("layoutOverrides")
    if contract != {"source": contract.get("source") if isinstance(contract, dict) else None, "schemaVersion": 1}:
        return [f"{case_id}: invalid layoutOverrides package contract"]
    try:
        layout_path = safe_repo_path(contract["source"], suffix="/source/layout-overrides.json")
        content_path = safe_repo_path(package["content"]["source"], suffix="/source/content.html")
    except (KeyError, ValueError) as exc:
        return [f"{case_id}: {exc}"]
    if layout_path.parent != package_path.parent or content_path.parent != package_path.parent:
        return [f"{case_id}: package sources must remain in the registered case source directory"]
    if not layout_path.is_file():
        return [f"{case_id}: layout override source is missing"]
    if package.get("sourceHashes", {}).get("layoutOverrides") != digest(layout_path):
        errors.append(f"{case_id}: layout override hash mismatch")
    data = json.loads(layout_path.read_text(encoding="utf-8"))
    expected_fields = {"schemaVersion", "caseId", "edition", "stepPx", "areas", "lockedAreas", "overrides", "student"}
    if set(data) != expected_fields:
        errors.append(f"{case_id}: layout override document has unexpected or missing top-level fields")
        return errors
    if (data["schemaVersion"], data["caseId"], data["edition"], data["stepPx"]) != (1, case_id, "accessible", 4):
        errors.append(f"{case_id}: layout override identity/edition/step is invalid")
    soup = BeautifulSoup(content_path.read_text(encoding="utf-8"), "html.parser")
    accessible = {key: data[key] for key in ("edition", "areas", "lockedAreas", "overrides")}
    errors.extend(validate_edition(case_id, soup, "accessible", accessible))
    errors.extend(validate_edition(case_id, soup, "student", data.get("student")))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", dest="cases", help="Validate only this registered case ID (repeatable)")
    args = parser.parse_args()
    packages = package_paths()
    selected = args.cases or sorted(packages)
    unknown = sorted(set(selected) - packages.keys())
    if unknown:
        print(f"ERROR: unknown cases: {', '.join(unknown)}", file=sys.stderr)
        return 2
    errors = [error for case_id in selected for error in validate_case(case_id, packages[case_id])]
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"Layout override validation: {len(errors)} failure(s), {len(selected)} case(s)")
        return 1
    totals = {"accessible": 0, "student": 0}
    locked_totals = {"accessible": 0, "student": 0}
    for case_id in selected:
        package = json.loads(packages[case_id].read_text(encoding="utf-8"))
        layout_path = safe_repo_path(package["layoutOverrides"]["source"], suffix="/source/layout-overrides.json")
        data = json.loads(layout_path.read_text(encoding="utf-8"))
        totals["accessible"] += len(data["areas"])
        locked_totals["accessible"] += len(data["lockedAreas"])
        totals["student"] += len(data["student"]["areas"])
        locked_totals["student"] += len(data["student"]["lockedAreas"])
    print(
        f"Layout override validation: PASS ({len(selected)} cases; "
        f"Accessible {totals['accessible']} eligible/{locked_totals['accessible']} locked; "
        f"Student {totals['student']} eligible/{locked_totals['student']} locked)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
