#!/usr/bin/env python3
"""
Skills Upstream Update Auditor — Antigravity Kit
================================================
Checks official GitHub repositories for upstream updates without altering files.
Reads repository mappings from skills_github_mapping.json and CATALOGO_SKILLS.md.

Usage:
    python .agent/scripts/updater.py
    python .agent/scripts/updater.py --skill LlamaFactory
    python .agent/scripts/updater.py --limit 10
"""

import os
import sys
import re
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional, Tuple, List

# Ensure scripts directory is on sys.path
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


def load_repository_mappings(agent_dir: Path) -> Dict[str, str]:
    """
    Load upstream GitHub repositories mapped to each skill.
    Combines skills_github_mapping.json, CATALOGO_SKILLS.md, and local frontmatters.
    """
    mappings: Dict[str, str] = {}

    # 1. Try skills_github_mapping.json
    mapping_file = agent_dir / "skills_github_mapping.json"
    if mapping_file.exists():
        try:
            mappings.update(json.loads(mapping_file.read_text(encoding="utf-8")))
        except Exception:
            pass

    # 2. Extract any markdown links from CATALOGO_SKILLS.md
    catalogo_file = agent_dir / "CATALOGO_SKILLS.md"
    if catalogo_file.exists():
        try:
            content = catalogo_file.read_text(encoding="utf-8")
            # Match patterns like: [`skill_name`](...) ... (https://github.com/owner/repo)
            matches = re.findall(
                r'\[`?([a-zA-Z0-9_\-]+)`?\].*?(https?://github\.com/[a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)',
                content
            )
            for skill_name, repo_url in matches:
                if skill_name not in mappings:
                    mappings[skill_name] = repo_url
        except Exception:
            pass

    return mappings


def get_local_skill_date(skill_path: Path) -> str:
    """Retrieve the last modified date of the skill directory / SKILL.md in ISO format."""
    skill_md = skill_path / "SKILL.md"
    target = skill_md if skill_md.exists() else skill_path
    mtime = os.path.getmtime(target)
    return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")


def check_github_latest_commit(repo_url: str, token: Optional[str] = None) -> Tuple[Optional[str], Optional[str]]:
    """
    Query GitHub API for latest commit date of repository.
    Returns (commit_date_iso, error_message).
    """
    clean_url = repo_url.split("/tree/")[0].split("/blob/")[0].rstrip("/")
    match = re.match(r'https?://github\.com/([^/]+)/([^/]+)', clean_url)
    if not match:
        return None, "Invalid GitHub URL"

    owner, repo = match.groups()
    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=1"

    headers = {"User-Agent": "Antigravity-Agent"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            if isinstance(data, list) and len(data) > 0:
                commit_date_str = data[0]["commit"]["author"]["date"]
                return commit_date_str[:10], None
            return None, "No commits returned"
    except urllib.error.HTTPError as e:
        if e.code == 403:
            return None, "Rate limit exceeded (set GITHUB_TOKEN)"
        return None, f"HTTP Error {e.code}"
    except Exception as e:
        return None, str(e)


def main():
    parser = argparse.ArgumentParser(description="Audit upstream updates for Antigravity skills")
    parser.add_argument("--skill", help="Check a specific skill only")
    parser.add_argument("--limit", type=int, default=15, help="Limit number of online checks to prevent rate limits (default: 15)")
    parser.add_argument("--token", help="GitHub Personal Access Token (or set GITHUB_TOKEN env var)")
    args = parser.parse_args()

    agent_dir = SCRIPT_DIR.parent
    skills_dir = agent_dir / "skills"
    token = args.token or os.environ.get("GITHUB_TOKEN")

    print_header("🔍 SKILLS UPSTREAM UPDATE AUDITOR")
    print("Mode: SAFE READ-ONLY (No files will be modified).")
    if token:
        print(f"Auth: {Colors.GREEN}GitHub Token detected (authenticated requests){Colors.ENDC}")
    else:
        print(f"Auth: {Colors.YELLOW}Unauthenticated (Rate limit 60 req/hr. Use GITHUB_TOKEN for more){Colors.ENDC}")
    print()

    mappings = load_repository_mappings(agent_dir)
    skills_to_check = [args.skill] if args.skill else sorted(mappings.keys())

    if args.skill and args.skill not in mappings:
        print_error(f"Skill '{args.skill}' does not have a mapped upstream GitHub repository.")
        sys.exit(1)

    checked_count = 0
    updates_available: List[Dict[str, str]] = []

    for name in skills_to_check:
        if checked_count >= args.limit and not args.skill:
            print(f"\n{Colors.YELLOW}⏸️  Limit of {args.limit} online checks reached. Use --limit N or check individual skills with --skill <name>{Colors.ENDC}")
            break

        repo_url = mappings[name]
        skill_path = skills_dir / name
        local_date = get_local_skill_date(skill_path) if skill_path.exists() else "Not on disk"

        print_step(f"Checking: {name:<28} -> {repo_url}")
        checked_count += 1

        remote_date, err = check_github_latest_commit(repo_url, token)

        if err:
            print_warning(f"  {name}: {err}")
            if "Rate limit" in err and not token:
                print_error("GitHub unauthenticated rate limit reached. Halting checks.")
                break
            continue

        if remote_date:
            if remote_date > local_date:
                print_warning(f"  {name}: UPDATE AVAILABLE (Local: {local_date} | Upstream: {remote_date})")
                updates_available.append({
                    "skill": name,
                    "local_date": local_date,
                    "remote_date": remote_date,
                    "repo_url": repo_url
                })
            else:
                print_success(f"  {name}: Up to date ({local_date})")

    # Summary
    print_header("📊 UPSTREAM UPDATE SUMMARY")
    if not updates_available:
        print_success("All checked skills are up to date with upstream repositories! ✨")
    else:
        print(f"{Colors.BOLD}{Colors.YELLOW}Found {len(updates_available)} skill(s) with newer upstream commits:{Colors.ENDC}\n")
        for u in updates_available:
            print(f"  • {Colors.BOLD}{u['skill']}{Colors.ENDC}")
            print(f"    Local: {u['local_date']} | Upstream: {u['remote_date']}")
            print(f"    Source: {u['repo_url']}\n")
        print(f"{Colors.DIM}To update, review the upstream repository changes before making manual adjustments.{Colors.ENDC}")


if __name__ == "__main__":
    main()
