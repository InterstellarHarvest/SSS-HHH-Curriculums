#!/usr/bin/env python3
"""Validate canonical packages, registry, worksheet sources, and editor contracts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared/validation"))
import corrective_release_lifecycle  # noqa: E402


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[1]
ROLES = ["student", "teacher", "answer", "accessible"]
CANONICAL_SAA = "Solar Agricultural Agency"
REJECTED_SAA = (
    "Solar Agricultural Authority", "Space Agricultural Authority", "Space Agricultural Agency",
    "Solar Agriculture Agency", "Space Agriculture Authority",
)
FORMAL_STUDENT_IDENTITY_LABEL = re.compile(r"^(?:your\s+role|role|student\s+identity|student\s+role(?:\s+and\s+primary\s+practice)?|instructional\s+identity)$", re.I)
LEGACY_STUDENT_IDENTITY = re.compile(r"\b(?:pattern investigator|process modeler|data analyst|timeline analyst|risk assessor)\b", re.I)
FORMAL_IDENTITY_MARKER_SELECTORS = ".label,.callout-label,.technical-label,.section-title,.response-label,label,h1,h2,h3,h4,h5,h6,.teacher-card > strong"
EXPECTED = {
    "SSS-C1-CASE01": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 9, "counts": {"student": 3, "teacher": 8, "answer": 3}},
    "SSS-C1-CASE02": {"version": "1.1", "status": "APPROVED_STABLE", "tasks": 9, "counts": {"student": 3, "teacher": 7, "answer": 3}},
    "SSS-C1-CASE03": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 9, "counts": {"student": 4, "teacher": 8, "answer": 4}},
    "SSS-C1-CASE04": {"version": "1.1", "status": "APPROVED_STABLE", "tasks": 8, "counts": {"student": 4, "teacher": 7, "answer": 4}},
    "SSS-C1-CASE05": {"version": "1.1", "status": "APPROVED_STABLE", "tasks": 8, "counts": {"student": 4, "teacher": 8, "answer": 4}},
    "SSS-C1-CASE06": {"version": "1.1", "status": "APPROVED_STABLE", "tasks": 8, "counts": {"student": 5, "teacher": 8, "answer": 5}},
    "SSS-C1-CASE07": {"version": "1.1", "status": "APPROVED_STABLE", "tasks": 8, "counts": {"student": 6, "teacher": 8, "answer": 6}},
    "SSS-C2-CASE01": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 8, "counts": {"student": 5, "teacher": 9, "answer": 4}},
    "SSS-C2-CASE02": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 8, "counts": {"student": 6, "teacher": 8, "answer": 4}},
    "SSS-C2-CASE03": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 8, "counts": {"student": 5, "teacher": 8, "answer": 4}},
    "SSS-C2-CASE04": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 8, "counts": {"student": 6, "teacher": 8, "answer": 4}},
    "SSS-C2-CASE05": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 7, "counts": {"student": 7, "teacher": 9, "answer": 5}},
    "SSS-C2-CASE06": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 7, "counts": {"student": 6, "teacher": 7, "answer": 5}},
}
# (eligible resize areas, locked areas) per Student edition. The final remediation added
# response controls, and classify_sss_final_response_controls.py registered each new one as
# a locked area; the eligible count is unchanged in every case, so no Student resize
# capability was lost.
STUDENT_LAYOUT_COUNTS = {
    "SSS-C1-CASE01": (9, 28),
    "SSS-C1-CASE02": (9, 23),
    "SSS-C1-CASE03": (6, 19),
    "SSS-C1-CASE04": (5, 25),
    "SSS-C1-CASE05": (8, 26),
    "SSS-C1-CASE06": (8, 26),
    "SSS-C1-CASE07": (11, 31),
    "SSS-C2-CASE01": (11, 35),
    "SSS-C2-CASE02": (10, 34),
    "SSS-C2-CASE03": (8, 34),
    "SSS-C2-CASE04": (10, 34),
    "SSS-C2-CASE05": (13, 32),
    "SSS-C2-CASE06": (10, 35),
}
ACCESSIBLE_CER_SUBTITLE = "You may write sentences or use bullet points. Use evidence from more than one source."
NON_ACCESSIBLE_BASELINE_HASHES = {
    # Re-pinned at the v1.2 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.2.
    "SSS-C1-CASE01": {"student": "35560b98c86466c46ce4e3e695aa75b9158def2b46541ca99f8827616b35ec91", "teacher": "219f25b45a508bb1e10b7a8e87e1a25a2c14d671f1d6ed5281467a120f4caf88", "answer": "4f822c76a293c411b2d0882da4b3dcf138164ea5bbaea2aa5fe3d19bcbfd0205"},
    # Re-pinned at the v1.1 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.1.
    "SSS-C1-CASE02": {"student": "5b714dd328c7e99ae2064499015137aa5633a329d76bef36abe040c21528613a", "teacher": "84fa34457e2b7cbf2a7c4b751c60ed4c952736a11856af61a32432b690d67719", "answer": "f8e9efdb1c5103cd07e52183f0f8736a4ee96a05c32901553637b3a70a4a117d"},
    # Re-pinned at the v1.2 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.2.
    "SSS-C1-CASE03": {"student": "c2bce0c8e81cba6733b7b7593145bb72b789e5341216be3176beac691d40a725", "teacher": "6c9c180e63e03f9913a6962bd08b216d06e92b4b58e693392d04bdbcf8295877", "answer": "37db96007f095cdc2a7024537888869f833cb9fc985134e074520a453b925d73"},
    # Re-pinned at the v1.1 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.1.
    "SSS-C1-CASE04": {"student": "5ec2de3055317dc561c71e162d1384dce5a74ffd81d59d9321d62e8c2a22d27c", "teacher": "33d882f329d98a5f9a3e673e3df1b94e7824c3df7fc71d0a77ef748c1c5171f7", "answer": "48f8a053a17fe1230477e121fdec67f8b6dbf0dc5d30aaa0575e4469757a5d8a"},
    # Re-pinned at the v1.1 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.1.
    "SSS-C1-CASE05": {"student": "f41462a53f77e18762f0f2510d4ba40a70e13ae8f649c566dbc6385c2ae9dac3", "teacher": "e6eb5141545690ec842755ab548adeb5506daced2a97fa24c6b787211cd7891d", "answer": "6a3e8a7b42d11d900636459571f8357dfb36c5c0416ad485d970702e63513b77"},
    # Re-pinned at the v1.1 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.1.
    "SSS-C1-CASE06": {"student": "577d7411d135232744aa1df7c9fb174bd30763f9f6fe60dfc25b343637a89a58", "teacher": "19054a1c59c9c681bdd7ecafae8be953c80caf83af33a9f3da65d81ea8ec6b4b", "answer": "134b05fd099ac7d168dc033efb181db987d2ade3b9577c4e3f540aed2d22f996"},
    # Re-pinned at the v1.1 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.1.
    "SSS-C1-CASE07": {"student": "796149a5e5eea1cc2e92c4d393bf73e9b052d0d3db94ab686520d0ac7dc5036e", "teacher": "f44ad0a98621e53d585c12c25276c686b96d11707a7055f4ca473d5b637e39cb", "answer": "9621dc007fd71182acbeef096c56af893de779e34d33ee9c54faf958b3c2140d"},
    # Re-pinned at the v1.2 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.2.
    "SSS-C2-CASE01": {"student": "6f02de8a1f56bada6ef119061ebe0c47335aaefd2a3fd6943f639409421aff4c", "teacher": "acf03abaadde403426e766d4e6d2b56087a224f7497d084898ac9f119626e245", "answer": "b72e77f7d24f4c6c3ceaebd0bf8152fa0a0e1dc8996a980b2b68fc6a2e542ae1"},
    # Re-pinned at the v1.2 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.2.
    "SSS-C2-CASE02": {"student": "09da81379605b47b6eaef3130f63b55c070931ea5daedb68200d335427bc6aac", "teacher": "22384f7fb44b6c7b9ca327b4fe8f8798a4a74684062466842d2f4ef223de20fd", "answer": "0014a645f17e55171b113149cc06a1b46214e466bbf2cf9ec8dcd4b4cf8e0e8d"},
    # Re-pinned at the v1.2 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.2.
    "SSS-C2-CASE03": {"student": "7777ea321455a7b0e545a299b3b6e1b45f0afe4d24d37f92b6f397551a7e1493", "teacher": "6613e8d68662c84a63740b0a63b886a1515c59db9d8c84218e81be1e0192fde7", "answer": "c0fa5030e250b498f7f6ad32612886ecc73676e8f6d7859745e0a7b845d09090"},
    # Re-pinned at the v1.2 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.2.
    "SSS-C2-CASE04": {"student": "07249953614491ad8502541f4c57038737a037903076e4d0b64516c71d5ede9e", "teacher": "1a58af684cb70ef02e02645eeda40d3159aafddd64eec93ac47902238aefa7e9", "answer": "3dd864eb1ca78b4de6d6ea09a97749e84b5a444f987f3edf8956fed651b735c6"},
    # Re-pinned at the v1.2 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.2.
    "SSS-C2-CASE05": {"student": "4f18b96e52bfef44919c40bca9668b95e61430e7ad77735c3d146c1669a5d331", "teacher": "afbdbdb25a9f00c98a889b3036472b6569079cec8faa3256473d04662c620c78", "answer": "cb541ae8d92cad0c1e8bd916b943c7561d6fbab1ce52959347a7f00d8c3a0d8d"},
    # Re-pinned at the v1.2 final-system release: the owner-approved corrective and
    # visually modernized markup. Superseded baselines are retained in the release records
    # and cannot satisfy approved-baseline enforcement for v1.2.
    "SSS-C2-CASE06": {"student": "747115744832d18302d5cb8b2ed7b900cd6bc5c61a36a7161fe9b642a605fde2", "teacher": "d1d8f6551ba78f6da00caf193145131f07ecc2605ae9e17ce8e6d7a8439e4daf", "answer": "db18da7f4a28beef54e88d4e61bfaaa6cc8654b66dab932a973fba34a379b516"},
}
CASE04_TASK_TITLES = [
    "Initial Thinking — Identify the Variable",
    "Build the Change-to-Crash Timeline",
    "Isolate Variables and Test Alternatives",
    "Diagnose the Reactor Failure",
    "Model the Repeating Crash Cycle",
    "Explain the Failure with CER",
    "Design Independent Reactor Controls",
    "Exit Ticket — Cause or Effect?",
]
CASE05_TASK_TITLES = [
    "Frame the Mission Problem",
    "Separate Observation from Interpretation",
    "Converge the Four Clue Routes",
    "Compare the Competing Diagnoses",
    "Model the Radiation-to-Growth Pathway",
    "Explain the Diagnosis with CER",
    "Define the Engineering Design Problem",
    "Recommend Immediate and Durable Responses",
]
CASE06_TASK_TITLES = [
    "Predict What Changed at Docking",
    "Separate Observation from Interpretation",
    "Connect the Four Evidence Sources",
    "Model the Broken Coordination System",
    "Compare and Reject Competing Diagnoses",
    "Recommend a Monitored Signal-Safe Response",
    "Explain the Diagnosis with CER",
    "Transfer the Systems Reasoning",
]
CASE07_TASK_TITLES = [
    "Frame the Missing-Variable Problem",
    "Connect the Four Evidence Channels",
    "Distinguish Dormancy from Death",
    "Model the Trigger-to-Response System",
    "Compare and Reject Competing Diagnoses",
    "Explain the Missing Trigger with CER",
    "Choose and Monitor a Safe Intervention",
    "Synthesize Campaign 1 and Exit Independently",
]
LEGACY_SELF_STYLED_CASES = {"SSS-C1-CASE01", "SSS-C1-CASE02", "SSS-C1-CASE03"}
PROTECTED_SELECTOR_PATTERNS = {
    ".student-id": r"(?<![\w-])\.student-id(?![\w-])",
    ".id-field": r"(?<![\w-])\.id-field(?![\w-])",
    ".mission-title-block": r"(?<![\w-])\.mission-title-block(?![\w-])",
    ".mission-rail": r"(?<![\w-])\.mission-rail(?![\w-])",
    ".hero-title": r"(?<![\w-])\.hero-title(?![\w-])",
    ".mission-subtitle": r"(?<![\w-])\.mission-subtitle(?![\w-])",
    ".identity-mark": r"(?<![\w-])\.identity-mark(?![\w-])",
    ".identity-copy": r"(?<![\w-])\.identity-copy(?![\w-])",
    ".saa-insignia": r"(?<![\w-])\.saa-insignia(?![\w-])",
    ".institution": r"(?<![\w-])\.institution(?![\w-])",
    ".document-role": r"(?<![\w-])\.document-role(?![\w-])",
    ".continuation-header": r"(?<![\w-])\.continuation-header(?![\w-])",
    ".continuation-copy": r"(?<![\w-])\.continuation-copy(?![\w-])",
    ".continuation-role": r"(?<![\w-])\.continuation-role(?![\w-])",
    ".continuation-identity": r"(?<![\w-])\.continuation-identity(?![\w-])",
    "[data-publication-footer]": r"\[data-publication-footer(?:[^\]]*)\]",
    ".canonical-cer": r"(?<![\w-])\.canonical-cer(?![\w-])",
    ".canonical-cer-box": r"(?<![\w-])\.canonical-cer-box(?![\w-])",
    ".canonical-cer-label": r"(?<![\w-])\.canonical-cer-label(?![\w-])",
    ".canonical-cer-response": r"(?<![\w-])\.canonical-cer-response(?![\w-])",
}
PRINTABLE_STATUS_SELECTORS = ".draft-banner,.validation-banner,.status-banner,[data-lifecycle-status],[data-validation-status]"
PRINTABLE_HEADING_SELECTORS = "header,h1,h2,h3,h4,h5,h6,.continuation-role,.document-role,.technical-label,.label,[data-publication-footer]"
PRODUCTION_METADATA_PATTERNS = {
    "lifecycle-token": re.compile(r"\b(?:DRAFT|VALIDATION[_ -]?BUILD|OWNER[_ -]?GATE(?:[_ -]?OPEN)?|OWNER[_ -]?REVIEW(?:[_ -]?(?:NOT[_ -]?STARTED|PASS))?|READY[_ -]?TO[_ -]?MERGE|APPROVED[_ -]?STABLE)\b"),
    "owner-review": re.compile(r"\bowner[ _-]+review\b", re.I),
    "repository-workflow": re.compile(r"\bgit\s+(?:branch|switch|merge|push|pull|checkout|status|log)\b|\bgithub\s+(?:repository|repo|branch|pull request|workflow|actions)\b|\bworktree\b|\brepository\s+(?:branch|path|workflow|status|history)\b|\b(?:stored|committed|tracked)\s+in\s+the\s+repository\b", re.I),
    "branch-name": re.compile(r"\b(?:feature|hotfix|bugfix|chore|fix)/[a-z0-9][a-z0-9._/-]*\b|\brelease/v?\d[a-z0-9._/-]*\b", re.I),
    "commit-sha": re.compile(r"\b[0-9a-f]{40}\b|\b(?:commit|revision|sha(?:-?1|-?256)?)\s*(?::|#)?\s*[0-9a-f]{7,40}\b", re.I),
    "merge-instruction": re.compile(r"\bgit\s+(?:merge|push|pull|switch|checkout)\b|\bmerge\s+(?:the\s+branch|into\s+(?:main|master))\b|\bpush\s+(?:the\s+)?branch\s+to\b|\bpull\s+from\s+origin\b|\bswitch\s+(?:to\s+)?(?:the\s+)?branch\b|\bcheckout\s+(?:the\s+)?branch\b|\bfast-forward\s+merge\b|\bdo\s+not\s+merge\b", re.I),
    "validation-status": re.compile(r"\bvalidation\s+(?:status|build|pass(?:ed)?|fail(?:ed)?|complete|result)\b", re.I),
}


def protected_css_definitions(css: str) -> list[str]:
    clean = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    selectors = [match.group(1).strip() for match in re.finditer(r"(?:^|})\s*([^{}]+)\{", clean)]
    return sorted({name for selector in selectors if not selector.startswith("@") for name, pattern in PROTECTED_SELECTOR_PATTERNS.items() if re.search(pattern, selector)})


def printable_production_metadata_findings(root) -> list[str]:
    findings: list[str] = []
    for page in root.select(".page[data-role]"):
        page_id = page.get("data-page-id", "unknown-page")
        text = " ".join(page.stripped_strings)
        for node in page.select(PRINTABLE_STATUS_SELECTORS):
            findings.append(f"{page_id}:status-banner:{' '.join(node.stripped_strings)[:120]}")
        for name, pattern in PRODUCTION_METADATA_PATTERNS.items():
            match = pattern.search(text)
            if match:
                findings.append(f"{page_id}:{name}:{match.group(0)}")
    return findings


def printable_owner_review_headings(root) -> list[str]:
    return [
        f"{node.find_parent(class_='page').get('data-page-id', 'unknown-page')}:{' '.join(node.stripped_strings)}"
        for node in root.select(f".page[data-role] {PRINTABLE_HEADING_SELECTORS}")
        if re.search(r"\bowner[ _-]+review\b", " ".join(node.stripped_strings), re.I)
    ]


class Results:
    def __init__(self):
        self.assertions: list[dict[str, object]] = []

    def check(self, name: str, passed: bool, detail="") -> None:
        self.assertions.append({"name": name, "pass": bool(passed), "detail": str(detail)})

    @property
    def passed(self) -> int:
        return sum(1 for item in self.assertions if item["pass"])


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def schema_errors(instance, schema) -> list[str]:
    """Validate the JSON-Schema features used by the repository's v2 schemas."""
    errors: list[str] = []

    def resolve(reference: str):
        node = schema
        for part in reference.removeprefix("#/").split("/"):
            node = node[part]
        return node

    def visit(value, rule, path="$", root_rule=None):
        if "$ref" in rule:
            visit(value, resolve(rule["$ref"]), path)
            return
        if "const" in rule and value != rule["const"]:
            errors.append(f"{path}: must equal {rule['const']!r}")
        if "enum" in rule and value not in rule["enum"]:
            errors.append(f"{path}: must be one of {rule['enum']!r}")
        expected = rule.get("type")
        type_ok = {
            "object": isinstance(value, dict),
            "array": isinstance(value, list),
            "string": isinstance(value, str),
            "integer": isinstance(value, int) and not isinstance(value, bool),
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
            "boolean": isinstance(value, bool),
        }.get(expected, True)
        if expected and not type_ok:
            errors.append(f"{path}: expected {expected}")
            return
        if isinstance(value, dict):
            for key in rule.get("required", []):
                if key not in value:
                    errors.append(f"{path}: missing required property {key}")
            properties = rule.get("properties", {})
            if rule.get("additionalProperties") is False:
                for key in value.keys() - properties.keys():
                    errors.append(f"{path}: unexpected property {key}")
            for key, child in value.items():
                if key in properties:
                    visit(child, properties[key], f"{path}.{key}")
        if isinstance(value, list):
            if len(value) < rule.get("minItems", 0):
                errors.append(f"{path}: too few items")
            if rule.get("uniqueItems") and len({json.dumps(item, sort_keys=True) for item in value}) != len(value):
                errors.append(f"{path}: items must be unique")
            if "items" in rule:
                for index, child in enumerate(value):
                    visit(child, rule["items"], f"{path}[{index}]")
        if isinstance(value, str):
            if len(value) < rule.get("minLength", 0):
                errors.append(f"{path}: string is too short")
            if "pattern" in rule and not re.search(rule["pattern"], value):
                errors.append(f"{path}: does not match {rule['pattern']}")
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "minimum" in rule and value < rule["minimum"]:
                errors.append(f"{path}: below minimum")
            if "maximum" in rule and value > rule["maximum"]:
                errors.append(f"{path}: above maximum")
        if "anyOf" in rule and not any(not schema_errors_for(value, option) for option in rule["anyOf"]):
            errors.append(f"{path}: does not satisfy anyOf")

    def schema_errors_for(value, rule):
        before = len(errors)
        visit(value, rule, "$probe")
        probe = errors[before:]
        del errors[before:]
        return probe

    visit(instance, schema)
    return errors


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stored_layout_override_findings(case_id: str, layout_data: dict) -> list[str]:
    findings = []
    editions = {
        "accessible": {key: layout_data[key] for key in ("edition", "areas", "lockedAreas", "overrides")},
        "student": layout_data["student"],
    }
    for edition, definition in editions.items():
        areas = {area["id"]: area for area in definition["areas"]}
        locked = {item["persistId"] for item in definition["lockedAreas"]}
        for area_id, override in definition["overrides"].items():
            area = areas.get(area_id)
            if area is None:
                findings.append(f"{edition}:{area_id}:not-eligible")
                continue
            expected_id = f'{case_id}:{edition}:t{area["taskId"]}:{area["persistId"]}'
            if area_id != expected_id or not area["pageId"].startswith(edition):
                findings.append(f"{edition}:{area_id}:metadata")
            if area["persistId"] in locked:
                findings.append(f"{edition}:{area_id}:locked")
            if set(override) != {"heightPx", "sourceHeightPx"}:
                findings.append(f"{edition}:{area_id}:fields")
                continue
            height = override["heightPx"]
            source = override["sourceHeightPx"]
            if not isinstance(height, int) or isinstance(height, bool) or height % 4 or not area["minPx"] <= height <= area["maxPx"]:
                findings.append(f"{edition}:{area_id}:height")
            if not isinstance(source, int) or isinstance(source, bool) or not 16 <= source <= 2000 or source == height:
                findings.append(f"{edition}:{area_id}:source")
    return findings


