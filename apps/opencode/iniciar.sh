#!/usr/bin/env bash
set -e

echo "==================================================="
echo "    🚀 OpenCode v2 - Assistente de Codigo IA"
echo "==================================================="
echo ""

if ! command -v node &> /dev/null; then
    echo "[ERRO] Node.js nao foi encontrado no sistema!"
    echo "Instale o Node.js v18+ para continuar."
    exit 1
fi

if command -v opencode &> /dev/null; then
    echo "[OK] OpenCode CLI encontrado globalmente."
    opencode "$@"
    exit 0
fi

echo "[INFO] Executando OpenCode v2 via npx..."
npx --yes opencode-ai@latest "$@"
