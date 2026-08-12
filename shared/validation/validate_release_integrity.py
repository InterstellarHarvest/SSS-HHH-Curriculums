#!/usr/bin/env python3
"""Validate that every approved release certifies source that really exists.

Every other validator in this repository compares a release record to the working
tree: the record's ``sourceHashes`` against the files on disk, its page counts
against the package, its baselines against the rendered markup. None of them ever
asked the one question a release record exists to answer -- *does the commit this
record pins actually contain the source it certifies?*

That gap shipped four false pins across Campaign 2 (Cases 01, 02, 04 and 05 at
v1.0, and Case 02 again at v1.1). The failure mode is always the same: the last
candidate commit is pinned, and the lifecycle promotion that stamps the task
registry lands in the release commit *after* it, so the pinned commit holds a
registry the record does not describe. Record and package agree, so every
record-to-package validator passes, and the pin silently certifies nothing.

This module closes that class of defect once, for the whole repository, by
hashing the four source blobs *at the pinned commit* and comparing them to the
hashes the record certifies. It also confirms the surrounding release contract:
lifecycle, owner approval, print status, complete current source hashes, valid
frozen baselines, and -- for a corrective release -- prior records that are still
byte-identical to the day they were written.

The case roster is derived from ``shared/implementation/case-registry.v2.json``,
so a newly registered case is covered the moment it is registered.

Deliberately *not* required: that every frozen DOM baseline of a corrective
release differs from the prior release's. A correction that leaves one role's
markup untouched is legitimate -- Campaign 2 Case 05 v1.1 corrected the Teacher
Guide and Answer Key without touching the Student edition, and its Student
baseline is identical to v1.0 by design. What a corrective release must change is
*source*, and that is what this module enforces.

Two record formats
------------------
Campaign 1 was released before this contract existed. Its records predate the
canonical-case-structure migration: they carry no ``frozenNonAccessibleDomBaselines``,
omit ``layoutOverrides`` from ``sourceHashes``, and -- for Cases 01-03 -- certify
source files at ``master/`` and ``published/`` paths the migration retired, so
their hashes and pins describe a tree this repository no longer has. Those are
frozen historical records; rewriting them would destroy the evidence of what was
actually approved.

So a record that declares ``frozenNonAccessibleDomBaselines`` is *contract-format*
and receives the full certification above. One that does not is *legacy-format*
and receives only the checks that are true of it: lifecycle, identity, owner and
print approval, fixed-role page counts, well-formed digests, and a pin that
resolves to a real commit. The exemption is not a list of grandfathered cases --
it is asserted to be confined to Campaign 1. Every case in any later campaign must
carry a contract-format current release, so this exemption can only shrink, and
it disappears the day Campaign 1 is reissued.

Usage:
    python3 shared/validation/validate_release_integrity.py [CASE-ID ...]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "shared/implementation/case-registry.v2.json"

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import corrective_release_lifecycle  # noqa: E402

SOURCE_KEYS = ("content", "presentation", "taskRegistry", "layoutOverrides")
ROLES = ("student", "teacher", "answer", "accessible")
# Accessible page count is content-driven and may drift from what a record froze;
# the three fixed roles are exact. This mirrors validate_static.py.
FIXED_ROLES = ("student", "teacher", "answer")
BASELINE_ROLES = ("student", "teacher", "answer")
# The one campaign released before the current release contract existed. The
# exemption is curriculum-qualified: HHH also numbers its campaigns from 1, and an
# HHH campaign-1 release must never inherit SSS Campaign 1's legacy allowance.
LEGACY_CONTRACT_SCOPE = ("SSS", "campaign-1")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
VERSION_RE = re.compile(r"^(\d+)\.(\d+)$")
CASE_ID_RE = re.compile(r"^[A-Z]{3}-C\d-CASE(\d{2})$")
# Generated artifacts are recoverable from Git and are never committed. Anything
# matching these is a build output that escaped .gitignore.
GENERATED_ARTIFACT_RE = re.compile(
    r"(\.(pdf|pyc|pyo|png|jpg|jpeg)$)|(^|/)__pycache__(/|$)|_CUSTOM\.html$|GRAYSCALE",
    re.IGNORECASE,
)


class Results:
    def __init__(self) -> None:
        self.passed = 0
        self.failures: list[str] = []

    def check(self, label: str, condition: bool, detail: object = "") -> bool:
        if condition:
            self.passed += 1
        else:
            self.failures.append(f"{label}{f' -- {detail}' if detail else ''}")
        return bool(condition)

    @property
    def total(self) -> int:
        return self.passed + len(self.failures)


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)


def blob_digest_at(commit: str, repo_path: str) -> str | None:
    """SHA-256 of a file's content at a commit, or None if it is not there."""
    result = git("show", f"{commit}:{repo_path}")
    if result.returncode != 0:
        return None
    return hashlib.sha256(result.stdout).hexdigest()


