#!/usr/bin/env python3
"""Run dependency-free browser assertions in installed Google Chrome."""
from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
import threading
import time
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

import sys

APP = Path(__file__).resolve().parents[1]
REPO = APP.parents[1]
sys.path.insert(0, str(APP))
from serve import CurriculumEditorHandler  # noqa: E402


class BrowserTestHandler(CurriculumEditorHandler):
    def do_POST(self) -> None:  # noqa: N802 - stdlib handler API
        if urlsplit(self.path).path != "/__browser_test_result":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            payload = json.loads(self.rfile.read(length))
        except (json.JSONDecodeError, UnicodeDecodeError):
            self.send_error(400)
            return
        self.server.test_result = payload  # type: ignore[attr-defined]
        self.send_response(204)
        self.end_headers()


def chrome_command(chrome: Path, profile: Path, url: str, *extra: str) -> list[str]:
    return [
        str(chrome),
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-background-networking",
        "--disable-component-update",
        "--disable-default-apps",
        "--no-first-run",
        f"--user-data-dir={profile}",
        "--virtual-time-budget=30000",
        *extra,
        url,
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chrome", type=Path, default=Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"))
    args = parser.parse_args()
    if not args.chrome.is_file():
        raise SystemExit(f"Chrome executable not found: {args.chrome}")
    server = ThreadingHTTPServer(("127.0.0.1", 0), BrowserTestHandler)
    server.test_result = None  # type: ignore[attr-defined]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    port = server.server_address[1]
    base = f"http://127.0.0.1:{port}/apps/curriculum-editor"
    try:
        with tempfile.TemporaryDirectory(prefix="curriculum-editor-browser-") as temporary:
            temp = Path(temporary)
            browser = subprocess.Popen(
                chrome_command(args.chrome, temp / "profile", f"{base}/tests/browser-harness.html"),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            deadline = time.monotonic() + 90
            while server.test_result is None and time.monotonic() < deadline:  # type: ignore[attr-defined]
                if browser.poll() is not None:
                    break
                time.sleep(.1)
            if browser.poll() is None:
                browser.terminate()
                try:
                    browser.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    browser.kill()
                    browser.wait(timeout=5)
            payload = server.test_result  # type: ignore[attr-defined]
            if payload is None:
                print("Browser harness did not post results before timeout.")
                return 1
            screenshot = temp / "curriculum-editor.png"
            capture = subprocess.Popen(
                chrome_command(
                    args.chrome,
                    temp / "screenshot-profile",
                    f"{base}/index.html?role=student",
                    "--window-size=1440,1200",
                    f"--screenshot={screenshot}",
                ),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            screenshot_deadline = time.monotonic() + 20
            while time.monotonic() < screenshot_deadline:
                if screenshot.is_file() and screenshot.stat().st_size > 10_000:
                    break
                if capture.poll() is not None:
                    break
                time.sleep(.1)
            if capture.poll() is None:
                capture.terminate()
                try:
                    capture.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    capture.kill()
                    capture.wait(timeout=5)
            screenshot_ok = screenshot.is_file() and screenshot.stat().st_size > 10_000
            payload["assertions"].append({"name": "browser-rendered screenshot smoke review completed", "pass": screenshot_ok, "detail": f"temporary PNG bytes: {screenshot.stat().st_size if screenshot.is_file() else 0}"})
            payload["total"] += 1
            if screenshot_ok:
                payload["passed"] += 1
            payload["status"] = "PASS" if payload["passed"] == payload["total"] else "FAIL"
            print(json.dumps(payload, indent=2))
            return 0 if payload["status"] == "PASS" else 1
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


if __name__ == "__main__":
    raise SystemExit(main())
