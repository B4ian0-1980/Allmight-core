#!/usr/bin/env bash
set -e

echo "======================================================"
echo "   FREELLMAPI - GATEWAY LOCAL DE MODELOS DE IA"
echo "======================================================"

command -v node >/dev/null 2>&1 || { echo "[x] Node.js não encontrado. Instale o Node.js v20+."; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${SCRIPT_DIR}/../../.agent/skills/freellmapi"

cd "$TARGET_DIR"

if [ ! -d "node_modules" ]; then
    echo "[*] Instalando dependências (npm install)..."
    npm install
fi

echo "[*] Iniciando servidor em http://localhost:3001..."
npm run dev
