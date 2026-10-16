import os
import re

mapping = {
    "laws-of-ux": "https://github.com/keysjoao/laws-of-ux-skills",
    "frontend-design": "https://github.com/anthropics/skills/tree/main/skills/frontend-design",
    "pre-mortem": "https://github.com/borghei/Claude-Skills",
    "loop-engineering": "https://github.com/cobusgreyling/loop-engineering",
    "find-skills": "https://github.com/vercel-labs/skills/tree/main/skills/find-skills",
    "coding-discipline": "https://github.com/karpathy",
    "claude-mem": "https://github.com/thedotmack/claude-mem",
    "agent-browser": "https://github.com/vercel-labs/agent-browser",
    "openjarvis": "https://github.com/open-jarvis/openjarvis",
    "superpowers": "https://github.com/obra/superpowers",
    "gstack": "https://github.com/garrytan/gstack",
    "i-have-adhd": "https://github.com/ayghri/i-have-adhd",
    "octopusreview": "https://github.com/octopusreview",
    "chrome-devtools-mcp": "https://github.com/ChromeDevTools/chrome-devtools-mcp",
    "autoloop": "https://github.com/githubnext/autoloop",
    "loopy": "https://github.com/Forward-Future/loopy",
    "agent-loop": "https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/agent-loop",
    "anydoc": "https://github.com/firecrawl/anydoc",
    "claude-code-setup": "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup",
    "addyosmani-skills": "https://github.com/addyosmani/agent-skills",
    "rea": "https://github.com/morluto/rea",
    "opendots": "https://github.com/CopilotKit/OpenDots"
}

skills_dir = r"d:\xampp\htdocs\0-fonte\.agent\skills"

for skill_name, url in mapping.items():
    skill_path = os.path.join(skills_dir, skill_name, "SKILL.md")
    if os.path.exists(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "upstream_source:" not in content:
            new_content = re.sub(r'(\n---\n)', f'\nupstream_source: {url}\nlast_updated: 2026-10-10\\1', content, count=1)
            with open(skill_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ Injetado em {skill_name}")

print("Concluido.")
