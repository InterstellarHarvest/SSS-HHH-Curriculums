#!/usr/bin/env python3
"""Refresh manifest file metadata and a case-local SHA-256 ledger."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


REPO = Path(__file__).resolve().parents[2]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def refresh_entry(entry: dict[str, Any], case_root: Path) -> Path:
    path = case_root / entry["path"]
    if not path.is_file():
        raise FileNotFoundError(path)
    entry["sha256"] = digest(path)
    entry["bytes"] = path.stat().st_size
    return path


def refresh_manifest(manifest_path: Path) -> tuple[dict[str, Any], list[Path]]:
    case_root = manifest_path.parent
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    files: list[Path] = []

    if isinstance(manifest.get("current_master"), dict):
        files.append(refresh_entry(manifest["current_master"], case_root))
    for output in manifest.get("outputs", {}).values():
        if isinstance(output.get("html"), dict):
            files.append(refresh_entry(output["html"], case_root))
    for collection in ("controlled_sources", "reports", "validation_files", "files"):
        for entry in manifest.get(collection, []):
            files.append(refresh_entry(entry, case_root))

    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest, files


def unique_paths(paths: Iterable[Path]) -> list[Path]:
    return sorted(set(path.resolve() for path in paths), key=lambda path: str(path))


def write_ledger(manifest_path: Path, ledger_path: Path, represented: list[Path]) -> None:
    case_root = manifest_path.parent
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("artifact_policy") == "HTML_ONLY":
        paths = [case_root / manifest["current_master"]["path"]]
        paths.extend(
            case_root / output["html"]["path"]
            for output in manifest["outputs"].values()
        )
    else:
        paths = [manifest_path.resolve(), *represented]
    if "files" not in manifest and manifest.get("artifact_policy") != "HTML_ONLY":
        paths.extend((case_root / "README.md", case_root / "published/README.md"))
        paths.extend((case_root / "published").glob("*"))
    paths = [path for path in unique_paths(paths) if path.is_file() and path.resolve() != ledger_path.resolve()]
    lines = [
        f"{digest(path)}  {path.relative_to(case_root)}"
        for path in sorted(paths, key=lambda item: str(item.relative_to(case_root)))
    ]
    ledger_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args()
    manifest_path = args.manifest.resolve()
    ledger_path = args.ledger.resolve()
    _, represented = refresh_manifest(manifest_path)
    write_ledger(manifest_path, ledger_path, represented)
    print(f"Refreshed manifest: {manifest_path.relative_to(REPO)}")
    print(f"Refreshed checksum ledger: {ledger_path.relative_to(REPO)}")
    print(f"Ledger entries: {len(ledger_path.read_text(encoding='utf-8').splitlines())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
