#!/usr/bin/env python3
"""Corrective-release lifecycle rules for canonical case packages.

The repository previously modelled only two lifecycle situations: a package that
has never been released (no ``history/`` at all), and an approved package (a
release record for its current version). Reopening an approved case for
correction is neither. Its current version is unreleased, but the records for the
versions that *were* approved must survive untouched.

This module states the distinction precisely, so that reopening a case never
requires deleting the evidence of its earlier approvals.

A package whose status is not ``APPROVED_STABLE`` may retain ``history/`` records,
but only for versions strictly below its own, and only if those records are
genuine canonical records. It may never carry a record for its own version, and
it may never point at one.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

RELEASE_RE = re.compile(r"^release-v(\d+)\.(\d+)\.json$")
APPROVAL_RE = re.compile(r"^CASE(\d{2})_OWNER_APPROVAL_v(\d+)\.(\d+)\.md$")
VERSION_RE = re.compile(r"^(\d+)\.(\d+)$")
IGNORED = {".DS_Store"}


def parse_version(value: object) -> tuple[int, int] | None:
    """Return a numerically comparable version, or None when malformed.

    Two components only, matching the package and release-history schemas.
    Comparison is numeric so that 1.10 correctly outranks 1.9.
    """
    if not isinstance(value, str):
        return None
    match = VERSION_RE.match(value)
    return (int(match.group(1)), int(match.group(2))) if match else None


def classify(name: str) -> tuple[str, tuple[int, int]] | None:
    """Classify a ``history/`` filename as a canonical record, or None."""
    release = RELEASE_RE.match(name)
    if release:
        return "release", (int(release.group(1)), int(release.group(2)))
    approval = APPROVAL_RE.match(name)
    if approval:
        return "approval", (int(approval.group(2)), int(approval.group(3)))
    return None


def _record_findings(path: Path, case_id: str, declared: tuple[int, int]) -> list[str]:
    """Confirm a retained release record really is that case's record for that version."""
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"{path.name} is not readable canonical JSON ({error.__class__.__name__})"]
    findings = []
    if record.get("caseId") != case_id:
        findings.append(f"{path.name} records caseId {record.get('caseId')!r}, not {case_id}")
    internal = parse_version(record.get("curriculumVersion"))
    if internal != declared:
        findings.append(
            f"{path.name} filename version and curriculumVersion "
            f"{record.get('curriculumVersion')!r} disagree")
    if record.get("status") != "APPROVED_STABLE":
        findings.append(f"{path.name} is retained as history but is not an approved release")
    return findings


def history_findings(case_root: Path, case_id: str, package: dict,
                     registry: dict | None = None) -> list[str]:
    """Return every lifecycle violation for one case, or an empty list.

    Applies to both released and unreleased packages: the shared rules are that
    ``history/`` holds only canonical records, and that no record may claim a
    version above the package's own.
    """
    findings: list[str] = []
    current = parse_version(package.get("version"))
    if current is None:
        return [f"package version {package.get('version')!r} is not a two-component version"]

    approved = package.get("status") == "APPROVED_STABLE"
    history = case_root / "history"
    entries = ([p for p in sorted(history.iterdir()) if p.name not in IGNORED]
               if history.is_dir() else [])

    releases: dict[tuple[int, int], Path] = {}
    approvals: dict[tuple[int, int], Path] = {}
    for entry in entries:
        if not entry.is_file():
            findings.append(f"history/{entry.name} is not a canonical record file")
            continue
        kind = classify(entry.name)
        if kind is None:
            findings.append(f"history/{entry.name} is not a canonical release or approval record")
            continue
        label, version = kind
        (releases if label == "release" else approvals)[version] = entry

    for version, path in releases.items():
        findings.extend(_record_findings(path, case_id, version))

    # No record may ever claim a version above the package's own.
    for label, table in (("release", releases), ("owner-approval", approvals)):
        for version in sorted(v for v in table if v > current):
            findings.append(
                f"history/{table[version].name} is a {label} record for "
                f"{version[0]}.{version[1]}, above the package version "
                f"{current[0]}.{current[1]}")

    if approved:
        return findings

    # Unreleased: a first release, or a corrective candidate.
    if "releaseHistory" in package:
        findings.append("an unreleased package declares a releaseHistory pointer")
    if registry is not None and "releaseHistory" in registry:
        findings.append("an unreleased task registry declares a releaseHistory pointer")
    if current in releases:
        findings.append(
            f"history/{releases[current].name} releases the candidate's own version "
            f"{current[0]}.{current[1]}")
    if current in approvals:
        findings.append(
            f"history/{approvals[current].name} approves the candidate's own version "
            f"{current[0]}.{current[1]}")

    # Every retained record must belong to a genuinely earlier approved release,
    # and an approval record must accompany a release record for that version.
    for version in sorted(approvals):
        if version < current and version not in releases:
            findings.append(
                f"history/{approvals[version].name} claims an approval for "
                f"{version[0]}.{version[1]} with no retained release record")
    return findings


__all__ = ["parse_version", "classify", "history_findings"]
