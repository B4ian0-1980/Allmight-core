#!/usr/bin/env python3
"""
Antigravity Agent CLI — Unified Operations Runner
==================================================
Unified operational entrypoint for the Antigravity Cognitive Operating System.
Orchestrates healthchecks, checklists, preview servers, session analytics, and skills inspection.

Usage:
    python .agent/scripts/agent-cli.py healthcheck [--skills|--agents|--json]
    python .agent/scripts/agent-cli.py checklist [path] [--full] [--url URL]
    python .agent/scripts/agent-cli.py preview {start|stop|status} [port]
    python .agent/scripts/agent-cli.py session {status|info} [path]
    python .agent/scripts/agent-cli.py update [--skill NAME] [--limit N]
    python .agent/scripts/agent-cli.py skills list [--status READY|PLAYBOOK|BLOCKED|BROKEN]
    python .agent/scripts/agent-cli.py skills show <skill-name>
"""

import sys
import os
import json
import argparse
from pathlib import Path
from typing import Optional

SCRIPT_DIR = Path(__file__).resolve().parent
AGENT_DIR = SCRIPT_DIR.parent

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _common import Colors, print_header, print_step, print_success, print_warning, print_error, load_manifest


def cmd_healthcheck(args):
    import healthcheck
    sys.argv = ["healthcheck.py"]
    if args.skills: sys.argv.append("--skills")
    if args.agents: sys.argv.append("--agents")
    if args.json: sys.argv.append("--json")
    healthcheck.main()


def cmd_checklist(args):
    import checklist
    sys.argv = ["checklist.py", args.project]
    if args.url: sys.argv.extend(["--url", args.url])
    if args.full: sys.argv.append("--full")
    if args.stop_on_fail: sys.argv.append("--stop-on-fail")
    if args.json: sys.argv.append("--json")
    checklist.main()


def cmd_preview(args):
    import auto_preview
    if args.action == "start":
        auto_preview.start_server(int(args.port))
    elif args.action == "stop":
        auto_preview.stop_server()
    elif args.action == "status":
        auto_preview.status_server()


def cmd_session(args):
    import session_manager
    sys.argv = ["session_manager.py", args.action, args.path]
    session_manager.main()


def cmd_update(args):
    import updater
    sys.argv = ["updater.py"]
    if args.skill: sys.argv.extend(["--skill", args.skill])
    if args.limit: sys.argv.extend(["--limit", str(args.limit)])
    updater.main()


def cmd_skills(args):
    manifest = load_manifest(AGENT_DIR / "skills_manifest.json")
    if not manifest or "skills" not in manifest:
        print_error("Manifest skills_manifest.json not found. Run 'agent-cli healthcheck' first.")
        return

    skills = manifest["skills"]

    if args.subcommand == "list":
        filter_status = args.status.upper() if args.status else None
        print_header("SKILLS CATALOG AUDIT", width=74)
        print(f"{'Skill Name':<32} | {'Status':<10} | {'Tokens':>7} | {'Scripts':>8}")
        print("-" * 74)

        for name, data in sorted(skills.items()):
            status = data.get("status", "UNKNOWN")
            if filter_status and status != filter_status:
                continue

            color = Colors.GREEN if status == "READY" else (
                Colors.BLUE if status == "PLAYBOOK" else (
                    Colors.YELLOW if status == "BLOCKED" else Colors.RED
                )
            )

            tok = data.get("tokens", 0)
            script_count = len(data.get("scripts", []))
            print(f"{name:<32} | {color}{status:<10}{Colors.ENDC} | {tok:>7,d} | {script_count:>8d}")

        print("-" * 74)
        print(f"Total shown: {len([s for s in skills.values() if not filter_status or s.get('status') == filter_status])}\n")

    elif args.subcommand == "show":
        skill_name = args.skill
        if skill_name not in skills:
            print_error(f"Skill '{skill_name}' not found in manifest.")
            return

        skill_md = AGENT_DIR / "skills" / skill_name / "SKILL.md"
        if not skill_md.exists():
            print_error(f"SKILL.md not found for '{skill_name}' at {skill_md}")
            return

        print_header(f"SKILL: {skill_name.upper()}", width=74)
        print(skill_md.read_text(encoding="utf-8", errors="replace"))


