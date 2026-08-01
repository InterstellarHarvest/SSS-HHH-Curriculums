#!/usr/bin/env python3
"""Validate canonical packages, registry, worksheet sources, and editor contracts."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[1]
ROLES = ["student", "teacher", "answer", "accessible"]
CANONICAL_SAA = "Solar Agricultural Agency"
REJECTED_SAA = (
    "Solar Agricultural Authority", "Space Agricultural Authority", "Space Agricultural Agency",
    "Solar Agriculture Agency", "Space Agriculture Authority",
)
EXPECTED = {
    "SSS-C1-CASE01": ("1.1", {"student": 3, "teacher": 7, "answer": 3, "accessible": 6}),
    "SSS-C1-CASE02": ("1.0", {"student": 3, "teacher": 7, "answer": 3, "accessible": 5}),
    "SSS-C1-CASE03": ("1.1", {"student": 4, "teacher": 8, "answer": 4, "accessible": 7}),
}


class Results:
    def __init__(self):
        self.assertions: list[dict[str, object]] = []

    def check(self, name: str, passed: bool, detail="") -> None:
        self.assertions.append({"name": name, "pass": bool(passed), "detail": str(detail)})

    @property
    def passed(self) -> int:
        return sum(1 for item in self.assertions if item["pass"])


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def schema_errors(instance, schema) -> list[str]:
    """Validate the JSON-Schema features used by the repository's v2 schemas."""
    errors: list[str] = []

    def resolve(reference: str):
        node = schema
        for part in reference.removeprefix("#/").split("/"):
            node = node[part]
        return node

    def visit(value, rule, path="$", root_rule=None):
        if "$ref" in rule:
            visit(value, resolve(rule["$ref"]), path)
            return
        if "const" in rule and value != rule["const"]:
            errors.append(f"{path}: must equal {rule['const']!r}")
        if "enum" in rule and value not in rule["enum"]:
            errors.append(f"{path}: must be one of {rule['enum']!r}")
        expected = rule.get("type")
        type_ok = {
            "object": isinstance(value, dict),
            "array": isinstance(value, list),
            "string": isinstance(value, str),
            "integer": isinstance(value, int) and not isinstance(value, bool),
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
            "boolean": isinstance(value, bool),
        }.get(expected, True)
        if expected and not type_ok:
            errors.append(f"{path}: expected {expected}")
            return
        if isinstance(value, dict):
            for key in rule.get("required", []):
                if key not in value:
                    errors.append(f"{path}: missing required property {key}")
            properties = rule.get("properties", {})
            if rule.get("additionalProperties") is False:
                for key in value.keys() - properties.keys():
                    errors.append(f"{path}: unexpected property {key}")
            for key, child in value.items():
                if key in properties:
                    visit(child, properties[key], f"{path}.{key}")
        if isinstance(value, list):
            if len(value) < rule.get("minItems", 0):
                errors.append(f"{path}: too few items")
            if rule.get("uniqueItems") and len({json.dumps(item, sort_keys=True) for item in value}) != len(value):
                errors.append(f"{path}: items must be unique")
            if "items" in rule:
                for index, child in enumerate(value):
                    visit(child, rule["items"], f"{path}[{index}]")
        if isinstance(value, str):
            if len(value) < rule.get("minLength", 0):
                errors.append(f"{path}: string is too short")
            if "pattern" in rule and not re.search(rule["pattern"], value):
                errors.append(f"{path}: does not match {rule['pattern']}")
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "minimum" in rule and value < rule["minimum"]:
                errors.append(f"{path}: below minimum")
            if "maximum" in rule and value > rule["maximum"]:
                errors.append(f"{path}: above maximum")
        if "anyOf" in rule and not any(not schema_errors_for(value, option) for option in rule["anyOf"]):
            errors.append(f"{path}: does not satisfy anyOf")

    def schema_errors_for(value, rule):
        before = len(errors)
        visit(value, rule, "$probe")
        probe = errors[before:]
        del errors[before:]
        return probe

    visit(instance, schema)
    return errors


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def task_registry(path: Path):
    text = path.read_text(encoding="utf-8")
    payload = re.sub(r"^\s*window\.[A-Z0-9_]+\s*=\s*", "", text).rstrip().removesuffix(";")
    return json.loads(payload)


