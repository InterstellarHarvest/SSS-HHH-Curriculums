#!/usr/bin/env python3
"""Compare Case 03 v1.1 master, isolated editor, and role exports page by page."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageDraw
from playwright.sync_api import Locator, sync_playwright


APP = Path(__file__).resolve().parents[1]
REPO = APP.parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(APP))
from serve import CurriculumEditorHandler  # noqa: E402

MASTER_PATH = "sss/campaign-1/case-03-mars-habitat/master/SSS_C1_CASE03_EDITABLE_MASTER_v1.1.html"
RESULTS = APP / "tests/parity-v1.1-results.json"
SCREENSHOTS = APP / "tests/screenshots/parity-v1.1"
ROLES = {"student": 4, "teacher": 8, "answer": 4, "accessible": 7, "grayscale": 4}
ROLE_FILES = {
    "student": "SSS_C1_CASE03_STUDENT_MISSION_v1.1.html",
    "teacher": "SSS_C1_CASE03_TEACHER_GUIDE_v1.1.html",
    "answer": "SSS_C1_CASE03_ANSWER_KEY_v1.1.html",
    "accessible": "SSS_C1_CASE03_ACCESSIBLE_MISSION_v1.1.html",
    "grayscale": "SSS_C1_CASE03_GRAYSCALE_MISSION_v1.1.html",
}
GEOMETRY_TOLERANCE = 0.25
PIXEL_DELTA_THRESHOLD = 8
# At most 0.05% of page pixels may differ after ignoring channel deltas <= 8.
# This covers SVG edge antialiasing without permitting visible layout drift.
PIXEL_RATIO_TOLERANCE = 0.0005

SNAPSHOT_SCRIPT = """
(page) => {
  const relativeRect = node => {
    const outer = page.getBoundingClientRect();
    const rect = node.getBoundingClientRect();
    const round = value => Math.round(value * 1000) / 1000;
    return {x: round(rect.x - outer.x), y: round(rect.y - outer.y), width: round(rect.width), height: round(rect.height), right: round(rect.right - outer.x), bottom: round(rect.bottom - outer.y)};
  };
  const groups = [
    ["page", ":scope"], ["frame", ":scope > .page-frame"], ["header", ".mission-title-block,.continuation-header"],
    ["footer", "[data-publication-footer]"], ["task", ".task-heading"], ["response", "[data-response]"],
    ["figure", "figure"], ["table", "table"], ["cer", "[data-cer-contract]"],
    ["cer-row", ".canonical-cer-box"], ["process", "[data-process-contract]"],
    ["phrase-bank", "[data-phrase-bank-contract]"], ["phrase-item", ".canonical-phrase-bank-item"],
    ["optional", "[data-optional-extension]"], ["choices", ".choice-list"]
  ];
  const geometry = {};
  const presentation = {};
  const properties = ["display","visibility","fontFamily","fontSize","lineHeight","marginTop","marginRight","marginBottom","marginLeft","paddingTop","paddingRight","paddingBottom","paddingLeft","borderTopWidth","borderRightWidth","borderBottomWidth","borderLeftWidth","gridTemplateColumns","gridTemplateRows","flexDirection","gap","backgroundColor","color","breakInside"];
  for (const [kind, selector] of groups) {
    const nodes = selector === ":scope" ? [page] : Array.from(page.querySelectorAll(selector));
    nodes.forEach((node, index) => {
      const identity = node.dataset.persistId || node.dataset.taskId || node.dataset.cerContract || node.dataset.processContract || node.dataset.phraseBankContract || node.dataset.pageId || index;
      const key = `${kind}:${identity}:${index}`;
      geometry[key] = relativeRect(node);
      const style = getComputedStyle(node);
      presentation[key] = Object.fromEntries(properties.map(property => [property, style[property]]));
    });
  }
  const orderSelector = ".task-heading,[data-cer-contract],[data-process-contract],[data-phrase-bank-contract],figure,table,[data-optional-extension],[data-response]";
  const structure = {
    pageId: page.dataset.pageId,
    role: page.dataset.role,
    ariaLabel: page.getAttribute("aria-label"),
    header: Array.from(page.querySelectorAll("[data-header-contract]")).map(node => [node.dataset.headerContract, node.dataset.pageIdentity]),
    footer: page.querySelector("[data-publication-footer]")?.textContent.trim(),
    tasks: Array.from(page.querySelectorAll(".task-heading")).map(node => [node.dataset.taskId, node.dataset.taskTitle, node.querySelector(".section-title")?.textContent.trim()]),
    responses: Array.from(page.querySelectorAll("[data-response]")).map(node => [node.dataset.persistId, node.getAttribute("aria-label"), node.className]),
    cers: Array.from(page.querySelectorAll("[data-cer-contract]")).map(root => ({contract: root.dataset.cerContract, rows: Array.from(root.querySelectorAll(":scope > .canonical-cer-box")).map(row => [row.className, row.querySelector(".canonical-cer-label")?.textContent.trim(), row.querySelector("[data-response]")?.dataset.persistId || null])})),
    processes: Array.from(page.querySelectorAll("[data-process-contract]")).map(node => [node.dataset.processContract, node.querySelectorAll("[data-process-stage]").length, node.querySelectorAll("[data-process-connector]").length]),
    phraseBanks: Array.from(page.querySelectorAll("[data-phrase-bank-contract]")).map(node => ({contract: node.dataset.phraseBankContract, task: node.dataset.phraseBankTask, children: Array.from(node.children).map(child => child.className), label: node.querySelector(":scope > .canonical-phrase-bank-label")?.textContent.trim(), instruction: node.querySelector(":scope > .canonical-phrase-bank-instruction")?.textContent.trim(), phrases: Array.from(node.querySelectorAll(":scope > .canonical-phrase-bank-items > .canonical-phrase-bank-item")).map(item => item.textContent.trim())})),
    figures: Array.from(page.querySelectorAll("figure")).map(node => [node.className, node.querySelector("figcaption")?.textContent.trim()]),
    tables: Array.from(page.querySelectorAll("table")).map(node => [node.className, node.querySelector("caption")?.textContent.trim(), node.querySelectorAll("tr").length]),
    order: Array.from(page.querySelectorAll(orderSelector)).map(node => [node.tagName, node.dataset.taskId || node.dataset.cerContract || node.dataset.processContract || node.dataset.persistId || node.className])
  };
  return {structure, geometry, presentation};
}
"""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare_geometry(reference: dict[str, Any], actual: dict[str, Any]) -> tuple[int, int, list[str]]:
    failures: list[str] = []
    total = 0
    if set(reference) != set(actual):
        failures.append(f"geometry key mismatch: reference-only={sorted(set(reference) - set(actual))}; editor-only={sorted(set(actual) - set(reference))}")
    for key in sorted(set(reference) & set(actual)):
        for property_name, expected in reference[key].items():
            total += 1
            received = actual[key][property_name]
            if abs(expected - received) > GEOMETRY_TOLERANCE:
                failures.append(f"{key}.{property_name}: {expected} != {received}")
    return total - len(failures), total, failures


def compare_presentation(reference: dict[str, Any], actual: dict[str, Any]) -> tuple[int, int, list[str]]:
    failures: list[str] = []
    total = 0
    if set(reference) != set(actual):
        failures.append(f"presentation key mismatch: reference-only={sorted(set(reference) - set(actual))}; editor-only={sorted(set(actual) - set(reference))}")
    for key in sorted(set(reference) & set(actual)):
        for property_name, expected in reference[key].items():
            total += 1
            received = actual[key][property_name]
            if expected != received:
                failures.append(f"{key}.{property_name}: {expected!r} != {received!r}")
    return total - len(failures), total, failures


def pixel_diff(reference: Path, actual: Path, destination: Path) -> dict[str, Any]:
    with Image.open(reference).convert("RGB") as before, Image.open(actual).convert("RGB") as after:
        if before.size != after.size:
            return {"pass": False, "reason": f"image dimensions differ: {before.size} != {after.size}"}
        difference = ImageChops.difference(before, after)
        mask = difference.convert("L").point(lambda value: 255 if value > PIXEL_DELTA_THRESHOLD else 0)
        changed = sum(1 for value in mask.getdata() if value)
        total = before.width * before.height
        ratio = changed / total
        visual = Image.new("RGB", before.size, "white")
        visual.paste((220, 32, 32), mask=mask)
        destination.parent.mkdir(parents=True, exist_ok=True)
        visual.save(destination, optimize=True)
        return {
            "pass": ratio <= PIXEL_RATIO_TOLERANCE,
            "changedPixels": changed,
            "totalPixels": total,
            "ratio": ratio,
            "threshold": PIXEL_DELTA_THRESHOLD,
            "tolerance": PIXEL_RATIO_TOLERANCE,
        }


def contact_sheet(label: str, paths: list[Path], destination: Path) -> None:
    images = [Image.open(path).convert("RGB") for path in paths]
    width = 306
    thumbs = [image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS) for image in images]
    columns = 2
    padding = 18
    label_height = 30
    cell_height = max(image.height for image in thumbs) + label_height
    rows = (len(thumbs) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * width + (columns + 1) * padding, rows * cell_height + (rows + 1) * padding), "white")
    draw = ImageDraw.Draw(sheet)
    for index, image in enumerate(thumbs):
        row, column = divmod(index, columns)
        x = padding + column * (width + padding)
        y = padding + row * cell_height
        draw.text((x, y), f"{label} · page {index + 1}", fill="black")
        sheet.paste(image, (x, y + label_height))
    destination.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(destination, optimize=True)
    for image in images:
        image.close()


def page_locators(master_page, editor_page, role: str) -> tuple[Locator, Locator]:
    source_role = "student" if role == "grayscale" else role
    return (
        master_page.locator(f'.page[data-role="{source_role}"]'),
        editor_page.locator("#worksheetHost").locator(f'.page[data-role="{source_role}"]'),
    )


def set_role(master_page, editor_page, role: str) -> None:
    source_role = "student" if role == "grayscale" else role
    grayscale = role == "grayscale"
    master_page.evaluate("([role, grayscale]) => window.__case03.saveState({role, grayscale, density: 'balanced', guides: false, boundaries: true})", [source_role, grayscale])
    editor_page.evaluate("([role, grayscale]) => { window.__curriculumEditor.setRole(role); window.__curriculumEditor.saveState({grayscale, density: 'normal', guides: false, boundaries: true}); }", [source_role, grayscale])
    master_page.wait_for_timeout(80)
    editor_page.wait_for_timeout(80)


def capture_isolated_pair(master_page, editor_page, master_node: Locator, editor_node: Locator, master_path: Path, editor_path: Path) -> None:
    master_node.evaluate("node => node.dataset.parityCapture = 'true'")
    editor_node.evaluate("node => node.dataset.parityCapture = 'true'")
    master_page.evaluate("() => { const style = document.createElement('style'); style.id = 'parityCaptureStyle'; style.textContent = '.toolbar{display:none!important}.page:not([data-parity-capture]){visibility:hidden!important}.page[data-parity-capture]{position:fixed!important;inset:0 auto auto 0!important;margin:0!important;box-shadow:none!important}'; document.head.append(style); }")
    editor_page.evaluate("() => { const outer = document.createElement('style'); outer.id = 'parityOuterCaptureStyle'; outer.textContent = '#editorToolbarHost{display:none!important}'; document.head.append(outer); const root = document.querySelector('#worksheetHost').shadowRoot; const style = document.createElement('style'); style.id = 'parityCaptureStyle'; style.textContent = '.page:not([data-parity-capture]){visibility:hidden!important}.page[data-parity-capture]{position:fixed!important;inset:0 auto auto 0!important;margin:0!important;box-shadow:none!important}'; root.append(style); }")
    master_node.screenshot(path=str(master_path), animations="disabled")
    editor_node.screenshot(path=str(editor_path), animations="disabled")
    master_page.evaluate("() => { document.querySelector('#parityCaptureStyle')?.remove(); document.querySelector('[data-parity-capture]')?.removeAttribute('data-parity-capture'); }")
    editor_page.evaluate("() => { document.querySelector('#parityOuterCaptureStyle')?.remove(); const root = document.querySelector('#worksheetHost').shadowRoot; root.querySelector('#parityCaptureStyle')?.remove(); root.querySelector('[data-parity-capture]')?.removeAttribute('data-parity-capture'); }")


def run(chrome: Path) -> dict[str, Any]:
    if SCREENSHOTS.exists():
        shutil.rmtree(SCREENSHOTS)
    SCREENSHOTS.mkdir(parents=True)
    server = ThreadingHTTPServer(("127.0.0.1", 0), CurriculumEditorHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    page_results: list[dict[str, Any]] = []
    structural_passed = geometry_passed = geometry_total = presentation_passed = presentation_total = rendered_passed = export_passed = 0
    atomic_passed = atomic_total = phrase_bank_passed = phrase_bank_total = role_artifact_passed = zero_overflow_roles = complete_export_passed = complete_export_total = 0
    total_pages = sum(ROLES.values())
    try:
        with tempfile.TemporaryDirectory(prefix="case03-v11-parity-") as temporary:
            temp = Path(temporary)
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=True, executable_path=str(chrome), args=["--no-sandbox"])
                context = browser.new_context(viewport={"width": 1440, "height": 1200}, device_scale_factor=1)
                master_page = context.new_page()
                editor_page = context.new_page()
                master_errors: list[str] = []
                editor_errors: list[str] = []
                master_page.on("pageerror", lambda error: master_errors.append(str(error)))
                editor_page.on("pageerror", lambda error: editor_errors.append(str(error)))
                master_page.goto(f"{base}/{MASTER_PATH}", wait_until="load")
                editor_page.goto(f"{base}/apps/curriculum-editor/index.html?parity=v1.1", wait_until="load")
                master_page.wait_for_function("window.__case03")
                editor_page.wait_for_function("window.__curriculumEditor")
                for role, expected_count in ROLES.items():
                    set_role(master_page, editor_page, role)
                    master_pages, editor_pages = page_locators(master_page, editor_page, role)
                    if master_pages.count() != expected_count or editor_pages.count() != expected_count:
                        page_results.append({"role": role, "pass": False, "reason": f"page count {master_pages.count()}/{editor_pages.count()} expected {expected_count}"})
                        continue
                    master_images: list[Path] = []
                    editor_images: list[Path] = []
                    diff_images: list[Path] = []
                    for index in range(expected_count):
                        master_node = master_pages.nth(index)
                        editor_node = editor_pages.nth(index)
                        master_snapshot = master_node.evaluate(SNAPSHOT_SCRIPT)
                        editor_snapshot = editor_node.evaluate(SNAPSHOT_SCRIPT)
                        structural_match = master_snapshot["structure"] == editor_snapshot["structure"]
                        structural_passed += int(structural_match)
                        g_passed, g_total, g_failures = compare_geometry(master_snapshot["geometry"], editor_snapshot["geometry"])
                        p_passed, p_total, p_failures = compare_presentation(master_snapshot["presentation"], editor_snapshot["presentation"])
                        geometry_passed += g_passed
                        geometry_total += g_total
                        presentation_passed += p_passed
                        presentation_total += p_total
                        frame_rect = editor_snapshot["geometry"].get("frame:0:0")
                        for cer_index, cer in enumerate(editor_snapshot["structure"]["cers"]):
                            atomic_total += 1
                            cer_rect = editor_snapshot["geometry"].get(f'cer:{cer["contract"]}:{cer_index}')
                            row_labels = [row[1] for row in cer["rows"]]
                            contained = bool(frame_rect and cer_rect and cer_rect["x"] >= frame_rect["x"] - GEOMETRY_TOLERANCE and cer_rect["y"] >= frame_rect["y"] - GEOMETRY_TOLERANCE and cer_rect["right"] <= frame_rect["right"] + GEOMETRY_TOLERANCE and cer_rect["bottom"] <= frame_rect["bottom"] + GEOMETRY_TOLERANCE)
                            atomic_passed += int(row_labels == ["CLAIM", "EVIDENCE", "REASONING"] and contained)
                        for bank_index, bank in enumerate(editor_snapshot["structure"]["phraseBanks"]):
                            phrase_bank_total += 1
                            bank_rect = editor_snapshot["geometry"].get(f'phrase-bank:{bank["contract"]}:{bank_index}')
                            expected_phrases = [
                                "New chlorophyll production is disrupted",
                                "Wrong BP-4 filter installed",
                                "New growth becomes pale or white",
                                "Red and deep-red transmission drops",
                            ]
                            contained = bool(frame_rect and bank_rect and bank_rect["x"] >= frame_rect["x"] - GEOMETRY_TOLERANCE and bank_rect["y"] >= frame_rect["y"] - GEOMETRY_TOLERANCE and bank_rect["right"] <= frame_rect["right"] + GEOMETRY_TOLERANCE and bank_rect["bottom"] <= frame_rect["bottom"] + GEOMETRY_TOLERANCE)
                            phrase_bank_passed += int(
                                bank["task"] == "6"
                                and bank["children"] == ["canonical-phrase-bank-label", "canonical-phrase-bank-instruction", "canonical-phrase-bank-items"]
                                and bank["label"] == "PHRASE BANK"
                                and bank["instruction"] == "Use each phrase once."
                                and bank["phrases"] == expected_phrases
                                and len(set(bank["phrases"])) == 4
                                and any(task[0] == "6" for task in editor_snapshot["structure"]["tasks"])
                                and contained
                            )
                        master_image = temp / f"{role}-{index + 1}-master.png"
                        editor_image = temp / f"{role}-{index + 1}-editor.png"
                        diff_image = temp / f"{role}-{index + 1}-diff.png"
                        capture_isolated_pair(master_page, editor_page, master_node, editor_node, master_image, editor_image)
                        rendered = pixel_diff(master_image, editor_image, diff_image)
                        rendered_passed += int(rendered["pass"])
                        master_images.append(master_image)
                        editor_images.append(editor_image)
                        diff_images.append(diff_image)
                        page_id = master_snapshot["structure"]["pageId"]
                        if role == "accessible" and page_id == "accessible-mission-06":
                            shutil.copy2(master_image, SCREENSHOTS / "accessible-task7-master.png")
                            shutil.copy2(editor_image, SCREENSHOTS / "accessible-task7-editor.png")
                            shutil.copy2(diff_image, SCREENSHOTS / "accessible-task7-diff.png")
                        page_results.append({
                            "role": role,
                            "page": index + 1,
                            "pageId": page_id,
                            "structuralParity": structural_match,
                            "geometry": {"passed": g_passed, "total": g_total, "failures": g_failures[:20]},
                            "presentation": {"passed": p_passed, "total": p_total, "failures": p_failures[:20]},
                            "rendered": rendered,
                        })
                    contact_sheet(f"{role} master", master_images, SCREENSHOTS / f"{role}-master.png")
                    contact_sheet(f"{role} editor", editor_images, SCREENSHOTS / f"{role}-editor.png")
                    contact_sheet(f"{role} diff", diff_images, SCREENSHOTS / f"{role}-diff.png")

                    # Current-role exports must retain the same page structure and geometry.
                    source_role = "student" if role == "grayscale" else role
                    export_html = editor_page.evaluate("([role, grayscale]) => { window.__curriculumEditor.saveState({grayscale}); return window.__curriculumEditor.serializeRoleHTML(role); }", [source_role, role == "grayscale"])
                    export_page = context.new_page()
                    export_page.set_content(export_html, wait_until="load")
                    export_page.wait_for_function("window.__curriculumPortable")
                    export_nodes = export_page.locator(f'.page[data-role="{source_role}"]')
                    export_role_pass = export_nodes.count() == expected_count
                    for index in range(min(expected_count, export_nodes.count())):
                        live_snapshot = editor_pages.nth(index).evaluate(SNAPSHOT_SCRIPT)
                        export_snapshot = export_nodes.nth(index).evaluate(SNAPSHOT_SCRIPT)
                        export_role_pass = export_role_pass and live_snapshot["structure"] == export_snapshot["structure"]
                        _, _, failures = compare_geometry(live_snapshot["geometry"], export_snapshot["geometry"])
                        export_role_pass = export_role_pass and not failures
                    export_passed += int(export_role_pass)
                    export_page.close()

                    artifact_page = context.new_page()
                    artifact_errors: list[str] = []
                    artifact_page.on("pageerror", lambda error, errors=artifact_errors: errors.append(str(error)))
                    artifact_page.goto(f"{base}/sss/campaign-1/case-03-mars-habitat/published/{ROLE_FILES[role]}", wait_until="load")
                    artifact_page.wait_for_function("window.__case03")
                    artifact_nodes = artifact_page.locator(f'.page[data-role="{source_role}"]')
                    overflow = artifact_page.evaluate("window.__case03.checkOverflow()")
                    artifact_match = artifact_nodes.count() == expected_count and overflow == 0 and not artifact_errors
                    for index in range(min(expected_count, artifact_nodes.count())):
                        artifact_snapshot = artifact_nodes.nth(index).evaluate(SNAPSHOT_SCRIPT)
                        master_snapshot = master_pages.nth(index).evaluate(SNAPSHOT_SCRIPT)
                        _, _, artifact_geometry_failures = compare_geometry(master_snapshot["geometry"], artifact_snapshot["geometry"])
                        artifact_match = artifact_match and artifact_snapshot["structure"] == master_snapshot["structure"] and not artifact_geometry_failures
                    role_artifact_passed += int(artifact_match)
                    zero_overflow_roles += int(overflow == 0)
                    artifact_page.close()

                editor_page.evaluate("window.__curriculumEditor.saveState({grayscale: false})")
                complete_html = editor_page.evaluate("window.__curriculumEditor.serializePortableHTML()")
                complete_page = context.new_page()
                complete_page.set_content(complete_html, wait_until="load")
                complete_page.wait_for_function("window.__curriculumPortable")
                for role, expected_count in ((name, count) for name, count in ROLES.items() if name != "grayscale"):
                    master_page.evaluate("role => window.__case03.saveState({role, grayscale: false})", role)
                    complete_page.evaluate("role => window.__curriculumPortable.setRole(role)", role)
                    master_nodes = master_page.locator(f'.page[data-role="{role}"]')
                    complete_nodes = complete_page.locator(f'.page[data-role="{role}"]')
                    for index in range(expected_count):
                        complete_export_total += 1
                        reference = master_nodes.nth(index).evaluate(SNAPSHOT_SCRIPT)
                        exported = complete_nodes.nth(index).evaluate(SNAPSHOT_SCRIPT)
                        _, _, failures = compare_geometry(reference["geometry"], exported["geometry"])
                        complete_export_passed += int(reference["structure"] == exported["structure"] and not failures)
                complete_page.close()
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)

    all_pass = (
        structural_passed == total_pages
        and geometry_passed == geometry_total
        and presentation_passed == presentation_total
        and rendered_passed == total_pages
        and export_passed == len(ROLES)
        and atomic_passed == atomic_total == 4
        and phrase_bank_passed == phrase_bank_total == 4
        and role_artifact_passed == len(ROLES)
        and zero_overflow_roles == len(ROLES)
        and complete_export_passed == complete_export_total == 23
        and not master_errors
        and not editor_errors
    )
    screenshots = {
        path.stem: {"path": str(path.relative_to(REPO)), "sha256": sha256(path)}
        for path in sorted(SCREENSHOTS.glob("*.png"))
    }
    return {
        "validator": "case03-v1.1-central-editor-parity",
        "status": "PASS" if all_pass else "FAIL",
        "browser": str(chrome),
        "viewport": {"width": 1440, "height": 1200, "deviceScaleFactor": 1},
        "pageCounts": ROLES,
        "structuralParity": {"passed": structural_passed, "total": total_pages},
        "pageAssignmentParity": {"passed": structural_passed, "total": total_pages},
        "geometryParity": {"passed": geometry_passed, "total": geometry_total, "tolerancePx": GEOMETRY_TOLERANCE},
        "computedPresentationParity": {"passed": presentation_passed, "total": presentation_total},
        "renderedComparison": {"passed": rendered_passed, "total": total_pages, "pixelDeltaThreshold": PIXEL_DELTA_THRESHOLD, "pixelRatioTolerance": PIXEL_RATIO_TOLERANCE},
        "cerAtomicity": {"passed": atomic_passed, "total": atomic_total},
        "phraseBankContract": {"passed": phrase_bank_passed, "total": phrase_bank_total},
        "v1.1RoleArtifacts": {"passed": role_artifact_passed, "total": len(ROLES)},
        "zeroOverflowRoles": {"passed": zero_overflow_roles, "total": len(ROLES)},
        "currentRoleExportParity": {"passed": export_passed, "total": len(ROLES)},
        "completePortableExportParity": {"passed": complete_export_passed, "total": complete_export_total},
        "javascriptErrors": {"master": master_errors, "editor": editor_errors},
        "pages": page_results,
        "screenshots": screenshots,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chrome", type=Path, default=Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    args = parser.parse_args()
    if not args.chrome.is_file():
        raise SystemExit(f"Chrome executable not found: {args.chrome}")
    result = run(args.chrome.resolve())
    RESULTS.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ["status", "structuralParity", "pageAssignmentParity", "geometryParity", "computedPresentationParity", "renderedComparison", "cerAtomicity", "phraseBankContract", "v1.1RoleArtifacts", "zeroOverflowRoles", "currentRoleExportParity", "completePortableExportParity", "javascriptErrors"]}, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
