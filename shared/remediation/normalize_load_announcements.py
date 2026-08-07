#!/usr/bin/env python3
"""Make the screen-reader load announcement lifecycle-neutral.

Campaign 1 Cases 04-07 announced themselves as an "approved package loaded". That was
true when those packages were approved releases; the final remediation reopened all
thirteen as corrective DRAFT candidates, so the wording now tells a screen-reader user
something about the package's lifecycle that is not true. Campaign 1 Cases 01-03 and all
of Campaign 2 never used the word, so the fix also removes a gratuitous inconsistency.

"approved package loaded" -> "curriculum package loaded".

Nothing else in the announcement changes: the case name, the version and the
"Student Mission selected." role sentence are all preserved, which is what the browser
harness and the corrective-candidate contract actually assert. The wording carries no
lifecycle claim afterwards, so it stays correct through approval and re-release and will
not need revisiting.

Idempotent.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

OLD = "approved package loaded"
NEW = "curriculum package loaded"


def normalize(package_path: Path, apply: bool) -> bool:
    package = json.loads(package_path.read_text(encoding="utf-8"))
    accessibility = package.get("accessibility") or {}
    announcement = accessibility.get("loadAnnouncement")
    if not isinstance(announcement, str) or OLD not in announcement:
        return False
    if apply:
        accessibility["loadAnnouncement"] = announcement.replace(OLD, NEW)
        package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{package.get('id')}: {announcement!r} -> {announcement.replace(OLD, NEW)!r}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    changed = 0
    for package_path in sorted((ROOT / "sss").glob("campaign-*/*/source/case-package.json")):
        if normalize(package_path, args.apply):
            changed += 1
    print(f"Load-announcement normalization: {changed} package(s) "
          f"{'updated' if args.apply else 'pending'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
