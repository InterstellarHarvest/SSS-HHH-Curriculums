#!/usr/bin/env python3
"""Build Case 03 master and role HTML from the canonical shared shell."""
from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
ASSEMBLER = REPO / "shared/implementation/editor-shell/v1.0/assemble_editable_master.py"
CONFIG = ROOT / "source/editor/case03-editor-config.json"
MASTER = ROOT / "master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html"
PUBLISHED = ROOT / "published"


def load_assembler():
    spec = importlib.util.spec_from_file_location("sss_editor_shell_assembler", ASSEMBLER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load assembler: {ASSEMBLER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_assembler()
    written = module.write_outputs(CONFIG, MASTER, PUBLISHED)
    print(f"HTML-only build: {len(written)} files")
    for path in written:
        print(path.relative_to(REPO))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