def commit_exists(commit: str) -> bool:
    return git("cat-file", "-e", f"{commit}^{{commit}}").returncode == 0


def commits_touching(repo_path: str) -> list[str]:
    result = git("log", "--format=%H", "--", repo_path)
    return result.stdout.decode().split() if result.returncode == 0 else []


def safe_repo_path(raw: object, *, suffix: str) -> Path:
    if not isinstance(raw, str) or not raw or raw.startswith(("/", "~")) or "\\" in raw:
        raise ValueError(f"unsafe repository path: {raw!r}")
    candidate = (ROOT / raw).resolve()
    candidate.relative_to(ROOT.resolve())
    if not candidate.as_posix().endswith(suffix):
        raise ValueError(f"unexpected source target: {raw!r}")
    return candidate


def registered_cases() -> list[tuple[str, str, dict]]:
    """Every operational registered case, with its curriculum and campaign.

    Registry entries without an ``editorPackage`` are planned reservations: they
    have no canonical package, so there is no release to certify. They are skipped
    here and validated by validate_hhh_activation.py instead.
    """
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return [
        (curriculum["id"], campaign["id"], case)
        for curriculum in registry["curricula"]
        for campaign in curriculum["campaigns"]
        for case in campaign["cases"]
        if "editorPackage" in case
    ]


def load_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def source_repo_paths(package: dict) -> dict[str, str]:
    """The four package-pinned source files, as repository-relative paths."""
    return {
        "content": package["content"]["source"],
        "presentation": package["presentation"]["source"],
        "taskRegistry": package["taskRegistry"]["source"],
        "layoutOverrides": package["layoutOverrides"]["source"],
    }