def main() -> int:
    results = Results()
    registry_path = ROOT / "shared/implementation/case-registry.v2.json"
    registry_schema_path = ROOT / "shared/implementation/case-registry.schema.v2.json"
    package_schema_path = ROOT / "shared/implementation/case-package.schema.v2.json"
    registry = load_json(registry_path)
    registry_schema = load_json(registry_schema_path)
    package_schema = load_json(package_schema_path)

    results.check("registry validates against schema v2", not schema_errors(registry, registry_schema), schema_errors(registry, registry_schema))
    entries = [case for curriculum in registry["curricula"] for campaign in curriculum["campaigns"] for case in campaign["cases"]]
    results.check("registry discovers exactly Cases 01–03 in display order", [entry["id"] for entry in entries] == list(EXPECTED), [entry["id"] for entry in entries])
    results.check("registry contains only operational case fields", all(set(entry) == {"id", "displayOrder", "displayLabel", "title", "version", "status", "editorShell", "editorPackage", "centralWorkflow", "packageStatus", "approval", "historyRecord"} for entry in entries))

    for entry in entries:
        case_id = entry["id"]
        expected_version, expected_counts = EXPECTED[case_id]
        package_path = ROOT / entry["editorPackage"]
        package = load_json(package_path)
        errors = schema_errors(package, package_schema)
        results.check(f"{case_id} package validates against schema v2", not errors, errors)
        results.check(f"{case_id} registry and package identity agree", package["id"] == case_id and package["version"] == entry["version"] == expected_version and package["status"] == entry["status"] == "APPROVED_STABLE")
        results.check(f"{case_id} has exactly four instructional roles", package["supportedRoles"] == ROLES and list(package["rolePageStructure"]) == ROLES)
        results.check(f"{case_id} has complete plus four normal output names", list(package["outputs"]) == ["complete", *ROLES] and all("GRAYSCALE" not in filename.upper() for filename in package["outputs"].values()))
        counts = {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
        results.check(f"{case_id} package page counts are exact", counts == expected_counts, counts)
        results.check(f"{case_id} package uses the canonical institutional identity", package["institutionalIdentity"]["name"] == CANONICAL_SAA and package["institutionalIdentity"]["lockupLines"] == ["Solar", "Agricultural", "Agency"])
        results.check(f"{case_id} package has no migration-era fields", not {"migrationSource", "phase2Authorization", "historicalMaster", "successorMaster", "goldenMaster", "reconciliationRecord"}.intersection(package))

        paths = {
            "content": ROOT / package["content"]["source"],
            "presentation": ROOT / package["presentation"]["source"],
            "taskRegistry": ROOT / package["taskRegistry"]["source"],
        }
        if "icons" in package["sourceHashes"]:
            paths["icons"] = ROOT / package["shell"]["icons"]
        results.check(f"{case_id} all package-controlled sources exist", all(path.is_file() for path in paths.values()), paths)
        results.check(f"{case_id} source hashes verify", all(sha256(path) == package["sourceHashes"][name] for name, path in paths.items()))

        content = paths["content"].read_text(encoding="utf-8")
        identity_sources = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in paths.values())
        results.check(f"{case_id} active sources reject noncanonical SAA expansions", CANONICAL_SAA in identity_sources and not any(variant in identity_sources for variant in REJECTED_SAA))
        soup = BeautifulSoup(content, "html.parser")
        actual_counts = {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES}
        results.check(f"{case_id} worksheet DOM page counts are exact", actual_counts == expected_counts, actual_counts)
        results.check(f"{case_id} content is a worksheet-only fragment", bool(soup.select_one("main")) and not soup.select("script,style,link,iframe,.toolbar"))
        page_ids = [node.get("data-page-id") for node in soup.select(".page[data-page-id]")]
        persist_ids = [node.get("data-persist-id") for node in soup.select("[data-persist-id]")]
        results.check(f"{case_id} page and persistence IDs are unique", len(page_ids) == len(set(page_ids)) and len(persist_ids) == len(set(persist_ids)) and None not in persist_ids)
        results.check(f"{case_id} response fields have accessible names", all(node.get("aria-label") or node.get("aria-labelledby") for node in soup.select("[data-response]")))
        registry_data = task_registry(paths["taskRegistry"])
        results.check(f"{case_id} task registry owns Tasks 1–9 and four roles", [int(task["number"]) for task in registry_data["tasks"]] == list(range(1, 10)) and set(registry_data["roles"]) == set(ROLES))
        results.check(f"{case_id} CER components are page-atomic", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in soup.select("[data-cer-contract],.cer-stack")))
        results.check(f"{case_id} process models are page-atomic", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in soup.select("[data-process-contract],.process-figure,.linear-process")))
        results.check(f"{case_id} figures and tables retain structure", all(figure.select_one("figcaption") for figure in soup.select("figure")) and all(table.select_one("th") and len(table.select("tr")) >= 2 for table in soup.select("table")))

        presentation = paths["presentation"].read_text(encoding="utf-8")
        whole_page_filter = re.search(r"(?:body|\.page)\.grayscale\s*\{[^}]*filter\s*:", presentation, re.I | re.S)
        results.check(f"{case_id} grayscale uses presentation tokens without whole-page filtering", "grayscale" in presentation.lower() and not whole_page_filter)

        history_path = ROOT / package["releaseHistory"]
        history = load_json(history_path)
        former_roles = history.get("formerArtifacts", {}).get("roles", {})
        results.check(f"{case_id} compact release history is complete", history.get("caseId") == case_id and history.get("curriculumVersion") == expected_version and set(former_roles) == set(ROLES) and history.get("rolePageCounts") == expected_counts and history.get("formerArtifactRecoveryCommit") and history.get("recovery"))

    runtime = (APP / "editor-app.js").read_text(encoding="utf-8")
    portable = (APP / "portable-runtime.js").read_text(encoding="utf-8")
    results.check("central editor loads registry and package schema v2", "case-registry.v2.json" in runtime and "SUPPORTED_PACKAGE_SCHEMA = 2" in runtime)
    results.check("central and portable exports never remap grayscale to an output role", 'outputRole: state.role' in runtime and 'outputRole: state.role' in portable and "GRAYSCALE_MISSION" not in runtime + portable)
    results.check("central and portable runtimes preserve grayscale as Boolean presentation state", "state.grayscale" in runtime and "state.grayscale" in portable and 'classList.toggle("grayscale", state.grayscale)' in runtime and 'classList.toggle("grayscale", state.grayscale)' in portable)
    results.check("isolated print paths exclude chrome and page shadow", all(token in runtime and token in portable for token in ["preparePrintFrame", "print-document", "box-shadow:none!important"]))

    structure = subprocess.run([sys.executable, str(ROOT / "shared/validation/validate_canonical_case_structure.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("canonical case-structure validator passes", structure.returncode == 0, (structure.stdout + structure.stderr).strip())
    tracked_candidates = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True, capture_output=True, check=True).stdout.splitlines()
    tracked_png = [path for path in tracked_candidates if (ROOT / path).is_file() and path.endswith(".png") and (path.startswith("apps/curriculum-editor/tests/screenshots/") or "/validation-artifacts/" in path)]
    results.check("no routine generated screenshots remain tracked", not tracked_png, tracked_png)

    payload = {
        "validator": "curriculum-editor-static-v2",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
