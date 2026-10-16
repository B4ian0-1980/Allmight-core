#!/usr/bin/env bash
set -e

echo "======================================================"
echo "   FREE CLAUDE CODE - PROXY DE MODELOS ABERTOS"
echo "======================================================"

command -v python3 >/dev/null 2>&1 || { echo "[x] Python3 não encontrado."; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${SCRIPT_DIR}/../../.agent/skills/free-claude-code"

cd "$TARGET_DIR"

if [ ! -d "venv" ]; then
    echo "[*] Criando ambiente virtual venv..."
    python3 -m venv venv
    ./venv/bin/pip install fastapi uvicorn httpx pydantic
fi

echo "[*] Iniciando proxy na porta 8080..."
./venv/bin/python3 -m uvicorn src.main:app --host 0.0.0.0 --port 8080
