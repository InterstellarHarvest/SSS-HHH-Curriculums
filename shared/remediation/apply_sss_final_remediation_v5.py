#!/usr/bin/env python3
"""Final SSS remediation transformer v5.

Builds on v4 and closes the one audit-backed digital-choice insertion that could
not be expressed by the generic diagnosis-table helper: The Gift Accessible
Task 5 uses four source cards rather than a diagnosis table, so its final
best-supported diagnosis needs an explicit persisted field after those cards.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from bs4 import BeautifulSoup, Tag

import apply_sss_final_remediation as v1
import apply_sss_final_remediation_v2 as v2
import apply_sss_final_remediation_v3 as v3
import apply_sss_final_remediation_v4 as v4


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add_gift_accessible_best_choice(case_dir: Path, apply: bool) -> bool:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    original = content_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(original, "html.parser")
    if soup.find(attrs={"data-persist-id": "a5-best"}):
        return False

    heading = soup.select_one('[data-role="accessible"] [data-shell-task-heading="5"]')
    if not heading:
        raise RuntimeError("The Gift Accessible Task 5 heading not found")
    page = heading.find_parent(attrs={"data-role": "accessible"})
    if not page:
        raise RuntimeError("The Gift Accessible Task 5 page not found")

    source_cards = []
    for card in heading.find_all_next("section", class_="source-card"):
        if card.find_parent(attrs={"data-role": "accessible"}) != page:
            break
        source_cards.append(card)
    if len(source_cards) < 4:
        raise RuntimeError("The Gift Accessible Task 5 diagnosis source cards not found")

    block = BeautifulSoup(
        '''<div class="response-block final-diagnosis-choice" data-final-diagnosis-choice="v1.0"><span class="response-label">Best-supported diagnosis</span><div aria-label="Accessible Task 5 best-supported diagnosis" class="response short" data-persist-id="a5-best" data-response="" role="textbox"></div></div>''',
        "html.parser",
    ).div
    source_cards[-1].insert_after(block)

    for text_node in list(page.find_all(string=True)):
        text = str(text_node)
        if "Circle the best-supported diagnosis" in text:
            text_node.replace_with(text.replace("Circle the best-supported diagnosis", "Record the best-supported diagnosis in the field below"))
        elif "Circle the diagnosis best supported by all four channels" in text:
            text_node.replace_with(text.replace("Circle the diagnosis best supported by all four channels", "Record the diagnosis best supported by all four channels in the field below"))

    if apply:
        content_path.write_text(soup.decode(formatter="minimal"), encoding="utf-8")
        package = json.loads(package_path.read_text(encoding="utf-8"))
        if "sourceHashes" in package and "content" in package["sourceHashes"]:
            package["sourceHashes"]["content"] = sha256(content_path)
        package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--case", action="append", dest="cases")
    args = parser.parse_args()

    selected = args.cases or list(v1.CASE_DIRS)
    changed_cases = 0
    for case_id in selected:
        case_dir = v1.CASE_DIRS.get(case_id)
        if case_dir is None:
            print(f"ERROR unknown case id: {case_id}")
            return 2

        changed1, operations = v1.remediate_case(case_id, case_dir, args.apply)
        normalized = case_id == "SSS-C1-CASE03" and v2.normalize_case03_alternative_block(case_dir, args.apply)
        changed3 = False
        if case_id == "SSS-C1-CASE03":
            changed3 = v3.remediate_case03_procedure(case_dir, args.apply)
        elif case_id == "SSS-C1-CASE04":
            changed3 = v3.remediate_case04_teacher(case_dir, args.apply)
        changed4, ops4 = v4.apply_wave4(case_id, case_dir, args.apply)
        changed5 = case_id == "SSS-C1-CASE07" and add_gift_accessible_best_choice(case_dir, args.apply)

        net = bool(changed1 or normalized or changed3 or changed4 or changed5)
        changed_cases += int(net)
        print(f"{case_id}: {'CHANGE' if net else 'NO CHANGE'}")
        for op in operations:
            print(f"  - {op}")
        for op in ops4:
            print(f"  - accessible/digital: {op}")
        if changed5:
            print("  - accessible/digital: added persisted The Gift Task 5 final diagnosis field")

    print(f"SSS final remediation v5: {'applied' if args.apply else 'planned'}; {changed_cases} case package(s) changed/planned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
