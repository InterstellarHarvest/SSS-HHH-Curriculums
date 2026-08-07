#!/usr/bin/env python3
"""Apply deterministic source-level remediations from the final SSS C1+C2 audit.

This script is intentionally conservative:
- frozen release history is never rewritten;
- only canonical source/package files on a remediation branch are changed;
- approved page counts are preserved in this pass;
- visual-modernization work is not performed here;
- broad science content is not re-authored.

The script is idempotent. Re-running it should produce no additional diff once the
same remediation wave has already been applied.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parents[2]

CASE_DIRS = {
    "SSS-C1-CASE01": ROOT / "sss/campaign-1/case-01-iss-greenhouse",
    "SSS-C1-CASE02": ROOT / "sss/campaign-1/case-02-lunar-greenhouse",
    "SSS-C1-CASE03": ROOT / "sss/campaign-1/case-03-mars-habitat",
    "SSS-C1-CASE04": ROOT / "sss/campaign-1/case-04-hayes-orbital-station",
    "SSS-C1-CASE05": ROOT / "sss/campaign-1/case-05-europa-bunker",
    "SSS-C1-CASE06": ROOT / "sss/campaign-1/case-06-first-contact-protocol",
    "SSS-C1-CASE07": ROOT / "sss/campaign-1/case-07-the-gift",
    "SSS-C2-CASE01": ROOT / "sss/campaign-2/case-01-heavy-hands",
    "SSS-C2-CASE02": ROOT / "sss/campaign-2/case-02-missing-dance",
    "SSS-C2-CASE03": ROOT / "sss/campaign-2/case-03-wrong-color-light",
    "SSS-C2-CASE04": ROOT / "sss/campaign-2/case-04-silent-grove",
    "SSS-C2-CASE05": ROOT / "sss/campaign-2/case-05-too-clean-room",
    "SSS-C2-CASE06": ROOT / "sss/campaign-2/case-06-first-garden",
}

# C1 Case 07 already has a complete four-level analytic rubric. Case 01 is the
# template authority and already carries the common grading system.
RUBRIC_TARGETS = {
    "SSS-C1-CASE02", "SSS-C1-CASE03", "SSS-C1-CASE04", "SSS-C1-CASE05", "SSS-C1-CASE06",
    "SSS-C2-CASE01", "SSS-C2-CASE02", "SSS-C2-CASE03", "SSS-C2-CASE04", "SSS-C2-CASE05", "SSS-C2-CASE06",
}

C2_TWO_PERIOD_CASES = {"SSS-C2-CASE01", "SSS-C2-CASE02", "SSS-C2-CASE03", "SSS-C2-CASE04"}

CONTROLLED_REFERENCES = {
    "SSS-C2-CASE05": [
        ("IAEA Radiation Biology handbook", "https://www-pub.iaea.org/MTCD/Publications/PDF/TCS-42_web.pdf",
         "Absorbed dose is energy per unit mass and is measured in gray; sievert quantities add radiation/tissue weighting."),
        ("Dadachova et al. — Ionizing Radiation Changes the Electronic Properties of Melanin and Enhances the Growth of Melanized Fungi",
         "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0000457",
         "Laboratory analogy only; does not establish radiation-powered photosynthesis or a radiation requirement."),
    ],
    "SSS-C2-CASE06": [
        ("Karst et al. — Positive citation bias and overinterpreted results", "https://www.nature.com/articles/s41559-023-01986-1",
         "Boundary against universal cooperative ‘wood wide web’ claims."),
        ("Arbuscular mycorrhizal fungi influence host infection", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9827988/",
         "Demonstrates that inoculation can carry benefits and risks."),
        ("Inoculation effects spread beyond directly inoculated plants", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5524347/",
         "Supports monitoring for spread beyond directly treated plants."),
        ("Global density and biomass of arbuscular mycorrhizal fungal networks", "https://doi.org/10.1126/science.adu4373",
         "Published global estimate; not a measurement of this garden."),
        ("Mycorrhizal mycelium as a global carbon pool", "https://www.sciencedirect.com/science/article/pii/S0960982223001677",
         "Annual carbon-allocation flux estimate, not permanent stored carbon."),
    ],
}

PREFILLS = {
    "SSS-C1-CASE01": {
        "a-crew-evidence": "Roots do not grow downward; resource adjustments did not fix the pattern.",
        "a-crew-meaning": "This weakens a simple resource explanation and points toward an orientation problem.",
        "a-earth-settle": "settle",
        "a-earth-root": "downward",
    },
    "SSS-C1-CASE03": {
        "a6-2": "Wrong BP-4 filter installed",
    },
    "SSS-C2-CASE05": {
        "a5-nutrient": "The nutrient mix was reformulated four times with no change, and nutrient uptake is normal.",
    },
    "SSS-C2-CASE06": {
        "a3-ph": "The soil pH was corrected years ago and has been checked again since.",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_json_object_from_js(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError(f"Unable to find object literal in {path}")
    return json.loads(text[start : end + 1])


def soup_fragment(html: str) -> list[Tag | NavigableString]:
    fragment = BeautifulSoup(html, "html.parser")
    return list(fragment.contents)


def role_pages(soup: BeautifulSoup, role: str) -> list[Tag]:
    return list(soup.select(f'[data-role="{role}"]'))


def page_content(page: Tag) -> Tag:
    return page.select_one(".content-area") or page.select_one(".content") or page


def append_to_content(page: Tag, html: str) -> None:
    """Append printable blocks to the end of a page's content area.

    The publication footer is a sibling of .content-area inside .page-frame, not a
    child of it, so inserting "before the footer" placed printable material outside
    the content area entirely. Everything downstream -- the page-fit overflow
    contract, the layout-override resize system, and the flex sizing of the frame --
    is defined against .content-area, so misplaced blocks both escaped the overflow
    check and squeezed the real content area until its text overlapped them.
    """
    content = page_content(page)
    for node in soup_fragment(html):
        content.append(node)


# Retained under the historical name so any external caller keeps working; the
# behavior is now the corrected content-area append.
insert_before_footer = append_to_content


def text_of_role(soup: BeautifulSoup, role: str) -> str:
    return " ".join(p.get_text(" ", strip=True) for p in role_pages(soup, role))


def find_task_heading(page_or_role: Tag, task_number: int) -> Tag | None:
    return page_or_role.find(attrs={"data-task-id": str(task_number)}) or page_or_role.find(attrs={"data-shell-task-heading": str(task_number)})


def closest_task_number(node: Tag, role_page: Tag) -> int | None:
    previous = node.find_previous(lambda t: isinstance(t, Tag) and (t.has_attr("data-task-id") or t.has_attr("data-shell-task-heading")))
    if previous is None or previous.find_parent(attrs={"data-role": role_page.get("data-role")}) != role_page:
        return None
    raw = previous.get("data-task-id") or previous.get("data-shell-task-heading")
    return int(raw) if raw and str(raw).isdigit() else None


def set_prefill(soup: BeautifulSoup, persist_id: str, value: str) -> bool:
    node = soup.find(attrs={"data-persist-id": persist_id})
    if not isinstance(node, Tag) or not node.has_attr("data-response"):
        return False
    if node.get("data-prefilled") == "final-audit-v1.0":
        return False
    node["data-prefilled"] = "final-audit-v1.0"
    node.clear()
    node.append(value)
    return True


def persist_print_marks(soup: BeautifulSoup, case_id: str) -> int:
    """Make decorative print check/X boxes writable/persistent without redesigning them."""
    count = 0
    prefixes = {"student": "s", "accessible": "a"}
    for role, prefix in prefixes.items():
        for page in role_pages(soup, role):
            task_counters: dict[int, int] = {}
            for mark in page.select("span.check"):
                if mark.has_attr("data-response"):
                    continue
                task = closest_task_number(mark, page)
                if task is None:
                    continue
                task_counters[task] = task_counters.get(task, 0) + 1
                idx = task_counters[task]
                mark["data-response"] = ""
                mark["data-persist-id"] = f"{prefix}-t{task}-mark-{idx}"
                mark["role"] = "textbox"
                mark["aria-label"] = f"Task {task} mark {idx}"
                mark["data-semantic-action"] = "mark"
                count += 1
    return count


def prefill_alternating_source_contributions(soup: BeautifulSoup, case_id: str) -> int:
    """Reduce repeated Accessible five-source writing while preserving limit reasoning."""
    if not case_id.startswith("SSS-C2-"):
        return 0
    count = 0
    for page in role_pages(soup, "accessible"):
        for table in page.find_all("table"):
            rows = table.find_all("tr")
            data_rows = []
            for row in rows:
                cells = row.find_all(["th", "td"], recursive=False)
                response_cells = [c for c in cells if c.find(attrs={"data-response": True})]
                if len(cells) >= 3 and len(response_cells) >= 2:
                    data_rows.append((row, cells))
            if len(data_rows) != 5:
                continue
            for index in (0, 2, 4):
                _, cells = data_rows[index]
                first = cells[0]
                contribution_response = cells[1].find(attrs={"data-response": True})
                if not isinstance(contribution_response, Tag) or contribution_response.get("data-prefilled"):
                    continue
                source_name = first.find("strong")
                source_name_text = source_name.get_text(" ", strip=True) if source_name else ""
                summary = first.get_text(" ", strip=True)
                if source_name_text and summary.startswith(source_name_text):
                    summary = summary[len(source_name_text) :].strip(" —:-")
                if len(summary) < 8:
                    continue
                contribution_response["data-prefilled"] = "final-audit-v1.0"
                contribution_response.clear()
                contribution_response.append(summary)
                count += 1
    return count


def remove_runtime_identifiers(soup: BeautifulSoup, registry: dict) -> int:
    tokens = list(registry.get("formalClues", []))
    routes = list(registry.get("requiredRoutes", []))
    replacements: dict[str, str] = {}
    route_labels = {
        "crew": "crew conversation",
        "sensors": "sensor panel",
        "plants": "plant examination",
        "logs": "case records",
        "database": "Federation Database",
        "nova": "Dr. Nova conversation",
        "vorn_shael": "Delegate Vorn-Shael conversation",
        "kess": "Delegate Kess conversation",
        "ilreth_mar": "Delegate Ilreth-Mar conversation",
    }
    for route in routes:
        prefix = route.split(".", 1)[0]
        replacements[route] = route_labels.get(prefix, "game evidence source")
    for token in tokens:
        replacements[token] = token.replace("_", " ").lower()

    changed = 0
    for page in role_pages(soup, "teacher"):
        for node in list(page.find_all(string=True)):
            original = str(node)
            new = original
            for old, replacement in replacements.items():
                if old in new:
                    new = new.replace(old, replacement)
            if new != original:
                node.replace_with(new)
                changed += 1
    return changed


def full_rubric_html() -> str:
    return '''
<h3 class="support-heading" data-final-analytic-rubric="v1.0">Analytic rubric · 4/3/2/1</h3>
<table class="data-table rubric final-analytic-rubric" data-rubric-contract="4-3-2-1-v1.0">
<caption>Common analytic rubric — apply to the case's principal diagnosis/explanation and transfer/design work</caption>
<thead><tr><th scope="col">Criterion</th><th scope="col">4 · Accomplished</th><th scope="col">3 · Proficient</th><th scope="col">2 · Developing</th><th scope="col">1 · Beginning</th></tr></thead>
<tbody>
<tr><td>Diagnosis / claim</td><td>States the best-supported explanation accurately and keeps the claim within the evidence boundary.</td><td>States the correct explanation with only minor loss of qualification.</td><td>Names part of the explanation but leaves an important causal or boundary gap.</td><td>Selects an unsupported explanation or does not state a usable claim.</td></tr>
<tr><td>Evidence</td><td>Uses multiple relevant sources, including exact reported values/observations where the task provides them.</td><td>Uses more than one relevant source with generally accurate reporting.</td><td>Uses one useful source or mixes relevant evidence with unsupported detail.</td><td>Provides little usable evidence or materially changes the record.</td></tr>
<tr><td>Mechanism / reasoning</td><td>Connects condition → mechanism → observed effect in a complete causal chain and addresses competing explanations.</td><td>Connects the main cause to the effect with a mostly complete mechanism.</td><td>Gives a cause/effect connection with a missing or reversed step.</td><td>Restates the claim without explaining why the evidence supports it.</td></tr>
<tr><td>Precision / boundaries</td><td>Preserves ranges, inequalities, measured/modeled status, and case-vs-established-science limits that matter here.</td><td>Preserves the important limits with at most a minor wording slip.</td><td>Drops a meaningful qualifier or overstates one part of the evidence.</td><td>Turns bounded evidence into an absolute/universal claim or invents precision.</td></tr>
<tr><td>Transfer / design</td><td>Uses clear criteria/constraints or a testable transfer response with monitoring/stop logic where required.</td><td>Gives a workable response with most required criteria/constraints.</td><td>Proposes a plausible response but omits an important criterion, constraint, control, or monitoring step.</td><td>Asserts a fix without showing how it would be judged or tested.</td></tr>
</tbody></table>'''


def quick_rubric_html() -> str:
    return '''<h3 class="support-heading" data-final-quick-rubric="v1.0">Quick grading</h3>
<p class="teacher-note" data-final-quick-rubric-note="v1.0"><strong>Fast check:</strong> diagnosis/claim correct; evidence from more than one source; causal reasoning complete; important precision/boundaries preserved; transfer/design response testable when required.</p>'''


def ensure_common_rubric(soup: BeautifulSoup, case_id: str) -> int:
    if case_id not in RUBRIC_TARGETS:
        return 0
    teacher_pages = role_pages(soup, "teacher")
    if not teacher_pages:
        return 0
    if soup.select_one('[data-rubric-contract="4-3-2-1-v1.0"]'):
        return 0

    target_page = None
    formal_heading = None
    for page in teacher_pages:
        for heading in page.find_all(["h2", "h3"]):
            txt = heading.get_text(" ", strip=True).lower()
            if "formal grading" in txt or "formal rubric" in txt or "analytic rubric" in txt:
                target_page, formal_heading = page, heading
                break
        if target_page:
            break
    if target_page is None:
        for page in reversed(teacher_pages):
            if re.search(r"grading|assessment|rubric", page.get_text(" ", strip=True), re.I):
                target_page = page
                break
    target_page = target_page or teacher_pages[-1]

    nodes = soup_fragment(full_rubric_html())
    if formal_heading:
        # Remove the old limited table or dimensions paragraph immediately following the formal heading.
        nxt = formal_heading.find_next_sibling()
        while nxt is not None and isinstance(nxt, Tag) and nxt.name not in {"h2", "h3"}:
            following = nxt.find_next_sibling()
            if nxt.name == "table" or (nxt.name == "p" and "dimension" in formal_heading.get_text(" ", strip=True).lower()):
                nxt.decompose()
            nxt = following
        anchor = formal_heading
        formal_heading.string = "Analytic rubric · 4/3/2/1"
        formal_heading["data-final-analytic-rubric"] = "v1.0"
        # Insert only the table because the heading already exists.
        table = BeautifulSoup(full_rubric_html(), "html.parser").find("table")
        anchor.insert_after(table)
    else:
        content = page_content(target_page)
        for node in nodes:
            content.append(node)

    teacher_text = text_of_role(soup, "teacher")
    if not re.search(r"quick\s+(?:grading|rubric)", teacher_text, re.I):
        rubric = soup.select_one('[data-rubric-contract="4-3-2-1-v1.0"]')
        if rubric:
            for node in reversed(soup_fragment(quick_rubric_html())):
                rubric.insert_before(node)
    return 1


def ensure_controlled_references(soup: BeautifulSoup, case_id: str) -> int:
    refs = CONTROLLED_REFERENCES.get(case_id)
    if not refs or soup.select_one('[data-final-reference-list="v1.0"]'):
        return 0
    teacher_pages = role_pages(soup, "teacher")
    if not teacher_pages:
        return 0
    items = "".join(
        f'<li><strong>{title}</strong> — <span class="source-url">{url}</span><br/><span class="small">{note}</span></li>'
        for title, url, note in refs
    )
    html = f'''<h2 class="support-heading" data-final-reference-list="v1.0">Authoritative science references</h2>
<ol class="references final-reference-list">{items}</ol>
<p class="small">These controlled references are reproduced from the frozen game repository's Campaign 2 science-source register. Case-specific measurements and narrative outcomes remain case records rather than Earth-science claims.</p>'''
    insert_before_footer(teacher_pages[-1], html)
    return 1


def explicit_two_period_pacing(soup: BeautifulSoup, case_id: str) -> int:
    if case_id not in C2_TWO_PERIOD_CASES:
        return 0
    teacher_pages = role_pages(soup, "teacher")
    if not teacher_pages or soup.select_one('[data-remediation-pacing="two-period-v1.0"]'):
        return 0
    for page in teacher_pages:
        heading = next((h for h in page.find_all(["h2", "h3"]) if "suggested pacing" in h.get_text(" ", strip=True).lower()), None)
        if heading:
            heading.string = "Recommended two-period route"
            heading["data-remediation-pacing"] = "two-period-v1.0"
            note = BeautifulSoup(
                '<div class="teacher-note" data-remediation-pacing-note="v1.0"><span class="label">Scope integrity</span><p>This full route is intentionally taught across two class periods. Do not make it fit one period by deleting a registry-defined graded source, diagnosis, CER, or design requirement. If only one period is available, assign unfinished graded work for completion rather than narrowing the assessment contract.</p></div>',
                "html.parser",
            ).div
            heading.insert_after(note)
            return 1
    return 0


def fix_heavy_hands_fallback(soup: BeautifulSoup, case_id: str) -> int:
    if case_id != "SSS-C2-CASE01":
        return 0
    changed = 0
    for page in role_pages(soup, "teacher"):
        for node in list(page.find_all(string=True)):
            text = str(node)
            if "shorten the task" in text.lower() or "three sources" in text.lower() and "task 5" in page.get_text(" ", strip=True).lower():
                replacement = re.sub(
                    r"If time is short[^.]*\.",
                    "If time is short, complete as many source rows as the period allows and assign the remaining rows for completion; the graded Task 5 remains a five-source analysis.",
                    text,
                    flags=re.I,
                )
                if replacement != text:
                    node.replace_with(replacement)
                    changed += 1
    return changed


def fix_c2c2_status_code(soup: BeautifulSoup, case_id: str) -> int:
    if case_id != "SSS-C2-CASE02" or soup.find(attrs={"data-remediated-status-code": "v1.0"}):
        return 0
    changed = 0
    replacements = {
        "OK or ?": "SETTLED or RECHECK",
        "write OK if the record already settles that condition and you can stop investigating it, or ? if it is still worth a second look":
            "write SETTLED if the condition can be closed as a causal lead, or RECHECK if the observation is established but the condition still matters to the diagnosis",
        "the first three rows are OK": "the first three rows are SETTLED",
        "The last three are ?": "The last three are RECHECK",
        "Airflow earns a ?": "Airflow earns RECHECK",
    }
    for role in ("student", "accessible", "teacher", "answer"):
        for page in role_pages(soup, role):
            for node in list(page.find_all(string=True)):
                text = str(node)
                new = text
                for old, rep in replacements.items():
                    new = re.sub(re.escape(old), rep, new, flags=re.I)
                # Standalone expected statuses in answer tables.
                if role == "answer":
                    if new.strip() == "OK":
                        new = "SETTLED"
                    elif new.strip() == "?":
                        new = "RECHECK"
                if new != text:
                    node.replace_with(new)
                    changed += 1
    marker = role_pages(soup, "student")[0].find("main") if role_pages(soup, "student") else None
    root = soup.find("main")
    if root:
        root["data-remediated-status-code"] = "v1.0"
    return changed


def fix_c2c4_answer_space(soup: BeautifulSoup, case_id: str) -> int:
    if case_id != "SSS-C2-CASE04" or soup.find(attrs={"data-remediated-dark-hours": "v1.0"}):
        return 0
    changed = 0
    for page in role_pages(soup, "accessible"):
        for node in list(page.find_all(string=True)):
            text = str(node)
            if "You must choose one and say why" in text:
                node.replace_with(
                    text.replace(
                        "You must choose one and say why.",
                        "Use 6 dark hours for the specification and explain why: 5 hours is the recorded trial minimum, while 6 hours is the schedule with a two-year record of full signalling in this grove."
                    )
                )
                changed += 1
    root = soup.find("main")
    if root:
        root["data-remediated-dark-hours"] = "v1.0"
    return changed


def fix_c1c1_exact(soup: BeautifulSoup, case_id: str) -> int:
    if case_id != "SSS-C1-CASE01":
        return 0
    changed = 0
    if not soup.select_one('[data-final-c1c1-task5-procedure="v1.0"]'):
        teacher_pages = role_pages(soup, "teacher")
        if len(teacher_pages) >= 3:
            task4 = find_task_heading(teacher_pages[2], 4)
            # Case 01 uses procedure headings without data-task-id; anchor to exact task-reference text instead.
            anchor = teacher_pages[2].find(string=re.compile(r"4\s*·\s*Test the competing explanations", re.I))
            p = anchor.find_parent("p") if anchor else None
            if p:
                block = BeautifulSoup(
                    '<div class="teacher-note" data-final-c1c1-task5-procedure="v1.0"><span class="technical-label">PROCEDURE · TASK 5</span><span><strong>Before diagnosis:</strong> students complete <strong class="task-reference">5 · Build the mechanism</strong>, ordering the gravity-sensing sequence so the causal chain is explicit before they select the diagnosis.</span></div>',
                    "html.parser",
                ).div
                p.insert_after(block)
                changed += 1
        # Add Task 5 to the Page 1 collection list as an explicit work product.
        if teacher_pages:
            collection = teacher_pages[0].find(string=re.compile(r"3\s*·\s*Investigate four evidence sources"))
            collection_p = collection.find_parent("p") if collection else None
            if collection_p and "5 · Build the mechanism" not in collection_p.get_text(" ", strip=True):
                strong = soup.new_tag("strong", attrs={"class": "task-reference", "data-final-c1c1-task5-procedure": "v1.0"})
                strong.string = "5 · Build the mechanism"
                collection_p.append(" · ")
                collection_p.append(strong)
                changed += 1

    if not soup.select_one('[data-final-c1c1-oi-key="v1.0"]'):
        answer_pages = role_pages(soup, "answer")
        for page in answer_pages:
            h = find_task_heading(page, 3)
            if h:
                block = BeautifulSoup(
                    '''<div class="answer-block" data-final-c1c1-oi-key="v1.0"><strong>Observation / inference classifications:</strong><table class="tech-table compact"><thead><tr><th>Source</th><th>O or I</th></tr></thead><tbody><tr><td>Crew</td><td>O — observation/testimony from the case</td></tr><tr><td>Sensors</td><td>O — measured environmental readings</td></tr><tr><td>Plants</td><td>O — direct plant observations</td></tr><tr><td>Mission logs</td><td>I — the mechanism/explanatory interpretation drawn from the evidence</td></tr></tbody></table></div>''',
                    "html.parser",
                ).div
                next_block = h.find_next_sibling()
                if next_block:
                    next_block.insert_after(block)
                else:
                    h.insert_after(block)
                changed += 1
                break
    return changed


def fix_c1c3_exact(soup: BeautifulSoup, case_id: str) -> int:
    if case_id != "SSS-C1-CASE03":
        return 0
    changed = 0
    # Clarify the >700 nm band boundary without altering a reported transmission value.
    for node in list(soup.find_all(string=True)):
        text = str(node)
        if "700 nm+" in text:
            node.replace_with(text.replace("700 nm+", ">700 nm"))
            changed += 1

    if not soup.select_one('[data-final-c1c3-procedure="v1.0"]'):
        teacher_pages = role_pages(soup, "teacher")
        if len(teacher_pages) >= 3:
            page = teacher_pages[2]
            explain = page.find(string=re.compile(r"At\s+6\s*·\s*Model the mechanism", re.I))
            p = explain.find_parent("p") if explain else None
            if p:
                block = BeautifulSoup(
                    '''<div class="teacher-note" data-final-c1c3-procedure="v1.0"><span class="label">Required task order before the mechanism</span><p>After Tasks 2–3, students complete <strong>4 · Connect the symptom pattern</strong>, then <strong>5 · Select and reject diagnoses</strong>. Use the old-leaf/new-leaf/root pattern to test alternatives before students sequence <strong>6 · Model the mechanism</strong> and write <strong>7 · Claim-Evidence-Reasoning</strong>.</p></div>''',
                    "html.parser",
                ).div
                p.insert_before(block)
                changed += 1

    # Remove production/release gate text while preserving classroom fallback/filter evidence.
    for page in role_pages(soup, "teacher"):
        for heading in list(page.find_all(["h2", "h3"])):
            txt = heading.get_text(" ", strip=True).lower()
            if txt in {"figure rights", "data rights and precision", "browser physical-print gate"}:
                nxt = heading.find_next_sibling()
                heading.decompose()
                if isinstance(nxt, Tag) and nxt.name == "p":
                    nxt.decompose()
                changed += 1
        h2 = page.find(["h2", "h3"], string=re.compile(r"Technical fallback and rights record", re.I))
        if h2:
            h2.string = "Technical fallback and filter record"
            changed += 1

    if not soup.select_one('[data-final-c1c3-task4-key="v1.0"]'):
        for page in role_pages(soup, "answer"):
            h = find_task_heading(page, 4)
            if h:
                existing = h.find_next_sibling()
                table = BeautifulSoup(
                    '''<table class="data-table" data-final-c1c3-task4-key="v1.0"><caption>Completed Task 4 symptom-pattern fields</caption><thead><tr><th>Evidence</th><th>Completed interpretation</th></tr></thead><tbody><tr><td>Older lower leaves retain green</td><td>They already contain chlorophyll made before the current failure became limiting.</td></tr><tr><td>New leaves are pale yellow to white</td><td>New tissue is failing during new chlorophyll formation.</td></tr><tr><td>Roots healthy; iron and nitrogen did not help</td><td>Root damage and a simple nutrient shortage fit poorly.</td></tr></tbody></table><div class="answer-block"><strong>Best overall pattern conclusion:</strong> adequate total photon quantity is reaching the habitat, but the wavelength distribution is selectively depleted where the case mechanism needs it for healthy new chlorophyll formation.</div>''',
                    "html.parser",
                )
                anchor = existing or h
                for node in list(table.contents):
                    anchor.insert_after(node)
                    anchor = node
                changed += 1
                break
    # Add concise acceptable rejections/exit wording.
    answer_text = text_of_role(soup, "answer")
    if "CO₂ or photoperiod" not in answer_text:
        for page in role_pages(soup, "answer"):
            h = find_task_heading(page, 5)
            if h:
                block = BeautifulSoup(
                    '<div class="answer-block" data-final-c1c3-alternatives="v1.0"><strong>Acceptable alternative rejections:</strong> students may reject perchlorates, CO₂, or photoperiod when they cite a specific contradictory case record. The key need not require the same distractor from every student.</div>',
                    "html.parser",
                ).div
                existing = h.find_next_sibling()
                (existing or h).insert_after(block)
                changed += 1
                break
    return changed


def fix_c1c7_exact(soup: BeautifulSoup, case_id: str) -> int:
    if case_id != "SSS-C1-CASE07":
        return 0
    changed = 0
    # Normalize pacing text so diagnosis -> CER -> intervention.
    for page in role_pages(soup, "teacher"):
        for node in list(page.find_all(string=True)):
            text = str(node)
            if "compare diagnoses and interventions" in text.lower():
                node.replace_with(re.sub(r"compare diagnoses and interventions", "compare diagnoses", text, flags=re.I))
                changed += 1
            if re.search(r"complete dedicated CER", text, re.I) and "intervention" not in text.lower():
                node.replace_with(text + " Then complete the intervention comparison in Task 7 before the final synthesis/exit work.")
                changed += 1

    if not soup.select_one('[data-final-c1c7-task4-key="v1.0"]'):
        for page in role_pages(soup, "answer"):
            h = find_task_heading(page, 4)
            if h:
                block = BeautifulSoup(
                    '''<div class="answer-block" data-final-c1c7-task4-key="v1.0"><strong>Unavailable-stage status — completed exemplar:</strong><ul><li><strong>X — mature source:</strong> the isolated lab does not currently supply the mature source organism.</li><li><strong>X — available path:</strong> the isolated lab does not currently provide the supported natural-range path needed to deliver the cue.</li><li><strong>Available/represented:</strong> downstream receptor, commitment, and young-symbiosis stages are biologically represented but cannot proceed when the first required source/path link is missing.</li></ul><p>The first missing stage interrupts the chain before a supported cue can reach the downstream response system.</p></div>''',
                    "html.parser",
                ).div
                existing = h.find_next_sibling()
                (existing or h).insert_after(block)
                changed += 1
                break
    return changed


def ensure_task_traceability(soup: BeautifulSoup, case_id: str, registry: dict) -> int:
    """Add a compact task-order strip where audit found missing or absent Teacher procedure coverage."""
    target_cases = {"SSS-C1-CASE05", "SSS-C2-CASE06"}
    if case_id not in target_cases or soup.select_one('[data-final-task-route="v1.0"]'):
        return 0
    pages = role_pages(soup, "teacher")
    if not pages:
        return 0
    target = pages[2] if len(pages) >= 3 else pages[0]
    tasks = registry.get("tasks", [])
    items = "".join(
        f'<li><strong>Task {t.get("number")} · {t.get("title", "")}</strong> — {t.get("description", "")}</li>' for t in tasks
    )
    if case_id == "SSS-C2-CASE06":
        intro = "<strong>Two-period class flow:</strong> Period 1 completes Tasks 1–3; Period 2 completes Tasks 4–7. Preserve the registry order and the full graded scope."
    else:
        intro = "<strong>Complete instructional route:</strong> use the registry order below. Detailed case notes elsewhere in the guide supplement this route; they do not replace tasks that are not individually expanded."
    html = f'''<h2 class="support-heading" data-final-task-route="v1.0">Complete teaching procedure / task route</h2><p>{intro}</p><ol class="procedure final-task-route">{items}</ol>'''
    insert_before_footer(target, html)
    return 1


def add_accessible_support_notes(soup: BeautifulSoup, case_id: str) -> int:
    changed = 0
    # C1 Case 01: make status support explicit while preserving evidence reasoning.
    if case_id == "SSS-C1-CASE01":
        for pid, prefix in {
            "a-cause-nutrient": "WEAKENED — ",
            "a-cause-light": "WEAKENED — ",
            "a-cause-seed": "WEAKENED — ",
            "a-cause-micro": "SUPPORTED — ",
        }.items():
            node = soup.find(attrs={"data-persist-id": pid})
            if isinstance(node, Tag) and not node.get("data-prefilled"):
                node["data-prefilled"] = "final-audit-v1.0"
                node.clear(); node.append(prefix)
                changed += 1
    return changed


def fix_metadata(case_id: str, package: dict, soup: BeautifulSoup) -> int:
    changed = 0
    if case_id == "SSS-C1-CASE03":
        desired_subtitle = "Campaign 1 · Case 03 · Arcadia Planitia, Mars"
        if package.get("subtitle") != desired_subtitle:
            package["subtitle"] = desired_subtitle; changed += 1
        if package.get("location") != "Arcadia Planitia, Mars":
            package["location"] = "Arcadia Planitia, Mars"; changed += 1
    if case_id == "SSS-C1-CASE05":
        desired = "Campaign 1 · Case 05 · Europa, Sub-Surface Bunker"
        if package.get("subtitle") != desired:
            package["subtitle"] = desired; changed += 1
        if package.get("location") != "Europa, Sub-Surface Bunker":
            package["location"] = "Europa, Sub-Surface Bunker"; changed += 1
        for node in list(soup.find_all(string=True)):
            text = str(node)
            if "Europa, orbiting Jupiter" in text:
                node.replace_with(text.replace("Europa, orbiting Jupiter", "Europa, Sub-Surface Bunker"))
                changed += 1
    return changed


def update_source_hashes(package: dict, case_dir: Path) -> None:
    hashes = package.setdefault("sourceHashes", {})
    source_root = case_dir / "source"
    mapping = {
        "content": source_root / "content.html",
        "presentation": source_root / "presentation.css",
        "taskRegistry": source_root / "task-registry.js",
        "layoutOverrides": source_root / "layout-overrides.json",
        "icons": source_root / "icons.svg",
    }
    for key, path in mapping.items():
        if key in hashes and path.exists():
            hashes[key] = sha256(path)


def remediate_case(case_id: str, case_dir: Path, apply: bool) -> tuple[int, list[str]]:
    source_dir = case_dir / "source"
    package_path = source_dir / "case-package.json"
    content_path = source_dir / "content.html"
    task_path = source_dir / "task-registry.js"
    if not package_path.exists() or not content_path.exists() or not task_path.exists():
        return 0, [f"SKIP {case_id}: canonical source files not found"]

    package = json.loads(package_path.read_text(encoding="utf-8"))
    registry = parse_json_object_from_js(task_path)
    original = content_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(original, "html.parser")
    operations: list[str] = []

    count = persist_print_marks(soup, case_id)
    if count: operations.append(f"persisted {count} print mark(s)")

    for pid, value in PREFILLS.get(case_id, {}).items():
        if set_prefill(soup, pid, value):
            operations.append(f"prefilled {pid}")

    count = add_accessible_support_notes(soup, case_id)
    if count: operations.append(f"added {count} Accessible status scaffold(s)")

    count = prefill_alternating_source_contributions(soup, case_id)
    if count: operations.append(f"prefilled {count} repeated Accessible source contribution(s)")

    count = remove_runtime_identifiers(soup, registry)
    if count: operations.append(f"cleaned {count} Teacher implementation-identifier text node(s)")

    count = ensure_common_rubric(soup, case_id)
    if count: operations.append("normalized Teacher quick + analytic rubric")

    count = ensure_controlled_references(soup, case_id)
    if count: operations.append("added controlled authoritative Teacher reference list")

    count = explicit_two_period_pacing(soup, case_id)
    if count: operations.append("declared full Teacher route as two-period implementation")

    count = fix_heavy_hands_fallback(soup, case_id)
    if count: operations.append("preserved five-source Heavy Hands graded fallback scope")

    count = fix_c2c2_status_code(soup, case_id)
    if count: operations.append("reframed Missing Dance status code as diagnostic priority")

    count = fix_c2c4_answer_space(soup, case_id)
    if count: operations.append("aligned Silent Grove Accessible 6-hour answer space")

    count = fix_c1c1_exact(soup, case_id)
    if count: operations.append("completed Case 01 Task 5 Teacher route and O/I key")

    count = fix_c1c3_exact(soup, case_id)
    if count: operations.append("applied Mars Habitat exact audit corrections")

    count = fix_c1c7_exact(soup, case_id)
    if count: operations.append("applied The Gift exact audit corrections")

    count = ensure_task_traceability(soup, case_id, registry)
    if count: operations.append("added complete Teacher task route")

    meta_changes = fix_metadata(case_id, package, soup)
    if meta_changes: operations.append(f"synchronized {meta_changes} controlled identity metadata/text item(s)")

    new_content = soup.decode(formatter="minimal")
    content_changed = new_content != original
    if content_changed and apply:
        content_path.write_text(new_content, encoding="utf-8")

    if apply:
        update_source_hashes(package, case_dir)
        package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return int(content_changed or meta_changes), operations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write remediated sources. Without this flag, report planned changes only.")
    parser.add_argument("--case", action="append", dest="cases", help="Restrict to a case id; may be repeated.")
    args = parser.parse_args()

    selected = args.cases or list(CASE_DIRS)
    changed_cases = 0
    for case_id in selected:
        case_dir = CASE_DIRS.get(case_id)
        if case_dir is None:
            print(f"ERROR unknown case id: {case_id}")
            return 2
        changed, operations = remediate_case(case_id, case_dir, args.apply)
        changed_cases += changed
        print(f"{case_id}: {'CHANGE' if changed else 'NO CHANGE'}")
        for op in operations:
            print(f"  - {op}")

    mode = "applied" if args.apply else "planned"
    print(f"SSS final remediation: {mode}; {changed_cases} case package(s) changed/planned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
