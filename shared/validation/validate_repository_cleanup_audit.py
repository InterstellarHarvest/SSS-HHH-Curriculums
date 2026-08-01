#!/usr/bin/env python3
"""Validate the baseline-anchored repository cleanup audit."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASELINE = "66b4d5514d55aa4ce9972bea46227d7362d10ce3"
INVENTORY_PATH = ROOT / "shared/cleanup/REPOSITORY_INVENTORY_v1.json"
INVENTORY_MD_PATH = ROOT / "shared/cleanup/REPOSITORY_INVENTORY_v1.md"
PLAN_PATH = ROOT / "shared/cleanup/PROPOSED_CLEANUP_PLAN_v1.json"
PLAN_MD_PATH = ROOT / "shared/cleanup/PROPOSED_CLEANUP_PLAN_v1.md"
CHECKLIST_PATH = ROOT / "shared/cleanup/CLEANUP_OWNER_REVIEW_CHECKLIST_v1.md"
LEGACY_PATH = ROOT / "shared/implementation/CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json"
LEDGER_PATH = ROOT / "shared/implementation/phase2-protected-artifacts.v1.json"
CUTOVER_PATH = ROOT / "shared/implementation/CURRICULUM_EDITOR_CUTOVER_v1.json"
CUTOVER_RESULTS_PATH = ROOT / "apps/curriculum-editor/CUTOVER_VALIDATION_RESULTS.json"

AUDIT_ADDITIONS = {
    "shared/cleanup/REPOSITORY_INVENTORY_v1.json",
    "shared/cleanup/REPOSITORY_INVENTORY_v1.md",
    "shared/cleanup/PROPOSED_CLEANUP_PLAN_v1.json",
    "shared/cleanup/PROPOSED_CLEANUP_PLAN_v1.md",
    "shared/cleanup/CLEANUP_OWNER_REVIEW_CHECKLIST_v1.md",
    "shared/validation/validate_repository_cleanup_audit.py",
}
CLASSIFICATIONS = {
    "A": "ACTIVE_PRODUCTION",
    "B": "APPROVED_RELEASE_SNAPSHOT",
    "C": "HISTORICAL_PROVENANCE",
    "D": "VALIDATION_REQUIRED",
    "E": "COMPATIBILITY_RETAIN",
    "F": "DOCUMENTATION_CURRENT",
    "G": "DOCUMENTATION_HISTORICAL",
    "H": "GENERATED_REPRODUCIBLE",
    "I": "DUPLICATE_REDUNDANT",
    "J": "OBSOLETE_TOOLING",
    "K": "TEMPORARY_OR_ACCIDENTAL",
    "L": "AMBIGUOUS_RETAIN_PENDING_OWNER",
}
BUCKETS = {"SAFE_DELETE", "SAFE_ARCHIVE_OR_CONSOLIDATE", "RETAIN", "AMBIGUOUS_OWNER_DECISION"}
TEXT_SUFFIXES = {"", ".css", ".html", ".js", ".json", ".md", ".mjs", ".py", ".sha256", ".svg", ".txt"}


class Results:
    def __init__(self) -> None:
        self.passed = 0
        self.total = 0
        self.failures: list[str] = []
        self.warnings: list[str] = []

    def check(self, label: str, condition: bool, detail: Any = None) -> None:
        self.total += 1
        if condition:
            self.passed += 1
        else:
            message = label if detail is None else f"{label}: {detail}"
            self.failures.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def baseline_files() -> list[str]:
    return git("ls-tree", "-r", "--name-only", "-z", BASELINE).decode().split("\0")[:-1]


def baseline_blob(path: str) -> bytes:
    return git("show", f"{BASELINE}:{path}")


def reference_index(files: list[str], data: dict[str, bytes]) -> dict[str, set[str]]:
    texts: dict[str, str] = {}
    for path, content in data.items():
        if Path(path).suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            texts[path] = content.decode("utf-8")
        except UnicodeDecodeError:
            pass
    basename_counts = Counter(PurePosixPath(path).name for path in files)
    result: dict[str, set[str]] = {}
    for target in files:
        basename = PurePosixPath(target).name
        sources: set[str] = set()
        for source, text in texts.items():
            if source == target:
                continue
            if target in text or ("/" + target) in text:
                sources.add(source)
                continue
            rel = os.path.relpath(target, PurePosixPath(source).parent.as_posix()).replace(os.sep, "/")
            if rel in text or rel.removeprefix("./") in text:
                sources.add(source)
                continue
            if basename_counts[basename] == 1 and len(basename) >= 8 and basename in text:
                sources.add(source)
        result[target] = sources
    return result


def path_strings(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for child in value.values():
            found |= path_strings(child)
    elif isinstance(value, list):
        for child in value:
            found |= path_strings(child)
    elif isinstance(value, str) and "/" in value and not value.startswith(("http://", "https://")):
        if (ROOT / value).is_file() or value in baseline_files():
            found.add(value)
    return found


def main() -> int:
    sys.dont_write_bytecode = True
    results = Results()
    inventory = load(INVENTORY_PATH)
    plan = load(PLAN_PATH)
    legacy = load(LEGACY_PATH)
    ledger = load(LEDGER_PATH)
    cutover = load(CUTOVER_PATH)
    cutover_results = load(CUTOVER_RESULTS_PATH)

    files = baseline_files()
    file_set = set(files)
    baseline_data = {path: baseline_blob(path) for path in files}
    inventory_items = inventory.get("files", [])
    inventory_paths = [item.get("path") for item in inventory_items]
    by_path = {item["path"]: item for item in inventory_items if "path" in item}

    results.check("required baseline resolves", git("rev-parse", BASELINE).decode().strip() == BASELINE)
    results.check("inventory baseline is exact", inventory.get("scope", {}).get("baseline_commit") == BASELINE)
    results.check("plan baseline is exact", plan.get("baseline_commit") == BASELINE)
    results.check("baseline contains 477 tracked files", len(files) == 477, len(files))
    results.check("every baseline tracked file appears exactly once", Counter(inventory_paths) == Counter(files), {
        "missing": sorted(file_set - set(inventory_paths)),
        "extra": sorted(set(inventory_paths) - file_set),
        "duplicates": sorted(path for path, count in Counter(inventory_paths).items() if count != 1),
    })
    results.check("inventory JSON reports tracked count", inventory["totals"]["tracked_files"] == len(files))
    results.check("inventory JSON reports baseline bytes", inventory["totals"]["total_repository_size_bytes"] == sum(len(data) for data in baseline_data.values()))

    allowed_names = set(CLASSIFICATIONS.values())
    bad_classifications = []
    bad_metadata = []
    changed_baseline = []
    for path in files:
        item = by_path[path]
        category = item.get("classification", {})
        if category.get("code") not in CLASSIFICATIONS or category.get("name") != CLASSIFICATIONS.get(category.get("code")):
            bad_classifications.append(path)
        required = ("file_type", "size_bytes", "sha256", "git", "owner", "references", "latest_meaningful_role", "duplicate_content_relationships", "historical_provenance", "deletion_risk", "cleanup_disposition")
        if any(key not in item for key in required):
            bad_metadata.append(path)
        expected = baseline_data[path]
        current = ROOT / path
        if not current.is_file() or current.read_bytes() != expected:
            changed_baseline.append(path)
        results.check(f"size/hash recorded for {path}", item.get("size_bytes") == len(expected) and item.get("sha256") == sha256(expected))
    results.check("every file has exactly one valid primary classification", not bad_classifications, bad_classifications)
    results.check("every file has required inventory metadata", not bad_metadata, bad_metadata)
    results.check("no baseline file deleted, moved, or modified", not changed_baseline, changed_baseline)

    inventory_md = INVENTORY_MD_PATH.read_text()
    missing_md_paths = [path for path in files if f"`{path}`" not in inventory_md]
    results.check("Markdown inventory lists every tracked path", not missing_md_paths, missing_md_paths)

    computed_refs = reference_index(files, baseline_data)
    reference_mismatches = []
    for path in files:
        recorded = by_path[path].get("references", {})
        recorded_sources = {entry["path"] for entry in recorded.get("sources", [])}
        if recorded.get("count") != len(recorded_sources) or recorded_sources != computed_refs[path]:
            reference_mismatches.append({"path": path, "recorded": sorted(recorded_sources), "computed": sorted(computed_refs[path])})
    results.check("every programmatically detected reference is recorded", not reference_mismatches, reference_mismatches[:10])

    exact_expected: dict[str, list[str]] = defaultdict(list)
    for path, data in baseline_data.items():
        exact_expected[sha256(data)].append(path)
    exact_expected_sets = {frozenset(paths) for paths in exact_expected.values() if len(paths) > 1}
    exact_recorded_sets = {frozenset(group["paths"]) for group in inventory.get("exact_duplicate_groups", {}).values()}
    results.check("all exact byte-duplicate groups are recorded", exact_recorded_sets == exact_expected_sets, {
        "expected_groups": len(exact_expected_sets), "recorded_groups": len(exact_recorded_sets)
    })

    buckets = plan.get("buckets", {})
    results.check("all four cleanup buckets are present", set(buckets) == BUCKETS, sorted(set(buckets)))
    plan_entries = [entry for bucket in BUCKETS for entry in buckets.get(bucket, [])]
    plan_paths = [entry.get("path") for entry in plan_entries]
    results.check("every baseline file appears in exactly one cleanup bucket", Counter(plan_paths) == Counter(files))
    missing_candidates = [path for path in plan_paths if path not in file_set or not (ROOT / path).is_file()]
    results.check("every cleanup candidate exists", not missing_candidates, missing_candidates)

    protected = {item["path"]: item for item in ledger["artifacts"]}
    safe_delete_paths = {entry["path"] for entry in buckets.get("SAFE_DELETE", [])}
    results.check("no protected artifact is SAFE_DELETE", not (safe_delete_paths & set(protected)), sorted(safe_delete_paths & set(protected)))
    incomplete_deletes = []
    for entry in buckets.get("SAFE_DELETE", []):
        if not entry.get("reason") or not entry.get("obsolescence_or_supersession_evidence") or not entry.get("superseding_retained_path"):
            incomplete_deletes.append(entry.get("path"))
    results.check("every SAFE_DELETE item has reason and supersession/obsolescence evidence", not incomplete_deletes, incomplete_deletes)

    bad_archive = []
    retain_paths = {entry["path"] for entry in buckets.get("RETAIN", [])}
    for entry in buckets.get("SAFE_ARCHIVE_OR_CONSOLIDATE", []):
        superseder = entry.get("superseding_retained_path")
        if not superseder or superseder not in retain_paths or not entry.get("validation_required_after_removal"):
            bad_archive.append(entry.get("path"))
    results.check("every consolidation item has a retained superseder and validation gate", not bad_archive, bad_archive)
    results.check("no tracked file is proposed SAFE_DELETE without owner evidence", len(buckets.get("SAFE_DELETE", [])) == 0)

    class_counts = Counter(item["classification"]["name"] for item in inventory_items)
    class_bytes: Counter[str] = Counter()
    for item in inventory_items:
        class_bytes[item["classification"]["name"]] += item["size_bytes"]
    results.check("classification file totals reconcile", inventory["totals"]["files_by_classification"] == dict(sorted(class_counts.items())))
    results.check("classification byte totals reconcile", inventory["totals"]["bytes_by_classification"] == dict(sorted(class_bytes.items())))
    results.check("cleanup deletion totals reconcile", plan["totals"]["proposed_deletion_count"] == len(buckets["SAFE_DELETE"]) and plan["totals"]["proposed_deletion_bytes"] == sum(x["file_size_bytes"] for x in buckets["SAFE_DELETE"]))
    results.check("cleanup consolidation totals reconcile", plan["totals"]["safe_archive_or_consolidate_count"] == len(buckets["SAFE_ARCHIVE_OR_CONSOLIDATE"]) and plan["totals"]["safe_archive_or_consolidate_bytes"] == sum(x["file_size_bytes"] for x in buckets["SAFE_ARCHIVE_OR_CONSOLIDATE"]))

    legacy_paths = [item["path"] for item in legacy["items"]]
    legacy_review = inventory.get("legacy_workflow_review", [])
    legacy_review_paths = [item.get("path") for item in legacy_review]
    results.check("governing legacy inventory has 44 items", len(legacy_paths) == 44, len(legacy_paths))
    results.check("all 44 legacy-workflow items are accounted for exactly once", Counter(legacy_review_paths) == Counter(legacy_paths))
    allowed_legacy = {"RETAIN_PERMANENTLY", "RETAIN_UNTIL_LATER_COMPATIBILITY_MILESTONE", "CANDIDATE_FOR_CLEANUP_NOW", "ALREADY_SUPERSEDED_BUT_NEEDED_FOR_APPROVED_SNAPSHOT_INTEGRITY", "UNCLEAR"}
    results.check("legacy dispositions use approved vocabulary", all(item.get("disposition") in allowed_legacy for item in legacy_review))
    permanent_legacy = {item["path"] for item in legacy_review if item["disposition"] == "RETAIN_PERMANENTLY"}
    results.check("all must-retain legacy items are permanent", all(path in permanent_legacy for path, source in ((x["path"], x) for x in legacy["items"]) if "must retain permanently" in source["classifications"]))
    results.check("all legacy items remain in RETAIN cleanup bucket", set(legacy_paths) <= retain_paths, sorted(set(legacy_paths) - retain_paths))

    external = {item["path"]: item for item in inventory.get("ignored_local_observations", [])}
    pdfs = [item for item in ledger["artifacts"] if item["category"] == "historical-pdf"]
    retained_pdf_failures = []
    for artifact in pdfs:
        path = artifact["path"]
        record = by_path.get(path) or external.get(path)
        if not record or record.get("cleanup_disposition") != "RETAIN" or record.get("sha256") != artifact["sha256"]:
            retained_pdf_failures.append(path)
    results.check("protected ledger declares exactly 20 historical PDFs", len(pdfs) == 20, len(pdfs))
    results.check("all 20 historical PDFs are recorded RETAIN with ledger hashes", not retained_pdf_failures, retained_pdf_failures)
    tracked_pdfs = {path for path in files if path.endswith(".pdf")}
    results.check("the tracked-PDF contradiction is recorded precisely", len(tracked_pdfs) == 19 and any(finding.get("id") == "PROTECTED_PDF_NOT_TRACKED" for finding in inventory.get("contradictions", [])))
    external_pdf = "sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/teacher_v1.0_revalidated.pdf"
    if not (ROOT / external_pdf).is_file():
        results.warn(f"ledger-protected PDF is not present in this checkout (known audit contradiction): {external_pdf}")

    required_retain = set(protected) & file_set
    for case in cutover["effectiveCases"]:
        required_retain.add(case["packagePath"])
        required_retain.add(case["currentMasterPath"])
        required_retain.update(role["path"] for role in case["currentRoles"].values())
        required_retain.update(snapshot["path"] for snapshot in case["protectedMasterSnapshots"])
        required_retain.update(case.get("ownerApprovalReferences", []))
    required_retain |= path_strings(cutover)
    required_retain |= {
        "shared/implementation/CURRICULUM_EDITOR_CUTOVER_v1.json",
        "shared/implementation/CURRICULUM_EDITOR_CUTOVER_v1.md",
        "shared/implementation/CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.json",
        "shared/implementation/CURRICULUM_EDITOR_LEGACY_WORKFLOW_INVENTORY_v1.md",
        "shared/implementation/phase2-protected-artifacts.v1.json",
        "apps/curriculum-editor/PHASE1_ACCEPTANCE.md",
        "apps/curriculum-editor/PHASE2_OWNER_APPROVAL.md",
        "apps/curriculum-editor/CUTOVER_OWNER_APPROVAL.md",
        "apps/curriculum-editor/CUTOVER_OWNER_REVIEW_CHECKLIST.md",
        "apps/curriculum-editor/CUTOVER_VALIDATION_RESULTS.json",
    }
    required_retain &= file_set
    results.check("all current packages, masters, role outputs, approvals, ledgers, reconciliation, and cutover records are RETAIN", required_retain <= retain_paths, sorted(required_retain - retain_paths))
    results.check("all protected tracked artifacts are marked protected", all(by_path[path].get("protected_artifact") for path in set(protected) & file_set))

    case04_paths = [path for path in files if "case-04" in path.lower() or "case04" in path.lower()]
    results.check("Case 04 has no tracked implementation paths", not case04_paths, case04_paths)
    results.check("cutover manifest keeps Case 04 NOT_STARTED", cutover.get("policies", {}).get("case04") == "NOT_STARTED")
    results.check("cutover results keep Case 04 NOT_STARTED", cutover_results.get("case04") == "NOT_STARTED")
    results.check("cleanup plan keeps Case 04 NOT_STARTED", plan.get("policy", {}).get("case04") == "NOT_STARTED")

    missing_additions = [path for path in AUDIT_ADDITIONS if not (ROOT / path).is_file()]
    results.check("all six authorized audit additions exist", not missing_additions, missing_additions)
    status_lines = git("status", "--porcelain=v1", "--untracked-files=all").decode().splitlines()
    unexpected_changes = []
    for line in status_lines:
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if path not in AUDIT_ADDITIONS:
            unexpected_changes.append(line)
    results.check("only audit records and validator differ from baseline", not unexpected_changes, unexpected_changes)

    plan_md = PLAN_MD_PATH.read_text()
    checklist = CHECKLIST_PATH.read_text()
    results.check("plan states no deletion authorization", "NO DELETIONS AUTHORIZED" in plan_md and plan.get("status") == "PROPOSAL_ONLY_NO_DELETIONS_AUTHORIZED")
    results.check("owner checklist records Case 04 boundary", "Case 04 remains `NOT_STARTED`" in checklist)
    results.check("owner checklist records protected-PDF contradiction", external_pdf in checklist)

    print(f"Repository cleanup audit validation: {results.passed}/{results.total} checks passed")
    print(f"Baseline: {BASELINE}")
    print(f"Tracked inventory: {len(files)} files / {sum(len(data) for data in baseline_data.values())} bytes")
    print(f"SAFE_DELETE: {len(buckets['SAFE_DELETE'])} files / {sum(x['file_size_bytes'] for x in buckets['SAFE_DELETE'])} bytes")
    print(f"SAFE_ARCHIVE_OR_CONSOLIDATE: {len(buckets['SAFE_ARCHIVE_OR_CONSOLIDATE'])} files / {sum(x['file_size_bytes'] for x in buckets['SAFE_ARCHIVE_OR_CONSOLIDATE'])} bytes")
    print(f"Protected ledger: {len(protected)} items; historical PDFs: {len(pdfs)} declared / {len(tracked_pdfs)} tracked")
    print(f"Legacy workflow: {len(legacy_review)} items")
    for warning in results.warnings:
        print(f"WARNING: {warning}")
    if results.failures:
        for failure in results.failures:
            print(f"FAIL: {failure}")
        return 1
    print("PASS: no baseline file was deleted, moved, renamed, or modified; Case 04 remains NOT_STARTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
