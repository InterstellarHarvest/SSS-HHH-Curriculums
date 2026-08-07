#!/usr/bin/env python3
"""Validate the post-audit SSS/HHH cross-edition production contracts.

This validator is intentionally quality-contract focused. It does not replace release,
geometry, browser, PDF, source-hash, or case-specific validators. It catches mechanical
signals for defect classes identified by the final SSS Campaign 1 + Campaign 2 audit.

Run from the repository root:
    python3 shared/validation/validate_final_quality_contract.py

During remediation, failures are expected until the affected packages are corrected.
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

PROCEDURE_RE = re.compile(
    r"\b(?:procedure|lesson\s+flow|suggested\s+pacing|pacing|running\s+the\s+packet|class\s+period|instructional\s+sequence)\b",
    re.I,
)
RUBRIC_RE = re.compile(r"\brubric\b", re.I)
SOURCE_HEADING_RE = re.compile(r"\b(?:authoritative\s+sources?|science[- ]source\s+ledger|references?|sources?)\b", re.I)
INTERNAL_NODE_RE = re.compile(r"\b[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*->?[a-z][a-z0-9_]*\b", re.I)
INTERNAL_CLUE_RE = re.compile(r"\b[A-Z][A-Z0-9]+(?:_[A-Z0-9]+){1,}\b")
ACTION_RE = re.compile(r"\b(?:mark|circle|select|choose|put\s+an?\s+x|write\s+[A-Z]\s+next\s+to|rank)\b", re.I)
URL_RE = re.compile(r"https?://", re.I)

# Internal uppercase tokens that can legitimately appear in teacher-facing science/standards.
INTERNAL_CLUE_ALLOWLIST = {
    "CER", "DNA", "PAR", "NGSS", "NASA", "ISS", "SAA", "TAA", "CO2", "O2", "N2",
}

# Exact post-audit checks whose missing subparts are not inferable from task counts alone.
EXACT_CHECKS = {
    "SSS-C1-CASE01": (
        ("answer", re.compile(r"\bO\s*/\s*I\b|observation\s*/\s*inference", re.I),
         "Answer Key must visibly complete/teach the Task 3 O/I classification subpart."),
    ),
    "SSS-C1-CASE07": (
        ("answer", re.compile(r"missing\s+stage.*\bX\b|\bX\b.*missing\s+stage", re.I | re.S),
         "Answer Key must visibly complete the Task 4 missing-stage X/status subpart."),
    ),
}


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
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end < start:
        raise ValueError(f"No object literal found in {path}")
    return json.loads(text[start : end + 1])


def read_registry() -> list[dict]:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    for key in ("cases", "entries", "registry"):
        if isinstance(data.get(key), list):
            return data[key]
    raise ValueError("Unable to find case list in case-registry.v2.json")


def resolve_case_dir(entry: dict) -> Path:
    for key in ("path", "casePath", "packageRoot", "root"):
        value = entry.get(key)
        if value:
            p = ROOT / value
            if p.is_dir():
                return p
    package = entry.get("package") or entry.get("casePackage") or entry.get("casePackagePath")
    if package:
        p = ROOT / package
        if p.is_file():
            return p.parent.parent if p.parent.name == "source" else p.parent
    case_id = entry.get("id", "")
    m = re.fullmatch(r"SSS-C(\d+)-CASE(\d+)", case_id)
    if m:
        campaign, case_num = m.groups()
        campaign_dir = ROOT / f"sss/campaign-{int(campaign)}"
        candidates = sorted(campaign_dir.glob(f"case-{int(case_num):02d}-*"))
        if len(candidates) == 1:
            return candidates[0]
    raise ValueError(f"Unable to resolve case directory for {case_id or entry}")


def role_sections(soup: BeautifulSoup, role: str) -> list[Tag]:
    return list(soup.select(f'[data-role="{role}"]'))


def role_text(soup: BeautifulSoup, role: str) -> str:
    return "\n".join(section.get_text(" ", strip=True) for section in role_sections(soup, role))


def task_numbers_from_registry(registry: dict) -> list[int]:
    result = []
    for task in registry.get("tasks", []):
        raw = task.get("number")
        if raw is None:
            continue
        m = re.search(r"\d+", str(raw))
        if m:
            result.append(int(m.group()))
    return result


def keyed_task_numbers(registry: dict) -> list[int]:
    result = []
    for task in registry.get("tasks", []):
        if not task.get("keyed", True):
            continue
        raw = task.get("number")
        m = re.search(r"\d+", str(raw)) if raw is not None else None
        if m:
            result.append(int(m.group()))
    return result


def visible_task_numbers(sections: Iterable[Tag]) -> set[int]:
    numbers: set[int] = set()
    for section in sections:
        for node in section.select("[data-task-id], [data-shell-task-heading]"):
            raw = node.get("data-task-id") or node.get("data-shell-task-heading")
            if raw and str(raw).isdigit():
                numbers.add(int(raw))
        text = section.get_text(" ", strip=True)
        for m in re.finditer(r"\bTask\s+(\d+)\b", text, re.I):
            numbers.add(int(m.group(1)))
    return numbers


def heading_texts(sections: Iterable[Tag]) -> list[str]:
    return [h.get_text(" ", strip=True) for section in sections for h in section.select("h1,h2,h3,h4")]


def has_four_level_rubric(teacher_sections: list[Tag]) -> bool:
    for table in [t for s in teacher_sections for t in s.select("table")]:
        text = table.get_text(" ", strip=True)
        if not RUBRIC_RE.search(text) and not any(RUBRIC_RE.search(x or "") for x in (table.get("class") or [])):
            continue
        normalized = re.sub(r"\s+", " ", text)
        level_patterns = (
            r"\b4\b.*\b3\b.*\b2\b.*\b1\b",
            r"4\s*[·.-].*3\s*[·.-].*2\s*[·.-].*1\s*[·.-]",
        )
        if any(re.search(p, normalized, re.I | re.S) for p in level_patterns):
            return True
    return False


def has_quick_rubric(teacher_sections: list[Tag]) -> bool:
    text = " ".join(s.get_text(" ", strip=True) for s in teacher_sections)
    return bool(re.search(r"quick\s+(?:classroom\s+)?rubric|quick\s+grading|checklist\s+rubric", text, re.I))


def has_reference_list(teacher_sections: list[Tag]) -> bool:
    text = "\n".join(s.get_text(" ", strip=True) for s in teacher_sections)
    headings = heading_texts(teacher_sections)
    heading_ok = any(SOURCE_HEADING_RE.search(h) for h in headings)
    url_ok = bool(URL_RE.search(text))
    structured = any(s.select_one(".references,.source-url") for s in teacher_sections)
    return (heading_ok and url_ok) or bool(structured and url_ok)


def has_procedure(teacher_sections: list[Tag]) -> bool:
    headings = heading_texts(teacher_sections)
    if any(PROCEDURE_RE.search(h) for h in headings):
        return True
    text = " ".join(s.get_text(" ", strip=True) for s in teacher_sections)
    # Accept an explicitly declared multi-period route only when it names task ranges/order.
    return bool(re.search(r"\b(?:one|two|three|\d+)\s+class\s+periods?\b", text, re.I) and re.search(r"\bTasks?\s+\d", text, re.I))


def internal_leaks(teacher_sections: list[Tag]) -> list[str]:
    text = "\n".join(s.get_text(" ", strip=True) for s in teacher_sections)
    found: list[str] = []
    found.extend(sorted(set(m.group(0) for m in INTERNAL_NODE_RE.finditer(text))))
    for m in INTERNAL_CLUE_RE.finditer(text):
        token = m.group(0)
        if token in INTERNAL_CLUE_ALLOWLIST:
            continue
        # Ignore common standards-like tokens and unit spellings.
        if re.fullmatch(r"MS_[A-Z0-9_]+", token):
            continue
        found.append(token)
    return sorted(set(found))[:12]


def task_response_counts(sections: list[Tag]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for section in sections:
        headings = section.select("[data-task-id], [data-shell-task-heading]")
        for heading in headings:
            raw = heading.get("data-task-id") or heading.get("data-shell-task-heading")
            if not raw or not str(raw).isdigit():
                continue
            number = int(raw)
            count = 0
            node = heading.next_sibling
            while node is not None:
                if isinstance(node, Tag) and (node.has_attr("data-task-id") or node.has_attr("data-shell-task-heading")):
                    break
                if isinstance(node, Tag):
                    if node.has_attr("data-response"):
                        count += 1
                    count += len(node.select("[data-response]"))
                node = node.next_sibling
            counts[number] = counts.get(number, 0) + count
    return counts


def task_action_without_response(sections: list[Tag]) -> list[int]:
    missing: list[int] = []
    for section in sections:
        headings = section.select("[data-task-id], [data-shell-task-heading]")
        for heading in headings:
            raw = heading.get("data-task-id") or heading.get("data-shell-task-heading")
            if not raw or not str(raw).isdigit():
                continue
            number = int(raw)
            text_parts: list[str] = []
            responses = 0
            node = heading.next_sibling
            while node is not None:
                if isinstance(node, Tag) and (node.has_attr("data-task-id") or node.has_attr("data-shell-task-heading")):
                    break
                if isinstance(node, Tag):
                    text_parts.append(node.get_text(" ", strip=True))
                    responses += int(node.has_attr("data-response")) + len(node.select("[data-response]"))
                node = node.next_sibling
            if ACTION_RE.search(" ".join(text_parts)) and responses == 0:
                missing.append(number)
    return sorted(set(missing))


def validate_case(entry: dict) -> list[Finding]:
    findings: list[Finding] = []
    case_dir = resolve_case_dir(entry)
    package_path = case_dir / "source/case-package.json"
    package = json.loads(package_path.read_text(encoding="utf-8"))
    case_id = package["id"]
    content_path = ROOT / package["content"]["source"]
    task_path = ROOT / package["taskRegistry"]["source"]
    soup = BeautifulSoup(content_path.read_text(encoding="utf-8"), "html.parser")
    registry = load_js_object(task_path)

    sections = {role: role_sections(soup, role) for role in REQUIRED_ROLES}
    for role in REQUIRED_ROLES:
        if not sections[role]:
            findings.append(Finding("FAIL", case_id, "ROLE", f"No {role} sections found in canonical content."))

    tasks = task_numbers_from_registry(registry)
    keyed = keyed_task_numbers(registry)

    teacher_visible = visible_task_numbers(sections["teacher"])
    missing_teacher = [n for n in tasks if n not in teacher_visible]
    if missing_teacher:
        findings.append(Finding("FAIL", case_id, "TEACHER_TASK_TRACE", f"Teacher support does not explicitly represent registry task(s): {missing_teacher}."))

    answer_visible = visible_task_numbers(sections["answer"])
    missing_answer = [n for n in keyed if n not in answer_visible]
    if missing_answer:
        findings.append(Finding("FAIL", case_id, "ANSWER_TASK_TRACE", f"Answer Key is missing keyed task heading(s): {missing_answer}."))

    if not has_procedure(sections["teacher"]):
        findings.append(Finding("FAIL", case_id, "TEACHER_PROCEDURE", "Teacher Edition lacks a coherent procedure/pacing/class-period route."))
    if not has_quick_rubric(sections["teacher"]):
        findings.append(Finding("FAIL", case_id, "TEACHER_QUICK_RUBRIC", "Teacher Edition lacks the common quick grading/rubric function."))
    if not has_four_level_rubric(sections["teacher"]):
        findings.append(Finding("FAIL", case_id, "TEACHER_ANALYTIC_RUBRIC", "Teacher Edition lacks the required analytic 4/3/2/1 rubric."))
    if not has_reference_list(sections["teacher"]):
        findings.append(Finding("FAIL", case_id, "TEACHER_REFERENCES", "Teacher Edition lacks an authoritative source/reference list with URLs."))

    leaks = internal_leaks(sections["teacher"])
    if leaks:
        findings.append(Finding("FAIL", case_id, "TEACHER_IMPLEMENTATION_LEAK", f"Teacher-visible implementation identifiers detected: {', '.join(leaks)}"))

    for role in ("student", "accessible"):
        missing_actions = task_action_without_response(sections[role])
        if missing_actions:
            findings.append(Finding("FAIL", case_id, f"{role.upper()}_DIGITAL_ACTION", f"Required mark/select action has no persistent response control in task(s): {missing_actions}."))

    student_counts = task_response_counts(sections["student"])
    accessible_counts = task_response_counts(sections["accessible"])
    for task in sorted(set(student_counts) & set(accessible_counts)):
        s_count = student_counts[task]
        a_count = accessible_counts[task]
        if s_count >= 6 and a_count >= s_count:
            findings.append(Finding(
                "REVIEW", case_id, "ACCESSIBLE_WORKLOAD",
                f"Task {task}: Accessible has {a_count} open response controls versus Student {s_count}; verify meaningful scaffolding/partial completion.",
            ))
        if a_count >= 10:
            findings.append(Finding(
                "REVIEW", case_id, "ACCESSIBLE_HIGH_RESPONSE_COUNT",
                f"Task {task}: Accessible presents {a_count} open response controls; inspect for repeated-writing burden.",
            ))

    texts = {role: role_text(soup, role) for role in REQUIRED_ROLES}
    for role, pattern, message in EXACT_CHECKS.get(case_id, ()): 
        if not pattern.search(texts[role]):
            findings.append(Finding("FAIL", case_id, "AUDIT_EXACT_SUBPART", message))

    # Known cross-edition answer-space defect from final audit: the Accessible prompt explicitly
    # allows choosing the five-hour minimum while the common key historically hardens the answer
    # to six. Keep this semantic check until the wording is reconciled.
    if case_id == "SSS-C2-CASE04":
        accessible = texts["accessible"]
        answer = texts["answer"]
        if re.search(r"5\s+dark\s+hours|five\s+dark\s+hours", accessible, re.I) and re.search(r"at\s+least\s+6(?:\.0)?\s*h", answer, re.I):
            findings.append(Finding("FAIL", case_id, "ACCESSIBLE_ANSWER_SPACE", "Accessible Task 8 permits the five-hour minimum while the common Answer Key requires at least six hours."))

    return findings


def main() -> int:
    entries = read_registry()
    findings: list[Finding] = []
    errors: list[str] = []

    for entry in entries:
        case_id = entry.get("id", "(unknown)")
        try:
            findings.extend(validate_case(entry))
        except Exception as exc:  # validation must name a broken case rather than silently skip it
            errors.append(f"ERROR: {case_id} — {exc}")

    print("SSS/HHH final quality contract validation")
    print(f"Cases inspected: {len(entries)}")
    for line in errors:
        print(line)
    for finding in findings:
        print(finding.line())

    fails = len(errors) + sum(f.severity == "FAIL" for f in findings)
    reviews = sum(f.severity == "REVIEW" for f in findings)
    print(f"Result: {fails} failure(s), {reviews} manual-review flag(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
