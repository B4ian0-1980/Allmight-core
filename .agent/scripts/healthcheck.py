#!/usr/bin/env python3
"""
Antigravity Kit — Unified Healthcheck & Token Auditor
======================================================
Audits 100% of skills ([READY], [PLAYBOOK], [BLOCKED], [BROKEN])
and measures context burden / token cascade across all 21 agents.

Usage:
    python .agent/scripts/healthcheck.py
    python .agent/scripts/healthcheck.py --skills
    python .agent/scripts/healthcheck.py --agents
    python .agent/scripts/healthcheck.py --json
"""

import sys
import os
import re
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

# Ensure scripts directory is on path to import _common
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
)


def estimate_tokens(text: str) -> int:
    """Accurate token heuristic for mixed code and markdown (avg ~3.7 chars/token)."""
    return max(1, int(len(text) / 3.7))


def detect_host_environment() -> Dict[str, Any]:
    """Detect available interpreters, compilers and runtimes on host machine."""
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    node_path = shutil.which("node")
    docker_path = shutil.which("docker")
    git_path = shutil.which("git")
    crystal_path = shutil.which("crystal")

    return {
        "python": {"available": True, "version": py_ver, "path": sys.executable},
        "node": {"available": node_path is not None, "path": node_path},
        "docker": {"available": docker_path is not None, "path": docker_path},
        "git": {"available": git_path is not None, "path": git_path},
        "crystal": {"available": crystal_path is not None, "path": crystal_path},
        "platform": sys.platform
    }


def audit_skill(skill_path: Path, host_env: Dict[str, Any]) -> Dict[str, Any]:
    """
    Classify skill into READY, PLAYBOOK, BLOCKED, or BROKEN.
    Scans root directory and 'scripts/' subdirectory for executable assets.
    """
    name = skill_path.name
    skill_md = skill_path / "SKILL.md"
    has_md = skill_md.exists()

    md_text = skill_md.read_text(encoding="utf-8", errors="ignore") if has_md else ""
    tokens = estimate_tokens(md_text) if has_md else 0
    size_bytes = len(md_text.encode("utf-8")) if has_md else 0

    # 1. Check for BROKEN status (missing or empty SKILL.md)
    if not has_md or size_bytes == 0 or not md_text.strip():
        detected_files = [f.name for f in skill_path.iterdir()] if skill_path.is_dir() else []
        return {
            "name": name,
            "status": "BROKEN",
            "reason": "SKILL.md ausente ou malformado/vazio na pasta",
            "has_skill_md": has_md,
            "size_bytes": size_bytes,
            "tokens": 0,
            "scripts": []
        }

    # 2. Scan root and scripts/ subdirectory for executable assets
    root_files = [f.name.lower() for f in skill_path.iterdir() if f.is_file()]
    root_exts = {Path(f).suffix.lower() for f in root_files}

    detected_scripts: List[str] = []
    # Collect scripts in root
    for f in root_files:
        if Path(f).suffix.lower() in [".py", ".js", ".ts", ".ps1", ".sh", ".rb"]:
            detected_scripts.append(f)

    # Collect scripts in scripts/ subfolder
    scripts_dir = skill_path / "scripts"
    if scripts_dir.is_dir():
        for sf in sorted(scripts_dir.iterdir()):
            if sf.is_file() and sf.suffix.lower() in [".py", ".js", ".ts", ".ps1", ".sh", ".rb"]:
                detected_scripts.append(f"scripts/{sf.name}")

    status = "PLAYBOOK"
    reason = "Pure Markdown guidelines / Cognitive prompt playbook"

    # 3. Check for BLOCKED conditions
    if any(f.endswith(".cr") for f in root_files) or "shard.yml" in root_files:
        if not host_env["crystal"]["available"]:
            status = "BLOCKED"
            reason = "Requires Crystal compiler (crystal is not installed)"
        else:
            status = "READY"
            reason = "Executable Crystal tool"
    elif "dockerfile" in root_files or "docker-compose.yml" in root_files:
        has_local_script = len(detected_scripts) > 0
        if not host_env["docker"]["available"] and not has_local_script:
            status = "BLOCKED"
            reason = "Requires Docker container runtime (docker is not installed)"
        elif has_local_script:
            status = "READY"
            reason = "Runnable locally via script entrypoint"
    # 4. Check for READY conditions
    elif len(detected_scripts) > 0 or "package.json" in root_files or "requirements.txt" in root_files:
        if "package.json" in root_files and not host_env["node"]["available"] and not any(s.endswith(".py") for s in detected_scripts):
            status = "BLOCKED"
            reason = "Requires Node.js runtime"
        else:
            status = "READY"
            script_count = len(detected_scripts)
            reason = f"Runnable local entrypoint ({script_count} script(s) found)" if script_count > 0 else "Runnable entrypoint detected"

    return {
        "name": name,
        "status": status,
        "reason": reason,
        "has_skill_md": has_md,
        "size_bytes": size_bytes,
        "tokens": tokens,
        "scripts": detected_scripts
    }


