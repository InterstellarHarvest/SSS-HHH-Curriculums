#!/usr/bin/env python3
"""Lifecycle tests for the Curriculum Editor local server and one-click launcher.

Covers the heartbeat/auto-shutdown contract, loopback-only server control,
clean stop/restart, and the launcher's refusal to touch unrelated services.
Dependency-free: stdlib only, real subprocesses on ephemeral loopback ports.
"""
from __future__ import annotations

import http.client
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[1]
SERVE = APP / "serve.py"
LAUNCHER = ROOT / "Open Curriculum Editor.command"


def free_port() -> int:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


def request(port: int, method: str, path: str, body: bytes | None = None, headers: dict[str, str] | None = None, timeout: float = 3.0):
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    try:
        connection.request(method, path, body=body, headers=headers or {})
        response = connection.getresponse()
        raw = response.read()
    finally:
        connection.close()
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError):
        payload = None
    return response.status, payload


def heartbeat(port: int, state: str = "visible", headers: dict[str, str] | None = None):
    body = json.dumps({"state": state}).encode()
    merged = {"Content-Type": "application/json", **(headers or {})}
    return request(port, "POST", "/__server/heartbeat", body=body, headers=merged)


def wait_for_health(port: int, deadline_seconds: float = 10.0) -> dict:
    deadline = time.monotonic() + deadline_seconds
    while time.monotonic() < deadline:
        try:
            status, payload = request(port, "GET", "/__health", timeout=1.0)
            if status == 200 and isinstance(payload, dict) and payload.get("application") == "curriculum-editor":
                return payload
        except OSError:
            pass
        time.sleep(0.1)
    raise AssertionError(f"Curriculum Editor health did not come up on port {port}")


def port_refuses(port: int) -> bool:
    try:
        request(port, "GET", "/__health", timeout=1.0)
        return False
    except OSError:
        return True


