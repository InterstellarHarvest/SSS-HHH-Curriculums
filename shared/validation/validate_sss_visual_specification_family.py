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
HEAVY_CASE = ROOT / "sss/campaign-2/case-01-heavy-hands/source"
HEAVY_CONTENT = HEAVY_CASE / "content.html"
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

HEAVY_FROZEN_HASHES = {
    "content.html": "da20f3c12b1762ec1a2de57e170f707525d10e9f0ad740765a0b732395a86a1a",
    "presentation.css": "89fb9e784fae5ddec39bb5139c9254bf4b35ed2aa1596f4fe60622149ffb40ea",
    "layout-overrides.json": "c003ea05f6ad7dd2d9085c0f0e60e6471e9207f2401784d4e413637348edc605",
    "case-package.json": "f6244b5db18e7de66c32bc787792898612195cecb1927d23b5e52a8d5119a0c4",
    "task-registry.js": "a62376edaf946fc28f54527cd4c7d7190fd4b96826bc52b4d693a0ab6d543f51",
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
    heavy_source = HEAVY_CONTENT.read_text(encoding="utf-8")
    heavy_soup = BeautifulSoup(heavy_source, "html.parser")
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
        harness.count("C1 Case 05 specification-verification pages retain strict fit, page counts and geometry") == 1
        and harness.count("C1 Case 05 ${grayscale ? \"grayscale\" : \"normal\"} specification panel preserves requirements, response fields and monitoring gate") == 1
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
        "the production matrix accepts C1C5-VIS03 as the 35-check Family 6 finding",
        bool(re.search(
            r"\| `C1C5-VIS03` .*\| 6 · Specification/verification \|.*"
            r"`VERIFIED-FAMILY · 35/35 SPECIFICATION STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 22ab529 ACCEPTED`",
            plan,
        ))
        and "accepted first standalone Family 6 specification/verification finding" in plan
        and "`VERIFIED-FAMILY`. Family 6 now has two of four assignments verified" in plan,
    )
    check(
        "the plan advances formal inventory to 27 of 36 with 9 remaining without double-counting the hybrid",
        "Accepted progress after the Europa specification/verification closeout is **27 of 36 completed**" in plan
        and "**9 of 36 remaining**" in plan
        and "At the preceding Hayes engineering-control-loop closeout, accepted progress was 26 of 36 completed" in plan
        and "hybrid `C2C3-VIS03`, already counted once" in plan,
    )
    check(
        "the handoff records the accepted differential gate and preserved scope",
        "Accepted Family 6 finding — Europa crop-protection specification" in handoff
        and "22ab529c388ee4f33be97ce3150fc5b5c49cba0b" in handoff
        and "3b19fcbcf7cabec08aadf303b41eb8168604c931" in handoff
        and all(expected_hash in handoff for expected_hash in FROZEN_HASHES.values())
        and "2347/2347 PASS" in handoff
        and handoff.count("2350/2350 PASS") >= 2
        and "candidate delta is exactly +3" in handoff
        and "**2320/2351**" in handoff,
    )
    check(
        "the handoff records the Family 6 register and accepted inventory without creating platform policy",
        "does not establish a general platform policy" in handoff
        and "| `C2C3-VIS03` | `79a7c80` | `VERIFIED-FAMILY` |" in handoff
        and "| `C1C5-VIS03` | `22ab529` | `VERIFIED-FAMILY` |" in handoff
        and "Family 6 has two of four assignments verified" in handoff
        and "27 of 36 completed" in handoff
        and "9 remaining" in handoff
        and "Do not mark any additional finding accepted" in handoff,
    )

    heavy_student = heavy_soup.select_one('section[data-role="student"][data-page-id="student-mission-05"]')
    heavy_answer = heavy_soup.select_one('section[data-role="answer"][data-page-id="answer-key-04"]')
    heavy_accessible = heavy_soup.select_one('section[data-role="accessible"][data-page-id="accessible-mission-08"]')
    check("Heavy Hands retains the three frozen Task 8 page targets", all((heavy_student, heavy_answer, heavy_accessible)))
    check(
        "Heavy Hands page counts remain frozen across all four roles",
        {role: len(heavy_soup.select(f'section[data-role="{role}"]')) for role in ("student", "answer", "teacher", "accessible")}
        == {"student": 5, "answer": 4, "teacher": 9, "accessible": 8},
    )

    heavy_student_fields = ["t8-criterion", "t8-constraint", "t8-o1", "t8-o2", "t8-choice", "t8-trial", "t8-stop"]
    heavy_accessible_fields = ["a8-criterion", "a8-constraint", "a8-o1", "a8-o2", "a8-choice", "a8-trial", "a8-stop"]
    check(
        "Heavy Hands Student Task 8 retains all seven response identities in order",
        [node.get("data-persist-id") for node in heavy_student.select('.task-block [data-response]')] == heavy_student_fields,
    )
    check(
        "Heavy Hands Accessible Task 8 retains the parallel seven response identities",
        [node.get("data-persist-id") for node in heavy_accessible.select('[data-response]')] == heavy_accessible_fields,
    )
    heavy_learner_fields = [heavy_soup.select_one(f'[data-persist-id="{persist_id}"]') for persist_id in heavy_student_fields + heavy_accessible_fields]
    check(
        "all fourteen Heavy Hands learner fields remain blank writable responses",
        all(field and field.has_attr("data-response") and not normalized(field) for field in heavy_learner_fields),
    )
    check(
        "Heavy Hands preserves the accepted Task 7 and Task 8 heading structure",
        [heading.get("data-shell-task-heading") for heading in heavy_student.select("h2[data-shell-task-heading]")] == ["7", "8"]
        and [heading.get("data-shell-task-heading") for heading in heavy_answer.select("h2[data-shell-task-heading]")] == ["7", "8"]
        and [heading.get("data-shell-task-heading") for heading in heavy_accessible.select("h2[data-shell-task-heading]")] == ["8"],
    )
    check(
        "Heavy Hands directions preserve the midpoint-only rule and across-bed task boundary",
        "2.10 g ±0.05 g at midpoint" in normalized(heavy_student)
        and "The across-bed criterion the rule left out" in normalized(heavy_student)
        and "The rule you would add" in normalized(heavy_accessible),
    )
    heavy_student_proposals = [normalized(row.select_one("td")) for row in heavy_student.select("table tbody tr")]
    heavy_accessible_proposals = [normalized(row.select_one("td")) for row in heavy_accessible.select("table tbody tr")]
    check(
        "Heavy Hands preserves the two proposals and their order across learner editions",
        len(heavy_student_proposals) == len(heavy_accessible_proposals) == 2
        and heavy_student_proposals[0].startswith("Build a larger ring radius")
        and heavy_student_proposals[1].startswith("Use a thinner growing bed")
        and heavy_accessible_proposals[0].startswith("Build a bigger ring")
        and heavy_accessible_proposals[1].startswith("Use a thinner bed"),
    )

    expected_heavy_answers = [
        "Across-bed criterion the specification left out: A maximum permitted difference in magnitude across the full radial depth of the growing bed, measured at the bed top and the bed base rather than at one point. A secure answer names where the requirement applies and over what span. Accept any tolerance value provided the student says the number itself would have to be justified by a trial.",
        "One constraint reported in this case: A larger ring requires engineering work, while a thinner bed can be trialled immediately. Accept also the fixed 2.1 g target.",
        "Table 7 — does each proposal meet the criterion: Larger radius: yes. Spinning a longer ring more slowly keeps the pull at the same target, and the same 20 cm of bed depth is then a smaller share of a longer radius, so the difference across the bed falls. Record GC-1208 resolved the matching problem this way, by extending the radius to 600 m. Thinner bed: yes, by the other route — a shallower bed reaches across less of the difference, so each plant samples less of it. Neither answer may promise recovery; both proposals still need the monitored trial.",
        "Monitored trial and stop rule: A secure answer measures the magnitude at the bed top and the bed base rather than at the midpoint alone, records tuber diameter alongside deformation on a stated schedule, and runs alongside an unchanged control planting. The stop rule should name an observation that ends the trial — for example, deformation still increasing with diameter by the day it first appeared in earlier crops — and should send the design back for revision rather than continuing to full scale.",
        "Marking note: Full credit requires the student to keep the claim bounded to this crop in this habitat. Answers that promise recovery, or that generalise the response to other organisms, have not met the bounded-claim dimension.",
    ]
    heavy_answer_block = heavy_answer.select_one('[data-shell-task-heading="8"] + .answer-block')
    check(
        "Heavy Hands Answer Key preserves the exact five-part specification exemplar",
        [normalized(node) for node in heavy_answer_block.select(":scope > p")] == expected_heavy_answers,
    )
    check(
        "Heavy Hands keeps every tolerance conditional on trial justification",
        "Accept any tolerance value provided the student says the number itself would have to be justified by a trial." in normalized(heavy_answer),
    )
    check(
        "Heavy Hands keeps both proposals unproven and trial-dependent",
        "Neither answer may promise recovery; both proposals still need the monitored trial." in normalized(heavy_answer),
    )
    check(
        "Heavy Hands keeps GC-1208 bounded and GC-1445 outside learner and Answer Key pages",
        all("GC-1208" in normalized(page) and "600 m" in normalized(page) for page in (heavy_student, heavy_accessible, heavy_answer))
        and all("GC-1445" not in normalized(page) for page in (heavy_student, heavy_accessible, heavy_answer)),
    )
    check(
        "Heavy Hands keeps the target magnitude distinct from an across-bed criterion",
        "fixed 2.1 g target" in normalized(heavy_answer)
        and "maximum permitted difference in magnitude across the full radial depth" in normalized(heavy_answer),
    )
    check(
        "Heavy Hands retains the warning that present readings are not completed tests",
        "present readings are not completed tests" in normalized(heavy_soup),
    )
    check(
        "Heavy Hands keeps the outcome bounded to this crop in this habitat",
        "bounded to this crop in this habitat" in normalized(heavy_answer)
        and "generalise the response to other organisms" in normalized(heavy_answer),
    )

    for filename, expected_hash in HEAVY_FROZEN_HASHES.items():
        check(
            f"frozen Heavy Hands {filename} SHA-256 remains exact",
            sha256(HEAVY_CASE / filename) == expected_hash,
            sha256(HEAVY_CASE / filename),
        )

    heavy_css_start = css.index("Specification/verification family expansion: Heavy Hands.")
    heavy_css_end = css.index("/* END SSS/HHH SPECIFICATION-VISUAL EXTENSIONS */", heavy_css_start)
    heavy_css = css[heavy_css_start:heavy_css_end]
    check(
        "the shared component layer declares the complete Heavy Hands SV1 grammar",
        all(token in heavy_css for token in (
            '.worksheet-document[data-case-id="SSS-C2-CASE01"]',
            "POINT RULE → ACROSS-BED TEST",
            "COMPARE AGAINST CRITERION",
            "DECISION GATE",
            "t8-criterion",
            "t8-constraint",
            "t8-o1",
            "t8-o2",
            "t8-choice",
            "t8-trial",
            "t8-stop",
            "a8-stop",
            "repeating-linear-gradient",
            ".worksheet-document.grayscale",
        )),
    )
    check(
        "the Heavy Hands SV1 layer stays inside the specification-visual extension payload",
        css.index("/* BEGIN SSS/HHH SPECIFICATION-VISUAL EXTENSIONS */") < heavy_css_start < heavy_css_end,
    )
    check(
        "the Heavy Hands SV1 layer remains strictly Case 01 scoped",
        heavy_css.count('.worksheet-document[data-case-id="SSS-C2-CASE01"]') >= 25
        and not re.search(r'SSS-(?:C1|C2)-CASE(?!01)', heavy_css),
    )
    heavy_persist_blocks = [
        f"{selector}{{{body}}}"
        for selector, body in re.findall(r"([^{}]*data-persist-id[^{}]*)\{([^{}]*)\}", heavy_css)
        if ":has(" not in selector
    ]
    check(
        "the Heavy Hands SV1 layer never sizes or prefills learner responses",
        heavy_persist_blocks
        and all(not re.search(r"\b(?:min-|max-)?(?:width|height)\s*:|\bcontent\s*:", block) for block in heavy_persist_blocks),
    )
    check(
        "Heavy Hands retains five independent requirement and verification patterns",
        all(token in heavy_css for token in (
            "heavy-spec-rule-pattern",
            "heavy-spec-criterion-pattern",
            "heavy-spec-constraint-pattern",
            "heavy-spec-option-pattern",
            "heavy-spec-verify-pattern",
            "padding-left: 6px",
        )),
    )
    check(
        "normal and grayscale Heavy Hands surfaces retain paper and ink fallbacks",
        ".worksheet-document.grayscale" in heavy_css
        and "background-color: var(--paper, #fff)" in heavy_css
        and "color: var(--ink, #18212b)" in heavy_css,
    )
    heavy_generated_labels = re.findall(r'content:\s*"([^"]+)"', heavy_css)
    check(
        "the CSS adds only relationship labels and no engineering value or result",
        heavy_generated_labels == ["POINT RULE → ACROSS-BED TEST", "COMPARE AGAINST CRITERION", "DECISION GATE"],
        heavy_generated_labels,
    )

    check(
        "the browser harness registers exactly three focused Heavy Hands specification assertions",
        harness.count("C2 Case 01 specification-verification pages retain strict fit, page counts and geometry") == 1
        and harness.count("C2 Case 01 ${grayscale ? \"grayscale\" : \"normal\"} specification panel preserves criterion, proposal comparison and monitored verification") == 1,
    )
    check(
        "the Heavy Hands browser contract covers all six views and strict fit",
        all(token in harness for token in (
            "student-mission-05",
            "answer-key-04",
            "accessible-mission-08",
            'state.pageSize === "816x1056"',
            "state.fits",
            "heavySpecificationPageFit.length === 6",
            "labelRailClearance.length === 5",
            "value >= 6",
            "width >= 108 && height >= 30",
        )),
    )
    check(
        "the Heavy Hands browser contract preserves all fourteen learner field identities",
        all(persist_id in harness for persist_id in heavy_student_fields + heavy_accessible_fields),
    )
    check(
        "the Heavy Hands browser contract pins Answer Key wording and science boundaries",
        all(token in harness for token in (
            expected_heavy_answers[0],
            expected_heavy_answers[2],
            expected_heavy_answers[3],
            expected_heavy_answers[4],
            '!state.pageText.includes("GC-1445")',
        )),
    )
    check(
        "the production matrix freezes C2C1-VIS03 as the corrected unaccepted 70-check candidate",
        bool(re.search(
            r"\| `C2C1-VIS03` .*\| 6 · Specification/verification \|.*"
            r"`CORRECTED-CANDIDATE · UNACCEPTED · 70/70 SPECIFICATION STATIC PASS "
            r"· 2323/2354 LINUX BROWSER · 3/3 NEW CONTRACTS PASS · 0 JS ERRORS · STRICT FIT 936/936`",
            plan,
        ))
        and "corrected but unaccepted second standalone Family 6" in plan,
    )
    check(
        "the handoff records the Heavy Hands candidate gate hashes and canonical total",
        "Active unaccepted Family 6 candidate — Heavy Hands across-bed specification" in handoff
        and "b95563f181c0d442d40784bbe1a45d1794cfb256" in handoff
        and all(expected_hash in handoff for expected_hash in HEAVY_FROZEN_HASHES.values())
        and "2323/2354" in handoff
        and "2354/2354 PASS" in handoff
        and "candidate delta is exactly +3" in handoff,
    )
    check(
        "the handoff freezes Heavy Hands field dimensions and makes reserve metrics non-contractual",
        all(token in handoff for token in (
            "356 × 32.63 px",
            "151.34 × 44.16 px",
            "720 × 53.75 px",
            "115.2 × 44.16 px",
            "720 × 61.44 px",
            "39.59 / 150.05 / 211.36 px",
            "not a numeric acceptance gate",
        )),
    )
    check(
        "Heavy Hands remains unaccepted without changing inventory or platform policy",
        "The formal inventory remains **27 of 36 completed**, with **9 remaining**" in handoff
        and re.search(r"Family 6 remains two of\s+four verified assignments while this candidate is unaccepted", handoff)
        and re.search(r"creates no general\s+platform policy", handoff)
        and "does not authorize a push" in handoff,
    )

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f" — {detail}" if detail and not ok else ""))
    print(f"\nSpecification/verification validator: {passed}/{len(checks)} PASS")
    return 0 if passed == len(checks) == 70 else 1


if __name__ == "__main__":
    raise SystemExit(main())
