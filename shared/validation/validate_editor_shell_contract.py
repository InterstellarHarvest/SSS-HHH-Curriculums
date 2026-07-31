#!/usr/bin/env python3
"""Validate an assembled editable master against the canonical shared shell."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup


REPO = Path(__file__).resolve().parents[2]
SHELL = REPO / "shared/implementation/editor-shell/v1.0"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized_text(node: Any) -> str:
    return " ".join(node.get_text(" ", strip=True).split())


def validate(config_path: Path, master_path: Path, registry_path: Path) -> dict[str, Any]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    contract_path = SHELL / "editor-shell.contract.json"
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    master_text = master_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(master_text, "html.parser")
    assertions: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: str = "") -> None:
        assertions.append({"name": name, "pass": bool(condition), "detail": detail})

    check("config targets shell 1.0", config.get("shellVersion") == contract["shellVersion"])
    output_policy = contract.get("outputPolicy", {})
    check("shell canonical output format is HTML", output_policy.get("canonicalFormat") == "HTML")
    check("shell workflow does not generate PDFs", output_policy.get("workflowGeneratesPdf") is False)
    check("browser print remains available", output_policy.get("browserPrintAvailable") is True)
    check(
        "browser PDF accessibility is not guaranteed",
        output_policy.get("browserPdfAccessibilityGuaranteed") is False,
    )
    check(
        "distributed manual PDFs require accessibility verification",
        output_policy.get("manualPdfDistributionRequiresAccessibilityVerification") is True,
    )
    shell_meta = soup.select_one('meta[name="sss-editor-shell"]')
    check("master declares shell version", shell_meta is not None and shell_meta.get("content") == "1.0")
    contract_meta = soup.select_one('meta[name="sss-editor-shell-contract-sha256"]')
    check(
        "master declares exact contract hash",
        contract_meta is not None and contract_meta.get("content") == sha256(contract_path),
    )

    asset_specs = [
        ("components", SHELL / "curriculum-components.css", "#sssCurriculumComponentsCss"),
        ("css", SHELL / "editor-shell.css", "#sssEditorShellCss"),
        ("cer", SHELL / "cer.css", "#sssCerComponentCss"),
    ]
    for label, source, selector in asset_specs:
        embedded = soup.select_one(selector)
        check(f"{label} asset is embedded", embedded is not None)
        if embedded is not None:
            check(
                f"{label} source hash attribute matches",
                embedded.get("data-source-sha256") == sha256(source),
            )
            check(
                f"{label} embedded bytes match shared source",
                (embedded.string or "") == source.read_text(encoding="utf-8"),
            )

    runtime_source_path = SHELL / "editor-shell.js"
    embedded_runtime = soup.select_one("#sssEditorShellRuntime")
    check("runtime asset is embedded", embedded_runtime is not None)
    if embedded_runtime is not None:
        check(
            "runtime source hash attribute matches",
            embedded_runtime.get("data-source-sha256") == sha256(runtime_source_path),
        )
        expected_runtime = (
            runtime_source_path.read_text(encoding="utf-8")
            .replace("sss-c1-case02-v1-state", f'{config["documentKey"]}:state')
            .replace("sss-c1-case02-v1-content", f'{config["documentKey"]}:content')
            .replace("SSS_C1_CASE02_EDITABLE_MASTER_v1.0_CUSTOM.html", config["editedMasterFilename"])
            .replace("window.__case02", "window.__case03")
        )
        check("runtime differs from Case 02 only by case identity constants", (embedded_runtime.string or "") == expected_runtime)

    icon_source = (SHELL / "icons.svg").read_text(encoding="utf-8")
    toolbar_source = BeautifulSoup((SHELL / "toolbar.html").read_text(encoding="utf-8"), "html.parser")
    check("shared icon sprite is embedded exactly", icon_source in master_text)
    toolbar = soup.select_one(".toolbar")
    check("canonical toolbar is present", toolbar is not None)
    if toolbar is not None:
        actual_controls = [node.get("id") for node in toolbar.select("[id]")]
        check(
            "toolbar controls follow contract order",
            actual_controls == contract["toolbar"]["controlOrder"],
            f"actual={actual_controls}",
        )
        source_controls = [node.get("id") for node in toolbar_source.select("[id]")]
        check("toolbar markup is the shared source", str(toolbar) == str(toolbar_source.select_one(".toolbar")))
        reference_path = REPO / contract["toolbar"]["literalReference"]
        reference_toolbar = BeautifulSoup(reference_path.read_text(encoding="utf-8"), "html.parser").select_one(".toolbar")
        check("toolbar HTML is identical to Case 02", str(toolbar) == str(reference_toolbar))
        for control_id, expected_label in contract["toolbar"]["labels"].items():
            node = toolbar.select_one(f"#{control_id}")
            if node is None:
                check(f"{control_id} exists for label check", False)
                continue
            label = node.find_parent("label")
            actual_label = normalized_text(label or node)
            check(
                f"{control_id} uses canonical label",
                expected_label in actual_label,
                f"actual={actual_label}",
            )
        reference_script = BeautifulSoup(reference_path.read_text(encoding="utf-8"), "html.parser").select_one("script:not([id])")
        check("shared toolbar runtime source is identical to Case 02", runtime_source_path.read_text(encoding="utf-8").strip() == (reference_script.string or "").strip())

    runtime_text = (soup.select_one("#sssEditorShellRuntime").string or "") if soup.select_one("#sssEditorShellRuntime") else ""
    for method in contract["requiredRuntimeApi"]:
        check(f"runtime exposes {method}", method in runtime_text)

    check("no unexpanded task placeholders remain", not soup.select("[data-shell-task-heading]"))
    task_map = {str(item["number"]): item for item in config["tasks"]}
    headings = soup.select(".task-heading[data-task-id]")
    check("task headings are present", bool(headings), f"count={len(headings)}")
    allowed_labels = set(contract["taskHeading"]["allowedSemanticLabels"])
    for index, heading in enumerate(headings, 1):
        number = heading.get("data-task-id", "")
        task = task_map.get(number)
        prefix = f"heading {index} task {number}"
        check(f"{prefix} maps to case config", task is not None)
        if task is None:
            continue
        label = heading.select_one(".technical-label")
        title = heading.select_one(".section-title")
        icon = heading.select_one(".ph-icon use")
        label_text = normalized_text(label) if label else ""
        title_text = normalized_text(title) if title else ""
        expected_title = f'{number} · {task["title"]}'
        check(f"{prefix} semantic label exact", label_text == task["semanticLabel"])
        check(f"{prefix} semantic label allowed", label_text in allowed_labels)
        check(f"{prefix} title exact", title_text == expected_title, f"actual={title_text}")
        check(f"{prefix} number appears once", title_text.count(number) == 1)
        check(f"{prefix} icon exact", icon is not None and icon.get("href") == f'#{task["icon"]}')
        check(f"{prefix} data title exact", heading.get("data-task-title") == task["title"])

    check("legacy TASK 0N headings absent", not any(f"TASK 0{n}" in master_text for n in range(1, 10)))
    pages = soup.select(".page[data-role]")
    for page in pages:
        page_id = page.get("data-page-id", "unknown")
        identities = page.select("[data-page-identity]")
        footers = page.select("[data-publication-footer]")
        check(f"{page_id} has one shared page identity", len(identities) == 1)
        check(f"{page_id} has one shared publication footer", len(footers) == 1)
    for role in config["roles"]:
        role_pages = soup.select(f'.page[data-role="{role}"]')
        if not role_pages:
            continue
        check(
            f"{role} first page uses first-page identity",
            role_pages[0].select_one('[data-page-identity="first"]') is not None,
        )
        check(
            f"{role} later pages use continuation identity",
            all(
                page.select_one('[data-page-identity="continuation"]') is not None
                for page in role_pages[1:]
            ),
        )
    for role, contract_name in {
        "student": "student-v1.0",
        "answer": "answer-v1.0",
        "accessible": "accessible-v1.0",
    }.items():
        role_cer = soup.select(f'.page[data-role="{role}"] [data-cer-contract="{contract_name}"]')
        boxes = [box for cer in role_cer for box in cer.select(":scope > .canonical-cer-box")]
        labels = [normalized_text(box.select_one(".canonical-cer-label")) for box in boxes if box.select_one(".canonical-cer-label")]
        check(f"{role} uses canonical CER contract", bool(role_cer))
        check(f"{role} CER has Claim Evidence Reasoning in order", labels == ["CLAIM", "EVIDENCE", "REASONING"], labels)
        check(f"{role} CER boxes use canonical response fields", all(box.select_one(".canonical-cer-response") for box in boxes))
        if role == "answer":
            check("answer CER responses are completed", all(normalized_text(box.select_one(".canonical-cer-response")) for box in boxes))

    processes = soup.select('[data-process-contract="five-stage-v1.0"]')
    check("canonical five-stage process models are present", len(processes) == 4, f"actual={len(processes)}")
    for index, process in enumerate(processes, 1):
        stages = process.select(":scope > .canonical-process-stage")
        connectors = process.select(":scope > .canonical-process-arrow")
        check(f"process {index} has five numbered stages", [stage.get("data-process-stage") for stage in stages] == ["1", "2", "3", "4", "5"])
        check(f"process {index} has four connectors", len(connectors) == 4)
    accessible_process = soup.select_one('.page[data-role="accessible"] [data-process-contract="five-stage-v1.0"]')
    check("accessible process uses vertical canonical layout", accessible_process is not None and accessible_process.get("data-process-layout") == "vertical")

    first_headers = soup.select('.mission-title-block[data-header-contract="printable-v1.1"]')
    continuation_headers = soup.select('.continuation-header[data-header-contract="printable-v1.1"]')
    check("every role uses approved first-page identity", len(first_headers) == len(config["roles"]))
    check("all continuation pages use approved identity", len(first_headers) + len(continuation_headers) == len(pages))
    check("all page identities use the approved color insignia", all(header.select_one(".saa-insignia .ins-sun") and header.select_one(".saa-insignia .ins-leaf") and header.select_one(".saa-insignia .ins-ring") for header in first_headers + continuation_headers))
    student_id = soup.select('.page[data-role="student"] .student-id')
    accessible_id = soup.select('.page[data-role="accessible"] .student-id')
    check(
        "Student and Accessible use approved identification geometry",
        len(student_id) == len(accessible_id) == 1
        and student_id[0].find_parent("section") is soup.select_one('.page[data-role="student"]')
        and accessible_id[0].find_parent("section") is soup.select_one('.page[data-role="accessible"]')
        and [node.get("data-field") for node in student_id[0].select("[data-field]")]
        == ["student-name", "student-date", "student-period"]
        and [node.get("data-field") for node in accessible_id[0].select("[data-field]")]
        == ["accessible-name", "accessible-date", "accessible-period"],
    )
    check("master has no external stylesheet", not soup.select('link[rel~="stylesheet"]'))
    check("master has no external script", not soup.select("script[src]"))
    check(
        "master has no external image dependency",
        not any((img.get("src") or "").startswith(("http:", "https:")) for img in soup.select("img[src]")),
    )
    persist_ids = [node.get("data-persist-id") for node in soup.select("[data-persist-id]")]
    check("editable persist identifiers are unique", len(persist_ids) == len(set(persist_ids)))
    check("document language is English", soup.html is not None and soup.html.get("lang") == "en")
    check("document title is present", bool(soup.title and normalized_text(soup.title)))
    responses = soup.select("[data-response]")
    check(
        "every response field has a programmatic label",
        bool(responses)
        and all(node.get("aria-label") or node.get("aria-labelledby") for node in responses),
    )
    tables = soup.select("table")
    check(
        "every data table has an accessible caption",
        all(table.select_one(":scope > caption") is not None for table in tables),
    )
    check(
        "every table header declares scope",
        all(header.get("scope") in {"col", "row", "colgroup", "rowgroup"} for header in soup.select("th")),
    )
    figures = soup.select("figure svg")
    check(
        "every figure graphic has an accessible name",
        all(
            graphic.get("aria-label")
            or graphic.get("aria-labelledby")
            or graphic.find("title")
            for graphic in figures
        ),
    )
    heading_skips: list[str] = []
    for page in pages:
        levels = [int(node.name[1]) for node in page.select("h1,h2,h3,h4,h5,h6")]
        if any(current > previous + 1 for previous, current in zip(levels, levels[1:])):
            heading_skips.append(page.get("data-page-id", "unknown"))
    check("page heading hierarchies have no skipped levels", not heading_skips, f"pages={heading_skips}")

    for role, expected in config["pageCounts"].items():
        data_role = "student" if role == "grayscale" else role
        actual = len(soup.select(f'.page[data-role="{data_role}"]'))
        if role != "grayscale":
            check(f"{role} master page count", actual == expected, f"actual={actual}")

    for output_name, output in config["outputs"].items():
        output_path = master_path.parents[1] / "published" / output["filename"]
        check(f"{output_name} role output exists", output_path.is_file())
        if not output_path.is_file():
            continue
        output_soup = BeautifulSoup(output_path.read_text(encoding="utf-8"), "html.parser")
        pages = output_soup.select(".page[data-role]")
        expected_role = output["role"]
        check(f"{output_name} role output has no toolbar", output_soup.select_one(".toolbar") is None)
        check(
            f"{output_name} role output is role-isolated",
            bool(pages) and all(page.get("data-role") == expected_role for page in pages),
        )
        check(
            f"{output_name} role output page count",
            len(pages) == config["pageCounts"][output_name],
            f"actual={len(pages)}",
        )

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    registry_policy = registry.get("productionPolicy", {})
    check("registry declares HTML-only new production", registry_policy.get("newProduction") == "HTML_ONLY")
    check("registry disallows PDF paths in new production", registry_policy.get("pdfPathsAllowed") is False)
    registry_cases = [
        case
        for curriculum in registry.get("curricula", [])
        for campaign in curriculum.get("campaigns", [])
        for case in campaign.get("cases", [])
    ]
    case_entry = next((case for case in registry_cases if case.get("id") == config["metadata"]["sss-case"]), None)
    check("case registry includes current case", case_entry is not None)
    if case_entry:
        check("case registry records shell 1.0", case_entry.get("editorShell") == "1.0")
        check("case registry records HTML-only artifact policy", case_entry.get("artifactPolicy") == "HTML_ONLY")
        expected_registry_status = (
            "APPROVED_STABLE"
            if config["metadata"].get("sss-status") == "approved"
            else "VALIDATION BUILD"
        )
        check(
            "case registry status matches release metadata",
            case_entry.get("status") == expected_registry_status,
            f'actual={case_entry.get("status")} expected={expected_registry_status}',
        )
    for case in registry_cases:
        check(f"registry master exists for {case['id']}", (REPO / case["master"]).is_file())
        for role, path in case.get("roles", {}).items():
            check(f"registry {case['id']} {role} output exists", (REPO / path).is_file())

    failures = [item for item in assertions if not item["pass"]]
    return {
        "validator": "shared-editor-shell-contract",
        "shellVersion": contract["shellVersion"],
        "master": str(master_path.relative_to(REPO)),
        "assertions": len(assertions),
        "passed": len(assertions) - len(failures),
        "failed": len(failures),
        "failures": failures,
        "results": assertions,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--master", type=Path, required=True)
    parser.add_argument(
        "--registry",
        type=Path,
        default=REPO / "shared/implementation/case-registry.v1.json",
    )
    parser.add_argument("--results", type=Path)
    args = parser.parse_args()
    result = validate(args.config.resolve(), args.master.resolve(), args.registry.resolve())
    if args.results:
        args.results.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{result['passed']}/{result['assertions']} shared shell assertions passing")
    for failure in result["failures"]:
        print(f"FAIL: {failure['name']} {failure['detail']}")
    return 1 if result["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
