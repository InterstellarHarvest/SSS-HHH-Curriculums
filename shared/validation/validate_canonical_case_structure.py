#!/usr/bin/env python3
"""Fail unless every current case uses the lean canonical source/history layout."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CAMPAIGN = ROOT / "sss/campaign-1"
FORBIDDEN_DIRS = {
    "master", "published", "reports", "review", "validation-artifacts",
    "editor-package", "editor-phase2", "editor-v1.1", "editor",
}
REQUIRED_SOURCE = {"case-package.json", "content.html", "presentation.css", "task-registry.js"}
ROLES = ["student", "teacher", "answer", "accessible"]
COMMIT_FIELDS = {
    "case-01": {
        "originalReleaseApprovalCommit": "e524d333f28a1515571f038e3ed494d87aa812d3",
        "canonicalSourceApprovalCommit": "e347370ed55913f04b54b8e942f191808f8e4aa9",
    },
    "case-02": {
        "originalReleaseApprovalCommit": "e524d333f28a1515571f038e3ed494d87aa812d3",
        "canonicalSourceApprovalCommit": "e347370ed55913f04b54b8e942f191808f8e4aa9",
    },
    "case-03": {
        "originalReleaseApprovalCommit": "7b5b724b4941a7ad926fe1b0d644f6905ff55067",
        "canonicalSourceApprovalCommit": "7b5b724b4941a7ad926fe1b0d644f6905ff55067",
    },
    "case-04": {
        "originalReleaseApprovalCommit": "9d8c3dd9222f6b3a2954b8ba14eb1cee38eb69ba",
        "canonicalSourceApprovalCommit": "9d8c3dd9222f6b3a2954b8ba14eb1cee38eb69ba",
    },
    "case-05": {
        "originalReleaseApprovalCommit": "c73140841559b1ef56f5088e759e41a253856723",
        "canonicalSourceApprovalCommit": "c73140841559b1ef56f5088e759e41a253856723",
    },
    "case-06": {
        "originalReleaseApprovalCommit": "a1a7308cdb6803e7567dfec6cc7346bed03310c1",
        "canonicalSourceApprovalCommit": "a1a7308cdb6803e7567dfec6cc7346bed03310c1",
    },
}
EXPECTED_PRIOR = {
    "case-01": {
        "version": "1.0",
        "commit": "7f3504aa33aaefbf57583ceb2be1ab2af88d10b0",
        "complete": "sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html",
        "roles": {},
    },
    "case-02": None,
    "case-03": {
        "version": "1.0",
        "commit": "a81cdd728dc0f444b969f5fcec2f05dd54115549",
        "complete": "sss/campaign-1/case-03-mars-habitat/master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html",
        "roles": {
            "student": "sss/campaign-1/case-03-mars-habitat/published/SSS_C1_CASE03_STUDENT_MISSION_v1.0.html",
            "teacher": "sss/campaign-1/case-03-mars-habitat/published/SSS_C1_CASE03_TEACHER_GUIDE_v1.0.html",
            "answer": "sss/campaign-1/case-03-mars-habitat/published/SSS_C1_CASE03_ANSWER_KEY_v1.0.html",
            "accessible": "sss/campaign-1/case-03-mars-habitat/published/SSS_C1_CASE03_ACCESSIBLE_MISSION_v1.0.html",
        },
    },
    "case-04": None,
    "case-05": None,
    "case-06": None,
}
NATIVE_NO_ARTIFACTS_STATUS = "NO_FORMER_GENERATED_ARTIFACTS"
NATIVE_NO_RECOVERY = {
    "case-04": "NOT_APPLICABLE: Case 04 was produced natively under the canonical source model; no generated release artifacts exist.",
    "case-05": "NOT_APPLICABLE: Case 05 was produced natively under the canonical source model; no generated release artifacts exist.",
    "case-06": "NOT_APPLICABLE: Case 06 was produced natively under the canonical source model; no generated release artifacts exist.",
}


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, check=True, text=True, capture_output=True
    )
    return [line for line in result.stdout.splitlines() if line and (ROOT / line).is_file()]


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)


def commit_exists(commit: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"], cwd=ROOT, capture_output=True
    ).returncode == 0


def verify_commit(label: str, commit: str, failures: list[str], totals: dict[str, int]) -> None:
    totals["commitReferencesChecked"] += 1
    if not isinstance(commit, str) or not commit_exists(commit):
        failures.append(f"{label}: declared commit does not exist: {commit!r}")


def verify_artifact(label: str, commit: str, artifact: dict, failures: list[str], totals: dict[str, int]) -> None:
    totals["artifactRecoveriesChecked"] += 1
    path = artifact.get("path") if isinstance(artifact, dict) else None
    expected = artifact.get("sha256") if isinstance(artifact, dict) else None
    if not path or not expected:
        failures.append(f"{label}: artifact path and SHA-256 are required")
        return
    result = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=ROOT, capture_output=True)
    if result.returncode != 0:
        failures.append(f"{label}: path does not exist at {commit}: {path}")
        return
    actual = hashlib.sha256(result.stdout).hexdigest()
    if actual != expected:
        failures.append(f"{label}: SHA-256 mismatch for {commit}:{path}; expected {expected}, got {actual}")
        return
    totals["artifactHashesVerified"] += 1


def main() -> int:
    failures: list[str] = []
    totals = {
        "commitReferencesChecked": 0,
        "artifactRecoveriesChecked": 0,
        "artifactHashesVerified": 0,
        "priorApprovedReleaseEntries": 0,
        "localUntrackedArtifactsExcluded": 0,
    }
    cases = sorted(path for path in CAMPAIGN.glob("case-*") if path.is_dir())
    if [path.name[:7] for path in cases] != ["case-01", "case-02", "case-03", "case-04", "case-05", "case-06"]:
        failures.append(f"expected exactly Cases 01–06; found {[path.name for path in cases]}")

    tracked = tracked_files()
    pdfs = [path for path in tracked if path.lower().endswith(".pdf")]
    if pdfs:
        failures.append(f"tracked PDFs are prohibited: {pdfs}")

    for case in cases:
        top_entries = {path.name for path in case.iterdir() if path.name != ".DS_Store"}
        allowed_top = {"README.md", "source", "history", "assets"}
        unexpected = sorted(top_entries - allowed_top)
        if unexpected:
            failures.append(f"{case.name}: unexpected top-level entries: {unexpected}")
        if not (case / "README.md").is_file():
            failures.append(f"{case.name}: README.md is required")
        for path in case.rglob("*"):
            if path.is_dir() and path.name in FORBIDDEN_DIRS:
                failures.append(f"{case.name}: forbidden directory: {path.relative_to(case)}")

        source = case / "source"
        source_files = {path.name for path in source.iterdir() if path.is_file() and path.name != ".DS_Store"} if source.is_dir() else set()
        missing = sorted(REQUIRED_SOURCE - source_files)
        if missing:
            failures.append(f"{case.name}: missing canonical source files: {missing}")
            continue
        nested_source_dirs = sorted(str(path.relative_to(case)) for path in source.iterdir() if path.is_dir())
        if nested_source_dirs:
            failures.append(f"{case.name}: nested source directories are not canonical: {nested_source_dirs}")

        package_path = source / "case-package.json"
        try:
            package = json.loads(package_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"{case.name}: invalid case-package.json: {error}")
            continue
        if package.get("supportedRoles") != ROLES:
            failures.append(f"{case.name}: supportedRoles must be exactly {ROLES}")
        if list(package.get("rolePageStructure", {})) != ROLES:
            failures.append(f"{case.name}: rolePageStructure must contain exactly the four roles")
        if list(package.get("outputs", {})) != ["complete", *ROLES]:
            failures.append(f"{case.name}: outputs must contain complete plus exactly the four roles")
        package_text = package_path.read_text(encoding="utf-8")
        if "GRAYSCALE_" in package_text.upper() or '"grayscale": {' in package_text:
            failures.append(f"{case.name}: presentation state is declared as an output/profile")
        forbidden_fields = {
            "historicalMaster", "successorMaster", "goldenMaster", "migrationSource",
            "preMaintenanceMasterSha256", "reconciliationRecord", "phase2Authorization",
        }
        if forbidden_fields.intersection(package):
            failures.append(f"{case.name}: migration-only package fields remain")

        references = set(strings(package))
        for optional in source_files - REQUIRED_SOURCE:
            relative = (source / optional).relative_to(ROOT).as_posix()
            if relative not in references:
                failures.append(f"{case.name}: unreferenced optional source file: {relative}")

        assets = case / "assets"
        if assets.exists():
            asset_files = [path for path in assets.rglob("*") if path.is_file()]
            if not asset_files:
                failures.append(f"{case.name}: empty assets directory is prohibited")
            for asset in asset_files:
                relative = asset.relative_to(ROOT).as_posix()
                if relative not in references:
                    failures.append(f"{case.name}: unreferenced case asset: {relative}")

        history = case / "history"
        records = sorted(history.glob("release-v*.json")) if history.is_dir() else []
        approval_records = sorted(history.glob("CASE*_OWNER_APPROVAL_v*.md")) if history.is_dir() else []
        extra_history = sorted(path.name for path in history.iterdir() if path.is_file() and path not in records + approval_records) if history.is_dir() else []
        if extra_history:
            failures.append(f"{case.name}: unexpected history files: {extra_history}")
        released = package.get("status") == "APPROVED_STABLE"
        if released:
            if len(records) != 1:
                failures.append(f"{case.name}: APPROVED_STABLE requires exactly one history/release-vX.json")
            if package.get("releaseHistory") not in {path.relative_to(ROOT).as_posix() for path in records}:
                failures.append(f"{case.name}: package releaseHistory does not name a retained record")
            expected_approval_record = {
                "case-04": "CASE04_OWNER_APPROVAL_v1.0.md",
                "case-05": "CASE05_OWNER_APPROVAL_v1.0.md",
                "case-06": "CASE06_OWNER_APPROVAL_v1.0.md",
            }.get(case.name[:7])
            if expected_approval_record and [path.name for path in approval_records] != [expected_approval_record]:
                failures.append(f"{case.name}: approved v1.0 requires {expected_approval_record}")
        else:
            if package.get("status") not in {"DRAFT", "VALIDATION_BUILD", "OWNER_GATE_OPEN"}:
                failures.append(f"{case.name}: unsupported unreleased lifecycle status: {package.get('status')}")
            if records or "releaseHistory" in package:
                failures.append(f"{case.name}: unreleased DRAFT must not contain or declare release history")
            approval = package.get("approval", {})
            if package.get("status") == "DRAFT" and (approval.get("status") != "OWNER_REVIEW_NOT_STARTED" or approval.get("printStatus") != "NOT_RUN"):
                failures.append(f"{case.name}: DRAFT must remain OWNER_REVIEW_NOT_STARTED with printStatus NOT_RUN")

        if released and len(records) == 1:
            try:
                release = json.loads(records[0].read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as error:
                failures.append(f"{case.name}: invalid release history: {error}")
                release = {}

            case_key = case.name[:7]
            for field, expected_commit in COMMIT_FIELDS[case_key].items():
                commit = release.get(field)
                if commit != expected_commit:
                    failures.append(f"{case.name}: {field} must be {expected_commit}; found {commit}")
                verify_commit(f"{case.name} {field}", commit, failures, totals)

            former = release.get("formerArtifacts", {})
            native_no_artifacts = former.get("status") == NATIVE_NO_ARTIFACTS_STATUS if isinstance(former, dict) else False
            recovery_commit = release.get("formerArtifactRecoveryCommit")
            verify_commit(f"{case.name} formerArtifactRecoveryCommit", recovery_commit, failures, totals)
            expected_recovery = NATIVE_NO_RECOVERY.get(case_key) if native_no_artifacts else f"git show {recovery_commit}:<former path> > <destination>"
            if release.get("recovery") != expected_recovery:
                failures.append(f"{case.name}: current recovery command does not name its recovery commit")

            if native_no_artifacts:
                if case_key not in NATIVE_NO_RECOVERY or set(former) != {"status", "reason"}:
                    failures.append(f"{case.name}: native no-artifact release marker is not valid for this case")
            else:
                former_roles = former.get("roles", {})
                if set(former_roles) != set(ROLES) or "grayscale" in former_roles:
                    failures.append(f"{case.name}: current historical role artifacts must contain only the four roles")
                verify_artifact(f"{case.name} current complete", recovery_commit, former.get("complete", {}), failures, totals)
                for role, artifact in former_roles.items():
                    verify_artifact(f"{case.name} current {role}", recovery_commit, artifact, failures, totals)

            for retired in release.get("retiredArtifacts", []):
                classification = retired.get("classification", "")
                path = retired.get("path", "")
                if "GRAYSCALE" in path.upper():
                    if not classification.startswith("RETIRED_"):
                        failures.append(f"{case.name}: historical Grayscale artifact is not clearly retired: {path}")
                    verify_artifact(f"{case.name} retired presentation snapshot", recovery_commit, retired, failures, totals)
                elif classification == "IGNORED_LOCAL_RELEASE_ARTIFACT_REMOVED":
                    totals["localUntrackedArtifactsExcluded"] += 1

            prior = release.get("priorApprovedReleases")
            expected_prior = EXPECTED_PRIOR[case_key]
            if expected_prior is None:
                if prior != []:
                    failures.append(f"{case.name}: current v1.0 must explicitly have no earlier approved release")
                prior = prior if isinstance(prior, list) else []
            else:
                if not isinstance(prior, list) or len(prior) != 1:
                    failures.append(f"{case.name}: exactly one prior approved release must be indexed")
                    prior = []
                if prior:
                    item = prior[0]
                    totals["priorApprovedReleaseEntries"] += 1
                    if item.get("version") != expected_prior["version"]:
                        failures.append(f"{case.name}: prior approved version must be {expected_prior['version']}")
                    if item.get("approvalCommit") != expected_prior["commit"] or item.get("recoveryCommit") != expected_prior["commit"]:
                        failures.append(f"{case.name}: prior approval and recovery commits are incorrect")
                    for field in ["approvalCommit", "recoveryCommit"]:
                        verify_commit(f"{case.name} prior {field}", item.get(field), failures, totals)
                    expected_command = f"git show {item.get('recoveryCommit')}:<former path> > <destination>"
                    if item.get("recoveryCommand") != expected_command:
                        failures.append(f"{case.name}: prior release recovery command is incorrect")
                    prior_artifacts = item.get("formerArtifacts", {})
                    prior_roles = prior_artifacts.get("roles", {})
                    if prior_artifacts.get("complete", {}).get("path") != expected_prior["complete"]:
                        failures.append(f"{case.name}: prior complete-master path is incorrect")
                    if {role: artifact.get("path") for role, artifact in prior_roles.items()} != expected_prior["roles"]:
                        failures.append(f"{case.name}: prior role HTML index is incomplete or incorrect")
                    if "grayscale" in prior_roles:
                        failures.append(f"{case.name}: prior approved roles must not model Grayscale")
                    if case_key == "case-01":
                        unavailable = item.get("roleHtmlAvailability", {})
                        if set(unavailable) != set(ROLES) or set(unavailable.values()) != {"NOT_CREATED_AT_APPROVAL_COMMIT"}:
                            failures.append(f"{case.name}: absence of v1.0 standalone role HTML is not explicit")
                    verify_artifact(f"{case.name} prior complete", item.get("recoveryCommit"), prior_artifacts.get("complete", {}), failures, totals)
                    for role, artifact in prior_roles.items():
                        verify_artifact(f"{case.name} prior {role}", item.get("recoveryCommit"), artifact, failures, totals)
                    for legacy in item.get("legacyArtifacts", []):
                        path = legacy.get("path", "")
                        if "GRAYSCALE" in path.upper() and not legacy.get("classification", "").startswith("RETIRED_"):
                            failures.append(f"{case.name}: prior Grayscale artifact is not clearly retired: {path}")
                        verify_artifact(f"{case.name} prior retired artifact", item.get("recoveryCommit"), legacy, failures, totals)

        case_prefix = case.relative_to(ROOT).as_posix() + "/"
        case_html = [path for path in tracked if path.startswith(case_prefix) and path.endswith(".html")]
        expected_html = f"{case_prefix}source/content.html"
        if case_html != [expected_html]:
            failures.append(f"{case.name}: stored generated/editable HTML found: {case_html}")

    payload = {
        "validator": "canonical-case-structure-v1",
        "status": "PASS" if not failures else "FAIL",
        "cases": len(cases),
        "recoveryValidation": totals,
        "failures": failures,
    }
    print(json.dumps(payload, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
