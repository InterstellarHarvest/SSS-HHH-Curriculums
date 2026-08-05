#!/usr/bin/env python3
"""Case-scoped assertions for SSS Campaign 2 Case 02 — The Missing Dance.

Enforces the frozen source ledger, the five-clue instructional coverage, the figure
contract, the Earth-science/case-evidence boundary, and the prohibited scientific
overstatements against the printable content of every role.

Two distinctions carry this case, and most of the patterns below exist to protect them.
The anther cone's pores are already present, so nothing opens, unseals or is blocked and
the pollen is retained rather than trapped. And 124 Hz is where the strongest release was
recorded for this species, never a sufficient setting on its own.
"""

from __future__ import annotations

import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[3]
CASE_ID = "SSS-C2-CASE02"
CASE_ROOT = ROOT / "sss/campaign-2/case-02-missing-dance"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
RELEASE_VERSION = "1.0"
APPROVAL_DATE = "2026-08-05"
RUNTIME_ID = "missing_dance"
ROLES = ["student", "teacher", "answer", "accessible"]
TASK_TITLES = [
    "Rule Things Out",
    "Shake, Don't Touch",
    "Look Inside the Flower",
    "Ask Without Asking",
    "Connect the Five Evidence Sources",
    "Diagnose and Reject Alternatives",
    "Explain the Diagnosis with CER",
    "Specify a Safe Trial",
]
FORMAL_CLUES = [
    "LYREFLOWER_BUDS_ABORT",
    "NO_ACOUSTIC_TRIGGER",
    "POLLEN_RETAINED",
    "HAND_POLLINATION_FAILED",
    "BUZZ_POLLINATION_ACOUSTIC",
]
ACCESSIBLE_CER_SUBTITLE = ("You may write sentences or use bullet points. "
                           "Use evidence from more than one source.")

REQUIRED_LEDGER_STRINGS = [
    "22.1 °C", "62%", "6.8", "420 ppm", "78.1%", "1.01 atm",
    "98%", "0.0 m/s", "28 dB", "20–200 Hz", "100–150 Hz", "124 Hz", "14h/10h",
]

PROHIBITED = [
    (re.compile(r"\bpores?\s+(?:open|opens|opened|unseal|unseals|unblock|unblocks)\b", re.I),
     "the pores described as opening, unsealing or unblocking"),
    (re.compile(r"\bsealed\s+pores?\b", re.I), "the pores described as sealed"),
    (re.compile(r"\b(?:pollen|pores?)\s+(?:is|are|was|were)\s+block(?:ed|ing)\b", re.I),
     "the pollen or pores asserted to be blocked"),
    (re.compile(r"\bmagic\s+frequency\b", re.I), "124 Hz described as a magic frequency"),
    (re.compile(r"\b124\s*Hz\s+(?:is\s+)?(?:all\s+(?:you|that)|enough|sufficient)\b", re.I),
     "124 Hz presented as sufficient on its own"),
    (re.compile(r"\bhoneybees?\s+(?:buzz[- ]?pollinat|sonicat|perform\s+floral)", re.I),
     "honeybees said to perform floral buzzing"),
    (re.compile(r"\bonly\s+bumblebees\b", re.I), "floral buzzing limited to bumblebees"),
    (re.compile(r"\b(?:Earth|all)\s+flowers?\s+respond[^.]{0,30}\b124\b", re.I),
     "the 124 Hz figure generalised to Earth flowers"),
    (re.compile(r"\bflower\s+(?:hears|listens|is\s+listening)\b", re.I),
     "the flower described as hearing or listening"),
    (re.compile(r"\bguarantee(?:d|s)?\s+(?:to\s+)?(?:work|fix|restore|succeed)\b", re.I),
     "a remedy presented as guaranteed"),
    (re.compile(r"\b(?:proves|proving|proof\s+of)\s+(?:the\s+)?(?:diagnosis|cause)\b", re.I),
     "single-source proof language"),
    (re.compile(r"\bresearcher\s+(?:was\s+)?(?:hiding|withholding|keeping\s+a\s+secret)\b", re.I),
     "the cultural constraint described as secrecy"),
    (re.compile(r"\b(?:plant|flower)\s+(?:is|was)\s+(?:sick|diseased|unhealthy)\b", re.I),
     "the plant asserted to be unhealthy"),
]
CURVE_COMMANDS = re.compile(r"[CcSsQqTtAa]")
PROVENANCE = re.compile(
    r"in this case|for this case|this garden|garden record|specimen record|sensor array|"
    r"the case reports|as reported|recorded in this|the record reports",
    re.I,
)
INVENTED_SCENARIO_REMINDER = re.compile(r"\bfictional\b|\bfiction\b", re.I)


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
    """Printable text with enumerated and quoted claims removed.

    The packet must be able to list an alternative in order to reject it, and the Teacher
    Guide must be able to name a misconception in order to forbid it. Both are marked in
    the source, so the scan measures what the packet asserts rather than what it corrects.
    """
    working = BeautifulSoup(content, "html.parser")
    for node in working.select("[data-quoted-claim], [data-candidate-claim]"):
        node.decompose()
    return visible_text(working, roles)