def check_prior_release(results: Results, case_id: str, case_root: Path,
                        entry: dict, current_hashes: dict, current_pin: str | None = None) -> None:
    """A retained prior release must still be exactly what it was on its day."""
    version = entry.get("version")
    label = f"{case_id} prior release v{version}"
    if not (isinstance(version, str) and VERSION_RE.match(version)):
        results.check(f"{label} declares a two-component version", False, version)
        return
    record_path = case_root / "history" / f"release-v{version}.json"
    if not results.check(f"{label} retains its release record", record_path.is_file(),
                         record_path.relative_to(ROOT)):
        return
    retained = load_json(record_path)
    if not results.check(f"{label} retained record is readable canonical JSON", retained is not None):
        return

    results.check(f"{label} retained record identifies the same case and version",
                  retained.get("caseId") == case_id and retained.get("curriculumVersion") == version,
                  (retained.get("caseId"), retained.get("curriculumVersion")))
    results.check(f"{label} retained record is still an approved release",
                  retained.get("status") == entry.get("status") == "APPROVED_STABLE")

    # The inline index inside the current record must not drift from the record
    # it indexes. Either one being edited to describe the other is the failure.
    for field in ("approvalDate", "sourceHashes", "frozenNonAccessibleDomBaselines",
                  "rolePageCounts", "canonicalSourceApprovalCommit"):
        if field in entry and field in retained:
            results.check(f"{label} inline {field} matches the retained record verbatim",
                          entry[field] == retained[field],
                          json.dumps({"inline": entry[field], "retained": retained[field]}))

    # Unchanged means unchanged. A record written before the two-commit release
    # pattern was introduced in exactly one commit; a record released under that
    # pattern was legitimately touched twice — its release commit and the narrow
    # follow-up that pinned canonicalSourceApprovalCommit. Either way, every commit
    # that ever touched the retained record must predate the current release's
    # certified source commit; a touch after that pin is tampering.
    touching = commits_touching(str(record_path.relative_to(ROOT)))
    if isinstance(current_pin, str) and COMMIT_RE.match(current_pin) and commit_exists(current_pin):
        untampered = bool(touching) and all(
            git("merge-base", "--is-ancestor", touch, current_pin).returncode == 0
            for touch in touching
        )
        results.check(f"{label} retained record is unmodified since the current release certified its source",
                      untampered, f"{len(touching)} commits: {[c[:8] for c in touching]}")
    else:
        results.check(f"{label} retained record is unmodified since the commit that wrote it",
                      len(touching) <= 2, f"{len(touching)} commits: {[c[:8] for c in touching]}")

    if not is_inline_approval_case(case_root):
        approval = case_root / "history" / owner_approval_name(case_id, version)
        results.check(f"{label} retains its owner-approval record", approval.is_file() and approval.stat().st_size > 0,
                      approval.name)

    prior_hashes = entry.get("sourceHashes")
    if isinstance(prior_hashes, dict) and isinstance(current_hashes, dict):
        shared_keys = set(prior_hashes) & set(current_hashes)
        results.check(f"{label} is genuinely superseded -- the current release changed source",
                      any(prior_hashes[key] != current_hashes[key] for key in shared_keys),
                      "current sourceHashes are identical to the prior release")


# The three oldest Campaign 1 releases predate the standalone owner-approval record;
# their approval is captured inside the release record itself. Mirrors the identical
# exemption in validate_canonical_case_structure.py.
HISTORICAL_INLINE_OWNER_APPROVAL = {
    "campaign-1/case-01-iss-greenhouse",
    "campaign-1/case-02-lunar-greenhouse",
    "campaign-1/case-03-mars-habitat",
}


def is_inline_approval_case(case_root: Path) -> bool:
    return f"{case_root.parent.name}/{case_root.name}" in HISTORICAL_INLINE_OWNER_APPROVAL


def owner_approval_name(case_id: str, version: str) -> str:
    match = CASE_ID_RE.match(case_id)
    number = match.group(1) if match else "00"
    return f"CASE{number}_OWNER_APPROVAL_v{version}.md"


