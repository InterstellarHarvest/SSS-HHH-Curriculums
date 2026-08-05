#!/usr/bin/env python3
"""Generate and inspect browser PDFs for every registered case and edition."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from bs4 import BeautifulSoup

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[1]
sys.path.insert(0, str(APP))
from serve import CurriculumEditorHandler  # noqa: E402

AUTHORING_SELECTOR = "[data-layout-resize-ui],[data-layout-resizable],[data-layout-validation],.layout-changes,.layout-apply-dialog,.curriculum-print-frame"
AUTHORING_TEXT = ("Pending Layout Changes", "Apply to Source", "layout-resize:v1")
CASE01_APPROVED = {
    "s1-reason-nutrient": 56,
    "s1-reason-light": 56,
    "s1-reason-seed": 56,
    "s1-reason-micro": 56,
    "s2-diagnosis": 64,
}


REGISTRY_PATH = ROOT / "shared/implementation/case-registry.v2.json"


def read_package(relative_path: str) -> dict:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def registered_case_editions(registry: dict, package_reader=read_package) -> list[dict[str, object]]:
    """Every case-edition print document the registry and package contracts require.

    The roster is derived, never hard-coded: a case counts only when it declares an
    editorPackage (the same editor-compatibility rule the library uses), and it
    contributes exactly the roles that package declares as supported. Adding a case, or
    changing a package's supported roles, changes this total automatically.
    """
    if registry.get("schemaVersion") != 2:
        raise RuntimeError(f"Unsupported registry schema: {registry.get('schemaVersion')}")
    editions: list[dict[str, object]] = []
    for curriculum in registry.get("curricula", []):
        for campaign in curriculum.get("campaigns", []):
            for case in campaign.get("cases", []):
                package_path = case.get("editorPackage")
                if not package_path:
                    continue
                package = package_reader(package_path)
                structure = package["rolePageStructure"]
                for role in package["supportedRoles"]:
                    editions.append({
                        "caseId": case["id"],
                        "role": role,
                        "expectedPageCount": structure[role]["pageCount"],
                    })
    return editions


def derivation_guard() -> tuple[bool, str]:
    """Prove the roster tracks the registry instead of a constant.

    Uses controlled fixtures rather than the live registry, so the guard keeps its
    meaning as real cases are added.
    """
    four_roles = ["student", "teacher", "answer", "accessible"]

    def reader(path: str) -> dict:
        roles = ["student", "teacher"] if path == "two-role" else four_roles
        return {"supportedRoles": roles, "rolePageStructure": {role: {"pageCount": 1} for role in roles}}

    def registry(cases: list[dict]) -> dict:
        return {"schemaVersion": 2, "curricula": [{"campaigns": [{"cases": cases}]}]}

    a = {"id": "FIX-CASE01", "editorPackage": "four-role"}
    b = {"id": "FIX-CASE02", "editorPackage": "four-role"}
    unregistered = {"id": "FIX-CASE03"}
    two_role = {"id": "FIX-CASE04", "editorPackage": "two-role"}

    observed = {
        "two cases": len(registered_case_editions(registry([a, b]), reader)),
        "three cases": len(registered_case_editions(registry([a, b, dict(b, id="FIX-CASE05")]), reader)),
        "editor-incompatible case excluded": len(registered_case_editions(registry([a, unregistered]), reader)),
        "roles come from the package": len(registered_case_editions(registry([two_role]), reader)),
    }
    expected = {
        "two cases": 8,
        "three cases": 12,
        "editor-incompatible case excluded": 4,
        "roles come from the package": 2,
    }
    return observed == expected, json.dumps({"observed": observed, "expected": expected}, sort_keys=True)


class PdfTestHandler(CurriculumEditorHandler):
    def do_GET(self) -> None:  # noqa: N802
        match = re.fullmatch(r"/__pdf_test/(\d+)\.html", urlsplit(self.path).path)
        if match:
            index = int(match.group(1))
            documents = self.server.documents  # type: ignore[attr-defined]
            if index >= len(documents):
                self.send_error(404)
                return
            body = documents[index]["html"].encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def do_POST(self) -> None:  # noqa: N802
        if urlsplit(self.path).path != "/__pdf_test_documents":
            super().do_POST()
            return
        size = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(size))
        self.server.document_error = payload.get("error")  # type: ignore[attr-defined]
        self.server.documents = payload.get("documents", [])  # type: ignore[attr-defined]
        self.send_response(204)
        self.end_headers()


def stop(process: subprocess.Popen) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def chrome_base(chrome: Path, profile: Path) -> list[str]:
    return [
        str(chrome), "--headless=new", "--no-sandbox", "--disable-gpu",
        "--disable-background-networking", "--disable-component-update", "--disable-default-apps",
        "--no-first-run", f"--user-data-dir={profile}",
    ]


def generate_pdf(chrome: Path, profile: Path, url: str, target: Path) -> None:
    process = subprocess.Popen(
        [*chrome_base(chrome, profile), "--no-pdf-header-footer", f"--print-to-pdf={target}", url],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    deadline = time.monotonic() + 45
    previous_size = -1
    stable = 0
    while time.monotonic() < deadline:
        size = target.stat().st_size if target.is_file() else 0
        stable = stable + 1 if size > 10_000 and size == previous_size else 0
        previous_size = size
        if stable >= 10 or process.poll() is not None:
            break
        time.sleep(.1)
    stop(process)
    if not target.is_file() or target.stat().st_size <= 10_000:
        raise RuntimeError(f"Chrome did not generate {target.name}")


def pdf_pages(path: Path) -> list[dict[str, object]]:
    data = path.read_bytes()
    pages = []
    for match in re.finditer(rb"<</Type /Page\b.*?endobj", data, re.DOTALL):
        page = match.group(0)
        box = re.search(rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\]", page)
        contents = re.search(rb"/Contents\s+(\d+)\s+0\s+R", page)
        parent = re.search(rb"/StructParents\s+(\d+)", page)
        length = 0
        if contents:
            content_object = re.search(rb"(?:^|\n)" + contents.group(1) + rb" 0 obj\s*<<(.*?)>>\s*stream", data, re.DOTALL)
            length_match = re.search(rb"/Length\s+(\d+)", content_object.group(1)) if content_object else None
            length = int(length_match.group(1)) if length_match else 0
        pages.append({
            "mediaBox": tuple(float(value) for value in box.groups()) if box else None,
            "contentLength": length,
            "hasFont": b"/Font" in page,
            "structParent": int(parent.group(1)) if parent else None,
        })
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chrome", type=Path, default=Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    args = parser.parse_args()
    if not args.chrome.is_file():
        raise SystemExit(f"Chrome executable not found: {args.chrome}")

    server = ThreadingHTTPServer(("127.0.0.1", 0), PdfTestHandler)
    server.documents = []  # type: ignore[attr-defined]
    server.document_error = None  # type: ignore[attr-defined]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    port = server.server_address[1]
    base = f"http://127.0.0.1:{port}"
    assertions = []

    def check(name: str, passed: bool, detail: object = "") -> None:
        assertions.append({"name": name, "pass": bool(passed), "detail": detail if isinstance(detail, str) else json.dumps(detail, sort_keys=True)})

    guard_passed, guard_detail = derivation_guard()
    check("expected print-document roster is derived from the registry rather than hard-coded",
          guard_passed, guard_detail)

    try:
        with tempfile.TemporaryDirectory(prefix="curriculum-editor-pdf-") as temporary:
            temp = Path(temporary)
            harness = subprocess.Popen(
                [*chrome_base(args.chrome, temp / "harness-profile"), "--virtual-time-budget=30000", f"{base}/apps/curriculum-editor/tests/pdf-harness.html"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            deadline = time.monotonic() + 90
            while not server.documents and not server.document_error and time.monotonic() < deadline:  # type: ignore[attr-defined]
                if harness.poll() is not None:
                    break
                time.sleep(.1)
            stop(harness)
            if server.document_error:  # type: ignore[attr-defined]
                raise RuntimeError(server.document_error)  # type: ignore[attr-defined]
            documents = server.documents  # type: ignore[attr-defined]
            expected_editions = registered_case_editions(json.loads(REGISTRY_PATH.read_text(encoding="utf-8")))
            expected_keys = [(item["caseId"], item["role"]) for item in expected_editions]
            actual_keys = [(document["caseId"], document["role"]) for document in documents]
            missing = [key for key in expected_keys if key not in actual_keys]
            unexpected = [key for key in actual_keys if key not in expected_keys]
            check(
                f"PDF harness generated every registered case-edition print document "
                f"({len(expected_editions)} derived from the canonical registry)",
                actual_keys == expected_keys,
                {"derived": len(expected_editions), "generated": len(documents),
                 "missing": [list(key) for key in missing],
                 "unexpected": [list(key) for key in unexpected]},
            )
            declared_counts = {(item["caseId"], item["role"]): item["expectedPageCount"] for item in expected_editions}
            mismatched = [
                {"case": document["caseId"], "role": document["role"],
                 "package": declared_counts.get((document["caseId"], document["role"])),
                 "harness": document["expectedPageCount"]}
                for document in documents
                if declared_counts.get((document["caseId"], document["role"])) != document["expectedPageCount"]
            ]
            check("every generated document carries the page count its package declares",
                  not mismatched, mismatched)

            def render(index: int) -> Path:
                document = documents[index]
                target = temp / f'{document["caseId"]}-{document["role"]}.pdf'
                generate_pdf(args.chrome, temp / f"pdf-profile-{index}", f"{base}/__pdf_test/{index}.html", target)
                return target

            with ThreadPoolExecutor(max_workers=4) as pool:
                paths = list(pool.map(render, range(len(documents))))

            for index, (document, path) in enumerate(zip(documents, paths)):
                label = f'{document["caseId"]} {document["role"]}'
                soup = BeautifulSoup(document["html"], "html.parser")
                dom_pages = soup.select(f'.page[data-role="{document["role"]}"]')
                page_ids = [page.get("data-page-id") for page in dom_pages]
                check(f"{label} print DOM preserves expected nonblank page order", page_ids == document["expectedPageIds"] and len(page_ids) == document["expectedPageCount"] and all(page.get_text(" ", strip=True) for page in dom_pages), page_ids)
                check(f"{label} print DOM contains no authoring controls or draft-only content", not soup.select(AUTHORING_SELECTOR) and not soup.select("script") and not any(text in document["html"] for text in AUTHORING_TEXT))
                pages = pdf_pages(path)
                check(f"{label} browser PDF page count matches canonical count with no trailing page", len(pages) == document["expectedPageCount"], {"expected": document["expectedPageCount"], "actual": len(pages)})
                check(f"{label} browser PDF pages are all Letter dimensions", bool(pages) and all(page["mediaBox"] == (0.0, 0.0, 612.0, 792.0) for page in pages), [page["mediaBox"] for page in pages])
                check(f"{label} browser PDF has no blank or missing worksheet page", len(pages) == document["expectedPageCount"] and all(page["hasFont"] and page["contentLength"] > 500 for page in pages), pages)
                check(f"{label} browser PDF structure order follows the print DOM", [page["structParent"] for page in pages] == list(range(len(pages))), [page["structParent"] for page in pages])
                if document["caseId"] == "SSS-C1-CASE01" and document["role"] == "student":
                    actual = {
                        persist_id: int(node.get("data-layout-height-active", "0")) if (node := soup.select_one(f'[data-persist-id="{persist_id}"]')) else 0
                        for persist_id in CASE01_APPROVED
                    }
                    check("Case 01 Student PDF source includes all five approved canonical heights", actual == CASE01_APPROVED, actual)
    except Exception as error:
        check("PDF regression runner completed", False, f"{type(error).__name__}: {error}")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)

    passed = sum(assertion["pass"] for assertion in assertions)
    payload = {"validator": "curriculum-editor-pdf-v1", "status": "PASS" if passed == len(assertions) else "FAIL", "passed": passed, "total": len(assertions), "assertions": assertions}
    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
