#!/usr/bin/env python3
"""Focused deterministic checks for the SSS biological/structural cutaway family."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "sss/campaign-2/case-01-heavy-hands/source"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
HANDOFF = ROOT / "sss/audit/final/SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md"

FROZEN_HASHES = {
    "content.html": "da20f3c12b1762ec1a2de57e170f707525d10e9f0ad740765a0b732395a86a1a",
    "presentation.css": "89fb9e784fae5ddec39bb5139c9254bf4b35ed2aa1596f4fe60622149ffb40ea",
    "layout-overrides.json": "c003ea05f6ad7dd2d9085c0f0e60e6471e9207f2401784d4e413637348edc605",
    "case-package.json": "f6244b5db18e7de66c32bc787792898612195cecb1927d23b5e52a8d5119a0c4",
    "task-registry.js": "a62376edaf946fc28f54527cd4c7d7190fd4b96826bc52b4d693a0ab6d543f51",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(node: object) -> str:
    return " ".join(node.stripped_strings)  # type: ignore[attr-defined]


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    source = (CASE / "content.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(source, "html.parser")
    css = COMPONENTS.read_text(encoding="utf-8")
    harness = HARNESS.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    handoff = HANDOFF.read_text(encoding="utf-8")

    figures = soup.select('figure[data-figure-id^="fig-span-"]')
    figure_ids = [figure.get("data-figure-id") for figure in figures]
    roles = [figure.find_parent("section").get("data-role") for figure in figures]
    pages = [figure.find_parent("section").get("data-page-id") for figure in figures]
    check(
        "Heavy Hands retains exactly two synchronized Task 4 span figures",
        figure_ids == ["fig-span-s4", "fig-span-a4"]
        and roles == ["student", "accessible"]
        and pages == ["student-mission-03", "accessible-mission-04"],
        {"ids": figure_ids, "roles": roles, "pages": pages},
    )

    for figure in figures:
        figure_id = figure.get("data-figure-id")
        svg = figure.find("svg", recursive=False)
        title = svg.find("title") if svg else None
        direct_rects = svg.find_all("rect", recursive=False) if svg else []
        patterns = svg.select("defs > pattern") if svg else []
        axis_labels = [normalized(node) for node in svg.select(":scope > .fig-axis")] if svg else []
        sub_labels = [normalized(node) for node in svg.select(":scope > .fig-sub")] if svg else []
        caption = figure.find("figcaption")
        description = figure.select_one(".extended-description")

        check(
            f"{figure_id} retains its accessible SVG name and title relationship",
            bool(svg)
            and svg.get("role") == "img"
            and svg.get("aria-label") == "How much of the bed depth a tuber spans as it thickens"
            and svg.get("aria-labelledby") == title.get("id")
            and normalized(title) == "How much of the bed depth a tuber spans as it thickens",
        )
        check(
            f"{figure_id} retains the exact six-mark bed/tuber geometry source",
            len(direct_rects) == 6
            and [node.get("height") for node in direct_rects[::2]] == ["72", "72", "72"]
            and [node.get("height") for node in direct_rects[1::2]] == ["10", "22", "38"],
            [(node.get("width"), node.get("height")) for node in direct_rects],
        )
        check(
            f"{figure_id} retains three independent grayscale-safe tuber patterns",
            len(patterns) == 3
            and len({pattern.get("id") for pattern in patterns}) == 3
            and len({node.get("fill") for node in direct_rects[1::2]}) == 3
            and all(str(node.get("fill", "")).startswith("url(#span-") for node in direct_rects[1::2]),
        )
        check(
            f"{figure_id} retains the exact small-medium-large direct labels",
            axis_labels == ["Small tuber", "Medium tuber", "Large tuber"],
            axis_labels,
        )
        check(
            f"{figure_id} retains the same-bed-depth and qualitative-span statements",
            sub_labels == [
                "Same 20 cm bed depth in all three panels. The bar shows how much of that depth one tuber spans.",
                "spans a small part",
                "spans a larger part",
                "spans the largest part",
                "Dashed outline = full 20 cm bed depth. No deformation quantity is shown, because none is reported.",
            ],
            sub_labels,
        )
        check(
            f"{figure_id} retains the evidence-limit caption",
            normalized(caption).endswith(
                "From the specimen record in this case; qualitative, with no deformation quantity reported."
            ),
            normalized(caption),
        )
        check(
            f"{figure_id} retains the non-color extended description",
            "same dashed outline for the 20 cm bed depth" in normalized(description)
            and "Pattern and size both differ, so it reads without colour" in normalized(description),
            normalized(description),
        )
        check(
            f"{figure_id} introduces no unsupported decimal or deformation measurement",
            not re.search(r"\b\d+\.\d+\b|\b(?:mm|mGy|percent|%)\b", normalized(figure), re.IGNORECASE)
            and "No deformation quantity" in normalized(figure),
            normalized(figure),
        )

    for filename, expected_hash in FROZEN_HASHES.items():
        actual = sha256(CASE / filename)
        check(f"frozen Heavy Hands {filename} SHA-256 remains exact", actual == expected_hash, actual)

    check(
        "all Heavy Hands role page counts remain unchanged",
        len(soup.select('section[data-role="student"]')) == 5
        and len(soup.select('section[data-role="teacher"]')) == 9
        and len(soup.select('section[data-role="answer"]')) == 4
        and len(soup.select('section[data-role="accessible"]')) == 8,
    )
    check(
        "Task 4 learner response identities and blankness remain exact",
        [node.get("data-persist-id") for node in soup.select('[data-persist-id="t4-span"], [data-persist-id="t4-rules-out"]')]
        == ["t4-span", "t4-rules-out"]
        and [node.get("data-persist-id") for node in soup.select('[data-persist-id="a4-span"], [data-persist-id="a4-rules-out"]')]
        == ["a4-span", "a4-rules-out"]
        and all(
            node.has_attr("data-response") and not node.get_text(strip=True)
            for node in soup.select(
                '[data-persist-id="t4-span"], [data-persist-id="t4-rules-out"], '
                '[data-persist-id="a4-span"], [data-persist-id="a4-rules-out"]'
            )
        ),
    )
    page_text = " ".join(
        normalized(figure.find_parent("section")) for figure in figures
    )
    check(
        "Task 4 keeps the bounded gorlroot observation and direction distinction",
        "deformation increases with tuber diameter" in page_text
        and "curves sideways across the row" in page_text
        and "neither toward the axis nor away from it" in page_text
        and "No deformation quantity is reported" in page_text,
    )

    css_start = css.index("Biological/structural cutaway family pilot: Heavy Hands.")
    css_end = css.index("/* END SSS/HHH CUTAWAY-VISUAL EXTENSIONS */", css_start)
    cutaway_css = css[css_start:css_end]
    cutaway_declarations = cutaway_css.split("*/", 1)[1]
    cutaway_css_without_comments = re.sub(r"/\*.*?\*/", "", cutaway_declarations, flags=re.DOTALL)
    required_css = (
        '.worksheet-document[data-case-id="SSS-C2-CASE01"]',
        '.figure[data-figure-id^="fig-span-"]',
        "--heavy-cutaway-line",
        "--heavy-cutaway-bed",
        "vector-effect: non-scaling-stroke",
        "shape-rendering: geometricPrecision",
        "rect:nth-of-type(1)",
        "rect:nth-of-type(3)",
        "rect:nth-of-type(5)",
        "rect:nth-of-type(2)",
        "rect:nth-of-type(4)",
        "rect:nth-of-type(6)",
        "stroke-dasharray: 5 3",
        'content: "RADIAL BED CUTAWAY · NOT TO SCALE"',
        "repeating-linear-gradient",
        '.worksheet-document.grayscale[data-case-id="SSS-C2-CASE01"]',
    )
    check(
        "the shared component layer declares the complete Heavy Hands cutaway grammar",
        all(token in cutaway_css for token in required_css),
        [token for token in required_css if token not in cutaway_css],
    )
    check(
        "the cutaway layer remains inside its explicit extension sentinels",
        css.index("/* BEGIN SSS/HHH CUTAWAY-VISUAL EXTENSIONS */") < css_start < css_end,
    )
    check(
        "the cutaway layer remains strictly Heavy Hands and figure scoped",
        cutaway_css.count('.worksheet-document[data-case-id="SSS-C2-CASE01"]') >= 20
        and "SSS-C1-" not in cutaway_css
        and not re.search(r"SSS-C2-CASE(?!01)", cutaway_css)
        and "data-figure-id" in cutaway_css,
    )
    generated = re.findall(r'content:\s*"([^"]+)"', cutaway_css)
    check(
        "the cutaway layer generates only the qualitative cutaway status",
        generated == ["RADIAL BED CUTAWAY · NOT TO SCALE"],
        generated,
    )
    check(
        "the cutaway layer does not target learner responses or invent measurements",
        "data-persist-id" not in cutaway_css_without_comments
        and "data-response" not in cutaway_css_without_comments
        and not re.search(r"\b(?:g|cm|mm|percent|%)\b", cutaway_css_without_comments, re.IGNORECASE)
        and "deformation" not in cutaway_css_without_comments.lower(),
    )
    check(
        "the cutaway geometry keeps equal bed panels and strictly increasing organ spans",
        all(token in cutaway_css for token in (
            "width: 186px",
            "height: 52px",
            "width: 56px",
            "height: 12px",
            "width: 64px",
            "height: 26px",
            "width: 86px",
            "height: 42px",
        )),
    )
    check(
        "normal and grayscale cutaway surfaces retain paper and ink fallbacks",
        cutaway_css.count("var(--ink, #18212b)") >= 2
        and cutaway_css.count("var(--paper, #fff)") >= 2
        and "var(--panel-light, #f7f9fa)" in cutaway_css,
    )

    cutaway_start = harness.index("// Register the Family 7 cutaway pilot")
    cutaway_end = harness.index("// Register the second standalone Family 6 contract", cutaway_start)
    cutaway_harness = harness[cutaway_start:cutaway_end]
    check(
        "the browser harness registers exactly three focused Heavy Hands cutaway assertions",
        harness.count("C2 Case 01 cutaway pages retain strict fit, page counts and geometry in normal and grayscale") == 1
        and harness.count('C2 Case 01 ${grayscale ? "grayscale" : "normal"} tuber cutaway preserves matched bed depth, qualitative size order and evidence limits') == 1
        and "api.getPackage().presentation.sharedComponentStyles === true" in cutaway_harness
        and "api.getPackage().presentation.sharedVisualStyles" not in cutaway_harness,
    )
    check(
        "the cutaway browser contract covers all four rendered views and strict fit",
        all(token in cutaway_harness for token in (
            "student-mission-03",
            "accessible-mission-04",
            "fig-span-s4",
            "fig-span-a4",
            "heavyCutawayPageFit.length === 4",
            'state.pageSize === "816x1056"',
            "state.fits",
            "state.figureFits",
        )),
    )
    check(
        "the cutaway browser contract measures equal beds and increasing contained tubers",
        all(token in cutaway_harness for token in (
            "bedWidths",
            "bedHeights",
            "tuberWidths[0] < state.tuberWidths[1]",
            "tuberHeights[0] < state.tuberHeights[1]",
            "new Set(state.tuberPatterns).size === 3",
            "state.contained",
            "strokeDasharray",
        )),
    )
    check(
        "the cutaway browser contract pins source labels and evidence limits",
        all(token in cutaway_harness for token in (
            "Small tuber|Medium tuber|Large tuber",
            "Same 20 cm bed depth in all three panels",
            "No deformation quantity is shown, because none is reported",
            "qualitative, with no deformation quantity reported",
            "same dashed outline for the 20 cm bed depth",
            "RADIAL BED CUTAWAY · NOT TO SCALE",
        )),
    )
    check(
        "the cutaway browser contract restores Student normal state after its focused run",
        'api.setRole("student")' in cutaway_harness
        and 'api.saveState({ grayscale: false })' in cutaway_harness,
    )

    check(
        "the plan records C2C1-VIS01 as corrected but unaccepted",
        "`C2C1-VIS01` is the corrected but unaccepted Family 7 pilot" in plan
        and re.search(r"\| `C2C1-VIS01` .*\| `IMPLEMENTED-CANDIDATE` \|", plan) is not None
        and all(token in plan for token in (
            "b6a56b9c7b8a24cdb41942a2d32705d95432e0c0",
            "2363/2365",
            "zero application JavaScript errors",
            "identical assertion-name sets",
            "all 2362 inherited assertions passed",
            "three registered assertions but only one passing",
            "not the anticipated inherited 2365/2365 differential",
            "immutable evidence",
        )),
    )
    check(
        "the plan preserves 31/36 while the cutaway candidate awaits rendering",
        "C2C1-VIS01 does not advance the accepted **31 of 36 completed / 5 of 36 remaining** inventory" in plan
        and "Family 7 remains zero of two accepted assignments" in plan,
    )
    check(
        "the handoff records the pending Family 7 pilot and frozen Heavy Hands hashes",
        "Pending Family 7 pilot — Heavy Hands radial-bed cutaway" in handoff
        and "C2C1-VIS01" in handoff
        and "2366/2366" in handoff
        and "2363/2365" in handoff
        and "2362/2362 PASS" in handoff
        and "all 2362 inherited assertions passed" in handoff
        and "not the anticipated inherited 2365/2365 differential" in handoff
        and "sharedComponentStyles" in handoff
        and "31/36" in handoff
        and all(expected in handoff for expected in FROZEN_HASHES.values()),
    )
    check(
        "the handoff requires normal/grayscale geometry, fit and bounded-science inspection",
        all(token in handoff for token in (
            "Student page 3",
            "Accessible page 4",
            "RADIAL BED CUTAWAY · NOT TO SCALE",
            "same 20 cm bed depth",
            "No deformation quantity",
            "strict fit",
            "816 × 1056",
            "grayscale",
        )),
    )

    failures = [(name, detail) for name, passed, detail in checks if not passed]
    print("SSS visual modernization · cutaway family")
    print(f"Result: {len(checks) - len(failures)}/{len(checks)} PASS")
    for name, detail in failures:
        print(f"FAIL: {name}\n  {detail}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
