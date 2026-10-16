#!/usr/bin/env python3
"""
Auto Preview — Antigravity Kit
==============================
Manages (start/stop/status) the local development server for previewing applications.
Supports Node.js (Next/Vite/Express), Python (FastAPI/Flask/Django/HTTP), and Flutter.
Persists runtime state in .agent/preview.json.

Usage:
    python .agent/scripts/auto_preview.py start [port]
    python .agent/scripts/auto_preview.py stop
    python .agent/scripts/auto_preview.py status
"""

import os
import sys
import time
import json
import signal
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
AGENT_DIR = SCRIPT_DIR.parent
STATE_FILE = AGENT_DIR / "preview.json"
PID_FILE = AGENT_DIR / "preview.pid"
LOG_FILE = AGENT_DIR / "preview.log"

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _common import Colors, print_header, print_success, print_warning, print_error, print_step


def get_project_root() -> Path:
    return Path(".").resolve()


def is_running(pid: int) -> bool:
    """Verify if a process with given PID is actively executing."""
    if sys.platform == "win32":
        try:
            # Query tasklist with CSV output
            cmd = ["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"]
            out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True)
            return str(pid) in out
        except Exception:
            return False
    else:
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False


def detect_start_command(root: Path, port: int) -> Tuple[Optional[List[str]], str]:
    """
    Detect the appropriate dev server command across ecosystems.
    Returns (command_list, stack_name).
    """
    # 1. Node.js detection (package.json)
    pkg_file = root / "package.json"
    if pkg_file.exists():
        try:
            with open(pkg_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            scripts = data.get("scripts", {})
            if "dev" in scripts:
                return ["npm", "run", "dev"], "Node.js (npm run dev)"
            elif "start" in scripts:
                return ["npm", "start"], "Node.js (npm start)"
        except Exception:
            pass

    # 2. Python detection
    # Django
    if (root / "manage.py").exists():
        return [sys.executable, "manage.py", "runserver", str(port)], "Python (Django)"

    # FastAPI / Uvicorn
    for entry in ["main.py", "app.py", "api.py"]:
        entry_path = root / entry
        if entry_path.exists():
            content = entry_path.read_text(encoding="utf-8", errors="ignore").lower()
            if "fastapi" in content or "uvicorn" in content:
                module = entry_path.stem
                return [sys.executable, "-m", "uvicorn", f"{module}:app", "--reload", "--port", str(port)], "Python (FastAPI)"
            elif "flask" in content:
                return [sys.executable, "-m", "flask", "run", "--port", str(port)], "Python (Flask)"

    # Flutter Web
    if (root / "pubspec.yaml").exists():
        return ["flutter", "run", "-d", "web-server", "--web-port", str(port)], "Flutter (Web)"

    # 3. Static Web Server fallback (HTML files present)
    html_files = list(root.glob("*.html"))
    if html_files or (root / "index.html").exists():
        return [sys.executable, "-m", "http.server", str(port)], "Static HTTP Server (Python)"

    return None, "Unknown"


def start_server(port: int = 3000):
    root = get_project_root()
    agent_dir = root / ".agent"
    agent_dir.mkdir(exist_ok=True)

    state_path = agent_dir / "preview.json"

    # Check existing process
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            pid = state.get("pid")
            if pid and is_running(pid):
                print_warning(f"Preview server is already running (PID: {pid}, URL: {state.get('url')})")
                return
        except Exception:
            pass

    cmd, stack_name = detect_start_command(root, port)
    if not cmd:
        print_error("No supported dev runner found (no package.json dev/start, manage.py, FastAPI/Flask, or static HTML).")
        sys.exit(1)

    print_step(f"Starting {stack_name} preview on port {port}...")

    env = os.environ.copy()
    env["PORT"] = str(port)

    log_path = agent_dir / "preview.log"
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"\n--- Server started at {datetime.now().isoformat()} ({stack_name}) ---\n")
        log_file.flush()
        process = subprocess.Popen(
            cmd,
            cwd=str(root),
            stdout=log_file,
            stderr=log_file,
            env=env,
            shell=(sys.platform == "win32" and cmd[0] in ["npm", "flutter"])
        )

    url = f"http://localhost:{port}"
    state_payload = {
        "pid": process.pid,
        "port": port,
        "url": url,
        "stack": stack_name,
        "command": cmd,
        "started_at": datetime.now().isoformat(),
        "log_file": str(log_path)
    }

    state_path.write_text(json.dumps(state_payload, indent=2), encoding="utf-8")
    (agent_dir / "preview.pid").write_text(str(process.pid), encoding="utf-8")

    print_success(f"Preview started successfully! (PID: {process.pid})")
    print(f"  • Stack: {Colors.CYAN}{stack_name}{Colors.ENDC}")
    print(f"  • URL:   {Colors.BOLD}{Colors.GREEN}{url}{Colors.ENDC}")
    print(f"  • Logs:  {log_path}\n")


def stop_server():
    root = get_project_root()
    state_path = root / ".agent" / "preview.json"
    pid_path = root / ".agent" / "preview.pid"

    pid = None
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            pid = state.get("pid")
        except Exception:
            pass

    if not pid and pid_path.exists():
        try:
            pid = int(pid_path.read_text().strip())
        except Exception:
            pass

    if not pid:
        print("ℹ️  No active preview server process found.")
        return

    try:
        if is_running(pid):
            if sys.platform == "win32":
                subprocess.call(["taskkill", "/F", "/T", "/PID", str(pid)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                os.kill(pid, signal.SIGTERM)
            print_success(f"Preview server stopped (PID: {pid})")
        else:
            print("ℹ️  Process was already terminated.")
    except Exception as e:
        print_error(f"Error terminating preview server: {e}")
    finally:
        if state_path.exists():
            state_path.unlink()
        if pid_path.exists():
            pid_path.unlink()


def status_server():
    root = get_project_root()
    state_path = root / ".agent" / "preview.json"

    print_header("PREVIEW SERVER STATUS", width=60)

    if not state_path.exists():
        print("⚪ Status: Stopped (No preview server registered)")
        print(f"{'=' * 60}\n")
        return

    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        pid = state.get("pid")
        if pid and is_running(pid):
            print(f"✅ Status:     {Colors.GREEN}{Colors.BOLD}RUNNING{Colors.ENDC}")
            print(f"🔢 PID:        {pid}")
            print(f"🌐 URL:        {Colors.CYAN}{Colors.BOLD}{state.get('url')}{Colors.ENDC}")
            print(f"🔧 Stack:      {state.get('stack')}")
            print(f"⏰ Started:    {state.get('started_at')}")
            print(f"📝 Logs:       {state.get('log_file')}")
        else:
            print(f"⚠️  Status:     {Colors.YELLOW}STALE (PID {pid} not found in system){Colors.ENDC}")
            # Clean up stale state
            state_path.unlink(missing_ok=True)
    except Exception as e:
        print_error(f"Error reading preview status: {e}")

    print(f"\n{'=' * 60}\n")


def main():
    parser = argparse.ArgumentParser(description="Antigravity Auto Preview Manager")
    parser.add_argument("action", choices=["start", "stop", "status"], help="Preview action")
    parser.add_argument("port", nargs="?", default="3000", help="Port number (default: 3000)")

    args = parser.parse_args()

    if args.action == "start":
        start_server(int(args.port))
    elif args.action == "stop":
        stop_server()
    elif args.action == "status":
        status_server()


if __name__ == "__main__":
    main()
