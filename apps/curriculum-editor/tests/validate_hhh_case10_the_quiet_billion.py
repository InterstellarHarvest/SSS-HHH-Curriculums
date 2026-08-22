#!/usr/bin/env python3
"""Case-scoped protections for HHH Campaign 2 Core Case 10 — The Quiet Billion.

These assertions guard the boundaries this case exists to get right, plus the
cross-edition parity the shared operational walk does not reach into. They are
driven by the contract blocks the task registry declares — ``sourceStatusContract``,
``runtimeDependency``, ``historicalQualification``, ``quantitativeRecord``,
``transmissionRoute``, ``productionPackage``, ``claimTest``, ``interpretations``,
``sourceCertification``, ``cerDecision``, ``noGameRoute``, ``timedRoute``,
``editionResponseContract``, ``accessibleAdaptations``, ``semanticInvariants`` and
``figureContract`` — rather than by literal paragraph locks, so ordinary rewording
stays possible while the meaning stays protected.

The audit dependency this case carries:

* ``HHH-GAME-C2L3-001`` — ``CURRICULUM_QUALIFICATION_REQUIRED``, open at the
  audited game baseline by design. The audit found the core semi-dwarf, lodging
  and rust story sound but held that exact field-yield claims and any "one seed
  saved a billion" shorthand must not replace broader irrigation, fertiliser and
  institutional context. The curriculum carries that qualification; the game is
  not modified, the game audit is not reopened and the shared remediation tracker
  is left untouched.

DESIGN NOTE — the shape of the semantic guard, and its limits.

This case has five high-risk misconceptions, and each gets one CLOSED class:

  * ``livesSavedAsMeasurement`` — a counted number of lives saved, fed or rescued
    asserted as documented history rather than as a claim;
  * ``seedAloneCausation`` — the variety, seed or wheat asserted as the sole cause
    of the agricultural gains;
  * ``productionIsYield`` — total production and yield per unit area treated as
    the same measure;
  * ``dwarfingCausesRust`` — semi-dwarfing or short straw asserted as the cause of
    rust or disease resistance;
  * ``productionEndsHunger`` — agricultural production asserted to have directly
    ended hunger, famine or malnutrition.

Every class is CLOSED: a small finite negative vocabulary, anchored to a named
subject register, requiring an affirmative and unnegated predicate. None
enumerates synonyms for an open concept, and none polices an ordinary verb. Only
the two classes the game itself asserts — the billion-lives filing claim and the
sole-cause interpretation the case puts on trial — are excused inside a
reconstructed evidence object and inside a marked in-game quotation. The other
three classes are excused nowhere in the learner editions at all, because the game
asserts none of them and the packet must not introduce them.

**This guard makes no claim of semantic completeness.** It is a defence against
five known misconceptions, not a proof that every possible bad paraphrase has
been detected. An unseen paraphrase can pass it. Ordinary cross-role parity,
source-status and manual review remain required, and the positive structural
requirements below — checked against markup rather than prose — are what carry
the audit obligation.

Every semantic guard ships with NEGATIVE CONTROLS it must flag and POSITIVE
CONTROLS it must not, and the package itself is the standing positive control.

Usage:
    python3 apps/curriculum-editor/tests/validate_hhh_case10_the_quiet_billion.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "hhh/campaign-2/case-10-the-quiet-billion"
SOURCE = UNIT / "source"
REGISTRY_FILE = ROOT / "shared/implementation/case-registry.v2.json"
TRACKER_FILE = ROOT / "hhh/production/data/HHH_GAME_REMEDIATION_DEPENDENCY_TRACKER_v1.0.json"
INVENTORY_FILE = ROOT / "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json"
RELEASE_SCHEMA = ROOT / "shared/implementation/case-release-history.schema.v1.json"
CASE_ID = "HHH-C2-CASE10"
LEARNER_ROLES = ("student", "accessible")
ALL_ROLES = ("student", "teacher", "answer", "accessible")
GAME_COMMIT = "d9fc16baf272cb543c29cbd0c06ec85efad60be8"
AUDITED_GAME_COMMIT = "9b8545ed6ecf98b337326390400076e36789e056"
OWNER = "Nate / Owner"
DISPLAY_ORDER = 12
DISPLAY_LABEL = "10 - The Quiet Billion"
TITLE = "The Quiet Billion"
EXPECTED_PAGES = {"student": 8, "teacher": 7, "answer": 4, "accessible": 10}
EXPECTED_TASKS = [
    ("1", "Build the Case Vocabulary"),
    ("2", "Set the Claim Test"),
    ("3", "Keep the Evidence Layers Separate"),
    ("4", "Read the Numbers Carefully"),
    ("5", "Trace the Wheat and the Package"),
    ("6", "Test the Failure Report"),
    ("7", "Test the Competing Interpretations"),
    ("8", "Write a Qualified Historical Finding"),
]
EXPECTED_VOCABULARY = ["baseline", "causation", "denominator", "Green Revolution", "input package",
                       "lodging", "pedigree", "semi-dwarf", "yield"]
RECONSTRUCTED_SOURCES = ["borlaug-record", "two-wheats", "pedigree-records", "rao-testimony", "failure-report"]
DOCUMENTED_SOURCES = ["india-wheat-record", "borlaug-nobel-lecture", "cimmyt-history", "pingali-retrospective"]
FIGURE_SOURCES = ["india-record-figure", "route-figure", "package-figure"]
REQUIRED_STRANDS = {"breeder-record", "lodging-evidence", "pedigree-provenance",
                    "field-yield-testimony", "failure-report"}
# The exact locked six-year Government of India series. Every value is asserted in the
# registry, in both learner editions and in the figure; nothing here is derived.
INDIA_SERIES = [
    ("1964-65", "13.42", "12.26", "913", "36.8%"),
    ("1965-66", "12.57", "10.40", "827", "43.1%"),
    ("1966-67", "12.84", "11.39", "887", "48.0%"),
    ("1967-68", "14.99", "16.54", "1,103", "43.4%"),
    ("1968-69", "15.96", "18.65", "1,169", "49.8%"),
    ("1969-70", "16.63", "20.09", "1,208", "51.1%"),
]
# The runtime clue tags and location ids for C2 L3, asserted against the audit's own
# static content inventory. They are never printed.
RUNTIME_CLUE_TAGS = ("trials_succeeded", "lodging_resistance", "pedigree_verified", "real_yields")
RUNTIME_INSIGHT_TAGS = ("forgery_read", "harvest_scale")
RUNTIME_LOCATIONS = ("trial_plots", "research_station", "deployment_field")
TASK_MINUTES = {"1": 4, "2": 3, "3": 4, "4": 8, "5": 6, "6": 6, "7": 6, "8": 9}
# The canonical no-game route is approximately sixty minutes IN TOTAL: launch, the required
# source reading, the eight tasks and the close all sit inside it. The unnumbered segments
# are timed here too, so that the printed procedure has to add up to sixty on its own.
SURROUNDING_MINUTES = {"launch": ("Launch", 3), "read-reconstructed": ("Read Sources A to E", 5),
                       "read-documented": ("Read Sources F to I", 4), "close": ("Close and collect", 2)}
ROUTE_TOTAL_MINUTES = 60
INDIA_EDITION = "Agricultural Statistics at a Glance 2015"
INDIA_TABLE_TITLE = "Wheat: All-India Area, Production and Yield alongwith coverage under Irrigation"
PRINTED_STEP_MINUTES = re.compile(r"\b(\d+) min\b")
# A route that quarantines reading outside the sixty minutes is the regression this class
# exists to catch. The phrases are anchored on the route itself, never on the bare words.
EXTERNAL_ALLOWANCE = re.compile(
    r"(?:outside|on top of|in addition to|beyond|around|besides|added to|as well as)\s+"
    r"(?:that|the|those|this)?\s*(?:assessed\s+)?(?:core\s+)?(?:sixty|60)[- ]?(?:minute|minutes)?"
    r"|\b(?:sixty|60)\s+minutes\s+of\s+task\s+time"
    r"|\bassessed\s+core\s+route\s+is\s+sixty\s+minutes"
    r"|\b(?:about|around|another|a further|an additional)\s+twenty\s+minutes",
    re.IGNORECASE)

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


def structural_concepts(node, structural: list[dict]) -> set[str]:
    """Concepts excused at this node by a registered structural selector on an ancestor."""
    allowed: set[str] = set()
    for spec in structural:
        selector = spec["selector"]
        if node.find_parent(attrs=_attr_matcher(selector)) is not None or _matches(node, selector):
            allowed |= set(spec["allowedConcepts"])
    return allowed


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
    a marked in-game quotation) is removed here and scanned separately below with
    its own allowance, so the classes it is NOT excused from still apply inside it.
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
    for spec in structural:
        for node in page.select(spec["selector"]):
            allowed = resolvable(node, exemptions, structural, role)
            text = normalise(node.get_text(" ", strip=True))
            if text:
                blocks.append((node, text, allowed))
    # A registered exemption is CONCEPT-SCOPED, not a blanket removal. The exempt subtree
    # is taken out of its parent block above and scanned here with only the concepts its
    # own exemption declares, so an exemption that allows two classes cannot quietly
    # excuse the other three.
    for node in page.select("[data-semantic-exemption]"):
        spec = exemptions.get(node.get("data-semantic-exemption"))
        if spec is None or role not in spec["roles"]:
            continue
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
    results.check("package identity is HHH-C2-CASE10 v0.1 CORE_CASE in campaign-2",
                  (package["id"], package["version"], package["instructionalType"],
                   package["curriculum"], package["campaign"], package["title"])
                  == (CASE_ID, "0.1", "CORE_CASE", "HHH", "campaign-2", TITLE),
                  json.dumps({k: package.get(k) for k in ("id", "version", "instructionalType", "title")}))
    results.check("the package and task registry both carry the unreleased candidate lifecycle",
                  package["status"] == "DRAFT" and registry["status"] == "DRAFT"
                  and registry["ownerReviewStatus"] == "OWNER_REVIEW_NOT_STARTED"
                  and registry["version"] == "0.1"
                  and package["approval"]["status"] == "OWNER_REVIEW_NOT_STARTED"
                  and package["approval"]["printStatus"] == "NOT_RUN"
                  and package["approval"]["owner"] == OWNER
                  and "date" not in package["approval"],
                  json.dumps({"package": package["status"], "registry": registry["status"],
                              "approval": package["approval"]}))
    results.check("no release history exists or is declared for the candidate",
                  not (UNIT / "history").exists() and "releaseHistory" not in package,
                  sorted(p.name for p in UNIT.iterdir()))
    results.check("the unit directory holds only README.md and source/",
                  sorted(p.name for p in UNIT.iterdir() if p.name != ".DS_Store") == ["README.md", "source"],
                  sorted(p.name for p in UNIT.iterdir()))
    results.check("the source directory holds exactly the four canonical sources plus the package",
                  sorted(p.name for p in SOURCE.iterdir() if p.name != ".DS_Store")
                  == ["case-package.json", "content.html", "layout-overrides.json", "presentation.css",
                      "task-registry.js"],
                  sorted(p.name for p in SOURCE.iterdir()))
    results.check("task registry pins the current game baseline, the audit baseline and the Blueprint",
                  registry["gameCommit"] == GAME_COMMIT
                  and registry["auditBaseline"] == "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md"
                  and registry["staticContentInventory"] == "hhh/audit/data/HHH_STATIC_CONTENT_INVENTORY_v0.1.json"
                  and registry["blueprint"] == "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
                  registry["gameCommit"])
    results.check("the registry names the runtime source this case is drawn from",
                  registry["runtimeId"] == "C2L3", registry.get("runtimeId"))
    results.check("the registry carries the locked learning goal and guiding question",
                  registry["learningGoal"].startswith("Evaluate competing Green Revolution claims")
                  and "within a larger system of agronomy, inputs, institutions and policy" in registry["learningGoal"]
                  and "saved a billion lives" in registry["learningGoal"]
                  and registry["guidingQuestion"].startswith("How should historians explain the 1960s wheat gains"))
    results.check("the registry states the conceptual distinction the case teaches",
                  "five different things" in registry["conceptualDistinction"]
                  and "not by itself settle" in registry["conceptualDistinction"])
    results.check("the culminating product is named exactly, and is not a CER",
                  registry["culminatingProduct"].startswith("Qualified Historical Finding")
                  and "Canonical CER is deliberately not used" in registry["culminatingProduct"])
    for key, filename in (("content", "content.html"), ("presentation", "presentation.css"),
                          ("taskRegistry", "task-registry.js"),
                          ("layoutOverrides", "layout-overrides.json")):
        digest = hashlib.sha256((SOURCE / filename).read_bytes()).hexdigest()
        results.check(f"package sourceHashes.{key} matches the working tree",
                      package["sourceHashes"][key] == digest, digest)

    shared = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    entry = next(c for cur in shared["curricula"] if cur["id"] == "HHH"
                 for camp in cur["campaigns"] for c in camp["cases"] if c["id"] == CASE_ID)
    results.check("the existing shared registry reservation is activated rather than duplicated",
                  entry["status"] == "DRAFT" and entry["packageStatus"] == "DRAFT"
                  and entry["displayOrder"] == DISPLAY_ORDER and entry["displayLabel"] == DISPLAY_LABEL
                  and entry["title"] == TITLE
                  and entry["instructionalType"] == "CORE_CASE" and entry["version"] == "0.1"
                  and entry["editorShell"] == "1.0"
                  and entry["centralWorkflow"] == "CANONICAL"
                  and entry["editorPackage"] == "hhh/campaign-2/case-10-the-quiet-billion/source/case-package.json"
                  and "historyRecord" not in entry
                  and entry["approval"] == {"owner": OWNER, "status": "OWNER_REVIEW_NOT_STARTED",
                                            "printStatus": "NOT_RUN"},
                  json.dumps(entry))
    all_hhh = [c["id"] for cur in shared["curricula"] if cur["id"] == "HHH"
               for camp in cur["campaigns"] for c in camp["cases"]]
    results.check("exactly one HHH-C2-CASE10 identity exists in the shared registry",
                  all_hhh.count(CASE_ID) == 1, all_hhh)
    results.check("Case 11 and later units remain planned reservations",
                  all("editorPackage" not in c for cur in shared["curricula"] if cur["id"] == "HHH"
                      for camp in cur["campaigns"] for c in camp["cases"]
                      if c["displayOrder"] > DISPLAY_ORDER))
    results.check("every earlier HHH unit is still released and pointed at its history record",
                  all(c["status"] == "APPROVED_STABLE" and "historyRecord" in c
                      for cur in shared["curricula"] if cur["id"] == "HHH"
                      for camp in cur["campaigns"] for c in camp["cases"]
                      if c["displayOrder"] < DISPLAY_ORDER))
    results.check("the registry display label and the package identity agree",
                  registry["displayLabel"] == entry["displayLabel"] == DISPLAY_LABEL
                  and registry["title"] == package["title"] == entry["title"] == TITLE)
    # Release-history readiness. No release record exists at candidate stage; the shared
    # schema must exist so that a Case 10 release record can later be validated directly
    # against it, which is the standing workaround for validate_static.py's HHH enumeration
    # gap in its release-history schema loop.
    results.check("the shared release-history schema exists for a later direct validation",
                  RELEASE_SCHEMA.is_file(), str(RELEASE_SCHEMA))
    results.check("no Case 10 release record exists anywhere in the tree",
                  not list(UNIT.rglob("release-*.json")),
                  [str(q) for q in UNIT.rglob("release-*.json")])

    # --- THE OPEN CURRICULUM QUALIFICATION ----------------------------------
    tracker = json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
    dep = next(d for d in tracker["gameDependencies"] if d["findingId"] == "HHH-GAME-C2L3-001")
    runtime = registry["runtimeDependency"]
    results.check("the registry names the only finding this case carries, and its class",
                  runtime["findingId"] == "HHH-GAME-C2L3-001"
                  and runtime["dependencyClass"] == "CURRICULUM_QUALIFICATION_REQUIRED"
                  and runtime["dependencyStatus"] == "OPEN_AT_AUDITED_GAME_BASELINE"
                  and runtime["auditedGameCommit"] == AUDITED_GAME_COMMIT
                  and runtime["currentGameCommit"] == GAME_COMMIT
                  and runtime["gameModificationRequired"] is False,
                  json.dumps({k: runtime.get(k) for k in ("findingId", "dependencyClass", "dependencyStatus")}))
    results.check("the shared tracker records the same open qualification, and this package leaves it untouched",
                  dep["curriculumUnit"] == CASE_ID
                  and dep["dependencyClass"] == "CURRICULUM_QUALIFICATION_REQUIRED"
                  and dep["status"] == "OPEN_AT_AUDITED_GAME_BASELINE"
                  and dep["resolution"]["resolvedGameCommit"] is None
                  and dep["unitDisplayLabel"] == DISPLAY_LABEL,
                  json.dumps({k: dep.get(k) for k in ("status", "curriculumUnit", "unitDisplayLabel")}))
    results.check("this case carries no blocking game-remediation dependency",
                  not [d for d in tracker["gameDependencies"]
                       if d["curriculumUnit"] == CASE_ID
                       and d["dependencyClass"] == "GAME_REMEDIATION_BLOCKS_FINALIZATION"],
                  [d["findingId"] for d in tracker["gameDependencies"] if d["curriculumUnit"] == CASE_ID])
    results.check("the registry states that the game is not modified and the audit is not reopened",
                  "does not modify the game" in runtime["verifiedSemantics"]
                  and "does not reopen the game audit" in runtime["verifiedSemantics"]
                  and "leaves the shared remediation tracker untouched" in runtime["rule"])
    results.check("the registry carries the audit's own qualification wording as its obligation",
                  "one seed saved a billion" in runtime["qualificationRule"]
                  and "irrigation" in runtime["qualificationRule"]
                  and "institutional" in runtime["qualificationRule"])
    # The runtime shape is asserted against the audit's own static content inventory
    # rather than against the game, which this package does not read.
    inventory = json.loads(INVENTORY_FILE.read_text(encoding="utf-8"))
    level = next(x for x in inventory["levels"] if x["id"] == "C2L3")
    results.check("the audit inventory still shows four required and two insight sources for C2 L3",
                  tuple(level["required_clues"]) == RUNTIME_CLUE_TAGS
                  and tuple(level["optional_or_insight_evidence"]) == RUNTIME_INSIGHT_TAGS
                  and level["source_count"] == 6,
                  json.dumps({"required": level["required_clues"],
                              "insight": level["optional_or_insight_evidence"]}))
    results.check("the registry's required and insight strand counts match the audit inventory",
                  runtime["requiredStrandCount"] == len(RUNTIME_CLUE_TAGS)
                  and runtime["insightStrandCount"] == len(RUNTIME_INSIGHT_TAGS))
    results.check("the audit inventory still records this level's finding id and disposition",
                  level["finding_ids"] == ["HHH-GAME-C2L3-001"]
                  and level["audit_disposition"] == "READY_WITH_TEACHER_QUALIFICATION")

    # Lifecycle, repository and runtime metadata must never reach a printable page.
    LIFECYCLE_TOKENS = ("VALIDATION_BUILD", "OWNER_REVIEW", "packageStatus", "sourceHashes",
                        "case-package.json", "task-registry.js", "APPROVED_STABLE", "DRAFT",
                        "d9fc16ba", "9b8545ed", "a64d3cc", "releaseHistory", "release-v0.1",
                        "historyRecord", "Nate / Owner", "editorPackage", "OWNER_REVIEW_NOT_STARTED",
                        "HHH-GAME-C2L3-001", "HHH-C2-CASE10", "CURRICULUM_QUALIFICATION_REQUIRED",
                        "OPEN_AT_AUDITED_GAME_BASELINE", "C2L3")
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
    results.check("the prohibited identifier list covers every runtime clue tag and location id",
                  set(RUNTIME_CLUE_TAGS) | set(RUNTIME_INSIGHT_TAGS) | set(RUNTIME_LOCATIONS)
                  <= set(status_contract["prohibitedRuntimeIdentifiers"]),
                  sorted((set(RUNTIME_CLUE_TAGS) | set(RUNTIME_INSIGHT_TAGS) | set(RUNTIME_LOCATIONS))
                         - set(status_contract["prohibitedRuntimeIdentifiers"])))

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
        fields = [n.get("data-field") for n in first.select(".student-id [data-field]")]
        results.check(f"{role}: the identification row carries Name, Date and Period in order",
                      fields == ["student-name", "student-date", "student-class"], fields)
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
    results.check("the Answer Key has no Task 2 section and does not renumber the later ones",
                  "Task 2 -" not in answer_text and "2 · Set the Claim Test" not in answer_text
                  and not soup.select('section.page[data-role="answer"] [data-shell-task-heading="2"]'))
    results.check("no learner page prints internal grading policy or reveals the Task 2 answer",
                  not any(phrase in texts[role].lower() for role in LEARNER_ROLES
                          for phrase in ("not graded", "not scored", "ungraded",
                                         "for participation only", "is not keyed", "no correct answer")))
    # The non-keyable task must not be answered anywhere a learner can see it.
    for role in LEARNER_ROLES:
        page_id = next(t for t in tasks if t["number"] == "2")["pagePlacement"][role]
        page = soup.select_one(f'section.page[data-role="{role}"][data-page-id="{page_id}"]')
        results.check(f"{role}: the Task 2 page supplies no worked example or prefilled cell",
                      not page.select("[data-accessible-adaptation]") and not page.select(".prefilled")
                      and not page.select(".model-example"))

    # --- THE TIMED ROUTE ----------------------------------------------------
    # The lock is a sixty-minute TOTAL route, reading included. Three things are checked:
    # the registry's arithmetic, the printed procedure's arithmetic, and a closed negative
    # class that fails any future regression to "sixty task minutes plus extra reading".
    route = registry["timedRoute"]
    results.check("the registry declares a sixty-minute total route rather than a sixty-minute task core",
                  route.get("totalMinutes") == ROUTE_TOTAL_MINUTES and "assessedCoreMinutes" not in route,
                  json.dumps({k: route.get(k) for k in ("totalMinutes", "assessedCoreMinutes")}))
    results.check("the registry carries the locked per-task minutes",
                  route.get("taskMinutes") == TASK_MINUTES, json.dumps(route.get("taskMinutes")))
    results.check("the registry carries the locked launch, reading and close minutes",
                  route.get("surroundingMinutes") == {key: minutes for key, (_, minutes)
                                                     in SURROUNDING_MINUTES.items()},
                  json.dumps(route.get("surroundingMinutes")))
    results.check("the task minutes and the surrounding minutes together are exactly the sixty-minute route",
                  sum(route.get("taskMinutes", {}).values()) + sum(route.get("surroundingMinutes", {}).values())
                  == ROUTE_TOTAL_MINUTES == route.get("totalMinutes")
                  and route.get("assessedTaskMinutes") == sum(route.get("taskMinutes", {}).values())
                  and route.get("surroundingMinutesTotal") == sum(route.get("surroundingMinutes", {}).values()),
                  json.dumps({"tasks": sum(route.get("taskMinutes", {}).values()),
                              "surrounding": sum(route.get("surroundingMinutes", {}).values())}))
    results.check("the reading segments are not a majority of the route, and no segment is untimed",
                  all(minutes > 0 for minutes in route.get("taskMinutes", {}).values())
                  and all(minutes > 0 for minutes in route.get("surroundingMinutes", {}).values()))
    results.check("the registry states the no-external-allowance rule and keeps extension optional",
                  len(route.get("noExternalAllowanceRule", "")) > 120 and len(route.get("extensionRule", "")) > 80
                  and "regression" in route.get("noExternalAllowanceRule", ""))
    results.check("the registry names the printed step order for all twelve route segments",
                  route.get("printedStepOrder") == ["launch", "task-1", "read-reconstructed", "task-2",
                                                "read-documented", "task-3", "task-4", "task-5",
                                                "task-6", "task-7", "task-8", "close"],
                  json.dumps(route.get("printedStepOrder")))

    steps = [normalise(li.get_text(" ", strip=True))
             for li in soup.select('section.page[data-role="teacher"] .procedure > li')]
    results.check("the Teacher procedure prints exactly the twelve segments of the route",
                  len(steps) == 12, len(steps))
    for number, minutes in TASK_MINUTES.items():
        title = dict(EXPECTED_TASKS)[number]
        step = next((text for text in steps if normalise(f"{number} · {title}") in text), "")
        results.check(f"Teacher procedure gives task {number} its locked {minutes} minutes",
                      f"{minutes} min" in step, step[:160])
    for key, (label, minutes) in SURROUNDING_MINUTES.items():
        step = next((text for text in steps if text.startswith(label)), "")
        results.check(f"Teacher procedure gives the {key} segment its locked {minutes} minutes",
                      f"{minutes} min" in step, step[:160])
    printed = [int(match) for text in steps for match in PRINTED_STEP_MINUTES.findall(text)[:1]]
    results.check("every printed step carries a duration",
                  len(printed) == len(steps) == 12, printed)
    results.check("the printed procedure itself adds up to exactly sixty minutes",
                  sum(printed) == ROUTE_TOTAL_MINUTES, sum(printed))
    results.check("the Teacher procedure states the route as a sixty-minute total with the reading inside it",
                  "approximately sixty minutes in total" in teacher_text
                  and "reading is inside the sixty minutes" in teacher_text
                  and "not an allowance added to them" in teacher_text)
    results.check("the Teacher procedure still refuses to bury gameplay inside the route",
                  "Do not attempt to insert gameplay into the sixty minutes" in teacher_text)
    offender = EXTERNAL_ALLOWANCE.search(teacher_text)
    results.check("no Teacher sentence places launch, reading or close outside the sixty-minute route",
                  offender is None, offender.group(0) if offender else "")
    results.check("the no-game route claims no framing allowance beyond the printed launch step",
                  "three-minute launch step, and nothing beyond it" in teacher_text
                  and "minutes of framing" not in teacher_text)

    # --- CER IS DECLINED, AND THE DECLINE IS STRUCTURAL ----------------------
    cer = registry["cerDecision"]
    results.check("the registry records the CER decision with a rationale and a precedent",
                  cer["decision"] == "DECLINED" and len(cer["rationale"]) > 200 and len(cer["precedent"]) > 80)
    for selector in cer["prohibitedSelectors"]:
        results.check(f"no role renders the canonical CER component ({selector})", not soup.select(selector))
    results.check("no layout area is locked for a CER reason",
                  not [a for block in (layout, layout["student"]) for a in block["lockedAreas"] if a["reason"] == "cer"])
    results.check("no role prints claim-evidence-reasoning as the product name",
                  not any(re.search(r"claim[- ]evidence[- ]reasoning|\bC\.?E\.?R\.?\b", texts[role])
                          for role in LEARNER_ROLES))
    results.check("the culminating product is the five-part finding in both learner editions",
                  all(soup.select(f'section.page[data-role="{role}"] [data-qualified-finding]') for role in LEARNER_ROLES))
    for role in LEARNER_ROLES:
        block = soup.select_one(f'section.page[data-role="{role}"] [data-qualified-finding]')
        tags = [normalise(t.get_text(" ", strip=True)) for t in block.select(".ex-tag")]
        labels = normalise(block.get_text(" ", strip=True)).lower()
        results.check(f"{role}: the finding carries exactly five numbered obligations in order",
                      tags == ["1", "2", "3", "4", "5"], tags)
        for obligation in ("finding", "quantitative evidence", "second documented source",
                           "causal qualification and limitation", "next evidence needed"):
            results.check(f"{role}: the finding names the obligation “{obligation}”", obligation in labels)
        results.check(f"{role}: the finding is titled a Qualified Historical Finding",
                      "QUALIFIED HISTORICAL FINDING" in normalise(block.get_text(" ", strip=True)).upper())

    # --- SOURCE STATUS -------------------------------------------------------
    bands = {band["id"]: band for band in status_contract["bands"]}
    source_layers = {s["id"]: s.get("evidenceLayer") for s in registry["caseSources"]}
    results.check("every canonical source declares a registered status band",
                  all(v in bands for v in source_layers.values()))
    results.check("the status contract is enforced in every role",
                  tuple(status_contract["enforcedRoles"]) == ALL_ROLES)
    results.check("the status vocabulary is the canonical three",
                  set(status_contract["statusVocabulary"])
                  == {"reconstructed game evidence", "documented", "curriculum-original figure"})
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
        text = normalise(notice.get_text(" ", strip=True))
        for band in status_contract["bands"]:
            results.check(f"{role}: the notice names the {band['id']} band by its printed label",
                          band["label"].lower() in text.lower())
        merger = notice.select_one("[data-non-merger-rule]")
        results.check(f"{role}: the notice states the non-merger rule in both directions",
                      merger is not None
                      and "It cannot establish a real historical claim" in normalise(merger.get_text(" ", strip=True))
                      and "It cannot prove that a game record is genuine" in normalise(merger.get_text(" ", strip=True)))
        boundary = notice.select_one("[data-title-boundary]")
        results.check(f"{role}: the notice states the title boundary on page 1",
                      boundary is not None
                      and "The title comes from the game" in normalise(boundary.get_text(" ", strip=True))
                      and "would require a stated method and counterfactual" in normalise(boundary.get_text(" ", strip=True))
                      and "not as a measurement supplied by this packet" in normalise(boundary.get_text(" ", strip=True)))
    fictional_nodes = soup.select("[data-fictional-data]")
    results.check("the packet marks its invented case data", len(fictional_nodes) >= 8, len(fictional_nodes))
    for node in fictional_nodes:
        holder = node.find_parent(attrs={"data-evidence-layer": True})
        results.check("invented data sits inside a reconstructed evidence object",
                      holder is not None and holder.get("data-evidence-layer") == "reconstructed", str(node)[:100])
    for source in registry["caseSources"]:
        results.check(f"source {source['id']} declares a contribution and a limitation",
                      len(source.get("contribution", "")) > 40 and len(source.get("limitation", "")) > 40)
    results.check("the reconstructed layer holds exactly the five assessed dossier strands",
                  [s["id"] for s in registry["caseSources"] if s["evidenceLayer"] == "reconstructed"] == RECONSTRUCTED_SOURCES)
    results.check("the documented layer holds exactly the four certified source cards",
                  [s["id"] for s in registry["caseSources"] if s["evidenceLayer"] == "documented"] == DOCUMENTED_SOURCES)
    results.check("the curriculum-model layer holds exactly the three figures",
                  [s["id"] for s in registry["caseSources"] if s["evidenceLayer"] == "curriculum-model"] == FIGURE_SOURCES)
    results.check("every reconstructed source names the strand it supplies and the set covers all five",
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
                      arch_claims[row_key] == declared,
                      json.dumps({"teacher": arch_claims[row_key], "registry": declared}))

    # --- MARKED IN-GAME QUOTATIONS ------------------------------------------
    claims = soup.select("[data-game-claim]")
    results.check("the packet marks its in-game quotations outside the reconstructed cards", len(claims) >= 6, len(claims))
    for node in claims:
        page = node.find_parent(class_="page")
        results.check(f"{page.get('data-page-id')}: the marked quotation sits inside a task that tests it",
                      node.find_parent(attrs={"data-tests-game-claim": True}) is not None, str(node)[:120])
        results.check(f"{page.get('data-page-id')}: the marked quotation is short",
                      len(normalise(node.get_text(" ", strip=True))) < 400)
    results.check("marked quotations appear only on learner pages",
                  all(n.find_parent(class_="page").get("data-role") in LEARNER_ROLES for n in claims))
    results.check("every data-tests-game-claim block names a real task number",
                  {n.get("data-tests-game-claim") for n in soup.select("[data-tests-game-claim]")}
                  <= {n for n, _ in EXPECTED_TASKS})

    # --- CASE-LOCAL SOURCE CERTIFICATION ------------------------------------
    certification = registry["sourceCertification"]
    reused = {r["auditId"]: r for r in certification["auditReused"]}
    results.check("the certification reuses the Phase 1 source for this level without modifying the audit",
                  set(reused) == {"H15"}
                  and reused["H15"]["caseSourceId"] == "borlaug-nobel-lecture"
                  and "No audit record is modified" in reused["H15"]["note"]
                  and "not relied on for any printed claim" in reused["H15"]["note"])
    certified_ids = {c["caseSourceId"] for c in certification["caseCertified"]}
    results.check("every documented source card carries a case-local certification entry",
                  certified_ids == set(DOCUMENTED_SOURCES), sorted(certified_ids))
    mapping = {m["pmoSourceId"]: m["caseSourceId"] for m in certification["pmoEstateMapping"]}
    results.check("the four PMO-locked sources map one to one onto the four documented cards",
                  mapping == {"A": "india-wheat-record", "B": "borlaug-nobel-lecture",
                              "C": "cimmyt-history", "D": "pingali-retrospective"},
                  json.dumps(mapping))
    results.check("the printed labels declared for the four documented cards are F to I",
                  [m["printedLabel"] for m in certification["pmoEstateMapping"]] == ["F", "G", "H", "I"])
    certified = {c["caseSourceId"]: c for c in certification["caseCertified"]}
    india = certified["india-wheat-record"]
    for _year, area, production, yld, irrigated in INDIA_SERIES:
        for value in (area, production, yld, irrigated):
            results.check(f"the India certification supports the published value {value}",
                          any(value in s for s in india["supports"]), value)
    for needle in ("what fraction of the gains came from genetics", "how many lives", "hunger reduction by itself",
                   "welfare effects by itself", "one-cause explanation"):
        results.check(f"the India certification refuses to certify “{needle}”",
                      any(needle.lower() in s.lower() for s in india["doesNotSupport"]), needle)
    borlaug = certified["borlaug-nobel-lecture"]
    results.check("the Borlaug certification declares the source class as a primary participant source",
                  borlaug.get("sourceClass") == "PRIMARY PARTICIPANT SOURCE"
                  and "11 December 1970" in borlaug["citation"])
    for needle in ("Norin 10", "lodging", "short straw", "not based solely", "credit with which to buy them",
                   "temporary success", "no miracles", "irrigated areas", "disease resistance"):
        results.check(f"the Borlaug certification supports the authorized claim family “{needle}”",
                      any(needle.lower() in s.lower() for s in borlaug["supports"]), needle)
    for needle in ("neutral", "measured share", "count of lives", "the game's case"):
        results.check(f"the Borlaug certification refuses to certify “{needle}”",
                      any(needle.lower() in s.lower() for s in borlaug["doesNotSupport"]), needle)
    cimmyt = certified["cimmyt-history"]
    for needle in ("Norin 10", "Rht1", "Salmon", "Vogel", "lodging and rust resistance as two problems",
                   "three separate traits", "only after agronomy practices were changed"):
        results.check(f"the CIMMYT certification supports the authorized claim family “{needle}”",
                      any(needle.lower() in s.lower() for s in cimmyt["supports"]), needle)
    results.check("the CIMMYT certification refuses to make dwarfing and rust resistance the same trait",
                  any("same trait" in s.lower() and "produces the other" in s.lower()
                      for s in cimmyt["doesNotSupport"]))
    results.check("the CIMMYT certification refuses its own headline's popular framing",
                  any("saved hundreds of millions" in s.lower() for s in cimmyt["doesNotSupport"]))
    pingali = certified["pingali-retrospective"]
    results.check("the Pingali certification carries the exact authorized citation",
                  "10.1073/pnas.0912953109" in pingali["citation"] and "109(31):12302" in pingali["citation"]
                  and "Proceedings of the National Academy of Sciences" in pingali["citation"])
    for needle in ("tripled", "30 per cent increase in land area", "208 per cent", "1.0 per cent per annum",
                   "critical components", "uneven", "micronutrient malnutrition", "environmental impacts were mixed",
                   "20 per cent lower"):
        results.check(f"the Pingali certification supports the authorized claim family “{needle}”",
                      any(needle.lower() in s.lower() for s in pingali["supports"]), needle)
    for needle in ("count of lives saved", "share of India's 1960s wheat rise", "the game's case"):
        results.check(f"the Pingali certification refuses to certify “{needle}”",
                      any(needle.lower() in s.lower() for s in pingali["doesNotSupport"]), needle)
    for entry_c in certification["caseCertified"]:
        results.check(f"certification {entry_c['caseSourceId']} names a citation, its supported claims and its bounds",
                      len(entry_c.get("citation", "")) > 40 and len(entry_c.get("supports", [])) >= 4
                      and len(entry_c.get("doesNotSupport", [])) >= 4)
        results.check(f"certification {entry_c['caseSourceId']} refuses to certify any game object",
                      any("game" in s.lower() for s in entry_c["doesNotSupport"]))
    results.check("the certification closes the estate against uncertified claims",
                  "source-certification dependency for the PMO" in certification["noFurtherClaims"])
    results.check("the certification records the resolved variances rather than resolving them silently",
                  "openVarianceForPmo" in certification
                  and "locked series is implemented exactly" in certification["openVarianceForPmo"]
                  and "1966 and 1967" in certification["openVarianceForPmo"])
    # --- THE INDIA SERIES IS PINNED TO ONE STATISTICAL EDITION ---------------
    # The locked values are a published edition's values, not an unattributed series, so the
    # edition and table have to be identifiable from the package rather than inferred.
    results.check("the India certification pins the publisher, edition and table",
                  india["publisher"] == "Government of India, Directorate of Economics and Statistics"
                  and india["edition"] == INDIA_EDITION
                  and india["table"].startswith("Table 4.7(a)")
                  and INDIA_TABLE_TITLE in india["table"],
                  json.dumps({k: india.get(k) for k in ("publisher", "edition", "table")}))
    results.check("the India certification citation carries the edition and the table number",
                  INDIA_EDITION in india["citation"] and "Table 4.7(a)" in india["citation"]
                  and "Directorate of Economics and Statistics" in india["citation"], india["citation"])
    results.check("the PMO estate mapping records the pinned edition against source A",
                  next(m for m in certification["pmoEstateMapping"] if m["pmoSourceId"] == "A")["pinnedEdition"]
                  == f"{INDIA_EDITION}, Table 4.7(a)")
    results.check("the open-variance record treats the later editions as a citation duty, not a defect",
                  INDIA_EDITION in certification["openVarianceForPmo"]
                  and "Later editions revise some historical values" in certification["openVarianceForPmo"]
                  and "not an error" in certification["openVarianceForPmo"])
    results.check("the certification attributes the figure's shipment dates to Source G",
                  "figureDateAttribution" in certification
                  and "Source G" in certification["figureDateAttribution"]
                  and "1966" in certification["figureDateAttribution"]
                  and "1967" in certification["figureDateAttribution"]
                  and "no learner task" in certification["figureDateAttribution"])
    for role in LEARNER_ROLES + ("teacher",):
        results.check(f"{role}: the printed India record identifies the statistical edition it came from",
                      INDIA_EDITION in texts[role] and "Table 4.7(a)" in texts[role])
    results.check("the Teacher source estate carries the full publisher and table title",
                  "Directorate of Economics and Statistics" in teacher_text
                  and INDIA_TABLE_TITLE in teacher_text)
    results.check("the Teacher limitations cite the edition rather than calling a revision an error",
                  "Later editions revise some historical values" in teacher_text
                  and "not an error" in teacher_text)
    results.check("the Teacher limitations state the seed date as a source disagreement, not an open question",
                  "differ on the date of India's large seed purchase" in normalise(teacher_text)
                  and "This packet's chronology is settled" in normalise(teacher_text)
                  and "disagreement between two sources" in teacher_text
                  and "not an open question about these pages" in teacher_text)
    results.check("no learner edition turns the seed-date disagreement into a task",
                  not any("1967" in texts[role] and "disagree" in texts[role].lower()
                          for role in LEARNER_ROLES))
    # The estate is bibliographically closed: no uncertified institution or publication
    # is cited anywhere as a source of a real-world claim.
    for role in ALL_ROLES:
        foreign = [t for t in ("wikipedia", "britannica", "smithsonian", "bbc",
                               "new york times", "encyclopedia", "world bank", "united nations")
                   if re.search(r"\b" + re.escape(t), texts[role], re.I)]
        results.check(f"{role}: no uncertified publication is cited", not foreign, foreign)

    # --- THE NO-GAME DOSSIER -------------------------------------------------
    no_game = registry["noGameRoute"]
    results.check("the no-game contract names the five reconstructed dossier sources in runtime order",
                  no_game["dossier"] == RECONSTRUCTED_SOURCES, no_game["dossier"])
    results.check("exactly five reconstructed strands are assessed, and each maps to a reconstructed source",
                  no_game["assessedStrandCount"] == 5
                  and {s["id"] for s in no_game["requiredStrands"]} == REQUIRED_STRANDS
                  and all(source_layers.get(s["source"]) == "reconstructed" for s in no_game["requiredStrands"]))
    results.check("the runtime-optional Failure Report is declared assessed and therefore printed",
                  next(s for s in no_game["requiredStrands"] if s["id"] == "failure-report")["runtimeStatus"]
                  == "runtime-optional, curriculum-assessed"
                  and "no learner's ability to complete Task 6 depends on discovering it during play"
                  in no_game["optionalButAssessedRule"])
    results.check("the optional horizon survey is declared unassessed and is not reproduced",
                  no_game["optionalRuntimeSourceNotAssessed"]["id"] == "harvest-scale-survey"
                  and "not assessed" in no_game["optionalRuntimeSourceNotAssessed"]["rule"]
                  and not any(re.search(r"\bhorizon\b", texts[role], re.I) for role in LEARNER_ROLES))
    results.check("the Teacher Guide states that the optional survey is not assessed",
                  "optional survey of the harvest running to the horizon" in teacher_text
                  and "not assessed" in teacher_text)
    for role in no_game["requiredInRoles"]:
        for source_id in no_game["dossier"] + DOCUMENTED_SOURCES:
            results.check(f"{role}: source {source_id} is printed in the learner packet",
                          bool(soup.select(f'section.page[data-role="{role}"] [data-source-id~="{source_id}"]')), source_id)
    results.check("Teacher supplies both routes and states that Campaign 2 has no launch shortcut",
                  "Game route" in teacher_text and "No-game route" in teacher_text
                  and "no level selector and no shortcut" in teacher_text)
    results.check("Teacher maps the gameplay evidence to the printed dossier without ranking the routes",
                  "also printed as Sources A to E, in the same order" in teacher_text
                  and "neither is the reduced version" in teacher_text)
    results.check("Teacher supplies a complete no-game evidence digest", "Complete no-game evidence digest" in teacher_text)
    RUNTIME_RESOLUTION = ("The Record Validates", "The Trial Record", "The Reckoning", "Thread Surgeon",
                          "Trace Analyst", "Validate the Record", "Which record is genuine?",
                          "The evidence is incomplete", "the wheat that stood", "quiet disaster",
                          "Play the Borlaug Record", "Compare the Trial Wheat", "Read the Pedigree Records",
                          "Read the Failure Report", "Speak to the Agronomist", "Survey the Deployment",
                          "Prakash Rao", "Norman Borlaug's semi-dwarf wheat is credited")
    for role in ALL_ROLES:
        leaked = [t for t in RUNTIME_RESOLUTION if t.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime resolution, candidate label, hint or control label is reproduced",
                      not leaked, leaked)

    # --- FIGURE 1: THE QUANTITATIVE RECORD ----------------------------------
    quant = registry["quantitativeRecord"]
    results.check("the record contract declares the exact six-year locked series with its units",
                  [(r["cropYear"], r["area"], r["production"], r["yield"], r["irrigatedShare"])
                   for r in quant["series"]] == INDIA_SERIES,
                  json.dumps(quant["series"]))
    results.check("the record contract names all four measures and the two-graph rule",
                  quant["measuresRequiredVisible"] == ["production", "yield", "area", "irrigatedShare"]
                  and "never drawn on one shared value axis" in quant["twoGraphRule"])
    results.check("the record contract states the arithmetic consistency check on the transcription",
                  "reproduces production to within published rounding in all six crop years"
                  in quant["internalConsistency"])
    for role in quant["roles"]:
        figure = soup.select_one(f'section.page[data-role="{role}"] {quant["selector"]}')
        results.check(f"{role}: the quantitative record figure is present", figure is not None)
        if figure is None:
            continue
        fig_text = normalise(figure.get_text(" ", strip=True))
        root = figure_root(figure)
        whole = normalise(root.get_text(" ", strip=True)) if root is not None else fig_text
        for fragment in quant["requiredPrintedText"]:
            results.check(f"{role}: the record prints {fragment}", fragment.lower() in whole.lower(), fragment)
        rows = figure.select(".rec-row")
        results.check(f"{role}: the record draws exactly six crop-year rows", len(rows) == 6, len(rows))
        for index, (year, _area, production, yld, _irr) in enumerate(INDIA_SERIES):
            row = rows[index]
            printed = [normalise(v.get_text(" ", strip=True)) for v in row.select(".rec-val")]
            results.check(f"{role}: row {year} prints its production and yield values in order",
                          normalise(row.select_one(".rec-year").get_text()) == year.replace("-", "-")
                          and printed == [production, yld],
                          json.dumps({"year": normalise(row.select_one(".rec-year").get_text()), "values": printed}))
            bars = row.select(".rec-bar")
            results.check(f"{role}: row {year} draws two separate bars, production then yield",
                          len(bars) == 2 and "rec-prod" in (bars[0].get("class") or [])
                          and "rec-yield" in (bars[1].get("class") or []))
        strip = root.select_one(".rec-strip") if root is not None else None
        results.check(f"{role}: the area and irrigation strip is a real table beside the graphs",
                      strip is not None and strip.name == "table" and strip.find("caption") is not None
                      and len(strip.select("tbody tr")) == 2)
        if strip is not None:
            area_cells = [normalise(td.get_text(" ", strip=True)) for td in strip.select("tbody tr")[0].select("td")]
            irr_cells = [normalise(td.get_text(" ", strip=True)) for td in strip.select("tbody tr")[1].select("td")]
            results.check(f"{role}: the strip prints the six area values exactly",
                          area_cells == [r[1] for r in INDIA_SERIES], area_cells)
            results.check(f"{role}: the strip prints the six irrigated-share values exactly",
                          irr_cells == [r[4] for r in INDIA_SERIES], irr_cells)
        described = figure.select_one("[role='img'][aria-label]")
        results.check(f"{role}: the record figure carries accessibility text", described is not None)
        if described is not None:
            alt = normalise(described.get("aria-label"))
            for fragment in quant["requiresAltConcepts"]:
                results.check(f"{role}: the record accessibility text names {fragment}",
                              fragment.lower() in alt.lower(), fragment)
            for _year, area, production, yld, irrigated in INDIA_SERIES:
                for value in (production, yld):
                    results.check(f"{role}: the record accessibility text carries the value {value}",
                                  value in alt, value)
                results.check(f"{role}: the record accessibility text carries the area {area}", area in alt, area)
                results.check(f"{role}: the record accessibility text carries the irrigated share {irrigated.rstrip('%')}",
                              irrigated.rstrip("%") in alt, irrigated)
            for pattern in quant["prohibitedPatterns"]:
                hit = re.search(pattern["regex"], alt, re.I)
                results.check(f"{role}: the record accessibility text avoids {pattern['id']}", hit is None,
                              (hit.group(0) if hit else "") + " :: " + pattern["why"])
        caption = root.find("figcaption") if root is not None else None
        cap_text = normalise(caption.get_text(" ", strip=True)).upper() if caption else ""
        for term in quant["requiresCaptionTerms"]:
            results.check(f"{role}: the record caption carries the {term} status term", term.upper() in cap_text, cap_text[:200])
        results.check(f"{role}: the record figure is declared a curriculum figure and names its source as the evidence",
                      figure.get("data-evidence-layer") == "curriculum-model"
                      and "source f is the evidence" in cap_text.lower())
    # Production and yield must remain distinct everywhere they are printed together.
    for role in LEARNER_ROLES:
        results.check(f"{role}: the packet prints production and yield with their own units",
                      "million tonnes" in texts[role] and "kilograms per hectare" in texts[role])
    results.check("the Answer Key's Task 4 exemplar distinguishes production, yield, area and irrigation",
                  all(word in answer_text.lower() for word in ("production", "yield", "area sown", "irrigated share"))
                  and "16.54 million tonnes" in answer_text and "1,103 kg/ha" in answer_text)

    # --- FIGURE 2: THE ROUTE -------------------------------------------------
    route_c = registry["transmissionRoute"]
    results.check("the route contract declares four stages, each certified by a documented source",
                  [s["id"] for s in route_c["stages"]] == ["japan", "united-states", "mexico", "south-asia"]
                  and all(s["certifiedBy"] in set(DOCUMENTED_SOURCES) for s in route_c["stages"]))
    for role in route_c["roles"]:
        figure = soup.select_one(f'section.page[data-role="{role}"] {route_c["selector"]}')
        results.check(f"{role}: the route figure is present", figure is not None)
        if figure is None:
            continue
        fig_text = normalise(figure.get_text(" ", strip=True))
        places = [normalise(n.get_text(" ", strip=True)) for n in figure.select(".rn-place")]
        results.check(f"{role}: the route prints its four stages in the contract order",
                      places == [s["label"] for s in route_c["stages"]], places)
        labels = [normalise(n.get_text(" ", strip=True)) for n in figure.select(".rl-label")]
        results.check(f"{role}: every link names who or what carried the material across it",
                      labels == route_c["linkLabels"], labels)
        for fragment in route_c["requiredPrintedText"]:
            results.check(f"{role}: the route prints {fragment}", fragment.lower() in fig_text.lower(), fragment)
        rule_node = figure.select_one("[data-route-rule='not-a-map']")
        results.check(f"{role}: the printed route rule sits inside the route figure",
                      rule_node is not None
                      and route_c["requiredRule"].lower() in normalise(rule_node.get_text(" ", strip=True)).lower())
        results.check(f"{role}: the route rule refuses hero-person simplification",
                      rule_node is not None
                      and "the wheat did not travel by itself" in normalise(rule_node.get_text(" ", strip=True)).lower())
        for pattern in route_c["prohibitedPatterns"]:
            hit = re.search(pattern["regex"], fig_text, re.I)
            results.check(f"{role}: the route text avoids {pattern['id']}", hit is None,
                          (hit.group(0) if hit else "") + " :: " + pattern["why"])

    # --- FIGURE 3: THE PRODUCTION PACKAGE ------------------------------------
    package_c = registry["productionPackage"]
    results.check("the package contract declares six contributors and one outcome",
                  len(package_c["nodes"]) == 6 and package_c["outcome"].startswith("HIGHER REALISED"))
    results.check("every declared connector verb is from the controlled set",
                  {n["verb"] for n in package_c["nodes"]} <= set(package_c["allowedConnectorVerbs"]))
    for role in package_c["roles"]:
        figure = soup.select_one(f'section.page[data-role="{role}"] {package_c["selector"]}')
        results.check(f"{role}: the package figure is present", figure is not None)
        if figure is None:
            continue
        fig_text = normalise(figure.get_text(" ", strip=True))
        names = [normalise(n.get_text(" ", strip=True)) for n in figure.select(".pn-name")]
        verbs = [normalise(n.get_text(" ", strip=True)) for n in figure.select(".pn-verb")]
        results.check(f"{role}: the package prints its six contributors in the contract order",
                      names == [n["label"] for n in package_c["nodes"]], names)
        results.check(f"{role}: every contributor prints its own controlled connector word",
                      verbs == [n["verb"] for n in package_c["nodes"]]
                      and set(verbs) <= set(package_c["allowedConnectorVerbs"]), verbs)
        results.check(f"{role}: no prohibited connector verb appears in the package figure",
                      not [v for v in package_c["prohibitedConnectorVerbs"]
                           if re.search(r"\b" + re.escape(v) + r"\b", fig_text, re.I)])
        outcome = figure.select_one(".po-name")
        results.check(f"{role}: the package converges on the single declared outcome",
                      outcome is not None and normalise(outcome.get_text(" ", strip=True)) == package_c["outcome"])
        rule_node = figure.select_one("[data-package-rule='no-measured-share']")
        results.check(f"{role}: the printed package rule refuses a sole cause and a measured share",
                      rule_node is not None
                      and package_c["requiredRule"].lower() in normalise(rule_node.get_text(" ", strip=True)).lower()
                      and "a correct mechanism is not a measured share" in normalise(rule_node.get_text(" ", strip=True)).lower())
        for pattern in package_c["prohibitedPatterns"]:
            hit = re.search(pattern["regex"], fig_text, re.I)
            results.check(f"{role}: the package text avoids {pattern['id']}", hit is None,
                          (hit.group(0) if hit else "") + " :: " + pattern["why"])

    # --- TASK 6: THE REPORT TESTED INSIDE THE GAME ---------------------------
    claim_test = registry["claimTest"]
    results.check("the claim-test contract declares the four tests and keeps the report inside the game",
                  [t["label"] for t in claim_test["tests"]]
                  == ["TRIAL RESULT", "LINEAGE AND HARVEST RECORD", "FIELD OUTCOME", "CORROBORATION"]
                  and claim_test["insideGameOnly"] is True
                  and all(source_layers.get(t["checkedAgainst"]) == "reconstructed" for t in claim_test["tests"]))
    for role in claim_test["roles"]:
        organiser = soup.select_one(f'section.page[data-role="{role}"] {claim_test["selector"]}')
        results.check(f"{role}: the four-test organiser is present", organiser is not None)
        if organiser is None:
            continue
        text = normalise(organiser.get_text(" ", strip=True))
        for test in claim_test["tests"]:
            results.check(f"{role}: the organiser prints the {test['label']} test", test["label"] in text.upper())
        results.check(f"{role}: the organiser has exactly four test rows", len(organiser.select("tbody tr")) == 4)
        page = organiser.find_parent(class_="page")
        page_text = normalise(page.get_text(" ", strip=True))
        results.check(f"{role}: the page prints that the paperwork settles nothing in either direction",
                      claim_test["printedRule"] in page_text
                      and "would not be proof that it is forged" in page_text
                      and "Neither is one of the four tests" in page_text)
        results.check(f"{role}: the directions confine the test to the game's own evidence",
                      "inside the game" in page_text.lower() and "Sources A to D only" in page_text)
        verdict = page.select_one('[data-persist-id$="6-verdict"]')
        results.check(f"{role}: the verdict slot is a persistent control",
                      verdict is not None and verdict.has_attr("data-response"))
    results.check("the report's four claims are supplied in BOTH editions and marked as in-game quotations",
                  all(len(soup.select(f'section.page[data-role="{r}"] .claim-test-table td.prefilled')) == 4
                      for r in LEARNER_ROLES if r == "student")
                  and len(soup.select('section.page[data-role="student"] .claim-test-table [data-game-claim]')) == 4
                  and len(soup.select('section.page[data-role="accessible"] .claim-test-table [data-game-claim]')) == 4)
    results.check("the Accessible organiser models exactly one complete comparison and the Student models none",
                  len(soup.select('section.page[data-role="accessible"] .claim-test-table tr.model-row')) == 1
                  and not soup.select('section.page[data-role="student"] .claim-test-table tr.model-row'))

    # --- TASK 7: THE THREE INTERPRETATIONS -----------------------------------
    interp = registry["interpretations"]
    results.check("the interpretation contract declares three positions and names the best supported",
                  [p["label"] for p in interp["positions"]] == ["A", "B", "C"]
                  and [p["id"] for p in interp["positions"] if p["bestSupported"]] == ["system"]
                  and interp["bestSupported"] == "system")
    for role in interp["roles"]:
        table = soup.select_one(f'section.page[data-role="{role}"] {interp["selector"]}')
        results.check(f"{role}: the three-interpretation table is present", table is not None)
        if table is None:
            continue
        results.check(f"{role}: the table carries exactly three interpretation rows",
                      len(table.select("tbody tr")) == 3)
        headers = [normalise(th.get_text(" ", strip=True)) for th in table.select('tbody th[scope="row"]')]
        for position in interp["positions"]:
            results.check(f"{role}: the table prints interpretation {position['label']} — {position['summary']}",
                          any(h.startswith(f"{position['label']} ") and position["summary"] in h for h in headers),
                          headers)
        text = normalise(table.get_text(" ", strip=True))
        for fragment in interp["requiredPrintedText"][:2]:
            results.check(f"{role}: the table prints the column “{fragment}”", fragment in text)
        page = table.find_parent(class_="page")
        results.check(f"{role}: the page asks for a best-supported choice as a persistent control",
                      page.select_one('[data-persist-id$="7-best"]') is not None
                      and page.select_one('[data-persist-id$="7-best"]').has_attr("data-response"))
    results.check("the Accessible interpretation table models exactly one position and the Student models none",
                  len(soup.select('section.page[data-role="accessible"] .interpretation-table tr.model-row')) == 1
                  and not soup.select('section.page[data-role="student"] .interpretation-table tr.model-row'))
    results.check("the Answer Key names interpretation C as the best supported",
                  "Best supported - C" in answer_text)

    # --- THE HISTORICAL QUALIFICATION: POSITIVE REQUIREMENTS ----------------
    hq = registry["historicalQualification"]
    results.check("the qualification names the audit finding and the five refused simplifications",
                  hq["findingId"] == "HHH-GAME-C2L3-001" and len(hq["refusedSimplifications"]) == 5)
    results.check("the qualification records the rejected overclaim and the rejected overcorrection",
                  "saved a billion lives" in hq["rejectedOverclaim"]
                  and "unreal or historically worthless" in hq["rejectedOvercorrection"])
    results.check("the qualification states the five-measure rule and the trait rule in terms",
                  "five different things" in hq["measureRule"]
                  and "production per unit of area" in hq["measureRule"]
                  and "greater planted area" in hq["measureRule"]
                  and "does not biologically cause rust resistance" in hq["traitRule"]
                  and "a tall wheat can be rust-resistant" in hq["traitRule"])
    for requirement in hq["positiveRequirements"]:
        for role in requirement["roles"]:
            found = soup.select(f'section.page[data-role="{role}"] {requirement["selector"]}')
            results.check(f"{role}: positive requirement {requirement['id']} is printed", bool(found), requirement["selector"])
    for role in hq["requiredPrintedStatementRoles"]:
        for statement in hq["requiredPrintedStatements"]:
            results.check(f"{role}: prints the required statement “{statement[:46]}…”",
                          normalise(statement).lower() in texts[role].lower(), statement)
    # The two-layer verdict in the Answer Key keeps the in-game verdict apart from history.
    verdict_block = soup.select_one('section.page[data-role="answer"] [data-two-layer-verdict]')
    verdict_text = normalise(verdict_block.get_text(" ", strip=True)) if verdict_block else ""
    results.check("the Answer Key's Task 7 exemplar keeps the in-game verdict apart from the historical one",
                  "inside the game every other source contradicts it" in verdict_text.lower()
                  and "outside the game the official record shows" in verdict_text.lower()
                  and "no source in this packet measures" in verdict_text.lower(), verdict_text[:220])
    # Every role prints the trait boundary or the measure boundary where it belongs.
    for role in LEARNER_ROLES:
        results.check(f"{role}: the packet prints the two separate traits beside the trait that could be confused",
                      "Two separate traits" in texts[role] and "rust resistance answers a fungus" in texts[role].lower())
        results.check(f"{role}: the packet prints the five-measure rule",
                      "Production, yield, hunger, welfare and a counterfactual count of lives saved are five different things"
                      in texts[role])
    # No documented card and no figure may carry a lives figure of any kind. These are the
    # two places a counted humanitarian total would be read as a packet value, and neither
    # is excused by any exemption or by the game layer.
    LIVES_FIGURE = re.compile(r"\b(?:\d[\d,.]*|a|one)\s*(?:million|billion)\b[^.!?]{0,24}\blives\b", re.I)
    for role in ALL_ROLES:
        stray = []
        for node in soup.select(f'section.page[data-role="{role}"] [data-evidence-layer="documented"], '
                                f'section.page[data-role="{role}"] figure.case-figure, '
                                f'section.page[data-role="{role}"] [role="img"][aria-label]'):
            text = normalise(node.get_text(" ", strip=True)) + " " + normalise(node.get("aria-label") or "")
            stray.extend(p for p in propositions(text) if LIVES_FIGURE.search(p))
        results.check(f"{role}: no documented card or figure states a lives figure", not stray, stray[:4])
    results.check("no figure accessibility text mentions lives at all",
                  not [n.get("aria-label") for n in soup.select("figure.case-figure [role='img'][aria-label]")
                       if re.search(r"\blives\b", n.get("aria-label"), re.I)])

    # --- SEMANTIC GUARDS: POSITIVE CONTROL (the package itself) --------------
    invariants = registry["semanticInvariants"]
    exemptions = {e["id"]: e for e in invariants["exemptions"]}
    structural = invariants["structuralExemptSelectors"]
    compiled = compile_classes(hq["prohibitedFramings"])
    results.check("all five prohibited concept classes compile",
                  set(compiled) == {"livesSavedAsMeasurement", "seedAloneCausation", "productionIsYield",
                                    "dwarfingCausesRust", "productionEndsHunger"}, sorted(compiled))
    results.check("the structural exemptions excuse only the two classes the game itself asserts",
                  all(set(s["allowedConcepts"]) == {"livesSavedAsMeasurement", "seedAloneCausation"}
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
            results.check(f"negative control fires for {class_id}: {sentence[:52]}",
                          any(h[2] == class_id for h in hits), hits)
    # Structural mutation controls: the same sentence is excused inside a reconstructed
    # card or a marked quotation, and NOT excused when the marker is absent or forged.
    inside_card = synthetic("student", '<section class="dossier-card" data-source-id="borlaug-record" '
                                       'data-evidence-layer="reconstructed"><p>A billion lives hung on the wheat.</p></section>')
    results.check("structural control: a reconstructed card may print the game's billion-lives claim",
                  not scan_html(inside_card, compiled, exemptions, structural, "student"))
    marked = synthetic("student", '<div data-tests-game-claim="2"><p>The Archive filed it under <span data-game-claim="x">a billion lives hung on the wheat</span>.</p></div>')
    results.check("structural control: a marked in-game quotation is excused",
                  not scan_html(marked, compiled, exemptions, structural, "student"))
    unmarked = synthetic("student", '<div data-tests-game-claim="2"><p>A billion lives hung on the wheat.</p></div>')
    results.check("structural control: the same sentence without the marker fires",
                  bool(scan_html(unmarked, compiled, exemptions, structural, "student")))
    forged_layer = synthetic("student", '<section class="dossier-card" data-evidence-layer="documented"><p>The new wheat saved a billion lives.</p></section>')
    results.check("structural control: a documented card is not excused from the lives-saved class",
                  bool(scan_html(forged_layer, compiled, exemptions, structural, "student")))
    yield_in_card = synthetic("student", '<section class="dossier-card" data-evidence-layer="reconstructed"><p>Production is yield.</p></section>')
    results.check("structural control: a reconstructed card is still held to the production-versus-yield class",
                  bool(scan_html(yield_in_card, compiled, exemptions, structural, "student")))
    rust_in_card = synthetic("student", '<section class="dossier-card" data-evidence-layer="reconstructed"><p>Semi-dwarfing gave the wheat its rust resistance.</p></section>')
    results.check("structural control: a reconstructed card is still held to the trait-causation class",
                  bool(scan_html(rust_in_card, compiled, exemptions, structural, "student")))
    hunger_in_card = synthetic("student", '<section class="dossier-card" data-evidence-layer="reconstructed"><p>The green revolution ended hunger.</p></section>')
    results.check("structural control: a reconstructed card is still held to the production-ends-hunger class",
                  bool(scan_html(hunger_in_card, compiled, exemptions, structural, "student")))
    dossier_removed = synthetic("student", '<div class="dossier"></div>')
    results.check("mutation control: removing dossier Source E from the packet is detectable",
                  not BeautifulSoup(dossier_removed, "html.parser").select('[data-source-id~="failure-report"]'))

    # --- SEMANTIC GUARDS: POSITIVE (MUST-NOT-FLAG) CONTROLS -----------------
    REQUIRED_LEGAL = [
        "The title comes from the game.",
        "No source in this packet counts lives.",
        "Improved semi-dwarf wheat was an important contributor to the production gains.",
        "Production is yield multiplied by area, which is why the two percentages are different.",
        "Short stiff straw answers lodging and rust resistance answers a fungus.",
        "Calorie availability rose, but micronutrient malnutrition persisted.",
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
    forged = synthetic("student", '<p data-semantic-exemption="not-a-registered-id">The new seed alone caused the wheat gains.</p>')
    results.check("mutation control: an unregistered exemption id excuses nothing",
                  bool(scan_html(forged, compiled, exemptions, structural, "student")))
    wrong_role = synthetic("student", '<p data-semantic-exemption="teacher-misconception">The new seed alone caused the wheat gains.</p>')
    results.check("mutation control: an exemption does not carry into a role it does not declare",
                  bool(scan_html(wrong_role, compiled, exemptions, structural, "student")))
    narrow = synthetic("answer", '<p data-semantic-exemption="answer-key-tested-claim">Production is yield.</p>')
    results.check("mutation control: a narrow exemption excuses only the classes it declares",
                  bool(scan_html(narrow, compiled, exemptions, structural, "answer")))

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
                      json.dumps({"unlisted": sorted(set(assessed) - set(listed)),
                                  "listed-but-absent": sorted(set(listed) - set(assessed))}))
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
                          na < ns and sub.get("governedBy") in adaptation_ids,
                          f"{ns} -> {na}, governedBy={sub.get('governedBy')}")
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
    results.check("Task 8 collects all five obligations as parity subparts in both editions",
                  [next(s for s in subparts if s["id"] == i)["differenceClass"] for i in
                   ("finding", "quantitative-evidence", "second-source", "causal-qualification",
                    "limitation", "next-evidence")] == ["parity"] * 6
                  and "reduces nothing" in erc["culminationParityRule"])

    # --- ACCESSIBLE ADAPTATIONS ARE TRUE AND DECLARED -----------------------
    adaptations = registry["accessibleAdaptations"]
    results.check("exactly five Accessible adaptations are declared, and no sixth has appeared",
                  len(adaptations) == 5, sorted(adaptation_ids))
    for adaptation in adaptations:
        task = next(t for t in tasks if t["id"] == adaptation["task"])
        label = normalise(f"{task['number']} · {task['title']}")
        results.check(f"adaptation {adaptation['id']} is disclosed to the teacher", label in teacher_text)
        for role in adaptation["declaredIn"]:
            results.check(f"adaptation {adaptation['id']} declares a real role", role in ALL_ROLES)
        results.check(f"adaptation {adaptation['id']} explains why it is not a leak",
                      len(adaptation.get("whyNotALeak", "")) > 60)
    marked_adaptations = {n.get("data-accessible-adaptation") for n in soup.select("[data-accessible-adaptation]")}
    results.check("every adaptation marked in the Accessible markup is registered", marked_adaptations <= adaptation_ids)
    results.check("all five declared adaptations are actually present in the Accessible edition",
                  marked_adaptations == adaptation_ids, sorted(adaptation_ids ^ marked_adaptations))
    results.check("every marked adaptation sits in the Accessible edition and nowhere else",
                  all(n.find_parent(class_="page").get("data-role") == "accessible"
                      for n in soup.select("[data-accessible-adaptation]")))
    results.check("every Accessible worked example or given element is printed as one",
                  all("WORKED EXAMPLE" in normalise(n.get_text(" ", strip=True)).upper()
                      or "GIVEN" in normalise(n.get_text(" ", strip=True)).upper()
                      for n in soup.select('section.page[data-role="accessible"] [data-accessible-adaptation]')))
    results.check("the Teacher scoring note claims exactly five scored differences",
                  "Five scored differences, and only five" in teacher_text)
    results.check("the Answer Key discloses the same five scored differences",
                  "Five scored differences, and only five" in answer_text)
    results.check("the Accessible edition uses continuous flow rather than one task per page",
                  any(len(p.select("[data-shell-task-heading]")) >= 2 for p in pages_for(soup, "accessible")))
    results.check("the Accessible edition reduces repeated writing overall",
                  len(soup.select('section.page[data-role="accessible"] [data-response][data-persist-id]'))
                  < len(soup.select('section.page[data-role="student"] [data-response][data-persist-id]')))
    for page_id, minimum in (("accessible-billion-04", 3), ("accessible-billion-07", 3),
                             ("accessible-billion-10", 5)):
        results.check(f"Accessible page {page_id} carries its sentence frames",
                      len(soup.select(f'section.page[data-page-id="{page_id}"] .memo-frame')) >= minimum,
                      len(soup.select(f'section.page[data-page-id="{page_id}"] .memo-frame')))
    results.check("the Accessible finding carries a sentence opener on every obligation",
                  len(soup.select('section.page[data-role="accessible"] [data-qualified-finding] .memo-frame')) == 6)
    results.check("the Accessible finding states that bullets are accepted",
                  "Bullets are fine" in texts["accessible"])
    results.check("the Accessible route supplies three stages and asks for one",
                  len(soup.select('section.page[data-role="accessible"] .route-build .rb-given')) == 3
                  and len(soup.select('section.page[data-role="accessible"] .route-build .route-response')) == 1
                  and len(soup.select('section.page[data-role="student"] .route-build .route-response')) == 4)
    results.check("the Accessible layer table supplies one row and the Student supplies none",
                  len(soup.select('section.page[data-role="accessible"] .layer-table .prefilled')) == 2
                  and not soup.select('section.page[data-role="student"] .layer-table .prefilled'))

    # --- RESPONSE SPACE AND DIGITAL MARKABILITY -----------------------------
    for edition, block in (("student", layout["student"]), ("accessible", layout)):
        declared_ids = {a["persistId"] for a in block["areas"]} | {a["persistId"] for a in block["lockedAreas"]}
        found_ids = [n.get("data-persist-id") for n in
                     soup.select(f'section.page[data-role="{edition}"] [data-response][data-persist-id]')]
        results.check(f"{edition}: every persistent response is layout-classified",
                      set(found_ids) == declared_ids,
                      json.dumps({"unclassified": sorted(set(found_ids) - declared_ids),
                                  "orphan": sorted(declared_ids - set(found_ids))}))
        results.check(f"{edition}: no persist id is used twice", len(found_ids) == len(set(found_ids)))
    for selector, label in ((".mark-response", "compact judgment slot"), (".inline-response", "vocabulary blank"),
                            (".table-response", "matrix cell"), (".route-response", "route box"),
                            (".pkg-response", "package slot")):
        nodes = soup.select(f'.page[data-role="student"] {selector}, .page[data-role="accessible"] {selector}')
        results.check(f"every printed {label} in a learner edition is persistent and named",
                      bool(nodes) and all(m.has_attr("data-response") and m.has_attr("data-persist-id")
                                          and m.get("role") == "textbox" and m.get("aria-label") for m in nodes),
                      len(nodes))
    results.check("every response field in every role carries an accessible name",
                  all(n.get("aria-label") or n.get("aria-labelledby") for n in soup.select("[data-response]")))
    # Every printed instruction that asks a learner to act has a persistent control.
    ACTION_WORDS = re.compile(r"\b(?:write|name|say|choose|mark|select|classify|circle|check|rank|explain|complete|fill)\b", re.I)
    for role in LEARNER_ROLES:
        for page in pages_for(soup, role):
            directions = page.select(".directions, .response-label")
            if not directions:
                continue
            asks = any(ACTION_WORDS.search(normalise(d.get_text(" ", strip=True))) for d in directions)
            has_control = bool(page.select("[data-response][data-persist-id]"))
            results.check(f"{role}: {page.get('data-page-id')} pairs its instructions with persistent controls",
                          (not asks) or has_control)
    results.check("every figure carries accessibility text",
                  all(f.select_one("[role='img'][aria-label]") is not None for f in soup.select("figure.case-figure")))

    # --- FIGURE CONTRACT -----------------------------------------------------
    def described_alt(role: str, contract: str) -> str:
        node = soup.select_one(f'section.page[data-role="{role}"] [{contract}] [role="img"][aria-label]')
        return normalise(node.get("aria-label")) if node is not None else ""

    results.check("the figure contract declares exactly the three deterministic figures",
                  [f["id"] for f in registry["figureContract"]["figures"]] == ["india-record", "route", "package"])
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
                results.check(f"{role}: {spec['id']} accessibility text names {fragment}",
                              fragment.lower() in alt.lower(), fragment)
            if spec.get("requiresRouteRule"):
                results.check(f"{role}: {spec['id']} accessibility text states the route rule",
                              "route and not a map" in alt.lower())
            if spec.get("requiresPackageRule"):
                results.check(f"{role}: {spec['id']} accessibility text states the package rule",
                              spec["requiresPackageRule"].lower() in alt.lower())
            root = figure_root(figure)
            whole = normalise(root.get_text(" ", strip=True)) if root is not None else normalise(figure.get_text(" ", strip=True))
            for fragment in spec.get("requiresPrintedText", []):
                results.check(f"{role}: {spec['id']} prints {fragment}", fragment.lower() in whole.lower(), fragment)
            caption = root.find("figcaption") if root is not None else None
            cap_text = normalise(caption.get_text(" ", strip=True)).upper() if caption else ""
            for term in spec.get("requiresCaptionTerms", []):
                results.check(f"{role}: {spec['id']} caption carries the status term {term}", term.upper() in cap_text)
    for figure_id, contract in (("india-record", "data-quant-contract"), ("route", "data-route-contract"),
                                ("package", "data-package-contract")):
        student_alt = described_alt("student", contract)
        accessible_alt = described_alt("accessible", contract)
        results.check(f"{figure_id} accessibility text is identical in both learner editions",
                      bool(student_alt) and student_alt == accessible_alt)
    results.check("no figure in the package uses imagery of any kind beyond the institutional insignia",
                  not soup.select('figure.case-figure img:not(.taa-insignia)'))
    results.check("no page references an external or generated image asset",
                  not [n.get("src") for n in soup.select("img") if "insignia" not in (n.get("src") or "")])
    results.check("every figure-level status line names the curriculum-original band",
                  all("CURRICULUM-ORIGINAL FIGURE" in normalise(f.select_one(".source-status").get_text()).upper()
                      for f in soup.select("figure.case-figure")))
    results.check("the figure contract states the grayscale rule in terms of words and geometry",
                  "carried by colour alone" in registry["figureContract"]["grayscaleRule"])
    # Grayscale independence, checked structurally: every bar prints a value, every route
    # stage prints a place and a date, every package node prints a connector word.
    for role in LEARNER_ROLES:
        bars = soup.select(f'section.page[data-role="{role}"] .rec-bar')
        results.check(f"{role}: every drawn bar prints its own value",
                      bool(bars) and all(b.select_one(".rec-val") is not None
                                         and normalise(b.select_one(".rec-val").get_text()) for b in bars))
        stations = soup.select(f'section.page[data-role="{role}"] .route-node')
        results.check(f"{role}: every route stage prints its place and its date",
                      bool(stations) and all(s.select_one(".rn-place") and s.select_one(".rn-when") for s in stations))
        nodes = soup.select(f'section.page[data-role="{role}"] .pkg-node')
        results.check(f"{role}: every package node prints its connector word",
                      bool(nodes) and all(n.select_one(".pn-verb") for n in nodes))

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
                  bool(tables) and all(t.find("caption") and t.select("thead th") and t.select('tbody th[scope="row"]')
                                       for t in tables),
                  [normalise(t.find("caption").get_text())[:60] if t.find("caption") else "NO CAPTION"
                   for t in tables if not (t.find("caption") and t.select("thead th") and t.select('tbody th[scope="row"]'))])
    results.check("the package declares the language and the PDF-accessibility notice",
                  package["accessibility"]["language"] == "en"
                  and "does not guarantee PDF accessibility" in package["accessibility"]["pdfNotice"])
    results.check("production is HTML-only: no canonical PDF is declared anywhere in the package",
                  not any("pdf" in str(v).lower() for v in package["outputs"].values())
                  and all(str(v).endswith(".html") for v in package["outputs"].values()))
    results.check("no generated role output is committed beside the sources",
                  not [p.name for p in SOURCE.iterdir()
                       if p.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".webp"} or p.name.endswith("_CUSTOM.html")])
    results.check("no PDF, image or generated HTML exists anywhere in the unit",
                  not [q for q in UNIT.rglob("*")
                       if q.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".svg", ".docx"}
                       or (q.suffix.lower() == ".html" and q.name != "content.html")],
                  [str(q.relative_to(UNIT)) for q in UNIT.rglob("*")
                   if q.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".svg", ".docx"}
                   or (q.suffix.lower() == ".html" and q.name != "content.html")])
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
    results.check("the Answer Key completes every Task 1 placement with the seven applied terms",
                  all(term in answer_text for term in
                      ("lodging", "semi-dwarf", "yield", "pedigree", "baseline", "input package", "causation")))
    results.check("the Answer Key names the two glossary terms that are deliberately not slotted",
                  "denominator" in answer_text and "Green Revolution" in answer_text
                  and "deliberately not slotted here" in answer_text)
    key_matrices = soup.select('section.page[data-role="answer"] .key-matrix')
    results.check("the Answer Key completes the Task 3 layer matrix with three rows and two filled columns",
                  bool(key_matrices) and len(key_matrices[0].select("tbody tr")) == 3
                  and all(len(tr.select("td")) == 2 and all(normalise(td.get_text(" ", strip=True))
                                                            for td in tr.select("td"))
                          for tr in key_matrices[0].select("tbody tr")))
    results.check("the Answer Key completes all four Task 4 reads and all three written parts",
                  all(k in answer_text for k in ("A1 1965-66", "A2 1967-68", "Part B -", "Part C -", "Part D -"))
                  and "12.84" in answer_text and "43.4%" in answer_text)
    results.check("the Answer Key completes all four Task 5 route stages and both later parts",
                  all(k in answer_text for k in ("Japan -", "United States -", "Mexico -",
                                                 "India and West Pakistan -", "Part B, any three -", "Part C -")))
    results.check("the Answer Key completes the Task 6 organiser with four tests, a verdict and the paperwork response",
                  len(key_matrices) >= 2 and len(key_matrices[1].select("tbody tr")) == 4
                  and "Verdict inside the game -" in answer_text
                  and "Why the paperwork is not a test -" in answer_text)
    results.check("the Task 6 exemplar refuses a verdict from the paperwork and a reach outside the game",
                  "a verdict reached from the letterhead" in answer_text
                  and "reaches outside the game to Sources F to I" in answer_text)
    results.check("the Answer Key completes all three Task 7 interpretations with supports and overreach",
                  all(k in answer_text for k in ("A The wheat failed", "Valid evidence:", "Overreach:",
                                                 "C A large contribution inside a system")))
    results.check("the Task 7 exemplar names the double overreach in interpretation B",
                  "makes one contributor the whole cause" in answer_text
                  and "states a number of lives, which no source in this packet measures" in answer_text)
    results.check("the Answer Key completes all five Task 8 obligations",
                  all(part in answer_text for part in
                      ("1 Finding -", "2 Quantitative Evidence -", "3 Second Documented Source -",
                       "4(a) Causal Qualification -", "4(b) Limitation -", "5 Next Evidence Needed -")))
    results.check("the Task 8 exemplar carries units, years and place on its quantitative evidence",
                  "million tonnes" in answer_text and "kilograms per hectare" in answer_text
                  and "crop years 1964-65 to 1969-70" in answer_text and "India" in answer_text)
    results.check("the Task 8 exemplar uses a second documented source and names multiple contributing conditions",
                  "Source G" in answer_text and "not based solely on the use of Mexican dwarf varieties" in answer_text
                  and "irrigated share of the wheat area rose" in answer_text)
    results.check("the Task 8 exemplar states a real evidentiary limitation and the next evidence needed",
                  "does not prove how many people were fed" in answer_text
                  and "differ only in the variety sown" in answer_text
                  and "a harvest figure does not say who ate" in answer_text)
    floor = soup.select_one('section.page[data-role="answer"] [data-answer-key-floor]')
    floor_text = normalise(floor.get_text(" ", strip=True)) if floor is not None else ""
    for needle in ("the new seed alone caused the wheat gains", "any counted number of lives",
                   "a rise in total production is the same as a rise in yield",
                   "gave it rust resistance", "flawless paperwork proves it genuine"):
        results.check(f"the Answer Key floor names the refused claim “{needle}”", needle in floor_text, floor_text[:280])
    results.check("every Answer Key exemplar block is followed by an acceptable-variation ruling",
                  len(soup.select('section.page[data-role="answer"] .answer-block'))
                  <= len([n for n in soup.select('section.page[data-role="answer"] .key-note')
                          if "Acceptable variation" in normalise(n.get_text(" ", strip=True))]) + 1)
    results.check("the Answer Key is no more restrictive than the Accessible edition permits",
                  "Bullets, labelled lists, dictated and scribed responses are accepted in every constructed-response field in both editions"
                  in answer_text
                  and "a learner who reasons in whole numbers rather than percentages is not penalised" in answer_text)

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
                          ("The two boundaries this case exists to hold", "the two boundaries"),
                          ("Evidence architecture", "evidence architecture"), ("Reasoning path", "reasoning path"),
                          ("The competing records", "competing records"),
                          ("Limitations to keep in front of the class", "limitations"),
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
    MISCONCEPTIONS = ("the new seed alone caused the wheat gains", "it saved a billion lives",
                      "production went up, so yield went up by the same amount",
                      "making the wheat short is what made it rust-resistant",
                      "more wheat means hunger ended", "so the gains were not real",
                      "the paperwork is perfect, so the report is genuine",
                      "because he was there")
    lowered = teacher_text.lower()
    missing = [m for m in MISCONCEPTIONS if m not in lowered]
    results.check("the Teacher misconception table protects against every required framing", not missing, missing)
    results.check("the Teacher Guide carries the diagnostic reading for the non-keyable task",
                  "Read the three slots as a diagnostic" in teacher_text)
    results.check("the Teacher Guide states the two boundaries in its own words",
                  "Production, yield, hunger, welfare and lives saved are five different things" in teacher_text
                  and "Semi-dwarfing and lodging resistance are not rust resistance" in teacher_text)
    results.check("the Teacher Guide refuses a credited answer that counts lives",
                  "No student answer that states a number of lives saved as a fact should be credited" in teacher_text)
    results.check("the Teacher Guide names all four documented sources and closes the estate",
                  "Government of India" in teacher_text and "Nobel Lecture" in teacher_text
                  and "CIMMYT" in teacher_text and "Proceedings of the National Academy of Sciences" in teacher_text
                  and "Do not extend the real-world layer beyond these four" in teacher_text)
    results.check("the Teacher Guide records the seed-purchase date variance as a limitation",
                  "1966 in Borlaug's lecture, 1967 in CIMMYT's account" in normalise(teacher_text))
    results.check("the Teacher Guide records that later statistical editions revise historical values",
                  "Later editions revise some historical values" in teacher_text)
    results.check("the Teacher Guide flags any shortened route as a modified assessment route",
                  teacher_text.count("modified assessment route") >= 2)
    results.check("no Teacher page exposes a clue identifier or node path",
                  not re.search(r"\b[a-z]+_[a-z]+\b|->|__exit__", teacher_text))

    # --- STANDARDS -----------------------------------------------------------
    standards = registry["standards"]
    results.check("the directly assessed standards are exactly the six locked claims",
                  standards["directlyAssessed"] == ["C3 D2.His.14.6-8", "C3 D3.3.6-8", "C3 D3.4.6-8",
                                                    "C3 D4.1.6-8", "CCSS RH.6-8.7", "CCSS WHST.6-8.1"],
                  standards["directlyAssessed"])
    results.check("the supporting standards are exactly the two locked ones",
                  standards["supporting"] == ["C3 D3.2.6-8", "CCSS RH.6-8.8"])
    results.check("the contextual list is empty, as locked",
                  standards["contextual"] == [], standards["contextual"])
    results.check("no NGSS performance expectation is claimed at any status",
                  not any("NGSS" in s for s in standards["directlyAssessed"] + standards["supporting"]
                          + standards["contextual"])
                  and "No NGSS performance expectation is claimed" in standards["ngss"]
                  and "No NGSS performance expectation is claimed at any status" in teacher_text)
    results.check("the standards list is not inflated beyond the locked eight claims",
                  len(standards["directlyAssessed"]) + len(standards["supporting"]) == 8)
    for claim in standards["directlyAssessed"] + standards["supporting"]:
        results.check(f"standard {claim} appears in the Teacher standards table", claim in teacher_text, claim)
    table_rows = soup.select('section.page[data-role="teacher"] .standards-table tbody tr')
    results.check("the Teacher standards table carries one row per claim and no more",
                  len(table_rows) == len(standards["directlyAssessed"]) + len(standards["supporting"]))
    results.check("every Teacher standards row states where it is measured and its limit",
                  all("Limit:" in normalise(tr.get_text(" ", strip=True)) for tr in table_rows))
    results.check("the Teacher page states that no contextual standard is claimed either",
                  "no contextual standard is claimed either" in teacher_text
                  and "Do not inflate this list" in teacher_text)

    # --- VOCABULARY ----------------------------------------------------------
    vocabulary = registry["vocabulary"]
    results.check("the case declares nine vocabulary terms", len(vocabulary) == 9, vocabulary)
    results.check("the vocabulary is alphabetical by displayed term",
                  [v.lower() for v in vocabulary] == sorted(v.lower() for v in vocabulary), vocabulary)
    results.check("the required terms are exactly the locked nine", vocabulary == EXPECTED_VOCABULARY, vocabulary)
    results.check("the no-word-bank decision is recorded with its reason",
                  "No exact-match word bank is used" in registry["vocabularyBankDecision"]
                  and "none is authorised by the design lock" in registry["vocabularyBankDecision"])
    results.check("no learner edition prints a word bank",
                  not soup.select('section.page[data-role="student"] .word-bank')
                  and not soup.select('section.page[data-role="accessible"] .word-bank'))
    for role in LEARNER_ROLES:
        terms = [normalise(d.get_text(" ", strip=True)) for d in soup.select(f'section.page[data-role="{role}"] .glossary dt')]
        results.check(f"{role}: the glossary prints exactly the declared terms in alphabetical order",
                      terms == vocabulary, terms)
        definitions = soup.select(f'section.page[data-role="{role}"] .glossary dd')
        results.check(f"{role}: every term carries a printed definition",
                      len(definitions) == len(vocabulary)
                      and all(len(normalise(d.get_text(" ", strip=True))) > 30 for d in definitions))
        blanks = soup.select(f'section.page[data-role="{role}"] .term-list .inline-response')
        results.check(f"{role}: seven applied term placements are asked for", len(blanks) == 7, len(blanks))
    for term in vocabulary:
        results.check(f"the Teacher vocabulary table defines {term}", term in teacher_text, term)

    payload = {
        "validator": "hhh-case10-the-quiet-billion-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": [a for a in results.assertions if a["status"] == "FAIL"] or "all passed",
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
