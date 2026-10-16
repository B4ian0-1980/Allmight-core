#!/usr/bin/env bash
set -e

echo "======================================================"
echo "   BOOK-TO-SKILL - FÁBRICA DE SKILLS DE IA"
echo "======================================================"

command -v python3 >/dev/null 2>&1 || { echo "[x] Python3 não encontrado."; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${SCRIPT_DIR}/../../.agent/skills/book-to-skill"

cd "$TARGET_DIR"

if [ ! -d "venv" ]; then
    echo "[*] Criando ambiente virtual venv..."
    python3 -m venv venv
    ./venv/bin/pip install pypdf ebooklib markdown typer rich
fi

read -p "Digite o caminho do arquivo PDF/EPUB: " BOOK_PATH
./venv/bin/python3 -m book_to_skill.cli "$BOOK_PATH"
