#!/usr/bin/env python3
"""Focused deterministic checks for the first SSS telemetry-family pilot."""

from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "sss/audit/final/SSS_FINAL_AUDIT_REMEDIATION_REGISTER_v0.1.md"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
C1C3 = ROOT / "sss/campaign-1/case-03-mars-habitat/source/content.html"
C2C3 = ROOT / "sss/campaign-2/case-03-wrong-color-light/source/content.html"


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    register = REGISTER.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    css = COMPONENTS.read_text(encoding="utf-8")
    c1 = BeautifulSoup(C1C3.read_text(encoding="utf-8"), "html.parser")
    c2 = BeautifulSoup(C2C3.read_text(encoding="utf-8"), "html.parser")

    deferred = re.findall(
        r"^\| `((?:C1|C2)C\d-(?:VIS\d+|GS\d+))` .*\| \*\*DEFERRED-VISUAL\*\* \|",
        register,
        flags=re.MULTILINE,
    )
    visual_rows = re.findall(r"^\| `((?:C1|C2)C\d-VIS\d+)` \|", plan, flags=re.MULTILINE)
    check("the current register contains exactly 36 formal deferred visual findings", len(deferred) == 36, deferred)
    check("the production matrix reconciles exactly 35 VIS findings", len(visual_rows) == 35 and len(set(visual_rows)) == 35, visual_rows)

    required_css = (
        "data-visual-family",
        "data-visual-status",
        "--visual-line-primary",
        "--visual-line-secondary",
        "--visual-line-accent",
        "DOME SENSOR · DISCRETE CATEGORIES",
        "SITE RESPONSE · DISCRETE BAND",
        "OPTICAL LINK · DISCRETE BANDS",
        'font-family: "JetBrains Mono"',
        "shape-rendering: crispEdges",
    )
    missing_css = [token for token in required_css if token not in css]
    check("the shared component layer declares the telemetry frame, status, type, and line grammar", not missing_css, missing_css)
    check("the shared telemetry grammar never applies a whole-figure grayscale filter", "filter:" not in css[css.index("SSS/HHH explanatory-visual primitives."):css.index(".source-status")])

    c1_figures = c1.select("figure.spectrum-figure")
    c1_roles = [figure.find_parent("section", attrs={"data-role": True})["data-role"] for figure in c1_figures]
    check("the Mars optical-link figure remains synchronized across four role instances", len(c1_figures) == 4 and sorted(c1_roles) == ["accessible", "answer", "student", "teacher"], c1_roles)
    for index, figure in enumerate(c1_figures, start=1):
        text = " ".join(figure.stripped_strings)
        svg = figure.find("svg")
        patterned = svg.select('rect[fill^="url("]') if svg else []
        check(
            f"Mars optical-link figure {index} preserves exact discrete values and geometry",
            svg is not None
            and svg.get("viewbox") == "0 0 520 250"
            and all(value in text for value in ("92%", "88%", "31%", "12%"))
            and len(patterned) == 4,
            text,
        )

    expected_ids = {
        "fig-gro9-student",
        "fig-gro9-accessible",
        "fig-band-student",
        "fig-band-accessible",
    }
    c2_figures = {figure.get("data-figure-id"): figure for figure in c2.select("figure[data-figure-id]")}
    check("the Wrong Color of Light telemetry figures remain synchronized across Student and Accessible", set(c2_figures) == expected_ids, sorted(c2_figures))

    for figure_id in ("fig-gro9-student", "fig-gro9-accessible"):
        figure = c2_figures.get(figure_id)
        text = " ".join(figure.stripped_strings) if figure else ""
        svg = figure.find("svg") if figure else None
        check(
            f"{figure_id} preserves discrete categories, inequality, patterns, and footprint",
            figure is not None
            and svg is not None
            and svg.get("viewbox") == "0 0 640 166"
            and all(value in text for value in ("62%", "18%", "15%", "<5%", "280 µmol/m²/s"))
            and len(svg.select('rect[fill^="url("]')) == 4
            and figure.find("figcaption") is not None
            and figure.select_one(".extended-description") is not None,
            text,
        )

    for figure_id in ("fig-band-student", "fig-band-accessible"):
        figure = c2_figures.get(figure_id)
        text = " ".join(figure.stripped_strings) if figure else ""
        svg = figure.find("svg") if figure else None
        check(
            f"{figure_id} preserves the measured band, explicit uncertainty, and footprint",
            figure is not None
            and svg is not None
            and svg.get("viewbox") == "0 0 640 144"
            and "460–540 nm" in text
            and "not specified and is not zero" in text
            and "No curve is drawn" in text
            and len(svg.select('rect[fill^="url("]')) == 3,
            text,
        )

    failures = [(name, detail) for name, passed, detail in checks if not passed]
    print("SSS visual modernization · telemetry family")
    print(f"Result: {len(checks) - len(failures)}/{len(checks)} PASS")
    for name, detail in failures:
        print(f"FAIL: {name}\n  {detail}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
