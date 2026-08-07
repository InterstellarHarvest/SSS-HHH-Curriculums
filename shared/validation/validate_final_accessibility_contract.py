#!/usr/bin/env python3
"""Validate the audit-specific SSS Accessible remediation wave.

Unlike the broad quality gate, this validator does not infer quality from response
counts. It checks the exact adaptations accepted in the thirteen stable case
audits and confirms that final synthesis/CER work remains learner-owned.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from bs4 import BeautifulSoup, Tag

import validate_final_quality_contract as quality

ROOT = Path(__file__).resolve().parents[2]

# Required modeled/prefilled controls for the tasks the accepted audits actually
# identified as under-scaffolded. A value may have been populated by an earlier
# deterministic wave; any explicit data-prefilled marker is accepted.
REQUIRED_PREFILLS = {
    "SSS-C1-CASE02": [
        "response-accessible-task3-step1",
        "response-accessible-task3-step6",
        "response-accessible-task5-regolith-class",
        "response-accessible-task5-regolith-reason",
        "response-accessible-task5-pollination-class",
    ],
    "SSS-C1-CASE04": ["a5-2"],
    "SSS-C1-CASE05": ["a5-2", "a5-4"],
    "SSS-C1-CASE06": ["a5-damage", "a6-disable"],
    "SSS-C1-CASE07": ["a4-source", "a4-status-1", "a5-light", "a7-monitor"],
    "SSS-C2-CASE01": ["a5-c1", "a5-l1", "a5-c3", "a6-d1"],
    "SSS-C2-CASE02": ["a5-c1", "a5-l1", "a5-c3", "a6-d1"],
    "SSS-C2-CASE03": ["a5-c1", "a5-l1", "a5-c3"],
    "SSS-C2-CASE04": ["a5-c1", "a5-l1", "a5-c3"],
    "SSS-C2-CASE05": ["a4-c1", "a4-l1", "a4-c3", "a5-nutrient", "a5-m3"],
    "SSS-C2-CASE06": ["a4-c1", "a4-l1", "a4-c3", "a3-ph"],
}

# These remain the learner's independent synthesis/explanation products.
MUST_REMAIN_BLANK = {
    "SSS-C1-CASE02": ["response-accessible-task5-pollination-reason"],
    "SSS-C1-CASE04": ["a6c", "a6e", "a6r", "a7", "a7-longterm"],
    "SSS-C1-CASE05": ["a6c", "a6e", "a6r"],
    "SSS-C1-CASE06": ["a5-convergence", "a6-recommend", "a6-monitor", "a7c", "a7e", "a7r"],
    "SSS-C1-CASE07": ["a5-convergence", "a6c", "a6e", "a6r", "a7-recommend", "a7-predict"],
    "SSS-C2-CASE01": ["a5-synthesis", "a7c", "a7e", "a7r"],
    "SSS-C2-CASE02": ["a7c", "a7e", "a7r"],
    "SSS-C2-CASE03": ["a5-synthesis", "a7c", "a7e", "a7r"],
    "SSS-C2-CASE04": ["a5-synthesis", "a7c", "a7e", "a7r"],
    "SSS-C2-CASE05": ["a4-synthesis", "a6c", "a6e", "a6r"],
    "SSS-C2-CASE06": ["a4-synthesis", "a5-limit", "a6c", "a6e", "a6r"],
}

BEST_DIAGNOSIS_FIELDS = {
    "SSS-C1-CASE05": ("t4-best", "a4-best"),
    "SSS-C1-CASE06": ("t5-best", "a5-best"),
    "SSS-C1-CASE07": ("t5-best", "a5-best"),
}


def load_case(entry: dict) -> tuple[str, BeautifulSoup]:
    case_dir = quality.resolve_case_dir(entry)
    package = json.loads((case_dir / "source/case-package.json").read_text(encoding="utf-8"))
    content = ROOT / package["content"]["source"]
    return package["id"], BeautifulSoup(content.read_text(encoding="utf-8"), "html.parser")


def node(soup: BeautifulSoup, persist_id: str) -> Tag | None:
    found = soup.find(attrs={"data-persist-id": persist_id})
    return found if isinstance(found, Tag) else None


def fail(errors: list[str], case_id: str, message: str) -> None:
    errors.append(f"FAIL: {case_id} — {message}")


def validate_case(entry: dict) -> list[str]:
    case_id, soup = load_case(entry)
    errors: list[str] = []

    for pid in REQUIRED_PREFILLS.get(case_id, []):
        control = node(soup, pid)
        if control is None:
            fail(errors, case_id, f"required Accessible scaffold control `{pid}` is missing")
            continue
        if not control.get("data-prefilled"):
            fail(errors, case_id, f"required Accessible scaffold `{pid}` is not marked as prefilled/modeled")
        if not control.get_text(" ", strip=True):
            fail(errors, case_id, f"required Accessible scaffold `{pid}` has no visible modeled content")

    for pid in MUST_REMAIN_BLANK.get(case_id, []):
        control = node(soup, pid)
        if control is None:
            fail(errors, case_id, f"learner-owned response `{pid}` is missing")
            continue
        if control.get("data-prefilled") or control.get_text(" ", strip=True):
            fail(errors, case_id, f"learner-owned response `{pid}` was prefilled")

    for pid in BEST_DIAGNOSIS_FIELDS.get(case_id, ()):
        control = node(soup, pid)
        if control is None or not control.has_attr("data-response"):
            fail(errors, case_id, f"persisted final best-diagnosis field `{pid}` is missing")

    if case_id == "SSS-C1-CASE04":
        teacher_text = " ".join(x.get_text(" ", strip=True) for x in soup.select('[data-role="teacher"]'))
        if "six-page Accessible Mission" in teacher_text:
            fail(errors, case_id, "Teacher still calls the approved seven-page Accessible Mission six pages")
        if "seven-page Accessible Mission" not in teacher_text:
            fail(errors, case_id, "Teacher does not identify the approved seven-page Accessible Mission")
        if node(soup, "a7-longterm") is None:
            fail(errors, case_id, "Accessible Task 7 has not been restored to separate immediate and long-term fields")

    if case_id == "SSS-C1-CASE07":
        for prefix in ("t4-status", "a4-status"):
            for idx in range(1, 7):
                pid = f"{prefix}-{idx}"
                control = node(soup, pid)
                if control is None or not control.has_attr("data-response"):
                    fail(errors, case_id, f"Task 4 stage-status control `{pid}` is missing")
        # Only the Accessible first missing status is modeled; the remaining
        # statuses and all Student statuses stay learner-owned.
        for pid in [f"t4-status-{i}" for i in range(1, 7)] + [f"a4-status-{i}" for i in range(2, 7)]:
            control = node(soup, pid)
            if control is not None and (control.get("data-prefilled") or control.get_text(" ", strip=True)):
                fail(errors, case_id, f"stage-status `{pid}` should remain learner-owned")

    return errors


def main() -> int:
    errors: list[str] = []
    entries = quality.read_registry()
    for entry in entries:
        try:
            errors.extend(validate_case(entry))
        except Exception as exc:
            errors.append(f"ERROR: {entry.get('id', '(unknown)')} — {exc}")

    print("SSS final audit-specific accessibility validation")
    print(f"Cases inspected: {len(entries)}")
    for error in errors:
        print(error)
    print(f"Result: {len(errors)} failure(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
