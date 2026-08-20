#!/usr/bin/env python3
"""Case-scoped protections for HHH Campaign 2 Core Case 08 — The Floating Gardens.

These assertions guard the boundaries this case exists to get right, plus the
cross-edition parity the shared operational walk does not reach into. They are
driven by the contract blocks the task registry declares — ``sourceStatusContract``,
``terminologyQualification``, ``systemModel``, ``evidenceLayers``,
``sourceCertification``, ``cerDecision``, ``noGameRoute``,
``editionResponseContract``, ``accessibleAdaptations``, ``semanticInvariants`` and
``figureContract`` — rather than by literal paragraph locks, so ordinary rewording
stays possible while the meaning stays protected.

The audit dependency this case carries:

* ``HHH-GAME-C2L1-001`` — ``CURRICULUM_QUALIFICATION_REQUIRED``, and open at the
  audited game baseline by design. It is a **teacher-qualification** dependency,
  not a blocking one: no game remediation is required for Case 08 and none is
  requested. The curriculum carries the qualification the audit asked for, and the
  guards below are what keep that true.

DESIGN NOTE — the shape of the semantic guard, and its limits.

This case has three high-risk misconceptions, and each gets one CLOSED class:

  * ``chinampasFloat`` — chinampas literally float, drift, or are rafts;
  * ``reconstructionAsPrimary`` — reconstructed game material presented as
    surviving 1487 evidence;
  * ``mapAsExactSnapshot`` — the 1524 published plan described as an exact map,
    survey or snapshot of 1487.

Every class is CLOSED: a small finite negative vocabulary, anchored to a named
subject register, requiring an affirmative and unnegated predicate. None
enumerates synonyms for an open concept, and none polices an ordinary verb. That
restraint is deliberate — it is the lesson of the Case 04 catalyst spiral, and it
is why this file is short.

**This guard makes no claim of semantic completeness.** It is a defence against
three known misconceptions, not a proof that every possible bad paraphrase has
been detected. An unseen paraphrase can pass it. Ordinary cross-role parity,
source-status and manual review remain required, and the positive structural
requirements below — checked against markup rather than prose — are what carry
the audit obligation, because a guard that only forbade the wrong sentence would
be satisfied by a packet that said nothing at all.

Every semantic guard ships with NEGATIVE CONTROLS it must flag and POSITIVE
CONTROLS it must not, and the package itself is the standing positive control. A
guard that has silently stopped working therefore fails the run rather than
passing it quietly.

Usage:
    python3 apps/curriculum-editor/tests/validate_hhh_case08_floating_gardens.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "hhh/campaign-2/case-08-floating-gardens"
SOURCE = UNIT / "source"
REGISTRY_FILE = ROOT / "shared/implementation/case-registry.v2.json"
TRACKER_FILE = ROOT / "hhh/production/data/HHH_GAME_REMEDIATION_DEPENDENCY_TRACKER_v1.0.json"
CASE_ID = "HHH-C2-CASE08"
LEARNER_ROLES = ("student", "accessible")
ALL_ROLES = ("student", "teacher", "answer", "accessible")
GAME_COMMIT = "d9fc16baf272cb543c29cbd0c06ec85efad60be8"
AUDITED_GAME_COMMIT = "9b8545ed6ecf98b337326390400076e36789e056"

# Propositions break on terminal punctuation only. A semicolon, colon or dash is
# internal punctuation and not a safety boundary: splitting on them would let
# "the canal is deep; the chinampas floated on the lake" evade the gate by one
# character.
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
    """Every registered exemption id in force at this node, walking ancestors."""
    ids: set[str] = set()
    current = node
    while current is not None and getattr(current, "get", None):
        value = current.get("data-semantic-exemption")
        if value:
            ids.add(value)
        current = current.parent
    return ids


def resolvable(node, exemptions: dict, role: str) -> set[str]:
    """The concept classes actually excused at this node.

    An exemption id excuses something only if it is REGISTERED and declares this
    role. An id the registry has never heard of, or one borrowed from another
    role, resolves to the empty set and therefore excuses nothing. That is what
    makes "markup cannot self-authorize" true rather than aspirational, and the two
    mutation controls at the end of this file are what keep it true.
    """
    allowed: set[str] = set()
    for eid in exempt_ids(node):
        spec = exemptions.get(eid)
        if spec and role in spec["roles"]:
            allowed |= set(spec["allowedConcepts"])
    return allowed


def leaf_blocks(page, exemptions: dict, role: str) -> list:
    """Paragraph-level containers paired with the concepts excused inside them.

    Innermost-container selection means each run of prose is scanned exactly once.
    Exempt-subtree REMOVAL, rather than skipping the exempt node, is what makes a
    registered exemption work on a clause: an Answer Key floor that quotes the
    wording it refuses is a span inside an ordinary paragraph, and skipping the span
    while still scanning its parent would leave the quoted wording in the parent's
    text. Only subtrees whose exemption RESOLVES are removed.
    """
    blocks = []

    def prepared(node):
        allowed = resolvable(node, exemptions, role)
        clone = BeautifulSoup(str(node), "html.parser")
        for exempted in clone.select("[data-semantic-exemption]"):
            spec = exemptions.get(exempted.get("data-semantic-exemption"))
            if spec and role in spec["roles"]:
                exempted.decompose()
        return allowed, normalise(clone.get_text(" ", strip=True))

    for node in page.find_all(PARAGRAPH_TAGS):
        if node.find(PARAGRAPH_TAGS):
            continue
        allowed, text = prepared(node)
        if text:
            blocks.append((node, text, allowed))
    # Text living outside any paragraph container - a status strip built from
    # nested spans, for instance - would otherwise never be scanned.
    for node in page.find_all("span"):
        if node.find_parent(PARAGRAPH_TAGS) or node.find("span"):
            continue
        allowed, text = prepared(node)
        if text:
            blocks.append((node, text, allowed))
    # Fixed-width survey extracts are divs, not paragraphs, and carry printed
    # evidence. They are scanned as their own blocks rather than skipped.
    for node in page.select(".terminal"):
        allowed, text = prepared(node)
        if text:
            blocks.append((node, text, allowed))
    return blocks


# ---------------------------------------------------------------------------
# The semantic engine. One rule, three classes, compiled from the registry.
#
# A proposition violates a class when the class's patterns match AND, where the
# class declares a subject register, that subject is present in the same
# proposition. Nothing else violates anything.
# ---------------------------------------------------------------------------

def compile_classes(framings: dict) -> dict:
    compiled = {}
    for class_id, spec in framings.items():
        if not isinstance(spec, dict) or "patterns" not in spec:
            continue
        compiled[class_id] = {
            "subjects": [re.compile(p, re.I) for p in spec.get("subjectPatterns", [])],
            "patterns": [re.compile(p, re.I) for p in spec["patterns"]],
        }
    return compiled


def scan_html(html: str, compiled: dict, exemptions: dict, role: str) -> list[tuple]:
    """Return (role, page-id, class-id, sentence) for every violation."""
    soup = BeautifulSoup(html, "html.parser")
    violations = []
    for page in soup.select(f'section.page[data-role="{role}"]'):
        page_id = page.get("data-page-id")
        for _node, text, allowed in leaf_blocks(page, exemptions, role):
            for sentence in propositions(text):
                for class_id, spec in compiled.items():
                    if class_id in allowed:
                        continue
                    if spec["subjects"] and not any(s.search(sentence) for s in spec["subjects"]):
                        continue
                    if any(p.search(sentence) for p in spec["patterns"]):
                        violations.append((role, page_id, class_id, sentence[:220]))
    return violations


def figure_root(node):
    """The <figure> element a contract attribute belongs to, wherever it is declared."""
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
    results.check("package identity is HHH-C2-CASE08 v0.1 CORE_CASE in campaign-2",
                  (package["id"], package["version"], package["instructionalType"],
                   package["curriculum"], package["campaign"])
                  == (CASE_ID, "0.1", "CORE_CASE", "HHH", "campaign-2"))
    results.check("the package and task registry both carry the unreleased candidate lifecycle",
                  package["status"] == "DRAFT" and registry["status"] == "DRAFT"
                  and registry["ownerReviewStatus"] == "OWNER_REVIEW_NOT_STARTED"
                  and registry["version"] == "0.1"
                  and package["approval"]["status"] == "OWNER_REVIEW_NOT_STARTED"
                  and package["approval"]["printStatus"] == "NOT_RUN"
                  and package["approval"]["owner"] == "Nate / Owner"
                  and "date" not in package["approval"],
                  json.dumps({"package": package["status"], "registry": registry["status"],
                              "approval": package["approval"]}))
    results.check("no release history exists or is declared for the candidate",
                  not (UNIT / "history").exists() and "releaseHistory" not in package,
                  sorted(p.name for p in UNIT.iterdir()))
    results.check("the unit directory holds only README.md and source/",
                  sorted(p.name for p in UNIT.iterdir() if p.name != ".DS_Store") == ["README.md", "source"],
                  sorted(p.name for p in UNIT.iterdir()))
    results.check("the source directory holds exactly the four canonical sources",
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
                  registry["runtimeId"] == "C2L1", registry.get("runtimeId"))

    for key, filename in (("content", "content.html"), ("presentation", "presentation.css"),
                          ("taskRegistry", "task-registry.js"),
                          ("layoutOverrides", "layout-overrides.json")):
        digest = hashlib.sha256((SOURCE / filename).read_bytes()).hexdigest()
        results.check(f"package sourceHashes.{key} matches the working tree",
                      package["sourceHashes"][key] == digest, digest)

    shared = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    entry = next(c for cur in shared["curricula"] if cur["id"] == "HHH"
                 for camp in cur["campaigns"] for c in camp["cases"] if c["id"] == CASE_ID)
    results.check("the existing shared registry entry is activated rather than duplicated",
                  entry["status"] == "DRAFT" and entry["packageStatus"] == "DRAFT"
                  and entry["displayOrder"] == 10 and entry["displayLabel"] == "8 - The Floating Gardens"
                  and entry["title"] == "The Floating Gardens"
                  and entry["editorPackage"] == "hhh/campaign-2/case-08-floating-gardens/source/case-package.json"
                  and "historyRecord" not in entry
                  and entry["approval"] == {"owner": "Nate / Owner",
                                            "status": "OWNER_REVIEW_NOT_STARTED",
                                            "printStatus": "NOT_RUN"},
                  json.dumps(entry))
    all_hhh = [c["id"] for cur in shared["curricula"] if cur["id"] == "HHH"
               for camp in cur["campaigns"] for c in camp["cases"]]
    results.check("exactly one HHH-C2-CASE08 identity exists in the shared registry",
                  all_hhh.count(CASE_ID) == 1, all_hhh)
    results.check("the registry display label and the package identity agree",
                  registry["displayLabel"] == entry["displayLabel"]
                  and registry["title"] == package["title"] == entry["title"])

    # --- THE QUALIFICATION DEPENDENCY, WHICH IS NOT A BLOCKER ---------------
    tracker = json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
    dependency = next(d for d in tracker["gameDependencies"] if d["findingId"] == "HHH-GAME-C2L1-001")
    qualification = registry["terminologyQualification"]
    results.check("the case registry names the audit finding and its qualification class",
                  qualification["findingId"] == "HHH-GAME-C2L1-001"
                  and qualification["dependencyClass"] == "CURRICULUM_QUALIFICATION_REQUIRED"
                  and qualification["auditedGameCommit"] == AUDITED_GAME_COMMIT,
                  json.dumps({k: qualification.get(k) for k in
                              ("findingId", "dependencyClass", "auditedGameCommit")}))
    results.check("the shared remediation tracker agrees, and this package leaves it untouched",
                  dependency["curriculumUnit"] == CASE_ID
                  and dependency["dependencyClass"] == "CURRICULUM_QUALIFICATION_REQUIRED"
                  and dependency["status"] == "OPEN_AT_AUDITED_GAME_BASELINE"
                  and dependency["resolution"]["resolvedGameCommit"] is None,
                  json.dumps({k: dependency.get(k) for k in ("status", "curriculumUnit", "dependencyClass")}))
    results.check("no game remediation is requested by this package",
                  "not a blocking one" in qualification["gameNote"]
                  and "changes nothing in the shared remediation tracker" in qualification["gameNote"])
    results.check("the qualification states the nickname rule and the raised-field construction",
                  "conventional English nickname" in qualification["rule"]
                  and "staked structure set into the lake bottom" in qualification["rule"])
    results.check("the qualification refuses the opposite overcorrection in terms",
                  "perfect or incapable of environmental change" in qualification["overcorrectionNote"]
                  and "1604" in qualification["overcorrectionNote"])
    results.check("the qualification records the certified source's own nickname wording",
                  "floating artificial islands" in qualification["sourceWordingNote"]
                  and "the detail is what it documents" in qualification["sourceWordingNote"])

    # Lifecycle, repository and runtime metadata must never reach a printable page.
    LIFECYCLE_TOKENS = ("VALIDATION_BUILD", "OWNER_REVIEW", "packageStatus", "sourceHashes",
                        "case-package.json", "task-registry.js", "APPROVED_STABLE",
                        "d9fc16ba", "9b8545ed", "337b6b23", "releaseHistory", "release-v0.1",
                        "historyRecord", "Nate / Owner", "editorPackage", "OWNER_REVIEW_NOT_STARTED",
                        "HHH-GAME-C2L1-001", "HHH-C2-CASE08")
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
                      for i in status_contract["prohibitedRuntimeIdentifiers"]),
                  [i for i in status_contract["prohibitedRuntimeIdentifiers"]
                   if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", i)])

    # --- PAGE STRUCTURE AND DECLARED COUNTS ---------------------------------
    EXPECTED_PAGES = {"student": 8, "teacher": 7, "answer": 4, "accessible": 10}
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

    # The identification row is the first printable element on page 1 of the two
    # learner editions, and appears nowhere else in the packet.
    for role in LEARNER_ROLES:
        first = pages_for(soup, role)[0]
        content = first.select_one(".content-area")
        results.check(f"{role}: the Name / Date / Period row is the first printable element on page 1",
                      content is not None and content.find(True) is not None
                      and "student-id" in (content.find(True).get("class") or []),
                      str(content.find(True))[:120] if content else "no content area")
        extra = [p.get("data-page-id") for p in pages_for(soup, role)[1:] if p.select_one(".student-id")]
        results.check(f"{role}: no continuation page repeats the identification row", not extra, extra)
    for role in ("teacher", "answer"):
        results.check(f"{role}: carries no student identification row",
                      not soup.select(f'section.page[data-role="{role}"] .student-id'))

    # --- THE EIGHT TASKS ----------------------------------------------------
    EXPECTED_TASKS = [
        ("1", "Build the Case Vocabulary"),
        ("2", "Set a Geographic Test"),
        ("3", "Read the Lake-City Map"),
        ("4", "Trace the Chinampa System at Two Scales"),
        ("5", "Compare What the Sources Can Establish"),
        ("6", "Test the Buried Collapse Claim"),
        ("7", "Explain the Engineered Landscape"),
        ("8", "Transfer the Method"),
    ]
    results.check("the registry declares exactly the eight locked task numbers and titles",
                  [(t["number"], t["title"]) for t in tasks] == EXPECTED_TASKS,
                  [(t["number"], t["title"]) for t in tasks])
    keyed = {t["number"]: t["keyed"] for t in tasks}
    results.check("every task is keyed except Task 2, which declares why it is not",
                  keyed == {"1": True, "2": False, "3": True, "4": True,
                            "5": True, "6": True, "7": True, "8": True}
                  and len(next(t for t in tasks if t["number"] == "2")["nonKeyableReason"]) > 80,
                  keyed)
    for task in tasks:
        number, title = task["number"], task["title"]
        for role in LEARNER_ROLES:
            heading = soup.select_one(f'section.page[data-role="{role}"] [data-shell-task-heading="{number}"]')
            results.check(f"{role}: task {number} has exactly one shell heading",
                          len(soup.select(f'section.page[data-role="{role}"] '
                                          f'[data-shell-task-heading="{number}"]')) == 1
                          and heading is not None)
            placement = task["pagePlacement"][role]
            page = soup.select_one(f'section.page[data-role="{role}"][data-page-id="{placement}"]')
            results.check(f"{role}: task {number} starts on its declared page {placement}",
                          page is not None
                          and page.select_one(f'[data-shell-task-heading="{number}"]') is not None,
                          placement)
        # Teacher references reproduce the exact number and title, in bold.
        label = normalise(f"{number} · {title}")
        results.check(f"Teacher names task {number} by its exact number and title",
                      label in teacher_text, label)
        bold = [normalise(n.get_text(" ", strip=True))
                for n in soup.select('section.page[data-role="teacher"] strong.task-reference')]
        results.check(f"Teacher task {number} reference is emphasised as a bold task-reference",
                      label in bold, label)
        # The Answer Key keys every keyable task, preserving number and title, and
        # omits the non-keyable one silently rather than renumbering.
        answer_heading = soup.select_one(f'section.page[data-role="answer"] '
                                         f'[data-shell-task-heading="{number}"]')
        if task["keyed"]:
            results.check(f"Answer Key keys task {number} on its declared page",
                          answer_heading is not None
                          and answer_heading.find_parent(class_="page").get("data-page-id")
                          == task["pagePlacement"]["answer"],
                          task["pagePlacement"]["answer"])
        else:
            results.check(f"Answer Key omits non-keyable task {number} without renumbering",
                          answer_heading is None and task["pagePlacement"]["answer"] is None)
    results.check("every Teacher task reference names a real task and nothing else",
                  {normalise(n.get_text(" ", strip=True))
                   for n in soup.select('section.page[data-role="teacher"] strong.task-reference')}
                  == {normalise(f'{n} · {t}') for n, t in EXPECTED_TASKS},
                  sorted({normalise(n.get_text(" ", strip=True))
                          for n in soup.select('section.page[data-role="teacher"] strong.task-reference')}))
    results.check("no learner or Answer Key page carries a task heading outside the locked set",
                  {n.get("data-shell-task-heading") for n in soup.select("[data-shell-task-heading]")}
                  == {n for n, _ in EXPECTED_TASKS})
    results.check("the Answer Key states that Task 2 is not keyed",
                  "Task 2 is not keyed" in answer_text)
    results.check("no learner page prints internal grading policy",
                  not any(phrase in texts[role].lower() for role in LEARNER_ROLES
                          for phrase in ("not graded", "not scored", "ungraded",
                                         "for participation only", "is not keyed")))

    # --- CER IS DECLINED, AND THE DECLINE IS STRUCTURAL ----------------------
    cer = registry["cerDecision"]
    results.check("the registry records the CER decision with a rationale and a precedent",
                  cer["decision"] == "DECLINED" and len(cer["rationale"]) > 200
                  and len(cer["precedent"]) > 80)
    for selector in cer["prohibitedSelectors"]:
        results.check(f"no role renders the canonical CER component ({selector})",
                      not soup.select(selector))
    results.check("no layout area is locked for a CER reason",
                  not [a for block in (layout, layout["student"])
                       for a in block["lockedAreas"] if a["reason"] == "cer"])
    results.check("the culminating product is named as an engineered landscape explanation in both learner editions",
                  all(soup.select(f'section.page[data-role="{role}"] [data-landscape-explanation]')
                      for role in LEARNER_ROLES))

    # --- SOURCE STATUS -------------------------------------------------------
    bands = {band["id"]: band for band in status_contract["bands"]}
    source_layers = {s["id"]: s.get("evidenceLayer") for s in registry["caseSources"]}
    results.check("every canonical source declares a registered status band",
                  all(v in bands for v in source_layers.values()),
                  {k: v for k, v in source_layers.items() if v not in bands})
    results.check("the status contract is enforced in every role",
                  tuple(status_contract["enforcedRoles"]) == ALL_ROLES,
                  status_contract["enforcedRoles"])
    results.check("the status vocabulary is the canonical four",
                  set(status_contract["statusVocabulary"])
                  == {"reconstructed game evidence", "documented", "historical map",
                      "curriculum-original schematic"},
                  status_contract["statusVocabulary"])
    results.check("the four declared evidence-layer values are the ones the markup uses",
                  set(status_contract["layerValues"])
                  == {node.get("data-evidence-layer") for node in soup.select("[data-evidence-layer]")},
                  sorted({node.get("data-evidence-layer") for node in soup.select("[data-evidence-layer]")}))

    evidence_objects = soup.select("[data-source-id]")
    results.check("at least one evidence object exists", bool(evidence_objects))
    for node in evidence_objects:
        page = node.find_parent(class_="page")
        if page is None:
            continue
        page_id = page.get("data-page-id")
        ids = node.get("data-source-id").split()
        unknown = [i for i in ids if i not in source_layers]
        results.check(f"{page_id}: every data-source-id resolves to a canonical source",
                      not unknown, unknown)
        declared = node.get("data-evidence-layer")
        results.check(f"{page_id}: declared band is a registered band", declared in bands, declared)
        for source_id in ids:
            results.check(f"{page_id}: {source_id} markup band matches the registry",
                          source_layers.get(source_id) == declared,
                          f"markup {declared} vs registry {source_layers.get(source_id)}")
        status = node.select_one(".source-status")
        results.check(f"{page_id}: the evidence object prints a SOURCE STATUS line", status is not None,
                      str(node)[:120])
        if status is not None and declared in bands:
            printed = normalise(status.get_text(" ", strip=True))
            results.check(f"{page_id}: the status line uses the controlled concise form",
                          printed.upper().startswith("SOURCE STATUS ")
                          and bands[declared]["label"].lower() in printed.lower(),
                          printed)
    # The visible provenance labels are the controlled short form and nothing else:
    # no production explanation may be printed inside a student-facing status band.
    allowed_status_lines = {normalise(f"SOURCE STATUS · {band['label']}").upper()
                            for band in status_contract["bands"]}
    printed_status_lines = {normalise(n.get_text(" ", strip=True)).upper()
                            for n in soup.select(".source-status")}
    results.check("every printed status line is one of the four controlled labels",
                  printed_status_lines <= allowed_status_lines,
                  sorted(printed_status_lines - allowed_status_lines))
    for role in LEARNER_ROLES:
        notice = soup.select_one(f'section.page[data-role="{role}"] [data-source-status-notice]')
        results.check(f"{role}: page 1 carries the source-status notice", notice is not None)
        if notice is None:
            continue
        results.check(f"{role}: the notice is on page 1",
                      notice.find_parent(class_="page") is pages_for(soup, role)[0])
        text = normalise(notice.get_text(" ", strip=True)).lower()
        for band in status_contract["bands"]:
            results.check(f"{role}: the notice names the {band['id']} band by its printed label",
                          band["label"].lower() in text, band["label"])
        results.check(f"{role}: the notice states the non-merger rule in both directions",
                      "cannot establish what happened in 1487" in text
                      and "cannot prove any event in the game" in text, text[:260])
    fictional_nodes = soup.select("[data-fictional-data]")
    results.check("the packet marks its invented case data", len(fictional_nodes) >= 8,
                  len(fictional_nodes))
    for node in fictional_nodes:
        holder = node.find_parent(attrs={"data-evidence-layer": True})
        results.check("invented data sits inside a reconstructed evidence object",
                      holder is not None and holder.get("data-evidence-layer") == "reconstructed",
                      str(node)[:120])
    for source in registry["caseSources"]:
        results.check(f"source {source['id']} declares a contribution and a limitation",
                      len(source.get("contribution", "")) > 40
                      and len(source.get("limitation", "")) > 40, source["id"])
    results.check("the documented layer holds exactly the two certified real-world source cards",
                  [s["id"] for s in registry["caseSources"] if s["evidenceLayer"] == "documented"]
                  == ["fao-chinampas", "inah-record"])
    results.check("the historical-map layer holds exactly the certified published plan",
                  [s["id"] for s in registry["caseSources"] if s["evidenceLayer"] == "historical-map"]
                  == ["loc-plan"])
    results.check("every reconstructed source names the strand it supplies",
                  all("evidenceStrand" in s for s in registry["caseSources"]
                      if s["evidenceLayer"] == "reconstructed"))

    # Declared learner fallback pages must actually carry the source they name.
    PAGE_CLAIM = re.compile(r"(Student|Accessible) pages? ((?:\d+)(?:(?:,| and| to) \d+)*)", re.I)
    for source in registry["caseSources"]:
        for role_word, numbers in PAGE_CLAIM.findall(source.get("fallbackCorrespondence", "")):
            role = role_word.lower()
            declared = {int(n) for n in re.findall(r"\d+", numbers)}
            actual = {int(page.get("data-page-id").rsplit("-", 1)[1])
                      for page in pages_for(soup, role)
                      if page.select(f'[data-source-id~="{source["id"]}"]')}
            results.check(
                f"{source['id']}: declared {role} page(s) {sorted(declared)} carry the source",
                declared <= actual,
                f"declared {sorted(declared)}, source actually appears on {sorted(actual)}")

    # The Teacher evidence-architecture table states the same fallback locations a
    # second time. Nothing compared the two, and a table saying "Accessible page 5"
    # beside a registry saying page 6 is the kind of drift a teacher discovers in
    # front of a class. Both are now read from the same page map.
    arch_rows = soup.select('section.page[data-role="teacher"] .source-table tbody tr')
    arch_claims = {}
    for row in arch_rows:
        cells = row.find_all(["th", "td"])
        if len(cells) < 5:
            continue
        arch_claims[normalise(cells[0].get_text(" ", strip=True))] = \
            normalise(cells[-1].get_text(" ", strip=True))
    for source in registry["caseSources"]:
        declared = normalise(source.get("fallbackCorrespondence", ""))
        row_key = next((k for k in arch_claims if k.lower().startswith(
            source["displayLabel"].split(" ", 1)[0].lower() + " ")), None)
        if row_key is None or source["evidenceLayer"] == "curriculum-model":
            continue
        results.check(f"Teacher evidence architecture states the same location as the registry for {source['id']}",
                      arch_claims[row_key] == declared,
                      json.dumps({"teacher": arch_claims[row_key], "registry": declared}))

    # --- CASE-LOCAL SOURCE CERTIFICATION ------------------------------------
    certification = registry["sourceCertification"]
    results.check("the certification record reuses the Phase 1 source without modifying the audit",
                  certification["auditReused"] == [{"auditId": "H12", "caseSourceId": "fao-chinampas",
                                                    "note": certification["auditReused"][0]["note"]}]
                  and "No audit record is modified" in certification["auditReused"][0]["note"],
                  json.dumps(certification["auditReused"]))
    certified_ids = {c["caseSourceId"] for c in certification["caseCertified"]}
    results.check("every real-world source card carries a case-local certification entry",
                  certified_ids == {s["id"] for s in registry["caseSources"]
                                    if s["evidenceLayer"] in {"documented", "historical-map"}},
                  sorted(certified_ids))
    for entry_c in certification["caseCertified"]:
        label = entry_c["caseSourceId"] + (" / " + entry_c["strand"] if entry_c.get("strand") else "")
        results.check(f"certification {label} names a citation, its supported claims and its bounds",
                      len(entry_c.get("citation", "")) > 40
                      and len(entry_c.get("supports", [])) >= 4
                      and len(entry_c.get("doesNotSupport", [])) >= 3,
                      label)
    hydraulic = next(c for c in certification["caseCertified"] if c.get("strand") == "hydraulic works")
    results.check("the hydraulic-works certification expressly refuses the game's east-west overlay",
                  any("east-and-west" in item for item in hydraulic["doesNotSupport"]),
                  hydraulic["doesNotSupport"])
    results.check("the certification closes the estate against uncertified claims",
                  "source-certification dependency for the PMO" in certification["noFurtherClaims"])

    # --- THE NO-GAME DOSSIER -------------------------------------------------
    no_game = registry["noGameRoute"]
    results.check("the no-game contract names the five reconstructed dossier sources",
                  no_game["dossier"] == ["field-testimony", "plot-soil", "lake-works",
                                         "harvest-record", "collapse-account"],
                  no_game["dossier"])
    results.check("the four required reconstructed evidence strands are all declared",
                  {s["id"] for s in no_game["requiredStrands"]}
                  == {"cultivation", "soil", "waterworks", "harvest-record"},
                  [s["id"] for s in no_game["requiredStrands"]])
    strand_sources = {s["source"] for s in no_game["requiredStrands"]}
    results.check("every required strand names a canonical reconstructed source",
                  all(source_layers.get(s) == "reconstructed" for s in strand_sources), sorted(strand_sources))
    for role in no_game["requiredInRoles"]:
        for source_id in no_game["dossier"]:
            results.check(f"{role}: dossier source {source_id} is printed in the learner packet",
                          bool(soup.select(f'section.page[data-role="{role}"] '
                                           f'[data-source-id~="{source_id}"]')), source_id)
    for role in LEARNER_ROLES:
        for source_id in ("loc-plan", "fao-chinampas", "inah-record"):
            results.check(f"{role}: certified real-world source {source_id} is printed in the learner packet",
                          bool(soup.select(f'section.page[data-role="{role}"] '
                                           f'[data-source-id~="{source_id}"]')), source_id)
    results.check("Teacher supplies both routes and states that Campaign 2 has no launch shortcut",
                  "Game route" in teacher_text and "No-game route" in teacher_text
                  and "no level selector and no shortcut" in teacher_text)
    results.check("Teacher supplies a complete no-game evidence digest",
                  "Complete no-game evidence digest" in teacher_text)
    # Nothing in the packet may reproduce the runtime's resolution prose, its
    # candidate-record labels or its answer-revealing companion hints. That
    # prohibition is absolute and applies to every role, learner and teacher alike.
    RUNTIME_RESOLUTION = ("The Record Validates", "A triumph recast",
                          "farmed the valley to death", "The Untouched Lake",
                          "the gardens were simply perfect, forever",
                          "named plots, counted seasons, generations of tallies",
                          "Corruption Scout", "Keeper of the Chain",
                          "the best forgeries which borrow real fears")
    for role in ALL_ROLES:
        leaked = [t for t in RUNTIME_RESOLUTION if t.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime resolution, candidate label or hint text is reproduced",
                      not leaked, leaked)
    # On-screen control labels are a narrower class. A Teacher naming the button a
    # class will actually press is helping them run the level; a learner page that
    # named it would be assuming gameplay the no-game route does not have.
    RUNTIME_UI_LABELS = ("Validate the Record", "The evidence is incomplete", "Which record is genuine?",
                         "Speak to the Farmer", "Examine the Soil", "Survey the Waterworks",
                         "Read the Harvest Codex", "Read the Collapse Account", "Watch the Canoe Traffic",
                         "Speak to the Keeper")
    for role in LEARNER_ROLES + ("answer",):
        leaked = [t for t in RUNTIME_UI_LABELS if t.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime control label is printed", not leaked, leaked)

    # --- H3: THE SOURCED HISTORICAL MAP AND ITS LIMIT ------------------------
    loc = next(s for s in registry["caseSources"] if s["id"] == "loc-plan")
    results.check("the map source names its publication, its place and its year",
                  "1524" in loc["creator"] and "Nuremberg" in loc["creator"]
                  and "Library of Congress" in loc["creator"], loc["creator"])
    results.check("the map source states the 1487 limit in its registered limitation",
                  "1487" in loc["limitation"] and "1520" in loc["limitation"], loc["limitation"])
    for role in LEARNER_ROLES:
        card = soup.select_one(f'section.page[data-role="{role}"] [data-source-id~="loc-plan"]')
        results.check(f"{role}: the historical-map source card is present", card is not None)
        if card is None:
            continue
        text = normalise(card.get_text(" ", strip=True))
        results.check(f"{role}: the map card is declared as the historical-map band",
                      card.get("data-evidence-layer") == "historical-map", card.get("data-evidence-layer"))
        for fragment in ("1524", "1520", "island in the salt lake of Texcoco",
                         "causeways connect the island city to the shores",
                         "oriented with west at the top"):
            results.check(f"{role}: the map card records “{fragment[:44]}…”",
                          fragment.lower() in text.lower(), text[:220])
        limit = card.select_one("[data-map-limit='not-1487']")
        results.check(f"{role}: the map card prints its date and provenance limit", limit is not None)
        if limit is not None:
            limit_text = normalise(limit.get_text(" ", strip=True))
            results.check(f"{role}: the printed limit says plainly that this is not a 1487 picture",
                          "not a picture of the city in 1487" in limit_text, limit_text[:200])
        figure = soup.select_one(f'section.page[data-role="{role}"] [data-map-contract]')
        results.check(f"{role}: the adapted lake-city figure is present", figure is not None)
        if figure is None:
            continue
        fig_text = normalise(figure.get_text(" ", strip=True))
        for fragment in ("THE ISLAND CITY", "CAUSEWAYS", "LAKE", "LAKESHORE"):
            results.check(f"{role}: the map figure prints {fragment}", fragment in fig_text.upper(), fragment)
        # The connectors are finite strokes and are visible as such. What the figure
        # must refuse is not the existence of a drawn count but the reading of that
        # count as the source's; the printed note says exactly that.
        results.check(f"{role}: the map figure refuses the historical reading of its own drawn connectors",
                      "not historical measurements" in fig_text
                      and "at uneven lengths and angles" in fig_text, fig_text[:240])
        results.check(f"{role}: the map figure states what the shoreline treatment does and does not show",
                      "The plan names settlements around the lake" in fig_text
                      and "shows only that they ring the water" in fig_text, fig_text[:240])
        results.check(f"{role}: the map figure states the source's own orientation rather than imitating it",
                      "oriented with west at the top" in fig_text
                      and "No number, position, direction, distance, shape or size may be read" in fig_text,
                      fig_text[:240])
        # The enumeration guards run against the printed figure text as well as the
        # accessibility text, because a learner-facing count would be the same defect.
        for pattern in next(f for f in registry["figureContract"]["figures"]
                            if f["id"] == "lake-city-plan")["prohibitedPatterns"]:
            hit = re.search(pattern["regex"], fig_text, re.I)
            results.check(f"{role}: the printed map figure text avoids {pattern['id']}",
                          hit is None, (hit.group(0) if hit else "") + " :: " + pattern["why"])
        root = figure_root(figure)
        caption = root.find("figcaption") if root is not None else None
        cap_text = normalise(caption.get_text(" ", strip=True)) if caption else ""
        for term in ("ADAPTED FROM", "LIBRARY OF CONGRESS", "RECONSTRUCTION", "NOT TO SCALE"):
            results.check(f"{role}: the map figure caption carries the {term} status term",
                          term in cap_text.upper(), cap_text[:220])
        results.check(f"{role}: the map figure is declared a curriculum schematic, not the evidence itself",
                      figure.get("data-evidence-layer") == "curriculum-model"
                      and "this drawing organises it" in cap_text.lower(), cap_text[:200])

    map_contract = next(f for f in registry["figureContract"]["figures"] if f["id"] == "lake-city-plan")
    results.check("the map figure contract declares the schematic-connector rule rather than an impossible one",
                  "representative causeway connections" in map_contract["schematicConnectorRule"]
                  and "must not be interpreted or asserted as the historical count"
                  in map_contract["schematicConnectorRule"]
                  and "no learner-facing prose or accessibility text may claim"
                  in map_contract["schematicConnectorRule"]
                  and "ADAPTED FROM, RECONSTRUCTION and NOT TO SCALE" in map_contract["schematicConnectorRule"],
                  map_contract.get("schematicConnectorRule", "")[:300])
    results.check("the map figure contract declares the schematic-settlement rule",
                  "may not carry a settlement count" in map_contract["schematicSettlementRule"]
                  and "grouped rather than enumerable" in map_contract["schematicSettlementRule"],
                  map_contract.get("schematicSettlementRule", "")[:300])
    results.check("the contract still forbids enumerating connectors or settlements",
                  {p["id"] for p in map_contract["prohibitedPatterns"]}
                  == {"invented-distance", "exact-1487", "enumerated-connectors", "enumerated-settlements"},
                  sorted(p["id"] for p in map_contract["prohibitedPatterns"]))
    # The certification must carry the two directly observed relationships the drawing
    # now rests on, and must refuse the precision it does not have.
    loc_cert = next(c for c in registry["sourceCertification"]["caseCertified"]
                    if c["caseSourceId"] == "loc-plan")
    results.check("the LOC certification records the observed shoreline settlement relationship",
                  any("settlements around the lake and along its shores" in s for s in loc_cert["supports"]),
                  loc_cert["supports"])
    results.check("the LOC certification records the observed uneven causeway arrangement",
                  any("visibly uneven lengths and angles" in s for s in loc_cert["supports"]),
                  loc_cert["supports"])
    results.check("the LOC certification refuses a settlement count, placement and shoreline geometry",
                  any("any number of settlements" in s for s in loc_cert["doesNotSupport"])
                  and any("shoreline geometry" in s for s in loc_cert["doesNotSupport"])
                  and any("as it stood in 1487" in s for s in loc_cert["doesNotSupport"]),
                  loc_cert["doesNotSupport"])
    # The same sweep across every role's prose, with registered exemption subtrees
    # removed: a Teacher misconception row and an Answer Key floor exist precisely to
    # quote the claim they refuse, and quoting it is not asserting it.
    exemption_specs = {e["id"]: e for e in registry["semanticInvariants"]["exemptions"]}
    unexempt = {}
    for role in ALL_ROLES:
        parts = []
        for page in pages_for(soup, role):
            parts.extend(text for _n, text, _a in leaf_blocks(page, exemption_specs, role))
        unexempt[role] = normalise(" ".join(parts))
    enumerations = [(role, p["id"], re.search(p["regex"], unexempt[role], re.I).group(0))
                    for role in ALL_ROLES for p in map_contract["prohibitedPatterns"]
                    if re.search(p["regex"], unexempt[role], re.I)]
    results.check("no role enumerates the schematic connectors or the shoreline settlements",
                  not enumerations, enumerations)
    results.check("the retired alt-text enumeration appears nowhere in the package",
                  not any("four straight bands" in texts[role].lower() for role in ALL_ROLES))

    # --- H8: THE ENGINEERED SYSTEM AT TWO SCALES -----------------------------
    model = registry["systemModel"]
    results.check("the system model refuses to reproduce the game's hydrology overlay as history",
                  "is NOT reproduced as documented history" in model["rule"], model["rule"][:200])
    results.check("the basin panel declares its restraint about direction and salinity",
                  "assigns no compass direction" in model["basinScale"]["restraint"]
                  and "states no salinity" in model["basinScale"]["restraint"])
    results.check("the stabilising vegetation is included only because a certified source states it",
                  model["fieldScale"]["stabilisingVegetation"]["certifiedBy"] == "fao-chinampas"
                  and "the certified source states it directly"
                  in model["fieldScale"]["stabilisingVegetation"]["why"])
    results.check("the required status terms for the system figure are the accurate ones",
                  model["requiredStatusTerms"]
                  == ["CURRICULUM-ORIGINAL SCHEMATIC", "BASED ON", "RECONSTRUCTION", "NOT TO SCALE"],
                  model["requiredStatusTerms"])
    for role in LEARNER_ROLES:
        figure = soup.select_one(f'section.page[data-role="{role}"] [data-system-contract]')
        results.check(f"{role}: the two-scale system figure is present", figure is not None)
        if figure is None:
            continue
        fig_text = normalise(figure.get_text(" ", strip=True))
        for component in model["fieldScale"]["components"] + model["basinScale"]["components"]:
            results.check(f"{role}: the system figure prints the component {component}",
                          component in fig_text.upper(), component)
        results.check(f"{role}: the system figure prints both scale labels",
                      "FIELD SCALE" in fig_text.upper() and "BASIN SCALE" in fig_text.upper(), fig_text[:200])
        results.check(f"{role}: the system figure prints the stabilising vegetation the source certifies",
                      "ahuejote" in fig_text.lower(), fig_text[:200])
        results.check(f"{role}: the system figure prints the soil-renewal relationship",
                      "lifted from the canal floor onto the plot" in fig_text, fig_text[:220])
        results.check(f"{role}: the system figure joins the two scales rather than juxtaposing them",
                      normalise(model["joiningStatement"]) in fig_text, fig_text[:220])
        rule_node = figure.select_one("[data-terminology-rule='not-floating']")
        results.check(f"{role}: the printed not-floating rule sits inside the system figure",
                      rule_node is not None
                      and "built up from the lake bottom" in normalise(rule_node.get_text(" ", strip=True))
                      and "does not float" in normalise(rule_node.get_text(" ", strip=True)),
                      normalise(rule_node.get_text(" ", strip=True)) if rule_node else "missing")
        root = figure_root(figure)
        caption = root.find("figcaption") if root is not None else None
        cap_text = normalise(caption.get_text(" ", strip=True)) if caption else ""
        for term in ("BASED ON", "RECONSTRUCTION", "NOT TO SCALE"):
            results.check(f"{role}: the system figure caption carries the {term} status term",
                          term in cap_text.upper(), cap_text[:220])
        results.check(f"{role}: the system figure caption refuses to be read as evidence",
                      "not evidence about any particular field" in cap_text.lower(), cap_text[:200])
        results.check(f"{role}: no measurement is offered as readable from the system figure",
                      "no measurement may be read from it" in cap_text.lower(), cap_text[:200])

    # The Accessible edition supplies no figure label the Student edition lacks; the
    # figures are intentionally identical, and no role may claim otherwise.
    results.check("no role claims an Accessible figure-label support that does not exist",
                  not any("selected labels" in texts[role].lower() for role in ALL_ROLES),
                  [role for role in ALL_ROLES if "selected labels" in texts[role].lower()])
    def described_alt(role: str, contract: str) -> str:
        node = soup.select_one(f'section.page[data-role="{role}"] [{contract}] [role="img"][aria-label]')
        return normalise(node.get("aria-label")) if node is not None else ""

    for figure_id, contract in (("lake-city-plan", "data-map-contract"),
                                ("chinampa-system", "data-system-contract")):
        student_alt = described_alt("student", contract)
        accessible_alt = described_alt("accessible", contract)
        results.check(f"{figure_id} is identical in both learner editions, as declared",
                      bool(student_alt) and student_alt == accessible_alt,
                      json.dumps({"studentLen": len(student_alt), "accessibleLen": len(accessible_alt)}))
    # The H8 accessibility text describes the cue the figure actually renders.
    for role in LEARNER_ROLES:
        alt = described_alt(role, "data-system-contract")
        results.check(f"{role}: the H8 accessibility text names the soil-renewal cue that is drawn",
                      "upward soil-renewal cue" in alt.lower(), alt[:240])
        results.check(f"{role}: the H8 accessibility text describes no arrow the figure does not draw",
                      "arrow runs from the canal floor" not in alt.lower(), alt[:240])
        cue = soup.select_one(f'section.page[data-role="{role}"] [data-system-contract] .chs-flow')
        results.check(f"{role}: the soil-renewal cue is actually rendered beneath the panel",
                      cue is not None and "Soil renewal" in normalise(cue.get_text(" ", strip=True)),
                      normalise(cue.get_text(" ", strip=True)) if cue else "missing")
    # Source count and card count are different facts and both must stay true.
    results.check("the Teacher Guide counts the four certified real-world sources",
                  "Four published sources support everything this packet claims" in teacher_text)
    results.check("the Teacher Guide still counts the three real-world source cards the learner holds",
                  "all three real-world source cards" in teacher_text
                  and "three real-world source cards under printed status lines" in teacher_text)
    results.check("the four-source estate and the three-card packet are separately stated",
                  len(registry["sourceCertification"]["caseCertified"]) == 4
                  and len([s for s in registry["caseSources"]
                           if s["evidenceLayer"] in {"documented", "historical-map"}]) == 3)

    # --- H4: THE CONTRIBUTION AND LIMITATION MATRIX --------------------------
    for role in LEARNER_ROLES:
        table = soup.select_one(f'section.page[data-role="{role}"] .contribution-table')
        results.check(f"{role}: the contribution-and-limitation matrix is present", table is not None)
        if table is None:
            continue
        headers = [normalise(th.get_text(" ", strip=True)).lower() for th in table.select("thead th")]
        results.check(f"{role}: the matrix asks for a contribution and a limit",
                      any("contribut" in h for h in headers) and any("cannot establish" in h for h in headers),
                      headers)
        rows = [normalise(tr.select_one('th[scope="row"]').get_text(" ", strip=True))
                for tr in table.select("tbody tr")]
        results.check(f"{role}: the matrix carries exactly the four source classes", len(rows) == 4, rows)
        for needle in ("Reconstructed game evidence", "FAO", "INAH", "1524 published plan"):
            results.check(f"{role}: the matrix names the {needle} class",
                          any(needle.lower() in r.lower() for r in rows), rows)

    # --- TASK 6: THE TWO EVIDENCE LAYERS DO NOT JOIN -------------------------
    layers = registry["evidenceLayers"]
    results.check("the layer contract names an inside band and an outside band",
                  [b["label"] for b in layers["bands"]] == ["INSIDE THE GAME", "OUTSIDE THE GAME"],
                  [b["label"] for b in layers["bands"]])
    inside_sources = next(b for b in layers["bands"] if b["id"] == "inside")["sources"]
    outside_sources = next(b for b in layers["bands"] if b["id"] == "outside")["sources"]
    results.check("the inside band holds only reconstructed sources",
                  all(source_layers.get(s) == "reconstructed" for s in inside_sources), inside_sources)
    results.check("the outside band holds only certified real-world sources",
                  all(source_layers.get(s) in {"documented", "historical-map"} for s in outside_sources),
                  outside_sources)
    results.check("no source appears in both bands", not set(inside_sources) & set(outside_sources))
    results.check("the layer contract requires the two layers to be answered separately",
                  layers["separateResponsesRequired"] is True)
    for role in layers["roles"]:
        organiser = soup.select_one(f'section.page[data-role="{role}"] [data-layer-contract]')
        results.check(f"{role}: the two-layer organiser is present", organiser is not None)
        if organiser is None:
            continue
        text = normalise(organiser.get_text(" ", strip=True))
        for band in layers["bands"]:
            results.check(f"{role}: the organiser prints the band {band['label']}",
                          band["label"] in text.upper(), band["label"])
        results.check(f"{role}: the organiser prints the rule that the layers do not join",
                      normalise(layers["printedRule"]) in text, text[:200])
        results.check(f"{role}: the organiser prints the move it refuses",
                      "from the game's evidence to history" in text.lower()
                      and "is not a move this case allows" in text.lower(), text[:200])
        results.check(f"{role}: the organiser scopes each band to its own sources",
                      "Sources A to E" in text and "Sources F to H" in text, text[:240])

    # --- THE TERMINOLOGY RULE: POSITIVE REQUIREMENTS ------------------------
    for requirement in qualification["positiveRequirements"]:
        for role in requirement["roles"]:
            found = soup.select(f'section.page[data-role="{role}"] {requirement["selector"]}')
            results.check(f"{role}: positive requirement {requirement['id']} is printed",
                          bool(found), requirement["selector"])
    for role in qualification["requiredPrintedStatementRoles"]:
        for statement in qualification["requiredPrintedStatements"]:
            results.check(f"{role}: prints the required statement “{statement[:46]}…”",
                          normalise(statement).lower() in texts[role].lower(), statement)
    for role in LEARNER_ROLES:
        nickname = soup.select_one(f'section.page[data-role="{role}"] [data-terminology-rule="nickname"]')
        results.check(f"{role}: the nickname qualification is printed", nickname is not None)
        if nickname is None:
            continue
        text = normalise(nickname.get_text(" ", strip=True))
        results.check(f"{role}: the nickname qualification reports the source's own wording",
                      "floating artificial islands" in text.lower(), text[:220])
        results.check(f"{role}: the nickname qualification names it as a nickname",
                      "conventional nickname" in text.lower(), text[:220])
        results.check(f"{role}: the nickname qualification sets the construction beside the nickname",
                      "staked structure" in text.lower()
                      and "built up from the lake bottom" in text.lower(), text[:260])
    # The overcorrection is refused in the learner packet too, not only in the guide.
    for role in LEARNER_ROLES:
        results.check(f"{role}: the packet records that the basin's water works were rebuilt after flooding",
                      "1604" in texts[role] and "1856" in texts[role], texts[role][:0])

    # --- SEMANTIC GUARDS: POSITIVE CONTROL (the package itself) --------------
    invariants = registry["semanticInvariants"]
    exemptions = {e["id"]: e for e in invariants["exemptions"]}
    compiled = compile_classes(qualification["prohibitedFramings"])
    results.check("all three prohibited concept classes compile",
                  set(compiled) == {"chinampasFloat", "reconstructionAsPrimary", "mapAsExactSnapshot"},
                  sorted(compiled))
    for role in ALL_ROLES:
        violations = scan_html(html, compiled, exemptions, role)
        results.check(f"{role}: no unexempted proposition states a prohibited framing",
                      not violations, json.dumps(violations[:6], indent=1))

    # --- SEMANTIC GUARDS: NEGATIVE CONTROLS ---------------------------------
    for class_id, sentences in qualification["negativeControls"].items():
        results.check(f"negative controls exist for {class_id}", len(sentences) >= 3, sentences)
        for sentence in sentences:
            hits = scan_html(synthetic("student", f"<p>{sentence}</p>"), compiled, exemptions, "student")
            results.check(f"negative control fires for {class_id}: {sentence[:52]}",
                          any(h[2] == class_id for h in hits), hits)

    # --- SEMANTIC GUARDS: POSITIVE (MUST-NOT-FLAG) CONTROLS -----------------
    # Truthful prose the guards must leave alone, including the five sentences the
    # PMO named as required-legal. These confer no authority: authored wording this
    # list has never seen is expected to pass, and does.
    REQUIRED_LEGAL = [
        "“Floating gardens” is a conventional nickname.",
        "Chinampas are raised fields constructed in wetlands.",
        "The game reconstructs a plausible scene for investigation.",
        "The 1524 published map can provide geographic evidence while still having limits.",
        "Historical evidence supports chinampa agriculture without proving every detail of the game scene.",
    ]
    results.check("the registry carries every required positive control",
                  all(s in qualification["positiveControls"] for s in REQUIRED_LEGAL),
                  [s for s in REQUIRED_LEGAL if s not in qualification["positiveControls"]])
    for sentence in qualification["positiveControls"]:
        hits = scan_html(synthetic("student", f"<p>{sentence}</p>"), compiled, exemptions, "student")
        results.check(f"truthful prose is not flagged: {sentence[:52]}", not hits, hits)

    # --- EXEMPTION CONTRACT IS CLOSED ---------------------------------------
    declared_exemptions = set(exemptions)
    used = {n.get("data-semantic-exemption") for n in soup.select("[data-semantic-exemption]")}
    results.check("every exemption used in markup is registered",
                  used <= declared_exemptions, sorted(used - declared_exemptions))
    results.check("no learner edition uses a semantic exemption at all",
                  not soup.select('section.page[data-role="student"] [data-semantic-exemption]')
                  and not soup.select('section.page[data-role="accessible"] [data-semantic-exemption]'))
    for node in soup.select("[data-semantic-exemption]"):
        eid = node.get("data-semantic-exemption")
        page = node.find_parent(class_="page")
        if page is None or eid not in exemptions:
            continue
        results.check(f"exemption {eid} is used only in a role it declares",
                      page.get("data-role") in exemptions[eid]["roles"],
                      f"{eid} on {page.get('data-role')}")
    for spec in exemptions.values():
        unknown = [c for c in spec["allowedConcepts"] if c not in compiled]
        results.check(f"exemption {spec['id']} allows only registered concept classes",
                      not unknown, unknown)
    forged = synthetic("student", '<p data-semantic-exemption="not-a-registered-id">'
                                  'Chinampas were floating rafts.</p>')
    results.check("mutation control: an unregistered exemption id excuses nothing",
                  bool(scan_html(forged, compiled, exemptions, "student")))
    wrong_role = synthetic("student", '<p data-semantic-exemption="teacher-misconception">'
                                      'Chinampas were floating rafts.</p>')
    results.check("mutation control: an exemption does not carry into a role it does not declare",
                  bool(scan_html(wrong_role, compiled, exemptions, "student")))

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
        results.check(f"{edition}: no response id is claimed by two subparts",
                      len(listed) == len(set(listed)))
        results.check(f"{edition}: declared identity fields exist and are not assessed",
                      identity <= set(live) and not (identity & set(listed)))
    for sub in subparts:
        label = f"{sub['task']} {sub['id']}"
        klass, ns, na = sub["differenceClass"], len(sub["student"]), len(sub["accessible"])
        results.check(f"{label}: has no Accessible-only obligation", ns > 0,
                      "an Accessible response with no Student counterpart is a demand increase")
        results.check(f"{label}: names a real task", any(t["id"] == sub["task"] for t in tasks))
        if klass == "parity":
            results.check(f"{label}: declared parity holds", ns == na, f"{ns} vs {na}")
        elif klass == "declared-reduction":
            results.check(f"{label}: reduction is real and registered",
                          na < ns and sub.get("governedBy") in adaptation_ids,
                          f"{ns} -> {na}, governedBy={sub.get('governedBy')}")
        elif klass == "chunking":
            results.check(f"{label}: chunking splits rather than adds demand",
                          na >= ns and "chunkingNote" in sub, f"{ns} -> {na}")
        else:
            results.check(f"{label}: declares a known difference class", False, klass)
        if na > ns:
            results.check(f"{label}: an Accessible field increase is only ever a declared chunking split",
                          klass == "chunking", klass)
    results.check("the contract forbids an accessible-only obligation class",
                  erc["differenceClasses"]["accessible-only"].startswith("PROHIBITED"))
    results.check("every task with assessed responses is represented in the parity contract",
                  {sub["task"] for sub in subparts} == {t["id"] for t in tasks},
                  sorted({sub["task"] for sub in subparts}))
    results.check("Task 7 collects the two evidence links as separate scored responses in both editions",
                  next(s for s in subparts if s["id"] == "evidence-links")["student"]
                  == ["t7-link-1", "t7-link-2"]
                  and next(s for s in subparts if s["id"] == "evidence-links")["accessible"]
                  == ["a7-link-1", "a7-link-2"])
    results.check("Task 7 collects the source qualification as its own scored response in both editions",
                  next(s for s in subparts if s["id"] == "source-qualification")["differenceClass"] == "parity")
    for role in LEARNER_ROLES:
        block = soup.select_one(f'section.page[data-role="{role}"] [data-landscape-explanation]')
        results.check(f"{role}: the explanation asks for two links from different sources in print",
                      block is not None and "different" in normalise(block.get_text(" ", strip=True)).lower(),
                      normalise(block.get_text(" ", strip=True))[:200] if block else "missing")
        directions = [normalise(d.get_text(" ", strip=True)).lower()
                      for d in soup.select(f'section.page[data-role="{role}"] .directions')]
        results.check(f"{role}: the printed directions require two different real-world sources",
                      any("two different real-world sources or figures" in d for d in directions), directions[-3:])

    # --- ACCESSIBLE ADAPTATIONS ARE TRUE AND DECLARED -----------------------
    adaptations = registry["accessibleAdaptations"]
    results.check("exactly four Accessible adaptations are declared, and no fifth has appeared",
                  len(adaptations) == 4, sorted(adaptation_ids))
    for adaptation in adaptations:
        task = next(t for t in tasks if t["id"] == adaptation["task"])
        label = normalise(f"{task['number']} · {task['title']}")
        results.check(f"adaptation {adaptation['id']} is disclosed to the teacher",
                      label in teacher_text, adaptation["id"])
        for role in adaptation["declaredIn"]:
            results.check(f"adaptation {adaptation['id']} declares a real role", role in ALL_ROLES, role)
        results.check(f"adaptation {adaptation['id']} explains why it is not a leak",
                      len(adaptation.get("whyNotALeak", "")) > 60, adaptation["id"])
    marked = {n.get("data-accessible-adaptation") for n in soup.select("[data-accessible-adaptation]")}
    results.check("every adaptation marked in the Accessible markup is registered",
                  marked <= adaptation_ids, sorted(marked - adaptation_ids))
    results.check("all four declared adaptations are actually present in the Accessible edition",
                  marked == adaptation_ids, sorted(adaptation_ids - marked))
    results.check("every marked adaptation sits in the Accessible edition and nowhere else",
                  all(n.find_parent(class_="page").get("data-role") == "accessible"
                      for n in soup.select("[data-accessible-adaptation]")))
    results.check("the Accessible worked examples are printed as examples rather than as blanks",
                  all("WORKED EXAMPLE" in normalise(n.get_text(" ", strip=True)).upper()
                      for n in soup.select('section.page[data-role="accessible"] '
                                           '[data-accessible-adaptation="t3-supplied-setting"], '
                                           'section.page[data-role="accessible"] '
                                           '[data-accessible-adaptation="t4-modelled-relationship"], '
                                           'section.page[data-role="accessible"] '
                                           '[data-accessible-adaptation="t5-modelled-row"]')))
    prefilled = soup.select('section.page[data-role="accessible"] .contribution-table .prefilled')
    results.check("the Accessible matrix supplies three prefilled cells and no more",
                  len(prefilled) == 3 and not soup.select('section.page[data-role="student"] '
                                                          '.contribution-table .prefilled'),
                  len(prefilled))
    results.check("the Teacher scoring note claims exactly four scored differences",
                  "Four scored differences, and only four" in teacher_text)
    results.check("the Answer Key discloses the same four scored differences",
                  "Four scored differences, and only four" in answer_text)

    # --- RESPONSE SPACE AND DIGITAL MARKABILITY -----------------------------
    for edition, block, prefix in (("student", layout["student"], "student"),
                                   ("accessible", layout, "accessible")):
        declared_ids = ({a["persistId"] for a in block["areas"]}
                        | {a["persistId"] for a in block["lockedAreas"]})
        found_ids = [n.get("data-persist-id") for n in
                     soup.select(f'section.page[data-role="{prefix}"] [data-response][data-persist-id]')]
        results.check(f"{edition}: every persistent response is layout-classified",
                      set(found_ids) == declared_ids,
                      json.dumps({"unclassified": sorted(set(found_ids) - declared_ids),
                                  "orphan": sorted(declared_ids - set(found_ids))}))
        results.check(f"{edition}: no persist id is used twice",
                      len(found_ids) == len(set(found_ids)))
    all_marks = soup.select('.page[data-role="student"] .mark-response, '
                            '.page[data-role="accessible"] .mark-response')
    results.check("every printed compact judgment slot in a learner edition is persistent",
                  all(m.has_attr("data-response") and m.has_attr("data-persist-id")
                      and (m.get("role") == "textbox") and (m.get("aria-label")) for m in all_marks),
                  len(all_marks))
    results.check("the Accessible bounded judgment slots exist and are the declared ones",
                  [m.get("data-persist-id") for m in
                   soup.select('.page[data-role="accessible"] .mark-response')]
                  == ["a8-physical", "a8-source"],
                  [m.get("data-persist-id") for m in
                   soup.select('.page[data-role="accessible"] .mark-response')])
    for role in LEARNER_ROLES:
        inline = soup.select(f'section.page[data-role="{role}"] .inline-response')
        results.check(f"{role}: every printed vocabulary blank is persistent",
                      bool(inline) and all(m.has_attr("data-response") and m.has_attr("data-persist-id")
                                           and (m.get("role") == "textbox")
                                           and (m.get("aria-label")) for m in inline), len(inline))
        cells = soup.select(f'section.page[data-role="{role}"] .table-response')
        results.check(f"{role}: every printed matrix cell response is persistent",
                      bool(cells) and all(m.has_attr("data-response") and m.has_attr("data-persist-id")
                                          and (m.get("role") == "textbox")
                                          and (m.get("aria-label")) for m in cells), len(cells))
    results.check("every response field in every role carries an accessible name",
                  all(n.get("aria-label") or n.get("aria-labelledby") for n in soup.select("[data-response]")))
    results.check("every figure that is not a data table carries accessibility text",
                  all(f.select_one("[role='img'][aria-label]") is not None
                      for f in soup.select("figure.case-figure")),
                  [f.get("data-figure-id") for f in soup.select("figure.case-figure")
                   if f.select_one("[role='img'][aria-label]") is None])

    # --- FIGURE CONTRACT -----------------------------------------------------
    for spec in registry["figureContract"]["figures"]:
        for role in spec["roles"]:
            figure = soup.select_one(f'section.page[data-role="{role}"] {spec["selector"]}')
            results.check(f"{role}: figure {spec['id']} is present", figure is not None, spec["selector"])
            if figure is None:
                continue
            described = figure if figure.get("role") == "img" and figure.get("aria-label") \
                else figure.select_one("[role='img'][aria-label]")
            results.check(f"{role}: figure {spec['id']} carries accessibility text", described is not None)
            if described is None:
                continue
            alt = normalise(described.get("aria-label"))
            for pattern in spec.get("prohibitedPatterns", []):
                hit = re.search(pattern["regex"], alt, re.I)
                results.check(f"{role}: {spec['id']} accessibility text avoids {pattern['id']}",
                              hit is None, (hit.group(0) if hit else "") + " :: " + pattern["why"])
            for fragment in spec.get("requiresAltConcepts", []):
                results.check(f"{role}: {spec['id']} accessibility text names {fragment}",
                              fragment.lower() in alt.lower(), fragment)
            for scale in spec.get("requiresScales", []):
                results.check(f"{role}: {spec['id']} accessibility text names the {scale}",
                              scale.lower() in alt.lower(), scale)
            if spec.get("requiresAdaptationNote"):
                results.check(f"{role}: {spec['id']} accessibility text carries the adaptation note",
                              spec["requiresAdaptationNote"].lower() in alt.lower(), alt[:220])
            if spec.get("requiresOrientationNote"):
                results.check(f"{role}: {spec['id']} accessibility text states the source's orientation",
                              spec["requiresOrientationNote"].lower() in alt.lower(), alt[:220])
            if spec.get("requiresNotFloatingStatement"):
                results.check(f"{role}: {spec['id']} accessibility text states that the field does not float",
                              spec["requiresNotFloatingStatement"].lower() in alt.lower(), alt[:220])
            root = figure_root(figure)
            caption = root.find("figcaption") if root is not None else None
            cap_text = normalise(caption.get_text(" ", strip=True)).upper() if caption else ""
            for term in spec.get("requiresCaptionTerms", []):
                results.check(f"{role}: {spec['id']} caption carries the status term {term}",
                              term.upper() in cap_text, cap_text[:220])
    results.check("no figure in the package uses imagery of any kind beyond the institutional insignia",
                  not soup.select('figure.case-figure img:not(.taa-insignia)'))
    results.check("no page references an external or generated image asset",
                  not [n.get("src") for n in soup.select("img") if "insignia" not in (n.get("src") or "")],
                  [n.get("src") for n in soup.select("img") if "insignia" not in (n.get("src") or "")])

    # --- PRINTABLE HYGIENE AND DOCUMENT SEMANTICS ---------------------------
    # The shared printable-metadata detectors are SSS-scoped in the static suite;
    # running them here gives this package the same protection without touching a
    # shared validator.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import validate_static  # noqa: E402  (imported late, and only for its detectors)
    results.check("no printable page carries production metadata or a status banner",
                  not validate_static.printable_production_metadata_findings(soup),
                  validate_static.printable_production_metadata_findings(soup))
    results.check("no printable heading announces owner review",
                  not validate_static.printable_owner_review_headings(soup),
                  validate_static.printable_owner_review_headings(soup))
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
                  tables and all(t.find("caption") and t.select("thead th")
                                 and t.select('tbody th[scope="row"]') for t in tables),
                  [normalise(t.get_text(" ", strip=True))[:60] for t in tables
                   if not (t.find("caption") and t.select("thead th")
                           and t.select('tbody th[scope="row"]'))])
    results.check("the package declares the language and the PDF-accessibility notice",
                  package["accessibility"]["language"] == "en"
                  and "does not guarantee PDF accessibility" in package["accessibility"]["pdfNotice"])
    results.check("production is HTML-only: no canonical PDF is declared anywhere in the package",
                  not any("pdf" in str(v).lower() for k, v in package["outputs"].items())
                  and all(str(v).endswith(".html") for v in package["outputs"].values()),
                  json.dumps(package["outputs"]))
    results.check("no generated role output is committed beside the sources",
                  not [p.name for p in SOURCE.iterdir()
                       if p.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".webp"}
                       or p.name.endswith("_CUSTOM.html")],
                  [p.name for p in SOURCE.iterdir()])
    results.check("no source file carries a machine-local path",
                  not [f.name for f in sorted(SOURCE.iterdir())
                       if re.search(r"/Users/|/home/|file:///|C:\\\\", f.read_text(encoding="utf-8"))],
                  [f.name for f in sorted(SOURCE.iterdir())
                   if re.search(r"/Users/|/home/|file:///", f.read_text(encoding="utf-8"))])

    # --- ANSWER KEY COVERAGE -------------------------------------------------
    for task in tasks:
        if not task["keyed"]:
            continue
        heading = soup.select_one(f'section.page[data-role="answer"] '
                                  f'[data-shell-task-heading="{task["number"]}"]')
        block = heading.find_next(class_="answer-block") if heading is not None else None
        results.check(f"Answer Key task {task['number']} carries a completed exemplar block",
                      block is not None and len(normalise(block.get_text(" ", strip=True))) > 200,
                      task["number"])
    results.check("the Answer Key completes every Task 1 vocabulary placement",
                  all(term in answer_text for term in registry["vocabulary"]))
    results.check("the Answer Key completes all four Task 3 parts",
                  all(f"Part {p} -" in answer_text for p in ("A", "B", "C", "D")))
    results.check("the Answer Key completes the Task 4 relationships rather than naming parts",
                  "staked out in shallow water" in answer_text
                  and "four jobs at once" in answer_text
                  and "never rested" in answer_text
                  and "reaches every plot at once" in answer_text)
    results.check("the Answer Key completes the Task 5 matrix as an actual matrix",
                  bool(soup.select('section.page[data-role="answer"] .key-matrix')))
    key_matrix = soup.select_one('section.page[data-role="answer"] .key-matrix')
    results.check("the completed matrix carries all four source classes with both columns filled",
                  key_matrix is not None
                  and len(key_matrix.select("tbody tr")) == 4
                  and all(len(tr.select("td")) == 2 and all(normalise(td.get_text(" ", strip=True))
                                                            for td in tr.select("td"))
                          for tr in key_matrix.select("tbody tr")),
                  len(key_matrix.select("tbody tr")) if key_matrix else "missing")
    results.check("the Answer Key completes both Task 6 layers separately",
                  "Inside the game -" in answer_text and "Outside the game -" in answer_text)
    results.check("the Task 6 exemplar refuses the merger in both directions",
                  "reaches for FAO or INAH to settle it" in answer_text
                  and "as though they were evidence about the basin" in answer_text)
    results.check("the Task 6 exemplar refuses the overcorrection as well as the forgery",
                  "never in trouble" in answer_text and "1604" in answer_text)
    results.check("the Answer Key completes all six Task 7 parts",
                  all(part in answer_text for part in
                      ("What a chinampa is", "Evidence link 1", "Evidence link 2",
                       "Geography and function", "Source qualification", "The whole system")))
    results.check("the Task 7 exemplar uses two links from different real-world sources",
                  "Evidence link 1 - Source G" in answer_text
                  and "Evidence link 2 - Source H" in answer_text, answer_text[:0])
    results.check("the Task 7 exemplar carries an explicit source qualification",
                  "Source qualification -" in answer_text
                  and "cannot establish what the city or its fields were like in 1487" in answer_text)
    results.check("the Task 7 exemplar refuses two links from the same card",
                  "Do not credit two links from the same card" in answer_text)
    results.check("the Answer Key answers the transfer question rather than repeating the case",
                  "is a recall of Tenochtitlan, not a transfer of the method" in answer_text)
    results.check("the Answer Key states the floors it refuses at every level",
                  bool(soup.select('section.page[data-role="answer"] [data-answer-key-floor]')))
    floor = soup.select_one('section.page[data-role="answer"] [data-answer-key-floor]')
    floor_text = normalise(floor.get_text(" ", strip=True)) if floor is not None else ""
    for needle in ("floating rafts", "surviving primary source from 1487", "exact map of 1487"):
        results.check(f"the Answer Key floor names the refused claim “{needle}”",
                      needle in floor_text, floor_text[:260])
    results.check("every Answer Key exemplar block is followed by an acceptable-variation ruling",
                  len(soup.select('section.page[data-role="answer"] .answer-block'))
                  <= len([n for n in soup.select('section.page[data-role="answer"] .key-note')
                          if "Acceptable variation" in normalise(n.get_text(" ", strip=True))]) + 1,
                  len(soup.select('section.page[data-role="answer"] .answer-block')))

    # --- TEACHER EDITION CONTRACT -------------------------------------------
    for needle, label in (("Launch sheet", "launch sheet"),
                          ("The two routes", "both routes"),
                          ("Essential evidence", "essential evidence"),
                          ("Likely sticking point", "likely sticking point"),
                          ("What to collect", "what to collect"),
                          ("Teacher framing line", "framing line"),
                          ("Lesson overview", "lesson overview"),
                          ("Guiding historical question", "guiding question"),
                          ("Standards alignment and claim limits", "standards alignment"),
                          ("Measurable objectives", "measurable objectives"),
                          ("Success criteria", "success criteria"),
                          ("Academic vocabulary", "academic vocabulary"),
                          ("Materials and preparation", "materials and preparation"),
                          ("Complete teaching procedure", "teaching procedure"),
                          ("Facilitation prompts", "facilitation prompts"),
                          ("Transitions and collection points", "transitions and collection"),
                          ("Formative checks", "formative checks"),
                          ("Assessment guidance", "assessment guidance"),
                          ("Accessible supports actually present", "accessible supports"),
                          ("Misconceptions this case is built to catch", "misconceptions"),
                          ("Evidence architecture", "evidence architecture"),
                          ("The terminology qualification", "terminology qualification"),
                          ("The physical system in one paragraph", "the physical system"),
                          ("Limitations to keep in front of the class", "limitations"),
                          ("Instructional emphasis", "instructional emphasis"),
                          ("Quick classroom rubric", "quick rubric"),
                          ("Complete analytic rubric", "analytic rubric"),
                          ("Authoritative sources", "authoritative reference list"),
                          ("Complete no-game evidence digest", "no-game digest"),
                          ("Classroom and technical fallback", "classroom fallback")):
        results.check(f"Teacher Guide provides the {label}", needle in teacher_text, needle)
    rubric_levels = soup.select('section.page[data-role="teacher"] .analytic-rubric thead th')
    results.check("the analytic rubric uses four performance levels",
                  sum(1 for th in rubric_levels
                      if re.match(r"[1-4]\s", normalise(th.get_text(" ", strip=True)))) == 4,
                  [normalise(th.get_text(" ", strip=True)) for th in rubric_levels])
    results.check("the analytic rubric uses four criteria",
                  len(soup.select('section.page[data-role="teacher"] .analytic-rubric tbody tr')) == 4)
    results.check("a concise quick rubric exists alongside the analytic one",
                  bool(soup.select('section.page[data-role="teacher"] .quick-rubric')))
    MISCONCEPTIONS = ("floating rafts", "floating islands, so they floated",
                      "so that is what 1487 was like", "must have been perfect",
                      "salt was never a problem", "surviving aztec record",
                      "shows the city in 1487", "gardens on the lake shore",
                      "never wore out")
    lowered = teacher_text.lower()
    missing = [m for m in MISCONCEPTIONS if m.lower() not in lowered]
    results.check("the Teacher misconception table protects against every required framing",
                  not missing, missing)
    results.check("the Teacher Guide names the load-bearing misconception as load-bearing",
                  "The load-bearing misconception" in teacher_text)
    results.check("the Teacher Guide carries the diagnostic reading for the non-keyable task",
                  "Read the two slots as a diagnostic" in teacher_text)
    results.check("the Teacher Guide states the historical-map date and provenance limit",
                  "published in 1524" in teacher_text and "about 1520" in teacher_text
                  and "printed in Europe" in teacher_text)
    results.check("the Teacher Guide separates the reconstructed layer from the documented one",
                  "The reconstructed and the real" in teacher_text
                  and "proves nothing about 1487" in teacher_text)
    results.check("the Teacher Guide describes the physical system rather than only naming it",
                  "staked out in shallow water" in teacher_text
                  and "two layers" in teacher_text
                  and "carry away excess rain" in teacher_text
                  and "cropped through the year" in teacher_text)

    # --- STANDARDS -----------------------------------------------------------
    standards = registry["standards"]
    results.check("the directly assessed standards are exactly the three locked claims",
                  standards["directlyAssessed"] == ["C3 D2.His.1.6-8", "C3 D3.2.6-8", "CCSS RH.6-8.7"],
                  standards["directlyAssessed"])
    results.check("the supporting standards are exactly the two locked ones",
                  standards["supporting"] == ["CCSS RH.6-8.9", "CCSS WHST.6-8.2"], standards["supporting"])
    results.check("the standards list is not inflated with contextual claims",
                  standards["contextual"] == [], standards["contextual"])
    results.check("RH.6-8.9 is held at supporting and the reason is recorded",
                  "CCSS RH.6-8.9" not in standards["directlyAssessed"]
                  and "no task asks the learner to analyse the relationship between a primary and a secondary"
                  in standards["rationale"])
    results.check("no NGSS alignment is claimed at any status",
                  not any("NGSS" in s for s in
                          standards["directlyAssessed"] + standards["supporting"] + standards["contextual"])
                  and "No NGSS alignment is claimed" in standards["ngss"]
                  and "No NGSS alignment is claimed" in teacher_text)
    for claim in standards["directlyAssessed"] + standards["supporting"]:
        results.check(f"standard {claim} appears in the Teacher standards table",
                      claim in teacher_text, claim)
    table_rows = soup.select('section.page[data-role="teacher"] .standards-table tbody tr')
    results.check("the Teacher standards table carries one row per claim and no more",
                  len(table_rows) == len(standards["directlyAssessed"]) + len(standards["supporting"]),
                  len(table_rows))
    results.check("every Teacher standards row states where it is measured and its limit",
                  all("Limit:" in normalise(tr.get_text(" ", strip=True)) for tr in table_rows))

    # --- VOCABULARY ----------------------------------------------------------
    vocabulary = registry["vocabulary"]
    results.check("the case declares six vocabulary terms", len(vocabulary) == 6, vocabulary)
    results.check("the vocabulary bank is alphabetical by displayed term",
                  vocabulary == sorted(vocabulary), vocabulary)
    results.check("the required terms are exactly the locked six",
                  set(vocabulary) == {"canal", "chinampa", "dike", "intensive agriculture",
                                      "raised field", "salinity"}, vocabulary)
    for extra in ("agrobiodiversity", "causeway", "ahuejote", "tlacuilo", "chinampero"):
        results.check(f"{extra} is not promoted to a required retrieval term",
                      extra not in [v.lower() for v in vocabulary])
    for role in LEARNER_ROLES:
        items = [normalise(i.get_text(" ", strip=True)) for i in
                 soup.select(f'section.page[data-role="{role}"] .word-bank-item')]
        results.check(f"{role}: the word bank prints exactly the declared terms in order",
                      items == vocabulary, items)
        blanks = soup.select(f'section.page[data-role="{role}"] .term-list .inline-response')
        results.check(f"{role}: one blank per term, and no decoy in the bank",
                      len(blanks) == len(vocabulary) == len(items), len(blanks))
    for term in vocabulary:
        results.check(f"the Teacher vocabulary table defines {term}", term in teacher_text, term)

    payload = {
        "validator": "hhh-case08-floating-gardens-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": [a for a in results.assertions if a["status"] == "FAIL"] or "all passed",
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
