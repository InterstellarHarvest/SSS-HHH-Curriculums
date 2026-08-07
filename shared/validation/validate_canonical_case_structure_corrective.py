#!/usr/bin/env python3
"""Corrective-release-aware wrapper for canonical case structure validation.

`validate_canonical_case_structure.py` predates the repository's formal reopened-
release lifecycle. Its unreleased branch still rejects *any* retained history,
although `corrective_release_lifecycle.py` now correctly requires superseded
approved release records to survive when an approved package is reopened.

This wrapper deliberately preserves the legacy validator as the structural
engine. It suppresses only the obsolete per-case failure:

    unreleased package must not contain or declare release history

and only when the shared corrective-release lifecycle independently proves that:
- the package is unreleased;
- it has no current `releaseHistory` pointer;
- no release/owner-approval record exists for the candidate's own version;
- every retained record belongs to a strictly earlier approved version;
- retained approvals have matching retained release records.

Every other canonical-structure failure remains fatal unchanged.
"""
from __future__ import annotations

import contextlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATION = Path(__file__).resolve().parent
sys.path.insert(0, str(VALIDATION))

import corrective_release_lifecycle as lifecycle  # noqa: E402
import validate_canonical_case_structure as legacy  # noqa: E402

OBSOLETE_SUFFIX = ": unreleased package must not contain or declare release history"


def _task_registry(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    payload = re.sub(r"^\s*window\.[A-Z0-9_]+\s*=\s*", "", text).rstrip().removesuffix(";")
    return json.loads(payload)


def corrective_case_keys() -> tuple[set[str], list[str]]:
    """Return cases eligible for the one legacy exception, plus any lifecycle errors."""
    eligible: set[str] = set()
    errors: list[str] = []
    roster, roster_failures = legacy.registered_roster()
    errors.extend(roster_failures)

    for campaign_id, case_id, case_root in roster:
        package_path = case_root / "source/case-package.json"
        task_path = case_root / "source/task-registry.js"
        try:
            package = json.loads(package_path.read_text(encoding="utf-8"))
            task = _task_registry(task_path)
        except Exception as exc:
            errors.append(f"{campaign_id}/{case_root.name[:7]}: candidate lifecycle precheck failed: {exc}")
            continue

        if package.get("status") == "APPROVED_STABLE":
            continue
        findings = lifecycle.history_findings(case_root, case_id, package, task)
        if findings:
            errors.extend(f"{campaign_id}/{case_root.name[:7]}: {finding}" for finding in findings)
            continue

        history = case_root / "history"
        retained_release = any(history.glob("release-v*.json")) if history.is_dir() else False
        if retained_release:
            eligible.add(legacy.case_key_of(campaign_id, case_root))
    return eligible, errors


def run_legacy() -> tuple[int, dict]:
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        code = legacy.main()
    raw = stream.getvalue().strip()
    try:
        report = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"legacy canonical validator did not emit JSON: {exc}: {raw[-1000:]}") from exc
    return code, report


def main() -> int:
    eligible, lifecycle_errors = corrective_case_keys()
    _, report = run_legacy()

    original_failures = list(report.get("failures", []))
    kept: list[str] = []
    suppressed: list[str] = []
    for failure in original_failures:
        if not failure.endswith(OBSOLETE_SUFFIX):
            kept.append(failure)
            continue
        case_key = failure[: -len(OBSOLETE_SUFFIX)]
        if case_key in eligible:
            suppressed.append(failure)
        else:
            kept.append(failure)

    kept.extend(f"corrective lifecycle: {error}" for error in lifecycle_errors)
    report["validator"] = "canonical-case-structure-corrective-v1"
    report["legacyValidator"] = "canonical-case-structure-v1"
    report["correctiveHistoryExceptions"] = {
        "eligibleCases": sorted(eligible),
        "suppressedLegacyFailures": suppressed,
    }
    report["failures"] = kept
    report["status"] = "PASS" if not kept else "FAIL"

    print(json.dumps(report, indent=2))
    return 1 if kept else 0


if __name__ == "__main__":
    raise SystemExit(main())
