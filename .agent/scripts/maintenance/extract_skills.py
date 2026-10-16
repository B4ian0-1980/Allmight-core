import os, yaml, json
from pathlib import Path

skills_dir = Path(r"d:\xampp\htdocs\0-fonte\.agent\skills")
skills_info = []

for s in sorted(skills_dir.iterdir()):
    if s.is_dir():
        skill_file = s / "SKILL.md"
        if skill_file.exists():
            text = skill_file.read_text(encoding="utf-8", errors="ignore")
            name = s.name
            desc = "Sem descricao"
            if text.startswith("---"):
                parts = text.split("---", 2)
                if len(parts) >= 3:
                    try:
                        fm = yaml.safe_load(parts[1])
                        if isinstance(fm, dict):
                            desc = fm.get("description", desc)
                            name = fm.get("name", name)
                    except:
                        pass
            skills_info.append({"name": name, "dir": s.name, "desc": desc.strip().replace("\n", " ")})

print(f"TOTAL SKILLS ENCONTRADAS: {len(skills_info)}")

# Salvar catalogo de consulta rapida
out_file = Path(r"d:\xampp\htdocs\0-fonte\.agent\skills\CATALOGO_SKILLS.json")
out_file.write_text(json.dumps(skills_info, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Salvo em {out_file}")
