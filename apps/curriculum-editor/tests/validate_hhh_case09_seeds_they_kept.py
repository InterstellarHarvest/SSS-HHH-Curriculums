#!/usr/bin/env python3
"""Case-scoped protections for HHH Campaign 2 Core Case 09 — The Seeds They Kept.

These assertions guard the boundaries this case exists to get right, plus the
cross-edition parity the shared operational walk does not reach into. They are
driven by the contract blocks the task registry declares — ``sourceStatusContract``,
``runtimeDependency``, ``historicalQualification``, ``chronologyBoundary``,
``continuityChain``, ``claimTest``, ``sourceCertification``, ``cerDecision``,
``noGameRoute``, ``editionResponseContract``, ``accessibleAdaptations``,
``semanticInvariants`` and ``figureContract`` — rather than by literal paragraph
locks, so ordinary rewording stays possible while the meaning stays protected.

The audit dependencies this case carries:

* ``HHH-IMP-C2L2-001`` — ``GAME_REMEDIATION_BLOCKS_FINALIZATION``, and
  ``RESOLVED_VERIFIED`` at the current game baseline in the shared tracker. The
  package pins that resolution and the six-clue semantics it produced, and
  changes nothing in the tracker.
* ``HHH-GAME-C2L2-001`` — ``CURRICULUM_QUALIFICATION_REQUIRED``, and open at the
  audited game baseline by design. The curriculum carries the qualification the
  audit asked for — qualified death counts, Vavilov kept apart from the siege
  staff — and the guards below are what keep that true.

DESIGN NOTE — the shape of the semantic guard, and its limits.

This case has five high-risk misconceptions, and each gets one CLOSED class:

  * ``vavilovPresentAtSiege`` — Vavilov at, guarding or witnessing the Institute
    during the siege;
  * ``nothingMovedAsHistory`` — the real collection stated to have never left
    the room, building or city;
  * ``zeroLossAsHistory`` — the real collection stated to have survived with no
    loss at all;
  * ``cleanProvesForged`` — a clean document declared forged because it is clean;
  * ``settledDeathCount`` — a specific staff-death number stated as settled fact
    with no qualifier in the same proposition.

Every class is CLOSED: a small finite negative vocabulary, anchored to a named
subject register, requiring an affirmative and unnegated predicate. None
enumerates synonyms for an open concept, and none polices an ordinary verb. The
two historical-claim classes are excused inside a reconstructed evidence object
and inside a marked in-game quotation, because the game's scan and report have to
be printed in order to be tested, and a quotation is not an assertion.

**This guard makes no claim of semantic completeness.** It is a defence against
five known misconceptions, not a proof that every possible bad paraphrase has
been detected. An unseen paraphrase can pass it. Ordinary cross-role parity,
source-status and manual review remain required, and the positive structural
requirements below — checked against markup rather than prose — are what carry
the audit obligation.

Every semantic guard ships with NEGATIVE CONTROLS it must flag and POSITIVE
CONTROLS it must not, and the package itself is the standing positive control.

Usage:
    python3 apps/curriculum-editor/tests/validate_hhh_case09_seeds_they_kept.py
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "hhh/campaign-2/case-09-seeds-they-kept"
SOURCE = UNIT / "source"
REGISTRY_FILE = ROOT / "shared/implementation/case-registry.v2.json"
TRACKER_FILE = ROOT / "hhh/production/data/HHH_GAME_REMEDIATION_DEPENDENCY_TRACKER_v1.0.json"
CASE_ID = "HHH-C2-CASE09"
LEARNER_ROLES = ("student", "accessible")
ALL_ROLES = ("student", "teacher", "answer", "accessible")
GAME_COMMIT = "d9fc16baf272cb543c29cbd0c06ec85efad60be8"
AUDITED_GAME_COMMIT = "9b8545ed6ecf98b337326390400076e36789e056"
OWNER = "Nate / Owner"
HISTORY = UNIT / "history"
RELEASE_RECORD = HISTORY / "release-v0.1.json"
OWNER_APPROVAL_RECORD = HISTORY / "CASE09_OWNER_APPROVAL_v0.1.md"
RELEASE_RECORD_PATH = "hhh/campaign-2/case-09-seeds-they-kept/history/release-v0.1.json"
APPROVAL_DATE = "2026-08-21"
# The exact byte set the owner reviewed on screen and printed. It is NOT the
# certified-source commit: the released task-registry.js bytes are created by release
# conversion, so the release pins name the release-conversion commit. Conflating the
# two is the error these checks exist to prevent.
OWNER_PRINTABLE_BASELINE = "0202027acca362bc4b2ed4f3cee81dcdb564ee2b"
# Two separate owner statements, one per gate. They are recorded and checked
# separately, and a combined or polished quotation is a defect, not a tidy-up.
OWNER_VISUAL_STATEMENT = "approved good and stable"
OWNER_PRINT_STATEMENT = "physical print approved"
# The printable sources the owner approved. Release conversion may not move a byte of
# them; only task-registry.js is restamped, and only in its lifecycle leaves.
FROZEN_PRINTABLE_SOURCES = {
    "content.html": "2904f736c83993daf0585d5bdeed2d630a91e7847c6d43cff81fe3e5c26722cb",
    "presentation.css": "e7d180b152c654e22866dd56a39caff20c7ebc4435eac4b0a4a8a1c9e42c5b4e",
    "layout-overrides.json": "590500580cd97aa47b33994f35242884b713772d803ccecc4345d1d68fd9b60f",
}
# The only two task-registry leaves release conversion is permitted to move.
RELEASE_LIFECYCLE_LEAVES = {"status": ("DRAFT", "APPROVED_STABLE"),
                            "ownerReviewStatus": ("OWNER_REVIEW_NOT_STARTED", "OWNER_REVIEW_PASS")}
PENDING_TOKEN_PATTERN = re.compile(r"COMMIT_[A-Z]_PENDING|PENDING|TBD|XXX|PLACEHOLDER")
COMMIT_PATTERN = re.compile(r"^[a-f0-9]{40}$")
RESOLVED_COMMIT_FIELDS = ("originalReleaseApprovalCommit",
                          "canonicalSourceApprovalCommit",
                          "formerArtifactRecoveryCommit")
SOURCE_FILES = (("content", "content.html"), ("presentation", "presentation.css"),
                ("taskRegistry", "task-registry.js"),
                ("layoutOverrides", "layout-overrides.json"))
EXPECTED_PAGES = {"student": 8, "teacher": 7, "answer": 4, "accessible": 10}
EXPECTED_TASKS = [
    ("1", "Build the Case Vocabulary"),
    ("2", "Set a Continuity Test"),
    ("3", "Separate Vavilov's Timeline from the Siege"),
    ("4", "Trace the Collection Through Crisis"),
    ("5", "Compare What the Sources Can Establish"),
    ("6", "Test the Consumption Report"),
    ("7", "Make a Collection Continuity Judgment"),
    ("8", "Transfer the Method"),
]
EXPECTED_VOCABULARY = ["accession", "collection continuity", "ex situ conservation", "germplasm",
                       "provenance", "seed bank", "siege"]
RECONSTRUCTED_SOURCES = ["besieged-street", "keeper-testimony", "preservation-scan",
                         "accession-ledger", "vavilov-record", "consumption-report"]
DOCUMENTED_SOURCES = ["crop-trust-vavilov", "loskutov-wartime", "vir-institute"]
REQUIRED_STRANDS = {"siege-context", "keeper-testimony", "collection-condition",
                    "accession-continuity", "vavilov-fate", "consumption-report"}
# The six runtime clue tags the resolved remediation produced. They are asserted
# against the tracker's resolution evidence, which is the repository's authoritative
# record of the inspected game commit; they are never printed.
RESOLVED_CLUE_TAGS = ("siege_witnessed", "keeper_testimony", "collection_intact",
                      "accessions_continuous", "vavilov_fate", "report_read")
LOSKUTOV_DOI = "10.30901/2227-8834-2021-2-151-162"

PROPOSITION_SPLIT = re.compile(r"(?<=[.!?])\s+")
DECIMAL_GUARD = re.compile(r"(\d)\.(\d)")
PARAGRAPH_TAGS = ("p", "li", "td", "th", "dd", "figcaption", "caption")


class Results:
    def __init__(self) -> None:
        self.assertions: list[dict] = []
        self.passed = 0

    def check(self, name: str, ok: bool, detail: object = "") -> bool:
        self.assertions.append({"name": name, "status": "PASS" if ok else "FAIL",
                                **({"detail": str(detail)[:1400]} if not ok and detail != "" else {})})
        if ok:
            self.passed += 1
        return ok


def normalise(text: str) -> str:
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2014", " - ").replace("\u2013", "-").replace("\u00a0", " ")
    text = text.replace("\u2212", "-").replace("\u00b7", " ")
    return re.sub(r"\s+", " ", text).strip()


def propositions(text: str) -> list[str]:
    guarded = DECIMAL_GUARD.sub("\\1\u0001\\2", normalise(text))
    parts = [p.replace("\u0001", ".").strip() for p in PROPOSITION_SPLIT.split(guarded)]
    return [p for p in parts if p]


def registry_object(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    body = raw.split("=", 1)[1].strip()
    if body.endswith(";"):
        body = body[:-1]
    return json.loads(body)


def load() -> tuple[dict, dict, dict, BeautifulSoup]:
    package = json.loads((SOURCE / "case-package.json").read_text(encoding="utf-8"))
    registry = registry_object(SOURCE / "task-registry.js")
    layout = json.loads((SOURCE / "layout-overrides.json").read_text(encoding="utf-8"))
    soup = BeautifulSoup((SOURCE / "content.html").read_text(encoding="utf-8"), "html.parser")
    return package, registry, layout, soup


def pages_for(soup: BeautifulSoup, role: str) -> list:
    return soup.select(f'section.page[data-role="{role}"]')


def role_text(soup: BeautifulSoup, role: str) -> str:
    return normalise(" ".join(p.get_text(" ", strip=True) for p in pages_for(soup, role)))


def exempt_ids(node) -> set[str]:
    ids: set[str] = set()
    current = node
    while current is not None and getattr(current, "get", None):
        value = current.get("data-semantic-exemption")
        if value:
            ids.add(value)
        current = current.parent
    return ids


def structural_concepts(node, structural: list[dict]) -> set[str]:
    """Concepts excused at this node by a registered structural selector on an ancestor."""
    allowed: set[str] = set()
    for spec in structural:
        selector = spec["selector"]
        if node.find_parent(attrs=_attr_matcher(selector)) is not None or _matches(node, selector):
            allowed |= set(spec["allowedConcepts"])
    return allowed


def _attr_matcher(selector: str):
    # Selectors in this registry are attribute selectors of the form [name] or [name='value'].
    match = re.fullmatch(r"\[([a-zA-Z0-9-]+)(?:=['\"]([^'\"]*)['\"])?\]", selector)
    if not match:
        raise ValueError(f"unsupported structural selector {selector!r}")
    name, value = match.group(1), match.group(2)
    return {name: (value if value is not None else True)}


def _matches(node, selector: str) -> bool:
    matcher = _attr_matcher(selector)
    name, value = next(iter(matcher.items()))
    if not getattr(node, "get", None):
        return False
    actual = node.get(name)
    return actual is not None and (value is True or actual == value)


def resolvable(node, exemptions: dict, structural: list[dict], role: str) -> set[str]:
    allowed: set[str] = set()
    for eid in exempt_ids(node):
        spec = exemptions.get(eid)
        if spec and role in spec["roles"]:
            allowed |= set(spec["allowedConcepts"])
    allowed |= structural_concepts(node, structural)
    return allowed


def leaf_blocks(page, exemptions: dict, structural: list[dict], role: str) -> list:
    """Paragraph-level containers paired with the concepts excused inside them.

    Exempt-subtree REMOVAL, rather than skipping the exempt node, is what makes a
    registered exemption work on a clause. Only subtrees whose exemption RESOLVES
    for this role are removed; a structurally excused subtree (a reconstructed card,
    a marked in-game quotation) is removed for the two historical classes only by
    being scanned as its own block with its own allowance.
    """
    blocks = []

    def prepared(node):
        allowed = resolvable(node, exemptions, structural, role)
        clone = BeautifulSoup(str(node), "html.parser")
        for exempted in clone.select("[data-semantic-exemption]"):
            spec = exemptions.get(exempted.get("data-semantic-exemption"))
            if spec and role in spec["roles"]:
                exempted.decompose()
        for spec in structural:
            for excused in clone.select(spec["selector"]):
                excused.decompose()
        return allowed, normalise(clone.get_text(" ", strip=True))

    for node in page.find_all(PARAGRAPH_TAGS):
        if node.find(PARAGRAPH_TAGS):
            continue
        allowed, text = prepared(node)
        if text:
            blocks.append((node, text, allowed))
    for node in page.find_all("span"):
        if node.find_parent(PARAGRAPH_TAGS) or node.find("span"):
            continue
        allowed, text = prepared(node)
        if text:
            blocks.append((node, text, allowed))
    for node in page.select(".terminal"):
        allowed, text = prepared(node)
        if text:
            blocks.append((node, text, allowed))
    # Structurally excused subtrees are scanned as their own blocks with their
    # allowance, so that the classes they are NOT excused from still apply inside.
    for spec in structural:
        for node in page.select(spec["selector"]):
            allowed = resolvable(node, exemptions, structural, role)
            text = normalise(node.get_text(" ", strip=True))
            if text:
                blocks.append((node, text, allowed))
    return blocks


def compile_classes(framings: dict) -> dict:
    compiled = {}
    for class_id, spec in framings.items():
        if not isinstance(spec, dict) or "patterns" not in spec:
            continue
        compiled[class_id] = {
            "subjects": [re.compile(p, re.I) for p in spec.get("subjectPatterns", [])],
            "patterns": [re.compile(p, re.I) for p in spec["patterns"]],
            "unless": [re.compile(p, re.I) for p in spec.get("unlessPatterns", [])],
        }
    return compiled


def scan_html(html: str, compiled: dict, exemptions: dict, structural: list[dict], role: str) -> list[tuple]:
    soup = BeautifulSoup(html, "html.parser")
    violations = []
    for page in soup.select(f'section.page[data-role="{role}"]'):
        page_id = page.get("data-page-id")
        for _node, text, allowed in leaf_blocks(page, exemptions, structural, role):
            for sentence in propositions(text):
                for class_id, spec in compiled.items():
                    if class_id in allowed:
                        continue
                    if spec["subjects"] and not any(s.search(sentence) for s in spec["subjects"]):
                        continue
                    if spec["unless"] and any(u.search(sentence) for u in spec["unless"]):
                        continue
                    if any(p.search(sentence) for p in spec["patterns"]):
                        violations.append((role, page_id, class_id, sentence[:220]))
    return violations


def figure_root(node):
    return node if node.name == "figure" else node.find_parent("figure")


def synthetic(role: str, body: str) -> str:
    return (f'<section class="page" data-role="{role}" data-page-id="control-page">'
            f'<div class="content content-area">{body}</div></section>')


def main() -> int:  # noqa: C901 - one flat assertion sequence, deliberately readable
    results = Results()
    package, registry, layout, soup = load()
    html = (SOURCE / "content.html").read_text(encoding="utf-8")
    tasks = registry["tasks"]
    texts = {role: role_text(soup, role) for role in ALL_ROLES}
    teacher_text, answer_text = texts["teacher"], texts["answer"]

    # --- IDENTITY AND CANDIDATE LIFECYCLE -----------------------------------
    results.check("package identity is HHH-C2-CASE09 v0.1 CORE_CASE in campaign-2",
                  (package["id"], package["version"], package["instructionalType"],
                   package["curriculum"], package["campaign"])
                  == (CASE_ID, "0.1", "CORE_CASE", "HHH", "campaign-2"))
    # Release conversion turned the four candidate-state lifecycle assertions below into
    # released-state obligations. Nothing was deleted: every gate the candidate checked
    # in one direction is still checked, in the other.
    results.check("the package and task registry both carry the released lifecycle",
                  package["status"] == "APPROVED_STABLE" and registry["status"] == "APPROVED_STABLE"
                  and registry["ownerReviewStatus"] == "OWNER_REVIEW_PASS"
                  and registry["version"] == "0.1"
                  and package["approval"]["status"] == "APPROVED"
                  and package["approval"]["printStatus"] == "PASS"
                  and package["approval"]["owner"] == OWNER
                  and package["approval"]["date"] == APPROVAL_DATE,
                  json.dumps({"package": package["status"], "registry": registry["status"],
                              "approval": package["approval"]}))
    results.check("the package points at the release record",
                  package.get("releaseHistory") == RELEASE_RECORD_PATH,
                  package.get("releaseHistory"))
    results.check("the owner approval record and the release record both exist",
                  OWNER_APPROVAL_RECORD.is_file() and RELEASE_RECORD.is_file(),
                  sorted(x.name for x in HISTORY.iterdir()) if HISTORY.is_dir() else "no history/")
    results.check("the unit directory holds only README.md, source/ and history/",
                  sorted(p.name for p in UNIT.iterdir() if p.name != ".DS_Store")
                  == ["README.md", "history", "source"],
                  sorted(p.name for p in UNIT.iterdir()))
    results.check("history/ holds only the owner approval record and the release record",
                  sorted(p.name for p in HISTORY.iterdir() if p.name != ".DS_Store")
                  == ["CASE09_OWNER_APPROVAL_v0.1.md", "release-v0.1.json"],
                  sorted(p.name for p in HISTORY.iterdir()))
    results.check("the release added no generated artifact, published role HTML or PDF",
                  not [q for q in UNIT.rglob("*")
                       if q.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".svg", ".docx"}
                       or (q.suffix.lower() == ".html" and q.name != "content.html")],
                  [str(q.relative_to(UNIT)) for q in UNIT.rglob("*")
                   if q.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".svg", ".docx"}
                   or (q.suffix.lower() == ".html" and q.name != "content.html")])
    results.check("the source directory holds exactly the four canonical sources plus the package",
                  sorted(p.name for p in SOURCE.iterdir() if p.name != ".DS_Store")
                  == ["case-package.json", "content.html", "layout-overrides.json", "presentation.css",
                      "task-registry.js"],
                  sorted(p.name for p in SOURCE.iterdir()))
    results.check("task registry pins the current game baseline, the audit baseline and the Blueprint",
                  registry["gameCommit"] == GAME_COMMIT
                  and registry["auditBaseline"] == "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md"
                  and registry["blueprint"] == "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
                  registry["gameCommit"])
    results.check("the registry names the runtime source this case is drawn from",
                  registry["runtimeId"] == "C2L2", registry.get("runtimeId"))
    results.check("the registry carries the locked learning goal and guiding question",
                  registry["learningGoal"].startswith("Explain why preserving crop genetic diversity during the Siege of Leningrad mattered")
                  and "collection continuity, and corroboration" in registry["learningGoal"]
                  and registry["guidingQuestion"].startswith("How can historians tell whether a collection survived a crisis"))
    results.check("the registry states the conceptual distinction the case teaches",
                  "does not require physical immobility or perfect survival" in registry["conceptualDistinction"])
    for key, filename in (("content", "content.html"), ("presentation", "presentation.css"),
                          ("taskRegistry", "task-registry.js"),
                          ("layoutOverrides", "layout-overrides.json")):
        digest = hashlib.sha256((SOURCE / filename).read_bytes()).hexdigest()
        results.check(f"package sourceHashes.{key} matches the working tree",
                      package["sourceHashes"][key] == digest, digest)

    shared = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    entry = next(c for cur in shared["curricula"] if cur["id"] == "HHH"
                 for camp in cur["campaigns"] for c in camp["cases"] if c["id"] == CASE_ID)
    results.check("the shared registry entry carries the released lifecycle and its history pointer",
                  entry["status"] == "APPROVED_STABLE" and entry["packageStatus"] == "APPROVED"
                  and entry["displayOrder"] == 11 and entry["displayLabel"] == "9 - The Seeds They Kept"
                  and entry["title"] == "The Seeds They Kept"
                  and entry["instructionalType"] == "CORE_CASE" and entry["version"] == "0.1"
                  and entry["editorPackage"] == "hhh/campaign-2/case-09-seeds-they-kept/source/case-package.json"
                  and entry["historyRecord"] == RELEASE_RECORD_PATH
                  and entry["approval"] == {"date": APPROVAL_DATE, "owner": OWNER,
                                            "status": "APPROVED", "printStatus": "PASS"},
                  json.dumps(entry))
    results.check("the shared registry and the package name the same release record",
                  entry["historyRecord"] == package.get("releaseHistory") == RELEASE_RECORD_PATH,
                  json.dumps({"registry": entry.get("historyRecord"),
                              "package": package.get("releaseHistory")}))
    all_hhh = [c["id"] for cur in shared["curricula"] if cur["id"] == "HHH"
               for camp in cur["campaigns"] for c in camp["cases"]]
    results.check("exactly one HHH-C2-CASE09 identity exists in the shared registry",
                  all_hhh.count(CASE_ID) == 1, all_hhh)
    results.check("Case 10 and later units remain planned reservations",
                  all("editorPackage" not in c for cur in shared["curricula"] if cur["id"] == "HHH"
                      for camp in cur["campaigns"] for c in camp["cases"]
                      if c["displayOrder"] > 11))
    results.check("the registry display label and the package identity agree",
                  registry["displayLabel"] == entry["displayLabel"]
                  and registry["title"] == package["title"] == entry["title"])

    # --- THE RELEASE RECORD --------------------------------------------------
    # The release record is only trustworthy if it agrees with the package it describes,
    # resolves every commit pin to a real SHA, and can be shown to describe a tree that
    # actually carries the bytes it claims.
    release = json.loads(RELEASE_RECORD.read_text(encoding="utf-8"))
    results.check("release record identity, version, owner and date match the package",
                  (release["schemaVersion"], release["caseId"], release["curriculumVersion"],
                   release["status"], release["approvalDate"], release["owner"])
                  == (1, CASE_ID, package["version"], "APPROVED_STABLE",
                      package["approval"]["date"], package["approval"]["owner"]),
                  json.dumps({k: release.get(k) for k in
                              ("schemaVersion", "caseId", "curriculumVersion",
                               "status", "approvalDate", "owner")}))
    results.check("the release record, the package and the shared registry agree on owner and date",
                  release["owner"] == package["approval"]["owner"] == entry["approval"]["owner"] == OWNER
                  and release["approvalDate"] == package["approval"]["date"]
                  == entry["approval"]["date"] == APPROVAL_DATE,
                  json.dumps({"record": [release["owner"], release["approvalDate"]],
                              "package": package["approval"], "registry": entry["approval"]}))
    results.check("release record source hashes match the certified source hashes",
                  release["sourceHashes"] == package["sourceHashes"],
                  json.dumps({"release": release["sourceHashes"],
                              "package": package["sourceHashes"]}))
    results.check("release record page counts match the package role structure",
                  release["rolePageCounts"]
                  == {role: package["rolePageStructure"][role]["pageCount"] for role in ALL_ROLES},
                  json.dumps(release["rolePageCounts"]))
    results.check("release record page counts match the declared 8/7/4/10 and the task registry",
                  release["rolePageCounts"] == EXPECTED_PAGES == registry["roles"],
                  json.dumps({"record": release["rolePageCounts"], "registry": registry["roles"]}))
    for field in RESOLVED_COMMIT_FIELDS:
        results.check(f"release record {field} is a resolved 40-character commit",
                      bool(COMMIT_PATTERN.fullmatch(str(release.get(field, "")))),
                      release.get(field))
    results.check("no pending or placeholder token survives anywhere in the release record",
                  not PENDING_TOKEN_PATTERN.search(RELEASE_RECORD.read_text(encoding="utf-8")),
                  sorted(set(PENDING_TOKEN_PATTERN.findall(
                      RELEASE_RECORD.read_text(encoding="utf-8")))))
    results.check("no pending or placeholder token survives in the owner approval record",
                  not PENDING_TOKEN_PATTERN.search(OWNER_APPROVAL_RECORD.read_text(encoding="utf-8")),
                  sorted(set(PENDING_TOKEN_PATTERN.findall(
                      OWNER_APPROVAL_RECORD.read_text(encoding="utf-8")))))
    results.check("the release record carries measured validation rather than the provisional stub",
                  release["acceptedValidation"].get("status") == "PASS"
                  and "caseScopedValidator" in release["acceptedValidation"],
                  release["acceptedValidation"].get("status"))
    # The certified-source commit must actually carry the four hashes the record claims.
    # Checking the record against itself would prove nothing.
    certified = release["canonicalSourceApprovalCommit"]
    blobs = {}
    for key, filename in SOURCE_FILES:
        try:
            blobs[key] = hashlib.sha256(subprocess.run(
                ["git", "show", f"{certified}:hhh/campaign-2/case-09-seeds-they-kept/source/{filename}"],
                cwd=ROOT, check=True, capture_output=True).stdout).hexdigest()
        except (subprocess.CalledProcessError, FileNotFoundError):
            blobs[key] = None
    results.check("the certified-source commit really carries the released source bytes",
                  blobs == release["sourceHashes"], json.dumps(blobs))
    results.check("the working tree still carries the released source bytes",
                  {key: hashlib.sha256((SOURCE / filename).read_bytes()).hexdigest()
                   for key, filename in SOURCE_FILES} == release["sourceHashes"])
    # The printable baseline is a separate fact and must never be overwritten by the
    # certified-source commit, nor silently equated with it.
    approval_text = OWNER_APPROVAL_RECORD.read_text(encoding="utf-8")
    results.check("the owner approval record names the owner-approved printable baseline",
                  OWNER_PRINTABLE_BASELINE in approval_text)
    results.check("the release record preserves the printable baseline separately from the certified commit",
                  OWNER_PRINTABLE_BASELINE in json.dumps(release)
                  and certified != OWNER_PRINTABLE_BASELINE,
                  json.dumps({"printableBaseline": OWNER_PRINTABLE_BASELINE,
                              "certifiedSourceCommit": certified}))
    results.check("the README preserves the printable baseline separately from the certified commit",
                  OWNER_PRINTABLE_BASELINE in (UNIT / "README.md").read_text(encoding="utf-8"))
    # --- PRINTABLE PARITY AGAINST THE OWNER BASELINE -------------------------
    # Release conversion is only legitimate if it moved no printable byte. This is
    # proven against the owner-approved commit itself, not against the record's claim.
    baseline_blobs = {}
    for filename in FROZEN_PRINTABLE_SOURCES:
        try:
            baseline_blobs[filename] = hashlib.sha256(subprocess.run(
                ["git", "show",
                 f"{OWNER_PRINTABLE_BASELINE}:hhh/campaign-2/case-09-seeds-they-kept/source/{filename}"],
                cwd=ROOT, check=True, capture_output=True).stdout).hexdigest()
        except (subprocess.CalledProcessError, FileNotFoundError):
            baseline_blobs[filename] = None
    for filename, expected in FROZEN_PRINTABLE_SOURCES.items():
        live = hashlib.sha256((SOURCE / filename).read_bytes()).hexdigest()
        results.check(f"{filename} is byte-identical to the owner-approved printable baseline",
                      live == expected == baseline_blobs[filename],
                      json.dumps({"baseline": baseline_blobs[filename], "released": live}))
    # task-registry.js is the one source release conversion may restamp, and only in the
    # two lifecycle leaves. Whole-object comparison, so a quiet instructional edit hidden
    # behind an identical hash count cannot pass.
    try:
        baseline_registry = json.loads(re.sub(
            r"^\s*window\.[A-Z0-9_]+\s*=\s*", "",
            subprocess.run(["git", "show",
                            f"{OWNER_PRINTABLE_BASELINE}:hhh/campaign-2/case-09-seeds-they-kept/source/task-registry.js"],
                           cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8")
        ).rstrip().removesuffix(";"))
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError):
        baseline_registry = None

    def _leaves(node, prefix=""):
        found = {}
        if isinstance(node, dict):
            for key, value in node.items():
                found.update(_leaves(value, f"{prefix}.{key}" if prefix else key))
        elif isinstance(node, list):
            for index, value in enumerate(node):
                found.update(_leaves(value, f"{prefix}[{index}]"))
        else:
            found[prefix] = node
        return found

    baseline_leaves = _leaves(baseline_registry) if baseline_registry is not None else {}
    released_leaves = _leaves(registry)
    results.check("the task registry key set is unchanged from the owner-approved baseline",
                  bool(baseline_leaves) and set(baseline_leaves) == set(released_leaves),
                  json.dumps({"onlyBaseline": sorted(set(baseline_leaves) - set(released_leaves))[:20],
                              "onlyReleased": sorted(set(released_leaves) - set(baseline_leaves))[:20]}))
    moved = {k: (baseline_leaves.get(k), released_leaves.get(k))
             for k in released_leaves if baseline_leaves.get(k) != released_leaves.get(k)}
    results.check("only the two non-rendering lifecycle leaves moved in the task registry",
                  moved == {k: v for k, v in RELEASE_LIFECYCLE_LEAVES.items()},
                  json.dumps(moved))
    results.check("no instructional, historical, certification or rendering task-registry leaf moved",
                  all(k in RELEASE_LIFECYCLE_LEAVES for k in moved), sorted(moved))
    # The lifecycle leaves are non-rendering by construction: neither string may appear on
    # any printable page, which the lifecycle-token guard below also enforces per role.
    for leaf, (_, released_value) in RELEASE_LIFECYCLE_LEAVES.items():
        results.check(f"the {leaf} lifecycle value renders on no printable page",
                      not any(released_value.lower() in texts[role].lower() for role in ALL_ROLES),
                      released_value)
    # --- THE OWNER GATES, RECORDED EXACTLY AND SEPARATELY --------------------
    # The owner gave two statements, one per gate. Merging them into one polished
    # quotation would be a fabrication, so each is required to survive verbatim and the
    # records are checked for the separation as well as for the words.
    for label, text in (("owner approval record", approval_text),
                        ("release record", json.dumps(release))):
        results.check(f"the {label} preserves the exact on-screen owner statement",
                      OWNER_VISUAL_STATEMENT in text, OWNER_VISUAL_STATEMENT)
        results.check(f"the {label} preserves the exact physical-print owner statement",
                      OWNER_PRINT_STATEMENT in text, OWNER_PRINT_STATEMENT)
    results.check("the owner approval record keeps the two statements as separate quotations",
                  approval_text.count(f"> {OWNER_VISUAL_STATEMENT}") == 1
                  and approval_text.count(f"> {OWNER_PRINT_STATEMENT}") == 1
                  and f"{OWNER_VISUAL_STATEMENT} and {OWNER_PRINT_STATEMENT}" not in approval_text
                  and f"{OWNER_VISUAL_STATEMENT}, {OWNER_PRINT_STATEMENT}" not in approval_text)
    results.check("the README records both owner gates with both exact statements",
                  OWNER_VISUAL_STATEMENT in (UNIT / "README.md").read_text(encoding="utf-8")
                  and OWNER_PRINT_STATEMENT in (UNIT / "README.md").read_text(encoding="utf-8"))
    results.check("the owner approval record states both owner gates and the approval date",
                  APPROVAL_DATE in approval_text and OWNER in approval_text
                  and "**PASS**" in approval_text,
                  APPROVAL_DATE)
    results.check("the release record records the post-owner independent disposition exactly",
                  "INDEPENDENT_CASE09_POST_OWNER_PASS" in json.dumps(release)
                  and "INDEPENDENT_CASE09_POST_OWNER_PASS" in approval_text)
    results.check("the release record records the earlier independent dispositions exactly",
                  "CASE09_INDEPENDENT_REVIEW_BLOCKED" in json.dumps(release)
                  and "CASE09_REMEDIATION_VERIFICATION_PASS" in json.dumps(release))
    results.check("the Case09-local exemption mechanism is recorded as local, not as shared precedent",
                  "CASE09_LOCAL_MECHANISM_ACCEPTABLE" in json.dumps(release)
                  and "NOT a shared-system precedent" in json.dumps(release))
    # No print method may be attributed to the owner anywhere in the release records.
    # Word-anchored on purpose: a bare substring scan would match hexadecimal inside a
    # commit pin or a source hash and report a paper size that nobody wrote.
    PRINT_METHOD_PATTERNS = (r"\b100\s?%", r"\bactual size\b", r"\bletter paper\b", r"\bA4\b",
                             r"\bduplex\b", r"\bchrome\b", r"\bsafari\b", r"\bfirefox\b",
                             r"\blaserjet\b", r"\binkjet\b", r"\bfit to page\b",
                             r"\bprint scale of\b", r"\bat \d+\s?% scale\b")
    # The prohibition is on attributing a print method to the OWNER, so it is enforced over
    # every owner-facing surface individually rather than over the record as one blob. The
    # engineering entries are allowed to name the tool they actually ran - suppressing that
    # would make the release record less truthful, not safer - but they are separately
    # required to be declared engineering entries and to disclaim the owner's environment.
    owner_facing = (("release record acceptedPrintStatus", release["acceptedPrintStatus"]),
                    ("release record owner visual review entry",
                     release["acceptedValidation"].get("visualReview", "")),
                    ("release record owner print review entry",
                     release["acceptedValidation"].get("physicalPrintReview", "")),
                    ("release record migration notes", json.dumps(release["migrationNotes"])),
                    ("owner approval record", approval_text))
    for label, text in owner_facing:
        leaked = [pattern for pattern in PRINT_METHOD_PATTERNS if re.search(pattern, text, re.I)]
        results.check(f"the {label} asserts no owner print method", not leaked, leaked)
    for label, text in (("release record", json.dumps(release)),
                        ("owner approval record", approval_text)):
        results.check(f"the {label} states that no print method is asserted",
                      "no browser, printer" in text, label)
    BROWSER_NAME_PATTERN = re.compile(r"\bchrome\b|\bsafari\b|\bfirefox\b|\bedge\b", re.I)
    ENGINEERING_TOOLING_ENTRIES = {"browser", "browserRunnerEnvironment", "rolePageCountsAndFit"}
    named_tooling = sorted(key for key, value in release["acceptedValidation"].items()
                           if isinstance(value, str) and BROWSER_NAME_PATTERN.search(value))
    results.check("only declared engineering entries name a browser anywhere in the record",
                  set(named_tooling) <= ENGINEERING_TOOLING_ENTRIES, named_tooling)
    for key in named_tooling:
        value = release["acceptedValidation"][key]
        results.check(f"acceptedValidation.{key} declares its browser as engineering measurement, "
                      "not the owner's environment",
                      "not a description of the owner" in value or "not the owner's" in value, key)
    results.check("the release record keeps production HTML-only with no canonical PDF",
                  "HTML-only" in release["artifactPolicy"]
                  and "no canonical PDF artifact exists" in release["acceptedPrintStatus"])
    results.check("the release record records no former generated artifact, verified not assumed",
                  release["formerArtifacts"]["status"] == "NO_FORMER_GENERATED_ARTIFACTS"
                  and "every path ever committed" in release["formerArtifacts"]["reason"].lower(),
                  release["formerArtifacts"]["status"])
    results.check("the release record claims no owner-approved bundle",
                  "bundle" not in json.dumps(release).lower()
                  or "no owner-approved bundle exists and none is claimed" in json.dumps(release).lower(),
                  "a bundle claim must be accompanied by the explicit disclaimer")
    results.check("the owner approval record claims no owner-approved bundle",
                  "no owner-approved bundle exists and none is claimed" in approval_text.lower())
    results.check("no prior approved release is claimed for a first release",
                  release["priorApprovedReleases"] == [] and release["retiredArtifacts"] == []
                  and "correctiveOf" not in release)
    # The release-history schema loop in validate_static.py is bound to the SSS partition
    # and never reaches an HHH package, so an HHH release record would otherwise ship
    # unvalidated against its own schema. This closes that gap for Case 09, reusing the
    # shared helper and the shared schema rather than introducing or modifying either.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import validate_static as _vs  # noqa: E402
    history_schema = json.loads(
        (ROOT / "shared/implementation/case-release-history.schema.v1.json").read_text(encoding="utf-8"))
    schema_findings = _vs.schema_errors(release, history_schema)
    results.check("the release record validates against case-release-history.schema.v1.json",
                  not schema_findings, schema_findings)
    results.check("the release record declares no field the shared schema does not define",
                  set(release) <= set(history_schema["properties"]),
                  sorted(set(release) - set(history_schema["properties"])))
    results.check("every schema-required release field is present",
                  set(history_schema["required"]) <= set(release),
                  sorted(set(history_schema["required"]) - set(release)))
    results.check("the release record carries the four frozen role DOM baselines",
                  set(release["frozenNonAccessibleDomBaselines"]) == {"student", "teacher", "answer", "note"}
                  and all(re.fullmatch(r"[a-f0-9]{64}", release["frozenNonAccessibleDomBaselines"][role])
                          for role in ("student", "teacher", "answer")))
    live_dom = {role: _vs.role_dom_hash(soup, role) for role in ALL_ROLES}
    results.check("the frozen role DOM baselines match the released content.html",
                  all(release["frozenNonAccessibleDomBaselines"][role] == live_dom[role]
                      for role in ("student", "teacher", "answer")),
                  json.dumps(live_dom))
    results.check("the recorded Accessible DOM hash matches the released content.html",
                  live_dom["accessible"] in release["frozenNonAccessibleDomBaselines"]["note"],
                  live_dom["accessible"])
    # No release metadata may reach a printable classroom page.
    RELEASE_METADATA_TOKENS = ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                               "formerArtifactRecoveryCommit", "acceptedValidation",
                               "frozenNonAccessibleDomBaselines", "priorApprovedReleases",
                               "acceptedPrintStatus", OWNER_PRINTABLE_BASELINE, certified,
                               OWNER_VISUAL_STATEMENT, OWNER_PRINT_STATEMENT)
    for role in ALL_ROLES:
        leaked = [token for token in RELEASE_METADATA_TOKENS if token.lower() in texts[role].lower()]
        results.check(f"{role}: no release metadata reaches a printable page", not leaked, leaked)

    # --- THE RESOLVED GAME DEPENDENCY AND THE OPEN QUALIFICATION -------------
    tracker = json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
    blocking = next(d for d in tracker["gameDependencies"] if d["findingId"] == "HHH-IMP-C2L2-001")
    qualification_dep = next(d for d in tracker["gameDependencies"] if d["findingId"] == "HHH-GAME-C2L2-001")
    runtime = registry["runtimeDependency"]
    results.check("the registry names the blocking finding as resolved at the current game commit",
                  runtime["findingId"] == "HHH-IMP-C2L2-001"
                  and runtime["dependencyClass"] == "GAME_REMEDIATION_BLOCKS_FINALIZATION"
                  and runtime["dependencyStatus"] == "RESOLVED_VERIFIED"
                  and runtime["resolvedGameCommit"] == GAME_COMMIT
                  and runtime["auditedGameCommit"] == AUDITED_GAME_COMMIT,
                  json.dumps({k: runtime.get(k) for k in ("findingId", "dependencyStatus", "resolvedGameCommit")}))
    results.check("the shared tracker records the same resolution, and this package leaves it untouched",
                  blocking["curriculumUnit"] == CASE_ID
                  and blocking["status"] == "RESOLVED_VERIFIED"
                  and blocking["resolution"]["resolvedGameCommit"] == GAME_COMMIT
                  and blocking["resolution"]["verificationStatus"] == "RESOLVED_VERIFIED",
                  json.dumps({k: blocking.get(k) for k in ("status", "curriculumUnit")}))
    evidence = blocking["resolution"]["resolutionEvidence"]
    results.check("the tracker's resolution evidence names all six required clues and the retained bonus scoring",
                  all(tag in evidence for tag in RESOLVED_CLUE_TAGS) and "bonusInsight" in evidence
                  and "siege_witnessed" in evidence and "requires: null" in evidence,
                  evidence[:300])
    results.check("the registry pins six operationally required strands and the resolved status of the street evidence",
                  runtime["requiredStrandCount"] == 6
                  and {s["id"] for s in runtime["requiredStrands"]} == REQUIRED_STRANDS
                  and "formerly insight-flagged" in next(s for s in runtime["requiredStrands"] if s["id"] == "siege-context")["runtimeStatus"]
                  and "six operationally required evidence clues" in runtime["verifiedSemantics"]
                  and "bonus scoring was retained" in runtime["verifiedSemantics"])
    results.check("the registry refuses to modify the game or to recreate the optional-clue reading",
                  "does not modify the game" in runtime["rule"]
                  and "does not recreate the former optional-clue reading" in runtime["rule"])
    results.check("the teacher qualification stays open in the tracker and is carried by the package",
                  qualification_dep["curriculumUnit"] == CASE_ID
                  and qualification_dep["dependencyClass"] == "CURRICULUM_QUALIFICATION_REQUIRED"
                  and qualification_dep["status"] == "OPEN_AT_AUDITED_GAME_BASELINE"
                  and qualification_dep["resolution"]["resolvedGameCommit"] is None
                  and runtime["qualificationFindingId"] == "HHH-GAME-C2L2-001"
                  and runtime["qualificationStatus"] == "OPEN_AT_AUDITED_GAME_BASELINE")

    # Lifecycle, repository and runtime metadata must never reach a printable page.
    LIFECYCLE_TOKENS = ("VALIDATION_BUILD", "OWNER_REVIEW", "packageStatus", "sourceHashes",
                        "case-package.json", "task-registry.js", "APPROVED_STABLE",
                        "d9fc16ba", "9b8545ed", "0626468", "9bfbe76", "0202027", "5429c3c",
                        "releaseHistory", "release-v0.1", "OWNER_REVIEW_PASS",
                        "historyRecord", "Nate / Owner", "editorPackage", "OWNER_REVIEW_NOT_STARTED",
                        "HHH-IMP-C2L2-001", "HHH-GAME-C2L2-001", "HHH-C2-CASE09", "RESOLVED_VERIFIED")
    for role in ALL_ROLES:
        found = [t for t in LIFECYCLE_TOKENS if t.lower() in texts[role].lower()]
        results.check(f"{role}: no lifecycle or repository metadata is printed", not found, found)
    status_contract = registry["sourceStatusContract"]
    for role in ALL_ROLES:
        leaked = [i for i in status_contract["prohibitedRuntimeIdentifiers"]
                  if i.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime implementation identifier is printed", not leaked, leaked)
    results.check("every prohibited runtime identifier is identifier-shaped",
                  all(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", i)
                      for i in status_contract["prohibitedRuntimeIdentifiers"]))
    results.check("the prohibited identifier list covers every resolved clue tag and the three location ids",
                  set(RESOLVED_CLUE_TAGS) | {"besieged_street", "seed_vault", "institute_office"}
                  <= set(status_contract["prohibitedRuntimeIdentifiers"]))

    # --- PAGE STRUCTURE AND DECLARED COUNTS ---------------------------------
    for role, expected in EXPECTED_PAGES.items():
        declared = package["rolePageStructure"][role]["pageCount"]
        actual = len(pages_for(soup, role))
        results.check(f"{role}: the locked page count of {expected} holds in package, registry and DOM",
                      declared == expected and registry["roles"][role] == expected and actual == expected,
                      json.dumps({"package": declared, "registry": registry["roles"][role], "dom": actual}))
        for index, page in enumerate(pages_for(soup, role), start=1):
            footer = page.select_one("[data-publication-footer]")
            ok = footer is not None and f"{index} of {expected}" in normalise(footer.get_text(" ", strip=True))
            results.check(f"{role}: page {index} carries a correct publication footer", ok,
                          normalise(footer.get_text(" ", strip=True)) if footer else "missing")
        missing_frame = [p.get("data-page-id") for p in pages_for(soup, role)
                         if not p.select_one(".page-frame") or not p.select_one(".overflow-warning")
                         or not p.select_one("[data-header-contract]")]
        results.check(f"{role}: every page carries frame, overflow strip and header contract",
                      not missing_frame, missing_frame)
        first = pages_for(soup, role)[0]
        results.check(f"{role}: page 1 uses the first-page identity and later pages do not",
                      first.select_one('[data-page-identity="first"]') is not None
                      and all(p.select_one('[data-page-identity="continuation"]') is not None
                              for p in pages_for(soup, role)[1:]))
    page_ids = [node.get("data-page-id") for node in soup.select(".page[data-page-id]")]
    persist_ids = [node.get("data-persist-id") for node in soup.select("[data-persist-id]")]
    results.check("page and persistence IDs are unique and complete",
                  len(page_ids) == len(set(page_ids)) and len(persist_ids) == len(set(persist_ids))
                  and None not in persist_ids)
    for role in LEARNER_ROLES:
        first = pages_for(soup, role)[0]
        content = first.select_one(".content-area")
        results.check(f"{role}: the Name / Date / Period row is the first printable element on page 1",
                      content is not None and content.find(True) is not None
                      and "student-id" in (content.find(True).get("class") or []))
        extra = [p.get("data-page-id") for p in pages_for(soup, role)[1:] if p.select_one(".student-id")]
        results.check(f"{role}: no continuation page repeats the identification row", not extra, extra)
    for role in ("teacher", "answer"):
        results.check(f"{role}: carries no student identification row",
                      not soup.select(f'section.page[data-role="{role}"] .student-id'))

    # --- THE EIGHT TASKS ----------------------------------------------------
    results.check("the registry declares exactly the eight locked task numbers and titles",
                  [(t["number"], t["title"]) for t in tasks] == EXPECTED_TASKS,
                  [(t["number"], t["title"]) for t in tasks])
    keyed = {t["number"]: t["keyed"] for t in tasks}
    results.check("every task is keyed except Task 2, which declares why it is not",
                  keyed == {"1": True, "2": False, "3": True, "4": True,
                            "5": True, "6": True, "7": True, "8": True}
                  and len(next(t for t in tasks if t["number"] == "2")["nonKeyableReason"]) > 80, keyed)
    for task in tasks:
        number, title = task["number"], task["title"]
        for role in LEARNER_ROLES:
            heading = soup.select_one(f'section.page[data-role="{role}"] [data-shell-task-heading="{number}"]')
            results.check(f"{role}: task {number} has exactly one shell heading",
                          len(soup.select(f'section.page[data-role="{role}"] '
                                          f'[data-shell-task-heading="{number}"]')) == 1 and heading is not None)
            placement = task["pagePlacement"][role]
            page = soup.select_one(f'section.page[data-role="{role}"][data-page-id="{placement}"]')
            results.check(f"{role}: task {number} starts on its declared page {placement}",
                          page is not None and page.select_one(f'[data-shell-task-heading="{number}"]') is not None,
                          placement)
        label = normalise(f"{number} · {title}")
        results.check(f"Teacher names task {number} by its exact number and title", label in teacher_text, label)
        bold = [normalise(n.get_text(" ", strip=True))
                for n in soup.select('section.page[data-role="teacher"] strong.task-reference')]
        results.check(f"Teacher task {number} reference is emphasised as a bold task-reference", label in bold, label)
        procedure_text = normalise(" ".join(n.get_text(" ", strip=True)
                                            for n in soup.select('section.page[data-role="teacher"] .procedure strong.task-reference')))
        results.check(f"Teacher procedure names task {number} in the timed route", label in procedure_text, label)
        answer_heading = soup.select_one(f'section.page[data-role="answer"] [data-shell-task-heading="{number}"]')
        if task["keyed"]:
            results.check(f"Answer Key keys task {number} on its declared page",
                          answer_heading is not None
                          and answer_heading.find_parent(class_="page").get("data-page-id")
                          == task["pagePlacement"]["answer"], task["pagePlacement"]["answer"])
        else:
            results.check(f"Answer Key omits non-keyable task {number} without renumbering",
                          answer_heading is None and task["pagePlacement"]["answer"] is None)
    results.check("every Teacher task reference names a real task and nothing else",
                  {normalise(n.get_text(" ", strip=True))
                   for n in soup.select('section.page[data-role="teacher"] strong.task-reference')}
                  == {normalise(f'{n} · {t}') for n, t in EXPECTED_TASKS})
    results.check("no learner or Answer Key page carries a task heading outside the locked set",
                  {n.get("data-shell-task-heading") for n in soup.select("[data-shell-task-heading]")}
                  == {n for n, _ in EXPECTED_TASKS})
    results.check("the Answer Key states that Task 2 is not keyed", "Task 2 is not keyed" in answer_text)
    results.check("no learner page prints internal grading policy or reveals the Task 2 answer",
                  not any(phrase in texts[role].lower() for role in LEARNER_ROLES
                          for phrase in ("not graded", "not scored", "ungraded",
                                         "for participation only", "is not keyed")))

    # --- CER IS DECLINED, AND THE DECLINE IS STRUCTURAL ----------------------
    cer = registry["cerDecision"]
    results.check("the registry records the CER decision with a rationale and a precedent",
                  cer["decision"] == "DECLINED" and len(cer["rationale"]) > 200 and len(cer["precedent"]) > 80)
    for selector in cer["prohibitedSelectors"]:
        results.check(f"no role renders the canonical CER component ({selector})", not soup.select(selector))
    results.check("no layout area is locked for a CER reason",
                  not [a for block in (layout, layout["student"]) for a in block["lockedAreas"] if a["reason"] == "cer"])
    results.check("the culminating product is the four-part continuity judgment in both learner editions",
                  all(soup.select(f'section.page[data-role="{role}"] [data-continuity-judgment]') for role in LEARNER_ROLES))
    for role in LEARNER_ROLES:
        block = soup.select_one(f'section.page[data-role="{role}"] [data-continuity-judgment]')
        tags = [normalise(t.get_text(" ", strip=True)) for t in block.select(".ex-tag")]
        labels = normalise(block.get_text(" ", strip=True)).lower()
        results.check(f"{role}: the judgment carries exactly four parts in order",
                      tags == ["A", "B", "C", "D"], tags)
        results.check(f"{role}: the judgment asks for judgment, strongest evidence, qualification and why it mattered",
                      all(k in labels for k in ("judgment", "strongest evidence", "qualification", "why it mattered")))

    # --- SOURCE STATUS -------------------------------------------------------
    bands = {band["id"]: band for band in status_contract["bands"]}
    source_layers = {s["id"]: s.get("evidenceLayer") for s in registry["caseSources"]}
    results.check("every canonical source declares a registered status band",
                  all(v in bands for v in source_layers.values()))
    results.check("the status contract is enforced in every role",
                  tuple(status_contract["enforcedRoles"]) == ALL_ROLES)
    results.check("the status vocabulary is the canonical three",
                  set(status_contract["statusVocabulary"])
                  == {"reconstructed game evidence", "documented", "curriculum-original schematic"})
    results.check("the three declared evidence-layer values are the ones the markup uses",
                  set(status_contract["layerValues"])
                  == {node.get("data-evidence-layer") for node in soup.select("[data-evidence-layer]")})
    evidence_objects = soup.select("[data-source-id]")
    results.check("at least one evidence object exists", bool(evidence_objects))
    for node in evidence_objects:
        page = node.find_parent(class_="page")
        if page is None:
            continue
        page_id = page.get("data-page-id")
        ids = node.get("data-source-id").split()
        results.check(f"{page_id}: every data-source-id resolves to a canonical source",
                      not [i for i in ids if i not in source_layers], ids)
        declared = node.get("data-evidence-layer")
        results.check(f"{page_id}: declared band is a registered band", declared in bands, declared)
        for source_id in ids:
            results.check(f"{page_id}: {source_id} markup band matches the registry",
                          source_layers.get(source_id) == declared)
        status = node.select_one(".source-status")
        results.check(f"{page_id}: the evidence object prints a SOURCE STATUS line", status is not None)
        if status is not None and declared in bands:
            printed = normalise(status.get_text(" ", strip=True))
            results.check(f"{page_id}: the status line uses the controlled concise form",
                          printed.upper().startswith("SOURCE STATUS ")
                          and bands[declared]["label"].lower() in printed.lower(), printed)
    allowed_status_lines = {normalise(f"SOURCE STATUS · {band['label']}").upper() for band in status_contract["bands"]}
    printed_status_lines = {normalise(n.get_text(" ", strip=True)).upper() for n in soup.select(".source-status")}
    results.check("every printed status line is one of the three controlled labels",
                  printed_status_lines <= allowed_status_lines, sorted(printed_status_lines - allowed_status_lines))
    for role in LEARNER_ROLES:
        notice = soup.select_one(f'section.page[data-role="{role}"] [data-source-status-notice]')
        results.check(f"{role}: page 1 carries the source-status notice",
                      notice is not None and notice.find_parent(class_="page") is pages_for(soup, role)[0])
        if notice is None:
            continue
        text = normalise(notice.get_text(" ", strip=True)).lower()
        for band in status_contract["bands"]:
            results.check(f"{role}: the notice names the {band['id']} band by its printed label",
                          band["label"].lower() in text)
        results.check(f"{role}: the notice states the non-merger rule in both directions",
                      "cannot establish what happened to the real collection" in text
                      and "cannot prove any event in the game" in text)
    fictional_nodes = soup.select("[data-fictional-data]")
    results.check("the packet marks its invented case data", len(fictional_nodes) >= 10, len(fictional_nodes))
    for node in fictional_nodes:
        holder = node.find_parent(attrs={"data-evidence-layer": True})
        results.check("invented data sits inside a reconstructed evidence object",
                      holder is not None and holder.get("data-evidence-layer") == "reconstructed", str(node)[:100])
    for source in registry["caseSources"]:
        results.check(f"source {source['id']} declares a contribution and a limitation",
                      len(source.get("contribution", "")) > 40 and len(source.get("limitation", "")) > 40)
    results.check("the reconstructed layer holds exactly the six runtime evidence strands",
                  [s["id"] for s in registry["caseSources"] if s["evidenceLayer"] == "reconstructed"] == RECONSTRUCTED_SOURCES)
    results.check("the documented layer holds exactly the three certified source cards",
                  [s["id"] for s in registry["caseSources"] if s["evidenceLayer"] == "documented"] == DOCUMENTED_SOURCES)
    results.check("every reconstructed source names the strand it supplies and the set covers all six",
                  {s.get("evidenceStrand") for s in registry["caseSources"] if s["evidenceLayer"] == "reconstructed"} == REQUIRED_STRANDS)
    PAGE_CLAIM = re.compile(r"(Student|Accessible) pages? ((?:\d+)(?:(?:,| and| to) \d+)*)", re.I)
    for source in registry["caseSources"]:
        for role_word, numbers in PAGE_CLAIM.findall(source.get("fallbackCorrespondence", "")):
            role = role_word.lower()
            declared = {int(n) for n in re.findall(r"\d+", numbers)}
            actual = {int(page.get("data-page-id").rsplit("-", 1)[1]) for page in pages_for(soup, role)
                      if page.select(f'[data-source-id~="{source["id"]}"]')}
            results.check(f"{source['id']}: declared {role} page(s) {sorted(declared)} carry the source",
                          declared <= actual, f"declared {sorted(declared)}, actual {sorted(actual)}")
    arch_rows = soup.select('section.page[data-role="teacher"] .source-table tbody tr')
    arch_claims = {}
    for row in arch_rows:
        cells = row.find_all(["th", "td"])
        if len(cells) < 5:
            continue
        arch_claims[normalise(cells[0].get_text(" ", strip=True))] = normalise(cells[-1].get_text(" ", strip=True))
    for source in registry["caseSources"]:
        declared = normalise(source.get("fallbackCorrespondence", ""))
        row_key = next((k for k in arch_claims if k.lower().startswith(
            source["displayLabel"].split(" ", 1)[0].lower() + " ")), None)
        if row_key is None or source["evidenceLayer"] == "curriculum-model":
            continue
        results.check(f"Teacher evidence architecture states the same location as the registry for {source['id']}",
                      arch_claims[row_key] == declared, json.dumps({"teacher": arch_claims[row_key], "registry": declared}))

    # --- MARKED IN-GAME QUOTATIONS ------------------------------------------
    claims = soup.select("[data-game-claim]")
    results.check("the packet marks its in-game quotations outside the reconstructed cards", len(claims) >= 3, len(claims))
    for node in claims:
        page = node.find_parent(class_="page")
        results.check(f"{page.get('data-page-id')}: the marked quotation sits inside a task that tests it",
                      node.find_parent(attrs={"data-tests-game-claim": True}) is not None, str(node)[:100])
        results.check(f"{page.get('data-page-id')}: the marked quotation is short",
                      len(normalise(node.get_text(" ", strip=True))) < 400)
    results.check("marked quotations appear only on learner pages",
                  all(n.find_parent(class_="page").get("data-role") in LEARNER_ROLES for n in claims))

    # --- CASE-LOCAL SOURCE CERTIFICATION ------------------------------------
    certification = registry["sourceCertification"]
    reused = {r["auditId"]: r for r in certification["auditReused"]}
    results.check("the certification reuses Phase 1 sources H13 and H14 without modifying the audit",
                  set(reused) == {"H13", "H14"}
                  and reused["H14"]["caseSourceId"] == "crop-trust-vavilov"
                  and reused["H13"]["caseSourceId"] == "vir-institute"
                  and all("No audit record is modified" in r["note"] for r in reused.values()))
    results.check("the H13 reuse note records that the page carried no siege narrative when consulted",
                  "under construction" in reused["H13"]["note"] and "institutional identity only" in reused["H13"]["note"])
    certified_ids = {c["caseSourceId"] for c in certification["caseCertified"]}
    results.check("every documented source card carries a case-local certification entry",
                  certified_ids == set(DOCUMENTED_SOURCES), sorted(certified_ids))
    results.check("exactly one source is added beyond the Phase 1 estate, and it is the authorized Loskutov article",
                  [c["caseSourceId"] for c in certification["caseCertified"] if "auditId" not in c] == ["loskutov-wartime"])
    loskutov = next(c for c in certification["caseCertified"] if c["caseSourceId"] == "loskutov-wartime")
    results.check("the Loskutov certification carries the exact authorized citation",
                  LOSKUTOV_DOI in loskutov["citation"] and "182(2):151" in loskutov["citation"]
                  and "Proceedings on Applied Botany, Genetics and Breeding" in loskutov["citation"]
                  and "2021" in loskutov["citation"])
    for needle in ("evacuat", "two lots", "Krasnoufimsk", "reproduce", "potato", "cereal", "regeneration",
                   "died of hunger", "more than twenty", "about 40,000 accessions", "1946"):
        results.check(f"the Loskutov certification supports the authorized claim family “{needle}”",
                      any(needle.lower() in s.lower() for s in loskutov["supports"]), needle)
    for needle in ("Morozov", "Consumption Report", "preservation scan", "accession ledger",
                   "untouched in one room", "zero losses", "settled staff-death count",
                   "quotation attributed to Vavilov", "forensic result"):
        results.check(f"the Loskutov certification refuses to certify “{needle}”",
                      any(needle.lower() in s.lower() for s in loskutov["doesNotSupport"]), needle)
    crop = next(c for c in certification["caseCertified"] if c["caseSourceId"] == "crop-trust-vavilov")
    results.check("the Crop Trust certification carries the arrest year, the death date and place, and the 250,000 figure",
                  any("1940" in s for s in crop["supports"]) and any("26 January 1943" in s and "Saratov" in s for s in crop["supports"])
                  and any("250,000" in s for s in crop["supports"]))
    results.check("the Crop Trust certification refuses the arrest month and any staff count",
                  any("month of the arrest" in s for s in crop["doesNotSupport"])
                  and any("count of staff" in s for s in crop["doesNotSupport"]))
    for entry_c in certification["caseCertified"]:
        results.check(f"certification {entry_c['caseSourceId']} names a citation, its supported claims and its bounds",
                      len(entry_c.get("citation", "")) > 40 and len(entry_c.get("supports", [])) >= 3
                      and len(entry_c.get("doesNotSupport", [])) >= 3)
    results.check("the certification closes the estate against uncertified claims",
                  "source-certification dependency for the PMO" in certification["noFurtherClaims"])
    # The estate is bibliographically closed: no uncertified institution or publication
    # is cited anywhere as a source of a real-world claim.
    for role in ALL_ROLES:
        # Word-anchored: a bare substring scan matches "nature" inside "countersignature".
        foreign = [t for t in ("wikipedia", "britannica", "smithsonian", "bbc",
                               "new york times", "nature (journal)", "encyclopedia")
                   if re.search(r"\b" + re.escape(t), texts[role], re.I)]
        results.check(f"{role}: no uncertified publication is cited", not foreign, foreign)

    # --- THE NO-GAME DOSSIER -------------------------------------------------
    no_game = registry["noGameRoute"]
    results.check("the no-game contract names the six reconstructed dossier sources in runtime order",
                  no_game["dossier"] == RECONSTRUCTED_SOURCES, no_game["dossier"])
    results.check("the six required evidence strands are all declared and map to reconstructed sources",
                  {s["id"] for s in no_game["requiredStrands"]} == REQUIRED_STRANDS
                  and all(source_layers.get(s["source"]) == "reconstructed" for s in no_game["requiredStrands"]))
    for role in no_game["requiredInRoles"]:
        for source_id in no_game["dossier"] + DOCUMENTED_SOURCES:
            results.check(f"{role}: source {source_id} is printed in the learner packet",
                          bool(soup.select(f'section.page[data-role="{role}"] [data-source-id~="{source_id}"]')), source_id)
    results.check("Teacher supplies both routes and states that Campaign 2 has no launch shortcut",
                  "Game route" in teacher_text and "No-game route" in teacher_text
                  and "no level selector and no shortcut" in teacher_text)
    results.check("Teacher maps the gameplay evidence to the printed dossier without ranking the routes",
                  "also printed as Sources A to F, in the same order" in teacher_text
                  and "neither is the reduced version" in teacher_text)
    results.check("Teacher supplies a complete no-game evidence digest", "Complete no-game evidence digest" in teacher_text)
    RUNTIME_RESOLUTION = ("The Record Validates", "The Rationed Collection", "The Keeper's Record",
                          "named and mourned", "Perfection is not proof", "Reasonable is not the same as true",
                          "Trace Analyst", "Corruption Scout", "into the fire", "at least nine",
                          "The Keeper's Record", "the post-war bank was rebuilt later",
                          "Perfection is not proof", "the completeness is the sacrifice",
                          "nine of its staff", "1,300", "thirteen hundred", "quiet billion")
    for role in ALL_ROLES:
        leaked = [t for t in RUNTIME_RESOLUTION if t.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime resolution, candidate label, hint or invented quotation is reproduced",
                      not leaked, leaked)
    RUNTIME_UI_LABELS = ("Validate the Record", "The evidence is incomplete", "Which record is genuine?",
                         "Take In the Street", "Speak to the Keeper", "Examine the Collection",
                         "Read the Accession Ledger", "Play the Vavilov Record", "Read the Consumption Report")
    for role in LEARNER_ROLES + ("answer",):
        leaked = [t for t in RUNTIME_UI_LABELS if t.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime control label is printed", not leaked, leaked)

    # --- H2: THE TWO-STRAND CHRONOLOGY --------------------------------------
    chrono = registry["chronologyBoundary"]
    results.check("the chronology contract declares the two strands and dated rows from certified sources only",
                  [s["id"] for s in chrono["strands"]] == ["vavilov", "institute"]
                  and all(r["certifiedBy"] in {"crop-trust-vavilov", "loskutov-wartime"} for r in chrono["requiredRows"])
                  and len(chrono["requiredRows"]) >= 8)
    vav_rows = [r for r in chrono["requiredRows"] if r["strand"] == "vavilov"]
    results.check("the contract's Vavilov rows carry the arrest in 1940 and the death in 1943, and nothing in Leningrad after 1940",
                  any(r["year"] == "1940" and "arrested" in r["event"] for r in vav_rows)
                  and any(r["year"] == "1943" and "Saratov" in r["event"] for r in vav_rows)
                  and not any("leningrad" in r["event"].lower() for r in vav_rows if r["year"] not in ("1887",)))
    for role in chrono["roles"]:
        figure = soup.select_one(f'section.page[data-role="{role}"] {chrono["selector"]}')
        results.check(f"{role}: the two-strand chronology is present", figure is not None)
        if figure is None:
            continue
        fig_text = normalise(figure.get_text(" ", strip=True))
        for fragment in chrono["requiredPrintedText"]:
            results.check(f"{role}: the chronology prints {fragment}", fragment.lower() in fig_text.lower(), fragment)
        rows = figure.select(".tl-row")
        strands = [r.get("data-strand") for r in rows]
        results.check(f"{role}: every chronology row prints its strand word",
                      all(normalise(r.select_one(".tl-tag").get_text()).upper() == r.get("data-strand").upper()
                          for r in rows) and set(strands) == {"vavilov", "institute"})
        years = [normalise(r.select_one(".tl-year").get_text()) for r in rows]
        arrest_index = next(i for i, r in enumerate(rows) if r.get("data-strand") == "vavilov" and "Arrested" in r.get_text())
        siege_index = next(i for i, r in enumerate(rows) if "8 September 1941" in r.get_text())
        death_index = next(i for i, r in enumerate(rows) if "26 January 1943" in r.get_text())
        results.check(f"{role}: the arrest row precedes the siege row, which precedes the death row",
                      arrest_index < siege_index < death_index, years)
        results.check(f"{role}: the death row sits on the Vavilov strand and names Saratov",
                      rows[death_index].get("data-strand") == "vavilov" and "Saratov" in rows[death_index].get_text())
        results.check(f"{role}: no Vavilov row after 1940 places him at the Institute or in Leningrad",
                      not any(("Leningrad" in r.get_text() or "at the Institute" in r.get_text().replace("never at the besieged Institute", ""))
                              for r in rows[arrest_index + 1:] if r.get("data-strand") == "vavilov"))
        results.check(f"{role}: the last chronology row reaches the 1946 regeneration check",
                      years[-1] == "1946" and "regeneration" in rows[-1].get_text())
        for pattern in chrono["prohibitedPatterns"]:
            hit = re.search(pattern["regex"], fig_text, re.I)
            results.check(f"{role}: the chronology text avoids {pattern['id']}", hit is None,
                          (hit.group(0) if hit else "") + " :: " + pattern["why"])
        root = figure_root(figure)
        caption = root.find("figcaption") if root is not None else None
        cap_text = normalise(caption.get_text(" ", strip=True)) if caption else ""
        for term in chrono["requiresCaptionTerms"]:
            results.check(f"{role}: the chronology caption carries the {term} status term", term in cap_text.upper(), cap_text[:200])
        results.check(f"{role}: the chronology is declared a curriculum schematic and names its sources as the evidence",
                      figure.get("data-evidence-layer") == "curriculum-model" and "this drawing organises them" in cap_text.lower())
    # "August 1940" may appear only inside the reconstructed annotation card, never as a documented date.
    for role in ALL_ROLES:
        stray = []
        for page in pages_for(soup, role):
            for node in page.find_all(string=re.compile(r"August\s+1940")):
                holder = node.find_parent(attrs={"data-evidence-layer": "reconstructed"})
                if holder is None and node.find_parent(attrs={"data-semantic-exemption": True}) is None:
                    stray.append(normalise(str(node))[:80])
        results.check(f"{role}: the arrest month appears only as the game's own annotation", not stray, stray)

    # --- H1: THE CONTINUITY CHAIN -------------------------------------------
    chain = registry["continuityChain"]
    results.check("the chain contract draws eight documented nodes from pre-crisis to continuing collection",
                  [n["id"] for n in chain["nodes"]][0] == "pre-crisis" and [n["id"] for n in chain["nodes"]][-1] == "continuing"
                  and len(chain["nodes"]) == 8 and all(n["status"] == "documented" for n in chain["nodes"])
                  and "losses" in {n["id"] for n in chain["nodes"]})
    results.check("the chain contract refuses to reproduce the game's simplicity as history",
                  "not reproduced as history" in chain["rule"])
    for role in chain["roles"]:
        figure = soup.select_one(f'section.page[data-role="{role}"] {chain["selector"]}')
        results.check(f"{role}: the continuity chain is present", figure is not None)
        if figure is None:
            continue
        fig_text = normalise(figure.get_text(" ", strip=True))
        for fragment in chain["requiredPrintedText"]:
            results.check(f"{role}: the chain prints {fragment}", fragment.lower() in fig_text.lower(), fragment)
        names = [normalise(n.get_text(" ", strip=True)) for n in figure.select(".cn-name")]
        results.check(f"{role}: the chain nodes are in the contract order",
                      names == [n["label"] for n in chain["nodes"]], names)
        labels = [normalise(n.get_text(" ", strip=True)) for n in figure.select(".cl-label")]
        results.check(f"{role}: every link carries a label naming what preserved identity",
                      labels == chain["linkLabels"], labels)
        results.check(f"{role}: the LOSSES node is drawn as a link in the chain, not a break",
                      figure.select_one(".chain-node.chain-loss") is not None
                      and normalise(figure.select_one(".chain-node.chain-loss .cn-name").get_text()) == "LOSSES")
        rule_node = figure.select_one("[data-continuity-rule='not-immobility']")
        results.check(f"{role}: the printed continuity rule sits inside the chain figure",
                      rule_node is not None and normalise(chain["requiredRule"]).lower()
                      in normalise(rule_node.get_text(" ", strip=True)).lower())
        for pattern in chain["prohibitedPatterns"]:
            hit = re.search(pattern["regex"], fig_text, re.I)
            results.check(f"{role}: the chain text avoids {pattern['id']}", hit is None,
                          (hit.group(0) if hit else "") + " :: " + pattern["why"])
        root = figure_root(figure)
        caption = root.find("figcaption") if root is not None else None
        cap_text = normalise(caption.get_text(" ", strip=True)) if caption else ""
        for term in chain["requiresCaptionTerms"]:
            results.check(f"{role}: the chain caption carries the {term} status term", term in cap_text.upper(), cap_text[:200])
        results.check(f"{role}: the chain caption refuses to be read as evidence",
                      "not evidence about any particular accession" in cap_text.lower())
        build = soup.select_one(f'section.page[data-role="{role}"] .chain-build')
        results.check(f"{role}: the learner's five-box chain is present with five boxes",
                      build is not None and len(build.select(".cb-box")) == 5)
    student_build = soup.select_one('section.page[data-role="student"] .chain-build')
    accessible_build = soup.select_one('section.page[data-role="accessible"] .chain-build')
    results.check("Student fills all five chain boxes; Accessible is given the two ends",
                  len(student_build.select(".chain-response")) == 5
                  and len(accessible_build.select(".chain-response")) == 3
                  and len(accessible_build.select(".cb-given")) == 2
                  and accessible_build.get("data-accessible-adaptation") == "t4-ends-supplied")

    # --- TASK 6: THE REPORT TESTED INSIDE THE GAME ---------------------------
    claim_test = registry["claimTest"]
    results.check("the claim-test contract declares the four tests and keeps the report inside the game",
                  [t["label"] for t in claim_test["tests"]] == ["CHRONOLOGY", "COLLECTION CONDITION", "ACCESSION RECORD", "CORROBORATION"]
                  and claim_test["insideGameOnly"] is True
                  and all(source_layers.get(t["checkedAgainst"]) == "reconstructed" for t in claim_test["tests"]))
    for role in claim_test["roles"]:
        organiser = soup.select_one(f'section.page[data-role="{role}"] {claim_test["selector"]}')
        results.check(f"{role}: the four-test organiser is present", organiser is not None)
        if organiser is None:
            continue
        text = normalise(organiser.get_text(" ", strip=True))
        for fragment in ("CHRONOLOGY", "COLLECTION CONDITION", "ACCESSION RECORD", "CORROBORATION"):
            results.check(f"{role}: the organiser prints the {fragment} test", fragment in text.upper())
        results.check(f"{role}: the organiser has exactly four test rows", len(organiser.select("tbody tr")) == 4)
        page = organiser.find_parent(class_="page")
        page_text = normalise(page.get_text(" ", strip=True))
        results.check(f"{role}: the page prints that appearance is not proof of forgery",
                      "not one of them is proof that the report is forged" in page_text
                      and "not one of the four tests" in page_text)
        results.check(f"{role}: the directions confine the test to the game's own evidence",
                      "inside the game" in page_text.lower() and "Sources B to E only" in page_text)
        verdict = page.select_one('[data-persist-id$="6-verdict"]')
        results.check(f"{role}: the verdict slot is a persistent control", verdict is not None and verdict.has_attr("data-response"))
    accessible_claims = soup.select('section.page[data-role="accessible"] .claim-test-table .prefilled')
    results.check("the Accessible organiser supplies exactly the four report claims, and the Student organiser supplies none",
                  len(accessible_claims) == 4 and not soup.select('section.page[data-role="student"] .claim-test-table .prefilled'))
    results.check("the supplied claims are marked as in-game quotations, one marker per claim",
                  all(n.select_one("[data-game-claim]") is not None for n in accessible_claims)
                  and len(soup.select('section.page[data-role="accessible"] .claim-test-table [data-game-claim]')) == 4)

    # --- THE HISTORICAL QUALIFICATION: POSITIVE REQUIREMENTS ----------------
    hq = registry["historicalQualification"]
    results.check("the qualification names the audit finding and the five refused simplifications",
                  hq["findingId"] == "HHH-GAME-C2L2-001" and len(hq["refusedSimplifications"]) == 5)
    results.check("the qualification states the death-count rule and the Vavilov rule in terms",
                  "more than twenty" in hq["deathCountRule"] and "Other published accounts count differently" in hq["deathCountRule"]
                  and "arrested in 1940" in hq["vavilovRule"] and "26 January 1943" in hq["vavilovRule"]
                  and "never at the besieged Institute" in hq["vavilovRule"])
    for requirement in hq["positiveRequirements"]:
        for role in requirement["roles"]:
            found = soup.select(f'section.page[data-role="{role}"] {requirement["selector"]}')
            results.check(f"{role}: positive requirement {requirement['id']} is printed", bool(found), requirement["selector"])
    for role in hq["requiredPrintedStatementRoles"]:
        for statement in hq["requiredPrintedStatements"]:
            results.check(f"{role}: prints the required statement “{statement[:46]}…”",
                          normalise(statement).lower() in texts[role].lower(), statement)
    # The two-layer verdict in the Answer Key distinguishes the in-world verdict from history.
    verdict_block = soup.select_one('section.page[data-role="answer"] [data-two-layer-verdict]')
    verdict_text = normalise(verdict_block.get_text(" ", strip=True)) if verdict_block else ""
    results.check("the Answer Key's Task 7 exemplar separates the in-world verdict from the real-history conclusion",
                  "Inside the game" in verdict_text
                  and "the keeper's account is the one the evidence supports" in verdict_text
                  and "substantially preserved" in verdict_text and "partly lost" in verdict_text
                  and "not evidence for the historical one" in verdict_text, verdict_text[:200])
    # Every role prints the losses beside the continuity it argues for.
    for role in ALL_ROLES:
        results.check(f"{role}: the packet prints the documented losses beside the continuity",
                      "40,000" in texts[role], texts[role][:0])
    # Every death count printed in any role is qualified in the same proposition.
    for role in ALL_ROLES:
        results.check(f"{role}: every printed count of the dead is qualified",
                      all(re.search(r"\b(more than|at least|about|counts?|account|accounts|names|differ|disagree)\b", p, re.I)
                          for p in propositions(texts[role])
                          if re.search(r"\b(twenty|thirty|\d\d)\b[^.!?]{0,40}\b(experts|scientists|researchers|staff|employees|specialists)\b", p, re.I)
                          and re.search(r"\b(died|death|deaths|lives|lost|starv)", p, re.I)),
                      [p for p in propositions(texts[role])
                       if re.search(r"\b(twenty|thirty|\d\d)\b[^.!?]{0,40}\b(experts|scientists|researchers|staff|employees|specialists)\b", p, re.I)
                       and re.search(r"\b(died|death|deaths|lives|lost|starv)", p, re.I)
                       and not re.search(r"\b(more than|at least|about|counts?|account|accounts|names|differ|disagree)\b", p, re.I)])

    # --- SEMANTIC GUARDS: POSITIVE CONTROL (the package itself) --------------
    invariants = registry["semanticInvariants"]
    exemptions = {e["id"]: e for e in invariants["exemptions"]}
    structural = invariants["structuralExemptSelectors"]
    compiled = compile_classes(hq["prohibitedFramings"])
    results.check("all five prohibited concept classes compile",
                  set(compiled) == {"vavilovPresentAtSiege", "nothingMovedAsHistory", "zeroLossAsHistory",
                                    "cleanProvesForged", "settledDeathCount"}, sorted(compiled))
    results.check("the structural exemptions excuse only the historical-claim classes",
                  all(set(s["allowedConcepts"]) <= {"nothingMovedAsHistory", "zeroLossAsHistory", "vavilovPresentAtSiege"}
                      for s in structural)
                  and {s["selector"] for s in structural} == {"[data-evidence-layer='reconstructed']", "[data-game-claim]"})
    for role in ALL_ROLES:
        violations = scan_html(html, compiled, exemptions, structural, role)
        results.check(f"{role}: no unexempted proposition states a prohibited framing",
                      not violations, json.dumps(violations[:6], indent=1))

    # --- SEMANTIC GUARDS: NEGATIVE CONTROLS ---------------------------------
    for class_id, sentences in hq["negativeControls"].items():
        results.check(f"negative controls exist for {class_id}", len(sentences) >= 3, sentences)
        for sentence in sentences:
            hits = scan_html(synthetic("student", f"<p>{sentence}</p>"), compiled, exemptions, structural, "student")
            results.check(f"negative control fires for {class_id}: {sentence[:52]}", any(h[2] == class_id for h in hits), hits)
    # Structural mutation controls: the same sentence is excused inside a reconstructed
    # card or a marked quotation, and NOT excused when the marker is absent or forged.
    inside_card = synthetic("student", '<section class="dossier-card" data-source-id="preservation-scan" '
                                       'data-evidence-layer="reconstructed"><p>The collection never left the room.</p></section>')
    results.check("structural control: a reconstructed card may print the game's immobility claim",
                  not scan_html(inside_card, compiled, exemptions, structural, "student"))
    marked = synthetic("student", '<div data-tests-game-claim="4"><p>The scan reads: <span data-game-claim="x">the collection never left the room.</span></p></div>')
    results.check("structural control: a marked in-game quotation is excused",
                  not scan_html(marked, compiled, exemptions, structural, "student"))
    unmarked = synthetic("student", '<div data-tests-game-claim="4"><p>The collection never left the room.</p></div>')
    results.check("structural control: the same sentence without the marker fires",
                  bool(scan_html(unmarked, compiled, exemptions, structural, "student")))
    forged_layer = synthetic("student", '<section class="dossier-card" data-evidence-layer="documented"><p>The collection never left the room.</p></section>')
    results.check("structural control: a documented card is not excused from the immobility class",
                  bool(scan_html(forged_layer, compiled, exemptions, structural, "student")))
    clean_in_card = synthetic("student", '<section class="dossier-card" data-evidence-layer="reconstructed"><p>The report is too clean, so it is forged.</p></section>')
    results.check("structural control: a reconstructed card is still held to the clean-proves-forged class",
                  bool(scan_html(clean_in_card, compiled, exemptions, structural, "student")))

    # --- SEMANTIC GUARDS: POSITIVE (MUST-NOT-FLAG) CONTROLS -----------------
    REQUIRED_LEGAL = [
        "Collection continuity does not require physical immobility or perfect survival.",
        "Vavilov was arrested in 1940 and was never at the besieged Institute.",
        "The collection remained substantially continuous despite losses.",
        "A clean document can be genuine.",
        "Published accounts give different numbers of staff who died.",
    ]
    results.check("the registry carries every required positive control",
                  all(s in hq["positiveControls"] for s in REQUIRED_LEGAL),
                  [s for s in REQUIRED_LEGAL if s not in hq["positiveControls"]])
    for sentence in hq["positiveControls"]:
        hits = scan_html(synthetic("student", f"<p>{sentence}</p>"), compiled, exemptions, structural, "student")
        results.check(f"truthful prose is not flagged: {sentence[:52]}", not hits, hits)

    # --- EXEMPTION CONTRACT IS CLOSED ---------------------------------------
    used = {n.get("data-semantic-exemption") for n in soup.select("[data-semantic-exemption]")}
    results.check("every exemption used in markup is registered", used <= set(exemptions), sorted(used - set(exemptions)))
    results.check("no learner edition uses a semantic exemption at all",
                  not soup.select('section.page[data-role="student"] [data-semantic-exemption]')
                  and not soup.select('section.page[data-role="accessible"] [data-semantic-exemption]'))
    for node in soup.select("[data-semantic-exemption]"):
        eid = node.get("data-semantic-exemption")
        page = node.find_parent(class_="page")
        if page is None or eid not in exemptions:
            continue
        results.check(f"exemption {eid} is used only in a role it declares",
                      page.get("data-role") in exemptions[eid]["roles"], f"{eid} on {page.get('data-role')}")
    for spec in exemptions.values():
        results.check(f"exemption {spec['id']} allows only registered concept classes",
                      not [c for c in spec["allowedConcepts"] if c not in compiled])
    forged = synthetic("student", '<p data-semantic-exemption="not-a-registered-id">Vavilov guarded the collection during the siege.</p>')
    results.check("mutation control: an unregistered exemption id excuses nothing",
                  bool(scan_html(forged, compiled, exemptions, structural, "student")))
    wrong_role = synthetic("student", '<p data-semantic-exemption="teacher-misconception">Vavilov guarded the collection during the siege.</p>')
    results.check("mutation control: an exemption does not carry into a role it does not declare",
                  bool(scan_html(wrong_role, compiled, exemptions, structural, "student")))

    # --- EDITION RESPONSE PARITY --------------------------------------------
    erc = registry["editionResponseContract"]
    subparts = erc["subparts"]
    adaptation_ids = {a["id"] for a in registry["accessibleAdaptations"]}
    declared: dict[str, list[str]] = {"student": [], "accessible": []}
    for sub in subparts:
        declared["student"].extend(sub["student"])
        declared["accessible"].extend(sub["accessible"])
    for edition in ("student", "accessible"):
        live = [n.get("data-persist-id") for n in
                soup.select(f'section.page[data-role="{edition}"] [data-response][data-persist-id]')]
        identity = set(erc["identityFields"][edition])
        assessed = [i for i in live if i not in identity]
        listed = declared[edition]
        results.check(f"{edition}: every assessed response belongs to exactly one declared subpart",
                      sorted(assessed) == sorted(listed),
                      json.dumps({"unlisted": sorted(set(assessed) - set(listed)), "listed-but-absent": sorted(set(listed) - set(assessed))}))
        results.check(f"{edition}: no response id is claimed by two subparts", len(listed) == len(set(listed)))
        results.check(f"{edition}: declared identity fields exist and are not assessed",
                      identity <= set(live) and not (identity & set(listed)))
    for sub in subparts:
        label = f"{sub['task']} {sub['id']}"
        klass, ns, na = sub["differenceClass"], len(sub["student"]), len(sub["accessible"])
        results.check(f"{label}: has no Accessible-only obligation", ns > 0)
        results.check(f"{label}: names a real task", any(t["id"] == sub["task"] for t in tasks))
        if klass == "parity":
            results.check(f"{label}: declared parity holds", ns == na, f"{ns} vs {na}")
        elif klass == "declared-reduction":
            results.check(f"{label}: reduction is real and registered",
                          na < ns and sub.get("governedBy") in adaptation_ids, f"{ns} -> {na}, governedBy={sub.get('governedBy')}")
        elif klass == "chunking":
            results.check(f"{label}: chunking splits rather than adds demand", na >= ns and "chunkingNote" in sub)
        else:
            results.check(f"{label}: declares a known difference class", False, klass)
        if na > ns:
            results.check(f"{label}: an Accessible field increase is only ever a declared chunking split", klass == "chunking", klass)
    results.check("the contract forbids an accessible-only obligation class",
                  erc["differenceClasses"]["accessible-only"].startswith("PROHIBITED"))
    results.check("every task with assessed responses is represented in the parity contract",
                  {sub["task"] for sub in subparts} == {t["id"] for t in tasks})
    results.check("Task 7 collects its four parts as four separately scored responses in both editions",
                  [next(s for s in subparts if s["id"] == i)["differenceClass"] for i in
                   ("judgment", "strongest-evidence", "qualification", "why-it-mattered")] == ["parity"] * 4)

    # --- ACCESSIBLE ADAPTATIONS ARE TRUE AND DECLARED -----------------------
    adaptations = registry["accessibleAdaptations"]
    results.check("exactly six Accessible adaptations are declared, and no seventh has appeared",
                  len(adaptations) == 6, sorted(adaptation_ids))
    for adaptation in adaptations:
        task = next(t for t in tasks if t["id"] == adaptation["task"])
        label = normalise(f"{task['number']} · {task['title']}")
        results.check(f"adaptation {adaptation['id']} is disclosed to the teacher", label in teacher_text)
        for role in adaptation["declaredIn"]:
            results.check(f"adaptation {adaptation['id']} declares a real role", role in ALL_ROLES)
        results.check(f"adaptation {adaptation['id']} explains why it is not a leak", len(adaptation.get("whyNotALeak", "")) > 60)
    marked_adaptations = {n.get("data-accessible-adaptation") for n in soup.select("[data-accessible-adaptation]")}
    results.check("every adaptation marked in the Accessible markup is registered", marked_adaptations <= adaptation_ids)
    results.check("all six declared adaptations are actually present in the Accessible edition",
                  marked_adaptations == adaptation_ids, sorted(adaptation_ids ^ marked_adaptations))
    results.check("every marked adaptation sits in the Accessible edition and nowhere else",
                  all(n.find_parent(class_="page").get("data-role") == "accessible" for n in soup.select("[data-accessible-adaptation]")))
    results.check("the Accessible worked examples are printed as examples rather than as blanks",
                  all("WORKED EXAMPLE" in normalise(n.get_text(" ", strip=True)).upper()
                      for n in soup.select('section.page[data-role="accessible"] [data-accessible-adaptation="t3-dates-supplied"], '
                                           'section.page[data-role="accessible"] [data-accessible-adaptation="t5-modelled-row"]')))
    prefilled_matrix = soup.select('section.page[data-role="accessible"] .contribution-table .prefilled')
    results.check("the Accessible matrix supplies the three modelled cells and no more, and prints the status column",
                  len(prefilled_matrix) == 3 and not soup.select('section.page[data-role="student"] .contribution-table .prefilled')
                  and len(soup.select('section.page[data-role="accessible"] .contribution-table .status-chip')) == 4
                  and not soup.select('section.page[data-role="accessible"] .contribution-table .status-slot'))
    results.check("the Student matrix asks for all four statuses as persistent compact controls",
                  len(soup.select('section.page[data-role="student"] .contribution-table .status-slot[data-response]')) == 4)
    results.check("the Teacher scoring note claims exactly six scored differences", "Six scored differences, and only six" in teacher_text)
    results.check("the Answer Key discloses the same six scored differences", "Six scored differences, and only six" in answer_text)
    results.check("the Accessible edition uses continuous flow rather than one task per page",
                  any(len(p.select("[data-shell-task-heading]")) >= 2 for p in pages_for(soup, "accessible")))
    results.check("the Accessible Task 2 carries sentence frames",
                  len(soup.select('section.page[data-role="accessible"][data-page-id="accessible-seeds-05"] .memo-frame')) >= 2)
    results.check("the Accessible Task 7 carries sentence starters on every part",
                  len(soup.select('section.page[data-role="accessible"] [data-continuity-judgment] .memo-frame')) == 4)
    results.check("the Accessible Task 8 is a bounded choice with one persistent mark and one explanation",
                  [m.get("data-persist-id") for m in soup.select('section.page[data-role="accessible"] [data-accessible-adaptation="t8-bounded-choice"] ~ .count-grid .mark-response')] == ["a8-choice"]
                  and soup.select_one('section.page[data-role="accessible"] [data-persist-id="a8-why"]') is not None)

    # --- RESPONSE SPACE AND DIGITAL MARKABILITY -----------------------------
    for edition, block in (("student", layout["student"]), ("accessible", layout)):
        declared_ids = {a["persistId"] for a in block["areas"]} | {a["persistId"] for a in block["lockedAreas"]}
        found_ids = [n.get("data-persist-id") for n in
                     soup.select(f'section.page[data-role="{edition}"] [data-response][data-persist-id]')]
        results.check(f"{edition}: every persistent response is layout-classified",
                      set(found_ids) == declared_ids,
                      json.dumps({"unclassified": sorted(set(found_ids) - declared_ids), "orphan": sorted(declared_ids - set(found_ids))}))
        results.check(f"{edition}: no persist id is used twice", len(found_ids) == len(set(found_ids)))
    for selector, label in ((".mark-response", "compact judgment slot"), (".inline-response", "vocabulary blank"),
                            (".table-response", "matrix cell"), (".chain-response", "chain box")):
        nodes = soup.select(f'.page[data-role="student"] {selector}, .page[data-role="accessible"] {selector}')
        results.check(f"every printed {label} in a learner edition is persistent and named",
                      bool(nodes) and all(m.has_attr("data-response") and m.has_attr("data-persist-id")
                                          and m.get("role") == "textbox" and m.get("aria-label") for m in nodes), len(nodes))
    results.check("every response field in every role carries an accessible name",
                  all(n.get("aria-label") or n.get("aria-labelledby") for n in soup.select("[data-response]")))
    results.check("every figure carries accessibility text",
                  all(f.select_one("[role='img'][aria-label]") is not None for f in soup.select("figure.case-figure")))

    # --- FIGURE CONTRACT -----------------------------------------------------
    def described_alt(role: str, contract: str) -> str:
        node = soup.select_one(f'section.page[data-role="{role}"] [{contract}] [role="img"][aria-label]')
        return normalise(node.get("aria-label")) if node is not None else ""

    for spec in registry["figureContract"]["figures"]:
        for role in spec["roles"]:
            figure = soup.select_one(f'section.page[data-role="{role}"] {spec["selector"]}')
            results.check(f"{role}: figure {spec['id']} is present", figure is not None)
            if figure is None:
                continue
            described = figure.select_one("[role='img'][aria-label]")
            results.check(f"{role}: figure {spec['id']} carries accessibility text", described is not None)
            if described is None:
                continue
            alt = normalise(described.get("aria-label"))
            for pattern in spec.get("prohibitedPatterns", []):
                hit = re.search(pattern["regex"], alt, re.I)
                results.check(f"{role}: {spec['id']} accessibility text avoids {pattern['id']}", hit is None,
                              (hit.group(0) if hit else "") + " :: " + pattern["why"])
            for fragment in spec.get("requiresAltConcepts", []):
                results.check(f"{role}: {spec['id']} accessibility text names {fragment}", fragment.lower() in alt.lower(), fragment)
            if spec.get("requiresContinuityRule"):
                results.check(f"{role}: {spec['id']} accessibility text states the continuity rule",
                              spec["requiresContinuityRule"].lower() in alt.lower())
            fig_text = normalise(figure.get_text(" ", strip=True))
            for fragment in spec.get("requiresPrintedText", []):
                results.check(f"{role}: {spec['id']} prints {fragment}", fragment.lower() in fig_text.lower(), fragment)
            root = figure_root(figure)
            caption = root.find("figcaption") if root is not None else None
            cap_text = normalise(caption.get_text(" ", strip=True)).upper() if caption else ""
            for term in spec.get("requiresCaptionTerms", []):
                results.check(f"{role}: {spec['id']} caption carries the status term {term}", term.upper() in cap_text)
    for figure_id, contract in (("two-timelines", "data-chronology-contract"), ("continuity-chain", "data-continuity-contract")):
        student_alt = described_alt("student", contract)
        accessible_alt = described_alt("accessible", contract)
        results.check(f"{figure_id} is identical in both learner editions", bool(student_alt) and student_alt == accessible_alt)
    results.check("no figure in the package uses imagery of any kind beyond the institutional insignia",
                  not soup.select('figure.case-figure img:not(.taa-insignia)'))
    results.check("no page references an external or generated image asset",
                  not [n.get("src") for n in soup.select("img") if "insignia" not in (n.get("src") or "")])
    results.check("every figure-level status line names the schematic band",
                  all("CURRICULUM-ORIGINAL SCHEMATIC" in normalise(f.select_one(".source-status").get_text()).upper()
                      for f in soup.select("figure.case-figure")))

    # --- PRINTABLE HYGIENE AND DOCUMENT SEMANTICS ---------------------------
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import validate_static  # noqa: E402  (imported late, and only for its detectors)
    results.check("no printable page carries production metadata or a status banner",
                  not validate_static.printable_production_metadata_findings(soup),
                  validate_static.printable_production_metadata_findings(soup))
    results.check("no printable heading announces owner review",
                  not validate_static.printable_owner_review_headings(soup))
    results.check("no printable sentence advertises a role page count the package contradicts",
                  not validate_static.hhh_page_count_prose_findings(soup, package),
                  validate_static.hhh_page_count_prose_findings(soup, package))
    jumps = []
    for page in soup.select(".page[data-role]"):
        levels = [int(h.name[1]) for h in page.select("h1,h2,h3,h4,h5,h6")]
        previous = None
        for level in levels:
            if previous is not None and level > previous + 1:
                jumps.append((page.get("data-page-id"), levels))
            previous = level
    results.check("every page keeps a heading hierarchy that never skips a level", not jumps, jumps)
    tables = soup.select("table")
    results.check("every table carries a caption, column headers and scoped row headers",
                  tables and all(t.find("caption") and t.select("thead th") and t.select('tbody th[scope="row"]') for t in tables))
    results.check("the package declares the language and the PDF-accessibility notice",
                  package["accessibility"]["language"] == "en"
                  and "does not guarantee PDF accessibility" in package["accessibility"]["pdfNotice"])
    results.check("production is HTML-only: no canonical PDF is declared anywhere in the package",
                  not any("pdf" in str(v).lower() for v in package["outputs"].values())
                  and all(str(v).endswith(".html") for v in package["outputs"].values()))
    results.check("no generated role output is committed beside the sources",
                  not [p.name for p in SOURCE.iterdir()
                       if p.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".webp"} or p.name.endswith("_CUSTOM.html")])
    results.check("no source file carries a machine-local path",
                  not [f.name for f in sorted(SOURCE.iterdir())
                       if re.search(r"/Users/|/home/|file:///|C:\\\\", f.read_text(encoding="utf-8"))])
    results.check("the README carries no machine-local path",
                  not re.search(r"/Users/|/home/|file:///", (UNIT / "README.md").read_text(encoding="utf-8")))

    # --- ANSWER KEY COVERAGE -------------------------------------------------
    for task in tasks:
        if not task["keyed"]:
            continue
        heading = soup.select_one(f'section.page[data-role="answer"] [data-shell-task-heading="{task["number"]}"]')
        block = heading.find_next(class_="answer-block") if heading is not None else None
        results.check(f"Answer Key task {task['number']} carries a completed exemplar block",
                      block is not None and len(normalise(block.get_text(" ", strip=True))) > 200)
    results.check("the Answer Key completes every Task 1 vocabulary placement",
                  all(term in answer_text for term in registry["vocabulary"]))
    results.check("the Answer Key completes all four Task 3 parts with the two dates",
                  all(f"Part {p} -" in answer_text for p in ("A", "B", "C", "D"))
                  and "arrested in 1940" in answer_text and "8 September 1941" in answer_text)
    results.check("the Answer Key completes all five Task 4 boxes and both parts",
                  all(k in answer_text for k in ("Before -", "It moved -", "It was reproduced -", "It was partly lost -", "After -"))
                  and "Part B -" in answer_text and "Part C -" in answer_text
                  and "identity lives in the provenance, not in the place" in answer_text)
    key_matrix = soup.select_one('section.page[data-role="answer"] .key-matrix')
    results.check("the Answer Key completes the Task 5 matrix as an actual matrix with four rows and three filled columns",
                  key_matrix is not None and len(key_matrix.select("tbody tr")) == 4
                  and all(len(tr.select("td")) == 3 and all(normalise(td.get_text(" ", strip=True)) for td in tr.select("td"))
                          for tr in key_matrix.select("tbody tr")))
    results.check("the Task 5 exemplar states every status and the direction of corroboration",
                  key_matrix is not None and len(key_matrix.select("tbody th em")) == 4
                  and "runs from G to E and never back" in answer_text)
    key_tests = soup.select('section.page[data-role="answer"] .key-matrix')
    results.check("the Answer Key completes the Task 6 organiser with all four tests, a verdict and the appearance response",
                  len(key_tests) >= 2 and len(key_tests[1].select("tbody tr")) == 4
                  and "Verdict inside the game -" in answer_text and "Why the clean finish is not a test -" in answer_text)
    results.check("the Answer Key states the in-world verdict without reproducing the runtime record label",
                  "the keeper's account is the one the evidence supports" in answer_text
                  and "keeper's record" not in answer_text.lower())
    results.check("the Task 6 exemplar refuses a verdict from the typing and a reach outside the game",
                  "a verdict reached from the typing" in answer_text and "reaches outside the game" in answer_text)
    results.check("the Answer Key completes all four Task 7 parts",
                  all(part in answer_text for part in ("A Judgment -", "B Strongest evidence -", "C Qualification -", "D Why it mattered -")))
    results.check("the Task 7 exemplar names documented links and keeps the layers apart",
                  "Source H's inventory and sealing" in answer_text and "Source H's 1946 check" in answer_text
                  and "cannot establish anything about the real collection at all" in answer_text)
    results.check("the Task 7 exemplar gives a sourced reason the diversity mattered and accepts an unresolved moral answer",
                  "germplasm, not food" in answer_text and "still finds the choice terrible" in answer_text)
    results.check("the Answer Key answers the transfer question rather than repeating the case",
                  "is a recall of Leningrad, not a transfer of the method" in answer_text
                  and "Evidence 1 -" in answer_text and "Evidence 2 -" in answer_text)
    floor = soup.select_one('section.page[data-role="answer"] [data-answer-key-floor]')
    floor_text = normalise(floor.get_text(" ", strip=True)) if floor is not None else ""
    for needle in ("guarded the collection during the siege", "never left the room", "nothing was lost",
                   "specific number of staff died", "clean finish proves it forged"):
        results.check(f"the Answer Key floor names the refused claim “{needle}”", needle in floor_text, floor_text[:260])
    results.check("every Answer Key exemplar block is followed by an acceptable-variation ruling",
                  len(soup.select('section.page[data-role="answer"] .answer-block'))
                  <= len([n for n in soup.select('section.page[data-role="answer"] .key-note')
                          if "Acceptable variation" in normalise(n.get_text(" ", strip=True))]) + 1)

    # --- TEACHER EDITION CONTRACT -------------------------------------------
    for needle, label in (("Launch sheet", "launch sheet"), ("The two routes", "both routes"),
                          ("Essential evidence", "essential evidence"), ("Likely sticking point", "likely sticking point"),
                          ("What to collect", "what to collect"), ("Teacher framing line", "framing line"),
                          ("Lesson overview", "lesson overview"), ("Guiding historical question", "guiding question"),
                          ("Standards alignment and claim limits", "standards alignment"),
                          ("Measurable objectives", "measurable objectives"), ("Success criteria", "success criteria"),
                          ("Academic vocabulary", "academic vocabulary"), ("Materials and preparation", "materials and preparation"),
                          ("Complete teaching procedure", "teaching procedure"), ("Facilitation prompts", "facilitation prompts"),
                          ("Transitions and collection points", "transitions and collection"),
                          ("Formative checks", "formative checks"), ("Assessment guidance", "assessment guidance"),
                          ("Accessible supports actually present", "accessible supports"),
                          ("Misconceptions this case is built to catch", "misconceptions"),
                          ("Evidence architecture", "evidence architecture"), ("Reasoning path", "reasoning path"),
                          ("The competing record", "competing record"),
                          ("Limitations to keep in front of the class", "limitations"),
                          ("The ethical-history boundary", "ethical-history boundary"),
                          ("Quick classroom rubric", "quick rubric"), ("Complete analytic rubric", "analytic rubric"),
                          ("Authoritative sources", "authoritative reference list"),
                          ("Complete no-game evidence digest", "no-game digest"),
                          ("Classroom and technical fallback", "classroom fallback")):
        results.check(f"Teacher Guide provides the {label}", needle in teacher_text, needle)
    rubric_levels = soup.select('section.page[data-role="teacher"] .analytic-rubric thead th')
    results.check("the analytic rubric uses four performance levels",
                  sum(1 for th in rubric_levels if re.match(r"[1-4]\s", normalise(th.get_text(" ", strip=True)))) == 4)
    results.check("the analytic rubric uses four criteria",
                  len(soup.select('section.page[data-role="teacher"] .analytic-rubric tbody tr')) == 4)
    results.check("a concise quick rubric exists alongside the analytic one",
                  bool(soup.select('section.page[data-role="teacher"] .quick-rubric')))
    MISCONCEPTIONS = ("never left the room, so the collection survived", "different collection now",
                      "vavilov guarded the collection during the siege", "as settled fact",
                      "typed too clean, so it is a forgery", "survivor who saw it happen",
                      "because it matches the crop trust", "seeds are food")
    lowered = teacher_text.lower()
    missing = [m for m in MISCONCEPTIONS if m not in lowered]
    results.check("the Teacher misconception table protects against every required framing", not missing, missing)
    results.check("the Teacher Guide carries the diagnostic reading for the non-keyable task",
                  "Read the two slots as a diagnostic" in teacher_text)
    results.check("the Teacher Guide states the Vavilov separation and the staff-death qualification",
                  "arrested in 1940 and died in prison in Saratov" in teacher_text
                  and "Published accounts disagree" in teacher_text)
    results.check("the Teacher Guide names the Loskutov article with its DOI in the authoritative sources",
                  LOSKUTOV_DOI in teacher_text and "Proceedings on Applied Botany, Genetics and Breeding" in teacher_text)
    results.check("the Teacher Guide names the Crop Trust and the Institute as the other two sources and closes the estate",
                  "Crop Trust" in teacher_text and "N. I. Vavilov All-Russian Institute of Plant Genetic Resources" in teacher_text
                  and "Do not extend the real-world layer beyond these three" in teacher_text)
    results.check("the Teacher Guide holds the ethical boundary without a verdict on the staff",
                  "does not supply a quotation for Vavilov" in teacher_text and "still finds the choice unbearable" in teacher_text)
    results.check("no Teacher page exposes a clue identifier or node path",
                  not re.search(r"\b[a-z]+_[a-z]+\b|->|__exit__", teacher_text))

    # --- STANDARDS -----------------------------------------------------------
    standards = registry["standards"]
    results.check("the directly assessed standards are exactly the seven locked claims",
                  standards["directlyAssessed"] == ["C3 D2.His.1.6-8", "C3 D2.His.2.6-8", "C3 D3.1.6-8", "C3 D3.2.6-8",
                                                    "CCSS RH.6-8.1", "CCSS RH.6-8.7", "CCSS WHST.6-8.1"], standards["directlyAssessed"])
    results.check("the supporting standards are exactly the two locked ones",
                  standards["supporting"] == ["CCSS RH.6-8.9", "CCSS WHST.6-8.2"])
    results.check("the contextual entry names the science content and nothing else",
                  standards["contextual"] == ["crop genetic diversity / germplasm / ex situ conservation"])
    results.check("no NGSS performance expectation is claimed at any status",
                  not any("NGSS" in s for s in standards["directlyAssessed"] + standards["supporting"] + standards["contextual"])
                  and "No NGSS performance expectation is claimed" in standards["ngss"]
                  and "No NGSS alignment is claimed" in teacher_text)
    for claim in standards["directlyAssessed"] + standards["supporting"]:
        results.check(f"standard {claim} appears in the Teacher standards table", claim in teacher_text, claim)
    table_rows = soup.select('section.page[data-role="teacher"] .standards-table tbody tr')
    results.check("the Teacher standards table carries one row per claim and no more",
                  len(table_rows) == len(standards["directlyAssessed"]) + len(standards["supporting"]))
    results.check("every Teacher standards row states where it is measured and its limit",
                  all("Limit:" in normalise(tr.get_text(" ", strip=True)) for tr in table_rows))
    results.check("the Teacher page names the contextual science content as contextual",
                  "Contextual science content, no science standard" in teacher_text)

    # --- VOCABULARY ----------------------------------------------------------
    vocabulary = registry["vocabulary"]
    results.check("the case declares seven vocabulary terms", len(vocabulary) == 7, vocabulary)
    results.check("the vocabulary bank is alphabetical by displayed term", vocabulary == sorted(vocabulary))
    results.check("the required terms are exactly the locked seven", vocabulary == EXPECTED_VOCABULARY, vocabulary)
    results.check("the exact-match bank decision is recorded with its reason",
                  "genuinely requires constrained exact recall" in registry["vocabularyBankDecision"])
    for role in LEARNER_ROLES:
        items = [normalise(i.get_text(" ", strip=True)) for i in soup.select(f'section.page[data-role="{role}"] .word-bank-item')]
        results.check(f"{role}: the word bank prints exactly the declared terms in alphabetical order", items == vocabulary, items)
        blanks = soup.select(f'section.page[data-role="{role}"] .term-list .inline-response')
        results.check(f"{role}: one blank per term, and no decoy in the bank", len(blanks) == len(vocabulary) == len(items))
        statements = [normalise(li.get_text(" ", strip=True)) for li in soup.select(f'section.page[data-role="{role}"] .term-list li')]
        results.check(f"{role}: the statements are not printed in bank order",
                      [t for t in vocabulary] != [next((v for v in vocabulary if v in s.lower()), None) for s in statements])
    for term in vocabulary:
        results.check(f"the Teacher vocabulary table defines {term}", term in teacher_text, term)

    payload = {
        "validator": "hhh-case09-seeds-they-kept-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": [a for a in results.assertions if a["status"] == "FAIL"] or "all passed",
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