def main() -> int:
    results = Results()
    package = json.loads((SOURCE / "case-package.json").read_text(encoding="utf-8"))
    registry = task_registry(SOURCE / "task-registry.js")
    content_path = SOURCE / "content.html"
    content = content_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(content, "html.parser")

    # ── Identity and runtime linkage ─────────────────────────────────
    results.check("package and task registry declare the same case identity",
                  package["id"] == registry["case"] == CASE_ID and package["title"] == registry["title"])
    results.check("task registry pins the frozen game baseline and runtime case id",
                  registry.get("gameCommit") == GAME_COMMIT and registry.get("runtimeCaseId") == RUNTIME_ID,
                  {"gameCommit": registry.get("gameCommit"), "runtimeCaseId": registry.get("runtimeCaseId")})
    results.check("the package records the runtime identity the case was authored against",
                  (registry.get("runtimeInvestigationName"), registry.get("runtimeLocation"),
                   registry.get("runtimeSubtitle"))
                  == ("Ares Botanical Garden", "Olympia District", "Mars")
                  and package["location"] == "Ares Botanical Garden")
    results.check("package declares the routine SSS/SAA printable identity",
                  package["institutionalIdentity"]["name"] == "Solar Agricultural Agency"
                  and package["subtitle"] == "Campaign 2 · Case 02 · Olympia District, Mars")

    # ── Approved lifecycle ───────────────────────────────────────────
    results.check("the package records the approved release lifecycle",
                  package["status"] == "APPROVED_STABLE"
                  and package["version"] == RELEASE_VERSION
                  and package["approval"] == {"date": APPROVAL_DATE, "owner": "Nate / Owner",
                                              "status": "APPROVED", "printStatus": "PASS"},
                  package["approval"])
    results.check("the task registry records the same approved release lifecycle",
                  (registry.get("version"), registry.get("status"), registry.get("ownerReviewStatus"),
                   registry.get("mergeStatus"), registry.get("approvalDate"), registry.get("approvedBy"))
                  == (RELEASE_VERSION, "APPROVED_STABLE", "OWNER_REVIEW_PASS", "READY_TO_MERGE",
                      APPROVAL_DATE, "Nate / Owner"))
    history_path = CASE_ROOT / "history/release-v1.0.json"
    approval_path = CASE_ROOT / "history/CASE02_OWNER_APPROVAL_v1.0.md"
    results.check("the approved package names exactly one retained release-history record",
                  package.get("releaseHistory") == history_path.relative_to(ROOT).as_posix()
                  and sorted(path.name for path in (CASE_ROOT / "history").iterdir())
                  == ["CASE02_OWNER_APPROVAL_v1.0.md", "release-v1.0.json"])
    history = json.loads(history_path.read_text(encoding="utf-8"))
    results.check("the release history records a native release with no former generated artifacts",
                  history["caseId"] == CASE_ID and history["curriculumVersion"] == RELEASE_VERSION
                  and history["status"] == "APPROVED_STABLE" and history["approvalDate"] == APPROVAL_DATE
                  and history["formerArtifacts"]["status"] == "NO_FORMER_GENERATED_ARTIFACTS"
                  and history["priorApprovedReleases"] == [] and history["retiredArtifacts"] == []
                  and history["acceptedPrintStatus"] == "PASS at 100% / Actual Size")
    results.check("the release history page counts and source hashes match the approved package",
                  history["rolePageCounts"] == {"student": 5, "teacher": 8, "answer": 4, "accessible": 8}
                  and all(history["sourceHashes"][n] == package["sourceHashes"][n]
                          for n in ("content", "presentation", "taskRegistry")))
    results.check("every commit reference in the release history exists",
                  all(subprocess.run(["git", "cat-file", "-e", f"{history[field]}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")))
    results.check("the release history records the frozen game baseline and the retained case numbers",
                  any(GAME_COMMIT in note for note in history["migrationNotes"])
                  and any("keeps its runtime case number" in note for note in history["migrationNotes"]))
    owner_approval = approval_path.read_text(encoding="utf-8")
    results.check("the owner approval record captures every release gate and the no-artifact decision",
                  all(token in owner_approval for token in
                      ["Nate / Owner", APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS",
                       "READY_TO_MERGE", "On-screen content and visual review: **PASS**",
                       "Generated PDF review: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT]))
    results.check("no generated release artifact is stored beside the approved case",
                  not [path.name for path in CASE_ROOT.rglob("*")
                       if path.is_file() and path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".html"}
                       and path.name != "content.html"])
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

    # ── Task architecture and cross-role parity ──────────────────────
    results.check("task registry uses the eight design-locked titles",
                  [entry["title"] for entry in registry["tasks"]] == TASK_TITLES,
                  [entry["title"] for entry in registry["tasks"]])
    expected_numbers = list(range(1, 9))
    role_task_orders = {
        role: [int(node["data-shell-task-heading"])
               for page in soup.select(f'.page[data-role="{role}"]')
               for node in page.select("[data-shell-task-heading]")]
        for role in ["student", "answer", "accessible"]
    }
    results.check("Student, Answer Key, and Accessible task order has exact parity with each task once",
                  all(order == expected_numbers for order in role_task_orders.values()), role_task_orders)
    results.check("task identifiers are stable and unique",
                  [entry["id"] for entry in registry["tasks"]] == [f"C2-C02-T{n}" for n in expected_numbers])
    results.check("role page counts agree between the package and the task registry",
                  registry["roles"] == {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
                  and {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES} == registry["roles"],
                  registry["roles"])

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
                      for name in ["Researcher Miran-sel", "Garden sensor array", "Lyreflower specimen",
                                   "Garden records", "Federation database"]))

    # ── Evidence values ──────────────────────────────────────────────
    printable = visible_text(soup, ROLES)
    asserted = re.sub(r"\s+", " ", asserted_text(content, ROLES))
    # A prohibited claim can appear inside a sentence that forbids it, which is how the packet rules
    # the claim out. The scan below therefore measures affirmative assertions only.
    negation = re.compile(r"\b(?:not|never|cannot|neither|nothing)\b", re.I)
    affirmed = " ".join(part for part in re.split(r"(?<=[.!?])\s+", asserted)
                        if not negation.search(part))
    missing = [value for value in REQUIRED_LEDGER_STRINGS if value not in printable]
    results.check("every frozen value used in the packet appears exactly as reported", not missing, missing)
    results.check("the three failed hand-pollination trials are shown in both learner editions",
                  all(all(token in visible_text(soup, [role]) for token in ["Week 3", "Week 4", "Week 5"])
                      for role in ["student", "accessible"]))
    results.check("the numerical ledger records the acoustic absence that makes the case",
                  registry["numericalLedger"]["acoustic"]["periodicSignals"] == "none detected"
                  and registry["numericalLedger"]["acoustic"]["scanRangeHz"] == [20, 200]
                  and registry["numericalLedger"]["acoustic"]["telluvianGardenReferenceHz"] == [100, 150])
    results.check("the numerical ledger keeps 124 Hz qualified and names all four trial variables",
                  registry["numericalLedger"]["strongestResponseHz"] == 124
                  and "amplitude and duration" in registry["numericalLedger"]["strongestResponseQualifier"]
                  and len(registry["numericalLedger"]["trialVariables"]) == 4)
    results.check("the ledger records that three hand-pollination trials produced no success",
                  registry["numericalLedger"]["pollination"]["handPollinationAttempts"] == 3
                  and registry["numericalLedger"]["pollination"]["handPollinationSuccesses"] == 0
                  and registry["numericalLedger"]["pollination"]["pollenViabilityPercent"] == 98)

    # ── Science boundary ─────────────────────────────────────────────
    results.check("the source-status ledger separates established buzz pollination from case evidence",
                  set(registry["sourceStatus"]) >= {"establishedEarthScienceComparison", "caseSpecificEvidence"}
                  and "poricidal" in registry["sourceStatus"]["establishedEarthScienceComparison"].lower()
                  and "124 Hz" in registry["sourceStatus"]["caseSpecificEvidence"]
                  and not INVENTED_SCENARIO_REMINDER.search(json.dumps(registry, ensure_ascii=False)),
                  sorted(registry["sourceStatus"]))
    results.check("both learner editions attribute the case values to this investigation",
                  len(PROVENANCE.findall(visible_text(soup, ["student"]))) >= 3
                  and len(PROVENANCE.findall(visible_text(soup, ["accessible"]))) >= 3,
                  {"student": len(PROVENANCE.findall(visible_text(soup, ["student"]))),
                   "accessible": len(PROVENANCE.findall(visible_text(soup, ["accessible"])))})
    results.check("the Teacher Guide separates established science, case evidence, inference, and engineering layers",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["Established Earth science", "Case-specific evidence", "Case inference",
                       "Engineering extrapolation"]))
    results.check("the Teacher Guide states that honeybees do not perform floral buzzing",
                  "honeybees do not perform it" in visible_text(soup, ["teacher"]))
    results.check("the Teacher Guide keeps the two pollination routes distinct",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["grasps the flower", "airborne", "should not be merged"]))
    results.check("both learner editions state that the pores are already present",
                  all("already" in visible_text(soup, [role]).lower()
                      and "pores" in visible_text(soup, [role]).lower()
                      for role in ["student", "accessible"]))
    reminder_findings = [
        f"{page.get('data-page-id')}:{match.group(0)}"
        for page in soup.select(".page[data-role]")
        for match in INVENTED_SCENARIO_REMINDER.finditer(" ".join(page.stripped_strings))
    ]
    results.check("printable pages carry no repeated reminder that the scenario is invented",
                  not reminder_findings, reminder_findings)
    results.check("no mathematics standard is claimed",
                  "No mathematics standard is claimed" in visible_text(soup, ["teacher"])
                  and not re.search(r"CCSS|6\.EE|6\.RP", visible_text(soup, ROLES)))

    # ── Teaching analogy containment ─────────────────────────────────
    analogy_blocks = soup.select("[data-analogy]")
    results.check("the teaching analogy is present in both learner editions and marked as an analogy",
                  {node.find_parent(class_="page").get("data-role") for node in analogy_blocks}
                  == {"student", "accessible"},
                  [node.find_parent(class_="page").get("data-page-id") for node in analogy_blocks])
    results.check("the analogy states plainly that its counts are not garden measurements",
                  bool(analogy_blocks) and all(
                      "not measurements from the garden" in node.get_text(" ", strip=True)
                      for node in analogy_blocks))
    analogy_free = BeautifulSoup(content, "html.parser")
    for node in analogy_free.select("[data-analogy]"):
        node.decompose()
    invented_counts = ["0 grains", "about 5 grains", "about 200 grains"]
    results.check("the invented grain counts never appear outside the analogy block",
                  not any(count in visible_text(analogy_free, ROLES) for count in invented_counts))
    results.check("the task registry records the analogy and the cautions that guard the case",
                  "teachingAnalogy" in registry["sourceStatus"]
                  and any("already present" in note for note in registry["productionCautions"])
                  and any("sufficient on its own" in note for note in registry["productionCautions"]))

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
    results.check("no figure draws a curve or a response spectrum", not curve_findings, curve_findings)
    results.check("every figure caption attributes its data to this case",
                  all(PROVENANCE.search(figure.select_one("figcaption").get_text(" ", strip=True))
                      for figure in figures),
                  [figure.get("data-figure-id") for figure in figures
                   if not PROVENANCE.search(figure.select_one("figcaption").get_text(" ", strip=True))])
    cone_figures = [f for f in figures if "cone" in (f.get("data-figure-id") or "")]
    results.check("the cone figure states that the pores are already present and that nothing opens",
                  bool(cone_figures)
                  and all("already present" in f.get_text(" ", strip=True)
                          and "nothing opens or unseals" in f.get_text(" ", strip=True).lower()
                          for f in cone_figures),
                  [f.get("data-figure-id") for f in cone_figures])
    results.check("every graph is paired with a data-table equivalent on the same page",
                  all(figure.find_parent(class_="page").select_one("table.data-table") for figure in figures))
    results.check("figure marks use patterns rather than colour alone",
                  all(figure.select("pattern") for figure in figures))
    results.check("the four settings appear together so no single one reads as sufficient",
                  len(soup.select(".factor-grid .factor-card")) >= 8
                  and all(term in printable for term in ["Frequency", "Amplitude", "Duration", "Coupling"]))
    results.check("figure provenance is recorded in the task registry",
                  len(registry.get("figureProvenance", [])) >= 2
                  and all(entry.get("kind", "").startswith("curriculum-original")
                          for entry in registry["figureProvenance"]))

    # ── Prohibited scientific overstatement ──────────────────────────
    prohibited_findings = [reason for pattern, reason in PROHIBITED if pattern.search(affirmed)]
    results.check("no printable role asserts a prohibited scientific overstatement",
                  not prohibited_findings, prohibited_findings)
    results.check("the prohibited-claim registry is declared for the case",
                  len(registry.get("prohibitedClaims", [])) >= 12)
    results.check("the Teacher Guide names the prohibited claims for correction",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["Claims to correct on sight", "Data-use cautions", "Figure provenance"]))
    results.check("enumerated alternatives and quoted misconceptions are explicitly marked",
                  bool(soup.select("[data-candidate-claim]")) and bool(soup.select("[data-quoted-claim]")))
    results.check("quoted misconceptions appear only inside the Teacher Guide",
                  all(node.find_parent(class_="page").get("data-role") == "teacher"
                      for node in soup.select("[data-quoted-claim]")))
    results.check("the correct diagnosis and its three rejected alternatives are declared",
                  bool(registry["correctDiagnosis"]) and len(registry["incorrectAlternatives"]) == 3)
    results.check("the cultural constraint is presented as a boundary rather than obstruction",
                  "not secrecy" in visible_text(soup, ["teacher"]).lower())

    # ── CER, Answer Key and Accessible structure ─────────────────────
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
                  and accessible_subtitle.get_text(" ", strip=True) == ACCESSIBLE_CER_SUBTITLE)
    student_subtitle = soup.select_one('[data-student-cer-subtitle="canonical-v1.0"]')
    results.check("the Student CER carries the same approved subtitle",
                  student_subtitle is not None
                  and student_subtitle.get_text(" ", strip=True) == ACCESSIBLE_CER_SUBTITLE)
    answer_text = visible_text(soup, ["answer"])
    results.check("the Answer Key supplies a completed exemplar for every keyed task",
                  all(term in answer_text for term in
                      ["Completed rule-out", "Why three failed trials are useful evidence",
                       "What the salt was waiting for", "Two things working normally",
                       "Which source could establish the mechanism independently",
                       "Completed five-source analysis", "Completed diagnosis analysis",
                       "Completed rejections", "CLAIM", "EVIDENCE", "REASONING",
                       "Why 124 Hz alone is not a plan"]))
    results.check("Answer Key exemplars preserve the required qualifiers",
                  all(term in answer_text for term in
                      ["best-supported", "in this garden", "does not establish", "monitored trial"]))
    results.check("the Answer Key states the missing-event distinction the case turns on",
                  "an event, not an object" in answer_text)
    results.check("the completed mechanism model is a five-stage process contract",
                  len(soup.select('.page[data-role="answer"] '
                                  '[data-process-contract="vibration-release-five-stage-v1.0"] '
                                  '.path-stage')) == 5)

    # ── Accessible differentiation ───────────────────────────────────
    similarity = difflib.SequenceMatcher(
        None, visible_text(soup, ["student"]).split(), visible_text(soup, ["accessible"]).split()
    ).ratio()
    results.check("the Accessible edition is rewritten rather than reflowed",
                  similarity <= 0.80, f"{similarity * 100:.1f}% similar to the Student edition")
    results.check("the Accessible edition carries its own vocabulary support",
                  bool(soup.select('.page[data-role="accessible"] .word-bank'))
                  and bool(soup.select('.page[data-role="accessible"] .vocabulary-list')))
    results.check("both learner editions close by naming what solving the case taught",
                  all("Case closed — what it means" in visible_text(soup, [role])
                      for role in ["student", "accessible"]))

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
    results.check("the draft ships no owner-applied layout overrides",
                  layout["overrides"] == {} and layout["student"]["overrides"] == {})

    payload = {
        "validator": "sss-c2-case02-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
