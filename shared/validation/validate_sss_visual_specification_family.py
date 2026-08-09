#!/usr/bin/env python3
"""Focused deterministic checks for the SSS specification/verification family."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "sss/campaign-1/case-05-europa-bunker/source"
CONTENT = CASE / "content.html"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
HANDOFF = ROOT / "sss/audit/final/SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md"

FROZEN_HASHES = {
    "content.html": "8b85088d048afb6e291e316995f2a159e7efea523d00fa2c040e86766b96601d",
    "presentation.css": "5e4fb3d822dd337d593cc758436298a1103fa25d77638c07bebc723cacbe2aa8",
    "layout-overrides.json": "6667dec008f983f057c1bc56eec0ba5b1fd59b918c66b57f9872c418cd2578d2",
    "case-package.json": "b1477d499fcb1bfb026f606bc0c5c8d9833f967950daba45dff2c9cdd0a9a200",
    "task-registry.js": "402161f3aed5b834cc6228321329655086f5d42bca362605fefe54fa1a0820fc",
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

    student = soup.select_one('section[data-role="student"][data-page-id="student-mission-04"]')
    answer = soup.select_one('section[data-role="answer"][data-page-id="answer-key-04"]')
    accessible = soup.select_one('section[data-role="accessible"][data-page-id="accessible-mission-07"]')
    check("Europa retains the three frozen final-page targets", all((student, answer, accessible)))

    student_t7 = ["t7-need", "t7-criteria", "t7-constraints", "t7-verify"]
    accessible_t7 = ["a7-need", "a7-criteria", "a7-constraints", "a7-verify"]
    student_t8 = ["t8-immediate", "t8-durable", "t8-justify"]
    accessible_t8 = ["a8-immediate", "a8-durable", "a8-test"]
    check(
        "Student Task 7 retains Need Criteria Constraints and Verification identities",
        [node.get("data-persist-id") for node in student.select(".task7-design-grid [data-response]")] == student_t7,
    )
    check(
        "Accessible Task 7 retains the parallel four requirement identities",
        [node.get("data-persist-id") for node in accessible.select(".accessible-task7-design [data-response]")] == accessible_t7,
    )
    check(
        "Student Task 8 retains immediate durable and verification identities",
        [node.get("data-persist-id") for node in student.select(".task8-response-block [data-response]")] == student_t8,
    )
    check(
        "Accessible Task 8 retains immediate durable and test identities",
        [node.get("data-persist-id") for node in accessible.select(".accessible-task8-block [data-response]")] == accessible_t8,
    )
    learner_fields = [soup.select_one(f'[data-persist-id="{persist_id}"]') for persist_id in student_t7 + accessible_t7 + student_t8 + accessible_t8]
    check(
        "all fourteen learner fields remain blank writable responses",
        all(field and field.has_attr("data-response") and not normalized(field) for field in learner_fields),
    )
    check(
        "Task 7 and Task 8 retain separate headings on each final page",
        all(
            [heading.get("data-shell-task-heading") for heading in page.select("h2[data-shell-task-heading]")] == ["7", "8"]
            for page in (student, answer, accessible)
        ),
    )
    check(
        "Europa page counts remain frozen across all four roles",
        {role: len(soup.select(f'section[data-role="{role}"]')) for role in ("student", "answer", "teacher", "accessible")}
        == {"student": 4, "answer": 4, "teacher": 8, "accessible": 7},
    )

    expected_task7 = [
        "Need: Define a crop-protection system that permits long-duration cultivation while producing evidence that crop exposure and biological response are adequately controlled.",
        "Criteria: Reduce grow-chamber ionizing-radiation exposure; support normal meristem development and repeated crop growth; provide monitoring that can verify crop performance.",
        "Constraints: Europa’s trapped energetic-particle environment; possible secondary radiation from material interactions; limited habitat mass, volume, power, and placement; separate crew and crop assessments; crop-specific protection criteria are not yet verified.",
        "Verification: Compare monitor trends, plant microscopy, growth-stage outcomes, and repeated crop trials under the revised system. Do not substitute a crew criterion or invent a crop threshold.",
    ]
    answer_t7 = answer.select_one('[data-shell-task-heading="7"] + .answer-block')
    check(
        "Answer Key preserves the exact four-part requirements exemplar",
        [normalized(node) for node in answer_t7.select(":scope > p")] == expected_task7,
    )
    expected_task8 = [
        "Immediate operational response: Pause or limit long-duration planting, preserve monitoring data and plant samples, and move cultivation to the best-protected available location if operations can do so without claiming safety is verified.",
        "Durable engineering response: Redesign or supplement grow-chamber protection, placement, and monitoring, then conduct a crop-specific validation program that considers both primary and modeled secondary radiation.",
        "Justification and verification: The response follows from converging exposure, plant, repeated-failure, and construction-log evidence. Success requires improved monitor evidence together with normal meristem development and sustained crop growth across repeated trials.",
    ]
    answer_t8 = answer.select_one('[data-shell-task-heading="8"] + .answer-block')
    check(
        "Answer Key preserves the exact three-part response and verification exemplar",
        [normalized(node) for node in answer_t8.select(":scope > p")] == expected_task8,
    )
    check(
        "Accessible keeps the numerical-safe-level and no-in-game-fix boundary",
        "Do not invent a numerical safe level. The game provides a diagnosis, not an in-game “apply the fix” step." in normalized(accessible),
    )
    check(
        "Answer Key keeps acceptable variation conditional on criteria constraints and verification",
        "meet the stated criteria, respect the constraints, and include a verification plan" in normalized(answer)
        and "does not establish that one proposed design is already successful" in normalized(answer),
    )
    check(
        "the crop assessment remains separate from crew criteria",
        "separate crew and crop assessments" in normalized(answer)
        and "Do not substitute a crew criterion or invent a crop threshold" in normalized(answer),
    )
    check(
        "secondary radiation and location safety remain qualified",
        "modeled secondary radiation" in normalized(answer)
        and "without claiming safety is verified" in normalized(answer),
    )
    final_text = " ".join((normalized(student), normalized(answer), normalized(accessible)))
    check(
        "final pages invent no shielding percentage or numerical crop threshold",
        not re.search(r"\b\d+(?:\.\d+)?\s*(?:%|mGy|Gy|Sv|sievert)\b|crop[- ]safe\s+(?:level|threshold)\s*[:=]\s*\d", final_text, flags=re.IGNORECASE),
    )

    for filename, expected_hash in FROZEN_HASHES.items():
        check(
            f"frozen Europa {filename} SHA-256 remains exact",
            sha256(CASE / filename) == expected_hash,
            sha256(CASE / filename),
        )

    css_start = css.index("Specification/verification family expansion: Europa crop protection.")
    css_end = css.index("Mechanism/pathway family expansion: First Contact coordination system.", css_start)
    spec_css = css[css_start:css_end]
    required_css = (
        '.worksheet-document[data-case-id="SSS-C1-CASE05"]',
        "MISSION REQUIREMENTS · DEFINE BEFORE DESIGN",
        "ACTION PATH · CAUTIOUS NOW → DURABLE DESIGN",
        "MONITORING GATE",
        "ACCEPTED RESPONSE PATH · ACTION → DESIGN → VERIFY",
        "t7-need",
        "t7-criteria",
        "t7-constraints",
        "t7-verify",
        "t8-immediate",
        "t8-durable",
        "t8-justify",
        "a8-test",
        "repeating-linear-gradient",
        ".worksheet-document.grayscale",
    )
    check(
        "the shared component layer declares the complete Europa SV1 grammar",
        all(token in spec_css for token in required_css),
        [token for token in required_css if token not in spec_css],
    )
    check(
        "the SV1 layer stays inside the shared explanatory-visual payload",
        css.index("/* BEGIN SSS/HHH EXPLANATORY-VISUAL PRIMITIVES */") < css_start < css_end < css.index("/* END SSS/HHH EXPLANATORY-VISUAL PRIMITIVES */"),
    )
    check(
        "the SV1 layer remains strictly Case 05 scoped",
        spec_css.count('.worksheet-document[data-case-id="SSS-C1-CASE05"]') >= 20
        and not re.search(r'SSS-(?:C1|C2)-CASE(?!05)', spec_css),
    )
    persist_blocks = re.findall(r"[^{}]*data-persist-id[^{}]*\{[^{}]*\}", spec_css)
    check(
        "the SV1 layer never sizes or prefills learner responses",
        persist_blocks
        and all(not re.search(r"\b(?:min-|max-)?(?:width|height)\s*:|\bcontent\s*:", block) for block in persist_blocks),
    )
    check(
        "requirements retain four border states and independent patterns",
        all(token in spec_css for token in ("solid", "double", "dotted", "dashed", "europa-spec-need-pattern", "europa-spec-criteria-pattern", "europa-spec-constraint-pattern", "europa-spec-verify-pattern")),
    )
    check(
        "normal and grayscale SV1 surfaces retain paper and ink fallbacks",
        ".worksheet-document.grayscale" in spec_css and "background-color: var(--paper, #fff)" in spec_css and "color: var(--ink, #18212b)" in spec_css,
    )
    check(
        "the CSS introduces no radiation quantity or guaranteed result",
        not re.search(r"\b\d+(?:\.\d+)?\s*(?:%|mGy|Gy|Sv|sievert)\b|guaranteed\s+(?:safe|success|solution)", spec_css, flags=re.IGNORECASE),
    )

    check(
        "the browser harness registers exactly three focused Europa specification assertions",
        harness.count("specification-verification pages retain strict fit, page counts and geometry") == 1
        and harness.count("specification panel preserves requirements, response fields and monitoring gate") == 1
        and 'for (const grayscale of [false, true])' in harness,
    )
    check(
        "the browser contract covers all six final-page states and strict fit",
        all(token in harness for token in ("student-mission-04", "answer-key-04", "accessible-mission-07", 'state.pageSize === "816x1056"', "state.fits")),
    )
    check(
        "the browser contract preserves all fourteen learner field identities",
        all(persist_id in harness for persist_id in student_t7 + accessible_t7 + student_t8 + accessible_t8),
    )
    check(
        "the browser contract pins Answer Key wording and all safety boundaries",
        all(token in harness for token in (
            expected_task7[-1],
            expected_task8[0],
            expected_task8[-1],
            "The packet does not establish that one proposed design is already successful.",
            "Do not invent a numerical safe level. The game provides a diagnosis, not an in-game “apply the fix” step.",
        )),
    )

    check(
        "the production matrix records C1C5-VIS03 as the unaccepted 35-check candidate",
        bool(re.search(
            r"\| `C1C5-VIS03` .*\| 6 · Specification/verification \|.*"
            r"`IMPLEMENTED-CANDIDATE · 35/35 SPECIFICATION STATIC PASS · 2320/2351 LINUX BROWSER "
            r"· 3/3 CANDIDATE ASSERTIONS · 0 JS ERRORS · STRICT FIT 936/936 · EXTERNAL ACCEPTANCE PENDING`",
            plan,
        )),
    )
    check(
        "the plan keeps formal inventory at 26 of 36 with 10 remaining",
        "the formal inventory remains 26/36 completed with 10 remaining" in plan
        and "Accepted progress after the Hayes engineering-control-loop closeout is **26 of 36 completed**" in plan,
    )
    check(
        "the handoff binds prerequisite scope hashes and canonical browser evidence",
        "Unaccepted Family 6 candidate — Europa crop-protection specification" in handoff
        and "3b19fcbcf7cabec08aadf303b41eb8168604c931" in handoff
        and all(expected_hash in handoff for expected_hash in FROZEN_HASHES.values())
        and "**2320/2351**" in handoff
        and "**2351/2351 PASS**" in handoff,
    )
    check(
        "the handoff requires a candidate-specific stop and creates no acceptance",
        "Differential evidence does not itself authorize acceptance" in handoff
        and "does not establish a general platform policy" in handoff
        and "does not advance the 26/36 inventory" in handoff
        and "Do not mark `C1C5-VIS03` `VERIFIED-FAMILY`" in handoff,
    )

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f" — {detail}" if detail and not ok else ""))
    print(f"\nSpecification/verification validator: {passed}/{len(checks)} PASS")
    return 0 if passed == len(checks) == 35 else 1


if __name__ == "__main__":
    raise SystemExit(main())
