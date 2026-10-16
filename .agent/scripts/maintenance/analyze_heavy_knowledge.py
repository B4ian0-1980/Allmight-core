import os
from pathlib import Path

kb = Path(r"d:\xampp\htdocs\0-fonte\.agent\knowledge\allmight")

def scan_dir(p, depth=0, max_depth=3):
    if depth >= max_depth:
        return
    for item in sorted(p.iterdir()):
        if item.is_dir():
            file_count = 0
            size_bytes = 0
            has_node_modules = False
            has_git = False
            has_venv = False
            
            for root, dirs, files in os.walk(item):
                file_count += len(files)
                for f in files:
                    try:
                        size_bytes += (Path(root) / f).stat().st_size
                    except Exception:
                        pass
                if "node_modules" in dirs:
                    has_node_modules = True
                if ".git" in dirs:
                    has_git = True
                if ".venv" in dirs or "venv" in dirs:
                    has_venv = True
            
            size_mb = size_bytes / (1024 * 1024)
            flags = []
            if has_node_modules: flags.append("NODE_MODULES")
            if has_git: flags.append(".GIT")
            if has_venv: flags.append("VENV")
            flag_str = f" [{', '.join(flags)}]" if flags else ""
            
            indent = "  " * depth
            print(f"{indent}- {item.name}/: {file_count} arquivos ({size_mb:.1f} MB){flag_str}")
            
            if file_count > 1000 and depth < max_depth - 1:
                scan_dir(item, depth + 1, max_depth)

print("=== VARREDURA DE DENSIDADE E GARGALOS ===")
scan_dir(kb, 0, 3)
