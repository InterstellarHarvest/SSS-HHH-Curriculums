#!/usr/bin/env python3
"""Build the Case 03 v1.1 successor without changing approved v1.0 artifacts."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, Tag

sys.dont_write_bytecode = True


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
HISTORICAL_MASTER = ROOT / "master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html"
HISTORICAL_MASTER_SHA256 = "c97a880f0be0c58848c0d8a7394ce75925aff26f3fb542dc4d63cca25a9b6bce"
V1_CONFIG = ROOT / "source/editor/case03-editor-config.json"
V1_PACKAGE = ROOT / "source/editor-package/case-package.v1.json"
V11_SOURCE = ROOT / "source/editor-v1.1"
V11_CONTENT = V11_SOURCE / "case03-content.html"
V11_CASE_CSS = V11_SOURCE / "case03.css"
V11_CONFIG = V11_SOURCE / "case03-editor-config.json"
V11_PRESENTATION = V11_SOURCE / "case03-presentation.css"
V11_MASTER = ROOT / "master/SSS_C1_CASE03_EDITABLE_MASTER_v1.1.html"
V11_PACKAGE = ROOT / "source/editor-package/case-package.v1.1.json"
V11_MANIFEST = ROOT / "CASE03_V1_1_RELEASE_MANIFEST.json"
V11_CHECKSUMS = ROOT / "validation-artifacts/CASE03_V1_1_HTML_CHECKSUMS.sha256"
ASSEMBLER = REPO / "shared/implementation/editor-shell/v1.0/assemble_editable_master.py"

ROLE_OUTPUTS = {
    "student": "SSS_C1_CASE03_STUDENT_MISSION_v1.1.html",
    "teacher": "SSS_C1_CASE03_TEACHER_GUIDE_v1.1.html",
    "answer": "SSS_C1_CASE03_ANSWER_KEY_v1.1.html",
    "accessible": "SSS_C1_CASE03_ACCESSIBLE_MISSION_v1.1.html",
    "grayscale": "SSS_C1_CASE03_GRAYSCALE_MISSION_v1.1.html",
}
PAGE_COUNTS = {"student": 4, "teacher": 8, "answer": 4, "accessible": 7, "grayscale": 4}
PHRASE_BANK_SOURCE_STAGES = [2, 3, 4, 5]
PHRASE_BANK_DISPLAY_ORDER = [4, 2, 5, 3]
PHRASE_BANK_LABEL = "PHRASE BANK"
PHRASE_BANK_INSTRUCTION = "Use each phrase once."


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def digest(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def require_one(soup: BeautifulSoup | Tag, selector: str) -> Tag:
    matches = soup.select(selector)
    if len(matches) != 1:
        raise ValueError(f"Expected one {selector!r}; found {len(matches)}")
    return matches[0]


def update_accessible_page_identity(page: Tag, number: int, total: int) -> None:
    page["data-page-id"] = f"accessible-mission-{number:02d}"
    page["aria-label"] = f"Accessible Mission page {number} of {total}"
    footer = require_one(page, "[data-publication-footer] span")
    footer.string = f"Accessible Mission {number} of {total}"


def phrase_bank_config() -> dict[str, Any]:
    return {
        "contract": "sequence-v1.0",
        "taskId": 6,
        "sourceRole": "answer",
        "sourceStages": PHRASE_BANK_SOURCE_STAGES,
        "displayOrderSourceStages": PHRASE_BANK_DISPLAY_ORDER,
        "label": PHRASE_BANK_LABEL,
        "instruction": PHRASE_BANK_INSTRUCTION,
        "itemCount": 4,
        "roles": ["student", "answer", "accessible", "grayscale"],
    }


def controlled_answer_phrases(workspace: Tag) -> dict[int, str]:
    process = require_one(workspace, '.page[data-role="answer"] [data-process-contract="five-stage-v1.0"]')
    phrases: dict[int, str] = {}
    for stage_number in PHRASE_BANK_SOURCE_STAGES:
        stage = require_one(process, f'[data-process-stage="{stage_number}"]')
        content = require_one(stage, ".stage-content").get_text(" ", strip=True)
        if not content:
            raise ValueError(f"Controlled Answer Key Stage {stage_number} is blank")
        phrases[stage_number] = content
    if len(set(phrases.values())) != len(PHRASE_BANK_SOURCE_STAGES):
        raise ValueError("Controlled Answer Key Stages 2–5 must contain four unique phrases")
    return phrases


def make_phrase_bank(soup: BeautifulSoup, role: str, page_id: str, phrases: dict[int, str]) -> Tag:
    bank_id = f"{page_id}-task6-phrase-bank"
    instruction_id = f"{bank_id}-instruction"
    bank = soup.new_tag("aside", attrs={
        "class": "canonical-phrase-bank",
        "data-phrase-bank-contract": "sequence-v1.0",
        "data-phrase-bank-task": "6",
        "data-phrase-bank-role": role,
        "aria-labelledby": bank_id,
        "aria-describedby": instruction_id,
    })
    label = soup.new_tag("div", attrs={"class": "canonical-phrase-bank-label", "id": bank_id})
    label.string = PHRASE_BANK_LABEL
    instruction = soup.new_tag("p", attrs={"class": "canonical-phrase-bank-instruction", "id": instruction_id})
    instruction.string = PHRASE_BANK_INSTRUCTION
    items = soup.new_tag("ul", attrs={"class": "canonical-phrase-bank-items"})
    for stage_number in PHRASE_BANK_DISPLAY_ORDER:
        item = soup.new_tag("li", attrs={"class": "canonical-phrase-bank-item", "data-phrase-bank-item": ""})
        item.string = phrases[stage_number]
        items.append(item)
    bank.extend([label, instruction, items])
    return bank


def corrected_content(master_html: str) -> str:
    soup = BeautifulSoup(master_html, "html.parser")
    workspace = require_one(soup, "main#workspace")
    phrases = controlled_answer_phrases(workspace)
    page5 = require_one(workspace, '.page[data-page-id="accessible-mission-05"]')
    page6 = require_one(workspace, '.page[data-page-id="accessible-mission-06"]')
    page5_content = require_one(page5, ".content-area")
    page6_content = require_one(page6, ".content-area")

    task7 = require_one(page5_content, '.task-heading[data-task-id="7"]')
    first_cer = require_one(page5_content, '[data-cer-contract="accessible-v1.0"]')
    second_cer = require_one(page6_content, '[data-cer-contract="accessible-v1.0"]')
    first_labels = [node.get_text(" ", strip=True) for node in first_cer.select(":scope > .canonical-cer-box > .canonical-cer-label")]
    second_labels = [node.get_text(" ", strip=True) for node in second_cer.select(":scope > .canonical-cer-box > .canonical-cer-label")]
    if first_labels != ["CLAIM", "EVIDENCE"] or second_labels != ["REASONING"]:
        raise ValueError(f"Historical Accessible CER split changed: {first_labels!r} / {second_labels!r}")

    # Page 7 starts as an exact copy of historical page 6, minus its detached
    # Reasoning fragment. It retains Tasks 8–9 and the optional extension.
    page7 = copy.deepcopy(page6)
    require_one(page7, '[data-cer-contract="accessible-v1.0"]').decompose()
    update_accessible_page_identity(page7, 7, 7)

    # Page 5 retains the complete five-stage mechanism. Task 7 moves as one
    # heading/root unit to page 6; no response field or instruction is rewritten.
    task7.extract()
    first_cer.extract()
    reasoning_box = require_one(second_cer, ":scope > .canonical-cer-box.reasoning").extract()
    first_cer.append(reasoning_box)
    second_cer.decompose()

    page6_header = require_one(page6_content, ":scope > .continuation-header")
    for child in list(page6_content.children):
        if child is not page6_header:
            child.extract()
    page6_content.append(task7)
    page6_content.append(first_cer)
    page6.insert_after(page7)

    for number in range(1, 7):
        update_accessible_page_identity(
            require_one(workspace, f'.page[data-page-id="accessible-mission-{number:02d}"]'),
            number,
            7,
        )

    accessible_cer = workspace.select('.page[data-role="accessible"] [data-cer-contract="accessible-v1.0"]')
    if len(accessible_cer) != 1:
        raise ValueError(f"Corrected Accessible content must have one CER root; found {len(accessible_cer)}")
    labels = [node.get_text(" ", strip=True) for node in accessible_cer[0].select(":scope > .canonical-cer-box > .canonical-cer-label")]
    if labels != ["CLAIM", "EVIDENCE", "REASONING"]:
        raise ValueError(f"Corrected Accessible CER rows are invalid: {labels!r}")

    for role in ("student", "answer", "accessible"):
        task6 = require_one(workspace, f'.page[data-role="{role}"] .task-heading[data-task-id="6"]')
        page = task6.find_parent("section", class_="page")
        if page is None:
            raise ValueError(f"Task 6 page not found for {role}")
        process = require_one(page, '[data-process-contract="five-stage-v1.0"]')
        process.insert_after(make_phrase_bank(soup, role, page.get("data-page-id", role), phrases))

    teacher_guidance = require_one(workspace, '.page[data-page-id="teacher-guide-03"] p[data-persist-id="teacher-guide-03-instruction-090"]')
    task_references = teacher_guidance.select(":scope > strong.task-reference")
    if [node.get_text(" ", strip=True) for node in task_references] != [
        "6 · Model the mechanism",
        "7 · Claim-Evidence-Reasoning",
    ]:
        raise ValueError("Historical Task 6 teacher references changed")
    guidance_middle = task_references[0].next_sibling
    if str(guidance_middle) != ", require the causal chain. Then complete ":
        raise ValueError(f"Historical Task 6 teacher guidance changed: {guidance_middle!r}")
    guidance_middle.replace_with(
        ", require the causal chain: students sequence the supplied phrases into Stages 2–5 rather than "
        "generate all mechanism wording independently. Then complete "
    )

    return str(workspace) + "\n"


def corrected_case_css(master_html: str) -> str:
    soup = BeautifulSoup(master_html, "html.parser")
    css = require_one(soup, "style#caseStyles").string or ""
    css = css.replace(
        '.page[data-page-id="accessible-mission-06"] .canonical-cer-box.reasoning {\n  min-height: 1.55in;\n}\n',
        '.page[data-page-id="accessible-mission-06"] .canonical-cer[data-cer-contract="accessible-v1.0"] {\n'
        '  min-height: 7.8in;\n  break-inside: avoid;\n  page-break-inside: avoid;\n}\n'
        '.page[data-page-id="accessible-mission-06"] .canonical-cer-box.claim { flex: 1 1 1.35in; }\n'
        '.page[data-page-id="accessible-mission-06"] .canonical-cer-box.evidence,\n'
        '.page[data-page-id="accessible-mission-06"] .canonical-cer-box.reasoning { flex: 2 1 2.45in; }\n',
    )
    css = css.replace('page[data-page-id="accessible-mission-06"] .task-heading', 'page[data-page-id="accessible-mission-07"] .task-heading')
    css = css.replace('page[data-page-id="accessible-mission-06"] .response.large', 'page[data-page-id="accessible-mission-07"] .response.large')
    css = css.replace('page[data-page-id="accessible-mission-06"] .optional-extension', 'page[data-page-id="accessible-mission-07"] .optional-extension')
    return css.rstrip() + "\n"


def v11_config() -> dict[str, Any]:
    config = json.loads(V1_CONFIG.read_text(encoding="utf-8"))
    config.update({
        "documentKey": "SSS-C1-CASE03:v1.1:editor-shell-1.0",
        "title": "SSS C1 Case 03 - Mars Habitat - Editable Master v1.1",
        "pageCounts": PAGE_COUNTS,
        "editedMasterFilename": "SSS_C1_CASE03_EDITABLE_MASTER_v1.1_custom.html",
        "caseCss": "case03.css",
        "content": "case03-content.html",
    })
    config["metadata"].update({
        "sss-curriculum-version": "1.1",
        "sss-status": "validation-build",
        "sss-source-master": "SSS_C1_CASE03_EDITABLE_MASTER_v1.1.html",
        "sss-successor-reason": "accessible-cer-atomicity-and-task6-phrase-bank",
    })
    config["phraseBank"] = phrase_bank_config()
    for role, filename in ROLE_OUTPUTS.items():
        config["outputs"][role]["filename"] = filename
    return config


def load_assembler():
    spec = importlib.util.spec_from_file_location("sss_editor_shell_assembler_v11", ASSEMBLER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load assembler: {ASSEMBLER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def presentation_css(master_html: str) -> str:
    soup = BeautifulSoup(master_html, "html.parser")
    blocks = []
    for selector in ("#sssCurriculumComponentsCss", "#caseStyles", "#sssEditorShellCss", "#sssCerComponentCss"):
        style = require_one(soup, selector)
        blocks.append(style.string or "")
    return "\n\n".join(block.rstrip() for block in blocks) + "\n"


def package_data(content: bytes, case_css: bytes, presentation: bytes, master: bytes) -> dict[str, Any]:
    package = json.loads(V1_PACKAGE.read_text(encoding="utf-8"))
    package.update({
        "version": "1.1",
        "status": "VALIDATION_BUILD",
        "documentKey": "SSS-C1-CASE03:v1.1:curriculum-editor-v1",
    })
    package["content"] = {
        "source": "sss/campaign-1/case-03-mars-habitat/source/editor-v1.1/case03-content.html",
        "format": "html-fragment",
    }
    package["styles"] = [{
        "source": "sss/campaign-1/case-03-mars-habitat/source/editor-v1.1/case03.css",
        "scope": "case",
    }]
    package["rolePageStructure"]["accessible"]["pageCount"] = 7
    package["outputs"] = {
        "complete": "SSS_C1_CASE03_CURRICULUM_EDITOR_v1.1_CUSTOM.html",
        **{role: filename.replace(".html", "_CUSTOM.html") for role, filename in ROLE_OUTPUTS.items()},
    }
    package["migrationSource"] = {
        "kind": "approved-master-successor",
        "historicalMaster": "sss/campaign-1/case-03-mars-habitat/master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html",
        "historicalMasterSha256": HISTORICAL_MASTER_SHA256,
        "successorMaster": "sss/campaign-1/case-03-mars-habitat/master/SSS_C1_CASE03_EDITABLE_MASTER_v1.1.html",
        "successorMasterSha256": digest_bytes(master),
        "reason": "Accessible CER atomicity and Task 6 phrase-bank correction",
        "builder": "sss/campaign-1/case-03-mars-habitat/validation-artifacts/build_case03_v1_1.py",
    }
    package["presentation"] = {
        "contentSha256": digest_bytes(content),
        "caseCssSha256": digest_bytes(case_css),
        "stylesheet": "sss/campaign-1/case-03-mars-habitat/source/editor-v1.1/case03-presentation.css",
        "stylesheetSha256": digest_bytes(presentation),
        "isolation": "shadow-dom",
    }
    package["accessibility"]["documentTitle"] = "SSS Campaign 1 Case 03 v1.1 — Mars Habitat Curriculum Editor"
    package["accessibility"]["loadAnnouncement"] = "Mars Habitat Case 03 v1.1 validation build loaded. Student Mission selected."
    package["phraseBank"] = phrase_bank_config()
    return package


def manifest_data(master: bytes, role_bytes: dict[str, bytes], source_bytes: dict[Path, bytes]) -> dict[str, Any]:
    def artifact(path: Path, value: bytes) -> dict[str, Any]:
        return {
            "path": str(path.relative_to(ROOT)),
            "sha256": digest_bytes(value),
            "bytes": len(value),
        }

    return {
        "case": "SSS-C1-CASE03",
        "title": "Mars Habitat",
        "version": "1.1",
        "status": "VALIDATION_BUILD",
        "release_status": "OWNER_BROWSER_PHYSICAL_PRINT_GATE_OPEN",
        "artifact_policy": "HTML_ONLY",
        "successor_reason": "Accessible CER atomicity and Task 6 phrase-bank correction",
        "historical_v1_0": {
            "master": "master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html",
            "sha256": HISTORICAL_MASTER_SHA256,
            "preservation": "byte-identical approved historical release",
        },
        "current_validation_master": artifact(V11_MASTER, master),
        "page_counts": PAGE_COUNTS,
        "accessible_task_7_page": "accessible-mission-06",
        "task_6_phrase_bank": phrase_bank_config(),
        "physical_print_gate": "OPEN",
        "outputs": {
            role: {"pages": PAGE_COUNTS[role], "html": artifact(ROOT / "published" / ROLE_OUTPUTS[role], value)}
            for role, value in role_bytes.items()
        },
        "generated_sources": [artifact(path, value) for path, value in source_bytes.items()],
    }


def build_outputs(write_prerequisites: bool) -> dict[Path, bytes]:
    if digest(HISTORICAL_MASTER) != HISTORICAL_MASTER_SHA256:
        raise ValueError("Approved Case 03 v1.0 master hash does not match the owner-authorized baseline.")
    historical = HISTORICAL_MASTER.read_text(encoding="utf-8")
    content = corrected_content(historical).encode("utf-8")
    case_css = corrected_case_css(historical).encode("utf-8")
    config = json_bytes(v11_config())

    # The assembler reads these three controlled sources. They are written by
    # the caller before the second build pass and checked byte-for-byte later.
    prerequisites = {V11_CONTENT: content, V11_CASE_CSS: case_css, V11_CONFIG: config}
    if write_prerequisites:
        for path, value in prerequisites.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(value)
    else:
        mismatches = [path for path, value in prerequisites.items() if not path.is_file() or path.read_bytes() != value]
        if mismatches:
            joined = ", ".join(str(path.relative_to(REPO)) for path in mismatches)
            raise ValueError(f"Controlled v1.1 prerequisites differ from extraction: {joined}")

    assembler = load_assembler()
    master_text = assembler.build_master(V11_CONFIG)
    master = master_text.encode("utf-8")
    config_data = json.loads(config)
    role_bytes = {
        role: assembler.build_role(master_text, output["role"], bool(output.get("grayscale")), config_data).encode("utf-8")
        for role, output in config_data["outputs"].items()
    }
    presentation = presentation_css(master_text).encode("utf-8")
    package = json_bytes(package_data(content, case_css, presentation, master))
    sources = {**prerequisites, V11_PRESENTATION: presentation, V11_PACKAGE: package}
    manifest = json_bytes(manifest_data(master, role_bytes, sources))
    checksum_lines = [f"{digest_bytes(master)}  {V11_MASTER.relative_to(REPO)}"]
    checksum_lines.extend(
        f"{digest_bytes(role_bytes[role])}  {(ROOT / 'published' / ROLE_OUTPUTS[role]).relative_to(REPO)}"
        for role in ROLE_OUTPUTS
    )
    checksums = ("\n".join(checksum_lines) + "\n").encode("utf-8")
    return {
        **sources,
        V11_MASTER: master,
        **{ROOT / "published" / ROLE_OUTPUTS[role]: value for role, value in role_bytes.items()},
        V11_MANIFEST: manifest,
        V11_CHECKSUMS: checksums,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed outputs differ from a deterministic rebuild.")
    args = parser.parse_args()
    outputs = build_outputs(write_prerequisites=not args.check)
    failures = []
    for path, value in outputs.items():
        if args.check:
            if not path.is_file() or path.read_bytes() != value:
                failures.append(str(path.relative_to(REPO)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(value)
            print(f"wrote {path.relative_to(REPO)}")
    if failures:
        print("Deterministic v1.1 build mismatch:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    if args.check:
        print(f"Case 03 v1.1 deterministic build: {len(outputs)}/{len(outputs)} PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
