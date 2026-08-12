#!/usr/bin/env python3
"""Serve the repository-local Curriculum Editor over HTTP."""
from __future__ import annotations

import argparse
import ipaddress
import json
import os
import signal
import sys
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from authoring_service import MAX_REQUEST_BYTES, AuthoringError, apply_layout_changes, context_payload


APP_DIR = Path(__file__).resolve().parent
REPOSITORY_ROOT = APP_DIR.parents[1]

HEARTBEAT_TIMEOUT_SECONDS = 15.0
HIDDEN_HEARTBEAT_TIMEOUT_SECONDS = 180.0
STARTUP_GRACE_SECONDS = 60.0
LIFECYCLE_POLL_SECONDS = 0.25
MAX_HEARTBEAT_BODY_BYTES = 512
SERVER_CONTROL_PATHS = frozenset({"/__server/heartbeat", "/__server/stop", "/__server/restart"})


class ServerLifecycle:
    """In-memory editor-activity tracking and shutdown/restart coordination.

    A heartbeat is a timestamp update only; no filesystem or curriculum work
    happens on this path. Timeouts apply only when auto_shutdown is enabled
    (the one-click launcher passes --auto-shutdown; a directly launched
    development server never exits on its own).
    """

    def __init__(self, auto_shutdown: bool, heartbeat_timeout: float, startup_grace: float, hidden_timeout: float) -> None:
        self.auto_shutdown = auto_shutdown
        self.heartbeat_timeout = heartbeat_timeout
        self.startup_grace = startup_grace
        self.hidden_timeout = max(hidden_timeout, heartbeat_timeout)
        self._lock = threading.Lock()
        self._signal = threading.Event()
        self._started = time.monotonic()
        self._last_heartbeat: float | None = None
        self._last_tab_state = "visible"
        self._reason: str | None = None

    def record_heartbeat(self, tab_state: str | None) -> None:
        with self._lock:
            self._last_heartbeat = time.monotonic()
            self._last_tab_state = tab_state if tab_state in ("visible", "hidden", "closing") else "visible"

    def request(self, reason: str) -> None:
        with self._lock:
            if self._reason is None:
                self._reason = reason
        self._signal.set()

    @property
    def reason(self) -> str | None:
        with self._lock:
            return self._reason

    def snapshot(self) -> dict[str, bool]:
        with self._lock:
            return {"autoShutdown": self.auto_shutdown, "heartbeatSeen": self._last_heartbeat is not None}

    def expired_reason(self) -> str | None:
        with self._lock:
            now = time.monotonic()
            if self._last_heartbeat is None:
                return "startup-timeout" if now - self._started > self.startup_grace else None
            # A hidden tab's timers are heavily throttled by browsers, so it is
            # given a longer allowance than the visible-tab timeout.
            allowance = self.hidden_timeout if self._last_tab_state == "hidden" else self.heartbeat_timeout
            return "heartbeat-timeout" if now - self._last_heartbeat > allowance else None

    def wait_for_shutdown(self) -> str | None:
        while not self._signal.wait(LIFECYCLE_POLL_SECONDS):
            if self.auto_shutdown:
                expired = self.expired_reason()
                if expired:
                    self.request(expired)
        return self.reason


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
            payload: dict[str, object] = {"status": "ok", "application": "curriculum-editor"}
            lifecycle = getattr(self.server, "lifecycle", None)
            if lifecycle is not None:
                payload["lifecycle"] = lifecycle.snapshot()
            self.send_json(200, payload)
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
        if path in SERVER_CONTROL_PATHS:
            self.handle_server_control(path)
            return
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

    def handle_server_control(self, path: str) -> None:
        if not self.local_request():
            self.send_json(403, {"error": "Server control endpoints are loopback-only.", "code": "loopback_required"})
            return
        lifecycle = getattr(self.server, "lifecycle", None)
        if lifecycle is None:
            self.send_json(404, {"error": "Server lifecycle control is unavailable.", "code": "not_found"})
            return
        if path == "/__server/heartbeat":
            lifecycle.record_heartbeat(self.read_heartbeat_state())
            self.send_json(200, {"status": "ok"})
            return
        action = "stop" if path == "/__server/stop" else "restart"
        self.send_json(200, {"status": action})
        lifecycle.request(action)

    def read_heartbeat_state(self) -> str | None:
        try:
            size = int(self.headers.get("Content-Length") or "0")
        except ValueError:
            return None
        if size <= 0 or size > MAX_HEARTBEAT_BODY_BYTES:
            return None
        try:
            payload = json.loads(self.rfile.read(size))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None
        state = payload.get("state") if isinstance(payload, dict) else None
        return state if isinstance(state, str) else None

    def log_request(self, code: object = "-", size: object = "-") -> None:
        if urlsplit(self.path).path == "/__server/heartbeat" and str(code) == "200":
            return
        super().log_request(code, size)

    def log_exception(self, message: str) -> None:
        import traceback
        self.log_error("%s\n%s", message, traceback.format_exc())


