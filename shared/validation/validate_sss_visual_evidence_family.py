#!/usr/bin/env python3
"""Focused deterministic checks for the SSS evidence-convergence visual family."""

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
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
SOURCE = ROOT / "sss/campaign-1/case-05-europa-bunker/source"
CONTENT = SOURCE / "content.html"
PRESENTATION = SOURCE / "presentation.css"
LAYOUT = SOURCE / "layout-overrides.json"
PACKAGE = SOURCE / "case-package.json"
REGISTRY = SOURCE / "task-registry.js"

SOURCE_HASHES = {
    CONTENT: "8b85088d048afb6e291e316995f2a159e7efea523d00fa2c040e86766b96601d",
    PRESENTATION: "5e4fb3d822dd337d593cc758436298a1103fa25d77638c07bebc723cacbe2aa8",
    LAYOUT: "6667dec008f983f057c1bc56eec0ba5b1fd59b918c66b57f9872c418cd2578d2",
    PACKAGE: "2f2a6faecaad0cbeabce76274ea63ca1aaa110e9c95f1761033912688b7c5f59",
    REGISTRY: "b1b8f858ebbdee5d5232bc9024e17c44c6fd43aef5b5d498eeb2d6b67e01f7a3",
}

SOURCES = ["Crew", "Sensors", "Plants", "Logs"]
STUDENT_EVIDENCE = [
    "Different plantings follow the same sequence: germination, early growth, spots and growing-tip failure, then death.",
    "The grow-chamber monitor flags elevated ionizing radiation. Crop biological assessment remains incomplete.",
    "Meristem cells are disorganized; some divisions are uneven and some nuclei fragmented. The abnormalities are consistent with DNA damage.",
    "Shielding reduces primary energetic particles. Material interactions may produce modeled secondary radiation. Crop protection was not verified.",
]
ACCESSIBLE_EVIDENCE = [
    "Different plantings fail in the same sequence after early growth.",
    "The monitor flags elevated ionizing radiation. Crop assessment is incomplete.",
    "Meristem abnormalities are consistent with DNA damage.",
    "Crop protection was not verified. Modeled secondary radiation may contribute.",
]
ANSWER_CONTRIBUTIONS = [
    "Repeated failure across plantings supports a persistent environmental cause rather than one seed batch.",
    "Establishes elevated grow-chamber ionizing-radiation exposure, not biological harm by itself.",
    "Provides biological evidence: meristem abnormalities are consistent with DNA damage, without proving the cause or exact molecular mechanism.",
    "Shows crop protection was unverified and modeled secondary radiation may contribute through material interactions.",
]

GIFT_SOURCE = ROOT / "sss/campaign-1/case-07-the-gift/source"
GIFT_CONTENT = GIFT_SOURCE / "content.html"
GIFT_PRESENTATION = GIFT_SOURCE / "presentation.css"
GIFT_LAYOUT = GIFT_SOURCE / "layout-overrides.json"
GIFT_PACKAGE = GIFT_SOURCE / "case-package.json"
GIFT_REGISTRY = GIFT_SOURCE / "task-registry.js"

GIFT_SOURCE_HASHES = {
    GIFT_CONTENT: "45d6c471eab166b5761b8c7de43d0352597eb9c4dafa15cb8951ec56783b6a11",
    GIFT_PRESENTATION: "259b76e2d7752680d58e01092e2bc3528956e13be7b79c3b453611b6c2d258a4",
    GIFT_LAYOUT: "0b3fc73e9baddf29e982f01841a66c41f2ae2a96f44d6fe72aadd5e83ebae6ea",
    GIFT_PACKAGE: "fab83e4960d3913e43e0c344bba80cd1a4cfaa2b8d26f39fc37e40d05c300baa",
    GIFT_REGISTRY: "24a1ab7e3b15bb986a3a0276361cb7ad67d2270e733adbd7a300674825cfa0a5",
}

