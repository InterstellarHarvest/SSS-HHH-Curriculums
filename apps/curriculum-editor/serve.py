#!/usr/bin/env python3
"""Serve the repository-local Curriculum Editor over HTTP."""
from __future__ import annotations

import argparse
import ipaddress
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from authoring_service import MAX_REQUEST_BYTES, AuthoringError, apply_layout_changes, context_payload


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

    def send_json(self, status: int, payload: dict[str, object]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def local_request(self) -> bool:
        try:
            peer_is_local = ipaddress.ip_address(self.client_address[0]).is_loopback
        except ValueError:
            return False
        host = self.headers.get("Host", "")
        hostname = urlsplit(f"//{host}").hostname
        host_is_local = hostname == "localhost"
        if hostname and not host_is_local:
            try:
                host_is_local = ipaddress.ip_address(hostname).is_loopback
            except ValueError:
                host_is_local = False
        origin = self.headers.get("Origin")
        origin_is_local = True
        if origin:
            origin_host = urlsplit(origin).hostname
            origin_is_local = origin_host == "localhost"
            if origin_host and not origin_is_local:
                try:
                    origin_is_local = ipaddress.ip_address(origin_host).is_loopback
                except ValueError:
                    origin_is_local = False
        return peer_is_local and host_is_local and origin_is_local

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        path = urlsplit(self.path).path
        if path == "/":
            self.send_response(302)
            self.send_header("Location", "/apps/curriculum-editor/")
            self.end_headers()
            return
        if path == "/__health":
            self.send_json(200, {"status": "ok", "application": "curriculum-editor"})
            return
        if path == "/__authoring/context":
            if not self.local_request():
                self.send_json(403, {"error": "Authoring endpoints are loopback-only.", "code": "loopback_required"})
                return
            self.send_json(200, context_payload(REPOSITORY_ROOT))
            return
        super().do_GET()

    def do_POST(self) -> None:  # noqa: N802 - stdlib handler API
        path = urlsplit(self.path).path
        if path != "/__authoring/apply-layout-overrides":
            self.send_json(404, {"error": "Unknown authoring endpoint.", "code": "not_found"})
            return
        if not self.local_request():
            self.send_json(403, {"error": "Authoring endpoints are loopback-only.", "code": "loopback_required"})
            return
        if self.headers.get_content_type() != "application/json":
            self.send_json(415, {"error": "Content-Type must be application/json.", "code": "content_type"})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            size = 0
        if size < 2 or size > MAX_REQUEST_BYTES:
            self.send_json(413, {"error": "Invalid authoring request size.", "code": "request_size"})
            return
        try:
            payload = json.loads(self.rfile.read(size))
            result = apply_layout_changes(REPOSITORY_ROOT, payload)
        except (json.JSONDecodeError, UnicodeDecodeError):
            self.send_json(400, {"error": "Request body is not valid JSON.", "code": "invalid_json"})
            return
        except AuthoringError as error:
            self.send_json(error.status, {"error": str(error), "code": error.code})
            return
        except Exception:
            self.log_exception("Unexpected authoring service failure")
            self.send_json(500, {"error": "Unexpected authoring service failure.", "code": "internal_error"})
            return
        self.send_json(200, result)

    def log_exception(self, message: str) -> None:
        import traceback
        self.log_error("%s\n%s", message, traceback.format_exc())


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
