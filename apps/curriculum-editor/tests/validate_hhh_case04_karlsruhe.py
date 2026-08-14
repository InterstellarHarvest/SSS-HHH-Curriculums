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
# Phrase lists cannot be completed. A sentence can put the catalyst in charge of
# the settled amount without ever saying "equilibrium", finish the industrial
# engineering in Haber's laboratory without the bigram "finished industrial",
# and universalise a worked figure without the literal string "every plant". So
# the registry declares CONCEPT FAMILIES and the checks look for a RELATION
# between them inside one sentence, in any word order.
#
# Two design rules matter more than the vocabulary:
#
#   * A numeric temperature is EVIDENCE that mild language is wrong, never a
#     waiver for it. "a comfortable 450 C" fails because of the 450, not
#     despite it.
#
#   * Exemption is a closed contract. A node may be excused only by naming a
#     registered exemption id that resolves, for that role, through the
#     selector the registry declares, in the number the registry declares.
#     Adding an attribute cannot make a bad learner sentence disappear.
#
# Deterministic, no external dependencies, no probabilistic behaviour.
# ---------------------------------------------------------------------------

SENTENCE_SPLIT = re.compile(r"(?<=[.;:!?])\s+|(?<=\u2014)\s+")
WORDISH = re.compile(r"[a-z0-9%°]+")
SUBSCRIPTS = {ord("\u2080") + i: str(i) for i in range(10)}

# Every rendering of the ammonia formula folds onto one concept token. The HTML
# form NH<sub>3</sub> reaches this layer as "NH 3" once the DOM text is
# extracted, which is how a misconception previously hid behind notation.
AMMONIA_FORMULA = re.compile(r"\bnh\s*3\b")

# Deterministic suffix stripping so a family term matches its ordinary
# inflections without the registry listing each one. Applied identically to the
# sentence and to the family terms, so the comparison stays consistent.
IRREGULAR = {"came": "come", "comes": "come", "held": "hold", "holds": "hold",
             "went": "go", "gone": "go", "lay": "lie", "lies": "lie"}
SUFFIXES = ("ing", "ed", "es", "s")


def stem(token: str) -> str:
    if token in IRREGULAR:
        return IRREGULAR[token]
    for suffix in SUFFIXES:
        if token.endswith(suffix) and len(token) - len(suffix) >= 3:
            return token[: -len(suffix)]
    return token


def sentences(text: str) -> list[str]:
    return [part.strip() for part in SENTENCE_SPLIT.split(text) if part.strip()]


def normalise(text: str) -> str:
    """Lowercase, fold chemical notation, and pad for word-boundary matching.

    Deliberately NOT stemmed. The temperature, attribution and recycle contracts
    closed at 20ebcc0 against this exact behaviour, and stemming their families
    would change what they match - collapsing the noun "works" onto "work", for
    one. Only the catalyst contract, the sole concept in scope, uses the stemmed
    variant below.
    """
    low = text.lower().replace("\u2019", "'").replace("\u2014", " ").replace("\u2013", " ")
    low = low.translate(SUBSCRIPTS)
    low = AMMONIA_FORMULA.sub(" ammonia ", low)
    return " " + " ".join(WORDISH.findall(low)) + " "


def normalise_stemmed(text: str) -> str:
    """Catalyst-only: normalise, then stem, so inflections match without listing."""
    return " " + " ".join(stem(t) for t in normalise(text).split()) + " "


def has_any(norm: str, terms: list[str]) -> list[str]:
    """Terms present in a normalised sentence, matched on word boundaries."""
    hits = []
    for term in terms:
        needle = normalise(term).strip()
        if needle and f" {needle} " in norm:
            hits.append(term)
    return hits


def has_any_stemmed(norm: str, terms: list[str]) -> list[str]:
    """As has_any, with both sides stemmed. Catalyst contract only."""
    hits = []
    for term in terms:
        needle = normalise_stemmed(term).strip()
        if needle and f" {needle} " in norm:
            hits.append(term)
    return hits


def negated(norm: str, spec: dict) -> bool:
    """Explicit denial phrases, plus a deterministic negation-of-change pattern."""
    if has_any_stemmed(norm, spec.get("negationTerms", [])):
        return True
    pattern = spec.get("negationPattern")
    return bool(pattern and re.search(pattern, norm))


