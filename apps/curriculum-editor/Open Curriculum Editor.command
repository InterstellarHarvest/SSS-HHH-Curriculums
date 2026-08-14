#!/bin/bash
# One-click launcher for the SSS/HHH Curriculum Editor.
#
# Lives in apps/curriculum-editor/ (repository root is two levels up).
# Double-click this file in Finder: it starts the local editor server (unless
# one is already running), opens the editor in Firefox and brings Firefox to
# the foreground, and stays responsible for the server it started until that
# server exits. The server shuts itself down automatically once the editor tab
# closes (heartbeat loss), so this window closes on its own when you are done.
# For a launch with no Terminal window at all, use launcher.app beside this
# file instead.
set -u

REPO_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
SERVE_SCRIPT="$REPO_DIR/apps/curriculum-editor/serve.py"
PORT="${CURRICULUM_EDITOR_PORT:-8000}"
EDITOR_URL="http://127.0.0.1:$PORT/apps/curriculum-editor/"
FIREFOX_BIN="/Applications/Firefox.app/Contents/MacOS/firefox"

fail() {
  echo "" >&2
  echo "ERROR: $1" >&2
  if [ -t 0 ]; then
    read -r -p "Press Return to close this window. "
  fi
  exit 1
}

command -v python3 >/dev/null 2>&1 || fail "python3 was not found. Install the macOS Command Line Tools (xcode-select --install) and try again."
[ -f "$SERVE_SCRIPT" ] || fail "Could not find serve.py relative to this launcher. Keep this file in apps/curriculum-editor/ inside the repository."

# Open the editor in a real Firefox tab and explicitly bring Firefox forward.
# Calling Firefox's executable with -new-tab reliably hands the URL to an
# already-running Firefox instance; macOS `open -a Firefox URL` can activate
# Firefox without surfacing a new tab on some installations/session states.
# Tests and headless smoke checks may override the opener with
# CURRICULUM_EDITOR_OPEN. If Firefox is unavailable, use the default browser.
open_editor() {
  if [ -n "${CURRICULUM_EDITOR_OPEN:-}" ]; then
    "$CURRICULUM_EDITOR_OPEN" "$EDITOR_URL"
    return $?
  fi

  if [ -x "$FIREFOX_BIN" ]; then
    "$FIREFOX_BIN" -new-tab "$EDITOR_URL" >/dev/null 2>&1 &
    /usr/bin/osascript -e 'tell application "Firefox" to activate' >/dev/null 2>&1 || true
    return 0
  fi

  /usr/bin/open "$EDITOR_URL"
}

# Positively identify what is on the port before doing anything:
#   exit 0 = this Curriculum Editor is already serving
#   exit 3 = nothing is listening (port free)
#   exit 4 = something that is not the Curriculum Editor answers (leave it alone)
probe_health() {
  python3 - "$PORT" <<'PY'
import json, sys, urllib.error, urllib.request

port = int(sys.argv[1])
try:
    with urllib.request.urlopen(f"http://127.0.0.1:{port}/__health", timeout=3) as response:
        payload = json.load(response)
except urllib.error.URLError as error:
    raise SystemExit(3 if isinstance(error.reason, ConnectionRefusedError) else 4)
except Exception:
    raise SystemExit(4)
ok = isinstance(payload, dict) and payload.get("status") == "ok" and payload.get("application") == "curriculum-editor"
raise SystemExit(0 if ok else 4)
PY
}

probe_health
state=$?
if [ "$state" -eq 0 ]; then
  echo "Curriculum Editor is already running at $EDITOR_URL - opening it."
  open_editor || fail "Could not open the Curriculum Editor in Firefox or the default browser."
  exit 0
fi
if [ "$state" -ne 3 ]; then
  fail "Port $PORT is already in use by something that is not the Curriculum Editor. That process was left untouched. Quit it, or relaunch with CURRICULUM_EDITOR_PORT=<free port>."
fi

echo "Starting the Curriculum Editor server on port $PORT..."
python3 "$SERVE_SCRIPT" --host 127.0.0.1 --port "$PORT" --auto-shutdown &
SERVER_PID=$!
trap 'kill -TERM "$SERVER_PID" 2>/dev/null' INT TERM

ready=""
for _ in $(seq 1 60); do
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then
    wait "$SERVER_PID" 2>/dev/null
    STATUS=$?
    if [ "$STATUS" -eq 0 ]; then
      # The server was asked to stop (or shut itself down) before the launcher
      # finished its readiness check; that is a clean stop, not a failure.
      echo "Curriculum Editor server stopped."
      exit 0
    fi
    fail "The Curriculum Editor server exited before it became ready (exit $STATUS)."
  fi
  probe_health
  if [ $? -eq 0 ]; then
    ready=1
    break
  fi
  sleep 0.5
done
if [ -z "$ready" ]; then
  kill -TERM "$SERVER_PID" 2>/dev/null
  wait "$SERVER_PID" 2>/dev/null
  fail "The server did not become ready on port $PORT within 30 seconds."
fi

echo "Opening $EDITOR_URL in Firefox."
open_editor || fail "Could not open the Curriculum Editor in Firefox or the default browser."
echo ""
echo "Leave this window open; it closes on its own after the editor tab closes."
wait "$SERVER_PID"
# Reap again in case the first wait was interrupted by the signal trap.
wait "$SERVER_PID" 2>/dev/null
echo "Curriculum Editor server stopped."
exit 0
