#!/usr/bin/env python3
"""Final SSS remediation transformer v3.

Builds on v2 and applies the remaining audit-backed Teacher fixes exposed by the
cross-edition gate:
- Mars Habitat: make Tasks 1, 4 and 5 explicit in the existing 60-minute route.
- Hayes Orbital Station: add the missing authoritative science references and
  correct the stale Accessible page-count statement.

All edits preserve existing package page counts and update canonical content
hashes. Re-running the script is idempotent.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup, Tag

import apply_sss_final_remediation as v1
import apply_sss_final_remediation_v2 as v2


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_case(case_dir: Path, soup: BeautifulSoup, package: dict) -> None:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    content_path.write_text(soup.decode(formatter="minimal"), encoding="utf-8")
    if "sourceHashes" in package and "content" in package["sourceHashes"]:
        package["sourceHashes"]["content"] = sha256(content_path)
    package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def remediate_case03_procedure(case_dir: Path, apply: bool) -> bool:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    soup = BeautifulSoup(content_path.read_text(encoding="utf-8"), "html.parser")
    if soup.select_one('[data-final-c1c3-procedure="v2.0"]'):
        return False

    page = soup.select_one('[data-role="teacher"][data-page-id="teacher-guide-03"]')
    procedure = page.select_one(".procedure") if page else None
    if not procedure:
        raise RuntimeError("C1 Case 03 Teacher procedure container not found")

    rows = [node for node in procedure.find_all("div", recursive=False) if node.find("span", class_="time", recursive=False)]
    frame = next((row for row in rows if row.find("span", class_="time").get_text(" ", strip=True) == "5-10"), None)
    analyze = next((row for row in rows if row.find("span", class_="time").get_text(" ", strip=True) == "28-38"), None)
    explain = next((row for row in rows if row.find("span", class_="time").get_text(" ", strip=True) == "38-50"), None)
    transfer = next((row for row in rows if row.find("span", class_="time").get_text(" ", strip=True) == "50-60"), None)
    if not all((frame, analyze, explain, transfer)):
        raise RuntimeError("C1 Case 03 expected procedure timing rows not found")

    frame_p = frame.find("p")
    frame_p.clear()
    frame_p.append("Complete ")
    strong = soup.new_tag("strong", attrs={"class": "task-reference"})
    strong.string = "1 · Define the measurement"
    frame_p.append(strong)
    frame_p.append(": define PPFD without revealing the diagnosis, including one thing the total quantity reading cannot show.")

    pattern_row = BeautifulSoup(
        '''<div data-final-c1c3-procedure="v2.0"><span class="time">38-44</span><div><strong>Pattern / diagnose</strong><p>Complete <strong class="task-reference">4 · Connect the symptom pattern</strong>, then <strong class="task-reference">5 · Select and reject diagnoses</strong>. Require the tissue/root pattern to test alternatives before the mechanism is sequenced.</p></div></div>''',
        "html.parser",
    ).div
    analyze.insert_after(pattern_row)

    explain.find("span", class_="time").string = "44-52"
    transfer.find("span", class_="time").string = "52-60"
    procedure["data-final-c1c3-procedure"] = "v2.0"

    if apply:
        package = json.loads(package_path.read_text(encoding="utf-8"))
        write_case(case_dir, soup, package)
    return True


def remediate_case04_teacher(case_dir: Path, apply: bool) -> bool:
    content_path = case_dir / "source/content.html"
    package_path = case_dir / "source/case-package.json"
    soup = BeautifulSoup(content_path.read_text(encoding="utf-8"), "html.parser")
    changed = False

    # Fix stale Teacher statement about the Accessible edition's approved page count.
    for node in list(soup.select('[data-role="teacher"] *')):
        if not isinstance(node, Tag):
            continue
        for text_node in list(node.find_all(string=True, recursive=False)):
            text = str(text_node)
            new = re.sub(r"Accessible Mission\s*(?:=|is|has)?\s*8\s+pages", "Accessible Mission = 6 pages", text, flags=re.I)
            new = re.sub(r"Accessible Mission[^.]{0,40}8\s+pages", lambda m: re.sub(r"8\s+pages", "6 pages", m.group(0), flags=re.I), new, flags=re.I)
            if new != text:
                text_node.replace_with(new)
                changed = True

    if not soup.select_one('[data-final-reference-list="c1c4-v1.0"]'):
        teacher_pages = list(soup.select('[data-role="teacher"]'))
        if not teacher_pages:
            raise RuntimeError("C1 Case 04 Teacher pages not found")
        target = teacher_pages[-1]
        footer = target.find("footer")
        block = BeautifulSoup(
            '''<section data-final-reference-list="c1c4-v1.0"><h2 class="support-heading">Authoritative science references</h2><ol class="references final-reference-list"><li><strong>Dynamics of long-term continuous culture of <em>Limnospira indica</em> in an air-lift photobioreactor.</strong> <span class="source-url">https://pmc.ncbi.nlm.nih.gov/articles/PMC8913870/</span><br/><span class="small">Primary long-duration photobioreactor evidence. Continuous cultivation can be maintained under controlled conditions, while excessive photon flux can produce photoinhibition depending on culture conditions.</span></li><li><strong>Spiral breakage and photoinhibition of <em>Arthrospira platensis</em> caused by accumulation of reactive oxygen species under solar radiation.</strong> <span class="source-url">https://doi.org/10.1016/j.envexpbot.2009.11.010</span><br/><span class="small">Primary evidence connecting excessive irradiance and reactive oxygen stress with photosystem damage, photoinhibition, and reduced growth in <em>Arthrospira</em>.</span></li></ol><p class="small">These sources support the established photosynthetic-stress mechanism only. The Hayes schedule, crash timing, reactor readings, and diagnosis remain case-specific evidence.</p></section>''',
            "html.parser",
        ).section
        if footer:
            footer.insert_before(block)
        else:
            target.append(block)
        changed = True

    if changed and apply:
        package = json.loads(package_path.read_text(encoding="utf-8"))
        write_case(case_dir, soup, package)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--case", action="append", dest="cases")
    args = parser.parse_args()

    selected = args.cases or list(v1.CASE_DIRS)
    changed_cases = 0
    for case_id in selected:
        case_dir = v1.CASE_DIRS.get(case_id)
        if case_dir is None:
            print(f"ERROR unknown case id: {case_id}")
            return 2

        changed, operations = v1.remediate_case(case_id, case_dir, args.apply)
        normalized = case_id == "SSS-C1-CASE03" and v2.normalize_case03_alternative_block(case_dir, args.apply)
        wave3 = False
        if case_id == "SSS-C1-CASE03":
            wave3 = remediate_case03_procedure(case_dir, args.apply)
        elif case_id == "SSS-C1-CASE04":
            wave3 = remediate_case04_teacher(case_dir, args.apply)

        net = bool(changed or normalized or wave3)
        changed_cases += int(net)
        print(f"{case_id}: {'CHANGE' if net else 'NO CHANGE'}")
        for op in operations:
            print(f"  - {op}")
        if normalized:
            print("  - normalized duplicate Mars Habitat alternative-rejection guidance")
        if case_id == "SSS-C1-CASE03" and wave3:
            print("  - made Tasks 1, 4 and 5 explicit in the 60-minute Teacher route")
        if case_id == "SSS-C1-CASE04" and wave3:
            print("  - added Hayes authoritative references and synchronized Accessible page-count guidance")

    print(f"SSS final remediation v3: {'applied' if args.apply else 'planned'}; {changed_cases} case package(s) changed/planned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
