#!/usr/bin/env python3
"""Focused deterministic checks for the SSS biological/structural cutaway family."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
HEAVY_CASE = ROOT / "sss/campaign-2/case-01-heavy-hands/source"
DANCE_CASE = ROOT / "sss/campaign-2/case-02-missing-dance/source"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
HANDOFF = ROOT / "sss/audit/final/SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md"

HEAVY_FROZEN_HASHES = {
    "content.html": "da20f3c12b1762ec1a2de57e170f707525d10e9f0ad740765a0b732395a86a1a",
    "presentation.css": "89fb9e784fae5ddec39bb5139c9254bf4b35ed2aa1596f4fe60622149ffb40ea",
    "layout-overrides.json": "c003ea05f6ad7dd2d9085c0f0e60e6471e9207f2401784d4e413637348edc605",
    "case-package.json": "f6244b5db18e7de66c32bc787792898612195cecb1927d23b5e52a8d5119a0c4",
    "task-registry.js": "a62376edaf946fc28f54527cd4c7d7190fd4b96826bc52b4d693a0ab6d543f51",
}

DANCE_FROZEN_HASHES = {
    "content.html": "56338f5db3e89c9187f61fcf130f13c572f00f82173744cade9db810c627c57a",
    "presentation.css": "ed0fd67a1433a4c035e3f1b1a3c61065fee064fdc18d392985f285b8e378f28d",
    "layout-overrides.json": "92c3b314b05261245fe923cd278edfcaf7a1695fe526cdf2223e9509f897b49d",
    "case-package.json": "59026d6c4f54b362700018e268f2892a7c837817b4e6ec14e06d810dd9a66881",
    "task-registry.js": "8aaa2854d946f67e5c59261d314bf05764f4f4b21ccaa81009daa6ca4d51eda8",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(node: object) -> str:
    return " ".join(node.stripped_strings)  # type: ignore[attr-defined]


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    source = (HEAVY_CASE / "content.html").read_text(encoding="utf-8")
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

    for filename, expected_hash in HEAVY_FROZEN_HASHES.items():
        actual = sha256(HEAVY_CASE / filename)
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
    css_end = css.index("Biological/structural cutaway family completion: The Missing Dance.", css_start)
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
        "the plan records C2C1-VIS01 as the accepted corrected Family 7 finding",
        "`C2C1-VIS01` is the accepted first Family 7 biological/structural cutaway finding" in plan
        and re.search(
            r"\| `C2C1-VIS01` .*\| 7 · Biological/structural cutaway \|.*"
            r"`VERIFIED-FAMILY · 41/41 CUTAWAY STATIC PASS · DIFFERENTIAL MAC/CHROME PASS ×2 "
            r"· 0 JS ERRORS · STRICT FIT 936/936 · 95af208 ACCEPTED`",
            plan,
        ) is not None
        and all(token in plan for token in (
            "b6a56b9c7b8a24cdb41942a2d32705d95432e0c0",
            "95af208f713c15c84f9e5386c6c55ded8124755f",
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
        "the plan advances accepted inventory to 32 of 36 and Family 7 to one of two",
        "Accepted progress after the Heavy Hands radial-bed cutaway closeout is **32 of 36 completed**" in plan
        and "**4 of 36 remaining**" in plan
        and "Family 7 has one of two assignments verified" in plan
        and "Accepted progress after The Gift intervention-comparison closeout is **31 of 36 completed**" in plan,
    )
    check(
        "the handoff records the accepted Family 7 finding and frozen Heavy Hands hashes",
        "Accepted Family 7 finding — Heavy Hands radial-bed cutaway" in handoff
        and "C2C1-VIS01" in handoff
        and "Canonical project registration remains 2366" in handoff
        and "2363/2365" in handoff
        and "2362/2362 PASS" in handoff
        and "2365/2365 PASS" in handoff
        and "+3 registered and +3 passed" in handoff
        and "All three new Heavy Hands assertions registered and" in handoff
        and "no assertion was removed" in handoff
        and "all 2362 inherited assertions passed" in handoff
        and "not the anticipated inherited 2365/2365 differential" in handoff
        and "sharedComponentStyles" in handoff
        and "does not establish a general Mac/platform" in handoff
        and "The formal inventory is now **32 of 36 completed**" in handoff
        and "with **4 remaining**" in handoff
        and "Family 7 has one of two assignments verified" in handoff
        and all(expected in handoff for expected in HEAVY_FROZEN_HASHES.values()),
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

    dance_source = (DANCE_CASE / "content.html").read_text(encoding="utf-8")
    dance_soup = BeautifulSoup(dance_source, "html.parser")
    dance_registry = (DANCE_CASE / "task-registry.js").read_text(encoding="utf-8")
    dance_figures = dance_soup.select('figure[data-figure-id^="fig-cone-"]')
    dance_ids = [figure.get("data-figure-id") for figure in dance_figures]
    dance_roles = [figure.find_parent("section").get("data-role") for figure in dance_figures]
    dance_pages = [figure.find_parent("section").get("data-page-id") for figure in dance_figures]
    check(
        "The Missing Dance retains exactly two synchronized Task 3 cone figures",
        dance_ids == ["fig-cone-s3", "fig-cone-a3"]
        and dance_roles == ["student", "accessible"]
        and dance_pages == ["student-mission-03", "accessible-mission-03"],
        {"ids": dance_ids, "roles": dance_roles, "pages": dance_pages},
    )

    for figure in dance_figures:
        figure_id = figure.get("data-figure-id")
        svg = figure.find("svg", recursive=False)
        title = svg.find("title") if svg else None
        cone = svg.find("path", recursive=False) if svg else None
        pores = svg.find_all("rect", recursive=False) if svg else []
        patterns = svg.select("defs > pattern") if svg else []
        axis_labels = [normalized(node) for node in svg.select(":scope > .fig-axis")] if svg else []
        sub_labels = [normalized(node) for node in svg.select(":scope > .fig-sub")] if svg else []
        caption = figure.find("figcaption")
        description = figure.select_one(".extended-description")

        check(
            f"{figure_id} retains its accessible SVG name and title relationship",
            bool(svg)
            and svg.get("role") == "img"
            and svg.get("aria-label") == "Cut-away of the anther cone showing pores already present"
            and svg.get("aria-labelledby") == title.get("id")
            and normalized(title) == "Cut-away of the anther cone showing pores already present",
        )
        check(
            f"{figure_id} retains one cone section and eight already-present pore marks",
            bool(cone)
            and cone.get("d") == "M150,40 L112,150 L188,150 Z"
            and len(pores) == 8
            and all(node.get("width") == "5" and node.get("height") == "4" for node in pores),
            {"path": cone.get("d") if cone else None, "pores": len(pores)},
        )
        check(
            f"{figure_id} retains the mature-pollen pattern as the cone fill",
            len(patterns) == 1
            and str(patterns[0].get("id", "")).startswith("pollen-")
            and cone.get("fill") == f"url(#{patterns[0].get('id')})"
            and len(patterns[0].select("rect + circle")) == 1,
        )
        check(
            f"{figure_id} retains direct pore and mature-pollen labels",
            axis_labels == ["Pores", "Mature pollen"],
            axis_labels,
        )
        check(
            f"{figure_id} retains the exact pore, viability and contact statements",
            sub_labels == [
                "Cut-away of one anther cone. The pores are already there before anything touches the flower.",
                "already present, not blocked",
                "viable at 98%, still inside",
                "Gentle contact releases almost none of it.",
            ],
            sub_labels,
        )
        check(
            f"{figure_id} retains the no-opening evidence-limit caption",
            "nothing opens or unseals" in normalized(caption)
            and "Labels are direct, so the figure reads without colour" in normalized(caption),
            normalized(caption),
        )
        check(
            f"{figure_id} retains the non-color structural description",
            "triangular cut-away of the cone" in normalized(description)
            and "dot-patterned for dense pollen" in normalized(description)
            and "Four small pores sit along each sloping side, all drawn the same way" in normalized(description),
            normalized(description),
        )
        check(
            f"{figure_id} introduces no unsupported numeric evidence",
            sorted(re.findall(r"\b\d+(?:\.\d+)?\b", normalized(figure))) == ["1", "98"],
            re.findall(r"\b\d+(?:\.\d+)?\b", normalized(figure)),
        )

    for filename, expected_hash in DANCE_FROZEN_HASHES.items():
        actual = sha256(DANCE_CASE / filename)
        check(f"frozen The Missing Dance {filename} SHA-256 remains exact", actual == expected_hash, actual)

    check(
        "all The Missing Dance role page counts remain unchanged",
        len(dance_soup.select('section[data-role="student"]')) == 6
        and len(dance_soup.select('section[data-role="teacher"]')) == 8
        and len(dance_soup.select('section[data-role="answer"]')) == 4
        and len(dance_soup.select('section[data-role="accessible"]')) == 8,
    )
    check(
        "Task 3 learner response identities and blankness remain exact",
        [node.get("data-persist-id") for node in dance_soup.select('[data-persist-id="t3-healthy"], [data-persist-id="t3-missing"]')]
        == ["t3-healthy", "t3-missing"]
        and [node.get("data-persist-id") for node in dance_soup.select('[data-persist-id="a3-healthy"], [data-persist-id="a3-missing"]')]
        == ["a3-healthy", "a3-missing"]
        and all(
            node.has_attr("data-response") and not node.get_text(strip=True)
            for node in dance_soup.select(
                '[data-persist-id="t3-healthy"], [data-persist-id="t3-missing"], '
                '[data-persist-id="a3-healthy"], [data-persist-id="a3-missing"]'
            )
        ),
    )
    check(
        "The Missing Dance keeps Earth buzz pollination distinct from fictional case coupling",
        "establishedEarthScienceComparison" in dance_registry
        and "a bee grasps the flower and vibrates it mechanically" in dance_registry
        and "caseSpecificEvidence" in dance_registry
        and "the lyre-moth's hovering wingbeat" in dance_registry
        and "the airborne coupling route" in dance_registry
        and '"124 Hz is a magic frequency that guarantees pollen release"' in dance_registry,
    )

    dance_css_start = css.index("Biological/structural cutaway family completion: The Missing Dance.")
    dance_css_end = css.index("/* END SSS/HHH CUTAWAY-VISUAL EXTENSIONS */", dance_css_start)
    dance_css = css[dance_css_start:dance_css_end]
    dance_declarations = dance_css.split("*/", 1)[1]
    dance_css_without_comments = re.sub(r"/\*.*?\*/", "", dance_declarations, flags=re.DOTALL)
    required_dance_css = (
        '.worksheet-document[data-case-id="SSS-C2-CASE02"]',
        '.figure[data-figure-id^="fig-cone-"]',
        "--dance-cutaway-line",
        "--dance-cutaway-panel",
        "vector-effect: non-scaling-stroke",
        "shape-rendering: geometricPrecision",
        "transform: scale(1.35, 1.08)",
        "transform-box: view-box",
        "stroke-dasharray: 5 3",
        'content: "BOTANICAL CUTAWAY · SECTION A–A"',
        "repeating-linear-gradient",
        '.worksheet-document.grayscale[data-case-id="SSS-C2-CASE02"]',
    )
    check(
        "the shared component layer declares the complete Missing Dance cutaway grammar",
        all(token in dance_css for token in required_dance_css),
        [token for token in required_dance_css if token not in dance_css],
    )
    check(
        "the Missing Dance cutaway layer remains inside the Family 7 extension sentinels",
        css.index("/* BEGIN SSS/HHH CUTAWAY-VISUAL EXTENSIONS */") < dance_css_start < dance_css_end,
    )
    check(
        "the Missing Dance cutaway layer remains strictly Case 02 and figure scoped",
        dance_css.count('.worksheet-document[data-case-id="SSS-C2-CASE02"]') >= 13
        and "SSS-C1-" not in dance_css
        and not re.search(r"SSS-C2-CASE(?!02)", dance_css)
        and "data-figure-id" in dance_css,
    )
    dance_generated = re.findall(r'content:\s*"([^"]+)"', dance_css)
    check(
        "the Missing Dance layer generates only the qualitative section status",
        dance_generated == ["BOTANICAL CUTAWAY · SECTION A–A"],
        dance_generated,
    )
    check(
        "the Missing Dance layer does not target learner responses or invent science quantities",
        "data-persist-id" not in dance_css_without_comments
        and "data-response" not in dance_css_without_comments
        and not re.search(r"\b(?:Hz|percent|%)\b", dance_css_without_comments, re.IGNORECASE)
        and "release" not in dance_css_without_comments.lower(),
    )
    check(
        "the Missing Dance geometry enlarges one coherent cone section and its pore marks",
        "transform: scale(1.35, 1.08)" in dance_css
        and "transform-origin: 150px 95px" in dance_css
        and "> svg > path" in dance_css
        and "> svg > rect" in dance_css,
    )
    check(
        "the Missing Dance leaders preserve independent solid and dashed states",
        "> svg > line:nth-of-type(2)" in dance_css
        and "stroke-dasharray: 5 3" in dance_css,
    )
    check(
        "normal and grayscale Missing Dance cutaway surfaces retain paper and ink fallbacks",
        dance_css.count("var(--ink, #18212b)") >= 2
        and dance_css.count("var(--paper, #fff)") >= 2
        and "var(--panel-light, #f7f9fa)" in dance_css,
    )

    dance_harness_start = harness.index("// Register the second Family 7 cutaway")
    dance_harness_end = harness.index("// Register the second standalone Family 6 contract", dance_harness_start)
    dance_harness = harness[dance_harness_start:dance_harness_end]
    check(
        "the browser harness registers exactly three focused Missing Dance cutaway assertions",
        harness.count("C2 Case 02 cutaway pages retain strict fit, page counts and geometry in normal and grayscale") == 1
        and harness.count('C2 Case 02 ${grayscale ? "grayscale" : "normal"} poricidal cutaway preserves open pores, retained mature pollen and evidence limits') == 1
        and "api.getPackage().presentation.sharedComponentStyles === true" in dance_harness
        and "api.getPackage().presentation.sharedVisualStyles" not in dance_harness,
    )
    check(
        "the Missing Dance browser contract covers all four rendered views and strict fit",
        all(token in dance_harness for token in (
            "student-mission-03",
            "accessible-mission-03",
            "fig-cone-s3",
            "fig-cone-a3",
            "danceCutawayPageFit.length === 4",
            'state.pageSize === "816x1056"',
            "state.fits",
            "state.figureFits",
        )),
    )
    check(
        "the Missing Dance browser contract measures cone, pores, patterns and leader states",
        all(token in dance_harness for token in (
            "coneWidth > 100",
            "coneHeight > 110",
            "poreCount === 8",
            "leftPores",
            "rightPores",
            "pollenPattern.startsWith",
            'leaderDashes[0] === "none"',
            'leaderDashes[1] !== "none"',
        )),
    )
    check(
        "the Missing Dance browser contract pins direct labels and evidence limits",
        all(token in dance_harness for token in (
            "Pores|Mature pollen",
            "already present, not blocked",
            "viable at 98%, still inside",
            "Gentle contact releases almost none of it",
            "nothing opens or unseals",
            "BOTANICAL CUTAWAY · SECTION A–A",
        )),
    )
    check(
        "the Missing Dance cutaway browser contract restores Student normal state",
        'api.setRole("student")' in dance_harness
        and 'api.saveState({ grayscale: false })' in dance_harness,
    )

    check(
        "the plan records C2C2-VIS01 as the implemented but unaccepted Family 7 completion candidate",
        "`C2C2-VIS01` is the implemented but unaccepted second Family 7 candidate" in plan
        and re.search(r"\| `C2C2-VIS01` .*\| `IMPLEMENTED-CANDIDATE` \|", plan) is not None
        and re.search(r"Canonical project registration is\s+expected to become 2369", plan) is not None,
    )
    check(
        "the plan preserves 32/36 while the Missing Dance candidate awaits rendering",
        re.search(
            r"C2C2-VIS01 does not advance the accepted\s+\*\*32 of 36 completed / 4 of 36 remaining\*\* inventory",
            plan,
        ) is not None
        and re.search(r"Family 7 remains one of two accepted\s+assignments", plan) is not None,
    )
    check(
        "the handoff records the pending Missing Dance cutaway and its frozen hashes",
        "Pending Family 7 completion — The Missing Dance botanical cutaway" in handoff
        and "C2C2-VIS01" in handoff
        and "2369/2369" in handoff
        and "2368/2368" in handoff
        and "32/36" in handoff
        and all(expected in handoff for expected in DANCE_FROZEN_HASHES.values()),
    )
    check(
        "the handoff requires normal/grayscale Missing Dance geometry, fit and bounded-science inspection",
        all(token in handoff for token in (
            "Student page 3",
            "Accessible page 3",
            "BOTANICAL CUTAWAY · SECTION A–A",
            "98%",
            "strict fit",
            "816 × 1056",
            "grayscale",
            "already present, not blocked",
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
