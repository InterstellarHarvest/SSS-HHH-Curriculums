#!/usr/bin/env python3
"""Focused deterministic checks for the final SSS rendered-surface finding."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "sss/campaign-1/case-01-iss-greenhouse/source"
CONTENT = CASE / "content.html"
PACKAGE = CASE / "case-package.json"
COMPONENTS = ROOT / "shared/implementation/editor-shell/v1.0/curriculum-components.css"
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"
PLAN = ROOT / "sss/audit/final/SSS_FINAL_VISUAL_MODERNIZATION_PLAN_v1.0.md"
HANDOFF = ROOT / "sss/audit/final/SSS_VISUAL_MODERNIZATION_DESKTOP_BROWSER_HANDOFF_v1.0.md"

FROZEN_HASHES = {
    "content.html": "ab4aece5aea687efa477148af920c96aa24208d9e428100b6f2c80d40fd774a1",
    "presentation.css": "3b1fd1313b0388ba754d9fc982aa9a401cb060be4169c7834a6bacc08778ad41",
    "layout-overrides.json": "2f611b019f9b78f231d2bd91410560da4fd49a4f7abd095d0ce3120536500781",
    "case-package.json": "926b6bcbf0fdf59f234cd59527aab16a672650edc905cd61cbe1f7859dd454e8",
    "task-registry.js": "4c16e90619c69599721e766a9a8f8637f92ab431441c4b685a6458197265340d",
}

TOKEN_EXCEPTION = '''"SSS-C1-CASE01": ["--panel", "--panel-light", "--neutral-field", "--institution", "--botanical", "--accent-dark", "--accent-pale", "--primary", "--secondary", "--soft", "--caution", "--caution-field"],
              "SSS-C1-CASE02": ["--panel", "--panel-light", "--cyan-dark", "--slate", "--primary", "--secondary", "--soft", "--caution-field"],
              "SSS-C1-CASE06": ["--cyan-dark", "--slate"]'''


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def neutral_hex(value: str) -> bool:
    match = re.fullmatch(r"#([0-9a-fA-F]{6})", value)
    if not match:
        return False
    digits = match.group(1)
    return digits[0:2].lower() == digits[2:4].lower() == digits[4:6].lower()


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        checks.append((name, bool(passed), str(detail)))

    content = CONTENT.read_text(encoding="utf-8")
    package = json.loads(PACKAGE.read_text(encoding="utf-8"))
    css = COMPONENTS.read_text(encoding="utf-8")
    harness = HARNESS.read_text(encoding="utf-8")
    plan = " ".join(PLAN.read_text(encoding="utf-8").split())
    handoff = " ".join(HANDOFF.read_text(encoding="utf-8").split())

    for name, expected in FROZEN_HASHES.items():
        actual = sha256(CASE / name)
        check(f"frozen ISS Greenhouse {name} hash remains exact", actual == expected, actual)

    check("Case 01 package identity remains exact", package.get("id") == "SSS-C1-CASE01" and package.get("version") == "1.2", package.get("id"))
    check("Case 01 keeps shared visual styles enabled", package.get("presentation", {}).get("sharedVisualStyles") is True)
    check("Case 01 package retains the four printable roles", package.get("supportedRoles") == ["student", "teacher", "answer", "accessible"], package.get("supportedRoles"))
    check("Case 01 role page counts remain 3 / 8 / 3 / 6", {role: value["pageCount"] for role, value in package["rolePageStructure"].items()} == {"student": 3, "teacher": 8, "answer": 3, "accessible": 6})
    check("Case 01 package pins the frozen content hash", package["sourceHashes"]["content"] == FROZEN_HASHES["content.html"])
    check("Case 01 package pins the frozen presentation hash", package["sourceHashes"]["presentation"] == FROZEN_HASHES["presentation.css"])
    check("Case 01 package pins the frozen task-registry hash", package["sourceHashes"]["taskRegistry"] == FROZEN_HASHES["task-registry.js"])
    check("Case 01 package pins the frozen layout hash", package["sourceHashes"]["layoutOverrides"] == FROZEN_HASHES["layout-overrides.json"])

    check("source retains exactly four neutral callouts", len(re.findall(r'class="callout callout-neutral(?: optional-extension)?"', content)) == 4)
    check("source retains exactly two optional-extension callouts", content.count('class="callout callout-neutral optional-extension"') == 2)
    check("source retains exactly one success callout", content.count('class="callout callout-success"') == 1)

    block_match = re.search(
        r"/\*\n \* Grayscale-system correction: ISS Greenhouse callout fills\.(.*?)"
        r"(?=/\* END SSS/HHH EXPLANATORY-VISUAL PRIMITIVES \*/)",
        css,
        flags=re.DOTALL,
    )
    block = block_match.group(0) if block_match else ""
    check("GS01 correction is inside the extracted shared visual layer", bool(block_match))
    check("GS01 correction is scoped exactly to grayscale Case 01", block.count('.worksheet-document.grayscale[data-case-id="SSS-C1-CASE01"]') == 2, block)
    check("GS01 correction targets neutral callouts", ".callout-neutral" in block)
    check("GS01 correction targets success callouts", ".callout-success" in block)
    check("GS01 correction does not target color-mode Case 01", '.worksheet-document[data-case-id="SSS-C1-CASE01"]' not in block)
    check("GS01 correction authors no layout geometry", not re.search(r"\b(?:width|height|min-height|max-height|margin|padding|display|position)\s*:", block))
    check("GS01 correction changes backgrounds only", len(re.findall(r"^\s*[a-z-]+\s*:", block, flags=re.MULTILINE)) == 2)

    fills = re.findall(r"background-color:\s*(#[0-9a-fA-F]{6})", block)
    check("GS01 correction authors exactly two rendered fills", len(fills) == 2, fills)
    check("both GS01 rendered fills are neutral RGB", len(fills) == 2 and all(neutral_hex(value) for value in fills), fills)
    check("success fill remains darker than neutral fill", fills == ["#f2f2f2", "#e6e6e6"], fills)

    check("harness removes the inherited tinted-fill exception map", "knownTintedGrayscaleFills" not in harness)
    check("harness expects an empty tinted-fill set", "const expectedTintedFills = [];" in harness)
    check("harness retains the rendered-surface oracle", 'workspace.querySelectorAll(".callout,.data-table th,.teacher-card,.canonical-phrase-bank,.optional-extension")' in harness)
    check("harness retains the computed-background oracle", "win.getComputedStyle(node).backgroundColor" in harness)
    check("harness retains the stable rendered-fill assertion name", "grayscale rendered tinted fills match its recorded state exactly" in harness)
    check("harness preserves all three dormant-token records exactly", TOKEN_EXCEPTION in harness)
    check("harness preserves the accepted assertion registration count", harness.count("check(") == 416, harness.count("check("))

    check(
        "plan records GS01 as a 35-of-36 implementation candidate",
        all(token in plan for token in ("Implementation candidate — C1C1-GS01 grayscale-system correction", "35 of 36 completed / 1 of 36 remaining", "C1C1-GS01", "IMPLEMENTED-CANDIDATE", "Mac/Google Chrome")),
    )
    check("plan preserves the final-finding boundary pending rendered acceptance", "Do not advance the inventory to 36/36" in plan and "No rendered acceptance is inferred from static validation" in plan)
    check("plan preserves dormant-token audit scope", "Cases 01, 02 and 06" in plan and "dormant" in plan and "zero tinted rendered fills" in plan)
    check("plan lists all five frozen Case 01 hashes", all(value in plan for value in FROZEN_HASHES.values()))
    check(
        "handoff defines the exact GS01 rendered gate",
        all(token in handoff for token in ("Candidate final finding — C1C1-GS01 grayscale-system correction", "all four printable roles", "zero tinted rendered fills", "#f2f2f2", "#e6e6e6", "2375/2375 PASS")),
    )
    check("handoff preserves canonical registration and same-Mac disposition boundary", "Canonical project registration remains 2375" in handoff and "do not infer acceptance" in handoff)
    check("handoff keeps the inventory at 35/36 pending acceptance", "inventory remains **35 of 36 completed**" in handoff and "`C1C1-GS01` remains unaccepted" in handoff)
    check("handoff prohibits PDF and static-baseline repinning", "Do not run PDF automation" in handoff and "do not run or re-pin `validate_static.py`" in handoff)
    check("handoff lists all five frozen Case 01 hashes", all(value in handoff for value in FROZEN_HASHES.values()))

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f" — {detail}" if detail and not ok else ""))
    print(f"\nGrayscale-system validator: {passed}/{len(checks)} PASS")
    return 0 if passed == len(checks) == 42 else 1


if __name__ == "__main__":
    raise SystemExit(main())
