#!/usr/bin/env python3
"""
Common Utilities & Formatting — Antigravity Scripts Suite
=========================================================
Centralized ANSI colors, formatted logging, subprocess runner,
and manifest loader shared across all .agent/scripts/ tools.
"""

import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

# Ensure safe UTF-8 output on Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ENDC = '\033[0m'


def print_header(text: str, width: int = 60):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * width}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(width)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * width}{Colors.ENDC}\n")


def print_step(text: str):
    print(f"{Colors.BOLD}{Colors.BLUE}🔄 {text}{Colors.ENDC}")


def print_success(text: str):
    print(f"{Colors.GREEN}✅ {text}{Colors.ENDC}")


def print_warning(text: str):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.ENDC}")


def print_error(text: str):
    print(f"{Colors.RED}❌ {text}{Colors.ENDC}")


def check_script_exists(script_path: Path) -> bool:
    """Check if script file exists and is a valid file."""
    return script_path.exists() and script_path.is_file()


def run_script(
    name: str,
    script_path: Path,
    project_path: str,
    url: Optional[str] = None,
    timeout: int = 300
) -> Dict[str, Any]:
    """
    Run a validation or audit script with standardized timing and error handling.
    
    Returns:
        dict: name, passed, output, error, skipped, duration
    """
    if not check_script_exists(script_path):
        print_warning(f"{name}: Script not found ({script_path}), skipping")
        return {
            "name": name,
            "passed": True,
            "output": "",
            "error": "File not found",
            "skipped": True,
            "duration": 0.0
        }

    print_step(f"Running: {name}")
    start_time = datetime.now()

    # Build command
    cmd = [sys.executable, str(script_path), project_path]
    if url and any(kw in script_path.name.lower() for kw in ["lighthouse", "playwright", "url", "e2e"]):
        cmd.append(url)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace"
        )
        duration = (datetime.now() - start_time).total_seconds()
        passed = result.returncode == 0

        if passed:
            print_success(f"{name}: PASSED ({duration:.1f}s)")
        else:
            print_error(f"{name}: FAILED ({duration:.1f}s)")
            if result.stderr:
                err_preview = result.stderr.strip()[:200]
                print(f"  Error: {err_preview}")

        return {
            "name": name,
            "passed": passed,
            "output": result.stdout,
            "error": result.stderr,
            "skipped": False,
            "duration": duration
        }

    except subprocess.TimeoutExpired:
        duration = (datetime.now() - start_time).total_seconds()
        print_error(f"{name}: TIMEOUT (>{duration:.0f}s)")
        return {
            "name": name,
            "passed": False,
            "output": "",
            "error": f"Timeout after {timeout}s",
            "skipped": False,
            "duration": duration
        }

    except Exception as e:
        duration = (datetime.now() - start_time).total_seconds()
        print_error(f"{name}: ERROR - {str(e)}")
        return {
            "name": name,
            "passed": False,
            "output": "",
            "error": str(e),
            "skipped": False,
            "duration": duration
        }


def load_manifest(manifest_path: Optional[Path] = None) -> Optional[Dict[str, Any]]:
    """Load skills_manifest.json with standard path fallback."""
    if not manifest_path:
        base_dir = Path(__file__).resolve().parent.parent
        manifest_path = base_dir / "skills_manifest.json"

    if manifest_path.exists():
        try:
            return json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            return None
    return None
