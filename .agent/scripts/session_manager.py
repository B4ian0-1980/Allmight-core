#!/usr/bin/env python3
"""
Session Manager — Antigravity Kit
=================================
Analyzes project state, detects tech stack (Node, Python, Flutter, PHP),
tracks file statistics, and provides a structured project overview.

Usage:
    python .agent/scripts/session_manager.py status [path]
    python .agent/scripts/session_manager.py info [path]
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import Dict, Any, List

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _common import Colors, print_header


def get_project_root(path: str) -> Path:
    return Path(path).resolve()


def analyze_tech_stack(root: Path) -> Dict[str, Any]:
    """
    Detect multi-ecosystem tech stacks: Node.js, Python, Flutter, and PHP.
    """
    stack = []
    runtimes = []
    scripts = []
    project_name = root.name
    version = "0.0.0"

    # 1. Node.js detection (package.json)
    pkg_file = root / "package.json"
    if pkg_file.exists():
        try:
            with open(pkg_file, 'r', encoding='utf-8') as f:
                pkg_data = json.load(f)
            project_name = pkg_data.get("name", project_name)
            version = pkg_data.get("version", version)
            scripts = list(pkg_data.get("scripts", {}).keys())
            runtimes.append("Node.js")

            all_deps = {**pkg_data.get("dependencies", {}), **pkg_data.get("devDependencies", {})}
            if "next" in all_deps: stack.append("Next.js")
            elif "react" in all_deps: stack.append("React")
            elif "vue" in all_deps: stack.append("Vue")
            elif "svelte" in all_deps: stack.append("Svelte")
            elif "express" in all_deps: stack.append("Express")
            elif "nestjs" in all_deps or "@nestjs/core" in all_deps: stack.append("NestJS")

            if "tailwindcss" in all_deps: stack.append("Tailwind CSS")
            if "prisma" in all_deps: stack.append("Prisma")
            if "typescript" in all_deps: stack.append("TypeScript")
        except Exception:
            pass

    # 2. Python detection (requirements.txt, pyproject.toml, Pipfile, setup.py)
    py_files = ["requirements.txt", "pyproject.toml", "Pipfile", "setup.py"]
    has_py = any((root / pf).exists() for pf in py_files)
    if has_py:
        runtimes.append("Python")
        py_content = ""
        for pf in py_files:
            p = root / pf
            if p.exists():
                try:
                    py_content += " " + p.read_text(encoding="utf-8", errors="ignore").lower()
                except Exception:
                    pass

        if "fastapi" in py_content or "uvicorn" in py_content: stack.append("FastAPI")
        if "django" in py_content: stack.append("Django")
        if "flask" in py_content: stack.append("Flask")
        if "streamlit" in py_content: stack.append("Streamlit")
        if "sqlalchemy" in py_content: stack.append("SQLAlchemy")
        if "pydantic" in py_content: stack.append("Pydantic")
        if "torch" in py_content: stack.append("PyTorch")

        if not any(fw in stack for fw in ["FastAPI", "Django", "Flask", "Streamlit"]):
            stack.append("Python Standard")

    # 3. Flutter / Dart detection (pubspec.yaml)
    pubspec = root / "pubspec.yaml"
    if pubspec.exists():
        runtimes.append("Flutter / Dart")
        try:
            pub_text = pubspec.read_text(encoding="utf-8", errors="ignore").lower()
            name_m = re.search(r'name:\s*([^\s\n]+)', pub_text)
            if name_m:
                project_name = name_m.group(1)
            stack.append("Flutter")
            if "riverpod" in pub_text: stack.append("Riverpod")
            elif "flutter_bloc" in pub_text or "bloc" in pub_text: stack.append("Bloc")
            elif "provider" in pub_text: stack.append("Provider")
        except Exception:
            pass

    # 4. PHP detection (composer.json, index.php)
    composer = root / "composer.json"
    if composer.exists() or (root / "index.php").exists():
        runtimes.append("PHP")
        if composer.exists():
            try:
                comp_text = composer.read_text(encoding="utf-8", errors="ignore").lower()
                if "laravel/framework" in comp_text: stack.append("Laravel")
                elif "symfony/framework-bundle" in comp_text: stack.append("Symfony")
                else: stack.append("PHP Modern")
            except Exception:
                stack.append("PHP")
        else:
            stack.append("PHP Native")

    return {
        "name": project_name,
        "version": version,
        "runtimes": list(set(runtimes)),
        "stack": list(set(stack)) if stack else ["Generic"],
        "scripts": scripts
    }


def count_files(root: Path) -> Dict[str, int]:
    stats = {"total": 0}
    exclude = {".git", "node_modules", ".next", "dist", "build", ".agent", ".gemini", "__pycache__", "vendor"}

    for root_dir, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in exclude]
        stats["total"] += len(files)

    return stats


def detect_features(root: Path) -> List[str]:
    features = []
    for cand in ["src", "lib", "app"]:
        search_dir = root / cand
        if search_dir.exists() and search_dir.is_dir():
            for child in search_dir.iterdir():
                if child.is_dir() and not child.name.startswith("."):
                    features.append(child.name)
    return features[:12]


def print_status(root: Path):
    info = analyze_tech_stack(root)
    stats = count_files(root)
    features = detect_features(root)

    print_header("PROJECT SESSION OVERVIEW", width=60)
    print(f"📁 Project:   {Colors.BOLD}{info['name']}{Colors.ENDC} (v{info['version']})")
    print(f"📂 Path:      {root}")
    print(f"🏷️  Runtimes:  {', '.join(info['runtimes']) if info['runtimes'] else 'None detected'}")
    print(f"🔧 Stack:     {Colors.CYAN}{', '.join(info['stack'])}{Colors.ENDC}")
    print(f"📄 Files:     {stats['total']:,d} tracked source files")

    print(f"\n{Colors.BOLD}Detected Architecture Modules ({len(features)}):{Colors.ENDC}")
    if features:
        for feat in features:
            print(f"   • {feat}")
    else:
        print("   (No top-level src/lib/app modules detected)")
    print()


def main():
    parser = argparse.ArgumentParser(description="Session Manager")
    parser.add_argument("command", choices=["status", "info"], help="Command to run")
    parser.add_argument("path", nargs="?", default=".", help="Project path")

    args = parser.parse_args()
    root = get_project_root(args.path)

    if args.command == "status":
        print_status(root)
    elif args.command == "info":
        info = analyze_tech_stack(root)
        info["stats"] = count_files(root)
        info["modules"] = detect_features(root)
        print(json.dumps(info, indent=2))


if __name__ == "__main__":
    main()
