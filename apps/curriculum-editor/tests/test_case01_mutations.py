#!/usr/bin/env python3
"""Mutation tests for the Campaign 2 Case 01 protections.

Each mutation reproduces a defect the Campaign 2 completion audit found inside the
released v1.0 package, injects it into the working sources, and asserts that
``validate_case01_campaign2.py`` fails *for the intended reason*. Sources are always
restored, including when a test fails, so the tree is left exactly as it was found.

A protection that cannot be made to fail is not a protection, and a protection that
fires only through a hash check is not the protection it claims to be. Every mutation
therefore re-pins the package hashes before validating, and names the single assertion
it must trip. ``assert_trips`` additionally rejects a run whose only failures are the
hash or lifecycle plumbing, so a mutation can never be scored as caught by drift.

Case 01 is now the approved v1.1 corrective release, so a content edit is caught by the
package hash, the release-record hash and the release-record DOM baseline before any content
detector runs. Re-pinning all three is what makes these tests prove the content protections
rather than the integrity plumbing.
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
CASE_ROOT = ROOT / "sss/campaign-2/case-01-heavy-hands"
SOURCE = CASE_ROOT / "source"
CONTENT = SOURCE / "content.html"
REGISTRY = SOURCE / "task-registry.js"
PACKAGE = SOURCE / "case-package.json"
README = CASE_ROOT / "README.md"
RELEASE = CASE_ROOT / "history/release-v1.1.json"
RELEASE_APPROVAL = CASE_ROOT / "history/CASE01_OWNER_APPROVAL_v1.1.md"
RETAINED_RELEASE = CASE_ROOT / "history/release-v1.0.json"
RETAINED_APPROVAL = CASE_ROOT / "history/CASE01_OWNER_APPROVAL_v1.0.md"
VALIDATOR = ROOT / "apps/curriculum-editor/tests/validate_case01_campaign2.py"
TRACKED = (CONTENT, REGISTRY, PACKAGE, README, RELEASE, RELEASE_APPROVAL,
           RETAINED_RELEASE, RETAINED_APPROVAL)

# Failures that mean "something moved", not "the protection fired". A mutation whose only
# effect is one of these has not proved anything.
PLUMBING = {
    "package source hashes verify",
    "the shared corrective-release lifecycle rules are satisfied",
    "the v1.1 release record certifies all four sources and they match the package",
    "the v1.1 frozen DOM baselines match the released markup",
    "canonicalSourceApprovalCommit contains all four source blobs the record certifies",
}


def validator_result() -> tuple[bool, list[str]]:
    """Run the Case 01 validator and return (passed, failing assertion names)."""
    run = subprocess.run([sys.executable, str(VALIDATOR)], cwd=ROOT, text=True, capture_output=True)
    try:
        payload = json.loads(run.stdout[run.stdout.index("{"):])
    except (ValueError, json.JSONDecodeError):
        return False, ["validator crashed"]
    return run.returncode == 0, [a["name"] for a in payload["assertions"] if not a["pass"]]


class Case01Mutations(unittest.TestCase):
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
        RELEASE.write_text(json.dumps(release, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

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
        self.assertTrue(set(failures) - PLUMBING,
                        "the mutation was caught only by hash or lifecycle plumbing")

    # ── 1-3 · unsupported historical controls ────────────────────────────────

    def test_nutrient_supply_verified_row_restored(self):
        """The v1.0 Answer Key marked nutrient supply as verified. The game does not."""
        self.edit(CONTENT,
                  "<td>Nutrient supply</td><td>N — reported as precise now, never changed "
                  "between plantings</td>",
                  "<td>Nutrient supply</td><td>Y — verified against the cultivation standard</td>")
        self.assert_trips("the Answer Key marks the present-reading conditions N, not verified")

    def test_grow_light_verified_row_restored(self):
        """The v1.0 Answer Key marked the grow-light spectrum as calibrated and settled."""
        self.edit(CONTENT,
                  "<td>Grow-light spectrum</td><td>N — reported as calibrated now, never changed "
                  "between plantings</td>",
                  "<td>Grow-light spectrum</td><td>Y — calibrated to the homeworld standard</td>")
        self.assert_trips("the Answer Key marks the present-reading conditions N, not verified")

    def test_water_claimed_as_a_tested_variable(self):
        """The game reports water as a present condition, never as a variable it changed."""
        self.edit(CONTENT,
                  "Soil and seed stock were each changed across three plantings without effect;",
                  "Soil, nutrients, light and water were each changed across three plantings "
                  "without effect;")
        self.assert_trips("no printable role presents nutrients, light or water as a tested "
                          "or eliminated control")

    def test_controls_ledger_marks_an_unsupported_condition_as_tested(self):
        """Only soil and seed stock may carry changedBetweenPlantings."""
        self.edit(REGISTRY,
                  '"condition": "Nutrient supply",\n      "changedBetweenPlantings": false,',
                  '"condition": "Nutrient supply",\n      "changedBetweenPlantings": true,')
        self.assert_trips("the controls ledger marks exactly the two conditions the runtime "
                          "reports as varied")

    def test_a_condition_is_recorded_as_ruled_out(self):
        """A present reading never rules a condition out."""
        self.edit(REGISTRY,
                  '"canonicalEvidence": "\\"Nutrients: precise.\\" A present condition, not an '
                  'intervention in any planting.",\n      "learnerVisible": true,\n      '
                  '"answerKeyMark": "N",\n      "ruledOut": false',
                  '"canonicalEvidence": "\\"Nutrients: precise.\\" A present condition, not an '
                  'intervention in any planting.",\n      "learnerVisible": true,\n      '
                  '"answerKeyMark": "N",\n      "ruledOut": true')
        self.assert_trips("no condition in the ledger is recorded as ruled out")

    # ── 4-7 · learner evidence availability ──────────────────────────────────

    def test_reported_difference_required_without_learner_evidence(self):
        """0.00187 g is withheld from both learner editions and may not be graded."""
        self.edit(CONTENT,
                  "The centrifuge sensor array measured in three places instead of one and found "
                  "the pull weakest at the top of the 20 cm bed",
                  "The centrifuge sensor array reports a difference of 0.00187 g across the 20 cm "
                  "bed and found the pull weakest at the top")
        self.assert_trips("no Answer Key expectation requires a value withheld from the "
                          "learner editions")

    def test_endpoint_radii_and_magnitudes_required_without_learner_evidence(self):
        """The three radii and magnitudes are Teacher-facing by design."""
        self.edit(CONTENT,
                  "<td>The sensor array measured in three places and reported the pull weakest "
                  "at the bed top, exactly right in the middle, and strongest at the bottom.",
                  "<td>Both endpoint values, 2.0991 g at 224.8 m and 2.1009 g at 225.0 m, sit "
                  "inside the permitted band.")
        self.assert_trips("no Answer Key expectation requires a value withheld from the "
                          "learner editions")

    def test_specification_band_required_before_it_is_printed(self):
        """±0.05 g first reaches learners at Task 8; Task 6 cannot require it."""
        self.edit(CONTENT,
                  "<td>The sensor array measured in three places and reported the pull weakest "
                  "at the bed top, exactly right in the middle, and strongest at the bottom.",
                  "<td>The specification allows ±0.05 g, and the reported values sit inside it.")
        self.assert_trips("every reported value the Answer Key uses is printed in both learner "
                          "editions on or before the page carrying that task")

    def test_gc1445_required_without_being_printed_or_qualified(self):
        """GC-1445 appears in no learner edition, so no graded claim may need it."""
        self.edit(CONTENT,
                  "Record GC-1208 resolved the matching problem this way, by extending the "
                  "radius to 600 m.",
                  "Record GC-1208 resolved the matching problem this way, and GC-1445 at 300 m "
                  "reported no misalignment.")
        self.assert_trips("every use of GC-1445 carries the qualifier the record attaches to it")

    def test_precedent_radii_required_without_learner_evidence(self):
        """80 m and 300 m are Teacher-facing; the Answer Key may not lean on them."""
        self.edit(CONTENT,
                  "and two earlier centrifuge crops that met the same design question with "
                  "different outcomes.",
                  "and two earlier centrifuge outcomes at 80 m and 300 m.")
        self.assert_trips("no Answer Key expectation requires a value withheld from the "
                          "learner editions")

    # ── 8-9 · source attribution ─────────────────────────────────────────────

    def test_negligible_judgement_attributed_to_the_archive(self):
        """The botanist calls the bed-scale difference negligible; the archive never does."""
        self.edit(CONTENT,
                  "It is the botanist, not the archive, who calls the bed-scale difference "
                  "negligible",
                  "The archive says the bed-scale difference is negligible")
        self.assert_trips("the negligible judgement is attributed to the botanist, "
                          "not the archive")

    def test_nominal_ring_status_expanded_into_unreported_absences(self):
        """The array reports only NOMINAL. The absence claim belongs to the botanist."""
        self.edit(CONTENT,
                  "<td>Ring status</td><td>NOMINAL. Separately, the botanist reports the RPM "
                  "steady with no vibration and no wobble</td>",
                  "<td>Ring status</td><td>Nominal; no vibration and no wobble reported</td>")
        self.assert_trips("a nominal ring status is never expanded into an unreported absence")

    def test_gc1445_used_as_radius_evidence(self):
        """The record is a species counter-example, not evidence that 300 m is safe."""
        self.edit(CONTENT,
                  "So the record does not establish that a 300 m radius prevents misalignment,",
                  "So the record establishes that a 300 m radius prevents misalignment,")
        self.assert_trips("GC-1445 stays Teacher-facing and is never used as radius evidence")

    def test_universal_gradient_sensitivity_claim_introduced(self):
        """The database concludes sensitivity is species-dependent, never universal."""
        self.edit(CONTENT,
                  "The size-dependent pattern is what separates a mechanism from a coincidence "
                  "in time.",
                  "Every species is equally sensitive to a gradient of this size, so the pattern "
                  "generalises.")
        self.assert_trips("no role generalises gradient sensitivity across species")

    # ── 10-12 · Teacher synchronisation ──────────────────────────────────────

    def test_stale_task_3_subtraction_instruction_restored(self):
        """Commit bf0ad45 removed the arithmetic; the guide may not ask for it back."""
        self.edit(CONTENT,
                  "No calculator is required. No task in this packet asks for arithmetic of "
                  "any kind.",
                  "No calculator is required. Task 3 needs one subtraction of four-decimal values.")
        self.assert_trips("no stale calculation instruction survives in the Teacher Guide")

    def test_unscorable_precision_rubric_dimension_restored(self):
        """A rubric dimension may not grade values learners never receive."""
        self.edit(CONTENT,
                  "<tr><td>Reported values only</td><td>Copies the printed values (2.10 g, "
                  "±0.05 g, 20 cm, 600 m, the onset days) exactly, and adds no quantity the "
                  "packet does not report.</td><td>Copies the printed values correctly but adds "
                  "an unreported figure, such as an amount of bending.</td><td>Alters a printed "
                  "value, or invents a number for the difference across the bed.</td></tr>",
                  "<tr><td>Precision</td><td>Copies values at the precision given and treats "
                  "0.00187 g and 0.0018 g as consistent.</td><td>Copies values correctly but "
                  "cannot explain the difference in digits.</td><td>Alters reported values."
                  "</td></tr>")
        self.assert_trips("no rubric dimension or success criterion grades a value learners "
                          "never receive")

    def test_teacher_guidance_removed_for_one_task(self):
        """Every task must carry teacher-side guidance or an acceptable range."""
        body = CONTENT.read_text(encoding="utf-8")
        start = body.index("<li><strong>Task 5.</strong>")
        end = body.index("<li><strong>Task 6.</strong>")
        CONTENT.write_text(body[:start] + body[end:], encoding="utf-8")
        self.rehash()
        self.assert_trips("the Teacher Guide carries annotated guidance for every task")

    # ── 13-14 · standards ────────────────────────────────────────────────────

    def test_ms_ets1_3_restored_as_a_claimed_standard(self):
        """The withdrawn engineering standard may not return in any role."""
        self.edit(CONTENT,
                  "<p><strong>Supporting alignment: MS-ETS1-2, conditional.</strong>",
                  "<p><strong>Supporting alignment: MS-ETS1-3.</strong> Records GC-1208 and "
                  "GC-1445 are outcomes from two different ring radii.</p>"
                  "<p><strong>Supporting alignment: MS-ETS1-2, conditional.</strong>")
        self.assert_trips("no printable role claims MS-ETS1-3 as a direct or supporting alignment")

    def test_ms_ets1_3_restored_in_the_standards_ledger(self):
        """The registry is the ledger of record and must not re-declare it."""
        self.edit(REGISTRY,
                  '    {\n      "code": "MS-ETS1-2",\n      "claim": "supporting",',
                  '    {\n      "code": "MS-ETS1-3",\n      "claim": "supporting",\n'
                  '      "assessingTasks": [8],\n      "limitation": "restored"\n    },\n'
                  '    {\n      "code": "MS-ETS1-2",\n      "claim": "supporting",')
        self.assert_trips("the registry claims exactly the three supported standards")

    # ── 15-16 · revision propagation and release certification ───────────────

    def test_page_count_change_left_unpropagated(self):
        """A page-count change must reach every authority that records it."""
        self.edit(README,
                  "Role page counts: Student 5, Teacher 9, Answer Key 4, Accessible 8.",
                  "Role page counts: Student 5, Teacher 8, Answer Key 4, Accessible 8.")
        self.assert_trips("page counts agree across the DOM, the package, the registry, "
                          "the README, the static roster and the browser harness")

    def test_corrected_ring_geometry_reverted_in_one_file(self):
        """The 2 m-radius correction must hold in the guide, the README and the ledger."""
        self.edit(README,
                  "would need a radius of about two metres — roughly four\n  metres across —",
                  "would be about two metres across")
        self.assert_trips("the corrected merry-go-round geometry propagated to every file "
                          "that states it")

    def test_stray_history_record_added(self):
        """history/ holds exactly the canonical records for the two approved versions."""
        stray = CASE_ROOT / "history/release-v1.2.json"
        record = json.loads(RELEASE.read_text(encoding="utf-8"))
        record["curriculumVersion"] = "1.2"
        stray.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self.addCleanup(lambda: stray.unlink(missing_ok=True))
        self.assert_trips("history holds exactly the four canonical records, two per approved version")

    def test_retained_v1_0_record_rewritten(self):
        """v1.0 history is frozen, including its historically inaccurate commit pin."""
        record = json.loads(RETAINED_RELEASE.read_text(encoding="utf-8"))
        record["canonicalSourceApprovalCommit"] = "a4195913e7c2d98bd2174f2034a609d8e20f264c"
        RETAINED_RELEASE.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n",
                                    encoding="utf-8")
        self.assert_trips("both retained v1.0 records are byte-identical to synchronised main")

    def test_layout_overrides_hash_dropped_from_the_package(self):
        """All four sources must be certified, including layoutOverrides."""
        text = PACKAGE.read_text(encoding="utf-8")
        text = re.sub(r',\n    "layoutOverrides": "[0-9a-f]{64}"', "", text, count=1)
        PACKAGE.write_text(text, encoding="utf-8")
        self.assert_trips("the package certifies all four sources, including layoutOverrides")

    def test_release_downgraded_to_an_unapproved_candidate(self):
        """A released package must carry the approved lifecycle it claims."""
        self.edit(PACKAGE, '"status": "APPROVED_STABLE",', '"status": "OWNER_GATE_OPEN",')
        self.assert_trips("the package records the approved corrective-release lifecycle")

    # ── 23-28 · release-mode protections ─────────────────────────────────────

    def test_v1_1_release_record_missing(self):
        """A released package must carry a release record for its own version."""
        RELEASE.unlink()
        self.addCleanup(self.restore_missing)
        self.assert_trips("history holds exactly the four canonical records, two per approved version")

    def test_print_gate_downgraded(self):
        """The physical-print attestation may not be weakened after approval."""
        self.edit_record(RELEASE, lambda r: r.__setitem__("acceptedPrintStatus", "NOT_RUN"))
        self.assert_trips("the v1.1 release record records the physical print gate")

    def test_prior_v1_0_release_dropped(self):
        """v1.0 must stay represented as the prior approved release."""
        self.edit_record(RELEASE, lambda r: r.__setitem__("priorApprovedReleases", []))
        self.assert_trips("the v1.1 record represents exactly one prior approved release, v1.0")

    def test_prior_release_rewritten_to_describe_v1_1(self):
        """The prior-release block must keep v1.0's own page counts, not v1.1's."""
        self.edit_record(RELEASE, lambda r: r["priorApprovedReleases"][0]["rolePageCounts"]
                         .__setitem__("teacher", 9))
        self.assert_trips("the prior release carries v1.0's own hashes, baselines and page counts")

    def test_v1_1_baselines_reverted_to_v1_0(self):
        """v1.0 markup must never be able to satisfy the v1.1 baselines."""
        text = (ROOT / "apps/curriculum-editor/tests/validate_static.py").read_text(encoding="utf-8")
        static_path = ROOT / "apps/curriculum-editor/tests/validate_static.py"
        self.addCleanup(lambda: static_path.write_text(text, encoding="utf-8"))
        static_path.write_text(text.replace(
            '"SSS-C2-CASE01": {"student": "6f02de8a1f56bada6ef119061ebe0c47335aaefd2a3fd6943f639409421aff4c", "teacher": "12df1cfccead45cb0c37441b433ff13feefc5b335defe1b6046b7f9235976e14", "answer": "b72e77f7d24f4c6c3ceaebd0bf8152fa0a0e1dc8996a980b2b68fc6a2e542ae1"}',
            '"SSS-C2-CASE01": {"student": "d423e389da2a3907a042430505aee6127a064d0c1231889a73a035d47000c425", "teacher": "b717bbc1b39df84b7006a5972d51a87057d35492f0add63c58676db941bed3b8", "answer": "52fe5e018b612d871193cdb9615af29303a86ea10552f745cf5ab38e85278afa"}'),
            encoding="utf-8")
        self.assert_trips("the shared approved-baseline map holds the v1.1 baselines, not v1.0's")

    def test_false_certified_source_pin(self):
        """A pin must contain the sources it certifies — the exact v1.0 defect."""
        self.edit_record(RELEASE, lambda r: r.__setitem__(
            "canonicalSourceApprovalCommit", "864156f068cf89b595e1a394f1a4294c839f2876"))
        self.assert_trips("canonicalSourceApprovalCommit contains all four source blobs "
                          "the record certifies")

    def test_retained_v1_0_record_deleted(self):
        """v1.0 history is frozen evidence and may not be removed."""
        RETAINED_RELEASE.unlink()
        self.addCleanup(self.restore_missing)
        self.assert_trips("history holds exactly the four canonical records, two per approved version")

    def test_retained_v1_0_approval_rewritten_to_describe_v1_1(self):
        """The v1.0 approval record may not be edited to describe the corrective release."""
        body = RETAINED_APPROVAL.read_text(encoding="utf-8")
        RETAINED_APPROVAL.write_text(body.replace("Release status: **APPROVED_STABLE**",
                                                  "Release status: **APPROVED_STABLE** (superseded by v1.1)"),
                                     encoding="utf-8")
        self.assert_trips("both retained v1.0 records are byte-identical to synchronised main")


if __name__ == "__main__":
    unittest.main(verbosity=2)