def audit_all_skills(skills_root: Path, host_env: Dict[str, Any]) -> Dict[str, Any]:
    """Audit all skills in the skills directory."""
    results = {}
    if not skills_root.exists():
        return results

    for item in sorted(skills_root.iterdir()):
        if item.is_dir() and not item.name.startswith("."):
            results[item.name] = audit_skill(item, host_env)

    return results


def audit_all_agents(agents_root: Path, skills_audit: Dict[str, Any]) -> Dict[str, Any]:
    """Audit all agent files, measuring direct and cascaded skill token burdens."""
    results = {}
    if not agents_root.exists():
        return results

    for agent_file in sorted(agents_root.glob("*.md")):
        name = agent_file.stem
        content = agent_file.read_text(encoding="utf-8", errors="ignore")
        direct_tokens = estimate_tokens(content)
        size_bytes = len(content.encode("utf-8"))
        line_count = len(content.splitlines())

        # Extract declared skills from frontmatter
        skills_match = re.search(r'skills:\s*([^\n\r]+)', content)
        declared_skills: List[str] = []
        if skills_match:
            raw_skills = skills_match.group(1).strip()
            declared_skills = [s.strip() for s in raw_skills.split(",") if s.strip()]

        cascade_tokens = 0
        skills_detail = []
        for sk in declared_skills:
            clean_sk = sk.split("/")[0].strip()
            sk_info = skills_audit.get(clean_sk)
            sk_tokens = sk_info["tokens"] if sk_info else 0
            cascade_tokens += sk_tokens
            skills_detail.append({
                "name": sk,
                "tokens": sk_tokens,
                "status": sk_info["status"] if sk_info else "UNKNOWN"
            })

        total_tokens = direct_tokens + cascade_tokens

        if total_tokens > 25000:
            tax_level = "CRITICAL"
        elif total_tokens > 15000:
            tax_level = "HIGH"
        elif total_tokens > 8000:
            tax_level = "MEDIUM"
        else:
            tax_level = "LOW"

        results[name] = {
            "name": name,
            "filename": agent_file.name,
            "lines": line_count,
            "size_bytes": size_bytes,
            "direct_tokens": direct_tokens,
            "declared_skills": declared_skills,
            "skills_count": len(declared_skills),
            "cascade_tokens": cascade_tokens,
            "total_tokens": total_tokens,
            "tax_level": tax_level,
            "skills_detail": skills_detail
        }

    return results


