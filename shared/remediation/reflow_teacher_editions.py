#!/usr/bin/env python3
"""Reflow the expanded Teacher Editions toward the common seven-page architecture.

The final remediation added the material the Teacher Edition contract requires and the
first pass simply gave each over-full Guide one more page. This reflows the content
across the whole edition instead, so pages carry a balanced load and the Guides return
to (or reach) the common seven-page shape wherever the content actually allows it.

Nothing is cut. Every block is preserved in document order; only the page breaks move.

## What the measurements showed

Each Teacher block is atomic -- a table, a list, a callout cannot be split across a page
break -- and the block order is instructional, so it cannot be reordered. That makes the
minimum page count an exact quantity, not a matter of effort. Measured in Chromium, with
an exact dynamic-programming page-break search over the real rendered block heights:

    case            movable blocks   exact minimum   seven pages?
    SSS-C1-CASE01        51               8          no, short by one page
    SSS-C1-CASE02        37               7          yes, 82.4% worst-page fill
    SSS-C2-CASE01        68               8          no, short by one page
    SSS-C2-CASE06        60               6          yes, 76.1% worst-page fill

## Targets and why

- **SSS-C1-CASE02 -> 7 pages.** Reaches the common architecture, worst page 82.4% full.
  Restores the case's pre-remediation page count with all added content kept.
- **SSS-C2-CASE06 -> 7 pages.** Reaches the common architecture, worst page 76.1% full.
  One page shorter than its pre-remediation count.
- **SSS-C2-CASE01 -> 9 pages.** Cannot reach seven: its exact minimum is eight. Eight is
  additionally unsafe -- the best possible eight-page split leaves the worst page 99.7%
  full, about three pixels of slack, and a page tuned that tightly on macOS has already
  been shown to clip on the Linux CI runner where font metrics run taller. Nine pages
  leaves the worst page 86.5% full and restores the pre-remediation count.
- **SSS-C1-CASE01 is left exactly as it is, at 8 pages.** It is already at its exact
  minimum; no reflow can improve it and every eight-page split leaves a page ~99.9% full,
  so re-cutting it would only risk the fit it currently holds.

The two cases that cannot reach seven are reported as conflicts rather than forced. See
the status document for the exact conflict.

Idempotent: a case whose Teacher pages already match its recorded distribution is skipped.
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

SCAFFOLD_CLASSES = ("continuation-header", "mission-title-block")

# case id -> (case directory, movable blocks per page). Distributions come from an exact
# minimise-the-worst-page search over Chromium-measured block heights; see the docstring.
PLAN: dict[str, tuple[str, list[int]]] = {
    "SSS-C1-CASE02": ("sss/campaign-1/case-02-lunar-greenhouse", [3, 7, 4, 4, 5, 10, 4]),
    "SSS-C2-CASE06": ("sss/campaign-2/case-06-first-garden", [8, 10, 8, 10, 10, 7, 7]),
    "SSS-C2-CASE01": ("sss/campaign-2/case-01-heavy-hands", [11, 9, 9, 8, 7, 5, 7, 8, 4]),
}

# Recorded, deliberately not reflowed. Kept here so the exclusion is explicit rather than
# an omission someone later "fixes".
CANNOT_REACH_SEVEN = {
    "SSS-C1-CASE01": "exact minimum is 8 pages; already there, and every 8-page split is ~99.9% full",
    "SSS-C2-CASE01": "exact minimum is 8 pages; 8 is 99.7% full so the plan targets a safe 9",
}


def is_scaffold(node: Tag) -> bool:
    classes = set(node.get("class") or [])
    return any(name in classes for name in SCAFFOLD_CLASSES)


def teacher_pages(soup: BeautifulSoup) -> list[Tag]:
    return soup.select('.page[data-role="teacher"]')


def content_area(page: Tag) -> Tag:
    node = page.select_one(".content-area") or page.select_one(".content")
    if node is None:
        raise RuntimeError(f"page {page.get('data-page-id')} has no content area")
    return node


def movable_blocks(page: Tag) -> list[Tag]:
    return [n for n in content_area(page).find_all(recursive=False) if not is_scaffold(n)]


def page_id_format(page_ids: list[str]) -> tuple[str, int]:
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


def blank_clone(template: Tag) -> Tag:
    """A continuation page with its scaffolding intact and its content emptied."""
    clone = BeautifulSoup(template.decode(), "html.parser").find(class_="page")
    for node in movable_blocks(clone):
        node.decompose()
    return clone


def reflow(case_id: str, case_dir: Path, distribution: list[int], apply: bool) -> bool:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    soup = BeautifulSoup(content_path.read_text(encoding="utf-8"), "html.parser")

    pages = teacher_pages(soup)
    if [len(movable_blocks(p)) for p in pages] == distribution:
        return False  # already reflowed

    blocks: list[Tag] = [b for page in pages for b in movable_blocks(page)]
    if len(blocks) != sum(distribution):
        raise RuntimeError(
            f"{case_id}: {len(blocks)} movable blocks but the recorded distribution "
            f"expects {sum(distribution)}; the plan is stale and must be re-measured"
        )

    first, continuation_template = pages[0], pages[1]
    stem, width = page_id_format([p.get("data-page-id") for p in pages])

    # Rebuild page one in place, then rebuild the tail from clean clones.
    for node in movable_blocks(first):
        node.extract()
    rebuilt = [first] + [blank_clone(continuation_template) for _ in distribution[1:]]

    cursor = 0
    for page, count in zip(rebuilt, distribution):
        target = content_area(page)
        for node in blocks[cursor:cursor + count]:
            target.append(node.extract())
        cursor += count

    anchor = pages[-1]
    for page in rebuilt[1:]:
        anchor.insert_after(page)
        anchor = page
    for stale in pages[1:]:
        stale.decompose()

    pages = teacher_pages(soup)
    renumber(pages, stem, width)

    before = len(distribution)
    if apply:
        content_path.write_text(soup.decode(formatter="minimal"), encoding="utf-8")
        package = json.loads(package_path.read_text(encoding="utf-8"))
        package["rolePageStructure"]["teacher"]["pageCount"] = len(pages)
        if "content" in package.get("sourceHashes", {}):
            package["sourceHashes"]["content"] = hashlib.sha256(content_path.read_bytes()).hexdigest()
        package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"{case_id}: reflowed to {len(pages)} Teacher pages {distribution}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    changed = 0
    for case_id, (rel, distribution) in PLAN.items():
        if reflow(case_id, ROOT / rel, distribution, args.apply):
            changed += 1
    for case_id, reason in CANNOT_REACH_SEVEN.items():
        print(f"{case_id}: NOT reflowed to seven pages -- {reason}")
    print(f"Teacher reflow: {changed} case(s) {'reflowed' if args.apply else 'pending'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
