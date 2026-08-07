#!/usr/bin/env python3
"""Run the existing curriculum-editor browser harness in headless Chromium.

The harness itself owns the browser assertions. This runner supplies a local HTTP
origin plus the read-only authoring-context endpoint the editor normally receives from
its repository-aware preview server, waits for the harness's explicit completion marker,
prints the returned JSON, and fails CI if any browser assertion or JavaScript error fails.
The repository-context fixture is intentionally deterministic and read-only so repeated
PR validation exercises the same browser contract without mutating candidate sources.

No screenshot or generated artifact is written into the repository.
"""
from __future__ import annotations

import contextlib
import json
import socket
import subprocess
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
HARNESS = "/apps/curriculum-editor/tests/browser-harness.html"
REPOSITORY_ID = "InterstellarHarvest/SSS-HHH-Curriculums"
REPOSITORY_LABEL = "SSS-HHH-Curriculums"


def current_revision() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "unknown"


REVISION = current_revision()


class HarnessRequestHandler(SimpleHTTPRequestHandler):
    """Static repository server with the minimal read-only authoring API used by tests."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, _format: str, *_args) -> None:
        return

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler contract
        if urlparse(self.path).path == "/__authoring/context":
            payload = json.dumps(
                {
                    "repositoryId": REPOSITORY_ID,
                    "repositoryLabel": REPOSITORY_LABEL,
                    "revision": REVISION,
                }
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()

    def do_POST(self) -> None:  # noqa: N802 - stdlib handler contract
        if urlparse(self.path).path == "/__browser_test_result":
            length = int(self.headers.get("Content-Length", "0") or 0)
            if length:
                self.rfile.read(length)
            self.send_response(204)
            self.end_headers()
            return
        self.send_error(404)


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def wait_server(port: int, timeout: float = 10.0) -> None:
    import urllib.request

    deadline = time.time() + timeout
    url = f"http://127.0.0.1:{port}{HARNESS}"
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                if response.status == 200:
                    return
        except Exception:
            time.sleep(0.1)
    raise RuntimeError("local browser-harness server did not become ready")


def main() -> int:
    port = free_port()
    server = ThreadingHTTPServer(("127.0.0.1", port), HarnessRequestHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        wait_server(port)
        url = f"http://127.0.0.1:{port}{HARNESS}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1600, "height": 1400})
            console_errors: list[str] = []
            page.on("pageerror", lambda error: console_errors.append(str(error)))
            page.goto(url, wait_until="domcontentloaded", timeout=30_000)
            page.wait_for_selector('body[data-complete="true"]', timeout=180_000)
            raw = page.locator("#results").inner_text()
            browser.close()

        payload = json.loads(raw)
        status = str(payload.get("status", "")).upper()
        passed = payload.get("passed")
        total = payload.get("total")
        javascript_errors = list(payload.get("javascriptErrors") or []) + console_errors
        print(json.dumps(payload, indent=2))
        print(f"Browser harness summary: {status} {passed}/{total}; JavaScript errors: {len(javascript_errors)}")
        if status != "PASS" or javascript_errors:
            if javascript_errors:
                print("Browser/console errors:")
                for error in javascript_errors:
                    print(f"- {error}")
            return 1
        return 0
    finally:
        with contextlib.suppress(Exception):
            server.shutdown()
        with contextlib.suppress(Exception):
            server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    raise SystemExit(main())
