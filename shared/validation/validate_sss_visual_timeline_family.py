#!/usr/bin/env python3
"""Focused deterministic checks for the SSS timeline/event-log family pilot."""

from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
HAYES_CONTENT = ROOT / "sss/campaign-1/case-04-hayes-orbital-station/source/content.html"
CONTACT_CONTENT = ROOT / "sss/campaign-1/case-06-first-contact-protocol/source/content.html"
SILENT_CONTENT = ROOT / "sss/campaign-2/case-04-silent-grove/source/content.html"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
HANDOFF = ROOT / "sss/audit/final/SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md"


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    source = HAYES_CONTENT.read_text(encoding="utf-8")
    soup = BeautifulSoup(source, "html.parser")
    contact_source = CONTACT_CONTENT.read_text(encoding="utf-8")
    contact_soup = BeautifulSoup(contact_source, "html.parser")
    silent_source = SILENT_CONTENT.read_text(encoding="utf-8")
    silent_soup = BeautifulSoup(silent_source, "html.parser")
    css = COMPONENTS.read_text(encoding="utf-8")
    harness = HARNESS.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    handoff = HANDOFF.read_text(encoding="utf-8")

    logs = soup.select('[data-timeline-contract="relative-five-event-v1.0"]')
    roles = [log.find_parent("section", attrs={"data-role": True})["data-role"] for log in logs]
    check(
        "Hayes retains one synchronized relative timeline in Student, Answer Key and Accessible",
        len(logs) == 3 and sorted(roles) == ["accessible", "answer", "student"],
        roles,
    )

    expected_banks = [
        "A Between crashes: surviving cells rebuild",
        "B Four months of stable operation",
        "C Every 6–8 days: another crash",
        "D Lighting changes from 16/8 to uncontrolled 24/0",
        "E About one week later: first crash",
    ]
    student_bank = [" ".join(node.stripped_strings) for node in soup.select(".event-bank > span")]
    accessible_bank = [
        re.sub(r"\.$", "", " ".join(node.stripped_strings)).replace("A. ", "A ").replace("B. ", "B ")
        .replace("C. ", "C ").replace("D. ", "D ").replace("E. ", "E ")
        for node in soup.select(".accessible-event-bank > li")
    ]
    check("both learner event banks retain the same five exact events", student_bank == expected_banks and accessible_bank == expected_banks, {"student": student_bank, "accessible": accessible_bank})

    expected_fields = {
        "student": [f"t2-{index}" for index in range(1, 6)],
        "accessible": [f"a2-{index}" for index in range(1, 6)],
    }
    for role in ("student", "accessible"):
        log = next(log for log in logs if log.find_parent("section")["data-role"] == role)
        steps = log.select(":scope > .timeline-step")
        fields = [step.select_one(".timeline-response") for step in steps]
        check(
            f"the {role} incident log retains five ordered blank response fields",
            [step.get("data-timeline-event") for step in steps] == [str(index) for index in range(1, 6)]
            and [field.get("data-persist-id") for field in fields] == expected_fields[role]
            and all(field.has_attr("data-response") and not field.get_text(strip=True) for field in fields),
            [field.get("data-persist-id") for field in fields],
        )

    student_log = next(log for log in logs if log.find_parent("section")["data-role"] == "student")
    accessible_log = next(log for log in logs if log.find_parent("section")["data-role"] == "accessible")
    answer_log = next(log for log in logs if log.find_parent("section")["data-role"] == "answer")
    check("Student and Answer Key retain four explicit right-arrow connectors", [node.get_text(strip=True) for node in student_log.select(":scope > .timeline-arrow")] == ["→"] * 4 and [node.get_text(strip=True) for node in answer_log.select(":scope > .timeline-arrow")] == ["→"] * 4)
    check("Accessible retains one true vertical DOM sequence without duplicate arrow nodes", not accessible_log.select(":scope > .timeline-arrow") and len(accessible_log.select(":scope > .timeline-step")) == 5)

    expected_answer = [
        "Four months of stable operation",
        "Lighting changes from 16/8 to uncontrolled 24/0",
        "About one week later: first crash",
        "Every 6–8 days: another crash",
        "Between crashes: surviving cells rebuild",
    ]
    answer_text = [" ".join(step.select_one("strong").stripped_strings) for step in answer_log.select(":scope > .timeline-step")]
    check("the completed Answer Key retains the exact five-event sequence", answer_text == expected_answer, answer_text)
    answer_page_text = " ".join(answer_log.find_parent("section").stripped_strings)
    check("the Answer Key retains relative-timing and acceptable-alternative boundaries", "Invented mission-day labels" in answer_page_text and "survivor rebuilding between the first and repeated crashes" in answer_page_text)

    check(
        "all accepted Hayes role page counts remain unchanged",
        len(soup.select('section[data-role="student"]')) == 4
        and len(soup.select('section[data-role="answer"]')) == 4
        and len(soup.select('section[data-role="teacher"]')) == 7
        and len(soup.select('section[data-role="accessible"]')) == 7,
    )

    css_start = css.index("Timeline/event-log family pilot: Hayes Orbital Station.")
    css_end = css.index("Timeline/event-log family expansion: First Contact Protocol.", css_start)
    timeline_css = css[css_start:css_end]
    required_css = (
        '.worksheet-document[data-case-id="SSS-C1-CASE04"]',
        'data-timeline-contract="relative-five-event-v1.0"',
        "SAA INCIDENT LOG · RELATIVE SEQUENCE",
        'content: "BASELINE"',
        'content: "CHANGE"',
        'content: "FIRST FAILURE"',
        'content: "REPEAT"',
        'content: "RECOVERY"',
        "repeating-linear-gradient",
        "radial-gradient",
        'content: "↓"',
        "body.grayscale",
    )
    check("the shared component layer declares the complete case-scoped incident-log grammar", all(token in timeline_css for token in required_css), [token for token in required_css if token not in timeline_css])
    check("the incident-log layer stays inside the extracted shared visual payload", css.index("/* BEGIN SSS/HHH EXPLANATORY-VISUAL PRIMITIVES */") < css_start < css_end)
    check("the incident-log styling does not introduce mission dates or proportional spacing", not re.search(r"mission[- ]day|day\s*\d|proportional", timeline_css, flags=re.IGNORECASE), timeline_css[:240])
    check("the incident-log styling does not target learner response sizes", "timeline-response" not in timeline_css and "data-response" not in timeline_css)
    check("the incident-log styling remains strictly Case 04 scoped", timeline_css.count('.worksheet-document[data-case-id="SSS-C1-CASE04"]') >= 10 and "SSS-C1-CASE0" not in timeline_css.replace("SSS-C1-CASE04", ""))

    harness_start = harness.index('if (item.id === "SSS-C1-CASE04")')
    harness_end = harness.index('if (item.id === "SSS-C1-CASE05")', harness_start)
    harness_block = harness[harness_start:harness_end]
    check(
        "the browser harness measures incident-log fit and exact rendering in both modes",
        harness.count("incident-log pages retain strict fit, page counts and geometry") == 1
        and harness.count("incident log preserves relative sequence, learner fields and completed key") == 1
        and 'for (const grayscale of [false, true])' in harness_block
        and 'state.pageSize === "816x1056"' in harness_block
        and "SAA INCIDENT LOG · RELATIVE SEQUENCE" in harness_block
        and "t2-1|t2-2|t2-3|t2-4|t2-5" in harness_block
        and "a2-1|a2-2|a2-3|a2-4|a2-5" in harness_block
        and 'accessibleLog.accessibleConnectors === "↓|↓|↓|↓"' in harness_block,
    )

    check(
        "the plan and handoff accept C1C4-VIS01 as the first Family 3 finding",
        bool(re.search(
            r"\| `C1C4-VIS01` .*\| 3 · Timeline/event log \|.*"
            r"`VERIFIED-FAMILY · 17/17 TIMELINE STATIC PASS · 2333/2333 BROWSER PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · d5ffe37 ACCEPTED`",
            plan,
        ))
        and "Accepted Family 3 pilot — Hayes relative incident log" in handoff
        and "d5ffe37c0db952fb74c51c961d5b58bb405f01ea" in handoff
        and "2333/2333 PASS with 0 application JavaScript errors" in handoff
        and "17/17 PASS" in handoff
        and "| `C1C4-VIS01` | `d5ffe37` | `VERIFIED-FAMILY` |" in handoff
        and "21 of 36 completed" in handoff
        and "15 remaining" in handoff,
    )

    source_paths = (
        "sss/campaign-1/case-04-hayes-orbital-station/source/content.html",
        "sss/campaign-1/case-04-hayes-orbital-station/source/presentation.css",
        "sss/campaign-1/case-04-hayes-orbital-station/source/layout-overrides.json",
        "sss/campaign-1/case-04-hayes-orbital-station/source/case-package.json",
        "sss/campaign-1/case-04-hayes-orbital-station/source/task-registry.js",
    )
    check("the accepted handoff explicitly protects all frozen Hayes sources", all(path in handoff for path in source_paths), [path for path in source_paths if path not in handoff])

    contact_strips = contact_soup.select(".timing-strip")
    contact_roles = [strip.find_parent("section", attrs={"data-role": True})["data-role"] for strip in contact_strips]
    check(
        "First Contact retains one timing strip in Student and Accessible",
        len(contact_strips) == 2 and sorted(contact_roles) == ["accessible", "student"],
        contact_roles,
    )
    student_timing = next(strip for strip in contact_strips if strip.find_parent("section")["data-role"] == "student")
    accessible_timing = next(strip for strip in contact_strips if strip.find_parent("section")["data-role"] == "accessible")
    check(
        "First Contact Student retains the exact three reported event labels",
        [" ".join(node.stripped_strings) for node in student_timing.find_all("div", recursive=False)] == [
            "72.4 hours ago Docking and human-standard filtration",
            "72.1 hours ago Last detected network signal",
            "First post-docking cycle Activity declines toward dormancy",
        ],
    )
    check(
        "First Contact Accessible retains the exact two timestamped event labels",
        [" ".join(node.stripped_strings) for node in accessible_timing.find_all("div", recursive=False)] == [
            "72.4 hours ago Docking and filtration",
            "72.1 hours ago Last signal",
        ],
    )
    check(
        "First Contact elapsed connectors remain exact across learner editions",
        [" ".join(node.stripped_strings) for node in student_timing.find_all("b", recursive=False)] == ["→ 18 min →", "→"]
        and [" ".join(node.stripped_strings) for node in accessible_timing.find_all("b", recursive=False)] == ["→ 18 minutes →"],
    )
    contact_text = " ".join(contact_soup.stripped_strings)
    check(
        "First Contact preserves the timestamp arithmetic and correlation boundary",
        "0.3 hours, or 18 minutes, after docking" in contact_text
        and "larger “hours ago” value is earlier" in contact_text
        and "It remains correlation, not proof" in contact_text
        and "timing alone cannot rule out another docking-related cause" in contact_text,
    )
    check(
        "First Contact page counts remain unchanged",
        len(contact_soup.select('section[data-role="student"]')) == 5
        and len(contact_soup.select('section[data-role="answer"]')) == 5
        and len(contact_soup.select('section[data-role="teacher"]')) == 8
        and len(contact_soup.select('section[data-role="accessible"]')) == 7,
    )

    contact_css_start = css.index("Timeline/event-log family expansion: First Contact Protocol.")
    contact_css_end = css.index("Timeline/event-log family completion: Silent Grove sleep-pattern example.", contact_css_start)
    contact_css = css[contact_css_start:contact_css_end]
    contact_css_without_comments = re.sub(
        r"/\*.*?\*/",
        "",
        contact_css.split("*/", 1)[1],
        flags=re.DOTALL,
    )
    required_contact_css = (
        '.worksheet-document[data-case-id="SSS-C1-CASE06"]',
        "SAA EVENT TELEMETRY · REPORTED ORDER · NOT TO SCALE",
        'content: "DOCKING EVENT"',
        'content: "LAST SIGNAL"',
        'content: "FIRST-CYCLE OBSERVATION"',
        "repeating-linear-gradient",
        "radial-gradient",
        "body.grayscale",
    )
    check(
        "the shared component layer declares the complete case-scoped First Contact timing grammar",
        all(token in contact_css for token in required_contact_css),
        [token for token in required_contact_css if token not in contact_css],
    )
    check(
        "the First Contact timing layer stays inside the extracted shared visual payload",
        css.index("/* BEGIN SSS/HHH EXPLANATORY-VISUAL PRIMITIVES */") < contact_css_start < contact_css_end,
    )
    check(
        "the First Contact timing layer introduces no new numeric evidence or time axis",
        not re.search(r"72\.[14]|18\s*(?:min|minutes)|0\.3\s*h|axis|grid-template-columns:\s*\d", contact_css_without_comments, flags=re.IGNORECASE),
        contact_css_without_comments[:240],
    )
    check(
        "the First Contact timing layer remains strictly Case 06 scoped",
        contact_css.count('.worksheet-document[data-case-id="SSS-C1-CASE06"]') >= 10
        and "SSS-C1-CASE0" not in contact_css.replace("SSS-C1-CASE06", ""),
    )

    case06_harness_start = harness.index('if (item.id === "SSS-C1-CASE06")')
    case06_harness_end = harness.index('if (item.id === "SSS-C1-CASE07")', case06_harness_start)
    case06_harness = harness[case06_harness_start:case06_harness_end]
    check(
        "the browser harness measures First Contact timing fit and exact rendering in both modes",
        harness.count("reported timing strip preserves exact ordinal telemetry") == 1
        and harness.count("timing-strip pages retain strict fit, page counts and geometry") == 1
        and 'for (const grayscale of [false, true])' in case06_harness
        and 'state.pageSize === "816x1056"' in case06_harness
        and "SAA EVENT TELEMETRY · REPORTED ORDER · NOT TO SCALE" in case06_harness
        and "→ 18 min →|→" in case06_harness
        and "→ 18 minutes →" in case06_harness,
    )

    contact_source_paths = (
        "sss/campaign-1/case-06-first-contact-protocol/source/content.html",
        "sss/campaign-1/case-06-first-contact-protocol/source/presentation.css",
        "sss/campaign-1/case-06-first-contact-protocol/source/layout-overrides.json",
        "sss/campaign-1/case-06-first-contact-protocol/source/case-package.json",
        "sss/campaign-1/case-06-first-contact-protocol/source/task-registry.js",
    )
    check(
        "the accepted handoff protects all frozen First Contact sources",
        all(path in handoff for path in contact_source_paths),
        [path for path in contact_source_paths if path not in handoff],
    )
    check(
        "the plan and handoff accept C1C6-VIS01 as the second Family 3 finding",
        bool(re.search(
            r"\| `C1C6-VIS01` .*\| 3 · Timeline/event log \|.*"
            r"`VERIFIED-FAMILY · 30/30 TIMELINE STATIC PASS · 2336/2336 BROWSER PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 66a3d1b ACCEPTED`",
            plan,
        ))
        and "Accepted Family 3 expansion — First Contact reported-event telemetry" in handoff
        and "66a3d1b76077201cbd438f2b70b64e4a1380d7a2" in handoff
        and "2336/2336 PASS with 0 application JavaScript errors" in handoff
        and "30/30 PASS" in handoff
        and "| `C1C6-VIS01` | `66a3d1b` | `VERIFIED-FAMILY` |" in handoff
        and "At the preceding First Contact timing-telemetry closeout" in plan
        and bool(re.search(r"22 of 36 completed\s+and 14 of 36 remaining", plan)),
    )

    sleep_figures = silent_soup.select(
        '.teaching-analogy[data-analogy="sleep-pattern-v1"] .figure[data-figure-id^="fig-sleep-"]'
    )
    sleep_roles = [figure.find_parent("section", attrs={"data-role": True})["data-role"] for figure in sleep_figures]
    check(
        "Silent Grove retains one sleep-pattern teaching figure in Student and Accessible",
        len(sleep_figures) == 2 and sorted(sleep_roles) == ["accessible", "student"],
        sleep_roles,
    )

    expected_sleep_text = (
        "Mia sleeps one unbroken 8-hour block. Sam sleeps eight one-hour naps spread around the "
        "clock. Both sleep 8 hours in a day."
    )
    sleep_analogies = silent_soup.select('.teaching-analogy[data-analogy="sleep-pattern-v1"]')
    check(
        "both learner editions retain the exact same-total teaching example and source disclaimer",
        len(sleep_analogies) == 2
        and all(expected_sleep_text in " ".join(node.stripped_strings) for node in sleep_analogies)
        and all(
            "These sleep hours are just for this example. They are not measurements from the grove."
            in " ".join(node.stripped_strings)
            for node in sleep_analogies
        ),
    )

    expected_caption = (
        "Figure A · Two sleep patterns with the same daily total — teaching example, not grove data. "
        "Discrete blocks only; no curve is drawn."
    )
    check(
        "both sleep figures retain their semantic title, caption and extended description",
        all(
            figure.select_one("svg").get("aria-label") == "Two sleep patterns with the same daily total"
            and figure.select_one("title").get_text(strip=True) == "Two sleep patterns with the same daily total"
            and " ".join(figure.select_one("figcaption").stripped_strings) == expected_caption
            and "one shaded block running from hour 0 to hour 8" in " ".join(figure.select_one(".extended-description").stripped_strings)
            and "eight separate shaded blocks of one hour each" in " ".join(figure.select_one(".extended-description").stripped_strings)
            for figure in sleep_figures
        ),
    )

    def sleep_geometry(figure: object) -> tuple[object, ...]:
        svg = figure.select_one("svg")
        rects = svg.find_all("rect", recursive=False)
        return (
            svg.get("viewbox"),
            len(rects),
            len([rect for rect in rects if rect.get("fill", "").startswith("url(")]),
            (rects[1].get("x"), rects[1].get("width")),
            [(rect.get("x"), rect.get("width")) for rect in rects[3:]],
            [node.get_text(strip=True) for node in svg.select(".fig-tick")],
        )

    expected_geometry = (
        "0 0 640 104",
        11,
        9,
        ("120.0", "160.0"),
        [(f"{x:.1f}", "20.0") for x in (140, 200, 260, 320, 380, 440, 500, 560)],
        ["0", "6", "12", "18", "24"],
    )
    check(
        "both sleep figures retain the exact discrete 24-hour block geometry",
        all(sleep_geometry(figure) == expected_geometry for figure in sleep_figures),
        [sleep_geometry(figure) for figure in sleep_figures],
    )
    check(
        "the sleep example contains no direct curve or interpolated series",
        all(
            not figure.select_one("svg").find_all(["path", "polyline"], recursive=False)
            and len(figure.select_one("svg").find_all("line", recursive=False)) == 6
            for figure in sleep_figures
        ),
    )

    expected_sleep_fields = {
        "student": ["t3-total", "t3-why", "t3-grove"],
        "accessible": ["a3-total", "a3-why", "a3-grove"],
    }
    sleep_field_detail = {}
    for role, expected_ids in expected_sleep_fields.items():
        page = silent_soup.select_one(f'section[data-role="{role}"][data-page-id="{role}-mission-03"]')
        prefix = "t3-" if role == "student" else "a3-"
        fields = page.select(f'[data-persist-id^="{prefix}"][data-response]')
        sleep_field_detail[role] = [field.get("data-persist-id") for field in fields]
    check(
        "Silent Grove Task 3 retains all six ordered blank learner responses",
        sleep_field_detail == expected_sleep_fields
        and all(
            not field.get_text(strip=True)
            for role in expected_sleep_fields
            for field in silent_soup.select(
                f'section[data-role="{role}"][data-page-id="{role}-mission-03"] [data-persist-id^="{"t3-" if role == "student" else "a3-"}"][data-response]'
            )
        ),
        sleep_field_detail,
    )
    check(
        "Silent Grove role page counts remain unchanged",
        len(silent_soup.select('section[data-role="student"]')) == 6
        and len(silent_soup.select('section[data-role="answer"]')) == 4
        and len(silent_soup.select('section[data-role="teacher"]')) == 8
        and len(silent_soup.select('section[data-role="accessible"]')) == 8,
    )

    task3_tables = [
        silent_soup.select_one('section[data-page-id="student-mission-03"] .timeline-table'),
        silent_soup.select_one('section[data-page-id="accessible-mission-03"] .timeline-table'),
    ]
    check(
        "the teaching figures remain distinct from the exact six-row ship record",
        all(table is not None and len(table.select("tbody tr")) == 6 for table in task3_tables)
        and all("Within-cycle signalling record — ship records" in " ".join(table.caption.stripped_strings) for table in task3_tables)
        and all("40–80 ppb" not in " ".join(figure.stripped_strings) and "0.0 ppb" not in " ".join(figure.stripped_strings) for figure in sleep_figures),
    )

    silent_css_start = css.index("Timeline/event-log family completion: Silent Grove sleep-pattern example.")
    silent_css_end = css.index("/* END SSS/HHH EXPLANATORY-VISUAL PRIMITIVES */", silent_css_start)
    silent_css = css[silent_css_start:silent_css_end]
    silent_css_without_comments = re.sub(r"/\*.*?\*/", "", silent_css, flags=re.DOTALL)
    required_silent_css = (
        '.worksheet-document[data-case-id="SSS-C2-CASE04"]',
        'data-analogy="sleep-pattern-v1"',
        'data-figure-id^="fig-sleep-"',
        "SAA TEACHING EXAMPLE · SAME TOTAL / DIFFERENT PATTERN · NOT GROVE DATA",
        "stroke-dasharray: none",
        "stroke-dasharray: 3 2",
        "repeating-linear-gradient",
        "body.grayscale",
    )
    check(
        "the shared component layer declares the complete Silent Grove teaching-example grammar",
        all(token in silent_css for token in required_silent_css),
        [token for token in required_silent_css if token not in silent_css],
    )
    check(
        "the Silent Grove teaching-example layer stays inside the extracted shared visual payload",
        css.index("/* BEGIN SSS/HHH EXPLANATORY-VISUAL PRIMITIVES */") < silent_css_start < silent_css_end,
    )
    generated_strings = re.findall(r'content:\s*"([^"]*)"', silent_css_without_comments)
    check(
        "the Silent Grove visual layer generates only the approved teaching-example status rail",
        generated_strings == ["SAA TEACHING EXAMPLE · SAME TOTAL / DIFFERENT PATTERN · NOT GROVE DATA"],
        generated_strings,
    )
    check(
        "the Silent Grove teaching-example layer remains case- and figure-scoped",
        silent_css.count('.worksheet-document[data-case-id="SSS-C2-CASE04"]') >= 12
        and "SSS-C2-CASE0" not in silent_css.replace("SSS-C2-CASE04", "")
        and "timeline-table" not in silent_css
        and "data-response" not in silent_css,
    )

    case04_harness_start = harness.index('if (item.id === "SSS-C2-CASE04")')
    case04_harness_end = harness.index('if (item.id === "SSS-C2-CASE05")', case04_harness_start)
    case04_harness = harness[case04_harness_start:case04_harness_end]
    check(
        "the browser harness measures Silent Grove sleep-example semantics and fit in both modes",
        harness.count("sleep teaching example preserves same-total discrete patterns and source boundary") == 1
        and harness.count("sleep-example pages retain strict fit, page counts and geometry") == 1
        and 'for (const grayscale of [false, true])' in case04_harness
        and 'state.pageSize === "816x1056"' in case04_harness
        and "SAA TEACHING EXAMPLE · SAME TOTAL / DIFFERENT PATTERN · NOT GROVE DATA" in case04_harness
        and "120.0|160.0" in case04_harness
        and "140.0/20.0|200.0/20.0" in case04_harness
        and 'studentExample.responseIds === "t3-total|t3-why|t3-grove"' in case04_harness
        and 'accessibleExample.responseIds === "a3-total|a3-why|a3-grove"' in case04_harness,
    )

    silent_source_paths = (
        "sss/campaign-2/case-04-silent-grove/source/content.html",
        "sss/campaign-2/case-04-silent-grove/source/presentation.css",
        "sss/campaign-2/case-04-silent-grove/source/layout-overrides.json",
        "sss/campaign-2/case-04-silent-grove/source/case-package.json",
        "sss/campaign-2/case-04-silent-grove/source/task-registry.js",
    )
    check(
        "the plan and handoff accept C2C4-VIS01 and complete Family 3",
        bool(re.search(
            r"\| `C2C4-VIS01` .*\| 3 · Timeline/event log \|.*"
            r"`VERIFIED-FAMILY · 44/44 TIMELINE STATIC PASS · 2339/2339 BROWSER PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 73e8496 ACCEPTED`",
            plan,
        ))
        and "Accepted Family 3 completion — Silent Grove same-total sleep-pattern example" in handoff
        and "73e8496393f5f29d90abf0e805e4f43c90ca26f9" in handoff
        and "2339/2339 PASS with 0 application JavaScript errors" in handoff
        and "44/44 PASS" in handoff
        and all(path in handoff for path in silent_source_paths)
        and "`a3-total`, `a3-why`, `a3-grove`" in handoff
        and "| `C2C4-VIS01` | `73e8496` | `VERIFIED-FAMILY` |" in handoff
        and "Family 3 is complete with all three findings verified" in handoff
        and "23 of 36 completed" in handoff
        and "13 remaining" in handoff,
    )

    failures = [(name, detail) for name, passed, detail in checks if not passed]
    print("SSS visual modernization · timeline family")
    print(f"Result: {len(checks) - len(failures)}/{len(checks)} PASS")
    for name, detail in failures:
        print(f"FAIL: {name}\n  {detail}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
