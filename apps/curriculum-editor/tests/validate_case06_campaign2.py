#!/usr/bin/env python3
"""Case-scoped validation for SSS Campaign 2 Case 06 — The First Garden.

Corrective-release validator. Case 06 is released at v1.1 with the approved v1.0
records retained byte-identical alongside it. It enforces the canonical identity
and runtime linkage of the bonus case, the ledger recorded in
source/task-registry.js, the science boundary that separates established Earth
science from this garden's records, the print geometry of the four roles, and the
corrective-release integrity the Campaign 2 completion audit found missing: the
record must pin a commit that actually contains the sources it certifies, its
recorded validation total must be the total this validator produces, and its
frozen baselines must be unsatisfiable by the markup v1.1 replaced.

The prohibited-claim and precision detectors are self-tested: each must fire on a
synthetic probe carrying the claim it exists to catch, so a detector cannot rot
into a no-op regex without failing the suite.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "shared/validation"))
from corrective_release_lifecycle import history_findings as lifecycle_findings  # noqa: E402

CASE_ID = "SSS-C2-CASE06"
CASE_ROOT = ROOT / "sss/campaign-2/case-06-first-garden"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
RELEASE_VERSION = "1.2"
APPROVAL_DATE = "2026-08-10"
# v1.1 is the release v1.2 corrects and indexes as its prior approved release.
RETAINED_VERSION = "1.1"
RETAINED_APPROVAL_DATE = "2026-08-06"
RETAINED_PINNED_COMMIT = "f3e3ed7fefb375a97594be99d9744fff4d8f6f0b"
V11_SOURCE_HASHES = {
    "content": "8e66f5700268c295c0d2d1d397d4951addc1c676b0d5ae6284e5240a1e44abb9",
    "presentation": "6e3a18bfa050cb4b2900606d30052430eaf03d57c21cffe439c264099c39622d",
    "taskRegistry": "959b0f082f53ca430edf17c8167d679b764a096b47c99c71ab5bf3877aa1f8a8",
    "layoutOverrides": "b76d24211f032b404f8418f6bf862580f19b0f5e383d5f97b9f5e949e996a481",
}
V11_DOM_BASELINES = {
    "student": "747115744832d18302d5cb8b2ed7b900cd6bc5c61a36a7161fe9b642a605fde2",
    "teacher": "2720249b480c71e29b2dee472feaa90ddd990b51922459612a8f53e190b61bb3",
    "answer": "db18da7f4a28beef54e88d4e61bfaaa6cc8654b66dab932a973fba34a379b516",
}
# v1.1 shipped an eight-page Teacher Guide; C2C6-T02/T03/T04 reflowed it to the common
# seven-page architecture at v1.2. Learner and Answer Key page counts are unchanged.
V11_ROLE_PAGES = {"student": 6, "teacher": 8, "answer": 5, "accessible": 7}
# v1.0 remains retained beneath v1.1 as the case's first approved release.
LEGACY_VERSION = "1.0"
LEGACY_APPROVAL_DATE = "2026-08-05"
OWNER = "Nate / Owner"
RETAINED_RELEASE_COMMIT = "59005a86cbaf858fe68684aedb2607dd773e3f2c"
TOTAL_ASSERTIONS = 230  # asserted against the live count below, and against the recorded figure
# The superseded figure language, which must survive nowhere: not in a role, not in the
# ledger of record, not in the README, and not in the release or approval records.
STRIP = re.compile(r"twelve[- ]met(?:re|er)|\bthe strip\b|\balong a strip\b", re.I)
RUNTIME_ID = "first_garden"
RUNTIME_NAME = "The First Garden"
RUNTIME_LOCATION = "Restored Terrace"
RUNTIME_SUBTITLE = "Earth"
CASE_SUBTITLE = "Campaign 2 · Case 06 · Restored Terrace, Earth"
DISPLAY_LABEL = "6 - The First Garden"
ROLES = ["student", "teacher", "answer", "accessible"]
ROLE_PAGES = {"student": 6, "teacher": 7, "answer": 5, "accessible": 7}

TASK_IDS = [f"C2-C06-T{n}" for n in range(1, 8)]
TASK_TITLES = [
    "Sort What Was Tested from What Was Never Tested",
    "Read the Pattern in the Site Survey",
    "Weigh the Explanations",
    "Show Where the Five Sources Converge",
    "Model the Candidate Pathway",
    "Explain the Diagnosis with CER",
    "Specify the Screened, Approved Trial",
]
FORMAL_CLUES = ["RESTORATION_HISTORY", "CHEMICAL_DISCONNECTION", "MYCORRHIZAL_NETWORK",
                "CONCORD_REGULATION", "DATABASE_PRECEDENT"]
FIGURE_IDS = {"fig-patches-student", "fig-patches-accessible"}
PROCESS_CONTRACT = "mycorrhizal-candidate-five-stage-v1.0"
CER_SUBTITLE = ("You may write sentences or use bullet points. "
                "Use evidence from more than one source.")

# ── Detector guards ──────────────────────────────────────────────────────────
# A rule fires only when its pattern appears WITHOUT a nearby guard phrase. This
# is what lets the Teacher Guide name a misconception in order to correct it,
# while an unqualified assertion of the same claim still fails.
NEGATION = re.compile(r"\bnot\b|\bnever\b|\bcannot\b|\bno\s+(?:support|evidence)\b|\bdoes\s+not\b"
                      r"|\bboundary\s+against\b"
                      r"|\bis\s+not\b|\brather\s+than\b|\bwithout\b|\bdeclines\b|\bunsupported\b", re.I)
CANDIDATE = re.compile(r"\bcandidate\b|\bmay\b|\bcould\b|\bleading\s+explanation\b|\bhypothes|\bto\s+be\s+tested\b"
                       r"|\btest(?:ed|ing)?\b|\bnot\b|\bnever\b", re.I)
SAFEGUARD = re.compile(r"\bscreen|\bapprov|\bcontrol|\breview|\bprovenance|\bmonitor|\bidentif|\bbefore\b"
                       r"|\buntil\b|\bnot\b|\bnever\b", re.I)
DETECTED = re.compile(r"\btrace\b|\bdetected\b|\bpresent\b|\bnot\b|\bnever\b", re.I)
ESTIMATE_NEAR = re.compile(r"\bestimate|\bglobal\b|\bpublished\b|\bnot\b|\bflux\b", re.I)
NEVER = re.compile(r"(?!x)x")  # never matches, so the rule fires unconditionally

PROHIBITED: list[tuple[re.Pattern, re.Pattern, str]] = [
    (re.compile(r"wood\s+wide\s+web", re.I), NEGATION, "the soil described as a wood wide web"),
    (re.compile(r"underground\s+internet|forest'?s?\s+own\s+internet", re.I), NEGATION,
     "the network described as an internet"),
    (re.compile(r"superorganism|single\s+(?:cooperative\s+)?organism|one\s+cooperative\s+mind", re.I), NEGATION,
     "the forest or garden described as one organism"),
    (re.compile(r"mother\s+tree", re.I), NEGATION, "mature trees preferentially feeding their own seedlings"),
    (re.compile(r"(?:the\s+)?(?:proven|established|demonstrated)\s+mechanism", re.I), NEGATION,
     "the mycorrhizal explanation asserted as an established mechanism"),
    (re.compile(r"\bthis\s+is\s+the\s+mechanism\b|\bis\s+the\s+mechanism\b", re.I), NEGATION,
     "the mechanism stated as proven"),
    (re.compile(r"(?:fungi|partners|network)\s+are\s+(?:definitely\s+|certainly\s+)?(?:gone|absent|missing)", re.I),
     CANDIDATE, "compatible partners declared certainly absent"),
    (re.compile(r"never\s+(?:been\s+|fully\s+)?restored", re.I), NEVER,
     "the network declared never restored as a matter of fact"),
    (re.compile(r"guaranteed\s+cure|will\s+(?:definitely\s+)?fix\s+the\s+garden|is\s+a\s+cure", re.I), NEGATION,
     "inoculation presented as a guaranteed cure"),
    (re.compile(r"\bwill\s+recover\b|\bwill\s+return\s+to\s+normal\b", re.I), NEGATION,
     "recovery asserted as a certainty"),
    (re.compile(r"\brecover\s+(?:within|in)\s+\w+\s+(?:weeks?|months?|years?|seasons?)", re.I), NEVER,
     "a recovery time promised before evidence"),
    (re.compile(r"transplant\s+living\s+soil|\binoculate\s+now\b|move\s+the\s+soil\s+(?:over|across)", re.I),
     SAFEGUARD, "unscreened living-soil transfer proposed"),
    (re.compile(r"no\s+risk|risk[- ]free|perfectly\s+safe", re.I), NEGATION,
     "a within-world transfer described as risk-free"),
    (re.compile(r"(?:ignore|skip|waive|bypass)\s+(?:the\s+)?(?:regulation|review|approval|section\s*14\.7)", re.I),
     NEGATION, "the review requirement waived"),
    (re.compile(r"always\s+(?:move|moves|share|shares|benefit|benefits)\s", re.I), NEGATION,
     "transfer through shared pathways asserted as universal"),
    (re.compile(r"clean\s+(?:chemistry|panels?|results?)\s+(?:proves?|shows?)\s+", re.I), NEGATION,
     "clean chemistry treated as proof the biology is intact"),
    (re.compile(r"chemistry\s+proves\s|survey\s+proves\s", re.I), NEGATION,
     "the chemical survey treated as proof of which organism is missing"),
    (re.compile(r"all\s+(?:land\s+)?plants\s+(?:need|require)\b", re.I), NEGATION,
     "mycorrhizal fungi claimed to be required by all plants"),
    (re.compile(r"110\s+quadrillion|13\.12\s+gigatons?", re.I), ESTIMATE_NEAR,
     "a published global estimate presented without its estimate framing"),
    (re.compile(r"(?:carbon\s+)?stored\s+(?:each|per)\s+year|permanent(?:ly)?\s+stor", re.I), NEGATION,
     "annual carbon allocation presented as permanent storage"),
    (re.compile(r"(?:fungi|plants|roots)\s+(?:decide|decides|chose|choose|want|wants)\b", re.I), NEGATION,
     "intention attributed to fungi or plants"),
    (re.compile(r"\bbuy\b.*\binoculant\b|\binoculant\s+(?:product|supplier|brand)", re.I), NEGATION,
     "a commercial inoculant product or supplier named"),
    (re.compile(r"(?:the\s+)?(?:tests?|panels?)\s+were\s+wrong|restoration\s+(?:team\s+)?was\s+incompetent", re.I),
     NEGATION, "the restoration team or its tests blamed as incompetent"),
]

PRECISION: list[tuple[re.Pattern, re.Pattern, str]] = [
    (re.compile(r"between\s+the\s+patches[^.]{0,60}\b(?:zero|none|absent|nothing)\b", re.I), NEGATION,
     "trace levels between patches restated as zero or absent"),
    (re.compile(r"\bexactly\s+(?:four|five|six)\s+met(?:re|er)s\b|\bpatches\s+are\s+5\s*m\b", re.I), NEGATION,
     "the approximate patch-diameter range collapsed to an exact value"),
    (re.compile(r"\bfive\s+met(?:re|er)s?\s+(?:in\s+)?diameter\b", re.I), NEGATION,
     "an averaged patch diameter invented from the reported range"),
    (re.compile(r"\b(?:41|42|43|44)\s+years\b|\bfifty\s+years\s+of\s+remediation\b", re.I), NEVER,
     "the forty-year restoration period restated inaccurately"),
    (re.compile(r"\bsix\s+years\s+of\s+cover\s+crop", re.I), NEVER,
     "six species rotations restated as six years"),
]


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


def role_dom_hash(soup: BeautifulSoup, role: str) -> str:
    """The frozen non-Accessible DOM baseline, computed exactly as validate_static does."""
    fragment = BeautifulSoup("".join(str(page) for page in soup.select(f'.page[data-role="{role}"]')),
                             "html.parser")
    for node in list(fragment.find_all(string=True)):
        if isinstance(node, NavigableString) and not str(node).strip():
            node.extract()
    return hashlib.sha256(fragment.decode(formatter="minimal").encode("utf-8")).hexdigest()


def read_record(path: Path) -> dict:
    """Read a history record defensively.

    A deleted or malformed record must fail the assertion that names it, not crash the
    run and reduce every later protection to "validator crashed".
    """
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def task_registry(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    payload = re.sub(r"^\s*window\.[A-Z0-9_]+\s*=\s*", "", text).rstrip().removesuffix(";")
    return json.loads(payload)


def visible_text(soup: BeautifulSoup, roles: list[str]) -> str:
    selector = ",".join(f'.page[data-role="{role}"]' for role in roles)
    return " ".join(" ".join(page.stripped_strings) for page in soup.select(selector))


def asserted_text(content: str, roles: list[str]) -> str:
    working = BeautifulSoup(content, "html.parser")
    for node in working.select("[data-quoted-claim]"):
        node.decompose()
    return visible_text(working, roles)


def unqualified(text: str, pattern: re.Pattern, guard: re.Pattern,
                before: int = 130, after: int = 90) -> bool:
    return any(not guard.search(text[max(0, m.start() - before):m.end() + after])
               for m in pattern.finditer(text))


def scan(text: str, bank: list) -> list[str]:
    return [reason for pattern, guard, reason in bank if unqualified(text, pattern, guard)]


def probe(markup: str) -> str:
    """Visible text of a synthetic single-page document, used to self-test the detectors."""
    return visible_text(BeautifulSoup(
        f'<main><section class="page" data-role="student" data-page-id="probe">{markup}</section></main>',
        "html.parser"), ["student"])


def page_tasks(page) -> list[int]:
    return [int(h["data-shell-task-heading"]) for h in page.select("[data-shell-task-heading]")]


def main() -> int:
    results = Results()
    package = json.loads((SOURCE / "case-package.json").read_text(encoding="utf-8"))
    registry = task_registry(SOURCE / "task-registry.js")
    content = (SOURCE / "content.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(content, "html.parser")
    layout = json.loads((SOURCE / "layout-overrides.json").read_text(encoding="utf-8"))
    ledger = registry["numericalLedger"]

    role_text = {role: visible_text(soup, [role]) for role in ROLES}
    student_text, teacher_text = role_text["student"], role_text["teacher"]
    answer_text, accessible_text = role_text["answer"], role_text["accessible"]

    # ── Canonical identity, bonus status, and runtime linkage ────────
    results.check("the package carries the canonical Case 06 identity",
                  package["id"] == CASE_ID and package["curriculum"] == "SSS"
                  and package["campaign"] == "campaign-2" and package["title"] == RUNTIME_NAME,
                  package["id"])
    results.check("the printable subtitle names Campaign 2, Case 06, and the runtime location",
                  package["subtitle"] == CASE_SUBTITLE
                  and soup.select_one(".mission-subtitle").get_text(strip=True) == CASE_SUBTITLE,
                  package["subtitle"])
    results.check("the registry ledger pins the runtime case, name, location, and subtitle",
                  (registry["runtimeCaseId"], registry["runtimeInvestigationName"],
                   registry["runtimeLocation"], registry["runtimeSubtitle"])
                  == (RUNTIME_ID, RUNTIME_NAME, RUNTIME_LOCATION, RUNTIME_SUBTITLE),
                  registry["runtimeCaseId"])
    results.check("the ledger records the canonical bonus status and campaign position",
                  registry["runtimeBonusCase"] is True and registry["runtimeCampaignPosition"] == 6,
                  (registry.get("runtimeBonusCase"), registry.get("runtimeCampaignPosition")))
    results.check("the ledger records the runtime unlock condition",
                  "five main Campaign 2 cases" in registry["runtimeUnlockCondition"]
                  and "Hidden" in registry["runtimeUnlockCondition"],
                  registry["runtimeUnlockCondition"])
    results.check("the ledger pins the frozen game baseline",
                  registry["gameCommit"] == GAME_COMMIT, registry["gameCommit"])
    results.check("the package location matches the runtime location",
                  package["location"] == RUNTIME_LOCATION, package["location"])
    results.check("no printable role exposes the runtime case id or an internal clue tag",
                  not any(token in text for text in role_text.values()
                          for token in [RUNTIME_ID] + FORMAL_CLUES),
                  [token for token in [RUNTIME_ID] + FORMAL_CLUES
                   if any(token in text for text in role_text.values())])

    # ── Approved corrective-release lifecycle ────────────────────────
    results.check("the package records the approved corrective-release lifecycle",
                  package["status"] == "APPROVED_STABLE" and package["version"] == RELEASE_VERSION
                  and package["approval"] == {"date": APPROVAL_DATE, "owner": OWNER,
                                              "status": "APPROVED", "printStatus": "PASS"},
                  package["approval"])
    release_path = CASE_ROOT / f"history/release-v{RELEASE_VERSION}.json"
    release_approval_path = CASE_ROOT / f"history/CASE06_OWNER_APPROVAL_v{RELEASE_VERSION}.md"
    results.check("the approved package names its own v1.2 release record",
                  package.get("releaseHistory") == release_path.relative_to(ROOT).as_posix()
                  and release_path.is_file() and release_approval_path.is_file())
    results.check("the task registry records the same approved corrective lifecycle",
                  (registry.get("version"), registry.get("status"), registry.get("approvalDate"),
                   registry.get("approvedBy"), registry.get("ownerReviewStatus"),
                   registry.get("printStatus"), registry.get("mergeStatus"),
                   registry.get("correctiveOf"))
                  == (RELEASE_VERSION, "APPROVED_STABLE", APPROVAL_DATE, OWNER,
                      "OWNER_REVIEW_PASS", "PASS", "READY_TO_MERGE", RETAINED_VERSION),
                  (registry.get("status"), registry.get("correctiveOf")))
    results.check("the shared corrective-release lifecycle rules are satisfied",
                  not lifecycle_findings(CASE_ROOT, CASE_ID, package, registry),
                  lifecycle_findings(CASE_ROOT, CASE_ID, package, registry))
    results.check("the case retains exactly the v1.0, v1.1 and v1.2 history records",
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir())
                  == [f"CASE06_OWNER_APPROVAL_v{LEGACY_VERSION}.md",
                      f"CASE06_OWNER_APPROVAL_v{RETAINED_VERSION}.md",
                      f"CASE06_OWNER_APPROVAL_v{RELEASE_VERSION}.md",
                      f"release-v{LEGACY_VERSION}.json",
                      f"release-v{RETAINED_VERSION}.json",
                      f"release-v{RELEASE_VERSION}.json"],
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir()))

    # ── The v1.1 release record ──────────────────────────────────────
    release = read_record(release_path)
    results.check("the v1.2 release record identifies the corrective release it describes",
                  release.get("caseId") == CASE_ID
                  and release.get("curriculumVersion") == RELEASE_VERSION
                  and release.get("correctiveOf") == RETAINED_VERSION
                  and release.get("status") == "APPROVED_STABLE"
                  and release.get("approvalDate") == APPROVAL_DATE
                  and release.get("owner") == OWNER)
    results.check("the v1.2 release record pins the approved page counts",
                  release.get("rolePageCounts") == ROLE_PAGES, release.get("rolePageCounts"))
    results.check("the v1.2 release record pins all four source hashes, layout overrides included",
                  release.get("sourceHashes") == package["sourceHashes"]
                  and set(release.get("sourceHashes", {}))
                  == {"content", "presentation", "taskRegistry", "layoutOverrides"},
                  sorted(release.get("sourceHashes", {})))
    results.check("the v1.2 release record records the approved print gate",
                  release.get("acceptedPrintStatus") == "PASS at 100% / Actual Size"
                  and release.get("acceptedValidation", {}).get("status") == "PASS")
    accepted = release.get("acceptedValidation", {})
    results.check("the v1.2 release record records the accepted validation totals",
                  all(str(accepted.get(key, "")).startswith(value) for key, value in
                      (("static", "597/597"), ("browser", "2161/2161"), ("pdf", "316/316"),
                       ("correctiveReleaseLifecycle", "25/25"), ("case06Mutations", "28/28"),
                       ("case01Scoped", "74/74"), ("case02Scoped", "108/108"),
                       ("case03Scoped", "107/107"), ("case04Scoped", "82/82"),
                       ("case05Scoped", "101/101")))
                  and accepted.get("gitDiffCheck") == "clean",
                  accepted)
    # The audit found three Campaign 2 records whose accepted-validation figures their own
    # suites never produced. This case's figure is checked against the live total instead.
    results.check("the recorded Case 06 total is the total this validator actually produces",
                  str(accepted.get("case06Scoped", "")).startswith(
                      f"{TOTAL_ASSERTIONS}/{TOTAL_ASSERTIONS}"),
                  str(accepted.get("case06Scoped", ""))[:24])
    results.check("the v1.2 release record declares no generated artifacts",
                  release.get("formerArtifacts", {}).get("status") == "NO_FORMER_GENERATED_ARTIFACTS"
                  and release.get("artifactPolicy") == "NO_GENERATED_ARTIFACTS_COMMITTED"
                  and release.get("retiredArtifacts") == [])
    results.check("the v1.2 release record records the frozen game baseline",
                  any(GAME_COMMIT in note for note in release.get("migrationNotes", []))
                  and registry["gameCommit"] == GAME_COMMIT)
    results.check("the v1.2 release record keeps the case at its runtime case number",
                  any("not renumbered" in note for note in release.get("migrationNotes", [])))
    results.check("the v1.2 release record describes the plan-view figure, not a superseded one",
                  any("plan view" in note and "not to scale" in note
                      for note in release.get("migrationNotes", []))
                  and not any(STRIP.search(note) for note in release.get("migrationNotes", [])))
    results.check("the v1.2 release record describes the combined Student CER page contract",
                  any("combined-v1.0" in note and "canonical-v1.0" in note
                      for note in release.get("migrationNotes", [])))
    results.check("the v1.2 release record describes the differentiated Accessible presentation",
                  any("same evidence" in note and "presents it differently" in note
                      for note in release.get("migrationNotes", [])))
    summary = release.get("correctionSummary", {})
    results.check("the v1.2 release record explains what the corrective release corrects",
                  {"reason", "corrections", "unchanged"} <= set(summary)
                  and len(summary.get("corrections", [])) >= 8
                  and all(any(token in item for item in summary.get("corrections", []))
                          for token in ("C2C6-T02", "C2C6-T03", "C2C6-T04", "C2C6-ACC01",
                                        "C2C6-ACC02", "Teacher page architecture",
                                        "shared visual layer")),
                  [item[:44] for item in summary.get("corrections", [])])
    results.check("the v1.2 release record pins the whole corrective review, not just its last commit",
                  len(release.get("correctiveReviewCommits", [])) >= 5
                  and all(subprocess.run(["git", "cat-file", "-e", f"{entry['commit']}^{{commit}}"],
                                         cwd=ROOT, capture_output=True).returncode == 0
                          and entry["role"] for entry in release.get("correctiveReviewCommits", [])))
    results.check("every commit reference in the v1.2 release record exists",
                  all(subprocess.run(["git", "cat-file", "-e", f"{release.get(field, '')}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")))
    # The audit found released records pinning a canonicalSourceApprovalCommit that does not
    # contain the source it certifies, because every validator compared record to package and
    # never record to commit. This compares record to commit.
    certified = {}
    for name, filename in (("content", "content.html"), ("presentation", "presentation.css"),
                           ("taskRegistry", "task-registry.js"),
                           ("layoutOverrides", "layout-overrides.json")):
        blob = subprocess.run(
            ["git", "show", f"{release.get('canonicalSourceApprovalCommit', '')}:"
             f"{(SOURCE / filename).relative_to(ROOT).as_posix()}"],
            cwd=ROOT, capture_output=True)
        certified[name] = (hashlib.sha256(blob.stdout).hexdigest()
                           if blob.returncode == 0 else "MISSING")
    results.check("the certified source commit actually contains the sources the record pins",
                  certified == release.get("sourceHashes"),
                  {name: value for name, value in certified.items()
                   if value != release.get("sourceHashes", {}).get(name)})
    results.check("the v1.2 release record pins the live Student, Teacher and Answer Key DOM baselines",
                  all(release.get("frozenNonAccessibleDomBaselines", {}).get(role)
                      == role_dom_hash(soup, role) for role in ("student", "teacher", "answer")),
                  {role: role_dom_hash(soup, role) for role in ("student", "teacher", "answer")})

    # ── v1.1 represented as the canonical prior approved release ─────
    results.check("the v1.2 release record carries v1.1 as a canonical prior release",
                  len(release.get("priorApprovedReleases", [])) == 1
                  and release["priorApprovedReleases"][0].get("version") == RETAINED_VERSION
                  and release["priorApprovedReleases"][0].get("status") == "APPROVED_STABLE"
                  and release["priorApprovedReleases"][0].get("approvalDate") == RETAINED_APPROVAL_DATE,
                  release.get("priorApprovedReleases"))
    prior = (release.get("priorApprovedReleases") or [{}])[0]
    results.check("the prior-release entry indexes the retained v1.0 records",
                  sorted(prior.get("retainedRecords", []))
                  == sorted([f"sss/campaign-2/case-06-first-garden/history/"
                             f"CASE06_OWNER_APPROVAL_v{RETAINED_VERSION}.md",
                             f"sss/campaign-2/case-06-first-garden/history/"
                             f"release-v{RETAINED_VERSION}.json"]))
    results.check("the prior-release entry records the page counts v1.0 was approved with",
                  prior.get("rolePageCounts") == {"student": 6, "teacher": 8,
                                                  "answer": 5, "accessible": 7},
                  prior.get("rolePageCounts"))
    # Unlike Case 03, v1.0 and v1.1 pin the same game baseline, so there is no repin to
    # preserve — but the prior entry must still say so rather than leaving it unstated.
    prior_notes = " ".join(prior.get("notes", []))
    results.check("the prior-release entry records v1.1 as superseded rather than withdrawn",
                  "superseded" in prior_notes and "not withdrawn" in prior_notes,
                  prior_notes[:120])
    results.check("the prior-release entry records that the v1.1 records are retained byte-identical",
                  "retained byte-identical" in prior_notes
                  and "corrected in place" in prior_notes, prior_notes[-200:])
    results.check("no v1.2 baseline or hash can be satisfied by the superseded v1.1 markup",
                  bool(prior)
                  and prior.get("frozenNonAccessibleDomBaselines", {}).get("teacher")
                  != release.get("frozenNonAccessibleDomBaselines", {}).get("teacher")
                  and all(prior.get("sourceHashes", {}).get(name)
                          != release.get("sourceHashes", {}).get(name)
                          for name in ("content", "taskRegistry"))
                  and "deliberately identical"
                  in release.get("frozenNonAccessibleDomBaselines", {}).get("note", ""))
    results.check("every commit reference in the prior-release entry exists",
                  bool(prior) and all(
                      subprocess.run(["git", "cat-file", "-e", f"{prior[field]}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("approvalCommit", "recoveryCommit",
                                    "canonicalSourceApprovalCommit")))

    # ── The retained v1.0 records, unchanged ─────────────────────────
    history_path = CASE_ROOT / f"history/release-v{RETAINED_VERSION}.json"
    history = read_record(history_path)
    results.check("the retained v1.1 record still describes the v1.1 release, not v1.2",
                  history.get("caseId") == CASE_ID
                  and history.get("curriculumVersion") == RETAINED_VERSION
                  and history.get("status") == "APPROVED_STABLE"
                  and history.get("approvalDate") == RETAINED_APPROVAL_DATE
                  and history.get("owner") == OWNER
                  and history.get("rolePageCounts") == V11_ROLE_PAGES,
                  history.get("rolePageCounts"))
    results.check("the retained v1.1 record was not rewritten to describe v1.2 content",
                  bool(history)
                  and all(history["sourceHashes"][name] != package["sourceHashes"][name]
                          for name in ("content", "taskRegistry"))
                  and history.get("correctiveOf") == LEGACY_VERSION
                  and [e.get("version") for e in history.get("priorApprovedReleases", [])]
                  == [LEGACY_VERSION])
    legacy = read_record(CASE_ROOT / f"history/release-v{LEGACY_VERSION}.json")
    results.check("the retained v1.0 record keeps its own understated validation figures",
                  legacy.get("acceptedValidation", {}).get("case06Scoped") == "148/148"
                  and legacy.get("acceptedValidation", {}).get("static") == "576/576",
                  legacy.get("acceptedValidation", {}).get("case06Scoped"))
    results.check("the retained v1.0 record pins the frozen game baseline and declares no former artifacts",
                  any(GAME_COMMIT in note for note in legacy.get("migrationNotes", []))
                  and legacy.get("formerArtifacts", {}).get("status") == "NO_FORMER_GENERATED_ARTIFACTS"
                  and legacy.get("priorApprovedReleases") == []
                  and legacy.get("retiredArtifacts") == [])
    results.check("the retained v1.0 record still records its own accepted print status",
                  str(legacy.get("acceptedPrintStatus", "")).startswith("PASS")
                  and legacy.get("acceptedValidation", {}).get("status") == "PASS")
    results.check("every commit the retained v1.0 record pins exists",
                  all(subprocess.run(["git", "cat-file", "-e", f"{legacy.get(key, '')}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for key in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                  "formerArtifactRecoveryCommit")),
                  legacy.get("canonicalSourceApprovalCommit"))
    results.check("the retained v1.0 record pins the commit that contains the sources it certifies",
                  legacy.get("canonicalSourceApprovalCommit") == RETAINED_RELEASE_COMMIT
                  and subprocess.run(
                      ["git", "cat-file", "-e",
                       f"{RETAINED_RELEASE_COMMIT}:sss/campaign-2/case-06-first-garden/source/content.html"],
                      cwd=ROOT, capture_output=True).returncode == 0)
    approval = (CASE_ROOT / f"history/CASE06_OWNER_APPROVAL_v{LEGACY_VERSION}.md").read_text(encoding="utf-8")
    results.check("the retained v1.0 owner-approval record is unchanged and still describes v1.0",
                  all(token in approval for token in
                      ["APPROVED_STABLE", "OWNER_REVIEW_PASS", "READY_TO_MERGE", RUNTIME_ID,
                       "Physical print at 100% / Actual Size: **PASS**",
                       "Student Mission: 5 pages"])
                  and "1.1" not in approval)
    results.check("the retained v1.0 record carries the deferred campaign-level work",
                  "Campaign-level work deferred" in approval
                  and "CURRENT_PROJECT_STATE.md" in approval)

    # ── The v1.1 owner-approval record ───────────────────────────────
    release_approval = (release_approval_path.read_text(encoding="utf-8")
                        if release_approval_path.is_file() else "")
    results.check("the v1.2 owner-approval record records every gate the release passed",
                  all(token in release_approval for token in
                      ["Nate / Owner", APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS",
                       "READY_TO_MERGE", "Corrective of: **1.1**",
                       "On-screen content and visual review, including grayscale: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**"]),
                  release_approval[:80])
    results.check("the v1.2 owner-approval record records the approved page counts",
                  all(token in release_approval for token in
                      ["Student Mission: 6 pages", "Teacher Guide: 7 pages",
                       "Answer Key: 5 pages", "Accessible Mission: 7 pages"]))
    results.check("the v1.2 owner-approval record documents the timed-procedure correction",
                  "C2C6-T02" in release_approval and "timed procedure" in release_approval)
    results.check("the v1.2 owner-approval record documents the authoritative-source correction",
                  "C2C6-T04" in release_approval
                  and "authoritative reference list" in release_approval)
    results.check("the v1.2 owner-approval record documents the Accessible differentiation",
                  "C2C6-ACC01" in release_approval and "C2C6-ACC02" in release_approval)
    results.check("the v1.2 owner-approval record documents the rubric correction",
                  all(token in release_approval for token in
                      ["C2C6-T03", "4/3/2/1 analytic rubric"]))
    results.check("the v1.2 owner-approval record documents record preservation and no artifacts",
                  "retained byte-identical" in release_approval
                  and "NO_GENERATED_ARTIFACTS_COMMITTED" in release_approval)
    results.check("the v1.2 owner-approval record records the Teacher page reflow",
                  "Teacher page architecture" in release_approval)

    results.check("the case stores no PDFs or screenshots",
                  not [path.name for suffix in ("*.pdf", "*.png", "*.jpg", "*.jpeg")
                       for path in CASE_ROOT.rglob(suffix)])
    results.check("the case stores no generated role document",
                  sorted(path.name for path in CASE_ROOT.rglob("*.html")) == ["content.html"],
                  sorted(path.name for path in CASE_ROOT.rglob("*.html")))
    results.check("the case folder uses the canonical released layout",
                  sorted(p.name for p in CASE_ROOT.iterdir() if p.name != ".DS_Store")
                  == ["README.md", "history", "source"]
                  and sorted(p.name for p in SOURCE.iterdir() if p.name != ".DS_Store")
                  == ["case-package.json", "content.html", "layout-overrides.json",
                      "presentation.css", "task-registry.js"],
                  sorted(p.name for p in SOURCE.iterdir()))

    # ── Registry entry, positional numbering, and display label ──────
    case_registry = json.loads((ROOT / "shared/implementation/case-registry.v2.json")
                               .read_text(encoding="utf-8"))
    campaigns = {campaign["id"]: campaign["cases"]
                 for curriculum in case_registry["curricula"] for campaign in curriculum["campaigns"]}
    results.check("Campaign 1 still registers exactly seven cases", len(campaigns["campaign-1"]) == 7,
                  len(campaigns["campaign-1"]))
    results.check("Campaign 2 registers exactly Cases 01 to 06 in numerical display order",
                  [case["id"] for case in campaigns["campaign-2"]]
                  == [f"SSS-C2-CASE0{n}" for n in range(1, 7)]
                  and [case["displayOrder"] for case in campaigns["campaign-2"]] == [8, 9, 10, 11, 12, 13],
                  [(case["id"], case["displayOrder"]) for case in campaigns["campaign-2"]])
    entry = campaigns["campaign-2"][5]
    results.check("Case 06 is the sixth Campaign 2 case and is labelled positionally",
                  entry["id"] == CASE_ID and entry["displayLabel"] == DISPLAY_LABEL,
                  (entry["id"], entry["displayLabel"]))
    results.check("the display label carries no bonus, epilogue, or special-investigation wording",
                  not re.search(r"bonus|epilogue|special|finale|secret", entry["displayLabel"], re.I),
                  entry["displayLabel"])
    results.check("the Case 06 registry entry is the approved v1.2 corrective release",
                  entry["status"] == "APPROVED_STABLE" and entry["packageStatus"] == "APPROVED"
                  and entry["version"] == RELEASE_VERSION
                  and entry.get("historyRecord")
                  == f"sss/campaign-2/case-06-first-garden/history/release-v{RELEASE_VERSION}.json"
                  and entry["approval"] == {"date": APPROVAL_DATE, "owner": OWNER,
                                            "status": "APPROVED", "printStatus": "PASS"},
                  entry)
    results.check("all thirteen registered cases are approved or valid corrective candidates",
                  not unexpected_lifecycle(campaigns)
                  and sum(len(cases) for cases in campaigns.values()) == 13,
                  unexpected_lifecycle(campaigns)
                  or sum(len(cases) for cases in campaigns.values()))
    results.check("no Campaign 1 case leaks into Campaign 2 or the reverse",
                  all(case["id"].startswith("SSS-C1-") for case in campaigns["campaign-1"])
                  and all(case["id"].startswith("SSS-C2-") for case in campaigns["campaign-2"]))

    # ── Source hashes ────────────────────────────────────────────────
    hash_targets = {"content": "content.html", "presentation": "presentation.css",
                    "taskRegistry": "task-registry.js", "layoutOverrides": "layout-overrides.json"}
    stale = [key for key, name in hash_targets.items()
             if hashlib.sha256((SOURCE / name).read_bytes()).hexdigest() != package["sourceHashes"][key]]
    results.check("every declared source hash matches its file", not stale, stale)

    # ── Task architecture, order, and page counts ────────────────────
    results.check("the registry declares the seven canonical task identifiers in order",
                  [task["id"] for task in registry["tasks"]] == TASK_IDS,
                  [task["id"] for task in registry["tasks"]])
    results.check("the registry declares the seven canonical task titles in order",
                  [task["title"] for task in registry["tasks"]] == TASK_TITLES,
                  [task["title"] for task in registry["tasks"]])
    results.check("every task is keyed in the Answer Key",
                  all(task["keyed"] for task in registry["tasks"]))
    results.check("every task icon exists in the shared sprite",
                  all(f'id="{task["icon"]}"' in
                      (ROOT / "shared/implementation/editor-shell/v1.0/icons.svg").read_text(encoding="utf-8")
                      for task in registry["tasks"]),
                  [task["icon"] for task in registry["tasks"]])
    results.check("the registry role page counts match the package",
                  registry["roles"] == ROLE_PAGES
                  and {r: package["rolePageStructure"][r]["pageCount"] for r in ROLES} == ROLE_PAGES,
                  registry["roles"])
    for role in ROLES:
        pages = soup.select(f'.page[data-role="{role}"]')
        results.check(f"the {role} edition renders exactly {ROLE_PAGES[role]} pages",
                      len(pages) == ROLE_PAGES[role], len(pages))
        results.check(f"every {role} page declares its position in the aria label",
                      all(page["aria-label"].endswith(f"of {ROLE_PAGES[role]}") for page in pages))
    for role in ("student", "answer", "accessible"):
        order = [n for page in soup.select(f'.page[data-role="{role}"]') for n in page_tasks(page)]
        results.check(f"the {role} edition presents tasks 1 to 7 exactly once, in order",
                      order == list(range(1, 8)), order)
    results.check("the Accessible edition presents at most one task per page",
                  all(len(page_tasks(page)) <= 1 for page in soup.select('.page[data-role="accessible"]')),
                  [page_tasks(p) for p in soup.select('.page[data-role="accessible"]')])
    results.check("no printable role prints a formal Role or Identity field",
                  not re.search(r"\bRole:\s", student_text + accessible_text))

    # ── Five formal clues and source convergence ─────────────────────
    results.check("the ledger records the five canonical formal clues",
                  registry["formalClues"] == FORMAL_CLUES, registry["formalClues"])
    results.check("the source ledger covers all five clues once",
                  [item["clue"] for item in registry["sourceLedger"]] == FORMAL_CLUES)
    results.check("every source ledger entry states both a contribution and a limit",
                  all(item["establishes"].strip() and item["cannotEstablishAlone"].strip()
                      for item in registry["sourceLedger"]))
    results.check("every clue is covered by at least one task",
                  set(registry["clueTaskCoverage"]) == set(FORMAL_CLUES)
                  and all(registry["clueTaskCoverage"][c] for c in FORMAL_CLUES))
    ledger_sources = [item["source"] for item in registry["sourceLedger"]]
    results.check("every ledger source is named in the Student edition",
                  all(name in student_text for name in ledger_sources),
                  [n for n in ledger_sources if n not in student_text])
    results.check("the convergence task requires a contribution and a limit for each of the five sources",
                  all(f"t4-c{i}" in content and f"t4-l{i}" in content for i in range(1, 6)))
    results.check("the Answer Key names every source in its convergence answer",
                  all(name.replace("Delegate ", "") in answer_text for name in ledger_sources),
                  [n for n in ledger_sources if n.replace("Delegate ", "") not in answer_text])

    # ── Evidence values, units, inequalities, and precision ──────────
    survey = ledger["surveyedPattern"]
    results.check("the ledger records the patch diameter as an approximate range",
                  survey["patchDiameter"] == "approximately four to six metres",
                  survey["patchDiameter"])
    results.check("the ledger records the between-patch reading as trace levels only",
                  survey["betweenPatches"] == "trace levels only", survey["betweenPatches"])
    results.check("both learner editions print the approximate patch-diameter range",
                  "4–6 m" in student_text and "4–6 m" in accessible_text)
    results.check("the Student edition reproduces the survey wording for the patch diameter",
                  "approximately four to six metres" in student_text)
    results.check("both learner editions print the trace-level wording intact",
                  "Trace levels only" in student_text and "trace levels only" in accessible_text.lower())
    results.check("no printable role converts trace levels into zero, none, or absent",
                  not scan(" ".join(role_text.values()), [PRECISION[0]]))
    compounds = ["phosphorus", "nitrogen", "carbon chains", "auxins", "cytokinins", "strigolactones"]
    results.check("the Student edition names every surveyed compound the record lists",
                  all(term in student_text.lower() for term in compounds),
                  [c for c in compounds if c not in student_text.lower()])
    results.check("the Student edition reports the sharp boundary with its diffusion qualifier",
                  "Sharp, despite adequate matrix diffusion" in student_text)
    results.check("the restoration durations are reproduced exactly",
                  all(v in student_text for v in ["forty years", "Twenty years", "Six species rotations"]),
                  [v for v in ["forty years", "Twenty years", "Six species rotations"] if v not in student_text])
    results.check("the regulation designation is reproduced exactly",
                  "Section 14.7" in teacher_text and "Section 14.7" in answer_text)
    results.check("the ledger records that the case supplies no time series and no calculation",
                  "no time series" in ledger["note"] and "nothing to compute" in ledger["note"],
                  ledger["note"])
    results.check("no printable role invents a timeline, a trend line, or a dated event",
                  not re.search(r"\bmonth\s+[1-9]\b|\bweek\s+[1-9]\b|\btrend\s+line\b", " ".join(role_text.values()),
                                re.I))
    results.check("the global estimates stay out of every student-facing role",
                  not any(re.search(r"110\s+quadrillion|13\.12", role_text[r]) for r in
                          ("student", "accessible", "answer")))

    # ── Science boundary ─────────────────────────────────────────────
    status = registry["sourceStatus"]
    results.check("the ledger separates established Earth science from this garden's records",
                  all(key in status for key in
                      ["establishedEarthScience", "establishedEarthScienceBoundary", "caseSpecificEvidence",
                       "modeledEvidence", "caseInference", "engineeringExtrapolation"]),
                  sorted(status))
    results.check("the ledger states the uncertainty boundary the science register requires",
                  "does not support a universal cooperative network" in status["establishedEarthScienceBoundary"]
                  and "can cause harm" in status["establishedEarthScienceBoundary"])
    results.check("the ledger records the global figures as estimates and the carbon figure as a flux",
                  "global estimates" in status["modeledEvidence"] and "flux" in status["modeledEvidence"])
    results.check("the ledger frames the diagnosis as a candidate cause, not an established mechanism",
                  "candidate cause" in status["caseInference"]
                  and "not an established mechanism" in status["caseInference"])
    results.check("the correct diagnosis is recorded as a candidate to be tested",
                  "candidate cause" in registry["correctDiagnosis"]
                  and "before causation is claimed" in registry["correctDiagnosis"],
                  registry["correctDiagnosis"][:90])
    results.check("the ledger records exactly the three canonical rejected alternatives",
                  len(registry["incorrectAlternatives"]) == 3
                  and all(any(k in alt for k in ("pH", "rrigation", "nvasive"))
                          for alt in registry["incorrectAlternatives"]),
                  registry["incorrectAlternatives"])
    results.check("all three rejected alternatives reach the Student edition",
                  all(k in student_text for k in ("pH imbalance", "Inconsistent irrigation", "Invasive organisms")))
    results.check("the Answer Key supplies the record that rules out each rejected alternative",
                  all(k in answer_text for k in
                      ("pH was corrected", "irrigation uniformity was verified", "predates the summit")),
                  [k for k in ("pH was corrected", "irrigation uniformity was verified", "predates the summit")
                   if k not in answer_text])
    results.check("both learner editions frame the chosen explanation as a candidate",
                  "candidate cause" in student_text and "candidate cause" in accessible_text)
    results.check("the packet states on the page that the diagnosis has not been established",
                  "before causation is claimed" in student_text
                  and "still has to be tested" in accessible_text)
    results.check("the ledger records production cautions covering the superseded design language",
                  any("wood wide web" in c for c in registry["productionCautions"])
                  and any("mother-tree" in c for c in registry["productionCautions"]))

    # ── Prohibited overstatement, with self-tested detectors ─────────
    asserted = asserted_text(content, ROLES)
    prohibited_findings = scan(asserted, PROHIBITED)
    results.check("no printable role asserts a prohibited scientific overstatement",
                  not prohibited_findings, prohibited_findings)
    precision_findings = scan(" ".join(role_text.values()), PRECISION)
    results.check("no printable role degrades the precision of a reported value",
                  not precision_findings, precision_findings)
    results.check("the ledger records at least twenty prohibited claims",
                  len(registry["prohibitedClaims"]) >= 20, len(registry["prohibitedClaims"]))

    misconception_probes = [
        ("wood wide web", "<p>The soil is a wood wide web linking every plant together.</p>"),
        ("underground internet", "<p>The garden runs on an underground internet.</p>"),
        ("superorganism", "<p>The forest is a superorganism.</p>"),
        ("mother tree", "<p>A mother tree feeds its own seedlings first.</p>"),
        ("established mechanism", "<p>This is the established mechanism behind the patches.</p>"),
        ("is the mechanism", "<p>Missing fungi is the mechanism here.</p>"),
        ("partners absent", "<p>The compatible fungi are definitely gone from the expansion beds.</p>"),
        ("never restored", "<p>The network was never fully restored after the damage.</p>"),
        ("guaranteed cure", "<p>Adding fungi is a guaranteed cure for this garden.</p>"),
        ("recovery certain", "<p>The garden will recover once the fungi go in.</p>"),
        ("recovery time", "<p>The beds will recover within three seasons.</p>"),
        ("unscreened transfer", "<p>Transplant living soil from the good beds straight into the bad ones.</p>"),
        ("risk free", "<p>Both are on Earth, so the move is risk-free.</p>"),
        ("waive review", "<p>The garden is urgent, so we can skip the approval.</p>"),
        ("universal transfer", "<p>Nutrients always move to the plants that need them most.</p>"),
        ("clean chemistry proof", "<p>The clean panels prove the soil biology is fine.</p>"),
        ("survey proves", "<p>The chemistry proves the mycorrhizal fungi are what is missing.</p>"),
        ("all plants require", "<p>All land plants need mycorrhizal fungi to live.</p>"),
        ("global estimate", "<p>There are 110 quadrillion kilometres of hyphae under this garden.</p>"),
        ("carbon storage", "<p>Mycorrhizal fungi permanently store that carbon underground.</p>"),
        ("intention", "<p>The fungi decide which plants to help.</p>"),
        ("product named", "<p>Buy a commercial inoculant product and spread it.</p>"),
        ("blame", "<p>The soil tests were wrong all along.</p>"),
    ]
    undetected = [name for name, markup in misconception_probes if not scan(probe(markup), PROHIBITED)]
    results.check("every misconception detector fires on the claim it exists to catch",
                  not undetected, undetected)
    results.check("the misconception probe set covers every prohibited-claim rule",
                  len(misconception_probes) == len(PROHIBITED),
                  (len(misconception_probes), len(PROHIBITED)))

    precision_probes = [
        ("trace to zero", "<p>Between the patches there is nothing at all.</p>"),
        ("exact diameter", "<p>The patches are exactly five metres across.</p>"),
        ("averaged diameter", "<p>Each patch is five metres in diameter.</p>"),
        ("wrong period", "<p>The family spent fifty years of remediation on the land.</p>"),
        ("rotations as years", "<p>She tried six years of cover cropping.</p>"),
    ]
    undetected_precision = [name for name, markup in precision_probes if not scan(probe(markup), PRECISION)]
    results.check("every precision detector fires on the degradation it exists to catch",
                  not undetected_precision, undetected_precision)

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
    results.check("the Teacher Guide names the prohibited claims for correction",
                  "Claims to correct on sight" in teacher_text)
    results.check("the Teacher Guide supplies a correction for the quoted claims",
                  "The corrections are, in order" in teacher_text)

    # ── Figures ──────────────────────────────────────────────────────
    figures = soup.select("figure[data-figure-id]")
    results.check("the content carries exactly the declared figures",
                  {f["data-figure-id"] for f in figures} == FIGURE_IDS
                  and {item["id"] for item in registry["figureProvenance"]} == FIGURE_IDS,
                  sorted(f["data-figure-id"] for f in figures))
    results.check("every figure is curriculum-original",
                  all(item["kind"].startswith("curriculum-original") for item in registry["figureProvenance"]))
    results.check("figures appear only in the two learner editions",
                  all(f.find_parent(class_="page")["data-role"] in ("student", "accessible") for f in figures))
    for figure in figures:
        fid = figure["data-figure-id"]
        caption = figure.find("figcaption").get_text(" ", strip=True)
        desc = figure.select_one(".extended-description")
        svg = figure.find("svg")
        title = svg.find("title") if svg else None
        results.check(f"{fid} carries a lettered figure number and a useful caption",
                      bool(re.match(r"Figure [A-Z] · ", caption)) and len(caption) > 90, caption[:80])
        results.check(f"{fid} names its source boundary in the caption",
                      "site survey record" in caption, caption[-70:])
        results.check(f"{fid} states in its caption that no shape joins the readings",
                      "no boundary shape is drawn" in caption or "no shape is drawn" in caption, caption[-70:])
        results.check(f"{fid} carries an extended description that opens with the standard prefix",
                      desc is not None and desc.get_text(strip=True).startswith("Extended description: "))
        results.check(f"{fid} states in its extended description that it is not a map",
                      "not a map" in desc.get_text(" ", strip=True))
        results.check(f"{fid} states that it reads without colour",
                      "without colour" in desc.get_text(" ", strip=True))
        results.check(f"{fid} is labelled for assistive technology",
                      svg is not None and svg.get("role") == "img" and svg.get("aria-label")
                      and title is not None and title.get_text(strip=True) == svg["aria-label"])
        patterned = [n for n in svg.select("rect, circle")
                     if str(n.get("fill", "")).startswith("url(")]
        results.check(f"{fid} encodes its zones with fill patterns rather than colour",
                      len(svg.select("pattern")) >= 2 and len(patterned) >= 4, len(patterned))
        results.check(f"{fid} draws no curve, polyline, or polygon",
                      not svg.select("polyline") and not svg.select("polygon")
                      and not any(re.search(r"[CcSsQqTtAa]", p.get("d", "")) for p in svg.select("path")))
        results.check(f"{fid} labels both kinds of ground directly on the figure",
                      "compounds abundant" in svg.get_text(" ", strip=True)
                      and "trace levels only" in svg.get_text(" ", strip=True))
    results.check("figure numbering is unique within each learner edition",
                  all(len({re.match(r"Figure ([A-Z])", f.find("figcaption").get_text(strip=True)).group(1)
                           for f in soup.select(f'.page[data-role="{role}"] figure[data-figure-id]')})
                      == len(soup.select(f'.page[data-role="{role}"] figure[data-figure-id]'))
                      for role in ("student", "accessible")))
    learner_captions = [t.get_text(strip=True) for role in ("student", "accessible")
                        for t in soup.select(f'.page[data-role="{role}"] table.data-table caption')]
    results.check("every learner-edition table caption carries a table number",
                  all(c.startswith("Table ") for c in learner_captions),
                  [c for c in learner_captions if not c.startswith("Table ")])
    results.check("every table in every role carries a caption with real content",
                  all(len(t.get_text(strip=True)) > 12 for t in soup.select("table.data-table caption"))
                  and len(soup.select("table.data-table")) == len(soup.select("table.data-table caption")),
                  len(soup.select("table.data-table")))
    for role in ("student", "accessible"):
        nums = [re.match(r"Table (\d+)", t.get_text(strip=True)).group(1)
                for t in soup.select(f'.page[data-role="{role}"] table.data-table caption')]
        results.check(f"the {role} edition numbers its tables uniquely", len(nums) == len(set(nums)), nums)

    # ── Teaching analogy containment ─────────────────────────────────
    analogies = soup.select("[data-analogy]")
    results.check("the teaching analogy appears in both learner editions and nowhere else",
                  len(analogies) == 2
                  and {a.find_parent(class_="page")["data-role"] for a in analogies} == {"student", "accessible"},
                  len(analogies))
    results.check("the teaching analogy prints its own disclaimer",
                  all("not a garden record" in a.get_text(" ", strip=True) for a in analogies))
    results.check("the teaching analogy introduces no numeric value at all",
                  not any(re.search(r"\d", a.get_text(" ", strip=True)) for a in analogies),
                  [re.findall(r"\d+", a.get_text(" ", strip=True)) for a in analogies])
    results.check("the analogy never reaches the Answer Key or the Teacher Guide as a task",
                  "building inspector" not in answer_text.lower())

    # ── CER, mechanism model, Accessible differentiation ─────────────
    student_cer_pages = [p for p in soup.select('.page[data-role="student"]') if page_tasks(p) == [6, 7]]
    accessible_cer_pages = soup.select('.page[data-accessible-cer-page="canonical-v1.0"]')
    results.check("the Student CER shares one page with task 7 under the combined contract",
                  len(student_cer_pages) == 1
                  and student_cer_pages[0].get("data-student-cer-page") == "combined-v1.0",
                  [p.get("data-page-id") for p in student_cer_pages])
    results.check("the Accessible CER occupies one dedicated canonical page carrying only task 6",
                  len(accessible_cer_pages) == 1 and page_tasks(accessible_cer_pages[0]) == [6],
                  len(accessible_cer_pages))
    results.check("both learner editions print the canonical CER subtitle verbatim",
                  soup.select_one("[data-student-cer-subtitle]").get_text(strip=True) == CER_SUBTITLE
                  and soup.select_one("[data-accessible-cer-subtitle]").get_text(strip=True) == CER_SUBTITLE)
    results.check("every CER carries CLAIM, EVIDENCE and REASONING in order",
                  all([b.get_text(strip=True) for b in cer.select(".canonical-cer-label")]
                      == ["CLAIM", "EVIDENCE", "REASONING"] for cer in soup.select(".canonical-cer")),
                  len(soup.select(".canonical-cer")))
    results.check("the three CER contracts are the canonical student, answer, and accessible forms",
                  sorted(c["data-cer-contract"] for c in soup.select(".canonical-cer"))
                  == ["accessible-v1.0", "answer-v1.0", "student-v1.0"])
    results.check("the CER prompt requires evidence from more than one source",
                  "more than one source" in student_text and "more than one source" in accessible_text)
    results.check("the CER prompt requires a stated limit",
                  "does not establish" in student_text and "does not prove" in accessible_text)
    results.check("the packet asks for no recommendation the evidence cannot settle",
                  "recommendation" not in student_text.lower()
                  and "recommendation" not in accessible_text.lower(),
                  [w for w in ("recommendation",)
                   if w in student_text.lower() or w in accessible_text.lower()])

    models = soup.select(f'[data-process-contract="{PROCESS_CONTRACT}"]')
    results.check("the candidate pathway model appears once in each learner edition",
                  len(models) == 2
                  and {m.find_parent(class_="page")["data-role"] for m in models} == {"student", "accessible"},
                  len(models))
    results.check("every pathway model has five stages with the first and last fixed",
                  all(len(m.select("[data-process-stage]")) == 5
                      and len(m.select(".path-stage.fixed")) == 2 for m in models))
    results.check("every pathway model is fed by an exact-match word bank of three phrases",
                  all(len(bank.select(".word-bank-item")) == 3 for bank in soup.select(".word-bank")),
                  len(soup.select(".word-bank")))
    results.check("the Answer Key supplies both the Student and the Accessible word-bank wordings",
                  "compatible mycorrhizal fungi may not have re-established" in answer_text
                  and "compatible fungi may not have come back in the new beds" in answer_text)
    results.check("the mechanism task requires a stated limit on the model",
                  "does not establish" in student_text and "does not prove" in accessible_text)

    results.check("the Accessible edition is rewritten rather than reflowed",
                  difflib.SequenceMatcher(None, student_text.split(), accessible_text.split()).ratio() <= 0.70,
                  round(difflib.SequenceMatcher(None, student_text.split(),
                                                accessible_text.split()).ratio(), 3))
    results.check("the Accessible edition is shorter than the Student edition",
                  len(accessible_text.split()) < len(student_text.split()),
                  (len(accessible_text.split()), len(student_text.split())))
    results.check("the Accessible edition supplies just-in-time vocabulary as a definition list",
                  len(soup.select('.page[data-role="accessible"] .vocabulary-list')) >= 1)
    results.check("the Accessible edition supplies structured scaffolds on most pages",
                  len(soup.select('.page[data-role="accessible"] .alt-support')) >= 5,
                  len(soup.select('.page[data-role="accessible"] .alt-support')))
    results.check("the Accessible edition supplies sentence frames",
                  accessible_text.count("Sentence frame") >= 3, accessible_text.count("Sentence frame"))
    results.check("the Accessible edition does not name the diagnosis before task 6",
                  not any(re.search(r"mycorrhizal partners may not have re-established", " ".join(p.stripped_strings))
                          for p in soup.select('.page[data-role="accessible"]')
                          if page_tasks(p) and page_tasks(p)[0] < 3))
    results.check("the Student and Accessible editions ask the same reasoning prompts",
                  {n["data-persist-id"][1:] for n in
                   soup.select('.page[data-role="student"] [data-response]') if not n.get("data-field")}
                  == {n["data-persist-id"][1:] for n in
                      soup.select('.page[data-role="accessible"] [data-response]') if not n.get("data-field")})
    results.check("the Teacher Guide and Answer Key contain no learner response areas",
                  not soup.select('.page[data-role="teacher"] [data-response]')
                  and not soup.select('.page[data-role="answer"] [data-response]'))

    # ── Layout overrides and response eligibility ────────────────────
    results.check("the layout overrides target this case with the accessible edition at the root",
                  layout["caseId"] == CASE_ID and layout["edition"] == "accessible"
                  and layout["schemaVersion"] == 1 and layout["stepPx"] == 4)
    results.check("the layout overrides ship with no stored user deltas",
                  layout["overrides"] == {} and layout["student"]["overrides"] == {})
    for edition, block, role in (("accessible", layout, "accessible"), ("student", layout["student"], "student")):
        declared = {a["persistId"] for a in block["areas"]} | {a["persistId"] for a in block["lockedAreas"]}
        rendered = {n["data-persist-id"] for n in soup.select(f'.page[data-role="{role}"] [data-response]')}
        results.check(f"the {edition} layout override set covers exactly the rendered response areas",
                      declared == rendered, sorted(declared ^ rendered))
        results.check(f"every {edition} locked area records a reason",
                      all(a.get("reason") for a in block["lockedAreas"]))
    results.check("the Student CER, table cells, and fixed organisers are not resizable",
                  not any(a["persistId"] in {"t6c", "t6e", "t6r", "t5-m2", "t4-c1"}
                          for a in layout["student"]["areas"]))

    # ── Figure geometry, and the ledger that describes it ────────────────
    # The v1.0 defect: an owner-review revision turned Figure A into a plan view
    # of circular patches, but the Teacher Guide, the README and figureProvenance
    # went on describing a twelve-metre strip, and the drawing kept a dimension
    # line asserting a distance the survey never reports.
    readme = (CASE_ROOT / "README.md").read_text(encoding="utf-8")
    # The corrective-release section exists to name the defect it repaired, so it
    # is read for agreement with the rendered figure but exempt from the scan for
    # surviving strip language.
    readme_current = readme.split("## What v1.1 corrects")[0] + readme.split("## Science boundary")[-1]
    registry_text = (SOURCE / "task-registry.js").read_text(encoding="utf-8")
    strip_survivors = [name for name, body in
                       (("student", student_text), ("teacher", teacher_text),
                        ("answer", answer_text), ("accessible", accessible_text),
                        ("task-registry.js", registry_text), ("README.md", readme_current))
                       if STRIP.search(body)]
    results.check("no role, ledger or README still describes Figure A as a strip",
                  not strip_survivors, strip_survivors)
    results.check("the strip detector fires on the wording it exists to catch",
                  bool(STRIP.search("drawn along a twelve-metre strip"))
                  and bool(STRIP.search("The strip is drawn to show the pattern")))
    for figure in figures:
        fid = figure["data-figure-id"]
        svg = figure.find("svg")
        desc_text = figure.select_one(".extended-description").get_text(" ", strip=True)
        svg_text = svg.get_text(" ", strip=True)
        patches = [c for c in svg.select("circle") if str(c.get("fill", "")).startswith("url(")]
        results.check(f"{fid} renders the plan view its description claims",
                      len(patches) >= 3 and "plan view" in svg["aria-label"].lower()
                      and "plan view" in desc_text.lower(), len(patches))
        # The only quantity the survey reports about the drawing is the diameter range.
        stray = [m.group(0) for m in
                 re.finditer(r"\b\d+(?:[.,]\d+)?\s*m\b", svg_text.replace("4–6 m", ""))]
        results.check(f"{fid} carries no measurement beyond the reported diameter range",
                      not stray, stray)
        results.check(f"{fid} draws no distance between patches",
                      not re.search(r"(?:apart|between (?:the )?(?:circles|patches))[^.]{0,40}"
                                    r"\b(?:met(?:re|er)s?|m)\b", desc_text, re.I)
                      and not re.search(r"\b(?:three|3)\s*(?:met(?:re|er)s|m)\b", svg_text, re.I),
                      desc_text[:120])
        results.check(f"{fid} assigns no measurement to an individual patch",
                      not re.search(r"(?:each|the three drawn here|first|second|third)[^.]{0,60}"
                                    r"\b(?:five|six|four|\d)\s*met(?:re|er)s\b", desc_text, re.I),
                      desc_text[:120])
    provenance = {item["id"]: item for item in registry["figureProvenance"]}
    results.check("figureProvenance describes the rendered plan view, not a superseded figure",
                  all("plan view" in item["shows"].lower() and not STRIP.search(item["shows"])
                      for item in provenance.values()),
                  [i["shows"][:70] for i in provenance.values()])
    results.check("figureProvenance records that the figure is not to scale",
                  all("not to scale" in item["prohibited"].lower() for item in provenance.values()))
    results.check("the figure ledger, the README and the Teacher Guide agree on the plan view",
                  "plan view" in registry["sourceStatus"]["figures"].lower()
                  and "plan view" in readme.lower() and "plan view" in teacher_text.lower())

    # ── Evidence availability: an Answer Key must be producible ──────────────
    # The v1.0 defect: Task 4 graded five sources, and three of them had no
    # printed statement in any learner edition. GC-2201 appeared nowhere a
    # learner could read, and Section 14.7 first appeared a task too late.
    def page_index(role: str, needle: str) -> int:
        """First page (1-based) of that role whose visible text contains needle, else 0."""
        for n, page in enumerate(soup.select(f'.page[data-role="{role}"]'), 1):
            if needle.lower() in " ".join(page.stripped_strings).lower():
                return n
        return 0

    def task_page(role: str, task: int) -> int:
        for n, page in enumerate(soup.select(f'.page[data-role="{role}"]'), 1):
            if task in page_tasks(page):
                return n
        return 0

    SOURCE_EVIDENCE = {
        "Dr. Nova": ["forty years"],
        "Delegate Vorn-Shael": ["trace levels"],
        "Delegate Kess": ["compatible roots", "carbon"],
        "Delegate Ilreth-Mar": ["Section 14.7"],
        "Federation Database": ["GC-2201"],
    }
    results.check("the source-evidence roster covers exactly the five ledger sources",
                  list(SOURCE_EVIDENCE) == [item["source"] for item in registry["sourceLedger"]])
    unavailable = []
    for role in ("student", "accessible"):
        deadline = task_page(role, 4)
        for source, tokens in SOURCE_EVIDENCE.items():
            for token in tokens:
                found = page_index(role, token)
                if not found or found > deadline:
                    unavailable.append(f"{role}: {source} — {token!r} "
                                       f"{'absent' if not found else f'first on page {found}, after Task 4 on {deadline}'}")
    results.check("every source Task 4 grades reports on the learner page, at or before Task 4",
                  not unavailable, unavailable)

    # Nothing the Answer Key names by designation may be invisible to a learner.
    designations = set(re.findall(r"\bGC-\d+\b|\bSection \d+\.\d+\b", answer_text))
    ungrounded = [d for d in sorted(designations)
                  if d.lower() not in student_text.lower() or d.lower() not in accessible_text.lower()]
    results.check("every designation the Answer Key relies on is printed in both learner editions",
                  not ungrounded, ungrounded)

    # ── Accessible answerability ────────────────────────────────────────────
    # The v1.0 defect: the Accessible Task 1 table dropped the record column, so
    # no learner could tell which row was never tested, and Task 3's rejections
    # for pH and for invasive organisms had no record behind them.
    a_task1 = soup.select_one('.page[data-role="accessible"] table.checked-table')
    a_headers = [th.get_text(strip=True) for th in a_task1.select("thead th")]
    results.check("the Accessible Task 1 table carries the record the task is graded on",
                  len(a_headers) == 3 and "record" in a_headers[1].lower(), a_headers)
    a_rows = {tr.find("td").get_text(strip=True):
              [td.get_text(" ", strip=True) for td in tr.select("td")]
              for tr in a_task1.select("tbody tr")}
    results.check("the Accessible Task 1 record identifies the untested category",
                  "never tested" in a_rows["The soil fungal community"][1].lower()
                  and all("never tested" not in cells[1].lower()
                          for row, cells in a_rows.items() if row != "The soil fungal community"),
                  a_rows["The soil fungal community"][1])
    TASK3_EVIDENCE = {
        "pH rejection": "corrected years ago",
        "irrigation rejection": "same water",
        "toxicology record": "toxicology",
        "invasive-organism rejection": "decades",
        "the pattern predates the summit": "before the",
    }
    missing_task3 = [f"{role}: {label}" for role in ("student", "accessible")
                     for label, token in TASK3_EVIDENCE.items()
                     if token not in {"student": student_text, "accessible": accessible_text}[role].lower()]
    results.check("both learner editions carry the record behind every Task 3 rejection",
                  not missing_task3, missing_task3)

    # ── Cross-role references resolve in the role the reader holds ───────────
    # The v1.0 defect: the Student vocabulary table was numbered and the
    # Accessible equivalent was not, so four Teacher and Answer Key references
    # named a table that meant something else in the differentiated edition.
    def numbered_tables(role: str) -> dict[str, str]:
        found = {}
        for cap in soup.select(f'.page[data-role="{role}"] table.data-table caption'):
            match = re.match(r"Table (\d+) · (.+)", cap.get_text(strip=True))
            if match:
                found[match.group(1)] = match.group(2)
        return found

    student_tables, accessible_tables = numbered_tables("student"), numbered_tables("accessible")
    results.check("both learner editions number the same evidence tables",
                  set(student_tables) == set(accessible_tables),
                  sorted(set(student_tables) ^ set(accessible_tables)))

    def topic(caption: str) -> set[str]:
        return {w for w in re.findall(r"[a-z]{4,}", caption.lower())
                if w not in {"what", "that", "have", "does", "must", "will", "each", "they", "this"}}

    divergent = [f"Table {n}: student {student_tables[n]!r} vs accessible {accessible_tables.get(n)!r}"
                 for n in sorted(student_tables)
                 if n in accessible_tables and not (topic(student_tables[n]) & topic(accessible_tables[n]))]
    results.check("a table number means the same record in both learner editions",
                  not divergent, divergent)
    referenced = set(re.findall(r"Table (\d+)", teacher_text + " " + answer_text))
    referenced |= {str(n) for a, b in re.findall(r"Tables (\d+)[–-](\d+)", teacher_text + " " + answer_text)
                   for n in range(int(a), int(b) + 1)}
    unresolved = [f"Table {n}" for n in sorted(referenced, key=int)
                  if n not in student_tables or n not in accessible_tables]
    results.check("every table the Teacher Guide or Answer Key names resolves in both learner editions",
                  not unresolved, unresolved)
    VOCABULARY = re.compile(r"vocabulary|words you will need|working meanings", re.I)
    numbered_vocabulary = [c.get_text(strip=True)
                           for c in soup.select("table.data-table caption")
                           if c.get_text(strip=True).startswith("Table ")
                           and VOCABULARY.search(c.get_text(strip=True))]
    results.check("no vocabulary aid takes an evidence-table number",
                  not numbered_vocabulary, numbered_vocabulary)
    results.check("both learner editions still carry a vocabulary aid, unnumbered",
                  all(any(VOCABULARY.search(node.get_text(" ", strip=True))
                          for node in soup.select(f'.page[data-role="{role}"] '
                                                  '.vocabulary-list, .page[data-role="'
                                                  f'{role}"] .support-heading, .page[data-role="'
                                                  f'{role}"] table.vocabulary-table caption'))
                      for role in ("student", "accessible")))
    results.check("the numbered evidence tables run 1 to N with no gap in either edition",
                  sorted(map(int, student_tables)) == list(range(1, len(student_tables) + 1))
                  and sorted(map(int, accessible_tables)) == list(range(1, len(accessible_tables) + 1)),
                  (sorted(student_tables, key=int), sorted(accessible_tables, key=int)))
    figure_letters = {role: {re.match(r"Figure ([A-Z])", f.find("figcaption").get_text(strip=True)).group(1)
                             for f in soup.select(f'.page[data-role="{role}"] figure[data-figure-id]')}
                      for role in ("student", "accessible")}
    results.check("every figure the Teacher Guide or Answer Key names resolves in both learner editions",
                  set(re.findall(r"Figure ([A-Z])\b", teacher_text + " " + answer_text))
                  <= (figure_letters["student"] & figure_letters["accessible"]),
                  figure_letters)

    # ── Revision propagation: the guide describes the case that shipped ─────
    # The v1.0 defect: four Teacher Guide statements survived a revision that
    # changed the figure, the Student page contract and the Accessible edition.
    for page in soup.select("[data-analogy]"):
        holder = page.find_parent(class_="page")
        role = holder["data-role"]
        results.check(f"the {role} analogy prints inside the task it teaches",
                      page_tasks(holder) and page_tasks(holder)[0] == 1, page_tasks(holder))
        heading = holder.select_one("[data-shell-task-heading]")
        body = holder.decode()
        results.check(f"the {role} analogy prints after the Task 1 heading and before its record",
                      body.index(str(heading)) < body.index(page.decode())
                      < body.index(str(holder.select_one("table.checked-table"))))
    results.check("the Teacher Guide does not claim a full-page CER in both learner editions",
                  not re.search(r"CER occupies a full page in both", teacher_text, re.I)
                  and "combined" in teacher_text.lower())
    results.check("the Student CER page contract the Teacher Guide describes is the one rendered",
                  bool(soup.select_one('[data-student-cer-page="combined-v1.0"]'))
                  and bool(soup.select_one('[data-accessible-cer-page="canonical-v1.0"]')))
    results.check("the Teacher Guide does not claim the Accessible evidence is identical",
                  not re.search(r"the evidence(?:\s+available)?[^.]{0,40}\bare identical\b"
                                r"|evidence and the diagnosis are identical", teacher_text, re.I),
                  [m.group(0) for m in re.finditer(r"[^.]*identical[^.]*\.", teacher_text)])
    results.check("the Teacher Guide describes the Accessible adaptation the case ships",
                  "plainer register" in teacher_text and "sentence frame" in teacher_text.lower())

    # ── Standards claim only what a task assesses ───────────────────────────
    standards = {item["code"]: item for item in registry["standards"]}
    withdrawn = {item["code"]: item for item in registry["standardsWithdrawn"]}
    task_numbers = {int(task["number"]) for task in registry["tasks"]}
    results.check("every retained standard names an alignment, an assessing task, and its evidence",
                  all(item["alignment"] in {"direct", "supporting"}
                      and item["assessedAt"] in task_numbers
                      and len(item["taskEvidence"]) > 120 for item in standards.values()),
                  sorted(standards))
    results.check("every retained standard is named in the Teacher Guide beside its task",
                  all(code in teacher_text for code in standards), sorted(standards))
    results.check("MS-LS2-2 and MS-ETS1-2 are withdrawn and not claimed anywhere",
                  {"MS-LS2-2", "MS-ETS1-2"} <= set(withdrawn)
                  and not ({"MS-LS2-2", "MS-ETS1-2"} & set(standards))
                  and not re.search(r"MS-LS2-2 is (?:the )?direct|MS-LS2-2 is the direct alignment",
                                    teacher_text)
                  and not re.search(r"[Ss]upporting[^.]{0,80}MS-ETS1-2", teacher_text),
                  sorted(withdrawn))
    results.check("each withdrawal records why the task cannot carry the standard",
                  all(len(item["reason"]) > 120 and item["wasClaimed"] in {"direct", "supporting"}
                      for item in withdrawn.values()))
    results.check("no life-science standard was substituted for the withdrawn MS-LS2-2",
                  {c for c in standards if c.startswith("MS-LS")} == {"MS-LS2-3"}, sorted(standards))
    results.check("the ledger records that the withdrawn standards need a task before they return",
                  any("MS-LS2-2" in caution and "MS-ETS1-2" in caution
                      for caution in registry["productionCautions"]))

    # ── Metadata hygiene ─────────────────────────────────────────────
    LIFECYCLE_METADATA = re.compile(
        r"\bDRAFT\b|\bAPPROVED_STABLE\b|OWNER_REVIEW|\bNOT_RUN\b|\bmerge\b|\bbranch\b|feat/|"
        r"\bcommit\b|\bSHA\b|[0-9a-f]{40}", re.I)
    leaked = [role for role, text in role_text.items() if LIFECYCLE_METADATA.search(text)]
    results.check("no printable role prints lifecycle, branch, merge, approval, or production metadata",
                  not leaked, leaked)
    results.check("the lifecycle-metadata detector fires on a draft banner",
                  bool(LIFECYCLE_METADATA.search(
                      "DRAFT · OWNER_REVIEW_NOT_STARTED on feat/sss-c2-case06-first-garden")))
    results.check("no printable role repeats a reminder that the scenario is fictional",
                  not re.search(r"\bfiction(?:al)?\b|\bmade up\b|\bnot real\b", " ".join(role_text.values()), re.I))
    results.check("every response area is labelled for assistive technology",
                  all(n.get("aria-label") or n.get("data-field") for n in soup.select("[data-response]")))
    results.check("no printable role exposes an internal process-contract or persistence identifier as text",
                  PROCESS_CONTRACT not in " ".join(role_text.values()))

    results.check("the declared assertion total is the number this validator actually runs",
                  TOTAL_ASSERTIONS == len(results.assertions) + 1,
                  {"declared": TOTAL_ASSERTIONS, "live": len(results.assertions) + 1})

    payload = {
        "validator": "sss-c2-case06-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2))
    return 0 if results.passed == len(results.assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
