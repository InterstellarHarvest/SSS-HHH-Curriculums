#!/usr/bin/env python3
"""Case-scoped assertions for SSS Campaign 2 Case 03 — The Wrong Color of Light.

Enforces the frozen source ledger, the five-clue instructional coverage, the figure
contract, the Earth-science/fiction labels, and the prohibited scientific
overstatements against the printable content of every role.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[3]
CASE_ID = "SSS-C2-CASE03"
CASE_ROOT = ROOT / "sss/campaign-2/case-03-wrong-color-light"
SOURCE = CASE_ROOT / "source"
GAME_COMMIT = "46b9387bca95736f164f905596e3dd8b13968661"
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
    results.check("unreleased package declares no approval or release history",
                  package["status"] == "DRAFT"
                  and package["approval"]["status"] == "OWNER_REVIEW_NOT_STARTED"
                  and package["approval"]["printStatus"] == "NOT_RUN"
                  and "releaseHistory" not in package
                  and not (CASE_ROOT / "history").exists())
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
