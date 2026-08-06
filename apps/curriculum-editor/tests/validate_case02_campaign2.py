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
import sys
from pathlib import Path

from bs4 import BeautifulSoup

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))

# validate_static is guarded by __main__, so importing it runs nothing. Taking the baseline
# table and the hash function from there rather than restating them means this validator
# cannot drift from the enforcement that actually gates the build.
from validate_static import NON_ACCESSIBLE_BASELINE_HASHES, role_dom_hash  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
CASE_ID = "SSS-C2-CASE02"
CASE_ROOT = ROOT / "sss/campaign-2/case-02-missing-dance"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
RELEASE_VERSION = "1.1"
RETAINED_VERSION = "1.0"
APPROVAL_DATE = "2026-08-06"
RETAINED_APPROVAL_DATE = "2026-08-05"
OWNER = "Nate / Owner"
ROLE_PAGES = {"student": 6, "teacher": 8, "answer": 4, "accessible": 8}
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


def registry_entry(case_id: str) -> dict:
    data = json.loads((ROOT / "shared/implementation/case-registry.v2.json").read_text(encoding="utf-8"))
    for curriculum in data["curricula"]:
        for campaign in curriculum.get("campaigns", []):
            for case in campaign.get("cases", []):
                if case.get("id") == case_id:
                    return case
    raise AssertionError(f"{case_id} is not registered")


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
    entry = registry_entry(CASE_ID)
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

    # ── Approved corrective-release lifecycle ────────────────────────
    results.check("the package records the approved corrective-release lifecycle",
                  package["status"] == "APPROVED_STABLE"
                  and package["version"] == RELEASE_VERSION
                  and package["approval"] == {"date": APPROVAL_DATE, "owner": OWNER,
                                              "status": "APPROVED", "printStatus": "PASS"},
                  package["approval"])
    results.check("the task registry records the same approved corrective lifecycle",
                  (registry.get("version"), registry.get("status"), registry.get("approvalDate"),
                   registry.get("approvedBy"), registry.get("ownerReviewStatus"),
                   registry.get("printStatus"), registry.get("mergeStatus"),
                   registry.get("correctiveOf"))
                  == (RELEASE_VERSION, "APPROVED_STABLE", APPROVAL_DATE, OWNER,
                      "OWNER_REVIEW_PASS", "PASS", "READY_TO_MERGE", RETAINED_VERSION),
                  (registry.get("status"), registry.get("printStatus"), registry.get("correctiveOf")))
    results.check("the registry entry agrees with the approved package",
                  entry["version"] == RELEASE_VERSION and entry["status"] == "APPROVED_STABLE"
                  and entry["packageStatus"] == "APPROVED"
                  and entry["approval"] == package["approval"]
                  and entry.get("historyRecord") == package.get("releaseHistory"),
                  entry)
    results.check("the approved package names its own v1.1 release record",
                  package.get("releaseHistory")
                  == f"sss/campaign-2/case-02-missing-dance/history/release-v{RELEASE_VERSION}.json")

    history_path = CASE_ROOT / f"history/release-v{RELEASE_VERSION}.json"
    approval_path = CASE_ROOT / f"history/CASE02_OWNER_APPROVAL_v{RELEASE_VERSION}.md"
    retained_history_path = CASE_ROOT / f"history/release-v{RETAINED_VERSION}.json"
    retained_approval_path = CASE_ROOT / f"history/CASE02_OWNER_APPROVAL_v{RETAINED_VERSION}.md"
    results.check("the case retains exactly the v1.0 and v1.1 history records",
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir())
                  == [f"CASE02_OWNER_APPROVAL_v{RETAINED_VERSION}.md",
                      f"CASE02_OWNER_APPROVAL_v{RELEASE_VERSION}.md",
                      f"release-v{RETAINED_VERSION}.json",
                      f"release-v{RELEASE_VERSION}.json"],
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir()))

    # A deleted or emptied record is a named failure, not a traceback: a release whose
    # history has gone missing must be reported as such, not crash the validator.
    def record(path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}

    def text_of(path: Path) -> str:
        return path.read_text(encoding="utf-8") if path.is_file() else ""

    def commit_exists(sha) -> bool:
        return bool(sha) and subprocess.run(["git", "cat-file", "-e", f"{sha}^{{commit}}"],
                                            cwd=ROOT, capture_output=True).returncode == 0

    history = record(history_path)
    results.check("the v1.1 release record identifies the corrective release it describes",
                  history.get("caseId") == CASE_ID
                  and history.get("curriculumVersion") == RELEASE_VERSION
                  and history.get("correctiveOf") == RETAINED_VERSION
                  and history.get("status") == "APPROVED_STABLE"
                  and history.get("approvalDate") == APPROVAL_DATE
                  and history.get("owner") == OWNER,
                  {k: history.get(k) for k in ("caseId", "curriculumVersion", "correctiveOf")})
    results.check("the v1.1 release record pins the approved page counts",
                  history.get("rolePageCounts") == ROLE_PAGES, history.get("rolePageCounts"))
    results.check("the v1.1 release record pins the approved source hashes",
                  history.get("sourceHashes") == package["sourceHashes"], history.get("sourceHashes"))
    results.check("the v1.1 release record records the approved print gate",
                  history.get("acceptedPrintStatus") == "PASS at 100% / Actual Size"
                  and history.get("acceptedValidation", {}).get("status") == "PASS")
    results.check("the v1.1 release record declares no generated artifacts",
                  history.get("formerArtifacts", {}).get("status") == "NO_FORMER_GENERATED_ARTIFACTS"
                  and history.get("artifactPolicy") == "NO_GENERATED_ARTIFACTS_COMMITTED")
    corrections = history.get("correctionSummary", {}).get("corrections", [])
    results.check("the v1.1 release record explains what the corrective release corrects",
                  len(corrections) >= 6
                  and all(any(token in item for item in corrections)
                          for token in ("OK or ?", "Answer Key", "MS-LS2-2", "lyre-moth")),
                  corrections)
    results.check("the v1.1 release record records the frozen game baseline",
                  any(GAME_COMMIT in note for note in history.get("migrationNotes", [])))
    review_commits = [item["commit"] for item in history.get("correctiveReviewCommits", [])]
    results.check("every commit reference in the v1.1 release record exists",
                  all(commit_exists(sha)
                      for sha in [history.get("originalReleaseApprovalCommit"),
                                  history.get("canonicalSourceApprovalCommit"),
                                  history.get("formerArtifactRecoveryCommit"),
                                  *review_commits]))
    results.check("the v1.1 release record pins the whole corrective review, not just its last commit",
                  history.get("canonicalSourceApprovalCommit") in review_commits
                  and len(review_commits) >= 4,
                  review_commits)

    # ── Canonical prior-release representation ───────────────────────
    prior = history.get("priorApprovedReleases") or [{}]
    results.check("the v1.1 release record carries v1.0 as a canonical prior release",
                  len(history.get("priorApprovedReleases") or []) == 1
                  and prior[0].get("version") == RETAINED_VERSION
                  and prior[0].get("status") == "APPROVED_STABLE"
                  and prior[0].get("approvalDate") == RETAINED_APPROVAL_DATE,
                  history.get("priorApprovedReleases"))
    results.check("the prior-release entry indexes the retained v1.0 records",
                  sorted(prior[0].get("retainedRecords", []))
                  == sorted([f"sss/campaign-2/case-02-missing-dance/history/release-v{RETAINED_VERSION}.json",
                             f"sss/campaign-2/case-02-missing-dance/history/CASE02_OWNER_APPROVAL_v{RETAINED_VERSION}.md"]))
    prior_hashes = prior[0].get("sourceHashes", {})
    results.check("the prior-release entry preserves the v1.0 page counts and hashes as historical evidence",
                  prior[0].get("rolePageCounts") == {"student": 5, "teacher": 8, "answer": 4, "accessible": 8}
                  and all(prior_hashes.get(n) != package["sourceHashes"][n]
                          for n in ("content", "taskRegistry"))
                  and all(n in prior_hashes for n in ("content", "taskRegistry")))
    results.check("every commit reference in the prior-release entry exists",
                  all(commit_exists(prior[0].get(field))
                      for field in ("approvalCommit", "recoveryCommit",
                                    "canonicalSourceApprovalCommit")))

    # ── The retained v1.0 records, unchanged ─────────────────────────
    retained = record(retained_history_path)
    retained_hashes = retained.get("sourceHashes", {})
    results.check("the retained v1.0 record still describes the v1.0 release",
                  retained.get("caseId") == CASE_ID
                  and retained.get("curriculumVersion") == RETAINED_VERSION
                  and retained.get("status") == "APPROVED_STABLE"
                  and retained.get("approvalDate") == RETAINED_APPROVAL_DATE
                  and retained.get("rolePageCounts") == {"student": 5, "teacher": 8, "answer": 4,
                                                         "accessible": 8},
                  {k: retained.get(k) for k in ("caseId", "curriculumVersion", "approvalDate")})
    results.check("the retained v1.0 record was not rewritten to describe v1.1 content",
                  all(n in retained_hashes for n in ("content", "taskRegistry"))
                  and all(retained_hashes.get(n) != package["sourceHashes"][n]
                          for n in ("content", "taskRegistry"))
                  and retained_hashes == prior_hashes,
                  retained_hashes)
    results.check("every commit reference in the retained v1.0 record exists",
                  all(commit_exists(retained.get(field))
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")))
    results.check("the retained v1.0 record still records the frozen game baseline and case numbers",
                  any(GAME_COMMIT in note for note in retained.get("migrationNotes", []))
                  and any("keeps its runtime case number" in note
                          for note in retained.get("migrationNotes", [])))
    retained_owner_approval = text_of(retained_approval_path)
    results.check("the retained v1.0 owner approval still records the gates it passed",
                  all(token in retained_owner_approval for token in
                      ["Nate / Owner", RETAINED_APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS",
                       "READY_TO_MERGE", "On-screen content and visual review: **PASS**",
                       "Generated PDF review: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT]))

    # ── The v1.1 owner-approval record ───────────────────────────────
    owner_approval = text_of(approval_path)
    results.check("the v1.1 owner approval records all three gates",
                  all(token in owner_approval for token in
                      ["Nate / Owner", APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS",
                       "READY_TO_MERGE", "On-screen content and visual review: **PASS**",
                       "Generated PDF review: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT]))
    approval_tokens = ["OK or ?", "MS-LS2-2", "MS-ETS1-3", "lyre-moth", "100\u2013150 Hz",
                       "Table 1a", "Withdrawn"]
    results.check("the v1.1 owner approval documents the corrections it was approved for",
                  all(token in owner_approval for token in approval_tokens),
                  [token for token in approval_tokens if token not in owner_approval])
    results.check("the v1.1 owner approval records the Student page-count change and v1.0 preservation",
                  "| Student | 5 | **6** |" in owner_approval
                  and "superseded, not withdrawn" in owner_approval
                  and f"CASE02_OWNER_APPROVAL_v{RETAINED_VERSION}.md" in owner_approval)

    # ── Frozen v1.1 DOM baselines ────────────────────────────────────
    baselines = history.get("frozenNonAccessibleDomBaselines", {})
    prior_baselines = prior[0].get("frozenNonAccessibleDomBaselines", {})
    live_baselines = {role: role_dom_hash(soup, role) for role in ("student", "teacher", "answer")}
    results.check("the v1.1 release record pins the live Student, Teacher and Answer Key DOM baselines",
                  all(baselines.get(role) == live_baselines[role] for role in live_baselines),
                  live_baselines)
    results.check("the enforced baseline table holds exactly the v1.1 baselines",
                  NON_ACCESSIBLE_BASELINE_HASHES.get(CASE_ID) == live_baselines,
                  NON_ACCESSIBLE_BASELINE_HASHES.get(CASE_ID))
    results.check("no v1.1 baseline can be satisfied by the superseded v1.0 markup",
                  all(prior_baselines.get(role) for role in live_baselines)
                  and all(baselines.get(role) != prior_baselines.get(role)
                          for role in live_baselines),
                  prior_baselines)

    results.check("no generated release artifact is stored beside the case",
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
    rendered_figure_ids = {node["data-figure-id"] for node in soup.select("figure[data-figure-id]")}
    results.check("figure provenance names exactly the figures the packet renders",
                  {entry["id"] for entry in registry.get("figureProvenance", [])} == rendered_figure_ids
                  and all(entry.get("kind", "").startswith("curriculum-original")
                          for entry in registry["figureProvenance"]),
                  sorted(rendered_figure_ids))

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
                      ["Completed Table 1", "Why three failed trials are useful evidence",
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

    role_text = {role: visible_text(soup, [role]) for role in ROLES}
    student_text = role_text["student"]
    teacher_text = role_text["teacher"]
    accessible_text = role_text["accessible"]

    # ── A. Cross-role task-structure parity ──────────────────────────
    # Every table a role names in its directions must exist for that reader, and
    # every direction that tells a learner to write in a column must find one.
    def tables_named(text):
        return {int(n) for n in re.findall(r"Table (\d+)", text)}
    def tables_present(role):
        return {int(m.group(1)) for node in soup.select(f'.page[data-role="{role}"] table.data-table caption')
                for m in [re.match(r"Table (\d+)", node.get_text(strip=True))] if m}
    dangling = {}
    for role in ROLES:
        reader = role if role in ("student", "accessible") else "student"
        missing = tables_named(role_text[role]) - tables_present(reader)
        if missing:
            dangling[role] = sorted(missing)
    results.check("every table a role names resolves for the reader who holds it", not dangling, dangling)
    results.check("no role names a table suffix that was never rendered",
                  not re.search(r"Table \d+[a-z]\b", " ".join(role_text.values())),
                  re.findall(r"Table \d+[a-z]\b", " ".join(role_text.values())))

    def page_with_task(role, number):
        for page in soup.select(f'.page[data-role="{role}"]'):
            if any(h["data-shell-task-heading"] == str(number)
                   for h in page.select("[data-shell-task-heading]")):
                return page
        raise AssertionError(f"{role} has no page carrying task {number}")

    task1 = {role: page_with_task(role, 1) for role in ("student", "accessible")}
    for role, page in task1.items():
        status_table = next(tbl for tbl in page.select("table.data-table")
                            if tbl.find("caption").get_text(strip=True).startswith("Table 1"))
        headers = [th.get_text(strip=True) for th in status_table.select("th")]
        rows = status_table.select("tbody tr")
        cells = status_table.select("[data-response]")
        results.check(f"the {role} Task 1 table gives every row a writable mark cell",
                      headers[-1] == "OK or ?" and len(rows) == 6 and len(cells) == 6,
                      (headers[-1], len(rows), len(cells)))
        results.check(f"the {role} Task 1 directions define both mark categories",
                      "OK" in role_text[role] and "?" in role_text[role]
                      and "still worth a second look" in role_text[role])
    results.check("the Answer Key completes the same six-row Task 1 table the learners hold",
                  "Completed Table 1" in answer_text
                  and all(term in answer_text for term in
                          ["Air, humidity, light, soil and atmosphere", "Pollen", "Stigma",
                           "Pollinators in the garden", "Airflow", "Periodic vibration"]))
    results.check("no role still describes the retired two-column rule-out table",
                  "Completed rule-out" not in " ".join(role_text.values()))
    results.check("the Teacher Guide describes the six-row Task 1 that learners actually hold",
                  "the first three rows are" in teacher_text and "The last three are" in teacher_text
                  and "except the last two" not in teacher_text)

    # ── B. Evidence availability ─────────────────────────────────────
    # Anything the Answer Key or a graded task relies on must be readable in the
    # learner edition that student holds. Specialist terms must also be defined.
    learner_text = student_text + " " + accessible_text
    required_evidence = {
        "100–150 Hz Telluvian comparison": "100–150 Hz",
        "the lyre-moth pollinator": "lyre-moth",
        "its wingbeat": "wingbeat",
        "buzz pollination": "buzz pollination",
        "the poricidal anther": "poricidal",
        "the 124 Hz response": "124 Hz",
    }
    unavailable = [name for name, token in required_evidence.items()
                   if token.lower() not in learner_text.lower()]
    results.check("every item the Answer Key reasons from is present in the learner editions",
                  not unavailable, unavailable)
    per_role_missing = {role: [n for n, tok in required_evidence.items()
                               if tok.lower() not in role_text[role].lower()]
                        for role in ("student", "accessible")}
    results.check("both learner editions carry that evidence, not just one of them",
                  not any(per_role_missing.values()), per_role_missing)
    def vocabulary_text(role):
        """Only the glossary structures count as a definition, not any prose mention."""
        blocks = []
        for table in soup.select(f'.page[data-role="{role}"] table.data-table'):
            caption = table.find("caption")
            if caption and "vocabulary" in caption.get_text(strip=True).lower():
                blocks.append(" ".join(table.stripped_strings))
        for glossary in soup.select(f'.page[data-role="{role}"] dl.vocabulary-list'):
            blocks.append(" ".join(glossary.stripped_strings))
        return " ".join(blocks).lower()

    vocabulary = {role: vocabulary_text(role) for role in ("student", "accessible")}
    for term in ("Poricidal anther", "Buzz pollination"):
        undefined = [role for role in ("student", "accessible") if term.lower() not in vocabulary[role]]
        results.check(f"{term.lower()} is defined in the glossary of both learner editions",
                      not undefined, undefined)
    results.check("Teacher-only enrichment stays out of the graded requirements",
                  "28 dB" not in learner_text and "28 dB" not in answer_text)

    # ── C. Revision propagation ──────────────────────────────────────
    results.check("declared role page counts match the rendered document",
                  {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
                  == {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES})
    results.check("the task registry, package and content agree on the released version",
                  registry["version"] == package["version"] == entry["version"] == RELEASE_VERSION
                  and soup.select_one("[data-editor-content]")["data-editor-content"]
                  == f"sss-c2-case02-v{RELEASE_VERSION}")
    readme = (CASE_ROOT / "README.md").read_text(encoding="utf-8")
    results.check("the README describes the released version and its retained history",
                  f"`SSS-C2-CASE02`" in readme and RELEASE_VERSION in readme
                  and RETAINED_VERSION in readme)
    results.check("the README page counts match the package",
                  all(f"{role.title() if role != 'answer' else 'Answer Key'} "
                      f"{package['rolePageStructure'][role]['pageCount']}" in readme
                      or str(package["rolePageStructure"][role]["pageCount"]) in readme
                      for role in ROLES))
    results.check("no role advertises a standard the packet no longer claims",
                  "MS-LS2-2" not in " ".join(role_text.values())
                  and "MS-ETS1-3" not in " ".join(role_text.values()))

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