GIFT_CHANNELS = ["Liaison", "Biomonitors", "Specimen", "Archives"]
GIFT_STATUSES = ["SOURCE / RANGE", "MATCH / TRACE GAP", "VIABLE / RESPONSIVE", "MECHANISM RECORD"]
GIFT_STUDENT_EVIDENCE = [
    "Path A: Ask why established growth must be near. Path B: Ask whether a pod has germinated away from mature growth. Historic success occurred within 1–3 m along shared airflow. The cue is below threshold past 3 m.",
    "Path A: Scan atmospheric analysis. Path B: Compare with the living cultivation area. Primary targets match. The lab detects 12 residual trace identifiers versus 847+ near living growth, and the sets do not match.",
    "Path A: Look for receptor structures. Path B: Examine chambers, then ask what signal they await. The intact, primed pod has dense outward receptors and selective responses to controlled stimuli.",
    "Path A: Search germination biology. Path B: Search signal chemistry. Fictional records identify a short-lived cue from healthy mature networks, transported in fictional carrier droplets and detected by pod receptors.",
]
GIFT_ACCESSIBLE_EVIDENCE = [
    "Paths: ask why mature growth must be near; ask about isolated germination. Historic success: within 1–3 m on shared airflow. Cue below threshold past 3 m.",
    "Paths: atmospheric scan; living-area comparison. Primary targets match. Lab: 12 trace identifiers. Living area: 847+. The sets differ.",
    "Paths: inspect receptors; inspect chambers and ask what signal they await. The intact, primed pod has dense receptors and selective responses.",
    "Paths: germination biology; signal chemistry. Fictional records name a short-lived cue from a healthy mature network.",
]
GIFT_ANSWER_CELLS = [
    "Historic success within 1–3 m and shared airflow supports mature growth as source context and constrains delivery distance.",
    "Proximity alone does not prove the cue's identity, nutrient transfer, intention, or receptor mechanism.",
    "Primary targets match, but the lab has 12 residual trace identifiers compared with 847+ near living growth, and the sets differ.",
    "A broad trace gap does not show that every absence matters or identify the active cue.",
    "Integrity, primed chambers, dense receptors, and selective responses support a viable cue-gated dormant state.",
    "Response does not identify ligand structure, natural source, safe dose, or transport.",
    "Fictional records name a short-lived mature-network cue in carrier droplets and a receptor-mediated commitment pathway.",
    "An archive does not prove an Earth analogy or that any proposed intervention is safe.",
]
GIFT_TRACE_EXEMPLAR = (
    "The isolated lab detects 12 trace identifiers while the living area has 847 or more, and the two sets do not match. "
    "This establishes that their trace-chemical contexts differ substantially. It does not show which identifiers are shared, "
    "which differences matter, or which compound triggers germination; receptor, archive, and proximity evidence are also required."
)
GIFT_CONVERGENCE = (
    "The channels form a chain: matched primary targets shift attention away from known physical conditions; specimen data support "
    "dormancy rather than death; the trace mismatch supplies a missing-variable category; receptor data support a selective trigger; "
    "and archive plus proximity identify the mature network as the natural source. No single channel supplies the full diagnosis."
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text(node) -> str:
    return " ".join(node.stripped_strings) if node else ""


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    plan = PLAN.read_text(encoding="utf-8")
    handoff = HANDOFF.read_text(encoding="utf-8")
    css = COMPONENTS.read_text(encoding="utf-8")
    harness = HARNESS.read_text(encoding="utf-8")
    soup = BeautifulSoup(CONTENT.read_text(encoding="utf-8"), "html.parser")
    package = json.loads(PACKAGE.read_text(encoding="utf-8"))
    layout = json.loads(LAYOUT.read_text(encoding="utf-8"))
    registry_text = REGISTRY.read_text(encoding="utf-8")
    registry = json.loads(re.sub(r"^\s*window\.SSS_CASE05_TASK_REGISTRY\s*=\s*", "", registry_text).rstrip(";\n "))

    gift_soup = BeautifulSoup(GIFT_CONTENT.read_text(encoding="utf-8"), "html.parser")
    gift_package = json.loads(GIFT_PACKAGE.read_text(encoding="utf-8"))
    gift_layout = json.loads(GIFT_LAYOUT.read_text(encoding="utf-8"))
    gift_registry_text = GIFT_REGISTRY.read_text(encoding="utf-8")
    gift_registry = json.loads(re.sub(r"^\s*window\.SSS_CASE07_TASK_REGISTRY\s*=\s*", "", gift_registry_text).rstrip(";\n "))

    css_start = css.index("Evidence-convergence family pilot: Europa four-route diagnosis.")
    css_end = css.index("Mechanism/pathway family expansion: First Contact coordination system.", css_start)
    evidence_css = css[css_start:css_end]
    case05_start = harness.index('if (item.id === "SSS-C1-CASE05")')
    case05_end = harness.index('if (item.id === "SSS-C1-CASE06")', case05_start)
    case05_harness = harness[case05_start:case05_end]
    gift_css_start = css.index("Evidence-convergence family completion: The Gift diagnostic question.")
    gift_css_end = css.index("Mechanism/pathway family expansion: The Missing Dance failure path.", gift_css_start)
    gift_css = css[gift_css_start:gift_css_end]
    case07_start = harness.index('if (item.id === "SSS-C1-CASE07")')
    case07_end = harness.index('const approvedMatrixStates', case07_start)
    case07_harness = harness[case07_start:case07_end]

    student_page = soup.select_one('[data-page-id="student-mission-02"][data-role="student"]')
    accessible_page = soup.select_one('[data-page-id="accessible-mission-03"][data-role="accessible"]')
    answer_page = soup.select_one('[data-page-id="answer-key-02"][data-role="answer"]')
    student_root = student_page.select_one('[data-evidence-summary="qualitative-four-route-v1.0"]')
    accessible_root = accessible_page.select_one('[data-evidence-summary="qualitative-four-route-v1.0"]')
    answer_heading = answer_page.select_one('[data-shell-task-heading="3"]')
    answer_root = answer_heading.find_next_sibling("table")

    student_rows = student_root.select(":scope > tbody > tr")
    accessible_cards = accessible_root.select(":scope > section")
    answer_rows = answer_root.select(":scope > tbody > tr")

    gift_student_page = gift_soup.select_one('[data-page-id="student-mission-02"][data-role="student"]')
    gift_accessible_page = gift_soup.select_one('[data-page-id="accessible-mission-02"][data-role="accessible"]')
    gift_answer_page = gift_soup.select_one('[data-page-id="answer-key-02"][data-role="answer"]')
    gift_student_root = gift_student_page.select_one('[data-evidence-summary="case07-four-channel-v1.0"]')
    gift_accessible_root = gift_accessible_page.select_one('[data-evidence-summary="case07-accessible-four-channel-v1.0"]')
    gift_answer_root = gift_answer_page.select_one('[data-evidence-summary="case07-answer-four-channel-v1.0"]')
    gift_student_rows = gift_student_root.select(":scope > tbody > tr")
    gift_accessible_cards = gift_accessible_root.select(":scope > section")
    gift_answer_rows = gift_answer_root.select(":scope > tbody > tr")

    check(
        "the production plan accepts C1C5-VIS02 as the first Family 4 finding",
        bool(re.search(
            r"\| `C1C5-VIS02` .*\| 4 · Evidence-convergence map \|.*"
            r"`VERIFIED-FAMILY · 30/30 FAMILY STATIC PASS · 2342/2342 BROWSER PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 70375da ACCEPTED`",
            plan,
        )),
    )
    check(
        "the desktop handoff records the accepted Mac/Chrome and manual gate",
        "Accepted Family 4 pilot — Europa four-route evidence convergence" in handoff
        and "70375daa5bebe7dea127c0b8f6f6e0aeece48fc9" in handoff
        and "2342/2342 PASS with 0 application JavaScript errors" in handoff
        and "30/30 PASS" in handoff
        and "24 of 36 completed" in handoff
        and "12 remaining" in handoff,
    )
    check(
        "Family 4 register accepts both evidence-convergence findings",
        "| `C1C5-VIS02` | `70375da` | `VERIFIED-FAMILY` |" in handoff
        and "| `C1C7-VIS01` | `39325dc` | `VERIFIED-FAMILY` |" in handoff
        and "Family 4 is complete with both findings verified" in handoff
        and bool(re.search(
            r"\| `C1C7-VIS01` .*"
            r"`VERIFIED-FAMILY · 60/60 FAMILY STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 39325dc ACCEPTED`",
            plan,
        ))
        and bool(re.search(r"Do not\s+begin another finding in the same\s+run\.", handoff)),
    )
    check(
        "the evidence presentation block is isolated to Europa Case 05",
        'data-case-id="SSS-C1-CASE05"' in evidence_css
        and "SSS-C1-CASE0" not in evidence_css.replace("SSS-C1-CASE05", "")
        and "SSS-C2-CASE" not in evidence_css,
    )
    check(
        "the shared EC1 block targets Student, Accessible and generated Answer Key roots",
        'evidence-table[data-evidence-summary="qualitative-four-route-v1.0"]' in evidence_css
        and 'accessible-evidence[data-evidence-summary="qualitative-four-route-v1.0"]' in evidence_css
        and '.page[data-page-id="answer-key-02"] .task-heading[data-task-id="3"] + .data-table' in evidence_css,
    )
    check(
        "the qualified convergence node is exact and non-proving",
        evidence_css.count('content: "QUALIFIED CONVERGENCE · RADIATION BEST-SUPPORTED · NO SINGLE CLUE PROVES CAUSE";') == 1,
    )
    check(
        "the four direct channel states are exact",
        all(evidence_css.count(f'content: "{status}";') == 1 for status in (
            "REPEATED PATTERN", "EXPOSURE", "BIO EVIDENCE", "PROTECTION LIMIT"
        )),
    )
    check(
        "solid double dashed and dotted channel borders remain explicit",
        all(f"border-left-style: {style};" in evidence_css for style in ("solid", "double", "dashed", "dotted"))
        and "repeating-linear-gradient" in evidence_css,
    )
    check(
        "the Student footprint keeps a semantic header and full-height response boxes",
        '> thead {' in evidence_css
        and "clip: rect(0, 0, 0, 0);" in evidence_css
        and "grid-template-areas: \"source source\" \"evidence contribution\";" in evidence_css
        and ".table-response" not in evidence_css,
    )
    check(
        "the evidence map has an explicit grayscale surface contract",
        '.worksheet-document.grayscale[data-case-id="SSS-C1-CASE05"]' in evidence_css
        and "background-color: var(--paper, #fff);" in evidence_css,
    )
    check(
        "the new browser checks live inside the C1 Case 05 block",
        "europaConvergencePageFit" in case05_harness
        and "expectedConvergenceSources" in case05_harness
        and "expectedAnswerContributions" in case05_harness,
    )
    check(
        "the browser fit gate covers all six target states and exact page counts",
        '[["student", "student-mission-02", 4], ["answer", "answer-key-02", 4], ["accessible", "accessible-mission-03", 7]]' in case05_harness
        and "state.pageSize === \"816x1056\"" in case05_harness
        and "content.scrollHeight <= content.clientHeight" in case05_harness,
    )
    check(
        "the browser semantic gate checks channels statuses borders patterns and synthesis",
        "expectedConvergenceSources" in case05_harness
        and "expectedConvergenceStatuses" in case05_harness
        and "expectedConvergenceBorders" in case05_harness
        and "expectedConvergenceNode" in case05_harness
        and "state.contained && !state.cardCollision" in case05_harness,
    )
    check(
        "the browser semantic gate protects every learner field and Answer Key exemplar",
        "t3-crew|t3-sensors|t3-plants|t3-logs" in case05_harness
        and "a3-crew|a3-sensors|a3-plants|a3-logs" in case05_harness
        and all(value in case05_harness for value in ANSWER_CONTRIBUTIONS),
    )
    check(
        "all five package-controlled Case 05 sources retain their accepted hashes",
        all(sha256(path) == expected for path, expected in SOURCE_HASHES.items()),
        {path.name: sha256(path) for path in SOURCE_HASHES},
    )
    check(
        "the package preserves edition counts and shared visual delivery",
        package.get("supportedRoles") == ["student", "teacher", "answer", "accessible"]
        and {role: value.get("pageCount") for role, value in package.get("rolePageStructure", {}).items()}
        == {"student": 4, "teacher": 8, "answer": 4, "accessible": 7}
        and package.get("presentation", {}).get("sharedVisualStyles") is True,
        package.get("rolePageStructure"),
    )
    check(
        "the frozen content retains exact page counts",
        {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ("student", "teacher", "answer", "accessible")}
        == {"student": 4, "teacher": 8, "answer": 4, "accessible": 7},
    )
    check(
        "Student Task 3 retains one semantic four-row evidence table",
        student_root.name == "table"
        and student_root.get("data-evidence-summary") == "qualitative-four-route-v1.0"
        and len(student_rows) == 4,
    )
    check(
        "Student source labels remain exact and ordered",
        [text(row.find("th", scope="row")) for row in student_rows] == SOURCES,
    )
    check(
        "Student verified evidence remains verbatim",
        [text(row.find_all("td", recursive=False)[0]) for row in student_rows] == STUDENT_EVIDENCE,
    )
    check(
        "Student retains four genuinely blank contribution responses",
        [row.select_one("[data-response]").get("data-persist-id") for row in student_rows]
        == ["t3-crew", "t3-sensors", "t3-plants", "t3-logs"]
        and all(not text(row.select_one("[data-response]")) for row in student_rows),
    )
    check(
        "Accessible Task 3 retains one four-card evidence structure",
        accessible_root.name == "div"
        and accessible_root.get("data-evidence-summary") == "qualitative-four-route-v1.0"
        and len(accessible_cards) == 4,
    )
    check(
        "Accessible source labels and evidence remain exact and ordered",
        [text(card.find("h3")) for card in accessible_cards] == SOURCES
        and [text(card.find("p")) for card in accessible_cards] == ACCESSIBLE_EVIDENCE,
    )
    check(
        "Accessible retains four genuinely blank contribution responses",
        [card.select_one("[data-response]").get("data-persist-id") for card in accessible_cards]
        == ["a3-crew", "a3-sensors", "a3-plants", "a3-logs"]
        and all(not text(card.select_one("[data-response]")) for card in accessible_cards),
    )
    check(
        "Answer Key Task 3 retains one semantic four-row completion table",
        answer_root.name == "table" and len(answer_rows) == 4 and text(answer_root.find("caption")) == "Completed four-route convergence",
    )
    check(
        "Answer Key source labels remain exact and ordered",
        [text(row.find("th", scope="row")) for row in answer_rows] == SOURCES,
    )
    check(
        "Answer Key contribution exemplars remain verbatim",
        [text(row.find("td")) for row in answer_rows] == ANSWER_CONTRIBUTIONS,
    )
    check(
        "the frozen source keeps exposure biological-evidence and single-clue boundaries separate",
        "Exposure is not identical to biological damage." in text(soup)
        and "Scattered brown spots do not by themselves identify the cause" in text(student_page)
        and "Radiation is the best-supported diagnosis, not a diagnosis proved by any single clue." in text(answer_page),
    )
    check(
        "the task registry preserves the formal source set and prohibited causal overclaims",
        registry.get("formalClues") == ["CONSISTENT_FAILURE", "HIGH_RADIATION", "DNA_DAMAGE_PATTERN", "SHIELDING_INSUFFICIENT"]
        and "the evidence proves an exact molecular mechanism" in registry.get("prohibitedClaims", [])
        and "modeled secondary radiation is a measured percentage" in registry.get("prohibitedClaims", []),
    )
    check(
        "the layout contract retains all eight Task 3 learner response identities",
        {area.get("persistId") for area in layout.get("areas", []) if area.get("taskId") == 3}
        == {"a3-crew", "a3-sensors", "a3-plants", "a3-logs"}
        and {area.get("persistId") for area in layout.get("student", {}).get("lockedAreas", []) if str(area.get("persistId", "")).startswith("t3-")}
        == {"t3-crew", "t3-sensors", "t3-plants", "t3-logs"},
    )

    check(
        "the production plan accepts C1C7-VIS01 as the second Family 4 finding",
        bool(re.search(
            r"\| `C1C7-VIS01` .*\| 4 · Evidence-convergence/diagnostic map \|.*"
            r"`VERIFIED-FAMILY · 60/60 FAMILY STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 39325dc ACCEPTED`",
            plan,
        )),
    )
    check(
        "the desktop handoff records the accepted Gift differential browser gate",
        "Accepted Family 4 completion — The Gift diagnostic question" in handoff
        and "39325dcd1639c40e17aac435c599e17ecaffc3df" in handoff
        and "2341/2341 PASS" in handoff
        and handoff.count("2344/2344 PASS") >= 2
        and "candidate delta is exactly +3" in handoff
        and "2314/2345" in handoff
        and "60/60 PASS" in handoff
        and "25 of 36 completed" in handoff
        and "11 remaining" in handoff,
    )
    check(
        "Family 4 register accepts Europa and the Gift and records completion",
        "| `C1C5-VIS02` | `70375da` | `VERIFIED-FAMILY` |" in handoff
        and "| `C1C7-VIS01` | `39325dc` | `VERIFIED-FAMILY` |" in handoff
        and "Family 4 is complete with both findings verified" in handoff
        and "Do not mark any additional finding accepted" in handoff,
    )
    check(
        "the Gift evidence presentation block is isolated to Case 07",
        'data-case-id="SSS-C1-CASE07"' in gift_css
        and "SSS-C1-CASE0" not in gift_css.replace("SSS-C1-CASE07", "")
        and "SSS-C2-CASE" not in gift_css,
    )
    check(
        "the Gift EC1 block targets all three frozen Task 2 roots",
        'case07-four-channel-v1.0' in gift_css
        and 'case07-accessible-four-channel-v1.0' in gift_css
        and 'case07-answer-four-channel-v1.0' in gift_css,
    )
    check(
        "the primary-match and incomplete-trace diagnostic is exact",
        gift_css.count('content: "PRIMARY TARGETS MATCH · TRACE CONTEXT INCOMPLETE";') == 1,
    )
    check(
        "the final node remains an exact qualified question with both prohibited inferences",
        gift_css.count(
            'content: "QUALIFIED QUESTION · WHICH MISSING CONTEXT MATTERS? · 99.7% ≠ COMPLETE · SETS DIFFER / NO RATIO";'
        ) == 1,
    )
    check(
        "the four direct Gift channel states are exact",
        all(gift_css.count(f'content: "{status}";') == 1 for status in GIFT_STATUSES),
    )
    check(
        "the Gift channels preserve four borders and independent patterns",
        all(f"border-left-style: {style};" in gift_css for style in ("solid", "double", "dashed", "dotted"))
        and gift_css.count("repeating-linear-gradient") >= 6,
    )
    check(
        "the Gift diagnostic gate uses explicit converging connectors and sibling roots",
        'content: "↘  ↓  ↓  ↙ · DIAGNOSTIC GATE";' in gift_css
        and '+ .two-col' in gift_css
        and '+ .callout' in gift_css
        and '+ .answer-block' in gift_css,
    )
    check(
        "the Gift evidence map has an explicit grayscale contract",
        '.worksheet-document.grayscale[data-case-id="SSS-C1-CASE07"]' in gift_css
        and "background-color: var(--paper, #fff);" in gift_css,
    )
    check(
        "the new browser checks live inside the C1 Case 07 block",
        "giftConvergencePageFit" in case07_harness
        and "expectedGiftSources" in case07_harness
        and "expectedGiftAnswerCells" in case07_harness,
    )
    check(
        "the Gift browser fit gate covers six states and exact page counts",
        '[["student", "student-mission-02", 6], ["answer", "answer-key-02", 6], ["accessible", "accessible-mission-02", 8]]' in case07_harness
        and "state.pageSize === \"816x1056\"" in case07_harness
        and "content.scrollHeight <= content.clientHeight" in case07_harness,
    )
    check(
        "the Gift browser semantic gate checks channels states borders patterns and question",
        "expectedGiftSources" in case07_harness
        and "expectedGiftStatuses" in case07_harness
        and "expectedGiftBorders" in case07_harness
        and "expectedGiftDiagnostic" in case07_harness
        and "expectedGiftQuestion" in case07_harness
        and "state.contained && !state.cardCollision && state.gateContained" in case07_harness,
    )
    check(
        "the Gift browser gate protects ten learner fields and all Answer Key cells",
        "t2-liaison|t2-biomonitors|t2-specimen|t2-archives|t2-comparison" in case07_harness
        and "a2-liaison|a2-biomonitors|a2-specimen|a2-archives|a2-comparison" in case07_harness
        and all(value in case07_harness for value in GIFT_ANSWER_CELLS),
    )
    check(
        "all five package-controlled Case 07 sources retain accepted hashes",
        all(sha256(path) == expected for path, expected in GIFT_SOURCE_HASHES.items()),
        {path.name: sha256(path) for path in GIFT_SOURCE_HASHES},
    )
    check(
        "the Gift package preserves role counts and shared visual delivery",
        gift_package.get("supportedRoles") == ["student", "teacher", "answer", "accessible"]
        and {role: value.get("pageCount") for role, value in gift_package.get("rolePageStructure", {}).items()}
        == {"student": 6, "teacher": 8, "answer": 6, "accessible": 8}
        and gift_package.get("presentation", {}).get("sharedVisualStyles") is True,
        gift_package.get("rolePageStructure"),
    )
    check(
        "the frozen Gift content retains exact page counts",
        {role: len(gift_soup.select(f'.page[data-role="{role}"]')) for role in ("student", "teacher", "answer", "accessible")}
        == {"student": 6, "teacher": 8, "answer": 6, "accessible": 8},
    )
    check(
        "Student Task 2 retains one semantic four-row evidence table",
        gift_student_root.name == "table"
        and gift_student_root.get("data-evidence-summary") == "case07-four-channel-v1.0"
        and len(gift_student_rows) == 4,
    )
    check(
        "Student Gift channel labels remain exact and ordered",
        [text(row.find("th", scope="row")) for row in gift_student_rows] == GIFT_CHANNELS,
    )
    check(
        "Student Gift evidence and reveal paths remain verbatim",
        [text(row.find_all("td", recursive=False)[0]) for row in gift_student_rows] == GIFT_STUDENT_EVIDENCE,
    )
    check(
        "Student retains five genuinely blank Task 2 responses",
        [row.select_one("[data-response]").get("data-persist-id") for row in gift_student_rows]
        == ["t2-liaison", "t2-biomonitors", "t2-specimen", "t2-archives"]
        and not text(gift_student_page.select_one('[data-persist-id="t2-comparison"]'))
        and all(not text(row.select_one("[data-response]")) for row in gift_student_rows),
    )
    check(
        "Accessible Task 2 retains one four-card evidence structure",
        gift_accessible_root.name == "div"
        and gift_accessible_root.get("data-evidence-summary") == "case07-accessible-four-channel-v1.0"
        and len(gift_accessible_cards) == 4,
    )
    check(
        "Accessible Gift labels and evidence remain exact and ordered",
        [text(card.find("h3")) for card in gift_accessible_cards] == GIFT_CHANNELS
        and [" ".join(text(node) for node in card.find_all("p")) for card in gift_accessible_cards]
        == GIFT_ACCESSIBLE_EVIDENCE,
    )
    check(
        "Accessible retains five genuinely blank Task 2 responses",
        [card.select_one("[data-response]").get("data-persist-id") for card in gift_accessible_cards]
        == ["a2-liaison", "a2-biomonitors", "a2-specimen", "a2-archives"]
        and not text(gift_accessible_page.select_one('[data-persist-id="a2-comparison"]'))
        and all(not text(card.select_one("[data-response]")) for card in gift_accessible_cards),
    )
    check(
        "Answer Key Task 2 retains one semantic four-row completion table",
        gift_answer_root.name == "table"
        and len(gift_answer_rows) == 4
        and text(gift_answer_root.find("caption")) == "Completed four-channel analysis",
    )
    check(
        "Answer Key Gift channels and eight contribution-limit cells remain verbatim",
        [text(row.find("th", scope="row")) for row in gift_answer_rows] == GIFT_CHANNELS
        and [text(cell) for row in gift_answer_rows for cell in row.find_all("td", recursive=False)] == GIFT_ANSWER_CELLS,
    )
    check(
        "Answer Key trace and convergence exemplars remain verbatim",
        text(gift_answer_root.find_next_sibling("div").find("p")) == GIFT_TRACE_EXEMPLAR
        and text(gift_answer_root.find_next_sibling("h2").find_next_sibling("p")) == GIFT_CONVERGENCE,
    )
    check(
        "the Gift registry preserves the primary-summary and non-ratio boundaries",
        gift_registry.get("conditionLedger", {}).get("similarityIndex")
        == "99.7% composite of primary measured targets; weighting formula not supplied; trace compounds excluded"
        and gift_registry.get("conditionLedger", {}).get("traceIdentifiers")
        == {"lab": 12, "livingAreaMinimum": 847, "setsMatch": False, "ratioIsCoverage": False}
        and "matching measured targets recreates an ecosystem" in gift_registry.get("prohibitedClaims", []),
    )
    check(
        "the Gift layout contract retains all ten Task 2 learner identities",
        {area.get("persistId") for area in gift_layout.get("areas", []) if area.get("taskId") == 2}
        == {"a2-liaison", "a2-biomonitors", "a2-specimen", "a2-archives", "a2-comparison"}
        and {area.get("persistId") for area in gift_layout.get("student", {}).get("areas", []) if area.get("taskId") == 2}
        == {"t2-comparison"}
        and {area.get("persistId") for area in gift_layout.get("student", {}).get("lockedAreas", []) if str(area.get("persistId", "")).startswith("t2-")}
        == {"t2-liaison", "t2-biomonitors", "t2-specimen", "t2-archives"},
    )

    if len(checks) != 60:
        raise AssertionError(f"validator definition drift: expected 60 checks, found {len(checks)}")

    failures = [item for item in checks if not item[1]]
    for index, (name, passed, detail) in enumerate(checks, 1):
        print(f"[{index:02d}] {'PASS' if passed else 'FAIL'} · {name}")
        if not passed and detail:
            print(f"     {detail}")
    print(f"\nEvidence-convergence family: {len(checks) - len(failures)}/{len(checks)} PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
