#!/usr/bin/env python3
"""Assemble a portable editable master from the shared shell and case sources."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup


SHELL_DIR = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_config(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("shellVersion") != "1.0":
        raise ValueError("Case config must target editor shell 1.0.")
    return data


def resolve_case_path(config_path: Path, value: str) -> Path:
    return (config_path.parent / value).resolve()


def task_heading_html(task: dict[str, Any]) -> str:
    number = str(task["number"])
    title = task["title"]
    return (
        f'<h2 class="section-heading task-heading" data-task-id="{number}" data-task-title="{title}">'
        f'<svg class="ph-icon" aria-hidden="true"><use href="#{task["icon"]}"></use></svg>'
        '<span class="task-heading-copy">'
        f'<span class="technical-label">{task["semanticLabel"]}</span>'
        f'<span class="section-title">{number} · {title}</span>'
        "</span></h2>"
    )


def expand_case_content(content_html: str, config: dict[str, Any]) -> str:
    soup = BeautifulSoup(content_html, "html.parser")
    tasks = {str(task["number"]): task for task in config["tasks"]}
    for placeholder in soup.select("[data-shell-task-heading]"):
        number = placeholder["data-shell-task-heading"]
        if number not in tasks:
            raise ValueError(f"Unknown task-heading placeholder: {number}")
        replacement = BeautifulSoup(task_heading_html(tasks[number]), "html.parser").find("h2")
        placeholder.replace_with(replacement)
    if soup.select("[data-shell-task-heading]"):
        raise ValueError("Unexpanded task-heading placeholder remains.")
    return str(soup)


def build_master(config_path: Path) -> str:
    config = load_config(config_path)
    contract_path = SHELL_DIR / "editor-shell.contract.json"
    toolbar_path = SHELL_DIR / "toolbar.html"
    components_path = SHELL_DIR / "curriculum-components.css"
    css_path = SHELL_DIR / "editor-shell.css"
    cer_path = SHELL_DIR / "cer.css"
    icons_path = SHELL_DIR / "icons.svg"
    js_path = SHELL_DIR / "editor-shell.js"
    case_css_path = resolve_case_path(config_path, config["caseCss"])
    content_path = resolve_case_path(config_path, config["content"])

    metadata = "\n".join(
        f'<meta name="{name}" content="{value}">' for name, value in config["metadata"].items()
    )
    metadata += (
        f'\n<meta name="sss-editor-shell" content="{config["shellVersion"]}">'
        f'\n<meta name="sss-editor-shell-contract-sha256" content="{digest(contract_path)}">'
    )
    content = expand_case_content(content_path.read_text(encoding="utf-8"), config)
    runtime_config = {
        "shellVersion": config["shellVersion"],
        "documentKey": config["documentKey"],
        "roles": config["roles"],
        "defaults": config["defaults"],
        "editedMasterFilename": config["editedMasterFilename"],
        "roleFilenames": {key: value["filename"] for key, value in config["outputs"].items()},
        "standaloneRole": None,
    }
    runtime_source = js_path.read_text(encoding="utf-8")
    runtime_source = (
        runtime_source
        .replace("sss-c1-case02-v1-state", f'{config["documentKey"]}:state')
        .replace("sss-c1-case02-v1-content", f'{config["documentKey"]}:content')
        .replace(
            "SSS_C1_CASE02_EDITABLE_MASTER_v1.0_CUSTOM.html",
            config["editedMasterFilename"],
        )
        .replace("window.__case02", "window.__case03")
    )
    shell_assets = {
        "toolbar": toolbar_path,
        "components": components_path,
        "css": css_path,
        "cer": cer_path,
        "icons": icons_path,
        "runtime": js_path,
    }
    hashes = " ".join(f'{name}:{digest(path)}' for name, path in shell_assets.items())

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{config["title"]}</title>
{metadata}
<meta name="sss-editor-shell-assets" content="{hashes}">
<style id="sssCurriculumComponentsCss" data-source-sha256="{digest(components_path)}">{components_path.read_text(encoding="utf-8")}</style>
<style id="caseStyles">{case_css_path.read_text(encoding="utf-8")}</style>
<style id="sssEditorShellCss" data-source-sha256="{digest(css_path)}">{css_path.read_text(encoding="utf-8")}</style>
<style id="sssCerComponentCss" data-source-sha256="{digest(cer_path)}">{cer_path.read_text(encoding="utf-8")}</style>
</head>
<body>
<a class="visually-hidden" href="#workspace">Skip to curriculum pages</a>
{icons_path.read_text(encoding="utf-8")}
{toolbar_path.read_text(encoding="utf-8")}
{content}
<script id="sssEditorShellCaseConfig" type="application/json">{json.dumps(runtime_config, separators=(",", ":"))}</script>
<script id="sssEditorShellRuntime" data-source-sha256="{digest(js_path)}">{runtime_source}</script>
</body>
</html>
"""


def build_role(master_html: str, role: str, grayscale: bool, config: dict[str, Any]) -> str:
    soup = BeautifulSoup(master_html, "html.parser")
    toolbar = soup.select_one(".toolbar")
    if toolbar:
        toolbar.decompose()
    for page in soup.select(".page[data-role]"):
        if page.get("data-role") != role:
            page.decompose()
        else:
            page.attrs.pop("hidden", None)
            page.attrs.pop("aria-hidden", None)
    meta = soup.new_tag("meta")
    meta["name"] = "sss-standalone-role"
    meta["content"] = role
    soup.head.append(meta)
    soup.body["class"] = list(soup.body.get("class", [])) + ["standalone-role"]
    soup.body["data-standalone"] = "true"
    soup.body["data-export-role"] = role
    soup.body["data-export-grayscale"] = "true" if grayscale else "false"
    return "<!doctype html>\n" + str(soup.html)


def write_outputs(config_path: Path, master_output: Path, roles_root: Path | None) -> list[Path]:
    config = load_config(config_path)
    master_html = build_master(config_path)
    master_output.parent.mkdir(parents=True, exist_ok=True)
    master_output.write_text(master_html, encoding="utf-8")
    written = [master_output]
    if roles_root is not None:
        for output_name, output in config["outputs"].items():
            role_html = build_role(master_html, output["role"], bool(output.get("grayscale")), config)
            destination = roles_root / output["filename"]
            destination.write_text(role_html, encoding="utf-8")
            written.append(destination)
    return written


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--master-output", type=Path, required=True)
    parser.add_argument("--roles-root", type=Path)
    args = parser.parse_args()
    written = write_outputs(args.config.resolve(), args.master_output.resolve(), args.roles_root.resolve() if args.roles_root else None)
    for path in written:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
