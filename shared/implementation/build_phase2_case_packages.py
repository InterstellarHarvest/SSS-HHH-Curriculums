#!/usr/bin/env python3
"""Deterministically extract approved Case 01/02 central-editor packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, Tag


REPO = Path(__file__).resolve().parents[2]
BUILDER = "shared/implementation/build_phase2_case_packages.py"
SHELL = "shared/implementation/editor-shell/v1.0"
PDF_NOTICE = "Browser PDF export does not guarantee PDF accessibility. Any PDF distributed, published, or archived requires separate accessibility verification."

CASES: dict[str, dict[str, Any]] = {
    "case01": {
        "id": "SSS-C1-CASE01",
        "title": "ISS Greenhouse",
        "subtitle": "Campaign 1 · Case 01 · Low Earth Orbit",
        "location": "International Space Station",
        "version": "1.1",
        "master": "sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.1.html",
        "masterHash": "737239b53ae5af3f25cbaf037d0c9882f50d9e7e8d26b3d03408e469ced6b56f",
        "preMaintenanceHash": "f42365e58802201679b5cd751f102d9a4ecd0ea6f6a6565a860df070018ad02a",
        "reconciliation": "sss/campaign-1/case-01-iss-greenhouse/CASE01_CURRENT_HTML_RECONCILIATION_2026-07-31.json",
        "approvalRecord": "sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/phase2/CASE01_PHASE2_OWNER_APPROVAL_2026-08-01.json",
        "taskSource": "sss/campaign-1/case-01-iss-greenhouse/source/task-registry.js",
        "taskHash": "d01c10a4e286e632f261b831eea5a855c206878bb93f5a449abdfcd561ba2583",
        "sourceDir": "sss/campaign-1/case-01-iss-greenhouse/source/editor-phase2",
        "package": "sss/campaign-1/case-01-iss-greenhouse/source/editor-package/case-package.v1.1.json",
        "prefix": "case01",
        "global": "SSS_CASE01_TASK_REGISTRY",
        "pageCounts": {"student": 3, "teacher": 7, "answer": 3, "accessible": 6, "grayscale": 3},
        "roleNames": {"student": "Student Mission", "teacher": "Teacher Guide", "answer": "Answer Key", "accessible": "Accessible Mission", "grayscale": "Student Mission"},
        "outputs": {
            "complete": "SSS_C1_CASE01_CURRICULUM_EDITOR_v1.1_CUSTOM.html",
            "student": "SSS_C1_CASE01_STUDENT_MISSION_v1.1_CUSTOM.html",
            "teacher": "SSS_C1_CASE01_TEACHER_GUIDE_v1.1_CUSTOM.html",
            "answer": "SSS_C1_CASE01_ANSWER_KEY_v1.1_CUSTOM.html",
            "accessible": "SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.1_CUSTOM.html",
            "grayscale": "SSS_C1_CASE01_GRAYSCALE_MISSION_v1.1_CUSTOM.html",
        },
        "defaultFill": False,
        "controlled": {
            "sss/campaign-1/case-01-iss-greenhouse/source/student-mission-sheet.md": "94257ccab15d26d32e988fe2a04326a394a03c1271a721e843ba238fe508bbd8",
            "sss/campaign-1/case-01-iss-greenhouse/source/lesson-plan.md": "3cabd226b219ed80f4a24cf74aacaacbebab2cba46e2b4b23499a599e9bbd8e7",
            "sss/campaign-1/case-01-iss-greenhouse/source/quick-start.md": "0beb330a3e4ffb9e489d17a043ead43625afc995cd36878e02dbd2cfdca439dd",
            "sss/campaign-1/case-01-iss-greenhouse/source/teacher-case-analysis.md": "30b69ce9f303db0d3a8acdd4e37452c81cd0c0e8842e4ddb315013bf9c3c226f",
            "sss/campaign-1/case-01-iss-greenhouse/source/answer-key.md": "4eac39dc8e895cc117578b3f25de48c0135e91c6376a79f5cc060459048940ca",
            "sss/campaign-1/case-01-iss-greenhouse/source/quick-rubric.md": "a545333f4267e6b29ab32f866946ab3e2fb0f1b3e2bcf410af039515b5201ae8",
            "sss/campaign-1/case-01-iss-greenhouse/source/formal-rubric.md": "b2152d9409a84c967c777c7707a4d2c5e5e8b0ec5992755d7b1feac19bbfda5d",
            "sss/campaign-1/case-01-iss-greenhouse/source/references.md": "b9abbdb23373a8472a74c2ede640639b6829652ce2255e79b58de6056c7c6850",
            "sss/campaign-1/case-01-iss-greenhouse/source/technical-notes.md": "1ca7b33529d5244445abc0f299346dc4273283e609067efe590d1f338267dba9",
        },
    },
    "case02": {
        "id": "SSS-C1-CASE02",
        "title": "Lunar Greenhouse",
        "subtitle": "Campaign 1 · Case 02 · Pollination sequence failure",
        "location": "Lunar Greenhouse",
        "version": "1.0",
        "master": "sss/campaign-1/case-02-lunar-greenhouse/master/SSS_C1_CASE02_EDITABLE_MASTER_v1.0.html",
        "masterHash": "4e5d03a62cba494ae09604194f69578b4c4bcceeeca1f9d53d818109e132fd0d",
        "preMaintenanceHash": "d35c3e0d83a61cbf56799e52b6a1eb3fac4668c1089b674ad0681e92bf30ad86",
        "reconciliation": "sss/campaign-1/case-02-lunar-greenhouse/CASE02_CURRENT_HTML_RECONCILIATION_2026-07-31.json",
        "approvalRecord": "sss/campaign-1/case-02-lunar-greenhouse/validation-artifacts/phase2/CASE02_PHASE2_OWNER_APPROVAL_2026-08-01.json",
        "taskSource": "sss/campaign-1/case-02-lunar-greenhouse/source/task-registry.js",
        "taskHash": "4ac6a5e90d5d3a72ab1734c4458efd34c7d069a14840aa7c98e36a11c994ee1a",
        "sourceDir": "sss/campaign-1/case-02-lunar-greenhouse/source/editor-phase2",
        "package": "sss/campaign-1/case-02-lunar-greenhouse/source/editor-package/case-package.v1.0.json",
        "prefix": "case02",
        "global": "SSS_CASE02_TASK_REGISTRY",
        "pageCounts": {"student": 3, "teacher": 7, "answer": 3, "accessible": 5, "grayscale": 3},
        "roleNames": {"student": "Student Mission", "teacher": "Teacher Packet", "answer": "Answer Key", "accessible": "Accessible Mission", "grayscale": "Student Mission"},
        "outputs": {
            "complete": "SSS_C1_CASE02_CURRICULUM_EDITOR_v1.0_CUSTOM.html",
            "student": "SSS_C1_CASE02_STUDENT_MISSION_v1.0_CUSTOM.html",
            "teacher": "SSS_C1_CASE02_TEACHER_PACKET_v1.0_CUSTOM.html",
            "answer": "SSS_C1_CASE02_ANSWER_KEY_v1.0_CUSTOM.html",
            "accessible": "SSS_C1_CASE02_ACCESSIBLE_MISSION_v1.0_CUSTOM.html",
            "grayscale": "SSS_C1_CASE02_GRAYSCALE_MISSION_v1.0_CUSTOM.html",
        },
        "defaultFill": True,
        "controlled": {
            "sss/campaign-1/case-02-lunar-greenhouse/source/student-mission-sheet.md": "f50cda3f2697dd9d546fadc14ace6ada5832a60491390e3fe2706d7ca8cdcb71",
            "sss/campaign-1/case-02-lunar-greenhouse/source/lesson-plan.md": "ef2f3da0e68ce1a5311e8c29f9d21b37cb57f3b79006b343512738c24b68dbd3",
            "sss/campaign-1/case-02-lunar-greenhouse/source/quick-start.md": "94c68ab69b30bd41295a7d1dd657509f5244d3e20b553280bf7f06ab7e069974",
            "sss/campaign-1/case-02-lunar-greenhouse/source/teacher-case-analysis.md": "8b76270c2e467f779c5600c32e7a29280e02de2053375023efbf7d1a620e10cd",
            "sss/campaign-1/case-02-lunar-greenhouse/source/answer-key.md": "0cfe5eb9ceacdf9118b607f4707600b5da97ac98049ac25d1ac7358f197918c5",
            "sss/campaign-1/case-02-lunar-greenhouse/source/quick-rubric.md": "4ffa261d51615328d52c129563c4bb1a1e958a2c45c4d815c843ec967e463363",
            "sss/campaign-1/case-02-lunar-greenhouse/source/formal-rubric.md": "4e32ebff501a557a1161ff8d1bb42c59ab3f2994245c1d3e7f101b3da9c15efc",
            "sss/campaign-1/case-02-lunar-greenhouse/source/references.md": "c7a71843afc111278a568360260dd782fd19f92e5faef7a56023a5c22e0b76c6",
            "sss/campaign-1/case-02-lunar-greenhouse/source/technical-notes.md": "ef0c00bc716321f5566f28c0157bcf42f5896c5e6f004673794d7c0b4a609e39",
            "sss/campaign-1/case-02-lunar-greenhouse/source/figure-research-and-rights.md": "6107f2a902b745df062e4d2c2af298861a19047017e68d3a70772633a876dccf",
        },
    },
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def verify_inputs(config: dict[str, Any]) -> bytes:
    master = (REPO / config["master"]).read_bytes()
    if sha(master) != config["masterHash"]:
        raise ValueError(f"{config['id']} approved master hash changed")
    protected = {config["taskSource"]: config["taskHash"], **config["controlled"]}
    for path, expected in protected.items():
        actual = sha((REPO / path).read_bytes())
        if actual != expected:
            raise ValueError(f"{config['id']} protected input changed: {path}: {actual}")
    return master


def assign_case01_persistence(main: Tag) -> None:
    for page in main.select(".page[data-page-id]"):
        editable_number = 0
        response_number = 0
        for node in page.select("[data-editable]"):
            editable_number += 1
            node["data-persist-id"] = f"{page['data-page-id']}-e{editable_number}"
        for node in page.select("[data-response]"):
            response_number += 1
            node["data-persist-id"] = node.get("data-field") or f"{page['data-page-id']}-r{response_number}"


def task_data(config: dict[str, Any], soup: BeautifulSoup) -> list[dict[str, Any]]:
    source = (REPO / config["taskSource"]).read_text()
    titles = {int(number): title for number, title in re.findall(r'id:\s*(\d+).*?title:\s*"([^"]+)"', source)}
    tasks = []
    for number in range(1, 10):
        heading = soup.select_one(f'.task-heading[data-task-id="{number}"]')
        if heading is None or number not in titles:
            raise ValueError(f"{config['id']} canonical Task {number} missing")
        label = heading.select_one(".technical-label")
        use = heading.select_one("use[href]")
        tasks.append({
            "number": number,
            "semanticLabel": label.get_text(" ", strip=True) if label else "TASK",
            "title": titles[number],
            "icon": (use.get("href") or "#ph-book").lstrip("#") if use else "ph-book",
        })
    return tasks


def build_case(config: dict[str, Any]) -> dict[Path, bytes]:
    master = verify_inputs(config)
    soup = BeautifulSoup(master.decode(), "html.parser")
    main = soup.find("main")
    if main is None:
        raise ValueError(f"{config['id']} worksheet main missing")
    if config["prefix"] == "case01":
        assign_case01_persistence(main)
    content = (str(main) + "\n").encode()
    css = "\n\n".join((style.string or "").rstrip() for style in soup.find_all("style")) + "\n"
    if config["prefix"] == "case01":
        css += """
