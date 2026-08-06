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

Case 04 is now the approved v1.1 corrective release, so a content edit is caught by the package
hash, the release-record hash and the release-record DOM baseline before any content detector
runs. Re-pinning all three is what makes these tests prove the content protections rather than
the integrity plumbing.
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
RELEASE = CASE_ROOT / "history/release-v1.1.json"
RELEASE_APPROVAL = CASE_ROOT / "history/CASE04_OWNER_APPROVAL_v1.1.md"
RETAINED_RELEASE = CASE_ROOT / "history/release-v1.0.json"
RETAINED_APPROVAL = CASE_ROOT / "history/CASE04_OWNER_APPROVAL_v1.0.md"
VALIDATOR = ROOT / "apps/curriculum-editor/tests/validate_case04_campaign2.py"
TRACKED = (CONTENT, REGISTRY, PACKAGE, README, RELEASE, RELEASE_APPROVAL,
           RETAINED_RELEASE, RETAINED_APPROVAL)
V10_DOM_BASELINES = {
    "student": "78bd75e06a07acede806062efd4e5383ff618d42ecb6a668633f822cf1575186",
    "teacher": "27179d6b828914cce0d27280562bdd1b37d6cdf3a373b4a48e704c91e5f528b6",
    "answer": "a7c3566b867660f5614d8c078bc6306058e9afec721bfcb7758b4224dca720f1",
}

