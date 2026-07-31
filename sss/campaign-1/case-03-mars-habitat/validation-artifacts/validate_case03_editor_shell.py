#!/usr/bin/env python3
"""Browser assertions for the Case 03 shared-shell assembly and serializers."""
from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


CASE_ROOT = Path(__file__).resolve().parents[1]
REPO = CASE_ROOT.parents[2]
MASTER = CASE_ROOT / "master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html"
CONFIG = CASE_ROOT / "source/editor/case03-editor-config.json"
RESULTS = CASE_ROOT / "validation-artifacts/CASE03_EDITOR_SHELL_BROWSER_RESULTS.json"


def run(chrome: Path) -> dict[str, Any]:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    assertions: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: str = "") -> None:
        assertions.append({"name": name, "pass": bool(condition), "detail": detail})

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=str(chrome), headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 1100})
        page = context.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(error.stack or str(error)))
        page.goto(MASTER.resolve().as_uri(), wait_until="load")
        page.wait_for_timeout(250)

        check("master loads without JavaScript errors", not errors, "; ".join(errors))
        check(
            "runtime identifies shared shell 1.0",
            page.evaluate("window.SSSEditorShell?.shellVersion") == "1.0",
        )
        actual_controls = page.locator(".toolbar [id]").evaluate_all(
            "nodes => nodes.map(node => node.id)"
        )
        expected_controls = [
            "roleSelect", "fillToggle", "editToggle",
            "marginTop", "marginRight", "marginBottom", "marginLeft", "marginReset",
            "densitySelect", "grayToggle", "guidesToggle", "boundariesToggle",
            "printBtn", "downloadMasterBtn", "downloadRoleBtn", "clearRoleBtn", "resetSourceBtn",
            "localSaveStatus", "overflowStatus",
        ]
        check("browser toolbar order matches contract", actual_controls == expected_controls)
        check(
            "default Student view shows four pages",
            page.locator('.page[data-role="student"]:visible').count() == 4,
        )
        check(
            "nonselected roles are hidden",
            page.locator('.page[data-role]:visible').count() == 4,
        )

        page.locator("#editToggle").check()
        instruction_selector = '[data-persist-id="student-mission-01-instruction-018"]'
        response_selector = '[data-persist-id="t1"]'
        check(
            "Edit Text enables instructional content",
            page.locator(instruction_selector).get_attribute("contenteditable") == "true",
        )
        check(
            "Fill Responses enables response content",
            page.locator(response_selector).get_attribute("contenteditable") == "true",
        )
        edited_instruction = "SERIALIZATION TEST · edited instructional direction"
        edited_response = "SERIALIZATION TEST · student response"
        page.locator(instruction_selector).evaluate(
            "(node, value) => { node.innerHTML = value; node.dispatchEvent(new InputEvent('input', {bubbles:true})); }",
            edited_instruction,
        )
        page.locator(response_selector).evaluate(
            "(node, value) => { node.innerHTML = value; node.dispatchEvent(new InputEvent('input', {bubbles:true})); }",
            edited_response,
        )
        page.wait_for_timeout(250)
        check(
            "local autosave reaches saved state",
            "saved" in page.locator("#localSaveStatus").inner_text().lower(),
        )
        edited_master = page.evaluate("window.SSSEditorShell.serializeEditedMasterHTML()")
        check("edited-master serializer returns portable document", edited_master.startswith("<!doctype html>"))
        check("serialized master embeds instructional edit", edited_instruction in edited_master)
        check("serialized master embeds response edit", edited_response in edited_master)

        with tempfile.TemporaryDirectory(prefix="case03-shell-") as temp_dir:
            portable_path = Path(temp_dir) / "case03-edited-master.html"
            portable_path.write_text(edited_master, encoding="utf-8")
            fresh_context = browser.new_context(viewport={"width": 1440, "height": 1100})
            fresh_page = fresh_context.new_page()
            fresh_errors: list[str] = []
            fresh_page.on("pageerror", lambda error: fresh_errors.append(error.stack or str(error)))
            fresh_page.goto(portable_path.resolve().as_uri(), wait_until="load")
            fresh_page.wait_for_timeout(250)
            check("downloaded master opens in fresh storage without errors", not fresh_errors, "; ".join(fresh_errors))
            check(
                "instructional edit survives fresh empty storage",
                fresh_page.locator(instruction_selector).inner_text() == edited_instruction,
            )
            check(
                "response edit survives fresh empty storage",
                fresh_page.locator(response_selector).inner_text() == edited_response,
            )

            fresh_page.locator(instruction_selector).evaluate(
                "(node) => { node.innerHTML = 'temporary mutation'; node.dispatchEvent(new InputEvent('input', {bubbles:true})); }"
            )
            fresh_page.locator(response_selector).evaluate(
                "(node) => { node.innerHTML = 'temporary response'; node.dispatchEvent(new InputEvent('input', {bubbles:true})); }"
            )
            fresh_page.evaluate("window.SSSEditorShell.resetSource(true)")
            check(
                "Reset Source restores embedded edited instruction",
                fresh_page.locator(instruction_selector).inner_text() == edited_instruction,
            )
            check(
                "Reset Source restores embedded edited response",
                fresh_page.locator(response_selector).inner_text() == edited_response,
            )

            role_html = fresh_page.evaluate(
                "window.SSSEditorShell.serializeCurrentRoleHTML('student')"
            )
            role_soup = BeautifulSoup(role_html, "html.parser")
            role_pages = role_soup.select(".page[data-role]")
            check("role serializer removes authoring toolbar", role_soup.select_one(".toolbar") is None)
            check(
                "role serializer isolates Student pages",
                len(role_pages) == 4 and all(node.get("data-role") == "student" for node in role_pages),
            )
            check("role serializer retains instructional edit", edited_instruction in role_html)
            check("role serializer retains response edit", edited_response in role_html)
            check(
                "role serializer identifies standalone role",
                role_soup.select_one('meta[name="sss-standalone-role"][content="student"]') is not None,
            )
            fresh_context.close()

        expected_counts = {
            key: value
            for key, value in config["pageCounts"].items()
            if key != "grayscale"
        }
        actual_counts: dict[str, int] = {}
        overflow_counts: dict[str, int] = {}
        overflow_page_ids: dict[str, list[str]] = {}
        for role, expected in expected_counts.items():
            page.evaluate("(role) => window.SSSEditorShell.setRole(role)", role)
            page.wait_for_timeout(80)
            actual_counts[role] = page.locator(f'.page[data-role="{role}"]:visible').count()
            overflow_counts[role] = page.evaluate("window.SSSEditorShell.checkOverflow()")
            overflow_page_ids[role] = page.locator(
                f'.page[data-role="{role}"].has-overflow'
            ).evaluate_all("nodes => nodes.map(node => node.dataset.pageId)")
            check(f"{role} browser page count remains {expected}", actual_counts[role] == expected)
            check(
                f"{role} has no HTML page overflow",
                overflow_counts[role] == 0,
                f"actual={overflow_counts[role]} pages={overflow_page_ids[role]}",
            )

        standard_title_size = page.locator(
            '.page[data-role="student"] .task-heading .section-title'
        ).first.evaluate("node => getComputedStyle(node).fontSize")
        accessible_title_size = page.locator(
            '.page[data-role="accessible"] .task-heading .section-title'
        ).first.evaluate("node => getComputedStyle(node).fontSize")
        icon_size = page.locator(
            '.page[data-role="student"] .task-heading .ph-icon'
        ).first.evaluate("node => getComputedStyle(node).width")
        check("standard task title computes to 11.5pt", standard_title_size in {"15.3333px", "15.333px"})
        check("accessible task title computes to 14pt", accessible_title_size in {"18.6667px", "18.666px"})
        check("standard task icon computes to 20px", icon_size == "20px")
        check(
            "Task 7 uses canonical CER title",
            page.locator('.task-heading[data-task-id="7"] .section-title').first.inner_text()
            == "7 · Claim-Evidence-Reasoning",
        )
        check(
            "task headings contain their number once",
            page.locator(".task-heading .section-title").evaluate_all(
                "nodes => nodes.every(node => { const n = node.textContent.trim().split(' · ')[0]; return node.textContent.split(n).length - 1 === 1; })"
            ),
        )
        browser.close()

    failures = [item for item in assertions if not item["pass"]]
    return {
        "validator": "case03-editor-shell-browser",
        "shellVersion": "1.0",
        "browser": str(chrome),
        "assertions": len(assertions),
        "passed": len(assertions) - len(failures),
        "failed": len(failures),
        "pageCounts": actual_counts,
        "overflowCounts": overflow_counts,
        "overflowPageIds": overflow_page_ids,
        "serialization": {
            "instructionalEditPersisted": edited_instruction in edited_master,
            "responseEditPersisted": edited_response in edited_master,
            "freshStorageVerified": not any(
                item["name"].endswith("survives fresh empty storage") and not item["pass"]
                for item in assertions
            ),
            "resetRestoredEmbeddedEditedSource": not any(
                item["name"].startswith("Reset Source") and not item["pass"]
                for item in assertions
            ),
        },
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
    print(f"{result['passed']}/{result['assertions']} Case 03 browser assertions passing")
    print(f"HTML page counts: {result['pageCounts']}")
    print(f"HTML overflow counts: {result['overflowCounts']}")
    for failure in result["failures"]:
        print(f"FAIL: {failure['name']} {failure['detail']}")
    return 1 if result["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
