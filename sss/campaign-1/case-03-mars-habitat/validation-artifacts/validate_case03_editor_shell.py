#!/usr/bin/env python3
"""Rendered-browser assertions for the Case 03 Case-02 editor contract."""
from __future__ import annotations

import argparse
import json
import re
import tempfile
from pathlib import Path
from typing import Any

from playwright.sync_api import sync_playwright


CASE_ROOT = Path(__file__).resolve().parents[1]
REPO = CASE_ROOT.parents[2]
MASTER = CASE_ROOT / "master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html"
CASE02 = REPO / "sss/campaign-1/case-02-lunar-greenhouse/master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html"
CONFIG = CASE_ROOT / "source/editor/case03-editor-config.json"
RESULTS = CASE_ROOT / "validation-artifacts/CASE03_EDITOR_SHELL_BROWSER_RESULTS.json"
PUBLISHED = CASE_ROOT / "published"


def run(chrome: Path) -> dict[str, Any]:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    assertions: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: Any = "") -> None:
        assertions.append({"name": name, "pass": bool(condition), "detail": str(detail)})

    expected_controls = [
        "roleControl", "fillControl", "editControl",
        "marginTop", "marginRight", "marginBottom", "marginLeft", "marginReset",
        "densityControl", "grayControl", "guideControl", "boundaryControl",
        "printButton", "downloadButton", "clearButton", "resetButton",
        "stateStatus", "overflowStatus",
    ]
    toolbar_style_properties = [
        "position", "left", "right", "top", "display", "align-items", "gap",
        "padding-top", "padding-right", "padding-bottom", "padding-left",
        "background-color", "color", "font-family", "font-size", "line-height",
        "border-bottom-width", "border-bottom-style", "border-bottom-color", "z-index",
    ]
    child_style_properties = [
        "display", "align-items", "gap", "height", "padding-top", "padding-right",
        "padding-bottom", "padding-left", "margin-top", "margin-right", "margin-bottom",
        "margin-left", "font-family", "font-size", "font-weight", "line-height",
        "border-top-width", "border-right-width", "border-bottom-width", "border-left-width",
        "border-radius", "background-color", "color",
    ]

    def dom_signature(page, selector: str) -> Any:
        return page.locator(selector).first.evaluate(
            """node => {
              const walk = n => {
                if (n.nodeType === Node.TEXT_NODE) {
                  const text = n.textContent.replace(/\s+/g, ' ').trim();
                  return text ? {text} : null;
                }
                if (n.nodeType !== Node.ELEMENT_NODE) return null;
                return {
                  tag: n.tagName.toLowerCase(),
                  attrs: Array.from(n.attributes).map(a => [a.name, a.value]).sort(),
                  children: Array.from(n.childNodes).map(walk).filter(Boolean)
                };
              };
              return walk(node);
            }"""
        )

    def style_map(page, selector: str, properties: list[str]) -> Any:
        return page.locator(selector).first.evaluate(
            "(node, props) => Object.fromEntries(props.map(p => [p, getComputedStyle(node).getPropertyValue(p)]))",
            properties,
        )

    def geometry(page, selector: str) -> Any:
        return page.locator(selector).first.evaluate(
            """node => { const r=node.getBoundingClientRect(); return {
              x:+r.x.toFixed(2), y:+r.y.toFixed(2), width:+r.width.toFixed(2), height:+r.height.toFixed(2)
            }; }"""
        )

    def same_dimensions(left: Any, right: Any, tolerance: float = 0.6) -> bool:
        return all(abs(left[key] - right[key]) <= tolerance for key in ("width", "height"))

    actual_counts: dict[str, int] = {}
    overflow_counts: dict[str, int] = {}
    bottom_reserves: dict[str, dict[str, float]] = {}
    standalone_results: dict[str, Any] = {}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path=str(chrome), headless=True, args=["--no-sandbox"]
        )
        context = browser.new_context(viewport={"width": 1440, "height": 1200})
        case02 = context.new_page()
        case03 = context.new_page()
        case02_errors: list[str] = []
        case03_errors: list[str] = []
        case02.on("pageerror", lambda error: case02_errors.append(str(error)))
        case03.on("pageerror", lambda error: case03_errors.append(str(error)))
        case02.goto(CASE02.resolve().as_uri(), wait_until="load")
        case03.goto(MASTER.resolve().as_uri(), wait_until="load")
        case02.wait_for_timeout(300)
        case03.wait_for_timeout(300)

        check("Case 02 literal reference loads without JavaScript errors", not case02_errors, case02_errors)
        check("Case 03 master loads without JavaScript errors", not case03_errors, case03_errors)
        check("Case 03 exposes the Case 02 runtime API", bool(case03.evaluate("window.__case03")))
        check("Case 02 and Case 03 toolbar DOM contracts are identical", dom_signature(case02, ".toolbar") == dom_signature(case03, ".toolbar"))
        controls02 = case02.locator(".toolbar [id]").evaluate_all("nodes => nodes.map(n => n.id)")
        controls03 = case03.locator(".toolbar [id]").evaluate_all("nodes => nodes.map(n => n.id)")
        check("Case 02 toolbar control order is the approved order", controls02 == expected_controls, controls02)
        check("Case 03 toolbar control order exactly matches Case 02", controls03 == controls02, controls03)
        check("Case 02 and Case 03 toolbar labels are identical", case02.locator(".toolbar").inner_text() == case03.locator(".toolbar").inner_text())
        check("Case 02 and Case 03 toolbar computed CSS is identical", style_map(case02, ".toolbar", toolbar_style_properties) == style_map(case03, ".toolbar", toolbar_style_properties))
        for selector in [".toolbar-group:first-child", "#roleControl", "#marginTop", "#printButton", "#resetButton", ".toolbar-status"]:
            check(
                f"Case 02 and Case 03 {selector} sizing and spacing match",
                style_map(case02, selector, child_style_properties) == style_map(case03, selector, child_style_properties)
                and same_dimensions(geometry(case02, selector), geometry(case03, selector)),
                {"case02": geometry(case02, selector), "case03": geometry(case03, selector)},
            )

        # Literal Case 02 toolbar behavior and portable serialization.
        check("default Student view shows four pages", case03.locator('.page[data-role="student"]:visible').count() == 4)
        check("default view hides non-Student roles", case03.locator(".page:visible").count() == 4)
        check("Fill responses is enabled by default", case03.locator("#fillControl").is_checked())
        instruction_selector = '[data-persist-id="student-mission-01-instruction-018"]'
        response_selector = '[data-persist-id="t1"]'
        check("Fill responses enables Student response fields", case03.locator(response_selector).get_attribute("contenteditable") == "true")
        case03.locator("#editControl").check()
        check("Edit text enables instructional content", case03.locator(instruction_selector).get_attribute("contenteditable") == "true")
        edited_instruction = "SERIALIZATION TEST · edited instructional direction"
        edited_response = "SERIALIZATION TEST · student response"
        for selector, value in [(instruction_selector, edited_instruction), (response_selector, edited_response)]:
            case03.locator(selector).evaluate(
                "(node, value) => { node.innerHTML=value; node.dispatchEvent(new InputEvent('input',{bubbles:true})); }",
                value,
            )
        case03.wait_for_timeout(150)
        check("local autosave reaches saved state", "saved" in case03.locator("#stateStatus").inner_text().lower())
        portable = case03.evaluate("window.__case03.serializePortableHTML()")
        check("portable serializer returns a complete HTML document", portable.lower().startswith("<!doctype html>"))
        check("portable serializer embeds instructional edits", edited_instruction in portable)
        check("portable serializer embeds response edits", edited_response in portable)
        with tempfile.TemporaryDirectory(prefix="case03-shell-") as temp_dir:
            portable_path = Path(temp_dir) / "case03-portable.html"
            portable_path.write_text(portable, encoding="utf-8")
            fresh = browser.new_context(viewport={"width": 1440, "height": 1200}).new_page()
            fresh_errors: list[str] = []
            fresh.on("pageerror", lambda error: fresh_errors.append(str(error)))
            fresh.goto(portable_path.resolve().as_uri(), wait_until="load")
            fresh.wait_for_timeout(200)
            check("portable master opens in fresh browser storage", not fresh_errors, fresh_errors)
            check("instructional edit survives fresh storage", fresh.locator(instruction_selector).inner_text() == edited_instruction)
            check("response edit survives fresh storage", fresh.locator(response_selector).inner_text() == edited_response)
            fresh.evaluate("window.__case03.resetSource(true)")
            check("Reset Source clears response content", fresh.locator(response_selector).inner_text() == "")
            check("Reset Source preserves the portable file's embedded instructional source", fresh.locator(instruction_selector).inner_text() == edited_instruction)
            fresh.context.close()

        # Approved printable worksheet identity from Case 02.
        for selector in [
            '.page[data-role="student"] .student-id',
            '.page[data-role="student"] .student-id label:nth-child(1)',
            '.page[data-role="student"] .student-id label:nth-child(2)',
            '.page[data-role="student"] .student-id label:nth-child(3)',
        ]:
            left, right = geometry(case02, selector), geometry(case03, selector)
            check(f"Case 03 {selector} geometry matches Case 02", same_dimensions(left, right), {"case02": left, "case03": right})
        for selector in [
            '.page[data-role="student"] .mission-title-block',
            '.page[data-role="student"] .mission-rail',
            '.page[data-role="student"] .mission-title-block .saa-insignia',
            '.page[data-role="student"] .mission-title-block .identity-mark',
            '.page[data-role="student"] .continuation-header',
            '.page[data-role="student"] .continuation-header .saa-insignia',
        ]:
            left, right = geometry(case02, selector), geometry(case03, selector)
            check(f"Case 03 {selector} geometry matches Case 02", same_dimensions(left, right), {"case02": left, "case03": right})
        case02_logo = [style_map(case02, f'.page[data-role="student"] .mission-title-block .{name}', ["fill"]) for name in ["ins-sun", "ins-leaf", "ins-leaf2", "ins-ring", "ins-planet", "ins-orbit"]]
        case03_logo = [style_map(case03, f'.page[data-role="student"] .mission-title-block .{name}', ["fill"]) for name in ["ins-sun", "ins-leaf", "ins-leaf2", "ins-ring", "ins-planet", "ins-orbit"]]
        check("Case 03 color insignia palette exactly matches Case 02", case03_logo == case02_logo, case03_logo)
        check(
            "Case 03 institution lockup exactly reads Solar Agricultural Agency",
            case03.locator(".mission-title-block .institution").first.evaluate(
                "n => Array.from(n.querySelectorAll('span')).map(x => x.textContent.trim())"
            ) == ["Solar", "Agricultural", "Agency"],
        )

        # Component-layout handoff and corrected heading contract.
        heading_data = case03.locator(".task-heading").evaluate_all(
            """nodes => nodes.map(n => ({id:n.dataset.taskId, title:n.querySelector('.section-title')?.textContent.trim(),
              label:n.querySelector('.technical-label')?.textContent.trim(), icons:n.querySelectorAll('svg.ph-icon use').length}))"""
        )
        check("every task heading contains exactly one Phosphor icon", bool(heading_data) and all(item["icons"] == 1 for item in heading_data))
        check("no task heading uses a TASK label", all(not re.fullmatch(r"TASK\s*0?\d+", item["label"], re.I) for item in heading_data))
        check("every task title contains its task number exactly once", all(item["title"].startswith(f'{item["id"]} · ') and len(re.findall(rf'(?<!\d){re.escape(item["id"])}(?!\d)', item["title"])) == 1 for item in heading_data))
        task7 = [item for item in heading_data if item["id"] == "7"]
        check("Task 7 is EXPLANATION then 7 · Claim-Evidence-Reasoning everywhere", bool(task7) and all(item["label"] == "EXPLANATION" and item["title"] == "7 · Claim-Evidence-Reasoning" for item in task7), task7)
        standard_size = case03.locator('.page[data-role="student"] .task-heading .section-title').first.evaluate("n => getComputedStyle(n).fontSize")
        reference_size = case02.locator('.page[data-role="student"] .task-heading .section-title').first.evaluate("n => getComputedStyle(n).fontSize")
        check("Case 03 task-title font size matches Case 02", standard_size == reference_size, {"case02": reference_size, "case03": standard_size})
        check("Teacher direct Task 7 reference is canonical", case03.locator('.page[data-role="teacher"]').evaluate_all("nodes => nodes.some(n => n.innerText.includes('7 · Claim-Evidence-Reasoning'))"))
        check("Teacher direct task references do not use Task N hyphen labels", not re.search(r"\bTask\s+\d+\s*[-:]", " ".join(case03.locator('.page[data-role="teacher"]').all_inner_texts()), re.I))

        spectra = case03.locator('[data-quantity-spectrum="canonical-v1.0"]').evaluate_all(
            """svgs => svgs.map(svg => ({labels:svg.querySelectorAll('[data-spectrum-label-column] text').length,
              tracks:Array.from(svg.querySelectorAll('[data-spectrum-track]')).map(n=>({x:+n.getAttribute('x'),w:+n.getAttribute('width')})),
              bars:Array.from(svg.querySelectorAll('[data-spectrum-bar]')).map(n=>({x:+n.getAttribute('x'),w:+n.getAttribute('width'),p:+n.dataset.percent})),
              values:Array.from(svg.querySelectorAll('[data-spectrum-value]')).map(n=>({x:+n.getAttribute('x'),v:n.textContent.trim()}))}))"""
        )
        check("Task 3 quantity/spectrum graphic exists in Student, Answer Key, and Accessible", len(spectra) == 3)
        check("Task 3 labels, tracks, and values use independent columns without overlap", all(s["labels"] == 4 and len(s["tracks"]) == len(s["bars"]) == len(s["values"]) == 4 and all(b["x"] == t["x"] and b["w"] <= t["w"] and v["x"] > t["x"] + t["w"] for t, b, v in zip(s["tracks"], s["bars"], s["values"])) for s in spectra), spectra)
        check("Task 3 displays the four exact game values", all([v["v"] for v in s["values"]] == ["92%", "88%", "31%", "12%"] for s in spectra))

        process_data = case03.locator('[data-process-contract="five-stage-v1.0"]').evaluate_all(
            """nodes => nodes.map(n => ({layout:n.dataset.processLayout||'horizontal',
              stages:Array.from(n.querySelectorAll('[data-process-stage]')).map(s=>{const r=s.getBoundingClientRect();return {n:s.dataset.processStage,x:r.x,y:r.y,w:r.width,h:r.height}}),
              arrows:Array.from(n.querySelectorAll('[data-process-connector]')).map(a=>{const r=a.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height}})}))"""
        )
        check("Task 6 uses four canonical five-stage process models", len(process_data) == 4)
        check("every Task 6 model has stages 1–5 and four connectors", all([s["n"] for s in p["stages"]] == ["1", "2", "3", "4", "5"] and len(p["arrows"]) == 4 for p in process_data))
        # Hidden roles have zero rectangles; inspect each role after switching below for rendered geometry.

        expected_counts = {key: value for key, value in config["pageCounts"].items() if key != "grayscale"}
        for role, expected in expected_counts.items():
            case03.evaluate("role => window.__case03.setRole(role)", role)
            case03.wait_for_timeout(100)
            actual_counts[role] = case03.locator(f'.page[data-role="{role}"]:visible').count()
            overflow_counts[role] = case03.evaluate("window.__case03.checkOverflow()")
            check(f"{role} browser page count remains {expected}", actual_counts[role] == expected, actual_counts[role])
            check(f"{role} has no screen overflow", overflow_counts[role] == 0, overflow_counts[role])
            for index in range(case03.locator(f'.page[data-role="{role}"] [data-process-contract]').count()):
                model = case03.locator(f'.page[data-role="{role}"] [data-process-contract]').nth(index)
                stage_boxes = model.locator("[data-process-stage]").evaluate_all("nodes => nodes.map(n=>n.getBoundingClientRect()).map(r=>({x:r.x,y:r.y,w:r.width,h:r.height,right:r.right,bottom:r.bottom}))")
                arrow_boxes = model.locator("[data-process-connector]").evaluate_all("nodes => nodes.map(n=>n.getBoundingClientRect()).map(r=>({x:r.x,y:r.y,w:r.width,h:r.height,right:r.right,bottom:r.bottom}))")
                if role == "accessible":
                    aligned = max(b["x"] for b in stage_boxes) - min(b["x"] for b in stage_boxes) < 1 and max(b["w"] for b in stage_boxes) - min(b["w"] for b in stage_boxes) < 1
                    ordered = all(stage_boxes[i]["bottom"] <= stage_boxes[i + 1]["y"] for i in range(4))
                    check("Accessible Task 6 is a vertically aligned five-stage sequence", aligned and ordered, stage_boxes)
                else:
                    same_row = max(b["y"] for b in stage_boxes) - min(b["y"] for b in stage_boxes) < 1
                    equal_width = max(b["w"] for b in stage_boxes) - min(b["w"] for b in stage_boxes) < 1
                    ordered = all(stage_boxes[i]["right"] <= arrow_boxes[i]["x"] and arrow_boxes[i]["right"] <= stage_boxes[i + 1]["x"] for i in range(4))
                    check(f"{role} Task 6 keeps Stage 5 on the same row with attached connectors", same_row and equal_width and ordered, {"stages": stage_boxes, "arrows": arrow_boxes})

        for role in ["student", "accessible"]:
            case03.evaluate("role => window.__case03.setRole(role)", role)
            case03.wait_for_timeout(80)
            reserves = case03.locator(f'.page[data-role="{role}"]').evaluate_all(
                """pages => Object.fromEntries(pages.map(page => {
                  const content = page.querySelector('.content-area');
                  const children = Array.from(content.children);
                  const reserve = content.getBoundingClientRect().bottom - children.at(-1).getBoundingClientRect().bottom;
                  return [page.dataset.pageId, +reserve.toFixed(1)];
                }))"""
            )
            bottom_reserves[role] = reserves
            check(
                f"{role} pages use surplus height while preserving intentional bottom reserve",
                all(40 <= value <= 180 for value in reserves.values()),
                reserves,
            )

        text_student_accessible = " ".join(case03.locator('.page[data-role="student"], .page[data-role="accessible"]').all_inner_texts())
        check("PPFD first-use wording and compact definition are present", "PPFD: 280 µmol/m²/s — rated adequate." in text_student_accessible and "PPFD measures how many photosynthetically useful light photons reach each square meter each second." in text_student_accessible)
        check("obsolete PPFD unit spellings are absent", not re.search(r"umol\s*m-2\s*s-1|micromoles?\s+per\s+square\s+meter", text_student_accessible, re.I))
        check("Student and Accessible production pages omit removed science-boundary boxes", all(term not in text_student_accessible.upper() for term in ["SCIENCE BOUNDARY", "SOURCE STATUS", "GAME-PROVIDED COMPARISON", "TRANSPARENT ARITHMETIC"]))
        extensions = case03.locator('[data-optional-extension="canonical-v1.0"]')
        check("Student and Accessible each contain one optional extension", extensions.count() == 2)
        check("optional extensions follow Task 9 on the final required page", extensions.evaluate_all("nodes => nodes.every(n => n.closest('.page').querySelector('[data-task-id=\"9\"]') && !n.nextElementSibling)"))

        case03.emulate_media(media="print")
        check("toolbar is hidden in browser print preview", case03.locator(".toolbar").evaluate("n => getComputedStyle(n).display") == "none")
        for role, expected in expected_counts.items():
            case03.evaluate("role => window.__case03.setRole(role)", role)
            case03.wait_for_timeout(60)
            check(f"{role} print preview retains {expected} pages", case03.locator(f'.page[data-role="{role}"]:visible').count() == expected)
            check(f"{role} print preview has no flagged overflow", case03.locator(f'.page[data-role="{role}"].has-overflow').count() == 0)
        case03.emulate_media(media="screen")

        # Open every regenerated standalone role artifact in a real browser.
        for role in ["student", "teacher", "answer", "accessible", "grayscale"]:
            standalone = context.new_page()
            errors: list[str] = []
            standalone.on("pageerror", lambda error, errors=errors: errors.append(str(error)))
            standalone.goto((PUBLISHED / config["outputs"][role]["filename"]).resolve().as_uri(), wait_until="load")
            standalone.wait_for_timeout(150)
            expected = config["pageCounts"][role]
            pages = standalone.locator("section.page").count()
            visible_pages = standalone.locator("section.page:visible").count()
            overflow = standalone.locator("section.page.has-overflow").count()
            standalone_results[role] = {"pages": pages, "visiblePages": visible_pages, "overflow": overflow, "javascriptErrors": errors}
            check(f"{role} standalone HTML opens visibly with the expected pages", pages == visible_pages == expected, standalone_results[role])
            check(f"{role} standalone HTML opens without JavaScript errors or overflow", not errors and overflow == 0, standalone_results[role])
            check(f"{role} standalone HTML has no authoring toolbar", standalone.locator(".toolbar").count() == 0)
            standalone.close()
        browser.close()

    failures = [item for item in assertions if not item["pass"]]
    return {
        "validator": "case03-editor-shell-browser",
        "shellVersion": "1.0",
        "literalReference": str(CASE02.relative_to(REPO)),
        "browser": str(chrome),
        "assertions": len(assertions),
        "passed": len(assertions) - len(failures),
        "failed": len(failures),
        "pageCounts": actual_counts,
        "overflowCounts": overflow_counts,
        "bottomReservesPx": bottom_reserves,
        "standaloneOpenResults": standalone_results,
        "serialization": {
            "instructionalEditPersisted": edited_instruction in portable,
            "responseEditPersisted": edited_response in portable,
            "freshStorageVerified": not any("survives fresh storage" in item["name"] and not item["pass"] for item in assertions),
        },
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
    print(f"{result['passed']}/{result['assertions']} Case 03 browser assertions passing")
    print(f"HTML page counts: {result['pageCounts']}")
    print(f"HTML overflow counts: {result['overflowCounts']}")
    for failure in result["failures"]:
        print(f"FAIL: {failure['name']} {failure['detail']}")
    return 1 if result["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