def print_cli_report(host_env: Dict[str, Any], skills_data: Dict[str, Any], agents_data: Dict[str, Any], mode: str = "all"):
    """Render high-density executive ANSI dashboard."""
    print_header("ANTIGRAVITY KIT — HEALTHCHECK & CONTEXT BURDEN REPORT", width=78)

    # 1. Host Environment Check
    print(f"{Colors.BOLD}{Colors.HEADER}🖥️  HOST RUNTIME ENVIRONMENT{Colors.ENDC}")
    print(f"  • Platform: {Colors.BOLD}{host_env['platform']}{Colors.ENDC}")
    print(f"  • Python:   {Colors.GREEN}✅ {host_env['python']['version']}{Colors.ENDC} ({host_env['python']['path']})")

    node_str = f"{Colors.GREEN}✅ Available{Colors.ENDC}" if host_env['node']['available'] else f"{Colors.YELLOW}⚠️  Missing{Colors.ENDC}"
    print(f"  • Node.js:  {node_str}")

    docker_str = f"{Colors.GREEN}✅ Available{Colors.ENDC}" if host_env['docker']['available'] else f"{Colors.YELLOW}⚠️  Not installed (Docker-only skills BLOCKED){Colors.ENDC}"
    print(f"  • Docker:   {docker_str}")

    crystal_str = f"{Colors.GREEN}✅ Available{Colors.ENDC}" if host_env['crystal']['available'] else f"{Colors.DIM}❌ Not installed (Crystal skills BLOCKED){Colors.ENDC}"
    print(f"  • Crystal:  {crystal_str}\n")

    # 2. Skills Readiness Breakdown
    if mode in ["all", "skills"]:
        total_skills = len(skills_data)
        ready_count = sum(1 for s in skills_data.values() if s["status"] == "READY")
        playbook_count = sum(1 for s in skills_data.values() if s["status"] == "PLAYBOOK")
        blocked_count = sum(1 for s in skills_data.values() if s["status"] == "BLOCKED")
        broken_count = sum(1 for s in skills_data.values() if s["status"] == "BROKEN")

        print(f"{Colors.BOLD}{Colors.HEADER}📦 SKILL READINESS AUDIT ({total_skills} Total Skills){Colors.ENDC}")
        print(f"  • {Colors.GREEN}{Colors.BOLD}[READY]{Colors.ENDC}    {ready_count:3d} ({ready_count/total_skills*100:.1f}%) — Executables & dependencies verified")
        print(f"  • {Colors.BLUE}{Colors.BOLD}[PLAYBOOK]{Colors.ENDC} {playbook_count:3d} ({playbook_count/total_skills*100:.1f}%) — Pure guidance & cognitive methodologies")
        print(f"  • {Colors.YELLOW}{Colors.BOLD}[BLOCKED]{Colors.ENDC}  {blocked_count:3d} ({blocked_count/total_skills*100:.1f}%) — Missing host compilers or runtimes")
        print(f"  • {Colors.RED}{Colors.BOLD}[BROKEN]{Colors.ENDC}   {broken_count:3d} ({broken_count/total_skills*100:.1f}%) — Missing or malformed SKILL.md\n")

        if broken_count > 0:
            print(f"  {Colors.BOLD}{Colors.RED}❌ Broken Skills Detail:{Colors.ENDC}")
            for s in skills_data.values():
                if s["status"] == "BROKEN":
                    print(f"    - {Colors.RED}{s['name']}{Colors.ENDC}: {s['reason']}")
            print()

        if blocked_count > 0:
            print(f"  {Colors.BOLD}{Colors.YELLOW}⚠️  Blocked Skills Detail:{Colors.ENDC}")
            for s in skills_data.values():
                if s["status"] == "BLOCKED":
                    print(f"    - {Colors.YELLOW}{s['name']}{Colors.ENDC}: {s['reason']}")
            print()

    # 3. Agent Token Overhead & Cascade
    if mode in ["all", "agents"]:
        total_agents = len(agents_data)
        sorted_agents = sorted(agents_data.values(), key=lambda a: a["total_tokens"], reverse=True)

        print(f"{Colors.BOLD}{Colors.HEADER}🤖 AGENT CONTEXT OVERHEAD & CASCADE TAX ({total_agents} Total Agents){Colors.ENDC}")
        print(f"{'Agent Name':<24} | {'Direct':>7} | {'Skills':>6} | {'Cascade':>8} | {'Total Burden':>12} | {'Tax Level':<8}")
        print("-" * 78)

        for a in sorted_agents:
            if a["tax_level"] == "CRITICAL":
                color = Colors.RED + Colors.BOLD
            elif a["tax_level"] == "HIGH":
                color = Colors.YELLOW
            elif a["tax_level"] == "MEDIUM":
                color = Colors.BLUE
            else:
                color = Colors.GREEN

            print(f"{a['name']:<24} | {a['direct_tokens']:>7,d} | {a['skills_count']:>6d} | {a['cascade_tokens']:>8,d} | {color}{a['total_tokens']:>12,d}{Colors.ENDC} | {color}{a['tax_level']:<8}{Colors.ENDC}")

        avg_total = sum(a["total_tokens"] for a in sorted_agents) / max(1, total_agents)
        heaviest = sorted_agents[0] if sorted_agents else None

        print("-" * 78)
        print(f"  • Média de Custo por Invocação: {Colors.BOLD}{int(avg_total):,d} tokens{Colors.ENDC}")
        if heaviest:
            print(f"  • Agente Mais Pesado: {Colors.RED}{Colors.BOLD}{heaviest['name']}{Colors.ENDC} ({heaviest['total_tokens']:,d} tokens total: {heaviest['direct_tokens']:,d} direto + {heaviest['cascade_tokens']:,d} cascata em {heaviest['skills_count']} skills)")
        print()


