#!/usr/bin/env python3
"""Give the four over-full Teacher Guide pages the extra page their content needs.

The final remediation added the material the Teacher Edition contract requires -- the
common analytic 4/3/2/1 rubric, quick grading guidance, the complete task route, the
Case 01 Task 5 procedure step the audit found missing, and controlled reference lists --
to Teacher Guides whose page allowance was already full. Four pages then ran past their
printable frame, by 57px to 479px:

    SSS-C1-CASE01  teacher-3          884 available, 1363 used
    SSS-C1-CASE02  teacher-07         884 available, 1122 used
    SSS-C2-CASE01  teacher-guide-09   936 available,  993 used
    SSS-C2-CASE06  teacher-guide-08   936 available, 1245 used

Content overflowing a fixed Letter frame is clipped in print, so this is a real defect
rather than a cosmetic one. Audit finding C2C6-SYS01 settles which side gives way: a
Teacher package is validated on "the common functional set: usable procedure/class flow,
rubric system, and authoritative source function rather than merely a fixed page count."
So every block is preserved and the Guide gains a page, rather than content being cut to
defend a page count.

Each split point was measured in Chromium and falls on a section heading, so no block is
separated from its heading and no table or list is broken across the seam. The moved
remainder fits the new page in every case.

The two Campaign 1 cases carry the continuation header as a sibling of .content-area
inside .page-frame; the two Campaign 2 cases carry it as the first child of .content.
Both shapes are handled, and every teacher page is renumbered afterwards: data-page-id,
the "page N of M" aria-label, the aria-labelledby/heading id pair where the case uses
one, and the "Teacher Guide N of M" footer.

Idempotent: a case whose Teacher pages all fit their declared count is left alone.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).resolve().parents[2]

# Stamped on each page this script creates, so a rerun recognizes its own work.
MARKER = "teacher-overflow-v1.0"

# case id -> (case directory, overflowing page id, 0-based split index into the
# content area's children). Split indices were measured in headless Chromium against
# the rendered Teacher role; see the module docstring.
PLAN = {
    "SSS-C1-CASE01": ("sss/campaign-1/case-01-iss-greenhouse", "teacher-3", 11),
    "SSS-C1-CASE02": ("sss/campaign-1/case-02-lunar-greenhouse", "teacher-07", 8),
    "SSS-C2-CASE01": ("sss/campaign-2/case-01-heavy-hands", "teacher-guide-09", 5),
    "SSS-C2-CASE06": ("sss/campaign-2/case-06-first-garden", "teacher-guide-08", 9),
}


def teacher_pages(soup: BeautifulSoup) -> list[Tag]:
    return soup.select('.page[data-role="teacher"]')


def content_area(page: Tag) -> Tag:
    node = page.select_one(".content-area") or page.select_one(".content")
    if node is None:
        raise RuntimeError(f"page {page.get('data-page-id')} has no content area")
    return node


def page_id_format(page_ids: list[str]) -> tuple[str, int]:
    """Return the shared stem and zero-padding width of a teacher page-id series."""
    match = re.fullmatch(r"(.*?)(\d+)", page_ids[0])
    if not match:
        raise RuntimeError(f"unrecognized teacher page id: {page_ids[0]}")
    return match.group(1), len(match.group(2))


def renumber(pages: list[Tag], stem: str, width: int) -> None:
    total = len(pages)
    for index, page in enumerate(pages, start=1):
        new_id = f"{stem}{index:0{width}d}"
        page["data-page-id"] = new_id
        page["aria-label"] = f"Teacher Guide page {index} of {total}"
        if page.has_attr("aria-labelledby"):
            title = page.select_one("h1")
            if title is not None:
                title["id"] = f"{new_id}-title"
                page["aria-labelledby"] = f"{new_id}-title"
        footer = page.select_one(".publication-footer span")
        if footer is not None and re.fullmatch(r"\s*Teacher Guide \d+ of \d+\s*", footer.get_text()):
            footer.string = f"Teacher Guide {index} of {total}"


def split_page(page: Tag, split_index: int) -> Tag:
    """Move the tail of `page`'s content onto a fresh clone inserted after it."""
    content = content_area(page)
    children = content.find_all(recursive=False)
    if split_index <= 0 or split_index >= len(children):
        raise RuntimeError(f"split index {split_index} out of range for {page.get('data-page-id')}")

    new_page = copy.copy(page)
    new_page = BeautifulSoup(page.decode(), "html.parser").find(class_="page")
    new_content = content_area(new_page)

    # Empty the clone's content area, keeping only a continuation header if this case
    # nests one inside the content area.
    for node in new_content.find_all(recursive=False):
        if node.name == "header" and "continuation-header" in (node.get("class") or []):
            continue
        node.decompose()

    for node in children[split_index:]:
        new_content.append(node.extract())

    new_page["data-repagination"] = MARKER
    page.insert_after(new_page)
    return new_page


def repaginate(case_id: str, case_dir: Path, page_id: str, split_index: int, apply: bool) -> bool:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    soup = BeautifulSoup(content_path.read_text(encoding="utf-8"), "html.parser")

    pages = teacher_pages(soup)
    declared = json.loads(package_path.read_text(encoding="utf-8"))["rolePageStructure"]["teacher"]["pageCount"]
    if any(page.get("data-repagination") == MARKER for page in pages):
        return False  # this case already carries its added Teacher page

    target = next((p for p in pages if p.get("data-page-id") == page_id), None)
    if target is None:
        raise RuntimeError(f"{case_id}: teacher page {page_id} not found")

    stem, width = page_id_format([p.get("data-page-id") for p in pages])
    split_page(target, split_index)
    pages = teacher_pages(soup)
    renumber(pages, stem, width)

    if apply:
        content_path.write_text(soup.decode(formatter="minimal"), encoding="utf-8")
        package = json.loads(package_path.read_text(encoding="utf-8"))
        package["rolePageStructure"]["teacher"]["pageCount"] = len(pages)
        package.setdefault("sourceHashes", {})
        if "content" in package["sourceHashes"]:
            package["sourceHashes"]["content"] = hashlib.sha256(content_path.read_bytes()).hexdigest()
        package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"{case_id}: {page_id} split at child {split_index}; Teacher Guide {declared} -> {len(pages)} pages")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    changed = 0
    for case_id, (rel, page_id, split_index) in PLAN.items():
        if repaginate(case_id, ROOT / rel, page_id, split_index, args.apply):
            changed += 1
    print(f"Teacher repagination: {changed} case(s) {'repaginated' if args.apply else 'pending'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
