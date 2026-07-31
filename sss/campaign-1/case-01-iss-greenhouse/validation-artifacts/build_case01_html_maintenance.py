#!/usr/bin/env python3
"""Build the Case 01 v1.1 HTML-only canonical task-heading maintenance set.

This script never reads, writes, regenerates, or validates a PDF.
"""
from __future__ import annotations

import base64
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


CASE_ROOT = Path(__file__).resolve().parents[1]
REPO = CASE_ROOT.parents[2]
MASTER = CASE_ROOT / "master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html"
PUBLISHED = CASE_ROOT / "published/v1.1"
ROLE_EXPORTS = {
    "student": "SSS_C1_CASE01_STUDENT_MISSION_v1.1.html",
    "teacher": "SSS_C1_CASE01_TEACHER_GUIDE_v1.1.html",
    "answer": "SSS_C1_CASE01_ANSWER_KEY_v1.1.html",
    "accessible": "SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.1.html",
    "grayscale": "SSS_C1_CASE01_GRAYSCALE_MISSION_v1.1.html",
}
TASK_TITLE = re.compile(r"^(\d+) · (.+)$")
TASK_CSS = """.task-heading .section-title {
  font-size: 11.5pt;
  line-height: 1.15;
}
.accessible-page .task-heading .section-title {
  font-size: 14pt;
  line-height: 1.15;
}
"""


def apply_standard(soup: BeautifulSoup) -> None:
    old_meta = soup.select_one('meta[name="sss-task-heading-standard"]')
    if old_meta:
        old_meta.decompose()
    meta = soup.new_tag("meta")
    meta["name"] = "sss-task-heading-standard"
    meta["content"] = "1.0"
    soup.head.append(meta)

    old_style = soup.select_one("#sssTaskHeadingStandardCss")
    if old_style:
        old_style.decompose()
    style = soup.new_tag("style")
    style["id"] = "sssTaskHeadingStandardCss"
    style.string = TASK_CSS
    soup.head.append(style)

    for heading in soup.select(".section-heading"):
        title = heading.select_one(".section-title")
        match = TASK_TITLE.fullmatch(title.get_text(" ", strip=True)) if title else None
        if not match:
            continue
        heading["class"] = sorted(set(heading.get("class", [])) | {"task-heading"})
        heading["data-task-id"] = match.group(1)
        heading["data-task-title"] = match.group(2)

    for callout in soup.select("aside.callout"):
        label = callout.select_one(".technical-label")
        if label and label.get_text(" ", strip=True) == "OPTIONAL EXTENSION":
            callout["class"] = sorted(
                set(callout.get("class", [])) | {"callout-neutral", "optional-extension"}
            )
            callout["data-optional-extension"] = "canonical-v1.0"


def embed_insignia(soup: BeautifulSoup) -> None:
    insignia = REPO / "shared/assets/insignia/saa.svg"
    data = "data:image/svg+xml;base64," + base64.b64encode(insignia.read_bytes()).decode("ascii")
    for image in soup.select("img.saa-insignia,.continuation-header img"):
        image["src"] = data


def make_export(master_text: str, role: str) -> str:
    soup = BeautifulSoup(master_text, "html.parser")
    export_role = "student" if role == "grayscale" else role
    soup.body["data-role"] = export_role
    classes = list(soup.body.get("class", []))
    if role == "grayscale" and "grayscale" not in classes:
        classes.append("grayscale")
    soup.body["class"] = classes
    state = {"role": export_role}
    if role == "grayscale":
        state["grayscale"] = True
    seed = soup.new_tag("script")
    seed.string = (
        "try{localStorage.setItem('sss-case01-v1-1-state',JSON.stringify(%s))}catch(e){}"
        % json.dumps(state)
    )
    soup.body.insert(0, seed)
    for page in list(soup.select(".page")):
        if page.get("data-role") != export_role:
            page.decompose()
    embed_insignia(soup)
    return "<!DOCTYPE html>\n" + str(soup.html)


def main() -> int:
    soup = BeautifulSoup(MASTER.read_text(encoding="utf-8"), "html.parser")
    apply_standard(soup)
    master_text = "<!DOCTYPE html>\n" + str(soup.html)
    MASTER.write_text(master_text, encoding="utf-8")
    print(f"HTML-only task-heading build: {MASTER.relative_to(REPO)}")
    for role, filename in ROLE_EXPORTS.items():
        destination = PUBLISHED / filename
        destination.write_text(make_export(master_text, role), encoding="utf-8")
        print(f"HTML-only role build: {destination.relative_to(REPO)}")
    print("PDF generation: skipped by design")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
