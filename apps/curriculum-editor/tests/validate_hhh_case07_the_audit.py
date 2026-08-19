#!/usr/bin/env python3
"""Case-scoped protections for HHH Campaign 2 Core Case 07 — The Audit.

These assertions guard the boundaries this case exists to get right, plus the
cross-edition parity the shared operational walk does not reach into. They are
driven by the contract blocks the task registry declares — ``sourceStatusContract``,
``authenticityRule``, ``provenanceTrails``, ``evidenceWeighting``, ``cerDecision``,
``noGameRoute``, ``editionResponseContract``, ``accessibleAdaptations``,
``semanticInvariants`` and ``figureContract`` — rather than by literal paragraph
locks, so ordinary rewording stays possible while the meaning stays protected.

The audit dependency this case carries:

* ``HHH-GAME-C2L0-001`` — ``GAME_REMEDIATION_BLOCKS_FINALIZATION``, and **CLOSED**.
  It was resolved in the game at ``d9fc16ba…``, which is the baseline this package
  is produced against. The curriculum neither reopens the game nor propagates the
  retired "too clean" heuristic, and the guards below are what keep the second half
  of that sentence true.

DESIGN NOTE — the shape of the semantic guard, and its limits.

This case has exactly one high-risk misconception, and it has five idiomatic
surfaces:

  * ``neatProvesForged`` — a clean/pristine/unamended record *proves* forgery;
  * ``correctionsProveAuthentic`` — corrections *prove* the record genuine;
  * ``messyIsGenuine`` — a messy working record is *automatically* genuine;
  * ``noCorrectionsProveForgery`` — an absence of corrections *proves* forgery;
  * ``visibleCorrectionsProveAuthenticity`` — visible corrections *prove* authenticity.

Every class is CLOSED: a small finite negative vocabulary, anchored to a named
subject register, requiring an explicit proof relation. None enumerates synonyms
for an open concept, and none polices an ordinary verb. That restraint is
deliberate — it is the lesson of the Case 04 catalyst spiral, and it is why this
file is short.

**This guard makes no claim of semantic completeness.** It is a defence against
one known misconception, not a proof that every possible bad paraphrase has been
detected. An unseen paraphrase can pass it. Ordinary cross-role parity, source-status
and manual review remain required, and the positive structural requirements below —
checked against markup rather than prose — are what carry the audit obligation,
because a guard that only forbade the wrong sentence would be satisfied by a packet
that said nothing at all.

Every semantic guard ships with NEGATIVE CONTROLS it must flag and POSITIVE
CONTROLS it must not, and the package itself is the standing positive control. A
guard that has silently stopped working therefore fails the run rather than
passing it quietly.

Usage:
    python3 apps/curriculum-editor/tests/validate_hhh_case07_the_audit.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "hhh/campaign-2/case-07-the-audit"
SOURCE = UNIT / "source"
REGISTRY_FILE = ROOT / "shared/implementation/case-registry.v2.json"
TRACKER_FILE = ROOT / "hhh/production/data/HHH_GAME_REMEDIATION_DEPENDENCY_TRACKER_v1.0.json"
CASE_ID = "HHH-C2-CASE07"
LEARNER_ROLES = ("student", "accessible")
ALL_ROLES = ("student", "teacher", "answer", "accessible")
GAME_COMMIT = "d9fc16baf272cb543c29cbd0c06ec85efad60be8"
AUDITED_GAME_COMMIT = "9b8545ed6ecf98b337326390400076e36789e056"

# Propositions break on terminal punctuation only. A semicolon, colon or dash is
# internal punctuation and not a safety boundary: splitting on them would let
# "the trail is long; a clean copy proves forgery" evade the gate by one character.
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
    # Fixed-width record transcripts are divs, not paragraphs, and carry printed
    # evidence. They are scanned as their own blocks rather than skipped.
    for node in page.select(".terminal"):
        allowed, text = prepared(node)
        if text:
            blocks.append((node, text, allowed))
    return blocks


# ---------------------------------------------------------------------------
# The semantic engine. One rule, five classes, compiled from the registry.
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
    results.check("package identity is HHH-C2-CASE07 v0.1 CORE_CASE in campaign-2",
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
    results.check("task registry pins the current game baseline and the audit baseline",
                  registry["gameCommit"] == GAME_COMMIT
                  and registry["auditBaseline"] == "hhh/audit/HHH_MASTER_GAME_AUDIT_v0.1.md"
                  and registry["blueprint"] == "hhh/blueprint/HHH_CURRICULUM_BLUEPRINT_v1.0.md",
                  registry["gameCommit"])

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
                  and entry["displayOrder"] == 9 and entry["displayLabel"] == "7 - The Audit"
                  and entry["editorPackage"] == "hhh/campaign-2/case-07-the-audit/source/case-package.json"
                  and "historyRecord" not in entry
                  and entry["approval"] == {"owner": "Nate / Owner",
                                            "status": "OWNER_REVIEW_NOT_STARTED",
                                            "printStatus": "NOT_RUN"},
                  json.dumps(entry))
    all_hhh = [c["id"] for cur in shared["curricula"] if cur["id"] == "HHH"
               for camp in cur["campaigns"] for c in camp["cases"]]
    results.check("exactly one HHH-C2-CASE07 identity exists in the shared registry",
                  all_hhh.count(CASE_ID) == 1, all_hhh)

    # --- THE CLOSED GAME DEPENDENCY -----------------------------------------
    tracker = json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
    dependency = next(d for d in tracker["gameDependencies"] if d["findingId"] == "HHH-GAME-C2L0-001")
    rule = registry["authenticityRule"]
    results.check("the case registry names the audit finding and its closed state",
                  rule["findingId"] == "HHH-GAME-C2L0-001"
                  and rule["dependencyClass"] == "GAME_REMEDIATION_BLOCKS_FINALIZATION"
                  and rule["dependencyStatus"] == "RESOLVED_VERIFIED"
                  and rule["resolvedGameCommit"] == GAME_COMMIT)
    results.check("the shared remediation tracker agrees, and this package leaves it untouched",
                  dependency["curriculumUnit"] == CASE_ID
                  and dependency["status"] == "RESOLVED_VERIFIED"
                  and dependency["resolution"]["resolvedGameCommit"] == GAME_COMMIT,
                  json.dumps({k: dependency.get(k) for k in ("status", "curriculumUnit")}))
    results.check("the multi-factor rule names all five evidence families",
                  rule["families"] == ["materials", "handwriting", "provenance", "custody", "corroboration"],
                  rule["families"])

    # Lifecycle, repository and runtime metadata must never reach a printable page.
    LIFECYCLE_TOKENS = ("VALIDATION_BUILD", "OWNER_REVIEW", "packageStatus", "sourceHashes",
                        "case-package.json", "task-registry.js", "APPROVED_STABLE",
                        "d9fc16ba", "9b8545ed", "c0780256", "releaseHistory", "release-v0.1",
                        "historyRecord", "Nate / Owner", "editorPackage", "OWNER_REVIEW_NOT_STARTED")
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
        ("2", "Set an Authenticity Test"),
        ("3", "Separate a Clue from Proof"),
        ("4", "Trace Each Copy's Provenance"),
        ("5", "Weigh the Four Evidence Sources"),
        ("6", "Compare the Competing Records"),
        ("7", "Validate the Better-Supported Record"),
        ("8", "Test What Would Change Your Confidence"),
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
        label = normalise(f"{number} \u00b7 {title}")
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
                  == {normalise(f'{n} \u00b7 {t}') for n, t in EXPECTED_TASKS},
                  sorted({normalise(n.get_text(" ", strip=True))
                          for n in soup.select('section.page[data-role="teacher"] strong.task-reference')}))
    results.check("no learner or Answer Key page carries a task heading outside the locked set",
                  {n.get("data-shell-task-heading") for n in soup.select("[data-shell-task-heading]")}
                  == {n for n, _ in EXPECTED_TASKS})

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
    results.check("the culminating product is named as a validation memorandum in every role that shows it",
                  all(soup.select(f'section.page[data-role="{role}"] [data-validation-memorandum]')
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
    results.check("the status vocabulary is the canonical three",
                  set(status_contract["statusVocabulary"])
                  == {"fictional case evidence", "documented", "curriculum-original schematic"},
                  status_contract["statusVocabulary"])

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
        results.check(f"{page_id}: the evidence object prints a STATUS line", status is not None,
                      str(node)[:120])
        if status is not None and declared in bands:
            marker = bands[declared]["statusMarker"].lower()
            results.check(f"{page_id}: the STATUS line names the {declared} band",
                          marker in normalise(status.get_text(" ", strip=True)).lower(),
                          normalise(status.get_text(" ", strip=True)))
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
        results.check(f"{role}: the notice states the non-merger rule",
                      "proves nothing about the real world" in text
                      and "proves nothing about the taa" in text, text[:220])
    fictional_nodes = soup.select("[data-fictional-data]")
    results.check("the packet marks its invented case data", len(fictional_nodes) >= 6,
                  len(fictional_nodes))
    for node in fictional_nodes:
        holder = node.find_parent(attrs={"data-evidence-layer": True})
        results.check("invented data sits inside a fictional or curriculum-model object",
                      holder is not None
                      and holder.get("data-evidence-layer") in {"fictional", "curriculum-model"},
                      str(node)[:120])
    for source in registry["caseSources"]:
        results.check(f"source {source['id']} declares a contribution and a limitation",
                      len(source.get("contribution", "")) > 40
                      and len(source.get("limitation", "")) > 40, source["id"])
    results.check("the real-world layer holds exactly one source, and it is the certified reference",
                  [s["id"] for s in registry["caseSources"] if s["evidenceLayer"] == "real"]
                  == ["diplomatics-reference"])

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

    # --- THE NO-GAME DOSSIER -------------------------------------------------
    no_game = registry["noGameRoute"]
    results.check("the no-game contract names the four dossier sources",
                  no_game["dossier"] == ["audit-briefing", "audit-pattern", "audit-log", "memo-pair"],
                  no_game["dossier"])
    for role in no_game["requiredInRoles"]:
        for source_id in no_game["dossier"]:
            results.check(f"{role}: dossier source {source_id} is printed in the learner packet",
                          bool(soup.select(f'section.page[data-role="{role}"] '
                                           f'[data-source-id~="{source_id}"]')), source_id)
    results.check("Teacher supplies both routes and states that Campaign 2 has no launch shortcut",
                  "Game route" in teacher_text and "No-game route" in teacher_text
                  and "no level selector and no shortcut" in teacher_text)
    results.check("Teacher supplies a complete no-game evidence digest",
                  "Complete no-game evidence digest" in teacher_text)
    # Nothing in the packet may reproduce the runtime's resolution prose or its
    # answer-revealing companion hints. That prohibition is absolute and applies to
    # every role, learner and teacher alike.
    RUNTIME_RESOLUTION = ("The Record Validates", "Thread 1 (FERTILE CRESCENT)",
                          "your signature clean on every page", "nobody forges hesitation",
                          "the pristine copy is bait", "trust your own hand",
                          "the flawless copy is structurally impossible",
                          "validate the record that carries its errors")
    for role in ALL_ROLES:
        leaked = [t for t in RUNTIME_RESOLUTION if t.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime resolution or hint text is reproduced", not leaked, leaked)
    # On-screen control labels are a narrower class. A Teacher naming the button a
    # class will actually press is helping them run the level; a learner page that
    # named it would be assuming gameplay the no-game route does not have.
    RUNTIME_UI_LABELS = ("Validate the Record", "The audit is incomplete", "Which record is genuine?")
    for role in LEARNER_ROLES + ("answer",):
        leaked = [t for t in RUNTIME_UI_LABELS if t.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime control label is printed", not leaked, leaked)

    # --- PROVENANCE TRAILS ---------------------------------------------------
    trails = registry["provenanceTrails"]
    copy_a = next(c for c in trails["copies"] if c["id"] == "copy-a")
    copy_b = next(c for c in trails["copies"] if c["id"] == "copy-b")
    results.check("the two recorded trails are exactly the ones the game records",
                  copy_a["recordedSteps"] == ["intake", "catalogue", "shelf"]
                  and copy_b["recordedSteps"] == ["intake", "catalogue", "recalled", "re-filed", "shelf"]
                  and copy_a["recordedStepCount"] == 3 and copy_b["recordedStepCount"] == 5,
                  json.dumps({"a": copy_a["recordedSteps"], "b": copy_b["recordedSteps"]}))
    results.check("the differing links are the recall and the re-filing",
                  trails["differingLinks"] == ["recalled", "re-filed"], trails["differingLinks"])
    results.check("the registry states that the making of neither copy is recorded",
                  any("making of either copy" in item for item in trails["unrecordedEvents"]),
                  trails["unrecordedEvents"])
    results.check("the intended judgment is Copy B, and the single-factor route to it is refused",
                  trails["intendedJudgment"].startswith("Copy B")
                  and "therefore it is authentic" in trails["prohibitedJudgmentRoute"])
    for role in LEARNER_ROLES:
        figure = soup.select_one(f'section.page[data-role="{role}"] [data-provenance-contract]')
        results.check(f"{role}: the provenance figure is present", figure is not None)
        if figure is None:
            continue
        text = normalise(figure.get_text(" ", strip=True))
        results.check(f"{role}: the provenance figure draws the unrecorded head of both trails",
                      "NOT RECORDED" in text and "Both begin at intake" in text, text[:200])
        for step in copy_b["recordedSteps"]:
            results.check(f"{role}: the provenance figure prints the recorded step '{step}'",
                          step in text, step)
        results.check(f"{role}: the figure marks the two links Copy A's trail does not have",
                      len(figure.select(".tr-added")) == 2, len(figure.select(".tr-added")))
        results.check(f"{role}: the figure prints the reason recorded with the recall",
                      "grain count" in text and "Reason recorded at the time" in text, text[:200])

    # --- EVIDENCE WEIGHTING --------------------------------------------------
    weighting = registry["evidenceWeighting"]
    roles_by_id = {r["id"]: r for r in weighting["roles"]}
    results.check("the three qualitative evidentiary roles are declared",
                  {r["label"] for r in weighting["roles"]}
                  == {"CONTEXT", "CORROBORATING EVIDENCE", "DIRECT RECORD EVIDENCE"},
                  [r["label"] for r in weighting["roles"]])
    results.check("the two participant accounts are CONTEXT and the two records are not",
                  roles_by_id["context"]["sources"] == ["audit-briefing", "audit-pattern"]
                  and roles_by_id["corroborating"]["sources"] == ["audit-log"]
                  and roles_by_id["direct-record"]["sources"] == ["memo-pair"],
                  json.dumps({k: v["sources"] for k, v in roles_by_id.items()}))
    results.check("the registry states in terms that the four sources are not equally probative",
                  "not equally probative" in weighting["notEquallyProbative"])
    every_role_source = [s for r in weighting["roles"] for s in r["sources"]]
    results.check("every weighted source is a canonical source, each weighted exactly once",
                  sorted(every_role_source) == sorted(set(every_role_source))
                  and all(s in source_layers for s in every_role_source),
                  every_role_source)
    for role in LEARNER_ROLES:
        figure = soup.select_one(f'section.page[data-role="{role}"] [data-weight-contract]')
        results.check(f"{role}: the evidence-weight organiser is present", figure is not None)
        if figure is None:
            continue
        text = normalise(figure.get_text(" ", strip=True))
        for label in ("CONTEXT", "CORROBORATING EVIDENCE", "DIRECT RECORD EVIDENCE"):
            results.check(f"{role}: the organiser prints the role name {label}", label in text, label)
        results.check(f"{role}: the organiser states that it is kinds rather than a score",
                      "not a score" in text, text[:200])
        results.check(f"{role}: the organiser fabricates no numerical confidence",
                      not re.search(r"\d+\s?(?:%|per cent|percent)", text), text[:200])

    # --- THE AUTHENTICITY RULE: POSITIVE REQUIREMENTS ------------------------
    for requirement in rule["positiveRequirements"]:
        for role in requirement["roles"]:
            found = soup.select(f'section.page[data-role="{role}"] {requirement["selector"]}')
            results.check(f"{role}: positive requirement {requirement['id']} is printed",
                          bool(found), requirement["selector"])
    for role in rule["requiredPrintedStatementRoles"]:
        for statement in rule["requiredPrintedStatements"]:
            results.check(f"{role}: prints the required statement \u201c{statement[:44]}\u2026\u201d",
                          normalise(statement).lower() in texts[role].lower(), statement)
    for role in LEARNER_ROLES:
        figure = soup.select_one(f'section.page[data-role="{role}"] [data-authenticity-contract]')
        results.check(f"{role}: the multi-factor framework figure is present", figure is not None)
        if figure is None:
            continue
        text = normalise(figure.get_text(" ", strip=True))
        for family in ("MATERIALS", "HANDWRITING", "PROVENANCE", "CUSTODY", "CORROBORATION"):
            results.check(f"{role}: the framework figure prints the family {family}",
                          family in text.upper(), family)
        results.check(f"{role}: the framework figure prints the governing rule",
                      normalise(rule["printedRule"]).lower() in text.lower(), text[:200])
        results.check(f"{role}: the framework figure refuses a plan reading of itself",
                      "not evidence about any particular record" in text.lower(), text[:200])
    # Task 3 must carry an item about neatness and an item about corrections, and
    # neither may be presented as deciding anything.
    for role in LEARNER_ROLES:
        items = [normalise(i.get_text(" ", strip=True)).lower()
                 for i in soup.select(f'section.page[data-role="{role}"] .clue-item')]
        results.check(f"{role}: Task 3 prints six clue items", len(items) == 6, len(items))
        results.check(f"{role}: Task 3 carries an item about an absence of corrections",
                      any("no corrections" in i for i in items), items[:2])
        results.check(f"{role}: Task 3 carries an item about visible corrections",
                      any("struck-through" in i or "crossed-out" in i for i in items), items[:2])
        marks = soup.select(f'section.page[data-role="{role}"] .clue-item .mark-response')
        modelled = soup.select(f'section.page[data-role="{role}"] .clue-item .clue-answer')
        expected_marks = 6 if role == "student" else 5
        results.check(f"{role}: Task 3 collects {expected_marks} persistent marks",
                      len(marks) == expected_marks
                      and all(m.has_attr("data-response") and m.has_attr("data-persist-id") for m in marks),
                      len(marks))
        results.check(f"{role}: only the Accessible edition supplies a worked clue judgment",
                      len(modelled) == (0 if role == "student" else 1), len(modelled))
    results.check("the matched comparison states in print that surface features do not settle it",
                  all("surface characteristics alone do not settle this comparison"
                      in normalise(soup.select_one(f'section.page[data-role="{role}"] '
                                                   f'[data-authenticity-rule="surface-not-decisive"]')
                                   .get_text(" ", strip=True)).lower()
                      for role in LEARNER_ROLES))

    # --- SEMANTIC GUARDS: POSITIVE CONTROL (the package itself) --------------
    invariants = registry["semanticInvariants"]
    exemptions = {e["id"]: e for e in invariants["exemptions"]}
    compiled = compile_classes(rule["prohibitedFramings"])
    results.check("all five prohibited concept classes compile",
                  set(compiled) == {"neatProvesForged", "correctionsProveAuthentic",
                                    "messyIsGenuine", "noCorrectionsProveForgery",
                                    "visibleCorrectionsProveAuthenticity"},
                  sorted(compiled))
    for role in ALL_ROLES:
        violations = scan_html(html, compiled, exemptions, role)
        results.check(f"{role}: no unexempted proposition states a prohibited framing",
                      not violations, json.dumps(violations[:6], indent=1))

    # --- SEMANTIC GUARDS: NEGATIVE CONTROLS ---------------------------------
    for class_id, sentences in rule["negativeControls"].items():
        results.check(f"negative controls exist for {class_id}", len(sentences) >= 3, sentences)
        for sentence in sentences:
            hits = scan_html(synthetic("student", f"<p>{sentence}</p>"), compiled, exemptions, "student")
            results.check(f"negative control fires for {class_id}: {sentence[:52]}",
                          any(h[2] == class_id for h in hits), hits)

    # --- SEMANTIC GUARDS: POSITIVE (MUST-NOT-FLAG) CONTROLS -----------------
    # Truthful prose the guards must leave alone, including the five sentences the
    # governing rule requires to stay legal. These confer no authority: authored
    # wording this list has never seen is expected to pass, and does.
    REQUIRED_LEGAL = [
        "Unexplained neatness may prompt closer examination.",
        "Corrections can be one clue when they match a documented record history.",
        "A clean record can be authentic.",
        "A forged record can imitate corrections.",
        "No single surface feature proves authenticity or forgery.",
    ]
    results.check("the registry carries every required positive control",
                  all(s in rule["positiveControls"] for s in REQUIRED_LEGAL),
                  [s for s in REQUIRED_LEGAL if s not in rule["positiveControls"]])
    for sentence in rule["positiveControls"]:
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
                                  'Visible corrections prove authenticity.</p>')
    results.check("mutation control: an unregistered exemption id excuses nothing",
                  bool(scan_html(forged, compiled, exemptions, "student")))
    wrong_role = synthetic("student", '<p data-semantic-exemption="teacher-misconception">'
                                      'Visible corrections prove authenticity.</p>')
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
                  {sub["task"] for sub in subparts}
                  == {t["id"] for t in tasks},
                  sorted({sub["task"] for sub in subparts}))

    # --- ACCESSIBLE ADAPTATIONS ARE TRUE AND DECLARED -----------------------
    adaptations = registry["accessibleAdaptations"]
    results.check("exactly four Accessible adaptations are declared, and no fifth has appeared",
                  len(adaptations) == 4, sorted(adaptation_ids))
    for adaptation in adaptations:
        task = next(t for t in tasks if t["id"] == adaptation["task"])
        label = normalise(f"{task['number']} \u00b7 {task['title']}")
        results.check(f"adaptation {adaptation['id']} is disclosed to the teacher",
                      label in teacher_text, adaptation["id"])
        for role in adaptation["declaredIn"]:
            results.check(f"adaptation {adaptation['id']} declares a real role", role in ALL_ROLES, role)
        results.check(f"adaptation {adaptation['id']} explains why it is not a leak",
                      len(adaptation.get("whyNotALeak", "")) > 60, adaptation["id"])
    marked = {n.get("data-accessible-adaptation") for n in soup.select("[data-accessible-adaptation]")}
    results.check("every adaptation marked in the Accessible markup is registered",
                  marked <= adaptation_ids, sorted(marked - adaptation_ids))
    results.check("Task 5's modelled row and prefilled row are both present in the Accessible edition",
                  {"t3-modelled-judgment", "t5-modelled-row", "t5-prefilled-row"} <= marked, sorted(marked))
    results.check("the Accessible worked example is printed as an example rather than as a blank",
                  all("WORKED EXAMPLE" in normalise(n.get_text(" ", strip=True)).upper()
                      for n in soup.select('section.page[data-role="accessible"] '
                                           '[data-accessible-adaptation="t3-modelled-judgment"]')))
    prefilled = soup.select('section.page[data-role="accessible"] .weight-table .prefilled')
    results.check("the Accessible weighting table supplies four prefilled cells and no more",
                  len(prefilled) == 4 and not soup.select('section.page[data-role="student"] '
                                                          '.weight-table .prefilled'),
                  len(prefilled))
    results.check("the Teacher scoring note still claims exactly three scored differences",
                  "Three scored differences, and only three" in teacher_text)

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
    for role in LEARNER_ROLES:
        marks = soup.select(f'section.page[data-role="{role}"] .mark-response')
        results.check(f"{role}: every printed mark, choice and classification is persistent",
                      bool(marks) and all(m.has_attr("data-response") and m.has_attr("data-persist-id")
                                          and (m.get("role") == "textbox")
                                          and (m.get("aria-label")) for m in marks), len(marks))
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
            if spec.get("requiresPrintedRule"):
                results.check(f"{role}: {spec['id']} accessibility text carries the printed rule",
                              normalise(spec["requiresPrintedRule"]).lower() in alt.lower(), alt[:200])
            for family in spec.get("requiresFamilies", []):
                results.check(f"{role}: {spec['id']} accessibility text names {family}",
                              family.lower() in alt.lower(), family)
            if spec.get("requiresUnrecordedHead"):
                results.check(f"{role}: {spec['id']} accessibility text states that the head is unrecorded",
                              "not recorded" in alt.lower(), alt[:200])
            if spec.get("requiresBothTrails"):
                results.check(f"{role}: {spec['id']} accessibility text describes both trails",
                              "copy a's trail" in alt.lower() and "copy b's trail" in alt.lower(), alt[:200])
            for role_label in spec.get("requiresRoles", []):
                results.check(f"{role}: {spec['id']} accessibility text names the band {role_label}",
                              role_label.lower() in alt.lower(), role_label)
            if spec.get("requiresNoScore"):
                results.check(f"{role}: {spec['id']} accessibility text says it is not a score",
                              "not a score" in alt.lower(), alt[:200])
            if spec.get("requiresSchematicDisclaimer"):
                results.check(f"{role}: {spec['id']} accessibility text refuses to be read as evidence",
                              "not evidence about any particular record" in alt.lower(), alt[:200])
    results.check("no figure in the package uses generated imagery",
                  not soup.select('figure.case-figure img:not(.taa-insignia)'))

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
    results.check("no source file carries a machine-local path",
                  not [f.name for f in sorted(SOURCE.iterdir())
                       if re.search(r"/Users/|/home/|file:///|C:\\\\", f.read_text(encoding="utf-8"))],
                  [f.name for f in sorted(SOURCE.iterdir())
                   if re.search(r"/Users/|/home/|file:///", f.read_text(encoding="utf-8"))])

    # --- ANSWER KEY COVERAGE -------------------------------------------------
    results.check("the Answer Key completes the Task 7 finding on the intended record",
                  "the better-supported record" in answer_text.lower()
                  and "Copy B is the better-supported record" in answer_text)
    results.check("the Task 7 model answer uses two links from different sources",
                  "Evidence link 1 - Source D" in answer_text
                  and "Evidence link 2 - Source C" in answer_text, answer_text[:0])
    results.check("the Answer Key refuses the single-factor route in both directions",
                  "not accepted at any level" in answer_text.lower()
                  and "would reach the same answer about a forgery" in answer_text.lower())
    results.check("the Answer Key refuses to broaden acceptance to the other record",
                  "wording varies, the finding does not" in answer_text.lower())
    results.check("the Answer Key answers the transfer question rather than repeating the case",
                  "repeats the Case 07 result" in answer_text
                  and "not a transfer of the method" in answer_text)
    results.check("the Answer Key states that Task 2 is not keyed",
                  "Task 2 is not keyed" in answer_text)
    results.check("the Answer Key completes both counts, both extra links and the unrecorded gap",
                  all(fragment in answer_text for fragment in
                      ("3 recorded entries", "5 recorded entries", "Recalled and re-filed",
                       "Neither trail records the making of either copy")))
    results.check("the Answer Key completes all four weighting rows with their roles",
                  all(fragment in answer_text for fragment in
                      ("CONTEXT", "CORROBORATING EVIDENCE", "DIRECT RECORD EVIDENCE")))
    results.check("the Answer Key discloses the Accessible reductions it scores",
                  "eight" in answer_text.lower() and "twelve" in answer_text.lower()
                  and "five" in answer_text.lower() and "six" in answer_text.lower())

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
                          ("Evidentiary weighting", "evidentiary weighting"),
                          ("Reasoning path", "reasoning path"),
                          ("The competing records", "competing records"),
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
    results.check("a concise quick rubric exists alongside the analytic one",
                  bool(soup.select('section.page[data-role="teacher"] .quick-rubric')))
    MISCONCEPTIONS = ("too clean", "it has corrections", "messy means genuine",
                      "no corrections at all", "more clues", "custody trail is documented",
                      "no gaps", "author remembers", "pattern proves")
    lowered = teacher_text.lower()
    missing = [m for m in MISCONCEPTIONS if m not in lowered]
    results.check("the Teacher misconception table protects against every required framing",
                  not missing, missing)

    # --- STANDARDS -----------------------------------------------------------
    # The partition pinned below is the independent-review ruling that superseded the
    # original four-direct/one-supporting claim: the record-to-record comparison in
    # Tasks 6 and 7 practises the relationship RH.6-8.9 rests on, but no learner
    # performs a primary-versus-secondary analysis here, so it is supported rather
    # than directly assessed. Both checks remain exact list equality.
    standards = registry["standards"]
    results.check("the directly assessed standards are exactly the three locked claims",
                  standards["directlyAssessed"] == ["C3 D3.1.6-8", "C3 D3.2.6-8",
                                                    "CCSS RH.6-8.6"],
                  standards["directlyAssessed"])
    results.check("the supporting standards are exactly the two locked claims",
                  standards["supporting"] == ["CCSS WHST.6-8.1", "CCSS RH.6-8.9"],
                  standards["supporting"])
    results.check("the standards list is not inflated with contextual claims",
                  standards["contextual"] == [], standards["contextual"])
    results.check("no NGSS alignment is claimed at any status",
                  not any("NGSS" in s for s in
                          standards["directlyAssessed"] + standards["supporting"] + standards["contextual"])
                  and "No NGSS alignment is claimed" in standards["ngss"]
                  and "No NGSS alignment is claimed" in teacher_text)
    for claim in standards["directlyAssessed"] + standards["supporting"]:
        results.check(f"standard {claim} appears in the Teacher standards table",
                      claim in teacher_text, claim)

    # --- VOCABULARY ----------------------------------------------------------
    vocabulary = registry["vocabulary"]
    results.check("the case declares six vocabulary terms", len(vocabulary) == 6, vocabulary)
    results.check("the vocabulary bank is alphabetical by displayed term",
                  vocabulary == sorted(vocabulary), vocabulary)
    results.check("the required terms are exactly the locked six",
                  set(vocabulary) == {"authenticity", "chain of custody", "corroboration",
                                      "integrity", "provenance", "transmission"}, vocabulary)
    results.check("diplomatics is not a required retrieval term",
                  "diplomatics" not in [v.lower() for v in vocabulary])
    for role in LEARNER_ROLES:
        items = [normalise(i.get_text(" ", strip=True)) for i in
                 soup.select(f'section.page[data-role="{role}"] .word-bank-item')]
        results.check(f"{role}: the word bank prints exactly the declared terms in order",
                      items == vocabulary, items)
        blanks = soup.select(f'section.page[data-role="{role}"] .term-list .inline-response')
        results.check(f"{role}: one blank per term", len(blanks) == len(vocabulary), len(blanks))
    for term in vocabulary:
        results.check(f"the Teacher vocabulary table defines {term}", term in teacher_text, term)

    payload = {
        "validator": "hhh-case07-the-audit-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": [a for a in results.assertions if a["status"] == "FAIL"] or "all passed",
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
