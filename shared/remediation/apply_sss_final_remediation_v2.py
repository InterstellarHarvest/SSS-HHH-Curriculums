#!/usr/bin/env python3
"""Idempotent wrapper for the final SSS remediation transformer.

The v1 transformer performs the substantive source remediations. This wrapper
normalizes the one legacy insertion whose text guard was not structural, so a
second remediation pass produces no repository diff. It is intentionally small
and can be retired once the underlying v1 helper is consolidated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from bs4 import BeautifulSoup, Tag

import apply_sss_final_remediation as v1


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_case03_alternative_block(case_dir: Path, apply: bool) -> bool:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    original = content_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(original, "html.parser")

    blocks = list(soup.select('[data-final-c1c3-alternatives="v1.0"]'))
    changed = False
    if len(blocks) > 1:
        for duplicate in blocks[1:]:
            duplicate.decompose()
        changed = True

    if changed and apply:
        content_path.write_text(soup.decode(formatter="minimal"), encoding="utf-8")
        package = json.loads(package_path.read_text(encoding="utf-8"))
        if "sourceHashes" in package and "content" in package["sourceHashes"]:
            package["sourceHashes"]["content"] = sha256(content_path)
        package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--case", action="append", dest="cases")
    args = parser.parse_args()

    selected = args.cases or list(v1.CASE_DIRS)
    changed_cases = 0

    for case_id in selected:
        case_dir = v1.CASE_DIRS.get(case_id)
        if case_dir is None:
            print(f"ERROR unknown case id: {case_id}")
            return 2

        changed, operations = v1.remediate_case(case_id, case_dir, args.apply)
        normalized = False
        if case_id == "SSS-C1-CASE03":
            normalized = normalize_case03_alternative_block(case_dir, args.apply)

        net_changed = bool(changed or normalized)
        changed_cases += int(net_changed)
        print(f"{case_id}: {'CHANGE' if net_changed else 'NO CHANGE'}")
        for op in operations:
            print(f"  - {op}")
        if normalized:
            print("  - normalized duplicate Mars Habitat alternative-rejection guidance")

    print(f"SSS final remediation v2: {'applied' if args.apply else 'planned'}; {changed_cases} case package(s) changed/planned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
