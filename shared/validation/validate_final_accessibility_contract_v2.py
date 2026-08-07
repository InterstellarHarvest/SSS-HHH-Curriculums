#!/usr/bin/env python3
"""Audit-specific Accessible remediation validator v2.

Heavy Hands Task 5 intentionally ends at the five-source contribution/limit table;
it has no separate learner synthesis control. Remove that nonexistent field from
the protected-blank list, then run the governing v1 exact accessibility checks.
"""

from __future__ import annotations

import sys

import validate_final_accessibility_contract as v1

v1.MUST_REMAIN_BLANK["SSS-C2-CASE01"] = [
    pid for pid in v1.MUST_REMAIN_BLANK.get("SSS-C2-CASE01", []) if pid != "a5-synthesis"
]

if __name__ == "__main__":
    sys.exit(v1.main())
