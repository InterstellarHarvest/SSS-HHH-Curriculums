#!/usr/bin/env python3
"""Final SSS remediation transformer v4 — Accessible and digital-action wave.

This wave implements only adaptations explicitly supported by the accepted final
case audits. It does not chase raw response-count warnings where classification
or comparison itself is the learning target.

Changes include:
- selected worked/prefilled Accessible responses on dense comparison/model tasks;
- a modeled row in the recurring five-source contribution/limit task family;
- explicit persisted best-diagnosis fields where late C1 packets only said
  "circle" while providing no independent digital final-choice state;
- separate persisted stage-status controls for The Gift Task 4 X marks;
- Hayes Accessible Task 7 restored to two guided fields;
- the Hayes Teacher page-count statement corrected from six to seven pages.

Approved page counts and CER contracts are preserved.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup, Tag

import apply_sss_final_remediation as v1
import apply_sss_final_remediation_v2 as v2
import apply_sss_final_remediation_v3 as v3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_case(case_dir: Path, soup: BeautifulSoup, package: dict) -> None:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    content_path.write_text(soup.decode(formatter="minimal"), encoding="utf-8")
    if "sourceHashes" in package and "content" in package["sourceHashes"]:
        package["sourceHashes"]["content"] = sha256(content_path)
    package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def prefill(soup: BeautifulSoup, persist_id: str, value: str) -> bool:
    node = soup.find(attrs={"data-persist-id": persist_id})
    if not isinstance(node, Tag) or not node.has_attr("data-response"):
        return False
    if node.get("data-prefilled") == "final-audit-accessible-v1.0":
        return False
    # Preserve any earlier intentional final-audit prefill rather than replacing it.
    if node.get("data-prefilled"):
        return False
    node["data-prefilled"] = "final-audit-accessible-v1.0"
    node["data-accessible-scaffold"] = "modeled-or-partial"
    node.clear()
    node.append(value)
    return True


def find_task_heading(soup: BeautifulSoup, role: str, task: int) -> Tag | None:
    return soup.select_one(f'[data-role="{role}"] [data-task-id="{task}"]') or soup.select_one(
        f'[data-role="{role}"] [data-shell-task-heading="{task}"]'
    )


def add_best_diagnosis_field(soup: BeautifulSoup, role: str, task: int, persist_id: str) -> bool:
    if soup.find(attrs={"data-persist-id": persist_id}):
        return False
    heading = find_task_heading(soup, role, task)
    if not heading:
        return False
    page = heading.find_parent(attrs={"data-role": role})
    if not page:
        return False

    anchor = None
    for candidate in heading.find_all_next(["table", "div"], limit=30):
        if candidate.find_parent(attrs={"data-role": role}) != page:
            break
        classes = set(candidate.get("class") or [])
        if "diagnosis-table" in classes or "diagnosis-cards" in classes:
            anchor = candidate
            break
    if anchor is None:
        return False

    block = BeautifulSoup(
        f'''<div class="response-block final-diagnosis-choice" data-final-diagnosis-choice="v1.0"><span class="response-label">Best-supported diagnosis</span><div aria-label="Task {task} best-supported diagnosis" class="response short" data-persist-id="{persist_id}" data-response="" role="textbox"></div></div>''',
        "html.parser",
    ).div
    anchor.insert_after(block)

    # Replace print-only wording where it appears in the same task page.
    for node in list(page.find_all(string=True)):
        text = str(node)
        new = re.sub(
            r"Circle the (?:one )?(?:diagnosis|best-supported diagnosis)(?: best supported by all four channels)?\.?",
            "Record the best-supported diagnosis in the field below.",
            text,
            flags=re.I,
        )
        if new != text:
            node.replace_with(new)
    return True


def add_gift_stage_status_controls(soup: BeautifulSoup, role: str) -> bool:
    prefix = "a" if role == "accessible" else "t"
    if soup.find(attrs={"data-persist-id": f"{prefix}4-status-1"}):
        return False
    heading = find_task_heading(soup, role, 4)
    if not heading:
        return False
    page = heading.find_parent(attrs={"data-role": role})
    model = page.select_one('[data-process-contract="source-receptor-response-v1.0"], [data-process-contract="accessible-source-receptor-response-v1.0"]')
    if not model:
        return False
    stages = model.select(".model-stage")
    if len(stages) != 6:
        return False
    for idx, stage in enumerate(stages, start=1):
        holder = BeautifulSoup(
            f'''<div class="stage-status final-stage-status" data-stage-status="v1.0"><span class="small">Status</span><span aria-label="Task 4 stage {idx} status — AVAILABLE or X MISSING" class="compact-response" data-persist-id="{prefix}4-status-{idx}" data-response="" role="textbox"></span></div>''',
            "html.parser",
        ).div
        stage.append(holder)
    return True


def remediate_c1c2(soup: BeautifulSoup) -> list[str]:
    ops = []
    for pid, value in {
        "response-accessible-task3-step1": "viable pollen in anthers",
        "response-accessible-task3-step6": "fruit set",
        "response-accessible-task5-regolith-class": "Weakened",
        "response-accessible-task5-regolith-reason": "Roots and vegetative growth are healthy; broad regolith toxicity does not explain pollen staying on the anthers.",
        "response-accessible-task5-pollination-class": "Supported",
    }.items():
        if prefill(soup, pid, value):
            ops.append(pid)
    return ops


def remediate_c1c4(soup: BeautifulSoup) -> list[str]:
    ops = []
    if prefill(soup, "a5-2", "excessive daily light dose under current operating conditions"):
        ops.append("a5-2")

    # Restore the same two conceptual response slots used by the Student edition.
    node = soup.find(attrs={"data-persist-id": "a7"})
    if isinstance(node, Tag) and not soup.find(attrs={"data-persist-id": "a7-longterm"}):
        node["aria-label"] = "Accessible Task 7 immediate recovery action"
        label = BeautifulSoup('<span class="response-label" data-final-c1c4-a7="v1.0">Immediate recovery action</span>', "html.parser").span
        node.insert_before(label)
        second = BeautifulSoup(
            '''<span class="response-label" data-final-c1c4-a7="v1.0">Long-term independent control</span><div aria-label="Accessible Task 7 long-term independent control" class="response medium" data-persist-id="a7-longterm" data-response="" role="textbox"></div><div class="alt-support" data-final-c1c4-a7="v1.0">Sentence starters: “Right now, crews should …” · “For long-term control, the reactor should …”</div>''',
            "html.parser",
        )
        anchor: Tag = node
        for child in list(second.contents):
            anchor.insert_after(child)
            if isinstance(child, Tag):
                anchor = child
        ops.append("split-a7")

    # Correct the actual stale Teacher note documented by the accepted audit.
    for page in soup.select('[data-role="teacher"]'):
        for text_node in list(page.find_all(string=True)):
            text = str(text_node)
            new = re.sub(r"six-page Accessible Mission", "seven-page Accessible Mission", text, flags=re.I)
            if new != text:
                text_node.replace_with(new)
                ops.append("teacher-accessible-page-count")
    return ops


def remediate_c1c5(soup: BeautifulSoup) -> list[str]:
    ops = []
    for pid, value in {
        "a5-2": "interactions may produce modeled secondary radiation",
        "a5-4": "exposure is possible, but exposure alone does not prove damage",
    }.items():
        if prefill(soup, pid, value):
            ops.append(pid)
    if add_best_diagnosis_field(soup, "student", 4, "t4-best"):
        ops.append("student-best-diagnosis")
    if add_best_diagnosis_field(soup, "accessible", 4, "a4-best"):
        ops.append("accessible-best-diagnosis")
    return ops


def remediate_c1c6(soup: BeautifulSoup) -> list[str]:
    ops = []
    if prefill(soup, "a5-damage", "CONFLICT — the network structures are inert but not visibly damaged, so physical docking damage fits poorly."):
        ops.append("a5-damage")
    if prefill(soup, "a6-disable", "UNSAFE — disabling all atmospheric processing would weaken pressure, breathable-gas, and contaminant protection."):
        ops.append("a6-disable")
    if add_best_diagnosis_field(soup, "student", 5, "t5-best"):
        ops.append("student-best-diagnosis")
    if add_best_diagnosis_field(soup, "accessible", 5, "a5-best"):
        ops.append("accessible-best-diagnosis")
    return ops


def remediate_c1c7(soup: BeautifulSoup) -> list[str]:
    ops = []
    if add_gift_stage_status_controls(soup, "student"):
        ops.append("student-stage-status")
    if add_gift_stage_status_controls(soup, "accessible"):
        ops.append("accessible-stage-status")
    for pid, value in {
        "a4-source": "healthy mature network (source)",
        "a4-status-1": "X — MISSING",
        "a5-light": "CONFLICT — the fictional light spectrum already matches its target tolerance.",
        "a7-monitor": "Monitor cue identity and containment. I would stop if ________________________________.",
    }.items():
        if prefill(soup, pid, value):
            ops.append(pid)
    if add_best_diagnosis_field(soup, "student", 5, "t5-best"):
        ops.append("student-best-diagnosis")
    if add_best_diagnosis_field(soup, "accessible", 5, "a5-best"):
        ops.append("accessible-best-diagnosis")
    return ops


# Recurring five-source task family. Source 1 is fully modeled; Source 3 gets
# one extra modeled contribution where the first wave did not already supply it.
FIVE_SOURCE_PREFILLS = {
    "SSS-C2-CASE01": {
        "a5-c1": "The botanist reports what the crop is doing and what was changed across plantings.",
        "a5-l1": "A midpoint-only account cannot identify the difference across the full bed, and present readings are not completed tests.",
        "a5-c3": "The specimen shows that deformation increases with tuber diameter and curves sideways.",
        "a6-d1": "B — best supported",
    },
    "SSS-C2-CASE02": {
        "a5-c1": "Miran-sel reports that buds form and abort while the plant stays healthy, and can confirm an independently reached conclusion.",
        "a5-l1": "The cultural boundary prevents Miran-sel from supplying the mechanism first.",
        "a5-c3": "The specimen shows mature viable pollen retained behind pores that are already present.",
        "a6-d1": "B — best supported",
    },
    "SSS-C2-CASE03": {
        "a5-c1": "The aquaculturist establishes that the species and water conditions held while decline began after the fixture change.",
        "a5-l1": "The interview does not identify spectrum as the mechanism by itself.",
        "a5-c3": "The specimen shows intact photosynthetic structures and a pigment suite measured to harvest blue-green wavelengths efficiently.",
    },
    "SSS-C2-CASE04": {
        "a5-c1": "Vess-lor establishes a two-year healthy baseline and a gradual fade after the light-schedule change.",
        "a5-l1": "An account of what changed is not a measurement of what the change did.",
        "a5-c3": "The grove examination shows closed rather than damaged release structures, an intact receiver, and a normal vine reflex.",
    },
    "SSS-C2-CASE05": {
        "a4-c1": "Kel-tor establishes the transplant timeline and that every adjustable vault variable was changed without improving production.",
        "a4-l1": "This is experience and suspicion, not a measurement of the cause.",
        "a4-c3": "The specimen shows healthy tissue and a pathway that is present but quiescent.",
        "a5-m3": "the repair pathway stays switched off",
    },
    "SSS-C2-CASE06": {
        "a4-c1": "Dr. Nova establishes the forty-year restoration history, different bed origins, and the conventional fixes already ruled out.",
        "a4-l1": "She measured no living soil community, so the eliminated fixes do not identify what remains.",
        "a4-c3": "Kess supplies the candidate mechanism: compatible root-fungus partnerships can help acquire phosphorus, nitrogen, or water.",
    },
}


def remediate_c2(soup: BeautifulSoup, case_id: str) -> list[str]:
    ops = []
    for pid, value in FIVE_SOURCE_PREFILLS.get(case_id, {}).items():
        if prefill(soup, pid, value):
            ops.append(pid)
    # C2 Case 06 already has the pH rejection modeled by v1; keep candidate
    # selection learner-owned as required by the audit.
    return ops


def apply_wave4(case_id: str, case_dir: Path, apply: bool) -> tuple[bool, list[str]]:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    original = content_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(original, "html.parser")

    if case_id == "SSS-C1-CASE02":
        ops = remediate_c1c2(soup)
    elif case_id == "SSS-C1-CASE04":
        ops = remediate_c1c4(soup)
    elif case_id == "SSS-C1-CASE05":
        ops = remediate_c1c5(soup)
    elif case_id == "SSS-C1-CASE06":
        ops = remediate_c1c6(soup)
    elif case_id == "SSS-C1-CASE07":
        ops = remediate_c1c7(soup)
    elif case_id.startswith("SSS-C2-"):
        ops = remediate_c2(soup, case_id)
    else:
        ops = []

    changed = soup.decode(formatter="minimal") != original
    if changed and apply:
        package = json.loads(package_path.read_text(encoding="utf-8"))
        write_case(case_dir, soup, package)
    return changed, ops


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

        # Preserve all earlier deterministic waves first.
        changed1, operations = v1.remediate_case(case_id, case_dir, args.apply)
        normalized = case_id == "SSS-C1-CASE03" and v2.normalize_case03_alternative_block(case_dir, args.apply)
        changed3 = False
        if case_id == "SSS-C1-CASE03":
            changed3 = v3.remediate_case03_procedure(case_dir, args.apply)
        elif case_id == "SSS-C1-CASE04":
            changed3 = v3.remediate_case04_teacher(case_dir, args.apply)

        changed4, ops4 = apply_wave4(case_id, case_dir, args.apply)
        net = bool(changed1 or normalized or changed3 or changed4)
        changed_cases += int(net)
        print(f"{case_id}: {'CHANGE' if net else 'NO CHANGE'}")
        for op in operations:
            print(f"  - {op}")
        for op in ops4:
            print(f"  - accessible/digital: {op}")

    print(f"SSS final remediation v4: {'applied' if args.apply else 'planned'}; {changed_cases} case package(s) changed/planned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
