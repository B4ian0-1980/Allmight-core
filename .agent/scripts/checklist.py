#!/usr/bin/env python3
"""
Master Checklist & Verification Suite — Antigravity Kit
=======================================================
Orchestrates project validation scripts in priority order.
Combines fast incremental checks with full pre-deployment verification.

Usage:
    python .agent/scripts/checklist.py .                      # Core validation
    python .agent/scripts/checklist.py . --full               # Full suite (all categories)
    python .agent/scripts/checklist.py . --url <URL>          # Core + Performance checks
    python .agent/scripts/checklist.py . --full --url <URL>   # Full suite + Perf + E2E
"""

import sys
import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

# Ensure scripts directory is in sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _common import (
    Colors,
    print_header,
    print_step,
    print_success,
    print_warning,
    print_error,
    run_script,
    load_manifest,
)

# Canonical check definitions: (category, check_name, skill_name, script_filename, is_required, full_only, requires_url)
SUITE_CHECKS = [
    # P0: Security (CRITICAL)
    ("Security", "Security Scan", "vulnerability-scanner", "security_scan.py", True, False, False),
    ("Security", "Dependency Analysis", "vulnerability-scanner", "dependency_analyzer.py", False, True, False),
    # P1: Code Quality (CRITICAL)
    ("Code Quality", "Lint Check", "lint-and-validate", "lint_runner.py", True, False, False),
    ("Code Quality", "Type Coverage", "lint-and-validate", "type_coverage.py", False, True, False),
    # P2: Data Layer
    ("Data Layer", "Schema Validation", "database-design", "schema_validator.py", False, False, False),
    # P3: Testing
    ("Testing", "Test Suite", "testing-patterns", "test_runner.py", False, False, False),
    # P4: UX & Accessibility
    ("UX & Accessibility", "UX Audit", "frontend-design", "ux_audit.py", False, False, False),
    ("UX & Accessibility", "Accessibility Check", "frontend-design", "accessibility_checker.py", False, True, False),
    # P5: SEO & Content
    ("SEO & Content", "SEO Check", "seo-fundamentals", "seo_checker.py", False, False, False),
    ("SEO & Content", "GEO Check", "geo-fundamentals", "geo_checker.py", False, True, False),
    # P6: Performance (requires URL)
    ("Performance", "Lighthouse Audit", "performance-profiling", "lighthouse_audit.py", True, False, True),
    ("Performance", "Bundle Analysis", "performance-profiling", "bundle_analyzer.py", False, True, False),
    # P7: E2E Testing (requires URL)
    ("E2E Testing", "Playwright E2E", "webapp-testing", "playwright_runner.py", False, True, True),
    # P8: Mobile
    ("Mobile", "Mobile Audit", "mobile-design", "mobile_audit.py", False, True, False),
    # P9: Internationalization
    ("Internationalization", "i18n Check", "i18n-localization", "i18n_checker.py", False, True, False),
]


def resolve_check_script(skill_name: str, script_file: str, agent_dir: Path, manifest: Optional[Dict[str, Any]]) -> Optional[Path]:
    """
    Resolve path to script using skills_manifest.json metadata if available,
    falling back to conventional folder structure.
    """
    skill_dir = agent_dir / "skills" / skill_name

    # 1. Look in manifest registered scripts
    if manifest and "skills" in manifest and skill_name in manifest["skills"]:
        sk_info = manifest["skills"][skill_name]
        registered_scripts = sk_info.get("scripts", [])
        for reg in registered_scripts:
            if reg.endswith(script_file) or reg == script_file:
                target = skill_dir / reg
                if target.exists():
                    return target

    # 2. Fallback to standard convention
    candidate1 = skill_dir / "scripts" / script_file
    if candidate1.exists():
        return candidate1

    candidate2 = skill_dir / script_file
    if candidate2.exists():
        return candidate2

    return candidate1  # Return default path even if missing for standard warning logging


