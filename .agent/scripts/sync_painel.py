#!/usr/bin/env python3
"""
Dashboard Synchronizer — Antigravity Kit
=========================================
Rebuilds painel_sistema.html reading directly from skills_manifest.json,
skills_github_mapping.json, agents/, workflows/, and rules/.

Usage:
    python .agent/scripts/sync_painel.py
"""

import sys
import os
import json
import re
from pathlib import Path
from typing import Dict, Any, List

SCRIPT_DIR = Path(__file__).resolve().parent
AGENT_DIR = SCRIPT_DIR.parent
PAINEL_HTML = AGENT_DIR / "painel_sistema.html"

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _common import Colors, print_header, print_success, print_warning, print_error, load_manifest


def get_tag(name: str, desc: str) -> str:
    nl = name.lower()
    dl = desc.lower()
    if any(k in nl for k in ["claude-red", "offensive", "vulnerability", "security", "pentest", "reverse"]):
        return "Segurança / Pentest"
    elif any(k in nl for k in ["llama", "llm", "ai", "generative", "replicate", "laya", "airllm", "ruflo", "autoharness", "spec-kit"]):
        return "IA & Modelos"
    elif any(k in nl for k in ["video", "motion", "musica", "printer"]):
        return "Multimídia & Vídeo"
    elif any(k in nl for k in ["react", "tailwind", "design", "frontend", "ux", "impeccable", "taste", "image-to-code"]):
        return "Frontend & Design"
    elif any(k in dl for k in ["whatsapp", "wa-", "api", "node", "python", "rust", "database", "backend", "hosting", "server"]):
        return "Backend & Cloud"
    elif any(k in nl for k in ["test", "audit", "debugging", "lint", "code", "ponytail", "playwright"]):
        return "Qualidade & Testes"
    elif any(k in nl for k in ["book", "skill", "graph"]):
        return "Conhecimento & Docs"
    else:
        return "Engenharia"


def extract_skill_description(skill_dir: Path) -> str:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return "Módulo de engenharia do Antigravity Kit."

    try:
        content = skill_md.read_text(encoding="utf-8", errors="ignore")
        # 1. Try YAML frontmatter
        fm = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm:
            d = re.search(r'description:\s*([^\n\r]+)', fm.group(1))
            if d:
                return d.group(1).strip().strip('"\'')
        # 2. Try ## Description
        d2 = re.search(r'##\s*Description\s*\n+([^\n\r]+)', content)
        if d2:
            return d2.group(1).strip()
        # 3. First non-header paragraph
        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith('#')]
        if lines:
            return lines[0]
    except Exception:
        pass
    return "Módulo cognitivo especializado."


def main():
    manifest = load_manifest(AGENT_DIR / "skills_manifest.json")
    if not manifest:
        print_error("Manifest skills_manifest.json não encontrado. Rode o healthcheck primeiro.")
        return

    skills_data = manifest.get("skills", {})
    agents_data = manifest.get("agents", {})

    mapping_file = AGENT_DIR / "skills_github_mapping.json"
    github_map = {}
    if mapping_file.exists():
        try:
            github_map = json.loads(mapping_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    # 1. Build Skill Cards
    skill_cards = []
    skills_dir = AGENT_DIR / "skills"
    for name, data in sorted(skills_data.items()):
        status = data.get("status", "PLAYBOOK")
        tokens = data.get("tokens", 0)
        s_dir = skills_dir / name
        desc = extract_skill_description(s_dir)
        if len(desc) > 130:
            desc = desc[:127] + "..."

        tag = get_tag(name, desc)
        gh_url = github_map.get(name, "https://github.com/agentskills")
        rel_path = f"skills/{name}/SKILL.md" if (s_dir / "SKILL.md").exists() else f"skills/{name}/"

        if status == "READY":
            badge = '<span style="font-size: 0.65rem; padding: 2px 6px; border-radius: 4px; background: rgba(16, 185, 129, 0.15); color: #10B981; border: 1px solid rgba(16, 185, 129, 0.35); font-weight: 600;">READY</span>'
        elif status == "BLOCKED":
            badge = '<span style="font-size: 0.65rem; padding: 2px 6px; border-radius: 4px; background: rgba(239, 68, 68, 0.15); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.35); font-weight: 600;">BLOCKED</span>'
        elif status == "BROKEN":
            badge = '<span style="font-size: 0.65rem; padding: 2px 6px; border-radius: 4px; background: rgba(220, 38, 38, 0.25); color: #F87171; border: 1px solid rgba(220, 38, 38, 0.5); font-weight: 600;">BROKEN</span>'
        else:
            badge = '<span style="font-size: 0.65rem; padding: 2px 6px; border-radius: 4px; background: rgba(6, 182, 212, 0.15); color: #06B6D4; border: 1px solid rgba(6, 182, 212, 0.35); font-weight: 600;">PLAYBOOK</span>'

        skill_cards.append(f'''        <a class="card" href="{rel_path}" target="_blank">
          <div class="card-top">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="card-name">{name}</span>
              {badge}
            </div>
            <span class="card-tag">{tag}</span>
          </div>
          <p class="card-desc">{desc}</p>
          <div class="card-bottom">
            <span class="card-path">{rel_path}</span>
            <div style="display: flex; gap: 12px; align-items: center;">
              <a href="{gh_url}" target="_blank" style="color: #9CA3AF; text-decoration: none; font-size: 0.75rem;" title="Ver repositório no GitHub">GitHub ↗</a>
              <span class="action-arrow">Ver Skill ↗</span>
            </div>
          </div>
        </a>''')

    # Read current painel_sistema.html to preserve styling, agents, workflows, scripts and rules sections
    if not PAINEL_HTML.exists():
        print_error("painel_sistema.html original não encontrado.")
        return

    curr_html = PAINEL_HTML.read_text(encoding="utf-8")

    # Replace Skills Grid section cleanly
    skills_pattern = r'(<!-- Section 3: Skills -->\s*<div class="section-block" data-category="skills">.*?<div class="grid-container">)(.*?)(</div>\s*</div>\s*<!-- Section 4: Scripts -->)'
    match = re.search(skills_pattern, curr_html, re.DOTALL)
    if match:
        new_skills_html = "\n" + "\n".join(skill_cards) + "\n      "
        updated_html = curr_html[:match.start(2)] + new_skills_html + curr_html[match.end(2):]
        # Update tab counts
        total_skills = len(skills_data)
        updated_html = re.sub(r'Super Skills \(\d+\)', f'Super Skills ({total_skills})', updated_html)
        updated_html = re.sub(r'<span class="section-count">\d+ módulos</span>', f'<span class="section-count">{total_skills} módulos</span>', updated_html, count=1)

        PAINEL_HTML.write_text(updated_html, encoding="utf-8")
        print_success(f"painel_sistema.html atualizado com sucesso ({total_skills} skills)!")
    else:
        print_warning("Estrutura da seção de skills não encontrada para substituição precisa.")


if __name__ == "__main__":
    main()