def final_state_hits(norm: str, spec: dict) -> list[str]:
    """Strong terms stand alone; contextual terms need a mixture/reaction context."""
    strong = has_any_stemmed(norm, spec["finalStateStrongTerms"])
    if strong:
        return strong
    contextual = has_any_stemmed(norm, spec["finalStateContextualTerms"])
    if contextual and has_any_stemmed(norm, spec["mixtureContextTerms"]):
        return contextual
    return []


def accessible_name(node) -> str:
    """The accessible name a screen reader would receive for a figure region."""
    if node.get("aria-label"):
        return node["aria-label"]
    inner = node.select_one("[aria-label]")
    return inner["aria-label"] if inner else ""


def figure_accessibility_findings(soup, contract, chronology) -> list[str]:
    """Check figure accessibility text against canonical chronology metadata.

    Metadata-driven: the sourced conditions, their units and their epistemic
    status come from the registry, so correcting the visible figure without
    correcting the accessible name is caught, and so is the reverse.
    """
    findings: list[str] = []
    for figure in contract["figures"]:
        entry = next((c for c in chronology
                      if c.get("year") == figure["chronologyYear"]
                      and c.get("lane") == figure["chronologyLane"]
                      and c.get("sourcedConditions")), None)
        if entry is None:
            findings.append(f"{figure['id']}: no chronology entry with sourced conditions to check against")
            continue
        names: dict[str, str] = {}
        for node in soup.select(figure["selector"]):
            page = node.find_parent(class_="page")
            role = page.get("data-role") if page else None
            if role not in figure["roles"]:
                continue
            name = accessible_name(node)
            if not name:
                findings.append(f"{figure['id']} ({role}): figure has no accessible name")
                continue
            names[role] = name
            low = name.lower()
            for pattern in figure["prohibitedPatterns"]:
                if re.search(pattern["regex"], low):
                    findings.append(f"{figure['id']} ({role}): {pattern['id']} - {pattern['why']}")
            for cond in entry["sourcedConditions"]:
                value, unit = cond["pressure"]["value"], cond["pressure"]["unit"]
                if not re.search(rf"{value}\s*{unit[:3]}", low):
                    findings.append(
                        f"{figure['id']} ({role}): sourced condition {cond['id']} missing its own "
                        f"pressure {value} {unit}")
                    continue
                window = low[max(0, low.find(str(value)) - 260): low.find(str(value)) + 260]
                if not any(v.lower() in window for v in cond["verbFamily"]):
                    findings.append(
                        f"{figure['id']} ({role}): {cond['id']} is not marked "
                        f"{cond['epistemicStatus']} near its own value")
                for bad in cond["prohibitedVerbFamily"]:
                    if re.search(rf"{bad}\w*\s+(?:about\s+)?eight per cent[^.]*{value}\s*{unit[:3]}", low) or \
                       re.search(rf"{value}\s*{unit[:3]}[^.]*\b{bad}\b", low):
                        findings.append(
                            f"{figure['id']} ({role}): {cond['id']} described with the wrong "
                            f"epistemic verb {bad!r}")
        if figure.get("requiresRolePartity") and len(names) > 1:
            facts = {}
            for role, name in names.items():
                low = name.lower()
                facts[role] = tuple(sorted(
                    (str(c["pressure"]["value"]), c["pressure"]["unit"], c["epistemicStatus"])
                    for c in entry["sourcedConditions"]
                    if re.search(rf"{c['pressure']['value']}\s*{c['pressure']['unit'][:3]}", low)
                    and any(v.lower() in low for v in c["verbFamily"])))
            distinct = set(facts.values())
            if len(distinct) > 1:
                findings.append(f"{figure['id']}: Student and Accessible accessible names disagree: {facts}")
        for pattern in contract["attributionParity"]["prohibitedPatterns"]:
            for role, name in names.items():
                if re.search(pattern["regex"], name.lower()):
                    findings.append(f"{figure['id']} ({role}): {pattern['id']} - {pattern['why']}")
    return findings



