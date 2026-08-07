#!/usr/bin/env python3
"""Run the existing curriculum-editor browser harness in headless Chromium.

The harness itself owns the browser assertions. This runner supplies a local HTTP
origin, waits for the harness's explicit completion marker, prints the returned
JSON, and fails CI if any browser assertion or JavaScript error fails.

No screenshot or generated artifact is written into the repository.
"""
from __future__ import annotations

import contextlib
import json
import socket
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
HARNESS = "/apps/curriculum-editor/tests/browser-harness.html"


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
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
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
            server.terminate()
            server.wait(timeout=5)
        if server.poll() is None:
            with contextlib.suppress(Exception):
                server.kill()


if __name__ == "__main__":
    raise SystemExit(main())
