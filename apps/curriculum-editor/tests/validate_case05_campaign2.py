#!/usr/bin/env python3
"""Case-scoped assertions for SSS Campaign 2 Case 05 — Too Clean a Room.

Enforces the draft source ledger, the five-clue instructional coverage, the figure
contract, the dose-precision rules, the Earth-science/case-record/modeled boundary, and the
prohibited scientific overstatements against the printable content of every role.

The case is the campaign's highest over-generalisation risk: a species-specific
radiation-responsive pathway is one short step from "a little radiation is good for you", and
a reading below an instrument's detection limit is one short step from "there is no radiation".
Both steps are detected here, and the detectors are self-tested against probe documents so a
regex that silently stops matching fails this suite rather than passing it.
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


ROOT = Path(__file__).resolve().parents[3]
CASE_ID = "SSS-C2-CASE05"
CASE_ROOT = ROOT / "sss/campaign-2/case-05-too-clean-room"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
RELEASE_VERSION = "1.0"
APPROVAL_DATE = "2026-08-05"
OWNER = "Nate / Owner"
PREVIEW_BASELINE = "5c1453328ac40a7f7a653efa18ef70bf73759f69"
RUNTIME_ID = "too_clean_room"
RUNTIME_NAME = "Concord Botanical Vault"
RUNTIME_LOCATION = "Lagrange Point 5"
RUNTIME_SUBTITLE = "Concord Neutral Zone"
CASE_SUBTITLE = "Campaign 2 · Case 05 · Lagrange Point 5, Concord Neutral Zone"
ROLES = ["student", "teacher", "answer", "accessible"]
ROLE_PAGES = {"student": 7, "teacher": 9, "answer": 5, "accessible": 7}
TASK_TITLES = [
    "Sort What Was Specified from What Was Not",
    "What a Reading Can and Cannot Tell You",
    "Read the Decline and the Failed Adjustments",
    "Connect the Five Evidence Sources",
    "Diagnose, Reject the Alternatives, and Model the Mechanism",
    "Explain the Diagnosis with CER",
    "Specify a Monitored Trial and Recommend a Response",
]
TASK_COUNT = len(TASK_TITLES)
CER_TASK = 6
FORMAL_CLUES = [
    "BLOOMS_INERT",
    "RADIATION_ZERO",
    "DNA_REPAIR_PATHWAY_INACTIVE",
    "KARRETH_HOMEWORLD_HIGH_RAD",
    "HORMESIS_OBLIGATE_RADIATION",
]
CER_SUBTITLE = ("You may write sentences or use bullet points. "
                "Use evidence from more than one source.")
PROCESS_CONTRACT = "radiation-signal-five-stage-v1.0"

# Values that must appear verbatim wherever the case reports them.
REQUIRED_LEDGER_STRINGS = [
    "<0.01 mGy/day", "about 8.4 mGy/day", "about 12 mGy/day",
    "100%", "68%", "31%", "11%", "6%",
    "22.0 °C", "20–25 °C", "55%", "50–60%", "14 h on / 10 h off", "12–16 h",
    "Tier-1", "Protocol v3.2", "profile v4", "within 2%",
    "six months", "two months", "94%",
]
# The rain-gauge example carries the detection-limit idea in Task 2. Its invented values must
# stay inside its own block and must never be presented as vault evidence.
ANALOGIES = ["rain-gauge-v1"]
ANALOGY_DISCLAIMER = re.compile(r"not a vault instrument", re.I)
ANALOGY_VALUES = ["0.2 mm", "0.8 mm", "0 mm", "1 mm", "5 mm"]

# A claim only counts as asserted when the surrounding sentence does not already qualify or deny
# it. Teacher guidance has to be able to say "this is not a demonstration of X" without tripping
# the detector for X, and a bounded reading has to be able to name its own bound. Each rule below
# therefore carries a guard: the pattern is a finding only when the guard is absent from the
# window around the match. NEVER is the guard for rules that must fire unconditionally.
NEGATION = re.compile(r"\bnot\b|\bnever\b|\bcannot\b|\bno\s+(?:support|evidence)\b|"
                      r"\bdoes\s+not\b|\bis\s+not\b|\brather\s+than\b|\bwithout\b|\bstops\b", re.I)
BOUNDED = re.compile(r"<|\bbelow\b|\bsmaller\s+than\b|\bunder\b|\bnever\b|\bnot\b|"
                     r"\bdetection\s+limit\b|\bmonitor\b|\bbound\b", re.I)
PROVENANCE_NEAR = re.compile(r"\babout\b|\bsite\s+record\b|\bsurveyed\b|\bhomeworld\b|\brecorded\s+at\b", re.I)
MODELED_NEAR = re.compile(r"\bmodel(?:ed|led)?\b|\bcalculated\b", re.I)
NEVER = re.compile(r"(?!x)x")

# Precision failures. Each entry is a way the packet could silently upgrade a bounded, site-
# recorded, or modeled value into a measurement it is not.
PRECISION_PATTERNS = [
    (re.compile(r"(?<![.\d<])\b0\.01\s*mGy/day", re.I), BOUNDED,
     "the bounded vault reading restated as the exact value 0.01 mGy/day"),
    (re.compile(r"\b(?:dose|radiation|exposure)\s+(?:of|is|was|reads?)\s+(?:exactly\s+)?(?:0|zero)\b", re.I),
     NEGATION, "the vault dose stated as zero"),
    (re.compile(r"\b(?:no|zero)\s+radiation\s+(?:in|inside|reaches|reached|at)\s+the\s+vault", re.I),
     NEVER, "the vault described as containing no radiation"),
    (re.compile(r"\b\d+(?:\.\d+)?\s*(?:mSv|sievert)s?\b", re.I), NEVER,
     "an absorbed dose converted into sievert"),
    (re.compile(r"\b8\.4\s*mGy/day\b", re.I), PROVENANCE_NEAR,
     "the homeworld site record quoted without its 'about' or its provenance"),
    (re.compile(r"\b12\s*mGy/day\b", re.I), MODELED_NEAR,
     "the modeled Rhessi figure quoted without its modeled status"),
    (re.compile(r"\bdose[- ]response\s+curve\b", re.I), NEGATION,
     "a dose-response curve asserted from two dose conditions"),
]

# Prohibited scientific overstatements, case-specific. Scanned across every role after the
# deliberately quoted misconceptions in the Teacher Guide have been removed.
PROHIBITED = [
    (re.compile(r"\bradiation\s+is\s+(?:a\s+)?(?:nutrient|food|fuel)\b", re.I), NEGATION,
     "radiation described as a nutrient, food, or fuel"),
    (re.compile(r"\b(?:all\s+)?plants?\s+(?:need|require|must\s+have)\s+(?:ionizing\s+)?radiation\b", re.I),
     NEGATION, "universal claim that plants need radiation"),
    (re.compile(r"\b(?:a\s+)?(?:little|low[- ]dose|small\s+amount\s+of)\s+radiation\s+is\s+"
                r"(?:good|healthy|beneficial|fine)\b", re.I), NEGATION,
     "low-dose radiation asserted to be good for people"),
    (re.compile(r"\bradiation\s+(?:is\s+)?(?:good|beneficial|healthy)\s+for\s+"
                r"(?:you|people|humans|earth\s+organisms|organisms|life)\b", re.I), NEGATION,
     "radiation asserted to benefit people or Earth organisms"),
    (re.compile(r"\bDNA\s+damage\s+is\s+(?:good|beneficial|helpful|harmless)\b", re.I), NEGATION,
     "DNA damage described as beneficial or harmless"),
    (re.compile(r"\b(?:radiation[- ]powered\s+photosynthesis|radiosynthes\w+)\b", re.I), NEGATION,
     "radiation-powered photosynthesis asserted"),
    (re.compile(r"\bfungi\s+(?:eat|feed\s+on|live\s+on|need|require)\s+radiation\b", re.I), NEGATION,
     "fungi asserted to require or feed on radiation"),
    (re.compile(r"\bmore\s+radiation\s+(?:would|will|means?)\s+(?:make\s+)?more\b", re.I), NEGATION,
     "more exposure asserted to produce more compound"),
    (re.compile(r"\bthe\s+bloom\s+will\s+(?:recover|be\s+cured|start\s+producing\s+again)\b", re.I),
     NEGATION, "recovery asserted as a certainty"),
    (re.compile(r"\b8\.4\s*mGy/day\s+is\s+the\s+(?:optimal|ideal|required|correct|right|best)\b", re.I),
     NEGATION, "the homeworld site record presented as an optimum"),
    (re.compile(r"\bthe\s+bloom\s+(?:decided|chose|choose|wanted|refused)\s+to\b", re.I), NEGATION,
     "intention attributed to the bloom"),
    (re.compile(r"\b(?:use|install|add|obtain)\s+(?:a\s+)?"
                r"(?:cobalt|caesium|cesium|americium|radium|strontium|isotope|radioisotope|"
                r"radiation\s+source|x[- ]?ray\s+(?:tube|machine))\b", re.I), NEVER,
     "an isotope, source, or device prescribed for an intervention"),
    (re.compile(r"\bshielding\s+(?:is|was)\s+(?:harmful|dangerous|a\s+mistake|wrong)\b", re.I), NEGATION,
     "radiation shielding itself described as harmful or a mistake"),
    (re.compile(r"\bhormesis\b", re.I), NEVER,
     "the internal hormesis framing the Concord record explicitly refuses"),
    (re.compile(r"\bthis\s+(?:applies|is\s+true)\s+for\s+(?:all|every)\s+(?:plants?|species|organisms?)\b", re.I),
     NEGATION, "the species-specific result generalised to all organisms"),
]

# Provenance wording. Every vault value must read as a record made for this case rather than as
# established biology. Any of these phrases satisfies it.
PROVENANCE = re.compile(
    r"case data|vault record|vault production record|vault sensor|sensor array|site record|"
    r"habitat record|species record|species file|transplant record|examination record|"
    r"recorded for this vault|recorded at this site|recorded observations|recorded outcome|"
    r"modeled average|modeled result|Concord records|records report|the vault(?:'|’)s (?:own )?records",
    re.I,
)
# Wording whose only function is to remind the reader that the scenario is invented.
INVENTED_SCENARIO_REMINDER = re.compile(r"\bfictional\b|\bfiction\b|\bmade[- ]up\b|\bimaginary\b", re.I)
CURVE_COMMANDS = re.compile(r"[CcSsQqTtAa]")
LIFECYCLE_METADATA = re.compile(
    r"\b(?:DRAFT|APPROVED_STABLE|OWNER_REVIEW\w*|READY_TO_MERGE|NOT_READY|VALIDATION_BUILD)\b"
    r"|\bfeat/[\w-]+|\b[0-9a-f]{40}\b")


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
    quotations are explicitly marked in the source with data-quoted-claim and are excluded here,
    so the prohibited-claim scan measures what the packet asserts rather than what it corrects.
    The exclusion is deliberately narrow: it applies only to marked nodes, and a separate
    assertion confirms those nodes appear on Teacher pages and nowhere else.
    """
    working = BeautifulSoup(content, "html.parser")
    for node in working.select("[data-quoted-claim]"):
        node.decompose()
    return visible_text(working, roles)


