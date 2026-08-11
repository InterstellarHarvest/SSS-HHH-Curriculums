#!/usr/bin/env python3
"""Mutation tests for the Campaign 2 Case 02 protections.

Each mutation reproduces a defect the completion audit found in the released
v1.0 package, injects it into the working sources, and asserts that
``validate_case02_campaign2.py`` fails. Sources are always restored, including
when a test fails, so the tree is left exactly as it was found.

A protection that cannot be made to fail is not a protection.
"""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[3]
CASE_ROOT = ROOT / "sss/campaign-2/case-02-missing-dance"
SOURCE = CASE_ROOT / "source"
CONTENT = SOURCE / "content.html"
REGISTRY = SOURCE / "task-registry.js"
PACKAGE = SOURCE / "case-package.json"
RELEASE = CASE_ROOT / "history/release-v1.2.json"
RETAINED = CASE_ROOT / "history/release-v1.1.json"
VALIDATOR = ROOT / "apps/curriculum-editor/tests/validate_case02_campaign2.py"
TRACKED = (CONTENT, REGISTRY, PACKAGE, RELEASE)


def validator_result() -> tuple[bool, list[str]]:
    """Run the Case 02 validator and return (passed, failing assertion names)."""
    run = subprocess.run([sys.executable, str(VALIDATOR)], cwd=ROOT,
                         text=True, capture_output=True)
    try:
        payload = json.loads(run.stdout[run.stdout.index("{"):])
    except (ValueError, json.JSONDecodeError):
        # A crash is also a failure to validate, which is what we assert on.
        return False, ["validator crashed"]
    return run.returncode == 0, [a["name"] for a in payload["assertions"] if not a["pass"]]



# The release record cannot name the commit that certifies it: the lifecycle promotion changes
# the approved task registry, so those sources exist only from the release commit onward. The
# pin is therefore PENDING_RELEASE_COMMIT in the release commit and written by the narrow
# follow-up. Exactly these assertions fail during that window. The tolerance is gated on the
# placeholder still being present, so it evaporates the moment the pin lands.
PENDING_PIN_PLACEHOLDER = "PENDING_RELEASE_COMMIT"
PENDING_PIN_FAILURES = {
    "the v1.2 release record records the approved print gate",
    "the v1.2 release record records the physical print gate",
    "the v1.2 release record records the accepted validation totals",
    "the recorded Case 02 total is the total this validator actually produces",
    "every commit reference in the v1.2 release record exists",
    "the v1.2 release record pins the whole corrective review, not just its last commit",
    "canonicalSourceApprovalCommit contains all four source blobs the record certifies",
    "the certified source commit actually contains the sources the record pins",
    "the v1.2 release record certifies all four sources and they match the package",
}


