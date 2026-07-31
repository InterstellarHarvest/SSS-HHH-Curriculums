#!/usr/bin/env python3
"""Validate Case 01 v1.1 canonical task headings without producing PDFs."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


CASE_ROOT = Path(__file__).resolve().parents[1]
REPO = CASE_ROOT.parents[2]
MASTER = CASE_ROOT / "master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html"
HISTORICAL = CASE_ROOT / "master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html"
RESULTS = CASE_ROOT / "validation-artifacts/v1.1/CASE01_HTML_MAINTENANCE_RESULTS.json"
OUTPUTS = {
    "student": (CASE_ROOT / "published/v1.1/SSS_C1_CASE01_STUDENT_MISSION_v1.1.html", 3),
    "teacher": (CASE_ROOT / "published/v1.1/SSS_C1_CASE01_TEACHER_GUIDE_v1.1.html", 7),
    "answer": (CASE_ROOT / "published/v1.1/SSS_C1_CASE01_ANSWER_KEY_v1.1.html", 3),
    "accessible": (CASE_ROOT / "published/v1.1/SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.1.html", 6),
    "grayscale": (CASE_ROOT / "published/v1.1/SSS_C1_CASE01_GRAYSCALE_MISSION_v1.1.html", 3),
}


def head_bytes(path: Path) -> bytes:
    relative = path.relative_to(REPO).as_posix()
    return subprocess.run(
        ["git", "show", f"HEAD:{relative}"], cwd=REPO, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout


def run(chrome: Path) -> dict[str, Any]:
    assertions: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: Any = "") -> None:
        assertions.append({"name": name, "pass": bool(condition), "detail": str(detail)})

    master = BeautifulSoup(MASTER.read_text(encoding="utf-8"), "html.parser")
    headings = master.select(".task-heading[data-task-id]")
    check("Case 01 v1.0 historical master remains byte-identical", HISTORICAL.read_bytes() == head_bytes(HISTORICAL))
    tracked = subprocess.run(
        ["git", "ls-files", "*.pdf"], cwd=REPO, check=True,
        stdout=subprocess.PIPE, text=True,
    ).stdout.splitlines()
    pdfs = sorted(
        REPO / relative for relative in tracked
        if (REPO / relative).is_relative_to(CASE_ROOT)
    )
    check("all existing Case 01 PDFs remain byte-identical", bool(pdfs) and all(path.read_bytes() == head_bytes(path) for path in pdfs), len(pdfs))
    check("v1.1 master declares task-heading standard 1.0", master.select_one('meta[name="sss-task-heading-standard"][content="1.0"]') is not None)
    check("v1.1 master marks all numbered section headings as task headings", len(headings) == 27, len(headings))
    check("task titles retain one visible number and title", all(node.select_one(".section-title").get_text(" ", strip=True).startswith(f'{node.get("data-task-id")} · ') for node in headings))

    output_counts: dict[str, int] = {}
    overflow_counts: dict[str, int] = {}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=str(chrome), headless=True, args=["--no-sandbox"])
        for role, (path, expected_pages) in {"master": (MASTER, 0), **OUTPUTS}.items():
            page = browser.new_page(viewport={"width": 1440, "height": 1200})
            errors: list[str] = []
            page.on("pageerror", lambda error, bucket=errors: bucket.append(str(error)))
            page.goto(path.resolve().as_uri(), wait_until="load")
            page.wait_for_timeout(250)
            check(f"{role} HTML opens without JavaScript errors", not errors, errors)
            standard_sizes = page.locator('.task-heading .section-title').evaluate_all(
                "nodes => nodes.filter(n => !n.closest('.accessible-page')).map(n => getComputedStyle(n).fontSize)"
            )
            accessible_sizes = page.locator('.accessible-page .task-heading .section-title').evaluate_all(
                "nodes => nodes.map(n => getComputedStyle(n).fontSize)"
            )
            check(f"{role} standard task titles render at 11.5pt", all(value in {"15.3333px", "15.333px"} for value in standard_sizes), standard_sizes)
            check(f"{role} Accessible task titles render at 14pt", all(value in {"18.6667px", "18.666px"} for value in accessible_sizes), accessible_sizes)
            if role != "master":
                pages = page.locator("section.page")
                output_counts[role] = pages.count()
                overflow = pages.evaluate_all("nodes => nodes.filter(n => n.scrollHeight > n.clientHeight + 2).length")
                overflow_counts[role] = overflow
                check(f"{role} HTML page count remains {expected_pages}", pages.count() == expected_pages, pages.count())
                check(f"{role} HTML has zero overflow", overflow == 0, overflow)
            page.close()
        browser.close()

    failures = [item for item in assertions if not item["pass"]]
    return {
        "validator": "case01-html-task-heading-maintenance",
        "pdfGeneration": "SKIPPED",
        "assertions": len(assertions),
        "passed": len(assertions) - len(failures),
        "failed": len(failures),
        "pageCounts": output_counts,
        "overflowCounts": overflow_counts,
        "failures": failures,
        "results": assertions,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chrome", type=Path, default=Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    parser.add_argument("--results", type=Path, default=RESULTS)
    args = parser.parse_args()
    result = run(args.chrome.resolve())
    args.results.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{result['passed']}/{result['assertions']} Case 01 HTML maintenance assertions passing")
    print(f"HTML page counts: {result['pageCounts']}")
    print(f"HTML overflow counts: {result['overflowCounts']}")
    print("PDF generation: skipped")
    for failure in result["failures"]:
        print(f"FAIL: {failure['name']} {failure['detail']}")
    return 1 if result["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
