#!/usr/bin/env python3
"""Portable Case 01 v1.0 release-candidate validation and PDF build."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
CASE_DIR = HERE.parent
REPO_ROOT = CASE_DIR.parents[2]
MASTER = CASE_DIR / "master/SSS_C1_CASE01_EDITABLE_MASTER_v1.0.html"
PUBLISHED = CASE_DIR / "published"
RESULTS = HERE / "CASE01_RC_VALIDATION_RESULTS.json"
DOWNLOAD_TEST = HERE / "downloaded-html-portability-test.html"

EXPECTED_COUNTS = {"student": 3, "teacher": 7, "answer": 3, "accessible": 6, "all": 19}
TASKS = [
    (1, "Vocabulary", False),
    (2, "Initial thinking", False),
    (3, "Investigate four evidence sources", True),
    (4, "Test the competing explanations", True),
    (5, "Build the mechanism", True),
    (6, "Diagnose and reject an alternative", True),
    (7, "Claim-Evidence-Reasoning", True),
    (8, "Supply a consistent orientation cue", True),
    (9, "Exit ticket", True),
]
TASK_LABELS = [f"{i} · {title}" for i, title, _ in TASKS]
ANSWER_LABELS = [f"{i} · {title}" for i, title, keyable in TASKS if keyable]
PDFS = {
    "student": PUBLISHED / "SSS_C1_CASE01_STUDENT_MISSION_v1.0_RC.pdf",
    "teacher": PUBLISHED / "SSS_C1_CASE01_TEACHER_PACKET_v1.0_RC.pdf",
    "answer": PUBLISHED / "SSS_C1_CASE01_ANSWER_KEY_v1.0_RC.pdf",
    "accessible": PUBLISHED / "SSS_C1_CASE01_ACCESSIBLE_MISSION_v1.0_RC.pdf",
    "grayscale_review": PUBLISHED / "SSS_C1_CASE01_GRAYSCALE_REVIEW_v1.0_RC.pdf",
}


def rel(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def result(ok: bool, details: Any = None) -> dict[str, Any]:
    return {"ok": bool(ok), "details": details}


def static_checks(html: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")
    checks: dict[str, Any] = {}

    pages = soup.select("section.page")
    counts = {
        "student": len(soup.select("section.page.role-student")),
        "teacher": len(soup.select("section.page.role-teacher")),
        "answer": len(soup.select("section.page.role-answer")),
        "accessible": len(soup.select("section.page.role-accessible")),
        "all": len(pages),
    }
    checks["role_page_counts"] = result(counts == EXPECTED_COUNTS, {"expected": EXPECTED_COUNTS, "actual": counts})

    ids = [node.get("id") for node in soup.select("[id]")]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    checks["unique_dom_ids"] = result(not duplicates, {"duplicates": duplicates})

    response_errors = []
    fields = []
    for node in soup.select("[data-response]"):
        field = node.get("data-field")
        label = node.get("aria-label")
        if not field or not label:
            response_errors.append({"tag": node.name, "data-field": field, "aria-label": label})
        if field:
            fields.append(field)
    duplicate_fields = sorted({item for item in fields if fields.count(item) > 1})
    checks["response_field_accessible_names"] = result(not response_errors and not duplicate_fields, {"missing": response_errors, "duplicate_fields": duplicate_fields})

    student_ids = soup.select("section.role-student .student-id")
    accessible_ids = soup.select("section.role-accessible .student-id")
    first_student = soup.select_one('section[data-page-id="student-1"] .student-id') is not None
    first_accessible = soup.select_one('section[data-page-id="accessible-1"] .student-id') is not None
    continuation_ids = soup.select('section.role-student:not([data-page-id="student-1"]) .student-id, section.role-accessible:not([data-page-id="accessible-1"]) .student-id')
    teacher_answer_ids = soup.select("section.role-teacher .student-id, section.role-answer .student-id")
    checks["student_identification_placement"] = result(
        len(student_ids) == 1 and len(accessible_ids) == 1 and first_student and first_accessible and not continuation_ids and not teacher_answer_ids,
        {"student_rows": len(student_ids), "accessible_rows": len(accessible_ids), "continuation_rows": len(continuation_ids), "teacher_answer_rows": len(teacher_answer_ids)},
    )

    def section_titles(css: str) -> list[str]:
        return [n.get_text(" ", strip=True) for n in soup.select(css)]

    student_titles = section_titles("section.role-student .section-title")
    accessible_titles = section_titles("section.role-accessible .section-title")
    answer_titles = section_titles("section.role-answer .section-title")
    checks["student_task_heading_parity"] = result(all(label in student_titles for label in TASK_LABELS), {"required": TASK_LABELS, "actual": student_titles})
    checks["accessible_task_heading_parity"] = result(all(label in accessible_titles for label in TASK_LABELS), {"required": TASK_LABELS, "actual": accessible_titles})
    checks["answer_key_task_heading_parity"] = result(all(label in answer_titles for label in ANSWER_LABELS), {"required": ANSWER_LABELS, "actual": answer_titles})

    malformed_patterns = {
        "duplicated_teacher_phrase": r"Students complete\s+Students complete",
        "dangling_and_reasoning": r"\.\s+and reasoning\b",
        "dangling_sources_and_reasoning": r"sources\.\s+and reasoning",
    }
    malformed_hits = {name: bool(re.search(pattern, html, re.I)) for name, pattern in malformed_patterns.items()}
    checks["known_malformed_text_absent"] = result(not any(malformed_hits.values()), malformed_hits)

    teacher_text = " ".join(n.get_text(" ", strip=True) for n in soup.select("section.role-teacher"))
    prohibited = [term for term in ["COMPATIBILITY Source baseline", "Curriculum source master v0.3", "Migration history", "Build provenance"] if term.lower() in teacher_text.lower()]
    checks["teacher_metadata_body_absent"] = result(not prohibited, {"prohibited_visible_terms": prohibited})

    word_banks = [n.get_text(" ", strip=True).replace("WORD BANK ", "", 1) for n in soup.select(".word-bank")]
    expected_bank = "curve or grow without consistent orientation · downward · settle · settle in one direction"
    checks["exact_match_word_bank"] = result(len(word_banks) == 2 and all(bank == expected_bank for bank in word_banks), {"expected": expected_bank, "actual": word_banks})

    task_refs = [n.get_text(" ", strip=True) for n in soup.select("section.role-teacher strong.task-reference")]
    invalid_refs = [ref for ref in task_refs if ref not in TASK_LABELS]
    required_teacher_refs = [TASK_LABELS[i - 1] for i in [2, 3, 4, 6, 7, 8, 9]]
    checks["teacher_task_reference_emphasis"] = result(not invalid_refs and all(ref in task_refs for ref in required_teacher_refs), {"required": required_teacher_refs, "actual": task_refs, "invalid": invalid_refs})

    answer_text = " ".join(n.get_text(" ", strip=True) for n in soup.select("section.role-answer"))
    exemplar_markers = [
        "Roots grow in many directions",
        "Microgravity · supported",
        "settle in one direction",
        "Microgravity disrupted normal gravitropic orientation",
        "The crop problem was caused by disrupted gravitropism in microgravity",
        "Directional root channels inside the plant pillow",
        "Tangled roots should improve first",
    ]
    missing_markers = [marker for marker in exemplar_markers if marker not in answer_text]
    checks["completed_answer_key_exemplars"] = result(not missing_markers, {"required_markers": exemplar_markers, "missing": missing_markers})

    controls = {
        "clear_student": soup.select_one("#clearBtn") is not None and soup.select_one("#clearBtn").get_text(strip=True) == "Clear Student Responses",
        "clear_teacher": soup.select_one("#clearTeacherBtn") is not None and soup.select_one("#clearTeacherBtn").get_text(strip=True) == "Clear Teacher Notes",
        "reset": soup.select_one("#resetBtn") is not None and soup.select_one("#resetBtn").get_text(strip=True) == "Reset This File",
    }
    checks["control_labels"] = result(all(controls.values()), controls)

    institution = {
        "solar_agricultural_agency_count": html.count("SOLAR AGRICULTURAL AGENCY"),
        "prohibited_space_agricultural_authority_count": html.count("SPACE AGRICULTURAL AUTHORITY"),
        "prohibited_solar_agricultural_authority_count": html.count("SOLAR AGRICULTURAL AUTHORITY"),
    }
    checks["institution_name"] = result(
        institution["solar_agricultural_agency_count"] == 19
        and institution["prohibited_space_agricultural_authority_count"] == 0
        and institution["prohibited_solar_agricultural_authority_count"] == 0,
        institution,
    )

    source_requirements = {
        "source/student-mission-sheet.md": TASK_LABELS,
        "source/lesson-plan.md": [TASK_LABELS[i - 1] for i in [2, 3, 4, 6, 7, 8, 9]],
        "source/quick-start.md": [TASK_LABELS[i - 1] for i in [2, 3, 4, 6, 7, 8, 9]],
        "source/answer-key.md": ANSWER_LABELS,
    }
    source_sync = {"files": {}, "malformed": [], "missing_files": []}
    for relative, labels in source_requirements.items():
        path = CASE_DIR / relative
        if not path.exists():
            source_sync["missing_files"].append(relative)
            continue
        text = path.read_text(encoding="utf-8")
        missing = [label for label in labels if label not in text]
        source_sync["files"][relative] = {"required": labels, "missing": missing}
        if re.search(r"Students complete\s+Students complete|\.\s+and reasoning\b", text, re.I):
            source_sync["malformed"].append(relative)
    required_controlled = [
        "source/student-mission-sheet.md", "source/lesson-plan.md", "source/quick-start.md", "source/teacher-case-analysis.md",
        "source/answer-key.md", "source/quick-rubric.md", "source/formal-rubric.md", "source/references.md", "source/technical-notes.md", "source/task-registry.js"
    ]
    source_sync["missing_controlled"] = [relative for relative in required_controlled if not (CASE_DIR / relative).exists()]
    source_sync["answer_key_exemplar_rule"] = "completed exemplar" in (CASE_DIR / "source/answer-key.md").read_text(encoding="utf-8").lower()
    source_sync["technical_controls"] = all(term in (CASE_DIR / "source/technical-notes.md").read_text(encoding="utf-8") for term in ["Clear Student Responses", "Clear Teacher Notes", "Reset This File", "embeds the SAA insignia"])
    source_sync_ok = not source_sync["missing_files"] and not source_sync["missing_controlled"] and not source_sync["malformed"] and all(not item["missing"] for item in source_sync["files"].values()) and source_sync["answer_key_exemplar_rule"] and source_sync["technical_controls"]
    checks["controlled_source_synchronization"] = result(source_sync_ok, source_sync)

    checks["validation_status_retained"] = result(
        html.count("VALIDATION BUILD") >= 20 and 'name="sss-status"' in html and 'content="validation-build"' in html,
        {"visible_count": html.count("VALIDATION BUILD")},
    )

    return checks


def all_ok(group: dict[str, Any]) -> bool:
    return all(item.get("ok", False) for item in group.values())


def browser_checks() -> tuple[dict[str, Any], str]:
    checks: dict[str, Any] = {}
    PUBLISHED.mkdir(parents=True, exist_ok=True)
    if DOWNLOAD_TEST.exists():
        DOWNLOAD_TEST.unlink()

    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, format: str, *args: Any) -> None:
            return
        def copyfile(self, source: Any, outputfile: Any) -> None:
            try:
                super().copyfile(source, outputfile)
            except (BrokenPipeError, ConnectionResetError):
                return

    handler = partial(QuietHandler, directory=str(REPO_ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}"
    master_url = f"{base_url}/{rel(MASTER)}"

    with sync_playwright() as pw:
        browser_path = os.environ.get("CHROMIUM_PATH") or shutil.which("chromium") or shutil.which("chromium-browser")
        launch_kwargs = {"headless": True, "args": ["--no-sandbox", "--disable-dev-shm-usage"]}
        if browser_path:
            launch_kwargs["executable_path"] = browser_path
        browser = pw.chromium.launch(**launch_kwargs)
        chromium_version = browser.version
        context = browser.new_context(viewport={"width": 1400, "height": 1200}, accept_downloads=True)
        context.route("https://fonts.googleapis.com/**", lambda route: route.fulfill(status=200, content_type="text/css", body=""))
        context.route("https://fonts.gstatic.com/**", lambda route: route.abort())
        page = context.new_page()
        page.set_default_timeout(10000)
        page.set_default_navigation_timeout(15000)
        js_errors: list[str] = []
        page.on("pageerror", lambda error: js_errors.append(f"pageerror: {error}"))
        page.on("console", lambda msg: js_errors.append(f"console:{msg.type}: {msg.text}") if msg.type == "error" else None)
        page.goto(master_url, wait_until="domcontentloaded", timeout=15000)
        page.wait_for_timeout(300)
        page.evaluate("localStorage.clear()")
        page.reload(wait_until="domcontentloaded", timeout=15000)
        page.wait_for_timeout(500)

        role_results = {}
        for role, expected in EXPECTED_COUNTS.items():
            page.select_option("#roleSelect", role)
            page.wait_for_timeout(100)
            measured = page.evaluate("""
                () => {
                  const visible = [...document.querySelectorAll('.page')].filter(p => getComputedStyle(p).display !== 'none');
                  const rows = visible.map(p => {
                    const frame = p.querySelector('.page-frame');
                    const content = p.querySelector('.content-area');
                    const overflow = frame.scrollHeight > frame.clientHeight + 2 || frame.scrollWidth > frame.clientWidth + 2 || content.scrollHeight > content.clientHeight + 2 || content.scrollWidth > content.clientWidth + 2 || p.classList.contains('overflowing');
                    return {pageId:p.dataset.pageId, overflow, contentOverBy:Math.max(0, content.scrollHeight-content.clientHeight), frameOverBy:Math.max(0, frame.scrollHeight-frame.clientHeight)};
                  });
                  return {visible:visible.length, rows, status:document.querySelector('#toolbarStatus')?.textContent || ''};
                }
            """)
            over = [row for row in measured["rows"] if row["overflow"]]
            role_results[role] = {"expected": expected, "actual": measured["visible"], "overflow": over, "status": measured["status"], "ok": measured["visible"] == expected and not over}
        checks["roles_and_overflow"] = result(all(item["ok"] for item in role_results.values()), role_results)

        page.select_option("#roleSelect", "all")
        page.click("#grayToggle")
        page.wait_for_timeout(100)
        gray = page.evaluate("""
          () => ({
            active: document.body.classList.contains('grayscale'),
            visible: [...document.querySelectorAll('.page')].filter(p => getComputedStyle(p).display !== 'none').length,
            overflowing: [...document.querySelectorAll('.page.overflowing')].filter(p => getComputedStyle(p).display !== 'none').map(p=>p.dataset.pageId)
          })
        """)
        checks["grayscale_all_pages"] = result(gray["active"] and gray["visible"] == 19 and not gray["overflowing"], gray)
        page.click("#grayToggle")
        page.select_option("#roleSelect", "teacher")
        page.click("#previewToggle")
        preview = page.evaluate("() => ({active:document.body.classList.contains('print-preview'), overflow:[...document.querySelectorAll('.page.overflowing')].filter(p=>getComputedStyle(p).display!=='none').map(p=>p.dataset.pageId)})")
        checks["print_preview"] = result(preview["active"] and not preview["overflow"], preview)
        page.click("#previewToggle")

        page.select_option("#roleSelect", "student")
        page.click("#fillToggle")
        fill_access = page.evaluate("""
          () => {
            const visible = [...document.querySelectorAll('.role-student [data-response]')];
            return {count:visible.length, inactive:visible.filter(n=>n.contentEditable!=='true'||n.tabIndex!==0).map(n=>n.dataset.field)};
          }
        """)
        checks["fillable_keyboard_access"] = result(fill_access["count"] > 0 and not fill_access["inactive"], fill_access)
        page.click("#fillToggle")
        page.click("#editToggle")
        edit_access = page.evaluate("""
          () => {
            const nodes=[...document.querySelectorAll('.role-student [data-editable]')];
            return {count:nodes.length, inactive:nodes.filter(n=>n.contentEditable!=='true'||n.tabIndex!==0).length};
          }
        """)
        checks["edit_keyboard_access"] = result(edit_access["count"] > 0 and edit_access["inactive"] == 0, edit_access)
        page.click("#editToggle")

        page.select_option("#roleSelect", "student")
        page.click("#fillToggle")
        page.evaluate("""
          () => {
            const n=document.querySelector('.role-student [data-response]');
            n.innerHTML='PERSIST_STUDENT_TOKEN'; n.dispatchEvent(new Event('input',{bubbles:true}));
            const t=document.querySelector('.role-teacher [data-response]');
            t.innerHTML='PERSIST_TEACHER_TOKEN'; t.dispatchEvent(new Event('input',{bubbles:true}));
          }
        """)
        page.wait_for_timeout(150)
        page.reload(wait_until="domcontentloaded", timeout=15000)
        page.wait_for_timeout(300)
        persisted = page.evaluate("""
          () => ({
            student:[...document.querySelectorAll('.role-student [data-response]')].some(n=>n.innerHTML.includes('PERSIST_STUDENT_TOKEN')),
            teacher:[...document.querySelectorAll('.role-teacher [data-response]')].some(n=>n.innerHTML.includes('PERSIST_TEACHER_TOKEN'))
          })
        """)
        checks["persistence_reload"] = result(persisted["student"] and persisted["teacher"], persisted)

        page.on("dialog", lambda dialog: dialog.accept())
        page.evaluate("""
          () => {
            const roles=['student','accessible','teacher','answer'];
            for (const role of roles) {
              const n=document.querySelector(`.role-${role} [data-response]`);
              n.innerHTML=`CLEAR_${role.toUpperCase()}_TOKEN`; n.dispatchEvent(new Event('input',{bubbles:true}));
            }
          }
        """)
        page.click("#clearBtn")
        page.wait_for_timeout(100)
        clear_student = page.evaluate("""
          () => ({
            student:[...document.querySelectorAll('.role-student [data-response]')].some(n=>n.innerHTML.includes('CLEAR_STUDENT_TOKEN')),
            accessible:[...document.querySelectorAll('.role-accessible [data-response]')].some(n=>n.innerHTML.includes('CLEAR_ACCESSIBLE_TOKEN')),
            teacher:[...document.querySelectorAll('.role-teacher [data-response]')].some(n=>n.innerHTML.includes('CLEAR_TEACHER_TOKEN')),
            answer:[...document.querySelectorAll('.role-answer [data-response]')].some(n=>n.innerHTML.includes('CLEAR_ANSWER_TOKEN'))
          })
        """)
        checks["clear_student_scope"] = result(not clear_student["student"] and not clear_student["accessible"] and clear_student["teacher"] and clear_student["answer"], clear_student)
        page.click("#clearTeacherBtn")
        page.wait_for_timeout(100)
        clear_teacher = page.evaluate("""
          () => ({
            teacher:[...document.querySelectorAll('.role-teacher [data-response]')].some(n=>n.innerHTML.includes('CLEAR_TEACHER_TOKEN')),
            answer:[...document.querySelectorAll('.role-answer [data-response]')].some(n=>n.innerHTML.includes('CLEAR_ANSWER_TOKEN'))
          })
        """)
        checks["clear_teacher_scope"] = result(not clear_teacher["teacher"] and not clear_teacher["answer"], clear_teacher)

        original_editable = page.locator('.role-student [data-editable]').first.inner_html()
        page.evaluate("""
          () => {
            const e=document.querySelector('.role-student [data-editable]'); e.innerHTML='RESET_TEMP_EDIT'; e.dispatchEvent(new Event('input',{bubbles:true}));
            const r=document.querySelector('.role-student [data-response]'); r.innerHTML='RESET_TEMP_RESPONSE'; r.dispatchEvent(new Event('input',{bubbles:true}));
          }
        """)
        page.click("#resetBtn")
        page.wait_for_timeout(150)
        reset_state = page.evaluate("""
          () => ({
            editable:document.querySelector('.role-student [data-editable]').innerHTML,
            response:document.querySelector('.role-student [data-response]').innerHTML,
            role:document.body.dataset.role,
            margin:document.querySelector('#marginSelect').value,
            density:document.querySelector('#densitySelect').value
          })
        """)
        checks["reset_open_file_source"] = result(reset_state["editable"] == original_editable and reset_state["response"] == "" and reset_state["role"] == "student" and reset_state["margin"] == ".50" and reset_state["density"] == "balanced", {"expected_editable": original_editable, **reset_state})

        page.click("#editToggle")
        page.evaluate("""
          () => {
            const e=document.querySelector('.role-student [data-editable]'); e.innerHTML='DOWNLOAD_SOURCE_MARKER'; e.dispatchEvent(new Event('input',{bubbles:true}));
            const r=document.querySelector('.role-student [data-response]'); r.innerHTML='DOWNLOAD_RESPONSE_MARKER'; r.dispatchEvent(new Event('input',{bubbles:true}));
          }
        """)
        with page.expect_download() as download_info:
            page.click("#downloadBtn")
        download = download_info.value
        download.save_as(str(DOWNLOAD_TEST))
        downloaded_html = DOWNLOAD_TEST.read_text(encoding="utf-8")
        serialization = {
            "doctype": downloaded_html.startswith("<!DOCTYPE html>"),
            "portable_insignia": "data:image/svg+xml;base64," in downloaded_html and '../../../../shared/assets/insignia/saa.svg' not in downloaded_html,
            "marker": "DOWNLOAD_SOURCE_MARKER" in downloaded_html and "DOWNLOAD_RESPONSE_MARKER" in downloaded_html,
            "overflow_class_absent": not re.search(r'class="[^"]*\boverflowing\b', downloaded_html),
            "malformed_absent": "Students complete Students complete" not in downloaded_html and not re.search(r"\.\s+and reasoning\b", downloaded_html),
        }
        checks["downloaded_html_serialization"] = result(all(serialization.values()), serialization)

        dl_page = context.new_page()
        dl_errors: list[str] = []
        dl_page.on("pageerror", lambda error: dl_errors.append(str(error)))
        dl_page.goto(f"{base_url}/{rel(DOWNLOAD_TEST)}", wait_until="domcontentloaded", timeout=15000)
        dl_page.wait_for_timeout(300)
        dl_page.on("dialog", lambda dialog: dialog.accept())
        dl_page.evaluate("""
          () => {
            const e=document.querySelector('.role-student [data-editable]'); e.innerHTML='DOWNLOAD_TEMP_AFTER_OPEN'; e.dispatchEvent(new Event('input',{bubbles:true}));
            const r=document.querySelector('.role-student [data-response]'); r.innerHTML='DOWNLOAD_TEMP_RESPONSE'; r.dispatchEvent(new Event('input',{bubbles:true}));
          }
        """)
        dl_page.click("#resetBtn")
        dl_page.wait_for_timeout(100)
        downloaded_reset = dl_page.evaluate("""
          () => ({
            editable:document.querySelector('.role-student [data-editable]').innerHTML,
            response:document.querySelector('.role-student [data-response]').innerHTML,
            insigniaSources:[...document.querySelectorAll('img.saa-insignia,.continuation-header img')].map(i=>i.getAttribute('src'))
          })
        """)
        checks["downloaded_html_reset_semantics"] = result(downloaded_reset["editable"] == "DOWNLOAD_SOURCE_MARKER" and downloaded_reset["response"] == "DOWNLOAD_RESPONSE_MARKER" and all(src.startswith("data:image/svg+xml;base64,") for src in downloaded_reset["insigniaSources"]) and not dl_errors, {**downloaded_reset, "errors": dl_errors})
        dl_page.close()

        # Return original page to repository source before PDF generation.
        page.click("#resetBtn")
        page.wait_for_timeout(150)

        pdf_results: dict[str, Any] = {}
        pdf_specs = [
            ("student", "student", False, 3),
            ("teacher", "teacher", False, 7),
            ("answer", "answer", False, 3),
            ("accessible", "accessible", False, 6),
            ("grayscale_review", "all", True, 19),
        ]
        for name, role, gray_mode, expected_pages in pdf_specs:
            page.select_option("#roleSelect", role)
            page.wait_for_timeout(100)
            gray_active = page.evaluate("document.body.classList.contains('grayscale')")
            if gray_active != gray_mode:
                page.click("#grayToggle")
                page.wait_for_timeout(100)
            target = PDFS[name]
            page.pdf(path=str(target), format="Letter", print_background=True, prefer_css_page_size=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
            actual_pages = len(PdfReader(str(target)).pages)
            pdf_results[name] = {"file": rel(target), "expected_pages": expected_pages, "actual_pages": actual_pages, "bytes": target.stat().st_size, "sha256": sha256(target), "ok": actual_pages == expected_pages and target.stat().st_size > 10000}
        checks["pdf_generation"] = result(all(item["ok"] for item in pdf_results.values()), pdf_results)

        checks["javascript_errors"] = result(not js_errors, {"errors": js_errors})
        context.close()
        browser.close()

    server.shutdown()
    server.server_close()
    return checks, chromium_version


def main() -> int:
    if not MASTER.exists():
        raise SystemExit(f"Master not found: {MASTER}")
    html = MASTER.read_text(encoding="utf-8")
    static = static_checks(html)
    browser, chromium_version = browser_checks()
    overall = all_ok(static) and all_ok(browser)

    payload = {
        "schema_version": "1.0",
        "case": "SSS-C1-CASE01",
        "build": "v1.0 RC",
        "status": "VALIDATION BUILD",
        "validation_date": "2026-07-24",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "master": rel(MASTER),
        "master_sha256": sha256(MASTER),
        "environment": {"python": sys.version.split()[0], "playwright": "python", "chromium": chromium_version, "platform": sys.platform},
        "static_checks": static,
        "browser_checks": browser,
        "overall_pass": overall,
        "release_approved": False,
        "remaining_release_gate": "Owner physical print testing at 100% scale",
    }
    RESULTS.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"overall_pass": overall, "results": rel(RESULTS), "master_sha256": payload["master_sha256"]}, indent=2))
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