def exemption_findings(raw_html: str, spec: dict) -> tuple[list[str], list]:
    """Validate the closed exemption contract; return (findings, exempt nodes).

    Every marker in the DOM must name a registered id; every registered id must
    resolve through its own declared selector, in its declared role, in its
    declared count. Any of those failing is a validation failure, not a silent
    exemption.
    """
    soup = BeautifulSoup(raw_html, "html.parser")
    attr = spec["scanScope"]["exemptionAttribute"]
    registered = {e["id"]: e for e in spec["exemptions"]}
    findings: list[str] = []
    exempt_nodes: list = []

    marked = soup.select(f"[{attr}]")
    for node in marked:
        value = node.get(attr)
        if value not in registered:
            findings.append(f"unregistered exemption id in DOM: {value!r}")
            continue
        page = node.find_parent(class_="page")
        role = page.get("data-role") if page else None
        if role not in registered[value]["roles"]:
            findings.append(f"exemption {value!r} used in role {role!r}, which the registry does not permit")

    for entry in spec["exemptions"]:
        resolved = soup.select(entry["selector"])
        if len(resolved) != entry["expectedCount"]:
            findings.append(
                f"exemption {entry['id']!r} resolves to {len(resolved)} node(s) through its declared "
                f"selector, registry expects {entry['expectedCount']}")
        for node in resolved:
            page = node.find_parent(class_="page")
            role = page.get("data-role") if page else None
            if role not in entry["roles"]:
                findings.append(f"exemption {entry['id']!r} resolved in role {role!r}")
            exempt_nodes.append(node)

    # Every marker must also be reachable through its own registered selector,
    # so moving a valid marker to an unrelated node is caught even if the count
    # elsewhere happens to balance.
    resolved_ids = {id(n) for n in exempt_nodes}
    for node in marked:
        value = node.get(attr)
        if value in registered and id(node) not in resolved_ids:
            findings.append(
                f"exemption {value!r} is attached to a node its registered selector does not match")
    return findings, exempt_nodes


def scannable_blocks(raw_html: str, spec: dict) -> list[tuple[str, str]]:
    """(role, text) for every page block, with registered exemptions removed."""
    work = BeautifulSoup(raw_html, "html.parser")
    attr = spec["scanScope"]["exemptionAttribute"]
    registered = {e["id"]: e for e in spec["exemptions"]}
    for entry in spec["exemptions"]:
        for node in work.select(entry["selector"]):
            node.decompose()
    # An unregistered or misplaced marker removes nothing: it is reported by
    # exemption_findings and its text stays in the scan.
    for structural in spec.get("structuralExemptSelectors", []):
        for node in work.select(structural["selector"]):
            node.decompose()
    blocks: list[tuple[str, str]] = []
    for page in work.select(".page[data-role]"):
        role = page.get("data-role")
        for node in page.find_all(["p", "li", "td", "th", "span", "div"], recursive=True):
            if node.find(["p", "li", "td", "th"]):
                continue
            text = node.get_text(" ", strip=True)
            if text:
                blocks.append((role, text))
    return blocks


def catalyst_violations(blocks, spec) -> list[str]:
    """Two rules: the catalyst may not own the settled amount, and a bare
    function claim must resolve into a permitted rate/pathway role."""
    out = []
    result_markers = spec.get("resultReportMarkers", [])
    for role, text in blocks:
        for sentence in sentences(text):
            norm = normalise_stemmed(sentence)
            if not has_any_stemmed(norm, spec["subjectTerms"]):
                continue
            if negated(norm, spec):
                continue
            increase = has_any_stemmed(norm, spec["increaseRelationTerms"])
            final_state = final_state_hits(norm, spec)
            product = has_any_stemmed(norm, spec["productTerms"])
            if increase and final_state and product:
                out.append(
                    f"{role}: catalyst asserted to change the settled amount "
                    f"[{increase[0]} / {final_state[0]}] -> {sentence[:140]}")
                continue
            if role not in LEARNER_ROLES:
                continue
            if not has_any_stemmed(norm, spec["functionVerbTerms"]):
                continue
            # A sentence reporting a measured result under stated conditions is a
            # historical report, not a functional claim about what a catalyst does.
            # The negative relation rule above still governs it.
            if has_any_stemmed(norm, result_markers) or re.search(r"\b\d", sentence):
                continue
            if not has_any_stemmed(norm, spec["permittedRateTerms"]):
                out.append(
                    f"{role}: catalyst given a function that does not resolve into a "
                    f"rate or pathway role -> {sentence[:140]}")
    return out


