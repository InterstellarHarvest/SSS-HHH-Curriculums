#!/usr/bin/env python3
"""Mutation tests for the Campaign 2 Case 03 protections.

Each mutation reproduces a defect the Campaign 2 completion audit found in the
released v1.0 package, injects it into the working sources, and asserts that
``validate_case03_campaign2.py`` fails *for the intended reason*. Sources are
always restored, including when a test fails, so the tree is left exactly as it
was found.

A protection that cannot be made to fail is not a protection, and a protection
that fires only through a hash check or a frozen DOM baseline is not the
protection it claims to be. Every mutation therefore re-pins the source hashes
before validating and names the assertion it must trip.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[3]
CASE_ROOT = ROOT / "sss/campaign-2/case-03-wrong-color-light"
SOURCE = CASE_ROOT / "source"
CONTENT = SOURCE / "content.html"
REGISTRY = SOURCE / "task-registry.js"
PACKAGE = SOURCE / "case-package.json"
README = CASE_ROOT / "README.md"
RELEASE = CASE_ROOT / "history/release-v1.1.json"
RETAINED = CASE_ROOT / "history/release-v1.0.json"
VALIDATOR = ROOT / "apps/curriculum-editor/tests/validate_case03_campaign2.py"
TRACKED = (CONTENT, REGISTRY, PACKAGE, README, RELEASE)

INVERTED = "total PAR alone proves no effective spectrum"
CANONICAL = "total PAR alone does not establish an effective spectrum"


def validator_result() -> tuple[bool, list[str]]:
    """Run the Case 03 validator and return (passed, failing assertion names)."""
    run = subprocess.run([sys.executable, str(VALIDATOR)], cwd=ROOT, text=True, capture_output=True)
    try:
        payload = json.loads(run.stdout[run.stdout.index("{"):])
    except (ValueError, json.JSONDecodeError):
        # A crash is also a failure to validate, which is what we assert on.
        return False, ["validator crashed"]
    return run.returncode == 0, [a["name"] for a in payload["assertions"] if not a["pass"]]


class Case03Mutations(unittest.TestCase):
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
        """Re-pin every hash and baseline a mutation would otherwise trip incidentally.

        Case 03 is now a frozen release, so a content edit is caught by the package hash,
        the release-record hash and the release-record DOM baseline before any content
        detector runs. Re-pinning all three is what makes these tests prove the content
        protections rather than the integrity plumbing.
        """
        from bs4 import BeautifulSoup, NavigableString

        def role_dom_hash(soup, role):
            fragment = BeautifulSoup(
                "".join(str(page) for page in soup.select(f'.page[data-role="{role}"]')),
                "html.parser")
            for node in list(fragment.find_all(string=True)):
                if isinstance(node, NavigableString) and not str(node).strip():
                    node.extract()
            return hashlib.sha256(fragment.decode(formatter="minimal").encode("utf-8")).hexdigest()

        digests = {key: hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
                   for key, name in (("content", "content.html"),
                                     ("taskRegistry", "task-registry.js"))}
        text = PACKAGE.read_text(encoding="utf-8")
        for key, digest in digests.items():
            text = re.sub(rf'("{key}": ")[0-9a-f]{{64}}(")', rf"\g<1>{digest}\g<2>", text, count=1)
        PACKAGE.write_text(text, encoding="utf-8")

        release = json.loads(RELEASE.read_text(encoding="utf-8"))
        release["sourceHashes"].update(digests)
        soup = BeautifulSoup(CONTENT.read_text(encoding="utf-8"), "html.parser")
        for role in ("student", "teacher", "answer"):
            release["frozenNonAccessibleDomBaselines"][role] = role_dom_hash(soup, role)
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def mutate_content(self, old: str, new: str, count: int = 1):
        text = CONTENT.read_text(encoding="utf-8")
        self.assertEqual(text.count(old), count, f"mutation anchor not unique: {old[:70]!r}")
        CONTENT.write_text(text.replace(old, new), encoding="utf-8")
        self.rehash()

    def assertCaught(self, label: str, expect: str):
        passed, failures = validator_result()
        self.assertFalse(passed, f"{label} was NOT caught by validation")
        self.assertTrue(any(expect in name for name in failures),
                        f"{label} failed validation, but not via {expect!r}; got: {failures}")
        return failures

    # ── 1-2. the released inversion, whole and by half ───────────────

    def test_inverted_rule_restored_in_both_learner_editions(self):
        """The released defect: learner editions printing the inverse of the packet's rule."""
        self.mutate_content(CANONICAL, INVERTED, 6)
        failures = self.assertCaught("the inverted total-PAR rule restored in both learner editions",
                                     "no role inverts the total-PAR reasoning rule")
        self.assertTrue(any("every role states the same total-PAR reasoning rule" in name
                            for name in failures), failures)

    def test_only_one_learner_edition_states_the_rule(self):
        """Correcting one learner edition and not the other must not satisfy parity."""
        text = CONTENT.read_text(encoding="utf-8")
        student = text.index('data-role="student"')
        accessible = text.index('data-role="accessible"', student)
        head, tail = text[:accessible], text[accessible:]
        self.assertEqual(tail.count(CANONICAL), 2, "expected the rule twice in the Accessible edition")
        CONTENT.write_text(head + tail.replace(CANONICAL, INVERTED), encoding="utf-8")
        self.rehash()
        self.assertCaught("the rule corrected in only one learner edition",
                          "both learner editions state that rule, not just one of them")

    # ── 3-4. the Task 1 controlling evidence, per edition ────────────

    def test_task1_change_record_removed_from_student(self):
        """Task 1 grades a classification; without the record the Student cannot answer it."""
        text = CONTENT.read_text(encoding="utf-8")
        student = text.index('data-role="student"')
        accessible = text.index('data-role="accessible"', student)
        head, tail = text[:accessible], text[accessible:]
        stripped = re.sub(r'<span data-change-record="[^"]*">.*?</span>', "", head, flags=re.S)
        self.assertNotEqual(stripped, head, "no Student change record found to remove")
        CONTENT.write_text(stripped + tail, encoding="utf-8")
        self.rehash()
        self.assertCaught("the Task 1 change record removed from the Student edition",
                          "the student edition prints the Week 0 change record on or before Task 1")

    def test_task1_change_record_removed_from_accessible(self):
        """The same removal in the differentiated edition must fail independently."""
        text = CONTENT.read_text(encoding="utf-8")
        accessible = text.index('data-role="accessible"')
        head, tail = text[:accessible], text[accessible:]
        stripped = re.sub(r'<span data-change-record="[^"]*">.*?</span>', "", tail, flags=re.S)
        self.assertNotEqual(stripped, tail, "no Accessible change record found to remove")
        CONTENT.write_text(head + stripped, encoding="utf-8")
        self.rehash()
        self.assertCaught("the Task 1 change record removed from the Accessible edition",
                          "the accessible edition prints the Week 0 change record on or before Task 1")

    # ── 5. runtime-only evidence promoted into a graded answer ───────

    def test_answer_key_requires_the_runtime_only_photon_flux(self):
        """The released Answer Key reasoned from a 30%-higher flux no learner role prints."""
        self.mutate_content(
            "Total PAR is 280 µmol/m²/s and is reported adequate (Table 1)",
            "Total PAR is 280 µmol/m²/s and is reported adequate, and the case reports the "
            "installed total photon flux as 30% higher than the retired fixture’s")
        self.assertCaught("a graded Answer Key claim resting on runtime-only evidence",
                          "runtime-only and Teacher-only enrichment stays out of the graded requirements")

    def test_answer_key_evidence_removed_from_a_learner_edition(self):
        """A value the Answer Key reasons from must survive in both learner editions."""
        text = CONTENT.read_text(encoding="utf-8")
        accessible = text.index('data-role="accessible"')
        head, tail = text[:accessible], text[accessible:]
        CONTENT.write_text(head + tail.replace("460–540 nm", "the measured band"), encoding="utf-8")
        self.rehash()
        self.assertCaught("Answer Key evidence removed from the Accessible edition",
                          "every fact the Answer Key reasons from is printed in both learner editions")

    # ── 6. the invented provenance ───────────────────────────────────

    def test_unsupported_weighting_model_provenance_restored(self):
        """The canonical source states the value and nothing about how it was obtained."""
        self.mutate_content(
            "The investigation reports approximately that value and does not report how it was obtained.",
            "The investigation reports that figure as an approximation from an incomplete weighting model.")
        self.assertCaught("the unsupported weighting-model provenance restored in the Teacher Guide",
                          "the approximate effective-PAR value carries no unsupported model provenance")

    def test_unsupported_provenance_restored_in_the_task_registry(self):
        """The ledger of record must not carry the provenance the printable roles dropped."""
        text = REGISTRY.read_text(encoding="utf-8")
        old = "The runtime reports this value as approximate and does not report how it was obtained."
        self.assertEqual(text.count(old), 1)
        REGISTRY.write_text(text.replace(old, "The runtime reports this as an estimate from an "
                                              "incomplete weighting model."), encoding="utf-8")
        self.rehash()
        self.assertCaught("the unsupported provenance restored in the task registry",
                          "the approximate effective-PAR value carries no unsupported model provenance")

    # ── 7. the withdrawn standard ────────────────────────────────────

    def test_ms_ps4_2_restored_as_a_direct_standard(self):
        """MS-PS4-2 may not return while no task develops or uses the missing model."""
        self.mutate_content(
            "<p><strong>Supporting alignment: MS-ETS1-1.</strong>",
            "<p><strong>Direct assessment: MS-PS4-2.</strong> Students use a model of "
            "wavelength-dependent absorption and transmission.</p>"
            "<p><strong>Supporting alignment: MS-ETS1-1.</strong>")
        self.assertCaught("MS-PS4-2 restored as a direct standard",
                          "no withdrawn standard returns as a direct or supporting claim")

    def test_a_claimed_standard_that_names_no_assessing_task(self):
        """Every claimed standard must name the task that carries it."""
        self.mutate_content(
            "<p><strong>Supporting alignment: MS-ETS1-1.</strong> Task 8 defines a spectral criterion,"
            " an intensity criterion, and one constraint with enough precision to guide a solution."
            " It is supporting rather than direct because the Student task sets no impacts-on-people"
            " expectation.</p>",
            "<p><strong>Supporting alignment: MS-ETS1-1.</strong> The packet is supporting rather than"
            " direct for this expectation.</p>")
        self.assertCaught("a claimed standard naming no assessing task",
                          "every claimed standard names at least one assessing task")

    # ── 8-9. the case's approved science protections ─────────────────

    def test_exact_effective_par_calculation_introduced(self):
        """The approximate value must never become a student calculation."""
        self.mutate_content(
            "<span class=\"response-label\">Why timing alone is not enough</span>",
            "<span class=\"response-label\">Calculate the effective PAR for the kelp from the "
            "reported categories</span>", 2)
        self.assertCaught("an exact effective-PAR calculation asked of students",
                          "no printable role asserts a prohibited scientific overstatement")

    def test_zero_response_outside_the_measured_band_introduced(self):
        """Response outside 460–540 nm is unspecified, not zero."""
        self.mutate_content(
            "Response outside the marked band is not specified and is not zero.",
            "Response outside the marked band is zero response outside the measured range.", 2)
        self.assertCaught("a zero-response claim outside the measured band",
                          "no printable role asserts a prohibited scientific overstatement")

    # ── revision propagation and lifecycle ───────────────────────────

    def test_page_count_drift(self):
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        package["rolePageStructure"]["student"]["pageCount"] += 1
        PACKAGE.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("a declared page count drifting from the rendered document",
                          "declared role page counts match the rendered document")

    def test_content_editor_key_left_at_the_superseded_version(self):
        self.mutate_content('data-editor-content="sss-c2-case03-v1.1"',
                            'data-editor-content="sss-c2-case03-v1.0"')
        self.assertCaught("a content editor key left at the superseded version",
                          "agree on the version")

    def test_release_without_its_own_release_record(self):
        """An approved package must name the release record that documents it."""
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        del package["releaseHistory"]
        PACKAGE.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("an approved package naming no release record",
                          "the approved package names its own v1.1 release record")

    def test_print_gate_downgraded_after_approval(self):
        """The print gate is the whole point of the release; it cannot quietly regress."""
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        package["approval"]["printStatus"] = "NOT_RUN"
        PACKAGE.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("an approved package with the print gate downgraded",
                          "the package records the approved corrective-release lifecycle")

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

    def test_certified_source_commit_does_not_contain_the_certified_registry(self):
        """The audit's M-10/M-18 defect: a pin that does not contain what it certifies."""
        release = json.loads(RELEASE.read_text(encoding="utf-8"))
        release["canonicalSourceApprovalCommit"] = release["originalReleaseApprovalCommit"]
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("a certified-source pin that does not contain the certified sources",
                          "the certified source commit actually contains the sources the record pins")

    def test_v10_game_pin_rewritten_in_the_prior_release_entry(self):
        """v1.0's baseline is historical evidence and must not be normalised to v1.1's."""
        release = json.loads(RELEASE.read_text(encoding="utf-8"))
        prior = release["priorApprovedReleases"][0]
        prior["notes"] = [note.replace("46b9387bca95736f164f905596e3dd8b13968661",
                                       "29c3b222c53f51de11a3aa83e896a6d0ef6fb490")
                          for note in prior["notes"]]
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("v1.0's game pin rewritten to v1.1's",
                          "preserves v1.0's own game pin rather than rewriting it")

    def test_retained_v10_record_deleted(self):
        """v1.0 is superseded, not withdrawn; its records stay."""
        original = RETAINED.read_bytes()
        self.addCleanup(lambda: RETAINED.write_bytes(original))
        RETAINED.unlink()
        self.assertCaught("the retained v1.0 release record deleted",
                          "retains exactly the v1.0 and v1.1 history records")

    def test_retained_v10_record_rewritten_to_describe_v11(self):
        retained = RETAINED
        original = retained.read_bytes()
        self.addCleanup(lambda: retained.write_bytes(original))
        record = json.loads(retained.read_text(encoding="utf-8"))
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        record["sourceHashes"]["content"] = package["sourceHashes"]["content"]
        record["sourceHashes"]["taskRegistry"] = package["sourceHashes"]["taskRegistry"]
        retained.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.assertCaught("the retained v1.0 record rewritten to describe v1.1 content",
                          "was not rewritten to describe v1.1 content")


if __name__ == "__main__":
    unittest.main(verbosity=2)