def validate_case(results: Results, curriculum_id: str, campaign_id: str, entry: dict) -> str | None:
    """Validate one registered case. Returns its record format, or None if unreleased."""
    case_id = entry["id"]
    package_path = safe_repo_path(entry.get("editorPackage"), suffix="/source/case-package.json")
    package = load_json(package_path)
    if not results.check(f"{case_id} package is readable canonical JSON", package is not None,
                         package_path.relative_to(ROOT)):
        return None
    case_root = package_path.parent.parent
    version = package.get("version")

    findings = corrective_release_lifecycle.history_findings(case_root, case_id, package)
    results.check(f"{case_id} history/ satisfies the corrective-release lifecycle rules",
                  not findings, "; ".join(findings))

    if package.get("status") != "APPROVED_STABLE" or entry.get("status") != "APPROVED_STABLE":
        # An unreleased package has no release to certify. The lifecycle module
        # above already governs what it may retain.
        results.check(f"{case_id} unreleased package declares no release pointer",
                      "releaseHistory" not in package and "historyRecord" not in entry)
        return None

    record_path = case_root / "history" / f"release-v{version}.json"
    results.check(f"{case_id} registry, package and filename agree on the current release record",
                  entry.get("historyRecord") == package.get("releaseHistory")
                  == str(record_path.relative_to(ROOT)),
                  json.dumps({"registry": entry.get("historyRecord"),
                              "package": package.get("releaseHistory")}))
    if not results.check(f"{case_id} current release record exists", record_path.is_file(),
                         record_path.relative_to(ROOT)):
        return None
    record = load_json(record_path)
    if not results.check(f"{case_id} current release record is readable canonical JSON",
                         record is not None):
        return None

    # A record that freezes DOM baselines was written under the current release
    # contract and is certified in full. See the module docstring for the rest.
    contract_format = isinstance(record.get("frozenNonAccessibleDomBaselines"), dict)
    results.check(
        f"{case_id} current release is contract-format, or belongs to the one campaign that predates the contract",
        contract_format or (curriculum_id, campaign_id) == LEGACY_CONTRACT_SCOPE,
        f"{curriculum_id}/{campaign_id} release record declares no frozenNonAccessibleDomBaselines")

    results.check(f"{case_id} release record identity matches the package",
                  record.get("caseId") == case_id == package.get("id")
                  and record.get("curriculumVersion") == version
                  and record.get("status") == "APPROVED_STABLE",
                  json.dumps({"caseId": record.get("caseId"),
                              "curriculumVersion": record.get("curriculumVersion"),
                              "status": record.get("status")}))

    approval = package.get("approval") or {}
    results.check(f"{case_id} owner approval agrees across package, registry and release record",
                  approval.get("status") == (entry.get("approval") or {}).get("status") == "APPROVED"
                  and approval.get("owner") == record.get("owner")
                  and approval.get("date") == record.get("approvalDate"),
                  json.dumps({"package": approval, "record": {"owner": record.get("owner"),
                                                              "date": record.get("approvalDate")}}))
    results.check(f"{case_id} physical print approval is recorded as PASS",
                  approval.get("printStatus") == (entry.get("approval") or {}).get("printStatus") == "PASS"
                  and str(record.get("acceptedPrintStatus", "")).startswith("PASS"),
                  record.get("acceptedPrintStatus"))
    results.check(f"{case_id} accepted validation status is PASS",
                  (record.get("acceptedValidation") or {}).get("status") == "PASS")

    # A standalone owner-approval record is part of the current contract. The three
    # oldest Campaign 1 releases capture owner approval inline instead, which the
    # owner/date/print checks above verify for all thirteen either way.
    if contract_format:
        approval_record = case_root / "history" / owner_approval_name(case_id, str(version))
        results.check(f"{case_id} current release carries its owner-approval record",
                      approval_record.is_file() and approval_record.stat().st_size > 0,
                      approval_record.name)

    # --- source certification -------------------------------------------------
    paths = source_repo_paths(package)
    certified = record.get("sourceHashes")
    package_hashes = package.get("sourceHashes")
    if not results.check(f"{case_id} release record certifies source hashes", isinstance(certified, dict)):
        return None
    results.check(f"{case_id} every certified hash is a well-formed SHA-256 digest",
                  bool(certified) and all(SHA256_RE.match(str(value)) for value in certified.values()),
                  sorted(certified))

    commit = record.get("canonicalSourceApprovalCommit")
    pin_resolves = (
        results.check(f"{case_id} canonicalSourceApprovalCommit is a full commit SHA",
                      isinstance(commit, str) and bool(COMMIT_RE.match(commit)), commit)
        and results.check(f"{case_id} canonicalSourceApprovalCommit exists in this repository",
                          commit_exists(commit), commit))

    if contract_format:
        results.check(f"{case_id} release record certifies every package-pinned source",
                      set(SOURCE_KEYS) <= set(certified),
                      f"missing {sorted(set(SOURCE_KEYS) - set(certified))}")
        for key in SOURCE_KEYS:
            if key not in certified:
                continue
            on_disk = hashlib.sha256((ROOT / paths[key]).read_bytes()).hexdigest()
            results.check(f"{case_id} certified {key} hash matches the working tree",
                          certified[key] == on_disk,
                          f"record {certified[key][:12]} vs disk {on_disk[:12]}")
            results.check(f"{case_id} certified {key} hash matches the package",
                          isinstance(package_hashes, dict) and package_hashes.get(key) == certified[key])
        if pin_resolves:
            # The check this whole module exists for.
            for key in SOURCE_KEYS:
                if key not in certified:
                    continue
                at_commit = blob_digest_at(commit, paths[key])
                results.check(
                    f"{case_id} canonicalSourceApprovalCommit contains the certified {key} blob",
                    at_commit == certified[key],
                    f"{commit[:8]} holds {at_commit[:12] if at_commit else 'no such file'}, "
                    f"record certifies {certified[key][:12]}")

    recovery = record.get("formerArtifactRecoveryCommit")
    if isinstance(recovery, str) and COMMIT_RE.match(recovery):
        results.check(f"{case_id} formerArtifactRecoveryCommit exists in this repository",
                      commit_exists(recovery), recovery)

    # --- page counts and frozen baselines -------------------------------------
    declared = {role: (package.get("rolePageStructure") or {}).get(role, {}).get("pageCount")
                for role in ROLES}
    recorded = record.get("rolePageCounts") or {}
    results.check(f"{case_id} release record fixed-role page counts match the package",
                  all(recorded.get(role) == declared[role] for role in FIXED_ROLES),
                  json.dumps({"record": recorded, "package": declared}))
    results.check(f"{case_id} release record records an Accessible page count of at least one",
                  isinstance(recorded.get("accessible"), int) and recorded["accessible"] >= 1,
                  recorded.get("accessible"))

    if contract_format:
        baselines = record["frozenNonAccessibleDomBaselines"]
        results.check(f"{case_id} frozen baselines cover Student, Teacher and Answer Key",
                      all(SHA256_RE.match(str(baselines.get(role, ""))) for role in BASELINE_ROLES),
                      sorted(baselines))

    # --- corrective releases ---------------------------------------------------
    prior = record.get("priorApprovedReleases")
    if record.get("correctiveOf") is not None:
        if results.check(f"{case_id} corrective release indexes its prior approved releases",
                         isinstance(prior, list) and bool(prior)):
            results.check(f"{case_id} corrective release indexes the version it corrects",
                          any(item.get("version") == record["correctiveOf"] for item in prior),
                          record["correctiveOf"])
            for item in prior:
                check_prior_release(results, case_id, case_root, item, certified,
                                    record.get("canonicalSourceApprovalCommit"))
    elif contract_format:
        # Legacy-format records predate priorApprovedReleases entirely; Campaign 1
        # Case 01 and Case 03 reissued as v1.1 without indexing v1.0 in the record.
        results.check(f"{case_id} a first release indexes no prior approved release", not prior)

    return "contract" if contract_format else "legacy"


