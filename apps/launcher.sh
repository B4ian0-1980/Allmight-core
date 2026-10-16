#!/usr/bin/env bash

show_menu() {
    clear
    echo "======================================================================"
    echo "         CENTRAL DE SUPERFERRAMENTAS EXECUTÁVEIS (0-FONTE)"
    echo "======================================================================"
    echo ""
    echo "  [1] Git Web Hub         - Auditoria de Segredos e Publicador GitHub"
    echo "  [2] FreeLLMAPI          - Gateway Gratuito de 635 Modelos de IA"
    echo "  [3] MoneyPrinterTurbo   - Gerador de Vídeos Curtos (TikTok/Shorts)"
    echo "  [4] LLaMA-Factory       - Estúdio Visual de Fine-Tuning de LLMs"
    echo "  [5] Open Generative AI  - Estúdio Multimodal de Imagem, Vídeo e Voz"
    echo "  [6] Free Claude Code    - Proxy Local para Claude Code com Modelos Abertos"
    echo "  [7] Book-to-Skill       - Converter Livro/PDF em Conhecimento de IA"
    echo ""
    echo "  [0] Sair"
    echo "======================================================================"
    echo ""
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

while true; do
    show_menu
    read -p "Escolha uma opção [0-7]: " OPCAO
    case "$OPCAO" in
        1) bash "${SCRIPT_DIR}/../git-web-hub/iniciar.sh" ;;
        2) bash "${SCRIPT_DIR}/freellmapi/iniciar.sh" ;;
        3) bash "${SCRIPT_DIR}/MoneyPrinterTurbo/iniciar.sh" ;;
        4) bash "${SCRIPT_DIR}/LlamaFactory/iniciar.sh" ;;
        5) bash "${SCRIPT_DIR}/open-generative-ai/iniciar.sh" ;;
        6) bash "${SCRIPT_DIR}/free-claude-code/iniciar.sh" ;;
        7) bash "${SCRIPT_DIR}/book-to-skill/iniciar.sh" ;;
        0) exit 0 ;;
        *) echo "Opção inválida."; sleep 1 ;;
    esac
done
