"""Strict repository-local persistence for approved Accessible layout changes."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Callable


MAX_REQUEST_BYTES = 256 * 1024
PAYLOAD_FIELDS = {"schemaVersion", "repositoryId", "caseId", "edition", "preconditions", "changes"}
PRECONDITION_FIELDS = {"contentSha256", "presentationSha256", "layoutOverridesSha256"}
CHANGE_FIELDS = {"id", "heightPx", "sourceHeightPx"}


class AuthoringError(Exception):
    """An expected, safe-to-display authoring request failure."""

    def __init__(self, message: str, status: int = 400, code: str = "invalid_request") -> None:
        super().__init__(message)
        self.status = status
        self.code = code


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def repository_id(root: Path) -> str:
    return sha256_bytes(str(root.resolve()).encode("utf-8"))[:24]


def safe_repo_path(root: Path, raw: str, *, suffix: str) -> Path:
    if not isinstance(raw, str) or not raw or raw.startswith(("/", "~")) or "\\" in raw:
        raise AuthoringError("The registered source path is unsafe.", 500, "unsafe_source_path")
    target = (root / raw).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError as exc:
        raise AuthoringError("The registered source path escapes the repository.", 500, "unsafe_source_path") from exc
    if not target.as_posix().endswith(suffix):
        raise AuthoringError("The registered source path has an unexpected target.", 500, "unsafe_source_path")
    return target


def registered_packages(root: Path) -> dict[str, Path]:
    registry_path = root / "shared/implementation/case-registry.v2.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    packages: dict[str, Path] = {}
    for curriculum in registry["curricula"]:
        for campaign in curriculum["campaigns"]:
            for case in campaign["cases"]:
                source = case.get("editorPackage")
                if source:
                    packages[case["id"]] = safe_repo_path(root, source, suffix="/source/case-package.json")
    return packages


def git_revision(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, text=True, capture_output=True, check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "unavailable"


def context_payload(root: Path) -> dict[str, object]:
    return {
        "schemaVersion": 1,
        "repositoryId": repository_id(root),
        "repositoryLabel": root.name,
        "revision": git_revision(root),
        "sourcePersistence": True,
    }


def serialize_sparse_layout(original: bytes, overrides: dict[str, dict[str, int]]) -> bytes:
    marker = b'  "overrides": '
    if original.count(marker) != 1:
        raise AuthoringError("The sparse override source cannot be updated safely.", 409, "invalid_contract")
    prefix = original.split(marker, 1)[0]
    override_text = json.dumps(overrides, indent=2, ensure_ascii=False)
    indented = "\n".join(line if index == 0 else f"  {line}" for index, line in enumerate(override_text.splitlines()))
    return prefix + marker + indented.encode("utf-8") + b"\n}\n"


class SourceResponseIndex(HTMLParser):
    """Resolve persist IDs to source role/page/task and protected CER ancestry."""

    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[dict[str, object]] = [{"role": None, "page": None, "task": None, "cer": False}]
        self.responses: dict[str, dict[str, object]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        parent = self.stack[-1]
        frame = dict(parent)
        classes = set((values.get("class") or "").split())
        if "page" in classes:
            frame["role"] = values.get("data-role")
            frame["page"] = values.get("data-page-id")
            frame["task"] = None
            frame["cer"] = False
        if values.get("data-task-id"):
            frame["task"] = values["data-task-id"]
        if values.get("data-shell-task-heading"):
            frame["task"] = values["data-shell-task-heading"]
        frame["cer"] = bool(frame["cer"] or any("cer" in name.lower() for name in classes) or values.get("data-cer-contract"))
        persist_id = values.get("data-persist-id")
        if persist_id:
            if persist_id in self.responses:
                self.responses[persist_id] = {"duplicate": True}
            else:
                self.responses[persist_id] = dict(frame)
        if tag not in self.VOID:
            self.stack.append(frame)

    def handle_endtag(self, tag: str) -> None:
        if tag not in self.VOID and len(self.stack) > 1:
            completed = self.stack.pop()
            if completed.get("task") != self.stack[-1].get("task") and tag in {"h2", "div"}:
                self.stack[-1]["task"] = completed.get("task")


def validate_manifest(package: dict, package_path: Path, root: Path) -> tuple[Path, Path, Path, dict, bytes, bytes]:
    contract = package.get("layoutOverrides")
    if not isinstance(contract, dict) or set(contract) != {"source", "schemaVersion"} or contract["schemaVersion"] != 1:
        raise AuthoringError("The case has no recognized layout override contract.", 409, "unsupported_contract")
    layout_path = safe_repo_path(root, contract["source"], suffix="/source/layout-overrides.json")
    content_path = safe_repo_path(root, package["content"]["source"], suffix="/source/content.html")
    presentation_path = safe_repo_path(root, package["presentation"]["source"], suffix="/source/presentation.css")
    if layout_path.parent != package_path.parent or content_path.parent != package_path.parent or presentation_path.parent != package_path.parent:
        raise AuthoringError("Registered case sources do not share the case source directory.", 500, "unsafe_source_path")
    layout_bytes = layout_path.read_bytes()
    content_bytes = content_path.read_bytes()
    data = json.loads(layout_bytes)
    if set(data) != {"schemaVersion", "caseId", "edition", "stepPx", "areas", "lockedAreas", "overrides"}:
        raise AuthoringError("The layout override source has an invalid shape.", 409, "invalid_contract")
    if data["schemaVersion"] != 1 or data["caseId"] != package["id"] or data["edition"] != "accessible" or data["stepPx"] != 4:
        raise AuthoringError("The layout override source identity is invalid.", 409, "invalid_contract")
    if package.get("sourceHashes", {}).get("layoutOverrides") != sha256_bytes(layout_bytes):
        raise AuthoringError("The package layout hash is not synchronized.", 409, "source_conflict")
    return layout_path, content_path, presentation_path, data, layout_bytes, content_bytes


def exact_object(value: object, fields: set[str], label: str) -> dict:
    if not isinstance(value, dict) or set(value) != fields:
        raise AuthoringError(f"{label} has unexpected or missing fields.")
    return value


def validate_changes(data: dict, content_bytes: bytes, changes: object) -> list[dict]:
    if not isinstance(changes, list) or not 1 <= len(changes) <= 100:
        raise AuthoringError("Select between 1 and 100 layout changes.")
    areas = {area["id"]: area for area in data["areas"]}
    if len(areas) != len(data["areas"]):
        raise AuthoringError("The eligibility registry contains duplicate IDs.", 409, "invalid_contract")
    parser = SourceResponseIndex()
    parser.feed(content_bytes.decode("utf-8"))
    validated: list[dict] = []
    seen: set[str] = set()
    for raw in changes:
        change = exact_object(raw, CHANGE_FIELDS, "A layout change")
        area_id = change["id"]
        if area_id in seen:
            raise AuthoringError("A layout change ID was submitted more than once.")
        seen.add(area_id)
        area = areas.get(area_id)
        if not area:
            raise AuthoringError(f"Unknown or ineligible response area: {area_id}", 403, "ineligible_area")
        height = change["heightPx"]
        source_height = change["sourceHeightPx"]
        if not isinstance(height, int) or isinstance(height, bool) or height % data["stepPx"] or not area["minPx"] <= height <= area["maxPx"]:
            raise AuthoringError(f"Height violates the 4px snap or declared bounds: {area_id}")
        if not isinstance(source_height, int) or isinstance(source_height, bool) or source_height < 16 or source_height > 2000:
            raise AuthoringError(f"Source height is invalid: {area_id}")
        source = parser.responses.get(area["persistId"])
        if not source or source.get("duplicate"):
            raise AuthoringError(f"Eligible response locator is missing or ambiguous: {area_id}", 409, "source_conflict")
        if source.get("role") != "accessible" or source.get("page") != area["pageId"] or str(source.get("task")) != str(area["taskId"]):
            raise AuthoringError(f"Eligible response locator no longer matches its declared page/task: {area_id}", 409, "source_conflict")
        if source.get("cer"):
            raise AuthoringError(f"CER response areas cannot be resized: {area_id}", 403, "cer_protected")
        validated.append({"area": area, **change})
    return validated


def atomic_write(path: Path, value: bytes) -> None:
    with tempfile.NamedTemporaryFile(prefix=f".{path.name}.", dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(value)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def default_validation(root: Path, case_id: str) -> tuple[bool, str]:
    validator = root / "shared/validation/validate_layout_overrides.py"
    result = subprocess.run(
        [sys.executable, str(validator), "--case", case_id], cwd=root, text=True, capture_output=True, check=False,
    )
    detail = (result.stdout + result.stderr).strip()
    return result.returncode == 0, detail


def apply_layout_changes(
    root: Path,
    payload: object,
    validate: Callable[[Path, str], tuple[bool, str]] = default_validation,
) -> dict[str, object]:
    request = exact_object(payload, PAYLOAD_FIELDS, "The authoring request")
    if request["schemaVersion"] != 1 or request["edition"] != "accessible":
        raise AuthoringError("Only Accessible edition layout schema v1 may be persisted.", 403, "edition_protected")
    if request["repositoryId"] != repository_id(root):
        raise AuthoringError("The draft belongs to a different repository/worktree.", 409, "repository_conflict")
    packages = registered_packages(root)
    package_path = packages.get(request["caseId"])
    if not package_path:
        raise AuthoringError("The requested case is not registered.", 404, "unknown_case")
    package_bytes = package_path.read_bytes()
    package = json.loads(package_bytes)
    layout_path, content_path, presentation_path, data, layout_bytes, content_bytes = validate_manifest(package, package_path, root)
    preconditions = exact_object(request["preconditions"], PRECONDITION_FIELDS, "Source preconditions")
    actual = {
        "contentSha256": sha256_bytes(content_bytes),
        "presentationSha256": sha256_bytes(presentation_path.read_bytes()),
        "layoutOverridesSha256": sha256_bytes(layout_bytes),
    }
    if preconditions != actual:
        raise AuthoringError("Source files changed after this draft was created. Inspect or discard the stale draft.", 409, "source_conflict")
    if package["sourceHashes"]["content"] != actual["contentSha256"] or package["sourceHashes"]["presentation"] != actual["presentationSha256"]:
        raise AuthoringError("Package source hashes are not synchronized.", 409, "source_conflict")
    validated = validate_changes(data, content_bytes, request["changes"])
    overrides = dict(data["overrides"])
    applied: list[dict[str, object]] = []
    for change in validated:
        area_id = change["id"]
        previous = overrides.get(area_id)
        original_height = previous["sourceHeightPx"] if previous else change["sourceHeightPx"]
        if change["heightPx"] == original_height:
            overrides.pop(area_id, None)
        else:
            overrides[area_id] = {"heightPx": change["heightPx"], "sourceHeightPx": original_height}
        applied.append({
            "id": area_id,
            "pageId": change["area"]["pageId"],
            "taskId": change["area"]["taskId"],
            "label": change["area"]["label"],
            "fromPx": previous["heightPx"] if previous else change["sourceHeightPx"],
            "toPx": change["heightPx"],
        })
    data["overrides"] = {key: overrides[key] for key in sorted(overrides)}
    new_layout = serialize_sparse_layout(layout_bytes, data["overrides"])
    old_layout_hash = package["sourceHashes"]["layoutOverrides"]
    new_layout_hash = sha256_bytes(new_layout)
    if package_bytes.count(old_layout_hash.encode("ascii")) != 1:
        raise AuthoringError("The package layout hash cannot be updated safely.", 409, "invalid_contract")
    new_package = package_bytes.replace(old_layout_hash.encode("ascii"), new_layout_hash.encode("ascii"), 1)
    try:
        atomic_write(layout_path, new_layout)
        atomic_write(package_path, new_package)
        passed, detail = validate(root, request["caseId"])
        if not passed:
            raise AuthoringError(f"Focused validation failed; source changes were rolled back.\n{detail}", 422, "validation_failure")
    except Exception:
        atomic_write(layout_path, layout_bytes)
        atomic_write(package_path, package_bytes)
        raise
    return {
        "schemaVersion": 1,
        "caseId": request["caseId"],
        "edition": "accessible",
        "applied": applied,
        "filesChanged": [str(layout_path.relative_to(root.resolve())), str(package_path.resolve().relative_to(root.resolve()))],
        "sourceHashes": {**actual, "layoutOverridesSha256": new_layout_hash},
        "validation": {"passed": True, "detail": detail},
    }
