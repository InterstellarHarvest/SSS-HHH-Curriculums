#!/usr/bin/env python3
"""Static, schema, package, binding-rule, and protection validation for Phase 2."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup

from validate_static import Results, load_json, schema_errors, semantic_package_errors, task_registry


APP = Path(__file__).resolve().parents[1]
REPO = APP.parents[1]
ROLES = ["student", "teacher", "answer", "accessible", "grayscale"]
CASES = {
    "SSS-C1-CASE01": {
        "version": "1.1",
        "package": "sss/campaign-1/case-01-iss-greenhouse/source/editor-package/case-package.v1.1.json",
        "masterHash": "737239b53ae5af3f25cbaf037d0c9882f50d9e7e8d26b3d03408e469ced6b56f",
        "preMaintenanceHash": "f42365e58802201679b5cd751f102d9a4ecd0ea6f6a6565a860df070018ad02a",
        "counts": {"student": 3, "teacher": 7, "answer": 3, "accessible": 6, "grayscale": 3},
    },
    "SSS-C1-CASE02": {
        "version": "1.0",
        "package": "sss/campaign-1/case-02-lunar-greenhouse/source/editor-package/case-package.v1.0.json",
        "masterHash": "4e5d03a62cba494ae09604194f69578b4c4bcceeeca1f9d53d818109e132fd0d",
        "preMaintenanceHash": "d35c3e0d83a61cbf56799e52b6a1eb3fac4668c1089b674ad0681e92bf30ad86",
        "counts": {"student": 3, "teacher": 7, "answer": 3, "accessible": 5, "grayscale": 3},
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_check(results: Results, name: str, command: list[str]) -> None:
    completed = subprocess.run(command, cwd=REPO, text=True, capture_output=True)
    results.check(name, completed.returncode == 0, (completed.stdout + completed.stderr).strip())


def cer_labels(root) -> list[str]:
    labels = []
    for node in root.select(".canonical-cer-label,.cer-label,.answer-label,.response-prompt"):
        label = node.get_text(" ", strip=True).split(":")[0].upper()
        if label in {"CLAIM", "EVIDENCE", "REASONING"}:
            labels.append(label)
    return labels


def main() -> int:
    results = Results()
    registry = load_json(REPO / "shared/implementation/case-registry.v1.json")
    registry_schema = load_json(REPO / "shared/implementation/case-registry.schema.v1.json")
    package_schema = load_json(REPO / "shared/implementation/case-package.schema.v1.json")
    results.check("registry validates against schema", not schema_errors(registry, registry_schema), schema_errors(registry, registry_schema))
    entries = [case for curriculum in registry["curricula"] for campaign in curriculum["campaigns"] for case in campaign["cases"]]
    compatible = [case for case in entries if case.get("editorPackage")]
    results.check("exactly Cases 01, 02, and 03 are editor-compatible in case order", [case["id"] for case in compatible] == ["SSS-C1-CASE01", "SSS-C1-CASE02", "SSS-C1-CASE03"], [case["id"] for case in compatible])
    results.check("case display metadata provides exact owner labels and order", [(case.get("displayOrder"), case.get("displayLabel")) for case in compatible] == [(1, "1 - ISS Greenhouse"), (2, "2 - Lunar Greenhouse"), (3, "3 - Mars Habitat")])

    for case_id, expected in CASES.items():
        entry = next(case for case in entries if case["id"] == case_id)
        package = load_json(REPO / expected["package"])
        schema_failures = schema_errors(package, package_schema)
        semantic_failures = semantic_package_errors(package)
        results.check(f"{case_id} package validates against schema", not schema_failures, schema_failures)
        results.check(f"{case_id} semantic package validation passes", not semantic_failures, semantic_failures)
        results.check(f"{case_id} registry/package identity, version, and status agree", package["id"] == entry["id"] and package["version"] == entry["version"] == expected["version"] and package["status"] == entry["status"] == "APPROVED_WITH_HTML_MAINTENANCE")
        results.check(f"{case_id} registry points to generated package", entry["editorPackage"] == expected["package"] and (REPO / entry["editorPackage"]).is_file())
        authorization = package.get("phase2Authorization", {})
        approval_path = REPO / authorization.get("approvalRecord", "")
        approval = load_json(approval_path) if approval_path.is_file() else {}
        results.check(
            f"{case_id} final Phase 2 owner approval and closed gates are explicit",
            authorization.get("status") == entry.get("ownerAuthorization") == entry.get("currentMaintainedHtml") == "APPROVED"
            and authorization.get("phase2Status") == entry.get("phase2Status") == "READY_TO_MERGE"
            and authorization.get("ownerGate") == authorization.get("physicalPrintGate") == entry.get("physicalPrintGate") == "PASS"
            and all(authorization.get(key) == "PASS" for key in ["ownerReview", "browserPrintPreview", "physicalPrintReview", "phase2MigrationParity"])
            and authorization.get("approvalDate") == "2026-08-01"
            and authorization.get("owner") == "Nate / Owner"
            and authorization.get("scale") == "100% / Actual Size"
            and approval.get("currentMaintainedHtml") == "APPROVED"
            and all(approval.get(key) == "PASS" for key in ["ownerReview", "browserPrintPreview", "physicalPrintReview", "phase2MigrationParity"])
            and approval.get("rolePageCounts") == expected["counts"]
            and approval.get("allProfilesPagesFit") is True
            and approval.get("artifactPolicy") == {"historicalPdfs": "RETAINED", "currentProduction": "HTML_BASED", "newPdfsGenerated": False},
        )
        migration = package["migrationSource"]
        results.check(f"{case_id} owner-authorized golden and pre-maintenance hashes are recorded", migration.get("kind") == "approved-master-migration" and migration.get("goldenMasterSha256") == expected["masterHash"] and migration.get("preMaintenanceMasterSha256") == expected["preMaintenanceHash"] and migration.get("reconciliationRecord") == authorization.get("reconciliationRecord"))
        content_path = REPO / package["content"]["source"]
        css_path = REPO / package["presentation"]["stylesheet"]
        results.check(f"{case_id} extracted content and presentation hashes verify", sha(content_path) == package["presentation"]["contentSha256"] and sha(css_path) == package["presentation"]["stylesheetSha256"] == package["presentation"]["caseCssSha256"])
        results.check(f"{case_id} package uses Shadow DOM and no complete master at runtime", package["presentation"]["isolation"] == "shadow-dom" and "master/" not in package["content"]["source"])
        results.check(f"{case_id} declares five profiles and six distinct portable HTML outputs", package["supportedRoles"] == ROLES and len(set(package["outputs"].values())) == 6 and all(name.endswith(".html") for name in package["outputs"].values()))
        results.check(f"{case_id} Grayscale maps to Student source identity", package["rolePageStructure"]["grayscale"]["sourceRole"] == "student" and package["rolePageStructure"]["grayscale"]["grayscale"] is True)
        counts = {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
        results.check(f"{case_id} package role page counts match the golden", counts == expected["counts"], counts)
        soup = BeautifulSoup(content_path.read_text(encoding="utf-8"), "html.parser")
        actual_counts = {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES[:-1]}
        results.check(f"{case_id} extracted DOM role page counts match the golden", actual_counts == {role: expected["counts"][role] for role in ROLES[:-1]}, actual_counts)
        page_ids = [node.get("data-page-id") for node in soup.select(".page[data-page-id]")]
        persist_ids = [node.get("data-persist-id") for node in soup.select("[data-persist-id]")]
        results.check(f"{case_id} page and persistence IDs are present and unique", len(page_ids) == len(set(page_ids)) and len(persist_ids) == len(set(persist_ids)) and None not in persist_ids)
        results.check(f"{case_id} response fields retain accessible names", all(node.get("aria-label") or node.get("aria-labelledby") for node in soup.select("[data-response]")))
        tasks = task_registry(REPO / package["taskRegistry"]["source"])["tasks"]
        task_map = {str(task["number"]): task for task in tasks}
        headings = soup.select(".task-heading[data-task-id]")
        results.check(f"{case_id} task registry contains canonical Tasks 1–9", list(task_map) == [str(value) for value in range(1, 10)])
        results.check(f"{case_id} every task heading preserves its registry title", all(node.get("data-task-title") == task_map[node.get("data-task-id")]["title"] for node in headings))
        results.check(f"{case_id} every task heading remains attached to following page content", all((next_node := node.find_next_sibling()) is not None and next_node.find_parent(class_="page") is node.find_parent(class_="page") for node in headings))
        cer_roots = soup.select("[data-cer-contract],.cer-stack")
        results.check(f"{case_id} each CER root is canonical and atomic on one page", bool(cer_roots) and all(cer_labels(root) == ["CLAIM", "EVIDENCE", "REASONING"] and all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in cer_roots))
        process_roots = soup.select("[data-process-contract],.process-figure,.linear-process")
        results.check(f"{case_id} every process model remains atomic", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in process_roots))
        if case_id == "SSS-C1-CASE02":
            results.check("SSS-C1-CASE02 approved process is the intact six-step pollination sequence", any(len(root.select("[data-process-stage],.process-stage,:scope > li")) == 6 for root in process_roots))
        results.check(f"{case_id} figures retain captions on their page", all(figure.select_one("figcaption") and figure.select_one("figcaption").find_parent(class_="page") is figure.find_parent(class_="page") for figure in soup.select("figure")))
        results.check(f"{case_id} tables retain headers and first data rows", all(table.select_one("th") and len(table.select("tr")) >= 2 for table in soup.select("table")))
        results.check(f"{case_id} optional extensions remain intact", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in soup.select("[data-optional-extension]")))
        results.check(f"{case_id} worksheet fragment excludes old toolbar/runtime/iframe", not soup.select("script,style,link,iframe,.toolbar"))
        text = soup.get_text(" ", strip=True)
        results.check(f"{case_id} contains no mandatory group-work direction", not re.search(r"\b(must|required to)\s+(work|collaborate)\s+(with|in)\s+(a |your )?(group|team)\b", text, re.I))

    runtime = (APP / "editor-app.js").read_text(encoding="utf-8")
    portable_runtime = (APP / "portable-runtime.js").read_text(encoding="utf-8")
    app_css = (APP / "editor-app.css").read_text(encoding="utf-8")
    toolbar_source = (REPO / "shared/implementation/editor-shell/v1.0/toolbar.html").read_text(encoding="utf-8")
    results.check("central runtime has no Case 01/02 branches", "SSS-C1-CASE01" not in runtime and "SSS-C1-CASE02" not in runtime)
    results.check("selected-case, state, and content keys are case/version namespaced", "curriculum-editor:selected-case:v1" in runtime and "casePackage.documentKey" in runtime and "stateKey" in runtime and "contentKey" in runtime)
    results.check("case switching replaces isolated worksheet content and styles", "worksheetShadow.replaceChildren(style, worksheetDocument)" in runtime and "data-case-package-font" in runtime)
    results.check("central toolbar exposes Page shadow and exact accessible descriptions", 'document.createTextNode(" Page shadow")' in runtime and "Adds a screen-only shadow around each worksheet page for visual separation." in runtime and "A page is too full when content extends beyond its printable page area." in runtime)
    approved_actions = ["Print / Save PDF", "Download Editable Copy", "Download Worksheet", "Clear Responses", "Reset This Case"]
    transformed_actions = approved_actions[1:]
    old_actions = ["Download Current HTML", "Download Current Role", "Clear Current Role", "Reset Source"]
    results.check("central runtime defines exact approved toolbar labels in action order", approved_actions[0] in toolbar_source and all(label in runtime for label in transformed_actions) and all(runtime.index(transformed_actions[index]) < runtime.index(transformed_actions[index + 1]) for index in range(len(transformed_actions) - 1)))
    results.check("central and portable runtimes omit old visible action labels", all(label not in runtime and label not in portable_runtime for label in old_actions))
    results.check("download actions define exact accessible descriptions", all(description in runtime for description in ["Downloads all roles with the editing toolbar and current changes.", "Downloads only the selected role as a clean HTML worksheet without editing controls."]))
    results.check("clear and reset confirmations use exact owner-approved text", all(text in runtime and text in portable_runtime for text in ["Clear all responses in the current role?", "Reset this case to its approved defaults?\\n\\nThis will remove all locally saved responses, instructional edits, and display settings for this case."]))
    results.check("toolbar action labels cannot wrap internally", '#editorToolbarHost .toolbar button { white-space: nowrap; }' in app_css)
    results.check("page-fit wording covers zero, singular, and plural without changing detection tolerance", all(text in runtime and text in portable_runtime for text in ["Pages fit", "1 page too full", "pages too full"]) and "+ 2" in runtime and "+ 2" in portable_runtime)
    results.check("central and portable print paths use isolated role iframes rather than parent-window print", "preparePrintFrame" in runtime and "preparePrintFrame" in portable_runtime and "frame.contentWindow" in runtime and "printWindow.print()" in runtime and "printWindow.print()" in portable_runtime and "window.print()" not in runtime and "window.print()" not in portable_runtime)
    results.check("isolated printing waits for document load, fonts, and images", all(token in runtime and token in portable_runtime for token in ['addEventListener("load"', ".fonts?.ready", "waitForPrintImage", "image.decode"]))
    results.check("isolated print cleanup uses afterprint plus delayed fallback", all(token in runtime and token in portable_runtime for token in ['addEventListener("afterprint"', "cleanupFallbackMs", "frame.remove()"] ))
    results.check("defensive app print CSS excludes all chrome and resets application geometry", "#editorToolbarHost" in app_css and ".library-rail" in app_css and ".workspace-header" in app_css and ".editor-statuses" in app_css and "@media print" in app_css and "min-height: 0 !important" in app_css)
    harness = (APP / "tests/browser-harness.html").read_text(encoding="utf-8")
    results.check("cross-case browser harness exercises all three cases repeatedly", all(case_id in harness for case_id in ["SSS-C1-CASE01", "SSS-C1-CASE02", "SSS-C1-CASE03"]) and harness.count("for (const item of phase2Cases)") >= 2 and harness.count("selectCase") >= 2)
    results.check("browser harness asserts all 15 isolated print profiles and chrome exclusion", "const printProfiles" in harness and all(label in harness for label in ["Student Grayscale", "isolated print page count is exactly", ".toolbar,#editorToolbarHost,.library-rail,.workspace-header,.editor-statuses", "first-page and continuation identities are intact"]))
    results.check("binding-rule audit is recorded with no blocker", "NO BLOCKING CONTRADICTION" in (APP / "tests/PHASE2_BINDING_RULE_AUDIT.md").read_text(encoding="utf-8"))
    run_check(results, "deterministic Phase 2 extraction passes", [sys.executable, "shared/implementation/build_phase2_case_packages.py", "--check"])
    run_check(results, "protected-artifact inventory passes", [sys.executable, "shared/validation/validate_phase2_protected_inventory.py"])
    run_check(results, "owner reconciliation validator passes", [sys.executable, "shared/validation/validate_phase2_reconciliation.py"])
    run_check(results, "accepted Phase 1 static suite still passes", [sys.executable, "apps/curriculum-editor/tests/validate_static.py"])
    pdf_changes = subprocess.run(["git", "status", "--porcelain", "--", "*.pdf"], cwd=REPO, text=True, capture_output=True, check=True).stdout.splitlines()
    results.check("no PDF was generated or modified", not pdf_changes, pdf_changes)
    payload = {"validator": "curriculum-editor-phase2-static", "status": "PASS" if results.passed == len(results.assertions) else "FAIL", "passed": results.passed, "total": len(results.assertions), "assertions": results.assertions}
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
