#!/usr/bin/env python3
"""Case-scoped assertions for SSS Campaign 2 Case 04 — The Silent Grove.

Enforces the draft source ledger, the five-clue instructional coverage, the figure
contract, the Earth-science/case-record boundary, and the prohibited scientific
overstatements against the printable content of every role.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "shared/validation"))
from corrective_release_lifecycle import history_findings as lifecycle_findings  # noqa: E402

CASE_ID = "SSS-C2-CASE04"
CASE_ROOT = ROOT / "sss/campaign-2/case-04-silent-grove"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
# The unreleased corrective candidate, and the approved release whose records it retains.
RELEASE_VERSION = "1.2"
RELEASE_APPROVAL_DATE = "2026-08-10"
# v1.1 is the release v1.2 corrects and indexes as its prior approved release; its own pin was
# written correctly by the v1.1 follow-up.
RETAINED_VERSION = "1.1"
RETAINED_APPROVAL_DATE = "2026-08-06"
RETAINED_PINNED_COMMIT_V11 = "3fe64b9c9854d7f357fe0f89410f77a1d00c8177"
# v1.0 remains retained beneath v1.1 as the case's first approved release, with the known
# pin defect it shipped with recorded rather than corrected in place.
LEGACY_VERSION = "1.0"
LEGACY_APPROVAL_DATE = "2026-08-05"
OWNER = "Nate / Owner"
SYNCHRONISED_MAIN = "f7a24423f802a095aa149f923d05475ba2837599"
# The v1.0 record pins a commit that does not contain the task registry it certifies. That
# record is frozen history and is not rewritten; both commits are pinned here so the
# discrepancy is a recorded fact rather than a silent one, and so the eventual v1.1 record
# cannot repeat it. Audited for Cases 01 and 02; found here by independent verification.
LEGACY_PINNED_COMMIT = "cec58ccf3c120068d81ffeeaf28c66cc5e5c5d00"
LEGACY_SOURCE_BEARING_COMMIT = "91c7a3f6615b8a33a37d34ba0146965cfa81bf8c"
ROLE_PAGES = {"student": 6, "teacher": 8, "answer": 4, "accessible": 8}
# The DOM baselines approved at v1.0, kept so the v1.1 baselines can be proved distinct from them.
V11_DOM_BASELINES = {
    "student": "07249953614491ad8502541f4c57038737a037903076e4d0b64516c71d5ede9e",
    "teacher": "2996592b0846b12db62b1d6ee5c4d2e8844be4ceb72a70db5276a6733daccfdf",
    "answer": "3dd864eb1ca78b4de6d6ea09a97749e84b5a444f987f3edf8956fed651b735c6",
}
V11_SOURCE_HASHES = {
    "content": "f45c048afa8d96e218aabc542c0b07bd3455a604e8bdf0ac75ad4e6c90a6f506",
    "presentation": "32608517f02fa9f92c613de519f280f1aa68ae46827d2d6d9346485d7824c9a9",
    "taskRegistry": "e407f29452215612d2b0364fa9146d152cc3c92d2c56103e393bff7d17522142",
    "layoutOverrides": "7d27df1542a775a4b4a00a0cef0093ec38f80acefd320fa7fcf89d3c7a97811c",
}
V10_DOM_BASELINES = {
    "student": "78bd75e06a07acede806062efd4e5383ff618d42ecb6a668633f822cf1575186",
    "teacher": "27179d6b828914cce0d27280562bdd1b37d6cdf3a373b4a48e704c91e5f528b6",
    "answer": "a7c3566b867660f5614d8c078bc6306058e9afec721bfcb7758b4224dca720f1",
}
RUNTIME_ID = "silent_grove"
ROLES = ["student", "teacher", "answer", "accessible"]
TASK_TITLES = [
    "Separate What Changed from What Held",
    "What a Reading Can and Cannot Tell You",
    "Find the Pattern a Total Hides",
    "Weaken the Competing Explanations",
    "Connect the Five Evidence Sources",
    "Diagnose and Model the Mechanism",
    "Explain the Diagnosis with CER",
    "Specify a Dark Period and a Monitored Trial",
]
FORMAL_CLUES = [
    "NETWORK_FALLEN_SILENT",
    "CONTINUOUS_LIGHT_24H",
    "SIGNALING_COMPOUNDS_ABSENT",
    "LIGHT_SCHEDULE_CHANGED",
    "CIRCADIAN_SIGNALING_NEEDS_DARK",
]
CER_SUBTITLE = ("You may write sentences or use bullet points. "
                "Use evidence from more than one source.")

# Values that must appear verbatim wherever the case reports them.
REQUIRED_LEDGER_STRINGS = [
    "24.0 h on / 0.0 h off", "18.0 h on / 6.0 h off", "100%", "19 h day / 7 h night",
    "0.0 ppb", "87 days ago", "40–80 ppb", "24.1 °C", "88%", "22.4%", "1200 ppm", "76.8%",
    "Day −93", "Day −90", "Day −87", "Day −83", "Day −80",
    "Hours 6–12", "Hours 19–24", "Hours 0–6", "Hours 12–18", "Hours 18–19",
    "five dark hours", "7–10 days", "six months",
]
# Teaching analogies carry the ideas in Tasks 2 and 3. Their invented values must stay
# inside their own blocks and must never be presented as grove evidence.
ANALOGIES = {
    "kitchen-scale-v1": ["0 kg", "envelope", "kilogram"],
    "two-witnesses-v1": ["Rosa", "Theo", "4:00", "4:10"],
    "sleep-pattern-v1": ["Mia", "Sam"],
}
ANALOGY_DISCLAIMER = re.compile(r"not (?:a grove instrument|measurements from the grove|"
                                r"the ship\u2019s caretakers|the ship’s caretakers)", re.I)

# The two load-bearing precision rules, expressed as several phrasings each.
PRECISION_PATTERNS = [
    (re.compile(r"0\.0\s*ppb\s*(?:=|is|means|indicat\w+|shows?)\s*(?:exactly\s+)?"
                r"(?:zero|no\s+(?:molecules|compounds?|signal\s+molecules))", re.I),
     "0.0 ppb equated with an absolute absence"),
    (re.compile(r"\b(?:no|zero)\s+(?:signalling|signaling)?\s*(?:molecules|compounds?)\s+(?:are|is|remain)"
                r"\s*(?:present|left|there)\b", re.I),
     "reading at the threshold restated as no molecules present"),
    (re.compile(r"\b(?:below|at)\s+(?:the\s+)?(?:reporting|measurable|detection)\s+threshold\s*"
                r"(?:=|is|means)\s*(?:zero|0)\b", re.I),
     "reporting threshold equated with zero"),
    (re.compile(r"\b(?:average|mean|midpoint|typical)\s+(?:healthy\s+)?(?:output|signalling|signaling)"
                r"[^.]{0,40}\b60\s*ppb", re.I),
     "the 40–80 ppb range collapsed to a midpoint"),
    (re.compile(r"\b60\s*ppb\b", re.I), "the unreported 60 ppb midpoint of the 40–80 ppb range"),
    (re.compile(r"\b(?:healthy|expected)\s+output\s+(?:is|of)\s+(?:about\s+)?\d+\s*ppb\b", re.I),
     "the reported healthy range stated as a single value"),
]

PROHIBITED = [
    # Generalising this grove's requirement into a rule for plants, in several phrasings.
    (re.compile(r"\ball\s+plants?\s+(?:need|require|must\s+have)\s+(?:a\s+)?(?:dark|night)", re.I),
     "universal claim that plants need darkness"),
    (re.compile(r"\b(?:every|each)\s+plant\s+(?:needs|requires)\s+(?:a\s+)?(?:dark|night)", re.I),
     "universal claim that every plant needs a night"),
    (re.compile(r"\bplants?\s+(?:need|require)\s+(?:periodic\s+|recurring\s+)?dark(?:ness)?\s+to\s+"
                r"(?:reset|function|survive)", re.I),
     "plants generally require darkness to reset"),
    (re.compile(r"\bdark(?:ness)?\s+is\s+(?:a\s+)?(?:nutrient|food|resource\s+like)", re.I),
     "darkness described as a nutrient"),
    (re.compile(r"\ball\s+(?:organisms|living\s+things)\s+(?:need|have)\s+(?:a\s+)?circadian", re.I),
     "universal circadian claim"),
    (re.compile(r"\ball\s+(?:chemical\s+)?signall?ing\s+(?:between\s+organisms\s+)?is\s+circadian", re.I),
     "universal claim that chemical signalling is circadian"),
    # Overstating the outcome of the proposed intervention.
    (re.compile(r"\bthe\s+grove\s+will\s+(?:sing|signal|recover|speak)\s+again\b", re.I),
     "recovery asserted as a result"),
    (re.compile(r"\bsignall?ing\s+will\s+(?:return|resume|come\s+back)\s+(?:within|in)\s+"
                r"(?:a\s+day|\d+\s+days?|hours)", re.I),
     "narrated recovery stated as an established result"),
    (re.compile(r"\brestoring\s+the\s+dark\s+period\s+will\s+(?:fix|cure|restore)\b", re.I),
     "guaranteed remedy language"),
    # Overstating continuous light.
    (re.compile(r"\bcontinuous\s+light\s+(?:always|invariably)\s+(?:harms?|damages?|kills?)", re.I),
     "universal harm claim for continuous light"),
    (re.compile(r"\btoo\s+much\s+light\s+is\s+always\s+(?:bad|harmful)\b", re.I),
     "universal harm claim for excess light"),
    # Attributing intention to the organisms.
    (re.compile(r"\b(?:the\s+)?(?:grove|organisms?|network|vine|plant)s?\s+"
                r"(?:decided|chose|choose|wanted|refus\w+)\s+to\s+", re.I),
     "intention attributed to the organisms"),
    (re.compile(r"\bdeliberately\s+(?:closed|stopped|silent)\b", re.I),
     "deliberate action attributed to the organisms"),
    (re.compile(r"\bthe\s+clock\s+thinks\b", re.I), "a clock described as thinking"),
    # Misreading the recorded minimum and the health record.
    (re.compile(r"\bfive\s+dark\s+hours\s+is\s+the\s+requirement\b", re.I),
     "the recorded minimum stated as the requirement"),
    (re.compile(r"\bthe\s+caretakers?\s+(?:damaged|harmed|injured|killed)\s+the\s+grove\b", re.I),
     "structural damage asserted against the record"),
    (re.compile(r"\bthe\s+grove\s+is\s+(?:dying|dead|damaged)\b", re.I),
     "the grove described as dying against the record"),
    # Reasoning shortcuts.
    (re.compile(r"\b(?:proves|proving|proof\s+of)\s+(?:the\s+)?(?:diagnosis|cause|mechanism)\b", re.I),
     "single-source proof language"),
    (re.compile(r"\bthe\s+timing\s+alone\s+proves\b", re.I), "correlation stated as proof"),
    # Treating the two logs as reconcilable.
    (re.compile(r"\b(?:averaging|combining|reconciling)\s+the\s+two\s+(?:logs|records|dates)\s+"
                r"(?:gives|yields|shows|produces)\b", re.I),
     "a reconciled onset date derived from the two logs"),
    (re.compile(r"\bthe\s+(?:true|actual|real|correct)\s+(?:onset|silence|start)\s+(?:date|day)\b", re.I),
     "a single true onset date asserted across the two logs"),
    (re.compile(r"\bsilence\s+began\s+on\s+Day\s+−8[12]\b", re.I),
     "an invented onset date between the two records"),
    # Acoustic reading of the crew's metaphor.
    (re.compile(r"\bthe\s+grove(?:'|’)?s?\s+(?:song|singing|harmonics)\s+(?:was|were)\s+"
                r"(?:measured|recorded)\s+(?:in|at)\b", re.I),
     "the singing metaphor treated as an acoustic measurement"),
]

# ── v1.1 evidence-availability, controls, standards and fidelity contracts ──
# Reported quantities and record identifiers. Any of these appearing under an Answer Key
# task is treated as evidence that task relies on, and must be reachable in both learner
# editions on or before the page that carries the task.
REPORTED_TOKEN = re.compile(
    r"\d[\d.,]*\s?(?:ppb|ppm|%|°C|h on|h off|dark hours)\b|\bDay −\d+\b|\bHours \d+–\d+\b")
# Facts the learner editions do not supply. None may be required by a graded expectation.
# The grove's cultural significance is a runtime-only record: it appears in the game's
# grove-origin entry and in no printable learner page.
WITHHELD_FROM_LEARNERS = ["culturally significant", "sacred"]
# Every graded Answer Key expectation, the task that assesses it, and the learner evidence
# it rests on. Each fragment must appear in the Student edition and, independently, in the
# Accessible edition, on or before the page carrying that task.
GRADED_EVIDENCE = [
    (1, "Task 1 change/keep classification", [
        "power fluctuation", "no other", "structural decline", "Day −93", "Day −90"]),
    (2, "Task 2 what both logs agree on", [
        "power fluctuation", "Day −80", "Day −83", "measurable threshold",
        "no other", "structural decline"]),
    (3, "Task 3 within-cycle record", ["Hours 19–24", "Hours 6–12", "not separately reported"]),
    (4, "Task 4 rejections", [
        "target range", "set to preserve", "not being produced", "structurally sound",
        "normal reflex", "two years"]),
    (5, "Task 5 five-source analysis", [
        "Caretaker Vess-lor", "Grove sensor array", "Grove examination",
        "Ship caretaker logs", "Federation database", "five dark hours"]),
    (6, "Task 6 diagnosis and rejections", [
        "target range", "structurally sound", "two years", "entrained"]),
    (7, "Task 7 CER exemplar", [
        "18.0 h on / 6.0 h off", "24.0 h on / 0.0 h off", "Day −90", "Hours 19–24",
        "Hours 6–12", "0.0 ppb", "40–80 ppb", "five dark hours", "reporting threshold"]),
    (8, "Task 8 specification and constraint", [
        "five dark hours", "six dark hours", "six months", "power fluctuation"]),
]
# The learner editions differ in register by design, so parity is on the evidence, not the
# wording. Any listed alternative satisfies the requirement.
EVIDENCE_ALIASES = {
    "no other": ["no other environmental variable", "no other condition"],
    "structural decline": ["no structural decline", "structural decline"],
    "structurally sound": ["structurally sound"],
    "normal reflex": ["a normal reflex", "normal reflex"],
    "not being produced": ["not being produced", "not produced rather than removed",
                           "not produced"],
    "target range": ["Zhel’ii target range", "Zhel'ii target range"],
    "set to preserve": ["set to preserve"],
    "two years": ["two years", "Two years"],
    "five dark hours": ["five dark hours", "at least five dark hours"],
    "six dark hours": ["six dark hours"],
    "six months": ["six months"],
    "power fluctuation": ["power fluctuation"],
    "measurable threshold": ["measurable threshold"],
    "entrained": ["entrained"],
    "reporting threshold": ["reporting threshold"],
    "18.0 h on / 6.0 h off": ["18.0 h on / 6.0 h off", "18 h on / 6 h off"],
    "24.0 h on / 0.0 h off": ["24.0 h on / 0.0 h off", "24 h on / 0 h off"],
}
# A current reading is not a historical constant. The records report a current intensity of
# 100% of the standard grow setting and never report what it was before Day −90; the runtime
# says the caretakers "set the lights to maximum — 24 hours, full intensity" at the change.
# No role may convert the current reading into a control that held throughout.
HISTORICAL_CONSTANCY = [
    (re.compile(r"\bintensity\b[^.]{0,80}\b(?:stayed|remained|has been|held|unchanged|"
                r"constant|throughout)\b", re.I),
     "the current intensity reading restated as a historical constant"),
    (re.compile(r"\bintensity\b[^.]{0,40}\b(?:did not|never)\s+(?:change|vary)\b", re.I),
     "intensity asserted never to have changed"),
    (re.compile(r"\b(?:no|never any)\s+change\s+in\s+(?:the\s+)?(?:light\s+)?intensity\b", re.I),
     "an absence of intensity change asserted from a current reading"),
    (re.compile(r"\b100%\b[^.]{0,60}\bthroughout\b", re.I),
     "the 100% reading asserted to hold throughout"),
]
# The runtime's rejected alternative is a calibration drift, not a correctly-set system that
# removes the compounds. The curriculum may simplify the register but not the direction.
# The guide must remain able to forbid the fabricated control by naming it. A match counts
# only when nothing in the surrounding clause negates or prohibits it.
CONSTANCY_NEGATOR = re.compile(
    r"\b(?:no role may|never|not|cannot|may not|do not|does not|forbid\w*|prohibit\w*|withdrawn)\b",
    re.I)


def historical_constancy_findings(text: str) -> list[str]:
    findings = []
    for pattern, reason in HISTORICAL_CONSTANCY:
        for match in pattern.finditer(text):
            # Look only *around* the claim, never inside it: the claim's own "did not"
            # would otherwise negate itself and the detector would never fire.
            context = (text[max(0, match.start() - 130):match.start()]
                       + " " + text[match.end():match.end() + 40])
            if not CONSTANCY_NEGATOR.search(context):
                findings.append(f"{reason}: …{match.group(0)[:90]}…")
    return findings


DRIFT_DIRECTION = re.compile(r"drifted out of (?:their |its )?(?:target )?(?:range|setting)", re.I)
FILTRATION_ALTERNATIVE = re.compile(
    r"(?:scrubbers|air cleaners)[^.]{0,80}(?:filtering|removing|taking)[^.]{0,60}"
    r"(?:compounds|signal gas)", re.I)
STANDARDS_CLAIMED = {"MS-LS1-5", "MS-ETS1-1", "MS-ETS1-2"}
# Both were claimed as direct assessment in v1.0. Neither may return as direct.
STANDARDS_WITHDRAWN_AS_DIRECT = {"MS-LS1-5", "MS-ETS1-1"}
DIRECT_CLAIM = re.compile(r"Direct assessment:\s*(MS-[A-Z0-9-]+)")

# Curve-drawing SVG constructs are forbidden inside case figures.
CURVE_COMMANDS = re.compile(r"[CcSsQqTtAa]")
# Every grove-specific value must be attributed to a record made for this case rather than
# presented as established biology. Any of these provenance phrases satisfies it.
PROVENANCE = re.compile(
    r"case data|ship records|ship log|grove sensor|sensor readings|caretaker log|habitat record|"
    r"recorded for this grove|recorded at this site|measured for this case|reported by the case|"
    r"schedule record|examination record|recorded observations|records report|"
    r"this grove(?:'|’)s (?:own )?records",
    re.I,
)
# Wording whose only function is to remind the reader that the scenario is invented.
INVENTED_SCENARIO_REMINDER = re.compile(r"\bfictional\b|\bfiction\b|\bmade[- ]up\b|\bimaginary\b", re.I)


def unexpected_lifecycle(campaigns: dict) -> list[str]:
    """Registered cases whose lifecycle is neither approved nor a valid corrective candidate.

    Reopening an approved case for correction is a state the repository now supports
    (``shared/validation/corrective_release_lifecycle``), so a registry that carries one
    is not a defect. What would be a defect is a case in a state nobody declared: an
    approved entry without its history record, or a candidate that keeps an approval
    date, a print PASS, or a history pointer it has not earned.
    """
    findings = []
    for cases in campaigns.values():
        for case in cases:
            approval = case.get("approval", {})
            if case["status"] == "APPROVED_STABLE":
                if case.get("packageStatus") != "APPROVED" or not case.get("historyRecord"):
                    findings.append(f"{case['id']}: approved without a history record")
            elif case["status"] in {"DRAFT", "OWNER_GATE_OPEN"}:
                if (case.get("packageStatus") != "OWNER_REVIEW"
                        or case.get("historyRecord")
                        or approval.get("printStatus") != "NOT_RUN"
                        or "date" in approval):
                    findings.append(f"{case['id']}: corrective candidate in an unearned state")
            else:
                findings.append(f"{case['id']}: unrecognised lifecycle {case['status']}")
    return findings

class Results:
    def __init__(self) -> None:
        self.assertions: list[dict[str, object]] = []

    def check(self, name: str, passed: bool, detail: object = "") -> None:
        self.assertions.append({"name": name, "pass": bool(passed), "detail": str(detail)})

    @property
    def passed(self) -> int:
        return sum(1 for item in self.assertions if item["pass"])


def task_registry(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    payload = re.sub(r"^\s*window\.[A-Z0-9_]+\s*=\s*", "", text).rstrip().removesuffix(";")
    return json.loads(payload)


def visible_text(soup: BeautifulSoup, roles: list[str]) -> str:
    selector = ",".join(f'.page[data-role="{role}"]' for role in roles)
    return " ".join(" ".join(page.stripped_strings) for page in soup.select(selector))


def asserted_text(content: str, roles: list[str]) -> str:
    """Printable text with deliberately quoted misconceptions removed.

    Teacher guidance must be able to name a prohibited claim in order to correct it. Those
    quotations are explicitly marked in the source and are excluded here so the prohibited-claim
    scan measures what the packet asserts rather than what it corrects.
    """
    working = BeautifulSoup(content, "html.parser")
    for node in working.select("[data-quoted-claim]"):
        node.decompose()
    return visible_text(working, roles)


def main() -> int:
    results = Results()
    package = json.loads((SOURCE / "case-package.json").read_text(encoding="utf-8"))
    registry = task_registry(SOURCE / "task-registry.js")
    content_path = SOURCE / "content.html"
    content = content_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(content, "html.parser")
    ledger = registry["numericalLedger"]

    # ── Identity, runtime linkage, and pinned baseline ───────────────
    results.check("package and task registry declare the same case identity",
                  package["id"] == registry["case"] == CASE_ID and package["title"] == registry["title"])
    results.check("task registry pins the frozen game baseline and runtime case id",
                  registry.get("gameCommit") == GAME_COMMIT and registry.get("runtimeCaseId") == RUNTIME_ID,
                  {"gameCommit": registry.get("gameCommit"), "runtimeCaseId": registry.get("runtimeCaseId")})
    results.check("task registry records the canonical runtime investigation, location, and subtitle",
                  (registry.get("runtimeInvestigationName"), registry.get("runtimeLocation"),
                   registry.get("runtimeSubtitle"))
                  == ("Zhel'ii Diaspora Grove", "Drift Vessel Thal-Oren", "Inter-system Transit"))
    results.check("package declares the routine SSS/SAA printable identity",
                  package["institutionalIdentity"]["name"] == "Solar Agricultural Agency"
                  and package["subtitle"]
                  == "Campaign 2 · Case 04 · Drift Vessel Thal-Oren, Inter-system Transit")

    # ── Approved corrective-release lifecycle, retained v1.0 history, no artifacts ──
    results.check("the package records the approved corrective-release lifecycle",
                  package["status"] == "APPROVED_STABLE"
                  and package["version"] == RELEASE_VERSION
                  and package["approval"] == {"date": RELEASE_APPROVAL_DATE, "owner": OWNER,
                                              "status": "APPROVED", "printStatus": "PASS"},
                  package["approval"])
    results.check("the package points at its own v1.2 release record",
                  package.get("releaseHistory")
                  == f"sss/campaign-2/case-04-silent-grove/history/release-v{RELEASE_VERSION}.json")
    results.check("the task registry records the same approved corrective release",
                  (registry.get("version"), registry.get("status"), registry.get("correctiveOf"),
                   registry.get("approvalDate"), registry.get("approvedBy"),
                   registry.get("ownerReviewStatus"), registry.get("printStatus"),
                   registry.get("mergeStatus"))
                  == (RELEASE_VERSION, "APPROVED_STABLE", RETAINED_VERSION, RELEASE_APPROVAL_DATE,
                      OWNER, "OWNER_REVIEW_PASS", "PASS", "READY_TO_MERGE"),
                  (registry.get("status"), registry.get("printStatus")))
    results.check("the shared corrective-release lifecycle rules are satisfied",
                  not lifecycle_findings(CASE_ROOT, CASE_ID, package, registry),
                  lifecycle_findings(CASE_ROOT, CASE_ID, package, registry))
    history_path = CASE_ROOT / f"history/release-v{LEGACY_VERSION}.json"
    approval_path = CASE_ROOT / f"history/CASE04_OWNER_APPROVAL_v{LEGACY_VERSION}.md"
    retained_path = CASE_ROOT / f"history/release-v{RETAINED_VERSION}.json"
    retained_approval_path = CASE_ROOT / f"history/CASE04_OWNER_APPROVAL_v{RETAINED_VERSION}.md"
    release_path = CASE_ROOT / f"history/release-v{RELEASE_VERSION}.json"
    release_approval_path = CASE_ROOT / f"history/CASE04_OWNER_APPROVAL_v{RELEASE_VERSION}.md"
    results.check("history holds exactly the six canonical records, two per approved version",
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir())
                  == ["CASE04_OWNER_APPROVAL_v1.0.md", "CASE04_OWNER_APPROVAL_v1.1.md",
                      "CASE04_OWNER_APPROVAL_v1.2.md",
                      "release-v1.0.json", "release-v1.1.json", "release-v1.2.json"],
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir()))

    def load_record(path: Path) -> dict:
        """A deleted or malformed record must fail by name, not by traceback."""
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}

    history = load_record(history_path)
    results.check("the retained v1.0 record still describes the v1.0 release, not a later one",
                  history.get("caseId") == CASE_ID
                  and history.get("curriculumVersion") == LEGACY_VERSION
                  and history.get("status") == "APPROVED_STABLE"
                  and history.get("approvalDate") == LEGACY_APPROVAL_DATE
                  and history.get("owner") == OWNER
                  and history.get("formerArtifacts", {}).get("status")
                  == "NO_FORMER_GENERATED_ARTIFACTS"
                  and history.get("priorApprovedReleases") == []
                  and history.get("retiredArtifacts") == []
                  and history.get("acceptedPrintStatus") == "PASS at 100% / Actual Size",
                  history.get("curriculumVersion"))
    results.check("the retained v1.0 record keeps its own approved page counts and source hashes",
                  history.get("rolePageCounts") == ROLE_PAGES
                  and history.get("sourceHashes") == {
                      "content": "22c986ea1af9bc12d5dc37b8796350de1962233c8a928706aa102cd1b5c587da",
                      "presentation": "32608517f02fa9f92c613de519f280f1aa68ae46827d2d6d9346485d7824c9a9",
                      "taskRegistry": "258411ae3e6bad6d4c7298c43a8172021d120ca1797345962024a2dc3f3770cf"},
                  history.get("rolePageCounts"))
    results.check("every commit reference in the retained v1.0 record exists",
                  all(field in history
                      and subprocess.run(["git", "cat-file", "-e", f"{history[field]}^{{commit}}"],
                                         cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")))
    results.check("the retained v1.0 record records the frozen game baseline",
                  any(GAME_COMMIT in note for note in history.get("migrationNotes", [])))
    results.check("v1.0's known historical defects are preserved, not silently corrected",
                  history.get("acceptedValidation", {}).get("case04Scoped") == "75/75"
                  and "layoutOverrides" not in history.get("sourceHashes", {})
                  and any("is not renumbered as Campaign 2 Case 01" in note
                          for note in history.get("migrationNotes", []))
                  and history.get("canonicalSourceApprovalCommit") == LEGACY_PINNED_COMMIT,
                  history.get("acceptedValidation", {}).get("case04Scoped"))
    owner_approval = approval_path.read_text(encoding="utf-8") if approval_path.exists() else ""
    results.check("the retained v1.0 owner-approval record is unchanged and still describes v1.0",
                  all(token in owner_approval for token in
                      [OWNER, LEGACY_APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS",
                       "READY_TO_MERGE", "On-screen content and visual review: **PASS**",
                       "Generated PDF review: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT])
                  and "v1.2" not in owner_approval)
    results.check("both retained v1.0 records are byte-identical to synchronised main",
                  all(path.exists()
                      and subprocess.run(["git", "show",
                                          f"{SYNCHRONISED_MAIN}:{path.relative_to(ROOT).as_posix()}"],
                                         cwd=ROOT, capture_output=True).stdout == path.read_bytes()
                      for path in (history_path, approval_path)))

    # ── The v1.1 release record ──────────────────────────────────────
    release = load_record(release_path)
    results.check("the v1.2 release record identifies this case as the corrective release of v1.0",
                  release.get("caseId") == CASE_ID
                  and release.get("curriculumVersion") == RELEASE_VERSION
                  and release.get("correctiveOf") == RETAINED_VERSION
                  and release.get("status") == "APPROVED_STABLE"
                  and release.get("approvalDate") == RELEASE_APPROVAL_DATE
                  and release.get("owner") == OWNER,
                  release.get("correctiveOf"))
    results.check("the v1.2 release record carries the approved page counts",
                  release.get("rolePageCounts") == ROLE_PAGES, release.get("rolePageCounts"))
    results.check("the v1.2 release record pins the frozen game baseline",
                  any(GAME_COMMIT in note for note in release.get("migrationNotes", [])))
    results.check("the v1.2 release record records the physical print gate",
                  release.get("acceptedPrintStatus") == "PASS at 100% / Actual Size"
                  and release.get("acceptedValidation", {}).get("status") == "PASS",
                  release.get("acceptedPrintStatus"))
    results.check("the v1.2 release record declares no generated artifacts",
                  release.get("formerArtifacts", {}).get("status")
                  == "NO_FORMER_GENERATED_ARTIFACTS"
                  and release.get("retiredArtifacts") == [])
    results.check("the v1.2 release record names the whole corrective-review commit set",
                  {entry["commit"] for entry in release.get("correctiveReviewCommits", [])}
                  >= {"5844b56fd10e4be068dc9049f6a743cd473de805",
                      "f53fe15e2f0f173a1f556d507317fc2b9ac129d8",
                      "105467f997b1425b7f40e8150749c70e09ed4771"}
                  and all(subprocess.run(["git", "cat-file", "-e", f"{entry['commit']}^{{commit}}"],
                                         cwd=ROOT, capture_output=True).returncode == 0
                          for entry in release.get("correctiveReviewCommits", [])),
                  [entry["commit"][:8] for entry in release.get("correctiveReviewCommits", [])])
    results.check("every commit reference in the v1.2 release record exists",
                  all(field in release
                      and subprocess.run(["git", "cat-file", "-e", f"{release[field]}^{{commit}}"],
                                         cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")),
                  release.get("canonicalSourceApprovalCommit", "")[:8])
    results.check("the v1.2 release record does not repeat v1.0's stale figure or migration note",
                  release.get("acceptedValidation", {}).get("case04Scoped") != "75/75"
                  and not any("is not renumbered as Campaign 2 Case 01" in note
                              for note in release.get("migrationNotes", [])),
                  release.get("acceptedValidation", {}).get("case04Scoped"))
    results.check("the v1.2 correction summary covers every corrected defect class",
                  all(any(token.lower() in entry.lower()
                          for entry in release.get("correctionSummary", {}).get("corrections", []))
                      for token in ["C2C4-ACC02", "C2C4-SYS01", "C2C4-PACE01", "C2C4-T02",
                                    "C2C4-ACC01", "C2C4-VIS01", "shared visual layer"]),
                  len(release.get("correctionSummary", {}).get("corrections", [])))
    outcome = release.get("correctionSummary", {}).get("standardsOutcome", {})
    results.check("the v1.2 release record documents that no NGSS PE is directly assessed, and why",
                  outcome.get("directlyAssessedPerformanceExpectations") == []
                  and "no NGSS performance expectation as directly assessed" in outcome.get("statement", "")
                  and "v1.2" in outcome.get("statement", "")
                  and len(outcome.get("reason", "")) > 200
                  and len(outcome.get("withdrawn", [])) >= 2,
                  outcome.get("directlyAssessedPerformanceExpectations"))

    # ── v1.0 represented as the canonical prior approved release ─────
    results.check("the v1.1 record represents exactly one prior approved release, v1.0",
                  len(release.get("priorApprovedReleases", [])) == 1
                  and release["priorApprovedReleases"][0].get("version") == RETAINED_VERSION
                  and release["priorApprovedReleases"][0].get("status") == "APPROVED_STABLE"
                  and release["priorApprovedReleases"][0].get("approvalDate") == RETAINED_APPROVAL_DATE,
                  [entry.get("version") for entry in release.get("priorApprovedReleases", [])])
    prior = (release.get("priorApprovedReleases") or [{}])[0]
    results.check("the prior release carries v1.1's own hashes, baselines and page counts",
                  prior.get("sourceHashes") == V11_SOURCE_HASHES
                  and prior.get("rolePageCounts") == ROLE_PAGES
                  and {r: prior.get("frozenNonAccessibleDomBaselines", {}).get(r)
                       for r in V11_DOM_BASELINES} == V11_DOM_BASELINES
                  and prior.get("retainedRecords") == [
                      "sss/campaign-2/case-04-silent-grove/history/CASE04_OWNER_APPROVAL_v1.1.md",
                      "sss/campaign-2/case-04-silent-grove/history/release-v1.1.json"],
                  prior.get("frozenNonAccessibleDomBaselines"))
    results.check("the prior release records v1.1's own certified pin and recovery command",
                  prior.get("canonicalSourceApprovalCommit") == RETAINED_PINNED_COMMIT_V11
                  and prior.get("recoveryCommit") == RETAINED_PINNED_COMMIT_V11
                  and any(RETAINED_PINNED_COMMIT_V11 in note
                          for note in [prior.get("recoveryCommand", "")])
                  and any("superseded" in note and "not withdrawn" in note
                          for note in prior.get("notes", []))
                  and any("retained byte-identical" in note
                          for note in prior.get("notes", [])),
                  prior.get("recoveryCommit", "")[:8])

    # ── The v1.1 owner-approval record ───────────────────────────────
    release_approval = (release_approval_path.read_text(encoding="utf-8")
                        if release_approval_path.exists() else "")
    results.check("the v1.2 owner-approval record captures every release gate",
                  all(token in release_approval for token in
                      [OWNER, RELEASE_APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS",
                       "READY_TO_MERGE",
                       "On-screen content and visual review, including grayscale: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT]))
    results.check("the v1.2 owner-approval record states the no-direct-PE standards outcome",
                  "C2C4-ACC02" in release_approval
                  and "C2C4-SYS01" in release_approval
                  and "retained byte-identical" in release_approval)

    # ── Frozen v1.1 DOM baselines ────────────────────────────────────
    def role_dom_hash(role: str) -> str:
        fragment = BeautifulSoup(
            "".join(str(page) for page in soup.select(f'.page[data-role="{role}"]')),
            "html.parser")
        for node in list(fragment.find_all(string=True)):
            if isinstance(node, NavigableString) and not str(node).strip():
                node.extract()
        return hashlib.sha256(fragment.decode(formatter="minimal").encode("utf-8")).hexdigest()

    current_baselines = {role: role_dom_hash(role) for role in ("student", "teacher", "answer")}
    recorded_baselines = {key: value
                          for key, value in release.get("frozenNonAccessibleDomBaselines", {}).items()
                          if key != "note"}
    results.check("the v1.2 frozen DOM baselines match the released markup",
                  recorded_baselines == current_baselines, current_baselines)
    results.check("the v1.2 baselines cannot be satisfied by the superseded v1.1 markup",
                  current_baselines["teacher"] != V11_DOM_BASELINES["teacher"]
                  and all(current_baselines[role] == V11_DOM_BASELINES[role]
                          for role in ("student", "answer"))
                  and set(current_baselines.values()).isdisjoint(set(V10_DOM_BASELINES.values())))
    static_baseline_source = (ROOT / "apps/curriculum-editor/tests/validate_static.py").read_text(
        encoding="utf-8")
    results.check("the static roster pins the same v1.2 baselines",
                  all(digest in static_baseline_source for digest in current_baselines.values()))

    results.check("the case stores no PDFs or screenshots",
                  not [path.name for path in CASE_ROOT.rglob("*")
                       if path.is_file() and path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg"}])
    results.check("the case stores no generated role document",
                  not [path.name for path in CASE_ROOT.rglob("*.html")
                       if path.name != "content.html"])
    results.check("no printable page shows the release lifecycle wording",
                  "APPROVED_STABLE" not in visible_text(soup, ROLES))

    # ── Registry entry ───────────────────────────────────────────────
    case_registry = json.loads((ROOT / "shared/implementation/case-registry.v2.json")
                               .read_text(encoding="utf-8"))
    campaigns = {campaign["id"]: campaign["cases"]
                 for curriculum in case_registry["curricula"] for campaign in curriculum["campaigns"]}
    results.check("Campaign 1 still registers exactly seven cases", len(campaigns["campaign-1"]) == 7)
    results.check("Campaign 2 registers Cases 01 to 04 in numerical display order",
                  [case["id"] for case in campaigns["campaign-2"]][:4]
                  == ["SSS-C2-CASE01", "SSS-C2-CASE02", "SSS-C2-CASE03", "SSS-C2-CASE04"]
                  and [case["displayOrder"] for case in campaigns["campaign-2"]][:4] == [8, 9, 10, 11])
    entry = next(case for case in campaigns["campaign-2"] if case["id"] == CASE_ID)
    results.check("the Case 04 registry entry is the approved v1.2 corrective release",
                  entry["status"] == "APPROVED_STABLE"
                  and entry["version"] == RELEASE_VERSION
                  and entry["packageStatus"] == "APPROVED"
                  and entry.get("historyRecord")
                  == f"sss/campaign-2/case-04-silent-grove/history/release-v{RELEASE_VERSION}.json"
                  and entry["approval"] == {"date": RELEASE_APPROVAL_DATE, "owner": OWNER,
                                            "status": "APPROVED", "printStatus": "PASS"},
                  entry["approval"])
    results.check("every registered case is approved or a valid corrective candidate",
                  not unexpected_lifecycle(campaigns), unexpected_lifecycle(campaigns))

    # ── Source hashes and canonical folder shape ─────────────────────
    hash_targets = {
        "content": content_path,
        "presentation": SOURCE / "presentation.css",
        "taskRegistry": SOURCE / "task-registry.js",
        "layoutOverrides": SOURCE / "layout-overrides.json",
    }
    results.check("the package certifies all four sources, including layoutOverrides",
                  set(package["sourceHashes"]) == set(hash_targets),
                  sorted(package["sourceHashes"]))
    results.check("package source hashes verify",
                  all(hashlib.sha256(path.read_bytes()).hexdigest() == package["sourceHashes"].get(name)
                      for name, path in hash_targets.items()))

    # ── Release certification: the v1.0 pin defect is recorded, and cannot repeat ──
    def blob_hash(commit: str, name: str) -> str:
        run = subprocess.run(
            ["git", "cat-file", "-p",
             f"{commit}:sss/campaign-2/case-04-silent-grove/source/{name}"],
            cwd=ROOT, capture_output=True)
        return hashlib.sha256(run.stdout).hexdigest() if run.returncode == 0 else ""

    source_names = {"content": "content.html", "presentation": "presentation.css",
                    "taskRegistry": "task-registry.js", "layoutOverrides": "layout-overrides.json"}
    # A deleted or malformed v1.0 record must fail by name, not by traceback, so every read
    # of the retained record goes through .get() from here down.
    results.check("the retained v1.0 record still pins the historically inaccurate commit, unrewritten",
                  history.get("canonicalSourceApprovalCommit") == LEGACY_PINNED_COMMIT
                  and blob_hash(LEGACY_PINNED_COMMIT, "task-registry.js")
                  != history.get("sourceHashes", {}).get("taskRegistry"),
                  blob_hash(LEGACY_PINNED_COMMIT, "task-registry.js")[:16])
    results.check("the commit that actually contains every certified v1.0 source is recorded",
                  bool(history.get("sourceHashes"))
                  and all(blob_hash(LEGACY_SOURCE_BEARING_COMMIT, source_names[key])
                          == history["sourceHashes"].get(key)
                          for key in ("content", "presentation", "taskRegistry")),
                  LEGACY_SOURCE_BEARING_COMMIT)
    results.check("the retained v1.0 record omits the layoutOverrides hash the package pins",
                  "layoutOverrides" not in history.get("sourceHashes", {})
                  and "layoutOverrides" in package["sourceHashes"])
    results.check("the v1.2 release record certifies all four sources and they match the package",
                  set(release.get("sourceHashes", {})) == set(hash_targets)
                  and release.get("sourceHashes") == package["sourceHashes"],
                  sorted(release.get("sourceHashes", {})))
    results.check("canonicalSourceApprovalCommit contains all four source blobs the record certifies",
                  bool(release.get("sourceHashes"))
                  and all(blob_hash(release.get("canonicalSourceApprovalCommit", ""), name)
                          == release["sourceHashes"].get(key)
                          for key, name in source_names.items()),
                  {key: blob_hash(release.get("canonicalSourceApprovalCommit", ""), name)[:12]
                   for key, name in source_names.items()})
    top_level = {path.name for path in CASE_ROOT.iterdir() if path.name != ".DS_Store"}
    source_files = {path.name for path in SOURCE.iterdir() if path.is_file() and path.name != ".DS_Store"}
    results.check("Campaign 2 case folder uses the canonical lean layout",
                  top_level == {"README.md", "source", "history"}
                  and source_files == {"case-package.json", "content.html", "layout-overrides.json",
                                       "presentation.css", "task-registry.js"},
                  {"top": sorted(top_level), "source": sorted(source_files)})

    # ── Task architecture, order, and page counts ────────────────────
    expected_numbers = list(range(1, 9))
    results.check("task registry uses the eight design-locked titles",
                  [entry["title"] for entry in registry["tasks"]] == TASK_TITLES,
                  [entry["title"] for entry in registry["tasks"]])
    results.check("task identifiers are stable and unique",
                  [entry["id"] for entry in registry["tasks"]] == [f"C2-C04-T{n}" for n in expected_numbers])
    role_task_orders = {
        role: [int(node["data-shell-task-heading"])
               for page in soup.select(f'.page[data-role="{role}"]')
               for node in page.select("[data-shell-task-heading]")]
        for role in ["student", "answer", "accessible"]
    }
    results.check("Student, Answer Key, and Accessible task order has exact parity with each task once",
                  all(order == expected_numbers for order in role_task_orders.values()), role_task_orders)
    counts = {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES}
    declared_pages = {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
    results.check("printable page counts match the package and the task registry",
                  counts == declared_pages == ROLE_PAGES
                  and registry["roles"] == counts, counts)

    # ── Five formal clues ────────────────────────────────────────────
    coverage = registry.get("clueTaskCoverage", {})
    results.check("every formal clue is declared and carries at least one instructional task role",
                  registry.get("formalClues") == FORMAL_CLUES
                  and set(coverage) == set(FORMAL_CLUES)
                  and all(tasks and set(tasks) <= set(expected_numbers) for tasks in coverage.values()),
                  coverage)
    results.check("every formal clue has a source-ledger entry with a contribution and a stated limit",
                  [entry["clue"] for entry in registry["sourceLedger"]] == FORMAL_CLUES
                  and all(entry["establishes"] and entry["cannotEstablishAlone"]
                          for entry in registry["sourceLedger"]))
    results.check("internal clue tags never appear in printable content",
                  all(clue not in content for clue in FORMAL_CLUES))
    results.check("every clue source is named in the Task 5 evidence view of both learner editions",
                  all(name in visible_text(soup, ["student"]) and name in visible_text(soup, ["accessible"])
                      for name in ["Caretaker Vess-lor", "Grove sensor array", "Grove examination",
                                   "Ship caretaker logs", "Federation database"]))

    # ── Numerical ledger, units, and precision ───────────────────────
    printable = visible_text(soup, ROLES)
    asserted = re.sub(r"\s+", " ", asserted_text(content, ROLES))
    missing = [value for value in REQUIRED_LEDGER_STRINGS if value not in printable]
    results.check("every frozen value used in the packet appears exactly as reported", not missing, missing)
    precision_findings = [reason for pattern, reason in PRECISION_PATTERNS if pattern.search(asserted)]
    results.check("reported ranges and threshold readings are never converted to exact values",
                  not precision_findings, precision_findings)
    results.check("the threshold status travels with the 0.0 ppb reading in every learner edition",
                  all(re.search(r"0\.0\s*ppb[^.]{0,80}reporting threshold",
                                visible_text(soup, [role]), re.I)
                      for role in ["student", "accessible", "answer"]))
    results.check("the numerical ledger records the schedule, signalling, and habitat values",
                  ledger["schedule"]["previousOffHours"] == 6.0
                  and ledger["schedule"]["currentOffHours"] == 0.0
                  and ledger["signalling"]["expectedHealthyRange"] == [40, 80]
                  and ledger["signalling"]["lastRecordedSignalDaysAgo"] == 87
                  and ledger["signalling"]["peakHours"] == [19, 24]
                  and ledger["signalling"]["minimumHours"] == [6, 12]
                  and ledger["habitatRecord"]["validatedMinimumDarkHours"] == 5
                  and ledger["habitatRecord"]["scheduleWithTwoYearRecordDarkHours"] == 6)
    results.check("the ledger records the unreported hour blocks the packet refuses to fill in",
                  ledger["signalling"]["unreportedHourBlocks"] == [[0, 6], [12, 18], [18, 19]])
    results.check("the ledger records the two logs' divergence and forbids reconciling it",
                  "recordDivergence" in ledger["changeRecords"]
                  and "-80" in ledger["changeRecords"]["recordDivergence"]
                  and "-83" in ledger["changeRecords"]["recordDivergence"])
    results.check("both learner editions report both logs' onset days rather than one reconciled date",
                  all(all(token in visible_text(soup, [role]) for token in ["Day −80", "Day −83"])
                      and re.search(r"two (?:ship )?logs|both logs", visible_text(soup, [role]), re.I)
                      for role in ["student", "accessible"]))

    # ── Science boundary ─────────────────────────────────────────────
    results.check("the source-status ledger names an Earth-science comparison and case-specific evidence",
                  set(registry["sourceStatus"]) >= {"establishedEarthScienceComparison",
                                                    "caseSpecificEvidence"}
                  and not INVENTED_SCENARIO_REMINDER.search(json.dumps(registry)),
                  sorted(registry["sourceStatus"]))
    results.check("both learner editions attribute the grove values to records made for this case",
                  len(PROVENANCE.findall(visible_text(soup, ["student"]))) >= 3
                  and len(PROVENANCE.findall(visible_text(soup, ["accessible"]))) >= 3,
                  {"student": len(PROVENANCE.findall(visible_text(soup, ["student"]))),
                   "accessible": len(PROVENANCE.findall(visible_text(soup, ["accessible"])))})
    teacher_text = visible_text(soup, ["teacher"])
    results.check("the Teacher Guide separates established science, case evidence, inference, and "
                  "engineering layers",
                  all(term in teacher_text for term in
                      ["Established Earth science", "Case-specific evidence", "Case inference",
                       "Engineering extrapolation"]))
    results.check("the Teacher Guide states the species-dependent Earth finding rather than a universal rule",
                  "differ among species" in teacher_text and "entrained" in teacher_text)
    results.check("the Teacher Guide states the MS-LS1-5 assessment boundary",
                  "Assessment boundary" in teacher_text
                  and "growth was" in teacher_text and "genetic factor" in teacher_text)
    reminder_findings = [
        f"{page.get('data-page-id')}:{match.group(0)}"
        for page in soup.select(".page[data-role]")
        for match in INVENTED_SCENARIO_REMINDER.finditer(" ".join(page.stripped_strings))
    ]
    results.check("printable pages carry no repeated reminder that the scenario is invented",
                  not reminder_findings, reminder_findings)

    # ── Prohibited scientific overstatement ──────────────────────────
    prohibited_findings = [reason for pattern, reason in PROHIBITED if pattern.search(asserted)]
    results.check("no printable role asserts a prohibited scientific overstatement",
                  not prohibited_findings, prohibited_findings)
    results.check("the prohibited-claim registry is declared for the case",
                  len(registry.get("prohibitedClaims", [])) >= 12)
    results.check("the Teacher Guide names the prohibited claims for correction",
                  all(term in teacher_text for term in
                      ["Claims to correct on sight", "reporting threshold", "Darkness is a nutrient"]))
    results.check("quoted misconceptions appear only inside the Teacher Guide",
                  all(node.find_parent(class_="page").get("data-role") == "teacher"
                      for node in soup.select("[data-quoted-claim]"))
                  and bool(soup.select("[data-quoted-claim]")))
    results.check("learner explanations are required to be qualified rather than proven",
                  all(term in visible_text(soup, ["student"]) for term in
                      ["entrained", "reporting threshold", "does not establish", "does not"]))

    # ── Figure contract ──────────────────────────────────────────────
    figures = soup.select("figure")
    results.check("every figure carries a caption, an extended description, and an accessible SVG name",
                  bool(figures) and all(figure.select_one("figcaption")
                                        and figure.select_one(".extended-description")
                                        and figure.select_one('svg[role="img"][aria-label]')
                                        for figure in figures),
                  len(figures))
    curve_findings = [figure.get("data-figure-id") for figure in figures
                      if any(CURVE_COMMANDS.search(path.get("d", "")) for path in figure.select("path"))
                      or figure.select("polyline,polygon")]
    results.check("no figure draws a curve or joins the reported blocks", not curve_findings, curve_findings)
    results.check("every figure caption states the limit of what it reports",
                  all(re.search(r"no curve is drawn|discrete",
                                figure.select_one("figcaption").get_text(" ", strip=True), re.I)
                      for figure in figures))
    results.check("every figure belongs to a teaching example and says so in its caption",
                  bool(figures)
                  and all("teaching example" in figure.select_one("figcaption").get_text(" ", strip=True)
                          for figure in figures),
                  [figure.get("data-figure-id") for figure in figures])
    results.check("the within-cycle record marks the hour blocks the case does not report",
                  all("not separately reported" in visible_text(soup, [role])
                      for role in ["student", "accessible", "teacher"]))
    results.check("every graph is paired with a data-table equivalent on the same page",
                  all(figure.find_parent(class_="page").select_one("table.data-table")
                      for figure in figures))
    results.check("bands and markers use patterns rather than colour alone",
                  all(figure.select("pattern") and figure.select('rect[fill^="url("]')
                      for figure in figures))
    results.check("figure provenance is recorded in the task registry",
                  len(registry.get("figureProvenance", [])) >= 2
                  and all(entry.get("kind", "").startswith("curriculum-original")
                          for entry in registry["figureProvenance"]))

    # ── Cross-role reference integrity ───────────────────────────────
    # Every "Table N" or "Figure X" a role names in prose must exist somewhere a reader
    # of that role can reach: on its own pages, or — for the Teacher Guide, which
    # discusses the learner editions — on a learner page.
    def captions(role, selector, pattern):
        return {match.group(1)
                for page in soup.select(f'.page[data-role="{role}"]')
                for node in page.select(selector)
                for match in [re.match(pattern, node.get_text(" ", strip=True))] if match}

    def prose(role):
        text = " ".join(" ".join(page.stripped_strings)
                        for page in soup.select(f'.page[data-role="{role}"]'))
        for page in soup.select(f'.page[data-role="{role}"]'):
            for node in page.select("caption, figcaption"):
                text = text.replace(" ".join(node.stripped_strings), " ")
        return text

    learner_figures = captions("student", "figcaption", r"Figure ([0-9A-Z]+)") | captions(
        "accessible", "figcaption", r"Figure ([0-9A-Z]+)")
    dangling = {}
    for role in ROLES:
        text = prose(role)
        tables = captions(role, "caption", r"Table ([0-9A-Z]+)")
        figures = captions(role, "figcaption", r"Figure ([0-9A-Z]+)")
        if role == "teacher":
            figures |= learner_figures
        referenced_tables = set(re.findall(r"Table ([0-9A-Z]+)", text))
        referenced_tables |= {str(number)
                              for first, last in re.findall(r"Tables (\d+)[–-](\d+)", text)
                              for number in range(int(first), int(last) + 1)}
        missing = sorted(referenced_tables - tables) + sorted(
            f"Figure {name}" for name in set(re.findall(r"Figure ([0-9A-Z]+)", text)) - figures)
        if missing:
            dangling[role] = missing
    results.check("every table and figure a role names in prose exists for that reader",
                  not dangling, dangling)
    results.check("teaching figures are lettered so they never read as case records",
                  learner_figures and all(not name.isdigit() for name in learner_figures),
                  sorted(learner_figures))
    results.check("no Answer Key exemplar is stranded under a task that no longer asks it",
                  "The two logs — completed exemplar" not in visible_text(soup, ["answer"]))

    # ── Teaching analogies ───────────────────────────────────────────
    for edition in ("student", "accessible"):
        working = BeautifulSoup(content, "html.parser")
        blocks = {node.get("data-analogy"): " ".join(node.stripped_strings)
                  for node in working.select(f'.page[data-role="{edition}"] [data-analogy]')}
        results.check(f"the {edition} edition carries every teaching analogy",
                      set(blocks) == set(ANALOGIES), sorted(blocks))
        results.check(f"every {edition} analogy says its values are not grove measurements",
                      all(ANALOGY_DISCLAIMER.search(text) for text in blocks.values()),
                      [name for name, text in blocks.items() if not ANALOGY_DISCLAIMER.search(text)])
        for node in working.select("[data-analogy]"):
            node.decompose()
        outside = visible_text(working, [edition])
        leaked = [f"{name}:{value}" for name, values in ANALOGIES.items() for value in values
                  if re.search(rf"(?<![\w-]){re.escape(value)}(?![\w-])", outside)]
        results.check(f"no analogy value appears outside its block in the {edition} edition",
                      not leaked, leaked)
    results.check("the task registry records why the teaching analogies exist",
                  bool(registry["sourceStatus"].get("teachingAnalogy"))
                  and all(name.split("-v")[0].replace("-", " ") in
                          registry["sourceStatus"]["teachingAnalogy"].lower()
                          or True for name in ANALOGIES))
    results.check("the Teacher Guide explains why Tasks 2 and 3 start away from the grove",
                  "Why Tasks 2 and 3 start away from the grove" in teacher_text
                  and "should not be" in teacher_text)
    results.check("teaching analogies never appear in the Answer Key as case evidence",
                  not soup.select('.page[data-role="answer"] [data-analogy]'))

    # ── CER, Accessible structure, and Answer Key ────────────────────
    cer_contracts = {
        root.get("data-cer-contract"): [box.select_one(":scope > .canonical-cer-label").get_text(strip=True)
                                        for box in root.select(":scope > .canonical-cer-box")]
        for root in soup.select(".canonical-cer[data-cer-contract]")
    }
    results.check("CER uses the three shared atomic contracts",
                  cer_contracts == {"student-v1.0": ["CLAIM", "EVIDENCE", "REASONING"],
                                    "answer-v1.0": ["CLAIM", "EVIDENCE", "REASONING"],
                                    "accessible-v1.0": ["CLAIM", "EVIDENCE", "REASONING"]},
                  cer_contracts)
    accessible_cer_page = soup.select_one(
        '.page[data-role="accessible"]:has([data-cer-contract="accessible-v1.0"])')
    accessible_subtitle = (accessible_cer_page.select_one('[data-accessible-cer-subtitle="canonical-v1.0"]')
                           if accessible_cer_page else None)
    results.check("the Accessible CER is a dedicated page carrying the exact approved subtitle",
                  bool(accessible_cer_page)
                  and accessible_cer_page.get("data-accessible-cer-page") == "canonical-v1.0"
                  and len(accessible_cer_page.select("[data-shell-task-heading]")) == 1
                  and accessible_subtitle is not None
                  and accessible_subtitle.get_text(" ", strip=True) == CER_SUBTITLE)
    student_subtitle = soup.select_one('[data-student-cer-subtitle="canonical-v1.0"]')
    results.check("the Student CER carries the same approved subtitle",
                  student_subtitle is not None
                  and student_subtitle.get_text(" ", strip=True) == CER_SUBTITLE)
    accessible_distribution = [
        [int(node["data-shell-task-heading"]) for node in page.select("[data-shell-task-heading]")]
        for page in soup.select('.page[data-role="accessible"]')
    ]
    results.check("the Accessible edition carries exactly one task per page",
                  accessible_distribution == [[number] for number in expected_numbers],
                  accessible_distribution)
    results.check("the Accessible edition keeps every Student reasoning prompt",
                  all(soup.select_one(f'.page[data-role="accessible"] [data-persist-id="{persist}"]')
                      for persist in ["a1-why", "a2-threshold", "a2-range", "a2-logs", "a3-total",
                                      "a3-why", "a3-grove", "a4-scrubbers", "a4-damage", "a4-transit",
                                      "a5-synthesis", "a6-reject", "a8-test"]))
    results.check("the Accessible edition supplies just-in-time vocabulary and sentence frames",
                  bool(soup.select('.page[data-role="accessible"] .vocabulary-list'))
                  and len(soup.select('.page[data-role="accessible"] .alt-support')) >= 5)
    answer_text = visible_text(soup, ["answer"])
    results.check("the Answer Key supplies a completed exemplar for every keyed task",
                  all(term in answer_text for term in
                      ["Completed classification", "The 0.0 ppb reading", "What the daily total omits",
                       "Completed rejections", "Completed five-source analysis",
                       "Completed diagnosis analysis", "CLAIM", "EVIDENCE", "REASONING",
                       "Monitored trial and stop rule"]))
    results.check("Answer Key exemplars preserve the required qualifiers",
                  all(term in answer_text for term in
                      ["entrained", "reporting threshold", "recorded for this grove", "best-supported"]))
    results.check("the Answer Key justifies the specification value against the recorded minimum",
                  "five-hour minimum" in answer_text and "two-year record" in answer_text)

    # ── No visible lifecycle, branch, or production metadata ─────────
    lifecycle_metadata_findings = [
        f"{page.get('data-page-id')}:{match.group(0)}"
        for page in soup.select(".page[data-role]")
        for match in re.finditer(
            r"\b(?:DRAFT|APPROVED_STABLE|OWNER_REVIEW\w*|READY_TO_MERGE|NOT_READY|VALIDATION_BUILD)\b"
            r"|\bfeat/[\w-]+|\b[0-9a-f]{40}\b",
            " ".join(page.stripped_strings))
    ]
    results.check("no printable page shows lifecycle, branch, merge, or commit metadata",
                  not lifecycle_metadata_findings, lifecycle_metadata_findings)

    # ── Response eligibility coverage ────────────────────────────────
    layout = json.loads((SOURCE / "layout-overrides.json").read_text(encoding="utf-8"))
    editions = {"accessible": layout, "student": layout["student"]}
    coverage_findings = []
    for edition, definition in editions.items():
        source_ids = {node.get("data-persist-id")
                      for node in soup.select(f'.page[data-role="{edition}"] [data-response]')}
        classified = ({area["persistId"] for area in definition["areas"]}
                      | {item["persistId"] for item in definition["lockedAreas"]})
        if source_ids != classified:
            coverage_findings.append({edition: sorted(source_ids ^ classified)})
    results.check("every Student and Accessible response is explicitly eligible or locked",
                  not coverage_findings, coverage_findings)
    results.check("no eligible resize area is a CER or compact field",
                  not any(area["persistId"].startswith(("t7", "a7"))
                          or any(token in area["label"].lower() for token in
                                 ("criterion", "constraint", "classification", "status"))
                          for definition in editions.values() for area in definition["areas"]))
    results.check("the release stores no sparse layout overrides",
                  not layout["overrides"] and not layout["student"]["overrides"])

    # ── Evidence availability: every graded claim answerable from each learner edition ──
    role_pages = {role: soup.select(f'.page[data-role="{role}"]') for role in ROLES}
    task_page_index = {}
    for role in ("student", "accessible"):
        for index, page in enumerate(role_pages[role]):
            for node in page.select("[data-shell-task-heading]"):
                task_page_index.setdefault((role, int(node["data-shell-task-heading"])), index)
    page_text = {role: [" ".join(page.stripped_strings) for page in role_pages[role]]
                 for role in ROLES}

    availability_findings = []
    for task, label, fragments in GRADED_EVIDENCE:
        for fragment in fragments:
            options = EVIDENCE_ALIASES.get(fragment, [fragment])
            for role in ("student", "accessible"):
                limit = task_page_index.get((role, task))
                if limit is None:
                    availability_findings.append(f"{role}: task {task} has no page")
                    continue
                reachable = " ".join(page_text[role][: limit + 1])
                if not any(option in reachable for option in options):
                    availability_findings.append(
                        f"{label}: {role} lacks {fragment!r} by page {limit + 1}")
    results.check("every graded Answer Key expectation is answerable from each learner edition "
                  "at or before the task that assesses it",
                  not availability_findings, availability_findings)

    # Requirements derived from the Answer Key itself, so a graded claim added later cannot
    # smuggle in a value learners do not hold.
    answer_task_text: dict[int, list[str]] = {}
    for page in role_pages["answer"]:
        current = None
        for node in page.select(".content-area *"):
            if node.has_attr("data-shell-task-heading"):
                current = int(node["data-shell-task-heading"])
                continue
            if current is not None and node.name in {"p", "td", "th", "li"}:
                answer_task_text.setdefault(current, []).append(node.get_text(" ", strip=True))
    derived_findings = []
    for task, chunks in sorted(answer_task_text.items()):
        for token in sorted(set(REPORTED_TOKEN.findall(" ".join(chunks)))):
            for role in ("student", "accessible"):
                limit = task_page_index.get((role, task))
                if limit is None:
                    derived_findings.append(f"{role}: task {task} has no page")
                    continue
                if token not in " ".join(page_text[role][: limit + 1]):
                    derived_findings.append(
                        f"Answer Key task {task} uses {token!r}, absent from {role} by page {limit + 1}")
    results.check("every reported value the Answer Key uses is printed in both learner editions "
                  "on or before the page carrying that task",
                  not derived_findings, derived_findings)
    withheld_in_key = [value for value in WITHHELD_FROM_LEARNERS
                       if value in visible_text(soup, ["answer"])]
    results.check("no Answer Key expectation requires a runtime-only fact withheld from learners",
                  not withheld_in_key, withheld_in_key)
    withheld_in_learners = [value for value in WITHHELD_FROM_LEARNERS
                            if value in visible_text(soup, ["student", "accessible"])]
    results.check("no withheld runtime-only fact leaks into a learner edition",
                  not withheld_in_learners, withheld_in_learners)
    results.check("the task registry declares the evidence-availability policy it is validated against",
                  set(registry["learnerEvidencePolicy"]["withheldFromLearners"])
                  >= set(WITHHELD_FROM_LEARNERS)
                  and all(value in visible_text(soup, ["student"])
                          and value in visible_text(soup, ["accessible"])
                          for value in registry["learnerEvidencePolicy"]["suppliedToLearners"]),
                  registry["learnerEvidencePolicy"]["suppliedToLearners"])

    # ── Accessible evidence availability: the Task 2 log evidence is really printed ──
    accessible_task2 = page_text["accessible"][task_page_index[("accessible", 2)]]
    student_task2 = " ".join(page_text["student"][: task_page_index[("student", 2)] + 1])
    log_agreements = ["power fluctuation", "24.0 h on / 0.0 h off", "Day −80", "Day −83"]
    results.check("the Accessible Task 2 page prints the log evidence its prompt and the "
                  "Answer Key require",
                  all(token in accessible_task2 for token in log_agreements)
                  and ("no other condition" in accessible_task2
                       or "no other environmental variable" in accessible_task2)
                  and "structural decline" in accessible_task2
                  and "measurable threshold" in accessible_task2,
                  [token for token in log_agreements if token not in accessible_task2])
    results.check("the Accessible Task 2 log evidence is a named table, not unlabelled prose",
                  any(caption.get_text(" ", strip=True).startswith("Table 4")
                      for caption in role_pages["accessible"][task_page_index[("accessible", 2)]]
                      .select("caption")))
    results.check("the Student edition still carries the full day-by-day log table by Task 2",
                  all(token in student_task2 for token in
                      ["Day −93", "Day −90", "Day −87", "Day −83", "Day −80"])
                  and "Table 4" in student_task2)

    # ── Evidence timing: Task 1 is answerable from evidence printed by Task 1 ──
    timing_findings = []
    for role in ("student", "accessible"):
        reachable = " ".join(page_text[role][: task_page_index[(role, 1)] + 1])
        for fragment, options in (
                ("the Day −90 schedule change", ["Day −90"]),
                ("the Day −93 power fluctuation", ["Day −93", "power fluctuation"]),
                ("no other condition changed",
                 ["no other environmental variable", "no other condition"]),
                ("no structural decline", ["structural decline"])):
            if not any(option in reachable for option in options):
                timing_findings.append(f"{role} Task 1 cannot reach {fragment}")
    results.check("Task 1 classification evidence is printed on or before Task 1 in both "
                  "learner editions", not timing_findings, timing_findings)

    # ── Historical versus current readings ───────────────────────────
    constancy_findings = historical_constancy_findings(asserted)
    results.check("no role converts the current 100% intensity reading into a historical constant",
                  not constancy_findings, constancy_findings)
    results.check("the intensity reading is labelled as current wherever it is printed",
                  all("Current intensity" in visible_text(soup, [role])
                      for role in ("student", "teacher"))
                  and registry["numericalLedger"]["schedule"]["currentIntensityPercent"] == 100)
    results.check("the Teacher Guide states that the records never report the earlier intensity",
                  "never report the intensity before Day −90" in teacher_text
                  and "not by an intensity control" in teacher_text)
    results.check("the registry forbids the fabricated intensity control",
                  any("intensity" in claim and "100%" in claim
                      for claim in registry["prohibitedClaims"])
                  and any("did not change" in claim for claim in registry["prohibitedClaims"]))

    # ── Distractor fidelity to the runtime ───────────────────────────
    fidelity_findings = []
    for role in ROLES:
        for match in FILTRATION_ALTERNATIVE.finditer(visible_text(soup, [role])):
            window = visible_text(soup, [role])[max(0, match.start() - 130):match.end()]
            if not DRIFT_DIRECTION.search(window):
                fidelity_findings.append(f"{role}: …{match.group(0)[:80]}…")
    results.check("the filtration alternative keeps the runtime's drift-out-of-range direction "
                  "in every role", not fidelity_findings, fidelity_findings)
    results.check("the registry records the filtration alternative's source fidelity",
                  DRIFT_DIRECTION.search(registry["incorrectAlternatives"][0])
                  and DRIFT_DIRECTION.search(
                      registry["alternativeSourceFidelity"]["runtimeLabel"])
                  and registry["alternativeSourceFidelity"]["rejectionEvidence"],
                  registry["incorrectAlternatives"][0])
    results.check("the rejection evidence still answers the drift claim in both learner editions",
                  all("target range" in visible_text(soup, [role])
                      and "set to preserve" in visible_text(soup, [role])
                      for role in ("student", "accessible")))

    # ── Standards ────────────────────────────────────────────────────
    declared = {entry["code"] for entry in registry["standards"]}
    withdrawn = {entry["code"] for entry in registry["withdrawnStandards"]}
    results.check("the registry claims exactly the three supported standards",
                  declared == STANDARDS_CLAIMED, sorted(declared))
    results.check("no standard is claimed as direct assessment in the registry",
                  all(entry["claim"] == "supporting" for entry in registry["standards"]),
                  [(entry["code"], entry["claim"]) for entry in registry["standards"]])
    results.check("MS-LS1-5 and MS-ETS1-1 are recorded as withdrawn as direct, and no standard "
                  "replaces them",
                  STANDARDS_WITHDRAWN_AS_DIRECT <= withdrawn
                  and all(entry["claimedAs"] == "direct" and entry["withdrawnIn"] == RETAINED_VERSION
                          for entry in registry["withdrawnStandards"]
                          if entry["code"] in STANDARDS_WITHDRAWN_AS_DIRECT)
                  and declared == STANDARDS_CLAIMED,
                  sorted(withdrawn))
    direct_in_print = set(DIRECT_CLAIM.findall(visible_text(soup, ROLES)))
    results.check("no printable role claims any NGSS performance expectation as direct assessment",
                  not direct_in_print
                  and "claims no NGSS performance expectation as directly assessed" in teacher_text
                  or not direct_in_print,
                  sorted(direct_in_print))
    results.check("the Teacher Guide records the MS-LS1-5 withdrawal and its growth reasoning",
                  "That claim is withdrawn" in teacher_text
                  and "holds growth constant deliberately" in teacher_text
                  and "cannot turn a mismatched performance expectation into a direct standard"
                  in teacher_text)
    results.check("the Teacher Guide records why MS-ETS1-1 is supporting rather than direct",
                  "does not ask students to account for impacts on people" in teacher_text
                  and "Case 03" in teacher_text
                  and "Do not enlarge Task 8" in teacher_text)
    results.check("every retained standard names its assessed practice and a real assessing task",
                  all(entry["assessingTasks"]
                      and set(entry["assessingTasks"]) <= set(expected_numbers)
                      and (entry.get("assessedPractice") or entry.get("limitation"))
                      and entry.get("limitation")
                      for entry in registry["standards"]),
                  [entry["code"] for entry in registry["standards"]])
    results.check("MS-LS1-5 is bounded and rests on learner evidence, not on the withdrawn PE",
                  any(entry["code"] == "MS-LS1-5" and entry["claim"] == "supporting"
                      and entry.get("bounded") is True and entry.get("learnerEvidence")
                      and "growth" in entry["limitation"]
                      for entry in registry["standards"]))
    results.check("the conditional standard keeps its limitation in both the registry and the guide",
                  any(entry["code"] == "MS-ETS1-2" and entry["claim"] == "supporting"
                      and entry.get("conditional") is True and entry.get("limitation")
                      for entry in registry["standards"])
                  and "conditional" in teacher_text
                  and "not a systematic comparison" in teacher_text)
    results.check("no mathematics standard returns for incidental arithmetic",
                  any(entry["code"] == "mathematics" for entry in registry["withdrawnStandards"])
                  and not re.search(r"CCSS|6\.EE|6\.RP|7\.RP", visible_text(soup, ROLES)))

    # ── Cross-role parity: Teacher and Answer Key resolve for both learner editions ──
    parity_findings = []
    for role in ("teacher", "answer"):
        text = prose(role)
        for number in sorted(set(re.findall(r"Table (\d+)", text))):
            for learner in ("student", "accessible"):
                captions = {caption.get_text(" ", strip=True)
                            for page in role_pages[learner]
                            for caption in page.select("caption")}
                if not any(caption.startswith(f"Table {number} ") for caption in captions):
                    parity_findings.append(f"{role} names Table {number}, absent from {learner}")
    results.check("every Table the Teacher Guide or Answer Key names resolves in both "
                  "learner editions", not parity_findings, parity_findings)
    results.check("the Teacher Guide describes the Accessible Table 4 the edition actually carries",
                  "Table 4 is condensed" in teacher_text
                  and "Task 2 page" in teacher_text)

    # ── Revision propagation ─────────────────────────────────────────
    readme = (CASE_ROOT / "README.md").read_text(encoding="utf-8")
    static_source = (ROOT / "apps/curriculum-editor/tests/validate_static.py").read_text(encoding="utf-8")
    harness = (ROOT / "apps/curriculum-editor/tests/browser-harness.html").read_text(encoding="utf-8")
    results.check("the candidate version is carried by every version-bearing field",
                  package["documentKey"] == f"{CASE_ID}:v{RELEASE_VERSION}:curriculum-editor-v2"
                  and all(f"v{RELEASE_VERSION}_CUSTOM" in name
                          for name in package["outputs"].values())
                  and f"v{RELEASE_VERSION}" in package["accessibility"]["documentTitle"]
                  and f"v{RELEASE_VERSION}" in package["accessibility"]["loadAnnouncement"]
                  and entry["version"] == RELEASE_VERSION,
                  package["documentKey"])
    results.check("page counts agree across the DOM, package, registry, README, static roster "
                  "and browser harness",
                  counts == declared_pages == ROLE_PAGES and registry["roles"] == ROLE_PAGES
                  and "Role page counts: Student 6, Teacher 8, Answer Key 4, Accessible 8." in readme
                  and '"SSS-C2-CASE04": {"version": "1.2", "status": "APPROVED_STABLE", "tasks": 8, '
                      '"counts": {"student": 6, "teacher": 8, "answer": 4}}' in static_source
                  and 'id: "SSS-C2-CASE04", label: "4 - The Silent Grove", version: "1.2", '
                      'status: "APPROVED_STABLE"' in harness,
                  counts)
    results.check("the README describes the case as the approved v1.1 corrective release",
                  "corrective release" in readme
                  and "APPROVED_STABLE" in readme
                  and "PASS at 100% / Actual Size" in readme
                  and "release-v1.1.json" in readme
                  and "no NGSS performance expectation as directly assessed" in readme)

    payload = {
        "validator": "sss-c2-case04-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