def role_dom_hash(soup: BeautifulSoup, role: str) -> str:
    fragment = BeautifulSoup("".join(str(page) for page in soup.select(f'.page[data-role="{role}"]')), "html.parser")
    for node in list(fragment.find_all(string=True)):
        if isinstance(node, NavigableString) and not str(node).strip():
            node.extract()
    return hashlib.sha256(fragment.decode(formatter="minimal").encode("utf-8")).hexdigest()


def task_registry(path: Path):
    text = path.read_text(encoding="utf-8")
    payload = re.sub(r"^\s*window\.[A-Z0-9_]+\s*=\s*", "", text).rstrip().removesuffix(";")
    return json.loads(payload)


def partition_operational(registry: dict) -> tuple[list[tuple[str, dict]], list[tuple[str, dict]]]:
    """Split operational (editorPackage-declaring) entries by curriculum.

    The frozen SSS expectation maps in this module (EXPECTED, STUDENT_LAYOUT_COUNTS,
    NON_ACCESSIBLE_BASELINE_HASHES, exact task/page/CER assertions) bind ONLY to the
    SSS partition. HHH operational packages must never be indexed through them: they
    receive the generic shared checks in validate_hhh_operational_case instead, and
    their instructional products are governed by HHH package validation, not SSS
    diagnosis/CER assumptions. Returns (sss, hhh) of (campaign_id, entry) pairs.
    """
    sss: list[tuple[str, dict]] = []
    hhh: list[tuple[str, dict]] = []
    for curriculum in registry["curricula"]:
        for campaign in curriculum["campaigns"]:
            for case in campaign["cases"]:
                if "editorPackage" not in case:
                    continue
                (sss if curriculum["id"] == "SSS" else hhh).append((campaign["id"], case))
    return sss, hhh


# The one ordinary lifecycle for a package-backed HHH unit:
# registry status -> (registry packageStatus, shared approval status, shared print status).
# APPROVED_STABLE additionally requires a matching historyRecord/releaseHistory pair;
# every other state must carry neither pointer.
HHH_LIFECYCLE_CONTRACT = {
    "DRAFT": ("DRAFT", "OWNER_REVIEW_NOT_STARTED", "NOT_RUN"),
    "VALIDATION_BUILD": ("VALIDATION", "OWNER_REVIEW_NOT_STARTED", "NOT_RUN"),
    "OWNER_GATE_OPEN": ("OWNER_REVIEW", "OWNER_REVIEW_IN_PROGRESS", "NOT_RUN"),
    "APPROVED_STABLE": ("APPROVED", "APPROVED", "PASS"),
}
HHH_PACKAGE_PATH_RE = re.compile(r"^hhh/(campaign-\d+)/([a-z0-9][a-z0-9-]*)/source/case-package\.json$")
HHH_PACKAGE_SOURCES = {
    "content": "content.html",
    "presentation": "presentation.css",
    "taskRegistry": "task-registry.js",
    "layoutOverrides": "layout-overrides.json",
}


def hhh_lifecycle_findings(entry: dict, package: dict) -> list[str]:
    """Every registry/package lifecycle violation for one HHH operational unit.

    Rejects any status outside the four canonical states and any internally
    inconsistent combination across the registry entry and the package.
    """
    findings: list[str] = []
    status = entry.get("status")
    if package.get("status") != status:
        findings.append(f"registry status {status!r} and package status {package.get('status')!r} disagree")
    contract = HHH_LIFECYCLE_CONTRACT.get(status)
    if contract is None:
        findings.append(f"unsupported lifecycle status {status!r}")
        return findings
    package_status, approval_status, print_status = contract
    if entry.get("packageStatus") != package_status:
        findings.append(f"{status} requires registry packageStatus {package_status!r}; found {entry.get('packageStatus')!r}")
    entry_approval = entry.get("approval") or {}
    package_approval = package.get("approval") or {}
    if not (entry_approval.get("status") == package_approval.get("status") == approval_status):
        findings.append(f"{status} requires registry and package approval status {approval_status!r}; "
                        f"found registry {entry_approval.get('status')!r}, package {package_approval.get('status')!r}")
    if not (entry_approval.get("printStatus") == package_approval.get("printStatus") == print_status):
        findings.append(f"{status} requires registry and package print status {print_status!r}; "
                        f"found registry {entry_approval.get('printStatus')!r}, package {package_approval.get('printStatus')!r}")
    # Beyond the state-specific fields, the two approval records must be the same
    # record: owner, date when present, and any other schema-allowed field. A
    # package approved by one owner/date and registered under another is divergence,
    # not a formatting difference.
    if entry_approval != package_approval:
        findings.append("registry and package approval objects must be identical; "
                        f"registry {entry_approval!r}, package {package_approval!r}")
    if status == "APPROVED_STABLE":
        if not entry.get("historyRecord") or package.get("releaseHistory") != entry.get("historyRecord"):
            findings.append("APPROVED_STABLE requires a matching historyRecord/releaseHistory pair; "
                            f"found registry {entry.get('historyRecord')!r}, package {package.get('releaseHistory')!r}")
    else:
        if "historyRecord" in entry:
            findings.append(f"{status} entry must not declare a historyRecord")
        if "releaseHistory" in package:
            findings.append(f"{status} package must not declare a releaseHistory")
    return findings


def hhh_source_path_findings(editor_package: str, package: dict) -> list[str]:
    """Every canonical-ownership violation among an HHH package's declared sources.

    The four package-pinned sources must be exactly the registered unit's own
    ``source/`` files, as normalized repository-relative paths. Exact equality is
    the rule, so absolute paths, ``..`` traversal, another unit's or an SSS
    unit's sources, and alternate filenames or locations that merely satisfy the
    schema suffix all fail identically.
    """
    match = HHH_PACKAGE_PATH_RE.match(str(editor_package))
    if not match:
        return [f"editorPackage is not a canonical HHH unit package path: {editor_package!r}"]
    unit_source = editor_package[: -len("case-package.json")]
    findings: list[str] = []
    for key, filename in HHH_PACKAGE_SOURCES.items():
        declared = (package.get(key) or {}).get("source")
        expected = f"{unit_source}{filename}"
        if declared != expected:
            findings.append(f"{key} source must be the package-owned {expected!r}; declared {declared!r}")
    return findings


HHH_README_COUNTS_RE = re.compile(
    r"^Roles and page counts:\s*"
    r"Student\s+(?P<student>\d+)\s*[\u00b7\u2022]\s*"
    r"Teacher\s+(?P<teacher>\d+)\s*[\u00b7\u2022]\s*"
    r"Answer Key\s+(?P<answer>\d+)\s*[\u00b7\u2022]\s*"
    r"Accessible\s+(?P<accessible>\d+)\s*\.\s*$",
    re.MULTILINE)


