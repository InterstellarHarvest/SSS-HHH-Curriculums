#!/usr/bin/env python3
"""Validate the Case 02 Student-only CER HTML maintenance build."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


CASE_ROOT = Path(__file__).resolve().parents[1]
REPO = CASE_ROOT.parents[2]
CER_SOURCE = REPO / "shared/implementation/editor-shell/v1.0/cer.css"
RESULTS = CASE_ROOT / "validation-artifacts/CASE02_CER_HTML_VALIDATION_RESULTS.json"
TARGETS = {
    "master": CASE_ROOT / "master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html",
    "student": CASE_ROOT / "published/SSS_C1_CASE02_STUDENT_MISSION_v1.0.html",
    "grayscale": CASE_ROOT / "published/SSS_C1_CASE02_GRAYSCALE_MISSION_v1.0.html",
}
ACCESSIBLE = CASE_ROOT / "published/SSS_C1_CASE02_ACCESSIBLE_MISSION_v1.0.html"
HEADING_TARGETS = {
    **TARGETS,
    "teacher": CASE_ROOT / "published/SSS_C1_CASE02_TEACHER_PACKET_v1.0.html",
    "answer": CASE_ROOT / "published/SSS_C1_CASE02_ANSWER_KEY_v1.0.html",
    "accessible": ACCESSIBLE,
}
TASK_LABELS = {
    "1": "REFERENCE", "2": "PREDICTION", "3": "MECHANISM MODEL",
    "4": "CAUSE ANALYSIS", "5": "DIAGNOSIS", "6": "DIAGNOSIS",
    "7": "EXPLANATION", "8": "ENGINEERING RESPONSE", "9": "EXIT TICKET",
}
CASE01_MASTER = (
    REPO
    / "sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html"
)


def run(chrome: Path) -> dict[str, Any]:
    expected_css = CER_SOURCE.read_text(encoding="utf-8")
    expected_hash = hashlib.sha256(CER_SOURCE.read_bytes()).hexdigest()
    case01_css = CASE01_MASTER.read_text(encoding="utf-8")
    assertions: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: str = "") -> None:
        assertions.append({"name": name, "pass": bool(condition), "detail": detail})

    case01_geometry = {
        "Student CER minimum height": (
            ".student-conclusion-page .cer-stack { flex: 1 1 auto; min-height: 2.55in; }",
            "min-height: 2.55in",
        ),
        "CER vertical gap": ("gap:.055in", "gap: .055in"),
        "CER label column": ("grid-template-columns:.72in 1fr", "grid-template-columns: .72in"),
        "Claim flex basis": ("flex:1 1 .46in", "flex: 1 1 .46in"),
        "Evidence flex basis": ("flex:1 1 .66in", "flex: 1 1 .66in"),
        "Reasoning flex basis": ("flex:1 1 .76in", "flex: 1 1 .76in"),
    }
    for label, (case01_token, shared_token) in case01_geometry.items():
        check(
            f"shared {label} matches approved Case 01",
            case01_token in case01_css and shared_token in expected_css,
        )

    for label, path in TARGETS.items():
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        meta = soup.select_one('meta[name="sss-cer-component"]')
        style = soup.select_one("#sssCerComponentCss")
        pages = soup.select('.page[data-role="student"]')
        task7 = soup.select_one(
            '.page[data-page-id="student-03"] .task-heading[data-task-id="7"]'
        )
        cer = soup.select_one(
            '.page[data-page-id="student-03"] [data-cer-contract="student-v1.0"]'
        )
        check(f"{label} declares CER component 1.0", meta is not None and meta.get("content") == "1.0")
        check(f"{label} embeds shared CER CSS", style is not None)
        if style is not None:
            check(f"{label} CER hash exact", style.get("data-source-sha256") == expected_hash)
            check(f"{label} CER bytes exact", (style.string or "") == expected_css)
        check(f"{label} has three Student pages", len(pages) == 3, f"actual={len(pages)}")
        check(f"{label} places Task 7 on Student page 3", task7 is not None)
        check(f"{label} has canonical full-width CER", cer is not None)
        if cer is not None:
            labels = [node.get_text(" ", strip=True) for node in cer.select(".canonical-cer-label")]
            check(
                f"{label} CER labels are Claim Evidence Reasoning",
                labels == ["CLAIM", "EVIDENCE", "REASONING"],
                f"actual={labels}",
            )
            check(
                f"{label} CER retains three response identifiers",
                [
                    node.get("data-persist-id")
                    for node in cer.select("[data-response]")
                ]
                == [
                    "response-student-task7-claim",
                    "response-student-task7-evidence",
                    "response-student-task7-reasoning",
                ],
            )
        check(
            f"{label} footers identify three-page Student packet",
            [node.get_text(" ", strip=True) for node in pages[-1].select(".publication-footer span")]
            == ["Student Mission 3 of 3"],
        )

    accessible_soup = BeautifulSoup(ACCESSIBLE.read_text(encoding="utf-8"), "html.parser")
    check(
        "Accessible output remains five pages",
        len(accessible_soup.select('.page[data-role="accessible"]')) == 5,
    )
    check(
        "Accessible output does not adopt Student CER component",
        accessible_soup.select_one('meta[name="sss-cer-component"]') is None,
    )

    tracked_pdfs = subprocess.run(
        ["git", "ls-files", "*.pdf"], cwd=CASE_ROOT, check=True,
        capture_output=True, text=True,
    ).stdout.splitlines()
    pdf_drift = []
    for relative in tracked_pdfs:
        current = CASE_ROOT / relative
        baseline = subprocess.run(
            ["git", "show", f"HEAD:{current.relative_to(REPO).as_posix()}"],
            cwd=REPO, check=True, capture_output=True,
        ).stdout
        if current.read_bytes() != baseline:
            pdf_drift.append(relative)
    check(
        "all tracked Case 02 PDFs remain byte-identical to HEAD",
        not pdf_drift,
        str(pdf_drift),
    )

    for label, path in HEADING_TARGETS.items():
        heading_soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        headings = heading_soup.select(".task-heading[data-task-id]")
        check(
            f"{label} declares canonical task-heading standard",
            heading_soup.select_one('meta[name="sss-task-heading-standard"][content="1.0"]') is not None,
        )
        check(
            f"{label} has no duplicated TASK-number technical labels",
            all(not re.fullmatch(r"TASK\s*0?\d+", node.get_text(" ", strip=True), re.I)
                for node in heading_soup.select(".task-heading .technical-label")),
        )
        check(
            f"{label} task headings use the canonical semantic labels",
            all(
                heading.select_one(".technical-label") is not None
                and heading.select_one(".technical-label").get_text(" ", strip=True)
                == TASK_LABELS[heading.get("data-task-id")]
                for heading in headings
            ),
        )
        check(
            f"{label} task titles contain their number exactly once",
            all(
                (title := heading.select_one(".section-title")) is not None
                and title.get_text(" ", strip=True).startswith(f'{heading.get("data-task-id")} · ')
                and len(re.findall(rf'(?<!\d){heading.get("data-task-id")}(?!\d)', title.get_text(" ", strip=True))) == 1
                for heading in headings
            ),
        )

    dimensions: dict[str, dict[str, float]] = {}
    layout_dimensions: dict[str, dict[str, Any]] = {}
    overflow_counts: dict[str, int] = {}
    browser_errors: dict[str, list[str]] = {}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=str(chrome), headless=True)
        for label, path in TARGETS.items():
            context = browser.new_context(viewport={"width": 1440, "height": 1100})
            page = context.new_page()
            errors: list[str] = []
            page.on("pageerror", lambda error, bucket=errors: bucket.append(error.stack or str(error)))
            page.goto(path.resolve().as_uri(), wait_until="load")
            page.wait_for_timeout(300)
            browser_errors[label] = errors
            check(f"{label} loads without browser errors", not errors, "; ".join(errors))
            visible = page.locator('.page[data-role="student"]:visible').count()
            check(f"{label} shows three Student pages", visible == 3, f"actual={visible}")
            overflow = page.locator('.page[data-role="student"]:visible').evaluate_all(
                """pages => pages.filter(page => {
                  const frame = page.querySelector('.page-frame');
                  return frame.scrollHeight > frame.clientHeight + 2;
                }).length"""
            )
            overflow_counts[label] = overflow
            check(f"{label} has no Student HTML overflow", overflow == 0, f"actual={overflow}")
            dimensions[label] = page.locator(
                '.page[data-page-id="student-03"] [data-cer-contract="student-v1.0"]'
            ).evaluate(
                """node => {
                  const cer = node.getBoundingClientRect();
                  const content = node.closest('.content-area').getBoundingClientRect();
                  const boxes = [...node.querySelectorAll('.canonical-cer-box')].map(
                    box => box.getBoundingClientRect().height
                  );
                  return {width: cer.width, contentWidth: content.width, height: cer.height,
                    claim: boxes[0], evidence: boxes[1], reasoning: boxes[2]};
                }"""
            )
            check(
                f"{label} CER is full content width",
                dimensions[label]["width"] >= dimensions[label]["contentWidth"] - 2,
                f"cer={dimensions[label]['width']} content={dimensions[label]['contentWidth']}",
            )
            check(
                f"{label} CER meets shared minimum height",
                dimensions[label]["height"] >= 244,
                f"actual={dimensions[label]['height']}",
            )
            layout_dimensions[label] = page.evaluate(
                """() => {
                  const rect = selector => document.querySelector(selector).getBoundingClientRect();
                  const heights = selector => [...document.querySelectorAll(selector)].map(
                    node => node.getBoundingClientRect().height
                  );
                  const page2Content = rect('[data-page-id="student-02"] .content-area');
                  const page2Last = rect('[data-page-id="student-02"] .task6-row');
                  const page3Content = rect('[data-page-id="student-03"] .content-area');
                  const page3Last = rect('[data-page-id="student-03"] .task89-row');
                  const task8 = rect('[data-page-id="student-03"] [data-task-id="8"]');
                  const task8Section = document.querySelector(
                    '[data-page-id="student-03"] [data-task-id="8"]'
                  ).closest('section').getBoundingClientRect();
                  const task9Section = document.querySelector(
                    '[data-page-id="student-03"] [data-task-id="9"]'
                  ).closest('section').getBoundingClientRect();
                  return {
                    page2Reserve: page2Content.bottom - page2Last.bottom,
                    page3Reserve: page3Content.bottom - page3Last.bottom,
                    contentWidth: page3Content.width,
                    task8: {x: task8Section.x, y: task8Section.y,
                      width: task8Section.width, bottom: task8Section.bottom},
                    task9: {x: task9Section.x, y: task9Section.y,
                      width: task9Section.width, bottom: task9Section.bottom},
                    task4Heights: heights('[data-page-id="student-02"] .task4-block .response-area'),
                    task5Heights: heights('[data-page-id="student-02"] .task5-block .inline-response'),
                    task6Heights: heights('[data-page-id="student-02"] .task6-row .response-area'),
                    task8Heights: heights('[data-page-id="student-03"] [data-task-id="8"] ~ .design-grid .response-area'),
                    task9Heights: heights('[data-page-id="student-03"] [data-task-id="9"] ~ .response-block .response-area')
                  };
                }"""
            )
            layout = layout_dimensions[label]
            check(
                f"{label} Student page 2 converts lower-page surplus into writing space",
                40 <= layout["page2Reserve"] <= 180,
                str(layout["page2Reserve"]),
            )
            check(
                f"{label} Student page 3 retains a balanced lower-page reserve",
                40 <= layout["page3Reserve"] <= 180,
                str(layout["page3Reserve"]),
            )
            check(
                f"{label} Tasks 8 and 9 are stacked full-width",
                abs(layout["task8"]["x"] - layout["task9"]["x"]) <= 1
                and abs(layout["task8"]["width"] - layout["contentWidth"]) <= 2
                and abs(layout["task9"]["width"] - layout["contentWidth"]) <= 2
                and layout["task9"]["y"] >= layout["task8"]["bottom"] + 8,
                str({"task8": layout["task8"], "task9": layout["task9"]}),
            )
            check(
                f"{label} page 2 response fields meet expanded writing-space minimums",
                all(value >= 63 for value in layout["task4Heights"])
                and all(value >= 46 for value in layout["task5Heights"])
                and all(value >= 97 for value in layout["task6Heights"]),
                str({key: layout[key] for key in ("task4Heights", "task5Heights", "task6Heights")}),
            )
            context.close()

        for label, path in HEADING_TARGETS.items():
            context = browser.new_context(viewport={"width": 1440, "height": 1100})
            page = context.new_page()
            errors: list[str] = []
            page.on("pageerror", lambda error, bucket=errors: bucket.append(error.stack or str(error)))
            page.goto(path.resolve().as_uri(), wait_until="load")
            page.wait_for_timeout(150)
            check(f"{label} task-heading HTML opens without browser errors", not errors, "; ".join(errors))
            standard_sizes = page.locator('.task-heading .section-title').evaluate_all(
                "nodes => nodes.filter(n => !n.closest('[data-role=accessible]')).map(n => getComputedStyle(n).fontSize)"
            )
            accessible_sizes = page.locator('.page[data-role="accessible"] .task-heading .section-title').evaluate_all(
                "nodes => nodes.map(n => getComputedStyle(n).fontSize)"
            )
            check(
                f"{label} standard task titles render at 11.5pt",
                all(size in {"15.3333px", "15.333px"} for size in standard_sizes),
                str(standard_sizes),
            )
            check(
                f"{label} Accessible task titles render at canonical 14pt",
                all(size in {"18.6667px", "18.666px"} for size in accessible_sizes),
                str(accessible_sizes),
            )
            context.close()
        browser.close()

    baseline = dimensions["master"]
    for label in ("student", "grayscale"):
        check(
            f"{label} CER geometry matches master",
            all(abs(dimensions[label][key] - baseline[key]) <= 0.5 for key in baseline),
            f"master={baseline} actual={dimensions[label]}",
        )

    failures = [item for item in assertions if not item["pass"]]
    return {
        "validator": "case02-student-cer-html",
        "cerComponentVersion": "1.0",
        "pdfGeneration": "SKIPPED",
        "assertions": len(assertions),
        "passed": len(assertions) - len(failures),
        "failed": len(failures),
        "studentHtmlPageCounts": {label: 3 for label in TARGETS},
        "accessibleHtmlPageCount": 5,
        "overflowCounts": overflow_counts,
        "cerDimensions": dimensions,
        "layoutDimensions": layout_dimensions,
        "browserErrors": browser_errors,
        "failures": failures,
        "results": assertions,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--chrome",
        type=Path,
        default=Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    )
    parser.add_argument("--results", type=Path, default=RESULTS)
    args = parser.parse_args()
    result = run(args.chrome.resolve())
    args.results.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{result['passed']}/{result['assertions']} Case 02 CER HTML assertions passing")
    print(f"Student HTML page counts: {result['studentHtmlPageCounts']}")
    print(f"Accessible HTML page count: {result['accessibleHtmlPageCount']}")
    print(f"HTML overflow counts: {result['overflowCounts']}")
    print("PDF generation: skipped")
    for failure in result["failures"]:
        print(f"FAIL: {failure['name']} {failure['detail']}")
    return 1 if result["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
