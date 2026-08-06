#!/usr/bin/env python3
"""Case-scoped assertions for SSS Campaign 2 Case 03 — The Wrong Color of Light.

Enforces the frozen source ledger, the five-clue instructional coverage, the figure
contract, the Earth-science/fiction labels, and the prohibited scientific
overstatements against the printable content of every role.

Case 03 is a v1.1 corrective release. The lifecycle assertions therefore require an
approved package that names its own v1.1 records, retains its approved v1.0 records
unchanged, and represents v1.0 as a canonical prior release; and the sections after
the figure contract enforce the defect classes the Campaign 2
completion audit found inside the released v1.0 package: a learner edition that
inverted the packet's own total-PAR reasoning rule, a Task 1 classification asked
before its controlling evidence, an Answer Key reasoning from runtime-only facts, an
invented provenance for the approximate effective-PAR value, and a standards
overclaim that no task assesses.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parents[3]
# Importing the shared lifecycle module must not leave a __pycache__ directory behind:
# no generated artifact is tracked anywhere in this repository.
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "shared/validation"))
from corrective_release_lifecycle import history_findings as lifecycle_findings  # noqa: E402


CASE_ID = "SSS-C2-CASE03"
CASE_ROOT = ROOT / "sss/campaign-2/case-03-wrong-color-light"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
RETAINED_GAME_COMMIT = "46b9387bca95736f164f905596e3dd8b13968661"
RELEASE_VERSION = "1.1"
APPROVAL_DATE = "2026-08-06"
RETAINED_VERSION = "1.0"
RETAINED_APPROVAL_DATE = "2026-08-04"
OWNER = "Nate / Owner"
RUNTIME_ID = "wrong_color_light"
ROLES = ["student", "teacher", "answer", "accessible"]
TASK_TITLES = [
    "Frame What Changed",
    "Read the GRO-9 Spectrum",
    "Compare Lamp Output with Zhal-Kelp Response",
    "Use the Timeline and Controls",
    "Connect the Five Evidence Sources",
    "Diagnose and Reject Alternatives",
    "Explain the Diagnosis with CER",
    "Write a Better Lighting Specification",
]
FORMAL_CLUES = [
    "KELP_DYING_NEW_DOME",
    "LIGHT_SPECTRUM_RED_HEAVY",
    "PIGMENT_MISMATCH",
    "KELP_EVOLVED_DEEP_OCEAN_LIGHT",
    "CHLOROPHYLL_C_BLUE_GREEN",
]
ACCESSIBLE_CER_SUBTITLE = "You may write sentences or use bullet points. Use evidence from more than one source."

# The reasoning rule the whole case turns on. Every role must state it the same way,
# and no role may state its inverse. The released v1.1.0 learner editions printed the
# inverse, which is the defect this pair of patterns exists to make impossible.
TOTAL_PAR_RULE = re.compile(
    r"total PAR alone does not establish an effective spectrum", re.I)
TOTAL_PAR_RULE_INVERTED = re.compile(
    r"total PAR alone\s+(?:proves|establishes|shows|demonstrates|confirms|means)\b"
    r"|total PAR alone\s+proves no\b"
    r"|total PAR\s+(?:proves|establishes)\s+(?:an?\s+|no\s+)?effective spectrum", re.I)
# The four conditions Task 1 asks learners to classify. The controlling record must
# reach both learner editions on or before the task that grades them.
TASK1_CONDITIONS = {
    "light fixture": re.compile(r"fixture", re.I),
    "water and salinity": re.compile(r"water and salinity|water\b.*\bsalinity", re.I),
    "kelp species": re.compile(r"kelp species", re.I),
    "nutrient supply and feed line": re.compile(r"nutrient supply and feed line|feed line", re.I),
}
# Facts the Answer Key reasons from that the learner editions must therefore print.
ANSWER_KEY_EVIDENCE = {
    "the total PAR reading": "280 µmol/m²/s",
    "the old-dome control": "100%",
    "the reported blue-green share": "<5%",
    "the retired fixture's blue-green share": "78%",
    "the strongest measured response band": "460–540 nm",
}
# Runtime-only or Teacher-only enrichment that must never become a graded requirement.
RUNTIME_ONLY_FACTS = {
    "the 30%-higher photon flux": re.compile(r"30\s*%|photon flux", re.I),
    "the approximate effective-PAR value": re.compile(r"14\s*(?:µmol|umol)", re.I),
}
# Provenance the canonical game source does not establish for the approximate value.
UNSUPPORTED_PROVENANCE = re.compile(
    r"incomplete weighting model|weighting model|weighted (?:action )?spectrum model"
    r"|derived from (?:a|an|the) [^.]{0,40}model", re.I)
# A standard is claimed here, in this shape, or it is not claimed at all.
STANDARD_CLAIM = re.compile(
    r"^(Direct assessment|Supporting alignment):\s*(MS-[A-Z0-9-]+)[.,]?\s*(.*)$", re.S)
WITHDRAWN_STANDARDS = ["MS-PS4-2"]

# Values that must appear verbatim wherever the case reports them.
REQUIRED_LEDGER_STRINGS = [
    "280 µmol/m²/s", "62%", "18%", "15%", "78%", "12%", "10%",
    "620–680 nm", "440–490 nm", "490–560 nm", "460–540 nm", "440–460 nm",
    "4.2 °C", "34.8 ppt", "8.1", "7.2 mg/L", "40–120 m",
    "Week 0", "Week 1", "Week 2", "Week 3", "Week 6", "60%", "15% of nominal", "100%",
]
# Inequalities must never be silently converted.
INEQUALITY_PATTERNS = [
    (re.compile(r"(?<![<≤])\b5% (?:blue-green|of (?:the )?output|in the (?:strongest|blue-green))", re.I),
     "blue-green output stated without its inequality"),
    (re.compile(r"(?<![<≤])\b1% red\b", re.I), "OMS-4 red output stated without its inequality"),
    (re.compile(r"below detection\s*(?:=|is|means)\s*(?:zero|0)\b", re.I), "below detection equated with zero"),
]

PROHIBITED = [
    (re.compile(r"\bkelp\s+(?:cannot|can(?:'|’)t|does not|doesn(?:'|’)t)\s+use\s+(?:any\s+)?red\b", re.I),
     "absolute claim that kelp cannot use red light"),
    (re.compile(r"\bred\s+(?:light|photons?)\s+(?:is|are)\s+(?:completely\s+|absolutely\s+)?unused\b", re.I),
     "claim that red light is unused"),
    (re.compile(r"\bred\s+photons?\s+pass\s+through\b", re.I), "claim that red photons pass through unused"),
    (re.compile(r"\bred\s+light\s+is\s+(?:the\s+same\s+as|equivalent\s+to|like)\s+(?:complete\s+)?dark", re.I),
     "red light equated with darkness"),
    (re.compile(r"\bstarv\w*\s+in\s+a\s+brightly\s+lit\b", re.I), "starving-in-a-bright-room mechanism wording"),
    (re.compile(r"\ball\s+brown\s+algae\s+(?:share|use|have)\s+(?:one|the\s+same)\s+action\s+spectrum\b", re.I),
     "universal brown-algae action spectrum"),
    (re.compile(r"\b(?:only|sole)\s+usable\s+(?:range|band|wavelengths)\b", re.I),
     "claim that one band is the only usable range"),
    (re.compile(r"\bnot\s+all\s+photons\s+are\s+created\s+equal\b", re.I), "imprecise photon slogan"),
    (re.compile(r"\bphotobleaching\b", re.I), "photobleaching used without a source-supported definition"),
    (re.compile(r"\bpigment\s+evolution\s+takes\s+millions\s+of\s+years\b", re.I), "universal evolutionary timetable"),
    (re.compile(r"\bdifferent\s+chlorophyll,?\s+completely\s+different\s+wavelengths\b", re.I),
     "overstated pigment/wavelength equivalence"),
    (re.compile(r"\bwill\s+recover\s+within\s+days\b", re.I), "narrated recovery stated as an established result"),
    (re.compile(r"\b(?:effective\s+PAR|usable\s+PAR)\s*(?:of|is|=|:)?\s*(?:~|about\s+)?14\b", re.I),
     "approximate effective-PAR estimate presented as a result"),
    (re.compile(r"\b(?:proves|proving|proof\s+of)\s+(?:the\s+)?(?:diagnosis|cause)\b", re.I),
     "single-source proof language"),
    (re.compile(r"\bzero\s+response\s+outside\b", re.I), "zero response outside the measured band"),
    (re.compile(r"total PAR alone\s+proves\b", re.I), "inverted total-PAR reasoning rule"),
    (re.compile(r"(?:calculate|compute|work out|multiply)[^.]{0,60}effective PAR", re.I),
     "an exact effective-PAR calculation asked of students"),
]
# Curve-drawing SVG constructs are forbidden inside case figures.
CURVE_COMMANDS = re.compile(r"[CcSsQqTtAa]")
# Every zhal-kelp value must be attributed to a measurement made in this case rather than
# presented as established biology. The attribution is enforced semantically: any of these
# provenance phrases satisfies it, and no particular disclaimer wording is required.
PROVENANCE = re.compile(
    r"case data|case sensor data|case-specific|dome sensor data|dome record|sensor readings|"
    r"site measurement|measured at this (?:site|dome)|recorded (?:at this site|for this case|habitat)|"
    r"measured for this case|reported by the case|strongest measured|strongest-response range recorded",
    re.I,
)
# Wording whose only function is to remind the reader that the scenario is invented.
INVENTED_SCENARIO_REMINDER = re.compile(r"\bfictional\b|\bfiction\b", re.I)


class Results:
    def __init__(self) -> None:
        self.assertions: list[dict[str, object]] = []

    def check(self, name: str, passed: bool, detail: object = "") -> None:
        self.assertions.append({"name": name, "pass": bool(passed), "detail": str(detail)})

    @property
    def passed(self) -> int:
        return sum(1 for item in self.assertions if item["pass"])


TOTAL_ASSERTIONS = 107


def role_dom_hash(soup: BeautifulSoup, role: str) -> str:
    """The frozen non-Accessible DOM baseline, computed exactly as validate_static does."""
    fragment = BeautifulSoup("".join(str(page) for page in soup.select(f'.page[data-role="{role}"]')),
                             "html.parser")
    for node in list(fragment.find_all(string=True)):
        if isinstance(node, NavigableString) and not str(node).strip():
            node.extract()
    return hashlib.sha256(fragment.decode(formatter="minimal").encode("utf-8")).hexdigest()


def _walk_entries(node) -> list:
    """Every dict in the registry tree, so the Case 03 entry is found wherever it lives."""
    found = []
    if isinstance(node, dict):
        found.append(node)
        for value in node.values():
            found.extend(_walk_entries(value))
    elif isinstance(node, list):
        for value in node:
            found.extend(_walk_entries(value))
    return found


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

    # ── Source contract and lifecycle ────────────────────────────────
    results.check("package and task registry declare the same case identity",
                  package["id"] == registry["case"] == CASE_ID and package["title"] == registry["title"])
    results.check("task registry pins the frozen game baseline and runtime case id",
                  registry.get("gameCommit") == GAME_COMMIT and registry.get("runtimeCaseId") == RUNTIME_ID,
                  {"gameCommit": registry.get("gameCommit"), "runtimeCaseId": registry.get("runtimeCaseId")})
    results.check("package declares the routine SSS/SAA printable identity",
                  package["institutionalIdentity"]["name"] == "Solar Agricultural Agency"
                  and package["subtitle"] == "Campaign 2 · Case 03 · Trench Shelf IV, Kepler-186f (Ocean)")
    results.check("the package records the approved corrective-release lifecycle",
                  package["status"] == "APPROVED_STABLE"
                  and package["version"] == RELEASE_VERSION
                  and package["approval"] == {"date": APPROVAL_DATE, "owner": OWNER,
                                              "status": "APPROVED", "printStatus": "PASS"},
                  package["approval"])
    release_path = CASE_ROOT / f"history/release-v{RELEASE_VERSION}.json"
    release_approval_path = CASE_ROOT / f"history/CASE03_OWNER_APPROVAL_v{RELEASE_VERSION}.md"
    results.check("the approved package names its own v1.1 release record",
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
    results.check("the case retains exactly the v1.0 and v1.1 history records",
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir())
                  == [f"CASE03_OWNER_APPROVAL_v{RETAINED_VERSION}.md",
                      f"CASE03_OWNER_APPROVAL_v{RELEASE_VERSION}.md",
                      f"release-v{RETAINED_VERSION}.json",
                      f"release-v{RELEASE_VERSION}.json"],
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir()))

    # ── The v1.1 release record ──────────────────────────────────────
    # Read defensively: a deleted or malformed record must fail the assertion that names
    # it, not crash the run and reduce every later protection to "validator crashed".
    def read_record(path: Path) -> dict:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}

    release = read_record(release_path)
    results.check("the v1.1 release record identifies the corrective release it describes",
                  release.get("caseId") == CASE_ID
                  and release.get("curriculumVersion") == RELEASE_VERSION
                  and release.get("correctiveOf") == RETAINED_VERSION
                  and release.get("status") == "APPROVED_STABLE"
                  and release.get("approvalDate") == APPROVAL_DATE
                  and release.get("owner") == OWNER)
    results.check("the v1.1 release record pins the approved page counts",
                  release.get("rolePageCounts") == {"student": 5, "teacher": 8, "answer": 4,
                                                "accessible": 8})
    results.check("the v1.1 release record pins the approved source hashes, layout overrides included",
                  release.get("sourceHashes") == package["sourceHashes"]
                  and set(release.get("sourceHashes", {})) == {"content", "presentation", "taskRegistry",
                                                       "layoutOverrides"})
    results.check("the v1.1 release record records the approved print gate",
                  release.get("acceptedPrintStatus") == "PASS at 100% / Actual Size"
                  and release.get("acceptedValidation", {}).get("status") == "PASS")
    accepted = release.get("acceptedValidation", {})
    results.check("the v1.1 release record records the accepted validation totals",
                  all(accepted.get(key, "").startswith(value) for key, value in
                      (("static", "596/596"), ("browser", "2161/2161"), ("pdf", "316/316"),
                       ("correctiveReleaseLifecycle", "25/25"), ("case03Mutations", "22/22"),
                       ("case04Scoped", "82/82"), ("case05Scoped", "101/101"),
                       ("case06Scoped", "153/153")))
                  and accepted.get("gitDiffCheck") == "clean",
                  accepted)
    # Three Campaign 2 release records were written with accepted-validation figures their own
    # suites did not produce. This case's figure is checked against the live total instead.
    results.check("the recorded Case 03 total is the total this validator actually produces",
                  accepted.get("case03Scoped", "").startswith(f"{TOTAL_ASSERTIONS}/{TOTAL_ASSERTIONS}"),
                  accepted.get("case03Scoped", "")[:24])
    results.check("the v1.1 release record declares no generated artifacts",
                  release.get("formerArtifacts", {}).get("status") == "NO_FORMER_GENERATED_ARTIFACTS"
                  and release.get("artifactPolicy") == "NO_GENERATED_ARTIFACTS_COMMITTED"
                  and release.get("retiredArtifacts") == [])
    results.check("the v1.1 release record records the frozen game baseline",
                  any(GAME_COMMIT in note for note in release.get("migrationNotes", []))
                  and registry["gameCommit"] == GAME_COMMIT)
    results.check("the v1.1 release record keeps the case at its runtime case number",
                  any("not renumbered as Campaign 2 Case 01" in note
                      for note in release.get("migrationNotes", [])))
    results.check("the v1.1 release record explains what the corrective release corrects",
                  {"reason", "corrections", "unchanged"} <= set(release.get("correctionSummary", {}))
                  and len(release.get("correctionSummary", {}).get("corrections", [])) >= 5
                  and all(any(token in item for item in release.get("correctionSummary", {}).get("corrections", []))
                          for token in ("Task 5", "Task 1", "Task 4", "provenance", "MS-PS4-2")),
                  [item[:40] for item in release.get("correctionSummary", {}).get("corrections", [])])
    results.check("the v1.1 release record pins the whole corrective review, not just its last commit",
                  len(release.get("correctiveReviewCommits", [])) >= 4
                  and all(subprocess.run(["git", "cat-file", "-e", f"{entry['commit']}^{{commit}}"],
                                         cwd=ROOT, capture_output=True).returncode == 0
                          and entry["role"] for entry in release.get("correctiveReviewCommits", [])))
    results.check("every commit reference in the v1.1 release record exists",
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
    results.check("the v1.1 release record pins the live Student, Teacher and Answer Key DOM baselines",
                  all(release.get("frozenNonAccessibleDomBaselines", {}).get(role) == role_dom_hash(soup, role)
                      for role in ("student", "teacher", "answer")))

    # ── v1.0 represented as the canonical prior approved release ─────
    results.check("the v1.1 release record carries v1.0 as a canonical prior release",
                  len(release.get("priorApprovedReleases", [])) == 1
                  and release["priorApprovedReleases"][0].get("version") == RETAINED_VERSION
                  and release["priorApprovedReleases"][0].get("status") == "APPROVED_STABLE"
                  and release["priorApprovedReleases"][0].get("approvalDate") == RETAINED_APPROVAL_DATE,
                  release.get("priorApprovedReleases"))
    prior = (release.get("priorApprovedReleases") or [{}])[0]
    results.check("the prior-release entry indexes the retained v1.0 records",
                  sorted(prior.get("retainedRecords", []))
                  == sorted([f"sss/campaign-2/case-03-wrong-color-light/history/"
                             f"CASE03_OWNER_APPROVAL_v{RETAINED_VERSION}.md",
                             f"sss/campaign-2/case-03-wrong-color-light/history/"
                             f"release-v{RETAINED_VERSION}.json"]))
    # The release-history schema allows no gameCommit on a prior-release entry, so v1.0's
    # pin is preserved in its notes. It must still be v1.0's own pin, never normalised to v1.1's.
    prior_notes = " ".join(prior.get("notes", []))
    results.check("the prior-release entry preserves v1.0's own game pin rather than rewriting it",
                  f"v1.0 pinned game baseline {RETAINED_GAME_COMMIT}" in prior_notes
                  and GAME_COMMIT != RETAINED_GAME_COMMIT,
                  prior_notes[:100])
    results.check("no v1.1 baseline or hash can be satisfied by the superseded v1.0 markup",
                  bool(prior) and all(prior["frozenNonAccessibleDomBaselines"][role]
                                      != release["frozenNonAccessibleDomBaselines"][role]
                                      for role in ("student", "teacher", "answer"))
                  and all(prior["sourceHashes"][name] != release["sourceHashes"][name]
                          for name in ("content", "taskRegistry")))
    results.check("every commit reference in the prior-release entry exists",
                  bool(prior) and all(
                      subprocess.run(["git", "cat-file", "-e", f"{prior[field]}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("approvalCommit", "recoveryCommit",
                                    "canonicalSourceApprovalCommit")))

    # ── The retained v1.0 records, unchanged ─────────────────────────
    history_path = CASE_ROOT / f"history/release-v{RETAINED_VERSION}.json"
    approval_path = CASE_ROOT / f"history/CASE03_OWNER_APPROVAL_v{RETAINED_VERSION}.md"
    history = read_record(history_path)
    results.check("the retained v1.0 record still describes the v1.0 release",
                  history.get("caseId") == CASE_ID and history.get("curriculumVersion") == RETAINED_VERSION
                  and history.get("status") == "APPROVED_STABLE"
                  and history.get("approvalDate") == RETAINED_APPROVAL_DATE
                  and history.get("owner") == OWNER
                  and history.get("formerArtifacts", {}).get("status") == "NO_FORMER_GENERATED_ARTIFACTS"
                  and history.get("priorApprovedReleases") == []
                  and history.get("retiredArtifacts") == []
                  and history.get("acceptedPrintStatus") == "PASS at 100% / Actual Size")
    results.check("the retained v1.0 record keeps the page counts it was approved with",
                  history.get("rolePageCounts") == {"student": 5, "teacher": 8, "answer": 4, "accessible": 8})
    results.check("the retained v1.0 record was not rewritten to describe v1.1 content",
                  bool(history) and all(history["sourceHashes"][name] != package["sourceHashes"][name]
                                        for name in ("content", "taskRegistry"))
                  and history["curriculumVersion"] == RETAINED_VERSION
                  and "correctiveOf" not in history
                  and history["priorApprovedReleases"] == [])
    results.check("every commit reference in the retained v1.0 record exists",
                  all(subprocess.run(["git", "cat-file", "-e", f"{history.get(field, '')}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")))
    results.check("the retained v1.0 record still records the baseline it was approved against",
                  any(RETAINED_GAME_COMMIT in note for note in history.get("migrationNotes", [])))
    results.check("the retained v1.0 record keeps the case at its runtime case number",
                  any("not renumbered as Campaign 2 Case 01" in note for note in history.get("migrationNotes", [])))
    owner_approval = (approval_path.read_text(encoding="utf-8") if approval_path.is_file() else "")
    results.check("the retained v1.0 owner approval still records the gates it passed",
                  all(token in owner_approval for token in
                      ["Nate / Owner", RETAINED_APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS",
                       "READY_TO_MERGE",
                       "On-screen content and visual review: **PASS**", "Generated PDF review: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**", "NO_GENERATED_ARTIFACTS_COMMITTED",
                       RETAINED_GAME_COMMIT]))
    release_approval = (release_approval_path.read_text(encoding="utf-8")
                        if release_approval_path.is_file() else "")
    results.check("the v1.1 owner approval records all three release gates",
                  all(token in release_approval for token in
                      [OWNER, APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS", "READY_TO_MERGE",
                       "On-screen content and visual review: **PASS**",
                       "Generated PDF review: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT]))
    results.check("the v1.1 owner approval documents the corrections it was approved for",
                  all(token in release_approval for token in
                      ["Corrected total-PAR reasoning", "Corrected evidence availability",
                       "Corrected approximate-value provenance", "Standards changes",
                       "Accessible corrections"]))
    results.check("the v1.1 owner approval records the preserved figures, page counts and v1.0 history",
                  all(token in release_approval for token in
                      ["Student Mission 5 pages", "Teacher Guide 8 pages", "Answer Key 4 pages",
                       "Accessible Mission 8 pages", "byte-identical", RETAINED_GAME_COMMIT,
                       "superseded, not withdrawn"]))
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

    # ── Canonical Campaign 2 case-folder structure ───────────────────
    top_level = {path.name for path in CASE_ROOT.iterdir() if path.name != ".DS_Store"}
    source_files = {path.name for path in SOURCE.iterdir() if path.is_file() and path.name != ".DS_Store"}
    results.check("Campaign 2 case folder uses the canonical lean layout",
                  top_level == {"README.md", "source", "history"}
                  and source_files == {"case-package.json", "content.html", "layout-overrides.json",
                                       "presentation.css", "task-registry.js"},
                  {"top": sorted(top_level), "source": sorted(source_files)})
    stray = sorted(path.relative_to(ROOT).as_posix() for path in CASE_ROOT.rglob("*")
                   if path.is_file() and path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg"})
    results.check("Campaign 2 case stores no PDFs or screenshots", not stray, stray)

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
                  [entry["id"] for entry in registry["tasks"]] == [f"C2-C03-T{n}" for n in expected_numbers])

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
                      for name in ["Aquaculturist", "Dome sensor array", "Kelp specimen",
                                   "Oolian aquaculture records", "Federation database"]))

    # ── Numerical ledger ─────────────────────────────────────────────
    printable = visible_text(soup, ROLES)
    asserted = asserted_text(content, ROLES)
    missing = [value for value in REQUIRED_LEDGER_STRINGS if value not in printable]
    results.check("every frozen value used in the packet appears exactly as reported", not missing, missing)
    inequality_findings = [reason for pattern, reason in INEQUALITY_PATTERNS if pattern.search(asserted)]
    results.check("reported inequalities are never converted to exact numbers", not inequality_findings,
                  inequality_findings)
    learner_and_key = visible_text(soup, ["student", "answer", "accessible"])
    results.check("the approximate effective-PAR estimate never reaches Student, Answer Key, or Accessible",
                  "14 µmol" not in learner_and_key and "14 umol" not in learner_and_key)
    results.check("quoted misconceptions appear only inside the Teacher Guide",
                  all(node.find_parent(class_="page").get("data-role") == "teacher"
                      for node in soup.select("[data-quoted-claim]"))
                  and bool(soup.select("[data-quoted-claim]")))
    results.check("the source-status ledger names an Earth-science comparison and case-specific evidence",
                  set(registry["sourceStatus"]) >= {"establishedEarthScienceComparison", "caseSpecificEvidence"}
                  and not INVENTED_SCENARIO_REMINDER.search(json.dumps(registry)),
                  sorted(registry["sourceStatus"]))
    results.check("the numerical ledger records the excluded effective-PAR estimate and its reason",
                  registry["numericalLedger"]["excludedFromStudentWork"]["approximateEffectivePar"] == 14
                  and bool(registry["numericalLedger"]["excludedFromStudentWork"]["reason"]))

    # ── Earth science versus fictional case data ─────────────────────
    results.check("both learner editions attribute the zhal-kelp values to measurements made in this case",
                  len(PROVENANCE.findall(visible_text(soup, ["student"]))) >= 3
                  and len(PROVENANCE.findall(visible_text(soup, ["accessible"]))) >= 3,
                  {"student": len(PROVENANCE.findall(visible_text(soup, ["student"]))),
                   "accessible": len(PROVENANCE.findall(visible_text(soup, ["accessible"])))})
    results.check("the Teacher Guide separates established science, case evidence, inference, and engineering layers",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["Established Earth science", "Case-specific evidence", "Case inference",
                       "Engineering extrapolation"]))
    results.check("the source boundary keeps the Earth-science comparison distinct from the case evidence",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["chlorophyll a and c", "fucoxanthin", "Earth analogy", "460–540 nm"]))
    reminder_findings = [
        f"{page.get('data-page-id')}:{match.group(0)}"
        for page in soup.select(".page[data-role]")
        for match in INVENTED_SCENARIO_REMINDER.finditer(" ".join(page.stripped_strings))
    ]
    results.check("printable pages carry no repeated reminder that the scenario is invented",
                  not reminder_findings, reminder_findings)

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
                      or figure.select("polyline,polygon,ellipse,circle[r]:not(pattern circle)")
                      and figure.select("polyline,polygon")]
    results.check("no figure draws a continuous action-spectrum curve", not curve_findings, curve_findings)
    results.check("every figure caption attributes its data to a measurement made in this case",
                  all(PROVENANCE.search(figure.select_one("figcaption").get_text(" ", strip=True))
                      for figure in figures),
                  [figure.get("data-figure-id") for figure in figures
                   if not PROVENANCE.search(figure.select_one("figcaption").get_text(" ", strip=True))])
    results.check("every figure caption states the limit of what it reports",
                  all(re.search(r"no intermediate values|not identical between fixtures|is not zero|discrete",
                                figure.select_one("figcaption").get_text(" ", strip=True), re.I)
                      for figure in figures))
    band_figures = [figure for figure in figures if "band" in (figure.get("data-figure-id") or "")]
    results.check("the response-band figure states that response outside the band is not zero",
                  bool(band_figures) and all("is not zero" in figure.get_text(" ", strip=True)
                                             for figure in band_figures),
                  [figure.get("data-figure-id") for figure in band_figures])
    results.check("no figure or asserted text labels the response outside the measured band as zero",
                  not re.search(r"(?:response|absorption)\s+outside[^.]{0,60}\bis\s+zero\b", asserted, re.I))
    results.check("every graph is paired with a data-table equivalent on the same page",
                  all(figure.find_parent(class_="page").select_one("table.data-table") for figure in figures))
    results.check("bar and band fills use patterns rather than colour alone",
                  all(figure.select("pattern") and figure.select('rect[fill^="url("]') for figure in figures))
    results.check("figure provenance is recorded in the task registry",
                  len(registry.get("figureProvenance", [])) >= 2
                  and all(entry.get("kind", "").startswith("curriculum-original")
                          for entry in registry["figureProvenance"]))

    # ── Prohibited scientific overstatement ──────────────────────────
    normalized = re.sub(r"\s+", " ", asserted)
    prohibited_findings = [reason for pattern, reason in PROHIBITED if pattern.search(normalized)]
    results.check("no printable role asserts a prohibited scientific overstatement",
                  not prohibited_findings, prohibited_findings)
    results.check("the prohibited-claim registry is declared for the case",
                  len(registry.get("prohibitedClaims", [])) >= 10)
    results.check("the Teacher Guide names the prohibited claims for correction",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["Claims to correct on sight", "below detection", "narrated prediction"]))
    results.check("learner explanations are required to be qualified rather than proven",
                  all(term in visible_text(soup, ["student"]) for term in
                      ["poor match", "strongest measured", "cannot establish", "does not"]))

    # ── CER and Answer Key ───────────────────────────────────────────
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
    accessible_cer_page = soup.select_one('.page[data-role="accessible"]:has([data-cer-contract="accessible-v1.0"])')
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
                      ["Completed classification", "Largest reported category", "Qualified comparison",
                       "Completed rejections", "Completed five-source analysis", "Completed diagnosis analysis",
                       "CLAIM", "EVIDENCE", "REASONING", "Monitored trial and stop rule"]))
    results.check("Answer Key exemplars preserve the required qualifiers",
                  all(term in answer_text for term in
                      ["poor match", "strongest measured", "at this site", "best-supported"]))

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
    results.check("every Student and Accessible response is explicitly eligible or locked", not coverage_findings,
                  coverage_findings)
    results.check("no eligible resize area is a CER or compact field",
                  not any(area["persistId"].startswith(("t7", "a7"))
                          or any(token in area["label"].lower() for token in
                                 ("criterion", "constraint", "classification", "status"))
                          for definition in editions.values() for area in definition["areas"]))

    role_text = {role: visible_text(soup, [role]) for role in ROLES}
    learner_text = role_text["student"] + " " + role_text["accessible"]

    def pages(role):
        return soup.select(f'.page[data-role="{role}"]')

    def page_index_of_task(role, number):
        for index, page in enumerate(pages(role)):
            if any(node["data-shell-task-heading"] == str(number)
                   for node in page.select("[data-shell-task-heading]")):
                return index
        return None

    def page_index_of(role, selector):
        for index, page in enumerate(pages(role)):
            if page.select_one(selector):
                return index
        return None

    # ── A. Cross-role reasoning parity ───────────────────────────────
    # The released v1.0 learner editions printed the inverse of the rule the Teacher
    # Guide and Answer Key state, and the Answer Key graded against the other wording.
    # Parity is asserted in both directions: every role states the rule, and no role
    # states its inverse.
    rule_missing = [role for role in ROLES if not TOTAL_PAR_RULE.search(role_text[role])]
    results.check("every role states the same total-PAR reasoning rule", not rule_missing, rule_missing)
    learner_rule_missing = [role for role in ("student", "accessible")
                            if not TOTAL_PAR_RULE.search(role_text[role])]
    results.check("both learner editions state that rule, not just one of them",
                  not learner_rule_missing, learner_rule_missing)
    inverted = {role: TOTAL_PAR_RULE_INVERTED.findall(re.sub(r"\s+", " ", role_text[role]))
                for role in ROLES}
    inverted = {role: found for role, found in inverted.items() if found}
    results.check("no role inverts the total-PAR reasoning rule", not inverted, inverted)
    # The rule is not only present but stated in full where learners meet it: the total
    # is a photon count, the total alone settles nothing about spectrum, and the two
    # kinds of evidence are compared separately.
    rule_blocks = {role: [" ".join(node.stripped_strings)
                          for node in soup.select(f'.page[data-role="{role}"] [data-reasoning-rule]')]
                   for role in ("student", "accessible")}
    incomplete = {role: blocks for role, blocks in rule_blocks.items()
                  if not blocks or not any(
                      re.search(r"counts every photon", text, re.I)
                      and TOTAL_PAR_RULE.search(text)
                      and re.search(r"separately", text, re.I) for text in blocks)}
    results.check("each learner edition carries the rule in full in a marked reasoning block",
                  not incomplete, sorted(incomplete))
    results.check("the Answer Key's five-source row states the rule the learner table states",
                  TOTAL_PAR_RULE.search(role_text["answer"]) is not None
                  and TOTAL_PAR_RULE.search(registry["sourceLedger"][-1]["establishes"]) is not None)

    # ── B. Evidence timing and availability ──────────────────────────
    # Task 1 grades a changed/kept classification. The record that settles it must be
    # printed for that reader, on or before the page that asks for it.
    for role in ("student", "accessible"):
        record_nodes = soup.select(f'.page[data-role="{role}"] [data-change-record]')
        record_text = " ".join(" ".join(node.stripped_strings) for node in record_nodes)
        record_page = page_index_of(role, "[data-change-record]")
        task_page = page_index_of_task(role, 1)
        uncovered = [name for name, pattern in TASK1_CONDITIONS.items()
                     if not pattern.search(record_text)]
        results.check(
            f"the {role} edition prints the Week 0 change record on or before Task 1",
            bool(record_nodes) and record_page is not None and task_page is not None
            and record_page <= task_page and not uncovered,
            {"recordPage": record_page, "taskPage": task_page, "uncovered": uncovered})
    # Every fact the Answer Key reasons from must be readable in both learner editions.
    unavailable = {name: [role for role in ("student", "accessible") if token not in role_text[role]]
                   for name, token in ANSWER_KEY_EVIDENCE.items()}
    unavailable = {name: roles for name, roles in unavailable.items() if roles}
    results.check("every fact the Answer Key reasons from is printed in both learner editions",
                  not unavailable, unavailable)
    # Runtime-only and Teacher-only enrichment must never become a graded requirement.
    graded_text = role_text["answer"] + " " + learner_text
    promoted = [name for name, pattern in RUNTIME_ONLY_FACTS.items() if pattern.search(graded_text)]
    results.check("runtime-only and Teacher-only enrichment stays out of the graded requirements",
                  not promoted, promoted)

    # ── C. Provenance of the approximate effective-PAR value ─────────
    # The canonical source states the value and says nothing about how it was obtained.
    provenance_findings = {
        "printable content": bool(UNSUPPORTED_PROVENANCE.search(printable)),
        "task registry": bool(UNSUPPORTED_PROVENANCE.search(json.dumps(registry, ensure_ascii=False))),
        # Backtick spans in the README quote the strings v1.1 removed, so they record the
        # defect rather than asserting it — the same reason Teacher misconceptions are
        # marked data-quoted-claim and excluded from the prohibited-claim scan.
        "README": bool(UNSUPPORTED_PROVENANCE.search(
            re.sub(r"`[^`]*`", " ", (CASE_ROOT / "README.md").read_text(encoding="utf-8")))),
    }
    results.check("the approximate effective-PAR value carries no unsupported model provenance",
                  not any(provenance_findings.values()),
                  [where for where, found in provenance_findings.items() if found])
    excluded = registry["numericalLedger"]["excludedFromStudentWork"]
    results.check("the ledger labels that value approximate and keeps it out of student work",
                  excluded["approximateEffectivePar"] == 14
                  and re.search(r"approximate", excluded["reason"], re.I)
                  and re.search(r"not an exact", excluded["reason"], re.I)
                  and re.search(r"never used in student calculations", excluded["reason"], re.I),
                  excluded["reason"])
    results.check("the Teacher Guide keeps the value approximate rather than exact or calculated",
                  "approximate" in role_text["teacher"].lower()
                  and not re.search(r"exact(?:ly)? 14|effective PAR (?:is|=) 14 µmol/m²/s\.", role_text["teacher"]))
    results.check("measured, reported and approximate values keep their distinct labels",
                  "strongest measured" in learner_text
                  and "reported adequate" in learner_text
                  and "reported category" in learner_text.lower())

    # ── D. Standards ─────────────────────────────────────────────────
    # A claimed standard names the task that assesses it, or it is not claimed.
    # One claim per paragraph: a standard is claimed by the paragraph that justifies it.
    claims = [match.groups()
              for node in soup.select('.page[data-role="teacher"] p')
              for match in [STANDARD_CLAIM.match(" ".join(node.stripped_strings))] if match]
    unassessed = [f"{kind}: {code}" for kind, code, rest in claims
                  if not re.search(r"\bTasks? \d", rest)]
    results.check("every claimed standard names at least one assessing task", not unassessed, unassessed)
    results.check("at least one standard is claimed and its kinds are recognised",
                  bool(claims) and all(kind in ("Direct assessment", "Supporting alignment")
                                       for kind, _, _ in claims),
                  [f"{kind}: {code}" for kind, code, _ in claims])
    returned = [code for _, code, _ in claims if code in WITHDRAWN_STANDARDS]
    results.check("no withdrawn standard returns as a direct or supporting claim", not returned, returned)
    results.check("the Teacher Guide records why MS-PS4-2 is not claimed",
                  "MS-PS4-2 is not claimed" in role_text["teacher"]
                  and re.search(r"reflected, absorbed,? or transmitted through a material",
                                role_text["teacher"]) is not None)
    results.check("no printable role advertises a withdrawn standard as claimed",
                  not any(re.search(rf"(?:Direct assessment|Supporting alignment):\s*{code}", text)
                          for code in WITHDRAWN_STANDARDS for text in role_text.values()))
    bounded = [f"{kind}: {code}" for kind, code, rest in claims
               if kind == "Supporting alignment"
               and not re.search(r"only if|conditional|rather than direct|supporting rather than", rest, re.I)]
    results.check("every supporting or conditional standard states its bound", not bounded, bounded)
    results.check("no mathematics standard is claimed",
                  not re.search(r"\bCCSS[.\s]|\bMath(?:ematics)? standard\b", " ".join(role_text.values())))

    # ── E. Revision propagation ──────────────────────────────────────
    registry_file = json.loads((ROOT / "shared/implementation/case-registry.v2.json").read_text(encoding="utf-8"))
    entries = [node for node in json.dumps(registry_file) and _walk_entries(registry_file)
               if node.get("id") == CASE_ID]
    results.check("the shared case registry carries exactly one Case 03 entry", len(entries) == 1)
    entry = entries[0] if entries else {}
    results.check("the registry entry agrees with the approved package",
                  entry.get("version") == package["version"] == RELEASE_VERSION
                  and entry.get("status") == package["status"] == "APPROVED_STABLE"
                  and entry.get("packageStatus") == "APPROVED"
                  and entry.get("approval") == package["approval"]
                  and entry.get("historyRecord") == package.get("releaseHistory"),
                  {"version": entry.get("version"), "status": entry.get("status")})
    results.check("declared role page counts match the rendered document",
                  {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES}
                  == {role: len(pages(role)) for role in ROLES}
                  == registry["roles"],
                  {role: len(pages(role)) for role in ROLES})
    results.check("the task registry, package, registry entry and content agree on the version",
                  registry["version"] == package["version"] == entry.get("version") == RELEASE_VERSION
                  and soup.select_one("[data-editor-content]")["data-editor-content"]
                  == f"sss-c2-case03-v{RELEASE_VERSION}")
    results.check("the package output names carry the candidate version",
                  all(f"_v{RELEASE_VERSION}_CUSTOM.html" in name for name in package["outputs"].values())
                  and package["documentKey"] == f"{CASE_ID}:v{RELEASE_VERSION}:curriculum-editor-v2")
    readme = (CASE_ROOT / "README.md").read_text(encoding="utf-8")
    results.check("the README describes the corrective release and the release it retains",
                  f"`{CASE_ID}`" in readme and RELEASE_VERSION in readme
                  and RETAINED_VERSION in readme and "APPROVED_STABLE" in readme
                  and APPROVAL_DATE in readme and RETAINED_APPROVAL_DATE in readme
                  and "release-v1.1.json" in readme and "release-v1.0.json" in readme)
    results.check("the README page counts match the package",
                  all(f"{label} {package['rolePageStructure'][role]['pageCount']}" in readme
                      for role, label in (("student", "Student"), ("teacher", "Teacher"),
                                          ("answer", "Answer Key"), ("accessible", "Accessible"))))
    results.check("no role still prints the wording the corrective release removed",
                  not any(token in " ".join(role_text.values()) for token in
                          ["proves no effective spectrum", "incomplete weighting model",
                           "in at this site", "and and name"]))

    results.check("the declared assertion total matches this run, so the release record cannot drift",
                  TOTAL_ASSERTIONS == len(results.assertions) + 1,
                  {"declared": TOTAL_ASSERTIONS, "live": len(results.assertions) + 1})

    payload = {
        "validator": "sss-c2-case03-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