def unqualified(text: str, pattern: re.Pattern, guard: re.Pattern,
                before: int = 110, after: int = 70) -> bool:
    """True when the pattern appears somewhere its guard does not.

    The window is deliberately local. A guard far away in another sentence must not license a
    claim, and a correction sitting beside the claim it corrects must not be reported as one.
    """
    return any(not guard.search(text[max(0, match.start() - before):match.end() + after])
               for match in pattern.finditer(text))


def scan(text: str, bank: list) -> list[str]:
    return [reason for pattern, guard, reason in bank if unqualified(text, pattern, guard)]


def probe(markup: str) -> str:
    """Visible text of a synthetic single-page document, used to self-test the detectors."""
    return visible_text(BeautifulSoup(
        f'<main><section class="page" data-role="student" data-page-id="probe">{markup}</section></main>',
        "html.parser"), ["student"])


def main() -> int:
    results = Results()
    package = json.loads((SOURCE / "case-package.json").read_text(encoding="utf-8"))
    registry = task_registry(SOURCE / "task-registry.js")
    content_path = SOURCE / "content.html"
    content = content_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(content, "html.parser")
    ledger = registry["numericalLedger"]
    layout = json.loads((SOURCE / "layout-overrides.json").read_text(encoding="utf-8"))

    # ── Identity, runtime linkage, and pinned baseline ───────────────
    results.check("package and task registry declare the same case identity",
                  package["id"] == registry["case"] == CASE_ID and package["title"] == registry["title"])
    results.check("task registry pins the frozen game baseline and runtime case id",
                  registry.get("gameCommit") == GAME_COMMIT and registry.get("runtimeCaseId") == RUNTIME_ID,
                  {"gameCommit": registry.get("gameCommit"), "runtimeCaseId": registry.get("runtimeCaseId")})
    results.check("task registry records the canonical runtime investigation, location, and subtitle",
                  (registry.get("runtimeInvestigationName"), registry.get("runtimeLocation"),
                   registry.get("runtimeSubtitle")) == (RUNTIME_NAME, RUNTIME_LOCATION, RUNTIME_SUBTITLE),
                  [registry.get("runtimeInvestigationName"), registry.get("runtimeLocation"),
                   registry.get("runtimeSubtitle")])
    results.check("package declares the routine SSS/SAA printable identity",
                  package["institutionalIdentity"]["name"] == "Solar Agricultural Agency"
                  and package["subtitle"] == CASE_SUBTITLE
                  and package["location"] == RUNTIME_NAME)
    results.check("the printable subtitle states Campaign 2 Case 05 positionally on every first page",
                  all(page.select_one(".mission-subtitle")
                      and page.select_one(".mission-subtitle").get_text(strip=True) == CASE_SUBTITLE
                      for page in soup.select('[data-page-identity="first"]')),
                  len(soup.select('[data-page-identity="first"]')))
    results.check("the case folder and package path carry the Case 05 positional number",
                  CASE_ROOT.name == "case-05-too-clean-room"
                  and package["content"]["source"].startswith("sss/campaign-2/case-05-too-clean-room/"))

    # ── Approved lifecycle, release history, no artifacts ───────────
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
                      "OWNER_REVIEW_PASS", "READY_TO_MERGE"),
                  [registry.get("status"), registry.get("ownerReviewStatus"), registry.get("mergeStatus")])
    results.check("the approved package names exactly one retained release-history record",
                  package.get("releaseHistory")
                  == "sss/campaign-2/case-05-too-clean-room/history/release-v1.0.json"
                  and sorted(path.name for path in (CASE_ROOT / "history").iterdir())
                  == ["CASE05_OWNER_APPROVAL_v1.0.md", "release-v1.0.json"],
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir()))
    history = json.loads((CASE_ROOT / "history/release-v1.0.json").read_text(encoding="utf-8"))
    results.check("the release history records a native release with no former generated artifacts",
                  history["caseId"] == CASE_ID and history["status"] == "APPROVED_STABLE"
                  and history["approvalDate"] == APPROVAL_DATE and history["owner"] == OWNER
                  and history["formerArtifacts"]["status"] == "NO_FORMER_GENERATED_ARTIFACTS"
                  and history["priorApprovedReleases"] == []
                  and history["retiredArtifacts"] == [])
    results.check("the release history page counts match the approved release",
                  history["rolePageCounts"] == ROLE_PAGES, history["rolePageCounts"])
    results.check("the release history pins the source hashes it was approved at",
                  all(history["sourceHashes"][name] == package["sourceHashes"][name]
                      for name in ("content", "presentation", "taskRegistry")),
                  history["sourceHashes"])
    results.check("every commit reference in the release history exists",
                  all(subprocess.run(["git", "cat-file", "-e", f"{history[field]}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")))
    results.check("the release history records the frozen game baseline and the preview baseline",
                  any(GAME_COMMIT in note for note in history["migrationNotes"])
                  and any(PREVIEW_BASELINE in note for note in history["migrationNotes"]))
    results.check("the release history explains the seven-page Student edition",
                  any("seven pages" in note for note in history["migrationNotes"]))
    results.check("the release history records the accepted print gate",
                  history["acceptedPrintStatus"].startswith("PASS")
                  and history["acceptedValidation"]["status"] == "PASS")
    approval_record = (CASE_ROOT / "history/CASE05_OWNER_APPROVAL_v1.0.md").read_text(encoding="utf-8")
    results.check("the owner approval record captures every release gate and the no-artifact decision",
                  all(token in approval_record for token in
                      ["**APPROVED_STABLE**", "**OWNER_REVIEW_PASS**", "**READY_TO_MERGE**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT, PREVIEW_BASELINE]))
    results.check("the case stores no PDFs or screenshots",
                  not [path.name for suffix in ("*.pdf", "*.png", "*.jpg", "*.jpeg")
                       for path in CASE_ROOT.rglob(suffix)])
    results.check("the case stores no generated role document",
                  sorted(path.name for path in CASE_ROOT.rglob("*.html")) == ["content.html"],
                  sorted(path.name for path in CASE_ROOT.rglob("*.html")))
    results.check("the case folder uses the canonical lean layout",
                  sorted(path.name for path in CASE_ROOT.iterdir())
                  == ["README.md", "history", "source"]
                  and sorted(path.name for path in SOURCE.iterdir())
                  == ["case-package.json", "content.html", "layout-overrides.json",
                      "presentation.css", "task-registry.js"],
                  sorted(path.name for path in CASE_ROOT.iterdir()))

    # ── Registry entry and campaign ordering ─────────────────────────
    case_registry = json.loads((ROOT / "shared/implementation/case-registry.v2.json")
                               .read_text(encoding="utf-8"))
    campaigns = {campaign["id"]: campaign["cases"]
                 for curriculum in case_registry["curricula"] for campaign in curriculum["campaigns"]}
    results.check("Campaign 1 still registers exactly seven cases", len(campaigns["campaign-1"]) == 7)
    results.check("Campaign 2 registers Cases 01 to 05 in numerical display order",
                  [case["id"] for case in campaigns["campaign-2"]][:5]
                  == ["SSS-C2-CASE01", "SSS-C2-CASE02", "SSS-C2-CASE03", "SSS-C2-CASE04", CASE_ID]
                  and [case["displayOrder"] for case in campaigns["campaign-2"]][:5] == [8, 9, 10, 11, 12],
                  [(case["id"], case["displayOrder"]) for case in campaigns["campaign-2"]])
    results.check("Case 05 is the fifth Campaign 2 case and is labelled positionally",
                  campaigns["campaign-2"][4]["id"] == CASE_ID
                  and campaigns["campaign-2"][4]["displayLabel"] == "5 - Too Clean a Room")
    entry = campaigns["campaign-2"][4]
    results.check("the Case 05 registry entry is an approved release with a history record",
                  entry["status"] == "APPROVED_STABLE" and entry["packageStatus"] == "APPROVED"
                  and entry.get("historyRecord")
                  == "sss/campaign-2/case-05-too-clean-room/history/release-v1.0.json"
                  and entry["approval"] == {"date": APPROVAL_DATE, "owner": OWNER,
                                            "status": "APPROVED", "printStatus": "PASS"})
    results.check("all thirteen registered cases are approved or valid corrective candidates",
                  not unexpected_lifecycle(campaigns)
                  and sum(len(cases) for cases in campaigns.values()) == 13,
                  unexpected_lifecycle(campaigns)
                  or sum(len(cases) for cases in campaigns.values()))

    # ── Source hashes ────────────────────────────────────────────────
    hash_targets = {
        "content": content_path,
        "presentation": SOURCE / "presentation.css",
        "taskRegistry": SOURCE / "task-registry.js",
        "layoutOverrides": SOURCE / "layout-overrides.json",
    }
    results.check("package source hashes verify",
                  all(hashlib.sha256(path.read_bytes()).hexdigest() == package["sourceHashes"][name]
                      for name, path in hash_targets.items()),
                  {name: hashlib.sha256(path.read_bytes()).hexdigest()[:12]
                   for name, path in hash_targets.items()})

    # ── Task architecture, order, and page counts ────────────────────
    task_titles = [item["title"] for item in registry["tasks"]]
    results.check("task registry uses the eight design-locked titles", task_titles == TASK_TITLES, task_titles)
    task_ids = [item["id"] for item in registry["tasks"]]
    results.check("task identifiers are stable and unique",
                  task_ids == [f"C2-C05-T{n}" for n in range(1, TASK_COUNT + 1)]
                  and len(set(task_ids)) == TASK_COUNT, task_ids)
    role_task_orders = {
        role: [int(node["data-shell-task-heading"])
               for page in soup.select(f'.page[data-role="{role}"]')
               for node in page.select("[data-shell-task-heading]")]
        for role in ["student", "answer", "accessible"]
    }
    results.check("Student, Answer Key, and Accessible task order has exact parity with each task once",
                  all(order == list(range(1, TASK_COUNT + 1)) for order in role_task_orders.values()),
                  role_task_orders)
    actual_pages = {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES}
    results.check("printable page counts match the package and the task registry",
                  actual_pages == ROLE_PAGES
                  and {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES} == ROLE_PAGES
                  and registry["roles"] == ROLE_PAGES,
                  actual_pages)
    results.check("the CER task occupies a full page of its own in both learner editions",
                  [[int(x["data-shell-task-heading"]) for x in page.select("[data-shell-task-heading]")]
                   for page in soup.select('.page[data-role="student"]')].count([CER_TASK]) == 1
                  and any(page.get("data-accessible-cer-page") == "canonical-v1.0"
                          and [int(x["data-shell-task-heading"])
                               for x in page.select("[data-shell-task-heading]")] == [CER_TASK]
                          for page in soup.select('.page[data-role="accessible"]')))

    # ── Five formal clues ────────────────────────────────────────────
    results.check("the five formal clues are declared and covered by tasks",
                  registry["formalClues"] == FORMAL_CLUES
                  and set(registry["clueTaskCoverage"]) == set(FORMAL_CLUES)
                  and all(registry["clueTaskCoverage"][clue] for clue in FORMAL_CLUES))
    results.check("every clue has a source-ledger entry with a contribution and a limit",
                  {item["clue"] for item in registry["sourceLedger"]} == set(FORMAL_CLUES)
                  and all(item.get("establishes") and item.get("cannotEstablishAlone")
                          for item in registry["sourceLedger"]))
    results.check("the five runtime clue routes are recorded", len(registry["requiredRoutes"]) == 5
                  and all("->" in route for route in registry["requiredRoutes"]))
    printable_all = visible_text(soup, ROLES)
    leaked_tags = [clue for clue in FORMAL_CLUES if clue in printable_all]
    results.check("internal clue tags never appear in printable content", not leaked_tags, leaked_tags)
    for role in ("student", "accessible"):
        role_text = visible_text(soup, [role])
        missing_sources = [item["source"] for item in registry["sourceLedger"]
                           if item["source"] not in role_text]
        results.check(f"the {role} edition names all five evidence sources in Task 5",
                      not missing_sources, missing_sources)

    # ── Numerical ledger and precision ───────────────────────────────
    asserted = re.sub(r"\s+", " ", asserted_text(content, ROLES))
    missing = [value for value in REQUIRED_LEDGER_STRINGS if value not in printable_all]
    results.check("every frozen value used in the packet appears exactly as reported", not missing, missing)
    precision_findings = scan(asserted, PRECISION_PATTERNS)
    results.check("bounded, site-recorded, and modeled values are never converted to exact measurements",
                  not precision_findings, precision_findings)
    results.check("the detection-limit status travels with the vault reading in every learner edition",
                  all(re.search(r"<0\.01\s*mGy/day[^.]{0,120}detection limit"
                                r"|detection limit[^.]{0,120}<0\.01\s*mGy/day",
                                visible_text(soup, [role]), re.I)
                      for role in ["student", "accessible", "answer"]))
    results.check("the modeled comparison keeps its modeled status in every learner edition",
                  all(re.search(r"about 12 mGy/day[^.]{0,120}modeled|modeled[^.]{0,120}about 12 mGy/day",
                                visible_text(soup, [role]), re.I)
                      for role in ["student", "accessible"]))
    results.check("the ledger records the three dose values and their status",
                  ledger["dose"]["vaultReading"] == "<0.01 mGy/day"
                  and ledger["dose"]["homeworldSiteRecord"] == "about 8.4 mGy/day"
                  and ledger["dose"]["rhessiHabitat"] == "about 12 mGy/day"
                  and "detection limit" in ledger["dose"]["vaultReadingStatus"]
                  and "modeled" in ledger["dose"]["rhessiStatus"])
    results.check("the ledger records the six reported monthly production values",
                  [ledger["production"][f"month{n}"] for n in range(1, 7)]
                  == ["100%", "100%", "68%", "31%", "11%", "6%"])
    unreported_months = re.findall(r"\bMonth\s*(?:0|[7-9]|1[0-9])\b", printable_all, re.I)
    results.check("no printable role reports a production value for an unreported month",
                  not unreported_months, unreported_months)
    results.check("no numeric dose is ever expressed in sievert",
                  not re.search(r"\d+(?:\.\d+)?\s*(?:mSv|sieverts?)\b", printable_all, re.I)
                  and "mSv" not in printable_all)
    results.check("sievert is named only to explain why the packet does not use it",
                  all(re.search(r"sievert", visible_text(soup, [role]), re.I) is None
                      or re.search(r"(?:cannot|not)\b[^.]{0,160}sievert"
                                   r"|sievert[^.]{0,160}(?:not interchangeable|weighting)",
                                   visible_text(soup, [role]), re.I)
                      for role in ROLES))

    # ── Science boundary ─────────────────────────────────────────────
    teacher_text = visible_text(soup, ["teacher"])
    results.check("the Teacher Guide separates established science, case evidence, modeled evidence, "
                  "inference, and engineering layers",
                  all(term in teacher_text for term in
                      ["Established Earth science", "Case-specific evidence", "Modeled evidence",
                       "Case inference", "Engineering extrapolation"]))
    results.check("the registry records the same five source-status layers",
                  all(key in registry["sourceStatus"] for key in
                      ["establishedEarthScience", "establishedEarthScienceComparison",
                       "caseSpecificEvidence", "modeledEvidence", "caseInference",
                       "engineeringExtrapolation"]))
    results.check("both learner editions attribute the vault values to records made for this case",
                  len(PROVENANCE.findall(visible_text(soup, ["student"]))) >= 3
                  and len(PROVENANCE.findall(visible_text(soup, ["accessible"]))) >= 3,
                  [len(PROVENANCE.findall(visible_text(soup, [role]))) for role in ("student", "accessible")])
    results.check("the Teacher Guide states the species-specific limit of the Earth fungi comparison",
                  "melanin" in teacher_text.lower()
                  and re.search(r"not\s+a\s+demonstration\s+of\s+radiation-powered\s+photosynthesis"
                                r"|does not (?:establish|show)", teacher_text, re.I))
    results.check("the Teacher Guide records the bounded MS-LS1-5 assessment boundary",
                  "MS-ETS1-1" in teacher_text and "MS-LS1-5" in teacher_text
                  and "Direct assessment: MS-ETS1-1" in teacher_text
                  and re.search(r"MS-LS1-5[^.]{0,40}bounded|Supporting alignment: MS-LS1-5", teacher_text))
    results.check("the Teacher Guide names Task 7 as the MS-ETS1-1 task evidence",
                  re.search(r"MS-ETS1-1\.\*{0,2}\s*</?\w*>?\s*Task 7|Task 7 defines the criteria", teacher_text))
    reminder_findings = [page.get("data-page-id") for page in soup.select(".page[data-role]")
                         if INVENTED_SCENARIO_REMINDER.search(" ".join(page.stripped_strings))]
    results.check("no printable page reminds the reader that the scenario is invented",
                  not reminder_findings, reminder_findings)

    # ── Prohibited overstatement, with self-tested detectors ─────────
    prohibited_findings = scan(asserted, PROHIBITED)
    results.check("no printable role asserts a prohibited scientific overstatement",
                  not prohibited_findings, prohibited_findings)
    results.check("the prohibited-claim registry is declared for the case",
                  len(registry.get("prohibitedClaims", [])) >= 12,
                  len(registry.get("prohibitedClaims", [])))
    # Negative tests: each detector must actually fire on the misconception it exists to catch.
    misconception_probes = [
        ("radiation as nutrient", "<p>For this species radiation is a nutrient.</p>"),
        ("plants need radiation", "<p>All plants need radiation to make their compounds.</p>"),
        ("low dose good for people", "<p>A little radiation is good for you.</p>"),
        ("benefit to organisms", "<p>Radiation is beneficial for people everywhere.</p>"),
        ("DNA damage beneficial", "<p>DNA damage is beneficial to the plant.</p>"),
        ("radiosynthesis", "<p>The fungi use radiation-powered photosynthesis.</p>"),
        ("fungi require radiation", "<p>Chernobyl fungi eat radiation the way plants use light.</p>"),
        ("more is better", "<p>More radiation would make more medicine.</p>"),
        ("recovery certain", "<p>The bloom will recover once the trial ends.</p>"),
        ("site record as optimum", "<p>So 8.4 mGy/day is the optimal exposure for the bloom.</p>"),
        ("plant intention", "<p>The bloom decided to stop making the compound.</p>"),
        ("device prescribed", "<p>Install a cobalt source in the chamber.</p>"),
        ("shielding blamed", "<p>The shielding was a mistake from the beginning.</p>"),
        ("hormesis framing", "<p>This is an example of radiation hormesis.</p>"),
        ("over-generalised", "<p>This is true for all species in the Concord.</p>"),
    ]
    undetected = [name for name, markup in misconception_probes if not scan(probe(markup), PROHIBITED)]
    results.check("every misconception detector fires on the claim it exists to catch",
                  not undetected, undetected)
    precision_probes = [
        ("exact 0.01", "<p>The vault dose is 0.01 mGy/day.</p>"),
        ("dose stated as zero", "<p>The radiation is zero inside the chamber.</p>"),
        ("no radiation in the vault", "<p>There is no radiation in the vault at all.</p>"),
        ("sievert conversion", "<p>That is about 8.4 mSv per day.</p>"),
        ("modeled value unlabelled", "<p>The Rhessi habitat sits at 12 mGy/day.</p>"),
    ]
    undetected_precision = [name for name, markup in precision_probes
                            if not scan(probe(markup), PRECISION_PATTERNS)]
    results.check("every precision detector fires on the conversion it exists to catch",
                  not undetected_precision, undetected_precision)
    # False-positive guard: the Teacher Guide's quoted-and-corrected misconceptions must not trip
    # the scan, and the exclusion must stay narrow.
    quoted_nodes = soup.select("[data-quoted-claim]")
    results.check("quoted misconceptions exist and are corrected only in the Teacher Guide",
                  len(quoted_nodes) >= 5
                  and all(node.find_parent(class_="page").get("data-role") == "teacher"
                          for node in quoted_nodes),
                  len(quoted_nodes))
    quoted_text = " ".join(" ".join(node.stripped_strings) for node in quoted_nodes)
    quoted_hits = [reason for pattern, _guard, reason in PROHIBITED if pattern.search(quoted_text)]
    results.check("the quoted misconceptions really do contain claims the scan would otherwise reject",
                  len(quoted_hits) >= 4, quoted_hits)
    results.check("the Teacher Guide still names the prohibited claims for correction",
                  "Claims to correct on sight" in teacher_text)
    results.check("learner explanations are required to be qualified rather than proven",
                  all(re.search(r"does not (?:establish|prove)", visible_text(soup, [role]), re.I)
                      for role in ("student", "accessible")))

    # ── Figures ──────────────────────────────────────────────────────
    figures = soup.select("figure")
    results.check("every figure carries a caption, an extended description, and an accessible SVG name",
                  bool(figures) and all(figure.select_one("figcaption")
                                        and figure.select_one(".extended-description")
                                        and figure.select_one('svg[role="img"][aria-label]')
                                        for figure in figures),
                  len(figures))
    figure_ids = [figure.get("data-figure-id") for figure in figures]
    results.check("figure identifiers are unique", len(set(figure_ids)) == len(figure_ids), figure_ids)
    curve_findings = [figure.get("data-figure-id") for figure in figures
                      if any(CURVE_COMMANDS.search(path.get("d", "")) for path in figure.select("path"))
                      or figure.select("polyline,polygon")]
    results.check("no figure draws a curve or joins the reported values", not curve_findings, curve_findings)
    results.check("every figure caption states the limit of what it reports",
                  all(re.search(r"no curve is drawn|discrete",
                                figure.select_one("figcaption").get_text(" ", strip=True), re.I)
                      for figure in figures))
    results.check("every figure caption states its provenance boundary",
                  all(re.search(r"teaching example, not vault data|vault production record",
                                figure.select_one("figcaption").get_text(" ", strip=True), re.I)
                      for figure in figures),
                  [figure.select_one("figcaption").get_text(" ", strip=True)[:60] for figure in figures])
    results.check("teaching figures are lettered so they never read as case records",
                  all(re.match(r"Figure [A-Z] ·", figure.select_one("figcaption").get_text(" ", strip=True))
                      for figure in figures))
    results.check("bands and bars use patterns rather than colour alone",
                  all(figure.select("pattern") and figure.select('rect[fill^="url("]')
                      for figure in figures))
    results.check("every figure page also carries a data table",
                  all(figure.find_parent(class_="page").select("table.data-table") for figure in figures))
    results.check("figure provenance is recorded in the task registry for every drawn figure",
                  {item["id"] for item in registry.get("figureProvenance", [])} == set(figure_ids)
                  and all(item.get("kind", "").startswith("curriculum-original")
                          for item in registry["figureProvenance"]),
                  sorted({item["id"] for item in registry.get("figureProvenance", [])} ^ set(figure_ids)))

    # ── Teaching analogy containment ─────────────────────────────────
    for role in ("student", "accessible"):
        page_soup = BeautifulSoup(content, "html.parser")
        role_analogies = [node.get("data-analogy")
                          for node in page_soup.select(f'.page[data-role="{role}"] [data-analogy]')]
        results.check(f"the {role} edition carries every teaching analogy",
                      sorted(set(role_analogies)) == sorted(ANALOGIES), role_analogies)
        results.check(f"every {role} analogy states its disclaimer",
                      all(ANALOGY_DISCLAIMER.search(" ".join(node.stripped_strings))
                          for node in page_soup.select(f'.page[data-role="{role}"] [data-analogy]')))
        stripped = BeautifulSoup(content, "html.parser")
        for node in stripped.select("[data-analogy]"):
            node.decompose()
        outside = visible_text(stripped, [role])
        leaked = [value for value in ANALOGY_VALUES if value in outside]
        results.check(f"no teaching-example value leaks outside its block in the {role} edition",
                      not leaked, leaked)
    results.check("teaching analogies never appear in the Answer Key",
                  not soup.select('.page[data-role="answer"] [data-analogy]'))
    results.check("the registry records why the analogy exists",
                  "rain-gauge" in registry["sourceStatus"]["teachingAnalogy"].lower()
                  and "teachingExample" in ledger)

    # ── CER, Accessible structure, Answer Key ────────────────────────
    cer_contracts = {root.get("data-cer-contract"):
                     [box.select_one(":scope > .canonical-cer-label").get_text(strip=True)
                      for box in root.select(":scope > .canonical-cer-box")]
                     for root in soup.select(".canonical-cer[data-cer-contract]")}
    results.check("CER uses only the three approved atomic contracts",
                  cer_contracts == {"student-v1.0": ["CLAIM", "EVIDENCE", "REASONING"],
                                    "answer-v1.0": ["CLAIM", "EVIDENCE", "REASONING"],
                                    "accessible-v1.0": ["CLAIM", "EVIDENCE", "REASONING"]},
                  cer_contracts)
    accessible_cer_pages = soup.select('.page[data-accessible-cer-page="canonical-v1.0"]')
    results.check("the Accessible CER is a dedicated page carrying the exact approved subtitle",
                  len(accessible_cer_pages) == 1
                  and accessible_cer_pages[0].select_one('[data-accessible-cer-subtitle]')
                  .get_text(" ", strip=True) == CER_SUBTITLE)
    results.check("the Student CER carries the same approved subtitle",
                  soup.select_one('[data-student-cer-subtitle]').get_text(" ", strip=True) == CER_SUBTITLE)
    results.check("the Accessible edition presents exactly one task per page",
                  all(len(page.select("[data-shell-task-heading]")) == 1
                      for page in soup.select('.page[data-role="accessible"]')))
    student_prompts = {node["data-persist-id"][1:]
                       for node in soup.select('.page[data-role="student"] [data-response]')
                       if not node.has_attr("data-field") and node["data-persist-id"].startswith("t")}
    accessible_prompts = {node["data-persist-id"][1:]
                          for node in soup.select('.page[data-role="accessible"] [data-response]')
                          if not node.has_attr("data-field") and node["data-persist-id"].startswith("a")}
    results.check("the Accessible edition keeps every Student reasoning prompt",
                  student_prompts == accessible_prompts,
                  sorted(student_prompts ^ accessible_prompts))
    similarity = difflib.SequenceMatcher(
        None, visible_text(soup, ["student"]).split(), visible_text(soup, ["accessible"]).split()
    ).ratio()
    results.check("the Accessible edition is rewritten rather than reflowed",
                  similarity <= 0.70, f"{similarity * 100:.1f}% similar to the Student edition")
    results.check("the Accessible edition carries a lighter reading load than the Student edition",
                  len(visible_text(soup, ["accessible"]).split())
                  < len(visible_text(soup, ["student"]).split()),
                  {"student": len(visible_text(soup, ["student"]).split()),
                   "accessible": len(visible_text(soup, ["accessible"]).split())})
    results.check("the Accessible edition restates every evidence table in its own words",
                  all(phrase in visible_text(soup, ["accessible"]) for phrase in
                      ["no rule was written", "A modeled number", "What it cannot prove alone",
                       "Who says yes first"]))
    results.check("the Answer Key covers the Accessible mechanism wording as well as the Student wording",
                  all(phrase in visible_text(soup, ["answer"]) for phrase in
                      ["the repair pathway stays switched off",
                       "the repair-linked pathway stays quiescent instead of running"]))
    results.check("the Accessible edition carries vocabulary support and scaffolds",
                  bool(soup.select('.page[data-role="accessible"] .vocabulary-list'))
                  and len(soup.select('.page[data-role="accessible"] .alt-support')) >= 5,
                  len(soup.select('.page[data-role="accessible"] .alt-support')))
    results.check("the Accessible edition does not name the diagnosis before Task 6",
                  not any(re.search(r"the shielding (?:removed|reduced)", " ".join(page.stripped_strings), re.I)
                          for page in soup.select('.page[data-role="accessible"]')
                          if [int(n["data-shell-task-heading"])
                              for n in page.select("[data-shell-task-heading]")] < [6]))
    keyed = [item["number"] for item in registry["tasks"] if item.get("keyed")]
    answer_tasks = [node["data-shell-task-heading"]
                    for node in soup.select('.page[data-role="answer"] [data-shell-task-heading]')]
    results.check("the Answer Key supplies an exemplar for every keyed task",
                  sorted(answer_tasks, key=int) == sorted(keyed, key=int)
                  and len(soup.select('.page[data-role="answer"] .answer-block')) >= TASK_COUNT,
                  answer_tasks)
    results.check("Answer Key exemplars preserve the required qualifiers",
                  re.search(r"does not establish", visible_text(soup, ["answer"]), re.I)
                  and "detection limit" in visible_text(soup, ["answer"]))
    results.check("the mechanism model is a five-stage process contract with three student stages",
                  bool(soup.select(f'.pathway-model[data-process-contract="{PROCESS_CONTRACT}"]'))
                  and all(len(model.select("[data-process-stage]")) == 5
                          for model in soup.select(".pathway-model"))
                  and all(len(model.select(".stage-response")) == 3
                          for model in soup.select('.page[data-role="student"] .pathway-model,'
                                                   '.page[data-role="accessible"] .pathway-model')))
    results.check("the correct diagnosis and its three rejected alternatives are declared",
                  bool(registry.get("correctDiagnosis"))
                  and len(registry.get("incorrectAlternatives", [])) == 3)
    results.check("the design task states on the page that no learner prescribes a source, device, or setting",
                  all(re.search(r"not asked to (?:name|choose) a radiation source",
                                visible_text(soup, [role]), re.I)
                      for role in ("student", "accessible")))

    # ── Metadata hygiene and response eligibility ────────────────────
    lifecycle_findings = [
        f"{page.get('data-page-id')}:{match.group(0)}"
        for page in soup.select(".page[data-role]")
        for match in LIFECYCLE_METADATA.finditer(" ".join(page.stripped_strings))
    ]
    results.check("no printable page shows lifecycle, branch, merge, or commit metadata",
                  not lifecycle_findings, lifecycle_findings)
    results.check("the lifecycle-metadata detector fires on a draft banner",
                  bool(LIFECYCLE_METADATA.search(
                      "DRAFT · OWNER_REVIEW_NOT_STARTED on feat/sss-c2-case05-too-clean-room")))
    for edition, block in (("accessible", layout), ("student", layout["student"])):
        declared = {area["persistId"] for area in block["areas"]} | {
            item["persistId"] for item in block["lockedAreas"]}
        present = {node["data-persist-id"]
                   for node in soup.select(f'.page[data-role="{edition}"] [data-response]')}
        results.check(f"every {edition} response is explicitly eligible or locked",
                      declared == present, sorted(declared ^ present))
        cer_ids = {node["data-persist-id"]
                   for node in soup.select(f'.page[data-role="{edition}"] .canonical-cer-response')}
        eligible = {area["persistId"] for area in block["areas"]}
        results.check(f"no eligible {edition} resize area is a CER field", not (eligible & cer_ids),
                      sorted(eligible & cer_ids))
    results.check("the draft ships no owner-applied layout overrides",
                  layout["overrides"] == {} and layout["student"]["overrides"] == {})

    payload = {
        "validator": "sss-c2-case05-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2))
    return 0 if results.passed == len(results.assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
