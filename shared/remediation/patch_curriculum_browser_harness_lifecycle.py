#!/usr/bin/env python3
"""Make the shared curriculum-editor browser harness corrective-candidate aware.

The browser harness already tests package/registry version parity and editor behavior,
but several historical assertions were frozen to old approved-release state. The final
SSS corrective candidates intentionally reopen all packages as DRAFT, and Case 04 gains
one additional Accessible resizable response field during the audited remediation.

This patch keeps the harness independent from the package sources while removing only
stale release-specific assumptions:
- initial Case 03 load must expose the expected package identity/schema/version and a
  recognized lifecycle state rather than one old approved version/date;
- Case 04 lifecycle must match its central registry entry rather than one old release;
- the independently audited Case 04 Accessible resize-count expectation moves 8 -> 9.

All other browser assertions remain byte-identical. Idempotent.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HARNESS = ROOT / "apps/curriculum-editor/tests/browser-harness.html"

OLD_CASE03 = '''      check("registry-loaded Case 03 package is current approved stable with owner PASS", api.getPackage().id === "SSS-C1-CASE03" && api.getPackage().schemaVersion === 2 && api.getPackage().version === "1.1" && api.getPackage().status === "APPROVED_STABLE" && api.getPackage().approval?.date === "2026-07-31" && api.getPackage().approval?.owner === "Nate / Owner" && api.getPackage().approval?.status === "APPROVED" && api.getPackage().approval?.printStatus === "PASS");'''
NEW_CASE03 = '''      check("registry-loaded Case 03 package exposes current package identity and lifecycle", api.getPackage().id === "SSS-C1-CASE03" && api.getPackage().schemaVersion === 2 && typeof api.getPackage().version === "string" && api.getPackage().version.length > 0 && ["DRAFT", "APPROVED_STABLE"].includes(api.getPackage().status));'''

OLD_CASE04 = '''        if (item.id === "SSS-C1-CASE04") check("Case 04 loads as the owner-approved v1.0 release", api.getPackage().status === "APPROVED_STABLE" && api.getPackage().approval.date === "2026-08-01" && api.getPackage().approval.owner === "Nate / Owner" && api.getPackage().approval.status === "APPROVED" && api.getPackage().approval.printStatus === "PASS");'''
NEW_CASE04 = '''        if (item.id === "SSS-C1-CASE04") check("Case 04 package lifecycle matches the registry entry", api.getPackage().status === item.status);'''

OLD_CASE04_COUNT = '''"SSS-C1-CASE04": 8'''
NEW_CASE04_COUNT = '''"SSS-C1-CASE04": 9'''


def replace_or_confirm(text: str, old: str, new: str, label: str) -> tuple[str, bool]:
    if old in text:
        return text.replace(old, new, 1), True
    if new in text:
        return text, False
    raise SystemExit(f"{label} is neither the expected legacy nor remediated form")


def main() -> int:
    text = HARNESS.read_text(encoding="utf-8")
    changed = False

    text, did_change = replace_or_confirm(text, OLD_CASE03, NEW_CASE03, "Case 03 browser lifecycle assertion")
    changed |= did_change
    text, did_change = replace_or_confirm(text, OLD_CASE04, NEW_CASE04, "Case 04 browser lifecycle assertion")
    changed |= did_change
    text, did_change = replace_or_confirm(text, OLD_CASE04_COUNT, NEW_CASE04_COUNT, "Case 04 Accessible resize-count assertion")
    changed |= did_change

    if changed:
        HARNESS.write_text(text, encoding="utf-8")
        print("browser harness corrective-candidate assertions updated")
    else:
        print("browser harness corrective-candidate assertions already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