def temperature_violations(blocks, spec) -> list[str]:
    """Warmth language about the operating condition fails even with a hot value."""
    value_pattern = re.compile(spec["subjectValuePattern"])
    out = []
    for role, text in blocks:
        for sentence in sentences(text):
            norm = normalise(sentence)
            is_temperature_sentence = bool(has_any(norm, spec["subjectTerms"])) or bool(
                value_pattern.search(norm))
            if not is_temperature_sentence:
                continue
            warmth = has_any(norm, spec["warmthTerms"])
            if not warmth:
                continue
            if has_any(norm, spec["negationTerms"]):
                continue
            out.append(
                f"{role}: operating temperature characterised as {warmth[0]!r} "
                f"(a numeric value does not excuse this) -> {sentence[:140]}")
    return out


def attribution_violations(blocks, spec) -> list[str]:
    """Relation logic across families, not adjacent-word bigrams."""
    out = []
    for role, text in blocks:
        for sentence in sentences(text):
            norm = normalise(sentence)
            if has_any(norm, spec["negationTerms"]):
                continue
            lab = has_any(norm, spec["laboratorySubjectTerms"])
            ind_subject = has_any(norm, spec["industrialSubjectTerms"])
            completion = has_any(norm, spec["completionTerms"])
            ind_noun = has_any(norm, spec["industrialNounTerms"])
            if lab and completion and ind_noun:
                out.append(
                    f"{role}: laboratory work asserted to have completed the industrial "
                    f"engineering [{lab[0]} / {completion[0]} / {ind_noun[0]}] -> {sentence[:140]}")
                continue
            diminutive = has_any(norm, spec["diminutiveTerms"])
            reproduction = has_any(norm, spec["reproductionTerms"])
            if ind_subject and diminutive and reproduction:
                out.append(
                    f"{role}: industrial scale-up reduced to copying "
                    f"[{ind_subject[0]} / {diminutive[0]} / {reproduction[0]}] -> {sentence[:140]}")
    return out


