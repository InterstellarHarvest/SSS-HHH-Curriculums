#!/usr/bin/env python3
"""Reject noncanonical SAA expansions in current production sources and outputs."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

CANONICAL = "Solar Agricultural Agency"
REJECTED = (
    "Solar Agricultural Authority",
    "Space Agricultural Authority",
    "Space Agricultural Agency",
    "Solar Agriculture Agency",
    "Space Agriculture Authority",
)
TEXT_SUFFIXES = {".html", ".md", ".js", ".json", ".py", ".css", ".txt", ".svg"}
ALLOWED_REJECTED_NAMES = {
    "SAA_CANONICAL_INSTITUTION_NAME_v1.0.5.md",
    "SAA_AGENCY_CANONICALIZATION_HANDOFF.md",
    "CASE03_STRUCTURAL_STRESS_TEST_REPORT.md",
    "SSS_C1_CASE01_GAME_CONTENT_AUDIT.md",
    "VISUAL_STYLE_GUIDE_v1.0.md",
}
SKIP_PARTS = {".git", "node_modules", "__pycache__"}


def is_historical(rel: Path) -> bool:
    """Return true only for superseded, clearly versioned repository records."""
    posix = rel.as_posix()
    return (
        posix.startswith("shared/visual-style-guide/decision-labs/")
        or (
            rel.parent.as_posix() == "shared/visual-style-guide"
            and rel.name.startswith("VISUAL_STYLE_GUIDE_v0.")
        )
        or (
            rel.parent.as_posix() == "sss/audit"
            and rel.name.startswith("SSS_MASTER_AUDIT_v0.")
        )
        or posix == "sss/blueprint/SSS_CURRICULUM_BLUEPRINT_v0.1.md"
        or (
            posix.startswith("sss/campaign-1/case-01-iss-greenhouse/master/")
            and ("_v0.2." in rel.name or "_v0.3." in rel.name)
        )
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    violations: list[tuple[str, str]] = []
    canonical_files = 0
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(root)
        if any(part in SKIP_PARTS for part in rel.parts) or is_historical(rel):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if CANONICAL in text:
            canonical_files += 1
        if path.name in ALLOWED_REJECTED_NAMES or path.name.startswith("validate_"):
            continue
        for variant in REJECTED:
            if variant in text:
                violations.append((rel.as_posix(), variant))
    if violations:
        for path, variant in violations:
            print(f"FAIL: {path}: {variant}")
        return 1
    if canonical_files == 0:
        print(f"FAIL: canonical phrase not found: {CANONICAL}")
        return 1
    print(f"PASS: {CANONICAL}; {canonical_files} current text files contain the canonical name")
    return 0


if __name__ == "__main__":
    sys.exit(main())
