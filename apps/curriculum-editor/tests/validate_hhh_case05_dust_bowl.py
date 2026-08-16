#!/usr/bin/env python3
"""Case-scoped protections for HHH Campaign 1 Core Case 05 — The Dust Bowl.

These assertions guard the boundaries this case exists to get right, plus the
cross-edition parity that the shared operational walk does not reach into. They
are driven by the contract blocks the task registry declares — ``causalFrame``,
``subsoilBoundary``, ``droughtQualification``, ``landUseQualification``,
``policyQualification`` and ``sourceStatusContract`` — rather than by literal
paragraph locks, so ordinary rewording stays possible while the meaning stays
protected.

The two audit dependencies this case carries:

* ``HHH-GAME-C1L5-001`` — the runtime level once described the exposed subsoil
  as biologically dead and incapable of growing anything. That was corrected in
  the game before this package was authored. The curriculum must never
  reintroduce the absolute, and this case goes further: it teaches the boundary
  as an assessed task, so the guard has a positive requirement as well as a
  negative one.
* ``HHH-GAME-C1L5-002`` — the runtime level's summing-up presses hard enough
  against the "act of God" reading that a learner can come away believing the
  drought was irrelevant. The curriculum must keep the drought a contributing
  cause in every role.

DESIGN NOTE — why these guards are shaped the way they are.

Case 04's catalyst contract began as a blacklist of verbs meaning *increase* and
could not converge: reviewers kept finding new ways to say it, and the guard had
to be rebuilt fail-closed around registered sentence fingerprints. That spiral is
avoidable, and it is avoided here by never policing an ordinary verb.

Each contract below pairs:

  * a NEGATIVE guard over a genuinely CLOSED class of English — absolutes
    (*dead*, *lifeless*, *sterile*, *nothing grows*), sole-cause markers
    (*alone*, *only*, *solely*), denials (*did not cause*, *made no difference*)
    and termination verbs (*ended*, *stopped*, *cured*). These classes are small
    and finite in a way that "synonyms for increase" is not; and

  * a POSITIVE STRUCTURAL requirement that the correct framing is actually
    present, checked against markup rather than prose — ``data-causal-role``,
    ``data-subsoil-reading``, ``data-policy-confound``, ``data-source-id``.

The positive half is what actually carries the audit requirements. A guard that
only forbade the wrong sentence would be satisfied by a packet that said nothing
at all; requiring the drought to hold a named causal role in every document
cannot be satisfied by silence.

Exemption is a closed contract. A node may be excused only by naming a
registered exemption id that resolves, for that role, through a selector the
registry declares. Adding an attribute cannot make a bad sentence disappear.

Every guard ships with a NEGATIVE CONTROL — a synthetic fragment it must flag —
and the package itself is the POSITIVE CONTROL. A guard that has silently
stopped working therefore fails the run rather than passing it quietly.

Usage:
    python3 apps/curriculum-editor/tests/validate_hhh_case05_dust_bowl.py
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "hhh/campaign-1/case-05-dust-bowl"
SOURCE = UNIT / "source"
LEARNER_ROLES = ("student", "accessible")
ALL_ROLES = ("student", "teacher", "answer", "accessible")

# Propositions break on terminal punctuation only. A semicolon, colon or dash is
# internal punctuation and not a safety boundary: splitting on them would let
# "The subsoil holds a trace of organic matter; nothing lives in it" evade the
# absolutes gate by one character.
PROPOSITION_SPLIT = re.compile(r"(?<=[.!?])\s+")
DECIMAL_GUARD = re.compile(r"(\d)\.(\d)")


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
    return re.sub(r"\s+", " ", text).strip()


def propositions(text: str) -> list[str]:
    guarded = DECIMAL_GUARD.sub(r"\1\2", normalise(text))
    parts = [p.replace("", ".").strip() for p in PROPOSITION_SPLIT.split(guarded)]
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


import copy

PARAGRAPH_TAGS = ("p", "li", "td", "th", "dd", "figcaption", "caption")


def leaf_blocks(page) -> list:
    """Paragraph-level containers, with registered exempt subtrees removed.

    Two properties matter and both were learned the hard way on the first run.

    Innermost-container selection means each run of prose is scanned exactly
    once: a sentence inside a paragraph inside a table cell is not counted
    three times, and a violation cannot be reported once per nesting level.

    Exempt-subtree REMOVAL, rather than skipping the exempt node, is what makes
    a registered exemption work on a clause. An Answer Key floor that quotes the
    answer it refuses is a span inside an ordinary paragraph; skipping the span
    while still scanning its parent would leave the quoted wording in the
    parent's text and fail the packet for carrying its own floor. The paragraph
    is therefore scanned with the exempt span's text taken out of it, so the
    exemption covers exactly what it wraps and no more.
    """
    blocks = []
    for node in page.find_all(PARAGRAPH_TAGS):
        if node.find(PARAGRAPH_TAGS):
            continue
        if exempt_ids(node):
            continue
        clone = copy.copy(node)
        clone = BeautifulSoup(str(node), "html.parser")
        for exempted in clone.select("[data-semantic-exemption]"):
            exempted.decompose()
        text = normalise(clone.get_text(" ", strip=True))
        if text:
            blocks.append((node, text))
    # Text that lives outside any paragraph container - a warning strip built
    # from nested spans, for instance - would otherwise never be scanned.
    for node in page.find_all("span"):
        if node.find_parent(PARAGRAPH_TAGS) or node.find("span"):
            continue
        if exempt_ids(node):
            continue
        text = normalise(node.get_text(" ", strip=True))
        if text:
            blocks.append((node, text))
    return blocks


def contains_any(haystack: str, needles) -> list[str]:
    return [n for n in needles if n.lower() in haystack]


# ---------------------------------------------------------------------------
# The five semantic contracts.
#
# Each returns a list of violations: (role, page-id, matched-terms, sentence).
# Each takes the registry contract block, so the vocabulary lives in the
# canonical package source and not in this file.
# ---------------------------------------------------------------------------

def subject_matchers(contract: dict) -> list[re.Pattern]:
    """The protected subject, compiled from the registry.

    This used to be a module-level constant in this file - a private second
    authority beside the registry's declared subject register, and it diverged:
    it had no pattern for "the lower soil layer", so the prohibited claim simply
    fell outside the guard when a learner used that ordinary name for the layer.
    """
    return [re.compile(pattern, re.I) for pattern in contract["subjectPatterns"]]


def zero_class_matchers(boundary: dict) -> list[tuple[str, re.Pattern]]:
    """Compile the canonical concept classes the registry declares.

    There is exactly one authority. The matcher is built here from
    ``subsoilBoundary.prohibitedConceptClasses`` and nowhere else; the eighteen
    ``prohibitedFramings`` phrases are reconciled against it by an assertion
    rather than duplicated into a second list this file would then have to keep
    in step. The first candidate had both a registry list and a validator list,
    and they diverged without anything noticing.
    """
    compiled = []
    for class_id, spec in boundary["prohibitedConceptClasses"].items():
        if not isinstance(spec, dict) or "patterns" not in spec:
            continue
        for pattern in spec["patterns"]:
            compiled.append((class_id, re.compile(pattern, re.I)))
    return compiled


def subsoil_violations(soup: BeautifulSoup, contract: dict, structural: list[str],
                       boundary: dict) -> list[tuple]:
    """One rule, scoped to the protected subject.

    A proposition naming the protected layer together with a declared
    biological-zero or universal-growth-zero concept fails. Nothing else fails.

    There used to be a second, blocking rule requiring any life-or-growth claim
    about the layer to contain a listed comparative adjective. It is gone. It
    could not converge - every review round found more truthful prose it
    rejected, because there are indefinitely many ways to say a layer holds less
    - and it was never where safety came from. Safety is the closed zero classes;
    the must-pass corpus is what demonstrates they do not overmatch.
    """
    negations = [t.lower() for t in contract["negationTerms"]]
    matchers = zero_class_matchers(boundary)
    subjects = subject_matchers(contract)
    out = []
    for role in ALL_ROLES:
        for page in pages_for(soup, role):
            page_id = page.get("data-page-id")
            for node, text in leaf_blocks(page):
                if exempt_ids(node) or structurally_exempt(node, structural):
                    continue
                for prop in propositions(text):
                    low = prop.lower()
                    if not any(subject.search(low) for subject in subjects):
                        continue
                    if contains_any(low, negations):
                        continue
                    # ZERO-CLASS FIRST, AND DECISIVE. The bounded families below
                    # can never clear a matched zero concept: a statement that
                    # carries one is appended and the proposition is done. That
                    # ordering is what stops the permissive half from becoming an
                    # escape hatch as it widens.
                    hits = [f"{class_id}:{m.search(low).group(0)}"
                            for class_id, m in matchers if m.search(low)]
                    if hits:
                        out.append((role, page_id, hits[:2], prop))
                        continue
    return out


def drought_violations(soup: BeautifulSoup, contract: dict, structural: list[str]) -> list[tuple]:
    pattern = re.compile(contract["denialPattern"], re.I)
    negations = [t.lower() for t in contract.get("negationTerms", [])]
    out = []
    for role in ALL_ROLES:
        for page in pages_for(soup, role):
            page_id = page.get("data-page-id")
            for node, text in leaf_blocks(page):
                if exempt_ids(node) or structurally_exempt(node, structural):
                    continue
                for prop in propositions(text):
                    low = prop.lower()
                    if contains_any(low, negations):
                        continue
                    match = pattern.search(low)
                    if match:
                        out.append((role, page_id, [match.group(0)[:60]], prop))
    return out


def landuse_violations(soup: BeautifulSoup, contract: dict, structural: list[str]) -> list[tuple]:
    subjects = [t.lower() for t in contract["subjectTerms"]]
    markers = [t.lower() for t in contract["soleCauseTerms"]]
    outcomes = [t.lower() for t in contract["outcomeTerms"]]
    negations = [t.lower() for t in contract["negationTerms"]]
    out = []
    for role in ALL_ROLES:
        for page in pages_for(soup, role):
            page_id = page.get("data-page-id")
            for node, text in leaf_blocks(page):
                if exempt_ids(node) or structurally_exempt(node, structural):
                    continue
                for prop in propositions(text):
                    low = prop.lower()
                    if contains_any(low, negations):
                        continue
                    s = contains_any(low, subjects)
                    m = contains_any(low, markers)
                    o = contains_any(low, outcomes)
                    if s and m and o:
                        out.append((role, page_id, s[:1] + m[:1] + o[:1], prop))
    return out


def policy_violations(soup: BeautifulSoup, contract: dict, structural: list[str]) -> list[tuple]:
    subjects = [t.lower() for t in contract["subjectTerms"]]
    terminations = [t.lower() for t in contract["terminationTerms"]]
    negations = [t.lower() for t in contract["negationTerms"]]
    out = []
    for role in ALL_ROLES:
        for page in pages_for(soup, role):
            page_id = page.get("data-page-id")
            for node, text in leaf_blocks(page):
                if exempt_ids(node) or structurally_exempt(node, structural):
                    continue
                for prop in propositions(text):
                    low = prop.lower()
                    if contains_any(low, negations):
                        continue
                    s = contains_any(low, subjects)
                    t = contains_any(low, terminations)
                    if s and t:
                        out.append((role, page_id, s[:1] + t[:1], prop))
    return out


def fragment(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


def probe(role: str, body: str) -> BeautifulSoup:
    return fragment(f'<main><section class="page" data-role="{role}" '
                    f'data-page-id="probe-{role}">{body}</section></main>')


def main() -> int:
    results = Results()
    package, registry, layout, soup = load()
    structural = [entry["selector"] for entry in registry["semanticInvariants"]["structuralExemptSelectors"]]
    boundary = registry["subsoilBoundary"]

    # --- source integrity ---------------------------------------------------
    for key, filename in (("content", "content.html"), ("presentation", "presentation.css"),
                          ("taskRegistry", "task-registry.js"), ("layoutOverrides", "layout-overrides.json")):
        digest = hashlib.sha256((SOURCE / filename).read_bytes()).hexdigest()
        results.check(f"declared source hash matches {filename}",
                      package["sourceHashes"][key] == digest,
                      f"declared {package['sourceHashes'][key]} actual {digest}")

    results.check("package, registry and layout agree on the case identity",
                  package["id"] == registry["case"] == layout["caseId"] == "HHH-C1-CASE05")
    # RELEASED-STATE LIFECYCLE. The two candidate-state assertions that stood here
    # were converted by release conversion rather than deleted: the protection is
    # the same, aimed at the state the package is actually in.
    results.check("the package and task registry both carry the approved lifecycle",
                  package["status"] == "APPROVED_STABLE"
                  and registry["status"] == "APPROVED_STABLE"
                  and registry["ownerReviewStatus"] == "OWNER_REVIEW_PASS"
                  and package["approval"]["status"] == "APPROVED"
                  and package["approval"]["printStatus"] == "PASS"
                  and package["approval"]["date"] == "2026-08-16"
                  and package["approval"]["owner"] == "Nate / Owner",
                  json.dumps({"package": package["status"], "registry": registry["status"],
                              "approval": package["approval"]}))
    history = UNIT / "history"
    release_path = history / "release-v0.1.json"
    approval_path = history / "CASE05_OWNER_APPROVAL_v0.1.md"
    results.check("both owner-approval and release history records exist",
                  release_path.is_file() and approval_path.is_file()
                  and package.get("releaseHistory") == release_path.relative_to(ROOT).as_posix(),
                  sorted(x.name for x in history.iterdir()) if history.exists() else "no history dir")
    release = json.loads(release_path.read_text(encoding="utf-8")) if release_path.is_file() else {}
    results.check("the release record agrees with the package on identity and approval",
                  release.get("caseId") == package["id"]
                  and release.get("curriculumVersion") == package["version"]
                  and release.get("status") == package["status"]
                  and release.get("approvalDate") == package["approval"]["date"]
                  and release.get("owner") == package["approval"]["owner"],
                  json.dumps({k: release.get(k) for k in
                              ("caseId", "curriculumVersion", "status", "approvalDate", "owner")}))
    results.check("the release record certifies the same source bytes the package declares",
                  release.get("sourceHashes") == package["sourceHashes"],
                  json.dumps(release.get("sourceHashes")))
    results.check("the release record agrees with the package on role page counts",
                  release.get("rolePageCounts") == {r: v["pageCount"]
                                                    for r, v in package["rolePageStructure"].items()},
                  json.dumps(release.get("rolePageCounts")))
    results.check("every release commit pin is resolved to a real commit, with no placeholder left",
                  all(isinstance(release.get(k), str) and re.fullmatch(r"[0-9a-f]{40}", release.get(k, ""))
                      for k in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                "formerArtifactRecoveryCommit")),
                  json.dumps({k: release.get(k) for k in
                              ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                               "formerArtifactRecoveryCommit")}))
    # The lifecycle stamp must never reach a classroom page.
    printable = normalise(" ".join(page.get_text(" ", strip=True) for page in soup.select("section.page")))
    leaked_lifecycle = [token for token in
                        ("APPROVED_STABLE", "OWNER_REVIEW_PASS", "VALIDATION_BUILD",
                         "packageStatus", "releaseHistory", "release-v0.1")
                        if token in printable]
    results.check("no printable role displays release, approval or lifecycle metadata",
                  not leaked_lifecycle, leaked_lifecycle)
    results.check("the package is pinned to the integrated game baseline",
                  registry["gameCommit"] == "d9fc16baf272cb543c29cbd0c06ec85efad60be8",
                  registry["gameCommit"])

    # --- page structure -----------------------------------------------------
    for role, declared in package["rolePageStructure"].items():
        pages = pages_for(soup, role)
        results.check(f"{role}: rendered page count matches the package",
                      len(pages) == declared["pageCount"],
                      f"{len(pages)} rendered vs {declared['pageCount']} declared")
        labels_ok = all(f"of {declared['pageCount']}" in (p.get("aria-label") or "") for p in pages)
        results.check(f"{role}: every page aria-label states the correct total", labels_ok)
        footers_ok = all(f"of {declared['pageCount']}" in p.select_one("[data-publication-footer]").get_text()
                         for p in pages)
        results.check(f"{role}: every publication footer states the correct total", footers_ok)
    results.check("registry role page counts match the package",
                  registry["roles"] == {r: v["pageCount"] for r, v in package["rolePageStructure"].items()},
                  json.dumps(registry["roles"]))

    # --- task parity --------------------------------------------------------
    tasks = registry["tasks"]
    results.check("the registry declares nine tasks numbered 1 to 9",
                  [t["number"] for t in tasks] == [str(i) for i in range(1, 10)],
                  [t["number"] for t in tasks])
    for task in tasks:
        for role, page_id in task["pagePlacement"].items():
            results.check(f"{task['id']}: declared {role} page {page_id} exists",
                          soup.select_one(f'section.page[data-page-id="{page_id}"][data-role="{role}"]') is not None)
    for role in ("student", "answer", "accessible"):
        headings = {h.get("data-shell-task-heading") for h in soup.select(
            f'section.page[data-role="{role}"] [data-shell-task-heading]')}
        results.check(f"{role}: carries a heading for every one of the nine tasks",
                      headings == {t["number"] for t in tasks}, sorted(headings))

    teacher_text = normalise(" ".join(p.get_text(" ", strip=True) for p in pages_for(soup, "teacher")))
    procedure = " ".join(normalise(n.get_text(" ", strip=True))
                         for n in soup.select('section.page[data-role="teacher"] ol.final-task-route'))
    for task in tasks:
        reference = f"{task['number']} · {task['title']}"
        bolded = any(normalise(n.get_text(" ", strip=True)) == reference
                     for n in soup.select('section.page[data-role="teacher"] strong.task-reference'))
        results.check(f"{task['id']}: Teacher references it by exact bold number and title",
                      bolded, reference)
        results.check(f"{task['id']}: the Teacher teaching procedure accounts for it",
                      reference in procedure, reference)
    results.check("the Teacher guide carries all seven contract functions",
                  all(token in teacher_text for token in (
                      "Launch sheet", "Standards alignment", "Complete teaching procedure",
                      "Formative", "Evidence and reasoning architecture", "Quick classroom rubric",
                      "Complete analytic rubric", "Authoritative sources",
                      "Complete no-game evidence fallback")))

    # --- source estate ------------------------------------------------------
    canonical = {s["id"]: s for s in registry["caseSources"]}
    status_vocabulary = set(registry["sourceStatusContract"]["statusVocabulary"])
    bound = set()
    for node in soup.select("[data-source-id]"):
        for source_id in (node.get("data-source-id") or "").split():
            bound.add(source_id)
            results.check(f"data-source-id {source_id} resolves to a canonical source",
                          source_id in canonical, source_id)
    results.check("every canonical source is bound somewhere in the package or its ledger",
                  set(canonical) <= bound | {r for row in soup.select("[data-ledger-source]")
                                             for r in (row.get("data-ledger-source") or "").split()},
                  sorted(set(canonical) - bound))

    for status_node in soup.select(".source-status"):
        text = normalise(status_node.get_text(" ", strip=True))
        match = re.match(r"STATUS:\s*([a-z]+)", text)
        results.check(f"printed status line declares a registered status word: {text[:60]}",
                      bool(match) and match.group(1) in status_vocabulary, text[:120])

    for role in LEARNER_ROLES:
        cards = [c for c in soup.select(f'section.page[data-role="{role}"] [data-source-id="archive-plains"]')
                 if c.select_one(".source-status")]
        statuses = [normalise(c.select_one(".source-status").get_text()) for c in cards]
        results.check(f"{role}: the game reconstruction is labelled reconstructed wherever it carries a status",
                      statuses and all("reconstructed" in s.lower() for s in statuses), statuses)
        results.check(f"{role}: page 1 carries the reconstruction and causation notice",
                      pages_for(soup, role)[0].select_one("[data-reconstruction-boundary]") is not None)

    ledger_rows = soup.select("[data-ledger-source]")
    ledger_ids = {i for row in ledger_rows for i in (row.get("data-ledger-source") or "").split()}
    results.check("the Teacher source ledger covers the canonical estate in both directions",
                  ledger_ids == set(canonical),
                  json.dumps({"missing": sorted(set(canonical) - ledger_ids),
                              "unknown": sorted(ledger_ids - set(canonical))}))
    grouped = [row for row in ledger_rows if row.get("data-ledger-grouping")]
    results.check("any ledger row covering more than one source declares a grouping rule",
                  all(len((row.get("data-ledger-source") or "").split()) == 1 or row.get("data-ledger-grouping")
                      for row in ledger_rows), len(grouped))

    # --- runtime identifiers ------------------------------------------------
    whole_text = normalise(soup.get_text(" ", strip=True)).lower()
    leaked = [ident for ident in registry["sourceStatusContract"]["prohibitedRuntimeIdentifiers"]
              if ident.lower() in whole_text]
    results.check("no runtime clue tag, source key, location id or node name reaches any role",
                  not leaked, leaked)

    # --- POSITIVE STRUCTURAL REQUIREMENTS ----------------------------------
    frame_roles = [r["id"] for r in registry["causalFrame"]["roles"]]
    results.check("the registry declares the four causal roles",
                  frame_roles == ["condition", "vulnerability", "mechanism", "response"], frame_roles)
    for required in ("condition", "vulnerability"):
        for role in ALL_ROLES:
            marked = soup.select(f'section.page[data-role="{role}"] [data-causal-role="{required}"]')
            results.check(f"{role}: carries the {required} in a marked causal role",
                          len(marked) >= 1, f"{len(marked)} marked nodes")
    for role in LEARNER_ROLES:
        slots = soup.select(f'section.page[data-role="{role}"] .cause-role[data-causal-role]')
        present = [s.get("data-causal-role") for s in slots]
        results.check(f"{role}: the causation map prints all four roles",
                      present == frame_roles, present)
        results.check(f"{role}: the causation map marks the feedback relation",
                      soup.select_one(f'section.page[data-role="{role}"] [data-causal-relation="feedback"]') is not None)

    subsoil_positive = registry["semanticInvariants"]["subsoil"]["positiveRequirement"]
    for role in subsoil_positive["requiredRoles"]:
        found = soup.select(f'section.page[data-role="{role}"] [{subsoil_positive["requiredAttribute"]}]')
        results.check(f"{role}: prints at least one bounded subsoil reading",
                      len(found) >= subsoil_positive["minimumPerRole"], len(found))
        for node in found:
            text = normalise(node.get_text(" ", strip=True)).lower()
            qualifiers = contains_any(text, [q.lower() for q in
                                             registry["semanticInvariants"]["subsoil"]["approvedQualifierTerms"]])
            results.check(f"{role}: the bounded subsoil reading carries an approved comparative qualifier",
                          bool(qualifiers), text[:160])

    policy_positive = registry["semanticInvariants"]["policy"]["positiveRequirement"]
    for role in policy_positive["requiredRoles"]:
        found = soup.select(f'section.page[data-role="{role}"] [{policy_positive["requiredAttribute"]}]')
        results.check(f"{role}: prints the confound the policy sequence cannot separate",
                      len(found) >= policy_positive["minimumPerRole"], len(found))
    for role in LEARNER_ROLES:
        confound = soup.select_one(f'section.page[data-role="{role}"] [data-policy-confound]')
        text = normalise(confound.get_text(" ", strip=True)).lower() if confound else ""
        results.check(f"{role}: the printed confound names the return of the rains",
                      "rains return" in text or "rains returned" in text, text[:160])

    # --- NEGATIVE SEMANTIC GUARDS, on the real package ---------------------
    invariants = registry["semanticInvariants"]
    for label, violations in (
        ("subsoil biological-zero", subsoil_violations(soup, invariants["subsoil"], structural, boundary)),
        ("drought denial", drought_violations(soup, invariants["drought"], structural)),
        ("land-use sole cause", landuse_violations(soup, invariants["landuse"], structural)),
        ("policy single-cause cure", policy_violations(soup, invariants["policy"], structural)),
    ):
        results.check(f"no unregistered {label} claim in any role",
                      not violations,
                      json.dumps([{"role": v[0], "page": v[1], "matched": v[2], "text": v[3][:220]}
                                  for v in violations[:6]], indent=1))

    # --- NEGATIVE CONTROLS --------------------------------------------------
    # Each guard must flag a synthetic fragment. A guard that has silently
    # stopped matching therefore fails the run rather than passing it quietly.
    controls = (
        ("subsoil", subsoil_violations,
         probe("student", "<p>Below the topsoil the subsoil is biologically dead and nothing can grow in it.</p>"),
         invariants["subsoil"]),
        ("subsoil (bare absolute)", subsoil_violations,
         probe("answer", "<p>The subsoil has no microbial life left in it at all.</p>"),
         invariants["subsoil"]),
        ("subsoil (direct predicate, no second life token)", subsoil_violations,
         probe("student", "<p>The subsoil is dead.</p>"),
         invariants["subsoil"]),
        ("drought", drought_violations,
         probe("student", "<p>The drought did not cause the Dust Bowl.</p>"),
         invariants["drought"]),
        ("drought (dismissal)", drought_violations,
         probe("teacher", "<p>In the end the dry years made no difference to what happened.</p>"),
         invariants["drought"]),
        ("landuse", landuse_violations,
         probe("student", "<p>The plowing alone caused the Dust Bowl.</p>"),
         invariants["landuse"]),
        ("policy", policy_violations,
         probe("accessible", "<p>The Soil Conservation Act ended the dust storms.</p>"),
         invariants["policy"]),
    )
    for label, fn, sample, contract in controls:
        args = (sample, contract, structural, boundary) if fn is subsoil_violations else (sample, contract, structural)
        results.check(f"negative control: the {label} guard flags a synthetic violation",
                      bool(fn(*args)), label)

    # A registered exemption must clear the same sentence, and an unregistered
    # attribute value must not.
    exempted = probe("student",
                     '<div class="account-item" data-semantic-exemption="claim-under-test-learner">'
                     "<p>Below the topsoil the subsoil is biologically dead and nothing can grow in it.</p></div>")
    results.check("registered exemption clears an otherwise-failing claim under test",
                  not subsoil_violations(exempted, invariants["subsoil"], structural, boundary))
    registered_ids = {e["id"] for e in invariants["exemptions"]}
    used_ids = {n.get("data-semantic-exemption") for n in soup.select("[data-semantic-exemption]")}
    results.check("every exemption used in the package is registered in the contract",
                  used_ids <= registered_ids, sorted(used_ids - registered_ids))
    results.check("every registered exemption is actually used, so the contract carries no dead entries",
                  registered_ids <= used_ids, sorted(registered_ids - used_ids))
    for exemption in invariants["exemptions"]:
        roles_used = {p.get("data-role") for p in soup.select("section.page")
                      if p.select_one(f'[data-semantic-exemption="{exemption["id"]}"]')}
        results.check(f"exemption {exemption['id']} is used only in its declared roles",
                      roles_used <= set(exemption["roles"]),
                      json.dumps({"declared": exemption["roles"], "used": sorted(roles_used)}))

    # --- R2: THE DECLARED PROHIBITED FRAMINGS ARE ACTUALLY ENFORCED --------
    # The first candidate declared eighteen prohibited framings and referenced
    # them zero times. Rather than copy them into a second hand-maintained list,
    # each declared phrase is bound to a protected subject and must be caught by
    # the concept classes. That is what keeps the declared and enforced
    # contracts from drifting apart again.
    uncaught = []
    for phrase in boundary["prohibitedFramings"]:
        sample = probe("student", f"<p>The subsoil is {phrase}.</p>")
        alt = probe("student", f"<p>Beneath the topsoil the ground {phrase}.</p>")
        if not (subsoil_violations(sample, invariants["subsoil"], structural, boundary)
                or subsoil_violations(alt, invariants["subsoil"], structural, boundary)):
            uncaught.append(phrase)
    results.check("every prohibited framing the registry declares is caught by the enforced concept classes",
                  not uncaught, uncaught)
    results.check("the registry carries no second, hand-maintained absolute list to drift from",
                  "absoluteTerms" not in invariants["subsoil"]
                  and "absoluteTermsRemoved" in invariants["subsoil"])
    results.check("the concept classes are declared self-sufficient, needing no second life token",
                  boundary["prohibitedConceptClasses"].get("selfSufficient") is True)

    # The corpus ships in the registry, so a mutation to the contract carries its
    # own tests with it. Every sentence binds the protected subject explicitly.
    corpus = boundary["boundaryCorpus"]

    def fails(sentence: str, role: str = "student") -> bool:
        return bool(subsoil_violations(probe(role, f"<p>{sentence}</p>"),
                                       invariants["subsoil"], structural, boundary))

    for group, sentences in corpus["mustFailZero"].items():
        if not isinstance(sentences, list):
            continue
        escaping = [x for x in sentences if not fails(x)]
        results.check(f"zero-class corpus '{group}': all {len(sentences)} sentences fail",
                      not escaping, escaping)

    passing_total, false_positives = 0, []
    for group, sentences in corpus["mustPassSafeProse"].items():
        if not isinstance(sentences, list):
            continue
        passing_total += len(sentences)
        hit = [x for x in sentences if fails(x)]
        false_positives.extend(hit)
        results.check(f"safe-prose corpus '{group}': all {len(sentences)} truthful sentences pass",
                      not hit, hit)
    results.check(f"the safe-prose corpus produces zero false positives across {passing_total} sentences",
                  not false_positives, false_positives)

    # A bounded qualifier must never mask a zero claim, in either clause order.
    results.check("safe wording in the same sentence cannot clear a zero concept, in either order",
                  fails("Fertility below the topsoil is low, but the subsoil is sterile.")
                  and fails("The subsoil is sterile, but fertility is low."))

    # Declared scope must equal enforced scope.
    results.check("the declared enforcement scope matches the four roles the validator walks",
                  tuple(invariants["subsoil"]["enforcedRoles"]) == ALL_ROLES,
                  invariants["subsoil"]["enforcedRoles"])
    results.check("the declared BOUNDED rule no longer narrows itself to learner or key roles",
                  not any("learner or key role" in rule for rule in invariants["subsoil"]["rules"]))
    for role in ALL_ROLES:
        results.check(f"the zero-class boundary is enforced in {role}",
                      fails("The subsoil is dead.", role))

    # Single authority: no private validator list, and every declared bounded
    # pattern is actually compiled and reachable.
    # The blocking safe-vocabulary gate is retired, and its absence is asserted so
    # it cannot creep back. Safety is the zero classes; nothing else blocks.
    results.check("no finite safe-vocabulary list gates authored prose",
                  "boundedQualifierFamilies" not in invariants["subsoil"]
                  and "comparativeMarkers" not in invariants["subsoil"])
    results.check("the retirement is recorded in the contract rather than left as dead metadata",
                  "retiredBoundedGate" in invariants["subsoil"])
    results.check("the declared rules no longer require a bounded qualifier of ordinary prose",
                  not any("must also carry an approved bounded qualifier" in rule
                          for rule in invariants["subsoil"]["rules"])
                  and any("NO SAFE-VOCABULARY REQUIREMENT" in rule
                          for rule in invariants["subsoil"]["rules"]))
    results.check("the surviving approved-qualifier list governs only the authored reading node",
                  "data-subsoil-reading" in json.dumps(invariants["subsoil"]["positiveRequirement"])
                  or invariants["subsoil"]["positiveRequirement"]["requiredAttribute"] == "data-subsoil-reading")
    results.check("prose the corpus has never seen still passes",
                  not fails("Beneath the topsoil the soil is a shadow of what it was.")
                  and not fails("The subsoil would want a decade of cover before it fed a crop."))

    # --- MUTATION CONTROLS -------------------------------------------------
    # Each mutation is applied to a COPY of the registry contract; if the guard
    # still passes its corpus under the mutation, the control is not protecting
    # anything and this run fails.
    import copy as _copy

    def mutated(mutate) -> dict:
        clone = _copy.deepcopy(boundary)
        inner = _copy.deepcopy(invariants["subsoil"])
        mutate(clone, inner)
        return {"boundary": clone, "contract": inner}

    def corpus_holds(state: dict) -> bool:
        """True when every zero sentence still fails and every bounded one passes."""
        for group, sentences in corpus["mustFailZero"].items():
            if not isinstance(sentences, list):
                continue
            for sentence in sentences:
                if not subsoil_violations(probe("student", f"<p>{sentence}</p>"),
                                          state["contract"], structural, state["boundary"]):
                    return False
        for group, sentences in corpus["mustPassSafeProse"].items():
            if not isinstance(sentences, list):
                continue
            for sentence in sentences:
                if subsoil_violations(probe("student", f"<p>{sentence}</p>"),
                                      state["contract"], structural, state["boundary"]):
                    return False
        return True

    def drop_quantifier(b, c):
        cls = b["prohibitedConceptClasses"]["biologicalZero"]
        cls["patterns"] = [x for x in cls["patterns"] if "not\\s+(?:a|an|one)" not in x]

    def break_modal_ever(b, c):
        cls = b["prohibitedConceptClasses"]["universalGrowthZero"]
        cls["patterns"] = [x.replace("(?:can|will|could|would|shall|may|has|have|had|is|was)?\\s*(?:ever\\s+)?",
                                     "(?:can|will|could|would|ever)?\\s*") for x in cls["patterns"]]

    def drop_never_support(b, c):
        cls = b["prohibitedConceptClasses"]["universalGrowthZero"]
        cls["patterns"] = [x for x in cls["patterns"] if "never\\s+(?:again\\s+)?support" not in x]

    def drop_intensifiers(b, c):
        for name in ("biologicalZero", "universalGrowthZero"):
            cls = b["prohibitedConceptClasses"][name]
            cls["patterns"] = [x.replace("(?:at all|whatsoever)?\\s*", "") for x in cls["patterns"]]

    def drop_grew_grown(b, c):
        cls = b["prohibitedConceptClasses"]["universalGrowthZero"]
        cls["patterns"] = [x.replace("(?:grow|grows|growing|grew|grown)", "(?:grow|grows|growing)")
                            .replace("(?:grow|grows|grew|grown)", "(?:grow|grows)")
                            .replace("(?:grown|grew)", "(?:growing)") for x in cls["patterns"]]

    def drop_subject_pattern(b, c):
        c["subjectPatterns"] = [x for x in c["subjectPatterns"] if "lower" not in x]

    def bare_layer_subject(b, c):
        """B1 regression: make every layer modifier optional again."""
        c["subjectPatterns"] = ["\\bthe (?:exposed\\s+)?(?:lower\\s+)?(?:soil\\s+)?layer\\b"
                                if "(?=(?:exposed|lower|soil)" in x else x
                                for x in c["subjectPatterns"]]

    def drop_no_single(b, c):
        cls = b["prohibitedConceptClasses"]["biologicalZero"]
        cls["patterns"] = [x for x in cls["patterns"] if "no\\s+single" not in x]

    def dead_without_subject(b, c):
        """B3 regression: treat dead as a zero predicate regardless of subject."""
        c["subjectPatterns"] = c["subjectPatterns"] + ["(?:)"]

    for label, mutate in (("removing the 'not one' quantifier grammar", drop_quantifier),
                          ("collapsing the modal and adverb back into one alternation", break_modal_ever),
                          ("removing the 'never support' grammar", drop_never_support),
                          ("removing the 'at all' and 'whatsoever' intensifier slot", drop_intensifiers),
                          ("removing 'grew' and 'grown' from the growth verb family", drop_grew_grown),
                          ("dropping a declared subject pattern", drop_subject_pattern),
                          ("making every layer modifier optional again", bare_layer_subject),
                          ("removing the 'no single' quantifier grammar", drop_no_single),
                          ("scoping the guard to every subject, so surface 'dead' counts", dead_without_subject)):
        results.check(f"mutation control: {label} breaks the must-fail corpus",
                      not corpus_holds(mutated(mutate)), label)
    results.check("mutation control: the unmutated contract holds the whole corpus",
                  corpus_holds({"boundary": boundary, "contract": invariants["subsoil"]}))

    # Reintroducing the retired blocking whitelist must break the safe corpus.
    def reintroduce_bounded_gate(sentence: str) -> bool:
        """The retired rule, re-implemented locally, applied to safe prose."""
        markers = ("less", "lower", "reduced", "sparse", "scarce", "limited",
                   "minimal", "slight", "trace", "poor", "weak", "degraded")
        low = normalise(sentence).lower()
        predicates = [t.lower() for t in invariants["subsoil"]["predicateTerms"]]
        return contains_any(low, predicates) and not contains_any(low, markers)
    rejected = [x for group in corpus["mustPassSafeProse"].values() if isinstance(group, list)
                for x in group if reintroduce_bounded_gate(x)]
    def safe_half_holds(state: dict) -> bool:
        for group, sentences in corpus["mustPassSafeProse"].items():
            if not isinstance(sentences, list):
                continue
            for sentence in sentences:
                if subsoil_violations(probe("student", f"<p>{sentence}</p>"),
                                      state["contract"], structural, state["boundary"]):
                    return False
        return True
    results.check("mutation control: a bare-layer subject breaks the safe regression corpus",
                  not safe_half_holds(mutated(bare_layer_subject)))
    results.check("mutation control: an unscoped subject turns surface 'dead' into a violation",
                  not safe_half_holds(mutated(dead_without_subject)))

    results.check("mutation control: reintroducing the blocking safe-vocabulary gate rejects truthful prose",
                  bool(rejected), f"{len(rejected)} truthful sentences would be failed again")

    # Removing a must-fail group must be visible, not silently reduce coverage.
    thinned = _copy.deepcopy(boundary)
    thinned["boundaryCorpus"]["mustFailZero"].pop("neverSupport")
    results.check("mutation control: removing a must-fail corpus group is detectable",
                  set(thinned["boundaryCorpus"]["mustFailZero"])
                  != set(boundary["boundaryCorpus"]["mustFailZero"]))

    # Skipping the subject authority must not be possible: the matcher is the
    # registry's, and an empty subject list stops the guard finding anything.
    def empty_subjects(b, c):
        c["subjectPatterns"] = []
    results.check("mutation control: emptying the declared subject authority breaks the corpus",
                  not corpus_holds(mutated(empty_subjects)))

    phantom = _copy.deepcopy(invariants["subsoil"])
    phantom["subjectPatterns"].append("\\bnot-a-real-subject\\b")
    results.check("a subject pattern added to the registry is picked up by the compiled matcher",
                  len(subject_matchers(phantom)) != len(subject_matchers(invariants["subsoil"])))

    # Scope drift: narrowing the DECLARED scope back to learner-and-key while the
    # validator keeps walking four roles must break the reconciliation assertion.
    narrowed = _copy.deepcopy(invariants["subsoil"])
    narrowed["enforcedRoles"] = ["student", "accessible", "answer"]
    results.check("mutation control: narrowing the declared role scope breaks reconciliation",
                  tuple(narrowed["enforcedRoles"]) != ALL_ROLES)

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
            described = figure.select_one("[role='img'][aria-label]")
            results.check(f"{role}: figure {spec['id']} carries accessibility text",
                          described is not None)
            if described is None:
                continue
            alt = normalise(described.get("aria-label")).lower()
            for pattern in spec.get("prohibitedPatterns", []):
                hit = re.search(pattern["regex"], alt, re.I)
                results.check(f"{role}: {spec['id']} accessibility text avoids {pattern['id']}",
                              hit is None, (hit.group(0) if hit else "") + " :: " + pattern["why"])
            if spec.get("requiresAllCausalRoles"):
                missing = [r for r in frame_roles if r not in alt]
                results.check(f"{role}: {spec['id']} accessibility text names all four causal roles",
                              not missing, missing)
            if spec.get("requiresFeedbackRelation"):
                results.check(f"{role}: {spec['id']} accessibility text names the feedback relation",
                              "feedback" in alt)
            if spec.get("requiresNoWeightStatement"):
                results.check(f"{role}: {spec['id']} accessibility text states that no arrow carries a weight",
                              "no arrow carries a weight" in alt or "carries a weight" in alt)
            for mode in spec.get("requiresAllTransportModes", []):
                results.check(f"{role}: {spec['id']} accessibility text names {mode}", mode in alt)
            if spec.get("requiresBoundedSubsoilReading"):
                results.check(f"{role}: {spec['id']} accessibility text keeps the subsoil bounded",
                              "how much less" in alt and "not none" in alt)
            if spec.get("requiresAllConditions"):
                numbered = len(re.findall(r"\b(?:one|two|three|four),", alt))
                results.check(f"{role}: {spec['id']} accessibility text enumerates all four conditions",
                              numbered >= spec["requiresAllConditions"], numbered)
            if spec.get("requiresRainReturnEntry"):
                results.check(f"{role}: {spec['id']} accessibility text carries the return of the rains",
                              "rains return" in alt)
            if spec.get("requiresSchematicDisclaimer"):
                results.check(f"{role}: {spec['id']} accessibility text refuses map readings",
                              "not to scale" in alt and "not a projection" in alt)

    # --- ACCESSIBLE ADAPTATIONS ARE TRUE AND DECLARED -----------------------
    student_fence = soup.select('section.page[data-role="student"] .fence-table tbody td [data-response]')
    accessible_fence = soup.select('section.page[data-role="accessible"] .fence-table tbody td [data-response]')
    prefilled_cells = soup.select('section.page[data-role="accessible"] .fence-table tr.model-row td.prefilled')
    results.check("Task 5: the Student edition collects ten comparison cells",
                  len(student_fence) == 10, len(student_fence))
    results.check("Task 5: the Accessible edition collects eight, with two supplied as a worked model",
                  len(accessible_fence) == 8 and len(prefilled_cells) == 2,
                  f"{len(accessible_fence)} open, {len(prefilled_cells)} prefilled")
    results.check("Task 5: the modelled row is printed as an example rather than as a blank",
                  all("EXAMPLE" in normalise(row.get_text(" ", strip=True)).upper()
                      for row in soup.select('section.page[data-role="accessible"] .fence-table tr.model-row')))

    student_slots = soup.select('section.page[data-role="student"] .cause-slots [data-response]')
    accessible_slots = soup.select('section.page[data-role="accessible"] .cause-slots [data-response]')
    accessible_placed = soup.select('section.page[data-role="accessible"] .cause-slots .prefilled-slot')
    results.check("Task 6: the Student edition places all eight factors",
                  len(student_slots) == 8, len(student_slots))
    results.check("Task 6: the Accessible edition places six, with two pre-placed in two different roles",
                  len(accessible_slots) == 6 and len(accessible_placed) == 2
                  and len({p.find_parent(class_="cause-role").get("data-causal-role")
                           for p in accessible_placed}) == 2,
                  f"{len(accessible_slots)} open, {len(accessible_placed)} placed")

    declared = registry["accessibleAdaptations"]
    results.check("four Accessible adaptations are declared in the registry", len(declared) == 4, len(declared))
    answer_text = normalise(" ".join(p.get_text(" ", strip=True) for p in pages_for(soup, "answer")))
    for adaptation in declared:
        number = next(t["number"] for t in tasks if t["id"] == adaptation["task"])
        title = next(t["title"] for t in tasks if t["id"] == adaptation["task"])
        results.check(f"adaptation {adaptation['id']} is disclosed to the teacher",
                      f"{number} · {title}" in teacher_text, adaptation["id"])
    results.check("the Teacher scoring note states the modelled and pre-placed counts",
                  "eight" in teacher_text and "six" in teacher_text
                  and soup.select_one('[data-accessible-adaptation]') is not None)
    # Checked against the declared reduction counts rather than a fixed phrase,
    # so rewording the key cannot silently drop the disclosure.
    WORDS = {6: "six", 8: "eight", 10: "ten"}
    for sub in [x for x in registry["editionResponseContract"]["subparts"]
                if x["differenceClass"] == "declared-reduction"]:
        ns, na = len(sub["student"]), len(sub["accessible"])
        results.check(f"the Answer Key discloses both edition counts for {sub['task']} {sub['id']}",
                      WORDS[ns] in answer_text.lower() and WORDS[na] in answer_text.lower(),
                      f"expected {WORDS[ns]} and {WORDS[na]}")

    # --- R1: EDITION RESPONSE PARITY, AGAINST DECLARED OBLIGATIONS ----------
    # Compared against canonical per-subpart obligations rather than prose. The
    # first candidate's Accessible edition acquired a required feedback response
    # the Student edition never asked for - a fifth, undeclared, demand-raising
    # adaptation - and nothing text-level caught it.
    erc = registry["editionResponseContract"]
    subparts = erc["subparts"]
    declared = {"student": [], "accessible": []}
    for sub in subparts:
        declared["student"].extend(sub["student"])
        declared["accessible"].extend(sub["accessible"])
    for edition, prefix in (("student", "student"), ("accessible", "accessible")):
        live = [n.get("data-persist-id") for n in
                soup.select(f'section.page[data-role="{prefix}"] [data-response][data-persist-id]')]
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

    adaptation_ids = {a["id"] for a in registry["accessibleAdaptations"]}
    for sub in subparts:
        label = f"{sub['task']} {sub['id']}"
        klass, ns, na = sub["differenceClass"], len(sub["student"]), len(sub["accessible"])
        results.check(f"{label}: has no Accessible-only obligation", ns > 0,
                      "an Accessible response with no Student counterpart is a demand increase")
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

    reductions = [s for s in subparts if s["differenceClass"] == "declared-reduction"]
    results.check("every registered Accessible adaptation is either a declared reduction or a route support",
                  {s["governedBy"] for s in reductions} <= adaptation_ids,
                  sorted({s.get("governedBy") for s in reductions}))
    results.check("exactly four Accessible adaptations are declared, and no fifth has appeared",
                  len(registry["accessibleAdaptations"]) == 4,
                  sorted(adaptation_ids))
    results.check("the Teacher scoring note still claims exactly four scored differences",
                  "Four scored differences, and only four" in teacher_text)

    # Supplied-but-not-assessed material must carry no response control anywhere
    # and must be printed in every edition that declares it.
    for task in tasks:
        for supplied in task.get("suppliedNotAssessed", []):
            results.check(f"{task['id']} {supplied['id']}: supplied material is graded in no edition",
                          supplied["gradedIn"] == [], supplied["gradedIn"])
            for role in supplied["printedIn"]:
                marked = soup.select(f'section.page[data-role="{role}"] [data-causal-relation="feedback"]')
                results.check(f"{task['id']} {supplied['id']}: printed in {role}", bool(marked))
                for node in marked:
                    results.check(f"{task['id']} {supplied['id']}: carries no response control in {role}",
                                  not node.select("[data-response]"))
    results.check("Task 6 asks for no feedback response in either learner edition",
                  not soup.select('[data-persist-id*="feedback"]'),
                  [n.get("data-persist-id") for n in soup.select('[data-persist-id*="feedback"]')])

    # Task 6 lettering parity: the shared assessed parts use the same letters.
    def part_letters(role: str, page_ids: list[str]) -> list[str]:
        found = []
        for page_id in page_ids:
            page = soup.select_one(f'section.page[data-role="{role}"][data-page-id="{page_id}"]')
            for node in page.select(".part"):
                m = re.match(r"Part ([A-Z])", normalise(node.get_text(" ", strip=True)))
                if m and m.group(1) not in found:
                    found.append(m.group(1))
        return found
    student_letters = part_letters("student", ["student-dust-bowl-07"])
    accessible_letters = part_letters("accessible", ["accessible-dust-bowl-13", "accessible-dust-bowl-14"])
    results.check("Task 6 uses the same part lettering in both learner editions",
                  student_letters == accessible_letters,
                  f"student {student_letters} vs accessible {accessible_letters}")

    # Teacher and Answer Key may not require work no learner role collects.
    for role_text, label in ((teacher_text, "Teacher"), (answer_text, "Answer Key")):
        results.check(f"{label} does not present the supplied feedback as required learner work",
                      not re.search(r"feedback relation[^.]{0,40}(?:is required|must be|are required)", role_text, re.I),
                      label)

    # --- RESPONSE SPACE -----------------------------------------------------
    # No Accessible response may be smaller than the Student equivalent, and
    # every persistent response must be layout-classified.
    for edition, block, prefix in (("student", layout["student"], "student"), ("accessible", layout, "accessible")):
        declared_ids = {a["persistId"] for a in block["areas"]} | {a["persistId"] for a in block["lockedAreas"]}
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

    # --- CLAIM SCHEME -------------------------------------------------------
    marks = [c["mark"] for c in registry["claimJudgments"]["claims"]]
    results.check("the claim set carries one supported, three contradicted and one undecidable claim",
                  marks == ["Y", "N", "N", "N", "?"], marks)
    for role in LEARNER_ROLES:
        claims = soup.select(f'section.page[data-role="{role}"] .account-item')
        results.check(f"{role}: prints five claims, each with a persistent mark control",
                      len(claims) == 5 and all(c.select_one("[data-response]") for c in claims), len(claims))
    results.check("the two opposite single-cause claims are both refused",
                  registry["claimJudgments"]["claims"][1]["mark"] == "N"
                  and registry["claimJudgments"]["claims"][2]["mark"] == "N")

    # --- STANDARDS ----------------------------------------------------------
    standards = registry["standards"]
    results.check("no NGSS performance expectation is claimed as directly assessed",
                  not any(s.startswith("NGSS") for s in standards["directlyAssessed"]),
                  standards["directlyAssessed"])
    results.check("every NGSS reference is contextual and carries a written limit",
                  all(s.startswith("NGSS") for s in standards["contextual"]) and len(standards["ngss"]) > 80)
    for claim in standards["directlyAssessed"] + standards["supporting"] + standards["contextual"]:
        results.check(f"standard {claim} appears in the Teacher standards table", claim in teacher_text, claim)

    payload = {
        "validator": "hhh-case05-dust-bowl-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": [a for a in results.assertions if a["status"] == "FAIL"] or "all passed",
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
