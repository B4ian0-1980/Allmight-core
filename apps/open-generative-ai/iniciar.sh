#!/usr/bin/env bash
set -e

echo "======================================================"
echo "   OPEN GENERATIVE AI - ESTÚDIO DE VÍDEO E VOZ"
echo "======================================================"

command -v node >/dev/null 2>&1 || { echo "[x] Node.js não encontrado."; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${SCRIPT_DIR}/../../.agent/skills/open-generative-ai"

cd "$TARGET_DIR"

if [ ! -d "node_modules" ]; then
    echo "[*] Instalando dependências (npm install)..."
    npm install
fi

echo "[*] Iniciando Next.js em http://localhost:3000..."
npm run dev
