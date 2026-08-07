#!/usr/bin/env python3
"""Mutation tests for the Campaign 2 Case 05 protections.

Each mutation reproduces a defect the Campaign 2 completion audit found inside the released
v1.0 package — or one this remediation found independently — injects it into the working
sources, and asserts that ``validate_case05_campaign2.py`` fails *for the intended reason*.
Sources are always restored, including when a test fails, so the tree is left exactly as it
was found.

A protection that cannot be made to fail is not a protection, and a protection that fires only
through a hash check is not the protection it claims to be. Every mutation therefore re-pins
the package hashes before validating, and names the single assertion it must trip.
``assert_trips`` additionally rejects a run whose only failures are the hash or lifecycle
plumbing, so a mutation can never be scored as caught by drift.

Case 05 is the unreleased v1.1 corrective candidate, so it carries no release record and no
frozen DOM baseline; re-pinning the four package hashes is enough to isolate the content
protections from the integrity plumbing.
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
CASE_ROOT = ROOT / "sss/campaign-2/case-05-too-clean-room"
SOURCE = CASE_ROOT / "source"
CONTENT = SOURCE / "content.html"
REGISTRY = SOURCE / "task-registry.js"
PACKAGE = SOURCE / "case-package.json"
README = CASE_ROOT / "README.md"
RETAINED_RELEASE = CASE_ROOT / "history/release-v1.0.json"
RETAINED_APPROVAL = CASE_ROOT / "history/CASE05_OWNER_APPROVAL_v1.0.md"
VALIDATOR = ROOT / "apps/curriculum-editor/tests/validate_case05_campaign2.py"
TRACKED = (CONTENT, REGISTRY, PACKAGE, README, RETAINED_RELEASE, RETAINED_APPROVAL)

# Failures that mean "something moved", not "the protection fired". A mutation whose only
# effect is one of these has not proved anything.
PLUMBING = {
    "package source hashes verify",
    "the shared corrective-release lifecycle rules are satisfied",
    "the package certifies all four sources, including layoutOverrides",
    "both retained v1.0 records are byte-identical to synchronised main",
}


def validator_result() -> tuple[bool, list[str]]:
    """Run the Case 05 validator and return (passed, failing assertion names)."""
    run = subprocess.run([sys.executable, str(VALIDATOR)], cwd=ROOT, text=True,
                         capture_output=True)
    try:
        payload = json.loads(run.stdout[run.stdout.index("{"):])
    except (ValueError, json.JSONDecodeError):
        return False, ["validator crashed"]
    return run.returncode == 0, [a["name"] for a in payload["assertions"] if not a["pass"]]


class Case05Mutations(unittest.TestCase):
    """Every test mutates real sources, so restoration is unconditional."""

    def setUp(self):
        self.original = {path: path.read_bytes() for path in TRACKED}
        self.addCleanup(self.restore)
        passed, failures = validator_result()
        self.assertTrue(passed, f"baseline must be green before mutating; failures: {failures}")

    def restore(self):
        for path, body in self.original.items():
            path.write_bytes(body)

    # ── helpers ──────────────────────────────────────────────────────────────

    def rehash(self):
        """Re-pin the four package hashes a mutation would otherwise trip incidentally."""
        digests = {key: hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
                   for key, name in (("content", "content.html"),
                                     ("presentation", "presentation.css"),
                                     ("taskRegistry", "task-registry.js"),
                                     ("layoutOverrides", "layout-overrides.json"))}
        text = PACKAGE.read_text(encoding="utf-8")
        for key, digest in digests.items():
            text = re.sub(rf'("{key}": ")[0-9a-f]{{64}}(")', rf"\g<1>{digest}\g<2>", text, count=1)
        PACKAGE.write_text(text, encoding="utf-8")

    def edit(self, path: Path, old: str, new: str, count: int = 1):
        body = path.read_text(encoding="utf-8")
        self.assertEqual(body.count(old), count,
                         f"mutation anchor not unique in {path.name}: {old[:70]!r}")
        path.write_text(body.replace(old, new), encoding="utf-8")
        self.rehash()

    def assert_trips(self, assertion: str):
        passed, failures = validator_result()
        self.assertFalse(passed, "the mutation must not validate")
        self.assertIn(assertion, failures,
                      f"expected {assertion!r} to fail; actual failures: {failures}")
        self.assertTrue(set(failures) - (PLUMBING - {assertion}),
                        "the mutation was caught only by hash or lifecycle plumbing")

    # ── 1-3 · printable prose corruption (audit M-24) ────────────────────────

    def test_the_bare_x_is_restored(self):
        """The v1.0 defect verbatim: a bare `X` standing where a clause belongs."""
        self.edit(CONTENT,
                  "Tasks 4–7 in the second. Task 6 occupies a full page of its own in both "
                  "learner editions, so the explanation is written in one sitting",
                  "Tasks 4–7 in the second. X so the explanation is written in one sitting")
        self.assert_trips("no Teacher paragraph carries a bare placeholder token where "
                          "prose belongs")

    def test_the_repaired_clause_becomes_another_placeholder(self):
        """Any production marker in the same slot must fail, not only the letter X."""
        self.edit(CONTENT,
                  "Task 6 occupies a full page of its own in both learner editions, so the "
                  "explanation is written in one sitting",
                  "TODO so the explanation is written in one sitting")
        self.assert_trips("no Teacher paragraph carries a bare placeholder token where "
                          "prose belongs")

    def test_the_repaired_clause_is_silently_reworded(self):
        """The repaired sentence is pinned, so it cannot drift back to something weaker."""
        self.edit(CONTENT,
                  "Task 6 occupies a full page of its own in both learner editions, so the "
                  "explanation is written in one sitting",
                  "Keep them together so the explanation is written in one sitting")
        self.assert_trips("the repaired Teacher pacing clause is present and unmodified")

    def test_a_teacher_paragraph_is_truncated(self):
        """A sentence that stops mid-clause is the same corruption class as the bare X."""
        self.edit(CONTENT,
                  "Students who have played the case will recognise the five sources; "
                  "students who have not can work entirely from the printed records.",
                  "Students who have played the case will recognise the five sources; "
                  "students who have not can")
        self.assert_trips("every Teacher paragraph ends in terminal punctuation")

    # ── 4-5 · Teacher completeness ───────────────────────────────────────────

    def test_a_teacher_task_guidance_block_is_deleted(self):
        """Task 4's guidance removed: the audit's Case 01 M-7 defect class."""
        body = CONTENT.read_text(encoding="utf-8")
        start = body.index("<h3>Task 4 · Convergence, and the limit column</h3>")
        end = body.index("</p>", start) + len("</p>")
        CONTENT.write_text(body[:start] + body[end:], encoding="utf-8")
        self.rehash()
        self.assert_trips("every task receives a named Teacher guidance block")

    def test_a_stale_task_reference_is_introduced(self):
        """Case 05 has seven tasks; a guide that names Task 8 describes a case it is not."""
        self.edit(CONTENT,
                  "Tasks 1–3 sit naturally in the first, Tasks 4–7 in the second.",
                  "Tasks 1–3 sit naturally in the first, Tasks 4–8 in the second.")
        self.assert_trips("no Teacher task reference points past the seven tasks the case has")

    # ── 6-8 · evidence availability ──────────────────────────────────────────

    def test_accessible_rejection_evidence_is_removed(self):
        """The v1.0 defect: the Accessible word bank offered evidence the edition lacked."""
        self.edit(CONTENT,
                  "The cells are healthy and nutrient uptake is normal.",
                  "The cells are healthy.")
        self.assert_trips("every Accessible word-bank phrase has its evidence printed "
                          "outside the bank")

    def test_answer_key_requires_evidence_absent_from_student(self):
        """A graded quantity no Student edition prints must fail."""
        self.edit(CONTENT,
                  "Production fell from 100% to 6% of baseline across months 3 to 6.",
                  "Production fell from 100% to 6% of baseline, a fall of 47% per month, "
                  "across months 3 to 6.")
        self.assert_trips("every quantity the Answer Key reports is printed in both "
                          "learner editions")

    def test_answer_key_requires_evidence_absent_from_accessible(self):
        """The v1.0 defect: constraints accepted at Task 7 that neither edition prints."""
        self.edit(CONTENT,
                  "the stop criteria must be written down before the trial starts;",
                  "staff exposure limits apply and only a small number of specimens exist;")
        self.assert_trips("the Answer Key accepts no constraint absent from a learner edition")

    def test_the_accessible_stakes_sentence_is_removed(self):
        """Removing it strands the impacts-on-people evidence the direct standard rests on."""
        self.edit(CONTENT,
                  " The medicine treats a disease that affects several Concord species, "
                  "and supplies are running out.",
                  "")
        self.assert_trips("the Accessible briefing carries the stakes the direct standard "
                          "rests on")

    # ── 9 · standards ────────────────────────────────────────────────────────

    def test_a_supporting_standard_is_overclaimed_as_direct(self):
        """MS-LS1-5 is bounded by the packet's own assessment-boundary note."""
        self.edit(REGISTRY, '"code": "MS-LS1-5",\n      "claim": "supporting",',
                  '"code": "MS-LS1-5",\n      "claim": "direct",')
        self.assert_trips("the registry claims exactly the three current standards at their "
                          "current strength")

    def test_a_standards_claim_loses_its_limitation(self):
        """A claim with no stated limitation is an overclaim waiting to be reported."""
        registry = REGISTRY.read_text(encoding="utf-8")
        start = registry.index('"code": "MS-ETS1-2"')
        limitation = registry.index('"limitation":', start)
        end = registry.index('\n', registry.index('"', registry.index(':', limitation) + 2) + 1)
        REGISTRY.write_text(registry[:limitation] + '"limitation": ""' + registry[end:],
                            encoding="utf-8")
        self.rehash()
        self.assert_trips("every standards claim names a practice, a real task, and a limitation")

    # ── 10 · cross-role reference integrity (audit M-26 class) ───────────────

    def test_a_cross_role_table_reference_is_broken(self):
        """Renumbering one edition's table strands every reference that names it."""
        self.edit(CONTENT, "<caption>Table 4 · Changes the vault already tried</caption>",
                  "<caption>Table 8 · Changes the vault already tried</caption>")
        self.assert_trips("the two learner editions number the same tables and figures")

    def test_a_teacher_reference_names_a_table_no_learner_holds(self):
        """A Teacher prose reference must resolve in the edition the reader actually holds."""
        self.edit(CONTENT, "Tables 1–7 are case records.", "Tables 1–9 are case records.")
        self.assert_trips("every table and figure a Teacher or Answer Key prose reference "
                          "names resolves in both learner editions")

    # ── 11 · Accessible structural contracts ─────────────────────────────────

    def test_an_accessible_scaffold_block_is_dropped(self):
        """Nine scaffold blocks is the contract, not a floor."""
        body = CONTENT.read_text(encoding="utf-8")
        start = body.index('<div class="alt-support">Sentence frame: “The report only checks')
        end = body.index("</div>", start) + len("</div>")
        CONTENT.write_text(body[:start] + body[end:], encoding="utf-8")
        self.rehash()
        self.assert_trips("the Accessible edition carries exactly its nine scaffold blocks")

    # ── 12-13 · frozen history and record-to-commit certification ────────────

    def test_the_v10_release_record_is_rewritten_while_the_candidate_is_open(self):
        """Frozen history may never be edited to describe the version replacing it."""
        record = json.loads(RETAINED_RELEASE.read_text(encoding="utf-8"))
        record["curriculumVersion"] = "1.1"
        record["acceptedValidation"]["case05Scoped"] = "143/143"
        RETAINED_RELEASE.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n",
                                    encoding="utf-8")
        passed, failures = validator_result()
        self.assertFalse(passed, "rewriting frozen history must not validate")
        self.assertIn("both retained v1.0 records are byte-identical to synchronised main",
                      failures, f"actual failures: {failures}")

    def test_the_v10_source_pin_is_quietly_corrected_in_place(self):
        """The false pin is frozen history; correcting it in place must be caught, not silent."""
        self.edit(RETAINED_RELEASE,
                  '"canonicalSourceApprovalCommit": "5c1453328ac40a7f7a653efa18ef70bf73759f69"',
                  '"canonicalSourceApprovalCommit": "7f07ccb37c6ece9dace3ffe4487cff21a2f8030a"')
        self.assert_trips("the v1.0 canonicalSourceApprovalCommit is still the "
                          "known-inaccurate pin")

    # ── 14 · candidate lifecycle ─────────────────────────────────────────────

    def test_a_v11_release_record_is_created_before_approval(self):
        """An unreleased candidate may never carry a record for its own version."""
        (CASE_ROOT / "history/release-v1.1.json").write_text(
            json.dumps({"schemaVersion": 1, "caseId": "SSS-C2-CASE05",
                        "curriculumVersion": "1.1", "status": "APPROVED_STABLE"}, indent=2) + "\n",
            encoding="utf-8")
        self.addCleanup(lambda: (CASE_ROOT / "history/release-v1.1.json").unlink(missing_ok=True))
        passed, failures = validator_result()
        self.assertFalse(passed, "an unapproved v1.1 record must not validate")
        self.assertIn("history holds the retained v1.0 records only and no v1.1 record",
                      failures, f"actual failures: {failures}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
