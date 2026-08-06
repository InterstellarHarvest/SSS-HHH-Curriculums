#!/usr/bin/env python3
"""Mutation tests for the Campaign 2 Case 06 protections.

Each mutation reproduces a defect the Campaign 2 completion audit found in the
released v1.0 package, injects it into the working sources, and asserts that
``validate_case06_campaign2.py`` fails *for the intended reason*. Sources are
always restored, including when a test fails, so the tree is left exactly as it
was found.

A protection that cannot be made to fail is not a protection, and a protection
that fires only through a hash check is not the protection it claims to be.
Every mutation therefore re-pins the package hashes before validating, and names
the assertion it must trip. Case 06 is an unreleased corrective candidate, so it
has no release record and no frozen DOM baseline to re-pin, and nothing but the
content protections stands between a mutation and a green suite.
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
CASE_ROOT = ROOT / "sss/campaign-2/case-06-first-garden"
SOURCE = CASE_ROOT / "source"
CONTENT = SOURCE / "content.html"
REGISTRY = SOURCE / "task-registry.js"
PACKAGE = SOURCE / "case-package.json"
README = CASE_ROOT / "README.md"
VALIDATOR = ROOT / "apps/curriculum-editor/tests/validate_case06_campaign2.py"
TRACKED = (CONTENT, REGISTRY, PACKAGE, README)


def validator_result() -> tuple[bool, list[str]]:
    """Run the Case 06 validator and return (passed, failing assertion names)."""
    run = subprocess.run([sys.executable, str(VALIDATOR)], cwd=ROOT, text=True, capture_output=True)
    try:
        payload = json.loads(run.stdout[run.stdout.index("{"):])
    except (ValueError, json.JSONDecodeError):
        return False, ["validator crashed"]
    return run.returncode == 0, [a["name"] for a in payload["assertions"] if not a["pass"]]


class Case06Mutations(unittest.TestCase):
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
        """Re-pin the package hashes a content edit would otherwise trip first."""
        text = PACKAGE.read_text(encoding="utf-8")
        for key, name in (("content", "content.html"), ("taskRegistry", "task-registry.js")):
            digest = hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
            text = re.sub(rf'("{key}": ")[0-9a-f]{{64}}(")', rf"\g<1>{digest}\g<2>", text, count=1)
        PACKAGE.write_text(text, encoding="utf-8")

    # ── helpers ──────────────────────────────────────────────────────────────

    def edit(self, path: Path, old: str, new: str, count: int = 1):
        body = path.read_text(encoding="utf-8")
        self.assertEqual(body.count(old), count, f"mutation anchor not unique in {path.name}: {old[:70]!r}")
        path.write_text(body.replace(old, new), encoding="utf-8")
        self.rehash()

    def assert_trips(self, assertion: str):
        passed, failures = validator_result()
        self.assertFalse(passed, "the mutation must not validate")
        self.assertIn(assertion, failures,
                      f"expected {assertion!r} to fail; actual failures: {failures}")

    # ── 1-3 · figure geometry and the ledger that describes it ───────────────

    def test_strip_language_restored_in_the_teacher_guide(self):
        """The superseded twelve-metre strip must not come back into any role."""
        self.edit(CONTENT, "It is a plan view: circular patches of abundance drawn inside ground",
                  "It draws the surveyed pattern along a twelve-metre strip, inside ground")
        self.assert_trips("no role, ledger or README still describes Figure A as a strip")

    def test_strip_restored_in_the_figure_provenance_ledger(self):
        """The declared ledger of record must describe the figure that renders."""
        self.edit(REGISTRY, '"shows": "A plan view of the surveyed ground, seen from above:',
                  '"shows": "One twelve-metre strip on which the surveyed compounds are abundant:')
        self.assert_trips("figureProvenance describes the rendered plan view, not a superseded figure")

    def test_unsupported_three_metre_offset_restored(self):
        """Dr. Nova's described bed separation is not a surveyed patch-edge offset."""
        self.edit(CONTENT, '<text x="500" y="178" class="fig-tick">sharp edge</text>',
                  '<text x="248" y="178" class="fig-tick">about 3 m</text>'
                  '<text x="500" y="178" class="fig-tick">sharp edge</text>', count=2)
        self.assert_trips("fig-patches-student draws no distance between patches")

    def test_per_patch_measurements_restored_in_the_extended_description(self):
        """The survey reports a range, not a measurement for any single patch."""
        self.edit(CONTENT, "The circles vary in size within the reported range of about four to six metres "
                           "across; no single patch is given a measurement of its own.",
                  "The circles are about four to six metres across — the three drawn here are about five, "
                  "six and four metres.")
        self.assert_trips("fig-patches-student assigns no measurement to an individual patch")

    # ── 4-6 · evidence availability ──────────────────────────────────────────

    def test_kess_source_statement_removed_from_student(self):
        """Task 4 grades Kess's mechanism, so the Student edition must print it."""
        self.edit(CONTENT, "“Fungal hyphae colonise compatible roots and extend into soil.", "“Kess reports.")
        self.assert_trips("every source Task 4 grades reports on the learner page, at or before Task 4")

    def test_kess_source_statement_removed_from_accessible(self):
        """The same removal in the differentiated edition must fail independently."""
        self.edit(CONTENT, "Fungal threads grow into compatible roots and out into the soil. The fungi get "
                           "carbon from the plant.", "Kess remembers something about the soil.")
        self.assert_trips("every source Task 4 grades reports on the learner page, at or before Task 4")

    def test_gc_2201_required_by_the_answer_key_without_learner_evidence(self):
        """The original defect: a designation graded against but printed nowhere."""
        body = CONTENT.read_text(encoding="utf-8")
        body = body.replace("Case GC-2201 granted a same-species, same-world agricultural exception.",
                            "A precedent exists for an agricultural exception.")
        body = body.replace("Case GC-2201 allowed a same-species, same-world farming exception.",
                            "A precedent exists for a farming exception.")
        CONTENT.write_text(body, encoding="utf-8")
        self.rehash()
        self.assert_trips("every designation the Answer Key relies on is printed in both learner editions")

    def test_section_14_7_removed_from_the_accessible_task_4_evidence(self):
        """A constraint the task grades cannot first appear at the task it constrains."""
        self.edit(CONTENT, "Section 14.7 of the Concord Biosafety Protocol: living material may not be "
                           "moved between zones without Concord approval first.",
                  "The Concord has a rule about moving living material.")
        self.assert_trips("every source Task 4 grades reports on the learner page, at or before Task 4")

    # ── 7-8 · Accessible answerability ───────────────────────────────────────

    def test_accessible_task1_record_column_removed(self):
        """Without the record no Accessible learner can name the untested category."""
        body = CONTENT.read_text(encoding="utf-8")
        body = body.replace('<th scope="col">What the restoration examined</th>'
                            '<th scope="col">What the record says</th><th scope="col">T or X</th>',
                            '<th scope="col">What the restoration examined</th><th scope="col">T or X</th>')
        body = re.sub(r"<td>(Never tested\. No record says which fungi are in either kind of bed\.)</td>",
                      "", body)
        CONTENT.write_text(body, encoding="utf-8")
        self.rehash()
        self.assert_trips("the Accessible Task 1 table carries the record the task is graded on")

    def test_toxicology_and_dating_evidence_removed_from_task_3(self):
        """Task 3's rejections each rest on a record that must reach the learner."""
        body = CONTENT.read_text(encoding="utf-8")
        body = body.replace("Also on the record: the patchy growth is decades old.",
                            "Also on the record: the beds are watered together.")
        body = body.replace("On the record for both kinds of bed: the patchy growth is decades old.",
                            "On the record for both kinds of bed: the beds are watered together.")
        CONTENT.write_text(body, encoding="utf-8")
        self.rehash()
        self.assert_trips("both learner editions carry the record behind every Task 3 rejection")

    # ── 9 · cross-role numbering ─────────────────────────────────────────────

    def test_divergent_evidence_table_numbering_restored(self):
        """The original defect: one number meaning two different records."""
        self.edit(CONTENT, "<caption>Table 6 · What the approved trial must include</caption>"
                           "<thead><tr><th scope=\"col\">Requirement</th>"
                           "<th scope=\"col\">What it means</th></tr></thead>",
                  "<caption>Table 5 · What the approved trial must include</caption>"
                           "<thead><tr><th scope=\"col\">Requirement</th>"
                           "<th scope=\"col\">What it means</th></tr></thead>")
        self.assert_trips("a table number means the same record in both learner editions")

    def test_vocabulary_aid_renumbered_as_an_evidence_table(self):
        """A numbered vocabulary aid is what shifted every table in v1.0."""
        self.edit(CONTENT, "<h2 class=\"support-heading\">Words you will need</h2>"
                           "<dl class=\"vocabulary-list\">",
                  "<h2 class=\"support-heading\">Words you will need</h2>"
                  "<table class=\"data-table vocabulary-table\">"
                  "<caption>Table 1 · Words you will need</caption>"
                  "<thead><tr><th scope=\"col\">Term</th><th scope=\"col\">Meaning</th></tr></thead>"
                  "<tbody><tr><td>Hyphae</td><td>Fine fungal threads.</td></tr></tbody></table>"
                  "<dl class=\"vocabulary-list\">", count=2)
        self.assert_trips("no vocabulary aid takes an evidence-table number")

    def test_teacher_reference_to_a_table_only_one_edition_has(self):
        """A reference that resolves in Student but not Accessible is not resolved."""
        self.edit(CONTENT, "Tables 1–6 are the case records.", "Tables 1–7 are the case records.")
        self.assert_trips("every table the Teacher Guide or Answer Key names resolves in both learner editions")

    # ── 10-12 · revision propagation ─────────────────────────────────────────

    def test_full_page_cer_claim_restored(self):
        """The Student CER shares its page with Task 7 under the combined contract."""
        self.edit(CONTENT, "The Accessible CER occupies a full page of its own. In the Student edition it "
                           "shares its page with Task 7 under the approved combined contract, because on a "
                           "page of its own it left roughly half the page empty.",
                  "The CER occupies a full page in both learner editions.")
        self.assert_trips("the Teacher Guide does not claim a full-page CER in both learner editions")

    def test_identical_accessible_evidence_claim_restored(self):
        """The Accessible edition carries the same evidence, not the same presentation."""
        self.edit(CONTENT, "The task numbers, the evidence available and the diagnosis are the same in both; "
                           "the presentation is not.",
                  "The task numbers, the evidence and the diagnosis are identical.")
        self.assert_trips("the Teacher Guide does not claim the Accessible evidence is identical")

    def test_task1_analogy_moved_after_the_task_it_teaches(self):
        """The analogy exists to make Task 1 tractable, so it cannot follow it."""
        body = CONTENT.read_text(encoding="utf-8")
        start = body.index('<div class="teaching-analogy" data-analogy="inspection-checklist-v1">')
        end = body.index("</div>", body.index("It is not a garden record.</p>")) + len("</div>")
        block = body[start:end]
        body = body[:start] + body[end:]
        anchor = '<span class="response-label">Why a set of clean panels is not evidence that nothing is wrong</span>'
        body = body.replace(anchor, block + anchor, 1)
        CONTENT.write_text(body, encoding="utf-8")
        self.rehash()
        self.assert_trips("the student analogy prints after the Task 1 heading and before its record")

    # ── 13-14 · standards ────────────────────────────────────────────────────

    def test_ms_ls2_2_restored_as_direct(self):
        """The breadth the performance expectation names is still absent."""
        body = REGISTRY.read_text(encoding="utf-8")
        body = body.replace('  "standards": [\n    {\n      "code": "MS-ETS1-1",',
                            '  "standards": [\n    {\n      "code": "MS-LS2-2",\n'
                            '      "alignment": "direct",\n      "assessedAt": 4,\n'
                            '      "taskEvidence": "Task 4 requires students to construct an explanation for '
                            'patterns of interactions among organisms across the garden, and Task 6 requires '
                            'them to defend it against three rejected alternatives."\n    },\n    {\n'
                            '      "code": "MS-ETS1-1",', 1)
        REGISTRY.write_text(body, encoding="utf-8")
        self.edit(CONTENT, "MS-ETS1-1 is the direct alignment, and Task 7 is where it is assessed:",
                  "MS-LS2-2 is the direct alignment at Task 4. MS-ETS1-1 is also direct, and Task 7 is "
                  "where it is assessed:")
        self.assert_trips("MS-LS2-2 and MS-ETS1-2 are withdrawn and not claimed anywhere")

    def test_ms_ets1_2_restored_without_a_design_comparison(self):
        """Comparing explanations is not evaluating competing design solutions."""
        body = REGISTRY.read_text(encoding="utf-8")
        body = body.replace('  "standards": [\n    {\n      "code": "MS-ETS1-1",',
                            '  "standards": [\n    {\n      "code": "MS-ETS1-2",\n'
                            '      "alignment": "supporting",\n      "assessedAt": 3,\n'
                            '      "taskEvidence": "Task 3 asks students to evaluate four proposed '
                            'explanations and to write the record that rules out each of the three they '
                            'reject, which is an evaluation against shared evidence."\n    },\n    {\n'
                            '      "code": "MS-ETS1-1",', 1)
        REGISTRY.write_text(body, encoding="utf-8")
        self.rehash()
        self.assert_trips("MS-LS2-2 and MS-ETS1-2 are withdrawn and not claimed anywhere")

    # ── 15-16 · the science protections the case exists to hold ──────────────

    BRIEFING = ("The chemistry is clean, yet beds three metres apart get the same amendments, water, "
                "compost and seed — and some thrive while some fail.")

    def test_guaranteed_recovery_claim_introduced(self):
        """No printable role may promise the garden recovers."""
        self.edit(CONTENT, self.BRIEFING, self.BRIEFING + " The garden will recover once the fungi go in.")
        self.assert_trips("no printable role asserts a prohibited scientific overstatement")

    def test_unscreened_transfer_language_introduced(self):
        """Nothing living moves without identification, screening, approval and controls."""
        self.edit(CONTENT, self.BRIEFING,
                  self.BRIEFING + " Transplant living soil from the good beds straight into the bad ones.")
        self.assert_trips("no printable role asserts a prohibited scientific overstatement")


if __name__ == "__main__":
    unittest.main(verbosity=2)
