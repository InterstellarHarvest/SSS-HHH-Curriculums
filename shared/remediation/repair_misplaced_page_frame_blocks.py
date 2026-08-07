#!/usr/bin/env python3
"""Move remediation-inserted printable blocks back inside their page content area.

The wave-1/wave-3 transformers appended new Teacher Edition material (the common
analytic 4/3/2/1 rubric, controlled reference lists, and the complete task route)
with a "insert before the page footer" helper. The publication footer is a *sibling*
of `.content-area` inside `.page-frame`, not a child of it, so those blocks landed
outside the content area.

Consequences, all observed in Chromium against the remediation branch:

- `.page-frame` is a column flex container and `.content-area` is its `flex: 1 1 0`
  item, so every misplaced block stole height from the real content area until the
  content area's own text overflowed and rendered *on top of* the misplaced block.
- `checkOverflow()` measures `.page-frame` and `.content-area`, so material outside
  the content area escaped the page-fit contract that governs every printable page.
- The layout-override resize system addresses `.content-area` descendants, so the
  misplaced blocks were unreachable to it.

The frozen baseline f7a2442 had four `div.student-id` blocks as deliberate
page-frame siblings; those are Student/Accessible identity marks, are positioned
against the frame on purpose, and are left untouched. This repair only relocates
blocks that the final remediation itself inserted.

Idempotent: pages whose page-frame holds nothing but the header, content area and
footer are left alone.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).resolve().parents[2]

# Deliberate page-frame siblings that predate the final remediation (baseline f7a2442).
BASELINE_FRAME_SIBLINGS = {"student-id"}
STRUCTURAL = {"header", "footer"}
CONTENT_CLASSES = {"content-area", "content"}


def is_content_area(node: Tag) -> bool:
    return bool(CONTENT_CLASSES & set(node.get("class") or []))


def is_baseline_sibling(node: Tag) -> bool:
    return bool(BASELINE_FRAME_SIBLINGS & set(node.get("class") or []))


def misplaced_children(frame: Tag) -> list[Tag]:
    return [
        child
        for child in frame.find_all(recursive=False)
        if child.name not in STRUCTURAL
        and not is_content_area(child)
        and not is_baseline_sibling(child)
    ]


def repair_file(path: Path) -> list[str]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    moved: list[str] = []
    for page in soup.select(".page"):
        frame = page.select_one(".page-frame")
        if frame is None:
            continue
        stray = misplaced_children(frame)
        if not stray:
            continue
        content = next((c for c in frame.find_all(recursive=False) if is_content_area(c)), None)
        if content is None:
            raise RuntimeError(f"{path}: page {page.get('data-page-id')} has stray blocks but no content area")
        for node in stray:
            node.extract()
            content.append(node)
        moved.append(
            f"{page.get('data-role')}/{page.get('data-page-id')}: "
            + ", ".join(f"{n.name}.{' '.join(n.get('class') or []) or '-'}" for n in stray)
        )
    if moved:
        path.write_text(soup.decode(formatter="minimal"), encoding="utf-8")
    return moved


def refresh_content_hash(case_dir: Path) -> None:
    package_path = case_dir / "source/case-package.json"
    content_path = case_dir / "source/content.html"
    package = json.loads(package_path.read_text(encoding="utf-8"))
    hashes = package.get("sourceHashes")
    if isinstance(hashes, dict) and "content" in hashes:
        digest = hashlib.sha256(content_path.read_bytes()).hexdigest()
        if hashes["content"] != digest:
            hashes["content"] = digest
            package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    total = 0
    for content_path in sorted((ROOT / "sss").glob("campaign-*/*/source/content.html")):
        case_dir = content_path.parent.parent
        if not args.apply:
            soup = BeautifulSoup(content_path.read_text(encoding="utf-8"), "html.parser")
            pending = [
                page.get("data-page-id")
                for page in soup.select(".page")
                if (frame := page.select_one(".page-frame")) is not None and misplaced_children(frame)
            ]
            if pending:
                total += len(pending)
                print(f"{case_dir.name}: would repair {pending}")
            continue
        moved = repair_file(content_path)
        if moved:
            refresh_content_hash(case_dir)
            total += len(moved)
            print(f"{case_dir.name}:")
            for line in moved:
                print(f"  - {line}")

    print(f"misplaced page-frame blocks: {total} page(s) {'repaired' if args.apply else 'pending'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
