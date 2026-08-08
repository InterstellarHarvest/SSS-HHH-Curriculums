#!/usr/bin/env python3
"""Focused deterministic checks for the SSS mechanism/pathway family pilot."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
EDITOR = ROOT / "apps/curriculum-editor/editor-app.js"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
SOURCE = ROOT / "sss/campaign-1/case-02-lunar-greenhouse/source"
PACKAGE = SOURCE / "case-package.json"
CONTENT = SOURCE / "content.html"
PRESENTATION = SOURCE / "presentation.css"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    plan = PLAN.read_text(encoding="utf-8")
    css = COMPONENTS.read_text(encoding="utf-8")
    editor = EDITOR.read_text(encoding="utf-8")
    harness = HARNESS.read_text(encoding="utf-8")
    package = json.loads(PACKAGE.read_text(encoding="utf-8"))
    content = BeautifulSoup(CONTENT.read_text(encoding="utf-8"), "html.parser")

    check(
        "the production plan assigns the Lunar pollination sequence to Family 2",
        bool(re.search(r"\| `C1C2-VIS01` .*\| 2 · Causal mechanism/pathway \|", plan)),
    )
    check(
        "Lunar Greenhouse opts into extracted shared visuals without the full component layer",
        package.get("presentation", {}).get("sharedVisualStyles") is True
        and package.get("presentation", {}).get("sharedComponentStyles") is not True,
        package.get("presentation"),
    )
    check(
        "the package-controlled worksheet sources remain byte-identical to their declared hashes",
        package["sourceHashes"]["content"] == sha256(CONTENT)
        and package["sourceHashes"]["presentation"] == sha256(PRESENTATION),
        {
            "content": [package["sourceHashes"]["content"], sha256(CONTENT)],
            "presentation": [package["sourceHashes"]["presentation"], sha256(PRESENTATION)],
        },
    )

    marker_values = dict(
        re.findall(
            r'^const (VISUAL_PRIMITIVES_(?:START|END)) = "([^"]+)";$',
            editor,
            flags=re.MULTILINE,
        )
    )
    start_marker = marker_values.get("VISUAL_PRIMITIVES_START", "")
    end_marker = marker_values.get("VISUAL_PRIMITIVES_END", "")
    start_index = css.find(start_marker) if start_marker else -1
    content_start = start_index + len(start_marker)
    end_index = css.find(end_marker, content_start) if end_marker else -1
    extracted = css[content_start:end_index] if start_index >= 0 and end_index > content_start else ""
    required_css = (
        '.worksheet-document[data-case-id="SSS-C1-CASE02"] .process-figure',
        "DEPENDENCY RAIL · EARLIER EVENT ENABLES NEXT",
        "TRACE RESULT · FIRST INTERRUPTION AT STEP 2",
        ".process-figure.completed .failed-stage",
        '.linear-process[data-accessible-organizer="sequence"]',
        "grid-template-columns: repeat(5, minmax(0, 1fr) .19in) minmax(0, 1fr)",
        ".worksheet-document.grayscale",
    )
    check(
        "the editor sentinels delimit the complete case-scoped mechanism payload",
        start_index >= 0
        and end_index > content_start
        and all(token in extracted for token in required_css),
        {
            "start_index": start_index,
            "end_index": end_index,
            "missing": [token for token in required_css if token not in extracted],
        },
    )
    mechanism_css = extracted[extracted.index("Mechanism/pathway pilot.") :]
    check(
        "the mechanism grammar uses border and pattern states without a whole-figure filter",
        "repeating-linear-gradient" in mechanism_css
        and "border-top-style: double" in mechanism_css
        and "filter:" not in mechanism_css,
    )

    expected_phrases = [
        "viable pollen in anthers",
        "physical agitation",
        "pollen reaches stigma",
        "pollen tube growth",
        "fertilization",
        "fruit set",
    ]
    expected_bank = " · ".join(
        ["fruit set", "physical agitation", "viable pollen in anthers", "fertilization", "pollen tube growth", "pollen reaches stigma"]
    )

    student_page = content.select_one('section[data-role="student"][data-page-id="student-01"]')
    student_figure = student_page.select_one("figure.process-figure") if student_page else None
    student_stages = student_figure.select(".process-chain > .process-stage") if student_figure else []
    student_arrows = student_figure.select(".process-chain > .process-arrow") if student_figure else []
    student_fields = [stage.select_one(".stage-entry").get("data-persist-id") for stage in student_stages]
    check(
        "the Student pilot retains six writable stages and five directional connectors",
        len(student_stages) == 6
        and len(student_arrows) == 5
        and student_fields == [f"response-student-task3-step{i}" for i in range(1, 7)],
        {"stages": len(student_stages), "arrows": len(student_arrows), "fields": student_fields},
    )
    student_bank = " ".join(student_page.select_one(".word-bank-terms").stripped_strings) if student_page else ""
    check("the Student word bank remains exact and unexpanded", student_bank == expected_bank, student_bank)
    check(
        "the Student mechanism fields remain blank and preserve their response identities",
        all(not stage.select_one(".stage-entry").get_text(strip=True) for stage in student_stages)
        and all(stage.select_one(".stage-entry").has_attr("data-response") for stage in student_stages),
    )

    answer_page = content.select_one('section[data-role="answer"][data-page-id="answer-01"]')
    answer_figure = answer_page.select_one("figure.process-figure.completed") if answer_page else None
    answer_stages = answer_figure.select(".process-chain > .process-stage") if answer_figure else []
    answer_phrases = [" ".join(stage.select_one("strong").stripped_strings) for stage in answer_stages]
    answer_statuses = [" ".join(stage.select_one(".stage-status").stripped_strings) for stage in answer_stages]
    check(
        "the Answer Key completes the same six phrases in the exact mechanism order",
        answer_phrases == expected_phrases,
        answer_phrases,
    )
    check(
        "the Answer Key marks only Step 2 failed and every later event downstream blocked",
        len(answer_stages) == 6
        and answer_stages[1].get("class", []).count("failed-stage") == 1
        and all("failed-stage" not in stage.get("class", []) for stage in answer_stages[:1] + answer_stages[2:])
        and answer_statuses == ["WORKING", "FAILED STEP"] + ["DOWNSTREAM BLOCKED"] * 4,
        answer_statuses,
    )

    accessible_page = content.select_one('section[data-role="accessible"][data-page-id="accessible-02"]')
    accessible_list = accessible_page.select_one('ol.linear-process[data-accessible-organizer="sequence"]') if accessible_page else None
    accessible_steps = accessible_list.select(":scope > li") if accessible_list else []
    accessible_fields = [step.select_one("[data-persist-id]").get("data-persist-id") for step in accessible_steps]
    check(
        "the Accessible vertical variant retains six parallel writable fields",
        len(accessible_steps) == 6
        and accessible_fields == [f"response-accessible-task3-step{i}" for i in range(1, 7)],
        accessible_fields,
    )
    check(
        "the Accessible scaffold preserves only its approved first and final prefill",
        [step.select_one("[data-persist-id]").get_text(strip=True) for step in accessible_steps]
        == [expected_phrases[0], "", "", "", "", expected_phrases[-1]],
    )
    check(
        "the mechanism pilot does not add a learner organizer to the Teacher pages",
        not content.select_one('section[data-role="teacher"] .process-figure')
        and not content.select_one('section[data-role="teacher"] .linear-process'),
    )
    check(
        "the browser harness measures the mechanism grammar in normal and grayscale presentation",
        harness.count("shared mechanism grammar renders horizontal dependency and Accessible vertical rails") == 1
        and 'for (const grayscale of [false, true])' in harness
        and 'horizontal[1].failedBorder === "double"' in harness
        and "accessibleState.steps === 6" in harness,
    )

    failures = [(name, detail) for name, passed, detail in checks if not passed]
    print("SSS visual modernization · mechanism family pilot")
    print(f"Result: {len(checks) - len(failures)}/{len(checks)} PASS")
    for name, detail in failures:
        print(f"FAIL: {name}\n  {detail}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
