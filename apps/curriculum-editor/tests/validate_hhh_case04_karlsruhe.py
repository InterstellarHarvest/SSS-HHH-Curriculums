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


# Refusal vocabulary. A prohibited phrase may legitimately appear in the Teacher
# Guide's misconceptions table or in an Answer Key floor, because those documents
# exist partly to name the error and reject it. It may never appear in a learner
# edition, where there is nothing to mark it as wrong. So the learner editions are
# scanned strictly, and the two teaching documents are scanned for phrases that
# are *asserted* rather than refused.
REFUSAL_MARKERS = (
    "not accepted", "do not accept", "is wrong", "are wrong", "incorrect",
    "misconception", "error", "refus", "cannot be scored", "not proficient",
    "catch", "wrongly", "not negotiable", "trap", "goes against",
)


def asserted_occurrences(soup: BeautifulSoup, phrase: str) -> list[str]:
    """Occurrences of `phrase` that are not inside a block that also refuses it.

    Learner editions are strict: any occurrence counts. Teacher and Answer Key
    occurrences are excused when the enclosing row, list item, cell or paragraph
    also carries refusal language.
    """
    findings: list[str] = []
    needle = phrase.lower()
    for page in soup.select(".page[data-role]"):
        role = page.get("data-role")
        if needle not in page.get_text(" ", strip=True).lower():
            continue
        if role in LEARNER_ROLES:
            findings.append(f"{role}: {phrase}")
            continue
        for block in page.select("tr, li, td, p, div"):
            text = block.get_text(" ", strip=True).lower()
            if needle not in text:
                continue
            if any(marker in text for marker in REFUSAL_MARKERS):
                break
        else:
            findings.append(f"{role}: {phrase} (asserted, not refused)")
    return findings


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
    temperature = registry["temperatureQualification"]
    banned_temp = [f for phrase in temperature["prohibitedFramings"]
                   for f in asserted_occurrences(soup, phrase)]
    results.check("no role asserts the operating temperature is ordinary warmth", not banned_temp, banned_temp)
    for role in ALL_ROLES:
        results.check(
            f"the {role} edition frames the operating temperature as a compromise",
            "compromise" in lowered[role], "")
    # Both learner editions must carry an anchored value, not merely the word.
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
    results.check(
        "both learner editions carry the temperature ladder",
        all(soup.select(f'.page[data-role="{role}"] [data-temperature-ruler]') for role in LEARNER_ROLES), "")

    # ---- catalyst boundary --------------------------------------------------
    catalyst = registry["catalystBoundary"]
    banned_catalyst = [f for phrase in catalyst["prohibitedClaims"]
                       for f in asserted_occurrences(soup, phrase)]
    results.check("no role asserts that the catalyst moves the equilibrium", not banned_catalyst, banned_catalyst)
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
    banned_attr = [f for phrase in attribution["prohibitedClaims"]
                   for f in asserted_occurrences(soup, phrase)]
    results.check("no role asserts a single-actor account of the industrial process",
                  not banned_attr, banned_attr)
    for role in ALL_ROLES:
        missing = [name for name in ("Haber", "Bosch", "Mittasch", "Le Rossignol") if name not in texts[role]]
        results.check(f"the {role} edition names all four contributors", not missing, missing)
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

    # ---- recycle boundary ---------------------------------------------------
    recycle = registry["recycleBoundary"]
    banned_recycle = [f for phrase in recycle["prohibitedClaims"]
                      for f in asserted_occurrences(soup, phrase)]
    results.check("no role asserts that a single pass converts the whole feed", not banned_recycle, banned_recycle)
    for role in LEARNER_ROLES:
        results.check(
            f"the {role} edition prints the single-pass share and the recycled whole-plant share",
            "15" in texts[role] and "98" in texts[role], "")

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
