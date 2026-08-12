#!/usr/bin/env python3
"""Focused tests for generic HHH operational-package validation.

Exercises the pure lifecycle and source-ownership rules in ``validate_static.py``
against synthetic registry entries and packages. No test reads a real case
package, and the live activation registry keeps zero editor-ready HHH entries —
these rules must hold before the first HHH package exists.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_static  # noqa: E402

CASE00_PACKAGE_PATH = "hhh/campaign-1/case-00-archive-orientation/source/case-package.json"


def registry_entry(status: str = "DRAFT", **overrides) -> dict:
    contract = {
        "DRAFT": ("DRAFT", "OWNER_REVIEW_NOT_STARTED", "NOT_RUN"),
        "VALIDATION_BUILD": ("VALIDATION", "OWNER_REVIEW_NOT_STARTED", "NOT_RUN"),
        "OWNER_GATE_OPEN": ("OWNER_REVIEW", "OWNER_REVIEW_IN_PROGRESS", "NOT_RUN"),
        "APPROVED_STABLE": ("APPROVED", "APPROVED", "PASS"),
    }[status]
    entry = {
        "id": "HHH-C1-CASE00",
        "status": status,
        "packageStatus": contract[0],
        "approval": {"owner": "Nate / Owner", "status": contract[1], "printStatus": contract[2]},
        "editorPackage": CASE00_PACKAGE_PATH,
    }
    if status == "APPROVED_STABLE":
        entry["historyRecord"] = "hhh/campaign-1/case-00-archive-orientation/history/release-v1.0.json"
    entry.update(overrides)
    return entry


def matching_package(entry: dict, **overrides) -> dict:
    package = {
        "id": entry["id"],
        "status": entry["status"],
        "approval": dict(entry["approval"]),
    }
    if "historyRecord" in entry:
        package["releaseHistory"] = entry["historyRecord"]
    package.update(overrides)
    return package


def owned_sources(package_path: str = CASE00_PACKAGE_PATH) -> dict:
    root = package_path[: -len("case-package.json")]
    return {
        "content": {"source": f"{root}content.html"},
        "presentation": {"source": f"{root}presentation.css"},
        "taskRegistry": {"source": f"{root}task-registry.js"},
        "layoutOverrides": {"source": f"{root}layout-overrides.json"},
    }


class LifecycleStates(unittest.TestCase):
    """The four canonical states pass; every cross-state combination fails."""

    def assertClean(self, entry: dict, package: dict):
        self.assertEqual(validate_static.hhh_lifecycle_findings(entry, package), [])

    def assertViolates(self, entry: dict, package: dict, fragment: str):
        findings = validate_static.hhh_lifecycle_findings(entry, package)
        self.assertTrue(findings, "expected at least one lifecycle finding")
        self.assertTrue(any(fragment in f for f in findings),
                        f"expected a finding containing {fragment!r}, got {findings}")

    def test_draft_state_is_clean(self):
        entry = registry_entry("DRAFT")
        self.assertClean(entry, matching_package(entry))

    def test_validation_build_state_is_clean(self):
        entry = registry_entry("VALIDATION_BUILD")
        self.assertClean(entry, matching_package(entry))

    def test_owner_gate_open_state_is_clean(self):
        entry = registry_entry("OWNER_GATE_OPEN")
        self.assertClean(entry, matching_package(entry))

    def test_approved_stable_state_is_clean(self):
        entry = registry_entry("APPROVED_STABLE")
        self.assertClean(entry, matching_package(entry))

    def test_unsupported_status_is_rejected(self):
        entry = registry_entry("DRAFT")
        entry["status"] = "READY_TO_MERGE"
        self.assertViolates(entry, matching_package(entry), "unsupported lifecycle status")

    def test_registry_and_package_status_must_agree(self):
        entry = registry_entry("VALIDATION_BUILD")
        package = matching_package(entry, status="DRAFT")
        self.assertViolates(entry, package, "disagree")

    def test_draft_with_validation_package_status_is_rejected(self):
        entry = registry_entry("DRAFT", packageStatus="VALIDATION")
        self.assertViolates(entry, matching_package(entry), "requires registry packageStatus 'DRAFT'")

    def test_validation_build_with_owner_review_package_status_is_rejected(self):
        entry = registry_entry("VALIDATION_BUILD", packageStatus="OWNER_REVIEW")
        self.assertViolates(entry, matching_package(entry), "requires registry packageStatus 'VALIDATION'")

    def test_validation_build_with_in_progress_approval_is_rejected(self):
        entry = registry_entry("VALIDATION_BUILD")
        entry["approval"]["status"] = "OWNER_REVIEW_IN_PROGRESS"
        self.assertViolates(entry, matching_package(entry), "approval status 'OWNER_REVIEW_NOT_STARTED'")

    def test_owner_gate_open_with_passed_print_is_rejected(self):
        entry = registry_entry("OWNER_GATE_OPEN")
        entry["approval"]["printStatus"] = "PASS"
        self.assertViolates(entry, matching_package(entry), "print status 'NOT_RUN'")

    def test_registry_and_package_approval_metadata_must_be_identical(self):
        entry = registry_entry("OWNER_GATE_OPEN")
        package = matching_package(entry)
        package["approval"]["status"] = "OWNER_REVIEW_PASS"
        self.assertViolates(entry, package, "approval status 'OWNER_REVIEW_IN_PROGRESS'")

    def test_approved_stable_without_history_record_is_rejected(self):
        entry = registry_entry("APPROVED_STABLE")
        package = matching_package(entry)
        del entry["historyRecord"]
        self.assertViolates(entry, package, "matching historyRecord/releaseHistory")

    def test_approved_stable_with_mismatched_release_history_is_rejected(self):
        entry = registry_entry("APPROVED_STABLE")
        package = matching_package(entry, releaseHistory="hhh/campaign-1/other/history/release-v1.0.json")
        self.assertViolates(entry, package, "matching historyRecord/releaseHistory")

    def test_unreleased_states_must_not_carry_release_pointers(self):
        for status in ("DRAFT", "VALIDATION_BUILD", "OWNER_GATE_OPEN"):
            entry = registry_entry(status, historyRecord="hhh/x/history/release-v0.1.json")
            self.assertViolates(entry, matching_package(registry_entry(status)),
                                "must not declare a historyRecord")
            entry = registry_entry(status)
            package = matching_package(entry, releaseHistory="hhh/x/history/release-v0.1.json")
            self.assertViolates(entry, package, "must not declare a releaseHistory")


class SourceOwnership(unittest.TestCase):
    """Package-pinned sources must be exactly the registered unit's own files."""

    def assertClean(self, editor_package: str, package: dict):
        self.assertEqual(validate_static.hhh_source_path_findings(editor_package, package), [])

    def assertViolates(self, editor_package: str, package: dict, fragment: str):
        findings = validate_static.hhh_source_path_findings(editor_package, package)
        self.assertTrue(findings, "expected at least one ownership finding")
        self.assertTrue(any(fragment in f for f in findings),
                        f"expected a finding containing {fragment!r}, got {findings}")

    def test_canonical_case00_paths_pass(self):
        self.assertClean(CASE00_PACKAGE_PATH, owned_sources())

    def test_canonical_special_unit_paths_pass(self):
        path = "hhh/campaign-1/synthesis-campaign-1/source/case-package.json"
        self.assertClean(path, owned_sources(path))

    def test_another_units_source_is_rejected(self):
        package = owned_sources()
        package["content"]["source"] = "hhh/campaign-1/case-01-fertile-crescent/source/content.html"
        self.assertViolates(CASE00_PACKAGE_PATH, package, "content source must be the package-owned")

    def test_sss_source_is_rejected(self):
        package = owned_sources()
        package["taskRegistry"]["source"] = "sss/campaign-1/case-01-iss-greenhouse/source/task-registry.js"
        self.assertViolates(CASE00_PACKAGE_PATH, package, "taskRegistry source must be the package-owned")

    def test_traversal_is_rejected(self):
        package = owned_sources()
        package["presentation"]["source"] = (
            "hhh/campaign-1/case-00-archive-orientation/source/../../../sss/campaign-1/"
            "case-01-iss-greenhouse/source/presentation.css")
        self.assertViolates(CASE00_PACKAGE_PATH, package, "presentation source must be the package-owned")

    def test_absolute_path_is_rejected(self):
        package = owned_sources()
        package["content"]["source"] = "/hhh/campaign-1/case-00-archive-orientation/source/content.html"
        self.assertViolates(CASE00_PACKAGE_PATH, package, "content source must be the package-owned")

    def test_alternate_filename_satisfying_the_schema_suffix_is_rejected(self):
        package = owned_sources()
        package["content"]["source"] = "hhh/campaign-1/case-00-archive-orientation/source/final-content.html"
        self.assertViolates(CASE00_PACKAGE_PATH, package, "content source must be the package-owned")

    def test_alternate_location_is_rejected(self):
        package = owned_sources()
        package["layoutOverrides"]["source"] = "hhh/campaign-1/case-00-archive-orientation/assets/layout-overrides.json"
        self.assertViolates(CASE00_PACKAGE_PATH, package, "layoutOverrides source must be the package-owned")

    def test_missing_source_declaration_is_rejected(self):
        package = owned_sources()
        del package["taskRegistry"]
        self.assertViolates(CASE00_PACKAGE_PATH, package, "taskRegistry source must be the package-owned")

    def test_noncanonical_editor_package_path_is_rejected(self):
        for path in ("sss/campaign-1/case-01-iss-greenhouse/source/case-package.json",
                     "hhh/campaign-1/case-00/../case-01/source/case-package.json",
                     "/hhh/campaign-1/case-00-archive-orientation/source/case-package.json",
                     "hhh/campaign-1/case-00-archive-orientation/editor/case-package.json"):
            self.assertViolates(path, owned_sources(), "not a canonical HHH unit package path")


if __name__ == "__main__":
    unittest.main(verbosity=2)