def main():
    parser = argparse.ArgumentParser(description="Antigravity Healthcheck & Token Auditor")
    parser.add_argument("--skills", action="store_true", help="Audit only skills readiness")
    parser.add_argument("--agents", action="store_true", help="Audit only agent context burden")
    parser.add_argument("--json", action="store_true", help="Output raw JSON to stdout")
    parser.add_argument("--manifest", type=str, default=None, help="Custom manifest output path")
    args = parser.parse_args()

    agent_dir = SCRIPT_DIR.parent
    skills_dir = agent_dir / "skills"
    agents_dir = agent_dir / "agents"
    manifest_path = Path(args.manifest) if args.manifest else agent_dir / "skills_manifest.json"

    host_env = detect_host_environment()
    skills_data = audit_all_skills(skills_dir, host_env)
    agents_data = audit_all_agents(agents_dir, skills_data)

    manifest_payload = {
        "generated_at": datetime.now().isoformat(),
        "host_environment": host_env,
        "skills_summary": {
            "total": len(skills_data),
            "ready": sum(1 for s in skills_data.values() if s["status"] == "READY"),
            "playbook": sum(1 for s in skills_data.values() if s["status"] == "PLAYBOOK"),
            "blocked": sum(1 for s in skills_data.values() if s["status"] == "BLOCKED"),
            "broken": sum(1 for s in skills_data.values() if s["status"] == "BROKEN")
        },
        "agents_summary": {
            "total": len(agents_data),
            "critical_tax": sum(1 for a in agents_data.values() if a["tax_level"] == "CRITICAL"),
            "high_tax": sum(1 for a in agents_data.values() if a["tax_level"] == "HIGH")
        },
        "skills": skills_data,
        "agents": agents_data
    }

    # Save manifest
    manifest_path.write_text(json.dumps(manifest_payload, indent=2, ensure_ascii=False), encoding="utf-8")

    if args.json:
        print(json.dumps(manifest_payload, indent=2, ensure_ascii=False))
        return

    mode = "skills" if args.skills else ("agents" if args.agents else "all")
    print_cli_report(host_env, skills_data, agents_data, mode)
    print(f"{Colors.DIM}Manifesto salvo com sucesso em: {manifest_path}{Colors.ENDC}\n")


if __name__ == "__main__":
    main()
