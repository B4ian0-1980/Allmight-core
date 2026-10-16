import os, shutil, glob
from pathlib import Path

root = Path(r"d:\xampp\htdocs\0-fonte")
garbage = root / "old_garbage"
garbage.mkdir(parents=True, exist_ok=True)

# 1. Mover logs soltos
for pattern in ["hs_err_*.log", "replay_*.log", "cert_2026.zip"]:
    for f in root.glob(pattern):
        dest = garbage / f.name
        try:
            shutil.move(str(f), str(dest))
            print(f"Movido arquivo: {f.name}")
        except Exception as e:
            print(f"Erro em {f.name}: {e}")

# 2. Mover pastas que nao fazem parte do nucleo do sistema
dirs_to_move = ["certificado", "backend", "gpmc", "sistemas"]
for d in dirs_to_move:
    p = root / d
    if p.exists():
        dest = garbage / d
        try:
            shutil.move(str(p), str(dest))
            print(f"Movida pasta: {d}")
        except Exception as e:
            print(f"Erro ao mover {d}: {e}")

print("Limpeza para old_garbage concluida!")
