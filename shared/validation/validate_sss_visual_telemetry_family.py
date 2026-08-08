#!/usr/bin/env python3
"""Focused deterministic checks for the first SSS telemetry-family pilot."""

from __future__ import annotations

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "sss/audit/final/SSS_FINAL_AUDIT_REMEDIATION_REGISTER_v0.1.md"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
EDITOR = ROOT / "apps/curriculum-editor/editor-app.js"
C1C3 = ROOT / "sss/campaign-1/case-03-mars-habitat/source/content.html"
C1C3_PACKAGE = ROOT / "sss/campaign-1/case-03-mars-habitat/source/case-package.json"
C2C1 = ROOT / "sss/campaign-2/case-01-heavy-hands/source/content.html"
C2C3 = ROOT / "sss/campaign-2/case-03-wrong-color-light/source/content.html"
C2C4 = ROOT / "sss/campaign-2/case-04-silent-grove/source/content.html"
C2C5 = ROOT / "sss/campaign-2/case-05-too-clean-room/source/content.html"
C2C6 = ROOT / "sss/campaign-2/case-06-first-garden/source/content.html"


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    register = REGISTER.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    css = COMPONENTS.read_text(encoding="utf-8")
    editor = EDITOR.read_text(encoding="utf-8")
    c1_package = json.loads(C1C3_PACKAGE.read_text(encoding="utf-8"))
    c1 = BeautifulSoup(C1C3.read_text(encoding="utf-8"), "html.parser")
    c2c1 = BeautifulSoup(C2C1.read_text(encoding="utf-8"), "html.parser")
    c2 = BeautifulSoup(C2C3.read_text(encoding="utf-8"), "html.parser")
    c2c4 = BeautifulSoup(C2C4.read_text(encoding="utf-8"), "html.parser")
    c2c5 = BeautifulSoup(C2C5.read_text(encoding="utf-8"), "html.parser")
    c2c6 = BeautifulSoup(C2C6.read_text(encoding="utf-8"), "html.parser")

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
        "DUAL-CHANNEL DIAGNOSTIC · UNEVEN",
        "QUANTITY ≠ DISTRIBUTION",
        "SHIP RECORD · DISCRETE BLOCKS",
        '.worksheet-document[data-case-id="SSS-C2-CASE04"]',
        ".telemetry-table",
        'data-figure-id^="fig-profile-"',
        'data-figure-id^="fig-gauge-"',
        'data-figure-id^="fig-production-"',
        'data-figure-id^="fig-patches-"',
        'font-family: "JetBrains Mono"',
        "shape-rendering: crispEdges",
        ".figure:where(",
    )
    missing_css = [token for token in required_css if token not in css]
    check("the shared component layer declares the telemetry frame, status, type, and line grammar", not missing_css, missing_css)
    check(
        "Mars opts into the extracted shared visual layer without the full protected-component layer",
        c1_package.get("presentation", {}).get("sharedVisualStyles") is True
        and c1_package.get("presentation", {}).get("sharedComponentStyles") is not True,
        c1_package.get("presentation"),
    )
    check(
        "the editor delivers opt-in visual primitives and stamps a stable rendered case identity",
        all(
            token in editor
            for token in (
                "function visualPrimitiveCss(css)",
                "casePackage.presentation.sharedVisualStyles",
                "sharedStyles.push(visualPrimitiveCss",
                "worksheetDocument.dataset.caseId = casePackage.id",
            )
        ),
    )
    check("the shared telemetry grammar never applies a whole-figure grayscale filter", "filter:" not in css[css.index("SSS/HHH explanatory-visual primitives."):css.index(".source-status")])
    compact_band_rules = css[css.index("Compact telemetry footprint."):css.index('.figure:where(\n  [data-visual-family="telemetry"]')]
    check(
        "the dense Student response-band figure retains the accepted compact flow footprint",
        all(
            token in compact_band_rules
            for token in (
                '.figure[data-figure-id="fig-band-student"]',
                "border-width: 1px",
                "padding: 3px 0 0",
                "padding-top: 0",
                "border-top: 0",
            )
        ),
        compact_band_rules,
    )

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

    quantity_figures = c1.select('figure:has(svg[data-quantity-spectrum="canonical-v1.0"])')
    quantity_roles = [figure.find_parent("section", attrs={"data-role": True})["data-role"] for figure in quantity_figures]
    check(
        "the Mars quantity-versus-spectrum diagnostic remains synchronized across learner and key instances",
        len(quantity_figures) == 3 and sorted(quantity_roles) == ["accessible", "answer", "student"],
        quantity_roles,
    )
    for index, figure in enumerate(quantity_figures, start=1):
        text = " ".join(figure.stripped_strings)
        svg = figure.find("svg")
        check(
            f"Mars quantity-versus-spectrum figure {index} preserves both exact channels and their footprint",
            svg is not None
            and svg.get("viewbox") == "0 0 520 205"
            and all(value in text for value in ("280", "ADEQUATE", "92%", "88%", "31%", "12%"))
            and len(svg.select('rect[fill^="url("]')) == 4
            and figure.find("figcaption") is not None,
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

    grove_cycle_tables = []
    for role, page_id in (("student", "student-mission-03"), ("accessible", "accessible-mission-03")):
        page = c2c4.select_one(f'section[data-role="{role}"][data-page-id="{page_id}"]')
        table = page.select_one("table.timeline-table") if page else None
        if table is not None:
            grove_cycle_tables.append((role, table))
    check(
        "the Silent Grove within-cycle record remains synchronized as two semantic tables",
        len(grove_cycle_tables) == 2,
        [role for role, _ in grove_cycle_tables],
    )
    for role, table in grove_cycle_tables:
        rows = table.select("tbody tr")
        text = " ".join(table.stripped_strings)
        check(
            f"the Silent Grove {role} cycle panel preserves exact discrete and missing-data blocks",
            len(rows) == 6
            and text.count("not separately reported") == 3
            and all(
                value in text
                for value in (
                    "Hours 0–6",
                    "Hours 6–12",
                    "Hours 12–18",
                    "Hours 18–19",
                    "Hours 19–24",
                    "24 h on / 0 h off",
                    "minimum reported",
                    "peak reported",
                    "no cycling pattern detectable",
                )
            ),
            text,
        )
    c2c4_text = " ".join(c2c4.stripped_strings)
    check(
        "the Silent Grove telemetry context preserves schedule, range, and threshold distinctions",
        all(
            value in c2c4_text
            for value in (
                "24.0 h on / 0.0 h off",
                "18.0 h on / 6.0 h off",
                "40–80 ppb",
                "0.0 ppb — no signal at the reporting threshold",
            )
        ),
    )

    profile = c2c1.select_one('figure[data-figure-id="fig-profile-t4"]')
    profile_text = " ".join(profile.stripped_strings) if profile else ""
    check(
        "the Heavy Hands radial profile preserves three exact radii, magnitudes, and outward direction",
        profile is not None
        and profile.find("svg", attrs={"viewbox": "0 0 640 170"}) is not None
        and all(
            value in profile_text
            for value in ("224.8 m", "224.9 m", "225.0 m", "2.0991 g", "2.10 g", "2.1009 g")
        )
        and profile_text.count("outward") >= 4
        and "no intermediate values inferred" in profile_text,
        profile_text,
    )

    gauge_figures = c2c5.select('figure[data-figure-id^="fig-gauge-"]')
    check("the detection-bound instrument analogy remains synchronized across learner editions", len(gauge_figures) == 2)
    for figure in gauge_figures:
        figure_id = figure["data-figure-id"]
        text = " ".join(figure.stripped_strings)
        check(
            f"{figure_id} preserves sub-threshold inputs, reported bin, and teaching-example status",
            figure.find("svg", attrs={"viewbox": "0 0 640 112"}) is not None
            and all(value in text for value in ("0.2 mm", "0.8 mm", "reported as 0 mm"))
            and "teaching example, not vault data" in text
            and "neither was nothing" in text,
            text,
        )

    production_figures = c2c5.select('figure[data-figure-id^="fig-production-"]')
    check("the six-month production monitor remains synchronized across learner editions", len(production_figures) == 2)
    for figure in production_figures:
        figure_id = figure["data-figure-id"]
        text = " ".join(figure.stripped_strings)
        check(
            f"{figure_id} preserves all six discrete monthly readings and baseline context",
            figure.find("svg", attrs={"viewbox": "0 0 640 152"}) is not None
            and all(value in text for value in ("100%", "68%", "31%", "11%", "6%"))
            and "month 1–2 baseline" in text
            and "no curve is drawn between them" in text,
            text,
        )

    patch_figures = c2c6.select('figure[data-figure-id^="fig-patches-"]')
    check("the site-survey diagnostic remains synchronized across learner editions", len(patch_figures) == 2)
    for figure in patch_figures:
        figure_id = figure["data-figure-id"]
        text = " ".join(figure.stripped_strings)
        check(
            f"{figure_id} preserves the patch range, trace status, and map/spacing limits",
            figure.find("svg", attrs={"viewbox": "0 0 640 184"}) is not None
            and "4–6 m" in text
            and "trace levels only" in text
            and "not a map" in text.lower()
            and "No distance between circles is drawn" in text,
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
