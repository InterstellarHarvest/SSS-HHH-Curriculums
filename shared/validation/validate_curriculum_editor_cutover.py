#!/usr/bin/env python3
"""Validate the Cases 01-03 central Curriculum Editor workflow cutover."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASELINE = "e347370ed55913f04b54b8e942f191808f8e4aa9"
MANIFEST_PATH = ROOT / "shared/implementation/CURRICULUM_EDITOR_CUTOVER_v1.json"
INVENTORY_PATH = ROOT / "shared/implementation/CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json"
REGISTRY_PATH = ROOT / "shared/implementation/case-registry.v1.json"
LEDGER_PATH = ROOT / "shared/implementation/phase2-protected-artifacts.v1.json"
APPROVAL_PATH = ROOT / "apps/curriculum-editor/CUTOVER_OWNER_APPROVAL.md"
VALIDATION_RESULTS_PATH = ROOT / "apps/curriculum-editor/CUTOVER_VALIDATION_RESULTS.json"
CUTOVER_REF = "shared/implementation/CURRICULUM_EDITOR_CUTOVER_v1.json"
APPROVAL_REF = "apps/curriculum-editor/CUTOVER_OWNER_APPROVAL.md"
CASE_ROOTS = (
    "sss/campaign-1/case-01-iss-greenhouse/",
    "sss/campaign-1/case-02-lunar-greenhouse/",
    "sss/campaign-1/case-03-mars-habitat/",
)
ACTIVE_DOCS = (
    "README.md",
    "apps/curriculum-editor/README.md",
    "shared/implementation/CURRICULUM_EDITOR_ARCHITECTURE_v1.0.md",
    "shared/implementation/REPOSITORY_CURRICULUM_LIBRARY_ARCHITECTURE.md",
    "shared/implementation/SSS_HHH_V1_EDITABLE_MASTER_HANDOFF.md",
    "shared/implementation/CURRICULUM_EDITOR_CUTOVER_v1.md",
    "sss/campaign-1/case-01-iss-greenhouse/README.md",
    "sss/campaign-1/case-02-lunar-greenhouse/README.md",
    "sss/campaign-1/case-03-mars-habitat/README.md",
)
EXPECTED_CASES = (
    ("SSS-C1-CASE01", "1.1", "1 - ISS Greenhouse"),
    ("SSS-C1-CASE02", "1.0", "2 - Lunar Greenhouse"),
    ("SSS-C1-CASE03", "1.1", "3 - Mars Habitat"),
)
ROLES = ("student", "teacher", "answer", "accessible", "grayscale")
CLASSIFICATIONS = {
    "approved release snapshot",
    "historical provenance",
    "compatibility runtime",
    "validation dependency",
    "candidate for later cleanup",
    "must retain permanently",
}
LEGACY_TOOL_PATHS = {
    "sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/build_case01_html_maintenance.py",
    "sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/validate_case01_html_maintenance.py",
    "sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/validate_case01_rc.py",
    "sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/validate_case01_v1_1.py",
    "sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/revalidate_packet.mjs",
    "sss/campaign-1/case-02-lunar-greenhouse/validation-artifacts/build_case02_cer_html.py",
    "sss/campaign-1/case-02-lunar-greenhouse/validation-artifacts/validate_case02.py",
    "sss/campaign-1/case-02-lunar-greenhouse/validation-artifacts/validate_case02_cer_html.py",
    "sss/campaign-1/case-03-mars-habitat/validation-artifacts/build_case03_html.py",
    "sss/campaign-1/case-03-mars-habitat/validation-artifacts/build_case03_v1_1.py",
    "sss/campaign-1/case-03-mars-habitat/validation-artifacts/render_case03_browser_review.py",
    "sss/campaign-1/case-03-mars-habitat/validation-artifacts/validate_case03_editor_shell.py",
    "sss/campaign-1/case-03-mars-habitat/validation-artifacts/validate_case03_v1.py",
}


class Results:
    def __init__(self) -> None:
        self.checks: list[tuple[str, bool, str]] = []

    def check(self, name: str, condition: bool, detail: Any = "") -> None:
        self.checks.append((name, bool(condition), str(detail)))

    def finish(self) -> int:
        failures = [(name, detail) for name, passed, detail in self.checks if not passed]
        passed = len(self.checks) - len(failures)
        print(f"Curriculum Editor cutover validation: {passed}/{len(self.checks)} {'PASS' if not failures else 'FAIL'}")
        if failures:
            for name, detail in failures:
                print(f"FAIL: {name}" + (f" — {detail}" if detail else ""))
            return 1
        print("Cases: 3/3 registered and package/hash verified")
        print("Protected snapshots: 7 masters and 15 current role outputs verified")
        print("Legacy workflow inventory: 44/44 retained items covered")
        print("PDF policy: 20/20 retained PDFs unchanged; 0 added, 0 removed, 0 modified")
        print("Status: APPROVED · OWNER_REVIEW_PASS · READY_TO_MERGE")
        return 0


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def baseline_paths(*pathspecs: str) -> set[str]:
    output = git("ls-tree", "-r", "--name-only", BASELINE, "--", *pathspecs)
    return set(output.decode("utf-8").splitlines())


def baseline_bytes(path: str) -> bytes:
    return git("show", f"{BASELINE}:{path}")


def registry_cases(registry: dict[str, Any]) -> list[dict[str, Any]]:
    sss = next(item for item in registry["curricula"] if item["id"] == "SSS")
    campaign = next(item for item in sss["campaigns"] if item["id"] == "campaign-1")
    return campaign["cases"]


def referenced_package_paths(package: dict[str, Any]) -> set[str]:
    paths = {package["content"]["source"], package["taskRegistry"]["source"], package["shell"]["toolbar"], package["shell"]["icons"]}
    paths.update(package["shell"]["styles"])
    paths.update(style["source"] for style in package["styles"])
    paths.update(asset["source"] for asset in package.get("assets", []) if "source" in asset)
    presentation = package.get("presentation", {})
    if presentation.get("stylesheet"):
        paths.add(presentation["stylesheet"])
    return paths


def validate_packages(results: Results, manifest_cases: list[dict[str, Any]], registry: dict[str, Any]) -> None:
    cases = registry_cases(registry)
    actual_identity = [(case["id"], case["version"], case["displayLabel"]) for case in cases]
    results.check("registry has exact current cases, versions, order, and labels", actual_identity == list(EXPECTED_CASES), actual_identity)
    by_id = {case["id"]: case for case in cases}
    manifest_by_id = {case["id"]: case for case in manifest_cases}

    for case_id, version, label in EXPECTED_CASES:
        case = by_id.get(case_id, {})
        cutover_case = manifest_by_id.get(case_id, {})
        results.check(f"{case_id} registry central workflow metadata", all((
            case.get("editorShell") == "1.0",
            case.get("centralWorkflow") == "CANONICAL",
            case.get("packageStatus") == "APPROVED",
            case.get("legacyEmbeddedEditorStatus") == "DEPRECATED_COMPATIBILITY",
            case.get("approvedMasterStatus") == "APPROVED_RELEASE_SNAPSHOT",
            case.get("cutoverStatus") == "APPROVED",
            case.get("cutoverOwnerReview") == "OWNER_REVIEW_PASS",
            case.get("cutoverMergeStatus") == "READY_TO_MERGE",
            case.get("cutoverManifest") == CUTOVER_REF,
            case.get("cutoverOwnerApproval") == APPROVAL_REF,
        )), case)
        results.check(f"{case_id} manifest identity/status", all((
            cutover_case.get("version") == version,
            cutover_case.get("displayLabel") == label,
            cutover_case.get("centralWorkflow") == "CANONICAL",
            cutover_case.get("casePackage") == "CANONICAL_ACTIVE_SOURCE",
            cutover_case.get("approvedMaster") == "APPROVED_RELEASE_SNAPSHOT",
            cutover_case.get("embeddedEditor") == "DEPRECATED_COMPATIBILITY",
        )), cutover_case)

        package_rel = case.get("editorPackage", "")
        package_path = ROOT / package_rel
        results.check(f"{case_id} package path agrees", package_rel == cutover_case.get("packagePath") and package_path.is_file(), package_rel)
        if not package_path.is_file():
            continue
        package = load_json(package_path)
        package_hash = sha256(package_path)
        results.check(f"{case_id} package hash", package_hash == cutover_case.get("packageSha256"), package_hash)
        results.check(f"{case_id} package identity and shell", package.get("id") == case_id and package.get("version") == version and package.get("shell", {}).get("version") == "1.0", package.get("id"))
        refs = referenced_package_paths(package)
        missing = sorted(path for path in refs if not (ROOT / path).is_file())
        results.check(f"{case_id} package references exist", not missing, missing)
        presentation = package.get("presentation", {})
        content = ROOT / package["content"]["source"]
        case_css = ROOT / package["styles"][0]["source"]
        presentation_css = ROOT / presentation.get("stylesheet", package["styles"][0]["source"])
        results.check(f"{case_id} package content hash", content.is_file() and sha256(content) == presentation.get("contentSha256"), presentation.get("contentSha256"))
        results.check(f"{case_id} package case CSS hash", case_css.is_file() and sha256(case_css) == presentation.get("caseCssSha256"), presentation.get("caseCssSha256"))
        results.check(f"{case_id} package presentation hash", presentation_css.is_file() and sha256(presentation_css) == presentation.get("stylesheetSha256"), presentation.get("stylesheetSha256"))

        master_rel = case.get("master", "")
        master_path = ROOT / master_rel
        master_hash = sha256(master_path) if master_path.is_file() else "MISSING"
        results.check(f"{case_id} current master path/hash", master_rel == cutover_case.get("currentMasterPath") and master_hash == cutover_case.get("currentMasterSha256") == case.get("currentMasterSha256"), master_hash)
        role_paths_ok = case.get("roles", {}) == {role: cutover_case.get("currentRoles", {}).get(role, {}).get("path") for role in ROLES}
        results.check(f"{case_id} current role paths retained", role_paths_ok, case.get("roles"))
        for role in ROLES:
            role_rel = case.get("roles", {}).get(role, "")
            role_path = ROOT / role_rel
            role_hash = sha256(role_path) if role_path.is_file() else "MISSING"
            expected = cutover_case.get("currentRoles", {}).get(role, {}).get("sha256")
            results.check(f"{case_id} {role} role hash", role_hash == expected == case.get("currentRoleSha256", {}).get(role), role_hash)


def validate_protection(results: Results, manifest: dict[str, Any]) -> None:
    ledger_hash = sha256(LEDGER_PATH)
    results.check("protected ledger path/hash", manifest.get("protectedArtifactLedger") == {
        "path": "shared/implementation/phase2-protected-artifacts.v1.json",
        "sha256": ledger_hash,
    }, ledger_hash)
    ledger = load_json(LEDGER_PATH)
    for artifact in ledger["artifacts"]:
        path = ROOT / artifact["path"]
        actual = sha256(path) if path.is_file() else "MISSING"
        results.check(f"protected ledger {artifact['path']}", actual == artifact["sha256"], actual)

    protected_case_paths = baseline_paths(*CASE_ROOTS)
    protected_case_paths = {path for path in protected_case_paths if path not in {root + "README.md" for root in CASE_ROOTS}}
    changed = []
    missing = []
    for path in sorted(protected_case_paths):
        current = ROOT / path
        if not current.is_file():
            missing.append(path)
        elif current.read_bytes() != baseline_bytes(path):
            changed.append(path)
    results.check("all baseline case artifacts except active READMEs remain present", not missing, missing)
    results.check("all baseline case artifacts except active READMEs remain byte-identical", not changed, changed)

    baseline_pdfs = {path for path in baseline_paths() if path.lower().endswith(".pdf")}
    ledger_pdfs = {artifact["path"] for artifact in ledger["artifacts"] if artifact["category"] == "historical-pdf"}
    expected_pdfs = baseline_pdfs | ledger_pdfs
    ledger_pdf_hashes = {artifact["path"]: artifact["sha256"] for artifact in ledger["artifacts"] if artifact["category"] == "historical-pdf"}
    current_pdfs = {str(path.relative_to(ROOT)) for path in ROOT.rglob("*.pdf") if ".git" not in path.parts}
    results.check("no PDFs added or removed", current_pdfs == expected_pdfs, sorted(current_pdfs ^ expected_pdfs))
    changed_pdfs = []
    for path in sorted(expected_pdfs & current_pdfs):
        if path in baseline_pdfs:
            unchanged = (ROOT / path).read_bytes() == baseline_bytes(path)
        else:
            unchanged = sha256(ROOT / path) == ledger_pdf_hashes[path]
        if not unchanged:
            changed_pdfs.append(path)
    results.check("no PDFs modified", not changed_pdfs, changed_pdfs)
    results.check("expected historical PDF total retained", len(current_pdfs) == 20, len(current_pdfs))


def validate_inventory(results: Results, inventory: dict[str, Any]) -> None:
    items = inventory.get("items", [])
    paths = [item.get("path", "") for item in items]
    results.check("legacy inventory status and deletion policy", inventory.get("status") == "APPROVED" and inventory.get("policy") == {
        "embeddedEditor": "DEPRECATED_COMPATIBILITY",
        "deletionDuringCutover": "PROHIBITED",
        "repositoryCleanup": "NOT_STARTED",
    }, inventory.get("policy"))
    results.check("legacy inventory has 44 unique items", len(items) == len(set(paths)) == 44, len(items))
    results.check("legacy inventory paths all exist", all((ROOT / path).is_file() for path in paths), [path for path in paths if not (ROOT / path).is_file()])
    invalid_classes = {value for item in items for value in item.get("classifications", []) if value not in CLASSIFICATIONS}
    results.check("legacy inventory classifications use controlled vocabulary", not invalid_classes, invalid_classes)
    results.check("permanent and cleanup classifications do not conflict", all(not ({"must retain permanently", "candidate for later cleanup"} <= set(item.get("classifications", []))) for item in items))

    inventory_paths = set(paths)
    runtime_html = set()
    for root in CASE_ROOTS:
        case_root = ROOT / root
        for path in list((case_root / "master").glob("*.html")) + list((case_root / "published").rglob("*.html")):
            if "<script" in path.read_text(encoding="utf-8"):
                runtime_html.add(str(path.relative_to(ROOT)))
    results.check("all embedded master and portable role runtimes are inventoried", runtime_html <= inventory_paths, sorted(runtime_html - inventory_paths))
    historical_sources = {str(path.relative_to(ROOT)) for path in (ROOT / "sss/campaign-1/case-03-mars-habitat/source/editor").iterdir() if path.is_file()}
    results.check("historical Case 03 case-owned editor sources are inventoried", historical_sources <= inventory_paths, sorted(historical_sources - inventory_paths))
    results.check("legacy build and validation tools are inventoried", LEGACY_TOOL_PATHS <= inventory_paths, sorted(LEGACY_TOOL_PATHS - inventory_paths))
    type_totals = Counter(item.get("artifactType") for item in items)
    results.check("legacy inventory type totals", type_totals == {
        "embedded-editor-master": 7,
        "portable-role-runtime": 20,
        "validation-fixture": 1,
        "historical-case-owned-source": 3,
        "legacy-build-or-validation-tool": 13,
    }, dict(type_totals))


def validate_docs(results: Results) -> None:
    prohibited = (
        "central cutover has not been performed",
        "remain canonical until a separately authorized central cutover",
        "central cutover remains a separate decision",
        "opens the relevant case master or role output",
    )
    for rel in ACTIVE_DOCS:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        lower = text.lower()
        results.check(f"active documentation exists: {rel}", path.is_file())
        results.check(f"active documentation names canonical central workflow: {rel}", "central" in lower and "canonical" in lower)
        results.check(f"active documentation does not direct primary embedded workflow: {rel}", not any(phrase in lower for phrase in prohibited), [phrase for phrase in prohibited if phrase in lower])
    combined = "\n".join((ROOT / rel).read_text(encoding="utf-8") for rel in ACTIVE_DOCS)
    results.check("active documentation has exact launch command and URL", "python3 apps/curriculum-editor/serve.py" in combined and "http://127.0.0.1:8000/apps/curriculum-editor/" in combined)
    approved_actions = ("Print / Save PDF", "Download Editable Copy", "Download Worksheet", "Clear Responses", "Reset This Case")
    results.check("active documentation covers the exact approved toolbar actions", all(label in combined for label in approved_actions))
    results.check("active documentation omits superseded toolbar labels", all(label not in combined for label in ("Download Current HTML", "Download Current Role", "Clear Current Role", "Reset Source")))
    results.check("active documentation records version-menu and PDF accessibility rules", "Versions are not selected in the primary case menu" in combined and "separate accessibility review" in combined)
    results.check("active documentation records snapshots and compatibility-only editors", "release snapshots" in combined and "compatibility" in combined)


def main() -> int:
    results = Results()
    try:
        git("cat-file", "-e", f"{BASELINE}^{{commit}}")
    except subprocess.CalledProcessError as exc:
        results.check("required baseline commit exists", False, exc)
        return results.finish()
    results.check("required baseline commit exists", True)

    manifest = load_json(MANIFEST_PATH)
    inventory = load_json(INVENTORY_PATH)
    registry = load_json(REGISTRY_PATH)
    results.check("cutover manifest version/status/gate", manifest.get("schemaVersion") == 1 and manifest.get("cutoverVersion") == "1.0" and manifest.get("status") == "APPROVED" and manifest.get("ownerGate") == "OWNER_REVIEW_PASS" and manifest.get("mergeStatus") == "READY_TO_MERGE")
    acceptance = manifest.get("acceptance", {})
    results.check("cutover acceptance commits", acceptance.get("phase1Commit") == "7b5b724b4941a7ad926fe1b0d644f6905ff55067" and acceptance.get("phase2Commit") == BASELINE and acceptance.get("cutoverImplementationCommit") == "5afda8d78e22e433bbb1e20faab88b4bee882275" and acceptance.get("cutoverOwnerApproval") == APPROVAL_REF)
    results.check("cutover launch path", manifest.get("application", {}) == {
        "path": "apps/curriculum-editor/",
        "launchCommand": "python3 apps/curriculum-editor/serve.py",
        "url": "http://127.0.0.1:8000/apps/curriculum-editor/",
        "editorShellVersion": "1.0",
    })
    results.check("cutover policy boundary", all((
        manifest.get("policies", {}).get("historicalPdfs") == "RETAINED",
        manifest.get("policies", {}).get("pdfGeneration") == "PROHIBITED",
        manifest.get("policies", {}).get("repositoryCleanup") == "NOT_STARTED",
        manifest.get("policies", {}).get("case04") == "NOT_STARTED",
    )), manifest.get("policies"))

    validate_packages(results, manifest.get("effectiveCases", []), registry)
    validate_protection(results, manifest)
    validate_inventory(results, inventory)
    validate_docs(results)
    approval = manifest.get("ownerApproval", {})
    results.check("machine-readable owner approval is exact", approval == {
        "date": "2026-08-01",
        "tester": "Nate / Owner",
        "documentedLaunchPath": "PASS",
        "cases01Through03CentralLoading": "PASS",
        "activeDocumentationConsistency": "PASS",
        "canonicalCentralWorkflow": "PASS",
        "approvedReleaseSnapshotRetention": "PASS",
        "deprecatedCompatibilityClassification": "PASS",
        "noPrematureDeletion": "PASS",
        "repositoryCleanup": "NOT_STARTED",
        "case04": "NOT_STARTED",
        "record": APPROVAL_REF,
    }, approval)
    checklist_path = ROOT / manifest.get("ownerReviewChecklist", "")
    checklist = checklist_path.read_text(encoding="utf-8") if checklist_path.is_file() else ""
    results.check("owner checklist records approved closed gate", checklist_path.is_file() and "**Cutover status:** APPROVED" in checklist and "**Owner gate:** OWNER REVIEW PASS" in checklist and "**Merge status:** READY TO MERGE" in checklist and "- [x] PASS" in checklist)
    approval_text = APPROVAL_PATH.read_text(encoding="utf-8") if APPROVAL_PATH.is_file() else ""
    results.check("additive owner approval record is complete", manifest.get("ownerApprovalRecord") == APPROVAL_REF and APPROVAL_PATH.is_file() and all(token in approval_text for token in ("2026-08-01", "Nate / Owner", "APPROVED", "OWNER REVIEW PASS", "READY TO MERGE", "Repository cleanup: NOT_STARTED", "Case 04: NOT_STARTED")))
    validation_results = load_json(VALIDATION_RESULTS_PATH) if VALIDATION_RESULTS_PATH.is_file() else {}
    results.check("machine-readable cutover validation results are approved", manifest.get("validationResults") == "apps/curriculum-editor/CUTOVER_VALIDATION_RESULTS.json" and validation_results.get("status") == "PASS" and validation_results.get("cutoverStatus") == "APPROVED" and validation_results.get("ownerReview") == "OWNER_REVIEW_PASS" and validation_results.get("mergeStatus") == "READY_TO_MERGE")
    return results.finish()


if __name__ == "__main__":
    sys.exit(main())