def announce(message: str) -> None:
    try:
        print(message, flush=True)
    except OSError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="Local bind address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Local port (default: 8000; 0 selects a free port)")
    parser.add_argument("--auto-shutdown", action="store_true", help="Exit automatically when no editor tab is sending heartbeats (used by the one-click launcher).")
    parser.add_argument("--heartbeat-timeout", type=float, default=HEARTBEAT_TIMEOUT_SECONDS, help=argparse.SUPPRESS)
    parser.add_argument("--startup-grace", type=float, default=STARTUP_GRACE_SECONDS, help=argparse.SUPPRESS)
    parser.add_argument("--hidden-heartbeat-timeout", type=float, default=HIDDEN_HEARTBEAT_TIMEOUT_SECONDS, help=argparse.SUPPRESS)
    args = parser.parse_args()
    lifecycle = ServerLifecycle(args.auto_shutdown, args.heartbeat_timeout, args.startup_grace, args.hidden_heartbeat_timeout)
    server = ThreadingHTTPServer((args.host, args.port), CurriculumEditorHandler)
    server.lifecycle = lifecycle  # type: ignore[attr-defined]
    host, port = server.server_address[:2]
    print(f"Curriculum Editor: http://{host}:{port}/apps/curriculum-editor/", flush=True)
    print(f"Repository root: {REPOSITORY_ROOT}", flush=True)
    if args.auto_shutdown:
        print("Auto-shutdown: the server exits on its own after the editor tab closes.", flush=True)

    def handle_signal(signum: int, _frame: object) -> None:
        lifecycle.request("signal")

    signal.signal(signal.SIGTERM, handle_signal)
    if hasattr(signal, "SIGHUP"):
        signal.signal(signal.SIGHUP, handle_signal)

    def monitor() -> None:
        lifecycle.wait_for_shutdown()
        time.sleep(0.2)  # let the response that triggered stop/restart reach its client
        server.shutdown()

    threading.Thread(target=monitor, name="lifecycle-monitor", daemon=True).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        lifecycle.request("keyboard-interrupt")
    finally:
        server.server_close()
    reason = lifecycle.reason
    announce({
        "startup-timeout": f"No editor connected within {args.startup_grace:.0f}s; shutting down.",
        "heartbeat-timeout": "Editor heartbeat lost (tab closed); shutting down.",
        "stop": "Stop requested from the editor; shutting down.",
        "restart": "Restart requested from the editor; restarting…",
        "signal": "Termination signal received; shutting down.",
        "keyboard-interrupt": "\nServer stopped.",
    }.get(reason or "", "Server stopped."))
    if reason == "restart":
        restart_args = [
            sys.executable, str(APP_DIR / "serve.py"),
            "--host", args.host, "--port", str(port),
            "--heartbeat-timeout", str(args.heartbeat_timeout),
            "--startup-grace", str(args.startup_grace),
            "--hidden-heartbeat-timeout", str(args.hidden_heartbeat_timeout),
        ]
        if args.auto_shutdown:
            restart_args.append("--auto-shutdown")
        sys.stdout.flush()
        sys.stderr.flush()
        # Same PID, fresh process image: the owning launcher keeps waiting on
        # this exact process, so no orphan and nothing else is ever killed.
        os.execv(sys.executable, restart_args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
