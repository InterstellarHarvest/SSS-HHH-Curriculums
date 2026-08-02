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
    "SSS-C1-CASE01": {"version": "1.1", "status": "APPROVED_STABLE", "tasks": 9, "counts": {"student": 3, "teacher": 7, "answer": 3, "accessible": 6}},
    "SSS-C1-CASE02": {"version": "1.0", "status": "APPROVED_STABLE", "tasks": 9, "counts": {"student": 3, "teacher": 7, "answer": 3, "accessible": 5}},
    "SSS-C1-CASE03": {"version": "1.1", "status": "APPROVED_STABLE", "tasks": 9, "counts": {"student": 4, "teacher": 8, "answer": 4, "accessible": 7}},
    "SSS-C1-CASE04": {"version": "0.1", "status": "DRAFT", "tasks": 8, "counts": {"student": 4, "teacher": 7, "answer": 4, "accessible": 6}},
}
CASE04_TASK_TITLES = [
    "Initial Thinking — Identify the Variable",
    "Build the Change-to-Crash Timeline",
    "Isolate Variables and Test Alternatives",
    "Diagnose the Reactor Failure",
    "Model the Repeating Crash Cycle",
    "Explain the Failure with CER",
    "Design Independent Reactor Controls",
    "Exit Ticket — Cause or Effect?",
]
LEGACY_SELF_STYLED_CASES = {"SSS-C1-CASE01", "SSS-C1-CASE02", "SSS-C1-CASE03"}
PROTECTED_SELECTOR_PATTERNS = {
    ".student-id": r"(?<![\w-])\.student-id(?![\w-])",
    ".id-field": r"(?<![\w-])\.id-field(?![\w-])",
    ".mission-title-block": r"(?<![\w-])\.mission-title-block(?![\w-])",
    ".mission-rail": r"(?<![\w-])\.mission-rail(?![\w-])",
    ".hero-title": r"(?<![\w-])\.hero-title(?![\w-])",
    ".mission-subtitle": r"(?<![\w-])\.mission-subtitle(?![\w-])",
    ".identity-mark": r"(?<![\w-])\.identity-mark(?![\w-])",
    ".identity-copy": r"(?<![\w-])\.identity-copy(?![\w-])",
    ".saa-insignia": r"(?<![\w-])\.saa-insignia(?![\w-])",
    ".institution": r"(?<![\w-])\.institution(?![\w-])",
    ".document-role": r"(?<![\w-])\.document-role(?![\w-])",
    ".continuation-header": r"(?<![\w-])\.continuation-header(?![\w-])",
    ".continuation-copy": r"(?<![\w-])\.continuation-copy(?![\w-])",
    ".continuation-role": r"(?<![\w-])\.continuation-role(?![\w-])",
    ".continuation-identity": r"(?<![\w-])\.continuation-identity(?![\w-])",
    "[data-publication-footer]": r"\[data-publication-footer(?:[^\]]*)\]",
    ".canonical-cer": r"(?<![\w-])\.canonical-cer(?![\w-])",
    ".canonical-cer-box": r"(?<![\w-])\.canonical-cer-box(?![\w-])",
    ".canonical-cer-label": r"(?<![\w-])\.canonical-cer-label(?![\w-])",
    ".canonical-cer-response": r"(?<![\w-])\.canonical-cer-response(?![\w-])",
}


