#!/usr/bin/env python3
"""Serve the repository-local Curriculum Editor over HTTP."""
from __future__ import annotations

import argparse
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


APP_DIR = Path(__file__).resolve().parent
REPOSITORY_ROOT = APP_DIR.parents[1]


class CurriculumEditorHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript; charset=utf-8",
        ".mjs": "text/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".svg": "image/svg+xml",
    }

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, directory=str(REPOSITORY_ROOT), **kwargs)

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        super().end_headers()

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        path = urlsplit(self.path).path
        if path == "/":
            self.send_response(302)
            self.send_header("Location", "/apps/curriculum-editor/")
            self.end_headers()
            return
        if path == "/__health":
            body = json.dumps({"status": "ok", "application": "curriculum-editor"}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="Local bind address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Local port (default: 8000)")
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), CurriculumEditorHandler)
    print(f"Curriculum Editor: http://{args.host}:{args.port}/apps/curriculum-editor/", flush=True)
    print(f"Repository root: {REPOSITORY_ROOT}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
