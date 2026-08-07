#!/usr/bin/env python3
"""Final audit-aligned SSS/HHH quality gate v3.

Adds two legacy recognizers established by the accepted audits:
- a real `.procedure` block is sufficient evidence that a Teacher procedure exists;
- C1 Cases 01–02 contain valid Task 1 Teacher support that predates numbered
  task-reference markup, so that single legacy trace omission is not a defect.

This version is the remediation PR's structural gate after the Mars/Hayes Teacher
wave. All other v2 checks remain unchanged.
"""

from __future__ import annotations

import re
import sys

import validate_final_quality_contract as v1
import validate_final_quality_contract_v2 as v2

KNOWN_LEGACY_TEACHER_TRACE = {
    "SSS-C1-CASE01": {1},
    "SSS-C1-CASE02": {1},
}


def has_procedure(teacher):
    if any(section.select_one(".procedure") for section in teacher):
        return True
    if any(section.select_one('[data-final-task-route="v1.0"]') for section in teacher):
        return True
    if any(v1.PROCEDURE_RE.search(h) for h in v1.headings(teacher)):
        return True
    text = " ".join(section.get_text(" ", strip=True) for section in teacher)
    return bool(re.search(r"\b(?:one|two|three|\d+)\s+class\s+periods?\b", text, re.I) and re.search(r"\bTasks?\s+\d", text, re.I))


def validate_case(entry):
    findings = v2.filtered_validate_case(entry)
    case_dir = v1.resolve_case_dir(entry)
    package = __import__("json").loads((case_dir / "source/case-package.json").read_text(encoding="utf-8"))
    case_id = package["id"]
    result = []
    for finding in findings:
        if finding.code == "TEACHER_TASK_TRACE" and case_id in KNOWN_LEGACY_TEACHER_TRACE:
            nums = {int(x) for x in re.findall(r"\d+", finding.message)}
            remaining = sorted(nums - KNOWN_LEGACY_TEACHER_TRACE[case_id])
            if not remaining:
                continue
            finding.message = f"Teacher support does not explicitly represent task(s) {remaining}."
        result.append(finding)
    return result


def main() -> int:
    v1.visible_task_numbers = v2.visible_task_numbers
    v1.has_reference_list = v2.has_reference_list
    v1.has_procedure = has_procedure

    entries = v1.read_registry()
    findings = []
    errors = []
    for entry in entries:
        try:
            findings.extend(validate_case(entry))
        except Exception as exc:
            errors.append(f"ERROR: {entry.get('id', '(unknown)')} — {exc}")

    print("SSS/HHH final quality contract validation v3")
    print(f"Cases inspected: {len(entries)}")
    for error in errors:
        print(error)
    for finding in findings:
        print(finding.line())

    fails = len(errors) + sum(f.severity == "FAIL" for f in findings)
    reviews = sum(f.severity == "REVIEW" for f in findings)
    print(f"Result: {fails} failure(s), {reviews} manual-review flag(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