class ServerFixtureMixin:
    def start_server(self, *extra: str) -> tuple[subprocess.Popen, int]:
        port = free_port()
        process = subprocess.Popen(
            [sys.executable, str(SERVE), "--port", str(port), *extra],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        self.addCleanup(self.reap, process)
        wait_for_health(port)
        return process, port

    @staticmethod
    def reap(process: subprocess.Popen) -> None:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


class ServerLifecycleTests(ServerFixtureMixin, unittest.TestCase):
    def test_health_reports_editor_identity_and_lifecycle(self) -> None:
        _, port = self.start_server()
        status, payload = request(port, "GET", "/__health")
        self.assertEqual(status, 200)
        self.assertEqual(payload.get("status"), "ok")
        self.assertEqual(payload.get("application"), "curriculum-editor")
        self.assertEqual(payload.get("lifecycle"), {"autoShutdown": False, "heartbeatSeen": False})

    def test_heartbeat_accepts_loopback_and_records_activity_only(self) -> None:
        _, port = self.start_server()
        status, payload = heartbeat(port)
        self.assertEqual(status, 200)
        self.assertEqual(payload, {"status": "ok"})
        health = wait_for_health(port)
        self.assertTrue(health["lifecycle"]["heartbeatSeen"])

    def test_server_control_rejects_nonlocal_origin_and_host(self) -> None:
        process, port = self.start_server()
        for path, headers in (
            ("/__server/heartbeat", {"Origin": "https://example.com"}),
            ("/__server/stop", {"Origin": "https://example.com"}),
            ("/__server/restart", {"Origin": "https://example.com"}),
            ("/__server/stop", {"Host": "evil.example"}),
        ):
            status, payload = request(port, "POST", path, headers={"Content-Type": "application/json", **headers})
            self.assertEqual(status, 403, f"{path} with {headers} must be rejected")
            self.assertEqual(payload.get("code"), "loopback_required")
        self.assertIsNone(process.poll(), "rejected control requests must not affect the server")
        wait_for_health(port)

    def test_stop_endpoint_shuts_down_cleanly(self) -> None:
        process, port = self.start_server()
        status, payload = request(port, "POST", "/__server/stop")
        self.assertEqual(status, 200)
        self.assertEqual(payload, {"status": "stop"})
        self.assertEqual(process.wait(timeout=10), 0)
        self.assertTrue(port_refuses(port))

    def test_restart_keeps_pid_resets_state_and_frees_no_orphans(self) -> None:
        process, port = self.start_server()
        heartbeat(port)
        self.assertTrue(wait_for_health(port)["lifecycle"]["heartbeatSeen"])
        status, payload = request(port, "POST", "/__server/restart")
        self.assertEqual(status, 200)
        self.assertEqual(payload, {"status": "restart"})
        deadline = time.monotonic() + 10
        fresh = None
        while time.monotonic() < deadline:
            try:
                health_status, health = request(port, "GET", "/__health", timeout=1.0)
                if health_status == 200 and health["lifecycle"]["heartbeatSeen"] is False:
                    fresh = health
                    break
            except OSError:
                pass
            time.sleep(0.1)
        self.assertIsNotNone(fresh, "restarted server must come back with fresh lifecycle state")
        self.assertIsNone(process.poll(), "restart must reuse the exact owned process (execv), never spawn an orphan")
        request(port, "POST", "/__server/stop")
        self.assertEqual(process.wait(timeout=10), 0)

    def test_startup_grace_expires_without_any_editor(self) -> None:
        process, port = self.start_server("--auto-shutdown", "--startup-grace", "1", "--heartbeat-timeout", "1")
        self.assertEqual(process.wait(timeout=15), 0)
        self.assertTrue(port_refuses(port))

    def test_heartbeat_loss_shuts_down_after_editor_disappears(self) -> None:
        process, port = self.start_server("--auto-shutdown", "--startup-grace", "30", "--heartbeat-timeout", "1.5")
        heartbeat(port)
        self.assertEqual(process.wait(timeout=15), 0)
        self.assertTrue(port_refuses(port))

    def test_refresh_sized_heartbeat_gap_does_not_stop_server(self) -> None:
        process, port = self.start_server("--auto-shutdown", "--startup-grace", "30", "--heartbeat-timeout", "3")
        heartbeat(port)
        time.sleep(1.5)  # a page reload re-initializes well inside the timeout
        heartbeat(port)
        time.sleep(1.5)
        for _ in range(4):  # steady heartbeats spanning longer than the timeout
            heartbeat(port)
            time.sleep(1.0)
        self.assertIsNone(process.poll(), "server must stay up across reload-sized gaps and steady heartbeats")
        wait_for_health(port)
        request(port, "POST", "/__server/stop")
        self.assertEqual(process.wait(timeout=10), 0)


class LauncherTests(ServerFixtureMixin, unittest.TestCase):
    @staticmethod
    def launcher_env(port: int) -> dict[str, str]:
        return {
            **os.environ,
            "CURRICULUM_EDITOR_PORT": str(port),
            "CURRICULUM_EDITOR_OPEN": "/usr/bin/true",
        }

    def test_launcher_refuses_unrelated_service_on_port(self) -> None:
        port = free_port()
        with tempfile.TemporaryDirectory(prefix="foreign-server.") as scratch:
            foreign = subprocess.Popen(
                [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
                cwd=scratch,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            self.addCleanup(self.reap, foreign)
            deadline = time.monotonic() + 10
            while time.monotonic() < deadline:
                try:
                    request(port, "GET", "/", timeout=1.0)
                    break
                except OSError:
                    time.sleep(0.1)
            result = subprocess.run(
                [str(LAUNCHER)],
                env=self.launcher_env(port),
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("not the Curriculum Editor", result.stderr)
            self.assertIsNone(foreign.poll(), "launcher must never kill an unrelated process")
            status, _ = request(port, "GET", "/", timeout=2.0)
            self.assertEqual(status, 200, "unrelated service must still be serving after the launcher declined")

    def test_launcher_recognizes_running_editor_without_duplicating_it(self) -> None:
        process, port = self.start_server()
        result = subprocess.run(
            [str(LAUNCHER)],
            env=self.launcher_env(port),
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("already running", result.stdout)
        self.assertNotIn("Starting", result.stdout)
        self.assertIsNone(process.poll())
        request(port, "POST", "/__server/stop")
        self.assertEqual(process.wait(timeout=10), 0)

    def test_launcher_starts_server_and_exits_when_server_stops(self) -> None:
        port = free_port()
        launcher = subprocess.Popen(
            [str(LAUNCHER)],
            env=self.launcher_env(port),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            health = wait_for_health(port, deadline_seconds=20)
            self.assertTrue(health["lifecycle"]["autoShutdown"], "launcher must start the server with --auto-shutdown")
            request(port, "POST", "/__server/stop")
            output, _ = launcher.communicate(timeout=15)
            self.assertEqual(launcher.returncode, 0)
            self.assertIn("Curriculum Editor server stopped", output)
            self.assertTrue(port_refuses(port))
        finally:
            if launcher.poll() is None:
                launcher.terminate()
                try:
                    launcher.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    launcher.kill()
                    launcher.wait(timeout=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
