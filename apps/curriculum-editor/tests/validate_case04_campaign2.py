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

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[3]
CASE_ID = "SSS-C2-CASE04"
CASE_ROOT = ROOT / "sss/campaign-2/case-04-silent-grove"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
RELEASE_VERSION = "1.0"
APPROVAL_DATE = "2026-08-05"
OWNER = "Nate / Owner"
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

    # ── Approved lifecycle, release history, and no artifacts ────────
    results.check("the package records the approved release lifecycle",
                  package["status"] == "APPROVED_STABLE" and package["version"] == RELEASE_VERSION
                  and package["approval"] == {"date": APPROVAL_DATE, "owner": OWNER,
                                              "status": "APPROVED", "printStatus": "PASS"},
                  package["approval"])
    results.check("the task registry records the same approved release lifecycle",
                  (registry.get("version"), registry.get("status"), registry.get("approvalDate"),
                   registry.get("approvedBy"), registry.get("ownerReviewStatus"),
                   registry.get("mergeStatus"))
                  == (RELEASE_VERSION, "APPROVED_STABLE", APPROVAL_DATE, OWNER,
                      "OWNER_REVIEW_PASS", "READY_TO_MERGE"))
    history_path = CASE_ROOT / "history/release-v1.0.json"
    approval_path = CASE_ROOT / "history/CASE04_OWNER_APPROVAL_v1.0.md"
    results.check("the approved package names exactly one retained release-history record",
                  package.get("releaseHistory") == history_path.relative_to(ROOT).as_posix()
                  and sorted(path.name for path in (CASE_ROOT / "history").iterdir())
                  == ["CASE04_OWNER_APPROVAL_v1.0.md", "release-v1.0.json"])
    history = json.loads(history_path.read_text(encoding="utf-8"))
    results.check("the release history records a native release with no former generated artifacts",
                  history["caseId"] == CASE_ID and history["curriculumVersion"] == RELEASE_VERSION
                  and history["status"] == "APPROVED_STABLE"
                  and history["approvalDate"] == APPROVAL_DATE and history["owner"] == OWNER
                  and history["formerArtifacts"]["status"] == "NO_FORMER_GENERATED_ARTIFACTS"
                  and history["priorApprovedReleases"] == [] and history["retiredArtifacts"] == []
                  and history["acceptedPrintStatus"] == "PASS at 100% / Actual Size")
    results.check("the release history page counts match the approved release",
                  history["rolePageCounts"] == {"student": 6, "teacher": 8, "answer": 4,
                                                "accessible": 8})
    results.check("the release history pins the source hashes it was approved at",
                  all(history["sourceHashes"][name] == package["sourceHashes"][name]
                      for name in ("content", "presentation", "taskRegistry")))
    results.check("every commit reference in the release history exists",
                  all(subprocess.run(["git", "cat-file", "-e", f"{history[field]}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")))
    results.check("the release history records the frozen game baseline",
                  any(GAME_COMMIT in note for note in history["migrationNotes"]))
    results.check("the release history explains the six-page Student edition",
                  any("six pages" in note for note in history["migrationNotes"]))
    owner_approval = approval_path.read_text(encoding="utf-8")
    results.check("the owner approval record captures every release gate and the no-artifact decision",
                  all(token in owner_approval for token in
                      [OWNER, APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS", "READY_TO_MERGE",
                       "On-screen content and visual review: **PASS**",
                       "Generated PDF review: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT]))
    artifacts = sorted(path.relative_to(ROOT).as_posix() for path in CASE_ROOT.rglob("*")
                       if path.is_file() and path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg"})
    results.check("the case stores no PDFs or screenshots", not artifacts, artifacts)
    generated = sorted(path.name for path in CASE_ROOT.rglob("*.html") if path.name != "content.html")
    results.check("the case stores no generated role document", not generated, generated)
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
    results.check("the Case 04 registry entry is an approved release with a history record",
                  entry["status"] == "APPROVED_STABLE" and entry["packageStatus"] == "APPROVED"
                  and entry.get("historyRecord")
                  == "sss/campaign-2/case-04-silent-grove/history/release-v1.0.json"
                  and entry["approval"] == {"date": APPROVAL_DATE, "owner": OWNER,
                                            "status": "APPROVED", "printStatus": "PASS"})
    # Every case registered at the time Case 04 was approved must stay approved. Cases registered
    # afterwards are allowed to be unreleased drafts; naming them here keeps this assertion a
    # regression guard on the eleven approved packages rather than a bar on new work.
    unreleased = {"SSS-C2-CASE05"}
    results.check("every case approved at this release remains APPROVED_STABLE",
                  all(case["status"] == "APPROVED_STABLE"
                      for cases in campaigns.values() for case in cases
                      if case["id"] not in unreleased),
                  [case["id"] for cases in campaigns.values() for case in cases
                   if case["id"] not in unreleased and case["status"] != "APPROVED_STABLE"])

    # ── Source hashes and canonical folder shape ─────────────────────
    hash_targets = {
        "content": content_path,
        "presentation": SOURCE / "presentation.css",
        "taskRegistry": SOURCE / "task-registry.js",
        "layoutOverrides": SOURCE / "layout-overrides.json",
    }
    results.check("package source hashes verify",
                  all(hashlib.sha256(path.read_bytes()).hexdigest() == package["sourceHashes"][name]
                      for name, path in hash_targets.items()))
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
    declared = {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
    results.check("printable page counts match the package and the task registry",
                  counts == declared == {"student": 6, "teacher": 8, "answer": 4, "accessible": 8}
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
    lifecycle_findings = [
        f"{page.get('data-page-id')}:{match.group(0)}"
        for page in soup.select(".page[data-role]")
        for match in re.finditer(
            r"\b(?:DRAFT|APPROVED_STABLE|OWNER_REVIEW\w*|READY_TO_MERGE|NOT_READY|VALIDATION_BUILD)\b"
            r"|\bfeat/[\w-]+|\b[0-9a-f]{40}\b",
            " ".join(page.stripped_strings))
    ]
    results.check("no printable page shows lifecycle, branch, merge, or commit metadata",
                  not lifecycle_findings, lifecycle_findings)

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
