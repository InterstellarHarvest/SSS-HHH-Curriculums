#!/usr/bin/env python3
"""Validate the owner-authorized Phase 2 HTML-baseline reconciliation."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASELINE = "7b5b724b4941a7ad926fe1b0d644f6905ff55067"
RECORDS = {
    "SSS-C1-CASE01": ROOT / "sss/campaign-1/case-01-iss-greenhouse/CASE01_CURRENT_HTML_RECONCILIATION_2026-07-31.json",
    "SSS-C1-CASE02": ROOT / "sss/campaign-1/case-02-lunar-greenhouse/CASE02_CURRENT_HTML_RECONCILIATION_2026-07-31.json",
}
EXPECTED = {
    "SSS-C1-CASE01": ("1.1", "737239b53ae5af3f25cbaf037d0c9882f50d9e7e8d26b3d03408e469ced6b56f", "f42365e58802201679b5cd751f102d9a4ecd0ea6f6a6565a860df070018ad02a"),
    "SSS-C1-CASE02": ("1.0", "4e5d03a62cba494ae09604194f69578b4c4bcceeeca1f9d53d818109e132fd0d", "d35c3e0d83a61cbf56799e52b6a1eb3fac4668c1089b674ad0681e92bf30ad86"),
}
PROTECTED_ROOTS = (
    "sss/campaign-1/case-01-iss-greenhouse/",
    "sss/campaign-1/case-02-lunar-greenhouse/",
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, stdout=subprocess.PIPE).stdout


def protected(path: str) -> bool:
    if not path.startswith(PROTECTED_ROOTS):
        return False
    if "/source/editor-phase2/" in path or "/source/editor-package/" in path:
        return False
    return (
        "/master/" in path and path.endswith(".html")
        or "/published/" in path and (path.endswith(".html") or path.endswith(".pdf"))
        or "/source/" in path
        or path.endswith(".pdf")
    )


def find_case(registry: dict, case_id: str) -> dict:
    for curriculum in registry["curricula"]:
        for campaign in curriculum["campaigns"]:
            for case in campaign["cases"]:
                if case["id"] == case_id:
                    return case
    raise AssertionError(f"registry case missing: {case_id}")


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, condition: bool, detail: object = "") -> None:
        checks.append((name, bool(condition), str(detail)))

    registry = json.loads((ROOT / "shared/implementation/case-registry.v1.json").read_text())
    summary = json.loads((ROOT / "sss/campaign-1/CASE01_CASE02_FINAL_RELEASE_SUMMARY.json").read_text())
    check("earlier summary classified historical", summary.get("record_classification") == "PRE_MAINTENANCE_PRINT_APPROVED_HISTORICAL")

    for case_id, record_path in RECORDS.items():
        record = json.loads(record_path.read_text())
        version, master_hash, historical_hash = EXPECTED[case_id]
        case = find_case(registry, case_id)
        master = record["currentMaster"]
        check(f"{case_id} version", record["curriculumVersion"] == version == case["version"])
        check(f"{case_id} owner status", record["status"] == case.get("ownerAuthorization") == "OWNER_AUTHORIZED_FOR_PHASE2")
        check(f"{case_id} current classification", record["classification"] == "CURRENT_HTML_MIGRATION_BASELINE")
        check(f"{case_id} physical print gate", record["physicalPrintGate"] == case.get("physicalPrintGate") == "OPEN")
        check(f"{case_id} no new curriculum version", record["newCurriculumVersionCreated"] is False)
        check(f"{case_id} historical evidence not inherited", record["historicalPrintEvidencePreservedButNotInherited"] is True)
        check(f"{case_id} current parity target", record["currentHtmlIsParityTarget"] is True)
        check(f"{case_id} registry master path", master["path"] == case["master"])
        check(f"{case_id} registry record path", str(record_path.relative_to(ROOT)) == case["reconciliationRecord"])
        actual_master = digest((ROOT / master["path"]).read_bytes())
        check(f"{case_id} exact master hash", master["sha256"] == case["currentMasterSha256"] == actual_master == master_hash, actual_master)
        check(f"{case_id} earlier master retained as historical", record["preMaintenancePrintApprovedHistorical"]["masterSha256"] == historical_hash)
        check(f"{case_id} five roles", set(record["currentRoles"]) == {"student", "teacher", "answer", "accessible", "grayscale"})
        for role, artifact in record["currentRoles"].items():
            actual = digest((ROOT / artifact["path"]).read_bytes())
            check(f"{case_id} {role} role hash", actual == artifact["sha256"], actual)
            check(f"{case_id} {role} registry path", artifact["path"] == case["roles"][role])
        for artifact in record["historicalPdfs"]:
            actual = digest((ROOT / artifact["path"]).read_bytes())
            check(f"historical PDF {artifact['path']}", actual == artifact["sha256"], actual)

    baseline_paths = {p for p in git("ls-tree", "-r", "--name-only", BASELINE).decode().splitlines() if protected(p)}
    current_paths = {p for p in git("ls-files").decode().splitlines() if protected(p)}
    check("no protected curriculum artifact added or removed", baseline_paths == current_paths, sorted(baseline_paths ^ current_paths))
    for path in sorted(baseline_paths & current_paths):
        before = git("show", f"{BASELINE}:{path}")
        after = (ROOT / path).read_bytes()
        check(f"baseline-protected bytes {path}", before == after)

    failures = [item for item in checks if not item[1]]
    print(f"Phase 2 reconciliation: {len(checks) - len(failures)}/{len(checks)} PASS")
    for name, passed, detail in checks:
        if not passed:
            print(f"FAIL: {name}: {detail}")
    if failures:
        return 1
    print("Current HTML baselines are owner-authorized; historical PDFs and protected curriculum bytes are unchanged; no PDFs were generated or modified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
