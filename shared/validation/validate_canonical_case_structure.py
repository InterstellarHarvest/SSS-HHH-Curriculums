#!/usr/bin/env python3
"""Fail unless every current case uses the lean canonical source/history layout.

Covers every registered case in every campaign. The roster is derived from
``shared/implementation/case-registry.v2.json`` and cross-checked against what is
on disk in both directions, so a case that is registered but missing, or present
but unregistered, is a failure rather than a silent omission. This validator was
Campaign 1 only until the Campaign 2 finalization pass; Campaign 2 structural
coverage existed solely because each ``validate_caseNN_campaign2.py`` re-implemented
it by hand, and a fourteenth case would have received none at all.

Cases are keyed by ``campaign-N/case-NN`` throughout. The bare ``case-NN`` key the
Campaign 1 version used collides the moment two campaigns each have a Case 01.

Campaign 1's historical exceptions are preserved verbatim: its exact release-commit
pins, its two pre-canonical prior-release indexes, its native no-artifact recovery
wording, and the Campaign 1 Case 01 ``roleHtmlAvailability`` assertion, which is
scoped to that one case and no other.

This validator owns *structure*. Blob-level source certification -- proving that a
release record's ``canonicalSourceApprovalCommit`` really contains the source it
certifies -- belongs to ``validate_release_integrity.py``, which does it for every
registered case rather than against a hand-copied table of expected pins.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "shared/implementation/case-registry.v2.json"

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import corrective_release_lifecycle  # noqa: E402

FORBIDDEN_DIRS = {
    "master", "published", "reports", "review", "validation-artifacts",
    "editor-package", "editor-phase2", "editor-v1.1", "editor",
}
REQUIRED_SOURCE = {"case-package.json", "content.html", "presentation.css", "task-registry.js"}
ROLES = ["student", "teacher", "answer", "accessible"]
COMMIT_FIELDS = {
    "campaign-1/case-01": {
        "originalReleaseApprovalCommit": "e524d333f28a1515571f038e3ed494d87aa812d3",
        "canonicalSourceApprovalCommit": "e347370ed55913f04b54b8e942f191808f8e4aa9",
    },
    "campaign-1/case-02": {
        "originalReleaseApprovalCommit": "e524d333f28a1515571f038e3ed494d87aa812d3",
        "canonicalSourceApprovalCommit": "e347370ed55913f04b54b8e942f191808f8e4aa9",
    },
    "campaign-1/case-03": {
        "originalReleaseApprovalCommit": "7b5b724b4941a7ad926fe1b0d644f6905ff55067",
        "canonicalSourceApprovalCommit": "7b5b724b4941a7ad926fe1b0d644f6905ff55067",
    },
    "campaign-1/case-04": {
        "originalReleaseApprovalCommit": "9d8c3dd9222f6b3a2954b8ba14eb1cee38eb69ba",
        "canonicalSourceApprovalCommit": "9d8c3dd9222f6b3a2954b8ba14eb1cee38eb69ba",
    },
    "campaign-1/case-05": {
        "originalReleaseApprovalCommit": "c73140841559b1ef56f5088e759e41a253856723",
        "canonicalSourceApprovalCommit": "c73140841559b1ef56f5088e759e41a253856723",
    },
    "campaign-1/case-06": {
        "originalReleaseApprovalCommit": "a1a7308cdb6803e7567dfec6cc7346bed03310c1",
        "canonicalSourceApprovalCommit": "a1a7308cdb6803e7567dfec6cc7346bed03310c1",
    },
    "campaign-1/case-07": {
        "originalReleaseApprovalCommit": "f08066c15c161c5961cc88adad86282329cd7609",
        "canonicalSourceApprovalCommit": "f08066c15c161c5961cc88adad86282329cd7609",
    },
}
EXPECTED_PRIOR = {
    "campaign-1/case-01": {
        "version": "1.0",
        "commit": "7f3504aa33aaefbf57583ceb2be1ab2af88d10b0",
        "complete": "sss/campaign-1/case-01-iss-greenhouse/master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html",
        "roles": {},
    },
    "campaign-1/case-02": None,
    "campaign-1/case-03": {
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
    "campaign-1/case-04": None,
    "campaign-1/case-05": None,
    "campaign-1/case-06": None,
    "campaign-1/case-07": None,
}
NATIVE_NO_ARTIFACTS_STATUS = "NO_FORMER_GENERATED_ARTIFACTS"
# Campaign 1 Cases 04-07 each spell their own no-artifact recovery statement; those
# are frozen wording. Every later native release uses this one.
NATIVE_NO_RECOVERY_DEFAULT = ("No artifact recovery applies. The canonical source at the "
                              "approval commit is the whole release.")
NATIVE_NO_RECOVERY = {
    "campaign-1/case-04": "NOT_APPLICABLE: Case 04 was produced natively under the canonical source model; no generated release artifacts exist.",
    "campaign-1/case-05": "NOT_APPLICABLE: Case 05 was produced natively under the canonical source model; no generated release artifacts exist.",
    "campaign-1/case-06": "NOT_APPLICABLE: Case 06 was produced natively under the canonical source model; no generated release artifacts exist.",
    "campaign-1/case-07": "NOT_APPLICABLE: Case 07 was produced natively under the canonical source model; no generated release artifacts exist.",
}


HISTORICAL_INLINE_OWNER_APPROVAL = {
    # The three oldest Campaign 1 releases predate the standalone owner-approval
    # record. Their approval is captured inside the release record itself. Every
    # later release carries a CASE##_OWNER_APPROVAL_v#.#.md for its own version.
    "campaign-1/case-01",
    "campaign-1/case-02",
    "campaign-1/case-03",
}

# The frozen Campaign 1 tables above describe these historical release versions. The
# final-system release superseded them, so the frozen expectations transfer to the
# retained record of the frozen version — the protection is unchanged, it simply
# follows the record it has always described — while the current corrective release
# is validated by the generic corrective branch plus blob-level certification in
# validate_release_integrity.py, exactly like every other corrective release.
FROZEN_PIN_VERSIONS = {
    "campaign-1/case-01": "1.1",
    "campaign-1/case-02": "1.0",
    "campaign-1/case-03": "1.1",
    "campaign-1/case-04": "1.0",
    "campaign-1/case-05": "1.0",
    "campaign-1/case-06": "1.0",
    "campaign-1/case-07": "1.0",
}


def enforce_expected_prior(label: str, case_key: str, release: dict, failures: list[str], totals: dict) -> None:
    """Assert the frozen Campaign 1 prior-release table against the given record.

    Applied to whichever record carries the frozen version: the current record while
    that version is current, the retained record after a corrective release
    supersedes it. Verbatim relocation of the historical table checks.
    """
    prior = release.get("priorApprovedReleases")
    expected_prior = EXPECTED_PRIOR[case_key]
    if expected_prior is None:
        if prior != []:
            failures.append(f"{label}: current v1.0 must explicitly have no earlier approved release")
        return
    if not isinstance(prior, list) or len(prior) != 1:
        failures.append(f"{label}: exactly one prior approved release must be indexed")
        return
    item = prior[0]
    totals["priorApprovedReleaseEntries"] += 1
    if item.get("version") != expected_prior["version"]:
        failures.append(f"{label}: prior approved version must be {expected_prior['version']}")
    if item.get("approvalCommit") != expected_prior["commit"] or item.get("recoveryCommit") != expected_prior["commit"]:
        failures.append(f"{label}: prior approval and recovery commits are incorrect")
    for field in ["approvalCommit", "recoveryCommit"]:
        verify_commit(f"{label} prior {field}", item.get(field), failures, totals)
    expected_command = f"git show {item.get('recoveryCommit')}:<former path> > <destination>"
    if item.get("recoveryCommand") != expected_command:
        failures.append(f"{label}: prior release recovery command is incorrect")
    prior_artifacts = item.get("formerArtifacts", {})
    prior_roles = prior_artifacts.get("roles", {})
    if prior_artifacts.get("complete", {}).get("path") != expected_prior["complete"]:
        failures.append(f"{label}: prior complete-master path is incorrect")
    if {role: artifact.get("path") for role, artifact in prior_roles.items()} != expected_prior["roles"]:
        failures.append(f"{label}: prior role HTML index is incomplete or incorrect")
    if "grayscale" in prior_roles:
        failures.append(f"{label}: prior approved roles must not model Grayscale")
    if case_key == "campaign-1/case-01":
        unavailable = item.get("roleHtmlAvailability", {})
        if set(unavailable) != set(ROLES) or set(unavailable.values()) != {"NOT_CREATED_AT_APPROVAL_COMMIT"}:
            failures.append(f"{label}: absence of v1.0 standalone role HTML is not explicit")
    verify_artifact(f"{label} prior complete", item.get("recoveryCommit"), prior_artifacts.get("complete", {}), failures, totals)
    for role, artifact in prior_roles.items():
        verify_artifact(f"{label} prior {role}", item.get("recoveryCommit"), artifact, failures, totals)
    for legacy in item.get("legacyArtifacts", []):
        path = legacy.get("path", "")
        if "GRAYSCALE" in path.upper() and not legacy.get("classification", "").startswith("RETIRED_"):
            failures.append(f"{label}: prior Grayscale artifact is not clearly retired: {path}")
        verify_artifact(f"{label} prior retired artifact", item.get("recoveryCommit"), legacy, failures, totals)


def registered_roster() -> tuple[list[tuple[str, str, Path]], list[str]]:
    """Return (campaign_id, case_id, case_root) per registered case, plus failures.

    Cross-checked against the filesystem in both directions so neither an
    unregistered case directory nor a registered case without one can hide.
    """
    failures: list[str] = []
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    roster: list[tuple[str, str, Path]] = []
    registered_campaigns: dict[str, set[str]] = {}
    for curriculum in registry["curricula"]:
        for campaign in curriculum["campaigns"]:
            campaign_id = campaign["id"]
            campaign_root = ROOT / "sss" / campaign_id
            if not campaign_root.is_dir():
                failures.append(f"{campaign_id}: registered campaign has no directory")
                continue
            for case in campaign["cases"]:
                package = ROOT / case["editorPackage"]
                case_root = package.parent.parent
                if not case_root.is_dir():
                    failures.append(f"{case['id']}: registered case directory is missing: {case_root}")
                    continue
                if case_root.parent != campaign_root:
                    failures.append(f"{case['id']}: package lives outside its registered campaign: {case_root}")
                    continue
                roster.append((campaign_id, case["id"], case_root))
                registered_campaigns.setdefault(campaign_id, set()).add(case_root.name)

    for campaign_root in sorted((ROOT / "sss").glob("campaign-*")):
        if not campaign_root.is_dir():
            continue
        on_disk = {path.name for path in campaign_root.glob("case-*") if path.is_dir()}
        registered = registered_campaigns.get(campaign_root.name, set())
        unregistered = sorted(on_disk - registered)
        if unregistered:
            failures.append(f"{campaign_root.name}: case directories that no registry entry names: {unregistered}")
    return roster, failures


def case_key_of(campaign_id: str, case_root: Path) -> str:
    """Collision-free key. Bare ``case-NN`` aliases Campaign 1 onto Campaign 2."""
    return f"{campaign_id}/{case_root.name[:7]}"


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
    roster, roster_failures = registered_roster()
    failures.extend(roster_failures)
    campaigns = sorted({campaign_id for campaign_id, _, _ in roster})

    tracked = tracked_files()
    pdfs = [path for path in tracked if path.lower().endswith(".pdf")]
    if pdfs:
        failures.append(f"tracked PDFs are prohibited: {pdfs}")

    for campaign_id, case_id, case in roster:
        case_key = case_key_of(campaign_id, case)
        # Every message names the campaign, because two campaigns now have a case-01.
        label = case_key
        top_entries = {path.name for path in case.iterdir() if path.name != ".DS_Store"}
        allowed_top = {"README.md", "source", "history", "assets"}
        unexpected = sorted(top_entries - allowed_top)
        if unexpected:
            failures.append(f"{label}: unexpected top-level entries: {unexpected}")
        if not (case / "README.md").is_file():
            failures.append(f"{label}: README.md is required")
        for path in case.rglob("*"):
            if path.is_dir() and path.name in FORBIDDEN_DIRS:
                failures.append(f"{label}: forbidden directory: {path.relative_to(case)}")

        source = case / "source"
        source_files = {path.name for path in source.iterdir() if path.is_file() and path.name != ".DS_Store"} if source.is_dir() else set()
        missing = sorted(REQUIRED_SOURCE - source_files)
        if missing:
            failures.append(f"{label}: missing canonical source files: {missing}")
            continue
        nested_source_dirs = sorted(str(path.relative_to(case)) for path in source.iterdir() if path.is_dir())
        if nested_source_dirs:
            failures.append(f"{label}: nested source directories are not canonical: {nested_source_dirs}")

        package_path = source / "case-package.json"
        try:
            package = json.loads(package_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"{label}: invalid case-package.json: {error}")
            continue
        if package.get("supportedRoles") != ROLES:
            failures.append(f"{label}: supportedRoles must be exactly {ROLES}")
        if list(package.get("rolePageStructure", {})) != ROLES:
            failures.append(f"{label}: rolePageStructure must contain exactly the four roles")
        if list(package.get("outputs", {})) != ["complete", *ROLES]:
            failures.append(f"{label}: outputs must contain complete plus exactly the four roles")
        package_text = package_path.read_text(encoding="utf-8")
        if "GRAYSCALE_" in package_text.upper() or '"grayscale": {' in package_text:
            failures.append(f"{label}: presentation state is declared as an output/profile")
        forbidden_fields = {
            "historicalMaster", "successorMaster", "goldenMaster", "migrationSource",
            "preMaintenanceMasterSha256", "reconciliationRecord", "phase2Authorization",
        }
        if forbidden_fields.intersection(package):
            failures.append(f"{label}: migration-only package fields remain")

        references = set(strings(package))
        for optional in source_files - REQUIRED_SOURCE:
            relative = (source / optional).relative_to(ROOT).as_posix()
            if relative not in references:
                failures.append(f"{label}: unreferenced optional source file: {relative}")

        assets = case / "assets"
        if assets.exists():
            asset_files = [path for path in assets.rglob("*") if path.is_file()]
            if not asset_files:
                failures.append(f"{label}: empty assets directory is prohibited")
            for asset in asset_files:
                relative = asset.relative_to(ROOT).as_posix()
                if relative not in references:
                    failures.append(f"{label}: unreferenced case asset: {relative}")

        history = case / "history"
        records = sorted(history.glob("release-v*.json")) if history.is_dir() else []
        approval_records = sorted(history.glob("CASE*_OWNER_APPROVAL_v*.md")) if history.is_dir() else []
        extra_history = sorted(path.name for path in history.iterdir() if path.is_file() and path not in records + approval_records) if history.is_dir() else []
        if extra_history:
            failures.append(f"{label}: unexpected history files: {extra_history}")
        released = package.get("status") == "APPROVED_STABLE"
        current_record = None
        if released:
            version = package.get("version")
            # A corrective release legitimately retains its superseded records, so the
            # rule is one record per version with none above the package's own, not one
            # record per case. corrective_release_lifecycle states that precisely.
            lifecycle_findings = corrective_release_lifecycle.history_findings(case, case_id, package)
            for finding in lifecycle_findings:
                failures.append(f"{label}: {finding}")
            expected_record = history / f"release-v{version}.json"
            if expected_record not in records:
                failures.append(f"{label}: APPROVED_STABLE v{version} requires history/{expected_record.name}")
            elif package.get("releaseHistory") != expected_record.relative_to(ROOT).as_posix():
                failures.append(f"{label}: package releaseHistory does not name its own version's record")
            else:
                current_record = expected_record
            if case_key not in HISTORICAL_INLINE_OWNER_APPROVAL:
                expected_approval = f"CASE{case.name[5:7]}_OWNER_APPROVAL_v{version}.md"
                if expected_approval not in {path.name for path in approval_records}:
                    failures.append(f"{label}: approved v{version} requires history/{expected_approval}")
            # Every retained record must be accompanied by its owner-approval record.
            for record in records:
                retained_version = record.name[len("release-v"):-len(".json")]
                if case_key in HISTORICAL_INLINE_OWNER_APPROVAL:
                    continue
                companion = f"CASE{case.name[5:7]}_OWNER_APPROVAL_v{retained_version}.md"
                if companion not in {path.name for path in approval_records}:
                    failures.append(f"{label}: retained v{retained_version} release record has no history/{companion}")
        else:
            if package.get("status") not in {"DRAFT", "VALIDATION_BUILD", "OWNER_GATE_OPEN"}:
                failures.append(f"{label}: unsupported unreleased lifecycle status: {package.get('status')}")
            if records or "releaseHistory" in package:
                failures.append(f"{label}: unreleased package must not contain or declare release history")
            approval = package.get("approval", {})
            if package.get("status") == "DRAFT" and (approval.get("status") != "OWNER_REVIEW_NOT_STARTED" or approval.get("printStatus") != "NOT_RUN"):
                failures.append(f"{label}: DRAFT must remain OWNER_REVIEW_NOT_STARTED with printStatus NOT_RUN")

        if released and current_record is not None:
            try:
                release = json.loads(current_record.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as error:
                failures.append(f"{label}: invalid release history: {error}")
                release = {}

            # Campaign 1's pins are frozen historical expectations and stay asserted
            # literally — against the record of the version they were frozen for. While
            # that version is the current release they bind the current record; once a
            # later corrective release supersedes it they bind the retained record of
            # the frozen version, which must remain on disk. Later campaigns declare
            # their pins and have them certified at the blob level by
            # validate_release_integrity.py, which cannot be satisfied by copying a SHA
            # into a table.
            is_frozen_current = release.get("curriculumVersion") == FROZEN_PIN_VERSIONS.get(case_key)
            if is_frozen_current:
                for field, expected_commit in COMMIT_FIELDS.get(case_key, {}).items():
                    commit = release.get(field)
                    if commit != expected_commit:
                        failures.append(f"{label}: {field} must be {expected_commit}; found {commit}")
            elif case_key in FROZEN_PIN_VERSIONS:
                frozen_version = FROZEN_PIN_VERSIONS[case_key]
                frozen_record_path = history / f"release-v{frozen_version}.json"
                if frozen_record_path not in records:
                    failures.append(f"{label}: frozen v{frozen_version} release record is no longer retained")
                else:
                    try:
                        frozen_release = json.loads(frozen_record_path.read_text(encoding="utf-8"))
                    except (OSError, json.JSONDecodeError) as error:
                        failures.append(f"{label}: retained frozen release record is unreadable: {error}")
                        frozen_release = {}
                    for field, expected_commit in COMMIT_FIELDS.get(case_key, {}).items():
                        commit = frozen_release.get(field)
                        if commit != expected_commit:
                            failures.append(f"{label}: retained v{frozen_version} {field} must be {expected_commit}; found {commit}")
                    frozen_former = frozen_release.get("formerArtifacts", {})
                    frozen_native = frozen_former.get("status") == NATIVE_NO_ARTIFACTS_STATUS if isinstance(frozen_former, dict) else False
                    if frozen_native:
                        frozen_expected_recovery = NATIVE_NO_RECOVERY.get(case_key, NATIVE_NO_RECOVERY_DEFAULT)
                        if frozen_release.get("recovery") != frozen_expected_recovery:
                            failures.append(f"{label}: retained v{frozen_version} recovery statement lost its frozen wording")
                    enforce_expected_prior(f"{label} retained v{frozen_version}", case_key, frozen_release, failures, totals)
            for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit"):
                verify_commit(f"{label} {field}", release.get(field), failures, totals)

            former = release.get("formerArtifacts", {})
            native_no_artifacts = former.get("status") == NATIVE_NO_ARTIFACTS_STATUS if isinstance(former, dict) else False
            recovery_commit = release.get("formerArtifactRecoveryCommit")
            verify_commit(f"{label} formerArtifactRecoveryCommit", recovery_commit, failures, totals)
            if native_no_artifacts:
                expected_recovery = NATIVE_NO_RECOVERY.get(case_key, NATIVE_NO_RECOVERY_DEFAULT) if is_frozen_current else NATIVE_NO_RECOVERY_DEFAULT
            else:
                expected_recovery = f"git show {recovery_commit}:<former path> > <destination>"
            if release.get("recovery") != expected_recovery:
                failures.append(f"{label}: current recovery command does not name its recovery commit")

            if native_no_artifacts:
                if set(former) != {"status", "reason"}:
                    failures.append(f"{label}: native no-artifact release marker is not valid for this case")
            else:
                former_roles = former.get("roles", {})
                if set(former_roles) != set(ROLES) or "grayscale" in former_roles:
                    failures.append(f"{label}: current historical role artifacts must contain only the four roles")
                verify_artifact(f"{label} current complete", recovery_commit, former.get("complete", {}), failures, totals)
                for role, artifact in former_roles.items():
                    verify_artifact(f"{label} current {role}", recovery_commit, artifact, failures, totals)

            for retired in release.get("retiredArtifacts", []):
                classification = retired.get("classification", "")
                path = retired.get("path", "")
                if "GRAYSCALE" in path.upper():
                    if not classification.startswith("RETIRED_"):
                        failures.append(f"{label}: historical Grayscale artifact is not clearly retired: {path}")
                    verify_artifact(f"{label} retired presentation snapshot", recovery_commit, retired, failures, totals)
                elif classification == "IGNORED_LOCAL_RELEASE_ARTIFACT_REMOVED":
                    totals["localUntrackedArtifactsExcluded"] += 1

            prior = release.get("priorApprovedReleases")
            if case_key not in EXPECTED_PRIOR or not is_frozen_current:
                # Later campaigns, and every corrective release that supersedes a frozen
                # Campaign 1 version: the prior index is validated against the records it
                # indexes rather than against a frozen table. Exactness of the indexed
                # hashes, baselines and immutability is validate_release_integrity.py's.
                corrective_of = release.get("correctiveOf")
                if corrective_of is None:
                    if prior:
                        failures.append(f"{label}: a first release must index no earlier approved release")
                elif not isinstance(prior, list) or not prior:
                    failures.append(f"{label}: a corrective release must index its prior approved release(s)")
                else:
                    retained_versions = {record.name[len("release-v"):-len(".json")] for record in records}
                    for item in prior:
                        totals["priorApprovedReleaseEntries"] += 1
                        item_version = item.get("version")
                        if item_version not in retained_versions:
                            failures.append(f"{label}: indexed prior release v{item_version} is not retained in history/")
                        if item.get("status") != "APPROVED_STABLE":
                            failures.append(f"{label}: indexed prior release v{item_version} is not an approved release")
                        for field in ("approvalCommit", "recoveryCommit", "canonicalSourceApprovalCommit"):
                            verify_commit(f"{label} prior v{item_version} {field}", item.get(field), failures, totals)
                        expected_command_prefix = f"git show {item.get('recoveryCommit')}:"
                        if not str(item.get("recoveryCommand", "")).startswith(expected_command_prefix):
                            failures.append(f"{label}: prior v{item_version} recovery command does not name its recovery commit")
                        prior_artifacts = item.get("formerArtifacts", {})
                        if prior_artifacts.get("status") == NATIVE_NO_ARTIFACTS_STATUS:
                            if set(prior_artifacts) != {"status", "reason"}:
                                failures.append(f"{label}: prior v{item_version} no-artifact marker is not valid")
                        elif "grayscale" in prior_artifacts.get("roles", {}):
                            failures.append(f"{label}: prior approved roles must not model Grayscale")
                    if corrective_of not in {item.get("version") for item in prior}:
                        failures.append(f"{label}: the corrected version v{corrective_of} is not indexed as a prior release")
                prior = []
            else:
                enforce_expected_prior(label, case_key, release, failures, totals)
                prior = []

        case_prefix = case.relative_to(ROOT).as_posix() + "/"
        case_html = [path for path in tracked if path.startswith(case_prefix) and path.endswith(".html")]
        expected_html = f"{case_prefix}source/content.html"
        if case_html != [expected_html]:
            failures.append(f"{label}: stored generated/editable HTML found: {case_html}")

    payload = {
        "validator": "canonical-case-structure-v1",
        "status": "PASS" if not failures else "FAIL",
        "campaigns": campaigns,
        "cases": len(roster),
        "recoveryValidation": totals,
        "failures": failures,
    }
    print(json.dumps(payload, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
