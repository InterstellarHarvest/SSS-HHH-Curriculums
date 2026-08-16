#!/usr/bin/env python3
"""Case-scoped protections for HHH Campaign 1 Core Case 06 — The Vertical Farm.

These assertions guard the boundaries this case exists to get right, plus the
cross-edition parity the shared operational walk does not reach into. They are
driven by the contract blocks the task registry declares — ``twoLayerTruth``,
``systemsFrame``, ``scienceQualification``, ``accountabilityBoundary``,
``sourceStatusContract``, ``editionResponseContract``, ``semanticInvariants`` and
``figureAccessibilityContract`` — rather than by literal paragraph locks, so
ordinary rewording stays possible while the meaning stays protected.

The audit dependency this case carries:

* ``HHH-GAME-C1L6-001`` — TEACHER QUALIFICATION, not game remediation. The
  runtime level's nitrogen model simplifies microbial diversity and plant
  nitrogen chemistry. The curriculum corrects the model in print and leaves the
  game alone. That correction is assessed rather than announced, so the guards
  below have positive requirements as well as negative ones.

DESIGN NOTE — why these guards are shaped the way they are, and why they are
smaller than Case 05's.

Case 05 needed a large, registry-owned zero-boundary classifier because the
runtime level itself carried the prohibited absolute, reviewers kept finding
fresh English for it, and the correct framing was a bounded comparative that any
paraphrase could flatten. **None of that applies here**, and reproducing that
machinery would have been cargo-cult engineering rather than protection.

What this case actually needs guarding is five genuinely CLOSED classes:

  * ``universalTwoSpecies`` — a small finite set of ways to say *always exactly
    two*, bound to a nitrification subject;
  * ``nitrateOnly`` — a small finite set of ways to say *only nitrate*, bound to
    a plant subject;
  * ``universalToxicityThreshold`` — a numeric pattern, which needs no subject
    because a number with a concentration unit beside an ammonia token is the
    violation;
  * ``noAccountability`` — a small finite set of ways to say *nobody was
    responsible*;
  * ``verdictAdopted`` — a small finite set of ways to state the fictional
    public statement's verdict as this packet's finding.

Each is paired with a POSITIVE STRUCTURAL requirement checked against markup
rather than prose — ``data-evidence-layer``, ``data-science-qualification``,
``data-fictional-data``, ``data-two-layer-notice``. The positive half is what
carries the audit requirement: a guard that only forbade the wrong sentence
would be satisfied by a packet that said nothing at all, and requiring the
diversity note to be printed in both learner editions cannot be satisfied by
silence.

No guard here polices an ordinary verb, and none enumerates synonyms for an open
concept. That is the lesson from Case 04's catalyst spiral, and it is the reason
this file is roughly half the size of Case 05's.

Exemption is a closed contract. A node may be excused only by naming a
registered exemption id that resolves, for that role, to the concept classes the
registry allows it. Adding an attribute cannot make a bad sentence disappear.

Every semantic guard ships with NEGATIVE CONTROLS — synthetic fragments it must
flag — and the package itself is the POSITIVE CONTROL. A guard that has silently
stopped working therefore fails the run rather than passing it quietly.

Usage:
    python3 apps/curriculum-editor/tests/validate_hhh_case06_vertical_farm.py
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "hhh/campaign-1/case-06-vertical-farm"
SOURCE = UNIT / "source"
REGISTRY_FILE = ROOT / "shared/implementation/case-registry.v2.json"
CASE_ID = "HHH-C1-CASE06"
LEARNER_ROLES = ("student", "accessible")
ALL_ROLES = ("student", "teacher", "answer", "accessible")

# Propositions break on terminal punctuation only. A semicolon, colon or dash is
# internal punctuation and not a safety boundary: splitting on them would let
# "the community is diverse; it is always exactly two species" evade the gate by
# one character.
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
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("—", " - ").replace("–", "-").replace(" ", " ")
    text = text.replace("−", "-").replace("·", " ")
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


def structurally_exempt(node, selectors: list[str]) -> bool:
    current = node
    while current is not None and getattr(current, "name", None):
        classes = current.get("class") or []
        for selector in selectors:
            if selector.startswith(".") and selector[1:] in classes:
                return True
        current = current.parent
    return False


def resolvable(node, exemptions: dict, role: str) -> set[str]:
    """The concept classes actually excused at this node.

    An exemption id excuses something only if it is REGISTERED and declares this
    role. An id the registry has never heard of, or one borrowed from another
    role, resolves to the empty set and therefore excuses nothing. This is what
    makes the sentence "markup cannot self-authorize" true rather than aspirational,
    and the two mutation controls at the end of this file are what keep it true.
    """
    allowed: set[str] = set()
    for eid in exempt_ids(node):
        spec = exemptions.get(eid)
        if spec and role in spec["roles"]:
            allowed |= set(spec["allowedConcepts"])
    return allowed


def leaf_blocks(page, exemptions: dict, role: str) -> list:
    """Paragraph-level containers paired with the concepts excused inside them.

    Innermost-container selection means each run of prose is scanned exactly
    once: a sentence inside a paragraph inside a table cell is not counted three
    times, and a violation cannot be reported once per nesting level.

    Exempt-subtree REMOVAL, rather than skipping the exempt node, is what makes a
    registered exemption work on a clause. An Answer Key floor that quotes the
    answer it refuses is a span inside an ordinary paragraph; skipping the span
    while still scanning its parent would leave the quoted wording in the
    parent's text and fail the packet for carrying its own floor. The paragraph
    is therefore scanned with the exempt span's text taken out of it, so the
    exemption covers exactly what it wraps and no more.

    Only subtrees whose exemption RESOLVES are removed. A subtree carrying an
    unregistered id, or one registered for a different role, stays in the text
    and is scanned normally. An earlier revision of this function dropped any
    node that merely carried the attribute, which meant inventing an attribute
    value switched the guard off - the exact failure the guard exists to prevent.
    """
    blocks = []

    def prepared(node):
        allowed = resolvable(node, exemptions, role)
        clone = BeautifulSoup(str(node), "html.parser")
        for exempted in clone.select("[data-semantic-exemption]"):
            eid = exempted.get("data-semantic-exemption")
            spec = exemptions.get(eid)
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


def scan_html(html: str, compiled: dict, structural: list[str],
              exemptions: dict, role: str) -> list[tuple]:
    """Return (role, page-id, class-id, sentence) for every violation."""
    soup = BeautifulSoup(html, "html.parser")
    violations = []
    for page in soup.select(f'section.page[data-role="{role}"]'):
        page_id = page.get("data-page-id")
        for node, text, allowed in leaf_blocks(page, exemptions, role):
            if structurally_exempt(node, structural):
                continue
            for sentence in propositions(text):
                for class_id, spec in compiled.items():
                    if class_id in allowed:
                        continue
                    if spec["subjects"] and not any(s.search(sentence) for s in spec["subjects"]):
                        continue
                    hit = next((p for p in spec["patterns"] if p.search(sentence)), None)
                    if hit is not None:
                        violations.append((role, page_id, class_id, sentence[:220]))
    return violations


def synthetic(role: str, body: str) -> str:
    return (f'<section class="page" data-role="{role}" data-page-id="control-page">'
            f'<div class="content content-area">{body}</div></section>')


def main() -> int:
    results = Results()
    package, registry, layout, soup = load()
    html = (SOURCE / "content.html").read_text(encoding="utf-8")
    tasks = registry["tasks"]
    texts = {role: role_text(soup, role) for role in ALL_ROLES}
    teacher_text, answer_text = texts["teacher"], texts["answer"]

    # --- IDENTITY AND LIFECYCLE TRUTH ---------------------------------------
    results.check("package identity is HHH-C1-CASE06 v0.1 CORE_CASE",
                  (package["id"], package["version"], package["instructionalType"],
                   package["curriculum"], package["campaign"])
                  == (CASE_ID, "0.1", "CORE_CASE", "HHH", "campaign-1"))
    results.check("package lifecycle is an unapproved validation build",
                  package["status"] == "VALIDATION_BUILD"
                  and package["approval"]["status"] == "OWNER_REVIEW_NOT_STARTED"
                  and package["approval"]["printStatus"] == "NOT_RUN",
                  json.dumps({"status": package["status"], "approval": package["approval"]}))
    results.check("package declares no release history", "releaseHistory" not in package)
    results.check("no history directory exists for an unreleased package",
                  not (UNIT / "history").exists())
    results.check("registry lifecycle agrees with the package",
                  (registry["status"], registry["ownerReviewStatus"], registry["version"])
                  == ("VALIDATION_BUILD", "OWNER_REVIEW_NOT_STARTED", "0.1"))
    results.check("task registry pins the current game baseline",
                  registry["gameCommit"] == "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
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
    results.check("shared registry entry is an editor-ready validation package",
                  entry["status"] == "VALIDATION_BUILD" and entry["packageStatus"] == "VALIDATION"
                  and entry["editorPackage"] == "hhh/campaign-1/case-06-vertical-farm/source/case-package.json",
                  json.dumps(entry))
    results.check("shared registry entry declares no history record and no approval",
                  "historyRecord" not in entry
                  and entry["approval"]["status"] == "OWNER_REVIEW_NOT_STARTED"
                  and entry["approval"]["printStatus"] == "NOT_RUN")

    # Lifecycle and repository metadata must never reach a printable page.
    LIFECYCLE_TOKENS = ("VALIDATION_BUILD", "OWNER_REVIEW", "packageStatus", "sourceHashes",
                        "case-package.json", "task-registry.js", "APPROVED_STABLE",
                        "d9fc16ba", "9b8545ed")
    for role in ALL_ROLES:
        found = [t for t in LIFECYCLE_TOKENS if t.lower() in texts[role].lower()]
        results.check(f"{role}: no lifecycle or repository metadata is printed", not found, found)

    # --- PAGE STRUCTURE -----------------------------------------------------
    for role in ALL_ROLES:
        declared = package["rolePageStructure"][role]["pageCount"]
        actual = len(pages_for(soup, role))
        results.check(f"{role}: page count matches the package ({declared})",
                      actual == declared, actual)
        results.check(f"{role}: page count matches the task registry",
                      registry["roles"][role] == declared, registry["roles"][role])
        for index, page in enumerate(pages_for(soup, role), start=1):
            footer = page.select_one("[data-publication-footer]")
            ok = footer is not None and f"{index} of {declared}" in normalise(footer.get_text(" ", strip=True))
            results.check(f"{role}: page {index} carries a correct publication footer", ok,
                          normalise(footer.get_text(" ", strip=True)) if footer else "missing")
        missing_frame = [p.get("data-page-id") for p in pages_for(soup, role)
                         if not p.select_one(".page-frame") or not p.select_one(".overflow-warning")
                         or not p.select_one("[data-header-contract]")]
        results.check(f"{role}: every page carries frame, overflow strip and header contract",
                      not missing_frame, missing_frame)

    # --- TASK COVERAGE ------------------------------------------------------
    results.check("the registry declares nine tasks", len(tasks) == 9, len(tasks))
    for task in tasks:
        number = task["number"]
        for role in task["editions"]:
            if role == "teacher":
                continue
            heading = soup.select_one(f'section.page[data-role="{role}"] [data-shell-task-heading="{number}"]')
            results.check(f"{role}: task {number} has a shell heading", heading is not None)
        label = f"{number} · {task['title']}"
        results.check(f"Teacher names task {number} by number and title",
                      normalise(label) in teacher_text, label)
        anchor = soup.select_one(f'section.page[data-role="teacher"] .task-reference')
        results.check(f"Teacher task references are visually emphasised (task {number})",
                      anchor is not None and anchor.name in {"strong", "b", "span"})
        placement = task["pagePlacement"]
        for role in ("student", "teacher", "answer", "accessible"):
            page = soup.select_one(f'section.page[data-role="{role}"][data-page-id="{placement[role]}"]')
            results.check(f"{role}: declared page for task {number} exists", page is not None,
                          placement[role])

    # --- TWO-LAYER TRUTH ----------------------------------------------------
    two_layer = registry["twoLayerTruth"]
    layer_by_id = {layer["id"]: layer for layer in two_layer["layers"]}
    source_layers = {s["id"]: s.get("evidenceLayer") for s in registry["caseSources"]}
    results.check("every canonical source declares a truth layer",
                  all(v in layer_by_id for v in source_layers.values()),
                  {k: v for k, v in source_layers.items() if v not in layer_by_id})
    results.check("the two-layer contract is enforced in every role",
                  tuple(two_layer["enforcedRoles"]) == ALL_ROLES, two_layer["enforcedRoles"])

    evidence_objects = soup.select("[data-source-id]")
    results.check("at least one evidence object exists", bool(evidence_objects))
    for node in evidence_objects:
        page = node.find_parent(class_="page")
        if page is None:
            continue
        role, page_id = page.get("data-role"), page.get("data-page-id")
        ids = node.get("data-source-id").split()
        unknown = [i for i in ids if i not in source_layers]
        results.check(f"{page_id}: every data-source-id resolves to a canonical source",
                      not unknown, unknown)
        declared = node.get("data-evidence-layer")
        if declared is None:
            # Ledger rows and inline figure sub-panels inherit their layer.
            results.check(f"{page_id}: an unlayered evidence node sits inside a layered one",
                          node.find_parent(attrs={"data-evidence-layer": True}) is not None
                          or node.find_parent(class_="source-table") is not None,
                          str(node)[:160])
            continue
        results.check(f"{page_id}: declared layer is a registered layer",
                      declared in layer_by_id, declared)
        for source_id in ids:
            results.check(f"{page_id}: {source_id} markup layer matches the registry",
                          source_layers.get(source_id) == declared,
                          f"markup {declared} vs registry {source_layers.get(source_id)}")
        status = node.select_one(".source-status")
        results.check(f"{page_id}: layered evidence prints a STATUS line", status is not None,
                      str(node)[:120])
        if status is not None:
            marker = layer_by_id[declared]["statusMarker"].lower()
            results.check(f"{page_id}: the STATUS line names the {declared} layer",
                          marker in normalise(status.get_text(" ", strip=True)).lower(),
                          normalise(status.get_text(" ", strip=True)))

    for role in two_layer.get("enforcedRoles", []):
        if role not in LEARNER_ROLES:
            continue
        notice = soup.select_one(f'section.page[data-role="{role}"] [data-two-layer-notice]')
        results.check(f"{role}: page 1 carries the two-layer truth notice", notice is not None)
        if notice is None:
            continue
        first_page = pages_for(soup, role)[0]
        results.check(f"{role}: the notice is on page 1",
                      notice.find_parent(class_="page") is first_page)
        text = normalise(notice.get_text(" ", strip=True)).lower()
        for layer in two_layer["layers"][:2]:
            results.check(f"{role}: the notice names the {layer['id']} layer by its printed label",
                          layer["label"].lower() in text, layer["label"])
        results.check(f"{role}: the notice states the non-merger rule",
                      "proves nothing about" in text, text[:200])

    # Fictional data must be labelled, and must live inside fictional or model evidence.
    fictional_nodes = soup.select("[data-fictional-data]")
    results.check("the packet marks its fictional case data", len(fictional_nodes) >= 6,
                  len(fictional_nodes))
    for node in fictional_nodes:
        holder = node.find_parent(attrs={"data-evidence-layer": True})
        results.check("fictional data sits inside a fictional or curriculum-model object",
                      holder is not None
                      and holder.get("data-evidence-layer") in {"fictional", "curriculum-model"},
                      str(node)[:120])
    for role in LEARNER_ROLES:
        figure = soup.select_one(f'section.page[data-role="{role}"] [data-chronology-contract]')
        holder = figure if figure is not None and figure.name == "figure" \
            else (figure.find_parent("figure") if figure is not None else None)
        results.check(f"{role}: the figure displaying fictional values prints FICTIONAL CASE DATA",
                      holder is not None
                      and "FICTIONAL CASE DATA" in normalise(
                          holder.get_text(" ", strip=True)).upper())

    # --- SYSTEMS FRAME ------------------------------------------------------
    zones = registry["systemsFrame"]["zones"]
    zone_labels = [z["label"] for z in zones]
    for role in LEARNER_ROLES:
        figure = soup.select_one(f'section.page[data-role="{role}"] [data-boundary-contract]')
        results.check(f"{role}: the system-boundary figure is present", figure is not None)
        if figure is None:
            continue
        text = normalise(figure.get_text(" ", strip=True)).upper()
        missing = [z for z in zone_labels if z not in text]
        results.check(f"{role}: the boundary figure prints all three zone labels", not missing, missing)
        results.check(f"{role}: the boundary figure prints where the monitoring stops",
                      figure.select_one("[data-zone='monitoring']") is not None
                      and "DID NOT WATCH" in text, text[:200])

    # --- SCIENCE QUALIFICATION: HHH-GAME-C1L6-001 ---------------------------
    science = registry["scienceQualification"]
    results.check("the science qualification names the audit finding",
                  science["findingId"] == "HHH-GAME-C1L6-001"
                  and science["dependencyClass"] == "CURRICULUM_QUALIFICATION_REQUIRED")
    boundary_ids = {b["id"] for b in science["boundaries"]}
    results.check("all four science boundaries are declared",
                  boundary_ids == {"consortium-composition", "plant-usable-forms",
                                   "toxicity-threshold", "ammonia-ammonium-distinction"},
                  sorted(boundary_ids))
    for boundary in science["boundaries"]:
        for source_id in boundary["supportingSources"]:
            results.check(f"boundary {boundary['id']} cites a canonical source",
                          source_id in source_layers, source_id)
            results.check(f"boundary {boundary['id']} is supported by a real-world source",
                          source_layers.get(source_id) == "real", source_id)
        for task_id in boundary["assessedIn"]:
            results.check(f"boundary {boundary['id']} names a real task",
                          any(t["id"] == task_id for t in tasks), task_id)

    for requirement in science["positiveRequirements"]:
        for role in requirement["roles"]:
            found = soup.select(f'section.page[data-role="{role}"] {requirement["selector"]}')
            results.check(f"{role}: positive requirement {requirement['id']} is printed",
                          bool(found), requirement["selector"])

    # The diversity correction must actually carry its evidence, not just a label.
    for role in LEARNER_ROLES:
        node = soup.select_one(f'section.page[data-role="{role}"] '
                               f'[data-science-qualification="consortium-composition"]')
        text = normalise(node.get_text(" ", strip=True)).lower() if node else ""
        results.check(f"{role}: the diversity note names comammox and the measured biofilter",
                      "comammox" in text and ("archaea" in text or "nitrosomonas" in text),
                      text[:220])
        node = soup.select_one(f'section.page[data-role="{role}"] '
                               f'[data-science-qualification="plant-usable-forms"]')
        text = normalise(node.get_text(" ", strip=True)).lower() if node else ""
        results.check(f"{role}: the uptake note names both usable forms",
                      "nitrate" in text and "ammonium" in text, text[:220])
        node = soup.select_one(f'section.page[data-role="{role}"] '
                               f'[data-science-qualification="ammonia-ammonium-distinction"]')
        text = normalise(node.get_text(" ", strip=True)).lower() if node else ""
        results.check(f"{role}: the speciation note prints both formulas and the pH relationship",
                      "nh4" in text.replace(" ", "") and "nh3" in text.replace(" ", "")
                      and "ph" in text, text[:220])

    # --- ACCOUNTABILITY BOUNDARY -------------------------------------------
    accountability = registry["accountabilityBoundary"]
    results.check("the accountability boundary is declared two-sided",
                  accountability["requiredFraming"] == "two-sided"
                  and len(accountability["notEstablishedByEvidence"]) >= 3
                  and len(accountability["openInstitutionalQuestions"]) >= 3)
    for task_id in accountability["assessedIn"]:
        results.check(f"the accountability boundary names a real task ({task_id})",
                      any(t["id"] == task_id for t in tasks), task_id)
    for role in LEARNER_ROLES:
        figure = soup.select_one(f'section.page[data-role="{role}"] [data-verdict-contract]')
        results.check(f"{role}: the public-record comparison is present", figure is not None)
        if figure is None:
            continue
        results.check(f"{role}: the comparison holds an open-question column",
                      bool(figure.select(".vd-open")), "no open column")
        both = figure.select_one("[data-semantic-exemption='accountability-notice']")
        results.check(f"{role}: the comparison prints both halves of the finding",
                      both is not None, "missing both-halves notice")
    # Task 8 Part C must exist as a graded demand in both learner editions.
    erc = registry["editionResponseContract"]
    open_sub = next(s for s in erc["subparts"] if s["id"] == "open-question")
    for edition in ("student", "accessible"):
        ids = open_sub[edition]
        live = {n.get("data-persist-id") for n in
                soup.select(f'section.page[data-role="{edition}"] [data-response][data-persist-id]')}
        results.check(f"{edition}: the open institutional question is a required response",
                      set(ids) <= live and bool(ids), ids)
    results.check("the Answer Key refuses both accountability failures",
                  "not accepted at any level" in answer_text.lower())

    # --- SEMANTIC GUARDS: POSITIVE CONTROL ---------------------------------
    invariants = registry["semanticInvariants"]
    exemptions = {e["id"]: e for e in invariants["exemptions"]}
    structural = [s["selector"] for s in invariants["structuralExemptSelectors"]]
    compiled = compile_classes(science["prohibitedFramings"])
    results.check("all five prohibited concept classes compile",
                  set(compiled) == {"universalTwoSpecies", "nitrateOnly",
                                    "universalToxicityThreshold", "noAccountability",
                                    "verdictAdopted"},
                  sorted(compiled))
    for role in ALL_ROLES:
        violations = scan_html(html, compiled, structural, exemptions, role)
        results.check(f"{role}: no unexempted proposition states a prohibited framing",
                      not violations, json.dumps(violations[:6], indent=1))

    # --- SEMANTIC GUARDS: NEGATIVE CONTROLS --------------------------------
    # Each guard must flag a synthetic fragment. A guard that has stopped working
    # fails the run here rather than passing the package quietly.
    NEGATIVE_CONTROLS = {
        "universalTwoSpecies": [
            "A nitrifying consortium always consists of two species.",
            "The nitrifying community is always exactly two organisms.",
            "Every biofilter has the same two species doing the work.",
            "The consortium comprises only two bacteria.",
            "A nitrifying consortium is made up of exactly two microbes.",
        ],
        "nitrateOnly": [
            "For plants, nitrate is the only usable nitrogen.",
            "Nitrate is the only form of nitrogen that plants can absorb.",
            "Crops can only take up nitrate from the water.",
            "Plants cannot use ammonium at all.",
            "Roots are unable to absorb ammonium.",
        ],
        "universalToxicityThreshold": [
            "Ammonia above 5 mg/L is toxic to plants.",
            "The crops died at 12 ppm of ammonium.",
            "Ammonium at 30 mg/L kills a crop.",
        ],
        "noAccountability": [
            "In the end, no one was responsible.",
            "Nobody was to blame for what happened here.",
            "There is no accountability in a failure of this kind.",
            "Nothing could have been done about it.",
        ],
        "verdictAdopted": [
            "The engineer caused the failure.",
            "Human error caused the failure at the facility.",
            "The nutrient-cycling design was flawed.",
            "The failure was caused by human error.",
        ],
    }
    for class_id, sentences in NEGATIVE_CONTROLS.items():
        for sentence in sentences:
            body = f"<p>{sentence}</p>"
            hits = scan_html(synthetic("student", body), compiled, structural, exemptions, "student")
            results.check(f"negative control fires for {class_id}: {sentence[:52]}",
                          any(h[2] == class_id for h in hits), hits)

    # --- SEMANTIC GUARDS: POSITIVE (MUST-NOT-FLAG) CONTROLS ----------------
    # Representative truthful prose the guards must leave alone. These confer no
    # authority: authored wording this list has never seen is expected to pass,
    # and does. They exist to prove the classifier does not overmatch.
    MUST_PASS = [
        "The conversion is conventionally described in two steps.",
        "Nitrate is not the only form a plant can use.",
        "Plants take up both nitrate and ammonium, through separate transporters.",
        "A single comammox organism can carry out both steps.",
        "The community is not a fixed pair of species.",
        "The evidence clears the named engineer of the failure the statement describes.",
        "The machinery met every setpoint the design specified.",
        "Ammonium tolerance varies by species, ecotype and cultivar.",
        "The consortium held steady for fifty-eight days and then collapsed.",
        "Two research groups reported the discovery independently in 2015.",
        "Archaea were about six hundred thousand times as abundant as Nitrosomonas.",
        "The statement is evidence of what an institution said, and of nothing else.",
        "There is still a question about what the facility should have been required to monitor.",
        "The dosing hardware measured total nutrient and not which form the nitrogen was in.",
    ]
    for sentence in MUST_PASS:
        body = f"<p>{sentence}</p>"
        hits = scan_html(synthetic("student", body), compiled, structural, exemptions, "student")
        results.check(f"truthful prose is not flagged: {sentence[:52]}", not hits, hits)

    # --- EXEMPTION CONTRACT IS CLOSED --------------------------------------
    declared_exemptions = set(exemptions)
    used = {n.get("data-semantic-exemption") for n in soup.select("[data-semantic-exemption]")}
    results.check("every exemption used in markup is registered",
                  used <= declared_exemptions, sorted(used - declared_exemptions))
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
    # A guard that could be switched off by inventing an attribute is not a guard.
    forged = synthetic("student",
                       '<p data-semantic-exemption="not-a-registered-id">'
                       'A nitrifying consortium always consists of two species.</p>')
    results.check("mutation control: an unregistered exemption id does not excuse anything",
                  bool(scan_html(forged, compiled, structural, exemptions, "student")))
    wrong_role = synthetic("student",
                           '<p data-semantic-exemption="teacher-misconception">'
                           'A nitrifying consortium always consists of two species.</p>')
    results.check("mutation control: an exemption does not carry into a role it does not declare",
                  bool(scan_html(wrong_role, compiled, structural, exemptions, "student")))

    # --- SOURCE STATUS AND RUNTIME IDENTIFIERS ------------------------------
    status_contract = registry["sourceStatusContract"]
    results.check("the status vocabulary is the canonical three",
                  set(status_contract["statusVocabulary"])
                  == {"fictional / hypothetical", "documented", "modeled"},
                  status_contract["statusVocabulary"])
    for role in ALL_ROLES:
        leaked = [i for i in status_contract["prohibitedRuntimeIdentifiers"]
                  if i.lower() in texts[role].lower()]
        results.check(f"{role}: no runtime implementation identifier is printed", not leaked, leaked)
    results.check("every prohibited runtime identifier is identifier-shaped",
                  all(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", i)
                      for i in status_contract["prohibitedRuntimeIdentifiers"]),
                  [i for i in status_contract["prohibitedRuntimeIdentifiers"]
                   if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", i)])

    # Every canonical source must be reachable by a learner or named in the ledger.
    ledger_rows = soup.select("[data-ledger-source]")
    ledger_ids: set[str] = set()
    for row in ledger_rows:
        ledger_ids |= set(row.get("data-ledger-source").split())
    canonical = {s["id"] for s in registry["caseSources"]}
    results.check("the Teacher ledger covers every canonical source",
                  ledger_ids == canonical, sorted(canonical - ledger_ids))
    results.check("the registry declares fifteen canonical sources", len(canonical) == 15,
                  len(canonical))
    for layer, expected in (("fictional", 5), ("real", 5), ("curriculum-model", 5)):
        count = sum(1 for v in source_layers.values() if v == layer)
        results.check(f"the estate holds {expected} {layer} sources", count == expected, count)
    for source in registry["caseSources"]:
        results.check(f"source {source['id']} declares a contribution and a limitation",
                      len(source.get("contribution", "")) > 40
                      and len(source.get("limitation", "")) > 40, source["id"])

    # --- FALLBACK CORRESPONDENCE RESOLVES TO REAL PAGES ---------------------
    # Every source states where a learner without the game finds it. Those page
    # numbers are the no-game route's index, and they drift silently whenever a
    # page is added, split or recomposed - which happened twice during this
    # build and was caught by eye rather than by a gate. Checking the declared
    # numbers against the pages the source actually appears on turns that into a
    # failure. Roman-numbered figure rows and teacher-only pointers are ignored;
    # only "Student page N" and "Accessible page(s) N" claims are resolved.
    PAGE_CLAIM = re.compile(r"(Student|Accessible) pages? ((?:\d+)(?:(?:,| and| to) \d+)*)", re.I)
    for source in registry["caseSources"]:
        claim = source.get("fallbackCorrespondence", "")
        for role_word, numbers in PAGE_CLAIM.findall(claim):
            role = role_word.lower()
            declared = {int(n) for n in re.findall(r"\d+", numbers)}
            actual = {int(page.get("data-page-id").rsplit("-", 1)[1])
                      for page in pages_for(soup, role)
                      if page.select(f'[data-source-id~="{source["id"]}"]')}
            results.check(
                f"{source['id']}: declared {role} fallback page(s) {sorted(declared)} carry the source",
                declared <= actual,
                f"declared {sorted(declared)}, source actually appears on {sorted(actual)}")

    # Teacher page pointers must name a page that exists and, where the pointer
    # names a section, a page that actually carries it.
    teacher_pages = {page.get("data-page-id"): normalise(page.get_text(" ", strip=True))
                     for page in pages_for(soup, "teacher")}
    POINTERS = [
        (r"[Ff]ull citations are on pages (\d+) and (\d+)", ("Authoritative sources", "Source ledger")),
        (r"the scoring rule are on page (\d+)", ("Scoring the Accessible edition",)),
        (r"science-qualification note on page (\d+)", ("What this case must carry from the audit",)),
    ]
    for pattern, needles in POINTERS:
        for match in re.finditer(pattern, texts["teacher"]):
            for number in match.groups():
                page_id = f"teacher-guide-{int(number):02d}"
                body = teacher_pages.get(page_id, "")
                results.check(f"Teacher pointer to page {number} names a page that carries it",
                              bool(body) and any(n in body for n in needles),
                              f"{page_id}: expected one of {needles}")

    # --- ACCESSIBLE ADAPTATIONS ARE TRUE AND DECLARED -----------------------
    declared_adaptations = registry["accessibleAdaptations"]
    adaptation_ids = {a["id"] for a in declared_adaptations}
    results.check("exactly four Accessible adaptations are declared, and no fifth has appeared",
                  len(declared_adaptations) == 4, sorted(adaptation_ids))

    student_stages = soup.select('section.page[data-role="student"] .pw-chain .pw-blank [data-response]')
    accessible_stages = soup.select('section.page[data-role="accessible"] .pw-chain .pw-blank [data-response]')
    modelled_stage = soup.select('section.page[data-role="accessible"] .pw-chain .pw-modelled')
    results.check("Task 4: the Student edition completes two open stages",
                  len(student_stages) == 2, len(student_stages))
    results.check("Task 4: the Accessible edition completes one, with one supplied as a worked model",
                  len(accessible_stages) == 1 and len(modelled_stage) == 1,
                  f"{len(accessible_stages)} open, {len(modelled_stage)} modelled")
    results.check("Task 4: the modelled stage is printed as an example rather than as a blank",
                  all("WORKED EXAMPLE" in normalise(n.get_text(" ", strip=True)).upper()
                      for n in modelled_stage) and not any(n.select("[data-response]")
                                                           for n in modelled_stage))

    student_cells = soup.select('section.page[data-role="student"] .audit-table tbody [data-response]')
    accessible_cells = soup.select('section.page[data-role="accessible"] .audit-table tbody [data-response]')
    prefilled = soup.select('section.page[data-role="accessible"] .audit-table tr.model-row td.prefilled')
    results.check("Task 6: the Student edition completes ten matrix cells",
                  len(student_cells) == 10, len(student_cells))
    results.check("Task 6: the Accessible edition completes eight, with two supplied as a worked model",
                  len(accessible_cells) == 8 and len(prefilled) == 2,
                  f"{len(accessible_cells)} open, {len(prefilled)} prefilled")
    results.check("Task 6: the modelled row is printed as an example rather than as a blank",
                  all("EXAMPLE" in normalise(c.get_text(" ", strip=True)).upper() for c in prefilled))

    dated = soup.select('section.page[data-role="accessible"] .chrono-dated .chrono-card-day')
    student_dated = soup.select('section.page[data-role="student"] .chrono-card-list .chrono-card-day')
    results.check("Task 5: only the Accessible cards carry their day labels",
                  len(dated) == 4 and not student_dated,
                  f"accessible {len(dated)}, student {len(student_dated)}")
    pointers = soup.select('section.page[data-role="accessible"] .account-item .account-pointer')
    student_pointers = soup.select('section.page[data-role="student"] .account-item .account-pointer')
    results.check("Task 7: only the Accessible accounts carry source pointers",
                  len(pointers) == 5 and not student_pointers,
                  f"accessible {len(pointers)}, student {len(student_pointers)}")

    for adaptation in declared_adaptations:
        task = next(t for t in tasks if t["id"] == adaptation["task"])
        label = f"{task['number']} · {task['title']}"
        results.check(f"adaptation {adaptation['id']} is disclosed to the teacher",
                      normalise(label) in teacher_text, adaptation["id"])
        for role in adaptation["declaredIn"]:
            results.check(f"adaptation {adaptation['id']} declares a real role",
                          role in ALL_ROLES, role)
    results.check("the Teacher scoring note still claims exactly four scored differences",
                  "Four scored differences, and only four" in teacher_text)
    results.check("the Teacher scoring note is a declared adaptation block",
                  soup.select_one('[data-accessible-adaptation]') is not None)
    WORDS = {1: "one", 2: "two", 8: "eight", 10: "ten"}
    for sub in [s for s in erc["subparts"] if s["differenceClass"] == "declared-reduction"]:
        ns, na = len(sub["student"]), len(sub["accessible"])
        results.check(f"the Answer Key discloses both edition counts for {sub['task']} {sub['id']}",
                      WORDS[ns] in answer_text.lower() and WORDS[na] in answer_text.lower(),
                      f"expected {WORDS[ns]} and {WORDS[na]}")

    # --- EDITION RESPONSE PARITY, AGAINST DECLARED OBLIGATIONS -------------
    subparts = erc["subparts"]
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
    results.check("every declared reduction is governed by a registered adaptation",
                  {s["governedBy"] for s in subparts if s["differenceClass"] == "declared-reduction"}
                  <= adaptation_ids)
    results.check("the contract forbids an accessible-only obligation class",
                  erc["differenceClasses"]["accessible-only"].startswith("PROHIBITED"))
    # Mutation control: a fabricated Accessible-only subpart must be rejected.
    forged_sub = {"task": "C06-T3", "id": "forged", "obligation": "x",
                  "student": [], "accessible": ["a3-forged"], "differenceClass": "parity"}
    results.check("mutation control: an Accessible-only subpart fails the parity rule",
                  len(forged_sub["student"]) == 0)

    # --- RESPONSE SPACE -----------------------------------------------------
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
    results.check("the Accessible edition offers at least as many resizable areas as the Student edition",
                  len(layout["areas"]) >= len(layout["student"]["areas"]),
                  f"accessible {len(layout['areas'])} vs student {len(layout['student']['areas'])}")
    # Every mark, selection and classification is recordable in fill mode.
    for role in LEARNER_ROLES:
        marks = soup.select(f'section.page[data-role="{role}"] .mark-response')
        results.check(f"{role}: every printed mark has a persistent control",
                      all(m.has_attr("data-response") and m.has_attr("data-persist-id")
                          for m in marks) and bool(marks), len(marks))

    # --- CLAIM SCHEME -------------------------------------------------------
    marks = [c["mark"] for c in registry["claimJudgments"]["claims"]]
    results.check("the account set carries one supported, three contradicted and one undecidable",
                  marks == ["Y", "N", "N", "N", "?"], marks)
    results.check("the science-qualification account is one the evidence refuses",
                  registry["claimJudgments"]["claims"][3]["layer"] == "microbiology"
                  and registry["claimJudgments"]["claims"][3]["mark"] == "N")
    results.check("the trigger account is the undecidable one",
                  registry["claimJudgments"]["claims"][4]["layer"] == "trigger"
                  and registry["claimJudgments"]["claims"][4]["mark"] == "?")
    for role in LEARNER_ROLES:
        accounts = soup.select(f'section.page[data-role="{role}"] .account-item')
        results.check(f"{role}: prints five accounts, each with a persistent mark control",
                      len(accounts) == 5 and all(a.select_one("[data-response]") for a in accounts),
                      len(accounts))
    statement_marks = registry["claimJudgments"]["statementClaims"]
    results.check("the public statement is audited claim by claim, with one undecidable",
                  [c["mark"] for c in statement_marks] == ["N", "N", "?"],
                  [c["mark"] for c in statement_marks])

    # --- UNSETTLED DETAILS --------------------------------------------------
    unsettled = {u["id"] for u in registry["unsettledDetails"]}
    results.check("the case declares its unsettled details",
                  {"collapse-trigger", "consortium-species"} <= unsettled, sorted(unsettled))
    for item in registry["unsettledDetails"]:
        for role in item["printedIn"]:
            results.check(f"unsettled detail {item['id']} declares a real role",
                          role in ALL_ROLES, role)

    # --- FIGURE ACCESSIBILITY PARITY ---------------------------------------
    # Accessibility text is a factual curriculum surface, not a caption. It is
    # held to the same contracts as the visible figure.
    for spec in registry["figureAccessibilityContract"]["figures"]:
        selector = spec["selector"]
        for role in spec["roles"]:
            figure = soup.select_one(f'section.page[data-role="{role}"] {selector}')
            results.check(f"{role}: figure {spec['id']} is present", figure is not None, selector)
            if figure is None:
                continue
            if not spec.get("requiresAccessibilityText", True):
                # A data table carries its own semantics through caption, thead
                # and scoped row headers. Wrapping one in role="img" with a prose
                # alt would replace a navigable structure with a paragraph, which
                # is a regression rather than an accessibility gain.
                caption = figure.select_one("caption") if figure.name == "table" \
                    else figure.select_one("table caption")
                results.check(f"{role}: figure {spec['id']} carries a caption instead of alt text",
                              caption is not None)
                scoped = figure.select("tbody th[scope='row']") if figure.name == "table" \
                    else figure.select("table tbody th[scope='row']")
                results.check(f"{role}: figure {spec['id']} gives every row a scoped header",
                              bool(scoped), len(scoped))
                alt = ""
            else:
                described = figure if figure.get("role") == "img" and figure.get("aria-label") \
                    else figure.select_one("[role='img'][aria-label]")
                results.check(f"{role}: figure {spec['id']} carries accessibility text",
                              described is not None)
                if described is None:
                    continue
                alt = normalise(described.get("aria-label")).lower()
            for pattern in spec.get("prohibitedPatterns", []):
                hit = re.search(pattern["regex"], alt, re.I)
                results.check(f"{role}: {spec['id']} accessibility text avoids {pattern['id']}",
                              hit is None,
                              (hit.group(0) if hit else "") + " :: " + pattern["why"])
            if spec.get("requiresAllZones"):
                missing = [z.lower() for z in zone_labels if z.lower() not in alt]
                results.check(f"{role}: {spec['id']} accessibility text names all three zones",
                              not missing, missing)
            if spec.get("requiresMonitoringGap"):
                results.check(f"{role}: {spec['id']} accessibility text states where the monitoring stops",
                              "did not watch" in alt, alt[:160])
            if spec.get("requiresSchematicDisclaimer"):
                results.check(f"{role}: {spec['id']} accessibility text refuses plan readings",
                              "not to scale" in alt and "not a plan" in alt, alt[:160])
            for form in spec.get("requiresAllForms", []):
                results.check(f"{role}: {spec['id']} accessibility text names {form}", form in alt)
            if spec.get("requiresBothUsableForms"):
                results.check(f"{role}: {spec['id']} accessibility text keeps both usable forms",
                              "nitrate and as ammonium" in alt or "both forms" in alt, alt[:200])
            if spec.get("requiresDiversityNote"):
                results.check(f"{role}: {spec['id']} accessibility text carries the diversity note",
                              "comammox" in alt and "not a fixed pair" in alt, alt[:200])
            if spec.get("requiresFictionalDataLabel"):
                results.check(f"{role}: {spec['id']} accessibility text labels its values fictional",
                              "fictional case data" in alt, alt[:160])
            if spec.get("requiresEngineeringRail"):
                results.check(f"{role}: {spec['id']} accessibility text carries the unbroken engineering rail",
                              "no alarm raised" in alt and "unbroken" in alt, alt[:200])
            if spec.get("requiresAllRecords"):
                rows = soup.select(f'section.page[data-role="{role}"] .audit-table tbody tr')
                results.check(f"{role}: {spec['id']} prints all five records",
                              len(rows) == spec["requiresAllRecords"], len(rows))
            if spec.get("requiresBothColumns"):
                headers = [normalise(th.get_text(" ", strip=True)).lower()
                           for th in soup.select(f'section.page[data-role="{role}"] .audit-table thead th')]
                results.check(f"{role}: {spec['id']} keeps both audit columns",
                              any("measures" in h for h in headers)
                              and any("cannot show" in h for h in headers), headers)
            if spec.get("requiresOpenQuestionColumn"):
                results.check(f"{role}: {spec['id']} accessibility text carries the open-question column",
                              "still open" in alt, alt[:160])
            if spec.get("requiresBothAccountabilityHalves"):
                results.check(f"{role}: {spec['id']} accessibility text carries both accountability halves",
                              "clears the named engineer" in alt
                              and "does not close" in alt, alt[:220])

    # --- STANDARDS ----------------------------------------------------------
    standards = registry["standards"]
    results.check("no NGSS performance expectation is claimed as directly assessed",
                  not any(s.startswith("NGSS") for s in standards["directlyAssessed"]),
                  standards["directlyAssessed"])
    results.check("every NGSS reference is contextual and carries a written limit",
                  all(s.startswith("NGSS") for s in standards["contextual"])
                  and len(standards["ngss"]) > 80)
    results.check("the standards choice is justified against what the tasks assess",
                  len(standards.get("rationale", "")) > 120)
    for claim in standards["directlyAssessed"] + standards["supporting"] + standards["contextual"]:
        results.check(f"standard {claim} appears in the Teacher standards table",
                      claim in teacher_text, claim)

    # --- TEACHER EDITION CONTRACT ------------------------------------------
    for needle, label in (("Launch sheet", "launch sheet"),
                          ("Standards alignment", "standards alignment"),
                          ("Measurable objectives", "measurable objectives"),
                          ("Success criteria", "success criteria"),
                          ("Academic vocabulary", "academic vocabulary"),
                          ("Complete teaching procedure", "teaching procedure"),
                          ("Misconceptions", "misconceptions"),
                          ("Quick classroom rubric", "quick rubric"),
                          ("Complete analytic rubric", "analytic rubric"),
                          ("Authoritative sources", "authoritative reference list"),
                          ("Complete no-game evidence fallback", "no-game fallback")):
        results.check(f"Teacher Guide provides the {label}", needle in teacher_text, needle)
    rubric_levels = soup.select('section.page[data-role="teacher"] .analytic-rubric thead th')
    results.check("the analytic rubric uses four performance levels",
                  sum(1 for th in rubric_levels
                      if re.match(r"[1-4]\s", normalise(th.get_text(" ", strip=True)))) == 4,
                  [normalise(th.get_text(" ", strip=True)) for th in rubric_levels])
    for number in (str(t["number"]) for t in tasks):
        results.check(f"the Answer Key keys task {number}",
                      soup.select_one(f'section.page[data-role="answer"] '
                                      f'[data-shell-task-heading="{number}"]') is not None)
    results.check("every registry task is declared keyed", all(t["keyed"] for t in tasks))
    results.check("every registry task is present in all four editions",
                  all(tuple(t["editions"]) == ALL_ROLES for t in tasks))

    # --- VOCABULARY ---------------------------------------------------------
    vocabulary = registry["vocabulary"]
    results.check("the case declares seven vocabulary terms", len(vocabulary) == 7, vocabulary)
    results.check("the vocabulary bank is alphabetical", vocabulary == sorted(vocabulary))
    for role in LEARNER_ROLES:
        items = [normalise(i.get_text(" ", strip=True)) for i in
                 soup.select(f'section.page[data-role="{role}"] .word-bank-item')]
        results.check(f"{role}: the word bank prints exactly the declared terms",
                      items == vocabulary, items)
        blanks = soup.select(f'section.page[data-role="{role}"] .term-list .inline-response')
        results.check(f"{role}: one blank per term", len(blanks) == len(vocabulary), len(blanks))
    for term in vocabulary:
        results.check(f"the Teacher vocabulary table defines {term}", term in teacher_text, term)

    payload = {
        "validator": "hhh-case06-vertical-farm-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": [a for a in results.assertions if a["status"] == "FAIL"] or "all passed",
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
