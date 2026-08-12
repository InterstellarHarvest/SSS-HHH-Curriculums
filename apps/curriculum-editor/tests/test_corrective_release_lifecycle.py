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

    def __init__(self, root: Path, version: str, status: str, *,
                 case_id: str = CASE_ID, release_history: bool = False):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        self.case_id = case_id
        self.package = {"id": case_id, "version": version, "status": status}
        if release_history:
            self.package["releaseHistory"] = f"x/history/release-v{version}.json"

    def history(self) -> Path:
        path = self.root / "history"
        path.mkdir(exist_ok=True)
        return path

    def add_release(self, version: str, *, record: dict | None = None, name: str | None = None):
        body = record if record is not None else release_record(version, case_id=self.case_id)
        (self.history() / (name or f"release-v{version}.json")).write_text(
            json.dumps(body), encoding="utf-8")
        return self

    def add_approval(self, version: str, stem: str | None = None):
        stem = stem or lifecycle.approval_stem(self.case_id)
        (self.history() / f"{stem}_OWNER_APPROVAL_v{version}.md").write_text(
            f"# Owner approval v{version}\n", encoding="utf-8")
        return self

    def add_raw(self, name: str, body: str = "not a record"):
        (self.history() / name).write_text(body, encoding="utf-8")
        return self

    def findings(self, registry: dict | None = None) -> list[str]:
        return lifecycle.history_findings(self.root, self.case_id, self.package, registry)


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


class ApprovalStems(TempCaseTest):
    """The shared identity-to-approval-stem helper and special-unit filenames."""

    def test_numeric_identities_keep_their_zero_padded_case_number(self):
        self.assertEqual(lifecycle.approval_stem("HHH-C1-CASE00"), "CASE00")
        self.assertEqual(lifecycle.approval_stem("SSS-C1-CASE01"), "CASE01")
        self.assertEqual(lifecycle.approval_stem("HHH-C2-CASE07"), "CASE07")
        self.assertEqual(lifecycle.approval_stem("SSS-C2-CASE02"), "CASE02")

    def test_special_hhh_identities_map_to_their_own_stems(self):
        self.assertEqual(lifecycle.approval_stem("HHH-C1-SYNTHESIS"), "SYNTHESIS")
        self.assertEqual(lifecycle.approval_stem("HHH-C2-CAPSTONE"), "CAPSTONE")

    def test_canonical_approval_filenames(self):
        self.assertEqual(lifecycle.approval_record_name("HHH-C1-CASE00", "0.1"),
                         "CASE00_OWNER_APPROVAL_v0.1.md")
        self.assertEqual(lifecycle.approval_record_name("HHH-C1-SYNTHESIS", "1.0"),
                         "SYNTHESIS_OWNER_APPROVAL_v1.0.md")
        self.assertEqual(lifecycle.approval_record_name("HHH-C2-CAPSTONE", "1.0"),
                         "CAPSTONE_OWNER_APPROVAL_v1.0.md")

    def test_unknown_identities_are_rejected_not_defaulted(self):
        for identity in ("HHH-C1-FINALE", "SYNTHESIS", "HHH-C1-CASE1", "SSS-C1-CASE001", "", None):
            with self.assertRaises(ValueError, msg=identity):
                lifecycle.approval_stem(identity)

    def test_classification_recognizes_exactly_the_canonical_stems(self):
        self.assertEqual(lifecycle.classify("SYNTHESIS_OWNER_APPROVAL_v1.0.md"),
                         ("approval", (1, 0), "SYNTHESIS"))
        self.assertEqual(lifecycle.classify("CAPSTONE_OWNER_APPROVAL_v1.0.md"),
                         ("approval", (1, 0), "CAPSTONE"))
        self.assertEqual(lifecycle.classify("CASE00_OWNER_APPROVAL_v0.1.md"),
                         ("approval", (0, 1), "CASE00"))
        for malformed in ("SYNTH_OWNER_APPROVAL_v1.0.md", "CASE0A_OWNER_APPROVAL_v1.0.md",
                          "PROGRAM-CAPSTONE_OWNER_APPROVAL_v1.0.md", "capstone_OWNER_APPROVAL_v1.0.md"):
            self.assertIsNone(lifecycle.classify(malformed), malformed)


class SpecialUnitLifecycle(TempCaseTest):
    """Special HHH units flow through the one common lifecycle, not a parallel one."""

    def assertFails(self, findings: list[str], fragment: str):
        self.assertTrue(findings, "expected at least one finding")
        self.assertTrue(any(fragment in f for f in findings),
                        f"expected a finding containing {fragment!r}, got {findings}")

    def test_orientation_case00_first_release_draft_is_clean(self):
        f = self.fixture("a", "0.1", "DRAFT", case_id="HHH-C1-CASE00")
        self.assertEqual(f.findings(), [])

    def test_ordinary_core_case_corrective_candidate_retains_records(self):
        f = (self.fixture("b", "1.1", "DRAFT", case_id="HHH-C2-CASE07")
             .add_release("1.0").add_approval("1.0"))
        self.assertEqual(f.findings(), [])

    def test_approved_synthesis_with_its_own_release_and_stem_approval(self):
        f = (self.fixture("c", "1.0", "APPROVED_STABLE", case_id="HHH-C1-SYNTHESIS")
             .add_release("1.0").add_approval("1.0"))
        f.package["releaseHistory"] = "x/history/release-v1.0.json"
        self.assertEqual(f.findings(), [])
        self.assertTrue((f.history() / "SYNTHESIS_OWNER_APPROVAL_v1.0.md").is_file())

    def test_capstone_corrective_candidate_retains_capstone_records(self):
        f = (self.fixture("d", "1.1", "DRAFT", case_id="HHH-C2-CAPSTONE")
             .add_release("1.0").add_approval("1.0"))
        self.assertEqual(f.findings(), [])
        self.assertTrue((f.history() / "CAPSTONE_OWNER_APPROVAL_v1.0.md").is_file())

    def test_capstone_candidate_approving_its_own_version_is_rejected(self):
        f = (self.fixture("e", "1.1", "DRAFT", case_id="HHH-C2-CAPSTONE")
             .add_release("1.0").add_approval("1.1"))
        self.assertFails(f.findings(), "approves the candidate's own version")

    def test_malformed_special_approval_name_is_not_a_canonical_record(self):
        f = (self.fixture("f", "1.1", "DRAFT", case_id="HHH-C1-SYNTHESIS")
             .add_release("1.0").add_raw("SYNTH_OWNER_APPROVAL_v1.0.md"))
        self.assertFails(f.findings(), "not a canonical release or approval record")

    def test_approval_with_another_units_stem_is_rejected(self):
        f = (self.fixture("g", "1.1", "DRAFT", case_id="HHH-C1-SYNTHESIS")
             .add_release("1.0").add_approval("1.0", stem="CASE00"))
        self.assertFails(f.findings(), "not this case's canonical SYNTHESIS")

    def test_numeric_case_rejects_a_special_stem_approval(self):
        f = (self.fixture("h", "1.1", "DRAFT", case_id="SSS-C2-CASE02")
             .add_release("1.0").add_approval("1.0").add_approval("1.0", stem="CAPSTONE"))
        self.assertFails(f.findings(), "not this case's canonical CASE02")

    def test_unresolvable_identity_is_reported_not_defaulted(self):
        f = self.fixture("i", "1.0", "DRAFT", case_id="HHH-C1-FINALE")
        f.history()
        self.assertFails(f.findings(), "has no canonical owner-approval stem")


if __name__ == "__main__":
    unittest.main(verbosity=2)
