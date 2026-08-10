#!/usr/bin/env python3
"""Focused deterministic checks for the SSS intervention/trial visual family."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "sss/campaign-1/case-06-first-contact-protocol/source"
CONTENT = CASE / "content.html"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
HANDOFF = ROOT / "sss/audit/final/SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md"

FROZEN_HASHES = {
    "content.html": "d171f9b4611e3c7bea4d9b401c7e59ad70defdd07376cdfb171c21568553ec07",
    "presentation.css": "666799f312f1323432abc17fefff4f03dd65e380424fa19ce79b0173acf1369d",
    "layout-overrides.json": "7ce2fca0a49a949043cb5bae7513341add00cb409b546a5eef008a77b6be338d",
    "case-package.json": "9bb008a795b641c057e93dbcc5778ae9dd00c04d103ac720fafd491551eb7b91",
    "task-registry.js": "5afe3f4b35e4b80ef544c86898ec0314787e831c37ac8e5396d58753f95ef774",
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
    plan = " ".join(PLAN.read_text(encoding="utf-8").split())
    handoff = " ".join(HANDOFF.read_text(encoding="utf-8").split())

    pages = {
        "student": soup.select_one('[data-page-id="student-mission-03"]'),
        "answer": soup.select_one('[data-page-id="answer-key-03"]'),
        "accessible": soup.select_one('[data-page-id="accessible-mission-05"]'),
    }
    tables = {role: page.select_one(".intervention-table") if page else None for role, page in pages.items()}
    expected_options = {
        "student": [
            "Disable all atmospheric processing",
            "Keep the current setting unchanged",
            "Isolate the shared atmosphere or selectively preserve identified signals",
        ],
        "answer": ["Disable all processing", "Keep unchanged", "Isolate or selectively preserve signals"],
        "accessible": ["Disable all processing", "Keep unchanged", "Isolate or selectively preserve signals"],
    }

    for name, expected in FROZEN_HASHES.items():
        actual = sha256(CASE / name)
        check(f"frozen First Contact {name} hash remains exact", actual == expected, actual)

    for role in ("student", "answer", "accessible"):
        check(f"{role} Task 6 target page and intervention table remain present", pages[role] is not None and tables[role] is not None)
    for role in ("student", "answer", "accessible"):
        rows = tables[role].select("tbody > tr") if tables[role] else []
        check(f"{role} intervention table retains exactly three options", len(rows) == 3, len(rows))
    for role in ("student", "answer", "accessible"):
        actual = [normalized(row.select_one("th")) for row in tables[role].select("tbody > tr")]
        check(f"{role} intervention option order and wording remain exact", actual == expected_options[role], actual)

    student_ids = [node.get("data-persist-id") for node in pages["student"].select('[data-persist-id^="t6-"][data-response]')]
    accessible_ids = [node.get("data-persist-id") for node in pages["accessible"].select('[data-persist-id^="a6-"][data-response]')]
    check("Student retains the five exact Task 6 response identities", student_ids == ["t6-disable", "t6-unchanged", "t6-selective", "t6-recommend", "t6-monitor"], student_ids)
    check("Accessible retains the five exact Task 6 response identities", accessible_ids == ["a6-disable", "a6-unchanged", "a6-selective", "a6-recommend", "a6-monitor"], accessible_ids)
    check("all five Student Task 6 fields remain blank", all(not normalized(node) for node in pages["student"].select('[data-persist-id^="t6-"][data-response]')))
    accessible_fields = pages["accessible"].select('[data-persist-id^="a6-"][data-response]')
    check(
        "Accessible retains only the accepted unsafe-option scaffold",
        [normalized(node) for node in accessible_fields]
        == ["UNSAFE — disabling all atmospheric processing would weaken pressure, breathable-gas, and contaminant protection.", "", "", "", ""],
    )
    check("Student safety note preserves all three life-support safeguards", all(token in normalized(pages["student"].select_one(".science-note")) for token in ("pressure", "breathable-gas control", "contaminant protection", "Do not treat “turn everything off” as a safe fix")))
    check("Accessible safety note preserves all three life-support safeguards", all(token in normalized(pages["accessible"].select_one(".science-note")) for token in ("pressure", "breathable-gas control", "contaminant protection", "Do not disable everything")))

    answer_rows = tables["answer"].select("tbody > tr")
    check("Answer Key rejects shutdown because safeguards could be compromised", "Reject" in normalized(answer_rows[0]) and "breathable-gas and contaminant safeguards" in normalized(answer_rows[0]))
    check("Answer Key rejects no change because signals remain removed", "Reject" in normalized(answer_rows[1]) and "continues removing all detected network signals" in normalized(answer_rows[1]))
    check("Answer Key recommends only controlled testing of the selective option", "Recommend for controlled testing" in normalized(answer_rows[2]) and "monitored life-support functions" in normalized(answer_rows[2]))
    answer_panels = pages["answer"].select(".two-col > .answer-block")
    check("Answer Key retains separate recommendation and monitoring panels", len(answer_panels) == 2, len(answer_panels))
    check("Answer Key recommendation remains reversible and limited scale", "Begin reversibly and at limited scale" in normalized(answer_panels[0]))
    check("Answer Key monitoring retains signals, biology and life-support measures", all(token in normalized(answer_panels[1]) for token in ("signal compounds", "network micro-broadcasts", "nutrient transfer", "pressure", "breathable gases", "hazardous contaminants")))
    check("source authors no treatment magnitude, threshold or completed recovery result", not re.search(r"\b(?:ppm|ppb|mg|mGy|Hz|percent|%)\b|guaranteed recovery|recovered after", normalized(pages["student"]) + " " + normalized(pages["accessible"]), re.I))

    marker = "Intervention-comparison family pilot: First Contact Protocol."
    css_start = css.index(marker)
    css_end = len(css)
    contact_css = css[css_start:css_end]
    check("intervention layer is strictly scoped to First Contact Protocol", 'data-case-id="SSS-C1-CASE06"' in contact_css and "SSS-C1-CASE0" not in contact_css.replace("SSS-C1-CASE06", ""))
    check("intervention layer declares four independent hatch patterns", all(token in contact_css for token in ("--contact-intervention-unsafe-pattern", "--contact-intervention-hold-pattern", "--contact-intervention-test-pattern", "--contact-intervention-monitor-pattern")))
    check("Task 6 heading exposes the compare-select-monitor relationship", 'content: "COMPARE → SELECT → MONITOR"' in contact_css)
    check("all three target editions receive the Task 6 relationship rail", all(token in contact_css for token in ("student-mission-03", "accessible-mission-05", "answer-key-03")))
    check("intervention tables receive an outline and inset structural rail", "outline: 1.5px solid var(--contact-intervention-line)" in contact_css and "box-shadow: inset 4px 0 0 var(--contact-intervention-line)" in contact_css)
    check("unsafe option receives an explicit status", 'content: "UNSAFE"' in contact_css)
    check("unchanged option receives an explicit status", 'content: "NO CHANGE"' in contact_css)
    check("selective option receives an explicit controlled-test status", 'content: "CONTROLLED TEST"' in contact_css)
    check("option states use double dotted and solid borders", all(token in contact_css for token in ("border-left: 4px double", "border-left: 4px dotted", "border-left: 4px solid")))
    check("recommendation responses use a solid decision rail", all(token in contact_css for token in ('data-persist-id="t6-recommend"', 'data-persist-id="a6-recommend"', "border-left: 4px solid var(--contact-intervention-line)")))
    check("monitoring responses use a dashed verification rail", all(token in contact_css for token in ('data-persist-id="t6-monitor"', 'data-persist-id="a6-monitor"', "border-left: 4px dashed var(--contact-intervention-line)")))
    check("learner response labels retain six-pixel rail clearance", "padding-left: 6px" in contact_css)
    check("life-support notes use the independent unsafe-gate state", ".science-note" in contact_css and "--contact-intervention-unsafe-pattern" in contact_css)
    check("Answer Key recommendation and monitor panels mirror solid and dashed gates", ".two-col > .answer-block:first-child" in contact_css and ".two-col > .answer-block:nth-child(2)" in contact_css)
    check("grayscale treatment targets the same three Task 6 pages", '.worksheet-document.grayscale[data-case-id="SSS-C1-CASE06"]' in contact_css and all(token in contact_css for token in ("student-mission-03", "accessible-mission-05", "answer-key-03")))
    check("the shared layer does not author learner field dimensions", not re.search(r"(?:t6|a6)-(?:disable|unchanged|selective|recommend|monitor)[^}]*\b(?:width|height|min-height|max-height)\s*:", contact_css, re.S))

    case_start = harness.index('if (item.id === "SSS-C1-CASE06")')
    case_end = harness.index('if (item.id === "SSS-C1-CASE07")', case_start)
    case_harness = harness[case_start:case_end]
    check(
        "browser harness adds exactly three runtime intervention assertions",
        case_harness.count('`C1 Case 06 ${grayscale ? "grayscale" : "normal"} intervention panel') == 1
        and case_harness.count('"C1 Case 06 intervention pages retain strict fit') == 1,
    )
    check("browser harness measures all six normal and grayscale target views", 'interventionPageFit.length === 6' in case_harness and 'for (const grayscale of [false, true])' in case_harness)
    check("browser harness requires fixed worksheet geometry", 'state.pageSize === "816x1056"' in case_harness)
    check("browser harness requires exact role page counts", all(token in case_harness for token in ('["student", "student-mission-03", 5]', '["answer", "answer-key-03", 5]', '["accessible", "accessible-mission-05", 7]')))
    check("browser harness requires all three option status labels", 'UNSAFE|NO CHANGE|CONTROLLED TEST' in case_harness)
    check("browser harness requires all three border states", 'double|dotted|solid' in case_harness)
    check("browser harness verifies both learner field sets", all(token in case_harness for token in ("t6-disable|t6-unchanged|t6-selective|t6-recommend|t6-monitor", "a6-disable|a6-unchanged|a6-selective|a6-recommend|a6-monitor")))
    check("browser harness protects Accessible scaffold parity", "UNSAFE — disabling all atmospheric processing would weaken pressure, breathable-gas, and contaminant protection" in case_harness)
    check("browser harness protects minimum learner field utility", "field.size[0] >= 108 && field.size[1] >= 30" in case_harness)
    check("browser harness verifies recommendation and monitor rail clearance", "label.clearance >= 6" in case_harness and '"solid|dashed"' in case_harness)
    check("browser harness protects Answer Key reversibility and monitoring", "Begin reversibly and at limited scale" in case_harness and "pressure, breathable gases, and hazardous contaminants" in case_harness)
    check("browser harness rejects row collision and overflow", "!state.collisions" in case_harness and "state.scrollHeight <= state.clientHeight" in case_harness)

    check(
        "plan records C1C6-VIS03 as the accepted 63-check Family 8 finding",
        bool(re.search(
            r"\| `C1C6-VIS03` .*\| 8 · Intervention comparison/trial workflow \|.*"
            r"`VERIFIED-FAMILY · 63/63 INTERVENTION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 8d6a51a ACCEPTED`",
            plan,
        ))
        and "accepted first standalone Family 8 intervention-comparison finding" in plan
        and "`C1C6-VIS03` is therefore `VERIFIED-FAMILY`" in plan,
    )
    check(
        "plan advances accepted inventory to 30 of 36 and Family 8 to two of five",
        "Accepted progress after the First Contact intervention-comparison closeout is **30 of 36 completed**" in plan
        and "**6 of 36 remaining**" in plan
        and "Family 8 has two of five assignments verified" in plan
        and "Accepted progress after the Silent Grove specification/verification closeout is **29 of 36 completed**" in plan,
    )
    check(
        "plan identifies the accepted Family 8 hybrid without double-counting",
        "accepted hybrid `C2C5-VIS03`, already counted once in the unique inventory" in plan
        and "newly accepted standalone `C1C6-VIS03`" in plan,
    )
    check(
        "handoff accepts the First Contact Family 8 finding and preserves source ownership",
        "Accepted Family 8 finding — First Contact monitored response" in handoff
        and "8d6a51a58a18f1f4db51d7a25ea58317f1962408" in handoff
        and "dab27208c6fa352a506fbf6a80a7b3071fcad286" in handoff
        and "changes no worksheet wording" in handoff,
    )
    check("handoff records all five frozen First Contact hashes", all(value in handoff for value in FROZEN_HASHES.values()))
    check("handoff preserves the three exact option states", all(token in handoff for token in ("UNSAFE", "NO CHANGE", "CONTROLLED TEST")))
    check("handoff preserves recommendation monitoring and safety semantics", all(token in handoff for token in ("recommendation", "monitoring", "pressure", "breathable-gas", "contaminant")))
    check(
        "handoff records differential acceptance and advances inventory without platform policy",
        "2356/2356 PASS" in handoff
        and "Run 2 each passed **2359/2359 PASS**" in handoff
        and "+3 registered and +3 passed" in handoff
        and "Canonical project registration remains 2360" in handoff
        and "does not establish a general platform policy" in handoff
        and "The formal inventory is now **30 of 36 completed**" in handoff
        and "with **6 remaining**" in handoff
        and "Family 8 has two of five assignments verified" in handoff
        and "hybrid `C2C5-VIS03` is not counted again" in handoff,
    )

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f" — {detail}" if detail and not ok else ""))
    print(f"\nIntervention/trial validator: {passed}/{len(checks)} PASS")
    return 0 if passed == len(checks) == 63 else 1


if __name__ == "__main__":
    raise SystemExit(main())
