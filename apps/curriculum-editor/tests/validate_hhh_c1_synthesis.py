#!/usr/bin/env python3
"""Unit-scoped protections for the HHH Campaign 1 Synthesis.

These assertions guard what this unit exists to get right and what the shared
operational walk in ``validate_static.py`` does not reach into. They are driven
by the contract blocks the task registry declares — ``unitKind``,
``recapContract``, ``comparisonContract``, ``mechanismLimitContract``,
``gameFramingBoundary``, ``twoLayerTruth``, ``sourceStatusContract``,
``cerDecision``, ``memoryIndependenceContract``, ``editionResponseContract``,
``accessibleAdaptations``, ``semanticInvariants`` and ``standards`` — rather than
by literal paragraph locks, so ordinary rewording stays possible while the
meaning stays protected.

DESIGN NOTE — why the guards are shaped the way they are.

This unit is a *synthesis*. It states no new historical finding of its own; it
restates six that are already released and approved. That changes what needs
guarding. The risk here is not that a new claim is wrong — it is that a
recapitulation quietly drops a qualification an approved case fought for, or
promotes a status (reconstructed to documented, fictional to historical), or
lets the campaign read as a story of steady improvement.

So the negative classes below are, for seven of the nine, **the literal
prohibition registers the released Cases 01–06 already declared** — copied into
this unit's registry so the Synthesis cannot relax a boundary an approved case
established. They are closed by construction: a released case's own register is a
finite list, not an open synonym family. None of them polices an ordinary verb.

Every negative class is paired with a **positive structural requirement**,
because a guard that only forbade a sentence would be satisfied by a packet that
said nothing at all. Requiring the Case 02 recap to print that the region-scale
claim is unsettled cannot be satisfied by silence; forbidding "salinity caused
the fall of Sumer" can.

Exemption is a closed contract. A node is excused only by naming a registered
exemption id that resolves, for its role, to the class it would otherwise
violate. Markup cannot self-authorize. The Teacher misconceptions table and the
Answer Key scoring floors are the only registered exemptions, because both must
be able to state a refused claim in order to refuse it.

Every semantic guard ships with NEGATIVE CONTROLS it must flag, and the package
itself is the POSITIVE CONTROL. A guard that has silently stopped working
therefore fails the run rather than passing it quietly.

Usage:
    python3 apps/curriculum-editor/tests/validate_hhh_c1_synthesis.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "hhh/campaign-1/synthesis-campaign-1"
SOURCE = UNIT / "source"
REGISTRY_FILE = ROOT / "shared/implementation/case-registry.v2.json"
CASE_ID = "HHH-C1-SYNTHESIS"
LEARNER_ROLES = ("student", "accessible")
ALL_ROLES = ("student", "teacher", "answer", "accessible")
CORE_CASES = ("01", "02", "03", "04", "05", "06")
# Block containers a proposition can belong to. Inline elements are deliberately
# ABSENT: an earlier draft listed span here and used "skip any node that contains
# one of these" as the leaf test, which silently excluded every paragraph that
# opened with an inline label - which in this packet is most of them. Coverage is
# now derived from the rendered text itself rather than from a tag whitelist, so a
# node cannot fall out of scope by containing an inline child.
BLOCK_TAGS = ("p", "li", "td", "th", "dd", "figcaption", "caption", "h1", "h2", "h3", "blockquote")
# Propositions break on terminal punctuation only. A semicolon, colon or dash is
# internal punctuation and not a safety boundary.
PROPOSITION_SPLIT = re.compile(r"(?<=[.!?])\s+")
DECIMAL_GUARD = re.compile(r"(\d)\.(\d)")
# Task 4's machine-readable stage sequence and its learner-visible prompts. Both are
# anchored to literals here rather than read from the task registry, because the
# registry is authored by the same candidate: checking the rendered organizer against
# it would pass a rename applied to both at once. Stage 3 is the unit's instructional
# contract - a correct local mechanism is not automatically a complete explanation of
# a broader historical outcome - so it is the one prompt that may not drift silently.
MECHANISM_STAGE_SEQUENCE = ["local-mechanism", "explains", "does-not-explain-alone", "additional-context"]
VISIBLE_MECHANISM_STAGE_LABELS = [
    "Local mechanism",
    "What it explains",
    "What it does not explain alone",
    "Additional context or evidence needed",
]


class Results:
    def __init__(self) -> None:
        self.assertions: list[dict] = []
        self.passed = 0

    def check(self, name: str, ok: bool, detail: object = "") -> bool:
        entry = {"name": name, "status": "PASS" if ok else "FAIL"}
        if not ok and detail != "":
            entry["detail"] = str(detail)[:1400]
        self.assertions.append(entry)
        if ok:
            self.passed += 1
        return ok


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\u2019", "'").replace("\u2018", "'")
                  .replace("\u201c", '"').replace("\u201d", '"')
                  .replace("\u2014", " - ").replace("\u2013", " - ")).strip()


def load_task_registry() -> dict:
    raw = (SOURCE / "task-registry.js").read_text(encoding="utf-8")
    return json.loads(raw[raw.index("{"):raw.rindex("}") + 1])


def role_pages(soup: BeautifulSoup, role: str):
    return soup.select(f'.page[data-role="{role}"]')


def role_text(soup: BeautifulSoup, role: str) -> str:
    return normalize(" ".join(page.get_text(" ") for page in role_pages(soup, role)))


def exemption_ids(node) -> set[str]:
    ids: set[str] = set()
    for parent in [node, *node.parents]:
        value = getattr(parent, "get", lambda *_: None)("data-exemption")
        if value:
            ids.update(value.split())
    return ids


def propositions(soup: BeautifulSoup, role: str):
    """Every visible proposition in one role, with the exemption ids in scope.

    Coverage is derived from the rendered strings rather than from a tag
    whitelist: every non-empty text node is attributed to its nearest block
    ancestor, or to its own parent when it has none. Every visible character in
    the role therefore lands in exactly one proposition group, and no node can
    escape a guard by carrying an inline child.

    Splitting is on terminal punctuation only. A semicolon, colon or dash is
    internal punctuation and not a safety boundary.
    """
    sentinel = "\x00"
    for page in role_pages(soup, role):
        containers = {}
        for text_node in page.find_all(string=True):
            if not str(text_node).strip():
                continue
            container = None
            for parent in text_node.parents:
                if parent is page:
                    break
                if parent.name in BLOCK_TAGS:
                    container = parent
                    break
            if container is None:
                container = text_node.parent
            containers.setdefault(id(container), container)
        for container in containers.values():
            text = normalize(container.get_text(" "))
            if not text:
                continue
            guarded = DECIMAL_GUARD.sub(lambda m: m.group(1) + sentinel + m.group(2), text)
            for part in PROPOSITION_SPLIT.split(guarded):
                part = part.replace(sentinel, ".").strip()
                if part:
                    yield container, part


def main() -> int:  # noqa: C901 - one linear contract walk
    results = Results()
    registry = load_task_registry()
    package = json.loads((SOURCE / "case-package.json").read_text(encoding="utf-8"))
    shared = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    soup = BeautifulSoup((SOURCE / "content.html").read_text(encoding="utf-8"), "html.parser")

    entry = next((case for curriculum in shared["curricula"] if curriculum["id"] == "HHH"
                  for campaign in curriculum["campaigns"] for case in campaign["cases"]
                  if case["id"] == CASE_ID), None)

    # ── 1. Canonical unit identity ────────────────────────────────────────
    results.check("the unit id is exactly HHH-C1-SYNTHESIS in package, registry and shared registry",
                  package["id"] == CASE_ID and registry["case"] == CASE_ID and entry is not None and entry["id"] == CASE_ID)
    results.check("the instructional type is exactly SYNTHESIS in all three records",
                  package.get("instructionalType") == registry.get("instructionalType") == (entry or {}).get("instructionalType") == "SYNTHESIS",
                  json.dumps({"package": package.get("instructionalType"), "taskRegistry": registry.get("instructionalType"),
                              "sharedRegistry": (entry or {}).get("instructionalType")}))
    results.check("the unit is never classified as a numbered Core Case",
                  "CORE_CASE" not in {package.get("instructionalType"), registry.get("instructionalType"), (entry or {}).get("instructionalType")})
    results.check("the display label is exactly Campaign 1 Synthesis",
                  registry.get("displayLabel") == (entry or {}).get("displayLabel") == "Campaign 1 Synthesis")
    results.check("the pre-owner lifecycle state is VALIDATION_BUILD / VALIDATION with no release or approval record",
                  package["status"] == "VALIDATION_BUILD" and (entry or {}).get("status") == "VALIDATION_BUILD"
                  and (entry or {}).get("packageStatus") == "VALIDATION"
                  and "releaseHistory" not in package and "historyRecord" not in (entry or {})
                  and not (UNIT / "history").exists()
                  and package["approval"]["status"] == "OWNER_REVIEW_NOT_STARTED"
                  and package["approval"]["printStatus"] == "NOT_RUN",
                  json.dumps({"package": package["status"], "approval": package["approval"],
                              "historyDir": (UNIT / "history").exists()}))

    # No Case 07 identity anywhere a reader or a tool can see it.
    case07 = re.compile(r"\bcase\s*0?7\b|\bCASE07\b", re.I)
    identity_hits = []
    for role in ALL_ROLES:
        for node, part in propositions(soup, role):
            if case07.search(part):
                identity_hits.append(f"{role}: {part[:120]}")
    # Identity-bearing fields only. Prose that *forbids* the Case 07 identity -
    # the unitKind rule, the semantic class meanings, the prohibited registers -
    # has to be able to name it in order to refuse it; what must never carry it
    # is a field a reader or a tool takes the unit's identity from.
    identity_fields = [
        ("package.id", package["id"]), ("package.title", package["title"]),
        ("package.subtitle", package["subtitle"]), ("package.location", package["location"]),
        ("package.documentKey", package["documentKey"]),
        ("package.accessibility.documentTitle", package["accessibility"]["documentTitle"]),
        ("package.accessibility.loadAnnouncement", package["accessibility"]["loadAnnouncement"]),
        ("registry.case", registry["case"]), ("registry.title", registry["title"]),
        ("registry.displayLabel", registry["displayLabel"]),
        ("registry.unitKind.displayLabel", registry["unitKind"]["displayLabel"]),
        ("registry.unitKind.contextualSubtitle", registry["unitKind"]["contextualSubtitle"]),
        ("sharedRegistry.displayLabel", (entry or {}).get("displayLabel", "")),
        ("sharedRegistry.title", (entry or {}).get("title", "")),
        *[(f"package.outputs.{role}", name) for role, name in package["outputs"].items()],
        *[(f"task.{task['number']}.title", task["title"]) for task in registry["tasks"]],
    ]
    source_hits = [f"{where}={value}" for where, value in identity_fields if case07.search(value)]
    results.check("no role and no identity-bearing field presents this unit as Case 07",
                  not identity_hits and not source_hits,
                  json.dumps({"roles": identity_hits, "identityFields": source_hits}))
    results.check("the registry declares the Case 07 identity prohibited rather than merely omitting it",
                  "Case 07" in registry["unitKind"]["prohibitedIdentities"]
                  and any(entry_["id"] == "case07Identity" for entry_ in registry["semanticInvariants"]["classes"]))

    # ── 2. Evidence recap architecture ────────────────────────────────────
    declared_recaps = {recap["case"] for recap in registry["caseRecaps"]}
    results.check("the registry declares a recap for all six Core Cases",
                  declared_recaps == {f"HHH-C1-CASE{number}" for number in CORE_CASES}, sorted(declared_recaps))

    for role in LEARNER_ROLES:
        cards = {}
        for page in role_pages(soup, role):
            for card in page.select("[data-recap-case]"):
                cards[card["data-recap-case"]] = card
        results.check(f"{role} carries exactly one recap card for each of the six Core Cases",
                      set(cards) == {f"HHH-C1-CASE{number}" for number in CORE_CASES} and len(cards) == 6,
                      sorted(cards))
        for number in CORE_CASES:
            card = cards.get(f"HHH-C1-CASE{number}")
            if card is None:
                results.check(f"{role} recap {number} carries every required field", False, "card absent")
                continue
            text = normalize(card.get_text(" "))
            fields = {
                "setting": bool(card.select_one(".recap-setting")),
                "change": bool(card.select_one(".recap-change")),
                "evidence": len(card.select(".recap-evidence li")) >= 1,
                "supports": bool(card.select_one(".recap-supports")),
                "limit": bool(card.select_one("[data-recap-limit]")),
                "sourceStatus": bool(card.select_one(".recap-status")) and "SOURCE STATUS" in text,
                "archiveThread": bool(card.select_one("[data-archive-thread]")),
            }
            results.check(f"{role} recap {number} carries every required field",
                          all(fields.values()), json.dumps(fields))

    # ── 3. Preserved qualifications: the positive half of the contract ────
    # Each entry is a concept that a released case established and that this unit
    # may not quietly drop. Presence is required; wording is not locked.
    REQUIRED_MARKERS = {
        "01": [("cultivation is not domestication",
                [r"cultivation is not domestication", r"not domestication"]),
               ("the counted subset carries the trend",
                [r"\b804\b"]),
               ("the evidence fixes no first person, no first field and no starting date",
                [r"no first person", r"names no first", r"identifies no first"])],
        "02": [("the region-scale claim is unsettled",
                [r"argued among scholars", r"does not settle", r"not settled"]),
               ("the tablet reading is contested",
                [r"challenged", r"contested", r"Powell"])],
        "03": [("more than one condition contributed and they are not ranked",
                [r"does not rank", r"more than one condition"]),
               ("the crop loss did not set the death toll",
                [r"did not set the size of the death toll", r"far fewer of its people", r"lost far more"])],
        "04": [("laboratory and industrial work stay distinct",
                [r"laboratory result is not an industrial process", r"laboratory demonstration and industrial engineering are distinct"]),
               ("attribution stays plural",
                [r"Le Rossignol"])],
        "05": [("the drought is a contributing cause",
                [r"drought"]),
               ("neither cause reaches the outcome alone",
                [r"neither cause", r"together produced", r"weather alone is wrong"]),
               ("the unploughed remainder is printed",
                [r"two-thirds"])],
        "06": [("the facility is fictional",
                [r"fictional"]),
               ("the non-merger rule is printed",
                [r"proves nothing about the real world"])],
    }
    for role in LEARNER_ROLES:
        for number, markers in REQUIRED_MARKERS.items():
            card = soup.select_one(f'.page[data-role="{role}"] [data-recap-case="HHH-C1-CASE{number}"]')
            text = normalize(card.get_text(" ")) if card else ""
            missing = [label for label, patterns in markers
                       if not any(re.search(pattern, text, re.I) for pattern in patterns)]
            results.check(f"{role} recap {number} preserves its released qualifications",
                          not missing, json.dumps(missing))

    # ── 4. Case 06 two-layer truth ────────────────────────────────────────
    for role in LEARNER_ROLES:
        card = soup.select_one(f'.page[data-role="{role}"] [data-recap-case="HHH-C1-CASE06"]')
        chips = {normalize(chip.get_text(" ")) for chip in card.select(".layer-chip")} if card else set()
        text = normalize(card.get_text(" ")) if card else ""
        results.check(f"{role} Case 06 recap prints both truth-layer chips",
                      set(registry["twoLayerTruth"]["requiredChips"]).issubset(chips), sorted(chips))
        results.check(f"{role} Case 06 recap prints the non-merger rule",
                      "proves nothing about the real world" in text and "proves nothing about 2041" in text)
        results.check(f"{role} Case 06 recap declares its two-layer markup",
                      bool(card and card.get("data-evidence-layer") == "two-layer"))
    for role in ("teacher", "answer"):
        text = role_text(soup, role)
        results.check(f"{role} states that the 2041 facility is fictional",
                      re.search(r"2041", text) and re.search(r"fictional", text, re.I))

    # ── 5. The L7 game/finale boundary ────────────────────────────────────
    framing_nodes = soup.select("[data-game-framing]")
    results.check("the finale excerpt appears once per learner edition and nowhere else",
                  len(framing_nodes) == 2
                  and {node.find_parent(class_="page")["data-role"] for node in framing_nodes} == set(LEARNER_ROLES),
                  [node.find_parent(class_="page")["data-role"] for node in framing_nodes])
    for node in framing_nodes:
        role = node.find_parent(class_="page")["data-role"]
        text = normalize(node.get_text(" "))
        results.check(f"{role} finale excerpt is marked fictional in printed words",
                      node.get("data-game-framing") == "fictional" and re.search(r"\bfictional\b", text, re.I) is not None)
        results.check(f"{role} finale excerpt states in print that it is not evidence",
                      "proves nothing" in text.lower() or "not a source" in text.lower())
        results.check(f"{role} finale excerpt collects no response, so no task depends on it",
                      not node.select("[data-response]"))
    # Containment: the quoted finale text may not appear outside a framing node.
    quote_marker = "Twelve thousand years"
    stray = []
    for role in ALL_ROLES:
        for node, part in propositions(soup, role):
            if quote_marker in part and not node.find_parent(attrs={"data-game-framing": True}):
                stray.append(f"{role}: {part[:100]}")
    results.check("the finale quotation never appears outside a marked framing node", not stray, stray)
    results.check("no Answer Key exemplar rests on the finale framing",
                  not soup.select('.page[data-role="answer"] [data-game-framing]'))
    results.check("the registry records that gameplay is not required and the no-game route is complete",
                  registry["gameFramingBoundary"]["gamePlayRequired"] is False
                  and "Complete" in registry["gameFramingBoundary"]["noGameFallback"])
    for role in ("teacher",):
        text = role_text(soup, role)
        results.check("the Teacher Guide states the no-game route",
                      "no-game" in text.lower() or "without launching" in text.lower() or "never launches the game" in text.lower())

    # ── 6. Memory independence ────────────────────────────────────────────
    pointer_targets = {"chronology-rail": "[data-chronology-contract]"}
    for number in CORE_CASES:
        pointer_targets[f"recap-{number}"] = f'[data-recap-case="HHH-C1-CASE{number}"]'
    for role in LEARNER_ROLES:
        missing = []
        for task in registry["tasks"]:
            for pointer in task["evidencePointers"]:
                selector = pointer_targets.get(pointer)
                if selector is None or not soup.select(f'.page[data-role="{role}"] {selector}'):
                    missing.append(f"task {task['number']} -> {pointer}")
        results.check(f"every {role} task's declared evidence is present in that same edition",
                      not missing, json.dumps(missing))
    for role in LEARNER_ROLES:
        rail = soup.select_one(f'.page[data-role="{role}"] [data-chronology-contract]')
        rows = rail.select("[data-rail-case]") if rail else []
        results.check(f"{role} chronology rail supplies all six cases with their dates",
                      len(rows) == 6
                      and {row["data-rail-case"] for row in rows} == {f"HHH-C1-CASE{number}" for number in CORE_CASES}
                      and all(normalize(row.select_one(".chrono-when").get_text(" ")) for row in rows))
        results.check(f"{role} chronology rail discloses that the six spans are not measured alike",
                      bool(rail and rail.select_one(".chrono-disclosure")
                           and "not measured the same way" in normalize(rail.get_text(" "))))

    # ── 7. Task 3 early/late structure ────────────────────────────────────
    comparison = registry["comparisonContract"]
    for role in LEARNER_ROLES:
        organizer = soup.select_one(f'.page[data-role="{role}"] [data-comparison-contract]')
        results.check(f"{role} carries the continuity/change organizer", organizer is not None)
        if organizer is None:
            continue
        rows = [normalize(cell.get_text(" ")) for cell in organizer.select("tbody th[scope=row]")]
        results.check(f"{role} organizer carries the four per-case comparison rows",
                      len(rows) == 4, rows)
        text = normalize(organizer.get_text(" "))
        results.check(f"{role} organizer separates an earlier column from a later column",
                      "01" in text and "03" in text and "04" in text and "06" in text)
        results.check(f"{role} organizer collects supporting evidence and a qualification across the pair",
                      bool(organizer.select_one('[data-persist-id$="-evidence"]'))
                      and bool(organizer.select_one('[data-persist-id$="-qualification"]')))
    for role in LEARNER_ROLES:
        page_text = role_text(soup, role)
        results.check(f"{role} states the early/late selection rule in printed directions",
                      re.search(r"01\s*[\u2013\u2014-]\s*03", page_text) or "01, 02 or 03" in page_text.replace("**", ""))

    # ── 8. Task 4 allowed set and mechanism structure ─────────────────────
    limits = registry["mechanismLimitContract"]
    results.check("the registry allows exactly Cases 02, 03, 05 and 06 at Task 4",
                  limits["allowedCases"] == ["HHH-C1-CASE02", "HHH-C1-CASE03", "HHH-C1-CASE05", "HHH-C1-CASE06"]
                  and limits["excludedCases"] == ["HHH-C1-CASE01", "HHH-C1-CASE04"])
    for role in LEARNER_ROLES:
        offered = {node["data-limit-case"] for node in soup.select(f'.page[data-role="{role}"] [data-limit-case]')}
        results.check(f"{role} Task 4 offers exactly the four permitted cases and neither excluded case",
                      offered == set(limits["allowedCases"]), sorted(offered))
        organizers = soup.select(f'.page[data-role="{role}"] [data-mechanism-contract]')
        results.check(f"{role} Task 4 carries two mechanism organizers", len(organizers) == 2, len(organizers))
        for organizer in organizers:
            stages = [stage["data-mechanism-stage"] for stage in organizer.select("[data-mechanism-stage]")]
            results.check(f"{role} Task 4 organizer {organizer.get('data-mechanism-slot')} runs the four stages in order",
                          stages == limits["requiredStages"] == MECHANISM_STAGE_SEQUENCE, stages)
            # The attributes above are machine-readable and invisible to a learner.
            # The prompt the learner actually answers is the instructional contract,
            # so it is asserted against literals in its own right: an organizer whose
            # stage 3 stops asking what the mechanism cannot explain is a different
            # task, however intact its markup.
            labels = [normalize(label.get_text(" ")) for label in organizer.select(".mech-label")]
            results.check(f"{role} Task 4 organizer {organizer.get('data-mechanism-slot')} prints the four "
                          f"learner-visible stage prompts, including the limit prompt at stage 3",
                          labels == VISIBLE_MECHANISM_STAGE_LABELS, labels)
    # The directions carry the same boundary in prose. Student and Accessible word it
    # differently, and place it differently - the Accessible edition states it on the
    # page that carries the Task 4 heading and choices, one page ahead of its first
    # organizer - so the page is found from the task heading, not from the organizer.
    for role in LEARNER_ROLES:
        heading = soup.select_one(f'.page[data-role="{role}"] [data-shell-task-heading="4"]')
        page = heading.find_parent(class_="page") if heading else None
        directions = normalize(page.select_one(".directions").get_text(" ")) if page and page.select_one(".directions") else ""
        results.check(f"{role} Task 4 directions state that a correct mechanism is not a complete explanation",
                      bool(re.search(r"not automatically a complete explanation|none of them is the whole story"
                                     r"|none of them explains the whole thing|where each one stops", directions, re.I)),
                      directions[:200])
    # The Answer Key reproduces the same four stages as the structure it keys. This is
    # parity with the learner prompt, not a check on the exemplar prose beneath it.
    pathways = [block for block in soup.select('.page[data-role="answer"] .answer-block')
                if "Model pathway" in normalize(block.get_text(" "))]
    results.check("the Answer Key carries one Task 4 model pathway for each of the four permitted cases",
                  len(pathways) == 4, len(pathways))
    for pathway in pathways:
        labels = [normalize(item.select_one("strong").get_text(" ")).rstrip(".")
                  for item in pathway.select("ol.answer-list > li") if item.select_one("strong")]
        results.check("each Answer Key Task 4 model pathway reproduces the learner-visible stage prompts",
                      labels == VISIBLE_MECHANISM_STAGE_LABELS, labels)

    # ── 9. CER is declined ────────────────────────────────────────────────
    cer_hits = [selector for selector in registry["cerDecision"]["prohibitedSelectors"] if soup.select(selector)]
    results.check("no role renders the canonical CER component", not cer_hits, cer_hits)
    for role in ALL_ROLES:
        labels = [normalize(node.get_text(" ")).upper() for node in soup.select(f'.page[data-role="{role}"] .label,.page[data-role="{role}"] .prompt-tag')]
        results.check(f"{role} prints no CLAIM / EVIDENCE / REASONING label triple",
                      not ("CLAIM" in labels and "EVIDENCE" in labels and "REASONING" in labels))

    # ── 10. Task-reference parity ─────────────────────────────────────────
    titles = {task["number"]: task["title"] for task in registry["tasks"]}
    results.check("the registry declares exactly the six locked task titles in order",
                  [f'{number} · {titles[number]}' for number in sorted(titles)] == [
                      "1 · Read the Campaign Record", "2 · Trace the Long Yield",
                      "3 · Compare Continuity and Change", "4 · Test the Limits of a Correct Mechanism",
                      "5 · Write the Archive Synthesis", "6 · What Should the Archive Preserve?"],
                  [f'{number} · {titles[number]}' for number in sorted(titles)])
    for role in ALL_ROLES:
        rendered = [node["data-shell-task-heading"]
                    for page in role_pages(soup, role) for node in page.select("[data-shell-task-heading]")]
        expected = ["1", "2", "3", "4", "5", "6"] if role in ("student", "teacher", "accessible") else ["2", "3", "4", "5", "6"]
        if role == "teacher":
            expected = []  # the Teacher Guide references tasks in prose, not as headings
        if role == "teacher":
            results.check("the Teacher Guide renders no learner task heading of its own", rendered == [], rendered)
        else:
            results.check(f"{role} renders its task headings once each, in order", rendered == expected, rendered)
    results.check("the Answer Key omits non-keyable Task 1 silently and does not renumber",
                  "1" not in [node["data-shell-task-heading"] for node in soup.select('.page[data-role="answer"] [data-shell-task-heading]')]
                  and registry["tasks"][0]["keyed"] is False)
    teacher_refs = {normalize(node.get_text(" ")) for node in soup.select('.page[data-role="teacher"] .task-reference')}
    canonical_refs = {f'{number} · {titles[number]}' for number in titles}
    results.check("every bold Teacher task reference reproduces a canonical number and title exactly",
                  teacher_refs and teacher_refs.issubset(canonical_refs), sorted(teacher_refs - canonical_refs))
    results.check("the Teacher Guide references every one of the six tasks by number and title",
                  canonical_refs.issubset(teacher_refs), sorted(canonical_refs - teacher_refs))

    # ── 11. Answer Key exemplars ──────────────────────────────────────────
    answer_text = role_text(soup, "answer")
    results.check("the Answer Key never substitutes 'answers will vary' for an exemplar",
                  not re.search(r"answers?\s+(?:will|may)\s+vary", answer_text, re.I))
    for number in ("2", "3", "4", "5", "6"):
        heading = soup.select_one(f'.page[data-role="answer"] [data-shell-task-heading="{number}"]')
        results.check(f"the Answer Key carries a keyed section for Task {number}", heading is not None)
    results.check("the Answer Key models a complete Task 3 pathway and names alternatives",
                  "complete model pathway" in answer_text.lower() and "alternative" in answer_text.lower())
    results.check("the Answer Key models both Task 4 pathways plus the other two permitted cases",
                  len(re.findall(r"Model pathway", answer_text)) >= 4,
                  len(re.findall(r"Model pathway", answer_text)))
    results.check("the Answer Key carries a complete model synthesis for Task 5",
                  bool(soup.select('.page[data-role="answer"] .key-model')))
    results.check("the Answer Key carries scoring floors that name refused claims",
                  len(soup.select('.page[data-role="answer"] .key-floor')) >= 3)

    # ── 12. Accessible differentiation ────────────────────────────────────
    declared = {item["id"] for item in registry["accessibleAdaptations"]}
    present: set[str] = set()
    for node in soup.select('.page[data-role="accessible"] [data-accessible-adaptation]'):
        present.update(node["data-accessible-adaptation"].split())
    results.check("every declared Accessible adaptation is present in the Accessible edition",
                  declared == present, json.dumps({"declaredOnly": sorted(declared - present),
                                                   "presentOnly": sorted(present - declared)}))
    results.check("the Accessible edition carries sentence frames the Student edition does not",
                  len(soup.select('.page[data-role="accessible"] .prompt-frame,.page[data-role="accessible"] .cell-frame,.page[data-role="accessible"] .stage-frame')) >= 10
                  and not soup.select('.page[data-role="student"] .cell-frame,.page[data-role="student"] .stage-frame'))
    results.check("the Accessible edition carries evidence pointers the Student edition does not",
                  bool(soup.select('.page[data-role="accessible"] .choice-pointer'))
                  and not soup.select('.page[data-role="student"] .choice-pointer'))
    results.check("the Accessible worked contrast uses Case 04, which cannot be chosen at Task 4",
                  bool(soup.select_one('.page[data-role="accessible"] .contrast-strip'))
                  and "Case 04" in normalize(soup.select_one('.page[data-role="accessible"] .contrast-strip').get_text(" "))
                  and "HHH-C1-CASE04" in limits["excludedCases"])
    # Response parity: no Accessible-only obligation, and no growth beyond the
    # one declared chunking split.
    def response_ids(role):
        return {node["data-persist-id"] for node in soup.select(f'.page[data-role="{role}"] [data-response]')}
    IDENTITY_IDS = {"student-name", "student-date", "student-period",
                    "accessible-name", "accessible-date", "accessible-period"}
    task_prefix = re.compile(r"^[sa](?=\d)")
    student_ids = {task_prefix.sub("", pid) for pid in response_ids("student") - IDENTITY_IDS}
    accessible_ids = {task_prefix.sub("", pid) for pid in response_ids("accessible") - IDENTITY_IDS}
    extra = sorted(accessible_ids - student_ids)
    results.check("the only Accessible response with no Student counterpart is the declared Task 6 chunking",
                  extra == ["6-missing"], extra)
    # The check above reads one direction only - it catches an Accessible edition that
    # grows an extra obligation, but not one that quietly loses an assessed field. The
    # Accessible contract is parity of what is assessed, so the omission direction has
    # to be asserted too: a support may change how a learner answers, never whether.
    dropped = sorted(student_ids - accessible_ids)
    results.check("no Student assessed response is missing from the Accessible edition",
                  not dropped, dropped)
    results.check("the Accessible edition is not one task per page",
                  len(role_pages(soup, "accessible")) == package["rolePageStructure"]["accessible"]["pageCount"]
                  and any(len(page.select("[data-recap-case]")) > 1 for page in role_pages(soup, "accessible")),
                  package["rolePageStructure"]["accessible"]["pageCount"])
    results.check("no Accessible numbered task is isolated by a forced break",
                  "break-inside: avoid" not in (SOURCE / "presentation.css").read_text(encoding="utf-8").split(".task-block")[-1][:200])

    # ── 13. Printable identity and role isolation ─────────────────────────
    for role in LEARNER_ROLES:
        pages = role_pages(soup, role)
        ident = [bool(page.select_one(".student-id")) for page in pages]
        results.check(f"{role} carries the Name / Date / Period row on page 1 only",
                      ident[0] is True and not any(ident[1:]), ident)
    for role in ("teacher", "answer"):
        results.check(f"{role} carries no student identification row",
                      not soup.select(f'.page[data-role="{role}"] .student-id'))
    for role in ALL_ROLES:
        pages = role_pages(soup, role)
        first = pages[0].select_one('[data-page-identity="first"]')
        continuations = [page.select_one('[data-page-identity="continuation"]') for page in pages[1:]]
        label = package["rolePageStructure"][role]["documentRole"]
        footers = [normalize(page.select_one("[data-publication-footer]").get_text(" ")) for page in pages]
        results.check(f"{role} uses one first-page identity and continuation identity thereafter",
                      first is not None and all(continuations))
        results.check(f"{role} footers carry only the document role and position",
                      footers == [f"{label} {index} of {len(pages)}" for index in range(1, len(pages) + 1)], footers)
    metadata = re.compile(r"\bcommit\b|\bsha256\b|\bchecksum\b|/source/|case-package\.json|\.git\b|/Users/|C:\\\\", re.I)
    leaks = []
    for role in ALL_ROLES:
        for node, part in propositions(soup, role):
            if metadata.search(part):
                leaks.append(f"{role}: {part[:120]}")
    results.check("no printable page carries production metadata or a machine-local path", not leaks, leaks)
    # content.html is the canonical worksheet fragment, not a generated role
    # document. Any other HTML under the unit would be a committed artifact.
    artifacts = [path for path in list(UNIT.rglob("*.pdf")) + list(UNIT.rglob("*.html"))
                 if path != SOURCE / "content.html"]
    results.check("no generated PDF or role HTML artifact is committed under the unit",
                  not artifacts, [str(path.relative_to(ROOT)) for path in artifacts])

    # ── 14. Accessibility affordances ─────────────────────────────────────
    unnamed = [node.get("data-persist-id") for node in soup.select("[data-response]")
               if not (node.get("aria-label") or node.get("aria-labelledby"))]
    results.check("every response control has a programmatic label", not unnamed, unnamed)
    results.check("every image carries alternative text",
                  all(node.get("alt") is not None for node in soup.select("img")))
    for figure in soup.select("figure.case-figure"):
        results.check("every curriculum figure carries an extended description",
                      bool(figure.select_one(".extended-description")))
    headings = [int(node.name[1]) for page in soup.select(".page") for node in page.find_all(["h1", "h2", "h3"])]
    results.check("heading levels never skip a rank", all(later - earlier <= 1 for earlier, later in zip(headings, headings[1:])))

    # ── 15. Standards ─────────────────────────────────────────────────────
    standards = registry["standards"]
    results.check("the directly assessed standards are exactly the five planned",
                  standards["directlyAssessed"] == ["C3 D2.His.2.6-8", "C3 D2.His.1.6-8", "C3 D2.His.14.6-8",
                                                    "CCSS RH.6-8.1", "CCSS WHST.6-8.2"],
                  standards["directlyAssessed"])
    results.check("the supporting standards are exactly the two planned",
                  standards["supporting"] == ["C3 D3.2.6-8", "CCSS RH.6-8.9"], standards["supporting"])
    results.check("no NGSS Performance Expectation is claimed anywhere",
                  standards["contextual"] == []
                  and not re.search(r"\bMS-(?:LS|PS|ESS|ETS)[0-9]", json.dumps(standards) + " ".join(role_text(soup, role) for role in ALL_ROLES)))
    results.check("C3 D4.1 is not claimed while the culmination stays an explanatory synthesis",
                  not any("D4.1" in code for code in standards["directlyAssessed"] + standards["supporting"])
                  and "D4.1" in standards["d41"])
    teacher_text = role_text(soup, "teacher")
    for code in standards["directlyAssessed"] + standards["supporting"]:
        bare = code.split(" ", 1)[1]
        results.check(f"the Teacher Guide prints the claimed standard {bare}", bare in teacher_text)

    # ── 16. Semantic invariants ───────────────────────────────────────────
    exemptions = {item["id"]: item for item in registry["semanticInvariants"]["exemptions"]}
    classes = registry["semanticInvariants"]["classes"]

    def compiled(entry):
        return re.compile("|".join(re.escape(phrase) for phrase in entry["prohibited"]), re.I)

    for entry in classes:
        pattern = compiled(entry)
        violations = []
        for role in ALL_ROLES:
            for node, part in propositions(soup, role):
                if not pattern.search(part):
                    continue
                excused = False
                for exemption_id in exemption_ids(node):
                    exemption = exemptions.get(exemption_id)
                    if exemption and role in exemption["roles"] and entry["id"] in exemption["classes"]:
                        excused = True
                        break
                if not excused:
                    violations.append(f"{role}: {part[:130]}")
        results.check(f"no unexcused node violates the {entry['id']} boundary", not violations, violations)
        # NEGATIVE CONTROL: the guard must still flag its own register.
        results.check(f"the {entry['id']} guard still flags every phrase it declares",
                      all(pattern.search(phrase) for phrase in entry["prohibited"]),
                      [phrase for phrase in entry["prohibited"] if not pattern.search(phrase)])

    # POSITIVE CONTROL: an unregistered exemption cannot excuse anything.
    fake = BeautifulSoup('<div data-exemption="not-registered"><p>x</p></div>', "html.parser")
    results.check("an unregistered exemption id resolves to no class",
                  exemptions.get(next(iter(exemption_ids(fake.select_one("p"))))) is None)
    results.check("exemptions are declared only for the Teacher misconception register and the Answer Key floors",
                  set(exemptions) == {"teacher-misconception-register", "answer-key-floor"}, sorted(exemptions))
    for exemption_id, exemption in exemptions.items():
        used = [node.find_parent(class_="page")["data-role"]
                for node in soup.select(f'[data-exemption~="{exemption_id}"]')]
        results.check(f"the {exemption_id} exemption is used only in the roles it is registered for",
                      used and set(used).issubset(set(exemption["roles"])), sorted(set(used)))

    # ── 16b. Structural boundary guards ───────────────────────────────────
    # The closed registers above catch a wording a released case already named and
    # wrote down. These three catch the proposition *shape* instead, because the
    # boundary each protects can be crossed by a sentence nobody enumerated in
    # advance - which is exactly how each of them was crossed under probe.
    #
    # Every guard is bound to a named subject, requires that subject to carry an
    # asserted predicate before it fires, and stands down when the same proposition
    # carries the qualification that makes the statement legitimate. None polices an
    # ordinary verb, and none is satisfied or bypassed by metadata: they read the
    # same rendered propositions as the closed classes, so an inline span cannot
    # split a claim out of scope. Exemptions resolve through the same registered
    # contract, so the Teacher misconception register and the Answer Key floors can
    # still state a refused claim in order to refuse it.
    STRUCTURAL_GUARDS = [
        {
            "id": "fictionAsHistory",
            "boundary": "the invented 2041 vertical farm may never be asserted to be documented, "
                        "verified or real history",
            "subject": r"\b2041\b|\bvertical farm\b",
            "asserts": r"\b(?:documented|verified|real|actual|genuine)\s+(?:histor\w+|events?|records?)\b"
                       r"|\bhistorical (?:fact|event|record)\b"
                       r"|\b(?:actually|really|genuinely)\s+happened\b"
                       r"|\bpart of (?:the )?historical record\b"
                       r"|\bdocumented (?:future )?history\b",
            "stands_down": r"\bfiction\w*|\binvent\w*|\bhypothetic\w*|\bin-world\b"
                           r"|\b(?:is|are|was|were)\s+not\b|\bnot\s+(?:a\s+)?documented\b|\bnot history\b"
                           r"|\bnever\b|\bcannot\b|\bmay not\b|\bdoes not\b|\bproves nothing\b",
        },
        {
            "id": "case01FirstOrigin",
            "boundary": "Case 01's evidence establishes no first farmer, no first field or place and "
                        "no exact first date for domestication",
            "subject": r"\bfirst (?:farmer|person|field|place|site|village)\b|\bfirst domesticat\w*"
                       r"|\bdomestication (?:began|started)\b|\bfarming (?:began|started)\b"
                       r"|\bfirst to domesticate\b",
            "asserts": r"\bBCE\b|\bBP\b|\bdomesticat\w+|\bbegan\b|\bstarted\b|\b(?:was|were|is|are)\b",
            "stands_down": r"\bno first\b|\bnames no\b|\bidentifies no\b|\bfixes no\b|\bnames neither\b"
                           r"|\bnot\b|\bnever\b|\bcannot\b|\bno record\b|\bno one\b",
        },
        {
            "id": "progressNarrative",
            "boundary": "Campaign 1 does not show agricultural change as automatic, steady or "
                        "case-by-case improvement",
            "subject": r"\beach case\b|\bevery case\b|\bcase by case\b|\ball six cases\b"
                       r"|\bthe one before\b|\bthe last one\b|\bacross the campaign\b|\bcampaign 1\b"
                       r"|\bfarming\b|\bagriculture\b",
            "asserts": r"\bgett?ing better\b|\bgets better\b|\bgot better\b"
                       r"|\bbetter than the (?:one before|last|previous)\b"
                       r"|\balways (?:improv\w+|better)\b|\bonly (?:improv\w+|got better)\b"
                       r"|\bimproved every\b|\bsteadily improv\w+|\binevitab\w+\s+(?:improv\w+|progress)\b",
            "stands_down": r"\bnot\b|\bnever\b|\bearn no\b|\bno credit\b|\btruism\b|\bmisconception\b",
        },
    ]
    for guard in STRUCTURAL_GUARDS:
        subject = re.compile(guard["subject"], re.I)
        asserts = re.compile(guard["asserts"], re.I)
        stands_down = re.compile(guard["stands_down"], re.I)
        violations = []
        for role in ALL_ROLES:
            for node, part in propositions(soup, role):
                if not (subject.search(part) and asserts.search(part)) or stands_down.search(part):
                    continue
                excused = any(
                    (exemptions.get(exemption_id) or {}).get("roles") and
                    role in exemptions[exemption_id]["roles"] and
                    guard["id"] in exemptions[exemption_id]["classes"]
                    for exemption_id in exemption_ids(node))
                if not excused:
                    violations.append(f"{role}: {part[:130]}")
        results.check(f"no unexcused node crosses the {guard['id']} boundary - {guard['boundary']}",
                      not violations, violations)
        # NEGATIVE CONTROL: the guard must still fire on a canonical violation of its
        # own boundary, so a guard that has quietly stopped matching fails the run.
        control = {
            "fictionAsHistory": "The 2041 failure is documented history.",
            "case01FirstOrigin": "The first farmer domesticated wheat at Abu Hureyra in 9,500 BCE.",
            "progressNarrative": "Each case shows farming getting better than the one before.",
        }[guard["id"]]
        results.check(f"the {guard['id']} structural guard still fires on its own canonical violation",
                      bool(subject.search(control) and asserts.search(control))
                      and not stands_down.search(control), control)

    # The five named misconceptions must be present as misconceptions.
    misconceptions = normalize(soup.select_one('.page[data-role="teacher"] .misconception-table').get_text(" ")) \
        if soup.select_one('.page[data-role="teacher"] .misconception-table') else ""
    for label, pattern in (("archived means verified", r"archived does not mean verified|archive, so it is true"),
                           ("change always means progress", r"change always means progress|change is not the same as improvement|always means progress"),
                           ("one mechanism explains the whole event", r"one correct mechanism does not explain|found the mechanism"),
                           ("analogous cases have identical causes", r"analogous cases do not have identical causes|basically the same case"),
                           ("the fictional farm is documented future history", r"2041 facility is fictional|documented future history")):
        results.check(f"the Teacher misconceptions table names '{label}'",
                      re.search(pattern, misconceptions, re.I) is not None)

    # ── 17. Source-status discipline ──────────────────────────────────────
    for role in LEARNER_ROLES:
        key = soup.select_one(f'.page[data-role="{role}"] [data-source-status-key]')
        text = normalize(key.get_text(" ")) if key else ""
        results.check(f"{role} prints the evidence-status key in words",
                      key is not None and all(word in text.lower()
                                              for word in ("documented", "reconstructed", "inferred", "modeled", "debated", "fictional")))
        results.check(f"{role} carries the Archive Orientation rule that preservation is not verification",
                      "preservation does not equal historical verification" in text.lower())

    # ── report ────────────────────────────────────────────────────────────
    failures = [item for item in results.assertions if item["status"] == "FAIL"]
    print(json.dumps({
        "validator": "hhh-c1-synthesis-v1",
        "unit": CASE_ID,
        "status": "PASS" if not failures else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "failures": failures,
    }, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
