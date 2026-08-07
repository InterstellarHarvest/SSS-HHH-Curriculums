#!/usr/bin/env python3
"""Remove two release-specific lifecycle assertions from the shared browser harness.

The browser harness already tests package/registry version parity and has separate
branches for APPROVED_STABLE versus development/DRAFT UI. Two older one-off
assertions still hard-coded C1 Case 03 as approved v1.1 and C1 Case 04 as approved
v1.0. Those assertions make the otherwise lifecycle-aware harness reject a valid
corrective DRAFT candidate before its render/editor behavior can be tested.

This patch keeps equivalent useful checks while making them release-state neutral:
- initial Case 03 load must expose the expected package identity/schema/version and
  a recognized lifecycle state;
- Case 04 package lifecycle must match its central registry entry.

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


def main() -> int:
    text = HARNESS.read_text(encoding="utf-8")
    changed = False
    if OLD_CASE03 in text:
        text = text.replace(OLD_CASE03, NEW_CASE03, 1)
        changed = True
    elif NEW_CASE03 not in text:
        raise SystemExit("Case 03 browser lifecycle assertion is neither the expected legacy nor remediated form")

    if OLD_CASE04 in text:
        text = text.replace(OLD_CASE04, NEW_CASE04, 1)
        changed = True
    elif NEW_CASE04 not in text:
        raise SystemExit("Case 04 browser lifecycle assertion is neither the expected legacy nor remediated form")

    if changed:
        HARNESS.write_text(text, encoding="utf-8")
        print("browser harness lifecycle assertions updated")
    else:
        print("browser harness lifecycle assertions already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
