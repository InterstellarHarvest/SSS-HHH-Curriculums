#!/usr/bin/env python3
"""Create or validate the immutable Case 01/02 Phase 2 artifact ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
LEDGER = REPO / "shared/implementation/phase2-protected-artifacts.v1.json"
PROTECTED_AT = "63364fb4e6bc6f7639b861d9ae570f49e5d224ff"
CASE_ROOTS = {
    "SSS-C1-CASE01": REPO / "sss/campaign-1/case-01-iss-greenhouse",
    "SSS-C1-CASE02": REPO / "sss/campaign-1/case-02-lunar-greenhouse",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def category(path: Path, root: Path) -> str | None:
    relative = path.relative_to(root)
    parts = relative.parts
    name = path.name
    if name == ".DS_Store" or "phase2" in parts or "editor-phase2" in parts or "editor-package" in parts:
        return None
    if path.suffix.lower() == ".pdf":
        return "historical-pdf"
    if parts[0] == "master":
        return "approved-master" if path.suffix.lower() == ".html" else "master-record"
    if parts[0] == "published" and path.suffix.lower() == ".html":
        return "approved-role-html"
    if parts[0] in {"source", "assets"}:
        return "controlled-source"
    if "MANIFEST" in name or name == "manifest.json":
        return "release-manifest"
    if parts[0] in {"reports", "validation-artifacts"}:
        if path.suffix.lower() in {".py", ".mjs"} or name == "requirements.txt":
            return None
        return "validation-record"
    if "PRINT" in name or "OWNER" in name:
        return "owner-print-record"
    if "RECONCILIATION" in name:
        return "reconciliation-record"
    return None


def discover() -> list[dict[str, str]]:
    records = []
    for case_id, root in CASE_ROOTS.items():
        for path in sorted(item for item in root.rglob("*") if item.is_file()):
            kind = category(path, root)
            if kind:
                records.append({
                    "caseId": case_id,
                    "category": kind,
                    "path": path.relative_to(REPO).as_posix(),
                    "sha256": digest(path),
                })
    return records


def build_ledger() -> dict:
    artifacts = discover()
    counts = {}
    for item in artifacts:
        counts[item["category"]] = counts.get(item["category"], 0) + 1
    return {
        "schemaVersion": 1,
        "protectedAtCommit": PROTECTED_AT,
        "policy": "IMMUTABLE_DURING_PHASE2_MIGRATION",
        "pdfPolicy": "NO_GENERATION_OR_MODIFICATION",
        "artifacts": artifacts,
        "countsByCategory": dict(sorted(counts.items())),
        "totalArtifacts": len(artifacts),
    }


def validate() -> tuple[int, int, list[str]]:
    expected = json.loads(LEDGER.read_text())
    failures = []
    actual = discover()
    declared = expected.get("artifacts", [])
    actual_by_path = {item["path"]: item for item in actual}
    declared_by_path = {item["path"]: item for item in declared}
    checks = 4 + len(declared)
    if expected.get("schemaVersion") != 1:
        failures.append("schemaVersion is not 1")
    if expected.get("protectedAtCommit") != PROTECTED_AT:
        failures.append("protectedAtCommit changed")
    if expected.get("policy") != "IMMUTABLE_DURING_PHASE2_MIGRATION":
        failures.append("immutable policy changed")
    if expected.get("pdfPolicy") != "NO_GENERATION_OR_MODIFICATION":
        failures.append("PDF policy changed")
    for path, item in declared_by_path.items():
        current = actual_by_path.get(path)
        if current is None:
            failures.append(f"protected artifact missing: {path}")
        elif current != item:
            failures.append(f"protected artifact changed: {path}")
    extra_pdfs = sorted(
        path for path, item in actual_by_path.items()
        if item["category"] == "historical-pdf" and path not in declared_by_path
    )
    checks += 1
    if extra_pdfs:
        failures.extend(f"undeclared PDF generated: {path}" for path in extra_pdfs)
    checks += 1
    if len(actual_by_path) != len(declared_by_path):
        unexpected = sorted(set(actual_by_path) - set(declared_by_path))
        failures.extend(f"new protected-category artifact is undeclared: {path}" for path in unexpected)
    return checks - len(failures), checks, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Create the ledger at the reconciled baseline")
    args = parser.parse_args()
    if args.write:
        LEDGER.write_text(json.dumps(build_ledger(), indent=2) + "\n")
        print(f"Wrote {LEDGER.relative_to(REPO)}")
        return 0
    passed, total, failures = validate()
    print(f"Phase 2 protected-artifact inventory: {passed}/{total} PASS" if not failures else f"Phase 2 protected-artifact inventory: {passed}/{total} FAIL")
    for failure in failures:
        print(f"- {failure}")
    return int(bool(failures))


if __name__ == "__main__":
    sys.exit(main())
