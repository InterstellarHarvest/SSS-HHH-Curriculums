#!/usr/bin/env python3
"""Unit and round-trip tests for the loopback layout persistence boundary."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
from authoring_service import AuthoringError, apply_layout_changes, repository_id  # noqa: E402


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


class AuthoringServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="layout-service-test.")
        self.root = Path(self.temporary.name)
        self.source = self.root / "sss/campaign-1/case-01/source"
        self.source.mkdir(parents=True)
        registry = {
            "curricula": [{"campaigns": [{"cases": [{"id": "SSS-C1-CASE01", "editorPackage": "sss/campaign-1/case-01/source/case-package.json"}]}]}]
        }
        registry_path = self.root / "shared/implementation"
        registry_path.mkdir(parents=True)
        (registry_path / "case-registry.v2.json").write_text(json.dumps(registry), encoding="utf-8")
        self.content = b'''<main><section class="page" data-page-id="accessible-1" data-role="accessible"><h2 data-task-id="2">Task 2</h2><div data-persist-id="eligible" data-response></div><div data-persist-id="locked" data-response></div><div class="canonical-cer"><div data-persist-id="cer" data-response></div></div></section><section class="page" data-page-id="student-1" data-role="student"><h2 data-task-id="2">Task 2</h2><div data-persist-id="student" data-response></div></section></main>'''
        self.presentation = b".page{width:8.5in;height:11in}"
        (self.source / "content.html").write_bytes(self.content)
        (self.source / "presentation.css").write_bytes(self.presentation)
        self.layout = {
            "schemaVersion": 1,
            "caseId": "SSS-C1-CASE01",
            "edition": "accessible",
            "stepPx": 4,
            "areas": [{"id": "SSS-C1-CASE01:accessible:t2:eligible", "persistId": "eligible", "pageId": "accessible-1", "taskId": 2, "label": "Eligible response", "minPx": 32, "maxPx": 400}],
            "lockedAreas": [
                {"persistId": "locked", "reason": "compact-answer"},
                {"persistId": "cer", "reason": "cer"},
            ],
            "overrides": {},
        }
        self.write_layout()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_layout(self) -> None:
        layout_bytes = (json.dumps(self.layout, indent=2) + "\n").encode()
        (self.source / "layout-overrides.json").write_bytes(layout_bytes)
        package = {
            "id": "SSS-C1-CASE01",
            "content": {"source": "sss/campaign-1/case-01/source/content.html"},
            "presentation": {"source": "sss/campaign-1/case-01/source/presentation.css"},
            "layoutOverrides": {"source": "sss/campaign-1/case-01/source/layout-overrides.json", "schemaVersion": 1},
            "sourceHashes": {"content": digest(self.content), "presentation": digest(self.presentation), "layoutOverrides": digest(layout_bytes)},
        }
        (self.source / "case-package.json").write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")

    def payload(self, **change) -> dict:
        return {
            "schemaVersion": 1,
            "repositoryId": repository_id(self.root),
            "caseId": "SSS-C1-CASE01",
            "edition": "accessible",
            "preconditions": {
                "contentSha256": digest((self.source / "content.html").read_bytes()),
                "presentationSha256": digest((self.source / "presentation.css").read_bytes()),
                "layoutOverridesSha256": digest((self.source / "layout-overrides.json").read_bytes()),
            },
            "changes": [{"id": "SSS-C1-CASE01:accessible:t2:eligible", "heightPx": 120, "sourceHeightPx": 80, **change}],
        }

    @staticmethod
    def passing_validation(root: Path, case_id: str) -> tuple[bool, str]:
        return True, f"focused validation passed for {case_id}"

    def test_round_trip_writes_only_sparse_layout_and_package_hash(self) -> None:
        content_before = (self.source / "content.html").read_bytes()
        presentation_before = (self.source / "presentation.css").read_bytes()
        result = apply_layout_changes(self.root, self.payload(), self.passing_validation)
        stored = json.loads((self.source / "layout-overrides.json").read_text())
        package = json.loads((self.source / "case-package.json").read_text())
        self.assertEqual(stored["overrides"]["SSS-C1-CASE01:accessible:t2:eligible"], {"heightPx": 120, "sourceHeightPx": 80})
        self.assertEqual(package["sourceHashes"]["layoutOverrides"], digest((self.source / "layout-overrides.json").read_bytes()))
        self.assertEqual((self.source / "content.html").read_bytes(), content_before)
        self.assertEqual((self.source / "presentation.css").read_bytes(), presentation_before)
        self.assertEqual(len(result["filesChanged"]), 2)

    def test_reset_to_original_height_removes_sparse_override(self) -> None:
        apply_layout_changes(self.root, self.payload(), self.passing_validation)
        reset_payload = self.payload(heightPx=80, sourceHeightPx=120)
        apply_layout_changes(self.root, reset_payload, self.passing_validation)
        self.assertEqual(json.loads((self.source / "layout-overrides.json").read_text())["overrides"], {})

    def test_hash_conflict_is_rejected_without_writes(self) -> None:
        payload = self.payload()
        payload["preconditions"]["contentSha256"] = "0" * 64
        before = (self.source / "layout-overrides.json").read_bytes()
        with self.assertRaisesRegex(AuthoringError, "Source files changed"):
            apply_layout_changes(self.root, payload, self.passing_validation)
        self.assertEqual((self.source / "layout-overrides.json").read_bytes(), before)

    def test_unknown_and_non_accessible_requests_are_rejected(self) -> None:
        payload = self.payload()
        payload["changes"][0]["id"] = "SSS-C1-CASE01:accessible:t2:unknown"
        with self.assertRaisesRegex(AuthoringError, "Unknown or ineligible"):
            apply_layout_changes(self.root, payload, self.passing_validation)
        payload = self.payload()
        payload["edition"] = "student"
        with self.assertRaisesRegex(AuthoringError, "Only Accessible"):
            apply_layout_changes(self.root, payload, self.passing_validation)

    def test_explicitly_locked_response_is_rejected(self) -> None:
        payload = self.payload()
        payload["changes"][0]["id"] = "SSS-C1-CASE01:accessible:t2:locked"
        with self.assertRaisesRegex(AuthoringError, "Unknown or ineligible"):
            apply_layout_changes(self.root, payload, self.passing_validation)

    def test_malformed_values_arbitrary_fields_and_repository_mismatch_are_rejected(self) -> None:
        payload = self.payload(heightPx="120")
        with self.assertRaisesRegex(AuthoringError, "Height violates"):
            apply_layout_changes(self.root, payload, self.passing_validation)
        payload = self.payload()
        payload["path"] = "/tmp/arbitrary"
        with self.assertRaisesRegex(AuthoringError, "unexpected or missing fields"):
            apply_layout_changes(self.root, payload, self.passing_validation)
        payload = self.payload()
        payload["repositoryId"] = "different-worktree"
        with self.assertRaisesRegex(AuthoringError, "different repository/worktree"):
            apply_layout_changes(self.root, payload, self.passing_validation)

    def test_cer_is_rejected_even_if_manifest_is_accidentally_modified(self) -> None:
        self.layout["areas"][0].update({"id": "SSS-C1-CASE01:accessible:t2:cer", "persistId": "cer"})
        self.write_layout()
        payload = self.payload(id="SSS-C1-CASE01:accessible:t2:cer")
        with self.assertRaisesRegex(AuthoringError, "CER response areas cannot be resized"):
            apply_layout_changes(self.root, payload, self.passing_validation)

    def test_path_traversal_contract_is_rejected(self) -> None:
        package_path = self.source / "case-package.json"
        package = json.loads(package_path.read_text())
        package["layoutOverrides"]["source"] = "../../../../outside/layout-overrides.json"
        package_path.write_text(json.dumps(package), encoding="utf-8")
        with self.assertRaisesRegex(AuthoringError, "escapes the repository|unexpected target"):
            apply_layout_changes(self.root, self.payload(), self.passing_validation)

    def test_validation_failure_rolls_back_both_files(self) -> None:
        layout_before = (self.source / "layout-overrides.json").read_bytes()
        package_before = (self.source / "case-package.json").read_bytes()
        with self.assertRaisesRegex(AuthoringError, "rolled back"):
            apply_layout_changes(self.root, self.payload(), lambda _root, _case: (False, "forced failure"))
        self.assertEqual((self.source / "layout-overrides.json").read_bytes(), layout_before)
        self.assertEqual((self.source / "case-package.json").read_bytes(), package_before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
