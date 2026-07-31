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
        ("runtime", SHELL / "editor-shell.js", "#sssEditorShellRuntime"),
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

    icon_source = (SHELL / "icons.svg").read_text(encoding="utf-8")
    toolbar_source = BeautifulSoup((SHELL / "toolbar.html").read_text(encoding="utf-8"), "html.parser")
    check("shared icon sprite is embedded exactly", icon_source in master_text)
    toolbar = soup.select_one('[data-editor-shell-toolbar="1.0"]')
    check("canonical toolbar is present", toolbar is not None)
    if toolbar is not None:
        actual_controls = [node.get("id") for node in toolbar.select("[id]")]
        check(
            "toolbar controls follow contract order",
            actual_controls == contract["toolbar"]["controlOrder"],
            f"actual={actual_controls}",
        )
        source_controls = [node.get("id") for node in toolbar_source.select("[id]")]
        check("toolbar markup is the shared source", actual_controls == source_controls)
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
        print_button = toolbar.select_one("#printBtn")
        check(
            "print button warns that browser PDF accessibility is not guaranteed",
            print_button is not None
            and "accessibility is not guaranteed" in (print_button.get("aria-label") or "").lower(),
        )
        print_note = toolbar.select_one(".pdf-accessibility-note")
        check(
            "toolbar visibly requires PDF verification before distribution",
            print_note is not None
            and "requires accessibility verification before distribution"
            in normalized_text(print_note).lower(),
        )

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
    check("student CER contract is present", bool(soup.select('[data-cer-contract="student-v1.0"]')))
    check(
        "student CER has Claim Evidence Reasoning boxes",
        all(
            [cer.select_one(".claim"), cer.select_one(".evidence"), cer.select_one(".reasoning")]
            for cer in soup.select('[data-cer-contract="student-v1.0"]')
        ),
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