def hhh_readme_page_count_findings(unit_dir: Path, package: dict) -> list[str]:
    """Disagreements between an HHH package README's declared role page counts and the package.

    Case 01 shipped a README claiming eight Teacher pages against a seven-page
    Teacher Guide, and cross-referenced a "Teacher page 8" that did not exist.
    Nothing caught it: every other validator compares the package to the DOM and
    the registry, and no gate had ever read a README. This closes that gap for
    every package-backed HHH unit at once.

    The parse is deliberately narrow. It matches one standardized declaration
    line and nothing else, so it cannot drift into guessing at prose. A missing
    or unparseable line is a contract failure rather than a silent pass, which is
    what makes the guard meaningful for units that do not exist yet.
    """
    readme = unit_dir / "README.md"
    if not readme.is_file():
        return ["README.md is required and was not found"]
    matches = HHH_README_COUNTS_RE.findall(readme.read_text(encoding="utf-8"))
    if len(matches) != 1:
        return [f"README must carry exactly one 'Roles and page counts:' declaration line; found {len(matches)}"]
    match = HHH_README_COUNTS_RE.search(readme.read_text(encoding="utf-8"))
    declared = {role: int(match.group(role)) for role in ROLES}
    packaged = {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
    if declared != packaged:
        return [f"README role page counts {declared} disagree with the package {packaged}"]
    return []


PAGE_COUNT_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
    "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
}
HHH_PAGE_PROSE_RE = re.compile(r"\b(?P<count>[A-Za-z]+|\d+)-page\b")
HHH_ROLE_PROSE = {
    "student": "Student Mission",
    "teacher": "Teacher Guide",
    "answer": "Answer Key",
    "accessible": "Accessible Mission",
}


def hhh_page_count_prose_findings(soup: BeautifulSoup, package: dict) -> list[str]:
    """Every printable sentence that advertises a role page count the package contradicts.

    Case 02 shipped a Teacher Guide telling teachers to print "the ten-page
    Accessible Mission" against an eleven-page Accessible edition, on two
    separate pages. Nothing caught it: the package, the registry, the DOM and the
    README all agreed with each other, and no gate had ever read the *body prose*
    that a teacher actually follows. The README check closes the same drift one
    file over; this closes it inside the printed documents.

    The scan is deliberately narrow. An ``N-page`` token binds to whichever role
    name sits *adjacent* to it, ahead or behind, and only when that role is within
    a few words. Adjacency rather than direction is what the prose actually uses:
    "the eight-page Student Mission or the eleven-page Accessible Mission" binds
    each count forwards, while "the Accessible Mission is an eleven-page packet
    built alongside the Student Mission" binds backwards, and a rule that always
    looked forwards would read that second sentence as a claim about the Student
    edition. A token whose nearest role is further off than that is ordinary prose
    and is not treated as a page-count claim at all. Counts written as words and as
    digits resolve the same way.
    """
    adjacency = 14
    findings: list[str] = []
    for page in soup.select(".page[data-role]"):
        text = " ".join(page.get_text(" ").split())
        matches = list(HHH_PAGE_PROSE_RE.finditer(text))
        for index, match in enumerate(matches):
            raw = match.group("count")
            count = int(raw) if raw.isdigit() else PAGE_COUNT_WORDS.get(raw.lower())
            if count is None:
                continue
            # Neither span may cross a neighbouring page-count token, so one claim
            # can never borrow the role belonging to the next or previous one.
            stop = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            start = matches[index - 1].end() if index else 0
            ahead = text[match.end():min(stop, match.end() + 80)]
            behind = text[max(start, match.start() - 80):match.start()]
            candidates = []
            for role, label in HHH_ROLE_PROSE.items():
                if label in ahead:
                    candidates.append((ahead.index(label), role))
                if label in behind:
                    candidates.append((len(behind) - (behind.rindex(label) + len(label)), role))
            candidates = [item for item in candidates if item[0] <= adjacency]
            if not candidates:
                continue
            role = min(candidates)[1]
            declared = package["rolePageStructure"][role]["pageCount"]
            if count != declared:
                findings.append(
                    f"{page.get('data-page-id')} advertises a {count}-page {HHH_ROLE_PROSE[role]} "
                    f"against a package count of {declared}: "
                    f"{text[max(0, match.start() - 40):match.end() + 60].strip()!r}")
    return findings


