#!/usr/bin/env python3
"""Fail unless every current case uses the lean canonical source/history layout."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CAMPAIGN = ROOT / "sss/campaign-1"
FORBIDDEN_DIRS = {
    "master", "published", "reports", "review", "validation-artifacts",
    "editor-package", "editor-phase2", "editor-v1.1", "editor",
}
REQUIRED_SOURCE = {"case-package.json", "content.html", "presentation.css", "task-registry.js"}
ROLES = ["student", "teacher", "answer", "accessible"]


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, check=True, text=True, capture_output=True
    )
    return [line for line in result.stdout.splitlines() if line and (ROOT / line).is_file()]


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)


def main() -> int:
    failures: list[str] = []
    cases = sorted(path for path in CAMPAIGN.glob("case-*") if path.is_dir())
    if [path.name[:7] for path in cases] != ["case-01", "case-02", "case-03"]:
        failures.append(f"expected exactly Cases 01–03; found {[path.name for path in cases]}")

    tracked = tracked_files()
    pdfs = [path for path in tracked if path.lower().endswith(".pdf")]
    if pdfs:
        failures.append(f"tracked PDFs are prohibited: {pdfs}")

    for case in cases:
        top_entries = {path.name for path in case.iterdir()}
        allowed_top = {"README.md", "source", "history", "assets"}
        unexpected = sorted(top_entries - allowed_top)
        if unexpected:
            failures.append(f"{case.name}: unexpected top-level entries: {unexpected}")
        if not (case / "README.md").is_file():
            failures.append(f"{case.name}: README.md is required")
        for path in case.rglob("*"):
            if path.is_dir() and path.name in FORBIDDEN_DIRS:
                failures.append(f"{case.name}: forbidden directory: {path.relative_to(case)}")

        source = case / "source"
        source_files = {path.name for path in source.iterdir() if path.is_file()} if source.is_dir() else set()
        missing = sorted(REQUIRED_SOURCE - source_files)
        if missing:
            failures.append(f"{case.name}: missing canonical source files: {missing}")
            continue
        nested_source_dirs = sorted(str(path.relative_to(case)) for path in source.iterdir() if path.is_dir())
        if nested_source_dirs:
            failures.append(f"{case.name}: nested source directories are not canonical: {nested_source_dirs}")

        package_path = source / "case-package.json"
        try:
            package = json.loads(package_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"{case.name}: invalid case-package.json: {error}")
            continue
        if package.get("supportedRoles") != ROLES:
            failures.append(f"{case.name}: supportedRoles must be exactly {ROLES}")
        if list(package.get("rolePageStructure", {})) != ROLES:
            failures.append(f"{case.name}: rolePageStructure must contain exactly the four roles")
        if list(package.get("outputs", {})) != ["complete", *ROLES]:
            failures.append(f"{case.name}: outputs must contain complete plus exactly the four roles")
        package_text = package_path.read_text(encoding="utf-8")
        if "GRAYSCALE_" in package_text.upper() or '"grayscale": {' in package_text:
            failures.append(f"{case.name}: presentation state is declared as an output/profile")
        forbidden_fields = {
            "historicalMaster", "successorMaster", "goldenMaster", "migrationSource",
            "preMaintenanceMasterSha256", "reconciliationRecord", "phase2Authorization",
        }
        if forbidden_fields.intersection(package):
            failures.append(f"{case.name}: migration-only package fields remain")

        references = set(strings(package))
        for optional in source_files - REQUIRED_SOURCE:
            relative = (source / optional).relative_to(ROOT).as_posix()
            if relative not in references:
                failures.append(f"{case.name}: unreferenced optional source file: {relative}")

        assets = case / "assets"
        if assets.exists():
            asset_files = [path for path in assets.rglob("*") if path.is_file()]
            if not asset_files:
                failures.append(f"{case.name}: empty assets directory is prohibited")
            for asset in asset_files:
                relative = asset.relative_to(ROOT).as_posix()
                if relative not in references:
                    failures.append(f"{case.name}: unreferenced case asset: {relative}")

        history = case / "history"
        records = sorted(history.glob("release-v*.json")) if history.is_dir() else []
        if not records:
            failures.append(f"{case.name}: at least one history/release-vX.json is required")
        if package.get("releaseHistory") not in {path.relative_to(ROOT).as_posix() for path in records}:
            failures.append(f"{case.name}: package releaseHistory does not name a retained record")
        extra_history = sorted(path.name for path in history.iterdir() if path.is_file() and path not in records) if history.is_dir() else []
        if extra_history:
            failures.append(f"{case.name}: unexpected history files: {extra_history}")

        case_prefix = case.relative_to(ROOT).as_posix() + "/"
        case_html = [path for path in tracked if path.startswith(case_prefix) and path.endswith(".html")]
        expected_html = f"{case_prefix}source/content.html"
        if case_html != [expected_html]:
            failures.append(f"{case.name}: stored generated/editable HTML found: {case_html}")

    payload = {
        "validator": "canonical-case-structure-v1",
        "status": "PASS" if not failures else "FAIL",
        "cases": len(cases),
        "failures": failures,
    }
    print(json.dumps(payload, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
