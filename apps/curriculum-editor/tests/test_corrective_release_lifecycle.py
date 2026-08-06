#!/usr/bin/env python3
"""Focused tests for the corrective-release lifecycle rules.

Every fixture is synthetic and built in a temporary directory. No test reads or
writes a real case package.

The distinction under test: a first-release package has no history at all, while a
corrective candidate keeps the records of the versions that were genuinely
approved, and may never carry or point at a record for its own version.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared/validation"))
import corrective_release_lifecycle as lifecycle  # noqa: E402

CASE_ID = "SSS-C2-CASE02"


def release_record(version: str, case_id: str = CASE_ID, status: str = "APPROVED_STABLE") -> dict:
    return {"schemaVersion": 1, "caseId": case_id, "curriculumVersion": version,
            "status": status, "approvalDate": "2026-08-05", "owner": "Nate / Owner"}


class LifecycleFixture:
    """A synthetic case root with a package and an optional history/ directory."""

    def __init__(self, root: Path, version: str, status: str, *, release_history: bool = False):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        self.package = {"id": CASE_ID, "version": version, "status": status}
        if release_history:
            self.package["releaseHistory"] = f"x/history/release-v{version}.json"

    def history(self) -> Path:
        path = self.root / "history"
        path.mkdir(exist_ok=True)
        return path

    def add_release(self, version: str, *, record: dict | None = None, name: str | None = None):
        body = record if record is not None else release_record(version)
        (self.history() / (name or f"release-v{version}.json")).write_text(
            json.dumps(body), encoding="utf-8")
        return self

    def add_approval(self, version: str, case_number: str = "02"):
        (self.history() / f"CASE{case_number}_OWNER_APPROVAL_v{version}.md").write_text(
            f"# Owner approval v{version}\n", encoding="utf-8")
        return self

    def add_raw(self, name: str, body: str = "not a record"):
        (self.history() / name).write_text(body, encoding="utf-8")
        return self

    def findings(self, registry: dict | None = None) -> list[str]:
        return lifecycle.history_findings(self.root, CASE_ID, self.package, registry)


class TempCaseTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="corrective-lifecycle-")
        self.base = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def fixture(self, name: str, version: str, status: str, **kwargs) -> LifecycleFixture:
        return LifecycleFixture(self.base / name, version, status, **kwargs)


class VersionParsing(TempCaseTest):
    def test_two_component_versions_parse(self):
        self.assertEqual(lifecycle.parse_version("1.0"), (1, 0))
        self.assertEqual(lifecycle.parse_version("1.1"), (1, 1))

    def test_three_component_and_malformed_versions_are_rejected(self):
        for value in ("1.0.1", "v1.0", "1", "", "1.x", None, 1.0):
            self.assertIsNone(lifecycle.parse_version(value), value)

    def test_comparison_is_numeric_not_lexicographic(self):
        self.assertGreater(lifecycle.parse_version("1.10"), lifecycle.parse_version("1.9"))
        self.assertGreater(lifecycle.parse_version("2.0"), lifecycle.parse_version("1.11"))


class ValidStates(TempCaseTest):
    def test_first_release_draft_with_no_history(self):
        self.assertEqual(self.fixture("a", "1.0", "DRAFT").findings(), [])

    def test_first_release_owner_gate_open_with_no_history(self):
        self.assertEqual(self.fixture("b", "1.0", "OWNER_GATE_OPEN").findings(), [])

    def test_corrective_draft_retaining_canonical_v1_0_records(self):
        f = self.fixture("c", "1.1", "DRAFT").add_release("1.0").add_approval("1.0")
        self.assertEqual(f.findings(), [])

    def test_corrective_owner_gate_open_retaining_canonical_v1_0_records(self):
        f = self.fixture("d", "1.1", "OWNER_GATE_OPEN").add_release("1.0").add_approval("1.0")
        self.assertEqual(f.findings(), [])

    def test_approved_package_with_its_own_release_record(self):
        f = self.fixture("e", "1.0", "APPROVED_STABLE").add_release("1.0").add_approval("1.0")
        f.package["releaseHistory"] = "x/history/release-v1.0.json"
        self.assertEqual(f.findings(), [])

    def test_released_v1_1_preserving_v1_0_through_prior_releases(self):
        # The established corrective-release pattern: one record for the current
        # version, with the earlier release carried inside priorApprovedReleases.
        record = release_record("1.1")
        record["priorApprovedReleases"] = [{"version": "1.0", "status": "APPROVED_STABLE"}]
        f = self.fixture("f", "1.1", "APPROVED_STABLE").add_release("1.1", record=record)
        f.package["releaseHistory"] = "x/history/release-v1.1.json"
        self.assertEqual(f.findings(), [])

    def test_approved_package_may_also_retain_the_earlier_record_on_disk(self):
        f = (self.fixture("g", "1.1", "APPROVED_STABLE")
             .add_release("1.1").add_approval("1.1").add_release("1.0").add_approval("1.0"))
        f.package["releaseHistory"] = "x/history/release-v1.1.json"
        self.assertEqual(f.findings(), [])


class InvalidStates(TempCaseTest):
    def assertFails(self, findings: list[str], fragment: str):
        self.assertTrue(findings, "expected at least one finding")
        self.assertTrue(any(fragment in f for f in findings),
                        f"expected a finding containing {fragment!r}, got {findings}")

    def test_candidate_containing_a_release_record_for_its_own_version(self):
        f = self.fixture("a", "1.1", "DRAFT").add_release("1.0").add_release("1.1")
        self.assertFails(f.findings(), "releases the candidate's own version")

    def test_candidate_containing_an_owner_approval_for_its_own_version(self):
        f = self.fixture("b", "1.1", "DRAFT").add_release("1.0").add_approval("1.1")
        self.assertFails(f.findings(), "approves the candidate's own version")

    def test_candidate_declaring_a_release_history_pointer(self):
        f = self.fixture("c", "1.1", "DRAFT", release_history=True).add_release("1.0")
        self.assertFails(f.findings(), "declares a releaseHistory pointer")

    def test_candidate_task_registry_declaring_a_release_history_pointer(self):
        f = self.fixture("d", "1.1", "DRAFT").add_release("1.0")
        self.assertFails(f.findings({"releaseHistory": "x"}), "task registry declares a releaseHistory")

    def test_candidate_retaining_a_record_above_its_own_version(self):
        f = self.fixture("e", "1.1", "DRAFT").add_release("1.0").add_release("2.0")
        self.assertFails(f.findings(), "above the package version")

    def test_candidate_version_equal_to_its_retained_approved_version(self):
        f = self.fixture("f", "1.0", "DRAFT").add_release("1.0")
        self.assertFails(f.findings(), "releases the candidate's own version")

    def test_candidate_version_lower_than_its_retained_approved_version(self):
        f = self.fixture("g", "1.0", "DRAFT").add_release("1.1")
        self.assertFails(f.findings(), "above the package version")

    def test_arbitrary_file_smuggled_into_history(self):
        f = self.fixture("h", "1.1", "DRAFT").add_release("1.0").add_raw("notes.txt")
        self.assertFails(f.findings(), "not a canonical release or approval record")

    def test_malformed_release_record_in_history(self):
        f = self.fixture("i", "1.1", "DRAFT")
        f.history()
        (f.root / "history/release-v1.0.json").write_text("{ not json", encoding="utf-8")
        self.assertFails(f.findings(), "not readable canonical JSON")

    def test_filename_and_internal_version_disagree(self):
        f = self.fixture("j", "1.1", "DRAFT").add_release("1.0", record=release_record("1.1"))
        self.assertFails(f.findings(), "disagree")

    def test_retained_record_belongs_to_another_case(self):
        f = self.fixture("k", "1.1", "DRAFT").add_release(
            "1.0", record=release_record("1.0", case_id="SSS-C2-CASE05"))
        self.assertFails(f.findings(), "records caseId")

    def test_retained_record_is_not_an_approved_release(self):
        f = self.fixture("l", "1.1", "DRAFT").add_release(
            "1.0", record=release_record("1.0", status="DRAFT"))
        self.assertFails(f.findings(), "not an approved release")

    def test_first_release_claiming_an_approval_with_no_release_record(self):
        f = self.fixture("m", "1.1", "DRAFT").add_approval("1.0")
        self.assertFails(f.findings(), "with no retained release record")

    def test_package_version_is_not_two_component(self):
        f = self.fixture("n", "1.0.1", "DRAFT")
        self.assertFails(f.findings(), "not a two-component version")

    def test_approved_package_still_rejects_a_record_above_its_version(self):
        f = self.fixture("o", "1.0", "APPROVED_STABLE").add_release("1.0").add_release("1.1")
        f.package["releaseHistory"] = "x/history/release-v1.0.json"
        self.assertFails(f.findings(), "above the package version")


if __name__ == "__main__":
    unittest.main(verbosity=2)