def validate_hhh_operational_case(results: Results, campaign_id: str, entry: dict, package_schema: dict) -> None:
    """Generic shared-system checks for one package-backed HHH unit.

    Covers the shared operational contract only. It does not require canonical CER —
    the Blueprint's instructional products vary by unit — but when a package does use
    the shared CER component, the structural and page-atomicity contracts still hold.
    """
    case_id = entry["id"]
    package_path = ROOT / entry["editorPackage"]
    package = load_json(package_path)
    errors = schema_errors(package, package_schema)
    results.check(f"{case_id} package validates against schema v2", not errors, errors)
    results.check(
        f"{case_id} registry and package identity, curriculum, campaign, and instructional type agree",
        package["id"] == case_id and package.get("curriculum") == "HHH"
        and package.get("campaign") == campaign_id
        and package.get("version") == entry["version"] and package.get("status") == entry["status"]
        and package.get("title") == entry["title"]
        and package.get("instructionalType") == entry.get("instructionalType")
        and package.get("instructionalType") in {"ORIENTATION", "CORE_CASE", "SYNTHESIS", "CAPSTONE"},
        json.dumps({"registry": {key: entry.get(key) for key in ("id", "version", "status", "title", "instructionalType")},
                    "package": {key: package.get(key) for key in ("id", "curriculum", "campaign", "version", "status", "title", "instructionalType")}}))
    results.check(f"{case_id} has exactly four instructional roles",
                  package["supportedRoles"] == ROLES and list(package["rolePageStructure"]) == ROLES)
    results.check(f"{case_id} keeps Grayscale a presentation state, not an output or role",
                  list(package["outputs"]) == ["complete", *ROLES]
                  and all("GRAYSCALE" not in name.upper() for name in package["outputs"].values())
                  and '"grayscale": {' not in package_path.read_text(encoding="utf-8"))
    lifecycle_violations = hhh_lifecycle_findings(entry, package)
    results.check(f"{case_id} lifecycle metadata matches release policy across registry and package",
                  not lifecycle_violations, lifecycle_violations)

    results.check(f"{case_id} editorPackage lives under its registered campaign",
                  str(entry["editorPackage"]).startswith(f"hhh/{campaign_id}/"), entry["editorPackage"])
    ownership_violations = hhh_source_path_findings(entry["editorPackage"], package)
    results.check(f"{case_id} package-pinned sources are exactly the registered unit's own canonical paths",
                  not ownership_violations, ownership_violations)
    if ownership_violations:
        return
    paths = {
        "content": ROOT / package["content"]["source"],
        "presentation": ROOT / package["presentation"]["source"],
        "taskRegistry": ROOT / package["taskRegistry"]["source"],
        "layoutOverrides": ROOT / package["layoutOverrides"]["source"],
    }
    if "icons" in package["sourceHashes"]:
        paths["icons"] = ROOT / package["shell"]["icons"]
    results.check(f"{case_id} all package-controlled sources exist", all(path.is_file() for path in paths.values()), paths)
    if not all(path.is_file() for path in paths.values()):
        return
    results.check(f"{case_id} source hashes verify",
                  all(sha256(path) == package["sourceHashes"][name] for name, path in paths.items()))
    registry_data = task_registry(paths["taskRegistry"])
    lifecycle_findings = corrective_release_lifecycle.history_findings(
        package_path.parents[1], case_id, package, registry_data)
    results.check(f"{case_id} history satisfies the shared corrective-release lifecycle", not lifecycle_findings, lifecycle_findings)
    readme_findings = hhh_readme_page_count_findings(package_path.parents[1], package)
    results.check(f"{case_id} README role page counts match the package", not readme_findings, readme_findings)
    # The task registry is the authoritative record of the case's own shape, and it
    # states the role page counts a second time. Nothing compared the two, so a
    # registry could name a page count the package contradicts and every other gate
    # would still pass — the same class of drift the README check closes, one file
    # over. Registry-derived through the operational walk, so every HHH unit gains it
    # with no edit here.
    registry_roles = registry_data.get("roles")
    packaged_roles = {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
    results.check(f"{case_id} task registry identity and role page counts match the package",
                  registry_data.get("case") == case_id and registry_roles == packaged_roles,
                  json.dumps({"registryCase": registry_data.get("case"),
                              "registryRoles": registry_roles, "package": packaged_roles}))

    soup = BeautifulSoup(paths["content"].read_text(encoding="utf-8"), "html.parser")
    counts = {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
    actual_counts = {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES}
    results.check(f"{case_id} worksheet DOM page counts match package declarations", actual_counts == counts, actual_counts)
    page_prose_findings = hhh_page_count_prose_findings(soup, package)
    results.check(f"{case_id} printable prose never advertises a role page count the package contradicts",
                  not page_prose_findings, page_prose_findings)
    page_ids = [node.get("data-page-id") for node in soup.select(".page[data-page-id]")]
    persist_ids = [node.get("data-persist-id") for node in soup.select("[data-persist-id]")]
    results.check(f"{case_id} page and persistence IDs are unique",
                  len(page_ids) == len(set(page_ids)) and len(persist_ids) == len(set(persist_ids)) and None not in persist_ids)
    results.check(f"{case_id} response fields have accessible names",
                  all(node.get("aria-label") or node.get("aria-labelledby") for node in soup.select("[data-response]")))
    cer_roots = soup.select("[data-cer-contract],.canonical-cer,.cer-stack")
    if cer_roots:
        results.check(f"{case_id} CER components are page-atomic",
                      all(all(child.find_parent(class_="page") is root.find_parent(class_="page")
                              for child in root.select("*")) for root in cer_roots))
        canonical_labels = [[label.get_text(strip=True) for label in root.select(":scope > .canonical-cer-box > .canonical-cer-label")]
                            for root in soup.select(".canonical-cer[data-cer-contract]")]
        results.check(f"{case_id} declared canonical CER keeps the Claim/Evidence/Reasoning structure",
                      all(labels == ["CLAIM", "EVIDENCE", "REASONING"] for labels in canonical_labels), canonical_labels)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-mutation-tests", action="store_true",
        help="skip the six SSS mutation checks. Proportional-validation escape for diffs "
             "that cannot alter frozen SSS content protections; every ordinary static "
             "assertion and chained validator still runs. Default behavior is unchanged.")
    args = parser.parse_args()

    results = Results()
    registry_path = ROOT / "shared/implementation/case-registry.v2.json"
    registry_schema_path = ROOT / "shared/implementation/case-registry.schema.v2.json"
    package_schema_path = ROOT / "shared/implementation/case-package.schema.v2.json"
    history_schema_path = ROOT / "shared/implementation/case-release-history.schema.v1.json"
    registry = load_json(registry_path)
    registry_schema = load_json(registry_schema_path)
    package_schema = load_json(package_schema_path)
    history_schema = load_json(history_schema_path)

    detector_probe = protected_css_definitions(".student-id{display:grid}.canonical-cer-response:focus{outline:0}[data-publication-footer]{margin:0}")
    results.check("protected case-CSS selector detector rejects direct invariant-component rules", detector_probe == [".canonical-cer-response", ".student-id", "[data-publication-footer]"], detector_probe)
    ordinary_approved_probe = BeautifulSoup('<main><section class="page" data-role="teacher" data-page-id="probe"><h2>Approved classroom procedures</h2><p>Use the approved safety procedure.</p></section></main>', "html.parser")
    results.check("printable production-metadata detector permits ordinary instructional uses of approved", not printable_production_metadata_findings(ordinary_approved_probe))
    forbidden_metadata_probe = BeautifulSoup('<main><section class="page" data-role="teacher" data-page-id="probe"><header>Owner review</header><div class="draft-banner">APPROVED_STABLE · READY_TO_MERGE</div><p>VALIDATION_BUILD on hotfix/case04 at commit 0123456789abcdef0123456789abcdef01234567; validation status PASS; stored in the repository. Do not merge.</p></section></main>', "html.parser")
    forbidden_probe_categories = {finding.split(":", 2)[1] for finding in printable_production_metadata_findings(forbidden_metadata_probe)}
    results.check("printable production-metadata detector rejects workflow banners, lifecycle tokens, branches, commits, merge instructions, and repository status text", {"status-banner", "lifecycle-token", "owner-review", "repository-workflow", "branch-name", "commit-sha", "merge-instruction", "validation-status"}.issubset(forbidden_probe_categories), sorted(forbidden_probe_categories))
    results.check("registry validates against schema v2", not schema_errors(registry, registry_schema), schema_errors(registry, registry_schema))
    all_entries = [case for curriculum in registry["curricula"] for campaign in curriculum["campaigns"] for case in campaign["cases"]]
    # Operational (package-backed) coverage derives from editorPackage; entries without one
    # are planned registry reservations validated by validate_hhh_activation.py instead.
    # Frozen SSS expectation maps bind only to the SSS partition; HHH operational
    # packages take the generic shared checks.
    sss_operational, hhh_operational = partition_operational(registry)
    entries = [case for _, case in sss_operational]

    # Routing probe: an editor-ready HHH-C1-CASE00 must reach the generic HHH checks
    # and must never be indexed through an SSS-only expectation map. Fixture-driven so
    # the guarantee holds while the live registry still has zero editor-ready HHH units.
    probe_sss, probe_hhh = partition_operational({"curricula": [
        {"id": "SSS", "campaigns": [{"id": "campaign-1", "cases": [
            {"id": "SSS-C1-CASE01", "editorPackage": "sss/campaign-1/case-01-iss-greenhouse/source/case-package.json"},
            {"id": "SSS-C1-CASE99"}]}]},
        {"id": "HHH", "campaigns": [{"id": "campaign-1", "cases": [
            {"id": "HHH-C1-CASE00", "editorPackage": "hhh/campaign-1/case-00-archive-orientation/source/case-package.json"},
            {"id": "HHH-C1-CASE01"}]}]},
    ]})
    results.check("an editor-ready HHH-C1-CASE00 routes to the generic HHH checks and never into SSS-only expectation maps",
                  [case["id"] for _, case in probe_hhh] == ["HHH-C1-CASE00"]
                  and [case["id"] for _, case in probe_sss] == ["SSS-C1-CASE01"]
                  and all(case["id"] not in EXPECTED and case["id"] not in STUDENT_LAYOUT_COUNTS
                          and case["id"] not in NON_ACCESSIBLE_BASELINE_HASHES for _, case in probe_hhh),
                  json.dumps({"sss": [case["id"] for _, case in probe_sss], "hhh": [case["id"] for _, case in probe_hhh]}))

    results.check("SSS operational roster is exactly the approved Campaign 1 and Campaign 2 cases in display order", [entry["id"] for entry in entries] == list(EXPECTED), [entry["id"] for entry in entries])
    results.check("every approved SSS case retains a frozen non-Accessible DOM baseline", {entry["id"] for entry in entries if entry["status"] == "APPROVED_STABLE"} <= set(NON_ACCESSIBLE_BASELINE_HASHES))
    results.check("planned registry reservations stay unreleased DRAFT entries with no package or release pointer", all(entry["status"] == "DRAFT" and "historyRecord" not in entry for entry in all_entries if "editorPackage" not in entry))
    base_fields = {"id", "displayOrder", "displayLabel", "title", "version", "status", "editorShell", "editorPackage", "centralWorkflow", "packageStatus", "approval"}
    results.check("SSS registry contains lifecycle-appropriate operational case fields", all(set(entry) == (base_fields | ({"historyRecord"} if entry["status"] == "APPROVED_STABLE" else set())) for entry in entries))
    results.check("HHH operational entries carry exactly the operational fields plus instructionalType", all(set(case) == (base_fields | {"instructionalType"} | ({"historyRecord"} if case["status"] == "APPROVED_STABLE" else set())) for _, case in hhh_operational))
    results.check("no serialized SSS case entry acquired an instructional type", all("instructionalType" not in entry for entry in all_entries if entry["id"].startswith("SSS-")))

    for hhh_campaign_id, hhh_entry in hhh_operational:
        validate_hhh_operational_case(results, hhh_campaign_id, hhh_entry, package_schema)

    for entry in entries:
        case_id = entry["id"]
        expected = EXPECTED[case_id]
        expected_version = expected["version"]
        expected_counts = expected["counts"]
        expected_status = expected["status"]
        package_path = ROOT / entry["editorPackage"]
        package = load_json(package_path)
        errors = schema_errors(package, package_schema)
        results.check(f"{case_id} package validates against schema v2", not errors, errors)
        results.check(f"{case_id} registry and package identity agree", package["id"] == case_id and package["version"] == entry["version"] == expected_version and package["status"] == entry["status"] == expected_status)
        lifecycle_ok = (
            expected_status == "APPROVED_STABLE"
            and package.get("releaseHistory") == entry.get("historyRecord")
            and package["approval"].get("status") == entry["approval"].get("status") == "APPROVED"
            and package["approval"].get("printStatus") == entry["approval"].get("printStatus") == "PASS"
        ) or (
            expected_status == "DRAFT"
            and "releaseHistory" not in package
            and "historyRecord" not in entry
            and package["approval"].get("status") == entry["approval"].get("status") == "OWNER_REVIEW_NOT_STARTED"
            and package["approval"].get("printStatus") == entry["approval"].get("printStatus") == "NOT_RUN"
        ) or (
            expected_status == "OWNER_GATE_OPEN"
            and "releaseHistory" not in package
            and "historyRecord" not in entry
            and entry.get("packageStatus") == "OWNER_REVIEW"
            and package["approval"].get("status") == entry["approval"].get("status") == "OWNER_REVIEW_IN_PROGRESS"
            and package["approval"].get("printStatus") == entry["approval"].get("printStatus") == "NOT_RUN"
        )
        results.check(f"{case_id} lifecycle metadata matches release policy", lifecycle_ok)
        results.check(f"{case_id} has exactly four instructional roles", package["supportedRoles"] == ROLES and list(package["rolePageStructure"]) == ROLES)
        results.check(f"{case_id} has complete plus four normal output names", list(package["outputs"]) == ["complete", *ROLES] and all("GRAYSCALE" not in filename.upper() for filename in package["outputs"].values()))
        counts = {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
        results.check(f"{case_id} fixed-role package page counts are exact and Accessible is content-driven", {role: counts[role] for role in expected_counts} == expected_counts and counts["accessible"] >= 1, counts)
        results.check(f"{case_id} package uses the canonical institutional identity", package["institutionalIdentity"]["name"] == CANONICAL_SAA and package["institutionalIdentity"]["lockupLines"] == ["Solar", "Agricultural", "Agency"])
        results.check(f"{case_id} package has no migration-era fields", not {"migrationSource", "phase2Authorization", "historicalMaster", "successorMaster", "goldenMaster", "reconciliationRecord"}.intersection(package))

        paths = {
            "content": ROOT / package["content"]["source"],
            "presentation": ROOT / package["presentation"]["source"],
            "taskRegistry": ROOT / package["taskRegistry"]["source"],
            "layoutOverrides": ROOT / package["layoutOverrides"]["source"],
        }
        if "icons" in package["sourceHashes"]:
            paths["icons"] = ROOT / package["shell"]["icons"]
        results.check(f"{case_id} all package-controlled sources exist", all(path.is_file() for path in paths.values()), paths)
        results.check(f"{case_id} source hashes verify", all(sha256(path) == package["sourceHashes"][name] for name, path in paths.items()))
        layout_data = load_json(paths["layoutOverrides"])
        results.check(f"{case_id} Student response-area audit has exact eligible/locked coverage", (len(layout_data["student"]["areas"]), len(layout_data["student"]["lockedAreas"])) == STUDENT_LAYOUT_COUNTS[case_id])
        override_findings = stored_layout_override_findings(case_id, layout_data)
        results.check(f"{case_id} stored Student/Accessible overrides satisfy production eligibility, metadata, snap, and bounds contracts", not override_findings, override_findings)

        content = paths["content"].read_text(encoding="utf-8")
        identity_sources = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in paths.values())
        results.check(f"{case_id} active sources reject noncanonical SAA expansions", CANONICAL_SAA in identity_sources and not any(variant in identity_sources for variant in REJECTED_SAA))
        soup = BeautifulSoup(content, "html.parser")
        actual_counts = {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES}
        results.check(f"{case_id} worksheet DOM page counts match package declarations", actual_counts == counts, actual_counts)
        current_non_accessible_hashes = {role: role_dom_hash(soup, role) for role in ["student", "teacher", "answer"]}
        if case_id in NON_ACCESSIBLE_BASELINE_HASHES:
            results.check(f"{case_id} Student, Teacher, and Answer Key DOM remain at the authoritative baseline", current_non_accessible_hashes == NON_ACCESSIBLE_BASELINE_HASHES[case_id], current_non_accessible_hashes)
        else:
            results.check(f"{case_id} carries no frozen DOM baseline only because it is unreleased", expected_status != "APPROVED_STABLE", expected_status)
        results.check(f"{case_id} content is a worksheet-only fragment", bool(soup.select_one("main")) and not soup.select("script,style,link,iframe,.toolbar"))
        learner_pages = soup.select('.page[data-role="student"],.page[data-role="accessible"]')
        formal_identity_findings = []
        for page in learner_pages:
            page_id = page.get("data-page-id", "unknown-page")
            formal_identity_findings.extend(f"{page_id}:identity-strip" for _ in page.select(".identity-strip"))
            formal_identity_findings.extend(f"{page_id}:role-field:{node.name}" for node in page.select('[data-field*="role" i],[data-persist-id*="role" i]'))
            formal_identity_findings.extend(
                f"{page_id}:formal-label:{node.get_text(' ', strip=True)}"
                for node in page.select(FORMAL_IDENTITY_MARKER_SELECTORS)
                if FORMAL_STUDENT_IDENTITY_LABEL.fullmatch(node.get_text(" ", strip=True))
            )
        for page in soup.select('.page[data-role="teacher"]'):
            page_id = page.get("data-page-id", "unknown-page")
            formal_identity_findings.extend(
                f"{page_id}:dedicated-teacher-field:{node.get_text(' ', strip=True)}"
                for node in page.select(FORMAL_IDENTITY_MARKER_SELECTORS)
                if FORMAL_STUDENT_IDENTITY_LABEL.fullmatch(node.get_text(" ", strip=True))
            )
        formal_identity_findings.extend(
            f"legacy-identity:{match.group(0)}" for match in LEGACY_STUDENT_IDENTITY.finditer(" ".join(soup.stripped_strings))
        )
        results.check(f"{case_id} has no formal student Role or Identity element in printable editions", not formal_identity_findings, formal_identity_findings)
        page_ids = [node.get("data-page-id") for node in soup.select(".page[data-page-id]")]
        persist_ids = [node.get("data-persist-id") for node in soup.select("[data-persist-id]")]
        results.check(f"{case_id} page and persistence IDs are unique", len(page_ids) == len(set(page_ids)) and len(persist_ids) == len(set(persist_ids)) and None not in persist_ids)
        results.check(f"{case_id} response fields have accessible names", all(node.get("aria-label") or node.get("aria-labelledby") for node in soup.select("[data-response]")))
        if expected_status == "APPROVED_STABLE":
            draft_banners = [node.find_parent(class_="page").get("data-page-id", "unknown-page") for node in soup.select('.page[data-role] .draft-banner')]
            production_metadata = printable_production_metadata_findings(soup)
            owner_review_headings = printable_owner_review_headings(soup)
            results.check(f"{case_id} approved printable roles contain no .draft-banner", not draft_banners, draft_banners)
            results.check(f"{case_id} approved printable roles contain no visible production metadata", not production_metadata, production_metadata)
            results.check(f"{case_id} printable headings and headers contain no owner-review wording", not owner_review_headings, owner_review_headings)
        registry_data = task_registry(paths["taskRegistry"])
        expected_task_numbers = list(range(1, expected["tasks"] + 1))
        results.check(f"{case_id} task registry owns its numbered tasks and four roles", [int(task["number"]) for task in registry_data["tasks"]] == expected_task_numbers and set(registry_data["roles"]) == set(ROLES))
        accessible_pages = soup.select('.page[data-role="accessible"]')
        accessible_task_distribution = [
            [int(node.get("data-task-id") or node.get("data-shell-task-heading")) for node in page.select(".task-heading,[data-shell-task-heading]") if node.get("data-task-id") or node.get("data-shell-task-heading")]
            for page in accessible_pages
        ]
        accessible_task_numbers = [number for page_numbers in accessible_task_distribution for number in page_numbers]
        results.check(f"{case_id} Accessible pages contain one to three complete tasks", all(1 <= len(page_numbers) <= 3 for page_numbers in accessible_task_distribution), accessible_task_distribution)
        results.check(f"{case_id} Accessible task headings are ordered and never duplicated", accessible_task_numbers == expected_task_numbers and len(accessible_task_numbers) == len(set(accessible_task_numbers)), accessible_task_numbers)
        accessible_cer_roots = soup.select('.page[data-role="accessible"] .canonical-cer[data-cer-contract="accessible-v1.0"]')
        accessible_cer_pages = [root.find_parent(class_="page") for root in accessible_cer_roots]
        accessible_cer_subtitles = [page.select_one('[data-accessible-cer-subtitle="canonical-v1.0"]') if page else None for page in accessible_cer_pages]
        cer_labels = [[label.get_text(strip=True) for label in root.select(":scope > .canonical-cer-box > .canonical-cer-label")] for root in accessible_cer_roots]
        results.check(f"{case_id} has one dedicated canonical Accessible CER page", len(accessible_cer_roots) == len(accessible_cer_pages) == 1 and accessible_cer_pages[0].get("data-accessible-cer-page") == "canonical-v1.0" and len(accessible_task_distribution[accessible_pages.index(accessible_cer_pages[0])]) == 1, [page.get("data-page-id") for page in accessible_cer_pages])
        results.check(f"{case_id} Accessible CER has the exact subtitle and Claim/Evidence/Reasoning structure", len(accessible_cer_subtitles) == 1 and accessible_cer_subtitles[0] and accessible_cer_subtitles[0].get_text(" ", strip=True) == ACCESSIBLE_CER_SUBTITLE and cer_labels == [["CLAIM", "EVIDENCE", "REASONING"]], {"subtitles": [node.get_text(" ", strip=True) if node else None for node in accessible_cer_subtitles], "labels": cer_labels})
        results.check(f"{case_id} CER components are page-atomic", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in soup.select("[data-cer-contract],.cer-stack")))
        results.check(f"{case_id} process models are page-atomic", all(all(child.find_parent(class_="page") is root.find_parent(class_="page") for child in root.select("*")) for root in soup.select("[data-process-contract],.process-figure,.linear-process")))
        results.check(f"{case_id} figures and tables retain structure", all(figure.select_one("figcaption") for figure in soup.select("figure")) and all(table.select_one("th") and len(table.select("tr")) >= 2 for table in soup.select("table")))

        presentation = paths["presentation"].read_text(encoding="utf-8")
        whole_page_filter = re.search(r"(?:body|\.page)\.grayscale\s*\{[^}]*filter\s*:", presentation, re.I | re.S)
        results.check(f"{case_id} grayscale uses presentation tokens without whole-page filtering", "grayscale" in presentation.lower() and not whole_page_filter)
        uses_shared_components = package["presentation"].get("sharedComponentStyles") is True
        if case_id not in LEGACY_SELF_STYLED_CASES:
            results.check(f"{case_id} opts into shared protected-component styles", uses_shared_components)
        if uses_shared_components:
            protected_definitions = protected_css_definitions(presentation)
            results.check(f"{case_id} case presentation defines no protected shared selectors", not protected_definitions, protected_definitions)

        lifecycle_findings = corrective_release_lifecycle.history_findings(
            package_path.parents[1], case_id, package, registry_data)
        results.check(f"{case_id} history holds only canonical records at or below its version",
                      not [f for f in lifecycle_findings if "above the package version" in f
                           or "not a canonical" in f or "disagree" in f or "not readable" in f],
                      lifecycle_findings)

        if expected_status == "APPROVED_STABLE":
            history_path = ROOT / package["releaseHistory"]
            history = load_json(history_path)
            history_errors = schema_errors(history, history_schema)
            results.check(f"{case_id} release history validates against schema v1", not history_errors, history_errors)
            former_artifacts = history.get("formerArtifacts", {})
            former_roles = former_artifacts.get("roles", {})
            artifact_record_complete = set(former_roles) == set(ROLES) or former_artifacts.get("status") == "NO_FORMER_GENERATED_ARTIFACTS"
            history_counts = history.get("rolePageCounts", {})
            history_fixed_counts_match = all(history_counts.get(role) == expected_counts[role] for role in expected_counts)
            results.check(f"{case_id} compact release history is complete", history.get("caseId") == case_id and history.get("curriculumVersion") == expected_version and artifact_record_complete and history_fixed_counts_match and isinstance(history_counts.get("accessible"), int) and history.get("formerArtifactRecoveryCommit") and history.get("recovery") and isinstance(history.get("priorApprovedReleases"), list))
        else:
            case_root = package_path.parents[1]
            results.check(f"{case_id} unreleased package declares no release record for its own version", not lifecycle_findings, lifecycle_findings)

        if case_id == "SSS-C1-CASE04":
            task_titles = [task["title"] for task in registry_data["tasks"]]
            # The v1.0 release-lifecycle assertions describe a released package. The final
            # remediation reopened Case 04 as a corrective DRAFT candidate, which by design
            # carries no release history and no owner-review/merge verdict yet, so these run
            # only while the package is actually released. The corrective-candidate lifecycle
            # is validated by validate_sss_final_corrective_candidates.py instead.
            if expected_status == "APPROVED_STABLE":
                results.check("Case 04 task registry records the completed release lifecycle", registry_data.get("version") == "1.1" and registry_data.get("status") == "APPROVED_STABLE" and registry_data.get("ownerReviewStatus") == "OWNER_REVIEW_PASS" and registry_data.get("mergeStatus") == "READY_TO_MERGE")
                results.check("Case 04 release history records a native release with the superseded v1.0 retained as its prior", history.get("formerArtifacts", {}).get("status") == "NO_FORMER_GENERATED_ARTIFACTS" and [prior.get("version") for prior in history.get("priorApprovedReleases", [])] == ["1.0"] and history.get("acceptedPrintStatus") == "PASS at 100% / Actual Size")
            owner_approval_path = package_path.parents[1] / "history/CASE04_OWNER_APPROVAL_v1.0.md"
            owner_approval = owner_approval_path.read_text(encoding="utf-8") if owner_approval_path.is_file() else ""
            results.check("Case 04 owner approval record captures release, review, merge, and no-artifact decisions", all(token in owner_approval for token in ["Nate / Owner", "2026-08-01", "APPROVED_STABLE", "OWNER_REVIEW_PASS", "READY_TO_MERGE", "NO_GENERATED_ARTIFACTS_COMMITTED"]))
            results.check("Case 04 task registry uses the eight locked titles", task_titles == CASE04_TASK_TITLES, task_titles)
            role_task_orders = {
                role: [int(node["data-shell-task-heading"]) for page in soup.select(f'.page[data-role="{role}"]') for node in page.select("[data-shell-task-heading]")]
                for role in ["student", "answer", "accessible"]
            }
            results.check("Case 04 Student, Answer Key, and Accessible task order has exact parity", all(order == expected_task_numbers for order in role_task_orders.values()), role_task_orders)
            results.check("Case 04 visual component contracts are complete", all(soup.select_one(selector) for selector in ["[data-timeline-contract]", "[data-evidence-summary]", "[data-process-contract]", "[data-cause-effect-contract]", "[data-systems-contract]", "[data-cer-contract]"]))
            timeline_roots = soup.select("[data-timeline-contract]")
            process_roots = soup.select("[data-process-contract]")
            results.check("Case 04 timeline and process models are page-atomic", all(root.find_parent(class_="page") is child.find_parent(class_="page") for root in timeline_roots + process_roots for child in root.select("*")))
            accessible_pages = soup.select('.page[data-role="accessible"]')
            results.check("Case 04 Accessible pages preserve document and task reading order", [page.get("data-page-id") for page in accessible_pages] == [f"accessible-mission-{index:02d}" for index in range(1, counts["accessible"] + 1)] and role_task_orders["accessible"] == expected_task_numbers)
            required_sequence = ["Four months of stable operation", "Lighting changes from 16/8 to uncontrolled 24/0", "About one week later: first crash", "Every 6–8 days: another crash", "Between crashes: surviving cells rebuild"]
            results.check("Case 04 uses all locked relative sequence labels", all(label in content for label in required_sequence))
            results.check("Case 04 omits unsupported mission-day and precise-density data", not re.search(r"Day\s*12[18]|culture density\s*[:=]\s*\d", content, re.I))
            results.check("Case 04 keeps reactor-specific continuous-cultivation qualification", "Continuous cultivation may work with appropriate independent intensity, mixing, density, and process controls." in content)
            learner_first_pages = {role: soup.select_one(f'.page[data-role="{role}"]') for role in ["student", "accessible"]}
            expected_fields = {
                "student": ["student-name", "student-date", "student-class"],
                "accessible": ["a-name", "a-date", "a-class"],
            }
            id_contracts = {}
            for role, page in learner_first_pages.items():
                row = page.select_one(".student-id") if page else None
                fields = row.select(":scope > .id-field") if row else []
                id_contracts[role] = bool(
                    row
                    and row.get("aria-label") == "Student identification"
                    and row.parent.select_one(":scope > :first-child") is row
                    and len(fields) == 3
                    and [field.select_one(":scope > strong").get_text(strip=True) if field.select_one(":scope > strong") else None for field in fields] == ["Name", "Date", "Period"]
                    and [field.select_one(":scope > span").get("data-field") if field.select_one(":scope > span") else None for field in fields] == expected_fields[role]
                    and all(field.name == "div" and not field.select("label") for field in fields)
                )
            results.check("Case 04 Student and Accessible use the exact canonical identification-row structure", all(id_contracts.values()), id_contracts)

            first_pages = [soup.select_one(f'.page[data-role="{role}"]') for role in ROLES]
            title_blocks = [page.select_one('.mission-title-block[data-header-contract="printable-v1.1"]') if page else None for page in first_pages]
            title_contract = all(
                title
                and [child.get("class", [None])[0] for child in title.find_all(recursive=False)] == ["mission-rail", "mission-title-copy", "identity-mark"]
                and title.select_one(":scope > .mission-title-copy > .hero-title")
                and title.select_one(":scope > .mission-title-copy > .mission-subtitle")
                and title.select_one(':scope > .identity-mark > img.saa-insignia[alt="Solar Agricultural Agency insignia"][src="../../../../shared/assets/insignia/saa.svg"]')
                and title.select_one(":scope > .identity-mark > .identity-copy > .institution")
                and title.select_one(":scope > .identity-mark > .identity-copy > .document-role")
                for title in title_blocks
            )
            results.check("Case 04 first-page title blocks use the exact shared child contract and SAA image", title_contract)
            results.check("Case 04 mission subtitle uses the locked punctuation", all(title.select_one(".mission-subtitle").get_text(strip=True) == "Campaign 1 · Case 04 · L2 Lagrange Point, Orbital Research Station" for title in title_blocks if title))

            continuation_headers = soup.select('.continuation-header[data-header-contract="printable-v1.1"]')
            expected_continuations = sum(counts.values()) - len(ROLES)
            continuation_contract = len(continuation_headers) == expected_continuations and all(
                [child.get("class", [None])[0] for child in header.find_all(recursive=False)] == ["continuation-copy", "continuation-identity"]
                and header.select_one(":scope > .continuation-copy > h1")
                and header.select_one(":scope > .continuation-copy > .continuation-role")
                and header.select_one(':scope > .continuation-identity > img.saa-insignia[alt="Solar Agricultural Agency insignia"][src="../../../../shared/assets/insignia/saa.svg"]')
                and header.select_one(":scope > .continuation-identity > .institution")
                for header in continuation_headers
            )
            results.check("Case 04 continuation headers use the exact shared child contract and SAA image", continuation_contract, len(continuation_headers))
            saa_asset = next((asset for asset in package["assets"] if asset["id"] == "saa-insignia"), None)
            results.check("Case 04 package embeds the shared SAA SVG asset", saa_asset == {"id": "saa-insignia", "type": "image/svg+xml", "source": "shared/assets/insignia/saa.svg", "selector": ".saa-insignia", "embed": True}, saa_asset)

            cer_contracts = {root.get("data-cer-contract"): [box.select_one(":scope > .canonical-cer-label").get_text(strip=True) if box.select_one(":scope > .canonical-cer-label") else None for box in root.select(":scope > .canonical-cer-box")] for root in soup.select(".canonical-cer[data-cer-contract]")}
            results.check("Case 04 CER uses only the three approved atomic contracts", cer_contracts == {"student-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "answer-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "accessible-v1.0": ["CLAIM", "EVIDENCE", "REASONING"]}, cer_contracts)
            student_distribution = [[int(node["data-shell-task-heading"]) for node in page.select("[data-shell-task-heading]")] for page in soup.select('.page[data-role="student"]')]
            results.check("Case 04 Student page 1 contains complete Tasks 1 and 2 and does not split Task 3", student_distribution[0] == [1, 2] and student_distribution[1][0] == 3, student_distribution)
            task_two = soup.select_one('.page[data-page-id="student-mission-01"] .task-block [data-shell-task-heading="2"]')
            results.check("Case 04 Student Task 2 is atomic on page 1", bool(task_two and task_two.find_parent(class_="task-block") and task_two.find_parent(class_="task-block").find_parent(class_="page").get("data-page-id") == "student-mission-01"))

        if case_id == "SSS-C1-CASE05":
            task_titles = [task["title"] for task in registry_data["tasks"]]
            results.check("Case 05 task registry records the completed release lifecycle", registry_data.get("version") == "1.1" and registry_data.get("status") == "APPROVED_STABLE" and registry_data.get("ownerReviewStatus") == "OWNER_REVIEW_PASS" and registry_data.get("mergeStatus") == "READY_TO_MERGE" and package.get("approval", {}).get("printStatus") == "PASS" and registry_data.get("gameCommit") == "a7a725121f261373df32a5366c70e7df73ddf8f3")
            results.check("Case 05 task registry uses the eight locked titles", task_titles == CASE05_TASK_TITLES, task_titles)
            role_task_orders = {
                role: [int(node["data-shell-task-heading"]) for page in soup.select(f'.page[data-role="{role}"]') for node in page.select("[data-shell-task-heading]")]
                for role in ["student", "answer", "accessible"]
            }
            results.check("Case 05 Student, Answer Key, and Accessible task order has exact parity", all(order == expected_task_numbers for order in role_task_orders.values()), role_task_orders)
            expected_page_ids = {
                "student": [f"student-mission-{index:02d}" for index in range(1, 5)],
                "teacher": [f"teacher-guide-{index:02d}" for index in range(1, 9)],
                "answer": [f"answer-key-{index:02d}" for index in range(1, 5)],
                "accessible": [f"accessible-mission-{index:02d}" for index in range(1, 8)],
            }
            actual_page_ids = {role: [page.get("data-page-id") for page in soup.select(f'.page[data-role="{role}"]')] for role in ROLES}
            results.check("Case 05 page IDs preserve role and accessible reading order", actual_page_ids == expected_page_ids, actual_page_ids)

            required_clues = ["CONSISTENT_FAILURE", "HIGH_RADIATION", "DNA_DAMAGE_PATTERN", "SHIELDING_INSUFFICIENT"]
            results.check("Case 05 retains all four formal clue tags internally and omits them from printable content", all(clue in registry_data.get("formalClues", []) and clue not in content for clue in required_clues))
            results.check("Case 05 preserves radiation and the three plausible alternatives", registry_data.get("correctDiagnosis") == "radiation" and registry_data.get("incorrectAlternatives") == ["gravity", "minerals", "light"] and all(term in content for term in ["Gravity", "Minerals", "Light", "Radiation"]))
            required_science = [
                "energetic particles", "Jupiter’s magnetosphere", "ionizing radiation", "modeled secondary radiation",
                "dividing and nondividing cells", "meristem", "exposure alone does not", "best-supported diagnosis",
                "Crew and crop risk require separate assessment", "Brown spots alone do not",
            ]
            results.check("Case 05 preserves corrected qualitative science distinctions", all(term in content for term in required_science), [term for term in required_science if term not in content])
            prohibited_radiation = re.compile(
                r"\b(?:\d+(?:\.\d+)?\s*(?:mSv|Sv|Gy)(?:/\w+)?|annual equivalent|annual eq|human occupational limit|"
                r"rotation\s*:\s*\d|shielding (?:reduction|efficacy)\s*:\s*\d|required reduction|actual reduction|"
                r"deficit\s*:\s*\d|strand breaks per cell|meristematic tissue\. Mature plants|verified warning level|"
                r"randomness rules out|proportional to replication rate|DNA replication errors|secondary neutron cascade from Jupiter['’]s magnetosphere)\b",
                re.I,
            )
            results.check("Case 05 contains no unsupported quantities or superseded GC-01 through GC-04 wording", not prohibited_radiation.search(content), prohibited_radiation.search(content).group(0) if prohibited_radiation.search(content) else "")
            results.check("Case 05 uses no scene sprite or replacement artwork", not soup.select("figure,.scene,.hero-visual") and all(img.get("class") == ["saa-insignia"] for img in soup.select("img")))

            student_bank = [node.get_text(" ", strip=True) for node in soup.select('.page[data-role="student"] .phrase-bank span')]
            accessible_bank = [node.get_text(" ", strip=True) for node in soup.select('.page[data-role="accessible"] .phrase-bank span')]
            answer_sequence = [node.get_text(" ", strip=True).lower() for node in soup.select('.page[data-role="answer"] [data-process-contract] [data-process-stage] strong')][1:]
            results.check("Case 05 Task 5 word banks match and remain out of answer order", student_bank == accessible_bank and set(map(str.lower, student_bank)) == set(answer_sequence) and list(map(str.lower, student_bank)) != answer_sequence, {"student": student_bank, "answer": answer_sequence})
            results.check("Case 05 word banks have visible exact labels", len(soup.select('.page[data-role="student"] .response-label')) > 0 and all("WORD BANK" in page.get_text(" ", strip=True) for page in [soup.select_one('.page[data-page-id="student-mission-03"]'), soup.select_one('.page[data-page-id="accessible-mission-05"]')]))

            teacher_text = " ".join(page.get_text(" ", strip=True) for page in soup.select('.page[data-role="teacher"]'))
            teacher_components = [
                "Lesson overview", "Measurable objectives", "Success criteria", "Standards alignment and limitation",
                "Academic vocabulary", "Materials and technology", "Preparation", "Facilitation guidance",
                "Likely misconceptions", "Accessibility and differentiation", "Evidence analysis",
                "Annotated answers and grading guidance", "Quick grading", "Analytic rubric · 4/3/2/1",
                "References", "Technical notes",
            ]
            results.check("Case 05 Teacher Guide includes all required production components", all(term in teacher_text for term in teacher_components), [term for term in teacher_components if term not in teacher_text])
            results.check("Case 05 directly assesses MS-ETS1-1 and limits MS-ETS1-2 to supporting alignment", "Direct assessment: MS-ETS1-1" in teacher_text and "Supporting alignment: MS-ETS1-2" in teacher_text and "Do not claim direct assessment of MS-ETS1-2" in teacher_text)
            results.check("Case 05 distinguishes immediate operations from durable engineering", all(term in content for term in ["Immediate operational response", "Durable engineering response", "criteria", "constraints", "verification"]))
            results.check("Case 05 keeps the engineering scope in teacher guidance without an unnecessary student banner", "The class must design a proven shield" in teacher_text and "does not validate a radiation-transport solution" in teacher_text and "This is a classroom design task" not in content)

            learner_first_pages = {role: soup.select_one(f'.page[data-role="{role}"]') for role in ["student", "accessible"]}
            expected_fields = {"student": ["student-name", "student-date", "student-class"], "accessible": ["a-name", "a-date", "a-class"]}
            id_contracts = {}
            for role, page in learner_first_pages.items():
                row = page.select_one(".student-id") if page else None
                fields = row.select(":scope > .id-field") if row else []
                id_contracts[role] = bool(
                    row and row.parent.select_one(":scope > :first-child") is row and len(fields) == 3
                    and [field.select_one(":scope > strong").get_text(strip=True) for field in fields] == ["Name", "Date", "Period"]
                    and [field.select_one(":scope > span").get("data-field") for field in fields] == expected_fields[role]
                )
            results.check("Case 05 Student and Accessible identification rows use the shared contract", all(id_contracts.values()), id_contracts)
            first_pages = [soup.select_one(f'.page[data-role="{role}"]') for role in ROLES]
            title_blocks = [page.select_one('.mission-title-block[data-header-contract="printable-v1.1"]') for page in first_pages]
            results.check("Case 05 first-page title blocks separate title from location subtitle", all(title and title.select_one(".hero-title").get_text(strip=True) == "Sub Surface Bunker" and title.select_one(".mission-subtitle").get_text(strip=True) == "Campaign 1 · Case 05 · Europa, Sub-Surface Bunker" and title.select_one('img.saa-insignia[alt="Solar Agricultural Agency insignia"]') for title in title_blocks))
            continuation_headers = soup.select('.continuation-header[data-header-contract="printable-v1.1"]')
            results.check("Case 05 continuation identity count and structure are exact", len(continuation_headers) == sum(counts.values()) - len(ROLES) and all(header.select_one(".continuation-copy > h1") and header.select_one(".continuation-identity > .institution") for header in continuation_headers), len(continuation_headers))
            cer_contracts = {root.get("data-cer-contract"): [box.select_one(":scope > .canonical-cer-label").get_text(strip=True) for box in root.select(":scope > .canonical-cer-box")] for root in soup.select(".canonical-cer[data-cer-contract]")}
            results.check("Case 05 CER uses the three shared atomic contracts", cer_contracts == {"student-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "answer-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "accessible-v1.0": ["CLAIM", "EVIDENCE", "REASONING"]}, cer_contracts)

        if case_id == "SSS-C1-CASE06":
            task_titles = [task["title"] for task in registry_data["tasks"]]
            results.check("Case 06 task registry records the completed release lifecycle and frozen game baseline", registry_data.get("status") == "APPROVED_STABLE" and registry_data.get("ownerReviewStatus") == "OWNER_REVIEW_PASS" and registry_data.get("mergeStatus") == "READY_TO_MERGE" and registry_data.get("gameCommit") == "d723fb9b8085905a6048575a2cb3bb0fce1d312b" and package.get("approval", {}).get("printStatus") == "PASS")
            if expected_status == "APPROVED_STABLE":  # release history exists only for a released package
                results.check("Case 06 release history records a native release, approved print gate, and frozen game baseline", history.get("formerArtifacts", {}).get("status") == "NO_FORMER_GENERATED_ARTIFACTS" and [prior.get("version") for prior in history.get("priorApprovedReleases", [])] == ["1.0"] and history.get("acceptedPrintStatus") == "PASS at 100% / Actual Size" and any("d723fb9b8085905a6048575a2cb3bb0fce1d312b" in note for note in history.get("migrationNotes", [])))
            owner_approval_path = package_path.parents[1] / "history/CASE06_OWNER_APPROVAL_v1.0.md"
            owner_approval = owner_approval_path.read_text(encoding="utf-8") if owner_approval_path.is_file() else ""
            results.check("Case 06 owner approval record captures all owner gates and no-artifact decision", all(token in owner_approval for token in ["Nate / Owner", "2026-08-03", "APPROVED_STABLE", "OWNER_REVIEW_PASS", "READY_TO_MERGE", "On-screen content and visual review: **PASS**", "Generated PDF review: **PASS**", "Physical print at 100% / Actual Size: **PASS**", "NO_GENERATED_ARTIFACTS_COMMITTED"]))
            results.check("Case 06 task registry uses the eight design-locked titles", task_titles == CASE06_TASK_TITLES, task_titles)
            role_task_orders = {
                role: [int(node["data-shell-task-heading"]) for page in soup.select(f'.page[data-role="{role}"]') for node in page.select("[data-shell-task-heading]")]
                for role in ["student", "answer", "accessible"]
            }
            results.check("Case 06 Student, Answer Key, and Accessible task order has exact parity", all(order == expected_task_numbers for order in role_task_orders.values()), role_task_orders)
            expected_page_ids = {
                "student": [f"student-mission-{index:02d}" for index in range(1, 6)],
                "teacher": [f"teacher-guide-{index:02d}" for index in range(1, 9)],
                "answer": [f"answer-key-{index:02d}" for index in range(1, 6)],
                "accessible": [f"accessible-mission-{index:02d}" for index in range(1, 8)],
            }
            actual_page_ids = {role: [page.get("data-page-id") for page in soup.select(f'.page[data-role="{role}"]')] for role in ROLES}
            results.check("Case 06 page IDs preserve role and Accessible reading order", actual_page_ids == expected_page_ids, actual_page_ids)

            required_clues = ["SYMBIOSIS_BROKEN", "HUMAN_SCRUBBERS_ACTIVE", "NETWORK_DORMANT", "VOC_SIGNALING"]
            required_routes = ["crew.start->symbiosis_detail", "sensors.start->atmosphere", "plants.start->network", "logs.start->network_comm"]
            results.check("Case 06 retains the four audited clues internally and omits clue IDs from printable content", registry_data.get("formalClues") == required_clues and all(clue not in content for clue in required_clues))
            results.check("Case 06 retains exactly the four audited evidence routes", registry_data.get("requiredRoutes") == required_routes, registry_data.get("requiredRoutes"))
            alternatives = ["physical docking damage", "atmospheric drift during the journey", "incompatibility among the three organisms"]
            results.check("Case 06 preserves one correct diagnosis and the three audited distractors", registry_data.get("correctDiagnosis") == "human atmospheric processing filtered the volatile signal compounds, triggering network dormancy and loss of symbiosis coordination" and registry_data.get("incorrectAlternatives") == alternatives)
            timing = registry_data.get("timingLedger", {})
            results.check("Case 06 timing ledger proves docking precedes the last signal by 0.3 hours or 18 minutes", timing.get("dockingHoursAgo") > timing.get("lastSignalHoursAgo") and round(timing.get("dockingHoursAgo") - timing.get("lastSignalHoursAgo"), 1) == timing.get("differenceHours") == 0.3 and timing.get("differenceMinutes") == 18)
            results.check("Case 06 printable evidence preserves the corrected timing and causation qualification", all(term in content for term in ["72.4 hours ago", "72.1 hours ago", "18 minutes", "correlation alone does not prove it", "It remains correlation, not proof"]))
            student_bank = [node.get_text(" ", strip=True) for node in soup.select('.page[data-page-id="student-mission-02"] .phrase-bank span')]
            accessible_bank = [node.get_text(" ", strip=True) for node in soup.select('.page[data-page-id="accessible-mission-03"] .phrase-bank span')]
            ordered_bank = [
                "human-standard filtration removes unfamiliar signaling compounds",
                "network signals fall to zero and cannot persist",
                "the fictional network enters reversible dormancy when signals do not persist",
                "nutrient transfer and coordination stop",
            ]
            results.check("Case 06 Task 4 phrase banks match across learner roles and remain out of answer order", student_bank == accessible_bank and set(student_bank) == set(ordered_bank) and student_bank != ordered_bank, student_bank)
            model_arrow_contracts = [model.select(":scope > .path-arrow") for model in soup.select('[data-process-contract="atmosphere-signal-partnership-v1.0"]')]
            results.check("Case 06 Task 4 models use three standardized path arrows in every role", len(model_arrow_contracts) == 3 and all(len(arrows) == 3 for arrows in model_arrow_contracts), [len(arrows) for arrows in model_arrow_contracts])

            learner_text = " ".join(page.get_text(" ", strip=True) for page in soup.select('.page[data-role="student"],.page[data-role="accessible"]'))
            teacher_text = " ".join(page.get_text(" ", strip=True) for page in soup.select('.page[data-role="teacher"]'))
            results.check("Case 06 learner pages keep the Earth analogy and audit vocabulary out of the assessed evidence", not re.search(r"mother trees?|wood wide web|forest-wide|superorganism|biological networks? as an internet|source classification|audit terminology", learner_text, re.I))
            results.check("Case 06 Teacher Guide preserves qualified science and fiction categories", all(term in teacher_text for term in ["Established Earth science", "Debated or context-dependent Earth interpretation", "Plausible engineering extrapolation", "Fictional alien biology and measurement", "Curriculum-created model", "Alien evidence cannot serve as empirical proof about Earth ecosystems"]))
            results.check("Case 06 uses the corrected NASA system source and EPA adsorption qualification", "https://ntrs.nasa.gov/citations/20170005170" in teacher_text and "NASA/TP-2017-218235" in teacher_text and "https://www.epa.gov/air-emissions-monitoring-knowledge-base/monitoring-control-technique-activated-carbon-adsorber" in teacher_text and all(term in teacher_text for term in ["finite capacity", "breakthrough", "compound properties", "flow", "temperature", "moisture"]))
            results.check("Case 06 rejects blanket life-support disablement and requires monitored selective treatment", all(term in content for term in ["Do not accept blanket disablement", "pressure, breathable gas, and contaminant control", "monitored", "reversible", "selectively preserve"]))
            results.check("Case 06 keeps Case 07 evidence and resolution outside learner tasks", "GERMINATION-CASCADE" not in content and "alien2" not in content and not re.search(r"germination[- ]pod|network-derived germination|germination compound", learner_text, re.I) and "Do not introduce germination-pod evidence" in teacher_text)

            first_pages = [soup.select_one(f'.page[data-role="{role}"]') for role in ROLES]
            title_blocks = [page.select_one('.mission-title-block[data-header-contract="printable-v1.1"]') for page in first_pages]
            results.check("Case 06 title blocks use the audited location and canonical SAA identity", all(title and title.select_one(".hero-title").get_text(strip=True) == "First Contact Protocol" and title.select_one(".mission-subtitle").get_text(strip=True) == "Campaign 1 · Case 06 · Zhel'ora Botanical Vessel" and title.select_one('img.saa-insignia[alt="Solar Agricultural Agency insignia"]') for title in title_blocks))
            learner_first_pages = {role: soup.select_one(f'.page[data-role="{role}"]') for role in ["student", "accessible"]}
            expected_fields = {"student": ["student-name", "student-date", "student-class"], "accessible": ["a-name", "a-date", "a-class"]}
            id_contracts = {}
            for role, page in learner_first_pages.items():
                row = page.select_one(".student-id") if page else None
                fields = row.select(":scope > .id-field") if row else []
                id_contracts[role] = bool(row and row.parent.select_one(":scope > :first-child") is row and [field.select_one(":scope > strong").get_text(strip=True) for field in fields] == ["Name", "Date", "Period"] and [field.select_one(":scope > span").get("data-field") for field in fields] == expected_fields[role])
            results.check("Case 06 Student and Accessible identification rows use the shared contract", all(id_contracts.values()), id_contracts)
            cer_contracts = {root.get("data-cer-contract"): [box.select_one(":scope > .canonical-cer-label").get_text(strip=True) for box in root.select(":scope > .canonical-cer-box")] for root in soup.select(".canonical-cer[data-cer-contract]")}
            results.check("Case 06 CER uses the three shared atomic contracts", cer_contracts == {"student-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "answer-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "accessible-v1.0": ["CLAIM", "EVIDENCE", "REASONING"]}, cer_contracts)
            student_cer_page = soup.select_one('.page[data-role="student"]:has([data-cer-contract="student-v1.0"])')
            student_cer_subtitle = student_cer_page.select_one('[data-student-cer-subtitle="canonical-v1.0"]') if student_cer_page else None
            results.check("Case 06 Student CER occupies a dedicated page with the exact subtitle", bool(student_cer_page and [node.get("data-shell-task-heading") for node in student_cer_page.select("[data-shell-task-heading]")] == ["7"] and student_cer_subtitle and student_cer_subtitle.get_text(" ", strip=True) == ACCESSIBLE_CER_SUBTITLE))
            teacher_components = ["Learning target", "Standards alignment and limitation", "Materials and preparation", "Suggested pacing", "Evidence checkpoints", "Discussion guidance", "Likely misconceptions", "Accessibility and differentiation guidance", "Science and fiction distinctions", "Intervention caution", "Independent assessment guidance", "Science-source ledger"]
            results.check("Case 06 Teacher Guide includes all required instructional metadata", all(term in teacher_text for term in teacher_components), [term for term in teacher_components if term not in teacher_text])
            answer_pages = soup.select('.page[data-role="answer"]')
            results.check("Case 06 Answer Key provides a completed exemplar for every task", all(page.get_text(" ", strip=True) for page in answer_pages) and role_task_orders["answer"] == expected_task_numbers and all(term in " ".join(page.get_text(" ", strip=True) for page in answer_pages) for term in ["Initial prediction", "Why the distinction matters", "Completed exemplar", "Best supported", "Recommendation", "CLAIM", "EVIDENCE", "REASONING", "Independent exit response"]))

        if case_id == "SSS-C1-CASE07":
            task_titles = [task["title"] for task in registry_data["tasks"]]
            results.check("Case 07 task registry records the completed release lifecycle and exact frozen baselines", registry_data.get("status") == "APPROVED_STABLE" and registry_data.get("ownerReviewStatus") == "OWNER_REVIEW_PASS" and registry_data.get("mergeStatus") == "READY_TO_MERGE" and registry_data.get("gameCommit") == "a813c209dfde00634103f74d6673e7d4433e0e63" and registry_data.get("auditCommit") == "76a908400eb53c1c81fe91ce52337f414ae2c591" and package.get("approval") == {"date": "2026-08-10", "owner": "Nate / Owner", "status": "APPROVED", "printStatus": "PASS"})
            if expected_status == "APPROVED_STABLE":  # release history exists only for a released package
                results.check("Case 07 release history records a native release, approved print gate, and frozen game/audit baselines", history.get("formerArtifacts", {}).get("status") == "NO_FORMER_GENERATED_ARTIFACTS" and [prior.get("version") for prior in history.get("priorApprovedReleases", [])] == ["1.0"] and history.get("acceptedPrintStatus") == "PASS at 100% / Actual Size" and any("a813c209dfde00634103f74d6673e7d4433e0e63" in note for note in history.get("migrationNotes", [])) and any("76a908400eb53c1c81fe91ce52337f414ae2c591" in note for note in history.get("migrationNotes", [])))
            owner_approval_path = package_path.parents[1] / "history/CASE07_OWNER_APPROVAL_v1.0.md"
            owner_approval = owner_approval_path.read_text(encoding="utf-8") if owner_approval_path.is_file() else ""
            results.check("Case 07 owner approval record captures all owner gates and no-artifact decision", all(token in owner_approval for token in ["Nate / Owner", "2026-08-03", "APPROVED_STABLE", "OWNER_REVIEW_PASS", "READY_TO_MERGE", "On-screen content and visual review: **PASS**", "Generated PDF review: **PASS**", "Physical print at 100% / Actual Size: **PASS**", "NO_GENERATED_ARTIFACTS_COMMITTED"]))
            results.check("Case 07 task registry uses the eight production-locked titles", task_titles == CASE07_TASK_TITLES, task_titles)
            role_task_orders = {
                role: [int(node["data-shell-task-heading"]) for page in soup.select(f'.page[data-role="{role}"]') for node in page.select("[data-shell-task-heading]")]
                for role in ["student", "answer", "accessible"]
            }
            results.check("Case 07 Student, Answer Key, and Accessible task order has exact parity with each task once", all(order == expected_task_numbers and len(order) == len(set(order)) for order in role_task_orders.values()), role_task_orders)
            expected_page_ids = {
                "student": [f"student-mission-{index:02d}" for index in range(1, 7)],
                "teacher": [f"teacher-guide-{index:02d}" for index in range(1, 9)],
                "answer": [f"answer-key-{index:02d}" for index in range(1, 7)],
                "accessible": [f"accessible-mission-{index:02d}" for index in range(1, 9)],
            }
            actual_page_ids = {role: [page.get("data-page-id") for page in soup.select(f'.page[data-role="{role}"]')] for role in ROLES}
            results.check("Case 07 page IDs and continuous Accessible reading order are exact", actual_page_ids == expected_page_ids, actual_page_ids)

            required_task_fields = {"id", "number", "semanticLabel", "icon", "title", "description", "instructionalPurpose", "provenance", "responseType", "answerScope", "pagePlacement", "editions", "keyed"}
            results.check("Case 07 task registry owns exact IDs, purpose, provenance, response type, answer scope, edition presence, and page placement", [task.get("id") for task in registry_data["tasks"]] == [f"C07-T{number}" for number in expected_task_numbers] and all(set(task) == required_task_fields and task["editions"] == ROLES and set(task["pagePlacement"]) == set(ROLES) for task in registry_data["tasks"]))
            results.check("Case 07 task registry page placement names existing role pages", all(soup.select_one(f'.page[data-role="{role}"][data-page-id="{page_id}"]') for task in registry_data["tasks"] for role, page_id in task["pagePlacement"].items()))

            required_clues = ["PROXIMITY_REQUIRED", "MISSING_VOCS", "WAITING_FOR_TRIGGER", "GERMINATION_COMPOUND"]
            required_routes = ["crew.proximity_detail", "crew.isolated_germination", "sensors.atmosphere", "sensors.comparison", "plants.receptors", "plants.what_signal", "logs.germination", "logs.signal_chemistry"]
            results.check("Case 07 retains exactly four essential internal clues and eight reveal routes", registry_data.get("formalClues") == required_clues and registry_data.get("requiredRoutes") == required_routes and len(set(required_routes)) == 8)
            results.check("Case 07 internal IDs, aliases, and clue tags never appear in printable content", all(token not in content for token in [*required_clues, "alien2", "Case6b", "Case 6b", "germination_compound", "wrong_light", "transfer_damage", "human_microbes"]))
            alternatives = ["artificial light lacks a critical wavelength", "transfer damaged or killed the pod", "human microbes inhibit germination"]
            results.check("Case 07 preserves the exact cue diagnosis and three audited distractors", registry_data.get("correctDiagnosis") == "the viable pod is dormant because the isolated lab lacks the short-lived germination cue produced by the mature Zhel'ii biological network" and registry_data.get("incorrectAlternatives") == alternatives)

            learner_text = " ".join(page.get_text(" ", strip=True) for page in soup.select('.page[data-role="student"],.page[data-role="accessible"]'))
            teacher_text = " ".join(page.get_text(" ", strip=True) for page in soup.select('.page[data-role="teacher"]'))
            answer_text = " ".join(page.get_text(" ", strip=True) for page in soup.select('.page[data-role="answer"]'))
            results.check("Case 07 learner evidence contains all four channels, direct trace comparison, viability, Case 06, mature source, receptor reasoning, diagnosis, interventions, prediction, synthesis, and exit", all(term in learner_text for term in ["Liaison", "Biomonitors", "Specimen", "Archives", "12 trace identifiers", "847 or more", "viable", "dormant", "Case 06", "mature network", "receptors", "Light lacks", "Transfer damaged", "Human microbes", "Sealed natural plume", "Verified extraction", "Validated synthesis", "12, 18, or 24", "Case comparison", "Independent exit response"]))
            results.check("Case 07 accurately distinguishes measured match from biological completeness", all(term in content for term in ["99.7% primary-condition similarity", "Trace compounds are excluded", "no weighting formula is supplied", "does not mean every biological condition is present"]))
            results.check("Case 07 viability reasoning is qualified and receptor evidence does not overclaim", all(term in content for term in ["viable and dormant", "do not identify what signal is missing", "Response does not identify ligand structure", "does not reveal ligand", "safe dose"]))
            results.check("Case 07 connects Case 06 evidence while clearly distinguishing the immediate mechanisms", all(term in content for term in ["Connection to Case 06", "atmospheric processing removed", "never included the mature living source", "signal became unavailable for different reasons"]))

            ledger = registry_data.get("conditionLedger", {})
            trace = ledger.get("traceIdentifiers", {})
            results.check("Case 07 formula and molecular mass are exact and formula insufficiency is explicit", ledger.get("formula") == "C47H63N5O8S2" and ledger.get("formulaMassDa") == 890.17 and all(term in teacher_text for term in ["890.168 Da → 890.17 Da", "Formula does not supply structure, stereochemistry, biology, volatility, carrier, dose, purity, or safe synthesis"]))
            results.check("Case 07 trace ledger rejects a misleading coverage ratio while preserving temperature and humidity arithmetic", trace == {"lab": 12, "livingAreaMinimum": 847, "setsMatch": False, "ratioIsCoverage": False} and ledger.get("temperature", {}).get("differenceC") == 0.2 and ledger.get("humidity", {}).get("differencePercentagePoints") == -1 and all(term in content for term in ["Do not calculate “trace coverage”", "the identifier sets differ", "+0.2 °C", "1 percentage point"]))
            results.check("Case 07 distance and timing ledger preserves supported fictional units", ledger.get("range") == {"aboveThresholdThroughM": 3, "currentSeparationM": 40, "currentPath": "closed corridors", "supportedTransferLine": "sealed and shorter than 3 m"} and ledger.get("cycleEarthHours") == 6 and ledger.get("firstResponseHours") == [12, 18, 24] and ledger.get("stabilizationHours") == [24, 36] and all(term in content for term in ["less-than-3-m", "about 40 m", "12, 18, or 24 h", "24–36 h"]))
            results.check("Case 07 never invents a safe numerical dose", ledger.get("safeNumericalDose") is None and all(term in content for term in ["no safe numerical dose", "Do not invent one", "does not supply structure"]) and not re.search(r"safe (?:dose|concentration)\s*(?:is|=|:)\s*\d", content, re.I))

            interventions = registry_data.get("interventions", [])
            results.check("Case 07 intervention ranking and controls are complete while directions require evidence rather than points", [(item.get("id"), item.get("score")) for item in interventions] == [("proximity", 10), ("extract", 5), ("synthesize", 0)] and all(term in content for term in ["cell exclusion", "cross-contamination", "purity", "co-extraction", "stereochemistry", "authentic-standard comparison", "stopping rule", "joint authorization", "story rankings", "evidence, not points"]))
            results.check("Case 07 predicted outcomes are consistently labeled modeled or narrated rather than replicated trials", all(term in content for term in ["modeled/narrated outcomes", "not replicated tests", "not been tested in repeated trials", "modeled/narrated prediction"]))
            results.check("Case 07 operationalizes all four production cautions", len(registry_data.get("productionCautions", [])) == 4 and "MISSING_VOCS" not in content and all(term in content for term in ["no weighting formula", "no safe numerical dose", "not repeated trials"]))

            first_pages = [soup.select_one(f'.page[data-role="{role}"]') for role in ROLES]
            title_blocks = [page.select_one('.mission-title-block[data-header-contract="printable-v1.1"]') for page in first_pages]
            results.check("Case 07 title blocks preserve title, station subtitle, SAA identity, and distinct package location", package.get("location") == "SAA Xenobiology Lab" and package.get("subtitle") == "Campaign 1 · Case 07 · L2 Station Hayes — Secure Cultivation Wing" and all(title and title.select_one(".hero-title").get_text(strip=True) == "The Gift" and title.select_one(".mission-subtitle").get_text(strip=True) == package["subtitle"] and title.select_one('img.saa-insignia[alt="Solar Agricultural Agency insignia"]') for title in title_blocks))
            student_cer_page = soup.select_one('.page[data-role="student"]:has([data-cer-contract="student-v1.0"])')
            student_cer_subtitle = student_cer_page.select_one('[data-student-cer-subtitle="canonical-v1.0"]') if student_cer_page else None
            cer_contracts = {root.get("data-cer-contract"): [box.select_one(":scope > .canonical-cer-label").get_text(strip=True) for box in root.select(":scope > .canonical-cer-box")] for root in soup.select(".canonical-cer[data-cer-contract]")}
            results.check("Case 07 CER uses three shared atomic contracts", cer_contracts == {"student-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "answer-v1.0": ["CLAIM", "EVIDENCE", "REASONING"], "accessible-v1.0": ["CLAIM", "EVIDENCE", "REASONING"]}, cer_contracts)
            results.check("Case 07 Student CER follows Task 5 on page 4 with the exact subtitle", bool(student_cer_page and student_cer_page.get("data-page-id") == "student-mission-04" and student_cer_page.get("data-student-cer-page") == "combined-v1.0" and [node.get("data-shell-task-heading") for node in student_cer_page.select("[data-shell-task-heading]")] == ["5", "6"] and student_cer_subtitle and student_cer_subtitle.get_text(" ", strip=True) == ACCESSIBLE_CER_SUBTITLE))
            accessible_cer_page = soup.select_one('.page[data-role="accessible"]:has([data-cer-contract="accessible-v1.0"])')
            results.check("Case 07 Accessible CER remains a dedicated Task 6 page", bool(accessible_cer_page and accessible_cer_page.get("data-page-id") == "accessible-mission-06" and [node.get("data-shell-task-heading") for node in accessible_cer_page.select("[data-shell-task-heading]")] == ["6"]))
            results.check("Case 07 figures have captions, direct labels, extended descriptions, and accessible names", len(soup.select("figure")) >= 5 and all(figure.select_one("figcaption") and figure.select_one(".extended-description") and figure.select_one('[role="img"][aria-label]') for figure in soup.select("figure")))
            student_task4_bank = [node.get_text(" ", strip=True) for node in soup.select('.page[data-role="student"] [aria-label="Task 4 phrase bank"] span')]
            accessible_task4_bank = [node.get_text(" ", strip=True) for node in soup.select('.page[data-role="accessible"] [aria-label="Accessible Task 4 phrase bank"] span')]
            results.check("Case 07 Task 4 gives both learner editions one matching six-phrase completion bank", len(student_task4_bank) == 6 and student_task4_bank == accessible_task4_bank, {"student": student_task4_bank, "accessible": accessible_task4_bank})
            results.check("Case 07 Tasks 4 and 7 give direct numbered completion steps and actionable response labels", all(term in learner_text for term in ["Step 1", "Step 2", "Step 3", "How the first missing stage stops the chain", "Chosen route + two supporting details", "What to monitor + when to stop", "result that would weaken the prediction"]))
            continued_labels = {"student": "Student Mission · Continued", "teacher": "Teacher Guide · Continued", "answer": "Answer Key · Continued", "accessible": "Accessible Mission · Continued"}
            results.check("Case 07 source uses the canonical Continued subtitle on every secondary-page banner", all(header.select_one(".continuation-role").get_text(" ", strip=True) == continued_labels[header.find_parent(class_="page").get("data-role")] for header in soup.select('[data-page-identity="continuation"]')))

            teacher_components = ["Lesson overview", "Measurable objectives", "Standards alignment and limitation", "Materials and technology", "Preparation", "Suggested pacing", "Launch / gameplay / post-game flow", "Essential evidence ledger", "Fallback if gameplay is unavailable", "Check for understanding", "Discussion guidance", "Likely misconceptions", "Accessibility and differentiation guidance", "Independent assessment guidance", "Quick grading", "Formal grading dimensions", "Acceptable answer", "Full exemplars", "Science and fiction distinctions", "Science-source ledger and references", "Source-status ledger"]
            results.check("Case 07 Teacher Guide includes comprehensive teach-from-scratch pedagogy", all(term in teacher_text for term in teacher_components), [term for term in teacher_components if term not in teacher_text])
            results.check("Case 07 standards claims directly assess solution comparison while limiting performance-expectation scope", all(term in teacher_text for term in ["Direct components of MS-ETS1-2", "Supporting components: MS-LS1-5 and MS-LS2-4", "Do not claim the packet independently demonstrates the full performance expectation", "fictional biology prevents a full NGSS performance-expectation claim"]))
            results.check("Case 07 Teacher Guide distinguishes established, qualified, fictional, engineering, measurement, and curriculum-model source status", all(term in teacher_text for term in ["Established Earth science", "Qualified / debated Earth interpretation", "Fictional Zhel'ii biology", "Fictional measurements", "Plausible fictional engineering inference", "Curriculum-created models", "Alien evidence cannot serve as empirical proof"]))
            results.check("Case 07 Answer Key completes every field and full exemplar scope", role_task_orders["answer"] == expected_task_numbers and all(term in answer_text for term in ["completed exemplar", "Completed four-channel analysis", "Completed specimen-state analysis", "Completed causal chain", "Completed competing-diagnosis analysis", "Recommendation and evidence — completed exemplar", "CLAIM", "EVIDENCE", "REASONING", "Case comparison and systems reasoning — completed exemplar", "Independent exit response — completed exemplar"]))
            results.check("Case 07 printable content avoids release claims and Campaign 2 production assertions", not re.search(r"APPROVED_STABLE|READY_TO_MERGE|Campaign 1 (?:is )?complete|Campaign 2 curriculum", content, re.I))

    runtime = (APP / "editor-app.js").read_text(encoding="utf-8")
    portable = (APP / "portable-runtime.js").read_text(encoding="utf-8")
    protected_styles_path = ROOT / "shared/implementation/editor-shell/v1.0/protected-printable-components.css"
    accessible_styles_path = ROOT / "shared/implementation/editor-shell/v1.0/accessible-edition.css"
    results.check("central editor loads registry and package schema v2", "case-registry.v2.json" in runtime and "SUPPORTED_PACKAGE_SCHEMA = 2" in runtime)
    scope_module_path = APP / "library-scope.js"
    scope_module = scope_module_path.read_text(encoding="utf-8") if scope_module_path.is_file() else ""
    results.check("central editor derives the Case selector from the selected curriculum and campaign rather than a flat case list", scope_module_path.is_file() and "library-scope.js" in runtime and "casesForCampaign(compatibleCases, curriculumId, campaignId)" in runtime and "renderLibraryOptions(selection.curriculum.id, selection.campaign.id)" in runtime)
    results.check("central editor binds the Curriculum and Campaign selectors to scope changes", all(token in runtime for token in ['elements.curriculum.addEventListener("change"', 'elements.campaign.addEventListener("change"', "selectLibraryScope("]))
    results.check("campaign scoping rules read the canonical registry and invent no placeholder cases", all(token in scope_module for token in ["caseEntry.editorPackage", "item.campaign.id === campaignId", "item.curriculum.id === curriculumId"]) and "placeholder" not in scope_module.lower())
    results.check("central editor applies shared protected and Accessible styles after case presentation", protected_styles_path.is_file() and accessible_styles_path.is_file() and "protected-printable-components.css" in runtime and "accessible-edition.css" in runtime and "[...sharedStyles, presentationCss, protectedComponentStyles, accessibleEditionStyles]" in runtime)
    results.check("central and portable exports never remap grayscale to an output role", 'outputRole: state.role' in runtime and 'outputRole: state.role' in portable and "GRAYSCALE_MISSION" not in runtime + portable)
    results.check("central and portable runtimes preserve grayscale as Boolean presentation state", "state.grayscale" in runtime and "state.grayscale" in portable and 'classList.toggle("grayscale", state.grayscale)' in runtime and 'classList.toggle("grayscale", state.grayscale)' in portable)
    results.check("central and portable runtimes enforce canonical Continued subtitles on every secondary-page banner", "CONTINUATION_ROLE_LABELS" in runtime and "normalizeContinuationLabels(packageMain)" in runtime and "continuationRoleLabels" in portable and all(label in runtime and label in portable for label in ["Student Mission · Continued", "Teacher Guide · Continued", "Answer Key · Continued", "Accessible Mission · Continued"]))
    results.check("isolated print paths exclude chrome and page shadow", all(token in runtime and token in portable for token in ["preparePrintFrame", "print-document", "box-shadow:none!important"]))
    resize_runtime = (APP / "vertical-resize.js").read_text(encoding="utf-8")
    results.check("vertical resizing is restricted to explicit Student/Accessible eligibility metadata", all(token in runtime + resize_runtime for token in ["layoutOverrides", 'activeEdition = "accessible"', "rootManifest.student", "page.dataset.role !== edition"]))
    results.check("CER receives independent UI-level resize protection", "const cerSelector" in resize_runtime and "node.closest(cerSelector)" in resize_runtime)
    results.check("ordinary exports omit authoring controls and unapproved draft heights", "sanitizeClone" in runtime + resize_runtime and "data-layout-resize-ui" in resize_runtime)
    results.check("layout authoring exposes explicit browser-draft and written-source permanence states", all(token in resize_runtime for token in ["Browser draft", "Written to source", "Git commit and push are still required"]))
    results.check("pending changes and page-fit warnings provide editor-only jump navigation", "jumpToArea" in resize_runtime and "jumpToFirstOverflow" in runtime and "layout-jump-highlight" in runtime + resize_runtime)
    results.check("view recovery remembers layout panels without persisting Edit Text", all(token in runtime + resize_runtime for token in ["layoutPanelExpanded", "panelExpandedByEdition", "editMode: false", "preserveEditMode"]))
    editor_styles = (APP / "editor-app.css").read_text(encoding="utf-8")
    results.check("the worksheet loading placeholder is painted by a delayed visual state, never by aria-busy", '#worksheetHost[data-show-loading="true"]::before' in editor_styles and '#worksheetHost[aria-busy="true"]::before' not in editor_styles)
    results.check("worksheet loading announces immediately and defers the visual placeholder behind one cancellable timer", all(token in runtime for token in ["LOADING_PLACEHOLDER_DELAY_MS", "function beginWorksheetLoading", "function endWorksheetLoading", "window.clearTimeout(loadingPlaceholderTimer)", 'dataset.showLoading = "true"']))

    structure = subprocess.run([sys.executable, str(ROOT / "shared/validation/validate_canonical_case_structure.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("canonical case-structure validator passes", structure.returncode == 0, (structure.stdout + structure.stderr).strip())
    release_integrity = subprocess.run([sys.executable, str(ROOT / "shared/validation/validate_release_integrity.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("every approved release certifies source its pinned commit actually contains", release_integrity.returncode == 0, (release_integrity.stdout + release_integrity.stderr).strip())
    layout_validation = subprocess.run([sys.executable, str(ROOT / "shared/validation/validate_layout_overrides.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("Student/Accessible layout eligibility and sparse overrides validate", layout_validation.returncode == 0, (layout_validation.stdout + layout_validation.stderr).strip())
    hhh_activation = subprocess.run([sys.executable, str(ROOT / "shared/validation/validate_hhh_activation.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("HHH activation topology, lifecycle, and remediation-tracker contracts validate", hhh_activation.returncode == 0, (hhh_activation.stdout + hhh_activation.stderr).strip()[-2000:])
    case06_campaign2 = subprocess.run([sys.executable, str(APP / "tests/validate_case06_campaign2.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("SSS Campaign 2 Case 06 case-scoped validation passes", case06_campaign2.returncode == 0, (case06_campaign2.stdout + case06_campaign2.stderr).strip()[-2000:])
    hhh_case04 = subprocess.run([sys.executable, str(APP / "tests/validate_hhh_case04_karlsruhe.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("HHH Campaign 1 Case 04 case-scoped temperature, catalyst, attribution, recycle, source-status and parity checks pass", hhh_case04.returncode == 0, (hhh_case04.stdout + hhh_case04.stderr).strip()[-2000:])
    hhh_case05 = subprocess.run([sys.executable, str(APP / "tests/validate_hhh_case05_dust_bowl.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("HHH Campaign 1 Case 05 case-scoped subsoil, drought, land-use, policy, source-status and parity checks pass", hhh_case05.returncode == 0, (hhh_case05.stdout + hhh_case05.stderr).strip()[-2000:])
    hhh_case06 = subprocess.run([sys.executable, str(APP / "tests/validate_hhh_case06_vertical_farm.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("HHH Campaign 1 Case 06 case-scoped two-layer truth, science-qualification, accountability, source-status and parity checks pass", hhh_case06.returncode == 0, (hhh_case06.stdout + hhh_case06.stderr).strip()[-2000:])
    hhh_case07 = subprocess.run([sys.executable, str(APP / "tests/validate_hhh_case07_the_audit.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("HHH Campaign 2 Case 07 case-scoped authenticity, provenance, evidence-weighting, source-status and parity checks pass", hhh_case07.returncode == 0, (hhh_case07.stdout + hhh_case07.stderr).strip()[-2000:])
    hhh_case08 = subprocess.run([sys.executable, str(APP / "tests/validate_hhh_case08_floating_gardens.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("HHH Campaign 2 Case 08 case-scoped terminology, engineered-system, sourced-map, evidence-layer, source-status and parity checks pass", hhh_case08.returncode == 0, (hhh_case08.stdout + hhh_case08.stderr).strip()[-2000:])
    case05_campaign2 = subprocess.run([sys.executable, str(APP / "tests/validate_case05_campaign2.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("SSS Campaign 2 Case 05 case-scoped source, clue, figure, dose-precision, and prohibited-claim checks pass", case05_campaign2.returncode == 0, (case05_campaign2.stdout + case05_campaign2.stderr).strip()[-2000:])
    case04_campaign2 = subprocess.run([sys.executable, str(APP / "tests/validate_case04_campaign2.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("SSS Campaign 2 Case 04 case-scoped source, clue, figure, and prohibited-claim checks pass", case04_campaign2.returncode == 0, (case04_campaign2.stdout + case04_campaign2.stderr).strip()[-2000:])
    case03_campaign2 = subprocess.run([sys.executable, str(APP / "tests/validate_case03_campaign2.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("SSS Campaign 2 Case 03 case-scoped source, clue, figure, and prohibited-claim checks pass", case03_campaign2.returncode == 0, (case03_campaign2.stdout + case03_campaign2.stderr).strip()[-2000:])
    case02_campaign2 = subprocess.run([sys.executable, str(APP / "tests/validate_case02_campaign2.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("SSS Campaign 2 Case 02 case-scoped source, clue, figure, and prohibited-claim checks pass", case02_campaign2.returncode == 0, (case02_campaign2.stdout + case02_campaign2.stderr).strip()[-2000:])
    case01_campaign2 = subprocess.run([sys.executable, str(APP / "tests/validate_case01_campaign2.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("SSS Campaign 2 Case 01 case-scoped source, clue, figure, and prohibited-claim checks pass", case01_campaign2.returncode == 0, (case01_campaign2.stdout + case01_campaign2.stderr).strip()[-2000:])
    if args.skip_mutation_tests:
        # Proportional-validation escape: the six SSS mutation checks intentionally
        # rewrite frozen case sources to prove each protection fires, cost hours, and
        # are relevant only when the protections themselves change. They are reported
        # as skipped, never silently absent.
        pass
    else:
        case01_mutations = subprocess.run([sys.executable, str(APP / "tests/test_case01_mutations.py")], cwd=ROOT, text=True, capture_output=True)
        results.check("SSS Campaign 2 Case 01 mutation tests prove each protection fires", case01_mutations.returncode == 0, (case01_mutations.stdout + case01_mutations.stderr).strip()[-2000:])
        case02_mutations = subprocess.run([sys.executable, str(APP / "tests/test_case02_mutations.py")], cwd=ROOT, text=True, capture_output=True)
        results.check("SSS Campaign 2 Case 02 mutation tests prove each protection fires", case02_mutations.returncode == 0, (case02_mutations.stdout + case02_mutations.stderr).strip()[-2000:])
        case04_mutations = subprocess.run([sys.executable, str(APP / "tests/test_case04_mutations.py")], cwd=ROOT, text=True, capture_output=True)
        results.check("SSS Campaign 2 Case 04 mutation tests prove each protection fires", case04_mutations.returncode == 0, (case04_mutations.stdout + case04_mutations.stderr).strip()[-2000:])
        case05_mutations = subprocess.run([sys.executable, str(APP / "tests/test_case05_mutations.py")], cwd=ROOT, text=True, capture_output=True)
        results.check("SSS Campaign 2 Case 05 mutation tests prove each protection fires", case05_mutations.returncode == 0, (case05_mutations.stdout + case05_mutations.stderr).strip()[-2000:])
        case03_mutations = subprocess.run([sys.executable, str(APP / "tests/test_case03_mutations.py")], cwd=ROOT, text=True, capture_output=True)
        results.check("SSS Campaign 2 Case 03 mutation tests prove each protection fires", case03_mutations.returncode == 0, (case03_mutations.stdout + case03_mutations.stderr).strip()[-2000:])
        case06_mutations = subprocess.run([sys.executable, str(APP / "tests/test_case06_mutations.py")], cwd=ROOT, text=True, capture_output=True)
        results.check("SSS Campaign 2 Case 06 mutation tests prove each protection fires", case06_mutations.returncode == 0, (case06_mutations.stdout + case06_mutations.stderr).strip()[-2000:])
    corrective_lifecycle = subprocess.run([sys.executable, str(APP / "tests/test_corrective_release_lifecycle.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("corrective-release lifecycle tests pass", corrective_lifecycle.returncode == 0, (corrective_lifecycle.stdout + corrective_lifecycle.stderr).strip()[-2000:])
    service_tests = subprocess.run([sys.executable, str(APP / "tests/test_authoring_service.py")], cwd=ROOT, text=True, capture_output=True)
    results.check("source-persistence security and round-trip tests pass", service_tests.returncode == 0, (service_tests.stdout + service_tests.stderr).strip())
    tracked_candidates = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True, capture_output=True, check=True).stdout.splitlines()
    tracked_png = [path for path in tracked_candidates if (ROOT / path).is_file() and path.endswith(".png") and (path.startswith("apps/curriculum-editor/tests/screenshots/") or "/validation-artifacts/" in path)]
    results.check("no routine generated screenshots remain tracked", not tracked_png, tracked_png)

    payload = {
        "validator": "curriculum-editor-static-v2",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "mutationChecks": (
            "NOT RUN — six SSS mutation checks intentionally skipped under the proportional Phase 3 plan (--skip-mutation-tests)"
            if args.skip_mutation_tests else "RUN"
        ),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
