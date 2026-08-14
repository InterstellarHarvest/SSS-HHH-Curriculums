#!/usr/bin/env python3
"""Case-scoped protections for HHH Campaign 1 Core Case 04 — Karlsruhe.

These assertions guard the two things this case exists to get right, plus the
ordinary cross-edition parity that the shared operational walk does not reach
into. They are driven by the boundary blocks the task registry declares —
``temperatureQualification``, ``catalystBoundary``, ``attributionBoundary``,
``recycleBoundary`` and ``demonstrationDateBoundary`` — rather than by literal
paragraph locks, so ordinary rewording stays possible while the meaning stays
protected.

The two audit dependencies this case carries:

* ``HHH-GAME-C1L4-001`` — the runtime level's pressure field-note summary
  contains a transcription error in the word for modelling. The curriculum must
  never reproduce it.
* ``HHH-GAME-C1L4-002`` — the runtime level's temperature wording reads as
  ordinary warmth, and its attribution collapses four people's work into one
  name. The curriculum must qualify both, in every role.

Usage:
    python3 apps/curriculum-editor/tests/validate_hhh_case04_karlsruhe.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "hhh/campaign-1/case-04-karlsruhe"
LEARNER_ROLES = ("student", "accessible")
ALL_ROLES = ("student", "teacher", "answer", "accessible")

# The malformed token from the runtime level, and near neighbours, so a
# copy-paste from the game cannot reintroduce it under a different casing.
GAME_TYPO_PATTERN = re.compile(r"\bmdeled\b|\bmdelled\b|\bmodeld\b", re.I)


# ---------------------------------------------------------------------------
# Semantic engine.
#
# The first version of this validator matched prohibited *phrases*. Independent
# review showed that conceptually identical wording slipped through: a sentence
# can put the catalyst in charge of the final balance without ever using the
# word "equilibrium", and can reduce the scale-up to copying without ever saying
# "Haber alone". Phrase lists cannot be completed, so this version stops trying.
#
# Instead the registry declares, per concept, the SUBJECT terms, the OUTCOME
# terms that subject may not be given, the terms that make such a statement
# permissible, and the negations that defuse it. The check is co-occurrence
# inside a single sentence. That catches paraphrase while leaving truthful
# alternative wording free, and it stays a bounded lexical contract rather than
# becoming a parser.
#
# Evaluative context is declared in the markup, not guessed from wording: a
# competing claim under test, a Teacher misconception row and an Answer Key
# floor all legitimately contain the error they exist to refuse, and each is
# marked with a data attribute the registry names. Everything else is scanned in
# every role, including the learner editions.
# ---------------------------------------------------------------------------

SENTENCE_SPLIT = re.compile(r"(?<=[.;:!?])\s+|(?<=\u2014)\s+")


def sentences(text: str) -> list[str]:
    return [part.strip() for part in SENTENCE_SPLIT.split(text) if part.strip()]


def scannable_blocks(raw_html: str, exempt_selectors: list[str]) -> list[tuple[str, str]]:
    """(role, text) for every page block, with declared evaluative contexts removed.

    Exempt subtrees are deleted from a working copy before collection, so a marked
    clause is excluded whether it is the block itself or sits inside a larger one.
    """
    work = BeautifulSoup(raw_html, "html.parser")
    for selector in exempt_selectors:
        for node in work.select(selector):
            node.decompose()
    blocks: list[tuple[str, str]] = []
    for page in work.select(".page[data-role]"):
        role = page.get("data-role")
        for node in page.find_all(["p", "li", "td", "th", "span", "div"], recursive=True):
            if node.find(["p", "li", "td", "th"]):
                continue  # only leaf-ish blocks, so text is not counted twice
            text = node.get_text(" ", strip=True)
            if text:
                blocks.append((role, text))
    return blocks


def has_any(text: str, terms: list[str]) -> bool:
    return any(term.lower() in text for term in terms)


def catalyst_violations(blocks, spec) -> list[str]:
    out = []
    for role, text in blocks:
        for sentence in sentences(text):
            low = sentence.lower()
            if not has_any(low, spec["subjectTerms"]):
                continue
            if not has_any(low, spec["prohibitedOutcomeTerms"]):
                continue
            # Mentioning the balance is not a claim about it. The sentence only
            # offends when it also asserts a change in, or a larger amount at,
            # that outcome -- which is what "the catalyst changes the final
            # balance" and "settles with extra ammonia" both do, and what
            # "reaches its balance quickly" does not.
            if not has_any(low, spec["changeOrAmountTerms"]):
                continue
            if has_any(low, spec["negationTerms"]):
                continue
            out.append(f"{role}: catalyst given an equilibrium-position or final-amount outcome -> {sentence[:150]}")
    return out


def temperature_violations(blocks, spec) -> list[str]:
    out = []
    for role, text in blocks:
        for sentence in sentences(text):
            low = sentence.lower()
            if not has_any(low, spec["subjectTerms"]):
                continue
            if not has_any(low, spec["warmthTerms"]):
                continue
            if has_any(low, spec["hotAnchorTerms"]):
                continue
            if has_any(low, spec.get("negationTerms", [])):
                continue
            out.append(f"{role}: operating temperature carries warmth language with no hot anchor -> {sentence[:150]}")
    return out


def attribution_violations(blocks, spec) -> list[str]:
    out = []
    industrial_nouns = ["industrial", "factory", "factories", "plant", "works", "scale", "scale-up", "commercial"]
    for role, text in blocks:
        for sentence in sentences(text):
            low = sentence.lower()
            lab = has_any(low, [a.lower() for a in spec["laboratoryActors"]])
            ind = has_any(low, [a.lower() for a in spec["industrialActors"]])
            if lab and has_any(low, spec["completionTerms"]) and has_any(low, industrial_nouns):
                out.append(f"{role}: laboratory work described as already-complete industrial work -> {sentence[:150]}")
                continue
            if ind and has_any(low, spec["diminutiveTerms"]) and has_any(low, spec["reproductionTerms"]):
                out.append(f"{role}: industrial scale-up reduced to copying -> {sentence[:150]}")
    return out


def recycle_violations(blocks, spec) -> list[str]:
    """Two failures: an unqualified block, and a universality claim anywhere.

    The block check alone is not enough. A paragraph can keep its qualifying
    sentence and still gain a second sentence asserting the figure is what the
    process always does, so universality is checked per sentence and is not
    excused by a qualification sitting elsewhere in the same block.
    """
    out = []
    share_words = ["parts in", "per cent", "percent", "%", "convert"]
    for role, text in blocks:
        low = text.lower()
        carries_figure = any(f in text for f in spec["figures"])
        if not carries_figure or not has_any(low, share_words):
            continue
        for sentence in sentences(text):
            slow = sentence.lower()
            if not any(f in sentence for f in spec["figures"]):
                continue
            if has_any(slow, spec.get("universalityTerms", [])):
                out.append(f"{role}: conversion figure asserted as universal -> {sentence[:150]}")
        if role not in LEARNER_ROLES:
            continue
        if has_any(low, spec["qualificationTerms"]):
            continue
        out.append(f"{role}: conversion figure printed without a reported/example qualification -> {text[:150]}")
    return out


class Results:
    def __init__(self) -> None:
        self.checks: list[dict] = []

    def check(self, name: str, passed: bool, detail: object = "") -> None:
        self.checks.append({"name": name, "pass": bool(passed), "detail": str(detail)[:600]})

    @property
    def failed(self) -> list[dict]:
        return [c for c in self.checks if not c["pass"]]


def task_registry(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    start = text.index("{")
    end = text.rindex("}") + 1
    return json.loads(text[start:end])


def role_text(soup: BeautifulSoup, role: str) -> str:
    return " ".join(node.get_text(" ", strip=True) for node in soup.select(f'.page[data-role="{role}"]'))


def role_task_numbers(soup: BeautifulSoup, role: str) -> list[str]:
    numbers: list[str] = []
    for page in soup.select(f'.page[data-role="{role}"]'):
        for heading in page.select("[data-shell-task-heading]"):
            numbers.append(str(heading["data-shell-task-heading"]))
    return numbers


def main() -> int:
    results = Results()
    package = json.loads((UNIT / "source/case-package.json").read_text(encoding="utf-8"))
    registry = task_registry(UNIT / "source/task-registry.js")
    content_path = UNIT / "source/content.html"
    raw = content_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw, "html.parser")
    readme = (UNIT / "README.md").read_text(encoding="utf-8")
    texts = {role: role_text(soup, role) for role in ALL_ROLES}
    lowered = {role: text.lower() for role, text in texts.items()}
    everything = " ".join(texts.values())

    # ---- HHH-GAME-C1L4-001 -------------------------------------------------
    results.check(
        "the runtime level's malformed modelling token is not reproduced in any role",
        not GAME_TYPO_PATTERN.search(raw),
        [m.group(0) for m in GAME_TYPO_PATTERN.finditer(raw)])
    results.check(
        "the Teacher Guide tells the teacher the game's field note carries a typing error",
        "typing error" in lowered["teacher"] and "transcription error" in lowered["teacher"],
        "")

    # ---- HHH-GAME-C1L4-002, temperature ------------------------------------
    inv = registry["semanticInvariants"]
    blocks = scannable_blocks(raw, [c["selector"] for c in inv["scanScope"]["exemptContexts"]])
    results.check("declared evaluative contexts exist, so the scan has something to exempt",
                  all(soup.select(c["selector"]) for c in inv["scanScope"]["exemptContexts"]),
                  [c["selector"] for c in inv["scanScope"]["exemptContexts"] if not soup.select(c["selector"])])
    temp_findings = temperature_violations(blocks, inv["temperature"])
    results.check("no role characterises the operating temperature as ordinary warmth", not temp_findings, temp_findings)
    temperature = registry["temperatureQualification"]
    for role in ALL_ROLES:
        results.check(
            f"the {role} edition frames the operating temperature as a compromise",
            "compromise" in lowered[role], "")
    anchors = ("400", "500", "327", "600")
    for role in LEARNER_ROLES:
        present = [a for a in anchors if a in texts[role]]
        results.check(
            f"the {role} edition carries an anchored temperature value, not only the word compromise",
            len(present) >= 3, present)
    for role in LEARNER_ROLES:
        results.check(
            f"the {role} edition places the operating range against a fixed point a reader knows",
            "lead" in lowered[role] and "327" in texts[role], "")
        # Both directions are required evidence, not just the compromise word.
        equilibrium_direction = ("toward ammonia" in lowered[role] or "towards ammonia" in lowered[role])
        rate_direction = ("slow" in lowered[role] or "creep" in lowered[role] or "speed" in lowered[role])
        results.check(
            f"the {role} edition states both the equilibrium direction and the rate direction",
            equilibrium_direction and rate_direction,
            {"equilibriumDirection": equilibrium_direction, "rateDirection": rate_direction})
    results.check(
        "both learner editions carry the temperature ladder",
        all(soup.select(f'.page[data-role="{role}"] [data-temperature-ruler]') for role in LEARNER_ROLES), "")

    # ---- catalyst boundary --------------------------------------------------
    catalyst = registry["catalystBoundary"]
    cat_findings = catalyst_violations(blocks, inv["catalyst"])
    results.check("no role gives the catalyst an equilibrium-position or final-amount outcome",
                  not cat_findings, cat_findings)
    results.check("the registry states the catalyst has no effect on equilibrium position",
                  inv["catalyst"]["equilibriumPositionEffect"] == "NONE"
                  and inv["catalyst"]["cannotBePresentedAsChangingFinalEquilibriumBalance"] is True, "")
    for role in LEARNER_ROLES:
        text = lowered[role]
        states_boundary = ("no effect on where the balance sits" in text
                           or "does not change where the balance sits" in text
                           or "without changing where the balance sits" in text)
        results.check(
            f"the {role} edition states in print that a catalyst does not move the balance",
            states_boundary, "")
    results.check(
        "the Answer Key refuses the catalyst/equilibrium confusion explicitly",
        "not accepted at any level" in lowered["answer"] and "shifts the equilibrium" in lowered["answer"], "")

    # ---- attribution boundary ----------------------------------------------
    attribution = registry["attributionBoundary"]
    attr_findings = attribution_violations(blocks, inv["attribution"])
    results.check("no role collapses laboratory work and industrial scale-up into one",
                  not attr_findings, attr_findings)
    results.check("the registry keeps laboratory work and industrial scale-up distinct",
                  inv["attribution"]["laboratoryWorkIsNotIndustrialScaleUp"] is True
                  and inv["attribution"]["industrialProcessMayNotBeDescribedAsCompleteBeforeScaleUp"] is True, "")
    for role in ALL_ROLES:
        missing = [name for name in ("Haber", "Bosch", "Mittasch", "Le Rossignol") if name not in texts[role]]
        results.check(f"the {role} edition names all four contributors", not missing, missing)
    # R1: contributions may not exceed the strength the cited source supports.
    overcredit = []
    for role, text in blocks:
        low = text.lower()
        if "le rossignol" in low and re.search(r"le rossignol[^.;]{0,80}\b(built|made|constructed|invented)\b[^.;]{0,40}compressor", low):
            overcredit.append(f"{role}: Le Rossignol credited with building the compressor -> {text[:140]}")
        if "le rossignol" in low and re.search(r"le rossignol[^.;]{0,60}\bbuilt the (complete|whole) apparatus", low):
            overcredit.append(f"{role}: Le Rossignol credited with building the complete apparatus -> {text[:140]}")
    results.check("no role credits Le Rossignol beyond the strength the source supports", not overcredit, overcredit)
    results.check("the compressor's provenance is stated in both learner editions",
                  all(("bought by haber" in lowered[r] or "acquired by haber" in lowered[r]
                       or "haber had bought" in lowered[r]) for r in LEARNER_ROLES),
                  {r: ("bought by haber" in lowered[r]) for r in LEARNER_ROLES})
    results.check("the registry records source-strength rules for attribution",
                  len(attribution.get("sourceStrengthRules", [])) >= 4, "")
    results.check(
        "the Answer Key refuses a single-actor account explicitly",
        "not accepted at any level" in lowered["answer"]
        and ("crediting the industrial process to haber alone" in lowered["answer"]
             or "credited to one step or one kind of work" in lowered["answer"]), "")
    results.check(
        "the technology sequence prints three lanes in both learner editions",
        all(len(soup.select(f'.page[data-role="{role}"] [data-sequence-contract]')) == 1 for role in LEARNER_ROLES),
        "")
    results.check(
        "the sequence figure states in print why its lanes are drawn at equal weight",
        everything.count("no one of them was optional") >= 2, "")
    # P4: the embrittlement diagnosis belongs to Bosch; Lappe aided the solution.
    results.check("the embrittlement diagnosis is not awarded jointly against the source",
                  not re.search(r"bosch and (franz )?lappe (found|discovered|established|worked out)", everything, re.I),
                  "")
    results.check("Lappe's contribution is recorded as aiding the solution",
                  "aided by" in " ".join(lowered.values()), "")

    # ---- recycle boundary ---------------------------------------------------
    recycle = registry["recycleBoundary"]
    rec_findings = recycle_violations(blocks, inv["recycle"])
    results.check("every printed conversion figure carries its reported/example qualification",
                  not rec_findings, rec_findings)
    results.check("the registry marks both conversion figures as reported examples",
                  recycle["printedQualificationRequired"] is True
                  and recycle["singlePass"]["status"] == "reported example"
                  and recycle["overallWithRecycle"]["status"] == "reported example", "")
    for role in LEARNER_ROLES:
        results.check(
            f"the {role} edition prints the single-pass share and the recycled whole-plant share",
            "15" in texts[role] and "98" in texts[role], "")
        results.check(
            f"the {role} edition says the conversion figures vary from plant to plant",
            "varies from plant to plant" in lowered[role], "")

    # ---- demonstration date -------------------------------------------------
    date_boundary = registry["demonstrationDateBoundary"]
    for role in LEARNER_ROLES:
        results.check(
            f"the {role} edition prints both published dates for the 1909 demonstration",
            "1 July 1909" in texts[role] and "April 1909" in texts[role], "")
        results.check(
            f"the {role} edition marks the demonstration date as unsettled",
            "one version of events" in lowered[role], "")
    results.check(
        "the certified year is stated and no exact date is presented as settled",
        date_boundary["certifiedYear"] == "1909"
        and "published accounts differ" in " ".join(lowered.values()), "")

    # ---- source status parity ----------------------------------------------
    declared_statuses = {s["id"]: s["evidentiaryStatus"] for s in registry["caseSources"]}
    status_findings: list[str] = []
    for node in soup.select("[data-source-id]"):
        source_id = node["data-source-id"]
        if source_id not in declared_statuses:
            status_findings.append(f"unknown source id in content: {source_id}")
            continue
        status_line = node.select_one(".source-status")
        if status_line is None:
            continue
        printed = status_line.get_text(" ", strip=True).lower()
        expected = declared_statuses[source_id].lower()
        if expected not in printed:
            status_findings.append(f"{source_id}: printed {printed!r} does not carry declared {expected!r}")
    results.check("every printed learner STATUS line carries the status its canonical source declares",
                  not status_findings, status_findings)
    reconstruction_ids = [s["id"] for s in registry["caseSources"] if s["evidentiaryStatus"] == "reconstructed"]
    leak_findings: list[str] = []
    for node in soup.select("[data-source-id]"):
        if node["data-source-id"] not in reconstruction_ids:
            continue
        printed = node.get_text(" ", strip=True).lower()
        for forbidden in ("primary source", "eyewitness", "testimony from", "surviving testimony from"):
            if forbidden in printed:
                leak_findings.append(f"{node['data-source-id']}: {forbidden}")
    results.check("no game reconstruction is presented as primary or eyewitness evidence",
                  not leak_findings, leak_findings)
    results.check("the reconstruction and attribution notice is carried by both learner editions",
                  all(soup.select(f'.page[data-role="{role}"] [data-reconstruction-boundary]') for role in LEARNER_ROLES), "")

    # ---- load-bearing no-game facts, in BOTH learner editions ---------------
    fallback_facts = {
        "the reaction equation": lambda t, lt: "2NH" in t,
        "four gas molecules becoming two": lambda t, lt: "four" in lt and "two" in lt,
        "the patent's two named inventors": lambda t, lt: "1,202,995" in t and "Le Rossignol" in t,
        "the patent's recycle statement": lambda t, lt: "passed over the catalyst again" in lt,
        "the patent's stated catalyst temperature range": lambda t, lt: "500 and 1000" in t,
        "the modern operating range": lambda t, lt: "400" in t and "500" in t,
        "the promoted iron catalyst": lambda t, lt: "promoted iron" in lt,
        "the hydrogen embrittlement of the steel": lambda t, lt: "brittle" in lt,
        "the Oppau opening date": lambda t, lt: "9 September 1913" in t,
        "the population estimate": lambda t, lt: "48" in t and "erisman" in lt,
    }
    for role in LEARNER_ROLES:
        missing = [name for name, test in fallback_facts.items() if not test(texts[role], lowered[role])]
        results.check(f"every load-bearing no-game fact is present in the {role} edition", not missing, missing)

    # ---- R2: the Teacher source ledger must cover the canonical estate -----
    ledger_rows = soup.select('[data-source-ledger] tbody tr[data-ledger-source]')
    covered: list[str] = []
    for row in ledger_rows:
        covered.extend(row["data-ledger-source"].split())
    declared_ids = [src["id"] for src in registry["caseSources"]]
    missing_from_ledger = [i for i in declared_ids if i not in covered]
    unregistered_in_ledger = [i for i in covered if i not in declared_ids]
    results.check("the Teacher source ledger covers every canonical caseSource",
                  not missing_from_ledger, missing_from_ledger)
    results.check("the Teacher source ledger introduces no source the estate does not declare",
                  not unregistered_in_ledger, unregistered_in_ledger)
    results.check("no ledger row covers a source twice",
                  len(covered) == len(set(covered)), covered)
    grouped_rows = soup.select('[data-source-ledger] tr[data-ledger-grouping]')
    for row in grouped_rows:
        ids = row["data-ledger-source"].split()
        results.check(f"grouped ledger row {row['data-ledger-grouping']} declares the sources it groups",
                      len(ids) > 1 and "Grouped" in row.get_text(" ", strip=True), ids)
    results.check("the ledger's coverage claim is true of the estate it actually lists",
                  "traces to one of these" in lowered["teacher"]
                  and str(len(declared_ids)) in texts["teacher"], len(declared_ids))
    # Any supporting reference must be printed inside the row of the source it supports.
    for src in registry["caseSources"]:
        for ref in src.get("supportingReferences", []):
            owner_rows = [r for r in ledger_rows if src["id"] in r["data-ledger-source"].split()]
            label_head = ref["label"].split(",")[0]
            results.check(f"supporting reference '{label_head}' sits inside the {src['id']} ledger row",
                          any(label_head.split()[0] in r.get_text(" ", strip=True) for r in owner_rows), "")

    # ---- R3: Accessible adaptation must be documented where it is scored ---
    prefilled = soup.select('.page[data-role="accessible"] td.prefilled')
    adaptation_notes = soup.select('[data-accessible-adaptation]')
    if prefilled:
        results.check("a prefilled Accessible response is declared as an adaptation in the markup",
                      len(adaptation_notes) >= 2, len(adaptation_notes))
        results.check("the Accessible page itself labels the prefilled row as a worked model",
                      any(n.find_parent(class_="page") is not None
                          and n.find_parent(class_="page").get("data-role") == "accessible"
                          for n in adaptation_notes), "")
        results.check("the Teacher Guide states the prefilled row rather than claiming nothing is disclosed",
                      any(n.find_parent(class_="page") is not None
                          and n.find_parent(class_="page").get("data-role") == "teacher"
                          for n in adaptation_notes), "")
        results.check("no role claims that no keyed answer is disclosed in the Accessible edition",
                      not re.search(r"does\s+<strong>not</strong>\s+give away any keyed", raw, re.I)
                      and "never gives away any keyed" not in " ".join(lowered.values()), "")
        results.check("the Answer Key records the Student/Accessible completion difference",
                      "edition difference" in lowered["answer"]
                      and "twelve" in lowered["answer"] and "fifteen" in lowered["answer"], "")
        results.check("the scored count is stated for both editions in the Teacher Guide",
                      "twelve" in lowered["teacher"] and "four" in lowered["teacher"], "")

    # ---- R4: Accessible response space may not fall below Student capacity -
    css = (UNIT / "source/presentation.css").read_text(encoding="utf-8")

    def min_height_in(selector_fragment: str) -> float:
        m = re.search(re.escape(selector_fragment) + r"\s*\{[^}]*min-height:\s*([0-9.]+)in", css)
        return float(m.group(1)) if m else 0.0

    pairs = [
        (".response.medium.fill-sequence", ".accessible .response.roomy.fill-sequence", "Task 5 Part B"),
    ]
    ACCESSIBLE_TYPE_RATIO = 1.21  # 11.35pt Accessible body against 9.35pt Student
    for student_sel, accessible_sel, label in pairs:
        student_h = min_height_in(student_sel)
        accessible_h = min_height_in(accessible_sel)
        floor = round(student_h * ACCESSIBLE_TYPE_RATIO, 3)
        results.check(
            f"Accessible {label} response space is at least Student-equivalent for its type size",
            student_h > 0 and accessible_h >= floor,
            {"student": student_h, "accessible": accessible_h, "requiredFloor": floor})

    # ---- cross-edition task parity -----------------------------------------
    keyed = [task for task in registry["tasks"] if task.get("keyed")]
    expected_numbers = [task["number"] for task in keyed]
    student_numbers = role_task_numbers(soup, "student")
    accessible_numbers = role_task_numbers(soup, "accessible")
    answer_numbers = role_task_numbers(soup, "answer")
    results.check("the Student edition carries every registered task, in order",
                  student_numbers == expected_numbers, student_numbers)
    results.check("the Accessible edition carries the same task numbers in the same order",
                  accessible_numbers == expected_numbers, accessible_numbers)
    results.check("the Answer Key carries a keyed section for every keyed task, in order",
                  answer_numbers == expected_numbers, answer_numbers)

    # ---- Teacher exact task-reference parity --------------------------------
    titles = {task["number"]: task["title"] for task in registry["tasks"]}
    reference_findings: list[str] = []
    for node in soup.select('.page[data-role="teacher"] .task-reference'):
        label = node.get_text(" ", strip=True)
        match = re.match(r"^(\d+)\s*·\s*(.+)$", label)
        if not match:
            reference_findings.append(f"malformed reference: {label}")
            continue
        number, title = match.group(1), match.group(2).strip()
        if titles.get(number) != title:
            reference_findings.append(f"{label!r} does not match registry title {titles.get(number)!r}")
    results.check("every bold Teacher task reference uses the registered number and exact title",
                  not reference_findings, reference_findings)
    results.check("the Teacher Guide references at least one task by exact reference",
                  len(soup.select('.page[data-role="teacher"] .task-reference')) >= 6, "")

    # ---- role page-count agreement across every file that states it ---------
    dom_counts = {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ALL_ROLES}
    package_counts = {role: package["rolePageStructure"][role]["pageCount"] for role in ALL_ROLES}
    results.check("DOM, package and task registry agree on every role page count",
                  dom_counts == package_counts == registry["roles"],
                  json.dumps({"dom": dom_counts, "package": package_counts, "registry": registry["roles"]}))
    declared = f"Roles and page counts: Student {package_counts['student']} · Teacher {package_counts['teacher']} · Answer Key {package_counts['answer']} · Accessible {package_counts['accessible']}."
    results.check("the README declares the same role page counts", declared in readme, declared)
    footer_findings = []
    for role, label in (("student", "Student Mission"), ("teacher", "Teacher Guide"),
                        ("answer", "Answer Key"), ("accessible", "Accessible Mission")):
        total = package_counts[role]
        for index, page in enumerate(soup.select(f'.page[data-role="{role}"]'), start=1):
            footer = page.select_one("[data-publication-footer]")
            wanted = f"{label} {index} of {total}"
            if footer is None or footer.get_text(" ", strip=True) != wanted:
                footer_findings.append(f"{role} page {index}: {footer.get_text(' ', strip=True) if footer else None!r}")
    results.check("every page footer numbers itself against the declared role total",
                  not footer_findings, footer_findings)

    # ---- source-reference accuracy -----------------------------------------
    results.check("the Erisman DOI and journal are stated exactly once in the Teacher sources",
                  texts["teacher"].count("10.1038/ngeo325") == 1 and "Nature Geoscience" in texts["teacher"], "")
    results.check("the patent number is stated identically wherever it is printed",
                  everything.count("1,202,995") >= 3 and "1202995" not in everything.replace(" ", ""), "")
    results.check("no source reference invents a date the registry does not carry",
                  "13 August 1909" in everything and "31 October 1916" in everything, "")

    # ---- lifecycle: this is a candidate, not a release ----------------------
    results.check("the package is a validation candidate with no owner approval",
                  package["status"] == "VALIDATION_BUILD"
                  and package["approval"]["status"] == "OWNER_REVIEW_NOT_STARTED"
                  and package["approval"]["printStatus"] == "NOT_RUN"
                  and "releaseHistory" not in package,
                  json.dumps({"status": package["status"], "approval": package["approval"]}))
    results.check("no release or approval record exists on disk",
                  not (UNIT / "history").exists(), "")
    results.check("no printable role claims an approved or released state",
                  "approved_stable" not in " ".join(lowered.values()), "")

    print(json.dumps({
        "validator": "hhh-c1-case04-karlsruhe-v1",
        "status": "PASS" if not results.failed else "FAIL",
        "assertions": len(results.checks),
        "failures": results.failed,
    }, indent=2))
    return 0 if not results.failed else 1


if __name__ == "__main__":
    sys.exit(main())