def pin_is_pending() -> bool:
    """True only while the release record still holds the placeholder pin."""
    try:
        record = json.loads(RELEASE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return record.get("canonicalSourceApprovalCommit") == PENDING_PIN_PLACEHOLDER


class Case02Mutations(unittest.TestCase):
    """Every test mutates real sources, so restoration is unconditional."""

    def setUp(self):
        self.original = {path: path.read_bytes() for path in TRACKED}
        self.addCleanup(self.restore)
        passed, failures = validator_result()
        if not passed and pin_is_pending() and set(failures) <= PENDING_PIN_FAILURES:
            passed = True
        self.assertTrue(passed, f"baseline must be green before mutating; failures: {failures}")

    def restore(self):
        for path, body in self.original.items():
            path.write_bytes(body)

    def rehash(self):
        """Re-pin hashes everywhere they are declared, including the release record.

        Without the release-record half, every content mutation would be caught by the
        hash-agreement assertion instead of the defect assertion it targets, and these
        tests would prove far less than they appear to.
        """
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        import hashlib
        for key, name in (("content", "content.html"), ("taskRegistry", "task-registry.js")):
            package["sourceHashes"][key] = hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
        PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        release = json.loads(RELEASE.read_text(encoding="utf-8"))
        release["sourceHashes"] = dict(package["sourceHashes"])
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


    def mutate_content(self, old: str, new: str, count: int = 1):
        text = CONTENT.read_text(encoding="utf-8")
        self.assertEqual(text.count(old), count, f"mutation anchor not unique: {old[:60]!r}")
        CONTENT.write_text(text.replace(old, new), encoding="utf-8")
        self.rehash()

    def assertCaught(self, label: str, expect: str = ""):
        """Assert the mutation fails validation, and that the *intended* protection fired.

        Now that Case 02 is a frozen release, its DOM baseline catches any content edit.
        Asserting only that validation failed would therefore prove nothing about the
        content detectors, so every mutation names the assertion it must trip.
        """
        passed, failures = validator_result()
        self.assertFalse(passed, f"{label} was NOT caught by validation")
        if expect:
            self.assertTrue(any(expect in name for name in failures),
                            f"{label} failed validation, but not via {expect!r}; got: {failures}")
        return failures

    # ── the released blocker, in its parts ───────────────────────────

    def test_missing_task1_writable_field(self):
        """Removing a Task 1 mark cell must fail: directions would promise a column that is gone."""
        text = CONTENT.read_text(encoding="utf-8")
        start = text.index('data-persist-id="t1-c6"')
        cell_start = text.rindex("<td>", 0, start)
        cell_end = text.index("</td>", start) + len("</td>")
        CONTENT.write_text(text[:cell_start] + text[cell_end:], encoding="utf-8")
        self.rehash()
        self.assertCaught("a Task 1 row left with no writable mark cell",
                          "Task 1 table gives every row a writable mark cell")

    def test_stale_accessible_last_column_instruction(self):
        """The original defect: directions naming a Table 1a that does not exist."""
        self.mutate_content(
            "In the last column of <strong>Table 1</strong>, write <strong>OK</strong> if the record settles",
            "In the last column of Table 1a, write <strong>OK</strong> if the record settles")
        self.assertCaught("a stale Table 1a reference in the Accessible directions",
                          "no role names a table suffix that was never rendered")

    def test_stale_teacher_row_description(self):
        """The Teacher Guide must not describe a row split the learner table does not have."""
        self.mutate_content(
            "In Table 1 the first three rows are <strong>OK</strong>",
            "Every row is OK except the last two, and the first three rows are <strong>OK</strong>")
        self.assertCaught("a stale Teacher row description",
                          "Teacher Guide describes the six-row Task 1")

    def test_answer_key_structure_differs_from_learner_table(self):
        """The Answer Key must complete the table learners hold, not a different one."""
        self.mutate_content("Completed Table 1, in the order the learner editions print it",
                            "Completed rule-out")
        self.assertCaught("an Answer Key completing a differently shaped table",
                          "Answer Key completes the same six-row Task 1 table")

    # ── evidence availability ────────────────────────────────────────

    def test_required_150_hz_answer_without_learner_evidence(self):
        """Removing the Telluvian comparison from both learner editions must fail."""
        text = CONTENT.read_text(encoding="utf-8")
        text = text.replace(" — comparable Telluvian gardens report periodic signals at 100–150 Hz", "")
        text = text.replace(" — other Telluvian gardens report signals at 100–150 Hz", "")
        CONTENT.write_text(text, encoding="utf-8")
        self.rehash()
        self.assertCaught("a graded 100–150 Hz claim with no learner evidence",
                          "Answer Key reasons from")

    def test_evidence_present_in_only_one_learner_edition(self):
        """Evidence in the Student edition alone must not satisfy the check."""
        # The Student edition names the lyre-moth's wingbeat exactly once. Dropping it there
        # leaves the evidence in the Accessible edition alone, which is precisely what the
        # per-edition availability rule forbids.
        self.mutate_content("whose hovering wingbeat is measured strongest near 124 Hz",
                            "whose hovering flight is measured strongest near 124 Hz")
        self.assertCaught("evidence supplied to only one learner edition", "not just one of them")

    def test_required_specialist_vocabulary_without_a_definition(self):
        """Using a specialist term without defining it just in time must fail."""
        text = CONTENT.read_text(encoding="utf-8")
        text = text.replace("<tr><td>Poricidal anther</td><td>An anther that keeps its pollen inside and lets "
                            "it out only through small pores that are already open.</td></tr>", "")
        text = text.replace("<dt>Poricidal anther</dt><dd>An anther that holds its pollen in, and lets it out "
                            "only through small pores that are already open.</dd>", "")
        CONTENT.write_text(text, encoding="utf-8")
        self.rehash()
        self.assertCaught("a specialist term used but never defined for learners",
                          "poricidal anther is defined in the glossary of both learner editions")

    def test_teacher_only_enrichment_promoted_into_a_graded_answer(self):
        """A Teacher-only figure must not become a required student answer."""
        self.mutate_content("Completed Table 1, in the order the learner editions print it",
                            "Completed Table 1, ambient sound measured at 28 dB")
        self.assertCaught("Teacher-only enrichment promoted into the Answer Key",
                          "Teacher-only enrichment stays out of the graded requirements")

    # ── revision propagation ─────────────────────────────────────────

    def test_page_count_drift(self):
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        package["rolePageStructure"]["student"]["pageCount"] += 1
        PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        self.assertCaught("a declared page count drifting from the rendered document",
                          "declared role page counts match the rendered document")

    def test_figure_provenance_drift(self):
        registry = json.loads(REGISTRY.read_text(encoding="utf-8").split("=", 1)[1].rstrip().rstrip(";"))
        registry["figureProvenance"].append(
            {"id": "fig-factors", "kind": "curriculum-original inline SVG",
             "shows": "A figure the packet does not render.", "prohibited": "n/a"})
        REGISTRY.write_text("window.SSS_C2_CASE02_TASK_REGISTRY = "
                            + json.dumps(registry, indent=2, ensure_ascii=False) + ";\n", encoding="utf-8")
        self.rehash()
        self.assertCaught("a task registry declaring a figure the packet never renders",
                          "figure provenance names exactly the figures the packet renders")

    def test_version_drift_between_registry_and_content(self):
        self.mutate_content('data-editor-content="sss-c2-case02-v1.1"',
                            'data-editor-content="sss-c2-case02-v1.0"')
        self.assertCaught("a content editor key left at the superseded version",
                          "version is carried by every version-bearing package field")

    # ── lifecycle ────────────────────────────────────────────────────

    def test_release_without_its_own_release_record(self):
        """An approved package must name the release record that documents it."""
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        del package["releaseHistory"]
        PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        self.assertCaught("an approved package naming no release record",
                          "approved package names its own v1.2 release record")

    def test_print_gate_downgraded_after_approval(self):
        """The print gate is the whole point of the release; it cannot quietly regress."""
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        package["approval"]["printStatus"] = "NOT_RUN"
        PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        self.assertCaught("an approved package with the print gate downgraded",
                          "package records the approved corrective-release lifecycle")

    def test_prior_release_dropped_from_the_release_record(self):
        """Forgetting v1.0 in the v1.1 record would erase the only canonical index of it."""
        release = json.loads(RELEASE.read_text(encoding="utf-8"))
        release["priorApprovedReleases"] = []
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("the v1.0 prior release dropped from the v1.1 record",
                          "carries v1.0 as a canonical prior release")

    def test_v11_baseline_reverted_to_the_superseded_v10_markup(self):
        """The v1.1 baselines must not be satisfiable by the markup v1.1 replaced."""
        release = json.loads(RELEASE.read_text(encoding="utf-8"))
        release["frozenNonAccessibleDomBaselines"].update(
            release["priorApprovedReleases"][0]["frozenNonAccessibleDomBaselines"])
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("v1.1 baselines reverted to the superseded v1.0 markup",
                          "pins the live Student, Teacher and Answer Key DOM baselines")

    def test_release_record_hashes_drifting_from_the_package(self):
        """The release record must pin what was actually approved."""
        release = json.loads(RELEASE.read_text(encoding="utf-8"))
        release["sourceHashes"]["content"] = "0" * 64
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("a release record pinning a hash the package does not have",
                          "release record pins the approved source hashes")

    def test_retained_v10_record_deleted(self):
        """v1.0 is superseded, not withdrawn; its records stay."""
        original = RETAINED.read_bytes()
        self.addCleanup(lambda: RETAINED.write_bytes(original))
        RETAINED.unlink()
        self.assertCaught("the retained v1.0 release record deleted",
                          "retains exactly the v1.0, v1.1 and v1.2 history records")

    def test_retained_history_rewritten_to_describe_the_new_release(self):
        """The v1.0 record must not be edited to describe v1.1 content."""
        original = RETAINED.read_bytes()
        self.addCleanup(lambda: RETAINED.write_bytes(original))
        record = json.loads(RETAINED.read_text(encoding="utf-8"))
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        record["sourceHashes"]["content"] = package["sourceHashes"]["content"]
        record["sourceHashes"]["taskRegistry"] = package["sourceHashes"]["taskRegistry"]
        RETAINED.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        self.assertCaught("the retained v1.0 record rewritten to describe v1.1 content",
                          "was not rewritten to describe v1.2 content")

    # ── standards ────────────────────────────────────────────────────

    def test_reinstated_standard_overclaim(self):
        self.mutate_content("Standards: NGSS MS-LS1-4; MS-ETS1-1; MS-PS4-1",
                            "Standards: NGSS MS-LS1-4; MS-ETS1-1; MS-LS2-2; MS-PS4-1")
        self.assertCaught("a reinstated MS-LS2-2 overclaim",
                          "no role advertises a standard the packet no longer claims")


if __name__ == "__main__":
    unittest.main(verbosity=2)
