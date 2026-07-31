#!/usr/bin/env python3
"""Validate the HTML-only Case 03 release candidate."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
MASTER = ROOT / "master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html"
PUBLISHED = ROOT / "published"
VALIDATION = ROOT / "validation-artifacts"
MANIFEST = ROOT / "CASE03_V1_RELEASE_MANIFEST.json"
LEDGER = VALIDATION / "CASE03_V1_HTML_CHECKSUMS.sha256"
RESULTS = VALIDATION / "CASE03_V1_VALIDATION_RESULTS.json"
GAME = "c6c17be57880b365793fdf99ff4ad09b62ecacce"
REJECTED_SAA = [
    "Solar Agricultural Authority",
    "Space Agricultural Authority",
    "Space Agricultural Agency",
    "Solar Agriculture Agency",
    "Space Agriculture Authority",
]
ROLES = {
    "student": ("SSS_C1_CASE03_STUDENT_MISSION_v1.0.html", 4, "student"),
    "teacher": ("SSS_C1_CASE03_TEACHER_GUIDE_v1.0.html", 8, "teacher"),
    "answer": ("SSS_C1_CASE03_ANSWER_KEY_v1.0.html", 4, "answer"),
    "accessible": ("SSS_C1_CASE03_ACCESSIBLE_MISSION_v1.0.html", 6, "accessible"),
    "grayscale": ("SSS_C1_CASE03_GRAYSCALE_MISSION_v1.0.html", 4, "student"),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    checks: list[dict[str, object]] = []

    def check(group: str, name: str, condition: bool, detail: object = "") -> None:
        checks.append({"group": group, "name": name, "pass": bool(condition), "detail": str(detail)})

    master_text = MASTER.read_text(encoding="utf-8")
    master = BeautifulSoup(master_text, "html.parser")
    visible = " ".join(page.get_text(" ", strip=True) for page in master.select("section.page"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    # Static HTML and production-policy gate.
    check("static_html", "master exists", MASTER.is_file())
    check("static_html", "document language is English", master.html is not None and master.html.get("lang") == "en")
    check("static_html", "document title is present", bool(master.title and master.title.get_text(strip=True)))
    expected_meta = {
        "sss-case": "SSS-C1-CASE03",
        "sss-curriculum-version": "1.0",
        "sss-status": "validation-build",
        "sss-artifact-policy": "html-only",
        "sss-game-baseline": GAME,
        "sss-editor-shell": "1.0",
    }
    for name, expected in expected_meta.items():
        node = master.find("meta", attrs={"name": name})
        check("static_html", f"metadata {name}", node is not None and node.get("content") == expected)
    check("static_html", "canonical institution name present", "Solar Agricultural Agency" in visible)
    for index, rejected in enumerate(REJECTED_SAA, 1):
        check("static_html", f"rejected institution expansion {index} absent", rejected not in visible)
    check("static_html", "manifest status remains VALIDATION BUILD", manifest.get("status") == "VALIDATION BUILD")
    check("static_html", "manifest artifact policy is HTML_ONLY", manifest.get("artifact_policy") == "HTML_ONLY")
    check("static_html", "manifest contains no PDF output keys", '"pdf"' not in MANIFEST.read_text(encoding="utf-8").lower())
    case03_pdfs = sorted(path.name for path in ROOT.rglob("*.pdf"))
    check("static_html", "Case 03 stores no PDF files", not case03_pdfs, case03_pdfs)
    obsolete = [
        VALIDATION / "build_case03_pdfs.py",
        VALIDATION / "CASE03_V1_PDF_PREFLIGHT.json",
        VALIDATION / "CASE03_V1_RENDERER_PARITY.json",
    ]
    check("static_html", "Case 03 has no PDF production or preflight tooling", not any(path.exists() for path in obsolete))

    # Semantic accessibility gate.
    check("accessibility", "skip link targets workspace", master.select_one('a[href="#workspace"]') is not None)
    responses = master.select("[data-response]")
    check(
        "accessibility",
        "all response fields expose textbox semantics",
        bool(responses)
        and all(node.get("role") == "textbox" and node.get("aria-multiline") == "true" for node in responses),
    )
    check(
        "accessibility",
        "all response fields have programmatic labels",
        bool(responses) and all(node.get("aria-label") or node.get("aria-labelledby") for node in responses),
    )
    tables = master.select("table")
    check(
        "accessibility",
        "all tables have captions",
        bool(tables) and all(table.find("caption", recursive=False) is not None for table in tables),
    )
    check(
        "accessibility",
        "all table headers declare scope",
        all(node.get("scope") in {"col", "row", "colgroup", "rowgroup"} for node in master.select("th")),
    )
    graphics = master.select("figure svg")
    check(
        "accessibility",
        "all figure graphics have accessible names",
        bool(graphics)
        and all(node.get("aria-label") or node.get("aria-labelledby") or node.find("title") for node in graphics),
    )
    heading_skips: list[str] = []
    for page_node in master.select("section.page"):
        levels = [int(node.name[1]) for node in page_node.select("h1,h2,h3,h4,h5,h6")]
        if any(current > prior + 1 for prior, current in zip(levels, levels[1:])):
            heading_skips.append(page_node.get("data-page-id", "unknown"))
        check(
            "accessibility",
            f"{page_node.get('data-page-id')} has one page-title h1",
            len(page_node.select("h1")) == 1,
        )
    check("accessibility", "heading hierarchy has no skipped levels", not heading_skips, heading_skips)
    check(
        "accessibility",
        "meaning does not depend on color",
        all(token in master_text for token in ["url(#diag)", "url(#dots)", "url(#cross)", "url(#horiz)"])
        and all(f">{value}%<" in master_text for value in [92, 88, 31, 12]),
    )

    # Role isolation, portability, page-count, and HTML checksum gates.
    actual_counts: dict[str, int] = {}
    for role, (filename, expected_count, expected_data_role) in ROLES.items():
        path = PUBLISHED / filename
        check("role_isolation", f"{role} output exists", path.is_file())
        text = path.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        pages = soup.select("section.page[data-role]")
        actual_counts[role] = len(pages)
        check("role_isolation", f"{role} contains only its role", bool(pages) and all(page.get("data-role") == expected_data_role for page in pages))
        check("role_isolation", f"{role} HTML page count is {expected_count}", len(pages) == expected_count, len(pages))
        check("portability_serialization", f"{role} has no authoring toolbar", soup.select_one(".toolbar") is None)
        check("portability_serialization", f"{role} is self-contained", not soup.select("script[src],link[rel~='stylesheet']"))
        check(
            "portability_serialization",
            f"{role} has no external image dependency",
            not any((node.get("src") or "").startswith(("http:", "https:")) for node in soup.select("img[src]")),
        )
        check(
            "accessibility",
            f"{role} retains document language and title",
            soup.html is not None and soup.html.get("lang") == "en" and bool(soup.title and soup.title.get_text(strip=True)),
        )
    expected_counts = {role: data[1] for role, data in ROLES.items()}
    check("html_page_counts", "all HTML page counts match the release contract", actual_counts == expected_counts, actual_counts)

    ledger_entries: dict[str, str] = {}
    if LEDGER.is_file():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            checksum, relative = line.split("  ", 1)
            ledger_entries[relative] = checksum
    expected_ledger_paths = {
        "master/SSS_C1_CASE03_EDITABLE_MASTER_v1.0.html",
        *(f"published/{filename}" for filename, _, _ in ROLES.values()),
    }
    check("html_checksum", "HTML checksum ledger has exactly six canonical outputs", set(ledger_entries) == expected_ledger_paths, sorted(ledger_entries))
    for relative, expected in sorted(ledger_entries.items()):
        path = ROOT / relative
        check("html_checksum", f"checksum verifies {relative}", path.is_file() and digest(path) == expected)

    # Browser behavior, accessibility interaction, overflow, and print-preview gates.
    executable = next(
        (
            path
            for path in [
                os.environ.get("CHROMIUM_EXECUTABLE"),
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "/usr/bin/chromium",
            ]
            if path and Path(path).exists()
        ),
        None,
    )
    check("browser_behavior", "Chromium-family browser is available", executable is not None, executable)
    overflow_counts: dict[str, int] = {}
    print_overflow_counts: dict[str, int] = {}
    if executable:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True, executable_path=executable, args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 1440, "height": 1200})
            errors: list[str] = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(MASTER.resolve().as_uri(), wait_until="load")
            page.wait_for_timeout(300)
            check("browser_behavior", "master loads without JavaScript errors", not errors, errors)
            check("browser_behavior", "shared runtime identifies shell 1.0", page.evaluate("window.SSSEditorShell?.shellVersion") == "1.0")
            check("browser_behavior", "print action remains available", page.locator("#printBtn").is_visible())
            check(
                "accessibility",
                "print action warns about manual PDF accessibility",
                "accessibility is not guaranteed" in (page.locator("#printBtn").get_attribute("aria-label") or "").lower(),
            )
            page.locator("body").press("Tab")
            focused = page.evaluate("document.activeElement && document.activeElement.matches('a,button,select,input,[contenteditable=true]')")
            check("accessibility", "keyboard focus reaches an interactive control", bool(focused))
            for role in ["student", "teacher", "answer", "accessible"]:
                page.evaluate("(value) => window.SSSEditorShell.setRole(value)", role)
                page.wait_for_timeout(100)
                expected = ROLES[role][1]
                visible_pages = page.locator(f'section.page[data-role="{role}"]:visible').count()
                all_visible = page.locator("section.page:visible").count()
                check("role_isolation", f"{role} browser role isolation", visible_pages == expected and all_visible == expected, all_visible)
                overflow_counts[role] = page.evaluate("window.SSSEditorShell.checkOverflow()")
                check("overflow_print_preview", f"{role} screen has zero overflow", overflow_counts[role] == 0, overflow_counts[role])
            page.emulate_media(media="print")
            check("overflow_print_preview", "authoring toolbar is hidden in print media", page.locator(".toolbar").evaluate("node => getComputedStyle(node).display") == "none")
            for role in ["student", "teacher", "answer", "accessible"]:
                page.evaluate("(value) => window.SSSEditorShell.setRole(value)", role)
                page.wait_for_timeout(50)
                print_overflow_counts[role] = page.locator(f'section.page[data-role="{role}"].has-overflow').count()
                check("overflow_print_preview", f"{role} print preview has zero flagged overflow", print_overflow_counts[role] == 0, print_overflow_counts[role])
            browser.close()

    # Rendered-browser review is recorded as a separate human-inspected gate.
    review_results_path = VALIDATION / "CASE03_BROWSER_RENDERED_REVIEW_RESULTS.json"
    review = json.loads(review_results_path.read_text(encoding="utf-8")) if review_results_path.is_file() else {}
    check("rendered_browser_review", "browser rendering review passed", review.get("status") == "PASS")
    check("rendered_browser_review", "all 26 HTML pages were rendered", review.get("renderedPageCount") == 26, review.get("renderedPageCount"))
    check("owner_physical_print", "owner physical print gate remains OPEN", manifest.get("release_gate", {}).get("status") == "OPEN")

    status = all(item["pass"] for item in checks)
    groups: dict[str, dict[str, int]] = {}
    for item in checks:
        group = str(item["group"])
        groups.setdefault(group, {"pass": 0, "total": 0})
        groups[group]["total"] += 1
        groups[group]["pass"] += int(bool(item["pass"]))
    result = {
        "case": "SSS-C1-CASE03",
        "version": "1.0",
        "status": "PASS" if status else "FAIL",
        "buildStatus": "VALIDATION BUILD",
        "artifactPolicy": "HTML_ONLY",
        "activeReleaseGates": [
            "static HTML validation",
            "browser behavior validation",
            "role isolation",
            "portability and serialization",
            "accessibility",
            "overflow and print-preview checks",
            "HTML page counts",
            "HTML checksum verification",
            "rendered browser review",
            "owner physical print test (OPEN)",
        ],
        "pageCounts": actual_counts,
        "overflowCounts": overflow_counts,
        "printOverflowCounts": print_overflow_counts,
        "groups": groups,
        "total": {"pass": sum(int(bool(item["pass"])) for item in checks), "total": len(checks)},
        "failures": [item for item in checks if not item["pass"]],
        "checks": checks,
    }
    RESULTS.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "total": result["total"], "groups": groups, "failures": result["failures"]}, indent=2))
    return 0 if status else 1


if __name__ == "__main__":
    raise SystemExit(main())
