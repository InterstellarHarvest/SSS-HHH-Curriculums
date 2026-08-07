#!/usr/bin/env python3
"""Validate the post-audit SSS/HHH cross-edition production contracts.

This gate supplements — and does not replace — release, geometry, browser, PDF,
source-hash, or case-specific validation. It mechanizes defect classes identified
by the final SSS Campaign 1 + Campaign 2 audit.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "shared/implementation/case-registry.v2.json"
REQUIRED_ROLES = ("student", "teacher", "answer", "accessible")
PROCEDURE_RE = re.compile(r"\b(?:procedure|lesson\s+flow|pacing|running\s+the\s+packet|class\s+period|teaching\s+procedure|task\s+route)\b", re.I)
SOURCE_RE = re.compile(r"\b(?:authoritative\s+science\s+references?|science[- ]source\s+ledger|references?|sources?)\b", re.I)
ACTION_RE = re.compile(r"\b(?:mark|circle|select|choose|put\s+an?\s+x|write\s+[A-Z]\s+next\s+to|rank)\b", re.I)


@dataclass
class Finding:
    severity: str
    case_id: str
    code: str
    message: str

    def line(self) -> str:
        return f"{self.severity}: {self.case_id} {self.code} — {self.message}"


def load_js_object(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError(f"No object literal found in {path}")
    return json.loads(text[start : end + 1])


def read_registry() -> list[dict]:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    if isinstance(data.get("cases"), list):
        return data["cases"]
    result: list[dict] = []
    for curriculum in data.get("curricula", []):
        if curriculum.get("id") != "SSS":
            continue
        for campaign in curriculum.get("campaigns", []):
            result.extend(campaign.get("cases", []))
    if not result:
        raise ValueError("No SSS cases found in case-registry.v2.json")
    return result


def resolve_case_dir(entry: dict) -> Path:
    package = entry.get("editorPackage") or entry.get("package") or entry.get("casePackage")
    if package:
        p = ROOT / package
        if p.is_file():
            return p.parent.parent if p.parent.name == "source" else p.parent
    case_id = entry.get("id", "")
    m = re.fullmatch(r"SSS-C(\d+)-CASE(\d+)", case_id)
    if m:
        campaign, number = map(int, m.groups())
        candidates = sorted((ROOT / f"sss/campaign-{campaign}").glob(f"case-{number:02d}-*"))
        if len(candidates) == 1:
            return candidates[0]
    raise ValueError(f"Cannot resolve canonical directory for {case_id or entry}")


def role_sections(soup: BeautifulSoup, role: str) -> list[Tag]:
    return list(soup.select(f'[data-role="{role}"]'))


def role_text(soup: BeautifulSoup, role: str) -> str:
    return "\n".join(s.get_text(" ", strip=True) for s in role_sections(soup, role))


def registry_task_numbers(registry: dict, keyed_only: bool = False) -> list[int]:
    result: list[int] = []
    for task in registry.get("tasks", []):
        if keyed_only and not task.get("keyed", True):
            continue
        raw = task.get("number")
        m = re.search(r"\d+", str(raw)) if raw is not None else None
        if m:
            result.append(int(m.group()))
    return result


def visible_task_numbers(sections: Iterable[Tag]) -> set[int]:
    result: set[int] = set()
    for section in sections:
        for node in section.select("[data-task-id], [data-shell-task-heading]"):
            raw = node.get("data-task-id") or node.get("data-shell-task-heading")
            if raw and str(raw).isdigit():
                result.add(int(raw))
        for m in re.finditer(r"\bTask\s+(\d+)\b", section.get_text(" ", strip=True), re.I):
            result.add(int(m.group(1)))
    return result


def headings(sections: Iterable[Tag]) -> list[str]:
    return [h.get_text(" ", strip=True) for s in sections for h in s.select("h1,h2,h3,h4")]


def has_procedure(teacher: list[Tag]) -> bool:
    if any(PROCEDURE_RE.search(h) for h in headings(teacher)):
        return True
    text = " ".join(s.get_text(" ", strip=True) for s in teacher)
    return bool(re.search(r"\b(?:one|two|three|\d+)\s+class\s+periods?\b", text, re.I) and re.search(r"\bTasks?\s+\d", text, re.I))


def has_quick_rubric(teacher: list[Tag]) -> bool:
    text = " ".join(s.get_text(" ", strip=True) for s in teacher)
    return bool(re.search(r"quick\s+(?:classroom\s+)?(?:rubric|grading)|fast\s+check", text, re.I))


def has_four_level_rubric(teacher: list[Tag]) -> bool:
    for table in [t for s in teacher for t in s.select("table")]:
        if table.get("data-rubric-contract") == "4-3-2-1-v1.0":
            return True
        text = re.sub(r"\s+", " ", table.get_text(" ", strip=True))
        if re.search(r"\b4\b.*\b3\b.*\b2\b.*\b1\b", text, re.I | re.S):
            return True
    return False


def has_reference_list(teacher: list[Tag]) -> bool:
    for section in teacher:
        if section.select_one('[data-final-reference-list="v1.0"]'):
            return True
        for heading in section.find_all(["h2", "h3", "h4"]):
            if not SOURCE_RE.search(heading.get_text(" ", strip=True)):
                continue
            count = 0
            node = heading.find_next_sibling()
            while node is not None and not (isinstance(node, Tag) and node.name in {"h2", "h3"}):
                if isinstance(node, Tag):
                    if node.name in {"p", "li"} and len(node.get_text(" ", strip=True)) >= 20:
                        count += 1
                    count += len([x for x in node.select(".source-url") if x.get_text(" ", strip=True)])
                    count += len(node.select("a[href]"))
                node = node.find_next_sibling() if isinstance(node, Tag) else None
            if count >= 2:
                return True
    return False


def exact_implementation_leaks(teacher: list[Tag], registry: dict) -> list[str]:
    text = "\n".join(s.get_text(" ", strip=True) for s in teacher)
    leaks = []
    for token in registry.get("formalClues", []):
        if token and token in text:
            leaks.append(token)
    for route in registry.get("requiredRoutes", []):
        if route and route in text:
            leaks.append(route)
    return sorted(set(leaks))


def blank_response_count(node: Tag) -> int:
    controls: list[Tag] = []
    if node.has_attr("data-response"):
        controls.append(node)
    controls.extend(node.select("[data-response]"))
    unique = {id(c): c for c in controls}.values()
    return sum(1 for c in unique if not c.get("data-prefilled"))


def task_response_counts(sections: list[Tag]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for section in sections:
        for heading in section.select("[data-task-id], [data-shell-task-heading]"):
            raw = heading.get("data-task-id") or heading.get("data-shell-task-heading")
            if not raw or not str(raw).isdigit():
                continue
            number = int(raw)
            count = 0
            node = heading.find_next_sibling()
            while node is not None:
                if isinstance(node, Tag) and (node.has_attr("data-task-id") or node.has_attr("data-shell-task-heading")):
                    break
                if isinstance(node, Tag):
                    count += blank_response_count(node)
                node = node.find_next_sibling() if isinstance(node, Tag) else None
            counts[number] = counts.get(number, 0) + count
    return counts


def action_without_response(sections: list[Tag]) -> list[int]:
    missing: list[int] = []
    for section in sections:
        for heading in section.select("[data-task-id], [data-shell-task-heading]"):
            raw = heading.get("data-task-id") or heading.get("data-shell-task-heading")
            if not raw or not str(raw).isdigit():
                continue
            number = int(raw)
            text_parts, response_count = [], 0
            node = heading.find_next_sibling()
            while node is not None:
                if isinstance(node, Tag) and (node.has_attr("data-task-id") or node.has_attr("data-shell-task-heading")):
                    break
                if isinstance(node, Tag):
                    text_parts.append(node.get_text(" ", strip=True))
                    response_count += len(node.select("[data-response]")) + int(node.has_attr("data-response"))
                node = node.find_next_sibling() if isinstance(node, Tag) else None
            if ACTION_RE.search(" ".join(text_parts)) and response_count == 0:
                missing.append(number)
    return sorted(set(missing))


def validate_case(entry: dict) -> list[Finding]:
    findings: list[Finding] = []
    case_dir = resolve_case_dir(entry)
    package_path = case_dir / "source/case-package.json"
    package = json.loads(package_path.read_text(encoding="utf-8"))
    case_id = package["id"]
    content = ROOT / package["content"]["source"]
    task_registry = ROOT / package["taskRegistry"]["source"]
    soup = BeautifulSoup(content.read_text(encoding="utf-8"), "html.parser")
    registry = load_js_object(task_registry)
    sections = {role: role_sections(soup, role) for role in REQUIRED_ROLES}

    for role in REQUIRED_ROLES:
        if not sections[role]:
            findings.append(Finding("FAIL", case_id, "ROLE", f"No canonical {role} sections found."))

    for role in REQUIRED_ROLES:
        expected = package.get("rolePageStructure", {}).get(role, {}).get("pageCount")
        if expected is not None and len(sections[role]) != expected:
            findings.append(Finding("FAIL", case_id, "PAGE_COUNT", f"{role}: package says {expected}, canonical content has {len(sections[role])}."))

    tasks = registry_task_numbers(registry)
    teacher_tasks = visible_task_numbers(sections["teacher"])
    missing_teacher = [n for n in tasks if n not in teacher_tasks]
    if missing_teacher:
        findings.append(Finding("FAIL", case_id, "TEACHER_TASK_TRACE", f"Teacher support does not explicitly represent task(s) {missing_teacher}."))

    keyed = registry_task_numbers(registry, keyed_only=True)
    answer_tasks = visible_task_numbers(sections["answer"])
    missing_answer = [n for n in keyed if n not in answer_tasks]
    if missing_answer:
        findings.append(Finding("FAIL", case_id, "ANSWER_TASK_TRACE", f"Answer Key lacks keyed task heading(s) {missing_answer}."))

    teacher = sections["teacher"]
    if not has_procedure(teacher):
        findings.append(Finding("FAIL", case_id, "TEACHER_PROCEDURE", "No coherent procedure/pacing/period route detected."))
    if not has_quick_rubric(teacher):
        findings.append(Finding("FAIL", case_id, "TEACHER_QUICK_RUBRIC", "Common quick rubric/fast-check function is missing."))
    if not has_four_level_rubric(teacher):
        findings.append(Finding("FAIL", case_id, "TEACHER_ANALYTIC_RUBRIC", "Analytic 4/3/2/1 rubric is missing."))
    if not has_reference_list(teacher):
        findings.append(Finding("FAIL", case_id, "TEACHER_REFERENCES", "Authoritative Teacher reference list is missing."))

    leaks = exact_implementation_leaks(teacher, registry)
    if leaks:
        findings.append(Finding("FAIL", case_id, "TEACHER_IMPLEMENTATION_LEAK", f"Teacher-visible runtime identifiers remain: {', '.join(leaks)}"))

    for role in ("student", "accessible"):
        missing_actions = action_without_response(sections[role])
        if missing_actions:
            findings.append(Finding("FAIL", case_id, f"{role.upper()}_DIGITAL_ACTION", f"Required mark/select action has no persistent response in task(s) {missing_actions}."))

    student_counts = task_response_counts(sections["student"])
    accessible_counts = task_response_counts(sections["accessible"])
    for task in sorted(set(student_counts) & set(accessible_counts)):
        s_count, a_count = student_counts[task], accessible_counts[task]
        if s_count >= 6 and a_count >= s_count:
            findings.append(Finding("REVIEW", case_id, "ACCESSIBLE_WORKLOAD", f"Task {task}: {a_count} blank Accessible controls vs {s_count} Student controls."))
        if a_count >= 10:
            findings.append(Finding("REVIEW", case_id, "ACCESSIBLE_HIGH_RESPONSE_COUNT", f"Task {task}: {a_count} blank Accessible controls."))

    if case_id == "SSS-C1-CASE01" and not soup.select_one('[data-final-c1c1-oi-key="v1.0"]'):
        findings.append(Finding("FAIL", case_id, "AUDIT_EXACT_SUBPART", "Answer Key Task 3 O/I classification exemplar is missing."))
    if case_id == "SSS-C1-CASE07" and not soup.select_one('[data-final-c1c7-task4-key="v1.0"]'):
        findings.append(Finding("FAIL", case_id, "AUDIT_EXACT_SUBPART", "Answer Key Task 4 unavailable-stage status exemplar is missing."))
    if case_id == "SSS-C2-CASE04":
        accessible = role_text(soup, "accessible")
        answer = role_text(soup, "answer")
        if re.search(r"choose\s+one.*(?:5|five).*dark", accessible, re.I | re.S) and re.search(r"at\s+least\s+6(?:\.0)?\s*h", answer, re.I):
            findings.append(Finding("FAIL", case_id, "ACCESSIBLE_ANSWER_SPACE", "Accessible still invites a five-hour choice while the common key requires six."))

    return findings


def main() -> int:
    findings: list[Finding] = []
    errors: list[str] = []
    entries = read_registry()
    for entry in entries:
        try:
            findings.extend(validate_case(entry))
        except Exception as exc:
            errors.append(f"ERROR: {entry.get('id', '(unknown)')} — {exc}")

    print("SSS/HHH final quality contract validation")
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
