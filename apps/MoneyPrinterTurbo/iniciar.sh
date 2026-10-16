#!/usr/bin/env bash
set -e

echo "======================================================"
echo "   MONEYPRINTERTURBO - GERADOR DE VÍDEOS CURTOS"
echo "======================================================"

command -v python3 >/dev/null 2>&1 || { echo "[x] Python3 não encontrado."; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${SCRIPT_DIR}/../../.agent/skills/MoneyPrinterTurbo"

cd "$TARGET_DIR"

if [ ! -d "venv" ]; then
    echo "[*] Criando ambiente virtual venv..."
    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt
fi

echo "[*] Iniciando WebUI em http://localhost:8501..."
if [ -f "webui.sh" ]; then
    bash webui.sh
else
    ./venv/bin/streamlit run webui/Main.py
fi