def validate_repository(results: Results) -> None:
    tracked = git("ls-files").stdout.decode().splitlines()
    offenders = [path for path in tracked if GENERATED_ARTIFACT_RE.search(path)]
    results.check("no generated artifact is tracked in the repository", not offenders, offenders[:10])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cases", nargs="*", help="case ids to validate (default: every registered case)")
    args = parser.parse_args()

    entries = registered_cases()
    known = {entry["id"] for _, _, entry in entries}
    selected = args.cases or sorted(known)
    unknown = [case_id for case_id in selected if case_id not in known]
    if unknown:
        print(f"FAIL: unregistered or planned (package-less) case id(s): {', '.join(unknown)}")
        return 2

    results = Results()
    formats: dict[str, list[str]] = {"contract": [], "legacy": []}
    for curriculum_id, campaign_id, entry in entries:
        if entry["id"] not in selected:
            continue
        record_format = validate_case(results, curriculum_id, campaign_id, entry)
        if record_format:
            formats[record_format].append(entry["id"])
    validate_repository(results)

    for failure in results.failures:
        print(f"FAIL: {failure}")
    verdict = "PASS" if not results.failures else "FAIL"
    print(f"Release integrity: {verdict} {results.passed}/{results.total} "
          f"across {len(selected)} registered case(s); "
          f"{len(formats['contract'])} fully certified against their pinned commit")
    if formats["legacy"]:
        # Named, never silent: an exemption nobody can see is an exemption nobody audits.
        print(f"  legacy-format records exempt from blob-level source certification "
              f"({len(formats['legacy'])}): {', '.join(formats['legacy'])}")
    return 0 if not results.failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
