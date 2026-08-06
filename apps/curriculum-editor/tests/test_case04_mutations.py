#!/usr/bin/env python3
"""Mutation tests for the Campaign 2 Case 04 protections.

Each mutation reproduces a defect the Campaign 2 completion audit found inside the released
v1.0 package — or one this remediation found independently — injects it into the working
sources, and asserts that ``validate_case04_campaign2.py`` fails *for the intended reason*.
Sources are always restored, including when a test fails, so the tree is left exactly as it
was found.

A protection that cannot be made to fail is not a protection, and a protection that fires
only through a hash check is not the protection it claims to be. Every mutation therefore
re-pins the package hashes before validating, and names the single assertion it must trip.
``assert_trips`` additionally rejects a run whose only failures are the hash or lifecycle
plumbing, so a mutation can never be scored as caught by drift.

Case 04 is the unreleased v1.1 corrective candidate, so there is no release record and no
frozen DOM baseline to re-pin: the package hash is the only integrity plumbing in the way.
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
CASE_ROOT = ROOT / "sss/campaign-2/case-04-silent-grove"
SOURCE = CASE_ROOT / "source"
CONTENT = SOURCE / "content.html"
REGISTRY = SOURCE / "task-registry.js"
PACKAGE = SOURCE / "case-package.json"
README = CASE_ROOT / "README.md"
RETAINED_RELEASE = CASE_ROOT / "history/release-v1.0.json"
RETAINED_APPROVAL = CASE_ROOT / "history/CASE04_OWNER_APPROVAL_v1.0.md"
VALIDATOR = ROOT / "apps/curriculum-editor/tests/validate_case04_campaign2.py"
TRACKED = (CONTENT, REGISTRY, PACKAGE, README, RETAINED_RELEASE, RETAINED_APPROVAL)

# Failures that mean "something moved", not "the protection fired". A mutation whose only
# effect is one of these has not proved anything.
PLUMBING = {
    "package source hashes verify",
    "the shared corrective-release lifecycle rules are satisfied",
    "the package certifies all four sources, including layoutOverrides",
}


def validator_result() -> tuple[bool, list[str]]:
    """Run the Case 04 validator and return (passed, failing assertion names)."""
    run = subprocess.run([sys.executable, str(VALIDATOR)], cwd=ROOT, text=True, capture_output=True)
    try:
        payload = json.loads(run.stdout[run.stdout.index("{"):])
    except (ValueError, json.JSONDecodeError):
        return False, ["validator crashed"]
    return run.returncode == 0, [a["name"] for a in payload["assertions"] if not a["pass"]]


class Case04Mutations(unittest.TestCase):
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
        """Re-pin the package hashes a mutation would otherwise trip incidentally."""
        digests = {key: hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
                   for key, name in (("content", "content.html"),
                                     ("presentation", "presentation.css"),
                                     ("taskRegistry", "task-registry.js"),
                                     ("layoutOverrides", "layout-overrides.json"))}
        text = PACKAGE.read_text(encoding="utf-8")
        for key, digest in digests.items():
            text = re.sub(rf'("{key}": ")[0-9a-f]{{64}}(")', rf"\g<1>{digest}\g<2>", text, count=1)
        PACKAGE.write_text(text, encoding="utf-8")

    # ── helpers ──────────────────────────────────────────────────────────────

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

    # ── 1-2 · Accessible Task 2 evidence availability (audit M-21) ───────────

    def test_accessible_task2_log_evidence_removed(self):
        """The v1.0 defect: the Accessible edition dropped the log table Task 2 needs."""
        body = CONTENT.read_text(encoding="utf-8")
        start = body.index('<caption>Table 4 · What the two ship logs record</caption>')
        table_start = body.rindex("<table", 0, start)
        table_end = body.index("</table>", start) + len("</table>")
        CONTENT.write_text(body[:table_start] + body[table_end:], encoding="utf-8")
        self.rehash()
        self.assert_trips("the Accessible Task 2 page prints the log evidence its prompt and "
                          "the Answer Key require")

    def test_accessible_task2_prompt_references_evidence_not_printed(self):
        """A task may not pass merely by referring to a table the reader does not hold.

        The v1.0 Accessible edition carried no Table 4 at all, so the audit's cross-role
        check — which only fired on *named* tables — never saw the omission. Renaming the
        table so the Task 2 evidence is no longer a resolvable Table 4 must fail.
        """
        self.edit(CONTENT,
                  "<caption>Table 4 · What the two ship logs record</caption>",
                  "<caption>Ship records</caption>")
        self.assert_trips("the Accessible Task 2 log evidence is a named table, not "
                          "unlabelled prose")

    # ── 3-4 · historical versus current readings (audit M-22) ───────────────

    def test_intensity_did_not_change_restored(self):
        """The v1.0 Answer Key rejected light damage with a control the game contradicts."""
        self.edit(CONTENT,
                  "The organisms are structurally sound and the reflex is normal; no record "
                  "reports damaged tissue.",
                  "The organisms are structurally sound and the reflex is normal; intensity "
                  "did not change.")
        self.assert_trips("no role converts the current 100% intensity reading into a "
                          "historical constant")

    def test_intensity_100_percent_throughout_restored(self):
        """The runtime says the lights were set to maximum when the schedule changed."""
        self.edit(CONTENT,
                  "Both logs report no structural decline. Damaged tissue would show in the "
                  "examination record;",
                  "Both logs report no structural decline. Intensity has stayed at 100% of the "
                  "standard grow setting throughout;")
        self.assert_trips("no role converts the current 100% intensity reading into a "
                          "historical constant")

    # ── 5 · distractor fidelity to the runtime ──────────────────────────────

    def test_filtration_alternative_loses_the_drift_direction(self):
        """The runtime's alternative is a calibration drift, not a correctly-set system."""
        self.edit(CONTENT,
                  "The chemical scrubbers have drifted out of their target range and are "
                  "removing the signalling compounds from the air.",
                  "The scrubbers are removing the signalling compounds from the air.",
                  count=2)
        self.assert_trips("the filtration alternative keeps the runtime's drift-out-of-range "
                          "direction in every role")

    # ── 6-7 · Task 1 evidence timing (audit B-6) ────────────────────────────

    def test_student_task1_controlling_evidence_removed(self):
        """Task 1 asks for a change/keep classification; the change record must precede it."""
        body = CONTENT.read_text(encoding="utf-8")
        start = body.index('<div class="science-note"><span class="label">Change record</span>')
        end = body.index("</div>", body.index("</p>", start)) + len("</div>")
        CONTENT.write_text(body[:start] + body[end:], encoding="utf-8")
        self.rehash()
        self.assert_trips("Task 1 classification evidence is printed on or before Task 1 in "
                          "both learner editions")

    def test_accessible_task1_controlling_evidence_removed(self):
        """The Accessible edition needs the same record, in its own register."""
        body = CONTENT.read_text(encoding="utf-8")
        start = body.index('<div class="science-note"><span class="label">What the ship logs '
                           'record</span>')
        end = body.index("</div>", body.index("</p>", start)) + len("</div>")
        CONTENT.write_text(body[:start] + body[end:], encoding="utf-8")
        self.rehash()
        self.assert_trips("Task 1 classification evidence is printed on or before Task 1 in "
                          "both learner editions")

    # ── 8 · hidden runtime-only evidence (audit B-5) ────────────────────────

    def test_task8_requires_cultural_significance(self):
        """The grove's cultural significance is a runtime record, printed in no learner page."""
        self.edit(CONTENT,
                  "Strong answers name the ship’s power supply, which already fluctuated once "
                  "on Day −93",
                  "Strong answers name the grove as a culturally significant space whose "
                  "caretakers need access, the ship’s power supply, which already fluctuated "
                  "once on Day −93")
        self.assert_trips("no Answer Key expectation requires a runtime-only fact withheld "
                          "from learners")

    # ── 9-10 · standards (audit M-23 and F-3) ───────────────────────────────

    def test_ms_ls1_5_restored_as_direct(self):
        """The performance expectation names growth; this case holds growth constant."""
        self.edit(REGISTRY,
                  '"code": "MS-LS1-5",\n      "claim": "supporting",',
                  '"code": "MS-LS1-5",\n      "claim": "direct",')
        self.assert_trips("no standard is claimed as direct assessment in the registry")

    def test_ms_ets1_1_restored_as_direct_in_the_guide(self):
        """Task 8 never asks students to account for impacts on people."""
        self.edit(CONTENT,
                  "<p><strong>Supporting alignment: MS-ETS1-1.</strong>",
                  "<p><strong>Direct assessment: MS-ETS1-1.</strong>")
        self.assert_trips("no printable role claims any NGSS performance expectation as "
                          "direct assessment")

    # ── 11-12 · preserved science boundaries ────────────────────────────────

    def test_compromise_onset_date_invented(self):
        """The two logs give Day −80 and Day −83. The packet never reconciles them."""
        self.edit(CONTENT,
                  "The two ship logs give different days for the start of complete silence — the "
                  "sensor log says Day −80 and the caretaker log says Day −83.",
                  "The two ship logs disagree, so silence began on Day −81 and a half.")
        self.assert_trips("no printable role asserts a prohibited scientific overstatement")

    def test_darkness_described_as_a_nutrient(self):
        """Darkness supplies no matter or energy here; it is a timing cue."""
        self.edit(CONTENT,
                  "For two years the grove’s signalling rose during its dark hours and fell "
                  "during daylight, over and over.",
                  "Darkness is a nutrient the grove feeds on, so it signalled during its dark "
                  "hours.")
        self.assert_trips("no printable role asserts a prohibited scientific overstatement")


if __name__ == "__main__":
    unittest.main(verbosity=2)