# Failures that mean "something moved", not "the protection fired". A mutation whose only
# effect is one of these has not proved anything.
PLUMBING = {
    "package source hashes verify",
    "the shared corrective-release lifecycle rules are satisfied",
    "the package certifies all four sources, including layoutOverrides",
    "the v1.1 release record certifies all four sources and they match the package",
    "the v1.1 frozen DOM baselines match the released markup",
    "canonicalSourceApprovalCommit contains all four source blobs the record certifies",
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

    def restore_missing(self):
        """Recreate any record a mutation deleted."""
        for path, body in self.original.items():
            if not path.exists():
                path.write_bytes(body)

    def rehash(self):
        """Re-pin every hash and baseline a mutation would otherwise trip incidentally."""
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
                                     ("presentation", "presentation.css"),
                                     ("taskRegistry", "task-registry.js"),
                                     ("layoutOverrides", "layout-overrides.json"))}
        text = PACKAGE.read_text(encoding="utf-8")
        for key, digest in digests.items():
            text = re.sub(rf'("{key}": ")[0-9a-f]{{64}}(")', rf"\g<1>{digest}\g<2>", text, count=1)
        PACKAGE.write_text(text, encoding="utf-8")
        if not RELEASE.exists():
            return
        release = json.loads(RELEASE.read_text(encoding="utf-8"))
        release["sourceHashes"].update(digests)
        soup = BeautifulSoup(CONTENT.read_text(encoding="utf-8"), "html.parser")
        for role in ("student", "teacher", "answer"):
            release["frozenNonAccessibleDomBaselines"][role] = role_dom_hash(soup, role)
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")

    def edit_record(self, path: Path, mutate):
        """Mutate a JSON history record in place, leaving source hashes alone."""
        record = json.loads(path.read_text(encoding="utf-8"))
        mutate(record)
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

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

    # ── 13-20 · release-mode lifecycle protections ──────────────────────────

    def test_v11_release_record_missing(self):
        """An approved package must carry the release record for its own version."""
        self.addCleanup(self.restore_missing)
        RELEASE.unlink()
        self.assert_trips("history holds exactly the four canonical records, two per approved "
                          "version")

    def test_print_gate_downgraded(self):
        """The physical print gate is what a printable correction requires."""
        self.edit_record(RELEASE, lambda r: r.__setitem__("acceptedPrintStatus", "NOT_RUN"))
        self.assert_trips("the v1.1 release record records the physical print gate")

    def test_prior_release_dropped(self):
        """v1.0 must remain represented as the canonical prior approved release."""
        self.edit_record(RELEASE, lambda r: r.__setitem__("priorApprovedReleases", []))
        self.assert_trips("the v1.1 record represents exactly one prior approved release, v1.0")

    def test_v11_baselines_reverted_to_v10(self):
        """Approved-baseline enforcement must not be satisfiable by superseded markup."""
        self.edit_record(RELEASE, lambda r: r["frozenNonAccessibleDomBaselines"].update(
            V10_DOM_BASELINES))
        self.assert_trips("the v1.1 frozen DOM baselines match the released markup")

    def test_certified_source_commit_is_false(self):
        """A release record may not certify a commit that does not contain its sources.

        This is the exact v1.0 defect. Pinning the pre-promotion candidate tip reproduces
        it: the approved task registry does not exist at that commit.
        """
        self.edit_record(RELEASE, lambda r: r.__setitem__(
            "canonicalSourceApprovalCommit", "556cbf843a284835e23d3341ff356d5453db341f"))
        self.assert_trips("canonicalSourceApprovalCommit contains all four source blobs the "
                          "record certifies")

    def test_retained_v10_release_record_deleted(self):
        """The superseded release record is immutable evidence, not disposable."""
        self.addCleanup(self.restore_missing)
        RETAINED_RELEASE.unlink()
        self.assert_trips("history holds exactly the four canonical records, two per approved "
                          "version")

    def test_retained_v10_approval_record_deleted(self):
        """So is the superseded owner-approval record."""
        self.addCleanup(self.restore_missing)
        RETAINED_APPROVAL.unlink()
        self.assert_trips("history holds exactly the four canonical records, two per approved "
                          "version")

    def test_v10_rewritten_to_describe_v11(self):
        """A retained record may never be edited to describe the release that superseded it."""
        self.edit_record(RETAINED_RELEASE, lambda r: r.__setitem__("curriculumVersion", "1.1"))
        self.assert_trips("the retained v1.0 record still describes the v1.0 release, not the "
                          "corrective one")

    def test_v10_approval_rewritten_to_describe_v11(self):
        """The same rule holds for the prose approval record."""
        body = RETAINED_APPROVAL.read_text(encoding="utf-8")
        RETAINED_APPROVAL.write_text(
            body.replace("# Campaign 2 Case 04 v1.0 Owner Approval",
                         "# Campaign 2 Case 04 v1.0 Owner Approval\n\nSuperseded by v1.1."),
            encoding="utf-8")
        self.assert_trips("the retained v1.0 owner-approval record is unchanged and still "
                          "describes v1.0")

    def test_v10_stale_validation_figure_silently_corrected(self):
        """The stale 75/75 is historical fact. Correcting it in place destroys the evidence."""
        self.edit_record(RETAINED_RELEASE,
                         lambda r: r["acceptedValidation"].__setitem__("case04Scoped", "82/82"))
        self.assert_trips("v1.0's known historical defects are preserved, not silently corrected")

    def test_v10_missing_layout_hash_silently_added(self):
        """So is the omitted layoutOverrides hash."""
        self.edit_record(RETAINED_RELEASE, lambda r: r["sourceHashes"].__setitem__(
            "layoutOverrides", "7d27df1542a775a4b4a00a0cef0093ec38f80acefd320fa7fcf89d3c7a97811c"))
        self.assert_trips("v1.0's known historical defects are preserved, not silently corrected")

    def test_v10_bad_pin_silently_corrected(self):
        """And so is the inaccurate canonicalSourceApprovalCommit."""
        self.edit_record(RETAINED_RELEASE, lambda r: r.__setitem__(
            "canonicalSourceApprovalCommit", "91c7a3f6615b8a33a37d34ba0146965cfa81bf8c"))
        self.assert_trips("v1.0's known historical defects are preserved, not silently corrected")

    def test_v11_repeats_the_stale_figure(self):
        """The v1.1 record must not inherit the defect it exists to repair."""
        self.edit_record(RELEASE,
                         lambda r: r["acceptedValidation"].__setitem__("case04Scoped", "75/75"))
        self.assert_trips("the v1.1 release record does not repeat v1.0's stale figure or "
                          "migration note")

    def test_direct_pe_reclaimed_in_the_release_record(self):
        """The owner accepted that v1.1 claims no directly assessed performance expectation."""
        self.edit_record(RELEASE, lambda r: r["correctionSummary"]["standardsOutcome"].__setitem__(
            "directlyAssessedPerformanceExpectations", ["MS-LS1-5"]))
        self.assert_trips("the v1.1 release record documents that no NGSS PE is directly "
                          "assessed, and why")


if __name__ == "__main__":
    unittest.main(verbosity=2)