def print_summary_report(results: List[Dict[str, Any]], start_time: datetime, full_mode: bool) -> bool:
    """Print high-density summary report of all checks executed."""
    total_duration = (datetime.now() - start_time).total_seconds()
    mode_label = "FULL VERIFICATION REPORT" if full_mode else "CHECKLIST SUMMARY"
    print_header(f"📊 {mode_label}")

    total = len(results)
    passed = sum(1 for r in results if r["passed"] and not r.get("skipped"))
    failed = sum(1 for r in results if not r["passed"] and not r.get("skipped"))
    skipped = sum(1 for r in results if r.get("skipped"))

    print(f"Total Duration: {total_duration:.1f}s | Total Checks: {total}")
    print(f"{Colors.GREEN}✅ Passed: {passed}{Colors.ENDC} | {Colors.RED}❌ Failed: {failed}{Colors.ENDC} | {Colors.YELLOW}⏭️  Skipped: {skipped}{Colors.ENDC}\n")

    current_cat = None
    for r in results:
        if r.get("category") and r["category"] != current_cat:
            current_cat = r["category"]
            print(f"\n{Colors.BOLD}{Colors.CYAN}[{current_cat}]{Colors.ENDC}")

        if r.get("skipped"):
            icon = f"{Colors.YELLOW}⏭️ {Colors.ENDC}"
        elif r["passed"]:
            icon = f"{Colors.GREEN}✅{Colors.ENDC}"
        else:
            icon = f"{Colors.RED}❌{Colors.ENDC}"

        dur_str = f"({r.get('duration', 0):.1f}s)" if not r.get("skipped") else "(not found)"
        print(f"  {icon} {r['name']:<24} {dur_str}")

    print()
    if failed > 0:
        print_error(f"{failed} check(s) FAILED — review errors before proceeding")
        return False
    else:
        print_success("All executed checks PASSED ✨")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Antigravity Kit — Master Checklist & Verification Suite",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("project", nargs="?", default=".", help="Project path to validate (default: .)")
    parser.add_argument("--url", help="URL for performance (Lighthouse) and E2E checks")
    parser.add_argument("--full", action="store_true", help="Run full suite including extended checks (SEO/GEO, Mobile, i18n)")
    parser.add_argument("--skip-performance", action="store_true", help="Skip performance checks even if URL provided")
    parser.add_argument("--no-e2e", action="store_true", help="Skip Playwright E2E checks")
    parser.add_argument("--stop-on-fail", action="store_true", help="Stop execution immediately on first failure")
    parser.add_argument("--json", action="store_true", help="Output summary in JSON format")

    args = parser.parse_args()
    project_path = Path(args.project).resolve()

    if not project_path.exists():
        print_error(f"Project path does not exist: {project_path}")
        sys.exit(1)

    agent_dir = SCRIPT_DIR.parent
    manifest = load_manifest(agent_dir / "skills_manifest.json")

    start_time = datetime.now()
    results = []

    suite_name = "FULL VERIFICATION SUITE" if args.full else "MASTER CHECKLIST"
    print_header(f"🚀 ANTIGRAVITY KIT — {suite_name}")
    print(f"Target Project: {project_path}")
    print(f"Target URL:     {args.url if args.url else 'Not provided'}")
    print(f"Mode:           {'FULL (--full)' if args.full else 'CORE (run with --full for complete suite)'}")
    print(f"Manifest:       {'Loaded' if manifest else 'Not found (using disk fallback)'}\n")

    for cat, name, skill, script_name, req, full_only, req_url in SUITE_CHECKS:
        # Filter checks based on flags
        if full_only and not args.full:
            continue
        if req_url and not args.url:
            continue
        if req_url and args.skip_performance and "lighthouse" in script_name.lower():
            continue
        if req_url and args.no_e2e and "playwright" in script_name.lower():
            continue

        script_path = resolve_check_script(skill, script_name, agent_dir, manifest)
        res = run_script(name, script_path, str(project_path), url=args.url)
        res["category"] = cat
        res["required"] = req
        results.append(res)

        # Halt immediately if required check fails or --stop-on-fail is set
        if not res["passed"] and not res.get("skipped"):
            if req or args.stop_on_fail:
                print_error(f"CRITICAL STOP: {name} failed.")
                if not args.json:
                    print_summary_report(results, start_time, args.full)
                sys.exit(1)

    if args.json:
        print(json.dumps({
            "timestamp": datetime.now().isoformat(),
            "mode": "full" if args.full else "core",
            "passed": all(r["passed"] for r in results),
            "results": results
        }, indent=2))
        return

    all_passed = print_summary_report(results, start_time, args.full)
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
