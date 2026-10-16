#!/usr/bin/env bash
set -e

echo "======================================================"
echo "   LLAMA-FACTORY - ESTÚDIO DE FINE-TUNING DE LLMS"
echo "======================================================"

command -v python3 >/dev/null 2>&1 || { echo "[x] Python3 não encontrado."; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${SCRIPT_DIR}/../../.agent/skills/LlamaFactory"

cd "$TARGET_DIR"

if [ ! -d "venv" ]; then
    echo "[*] Criando ambiente virtual venv..."
    python3 -m venv venv
    ./venv/bin/pip install -e .[metrics,bitsandbytes]
fi

echo "[*] Iniciando WebUI em http://localhost:7860..."
./venv/bin/python3 -m llamafactory.webui.interface