/* Phase 2 legacy-shell adapter; default values preserve approved geometry. */
.page-frame{top:var(--margin-top);right:var(--margin-right);bottom:var(--margin-bottom);left:var(--margin-left);inset:var(--margin-top) var(--margin-right) var(--margin-bottom) var(--margin-left)}
.density-compact{--density:.82}.density-spacious{--density:1.18}.hide-boundaries .page{box-shadow:none}.page.has-overflow .overflow-warning{display:block}
.toolbar-group{display:flex;flex-wrap:wrap;align-items:end;gap:.35rem;padding-right:.65rem;border-right:1px solid rgba(255,255,255,.22)}
"""
    presentation = css.encode()
    sprite = soup.body.find("svg", class_="visually-hidden") or soup.body.find("svg")
    if sprite is None:
        raise ValueError(f"{config['id']} icon sprite missing")
    icons = (str(sprite) + "\n").encode()
    tasks = task_data(config, soup)
    registry = json_bytes({"schemaVersion": 1, "case": config["id"], "tasks": tasks, "roles": ["student", "teacher", "answer", "accessible"]})
    registry = f"window.{config['global']} = ".encode() + registry.rstrip() + b";\n"
    source_dir = config["sourceDir"]
    content_path = f"{source_dir}/{config['prefix']}-content.html"
    css_path = f"{source_dir}/{config['prefix']}-presentation.css"
    icons_path = f"{source_dir}/{config['prefix']}-icons.svg"
    tasks_path = f"{source_dir}/{config['prefix']}-task-registry.js"
    roles = {}
    for role in ["student", "teacher", "answer", "accessible", "grayscale"]:
        roles[role] = {
            "sourceRole": "student" if role == "grayscale" else role,
            "documentRole": config["roleNames"][role],
            "pageCount": config["pageCounts"][role],
            "grayscale": role == "grayscale",
        }
    package = {
        "schemaVersion": 1,
        "id": config["id"],
        "curriculum": "SSS",
        "campaign": "campaign-1",
        "title": config["title"],
        "subtitle": config["subtitle"],
        "location": config["location"],
        "version": config["version"],
        "status": "APPROVED_WITH_HTML_MAINTENANCE",
        "institutionalIdentity": {"id": "SAA", "name": "Solar Agricultural Agency", "lockupLines": ["Solar", "Agricultural", "Agency"], "insigniaSelector": ".saa-insignia"},
        "documentKey": f"{config['id']}:v{config['version']}:curriculum-editor-v1",
        "supportedRoles": ["student", "teacher", "answer", "accessible", "grayscale"],
        "defaultRole": "student",
        "shell": {"version": "1.0", "toolbar": f"{SHELL}/toolbar.html", "styles": [f"{SHELL}/curriculum-components.css", f"{SHELL}/editor-shell.css", f"{SHELL}/cer.css"], "icons": icons_path},
        "taskRegistry": {"source": tasks_path, "global": config["global"], "schemaVersion": 1},
        "content": {"source": content_path, "format": "html-fragment"},
        "styles": [{"source": css_path, "scope": "case"}],
        "assets": [
            {"id": f"{config['prefix']}-icon-sprite", "type": "image/svg+xml", "source": icons_path, "embed": True},
            ({"id": "saa-insignia", "type": "image/svg+xml", "source": "shared/assets/insignia/saa.svg", "selector": ".saa-insignia", "embed": True}
             if config["prefix"] == "case01" else
             {"id": "saa-insignia", "type": "inline-svg", "selector": ".saa-insignia", "embed": True}),
        ],
        "rolePageStructure": roles,
        "outputs": config["outputs"],
        "defaultToolbarState": {"role": "student", "fillMode": config["defaultFill"], "editMode": False, "marginTop": .5, "marginRight": .5, "marginBottom": .5, "marginLeft": .5, "density": "normal", "grayscale": False, "guides": False, "boundaries": True},
        "accessibility": {"language": "en", "documentTitle": f"SSS Campaign 1 {config['id'][-6:]} v{config['version']} — {config['title']} Curriculum Editor", "loadAnnouncement": f"{config['title']} {config['id'][-6:].replace('CASE', 'Case ')} v{config['version']} maintained HTML package loaded. Student Mission selected.", "extendedDescriptionSelectors": ["figure figcaption", "[aria-label]"], "pdfNotice": PDF_NOTICE},
        "migrationSource": {"kind": "approved-master-migration", "historicalMaster": config["master"], "historicalMasterSha256": config["masterHash"], "successorMaster": config["master"], "successorMasterSha256": config["masterHash"], "goldenMaster": config["master"], "goldenMasterSha256": config["masterHash"], "preMaintenanceMasterSha256": config["preMaintenanceHash"], "reconciliationRecord": config["reconciliation"], "reason": "Exact owner-authorized maintained-HTML migration; no curriculum successor version created", "builder": BUILDER},
        "phase2Authorization": {
            "htmlMaintenanceRevision": "2026-07-31",
            "reconciliationRecord": config["reconciliation"],
            "ownerAuthorizationDate": "2026-07-31",
            "approvalRecord": config["approvalRecord"],
            "approvalDate": "2026-08-01",
            "owner": "Nate / Owner",
            "status": "APPROVED",
            "phase2Status": "READY_TO_MERGE",
            "ownerGate": "PASS",
            "ownerReview": "PASS",
            "browserPrintPreview": "PASS",
            "physicalPrintGate": "PASS",
            "physicalPrintReview": "PASS",
            "phase2MigrationParity": "PASS",
            "scale": "100% / Actual Size",
            "browser": "Not recorded",
            "printerCopier": "Not recorded",
            "paper": "Not recorded",
            "artifactPolicy": {
                "historicalPdfs": "RETAINED",
                "currentProduction": "HTML_BASED",
                "newPdfsGenerated": False,
            },
        },
        "presentation": {"contentSha256": sha(content), "caseCssSha256": sha(presentation), "stylesheet": css_path, "stylesheetSha256": sha(presentation), "isolation": "shadow-dom"},
    }
    return {
        REPO / content_path: content,
        REPO / css_path: presentation,
        REPO / icons_path: icons,
        REPO / tasks_path: registry,
        REPO / config["package"]: json_bytes(package),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--case", choices=["case01", "case02", "all"], default="all")
    args = parser.parse_args()
    selected = CASES if args.case == "all" else {args.case: CASES[args.case]}
    outputs: dict[Path, bytes] = {}
    for config in selected.values():
        outputs.update(build_case(config))
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
        print("Deterministic Phase 2 package mismatch:")
        print("\n".join(f"- {path}" for path in failures))
        return 1
    if args.check:
        print(f"Phase 2 deterministic extraction: {len(outputs)}/{len(outputs)} PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
