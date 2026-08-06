#!/usr/bin/env python3
"""Case-scoped assertions for SSS Campaign 2 Case 01 — Heavy Hands.

Corrective-candidate validator. Case 01 is reopened at v1.1 and is unreleased: it
carries no release or owner-approval record of its own, no releaseHistory pointer and
no frozen DOM baseline, while the approved v1.0 records stay in history/ byte-identical.

It enforces the frozen source ledger, the five-clue instructional coverage, the figure
contract, the physics/case-evidence boundary, and the prohibited scientific
overstatements against the printable content of every role.

The case turns on one distinction: across the radial depth of the soil bed the reported
direction is outward everywhere and only the magnitude changes. Most of the prohibited
patterns below exist to keep that distinction intact in every role.

The v1.1 correction adds five families of protection the v1.0 estate did not have, each
answering a defect the Campaign 2 completion audit found inside the approved package:

* **Evidence availability.** Every graded Answer Key expectation is tied to the task that
  assesses it, and every value and proper noun it needs must be printed in the Student
  edition and, independently, in the Accessible edition, at or before that task's page.
  A value first printed at Task 8 can no longer be required to answer Task 6.
* **Supported controls.** Only the conditions the game reports as changed between
  plantings may be presented as tested. Nutrients, light and water are present readings,
  never eliminated controls, and ``Ring Status: NOMINAL`` may not be expanded into
  absences no source reported.
* **Teacher–task synchronisation.** Every task carries teacher guidance; no stale
  calculation instruction may survive; no rubric dimension, objective or success
  criterion may grade a value learners never receive.
* **Source attribution.** The botanist's judgements may not be attributed to the archive,
  and GC-1445 keeps the qualifier the game attaches to it.
* **Standards.** ``MS-ETS1-3`` cannot return, and every retained claim must name a real
  assessing task and the learner evidence it rests on.
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
sys.path.insert(0, str(ROOT / "shared/validation"))
from corrective_release_lifecycle import history_findings as lifecycle_findings  # noqa: E402

CASE_ID = "SSS-C2-CASE01"
CASE_ROOT = ROOT / "sss/campaign-2/case-01-heavy-hands"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
CANDIDATE_VERSION = "1.1"
RETAINED_VERSION = "1.0"
RETAINED_APPROVAL_DATE = "2026-08-04"
# The v1.0 record pins 864156f0 as canonicalSourceApprovalCommit, but that commit carries a
# pre-lifecycle task registry hashing 485076fa…, not the 7d92bac9… the record certifies. The
# commit that actually contains all four certified v1.0 sources is a4195913. The inaccurate
# pin is frozen history and is not rewritten; it is pinned here so the discrepancy stays a
# recorded fact rather than a silent one, and so v1.1 cannot repeat it.
RETAINED_PINNED_COMMIT = "864156f068cf89b595e1a394f1a4294c839f2876"
RETAINED_SOURCE_BEARING_COMMIT = "a4195913e7c2d98bd2174f2034a609d8e20f264c"
SYNCHRONISED_MAIN = "85602b0cbee5252c5ef15bd042865f920ddceb11"
ROLE_PAGES = {"student": 5, "teacher": 9, "answer": 4, "accessible": 8}
RUNTIME_ID = "heavy_hands"
ROLES = ["student", "teacher", "answer", "accessible"]
TASK_TITLES = [
    "Frame What Has Already Been Tested",
    "Ride the Merry-Go-Round",
    "Think Like the Investigator",
    "Why the Biggest Tubers Bend Most",
    "Connect the Five Evidence Sources",
    "Diagnose and Reject Alternatives",
    "Explain the Diagnosis with CER",
    "Write the Missing Habitat Specification",
]
FORMAL_CLUES = [
    "GORLROOT_UPWARD",
    "GRAVITY_GRADIENT",
    "TUBERS_MISALIGNED",
    "GORLROOT_NEEDS_UNIFORM_G",
    "CENTRIFUGAL_GRADIENT_KNOWN",
]
ACCESSIBLE_CER_SUBTITLE = "You may write sentences or use bullet points. Use evidence from more than one source."

# Values that must appear verbatim wherever the case reports them.
REQUIRED_LEDGER_STRINGS = [
    "2.0991 g", "2.1009 g", "2.10 g", "0.00187 g", "0.0018 g", "2.88966 RPM",
    "224.8 m", "224.9 m", "225.0 m", "20 cm", "±0.05 g", "±0.00001",
    "22.4 °C", "68%", "800 ppm", "78.2%", "1.08 atm", "0.3%",
    "Day 10", "Day 11", "Day 12", "80 m", "300 m", "600 m",
]
# Reported precision must survive in both directions.
PRECISION_PATTERNS = [
    (re.compile(r"\b2\.099\b(?!\d)"), "bed-top magnitude truncated below four decimals"),
    (re.compile(r"\b2\.101\b(?!\d)"), "bed-base magnitude truncated below four decimals"),
    (re.compile(r"\b0\.0019\s*g\b"), "reported difference rounded away from its five decimals"),
    (re.compile(r"\bnegligible\s*(?:=|is|means)\s*(?:zero|0)\b", re.I), "negligible equated with zero"),
]

PROHIBITED = [
    (re.compile(r"\bdirection\s+(?:changes|reverses|rotates|tilts|varies|differs)\b", re.I),
     "the reported direction described as changing across the bed"),
    (re.compile(r"\bdown\s+points?\s+(?:in\s+)?(?:different|another|two)\b", re.I),
     "down described as pointing more than one way"),
    (re.compile(r"\b(?:field|gravity|acceleration)\s+(?:is\s+)?(?:tilt(?:s|ed|ing)?|rotat(?:es|ed|ing))\b", re.I),
     "the apparent field described as tilting or rotating"),
    (re.compile(r"\breversal\s+of\s+down\b", re.I), "a reversal of down"),
    (re.compile(r"\bgrow(?:s|ing)?\s+upward\b", re.I),
     "tubers described as growing upward rather than sideways"),
    (re.compile(r"\btubers?\s+(?:point|curve|bend)s?\s+towards?\s+the\s+axis\b", re.I),
     "deformation described as pointing toward the rotation axis"),
    (re.compile(r"\bcalibrated\s+too\s+(?:strong|high|fast)\b", re.I),
     "over-calibration asserted rather than rejected"),
    (re.compile(r"\bmidpoint\s+calibration\s+(?:is|was)\s+wrong\b", re.I),
     "the midpoint calibration asserted to be wrong"),
    (re.compile(r"\bCoriolis\s+(?:effect\s+)?(?:is|causes?|caused|explains?|produces?|drives?)\b", re.I),
     "the Coriolis effect asserted as the cause"),
    (re.compile(r"\b(?:not|isn(?:'|’)t)\s+real\s+gravity\b", re.I),
     "the rotating habitat's acceleration dismissed as unreal"),
    (re.compile(r"\bEarth\s+(?:plants|crops)\s+(?:can|could|would|do|also)\s+(?:also\s+)?(?:detect|sense|notice)\b", re.I),
     "the response generalised to Earth crops"),
    (re.compile(r"\ball\s+plants\s+(?:can\s+)?(?:detect|sense)\s+(?:gravity\s+)?gradients?\b", re.I),
     "a universal claim that plants sense gravity gradients"),
    (re.compile(r"\bdetection\s+threshold\b", re.I),
     "the reported difference presented as a detection threshold"),
    (re.compile(r"\b(?:guarantee(?:d|s)?|will)\s+(?:to\s+)?(?:fix|solve|cure|recover)\b", re.I),
     "a remedy presented as guaranteed"),
    (re.compile(r"\b(?:proves|proving|proof\s+of)\s+(?:the\s+)?(?:diagnosis|cause)\b", re.I),
     "single-source proof language"),
    (re.compile(r"\b(?:disagree|conflict|contradict)\w*\b[^.]{0,60}\b0\.00187\b", re.I),
     "the two reported difference values presented as conflicting"),
    (re.compile(r"\b0\.00187[^.]{0,60}\b(?:disagree|conflict|contradict)\w*\b", re.I),
     "the two reported difference values presented as conflicting"),
]
# ── v1.1 evidence-availability contract ─────────────────────────────────────
# Values and proper nouns the learner editions deliberately withhold. None may appear in a
# learner edition, and none may be required by a graded Answer Key expectation. The raw
# gravity profile is Teacher-facing by design: a 20 cm bed inside a 224.9 m radius differs
# by less than a tenth of one percent, so learners meet the relationship through the
# labelled merry-go-round instead.
WITHHELD_FROM_LEARNERS = [
    "0.00187", "2.0991", "2.1009", "224.8", "224.9", "225.0", "2.88966",
    "0.3%", "80 m", "300 m", "GC-1445", "0.0018", "a = ω²r",
]
# Every graded Answer Key expectation, the task that assesses it, and the learner evidence
# it rests on. Each fragment must appear in the Student edition and, independently, in the
# Accessible edition, on or before the page carrying that task. A value first printed at
# Task 8 therefore cannot be required to answer Task 6.
GRADED_EVIDENCE = [
    (1, "Task 1 classification", [
        "Soil reformulated", "New seed", "Day 10", "Day 11", "Day 12",
        "Nutrients: precise", "nutrients precise", "Ring radius and rotation rate"]),
    (4, "Task 4 size pattern", ["20 cm", "tuber"]),
    (5, "Task 5 five-source analysis", [
        "Vressk botanist", "Centrifuge sensor array", "Gorlroot specimen",
        "Vressk botanical archive", "Federation database"]),
    (6, "Task 6 rejections", [
        "weakest at the top", "strongest at the bottom", "2.10 g",
        "outward", "roots point"]),
    (7, "Task 7 CER exemplar", [
        "weakest at the top", "strongest at the bottom", "20 cm",
        "neither toward the axis nor away from it", "Day 10", "Day 11",
        "nutrients", "middle of the bed"]),
    (8, "Task 8 specification", ["±0.05 g", "600 m", "GC-1208"]),
]
# Alternative spellings that satisfy the same requirement; the learner editions differ in
# register by design, so parity is on the evidence, not on the wording.
EVIDENCE_ALIASES = {
    "Soil reformulated": ["Soil reformulated", "New soil"],
    "New seed": ["New seed stock", "New seeds"],
    "Nutrients: precise": ["Nutrients: precise", "nutrients precise"],
    "nutrients precise": ["Nutrients: precise", "nutrients precise"],
    "weakest at the top": ["weakest at the top"],
    "strongest at the bottom": ["strongest at the bottom"],
    "roots point": ["roots point", "Primary roots point", "The roots point"],
    "middle of the bed": ["middle of the bed", "midpoint"],
    "neither toward the axis nor away from it": ["neither toward the axis nor away from it"],
}
# The historical controls the canonical runtime actually reports as varied between
# plantings. Everything else the botanist reports is a present reading.
TESTED_CONDITIONS = {"Soil mineral formulation", "Seed stock"}
# Language that turns a present reading into an eliminated control.
UNSUPPORTED_CONTROL = [
    (re.compile(r"\b(?:nutrients?|nutrient supply|light|grow-light|spectrum|water)\b[^.]{0,90}"
                r"\b(?:verified|ruled out|eliminated|excluded|were each changed|was each changed|"
                r"each changed|changed or verified|changed without effect)\b", re.I),
     "a present reading presented as a changed, verified or eliminated control"),
    (re.compile(r"\b(?:changed|varied|tested|verified)\b[^.]{0,60}\bwater\b", re.I),
     "water presented as a tested historical variable"),
    (re.compile(r"soil,\s*(?:nutrients|seed stock),?[^.]{0,60}\b(?:light|water)\b[^.]{0,60}"
                r"\bchanged\b", re.I),
     "the v1.0 four-variable control list restored"),
]
# The packet must be able to say that a condition was *not* tested and is *not* ruled out —
# that statement is the correction. So a match counts only when nothing negates it; otherwise
# the detector would forbid the very wording it exists to protect.
NEGATOR = re.compile(r"\b(?:not|never|no|nor|neither)\b", re.I)


def unsupported_control_findings(text: str) -> list[str]:
    findings = []
    for pattern, reason in UNSUPPORTED_CONTROL:
        for match in pattern.finditer(text):
            if not NEGATOR.search(text[max(0, match.start() - 45):match.end()]):
                findings.append(f"{reason}: …{match.group(0)[:90]}…")
    return findings
# The sensor array reports only "Ring Status: NOMINAL". The botanist, separately, reports
# steady RPM with no vibration and no wobble. A nominal status is not a report about every
# mechanical condition that went unmentioned.
NOMINAL_EXPANSION = re.compile(r"\bnominal\b", re.I)
# Attribution: only an *attributing* construction misattributes. The guide must remain free to
# say "it is the botanist, not the archive, who calls it negligible".
ARCHIVE_NEGLIGIBLE = re.compile(
    r"archive\s+(?:says|reports|states|records|claims|calls|describes|treats)[^.]{0,70}negligible",
    re.I)
# Both learner editions must say, in their own register, that N marks an untested condition.
N_IS_NOT_RULING_OUT = re.compile(
    r"\bN\b[^.]{0,60}\b(?:untested|not\s+(?:mean\s+)?(?:ruled out|tested))\b", re.I)
UNREPORTED_ABSENCE = re.compile(r"\bno\s+(?:vibration|wobble)\b", re.I)
# Stale revision text: no role may instruct anyone to perform arithmetic this packet removed.
STALE_CALCULATION = [
    (re.compile(r"Task\s*\d+\s*(?:needs|requires|produces)\b[^.]{0,80}"
                r"\b(?:subtract\w*|calculat\w*|arithmetic|four-decimal)\b", re.I),
     "a task described as needing or producing a calculation"),
    (re.compile(r"\bWhat Task \d+ produces\b", re.I),
     "a ledger row still keyed to a removed task calculation"),
    (re.compile(r"\bbefore Task 3\b[^.]{0,60}\brounded\b", re.I),
     "preparation still keyed to the removed Task 3 rounding work"),
]
# Reported quantities and record identifiers. Any of these appearing in an Answer Key task is
# treated as evidence that task relies on, and must be reachable in both learner editions.
REPORTED_TOKEN = re.compile(
    r"±?\d[\d.,]*\s?(?:g|m|cm|RPM|%|ppm|atm|°C)\b|\bGC-\d{4}\b|\bDay \d+\b")
STANDARDS_CLAIMED = {"MS-LS1-5", "MS-ETS1-1", "MS-ETS1-2"}
STANDARDS_WITHDRAWN = {"MS-ETS1-3"}
UNIVERSAL_SENSITIVITY = [
    (re.compile(r"gradient sensitivity is (?:universal|the same|identical|not species)", re.I),
     "gradient sensitivity presented as universal"),
    (re.compile(r"\b(?:all|every|any)\s+(?:species|crops?|plants?|organisms?)\b[^.]{0,70}"
                r"\b(?:gradient|sensitivit\w*)\b", re.I),
     "a universal cross-species gradient-sensitivity claim"),
    (re.compile(r"\ba 300 ?m (?:ring|radius) is safe\b", re.I),
     "GC-1445 read as establishing a safe radius"),
]

# Curve-drawing SVG constructs are forbidden inside case figures.
CURVE_COMMANDS = re.compile(r"[CcSsQqTtAa]")
# Case measurements must be attributed to this investigation rather than to established
# biology. Any of these provenance phrases satisfies it; no fixed disclaimer is required.
PROVENANCE = re.compile(
    r"in this case|for this case|this habitat|habitat record|specimen record|sensor array|"
    r"site measurement|as reported|reported in this|recorded in this|cultivation record",
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
    Guide must be able to name a misconception in order to correct it. Both are explicitly
    marked in the source and are excluded here, so the prohibited-claim scan measures what
    the packet asserts rather than what it rejects or corrects.
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

    # ── Source contract and lifecycle ────────────────────────────────
    results.check("package and task registry declare the same case identity",
                  package["id"] == registry["case"] == CASE_ID and package["title"] == registry["title"])
    results.check("task registry pins the frozen game baseline and runtime case id",
                  registry.get("gameCommit") == GAME_COMMIT and registry.get("runtimeCaseId") == RUNTIME_ID,
                  {"gameCommit": registry.get("gameCommit"), "runtimeCaseId": registry.get("runtimeCaseId")})
    results.check("the package records the runtime identity the case was authored against",
                  (registry.get("runtimeInvestigationName"), registry.get("runtimeLocation"),
                   registry.get("runtimeSubtitle"))
                  == ("Vressk Centrifuge Habitat", "Kepler-442b Orbit", "Vressk Territory")
                  and package["location"] == "Vressk Centrifuge Habitat")
    results.check("package declares the routine SSS/SAA printable identity",
                  package["institutionalIdentity"]["name"] == "Solar Agricultural Agency"
                  and package["subtitle"] == "Campaign 2 · Case 01 · Kepler-442b Orbit, Vressk Territory")
    results.check("the case keeps its canonical runtime case number",
                  package["subtitle"].startswith("Campaign 2 · Case 01 ·")
                  and CASE_ID.endswith("CASE01"))

    # ── Corrective-candidate lifecycle, retained v1.0 history, no artifacts ──
    results.check("the package records the unreleased corrective-candidate lifecycle",
                  package["status"] == "OWNER_GATE_OPEN"
                  and package["version"] == CANDIDATE_VERSION
                  and package["approval"] == {"owner": "Nate / Owner",
                                              "status": "OWNER_REVIEW_IN_PROGRESS",
                                              "printStatus": "NOT_RUN"},
                  package["approval"])
    results.check("the candidate declares no release-history pointer of its own",
                  "releaseHistory" not in package and "releaseHistory" not in registry)
    results.check("the task registry records the same corrective candidate",
                  (registry.get("version"), registry.get("status"), registry.get("ownerReviewStatus"),
                   registry.get("printStatus"), registry.get("correctiveOf"))
                  == (CANDIDATE_VERSION, "OWNER_GATE_OPEN", "OWNER_REVIEW_IN_PROGRESS",
                      "NOT_RUN", RETAINED_VERSION)
                  and "approvalDate" not in registry and "mergeStatus" not in registry
                  and "approvedBy" not in registry,
                  (registry.get("status"), registry.get("correctiveOf")))
    results.check("the shared corrective-release lifecycle rules are satisfied",
                  not lifecycle_findings(CASE_ROOT, CASE_ID, package, registry),
                  lifecycle_findings(CASE_ROOT, CASE_ID, package, registry))
    history_path = CASE_ROOT / f"history/release-v{RETAINED_VERSION}.json"
    approval_path = CASE_ROOT / f"history/CASE01_OWNER_APPROVAL_v{RETAINED_VERSION}.md"
    results.check("history retains exactly the two approved v1.0 records and nothing for v1.1",
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir())
                  == ["CASE01_OWNER_APPROVAL_v1.0.md", "release-v1.0.json"],
                  sorted(path.name for path in (CASE_ROOT / "history").iterdir()))
    history = json.loads(history_path.read_text(encoding="utf-8"))
    results.check("the retained v1.0 record still describes the v1.0 release, not the candidate",
                  history["caseId"] == CASE_ID and history["curriculumVersion"] == RETAINED_VERSION
                  and history["status"] == "APPROVED_STABLE"
                  and history["approvalDate"] == RETAINED_APPROVAL_DATE
                  and history["owner"] == "Nate / Owner"
                  and history["formerArtifacts"]["status"] == "NO_FORMER_GENERATED_ARTIFACTS"
                  and history["priorApprovedReleases"] == [] and history["retiredArtifacts"] == []
                  and history["acceptedPrintStatus"] == "PASS at 100% / Actual Size")
    results.check("the retained v1.0 record keeps its own approved page counts and source hashes",
                  history["rolePageCounts"] == {"student": 5, "teacher": 8, "answer": 4, "accessible": 8}
                  and history["sourceHashes"] == {
                      "content": "af6143c46bc166be3420ce0d6243e615f49caaca7d679e587633a0e66e975e4c",
                      "presentation": "9ba4fc5dffc501126032f8a06d1c21e17f5ea8fe914b0a0a885c377d0ccc3d05",
                      "taskRegistry": "7d92bac95a3661a8ae4eaa2843e91b2ec4c59541b07234e8b4a8d888131788d1"},
                  history["rolePageCounts"])
    results.check("every commit reference in the retained v1.0 record exists",
                  all(subprocess.run(["git", "cat-file", "-e", f"{history[field]}^{{commit}}"],
                                     cwd=ROOT, capture_output=True).returncode == 0
                      for field in ("originalReleaseApprovalCommit", "canonicalSourceApprovalCommit",
                                    "formerArtifactRecoveryCommit")))
    results.check("the retained v1.0 record records the frozen game baseline and the retained case number",
                  any(GAME_COMMIT in note for note in history["migrationNotes"])
                  and any("keeps its runtime case number" in note for note in history["migrationNotes"]))
    owner_approval = approval_path.read_text(encoding="utf-8")
    results.check("the retained v1.0 owner-approval record is unchanged and still describes v1.0",
                  all(token in owner_approval for token in
                      ["Nate / Owner", RETAINED_APPROVAL_DATE, "APPROVED_STABLE", "OWNER_REVIEW_PASS",
                       "READY_TO_MERGE", "On-screen content and visual review: **PASS**",
                       "Generated PDF review: **PASS**",
                       "Physical print at 100% / Actual Size: **PASS**",
                       "NO_GENERATED_ARTIFACTS_COMMITTED", GAME_COMMIT])
                  and "v1.1" not in owner_approval)
    results.check("both retained v1.0 records are byte-identical to synchronised main",
                  all(subprocess.run(["git", "show",
                                      f"{SYNCHRONISED_MAIN}:{path.relative_to(ROOT).as_posix()}"],
                                     cwd=ROOT, capture_output=True).stdout == path.read_bytes()
                      for path in (history_path, approval_path)))
    results.check("no v1.1 release or owner-approval record has been written",
                  not (CASE_ROOT / "history/release-v1.1.json").exists()
                  and not (CASE_ROOT / "history/CASE01_OWNER_APPROVAL_v1.1.md").exists())
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
             f"{commit}:sss/campaign-2/case-01-heavy-hands/source/{name}"],
            cwd=ROOT, capture_output=True)
        return hashlib.sha256(run.stdout).hexdigest() if run.returncode == 0 else ""

    source_names = {"content": "content.html", "presentation": "presentation.css",
                    "taskRegistry": "task-registry.js", "layoutOverrides": "layout-overrides.json"}
    results.check("the retained v1.0 record still pins the historically inaccurate commit, unrewritten",
                  history["canonicalSourceApprovalCommit"] == RETAINED_PINNED_COMMIT
                  and blob_hash(RETAINED_PINNED_COMMIT, "task-registry.js")
                  != history["sourceHashes"]["taskRegistry"],
                  blob_hash(RETAINED_PINNED_COMMIT, "task-registry.js")[:16])
    results.check("the commit that actually contains every certified v1.0 source is recorded",
                  all(blob_hash(RETAINED_SOURCE_BEARING_COMMIT, source_names[key])
                      == history["sourceHashes"][key]
                      for key in ("content", "presentation", "taskRegistry")),
                  RETAINED_SOURCE_BEARING_COMMIT)

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
                  [entry["id"] for entry in registry["tasks"]] == [f"C2-C01-T{n}" for n in expected_numbers])
    results.check("role page counts agree between the package and the task registry",
                  registry["roles"] == {role: package["rolePageStructure"][role]["pageCount"]
                                        for role in ROLES}
                  and {role: len(soup.select(f'.page[data-role="{role}"]')) for role in ROLES}
                  == registry["roles"],
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
                      for name in ["Vressk botanist", "Centrifuge sensor array", "Gorlroot specimen",
                                   "Vressk botanical archive", "Federation database"]))

    # ── Numerical ledger ─────────────────────────────────────────────
    printable = visible_text(soup, ROLES)
    asserted = re.sub(r"\s+", " ", asserted_text(content, ROLES))
    missing = [value for value in REQUIRED_LEDGER_STRINGS if value not in printable]
    results.check("every frozen value used in the packet appears exactly as reported", not missing, missing)
    precision_findings = [reason for pattern, reason in PRECISION_PATTERNS if pattern.search(asserted)]
    results.check("reported precision is preserved in both directions", not precision_findings,
                  precision_findings)
    results.check("both learner editions state in plain language that only the strength changes",
                  all("pulled the same way — outward, away from the middle" in visible_text(soup, [role])
                      for role in ["student", "accessible"]))
    results.check("the raw gravity profile stays out of the learner editions",
                  not any(value in visible_text(soup, ["student", "accessible"])
                          for value in ["2.0991 g", "2.1009 g", "0.00187 g", "2.88966 RPM", "224.8 m"]))
    results.check("the numerical ledger records both difference values and why they differ",
                  registry["numericalLedger"]["reportedDifferenceG"] == "0.00187"
                  and registry["numericalLedger"]["differenceOfRoundedEndpointsG"] == "0.0018"
                  and "do not conflict" in registry["numericalLedger"]["roundingNote"])
    results.check("the ledger records that the specification bounded the midpoint only",
                  registry["numericalLedger"]["specification"]["boundsMidpointOnly"] is True
                  and registry["numericalLedger"]["specification"]["acrossBedToleranceSpecified"] is False)
    results.check("the source-status ledger names an established-physics comparison and case evidence",
                  set(registry["sourceStatus"]) >= {"establishedEarthScienceComparison", "caseSpecificEvidence"}
                  and "a = ω²r" in registry["sourceStatus"]["establishedEarthScienceComparison"]
                  and not INVENTED_SCENARIO_REMINDER.search(json.dumps(registry, ensure_ascii=False)),
                  sorted(registry["sourceStatus"]))

    # ── Established physics versus case evidence ─────────────────────
    results.check("both learner editions attribute the case values to this investigation",
                  len(PROVENANCE.findall(visible_text(soup, ["student"]))) >= 3
                  and len(PROVENANCE.findall(visible_text(soup, ["accessible"]))) >= 3,
                  {"student": len(PROVENANCE.findall(visible_text(soup, ["student"]))),
                   "accessible": len(PROVENANCE.findall(visible_text(soup, ["accessible"])))})
    results.check("the Teacher Guide separates established science, case evidence, inference, and engineering layers",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["Established Earth science", "Case-specific evidence", "Case inference",
                       "Engineering extrapolation"]))
    results.check("the source boundary states the named relationship and its assessment limit",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["a = ω²r", "Assessment boundary", "requires no calculation"]))
    results.check("no mathematics standard is claimed once the arithmetic is removed",
                  "No mathematics standard is claimed" in visible_text(soup, ["teacher"])
                  and not re.search(r"CCSS|6\.EE|6\.RP", visible_text(soup, ROLES)))
    results.check("the rounding relationship is Teacher-facing only",
                  "0.0018 g" in visible_text(soup, ["teacher"])
                  and "0.0018 g" not in visible_text(soup, ["student", "accessible"])
                  and "Optional extension" in visible_text(soup, ["teacher"]))
    analogy_blocks = soup.select("[data-analogy]")
    results.check("the teaching analogy is present in both learner editions and marked as an analogy",
                  {node.find_parent(class_="page").get("data-role") for node in analogy_blocks}
                  == {"student", "accessible"},
                  [node.find_parent(class_="page").get("data-page-id") for node in analogy_blocks])
    results.check("the analogy states plainly that its values are not habitat measurements",
                  bool(analogy_blocks) and all(
                      "not measurements from the habitat" in node.get_text(" ", strip=True)
                      for node in analogy_blocks))
    analogy_free = BeautifulSoup(content, "html.parser")
    for node in analogy_free.select("[data-analogy]"):
        node.decompose()
    results.check("the invented ride values never appear outside the analogy block",
                  not re.search(r"pull of (?:2|5|8)\b", visible_text(analogy_free, ROLES)))
    results.check("the task registry records the analogy and why the real spread is unteachable",
                  "teachingAnalogy" in registry["sourceStatus"]
                  and any("30 RPM" in note for note in registry["productionCautions"]))
    # The Accessible edition must be genuinely rewritten, not the Student edition reflowed.
    # Every approved case sits between 43% and 68% word-sequence similarity; a refactor that
    # shares task blocks verbatim between editions pushes this above 90%.
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
                      or figure.select("polyline,polygon")]
    results.check("no figure draws a continuous curve or joins the reported points",
                  not curve_findings, curve_findings)
    results.check("every figure caption attributes its data to a measurement made in this case",
                  all(PROVENANCE.search(figure.select_one("figcaption").get_text(" ", strip=True))
                      for figure in figures),
                  [figure.get("data-figure-id") for figure in figures
                   if not PROVENANCE.search(figure.select_one("figcaption").get_text(" ", strip=True))])
    results.check("every figure caption states the limit of what it reports",
                  all(re.search(r"no intermediate values|no deformation quantity|"
                                r"discrete|qualitative",
                                figure.select_one("figcaption").get_text(" ", strip=True), re.I)
                      for figure in figures))
    profile_figures = [f for f in figures if "profile" in (f.get("data-figure-id") or "")]
    results.check("the radial-section figure states that the direction is identical at every radius",
                  bool(profile_figures)
                  and all(re.search(r"same way — outward|same way: radially outward|"
                                    r"direction is the same at all three",
                                    f.get_text(" ", strip=True), re.I) for f in profile_figures),
                  [f.get("data-figure-id") for f in profile_figures])
    span_figures = [f for f in figures if "span" in (f.get("data-figure-id") or "")]
    results.check("the tuber-span figure attaches no deformation quantity",
                  bool(span_figures)
                  and all("no deformation quantity" in f.get_text(" ", strip=True) for f in span_figures),
                  [f.get("data-figure-id") for f in span_figures])
    results.check("every graph is paired with a data-table equivalent on the same page",
                  all(figure.find_parent(class_="page").select_one("table.data-table")
                      for figure in figures))
    results.check("figure marks use patterns or shared markers rather than colour alone",
                  all(figure.select("pattern") or figure.select("marker") for figure in figures))
    results.check("figure provenance is recorded in the task registry",
                  len(registry.get("figureProvenance", [])) >= 2
                  and all(entry.get("kind", "").startswith("curriculum-original")
                          for entry in registry["figureProvenance"]))

    # ── Prohibited scientific overstatement ──────────────────────────
    prohibited_findings = [reason for pattern, reason in PROHIBITED if pattern.search(asserted)]
    results.check("no printable role asserts a prohibited scientific overstatement",
                  not prohibited_findings, prohibited_findings)
    results.check("the prohibited-claim registry is declared for the case",
                  len(registry.get("prohibitedClaims", [])) >= 15)
    results.check("the production cautions record the direction and precision rules",
                  any("outward at every sampled radius" in note for note in registry["productionCautions"])
                  and any("0.00187" in note for note in registry["productionCautions"]))
    results.check("the Teacher Guide names the prohibited claims for correction",
                  all(term in visible_text(soup, ["teacher"]) for term in
                      ["Claims to correct on sight", "Data-use cautions", "Figure provenance"]))
    results.check("enumerated alternatives and quoted misconceptions are explicitly marked",
                  bool(soup.select("[data-candidate-claim]")) and bool(soup.select("[data-quoted-claim]")))
    results.check("quoted misconceptions appear only inside the Teacher Guide",
                  all(node.find_parent(class_="page").get("data-role") == "teacher"
                      for node in soup.select("[data-quoted-claim]")))
    results.check("learner explanations are required to be qualified rather than proven",
                  all(term in visible_text(soup, ["student"]) for term in
                      ["cannot establish", "does not establish", "magnitude", "outward"]))
    results.check("the correct diagnosis and its three rejected alternatives are declared",
                  bool(registry["correctDiagnosis"]) and len(registry["incorrectAlternatives"]) == 3)

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
                      ["Completed classification", "Who feels the strongest pull",
                       "Cara lying down compared with Ana sitting",
                       "The question to ask the botanist next", "What the habitat rule forgot to say",
                       "Why a thick tuber feels more of a difference",
                       "Completed five-source analysis", "Completed diagnosis analysis",
                       "Completed rejections", "CLAIM", "EVIDENCE", "REASONING",
                       "Monitored trial and stop rule"]))
    results.check("Answer Key exemplars preserve the required qualifiers",
                  all(term in answer_text for term in
                      ["only the strength differs", "best-supported", "in this habitat",
                       "does not establish", "a monitored trial"]))
    results.check("the Answer Key separates a measurement being correct from being sufficient",
                  "measurement being correct from a measurement being sufficient" in answer_text)
    results.check("the Answer Key uses only riders introduced in the analogy",
                  not re.search(r"\bDev\b", visible_text(soup, ROLES)))
    results.check("the Teacher Guide keeps the rounding explanation as an optional extension",
                  "cannot recover precision" in visible_text(soup, ["teacher"]))
    results.check("the completed mechanism model is a five-stage process contract",
                  len(soup.select('.page[data-role="answer"] '
                                  '[data-process-contract="gradient-response-five-stage-v1.0"] '
                                  '.path-stage')) == 5)

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
    results.check("the draft ships no owner-applied layout overrides",
                  layout["overrides"] == {} and layout["student"]["overrides"] == {})

    # ── Evidence availability: every graded claim answerable from each learner edition ──
    role_pages = {role: soup.select(f'.page[data-role="{role}"]') for role in ROLES}
    task_page_index = {}
    for role in ("student", "accessible"):
        for index, page in enumerate(role_pages[role]):
            for node in page.select("[data-shell-task-heading]"):
                task_page_index.setdefault((role, int(node["data-shell-task-heading"])), index)
    page_text = {role: [" ".join(page.stripped_strings) for page in role_pages[role]] for role in ROLES}

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
                    availability_findings.append(f"{label}: {role} lacks {fragment!r} by page {limit + 1}")
    results.check("every graded Answer Key expectation is answerable from each learner edition "
                  "at or before the task that assesses it",
                  not availability_findings, availability_findings)
    withheld_in_key = [value for value in WITHHELD_FROM_LEARNERS
                       if value in visible_text(soup, ["answer"])]
    # Requirements derived from the Answer Key itself, so a new graded claim cannot smuggle in
    # a value learners do not hold. Every reported quantity and record identifier the Answer Key
    # uses under a task must already be printed, in both learner editions, on or before the page
    # that carries that task.
    answer_task_text: dict[int, list[str]] = {}
    for page in role_pages["answer"]:
        current = None
        for node in page.select(".content-area *"):
            if node.has_attr("data-shell-task-heading"):
                current = int(node["data-shell-task-heading"])
                continue
            if current is not None and node.name in {"p", "td", "li"}:
                answer_task_text.setdefault(current, []).append(node.get_text(" ", strip=True))
    derived_findings = []
    for task, chunks in sorted(answer_task_text.items()):
        tokens = sorted(set(REPORTED_TOKEN.findall(" ".join(chunks))))
        for token in tokens:
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
    results.check("no Answer Key expectation requires a value withheld from the learner editions",
                  not withheld_in_key, withheld_in_key)
    withheld_in_learners = [value for value in WITHHELD_FROM_LEARNERS
                            if value in visible_text(soup, ["student", "accessible"])]
    results.check("no withheld value leaks into a learner edition",
                  not withheld_in_learners, withheld_in_learners)
    results.check("the task registry declares the evidence-availability policy it is validated against",
                  set(registry["learnerEvidencePolicy"]["withheldFromLearners"]) == set(WITHHELD_FROM_LEARNERS)
                  and all(value in visible_text(soup, ["student"])
                          and value in visible_text(soup, ["accessible"])
                          for value in registry["learnerEvidencePolicy"]["suppliedToLearners"]),
                  registry["learnerEvidencePolicy"]["suppliedToLearners"])

    # ── Supported controls: only what the game reports as varied may be taught as tested ──
    controls = registry["historicalControls"]
    results.check("the controls ledger marks exactly the two conditions the runtime reports as varied",
                  {entry["condition"] for entry in controls if entry["changedBetweenPlantings"]}
                  == TESTED_CONDITIONS
                  and all(entry["ruledOut"] is False for entry in controls)
                  and all(entry.get("canonicalSource") and entry.get("canonicalEvidence")
                          for entry in controls),
                  sorted(entry["condition"] for entry in controls if entry["changedBetweenPlantings"]))
    results.check("no condition in the ledger is recorded as ruled out",
                  not [entry["condition"] for entry in controls if entry["ruledOut"]])
    control_findings = unsupported_control_findings(asserted)
    results.check("no printable role presents nutrients, light or water as a tested or eliminated control",
                  not control_findings, control_findings)
    answer_rows = {row.select("td")[0].get_text(" ", strip=True):
                   row.select("td")[1].get_text(" ", strip=True)
                   for row in soup.select('.page[data-role="answer"] table.classify-table tbody tr')
                   if len(row.select("td")) == 2}
    results.check("the Answer Key marks the present-reading conditions N, not verified",
                  answer_rows.get("Nutrient supply", "").startswith("N")
                  and answer_rows.get("Grow-light spectrum", "").startswith("N")
                  and answer_rows.get("Soil mineral formulation", "").startswith("Y")
                  and answer_rows.get("Seed stock", "").startswith("Y")
                  and answer_rows.get("Ring radius and rotation rate", "").startswith("N"),
                  answer_rows)
    results.check("both learner editions print the present-condition report the classification needs",
                  all("Nutrients: precise" in visible_text(soup, ["student"])
                      or "nutrients precise" in visible_text(soup, ["student"]) for _ in (0,))
                  and ("Nutrients: precise" in visible_text(soup, ["accessible"])
                       or "nutrients precise" in visible_text(soup, ["accessible"])))
    results.check("both learner editions tell learners that N is not a ruling-out",
                  all(N_IS_NOT_RULING_OUT.search(visible_text(soup, [role]))
                      for role in ("student", "accessible")))

    # ── Source attribution ───────────────────────────────────────────
    blocks = [node for role in ROLES for page in role_pages[role]
              for node in page.select("td, li, p, div.teacher-note")]
    absence_findings = [node.get_text(" ", strip=True)[:90] for node in blocks
                        if NOMINAL_EXPANSION.search(node.get_text(" ", strip=True))
                        and UNREPORTED_ABSENCE.search(node.get_text(" ", strip=True))
                        and "botanist" not in node.get_text(" ", strip=True).lower()
                        and not node.select_one("[data-quoted-claim]")
                        and node.get("data-quoted-claim") is None]
    results.check("a nominal ring status is never expanded into an unreported absence",
                  not absence_findings, absence_findings)
    results.check("the negligible judgement is attributed to the botanist, not the archive",
                  not ARCHIVE_NEGLIGIBLE.search(asserted)
                  and "It is the botanist, not the archive" in visible_text(soup, ["teacher"]),
                  bool(ARCHIVE_NEGLIGIBLE.search(asserted)))
    gc1445_blocks = [node for node in soup.select("tr, li, p, div.teacher-note")
                     if "GC-1445" in node.get_text(" ", strip=True)]
    results.check("every use of GC-1445 carries the qualifier the record attaches to it",
                  bool(gc1445_blocks)
                  and all("low gravitropic precision" in node.get_text(" ", strip=True)
                          for node in gc1445_blocks),
                  [node.get_text(" ", strip=True)[:80] for node in gc1445_blocks
                   if "low gravitropic precision" not in node.get_text(" ", strip=True)])
    results.check("GC-1445 stays Teacher-facing and is never used as radius evidence",
                  all(node.find_parent(class_="page").get("data-role") == "teacher"
                      for node in gc1445_blocks if node.find_parent(class_="page"))
                  and "GC-1445" not in visible_text(soup, ["student", "accessible", "answer"])
                  and "gradient sensitivity is species-dependent" in visible_text(soup, ["teacher"]).lower()
                  and "does not establish that a 300 m radius prevents misalignment"
                  in visible_text(soup, ["teacher"]))
    universal_findings = [reason for pattern, reason in UNIVERSAL_SENSITIVITY if pattern.search(asserted)]
    results.check("no role generalises gradient sensitivity across species",
                  not universal_findings, universal_findings)
    results.check("the precedent ledger keeps the GC-1445 qualifier and its evidentiary limit",
                  any(entry["record"] == "GC-1445"
                      and entry.get("qualifier") == "low gravitropic precision"
                      and "species-dependent" in entry.get("conclusion", "")
                      and "Not evidence" in entry.get("role", "")
                      for entry in registry["numericalLedger"]["precedents"]))

    # ── Teacher–task synchronisation ─────────────────────────────────
    teacher_text = visible_text(soup, ["teacher"])
    annotated = {int(match.group(1)) for match in
                 re.finditer(r"Task (\d)\.", " ".join(
                     node.get_text(" ", strip=True) for node in
                     soup.select('.page[data-role="teacher"] li strong')))}
    results.check("the Teacher Guide carries annotated guidance for every task",
                  annotated == set(expected_numbers), sorted(annotated))
    stale_findings = [reason for pattern, reason in STALE_CALCULATION if pattern.search(teacher_text)]
    results.check("no stale calculation instruction survives in the Teacher Guide",
                  not stale_findings, stale_findings)
    results.check("the Teacher Guide states plainly that no task asks for arithmetic",
                  "No task in this packet asks for arithmetic of any kind." in teacher_text)
    rubric_cells = [cell.get_text(" ", strip=True)
                    for cell in soup.select('.page[data-role="teacher"] table.rubric td')]
    criteria_cards = [card.get_text(" ", strip=True)
                      for card in soup.select('.page[data-role="teacher"] .teacher-card')]
    objectives = [node.get_text(" ", strip=True) for node in
                  soup.select('.page[data-page-id="teacher-guide-01"] ul li')]
    ungradeable = [text for text in rubric_cells + criteria_cards
                   if any(value in text for value in WITHHELD_FROM_LEARNERS)]
    results.check("no rubric dimension or success criterion grades a value learners never receive",
                  not ungradeable, ungradeable)
    results.check("no measurable objective grades a value learners never receive",
                  not [text for text in objectives
                       if any(value in text for value in WITHHELD_FROM_LEARNERS)],
                  [text[:70] for text in objectives
                   if any(value in text for value in WITHHELD_FROM_LEARNERS)])
    results.check("the formal rubric keeps four dimensions and none of them is the withdrawn Precision one",
                  len(soup.select('.page[data-role="teacher"] table.rubric tbody tr')) == 4
                  and not any(row.select("td")[0].get_text(strip=True) == "Precision"
                              for row in soup.select('.page[data-role="teacher"] table.rubric tbody tr')),
                  [row.select("td")[0].get_text(strip=True)
                   for row in soup.select('.page[data-role="teacher"] table.rubric tbody tr')])

    # ── Standards ────────────────────────────────────────────────────
    declared = {entry["code"] for entry in registry["standards"]}
    withdrawn = {entry["code"] for entry in registry["withdrawnStandards"]}
    results.check("the registry claims exactly the three supported standards",
                  declared == STANDARDS_CLAIMED, sorted(declared))
    results.check("MS-ETS1-3 is recorded as withdrawn and no standard replaces it",
                  STANDARDS_WITHDRAWN <= withdrawn
                  and len(declared) == 3
                  and not declared & STANDARDS_WITHDRAWN,
                  sorted(withdrawn))
    results.check("no printable role claims MS-ETS1-3 as a direct or supporting alignment",
                  not re.search(r"(?:Direct|Supporting)\s+(?:assessment|alignment):\s*MS-ETS1-3",
                                visible_text(soup, ROLES))
                  and "MS-ETS1-3 was claimed in v1.0 and is withdrawn" in teacher_text)
    results.check("every retained standard names a real assessing task and the learner evidence it rests on",
                  all(entry["assessingTasks"]
                      and set(entry["assessingTasks"]) <= set(expected_numbers)
                      and (entry.get("learnerEvidence") or entry.get("limitation"))
                      for entry in registry["standards"]),
                  [entry["code"] for entry in registry["standards"]])
    results.check("the conditional standard keeps its limitation in both the registry and the guide",
                  any(entry["code"] == "MS-ETS1-2" and entry["claim"] == "supporting"
                      and entry.get("conditional") is True and entry.get("limitation")
                      for entry in registry["standards"])
                  and "conditional" in teacher_text
                  and "If you do not run that comparison, do not claim it." in teacher_text)
    results.check("no withdrawn mathematics standard returns for incidental arithmetic",
                  any(entry["code"] == "mathematics" for entry in registry["withdrawnStandards"])
                  and not re.search(r"CCSS|6\.EE|6\.RP|7\.RP", visible_text(soup, ROLES)))

    # ── Revision propagation ─────────────────────────────────────────
    readme = (CASE_ROOT / "README.md").read_text(encoding="utf-8")
    static_source = (ROOT / "apps/curriculum-editor/tests/validate_static.py").read_text(encoding="utf-8")
    harness = (ROOT / "apps/curriculum-editor/tests/browser-harness.html").read_text(encoding="utf-8")
    case_registry = json.loads(
        (ROOT / "shared/implementation/case-registry.v2.json").read_text(encoding="utf-8"))
    entry = next(item for campaign in case_registry["curricula"][0]["campaigns"]
                 for item in campaign["cases"] if item["id"] == CASE_ID)
    results.check("the candidate version is carried by every version-bearing field",
                  package["documentKey"] == f"{CASE_ID}:v{CANDIDATE_VERSION}:curriculum-editor-v2"
                  and all(f"_v{CANDIDATE_VERSION}_CUSTOM.html" in name
                          for name in package["outputs"].values())
                  and f"v{CANDIDATE_VERSION}" in package["accessibility"]["documentTitle"]
                  and f"v{CANDIDATE_VERSION}" in package["accessibility"]["loadAnnouncement"]
                  and f'data-editor-content="sss-c2-case01-v{CANDIDATE_VERSION}"' in content
                  and entry["version"] == CANDIDATE_VERSION,
                  package["documentKey"])
    results.check("the registry entry is an unreleased corrective candidate with no history record",
                  entry["status"] == "OWNER_GATE_OPEN" and entry["packageStatus"] == "OWNER_REVIEW"
                  and "historyRecord" not in entry
                  and entry["approval"] == {"owner": "Nate / Owner",
                                            "status": "OWNER_REVIEW_IN_PROGRESS",
                                            "printStatus": "NOT_RUN"},
                  entry)
    results.check("Case 01 holds no frozen DOM baseline while the candidate is unreleased",
                  f'"{CASE_ID}": {{"student"' not in static_source)
    results.check("page counts agree across the DOM, the package, the registry, the README, "
                  "the static roster and the browser harness",
                  {role: len(role_pages[role]) for role in ROLES} == ROLE_PAGES
                  and registry["roles"] == ROLE_PAGES
                  and {role: package["rolePageStructure"][role]["pageCount"] for role in ROLES} == ROLE_PAGES
                  and "Role page counts: Student 5, Teacher 9, Answer Key 4, Accessible 8." in readme
                  and '"SSS-C2-CASE01": {"version": "1.1", "status": "OWNER_GATE_OPEN", "tasks": 8, '
                      '"counts": {"student": 5, "teacher": 9, "answer": 4}}' in static_source
                  and 'id: "SSS-C2-CASE01", label: "1 - Heavy Hands", version: "1.1", '
                      'status: "OWNER_GATE_OPEN", reviewStatus: "OWNER_REVIEW_IN_PROGRESS", '
                      'counts: { student: 5, teacher: 9, answer: 4 }' in harness,
                  {role: len(role_pages[role]) for role in ROLES})
    results.check("the corrected merry-go-round geometry propagated to every file that states it",
                  "two metres across" not in teacher_text
                  and "two metres across" not in readme
                  and "2 m across" not in json.dumps(registry, ensure_ascii=False)
                  and "radius of about two metres" in teacher_text
                  and "radius of about two metres" in readme
                  and any("radius of about 2 m" in note for note in registry["productionCautions"]))
    results.check("the README records the withdrawal and the evidence-availability rule",
                  "`MS-ETS1-3` was claimed" in readme and "**withdrawn**" in readme
                  and "must be producible from" in readme
                  and "be expanded into unreported absences" in readme)
    results.check("the source ledger and the controls ledger tell the same story about the botanist",
                  "nutrients, light and water are reported at present values that were never varied"
                  in registry["sourceLedger"][0]["establishes"]
                  and "is not ruled out" in registry["sourceLedger"][0]["cannotEstablishAlone"]
                  and "ruled out" in registry["controlsPolicy"])

    payload = {
        "validator": "sss-c2-case01-v1",
        "status": "PASS" if results.passed == len(results.assertions) else "FAIL",
        "passed": results.passed,
        "total": len(results.assertions),
        "assertions": results.assertions,
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
