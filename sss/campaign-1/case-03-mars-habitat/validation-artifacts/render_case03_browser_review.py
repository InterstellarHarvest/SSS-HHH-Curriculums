#!/usr/bin/env python3
"""Render all standalone Case 03 HTML pages for browser-based visual review."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
PUBLISHED = ROOT / "published"
OUT = ROOT / "validation-artifacts/browser-rendered-review"
RESULTS = ROOT / "validation-artifacts/CASE03_BROWSER_RENDERED_REVIEW_RESULTS.json"
ROLES = {
    "student": ("SSS_C1_CASE03_STUDENT_MISSION_v1.0.html", 4),
    "teacher": ("SSS_C1_CASE03_TEACHER_GUIDE_v1.0.html", 8),
    "answer": ("SSS_C1_CASE03_ANSWER_KEY_v1.0.html", 4),
    "accessible": ("SSS_C1_CASE03_ACCESSIBLE_MISSION_v1.0.html", 6),
    "grayscale": ("SSS_C1_CASE03_GRAYSCALE_MISSION_v1.0.html", 4),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contact_sheet(role: str, images: list[Path], destination: Path) -> None:
    opened = [Image.open(path).convert("RGB") for path in images]
    thumb_width = 306
    thumbs: list[Image.Image] = []
    for source in opened:
        height = round(source.height * thumb_width / source.width)
        thumbs.append(source.resize((thumb_width, height), Image.Resampling.LANCZOS))
    columns = 2
    padding = 18
    label_height = 34
    rows = (len(thumbs) + columns - 1) // columns
    cell_height = max(image.height for image in thumbs) + label_height
    sheet = Image.new(
        "RGB",
        (columns * thumb_width + (columns + 1) * padding, rows * cell_height + (rows + 1) * padding),
        "white",
    )
    draw = ImageDraw.Draw(sheet)
    for index, image in enumerate(thumbs):
        row, column = divmod(index, columns)
        x = padding + column * (thumb_width + padding)
        y = padding + row * cell_height
        draw.text((x, y), f"{role.title()} HTML page {index + 1}", fill="black")
        sheet.paste(image, (x, y + label_height))
    sheet.save(destination, optimize=True)
    for image in opened:
        image.close()


def run(chrome: Path) -> dict[str, Any]:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    roles: dict[str, Any] = {}
    rendered_count = 0
    all_pass = True
    with tempfile.TemporaryDirectory(prefix="case03-browser-render-") as temporary:
        temporary_root = Path(temporary)
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=True,
                executable_path=str(chrome),
                args=["--no-sandbox"],
            )
            for role, (filename, expected_pages) in ROLES.items():
                page = browser.new_page(viewport={"width": 1024, "height": 1200})
                errors: list[str] = []
                page.on("pageerror", lambda error, errors=errors: errors.append(str(error)))
                page.goto((PUBLISHED / filename).resolve().as_uri(), wait_until="load")
                page.wait_for_timeout(250)
                locator = page.locator("section.page")
                actual_pages = locator.count()
                overflow = page.locator("section.page.has-overflow").count()
                page_paths: list[Path] = []
                dimensions: list[list[int]] = []
                for index in range(actual_pages):
                    destination = temporary_root / f"{role}-{index + 1}.png"
                    node = locator.nth(index)
                    node.screenshot(path=str(destination), animations="disabled")
                    with Image.open(destination) as image:
                        dimensions.append([image.width, image.height])
                    page_paths.append(destination)
                contact_path = OUT / f"{role}-contact-sheet.png"
                contact_sheet(role, page_paths, contact_path)
                role_pass = actual_pages == expected_pages and overflow == 0 and not errors
                all_pass = all_pass and role_pass
                rendered_count += actual_pages
                roles[role] = {
                    "source": f"published/{filename}",
                    "expectedPages": expected_pages,
                    "renderedPages": actual_pages,
                    "overflowPages": overflow,
                    "javascriptErrors": errors,
                    "pagePixelDimensions": dimensions,
                    "contactSheet": str(contact_path.relative_to(ROOT)),
                    "contactSheetSha256": sha256(contact_path),
                    "status": "PASS" if role_pass else "FAIL",
                }
                page.close()
            browser.close()
    return {
        "validator": "case03-browser-rendered-review",
        "status": "PASS" if all_pass and rendered_count == 26 else "FAIL",
        "browser": str(chrome),
        "renderedPageCount": rendered_count,
        "expectedPageCount": 26,
        "roles": roles,
        "reviewNote": "Contact sheets require human visual inspection; this result records successful browser rendering, page count, JavaScript, and overflow checks.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--chrome",
        type=Path,
        default=Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    )
    args = parser.parse_args()
    result = run(args.chrome.resolve())
    RESULTS.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{result['renderedPageCount']}/{result['expectedPageCount']} HTML pages rendered")
    print(f"Browser rendered review capture: {result['status']}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
