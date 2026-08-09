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
    PACKAGE: "b1477d499fcb1bfb026f606bc0c5c8d9833f967950daba45dff2c9cdd0a9a200",
    REGISTRY: "402161f3aed5b834cc6228321329655086f5d42bca362605fefe54fa1a0820fc",
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

    css_start = css.index("Evidence-convergence family pilot: Europa four-route diagnosis.")
    css_end = css.index("Mechanism/pathway family expansion: First Contact coordination system.", css_start)
    evidence_css = css[css_start:css_end]
    case05_start = harness.index('if (item.id === "SSS-C1-CASE05")')
    case05_end = harness.index('if (item.id === "SSS-C1-CASE06")', case05_start)
    case05_harness = harness[case05_start:case05_end]

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

    check(
        "the production plan assigns C1C5-VIS02 to Family 4 as an implemented candidate",
        bool(re.search(r"\| `C1C5-VIS02` .*\| 4 · Evidence-convergence map \|.*`IMPLEMENTED-CANDIDATE · 30/30 FAMILY STATIC PASS · 2342/2342 MAC/CHROME GATE REQUIRED`", plan)),
    )
    check(
        "the desktop handoff records the rendered gate without advancing accepted inventory",
        "Implemented Family 4 candidate — Europa four-route evidence convergence" in handoff
        and "2342/2342" in handoff
        and "2311/2342" in handoff
        and "23 of 36" in handoff
        and "13 remaining" in handoff,
    )
    check(
        "Family 4 has no premature accepted-register or verified-family entry",
        "| `C1C5-VIS02` |" not in handoff
        and not bool(re.search(r"\| `C1C5-VIS02` .*`VERIFIED-FAMILY", plan))
        and "`C1C7-VIS01` before separate acceptance and closeout" in handoff,
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

    if len(checks) != 30:
        raise AssertionError(f"validator definition drift: expected 30 checks, found {len(checks)}")

    failures = [item for item in checks if not item[1]]
    for index, (name, passed, detail) in enumerate(checks, 1):
        print(f"[{index:02d}] {'PASS' if passed else 'FAIL'} · {name}")
        if not passed and detail:
            print(f"     {detail}")
    print(f"\nEvidence-convergence family: {len(checks) - len(failures)}/{len(checks)} PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