def protected_css_definitions(css: str) -> list[str]:
    clean = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    selectors = [match.group(1).strip() for match in re.finditer(r"(?:^|})\s*([^{}]+)\{", clean)]
    return sorted({name for selector in selectors if not selector.startswith("@") for name, pattern in PROTECTED_SELECTOR_PATTERNS.items() if re.search(pattern, selector)})


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
    history_schema_path = ROOT / "shared/implementation/case-release-history.schema.v1.json"
    registry = load_json(registry_path)
    registry_schema = load_json(registry_schema_path)
    package_schema = load_json(package_schema_path)
    history_schema = load_json(history_schema_path)

    detector_probe = protected_css_definitions(".student-id{display:grid}.canonical-cer-response:focus{outline:0}[data-publication-footer]{margin:0}")
    results.check("protected case-CSS selector detector rejects direct invariant-component rules", detector_probe == [".canonical-cer-response", ".student-id", "[data-publication-footer]"], detector_probe)
    results.check("registry validates against schema v2", not schema_errors(registry, registry_schema), schema_errors(registry, registry_schema))
    entries = [case for curriculum in registry["curricula"] for campaign in curriculum["campaigns"] for case in campaign["cases"]]
    results.check("registry discovers exactly Cases 01–04 in display order", [entry["id"] for entry in entries] == list(EXPECTED), [entry["id"] for entry in entries])
    base_fields = {"id", "displayOrder", "displayLabel", "title", "version", "status", "editorShell", "editorPackage", "centralWorkflow", "packageStatus", "approval"}
    results.check("registry contains lifecycle-appropriate operational case fields", all(set(entry) == (base_fields | ({"historyRecord"} if entry["status"] == "APPROVED_STABLE" else set())) for entry in entries))

    for entry in entries:
        case_id = entry["id"]
        expected = EXPECTED[case_id]
        expected_version = expected["version"]
        expected_counts = expected["counts"]
        expected_status = expected["status"]
        package_path = ROOT / entry["editorPackage"]
        package = load_json(package_path)
        errors = schema_errors(package, package_schema)
        results.check(f"{case_id} package validates against schema v2", not errors, errors)
        results.check(f"{case_id} registry and package identity agree", package["id"] == case_id and package["version"] == entry["version"] == expected_version and package["status"] == entry["status"] == expected_status)
        lifecycle_ok = (
            expected_status == "APPROVED_STABLE"
            and package.get("releaseHistory") == entry.get("historyRecord")
            and package["approval"].get("status") == entry["approval"].get("status") == "APPROVED"
            and package["approval"].get("printStatus") == entry["approval"].get("printStatus") == "PASS"
        ) or (
            expected_status == "DRAFT"
            and "releaseHistory" not in package
            and "historyRecord" not in entry
            and package["approval"].get("status") == entry["approval"].get("status") == "OWNER_REVIEW_NOT_STARTED"
            and package["approval"].get("printStatus") == entry["approval"].get("printStatus") == "NOT_RUN"
        )
        results.check(f"{case_id} lifecycle metadata matches release policy", lifecycle_ok)
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
        expected_task_numbers = list(range(1, expected["tasks"] + 1))
        results.check(f"{case_id} task registry owns its numbered tasks and four roles", [int(task["number"]) for task in registry_data["tasks"]] == expected_task_numbers and set(registry_data["roles"]) == set(ROLES))
        results.check(f"{case_id} CER components are page-atomic", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in soup.select("[data-cer-contract],.cer-stack")))
        results.check(f"{case_id} process models are page-atomic", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in soup.select("[data-process-contract],.process-figure,.linear-process")))
        results.check(f"{case_id} figures and tables retain structure", all(figure.select_one("figcaption") for figure in soup.select("figure")) and all(table.select_one("th") and len(table.select("tr")) >= 2 for table in soup.select("table")))

        presentation = paths["presentation"].read_text(encoding="utf-8")
        whole_page_filter = re.search(r"(?:body|\.page)\.grayscale\s*\{[^}]*filter\s*:", presentation, re.I | re.S)
        results.check(f"{case_id} grayscale uses presentation tokens without whole-page filtering", "grayscale" in presentation.lower() and not whole_page_filter)
        uses_shared_components = package["presentation"].get("sharedComponentStyles") is True
        if case_id not in LEGACY_SELF_STYLED_CASES:
            results.check(f"{case_id} opts into shared protected-component styles", uses_shared_components)
        if uses_shared_components:
            protected_definitions = protected_css_definitions(presentation)
            results.check(f"{case_id} case presentation defines no protected shared selectors", not protected_definitions, protected_definitions)

        if expected_status == "APPROVED_STABLE":
            history_path = ROOT / package["releaseHistory"]
            history = load_json(history_path)
            history_errors = schema_errors(history, history_schema)
            results.check(f"{case_id} release history validates against schema v1", not history_errors, history_errors)
            former_roles = history.get("formerArtifacts", {}).get("roles", {})
            results.check(f"{case_id} compact release history is complete", history.get("caseId") == case_id and history.get("curriculumVersion") == expected_version and set(former_roles) == set(ROLES) and history.get("rolePageCounts") == expected_counts and history.get("formerArtifactRecoveryCommit") and history.get("recovery") and isinstance(history.get("priorApprovedReleases"), list))
        else:
            case_root = package_path.parents[1]
            results.check(f"{case_id} unreleased DRAFT has no history release record", not (case_root / "history").exists() and "releaseHistory" not in package)

        if case_id == "SSS-C1-CASE04":
            task_titles = [task["title"] for task in registry_data["tasks"]]
            results.check("Case 04 task registry uses the eight locked titles", task_titles == CASE04_TASK_TITLES, task_titles)
            role_task_orders = {
                role: [int(node["data-shell-task-heading"]) for page in soup.select(f'.page[data-role="{role}"]') for node in page.select("[data-shell-task-heading]")]
                for role in ["student", "answer", "accessible"]
            }
            results.check("Case 04 Student, Answer Key, and Accessible task order has exact parity", all(order == expected_task_numbers for order in role_task_orders.values()), role_task_orders)
            results.check("Case 04 visual component contracts are complete", all(soup.select_one(selector) for selector in ["[data-timeline-contract]", "[data-evidence-summary]", "[data-process-contract]", "[data-cause-effect-contract]", "[data-systems-contract]", "[data-cer-contract]"]))
            timeline_roots = soup.select("[data-timeline-contract]")
            process_roots = soup.select("[data-process-contract]")
            results.check("Case 04 timeline and process models are page-atomic", all(root.find_parent(class_="page") is child.find_parent(class_="page") for root in timeline_roots + process_roots for child in root.select("*")))
            accessible_pages = soup.select('.page[data-role="accessible"]')
            results.check("Case 04 Accessible pages preserve document and task reading order", [page.get("data-page-id") for page in accessible_pages] == [f"accessible-mission-{index:02d}" for index in range(1, 7)] and role_task_orders["accessible"] == expected_task_numbers)
            required_sequence = ["Four months of stable operation", "Lighting changes from 16/8 to uncontrolled 24/0", "About one week later: first crash", "Every 6–8 days: another crash", "Between crashes: surviving cells rebuild"]
            results.check("Case 04 uses all locked relative sequence labels", all(label in content for label in required_sequence))
            results.check("Case 04 omits unsupported mission-day and precise-density data", not re.search(r"Day\s*12[18]|culture density\s*[:=]\s*\d", content, re.I))
            results.check("Case 04 keeps reactor-specific continuous-cultivation qualification", "Continuous cultivation may work with appropriate independent intensity, mixing, density, and process controls." in content)
            learner_first_pages = {role: soup.select_one(f'.page[data-role="{role}"]') for role in ["student", "accessible"]}
            expected_fields = {
                "student": ["student-name", "student-date", "student-class"],
                "accessible": ["a-name", "a-date", "a-class"],
            }
            id_contracts = {}
            for role, page in learner_first_pages.items():
                row = page.select_one(".student-id") if page else None
                fields = row.select(":scope > .id-field") if row else []
                id_contracts[role] = bool(
                    row
                    and row.get("aria-label") == "Student identification"
                    and row.parent.select_one(":scope > :first-child") is row
                    and len(fields) == 3
                    and [field.select_one(":scope > strong").get_text(strip=True) if field.select_one(":scope > strong") else None for field in fields] == ["Name", "Date", "Period"]
                    and [field.select_one(":scope > span").get("data-field") if field.select_one(":scope > span") else None for field in fields] == expected_fields[role]
                    and all(field.name == "div" and not field.select("label") for field in fields)
                )
            results.check("Case 04 Student and Accessible use the exact canonical identification-row structure", all(id_contracts.values()), id_contracts)

            first_pages = [soup.select_one(f'.page[data-role="{role}"]') for role in ROLES]
            title_blocks = [page.select_one('.mission-title-block[data-header-contract="printable-v1.1"]') if page else None for page in first_pages]
            title_contract = all(
                title
                and [child.get("class", [None])[0] for child in title.find_all(recursive=False)] == ["mission-rail", "mission-title-copy", "identity-mark"]
                and title.select_one(":scope > .mission-title-copy > .hero-title")
                and title.select_one(":scope > .mission-title-copy > .mission-subtitle")
                and title.select_one(':scope > .identity-mark > img.saa-insignia[alt="Solar Agricultural Agency insignia"][src="../../../../shared/assets/insignia/saa.svg"]')
                and title.select_one(":scope > .identity-mark > .identity-copy > .institution")
                and title.select_one(":scope > .identity-mark > .identity-copy > .document-role")
                for title in title_blocks
            )
            results.check("Case 04 first-page title blocks use the exact shared child contract and SAA image", title_contract)
            results.check("Case 04 mission subtitle uses the locked punctuation", all(title.select_one(".mission-subtitle").get_text(strip=True) == "Campaign 1 · Case 04 · L2 Lagrange Point, Orbital Research Station" for title in title_blocks if title))

            continuation_headers = soup.select('.continuation-header[data-header-contract="printable-v1.1"]')
            expected_continuations = sum(expected_counts.values()) - len(ROLES)
            continuation_contract = len(continuation_headers) == expected_continuations and all(
                [child.get("class", [None])[0] for child in header.find_all(recursive=False)] == ["continuation-copy", "continuation-identity"]
                and header.select_one(":scope > .continuation-copy > h1")
                and header.select_one(":scope > .continuation-copy > .continuation-role")
                and header.select_one(':scope > .continuation-identity > img.saa-insignia[alt="Solar Agricultural Agency insignia"][src="../../../../shared/assets/insignia/saa.svg"]')
                and header.select_one(":scope > .continuation-identity > .institution")
                for header in continuation_headers
            )
            results.check("Case 04 continuation headers use the exact shared child contract and SAA image", continuation_contract, len(continuation_headers))
            saa_asset = next((asset for asset in package["assets"] if asset["id"] == "saa-insignia"), None)
            results.check("Case 04 package embeds the shared SAA SVG asset", saa_asset == {"id": "saa-insignia", "type": "image/svg+xml", "source": "shared/assets/insignia/saa.svg", "selector": ".saa-insignia", "embed": True}, saa_asset)

            cer_contracts = {root.get("data-cer-contract"): [box.select_one(":scope > .canonical-cer-label").get_text(strip=True) if box.select_one(":scope > .canonical-cer-label") else None for box in root.select(":scope > .canonical-cer-box")] for root in soup.select(".canonical-cer[data-cer-contract]")}
            results.check("Case 04 CER uses only the three approved atomic contracts", cer_contracts == {"student-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "answer-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "accessible-v1.0": ["CLAIM", "EVIDENCE", "REASONING"]}, cer_contracts)
            student_distribution = [[int(node["data-shell-task-heading"]) for node in page.select("[data-shell-task-heading]")] for page in soup.select('.page[data-role="student"]')]
            results.check("Case 04 Student page 1 contains complete Tasks 1 and 2 and does not split Task 3", student_distribution[0] == [1, 2] and student_distribution[1][0] == 3, student_distribution)
            task_two = soup.select_one('.page[data-page-id="student-mission-01"] .task-block [data-shell-task-heading="2"]')
            results.check("Case 04 Student Task 2 is atomic on page 1", bool(task_two and task_two.find_parent(class_="task-block") and task_two.find_parent(class_="task-block").find_parent(class_="page").get("data-page-id") == "student-mission-01"))

    runtime = (APP / "editor-app.js").read_text(encoding="utf-8")
    portable = (APP / "portable-runtime.js").read_text(encoding="utf-8")
    protected_styles_path = ROOT / "shared/implementation/editor-shell/v1.0/protected-printable-components.css"
    results.check("central editor loads registry and package schema v2", "case-registry.v2.json" in runtime and "SUPPORTED_PACKAGE_SCHEMA = 2" in runtime)
    results.check("central editor applies the shared protected-component stylesheet after case presentation", protected_styles_path.is_file() and "protected-printable-components.css" in runtime and "[...sharedStyles, presentationCss, protectedComponentStyles]" in runtime)
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
