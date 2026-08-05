#!/usr/bin/env python3
"""Case-scoped assertions for SSS Campaign 2 Case 01 — Heavy Hands.

Enforces the frozen source ledger, the five-clue instructional coverage, the figure
contract, the physics/case-evidence boundary, and the prohibited scientific
overstatements against the printable content of every role.

The case turns on one distinction: across the radial depth of the soil bed the reported
direction is outward everywhere and only the magnitude changes. Most of the prohibited
patterns below exist to keep that distinction intact in every role.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[3]
CASE_ID = "SSS-C2-CASE01"
CASE_ROOT = ROOT / "sss/campaign-2/case-01-heavy-hands"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "29c3b222c53f51de11a3aa83e896a6d0ef6fb490"
DRAFT_VERSION = "1.0"
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

    # ── DRAFT lifecycle: no release history, no approval, no artifacts ──
    results.check("the package records an unstarted draft lifecycle",
                  package["status"] == "DRAFT"
                  and package["version"] == DRAFT_VERSION
                  and package["approval"] == {"owner": "Nate / Owner",
                                              "status": "OWNER_REVIEW_NOT_STARTED",
                                              "printStatus": "NOT_RUN"},
                  package["approval"])
    results.check("the task registry records the same unstarted draft lifecycle",
                  (registry.get("version"), registry.get("status"), registry.get("ownerReviewStatus"),
                   registry.get("mergeStatus"), registry.get("approvalDate"), registry.get("approvedBy"))
                  == (DRAFT_VERSION, "DRAFT", "OWNER_REVIEW_NOT_STARTED", "NOT_READY", None, None))
    results.check("the draft declares no release history and stores no history directory",
                  "releaseHistory" not in package and not (CASE_ROOT / "history").exists())
    results.check("no generated release artifact is stored beside the draft case",
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
    results.check("Campaign 2 draft case folder uses the canonical lean layout",
                  top_level == {"README.md", "source"}
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
    results.check("the profile is reported as outward at all three radii in every learner edition",
                  all(visible_text(soup, [role]).count("outward") >= 3
                      for role in ["student", "accessible"]),
                  {role: visible_text(soup, [role]).count("outward") for role in ["student", "accessible"]})
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
                      ["Completed classification", "Radius and reported magnitude at the bed base",
                       "Where the accelerometer was placed", "What one reading could not show",
                       "Why a thick tuber feels more of a difference",
                       "Completed five-source analysis", "Completed diagnosis analysis",
                       "Completed rejections", "CLAIM", "EVIDENCE", "REASONING",
                       "Monitored trial and stop rule"]))
    results.check("Answer Key exemplars preserve the required qualifiers",
                  all(term in answer_text for term in
                      ["only the magnitude differs", "best-supported", "in this habitat",
                       "does not establish", "a monitored trial"]))
    results.check("the Answer Key separates a measurement being correct from being sufficient",
                  "measurement being correct from a measurement being sufficient" in answer_text)
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