def recycle_violations(blocks, spec) -> list[str]:
    """An unqualified learner block, and a universality claim in any role."""
    out = []
    share_words = ["parts in", "per cent", "percent", "%", "convert", "converts", "conversion"]
    for role, text in blocks:
        norm_block = normalise(text)
        carries_figure = any(f in text for f in spec["figures"])
        if not carries_figure or not has_any(norm_block, share_words):
            continue
        for sentence in sentences(text):
            if not any(f in sentence for f in spec["figures"]):
                continue
            norm = normalise(sentence)
            quantifier = has_any(norm, spec["universalQuantifierTerms"])
            context = has_any(norm, spec["plantContextTerms"])
            if quantifier and context:
                out.append(
                    f"{role}: conversion figure universalised [{quantifier[0]} / {context[0]}] "
                    f"-> {sentence[:140]}")
        if role not in LEARNER_ROLES:
            continue
        if has_any(norm_block, spec["qualificationTerms"]):
            continue
        out.append(f"{role}: conversion figure printed without a reported/example qualification -> {text[:140]}")
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
    exempt_problems, _exempt_nodes = exemption_findings(raw, inv)
    results.check("every exemption marker is registered, in-role, and resolves through its declared selector",
                  not exempt_problems, exempt_problems)
    results.check("the exemption contract is closed and accounted for",
                  len(inv["exemptions"]) >= 8
                  and sum(e["expectedCount"] for e in inv["exemptions"]) == len(BeautifulSoup(raw, "html.parser").select(f'[{inv["scanScope"]["exemptionAttribute"]}]')),
                  {"registered": sum(e["expectedCount"] for e in inv["exemptions"]),
                   "inDom": len(BeautifulSoup(raw, "html.parser").select(f'[{inv["scanScope"]["exemptionAttribute"]}]'))})
    blocks = scannable_blocks(raw, inv)
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
                  and "may not change the amount" in inv["catalyst"]["protectedProposition"], "")
    # A catalyst this package actually names in learner evidence must resolve to
    # the catalyst subject concept. Osmium was silently dropped from that list in
    # an earlier hardening pass and three misconceptions escaped; this closes it.
    cat_spec = inv["catalyst"]
    named = cat_spec.get("namesInEvidence", [])
    unresolved = [n for n in named
                  if not has_any_stemmed(normalise_stemmed(n), cat_spec["subjectTerms"])]
    results.check("every catalyst named in the evidence estate resolves to the catalyst subject concept",
                  named and not unresolved, unresolved)
    learner_text = " ".join(lowered[r] for r in LEARNER_ROLES)
    absent = [n for n in named if n.lower() not in learner_text]
    results.check("every catalyst name the registry claims is in evidence is actually printed to learners",
                  not absent, absent)
    results.check("the catalyst subject list still carries the aliases an earlier pass dropped",
                  all(a in cat_spec["subjectTerms"] for a in ("osmium", "promoted iron")),
                  cat_spec["subjectTerms"])
    results.check("the final-state contract separates strong terms from context-dependent ones",
                  cat_spec.get("finalStateStrongTerms") and cat_spec.get("finalStateContextualTerms")
                  and cat_spec.get("mixtureContextTerms")
                  and "cannot satisfy it" in cat_spec.get("finalStateRule", ""), "")
    results.check("the ammonia formula is folded to one concept regardless of notation",
                  normalise("NH3").strip() == "ammonia"
                  and normalise("NH\u2083").strip() == "ammonia"
                  and normalise("NH 3").strip() == "ammonia"
                  and "ammonia" in normalise(
                      BeautifulSoup("<p>makes more NH<sub>3</sub> here</p>", "html.parser").get_text(" ")),
                  {"ascii": normalise("NH3").strip(), "subscript": normalise("NH\u2083").strip(),
                   "extracted": normalise("NH 3").strip()})
    results.check("the catalyst contract declares both a negative relation and a positive boundary",
                  len(inv["catalyst"]["rules"]) == 2
                  and any("NEGATIVE RELATION" in r for r in inv["catalyst"]["rules"])
                  and any("POSITIVE BOUNDARY" in r for r in inv["catalyst"]["rules"]), "")
    results.check("the temperature contract treats a numeric anchor as evidence, not a waiver",
                  inv["temperature"]["numericAnchorIsEvidenceNotWaiver"] is True
                  and "never a waiver" in inv["temperature"]["rule"], "")
    results.check("the attribution contract uses family relations rather than adjacency",
                  len(inv["attribution"]["rules"]) == 2
                  and "adjacency are irrelevant" in inv["attribution"]["rules"][0], "")
    results.check("the recycle contract declares a non-adjacent universality rule",
                  any("need not be adjacent" in r for r in inv["recycle"]["rules"]), "")
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

    # ---- B3: figure accessibility text against canonical chronology ---------
    access = registry["figureAccessibilityContract"]
    access_findings = figure_accessibility_findings(soup, access, registry["chronology"])
    results.check("figure accessibility text matches the canonical sourced conditions",
                  not access_findings, access_findings)
    demo = next(c for c in registry["chronology"]
                if c.get("year") == "1909" and c.get("sourcedConditions"))
    results.check("the chronology keeps the two 1909 conditions as separate sourced facts",
                  len(demo["sourcedConditions"]) == 2
                  and {c["epistemicStatus"] for c in demo["sourcedConditions"]} == {"calculated", "obtained"}
                  and {c["pressure"]["unit"] for c in demo["sourcedConditions"]} == {"atmospheres", "bar"}
                  and demo.get("unitConflationProhibited") is True,
                  [(c["id"], c["epistemicStatus"], c["pressure"]) for c in demo["sourcedConditions"]])
    # Scoped to the factual fields: conflationNote deliberately names the pattern
    # it forbids, and must not be read as an instance of it.
    factual = json.dumps([{k: v for k, v in c.items() if k not in ("conflationNote",)}
                          for c in registry["chronology"]])
    results.check("no chronology entry merges the two pressures into one range",
                  not re.search(r"175\s*(?:to|-|\u2013|\u2014)\s*200", factual), "")
    results.check("the chronology records why the two conditions may not be merged",
                  "conflationNote" in demo and "never be merged" in demo["conflationNote"], "")

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
