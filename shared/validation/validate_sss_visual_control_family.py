#!/usr/bin/env python3
"""Focused deterministic checks for the SSS engineering-control-loop family."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "sss/campaign-1/case-04-hayes-orbital-station/source"
CONTENT = CASE / "content.html"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
HANDOFF = ROOT / "sss/audit/final/SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md"

FROZEN_HASHES = {
    "content.html": "7725f9b5cd204171eae9d3a77158307ed4e9f6f66691cdd8dd27c0132d0bc061",
    "presentation.css": "be6192cd9401105d8978b59be3204432e5e095f58da2b2f349a8099a9cfb9d2f",
    "layout-overrides.json": "11653245ad346f9ccb67c938dbd4b021c8278601b154403bf25ded97d7ab754f",
    "case-package.json": "8cab25b388b5a6d7c371cf083acc7339a0bd81d11fc1d923f5d0e683b339ee37",
    "task-registry.js": "afb3e989647a2eb03e354800ee8413c0783f4f1f2ce723cd802bd0e5c9c6dfd7",
}


def normalized(node) -> str:
    return " ".join(node.stripped_strings) if node else ""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    source = CONTENT.read_text(encoding="utf-8")
    soup = BeautifulSoup(source, "html.parser")
    css = COMPONENTS.read_text(encoding="utf-8")
    harness = HARNESS.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    handoff = HANDOFF.read_text(encoding="utf-8")

    models = soup.select('.systems-diagram[data-systems-contract="reactor-control-v1.0"]')
    model_roles = [model.find_parent("section", attrs={"data-role": True})["data-role"] for model in models]
    check(
        "Hayes retains one reactor-control model in Student, Answer Key and Accessible",
        len(models) == 3 and sorted(model_roles) == ["accessible", "answer", "student"],
        model_roles,
    )
    expected_pages = {
        "student": "student-mission-04",
        "answer": "answer-key-03",
        "accessible": "accessible-mission-07",
    }
    check(
        "the three control models remain on their frozen role pages",
        all(model.find_parent("section")["data-page-id"] == expected_pages[model.find_parent("section")["data-role"]] for model in models),
    )
    check("each model retains exactly four direct control nodes", all(len(model.find_all("div", recursive=False)) == 4 for model in models))
    check(
        "each model retains exactly three direct right-arrow connectors",
        all([normalized(node) for node in model.find_all("i", recursive=False)] == ["→", "→", "→"] for model in models),
    )

    expected_text = {
        "student": [
            "Measure Light intensity and exposure time",
            "Compare Validated operating range",
            "Control Independent dimming or recovery interval",
            "Verify Culture response",
        ],
        "answer": [
            "Sensor Measure intensity and duration",
            "Controller Compare with validated range",
            "Actuator Dim or schedule recovery",
            "Feedback Track culture performance",
        ],
        "accessible": [
            "Measure Intensity and time",
            "Compare Validated range",
            "Control Dim or schedule recovery",
            "Verify Culture response",
        ],
    }
    check(
        "all role-specific source nodes retain their exact approved text",
        all(
            [normalized(node) for node in model.find_all("div", recursive=False)] == expected_text[model.find_parent("section")["data-role"]]
            for model in models
        ),
    )
    check(
        "all control models retain explicit nonempty image descriptions",
        all(model.get("role") == "img" and model.get("aria-label") for model in models),
        [model.get("aria-label") for model in models],
    )

    student_page = soup.select_one('section[data-role="student"][data-page-id="student-mission-04"]')
    accessible_page = soup.select_one('section[data-role="accessible"][data-page-id="accessible-mission-07"]')
    answer_page = soup.select_one('section[data-role="answer"][data-page-id="answer-key-04"]')
    student_fields = [student_page.select_one(f'[data-persist-id="{persist_id}"]') for persist_id in ("t7a", "t7b")]
    accessible_fields = [accessible_page.select_one(f'[data-persist-id="{persist_id}"]') for persist_id in ("a7", "a7-longterm")]
    check(
        "Student retains two blank writable Task 7 response identities",
        all(field and field.has_attr("data-response") and not normalized(field) for field in student_fields),
        [field.get("data-persist-id") if field else None for field in student_fields],
    )
    check(
        "Accessible retains two blank writable Task 7 response identities",
        all(field and field.has_attr("data-response") and not normalized(field) for field in accessible_fields),
        [field.get("data-persist-id") if field else None for field in accessible_fields],
    )
    student_directions = normalized(student_page.select_one('[data-shell-task-heading="7"] + .systems-diagram + .directions'))
    check(
        "Student directions preserve immediate recovery and corridor-independent control",
        "validated recovery schedule" in student_directions and "independently of corridor lighting" in student_directions,
        student_directions,
    )
    answer_task = answer_page.select_one('[data-shell-task-heading="7"] + .answer-block')
    answer_text = normalized(answer_task)
    check(
        "Answer Key retains the exact immediate recovery boundary",
        "Restore the validated dark or low-light recovery interval." in answer_text,
        answer_text,
    )
    check(
        "Answer Key retains independent control, monitoring and validation",
        "Add independent intensity and schedule control, monitor actual exposure and culture response, and validate settings for the current mixing and density." in answer_text,
        answer_text,
    )
    check(
        "Answer Key preserves controlled continuous cultivation as possible",
        "Continuous cultivation remains possible under appropriately controlled conditions." in answer_text,
        answer_text,
    )
    full_text = normalized(soup)
    check(
        "the released case keeps its reactor-specific science qualification",
        "Continuous cultivation may work with appropriate independent intensity, mixing, density, and process controls." in full_text
        and "The conclusion is specific to this reactor configuration." in full_text,
    )
    check(
        "Hayes page counts remain exactly frozen across all four roles",
        {role: len(soup.select(f'section[data-role="{role}"]')) for role in ("student", "answer", "teacher", "accessible")}
        == {"student": 4, "answer": 4, "teacher": 7, "accessible": 7},
    )

    for filename, expected_hash in FROZEN_HASHES.items():
        check(
            f"frozen Hayes {filename} SHA-256 remains exact",
            sha256(CASE / filename) == expected_hash,
            sha256(CASE / filename),
        )

    css_start = css.index("Engineering-control-loop family: Hayes independent reactor controls.")
    css_end = css.index("Mechanism/pathway family expansion: Europa radiation-to-growth pathway.", css_start)
    control_css = css[css_start:css_end]
    required_css = (
        '.worksheet-document[data-case-id="SSS-C1-CASE04"]',
        'data-systems-contract="reactor-control-v1.0"',
        "CLOSED CONTROL LOOP · INDEPENDENT REACTOR LIGHT SYSTEM",
        "SENSOR",
        "COMPARATOR / CONTROLLER",
        "INDEPENDENT ACTUATOR",
        "REACTOR / VERIFICATION",
        "MEASURES",
        "COMMANDS",
        "ADJUSTS",
        "PERFORMANCE FEEDBACK · CULTURE RESPONSE → SENSOR / COMPARATOR",
        "repeating-linear-gradient",
        "radial-gradient",
        ".worksheet-document.grayscale",
    )
    check(
        "the shared component layer declares the complete Case 04 CL1 grammar",
        all(token in control_css for token in required_css),
        [token for token in required_css if token not in control_css],
    )
    check(
        "the control-loop layer stays inside the extracted shared visual payload",
        css.index("/* BEGIN SSS/HHH EXPLANATORY-VISUAL PRIMITIVES */") < css_start < css_end < css.index("/* END SSS/HHH EXPLANATORY-VISUAL PRIMITIVES */"),
    )
    check(
        "the CL1 layer remains strictly Case 04 scoped",
        control_css.count('.worksheet-document[data-case-id="SSS-C1-CASE04"]') >= 15
        and "SSS-C1-CASE0" not in control_css.replace("SSS-C1-CASE04", ""),
    )
    check(
        "the CL1 layer does not size or prefill learner responses",
        "control-response" not in control_css and "data-response" not in control_css and "data-persist-id" not in control_css,
    )
    check(
        "the CL1 layer introduces no operating setpoint or universal continuous-light claim",
        not re.search(r"\b(?:16/8|24/0|\d+(?:\.\d+)?\s*(?:lux|ppfd|hour|minute))\b|continuous\s+(?:light|cultivation)\s+(?:fails|cannot)", control_css, flags=re.IGNORECASE),
    )
    check(
        "four node roles use direct text plus independent border and pattern states",
        all(token in control_css for token in ("solid", "double", "dashed", "dotted", "background-image", "background-size"))
        or all(token in control_css for token in ("double", "dashed", "dotted", "repeating-linear-gradient", "radial-gradient")),
    )

    case04_start = harness.index('if (item.id === "SSS-C1-CASE04")')
    case04_end = harness.index('if (item.id === "SSS-C1-CASE05")', case04_start)
    case04_harness = harness[case04_start:case04_end]
    check(
        "the browser harness registers exactly three focused CL1 assertions",
        harness.count("control-loop pages retain strict fit, page counts and geometry") == 1
        and harness.count("control loop preserves roles, feedback, learner fields and reactor boundary") == 1
        and 'for (const grayscale of [false, true])' in case04_harness,
    )
    check(
        "the browser harness covers all six role and grayscale target states",
        'for (const grayscale of [false, true])' in case04_harness
        and 'student-mission-04' in case04_harness
        and 'answer-key-03' in case04_harness
        and 'accessible-mission-07' in case04_harness
        and 'state.pageSize === "816x1056"' in case04_harness
        and "state.scrollHeight <= state.clientHeight" not in case04_harness[case04_harness.index("const controlLoopPageFit"):case04_harness.index("const controlLearnerText")]
        and "state.fits" in case04_harness,
    )
    check(
        "the browser contract preserves both learner field pairs and completed-key boundaries",
        all(token in case04_harness for token in ("t7a", "t7b", "a7-longterm", "Restore the validated dark or low-light recovery interval", "Continuous cultivation remains possible under appropriately controlled conditions")),
    )

    check(
        "the production plan records C1C4-VIS03 as an unaccepted 30-check Family 5 candidate",
        bool(re.search(
            r"\| `C1C4-VIS03` .*\| 5 · Engineering control loop \|.*"
            r"`IMPLEMENTED-CANDIDATE · 30/30 CONTROL STATIC PASS · 2348/2348 MAC/CHROME GATE REQUIRED`",
            plan,
        ))
        and "implemented but unaccepted Family 5 candidate" in plan,
    )
    check(
        "the handoff preserves the accepted inventory and external acceptance boundary",
        "Implemented Family 5 candidate — Hayes independent reactor control loop" in handoff
        and "e3abde0f0a05c3481bf6d03a7ca22c52c520d9ec" in handoff
        and "25 of 36 completed" in handoff
        and "11 remaining" in handoff
        and "2317/2348" in handoff
        and "2348/2348" in handoff
        and "do not add `C1C4-VIS03` to a Family 5 accepted register" in handoff,
    )

    if len(checks) != 30:
        raise AssertionError(f"validator definition drift: expected 30 checks, found {len(checks)}")

    failures = [item for item in checks if not item[1]]
    for index, (name, passed, detail) in enumerate(checks, 1):
        print(f"[{index:02d}] {'PASS' if passed else 'FAIL'} · {name}")
        if not passed and detail:
            print(f"     {detail}")
    print(f"\nEngineering-control-loop family: {len(checks) - len(failures)}/{len(checks)} PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
