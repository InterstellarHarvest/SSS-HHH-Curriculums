#!/usr/bin/env python3
"""Focused deterministic checks for the SSS mechanism/pathway visual family."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
HANDOFF = ROOT / "sss/audit/final/SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
EDITOR = ROOT / "apps/curriculum-editor/editor-app.js"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
ISS_SOURCE = ROOT / "sss/campaign-1/case-01-iss-greenhouse/source"
ISS_PACKAGE = ISS_SOURCE / "case-package.json"
ISS_CONTENT = ISS_SOURCE / "content.html"
ISS_PRESENTATION = ISS_SOURCE / "presentation.css"
SOURCE = ROOT / "sss/campaign-1/case-02-lunar-greenhouse/source"
PACKAGE = SOURCE / "case-package.json"
CONTENT = SOURCE / "content.html"
PRESENTATION = SOURCE / "presentation.css"
MARS_SOURCE = ROOT / "sss/campaign-1/case-03-mars-habitat/source"
MARS_PACKAGE = MARS_SOURCE / "case-package.json"
MARS_CONTENT = MARS_SOURCE / "content.html"
MARS_PRESENTATION = MARS_SOURCE / "presentation.css"
HAYES_SOURCE = ROOT / "sss/campaign-1/case-04-hayes-orbital-station/source"
HAYES_PACKAGE = HAYES_SOURCE / "case-package.json"
HAYES_CONTENT = HAYES_SOURCE / "content.html"
HAYES_PRESENTATION = HAYES_SOURCE / "presentation.css"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    plan = PLAN.read_text(encoding="utf-8")
    handoff = HANDOFF.read_text(encoding="utf-8")
    css = COMPONENTS.read_text(encoding="utf-8")
    editor = EDITOR.read_text(encoding="utf-8")
    harness = HARNESS.read_text(encoding="utf-8")
    iss_package = json.loads(ISS_PACKAGE.read_text(encoding="utf-8"))
    iss_content = BeautifulSoup(ISS_CONTENT.read_text(encoding="utf-8"), "html.parser")
    package = json.loads(PACKAGE.read_text(encoding="utf-8"))
    content = BeautifulSoup(CONTENT.read_text(encoding="utf-8"), "html.parser")
    mars_package = json.loads(MARS_PACKAGE.read_text(encoding="utf-8"))
    mars_content = BeautifulSoup(MARS_CONTENT.read_text(encoding="utf-8"), "html.parser")
    hayes_package = json.loads(HAYES_PACKAGE.read_text(encoding="utf-8"))
    hayes_content = BeautifulSoup(HAYES_CONTENT.read_text(encoding="utf-8"), "html.parser")

    check(
        "the production plan assigns the Lunar pollination sequence to Family 2",
        bool(re.search(r"\| `C1C2-VIS01` .*\| 2 · Causal mechanism/pathway \|", plan)),
    )
    check(
        "the production plan records the accepted ISS comparison and advances the Hayes fault loop",
        bool(re.search(
            r"\| `C1C1-VIS01` .*\| 2 · Causal mechanism/pathway \|.*"
            r"`VERIFIED-FAMILY · 35/35 FAMILY STATIC PASS · 2306/2306 BROWSER PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 884/884 · ceb632d ACCEPTED`",
            plan,
        ))
        and bool(re.search(
            r"\| `C1C4-VIS02` .*\| 2 · Causal mechanism/pathway \|.*"
            r"`IMPLEMENTED-CANDIDATE · BROWSER GATE PENDING`",
            plan,
        ))
        and "Current validation target — C1C4 closed reactor fault loop" in handoff
        and "2309/2309 PASS with 0 application JavaScript errors" in handoff
        and "44/44 PASS" in handoff,
    )
    check(
        "the accepted pilot and Mars expansion have explicit lifecycle states",
        bool(re.search(r"\| `C1C2-VIS01` .*`VERIFIED-FAMILY-PILOT .*2300/2300 BROWSER PASS", plan))
        and bool(re.search(
            r"\| `C1C3-VIS03` .*`VERIFIED-FAMILY · 25/25 FAMILY STATIC PASS "
            r"· 2303/2303 BROWSER PASS ×2 · 0 JS ERRORS · STRICT FIT 936/936 "
            r"· 3\.47px RESERVE · c532ac5 ACCEPTED`",
            plan,
        ))
        and "The earlier C1C3 expansion could advance from `IMPLEMENTED-CANDIDATE`" in handoff
        and "2303/2303 with zero JavaScript errors" in handoff
        and "3.47 px reserve" in handoff
        and "The recorded outcome above satisfies every condition." in handoff,
    )
    check(
        "Lunar Greenhouse opts into extracted shared visuals without the full component layer",
        package.get("presentation", {}).get("sharedVisualStyles") is True
        and package.get("presentation", {}).get("sharedComponentStyles") is not True,
        package.get("presentation"),
    )
    check(
        "ISS Greenhouse opts into extracted shared visuals without the full component layer",
        iss_package.get("presentation", {}).get("sharedVisualStyles") is True
        and iss_package.get("presentation", {}).get("sharedComponentStyles") is not True,
        iss_package.get("presentation"),
    )
    check(
        "the ISS package-controlled worksheet sources remain byte-identical to their declared hashes",
        iss_package["sourceHashes"]["content"] == sha256(ISS_CONTENT)
        and iss_package["sourceHashes"]["presentation"] == sha256(ISS_PRESENTATION),
        {
            "content": [iss_package["sourceHashes"]["content"], sha256(ISS_CONTENT)],
            "presentation": [iss_package["sourceHashes"]["presentation"], sha256(ISS_PRESENTATION)],
        },
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
    check(
        "Mars Habitat retains its shared-visual opt-in and byte-identical worksheet sources",
        mars_package.get("presentation", {}).get("sharedVisualStyles") is True
        and mars_package["sourceHashes"]["content"] == sha256(MARS_CONTENT)
        and mars_package["sourceHashes"]["presentation"] == sha256(MARS_PRESENTATION),
        {
            "presentation": mars_package.get("presentation"),
            "content": [mars_package["sourceHashes"]["content"], sha256(MARS_CONTENT)],
            "stylesheet": [mars_package["sourceHashes"]["presentation"], sha256(MARS_PRESENTATION)],
        },
    )
    check(
        "Hayes Orbital Station opts into shared visuals with byte-identical worksheet sources",
        hayes_package.get("presentation", {}).get("sharedVisualStyles") is True
        and hayes_package.get("presentation", {}).get("sharedComponentStyles") is True
        and hayes_package["sourceHashes"]["content"] == sha256(HAYES_CONTENT)
        and hayes_package["sourceHashes"]["presentation"] == sha256(HAYES_PRESENTATION),
        {
            "presentation": hayes_package.get("presentation"),
            "content": [hayes_package["sourceHashes"]["content"], sha256(HAYES_CONTENT)],
            "stylesheet": [hayes_package["sourceHashes"]["presentation"], sha256(HAYES_PRESENTATION)],
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
        '.worksheet-document[data-case-id="SSS-C1-CASE01"]',
        "SETTLED · CUE ↓",
        "NO STABLE CUE",
        "data:image/svg+xml,%3Csvg",
        '.worksheet-document[data-case-id="SSS-C1-CASE02"] .process-figure',
        "DEPENDENCY RAIL · EARLIER EVENT ENABLES NEXT",
        "TRACE RESULT · FIRST INTERRUPTION AT STEP 2",
        ".process-figure.completed .failed-stage",
        '.linear-process[data-accessible-organizer="sequence"]',
        "grid-template-columns: repeat(5, minmax(0, 1fr) .19in) minmax(0, 1fr)",
        '.worksheet-document[data-case-id="SSS-C1-CASE03"] .canonical-process',
        "SPECTRAL-LOSS PATHWAY · CASE-SPECIFIC MODEL",
        'data-process-stage="3"',
        'content: "BAND LOSS"',
        '.worksheet-document[data-case-id="SSS-C1-CASE04"]',
        'content: "↺ REPEAT TO STAGE 1"',
        'content: "RECURRENCE"',
        '.accessible-cycle::after',
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
    iss_css = extracted[extracted.index("Mechanism/pathway family expansion: ISS") : extracted.index("Mechanism/pathway pilot.")]
    hayes_css = extracted[extracted.index("Mechanism/pathway family expansion: Hayes") :]
    check(
        "the ISS cutaways encode distinct settled and dispersed statolith/root states without a color-only filter",
        iss_css.count("data:image/svg+xml,%3Csvg") == 2
        and "SETTLED · CUE ↓" in iss_css
        and "NO STABLE CUE" in iss_css
        and "border-left-style: solid" in iss_css
        and "border-left-style: double" in iss_css
        and "border-top-style: dashed" in iss_css
        and "filter:" not in iss_css,
    )
    check(
        "the mechanism grammar uses border and pattern states without a whole-figure filter",
        "repeating-linear-gradient" in mechanism_css
        and "border-top-style: double" in mechanism_css
        and "border-top-style: dashed" in mechanism_css
        and "filter:" not in mechanism_css,
    )
    check(
        "the Hayes fault loop uses a direct repeat rail plus grayscale-independent stage states",
        hayes_css.count('content: "↺ REPEAT TO STAGE 1"') == 2
        and all(f'content: "{label}"' in hayes_css for label in (
            "EXPOSURE", "LOAD", "DAMAGE", "DECLINE", "REBUILD", "RECURRENCE"
        ))
        and "border-top-style: double" in hayes_css
        and "border-top-style: dashed" in hayes_css
        and "repeating-linear-gradient" in hayes_css
        and ".accessible-cycle::after" in hayes_css
        and "filter:" not in hayes_css,
    )
    check(
        "the Mars Student page compacts only mechanism chrome while preserving stage response height",
        '.page[data-role="student"][data-page-id="student-mission-03"]' in mechanism_css
        and '.canonical-process[data-process-layout="horizontal"]' in mechanism_css
        and "margin-block: 1px" in mechanism_css
        and "padding-top: .2in" in mechanism_css
        and '+ .canonical-phrase-bank[data-phrase-bank-contract="sequence-v1.0"]' in mechanism_css
        and "margin-top: 2px" in mechanism_css
        and "min-height: 2.25in" not in mechanism_css,
    )
    case02_visual_start = harness.index('if (item.id === "SSS-C1-CASE02")')
    case03_visual_start = harness.index('if (item.id === "SSS-C1-CASE03")', case02_visual_start)
    next_visual_start = harness.index('if (item.id === "SSS-C2-CASE03")', case03_visual_start)
    case02_visual_block = harness[case02_visual_start:case03_visual_start]
    case03_visual_block = harness[case03_visual_start:next_visual_start]
    state_reset = (
        'api.setRole("student");\n'
        '          api.saveState({ grayscale: false });\n'
        '          await wait(20);'
    )
    check(
        "the C1C2 block restores Student normal state before the C1C3 block initializes it independently",
        bool(re.search(re.escape(state_reset) + r"\s+}\s*$", case02_visual_block))
        and bool(re.match(
            r'if \(item\.id === "SSS-C1-CASE03"\) \{\s+' + re.escape(state_reset),
            case03_visual_block,
        )),
    )
    check(
        "the C1C3 browser block requires strict Mars Student page fit with real bottom reserve",
        harness.count("C1 Case 03 Student mechanism page retains strict integer fit and positive bottom reserve") == 1
        and "C1 Case 03 Student mechanism page retains strict integer fit and positive bottom reserve" not in case02_visual_block
        and "C1 Case 03 Student mechanism page retains strict integer fit and positive bottom reserve" in case03_visual_block
        and "marsStudentContent.scrollHeight <= marsStudentContent.clientHeight" in case03_visual_block
        and "marsStudentReserve >= 3" in case03_visual_block,
    )

    iss_student_page = iss_content.select_one('section[data-role="student"][data-page-id="student-2"]')
    iss_student_cards = iss_student_page.select(".compare-card") if iss_student_page else []
    iss_student_fields = [field for card in iss_student_cards for field in card.select(".mini-blank")]
    iss_expected_bank = "curve or grow without consistent orientation · downward · settle · settle in one direction"
    check(
        "the ISS Student comparison retains two pathways and four blank response identities",
        len(iss_student_cards) == 2
        and [field.get("data-persist-id") for field in iss_student_fields]
        == ["s2-earth-settle", "s2-earth-root", "s2-micro-settle", "s2-micro-root"]
        and all(field.has_attr("data-response") and not field.get_text(strip=True) for field in iss_student_fields),
        [field.get("data-persist-id") for field in iss_student_fields],
    )
    check(
        "the ISS Student exact-match word bank remains unchanged",
        " ".join(iss_student_page.select_one(".word-bank-terms").stripped_strings) == iss_expected_bank,
    )

    iss_accessible_page = iss_content.select_one('section[data-role="accessible"][data-page-id="accessible-3"]')
    iss_accessible_cards = iss_accessible_page.select(".compare-card") if iss_accessible_page else []
    iss_accessible_fields = [field for card in iss_accessible_cards for field in card.select(".mini-blank")]
    check(
        "the ISS Accessible comparison preserves the approved Earth exemplar and two Microgravity blanks",
        len(iss_accessible_cards) == 2
        and [field.get("data-persist-id") for field in iss_accessible_fields]
        == ["a-earth-settle", "a-earth-root", "a-micro-settle", "a-micro-root"]
        and [field.get_text(strip=True) for field in iss_accessible_fields] == ["settle", "downward", "", ""]
        and all(field.has_attr("data-response") for field in iss_accessible_fields),
    )

    iss_answer_page = iss_content.select_one('section[data-role="answer"][data-page-id="answer-2"]')
    iss_answer_paths = iss_answer_page.select('.task-heading[data-task-id="5"] + .answer-block > p') if iss_answer_page else []
    iss_answer_text = [" ".join(path.stripped_strings) for path in iss_answer_paths]
    iss_accuracy_note = " ".join(iss_answer_page.select_one(".callout-caution").stripped_strings) if iss_answer_page else ""
    check(
        "the ISS Answer Key retains both complete qualified pathways",
        len(iss_answer_paths) == 2
        and all(
            phrase in "|".join(iss_answer_text)
            for phrase in (
                "statoliths settle",
                "roots grow downward",
                "do not settle in one direction",
                "curve or grow without consistent orientation",
            )
        )
        and "Avoid requiring “random.”" in iss_accuracy_note
        and "moisture, light, touch, chemicals, and internal growth programs" in iss_accuracy_note,
        {"paths": iss_answer_text, "accuracy_note": iss_accuracy_note},
    )
    check(
        "the ISS mechanism expansion adds no duplicate organizer to Teacher pages",
        not iss_content.select_one('section[data-role="teacher"] .compare-card'),
    )
    check(
        "the browser harness measures ISS cutaways, exact fields and strict page fit in normal and grayscale",
        harness.count("gravity-sensing cutaways distinguish settled and unsettled pathways") == 1
        and harness.count("gravity-sensing comparison pages retain strict integer fit") == 1
        and "SETTLED · CUE ↓" in harness
        and "NO STABLE CUE" in harness
        and "s2-earth-settle|s2-earth-root|s2-micro-settle|s2-micro-root" in harness
        and "a-earth-settle|a-earth-root|a-micro-settle|a-micro-root" in harness,
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
        and harness.count("shared mechanism grammar renders the spectral-loss chain") == 1
        and 'for (const grayscale of [false, true])' in harness
        and 'horizontal[1].failedBorder === "double"' in harness
        and "accessibleState.steps === 6" in harness
        and 'stageLabels.join("|") === "INTAKE|FILTER|BAND LOSS|CHLOROPHYLL|OUTCOME"' in harness,
    )

    mars_expected = [
        "12 m light pipe and collector filter",
        "Wrong BP-4 filter installed",
        "Red and deep-red transmission drops",
        "New chlorophyll production is disrupted",
        "New growth becomes pale or white",
    ]
    mars_bank = [
        "New chlorophyll production is disrupted",
        "Wrong BP-4 filter installed",
        "New growth becomes pale or white",
        "Red and deep-red transmission drops",
    ]

    mars_processes = {
        role: mars_content.select_one(
            f'section[data-role="{role}"] .canonical-process[data-process-contract="five-stage-v1.0"]'
        )
        for role in ("student", "teacher", "answer", "accessible")
    }
    mars_stages = {
        role: process.select(":scope > .canonical-process-stage") if process else []
        for role, process in mars_processes.items()
    }
    check(
        "the Mars chain retains five ordered stages and four connectors in every synchronized role",
        all(
            process
            and len(mars_stages[role]) == 5
            and len(process.select(":scope > .canonical-process-arrow")) == 4
            and [stage.get("data-process-stage") for stage in mars_stages[role]] == ["1", "2", "3", "4", "5"]
            for role, process in mars_processes.items()
        ),
        {role: [len(mars_stages[role]), len(process.select(":scope > .canonical-process-arrow")) if process else 0]
         for role, process in mars_processes.items()},
    )
    check(
        "the completed Teacher and Answer Key chains preserve the exact approved sequence",
        all(
            [" ".join(stage.stripped_strings) for stage in mars_stages[role]]
            == [f"{index} {phrase}" for index, phrase in enumerate(mars_expected, start=1)]
            for role in ("teacher", "answer")
        ),
        {role: [" ".join(stage.stripped_strings) for stage in mars_stages[role]] for role in ("teacher", "answer")},
    )
    student_mars_fields = [stage.select_one(".canonical-process-response") for stage in mars_stages["student"][1:]]
    check(
        "the Mars Student chain preserves one fixed intake and four blank writable response identities",
        " ".join(mars_stages["student"][0].stripped_strings) == "1 " + mars_expected[0]
        and [field.get("data-persist-id") for field in student_mars_fields] == ["m-2", "m-3", "m-4", "m-5"]
        and all(field.has_attr("data-response") and not field.get_text(strip=True) for field in student_mars_fields),
    )
    accessible_mars_fields = [stage.select_one(".canonical-process-response") for stage in mars_stages["accessible"][1:]]
    check(
        "the Mars Accessible chain stays vertical with only the approved filter-stage prefill",
        mars_processes["accessible"].get("data-process-layout") == "vertical"
        and [field.get("data-persist-id") for field in accessible_mars_fields] == ["a6-2", "a6-3", "a6-4", "a6-5"]
        and [field.get_text(strip=True) for field in accessible_mars_fields] == [mars_expected[1], "", "", ""]
        and all(field.has_attr("data-response") for field in accessible_mars_fields),
    )
    check(
        "the Mars phrase bank remains exact and synchronized across learner and key editions",
        all(
            [" ".join(item.stripped_strings) for item in mars_content.select(
                f'section[data-role="{role}"] .canonical-phrase-bank-item'
            )] == mars_bank
            for role in ("student", "answer", "accessible")
        ),
    )
    mars_source_text = MARS_CONTENT.read_text(encoding="utf-8")
    check(
        "the Mars mechanism retains the corrected PAR boundary and case-bounded chlorophyll wording",
        "400-700 nm waveband used for photosynthesis metrics" in mars_source_text
        and "New chlorophyll production is disrupted" in mars_source_text
        and "Red and deep-red transmission drops" in mars_source_text
        and "universal chlorophyll mechanism" not in mars_source_text,
    )

    hayes_student_page = hayes_content.select_one(
        'section[data-role="student"][data-page-id="student-mission-03"]'
    )
    hayes_student_model = hayes_student_page.select_one(
        '.cycle-model[data-process-contract="six-stage-cycle-v1.0"]'
    ) if hayes_student_page else None
    hayes_student_stages = hayes_student_model.select(":scope > .cycle-stage") if hayes_student_model else []
    hayes_student_connectors = [
        connector.get_text(strip=True)
        for connector in hayes_student_model.select(":scope > .cycle-connector")
    ] if hayes_student_model else []
    hayes_student_fields = [stage.select_one("[data-response]") for stage in hayes_student_stages[1:]]
    hayes_student_bank = [
        " ".join(item.stripped_strings) for item in hayes_student_page.select(".mechanism-bank > span")
    ] if hayes_student_page else []
    check(
        "the Hayes Student loop preserves six stages, five blank fields and the exact snake order",
        [stage.get("data-process-stage") for stage in hayes_student_stages] == ["1", "2", "3", "4", "5", "6"]
        and hayes_student_connectors == ["→", "→", "↓", "←", "←"]
        and [field.get("data-persist-id") for field in hayes_student_fields]
        == ["t5-2", "t5-3", "t5-4", "t5-5", "t5-6"]
        and all(field.has_attr("data-response") and not field.get_text(strip=True) for field in hayes_student_fields),
        {
            "stages": [stage.get("data-process-stage") for stage in hayes_student_stages],
            "connectors": hayes_student_connectors,
            "fields": [field.get("data-persist-id") for field in hayes_student_fields],
        },
    )
    check(
        "the Hayes Student mechanism bank remains exact and unexpanded",
        hayes_student_bank == [
            "excessive daily light dose under current conditions",
            "photodamage outpaces repair",
            "productivity and gas exchange fall",
            "survivors rebuild",
            "unchanged exposure causes another crash",
        ],
        hayes_student_bank,
    )

    hayes_accessible_page = hayes_content.select_one(
        'section[data-role="accessible"][data-page-id="accessible-mission-05"]'
    )
    hayes_accessible_model = hayes_accessible_page.select_one(
        '.cycle-model.accessible-cycle[data-process-contract="six-stage-cycle-v1.0"]'
    ) if hayes_accessible_page else None
    hayes_accessible_stages = hayes_accessible_model.select(":scope > .cycle-stage") if hayes_accessible_model else []
    hayes_accessible_fields = [stage.select_one("[data-response]") for stage in hayes_accessible_stages[1:]]
    hayes_accessible_connectors = [
        connector.get_text(strip=True)
        for connector in hayes_accessible_model.select(":scope > .cycle-connector")
    ] if hayes_accessible_model else []
    check(
        "the Hayes Accessible loop stays vertical with one approved prefill and four blanks",
        [stage.get("data-process-stage") for stage in hayes_accessible_stages] == ["1", "2", "3", "4", "5", "6"]
        and hayes_accessible_connectors == ["↓", "↓", "↓", "↓", "↓ then repeat"]
        and [field.get("data-persist-id") for field in hayes_accessible_fields]
        == ["a5-2", "a5-3", "a5-4", "a5-5", "a5-6"]
        and [field.get_text(strip=True) for field in hayes_accessible_fields]
        == ["excessive daily light dose under current operating conditions", "", "", "", ""]
        and all(field.has_attr("data-response") for field in hayes_accessible_fields),
        {
            "connectors": hayes_accessible_connectors,
            "fields": [field.get("data-persist-id") for field in hayes_accessible_fields],
            "contents": [field.get_text(strip=True) for field in hayes_accessible_fields],
        },
    )

    hayes_answer_page = hayes_content.select_one(
        'section[data-role="answer"][data-page-id="answer-key-03"]'
    )
    hayes_answer_model = hayes_answer_page.select_one(
        '.cycle-model.completed[data-process-contract="six-stage-cycle-v1.0"]'
    ) if hayes_answer_page else None
    hayes_answer_stages = hayes_answer_model.select(":scope > .cycle-stage") if hayes_answer_model else []
    hayes_expected = [
        "Uncontrolled 24/0 exposure",
        "Excessive daily light dose under current operating conditions",
        "Photodamage outpaces repair",
        "Culture productivity and gas exchange fall",
        "Surviving cells rebuild",
        "Unchanged exposure causes another crash",
    ]
    check(
        "the Hayes Answer Key completes the identical six-stage recurrence without invented quantities",
        [" ".join(stage.strong.stripped_strings) for stage in hayes_answer_stages] == hayes_expected
        and "Every 6–8 days" not in "|".join(hayes_expected),
        [" ".join(stage.strong.stripped_strings) for stage in hayes_answer_stages],
    )
    hayes_answer_text = " ".join(hayes_answer_page.stripped_strings) if hayes_answer_page else ""
    check(
        "the Hayes keyed commentary preserves the qualitative boundary and reactor-specific recurrence",
        "Qualitative only:" in hayes_answer_text
        and "Students should not invent density curves, exact photon totals, or mission-day timestamps." in hayes_answer_text
        and "Because the external lighting remains unchanged" in hayes_answer_text
        and "safe processing capacity" in hayes_answer_text,
    )
    check(
        "the Hayes fault-loop expansion adds no duplicate organizer to Teacher pages",
        not hayes_content.select_one('section[data-role="teacher"] .cycle-model'),
    )
    check(
        "the browser harness measures the closed loop, exact fields and strict fit in both modes",
        harness.count("fault cycle renders a direct closed repeat loop") == 1
        and harness.count("fault-loop pages retain strict integer fit in normal and grayscale") == 1
        and "REPEAT TO STAGE 1" in harness
        and "EXPOSURE|LOAD|DAMAGE|DECLINE|REBUILD|RECURRENCE" in harness
        and "t5-2|t5-3|t5-4|t5-5|t5-6" in harness
        and "a5-2|a5-3|a5-4|a5-5|a5-6" in harness
        and 'for (const grayscale of [false, true])' in harness,
    )

    failures = [(name, detail) for name, passed, detail in checks if not passed]
    print("SSS visual modernization · mechanism family")
    print(f"Result: {len(checks) - len(failures)}/{len(checks)} PASS")
    for name, detail in failures:
        print(f"FAIL: {name}\n  {detail}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
