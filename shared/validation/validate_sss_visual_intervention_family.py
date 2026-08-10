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
GIFT_CASE = ROOT / "sss/campaign-1/case-07-the-gift/source"
GIFT_CONTENT = GIFT_CASE / "content.html"
DANCE_CASE = ROOT / "sss/campaign-2/case-02-missing-dance/source"
DANCE_CONTENT = DANCE_CASE / "content.html"
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

GIFT_FROZEN_HASHES = {
    "content.html": "45d6c471eab166b5761b8c7de43d0352597eb9c4dafa15cb8951ec56783b6a11",
    "presentation.css": "259b76e2d7752680d58e01092e2bc3528956e13be7b79c3b453611b6c2d258a4",
    "layout-overrides.json": "0b3fc73e9baddf29e982f01841a66c41f2ae2a96f44d6fe72aadd5e83ebae6ea",
    "case-package.json": "fdd287d5b3874d20f49b94836f0bff3ccf24702eb3ee17093f60b2cc6f39871c",
    "task-registry.js": "5d6e5fe1223b4faee4e5f49c41e0bd4e1ae7e92767027ee15dce5adc268eeaff",
}

DANCE_FROZEN_HASHES = {
    "content.html": "56338f5db3e89c9187f61fcf130f13c572f00f82173744cade9db810c627c57a",
    "presentation.css": "ed0fd67a1433a4c035e3f1b1a3c61065fee064fdc18d392985f285b8e378f28d",
    "layout-overrides.json": "92c3b314b05261245fe923cd278edfcaf7a1695fe526cdf2223e9509f897b49d",
    "case-package.json": "59026d6c4f54b362700018e268f2892a7c837817b4e6ec14e06d810dd9a66881",
    "task-registry.js": "8aaa2854d946f67e5c59261d314bf05764f4f4b21ccaa81009daa6ca4d51eda8",
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
    gift_source = GIFT_CONTENT.read_text(encoding="utf-8")
    gift_soup = BeautifulSoup(gift_source, "html.parser")
    dance_source = DANCE_CONTENT.read_text(encoding="utf-8")
    dance_soup = BeautifulSoup(dance_source, "html.parser")
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

    gift_pages = {
        "student": gift_soup.select_one('[data-page-id="student-mission-05"]'),
        "answer": gift_soup.select_one('[data-page-id="answer-key-05"]'),
        "accessible": gift_soup.select_one('[data-page-id="accessible-mission-07"]'),
    }
    for name, expected in GIFT_FROZEN_HASHES.items():
        actual = sha256(GIFT_CASE / name)
        check(f"frozen The Gift {name} hash remains exact", actual == expected, actual)
    for role, page in gift_pages.items():
        check(f"The Gift {role} Task 7 target page remains present", page is not None)

    gift_student_table = gift_pages["student"].select_one('.intervention-table[data-design-contract="case07-intervention-v1.0"]')
    gift_student_rows = gift_student_table.select("tbody > tr") if gift_student_table else []
    check("The Gift Student retains the three-route decision matrix", len(gift_student_rows) == 3, len(gift_student_rows))
    check(
        "The Gift Student retains exact route order",
        [normalized(row.select_one("th")) for row in gift_student_rows]
        == ["Sealed natural plume", "Verified extraction", "Validated synthesis"],
    )
    check(
        "The Gift Student keeps story ranks subordinate and exact",
        [normalized(row.select("td")[-1]) for row in gift_student_rows]
        == ["+10 best supported", "+5 defensible", "+0 most uncertain"],
    )
    gift_accessible_cards = gift_pages["accessible"].select(".three-col > .source-card")
    check("The Gift Accessible retains exactly three route cards", len(gift_accessible_cards) == 3, len(gift_accessible_cards))
    check(
        "The Gift Accessible retains exact route order and story ranks",
        [normalized(card.select_one("h3")) for card in gift_accessible_cards]
        == ["Sealed natural plume · +10", "Verified extraction · +5", "Validated synthesis · +0"],
    )
    gift_student_fields = gift_pages["student"].select('[data-persist-id^="t7-"][data-response]')
    gift_accessible_fields = gift_pages["accessible"].select('[data-persist-id^="a7-"][data-response]')
    check("The Gift Student retains three exact blank Task 7 response identities", [field.get("data-persist-id") for field in gift_student_fields] == ["t7-recommend", "t7-monitor", "t7-predict"] and all(not normalized(field) for field in gift_student_fields))
    check("The Gift Accessible retains three exact Task 7 response identities", [field.get("data-persist-id") for field in gift_accessible_fields] == ["a7-recommend", "a7-monitor", "a7-predict"])
    check(
        "The Gift Accessible retains only the accepted monitoring scaffold",
        [normalized(field) for field in gift_accessible_fields]
        == ["", "Monitor cue identity and containment. I would stop if ________________________________.", ""],
    )
    gift_answer_blocks = gift_pages["answer"].select(":scope > .page-frame > .content-area > .answer-block")
    check("The Gift Answer Key retains exactly three Task 7 exemplars", len(gift_answer_blocks) == 3, len(gift_answer_blocks))
    check("The Gift Answer Key retains separate recommendation monitoring and prediction exemplars", [block.select_one("strong").get_text(" ", strip=True) for block in gift_answer_blocks] == ["Recommendation and evidence — completed exemplar", "Monitoring and stopping rule — completed exemplar", "Prediction and challenge observation — completed exemplar"])
    check("The Gift learner directions subordinate story ranks to evidence", "story rankings; justify your choice with evidence, not points" in normalized(gift_pages["student"]) and "points are story rankings; use evidence to justify your answer" in normalized(gift_pages["accessible"]))
    check("The Gift safety contract preserves the no-dose and commitment limits", all(token in normalized(gift_pages["accessible"].select_one(".science-note")) for token in ("no safe numerical dose", "Do not invent one", "Exposure can stop before commitment", "do not assume reversibility afterward")))
    check("The Gift Answer Key preserves authorization containment and stop conditions", all(token in normalized(gift_pages["answer"]) for token in ("joint SAA–Zhel'ii authorization", "loss of containment", "unexpected material", "adverse response", "failed verification")))
    check("The Gift prediction remains modeled rather than replicated", "modeled/narrated prediction, not a replicated trial" in normalized(gift_pages["answer"]) and "modeled story outcomes, not repeated trials" in normalized(gift_pages["accessible"]))
    check("The Gift source adds no unsupported dose purity synthesis or safety result", not re.search(r"safe dose (?:is|of)\s*\d|purity (?:is|of)\s*\d|synthesis (?:is|was) safe|guaranteed|replicated (?:success|recovery)", normalized(gift_pages["student"]) + " " + normalized(gift_pages["accessible"]), re.I))

    dance_pages = {
        "student": dance_soup.select_one('[data-page-id="student-mission-06"]'),
        "answer": dance_soup.select_one('[data-page-id="answer-key-04"]'),
        "accessible": dance_soup.select_one('[data-page-id="accessible-mission-08"]'),
    }
    for name, expected in DANCE_FROZEN_HASHES.items():
        actual = sha256(DANCE_CASE / name)
        check(f"frozen The Missing Dance {name} hash remains exact", actual == expected, actual)
    for role, page in dance_pages.items():
        check(f"The Missing Dance {role} Task 8 target page remains present", page is not None)

    dance_factor_names = ["Frequency", "Amplitude", "Duration", "Coupling"]
    for role in ("student", "accessible"):
        cards = dance_pages[role].select(".factor-grid > .factor-card")
        check(f"The Missing Dance {role} retains exactly four trial controls", len(cards) == 4, len(cards))
        check(
            f"The Missing Dance {role} retains exact control order",
            [normalized(card.select_one("strong")) for card in cards] == dance_factor_names,
        )
    dance_student_fields = dance_pages["student"].select('[data-persist-id^="t8-"][data-response]')
    dance_accessible_fields = dance_pages["accessible"].select('[data-persist-id^="a8-"][data-response]')
    check(
        "The Missing Dance Student retains five exact blank Task 8 response identities",
        [field.get("data-persist-id") for field in dance_student_fields]
        == ["t8-first", "t8-measure", "t8-limit", "t8-stop", "t8-why"]
        and all(not normalized(field) for field in dance_student_fields),
    )
    check(
        "The Missing Dance Accessible retains five exact blank Task 8 response identities",
        [field.get("data-persist-id") for field in dance_accessible_fields]
        == ["a8-first", "a8-measure", "a8-limit", "a8-stop", "a8-why"]
        and all(not normalized(field) for field in dance_accessible_fields),
    )
    check(
        "The Missing Dance learner directions require all four settings together",
        "All four of these settings have to be right together, so no single number is enough" in normalized(dance_pages["student"])
        and "These four settings all have to be right together" in normalized(dance_pages["accessible"]),
    )
    check(
        "The Missing Dance learner prompts preserve measurement damage and stop gates",
        all(token in normalized(dance_pages["student"]) for token in ("What you would measure", "damage limit", "Stop-and-revise rule", "not a sufficient plan"))
        and all(token in normalized(dance_pages["accessible"]) for token in ("What you would measure", "damage limit", "Stop-and-revise rule", "not enough")),
    )
    dance_answer = dance_pages["answer"].select_one('h2[data-shell-task-heading="8"] + .answer-block')
    dance_answer_paragraphs = dance_answer.find_all("p", recursive=False) if dance_answer else []
    check("The Missing Dance Answer Key retains exactly six Task 8 guidance paragraphs", len(dance_answer_paragraphs) == 6, len(dance_answer_paragraphs))
    check("The Missing Dance Answer Key accepts any first setting only with a reason", "Accept any of the four with a reason" in normalized(dance_answer_paragraphs[0]))
    check("The Missing Dance Answer Key measures released pollen rather than device state", all(token in normalized(dance_answer_paragraphs[1]) for token in ("Pollen actually released", "outcome, not the intervention")))
    check("The Missing Dance Answer Key treats visible damage as an immediate stop", all(token in normalized(dance_answer_paragraphs[2]) for token in ("observable harm", "immediate stop")))
    check("The Missing Dance Answer Key retains a named stop-and-revise condition", all(token in normalized(dance_answer_paragraphs[3]) for token in ("ends the trial", "no measurable pollen release", "any damage observed")))
    check("The Missing Dance Answer Key keeps 124 Hz insufficient by itself", all(token in normalized(dance_answer_paragraphs[4]) for token in ("Frequency is one of four settings", "too weak", "too brief", "amplitude, duration and coupling")))
    check("The Missing Dance Answer Key keeps conclusions species-and-garden bounded", all(token in normalized(dance_answer_paragraphs[5]) for token in ("this species in this garden", "promise recovery", "Earth flowers")))
    check(
        "The Missing Dance learner source authors no amplitude duration coupling setting or guaranteed result",
        not re.search(
            r"amplitude\s*(?:=|of|at)\s*\d|duration\s*(?:=|of|at)\s*\d|coupling\s*(?:=|of|at)\s*\d|guaranteed (?:release|recovery|fruit)",
            normalized(dance_pages["student"]) + " " + normalized(dance_pages["accessible"]),
            re.I,
        ),
    )

    marker = "Intervention-comparison family pilot: First Contact Protocol."
    css_start = css.index(marker)
    gift_marker = "Intervention-comparison family expansion: The Gift."
    css_end = css.index(gift_marker, css_start)
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

    dance_marker = "Intervention/trial family expansion: The Missing Dance."
    gift_css = css[css.index(gift_marker):css.index(dance_marker)]
    check("The Gift intervention layer is strictly scoped to Case 07", 'data-case-id="SSS-C1-CASE07"' in gift_css and "SSS-C1-CASE0" not in gift_css.replace("SSS-C1-CASE07", ""))
    check("The Gift intervention layer declares five independent structural patterns", all(token in gift_css for token in ("--gift-intervention-supported-pattern", "--gift-intervention-qualified-pattern", "--gift-intervention-uncertain-pattern", "--gift-intervention-monitor-pattern", "--gift-intervention-prediction-pattern")))
    check("The Gift Task 7 heading exposes the evidence-control-monitor relationship", 'content: "EVIDENCE → CONTROL → MONITOR"' in gift_css)
    check("The Gift relationship rail targets all three synchronized editions", all(token in gift_css for token in ("student-mission-05", "answer-key-05", "accessible-mission-07")))
    check("The Gift Student matrix receives a structural outline and rail", "outline: 1.5px solid var(--gift-intervention-line)" in gift_css and "box-shadow: inset 4px 0 0 var(--gift-intervention-line)" in gift_css)
    check("The Gift supported route receives an explicit state", 'content: "SUPPORTED"' in gift_css)
    check("The Gift qualified route receives an explicit state", 'content: "QUALIFIED"' in gift_css)
    check("The Gift synthesis route remains research only", 'content: "RESEARCH ONLY"' in gift_css)
    check("The Gift route states use solid dashed and double borders", all(token in gift_css for token in ("border-left: 4px solid", "border-left: 4px dashed", "border-left: 4px double")))
    check("The Gift Student story-rank column is typographically subordinate", '.intervention-table :is(th, td):last-child' in gift_css and 'font-size: 5.8pt' in gift_css and 'font-family: "JetBrains Mono", monospace' in gift_css)
    check("The Gift Accessible route cards mirror all three route states", ".three-col > .source-card:first-child" in gift_css and ".three-col > .source-card:nth-child(2)" in gift_css and ".three-col > .source-card:nth-child(3)" in gift_css)
    check("The Gift recommendation fields use a solid evidence-selection rail", all(token in gift_css for token in ('data-persist-id="t7-recommend"', 'data-persist-id="a7-recommend"', "border-left: 4px solid var(--gift-intervention-line)")))
    check("The Gift monitoring fields use a dashed stopping-rule rail", all(token in gift_css for token in ('data-persist-id="t7-monitor"', 'data-persist-id="a7-monitor"', "border-left: 4px dashed var(--gift-intervention-line)")))
    check("The Gift prediction fields use a dotted uncertainty rail", all(token in gift_css for token in ('data-persist-id="t7-predict"', 'data-persist-id="a7-predict"', "border-left: 4px dotted var(--gift-intervention-line)")))
    check("The Gift learner response labels retain six-pixel rail clearance", "padding-left: 6px" in gift_css)
    check("The Gift Accessible safety note preserves the uncertainty state", ".science-note" in gift_css and "--gift-intervention-uncertain-pattern" in gift_css)
    check("The Gift Answer Key mirrors recommendation monitoring and prediction gates", all(token in gift_css for token in (".answer-block:nth-of-type(1)", ".answer-block:nth-of-type(2)", ".answer-block:nth-of-type(3)")))
    check("The Gift grayscale treatment targets the same three Task 7 pages", '.worksheet-document.grayscale[data-case-id="SSS-C1-CASE07"]' in gift_css and all(token in gift_css for token in ("student-mission-05", "answer-key-05", "accessible-mission-07")))
    check("The Gift shared layer does not author learner field dimensions", not re.search(r"(?:t7|a7)-(?:recommend|monitor|predict)[^}]*\b(?:width|height|min-height|max-height)\s*:", gift_css, re.S))

    cutaway_marker = "BEGIN SSS/HHH CUTAWAY-VISUAL EXTENSIONS"
    dance_css = css[css.index(dance_marker):css.index(cutaway_marker, css.index(dance_marker))]
    check("The Missing Dance trial layer is strictly scoped to Case 02", 'data-case-id="SSS-C2-CASE02"' in dance_css and "SSS-C2-CASE0" not in dance_css.replace("SSS-C2-CASE02", ""))
    check("The Missing Dance trial layer declares six independent structural patterns", all(token in dance_css for token in ("--dance-trial-frequency-pattern", "--dance-trial-amplitude-pattern", "--dance-trial-duration-pattern", "--dance-trial-coupling-pattern", "--dance-trial-measure-pattern", "--dance-trial-limit-pattern")))
    check("The Missing Dance Task 8 heading exposes the set-measure-stop relationship", 'content: "SET → MEASURE → STOP"' in dance_css)
    check("The Missing Dance relationship rail targets all three synchronized editions", all(token in dance_css for token in ("student-mission-06", "answer-key-04", "accessible-mission-08")))
    check("The Missing Dance control grids receive a structural outline and rail", "outline: 1.5px solid var(--dance-trial-line)" in dance_css and "box-shadow: inset 4px 0 0 var(--dance-trial-line)" in dance_css)
    check("The Missing Dance four controls receive exact direct states", all(f'content: "{token}"' in dance_css for token in ("01 · RATE", "02 · FORCE", "03 · TIME", "04 · TRANSFER")))
    check("The Missing Dance control states use solid dashed dotted and double borders", all(token in dance_css for token in ("border-left: 4px solid", "border-left: 4px dashed", "border-left: 4px dotted", "border-left: 4px double")))
    check("The Missing Dance first-setting fields use a solid control rail", all(token in dance_css for token in ('data-persist-id="t8-first"', 'data-persist-id="a8-first"', "border-left: 4px solid var(--dance-trial-line)")))
    check("The Missing Dance measurement fields use a dashed outcome rail", all(token in dance_css for token in ('data-persist-id="t8-measure"', 'data-persist-id="a8-measure"', "border-left: 4px dashed var(--dance-trial-line)")))
    check("The Missing Dance damage-limit fields use a double safety rail", all(token in dance_css for token in ('data-persist-id="t8-limit"', 'data-persist-id="a8-limit"', "border-left: 4px double var(--dance-trial-line)")))
    check("The Missing Dance stop-rule fields use a double safety rail", all(token in dance_css for token in ('data-persist-id="t8-stop"', 'data-persist-id="a8-stop"', "border-left: 4px double var(--dance-trial-line)")))
    check("The Missing Dance evidence-limit fields use a dotted uncertainty rail", all(token in dance_css for token in ('data-persist-id="t8-why"', 'data-persist-id="a8-why"', "border-left: 4px dotted var(--dance-trial-line)")))
    check("The Missing Dance learner response labels retain six-pixel rail clearance", "padding-left: 6px" in dance_css)
    check("The Missing Dance Answer Key mirrors all six control measurement safety and evidence gates", all(token in dance_css for token in ("> p:first-child", "> p:nth-child(2)", "> p:nth-child(3)", "> p:nth-child(4)", "> p:nth-child(5)", "> p:nth-child(6)")))
    check("The Missing Dance grayscale treatment targets the same three Task 8 pages", '.worksheet-document.grayscale[data-case-id="SSS-C2-CASE02"]' in dance_css and all(token in dance_css for token in ("student-mission-06", "answer-key-04", "accessible-mission-08")))
    check("The Missing Dance shared layer does not author learner field dimensions", not re.search(r"(?:t8|a8)-(?:first|measure|limit|stop|why)[^}]*\b(?:width|height|min-height|max-height)\s*:", dance_css, re.S))

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

    gift_case_start = harness.index('if (item.id === "SSS-C1-CASE07")')
    gift_case_end = harness.index("const approvedMatrixStates", gift_case_start)
    gift_case_harness = harness[gift_case_start:gift_case_end]
    check(
        "browser harness adds exactly three The Gift intervention assertions",
        gift_case_harness.count('`C1 Case 07 ${grayscale ? "grayscale" : "normal"} intervention matrix') == 1
        and gift_case_harness.count('"C1 Case 07 intervention pages retain strict fit') == 1,
    )
    check("browser harness measures all six The Gift normal and grayscale target views", "giftInterventionPageFit.length === 6" in gift_case_harness and "for (const grayscale of [false, true])" in gift_case_harness)
    check("browser harness requires fixed The Gift worksheet geometry", 'state.pageSize === "816x1056"' in gift_case_harness)
    check("browser harness requires exact The Gift role page counts", all(token in gift_case_harness for token in ('["student", "student-mission-05", 6]', '["answer", "answer-key-05", 6]', '["accessible", "accessible-mission-07", 8]')))
    check("browser harness requires all three The Gift route states", 'SUPPORTED|QUALIFIED|RESEARCH ONLY' in gift_case_harness)
    check("browser harness requires all three The Gift route borders", 'solid|dashed|double' in gift_case_harness)
    check("browser harness preserves exact Student and Accessible route order", all(token in gift_case_harness for token in ("Sealed natural plume|Verified extraction|Validated synthesis", "Sealed natural plume · +10|Verified extraction · +5|Validated synthesis · +0")))
    check(
        "browser harness uses DOM-accurate story ranks and visible Task 7 heading text",
        "+10best supported|+5defensible|+0most uncertain" in gift_case_harness
        and 'rankSize === "7.73|7.73|7.73"' in gift_case_harness
        and 'pageText.includes("7 · Choose and Monitor a Safe Intervention")' in gift_case_harness,
    )
    check("browser harness verifies both The Gift learner field sets", all(token in gift_case_harness for token in ("t7-recommend|t7-monitor|t7-predict", "a7-recommend|a7-monitor|a7-predict")))
    check("browser harness protects The Gift Accessible monitoring scaffold", "Monitor cue identity and containment. I would stop if ________________________________." in gift_case_harness)
    check("browser harness protects The Gift minimum learner field utility", "field.size[0] >= 108 && field.size[1] >= 30" in gift_case_harness)
    check("browser harness verifies The Gift response-gate rail clearance", "label.clearance >= 6" in gift_case_harness and '"solid|dashed|dotted"' in gift_case_harness)
    check("browser harness protects The Gift authorization stopping and evidence limits", all(token in gift_case_harness for token in ("joint SAA–Zhel'ii authorization", "loss of containment, unexpected material, adverse response, or failed verification", "not a replicated trial", "story rankings")))
    check("browser harness rejects The Gift route collision and overflow", "!state.routeCollisions" in gift_case_harness and "state.scrollHeight <= state.clientHeight" in gift_case_harness)

    dance_case_start = harness.index('if (item.id === "SSS-C2-CASE02")')
    dance_case_end = harness.index('if (item.id === "SSS-C2-CASE03")', dance_case_start)
    dance_case_harness = harness[dance_case_start:dance_case_end]
    check(
        "browser harness adds exactly three The Missing Dance trial assertions",
        dance_case_harness.count('`C2 Case 02 ${grayscale ? "grayscale" : "normal"} monitored vibration trial') == 1
        and dance_case_harness.count('"C2 Case 02 monitored vibration trial pages retain strict fit') == 1,
    )
    check("browser harness measures all six The Missing Dance normal and grayscale Task 8 views", "danceTrialPageFit.length === 6" in dance_case_harness and "for (const grayscale of [false, true])" in dance_case_harness)
    check("browser harness requires fixed The Missing Dance worksheet geometry and role page counts", 'state.pageSize === "816x1056"' in dance_case_harness and all(token in dance_case_harness for token in ('["student", "student-mission-06", 6]', '["answer", "answer-key-04", 4]', '["accessible", "accessible-mission-08", 8]')))
    check("browser harness requires all four The Missing Dance control states and borders", all(token in dance_case_harness for token in ("01 · RATE|02 · FORCE|03 · TIME|04 · TRANSFER", "solid|dashed|dotted|double")))
    check("browser harness verifies both exact five-field The Missing Dance learner sets", all(token in dance_case_harness for token in ("t8-first|t8-measure|t8-limit|t8-stop|t8-why", "a8-first|a8-measure|a8-limit|a8-stop|a8-why", "solid|dashed|double|double|dotted")))
    check("browser harness protects The Missing Dance measurement stop and qualifier evidence", all(token in dance_case_harness for token in ("Pollen actually released", "immediate stop", "no measurable pollen release", "Frequency is one of four settings", "amplitude, duration and coupling")))
    check("browser harness rejects The Missing Dance control collision overflow and invented settings", "!state.factorCollisions" in dance_case_harness and "state.scrollHeight <= state.clientHeight" in dance_case_harness and "guaranteed (?:release|recovery|fruit)" in dance_case_harness)

    check(
        "plan records C2C2-VIS03 as the accepted 176-check Family 8 finding",
        bool(re.search(
            r"\| `C2C2-VIS03` .*\| 8 · Intervention comparison/trial workflow \|.*"
            r"`VERIFIED-FAMILY · 176/176 INTERVENTION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · f987bbb ACCEPTED`",
            plan,
        ))
        and "`C2C2-VIS03` is the accepted third standalone Family 8 intervention/trial finding" in plan
        and "`SET → MEASURE → STOP`" in plan
        and "`01 · RATE | 02 · FORCE | 03 · TIME | 04 · TRANSFER`" in plan,
    )
    check(
        "plan preserves The Missing Dance trial limits and records the accepted differential",
        all(token in plan for token in ("strongest release **near 124 Hz**", "does not supply an amplitude, duration or coupling setting", "measure pollen actually released", "Any observable harm is an immediate stop", "f987bbb0c4c7fc34f07bc0f00fd4f38aeceb066b", "**2368/2368 PASS**", "**2371/2371 PASS**", "**+3 registered and +3 passed**", "Canonical project registration remains 2372", "Family 8 now has four of five assignments verified", "**34 of 36 completed / 2 of 36 remaining**")),
    )
    check(
        "handoff accepts The Missing Dance trial and preserves source ownership and frozen hashes",
        "Accepted Family 8 finding — The Missing Dance monitored vibration trial" in handoff
        and "f987bbb0c4c7fc34f07bc0f00fd4f38aeceb066b" in handoff
        and "changes no worksheet wording" in handoff
        and all(value in handoff for value in DANCE_FROZEN_HASHES.values()),
    )
    check(
        "handoff preserves exact controls fields science rendered evidence and acceptance boundary",
        all(token in handoff for token in ("`01 · RATE | 02 · FORCE | 03 · TIME | 04 · TRANSFER`", "`SET → MEASURE → STOP`", "t8-first | t8-measure | t8-limit | t8-stop | t8-why", "a8-first | a8-measure | a8-limit | a8-stop | a8-why", "strongest release is reported **near 124 Hz**", "no numeric setting", "Observable damage is an immediate stop", "**176/176 PASS**", "**2371/2371 PASS**", "**2368/2368 PASS**", "**+3 registered and +3 passed**", "Canonical project registration remains 2372", "no general Mac, Chrome, browser, platform or environment exception", "exact 936/936 content fit", "The formal inventory is now **34 of 36 completed**", "with **2 remaining**")),
    )

    check(
        "plan records C1C7-VIS03 as the accepted corrected Family 8 finding",
        bool(re.search(
            r"\| `C1C7-VIS03` .*\| 8 · Intervention comparison/trial workflow \|.*"
            r"`VERIFIED-FAMILY · 125/125 INTERVENTION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 917908c ACCEPTED`",
            plan,
        ))
        and "accepted second standalone Family 8 intervention-comparison finding" in plan
        and "`C1C7-VIS03` is therefore `VERIFIED-FAMILY`" in plan
        and "`EVIDENCE → CONTROL → MONITOR`" in plan
        and all(token in plan for token in ("`SUPPORTED`", "`QUALIFIED`", "`RESEARCH ONLY`", "2360/2362", "DOM-structure oracle defects")),
    )
    check(
        "plan advances accepted inventory to 31 of 36 and Family 8 to three of five",
        "Accepted progress after The Gift intervention-comparison closeout is **31 of 36 completed**" in plan
        and "**5 of 36 remaining**" in plan
        and "At that checkpoint, Family 8 had three of five assignments verified" in plan
        and "Accepted progress after the First Contact intervention-comparison closeout is **30 of 36 completed**" in plan,
    )
    check(
        "handoff preserves The Gift source ownership and all five frozen hashes",
        "Accepted Family 8 finding — The Gift controlled response" in handoff
        and "changes no worksheet wording" in handoff
        and all(value in handoff for value in GIFT_FROZEN_HASHES.values()),
    )
    check("handoff preserves exact The Gift route and response-gate states", all(token in handoff for token in ("`SUPPORTED`", "`QUALIFIED`", "`RESEARCH ONLY`", "solid evidence-selection rail", "dashed verification rail", "dotted uncertainty rail")))
    check("handoff preserves The Gift dose commitment and prediction limits", all(token in handoff for token in ("no safe numerical dose", "Exposure can stop before commitment", "not replicated trials or guaranteed outcomes", "formula is insufficient")))
    check(
        "handoff records candidate-specific differential acceptance without platform policy",
        "2359/2359 PASS" in handoff
        and "Run 2 each passed **2362/2362 PASS**" in handoff
        and "+3 registered and +3 passed" in handoff
        and "all three The Gift assertions registered and passed" in handoff
        and "both formerly defective browser" in handoff
        and "Canonical project registration remains 2363" in handoff
        and "does not establish a general platform policy" in handoff
        and "focused intervention/trial validator is **125/125 PASS**" in handoff
        and "first browser execution" in handoff
        and "2360/2362" in handoff
        and "DOM-accurate expectations" in handoff
        and "The formal inventory is now **31 of 36 completed**" in handoff
        and "with **5 remaining**" in handoff
        and "Family 8 has three of five assignments verified" in handoff
        and "Failed implementation `d97fd46…` remains an immutable" in handoff,
    )

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
        "plan preserves the preceding First Contact 30-of-36 milestone",
        "Accepted progress after the First Contact intervention-comparison closeout is **30 of 36 completed**" in plan
        and "and **6 of 36 remaining**" in plan
        and "Accepted progress after the Silent Grove specification/verification closeout is **29 of 36 completed**" in plan,
    )
    check(
        "plan identifies the accepted Family 8 hybrid without double-counting in the current inventory",
        "accepted hybrid `C2C5-VIS03`, already counted once in the unique inventory" in plan
        and "accepted corrective standalone `C1C7-VIS03`" in plan
        and "Family 8 now has three of five assignments verified" in plan,
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
    return 0 if passed == len(checks) == 176 else 1


if __name__ == "__main__":
    raise SystemExit(main())
