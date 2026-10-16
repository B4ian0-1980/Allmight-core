import os
from pathlib import Path
from collections import Counter

kb_path = Path(r"d:\xampp\htdocs\0-fonte\.agent\knowledge")
exts = Counter()
folders = Counter()
total_files = 0
total_size = 0
all_files = []

for root, _, files in os.walk(kb_path):
    for f in files:
        total_files += 1
        p = Path(root) / f
        try:
            sz = p.stat().st_size
        except Exception:
            sz = 0
        total_size += sz
        ext = p.suffix.lower() if p.suffix else "(sem_extensao)"
        exts[ext] += 1
        
        rel = p.relative_to(kb_path)
        top_folder = rel.parts[1] if len(rel.parts) > 1 else "(raiz)"
        folders[top_folder] += 1
        all_files.append((str(rel).replace("\\", "/"), sz, ext))

print(f"TOTAL_ARQUIVOS={total_files}")
print(f"TOTAL_BYTES={total_size}")
print(f"TOTAL_KB={total_size / 1024:.1f}")
print(f"TOTAL_MB={total_size / (1024 * 1024):.2f}")

print("\n--- EXTENSOES ---")
for ext, count in exts.most_common():
    print(f"{ext}: {count}")

print("\n--- PASTAS PRINCIPAIS ---")
for folder, count in folders.most_common():
    print(f"{folder}: {count} arquivos")

# Salva inventário completo em JSON
import json
output_data = {
    "total_files": total_files,
    "total_bytes": total_size,
    "extensions": dict(exts),
    "folders": dict(folders),
    "files": all_files
}

out_file = Path(r"d:\xampp\htdocs\0-fonte\.agent\knowledge\INVENTARIO_KNOWLEDGE.json")
out_file.write_text(json.dumps(output_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nSalvo em {out_file}")
