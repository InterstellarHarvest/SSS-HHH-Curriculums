#!/usr/bin/env python3
"""Zero-write static validation for the Phase 1 Curriculum Editor."""
from __future__ import annotations

import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup


APP = Path(__file__).resolve().parents[1]
REPO = APP.parents[1]
REGISTRY = REPO / "shared/implementation/case-registry.v1.json"
REGISTRY_SCHEMA = REPO / "shared/implementation/case-registry.schema.v1.json"
PACKAGE_SCHEMA = REPO / "shared/implementation/case-package.schema.v1.json"
HISTORICAL_MANIFEST = REPO / "sss/campaign-1/case-03-mars-habitat/CASE03_V1_RELEASE_MANIFEST.json"
MANIFEST = REPO / "sss/campaign-1/case-03-mars-habitat/CASE03_V1_1_RELEASE_MANIFEST.json"
REQUIRED_ROLES = ["student", "teacher", "answer", "accessible", "grayscale"]


class Results:
    def __init__(self) -> None:
        self.assertions: list[dict[str, Any]] = []

    def check(self, name: str, condition: bool, detail: Any = "") -> None:
        self.assertions.append({"name": name, "pass": bool(condition), "detail": str(detail)})

    @property
    def passed(self) -> int:
        return sum(item["pass"] for item in self.assertions)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def schema_errors(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Validate the JSON-Schema subset used by the two versioned contracts."""
    errors: list[str] = []
    if "anyOf" in schema and not any(not schema_errors(instance, candidate, path) for candidate in schema["anyOf"]):
        errors.append(f"{path}: value does not satisfy any allowed schema")
    expected = schema.get("type")
    if expected:
        names = expected if isinstance(expected, list) else [expected]
        type_map = {
            "object": lambda value: isinstance(value, dict),
            "array": lambda value: isinstance(value, list),
            "string": lambda value: isinstance(value, str),
            "number": lambda value: isinstance(value, (int, float)) and not isinstance(value, bool),
            "integer": lambda value: isinstance(value, int) and not isinstance(value, bool),
            "boolean": lambda value: isinstance(value, bool),
            "null": lambda value: value is None,
        }
        if not any(type_map[name](instance) for name in names):
            return [f"{path}: expected {names}, got {type(instance).__name__}"]
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} is not in enum")
    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            errors.append(f"{path}: string is too short")
        if schema.get("pattern") and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: string does not match {schema['pattern']}")
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: value is below minimum")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: value is above maximum")
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: array has too few items")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(value, sort_keys=True) for value in instance]
            if len(serialized) != len(set(serialized)):
                errors.append(f"{path}: array items are not unique")
        if "items" in schema:
            for index, value in enumerate(instance):
                errors.extend(schema_errors(value, schema["items"], f"{path}[{index}]"))
    if isinstance(instance, dict):
        for required in schema.get("required", []):
            if required not in instance:
                errors.append(f"{path}: missing required property {required}")
        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                errors.extend(schema_errors(value, properties[key], f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected property {key}")
            elif isinstance(schema.get("additionalProperties"), dict):
                errors.extend(schema_errors(value, schema["additionalProperties"], f"{path}.{key}"))
    return errors


def task_registry(path: Path) -> dict[str, Any]:
    source = path.read_text(encoding="utf-8")
    match = re.fullmatch(r"\s*window\.[A-Za-z0-9_]+\s*=\s*(\{.*\});\s*", source, re.DOTALL)
    if not match:
        raise ValueError("task registry is not a JSON-compatible window assignment")
    return json.loads(match.group(1))


def semantic_package_errors(package: dict[str, Any], content_override: str | None = None) -> list[str]:
    errors: list[str] = []
    if package.get("schemaVersion") != 1:
        errors.append("unsupported schema version")
    for role in REQUIRED_ROLES:
        if role not in package.get("supportedRoles", []):
            errors.append(f"missing role definition: {role}")
        if role not in package.get("rolePageStructure", {}):
            errors.append(f"missing role page structure: {role}")
        if role not in package.get("outputs", {}):
            errors.append(f"missing role output: {role}")
    paths = [
        package.get("shell", {}).get("toolbar"),
        *package.get("shell", {}).get("styles", []),
        package.get("shell", {}).get("icons"),
        package.get("taskRegistry", {}).get("source"),
        package.get("content", {}).get("source"),
        package.get("presentation", {}).get("stylesheet"),
        *(item.get("source") for item in package.get("styles", [])),
        *(item.get("source") for item in package.get("assets", []) if item.get("source")),
    ]
    for value in paths:
        if not value or value.startswith("/") or ".." in Path(value).parts or not (REPO / value).is_file():
            errors.append(f"missing package file: {value}")
    content_path = package.get("content", {}).get("source")
    if content_override is not None:
        content = content_override
    elif content_path and (REPO / content_path).is_file():
        content = (REPO / content_path).read_text(encoding="utf-8")
    else:
        content = ""
        errors.append("missing content")
    soup = BeautifulSoup(content, "html.parser")
    registry_path = package.get("taskRegistry", {}).get("source")
    tasks: dict[str, Any] = {}
    if registry_path and (REPO / registry_path).is_file():
        try:
            registry_data = task_registry(REPO / registry_path)
            tasks = {str(task["number"]): task for task in registry_data.get("tasks", [])}
        except (ValueError, json.JSONDecodeError, KeyError) as error:
            errors.append(f"invalid task registry: {error}")
    for placeholder in soup.select("[data-shell-task-heading]"):
        reference = placeholder.get("data-shell-task-heading")
        if reference not in tasks:
            errors.append(f"invalid task reference: {reference}")
    for asset in package.get("assets", []):
        selector = asset.get("selector")
        if selector:
            try:
                found = soup.select_one(selector)
            except Exception:
                found = None
            if found is None:
                errors.append(f"invalid asset selector: {selector}")
    return errors


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    results = Results()
    registry = load_json(REGISTRY)
    registry_schema = load_json(REGISTRY_SCHEMA)
    package_schema = load_json(PACKAGE_SCHEMA)
    registry_validation = schema_errors(registry, registry_schema)
    results.check("registry validates against case-registry schema", not registry_validation, registry_validation)
    case03 = next(
        case
        for curriculum in registry["curricula"]
        for campaign in curriculum["campaigns"]
        for case in campaign["cases"]
        if case["id"] == "SSS-C1-CASE03"
    )
    results.check("Case 03 is discoverable", bool(case03))
    results.check("Case 03 current version is 1.1", case03["version"] == "1.1", case03["version"])
    results.check("Case 03 v1.1 status is APPROVED_STABLE", case03["status"] == "APPROVED_STABLE", case03["status"])
    results.check("Case 03 registry targets the corrected v1.1 master", case03["master"].endswith("SSS_C1_CASE03_EDITABLE_MASTER_v1.1.html"))
    historical = case03.get("historicalReleases", [])
    results.check("registry preserves v1.0 as historical approved metadata", len(historical) == 1 and historical[0]["version"] == "1.0" and historical[0]["status"] == "APPROVED_STABLE")
    results.check("registry records final owner and physical-print approval", case03.get("approval") == {"date": "2026-07-31", "tester": "Nate / Owner", "ownerReview": "PASS", "browserPhysicalPrint": "PASS", "scale": "100% / Actual Size", "printer": "Not recorded", "paper": "Not recorded", "artifactPolicy": "HTML_ONLY"})
    package_path = REPO / case03["editorPackage"]
    results.check("Case 03 editor package exists", package_path.is_file(), case03["editorPackage"])
    package = load_json(package_path)
    package_validation = schema_errors(package, package_schema)
    results.check("Case 03 package validates against package schema", not package_validation, package_validation)
    semantic_errors = semantic_package_errors(package)
    results.check("Case 03 package semantic validation passes", not semantic_errors, semantic_errors)
    results.check("package and registry IDs agree", package["id"] == case03["id"])
    results.check("package and registry versions agree", package["version"] == case03["version"])
    results.check("package and registry statuses agree", package["status"] == case03["status"])
    results.check("approved package records final owner and physical-print approval", package.get("approval") == case03.get("approval"))
    results.check("package uses shared editor shell 1.0", package["shell"]["version"] == "1.0")
    results.check("package content does not load a complete master", "master/" not in package["content"]["source"])
    results.check("all five package output profiles are declared", package["supportedRoles"] == REQUIRED_ROLES, package["supportedRoles"])
    expected_counts = {"student": 4, "teacher": 8, "answer": 4, "accessible": 7, "grayscale": 4}
    results.check("role page-count contract is 4/8/4/7/4", {role: package["rolePageStructure"][role]["pageCount"] for role in REQUIRED_ROLES} == expected_counts)
    results.check("Grayscale maps to Student source pages", package["rolePageStructure"]["grayscale"]["sourceRole"] == "student" and package["rolePageStructure"]["grayscale"]["grayscale"] is True)
    results.check("document key includes case and version", package["id"] in package["documentKey"] and "v1.1" in package["documentKey"])
    results.check("package records the owner-authorized v1.0 historical hash", package["migrationSource"]["historicalMasterSha256"] == "c97a880f0be0c58848c0d8a7394ce75925aff26f3fb542dc4d63cca25a9b6bce")
    results.check("package declares isolated extracted presentation", package["presentation"]["isolation"] == "shadow-dom")
    phrase_config = package.get("phraseBank", {})
    results.check("package declares the shared Task 6 phrase-bank contract", phrase_config.get("contract") == "sequence-v1.0" and phrase_config.get("taskId") == 6)
    results.check("phrase-bank configuration uses Answer Stages 2–5 once each", phrase_config.get("sourceRole") == "answer" and phrase_config.get("sourceStages") == [2, 3, 4, 5] and phrase_config.get("itemCount") == 4)
    results.check("phrase-bank configuration fixes a non-sequential display order", phrase_config.get("displayOrderSourceStages") == [4, 2, 5, 3] and phrase_config.get("displayOrderSourceStages") != phrase_config.get("sourceStages"))
    results.check("phrase-bank role contract includes Student, Answer, Accessible, and Grayscale", phrase_config.get("roles") == ["student", "answer", "accessible", "grayscale"])
    results.check("complete and role output names are distinct", len(set(package["outputs"].values())) == 6)
    results.check("all output names are HTML", all(name.lower().endswith(".html") for name in package["outputs"].values()))
    results.check("portable outputs use clear CUSTOM names", all("CUSTOM" in name for name in package["outputs"].values()))

    content = BeautifulSoup((REPO / package["content"]["source"]).read_text(encoding="utf-8"), "html.parser")
    role_counts = {role: len(content.select(f'.page[data-role="{role}"]')) for role in ["student", "teacher", "answer", "accessible"]}
    results.check("source content page counts are 4/8/4/7", role_counts == {"student": 4, "teacher": 8, "answer": 4, "accessible": 7}, role_counts)
    results.check("source content has one main landmark", len(content.select("main")) == 1)
    results.check("all worksheet pages have accessible names", all(page.get("aria-label") or page.get("aria-labelledby") for page in content.select(".page")))
    results.check("all response fields have accessible names", all(node.get("aria-label") or node.get("aria-labelledby") for node in content.select("[data-response]")))
    results.check("all data tables have captions", len(content.select("table")) == len(content.select("table caption")))
    results.check("all persistence IDs are unique", len(content.select("[data-persist-id]")) == len({node.get("data-persist-id") for node in content.select("[data-persist-id]")}))
    results.check("instruction and response contracts both exist", bool(content.select("[data-editable]")) and bool(content.select("[data-response]")))
    results.check("three CER variants are present", {node.get("data-cer-contract") for node in content.select("[data-cer-contract]")} == {"student-v1.0", "answer-v1.0", "accessible-v1.0"})
    cer_roots = content.select("[data-cer-contract]")
    cer_rows = {
        root.get("data-cer-contract"): [label.get_text(" ", strip=True) for label in root.select(":scope > .canonical-cer-box > .canonical-cer-label")]
        for root in cer_roots
    }
    results.check("each CER variant has one canonical Claim/Evidence/Reasoning root", len(cer_roots) == 3 and all(rows == ["CLAIM", "EVIDENCE", "REASONING"] for rows in cer_rows.values()), cer_rows)
    results.check("all CER rows share their root's closest page", all(box.find_parent(class_="page") is root.find_parent(class_="page") for root in cer_roots for box in root.select(":scope > .canonical-cer-box")))
    results.check("CER rows retain attached labels and response areas", all(len(root.select(":scope > .canonical-cer-box")) == 3 and all(box.select_one(":scope > .canonical-cer-label") and box.select_one(":scope > .canonical-cer-response, :scope > .answer-block") for box in root.select(":scope > .canonical-cer-box")) for root in cer_roots))
    accessible_cer = content.select('[data-role="accessible"] [data-cer-contract="accessible-v1.0"]')
    results.check("Accessible Task 7 CER is atomic on page 6", len(accessible_cer) == 1 and accessible_cer[0].find_parent(class_="page").get("data-page-id") == "accessible-mission-06")
    results.check("five-stage process model is present", bool(content.select('[data-process-contract="five-stage-v1.0"]')))
    answer_process = content.select_one('.page[data-role="answer"] [data-process-contract="five-stage-v1.0"]')
    answer_stage_phrases = [
        answer_process.select_one(f'[data-process-stage="{number}"] .stage-content').get_text(" ", strip=True)
        for number in range(2, 6)
    ]
    expected_bank_order = [answer_stage_phrases[index] for index in [2, 0, 3, 1]]
    banks = content.select('[data-phrase-bank-contract="sequence-v1.0"]')
    bank_roles = {bank.find_parent(class_="page").get("data-role"): bank for bank in banks}
    bank_orders = {
        role: [item.get_text(" ", strip=True) for item in bank.select(":scope > .canonical-phrase-bank-items > .canonical-phrase-bank-item")]
        for role, bank in bank_roles.items()
    }
    results.check("Student, Answer, and Accessible each have one Task 6 phrase bank", len(banks) == 3 and set(bank_roles) == {"student", "answer", "accessible"}, bank_orders)
    results.check("bank phrase set exactly equals controlled Answer Key Stages 2–5", all(set(order) == set(answer_stage_phrases) for order in bank_orders.values()), bank_orders)
    results.check("bank uses the fixed deliberately shuffled order", all(order == expected_bank_order and order != answer_stage_phrases for order in bank_orders.values()), bank_orders)
    results.check("bank contains every phrase exactly once", all(len(order) == len(set(order)) == 4 for order in bank_orders.values()), bank_orders)
    results.check("Student, Answer, and Accessible bank wording and order match", len({tuple(order) for order in bank_orders.values()}) == 1, bank_orders)
    results.check("phrase-bank DOM order is label, instruction, then phrases", all(["canonical-phrase-bank-label", "canonical-phrase-bank-instruction", "canonical-phrase-bank-items"] == [child.get("class", [""])[0] for child in bank.find_all(recursive=False)] for bank in banks))
    results.check("phrase-bank label and instruction are explicit", all(bank.select_one(":scope > .canonical-phrase-bank-label").get_text(" ", strip=True) == "PHRASE BANK" and bank.select_one(":scope > .canonical-phrase-bank-instruction").get_text(" ", strip=True) == "Use each phrase once." for bank in banks))
    results.check("phrase banks are unnumbered accessible lists", all(bank.select_one(":scope > ul.canonical-phrase-bank-items") and not bank.select_one(":scope > ol") and bank.get("aria-labelledby") and bank.get("aria-describedby") for bank in banks))
    results.check("each phrase bank follows its complete Task 6 model on the same page", all((page := bank.find_parent(class_="page")) is not None and page.select_one('.task-heading[data-task-id="6"]') and (model := page.select_one('[data-process-contract="five-stage-v1.0"]')) and model.find_next_sibling() is bank and len(model.select('[data-process-stage]')) == 5 and len(model.select('[data-process-connector]')) == 4 for bank in banks))
    results.check("Teacher guidance says students sequence supplied phrases", "students sequence the supplied phrases into Stages 2–5 rather than generate all mechanism wording independently" in content.select_one('.page[data-page-id="teacher-guide-03"]').get_text(" ", strip=True))
    results.check("optional-extension contract is present", bool(content.select('[data-optional-extension="canonical-v1.0"]')))
    results.check("spectral figures and captions are present", len(content.select('[data-quantity-spectrum="canonical-v1.0"]')) == 3 and bool(content.select("figure figcaption")))
    results.check("task headings remain attached to following task content", all((next_node := node.find_next_sibling()) is not None and next_node.find_parent(class_="page") is node.find_parent(class_="page") for node in content.select(".task-heading")))
    results.check("figures remain attached to captions on one page", all(figure.select_one(":scope > figcaption") and figure.select_one(":scope > figcaption").find_parent(class_="page") is figure.find_parent(class_="page") for figure in content.select("figure")))
    results.check("table headers remain attached to first data rows", all(len(table.select(":scope > tr, :scope > thead > tr, :scope > tbody > tr")) >= 2 and table.select_one("th") is not None for table in content.select("table")))
    results.check("five-stage models remain atomic on one page", all(len(model.select(":scope > [data-process-stage]")) == 5 and len(model.select(":scope > [data-process-connector]")) == 4 and all(node.find_parent(class_="page") is model.find_parent(class_="page") for node in model.select("[data-process-stage],[data-process-connector]")) for model in content.select('[data-process-contract="five-stage-v1.0"]')))
    results.check("optional extensions and diagnosis groups remain atomic", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in content.select("[data-optional-extension],.choice-list")))
    def response_has_context(node: Any) -> bool:
        page = node.find_parent(class_="page")
        if page is None:
            return False
        if node.find_parent(class_="canonical-cer-box") or node.find_parent(class_="canonical-process-stage") or node.find_parent("td") or node.find_parent("label"):
            return True
        prompt = node.find_previous(["p", "h2", "label"])
        return prompt is not None and prompt.find_parent(class_="page") is page
    results.check("response fields retain an in-page prompt or component context", all(response_has_context(node) for node in content.select("[data-response]")))
    results.check("content has no runtime, external styles, or iframes", not content.select("script, style, link, iframe"))

    tasks = task_registry(REPO / package["taskRegistry"]["source"])
    task_map = {str(task["number"]): task for task in tasks["tasks"]}
    references = [node.get("data-shell-task-heading") for node in content.select("[data-shell-task-heading]")]
    headings = content.select(".task-heading[data-task-id]")
    results.check("task registry contains canonical Tasks 1–9", list(task_map) == [str(value) for value in range(1, 10)])
    results.check("v1.1 extraction contains no unresolved task placeholders", not references)
    results.check("every task heading matches the canonical task registry title", all(node.get("data-task-title") == task_map[node.get("data-task-id")]["title"] and node.select_one(".section-title").get_text(" ", strip=True) == f'{node.get("data-task-id")} · {task_map[node.get("data-task-id")]["title"]}' for node in headings))
    results.check("every task appears in Student, Answer, and Accessible", all(sum(1 for node in headings if node.get("data-task-id") == str(value) and node.find_parent(class_="page").get("data-role") in {"student", "answer", "accessible"}) == 3 for value in range(1, 10)))
    results.check("task semantic labels are not numeric TASK labels", all(not re.fullmatch(r"TASK\s+0?\d+", task["semanticLabel"], re.I) for task in tasks["tasks"]))
    results.check("every task has one Phosphor icon ID", all(task["icon"].startswith("ph-") for task in tasks["tasks"]))

    app_html = BeautifulSoup((APP / "index.html").read_text(encoding="utf-8"), "html.parser")
    app_css = (APP / "editor-app.css").read_text(encoding="utf-8")
    app_runtime = (APP / "editor-app.js").read_text(encoding="utf-8")
    portable_runtime = (APP / "portable-runtime.js").read_text(encoding="utf-8")
    results.check("library rail is an aside with labelled navigation", bool(app_html.select_one("aside.library-rail nav[aria-label]")))
    results.check("library selectors have explicit labels", all(app_html.select_one(f'label[for="{identifier}"]') for identifier in ["curriculumSelect", "campaignSelect", "caseSelect"]))
    results.check("role selector is a fieldset with legend", bool(app_html.select_one("fieldset#roleLibrary legend")))
    results.check("load status is polite live status", app_html.select_one("#loadStatus").get("aria-live") == "polite")
    results.check("editor errors use alert semantics", app_html.select_one("#editorError").get("role") == "alert")
    results.check("skip link targets the main editor", app_html.select_one('a[href="#editorMain"]') is not None and app_html.select_one("main#editorMain") is not None)
    results.check("manual PDF accessibility warning is visible", "does not guarantee PDF accessibility" in app_html.get_text(" "))
    results.check("reduced-motion CSS is present", "prefers-reduced-motion" in app_css)
    results.check("app uses only local runtime sources", not app_html.select('script[src^="http"], link[href^="http"]'))
    results.check("worksheet host is separate from the application DOM", app_html.select_one("#worksheetHost") is not None and app_html.select_one("#worksheetWorkspace") is None)
    results.check("toolbar offset has a CSS fallback without the rejected 92px gap", "--app-toolbar-offset: 76px" in app_css and "--app-toolbar-offset: 92px" not in app_css)
    results.check("layout and rail share the measured toolbar offset variable", app_css.count("var(--app-toolbar-offset)") >= 3)
    results.check("toolbar measurement observes resize and font completion", "new ResizeObserver(syncToolbarOffset)" in app_runtime and "document.fonts?.ready.then(syncToolbarOffset)" in app_runtime)
    results.check("central navigation defines exactly four instructional roles", 'const NAVIGATION_ROLES = ["student", "teacher", "answer", "accessible"]' in app_runtime)
    results.check("central toolbar removes its duplicate Role label", 'roleControl.closest("label")?.remove()' in app_runtime)
    results.check("Grayscale is stored as a presentation modifier", 'classList.toggle("grayscale", state.grayscale)' in app_runtime and 'classList.toggle("grayscale", state.grayscale)' in portable_runtime)
    results.check("no whole-page grayscale filter was introduced", not re.search(r"filter\s*:\s*grayscale|grayscale\(", app_css + app_runtime + portable_runtime, re.I))

    # Required clean-failure cases are exercised in memory without changing repository files.
    unsupported = copy.deepcopy(package)
    unsupported["schemaVersion"] = 2
    results.check("unsupported package schema fails cleanly", any("unsupported schema version" in error for error in semantic_package_errors(unsupported)))
    missing_content = copy.deepcopy(package)
    missing_content["content"]["source"] = "missing/case-content.html"
    results.check("missing content fails cleanly", any("missing content" in error for error in semantic_package_errors(missing_content)))
    missing_role = copy.deepcopy(package)
    missing_role["supportedRoles"].remove("teacher")
    results.check("missing role definition fails cleanly", any("missing role definition: teacher" in error for error in semantic_package_errors(missing_role)))
    invalid_task_content = (REPO / package["content"]["source"]).read_text(encoding="utf-8") + '<div data-shell-task-heading="999"></div>'
    results.check("invalid task reference fails cleanly", any("invalid task reference: 999" in error for error in semantic_package_errors(package, invalid_task_content)))
    missing_asset = copy.deepcopy(package)
    missing_asset["assets"].append({"id": "missing", "type": "image/svg+xml", "source": "missing/asset.svg", "embed": True})
    results.check("invalid asset path fails cleanly", any("missing package file: missing/asset.svg" in error for error in semantic_package_errors(missing_asset)))
    missing_package = REPO / "missing/package.json"
    results.check("missing package file fails cleanly", not missing_package.is_file())

    manifest = load_json(HISTORICAL_MANIFEST)
    release_files: list[tuple[Path, str]] = [
        (HISTORICAL_MANIFEST.parent / manifest["current_master"]["path"], manifest["current_master"]["sha256"])
    ]
    release_files.extend((HISTORICAL_MANIFEST.parent / data["html"]["path"], data["html"]["sha256"]) for data in manifest["outputs"].values())
    release_files.extend((HISTORICAL_MANIFEST.parent / item["path"], item["sha256"]) for item in manifest["controlled_sources"])
    hash_failures = [str(path.relative_to(REPO)) for path, expected in release_files if sha256(path) != expected]
    results.check("approved Case 03 v1.0 master, role outputs, and controlled-source hashes are unchanged", not hash_failures, hash_failures)
    v11_manifest = load_json(MANIFEST)
    v11_master = BeautifulSoup((MANIFEST.parent / v11_manifest["current_approved_master"]["path"]).read_text(encoding="utf-8"), "html.parser")
    results.check("v1.1 package worksheet DOM exactly matches the approved master", str(content.select_one("main")) == str(v11_master.select_one("main")))
    master_meta = {node.get("name"): node.get("content") for node in v11_master.select("meta[name]")}
    results.check("approved master metadata records status, date, tester, and print gate", master_meta.get("sss-status") == "approved-stable" and master_meta.get("sss-approval-date") == "2026-07-31" and master_meta.get("sss-approval-tester") == "Nate / Owner" and master_meta.get("sss-browser-physical-print") == "pass")
    historical_master = BeautifulSoup((HISTORICAL_MANIFEST.parent / manifest["current_master"]["path"]).read_text(encoding="utf-8"), "html.parser")
    results.check("v1.1 Task 6 remains on the historical role pages", all(
        historical_master.select_one(f'.page[data-role="{role}"] .task-heading[data-task-id="6"]').find_parent(class_="page").get("data-page-id")
        == v11_master.select_one(f'.page[data-role="{role}"] .task-heading[data-task-id="6"]').find_parent(class_="page").get("data-page-id")
        for role in ["student", "answer", "accessible"]
    ))
    v11_files = [(MANIFEST.parent / v11_manifest["current_approved_master"]["path"], v11_manifest["current_approved_master"]["sha256"])]
    v11_files.extend((MANIFEST.parent / output["html"]["path"], output["html"]["sha256"]) for output in v11_manifest["outputs"].values())
    v11_failures = [str(path.relative_to(REPO)) for path, expected in v11_files if sha256(path) != expected]
    results.check("Case 03 v1.1 master and five role hashes match the approved manifest", not v11_failures, v11_failures)
    published_bank_orders = {}
    for role in ["student", "answer", "accessible", "grayscale"]:
        role_soup = BeautifulSoup((MANIFEST.parent / v11_manifest["outputs"][role]["html"]["path"]).read_text(encoding="utf-8"), "html.parser")
        role_banks = role_soup.select('[data-phrase-bank-contract="sequence-v1.0"]')
        published_bank_orders[role] = [item.get_text(" ", strip=True) for item in role_banks[0].select(".canonical-phrase-bank-item")] if len(role_banks) == 1 else []
    results.check("Student, Accessible, and Grayscale published banks match", published_bank_orders["student"] == published_bank_orders["accessible"] == published_bank_orders["grayscale"] == expected_bank_order, published_bank_orders)
    results.check("published Answer Key retains the same parity bank", published_bank_orders["answer"] == expected_bank_order, published_bank_orders["answer"])
    results.check("Case 03 v1.1 owner gate is closed PASS and Phase 1 is ready to merge", v11_manifest["physical_print_gate"] == "PASS" and v11_manifest["release_gate"] == "CLOSED_PASS" and v11_manifest["status"] == "APPROVED_STABLE" and v11_manifest["phase_1"]["status"] == "READY_TO_MERGE")
    parity_results = load_json(APP / "tests/parity-v1.1-results.json")
    results.check("machine-readable parity results record final approval", parity_results.get("status") == "PASS" and parity_results.get("releaseStatus") == "APPROVED_STABLE" and parity_results.get("phase1Status") == "READY_TO_MERGE" and parity_results.get("ownerApproval", {}).get("tester") == "Nate / Owner")
    deterministic = subprocess.run([sys.executable, str(MANIFEST.parent / "validation-artifacts/build_case03_v1_1.py"), "--check"], cwd=REPO, text=True, capture_output=True)
    results.check("Case 03 v1.1 extraction/build is deterministic", deterministic.returncode == 0, (deterministic.stdout + deterministic.stderr).strip())
    for case_number, path in [(1, "sss/campaign-1/case-01-iss-greenhouse"), (2, "sss/campaign-1/case-02-lunar-greenhouse")]:
        comparison = subprocess.run(["git", "diff", "--quiet", "main", "--", path], cwd=REPO)
        results.check(f"approved Case 0{case_number} tracked files are unchanged", comparison.returncode == 0)
    changed = subprocess.run(["git", "status", "--porcelain"], cwd=REPO, text=True, capture_output=True, check=True).stdout.splitlines()
    pdf_changes = [line for line in changed if line.lower().endswith(".pdf")]
    results.check("no PDF was generated or modified", not pdf_changes, pdf_changes)
    app_pdf_tools = [path for path in APP.rglob("*") if path.is_file() and "pdf" in path.name.lower()]
    results.check("no PDF builder, preflight, checksum, or output was added", not app_pdf_tools, app_pdf_tools)

    payload = {
        "validator": "curriculum-editor-static-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