def cmd_sync(args):
    import healthcheck
    import sync_architecture
    import sync_painel

    print_header("ANTIGRAVITY AUTOMATED ECOSYSTEM SYNC", width=74)

    print_step("Passo 1/3: Auditando integridade e recalculando tokens (Healthcheck)...")
    sys.argv = ["healthcheck.py"]
    healthcheck.main()

    print_step("Passo 2/3: Sincronizando inventario e documentacao (ARCHITECTURE.md)...")
    sys.argv = ["sync_architecture.py"]
    sync_architecture.main()

    print_step("Passo 3/3: Reconstruindo painel de controle web (painel_sistema.html)...")
    sys.argv = ["sync_painel.py"]
    sync_painel.main()

    print_success("Sincronizacao 100% concluida! O sistema esta totalmente atualizado.")


def main():
    parser = argparse.ArgumentParser(
        prog="agent-cli",
        description="Antigravity Unified Operations Runner"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 1. healthcheck
    p_health = subparsers.add_parser("healthcheck", help="Run system healthcheck & token auditor")
    p_health.add_argument("--skills", action="store_true", help="Audit only skills")
    p_health.add_argument("--agents", action="store_true", help="Audit only agents")
    p_health.add_argument("--json", action="store_true", help="Output JSON")

    # 2. checklist / audit
    p_check = subparsers.add_parser("checklist", help="Run project validation checklist")
    p_check.add_argument("project", nargs="?", default=".", help="Project path")
    p_check.add_argument("--full", action="store_true", help="Run full suite")
    p_check.add_argument("--url", help="URL for Lighthouse / E2E")
    p_check.add_argument("--stop-on-fail", action="store_true", help="Stop on first error")
    p_check.add_argument("--json", action="store_true", help="Output JSON")

    # 3. preview
    p_prev = subparsers.add_parser("preview", help="Manage development preview server")
    p_prev.add_argument("action", choices=["start", "stop", "status"])
    p_prev.add_argument("port", nargs="?", default="3000")

    # 4. session
    p_sess = subparsers.add_parser("session", help="Session & tech stack manager")
    p_sess.add_argument("action", choices=["status", "info"])
    p_sess.add_argument("path", nargs="?", default=".")

    # 5. update
    p_upd = subparsers.add_parser("update", help="Audit upstream repository updates")
    p_upd.add_argument("--skill", help="Check specific skill")
    p_upd.add_argument("--limit", type=int, default=15, help="Limit remote checks")

    # 6. skills
    p_skills = subparsers.add_parser("skills", help="Inspect skills catalog and playbooks")
    sub_skills = p_skills.add_subparsers(dest="subcommand", required=True)
    p_list = sub_skills.add_parser("list", help="List registered skills")
    p_list.add_argument("--status", choices=["READY", "PLAYBOOK", "BLOCKED", "BROKEN"], help="Filter by status")
    p_show = sub_skills.add_parser("show", help="Display SKILL.md for a skill")
    p_show.add_argument("skill", help="Name of skill to inspect")

    # 7. sync
    p_sync = subparsers.add_parser("sync", help="One-click full sync (Healthcheck + Architecture + Painel)")

    args = parser.parse_args()

    if args.command == "healthcheck":
        cmd_healthcheck(args)
    elif args.command == "checklist":
        cmd_checklist(args)
    elif args.command == "preview":
        cmd_preview(args)
    elif args.command == "session":
        cmd_session(args)
    elif args.command == "update":
        cmd_update(args)
    elif args.command == "skills":
        cmd_skills(args)
    elif args.command == "sync":
        cmd_sync(args)


if __name__ == "__main__":
    main()
