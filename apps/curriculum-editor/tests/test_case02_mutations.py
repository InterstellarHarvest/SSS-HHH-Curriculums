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
SOURCE = ROOT / "sss/campaign-2/case-02-missing-dance/source"
CONTENT = SOURCE / "content.html"
REGISTRY = SOURCE / "task-registry.js"
PACKAGE = SOURCE / "case-package.json"
VALIDATOR = ROOT / "apps/curriculum-editor/tests/validate_case02_campaign2.py"
TRACKED = (CONTENT, REGISTRY, PACKAGE)


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


class Case02Mutations(unittest.TestCase):
    """Every test mutates real sources, so restoration is unconditional."""

    def setUp(self):
        self.original = {path: path.read_bytes() for path in TRACKED}
        self.addCleanup(self.restore)
        passed, failures = validator_result()
        self.assertTrue(passed, f"baseline must be green before mutating; failures: {failures}")

    def restore(self):
        for path, body in self.original.items():
            path.write_bytes(body)

    def rehash(self):
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        import hashlib
        for key, name in (("content", "content.html"), ("taskRegistry", "task-registry.js")):
            package["sourceHashes"][key] = hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
        PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")

    def mutate_content(self, old: str, new: str, count: int = 1):
        text = CONTENT.read_text(encoding="utf-8")
        self.assertEqual(text.count(old), count, f"mutation anchor not unique: {old[:60]!r}")
        CONTENT.write_text(text.replace(old, new), encoding="utf-8")
        self.rehash()

    def assertCaught(self, label: str):
        passed, failures = validator_result()
        self.assertFalse(passed, f"{label} was NOT caught by validation")
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
        self.assertCaught("a Task 1 row left with no writable mark cell")

    def test_stale_accessible_last_column_instruction(self):
        """The original defect: directions naming a Table 1a that does not exist."""
        self.mutate_content(
            "In the last column of <strong>Table 1</strong>, write <strong>OK</strong> if the record settles",
            "In the last column of Table 1a, write <strong>OK</strong> if the record settles")
        self.assertCaught("a stale Table 1a reference in the Accessible directions")

    def test_stale_teacher_row_description(self):
        """The Teacher Guide must not describe a row split the learner table does not have."""
        self.mutate_content(
            "In Table 1 the first three rows are <strong>OK</strong>",
            "Every row is OK except the last two, and the first three rows are <strong>OK</strong>")
        self.assertCaught("a stale Teacher row description")

    def test_answer_key_structure_differs_from_learner_table(self):
        """The Answer Key must complete the table learners hold, not a different one."""
        self.mutate_content("Completed Table 1, in the order the learner editions print it",
                            "Completed rule-out")
        self.assertCaught("an Answer Key completing a differently shaped table")

    # ── evidence availability ────────────────────────────────────────

    def test_required_150_hz_answer_without_learner_evidence(self):
        """Removing the Telluvian comparison from both learner editions must fail."""
        text = CONTENT.read_text(encoding="utf-8")
        text = text.replace(" — comparable Telluvian gardens report periodic signals at 100–150 Hz", "")
        text = text.replace(" — other Telluvian gardens report signals at 100–150 Hz", "")
        CONTENT.write_text(text, encoding="utf-8")
        self.rehash()
        failures = self.assertCaught("a graded 100–150 Hz claim with no learner evidence")
        self.assertTrue(any("Answer Key reasons from" in f for f in failures), failures)

    def test_evidence_present_in_only_one_learner_edition(self):
        """Evidence in the Student edition alone must not satisfy the check."""
        self.mutate_content("Says how buzz pollination gets pollen out of a poricidal anther, and that the "
                            "pollinator is the Telluvian lyre-moth. Its hovering wingbeat is strongest near 124 Hz.",
                            "Says how vibration gets pollen out of pores already there.")
        failures = self.assertCaught("evidence supplied to only one learner edition")
        self.assertTrue(any("not just one of them" in f for f in failures), failures)

    def test_required_specialist_vocabulary_without_a_definition(self):
        """Using a specialist term without defining it just in time must fail."""
        text = CONTENT.read_text(encoding="utf-8")
        text = text.replace("<tr><td>Poricidal anther</td><td>An anther that keeps its pollen inside and lets "
                            "it out only through small pores that are already open.</td></tr>", "")
        text = text.replace("<dt>Poricidal anther</dt><dd>An anther that holds its pollen in, and lets it out "
                            "only through small pores that are already open.</dd>", "")
        CONTENT.write_text(text, encoding="utf-8")
        self.rehash()
        self.assertCaught("a specialist term used but never defined for learners")

    def test_teacher_only_enrichment_promoted_into_a_graded_answer(self):
        """A Teacher-only figure must not become a required student answer."""
        self.mutate_content("Completed Table 1, in the order the learner editions print it",
                            "Completed Table 1, ambient sound measured at 28 dB")
        self.assertCaught("Teacher-only enrichment promoted into the Answer Key")

    # ── revision propagation ─────────────────────────────────────────

    def test_page_count_drift(self):
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        package["rolePageStructure"]["student"]["pageCount"] += 1
        PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        self.assertCaught("a declared page count drifting from the rendered document")

    def test_figure_provenance_drift(self):
        registry = json.loads(REGISTRY.read_text(encoding="utf-8").split("=", 1)[1].rstrip().rstrip(";"))
        registry["figureProvenance"].append(
            {"id": "fig-factors", "kind": "curriculum-original inline SVG",
             "shows": "A figure the packet does not render.", "prohibited": "n/a"})
        REGISTRY.write_text("window.SSS_C2_CASE02_TASK_REGISTRY = "
                            + json.dumps(registry, indent=2, ensure_ascii=False) + ";\n", encoding="utf-8")
        self.rehash()
        self.assertCaught("a task registry declaring a figure the packet never renders")

    def test_version_drift_between_registry_and_content(self):
        self.mutate_content('data-editor-content="sss-c2-case02-v1.1"',
                            'data-editor-content="sss-c2-case02-v1.0"')
        self.assertCaught("a content editor key left at the superseded version")

    # ── lifecycle ────────────────────────────────────────────────────

    def test_candidate_claiming_a_release_record_of_its_own(self):
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        package["releaseHistory"] = "sss/campaign-2/case-02-missing-dance/history/release-v1.1.json"
        PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        self.assertCaught("a candidate declaring a release record of its own")

    def test_candidate_claiming_approval(self):
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        package["approval"] = {"date": "2026-08-05", "owner": "Nate / Owner",
                               "status": "APPROVED", "printStatus": "PASS"}
        PACKAGE.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        self.assertCaught("a candidate claiming approval and a print pass")

    def test_retained_history_rewritten_to_describe_the_candidate(self):
        """The v1.0 record must not be edited to describe v1.1 content."""
        history = ROOT / "sss/campaign-2/case-02-missing-dance/history/release-v1.0.json"
        original = history.read_bytes()
        self.addCleanup(lambda: history.write_bytes(original))
        record = json.loads(history.read_text(encoding="utf-8"))
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        record["sourceHashes"]["content"] = package["sourceHashes"]["content"]
        record["sourceHashes"]["taskRegistry"] = package["sourceHashes"]["taskRegistry"]
        history.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        self.assertCaught("the retained v1.0 record rewritten to describe v1.1 content")

    # ── standards ────────────────────────────────────────────────────

    def test_reinstated_standard_overclaim(self):
        self.mutate_content("Standards: NGSS MS-LS1-4; MS-ETS1-1; MS-PS4-1",
                            "Standards: NGSS MS-LS1-4; MS-ETS1-1; MS-LS2-2; MS-PS4-1")
        self.assertCaught("a reinstated MS-LS2-2 overclaim")


if __name__ == "__main__":
    unittest.main(verbosity=2)
