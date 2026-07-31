#!/usr/bin/env python3
"""Apply the shared Student CER component to Case 02 HTML only.

This maintenance builder intentionally does not read, write, or regenerate PDFs.
"""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path

from bs4 import BeautifulSoup, Tag


CASE_ROOT = Path(__file__).resolve().parents[1]
REPO = CASE_ROOT.parents[2]
CER_SOURCE = REPO / "shared/implementation/editor-shell/v1.0/cer.css"
TARGETS = [
    CASE_ROOT / "master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html",
    CASE_ROOT / "published/SSS_C1_CASE02_STUDENT_MISSION_v1.0.html",
    CASE_ROOT / "published/SSS_C1_CASE02_GRAYSCALE_MISSION_v1.0.html",
]


def set_text(node: Tag, text: str) -> None:
    node.clear()
    node.append(text)


def make_cer(soup: BeautifulSoup, task7: Tag) -> None:
    old_stack = task7.select_one(".cer-stack")
    if old_stack is None:
        if task7.select_one('[data-cer-contract="student-v1.0"]'):
            return
        raise ValueError("Task 7 does not contain the expected CER source.")

    responses = {
        "claim": old_stack.select_one('[data-field="student-task7-claim"]'),
        "evidence": old_stack.select_one('[data-field="student-task7-evidence"]'),
        "reasoning": old_stack.select_one('[data-field="student-task7-reasoning"]'),
    }
    if any(node is None for node in responses.values()):
        raise ValueError("Task 7 is missing a Claim, Evidence, or Reasoning response.")

    cer = soup.new_tag("div")
    cer["class"] = ["canonical-cer"]
    cer["data-cer-contract"] = "student-v1.0"
    for kind, label in (("claim", "CLAIM"), ("evidence", "EVIDENCE"), ("reasoning", "REASONING")):
        box = soup.new_tag("div")
        box["class"] = ["canonical-cer-box", kind]
        label_node = soup.new_tag("div")
        label_node["class"] = ["canonical-cer-label"]
        label_node.string = label
        response = copy.deepcopy(responses[kind])
        response["class"] = sorted(set(response.get("class", [])) | {"canonical-cer-response"})
        box.extend([label_node, response])
        cer.append(box)
    old_stack.replace_with(cer)


def install_component(soup: BeautifulSoup) -> None:
    digest = hashlib.sha256(CER_SOURCE.read_bytes()).hexdigest()
    old_meta = soup.select_one('meta[name="sss-cer-component"]')
    if old_meta:
        old_meta.decompose()
    meta = soup.new_tag("meta")
    meta["name"] = "sss-cer-component"
    meta["content"] = "1.0"
    soup.head.append(meta)

    old_style = soup.select_one("#sssCerComponentCss")
    if old_style:
        old_style.decompose()
    style = soup.new_tag("style")
    style["id"] = "sssCerComponentCss"
    style["data-source-sha256"] = digest
    style.string = CER_SOURCE.read_text(encoding="utf-8")
    soup.head.append(style)


def update_page_identity(page: Tag, current: int, total: int) -> None:
    page["aria-label"] = f"Student Mission page {current} of {total}"
    footer = page.select_one(".publication-footer span")
    if footer is None:
        raise ValueError(f"{page.get('data-page-id')} is missing its publication footer.")
    set_text(footer, f"Student Mission {current} of {total}")


def transform(path: Path) -> None:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    install_component(soup)
    student_pages = soup.select('.page[data-role="student"]')

    if len(student_pages) == 2:
        page1, page2 = student_pages
        task67 = page2.select_one(".task67-row")
        final_row = page2.select_one(".task89-row")
        if task67 is None or final_row is None:
            raise ValueError(f"{path.name}: expected Task 6/7 and Task 8/9 rows.")
        task_sections = task67.find_all("section", recursive=False)
        if len(task_sections) != 2:
            raise ValueError(f"{path.name}: expected separate Task 6 and Task 7 sections.")
        task6, task7 = task_sections
        make_cer(soup, task7)

        page3 = soup.new_tag("section")
        page3["class"] = list(page2.get("class", []))
        page3["data-page-id"] = "student-03"
        page3["data-role"] = "student"
        page3["role"] = "region"
        page3["aria-label"] = "Student Mission page 3 of 3"
        overflow = copy.deepcopy(page2.select_one(".overflow-warning"))
        frame = soup.new_tag("div")
        frame["class"] = ["page-frame"]
        frame.append(copy.deepcopy(page2.select_one(".continuation-header")))
        content = soup.new_tag("div")
        content["class"] = ["content-area", "student-cer-page"]
        task7["class"] = sorted(set(task7.get("class", [])) | {"major-task-block", "task7-full-width"})
        content.append(copy.deepcopy(task7))
        content.append(copy.deepcopy(final_row))
        frame.append(content)
        footer = copy.deepcopy(page2.select_one(".publication-footer"))
        set_text(footer.select_one("span"), "Student Mission 3 of 3")
        frame.append(footer)
        page3.extend([overflow, frame])

        task7.decompose()
        final_row.decompose()
        task67["class"] = [
            name for name in task67.get("class", [])
            if name not in {"two-col", "diagnosis-row", "task67-row"}
        ] + ["task6-row", "task6-full-width"]
        page2.insert_after(page3)
        update_page_identity(page1, 1, 3)
        update_page_identity(page2, 2, 3)
    elif len(student_pages) == 3:
        page1, page2, page3 = student_pages
        update_page_identity(page1, 1, 3)
        update_page_identity(page2, 2, 3)
        update_page_identity(page3, 3, 3)
        task7 = page3.select_one('.task-heading[data-task-id="7"]')
        if task7 is None:
            raise ValueError(f"{path.name}: existing page 3 is missing Task 7.")
        task7_section = task7.find_parent("section")
        make_cer(soup, task7_section)
    else:
        raise ValueError(f"{path.name}: expected two baseline or three maintained Student pages.")

    path.write_text("<!doctype html>\n" + str(soup.html), encoding="utf-8")
    print(f"HTML-only CER build: {path.relative_to(REPO)}")


def main() -> int:
    for target in TARGETS:
        transform(target)
    print("PDF generation: skipped by design")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
