---json
{
  "id": "opencode-v2-coding-agent",
  "title": "OpenCode v2 - Autonomous Terminal Coding Agent and Multi-Provider TUI",
  "categoria": "08-automacao",
  "subcategoria": "cli-agentes",
  "resumo": "Assistente de codigo aberto para terminal e IDE com suporte a 75+ provedores de LLM, conexao com MCP Servers e integracao LSP.",
  "gatilhos": ["opencode", "anomalyco", "coding-agent", "tui", "lsp", "terminal-agent", "mcp-client"],
  "perguntas_tipo": ["Como rodar o OpenCode v2?", "Como configurar provedores de IA no OpenCode?"],
  "nao_cobre": ["sandboxing de baixo nivel gVisor (ver substrate)", "declaracao kubernetes de tarefas (ver ax)"],
  "target_agent": ["software-engineer", "backend-developer", "fullstack-developer"],
  "compatibility": {"cli": "opencode CLI", "node": ">=18", "platforms": "Windows / Linux / macOS"},
  "source": {"origin": "https://github.com/anomalyco/opencode/tree/v2", "original_format": "markdown"},
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-cli-agentes",
  "prioridade": 1
}
---

# OpenCode v2 - Autonomous Terminal Coding Agent and Multi-Provider TUI

> Resumo: terminal UI interativo para pareamento com IA, alternância dinâmica de LLMs, suporte a LSP e clientes MCP.
> Seções: visao-geral · instalacao-e-execucao · suporte-multi-provedor · integracao-mcp-e-lsp

## Visão Geral

O **OpenCode v2** (desenvolvido por `anomalyco`) é uma ferramenta open-source de ponta para engenharia de software assistida por IA.
Ele funciona tanto como interface de terminal (TUI) elegante e rápida quanto como back-end integrado para IDEs (VS Code, Cursor, Zed, Windsurf) e GitHub Actions.

## Instalação e Execução

O ecossistema local já conta com scripts prontos na pasta de aplicações executáveis:

* **Windows:** [`d:\xampp\htdocs\0-fonte\apps\opencode\iniciar.bat`](file:///d:/xampp/htdocs/0-fonte/apps/opencode/iniciar.bat)
* **Linux/macOS:** [`d:\xampp\htdocs\0-fonte\apps\opencode\iniciar.sh`](file:///d:/xampp/htdocs/0-fonte/apps/opencode/iniciar.sh)

Ou via gerenciador de pacotes global:
```bash
npm install -g @opencode/cli
```

## Suporte Multi-Provedor (75+ LLMs)

O OpenCode v2 se destaca pela neutralidade de fornecedores, permitindo conectar:
* **Provedores de Nuvem:** Anthropic Claude (3.7 Sonnet), OpenAI (GPT-4o), Google Gemini (2.5 Pro).
* **Modelos Locais:** Conexão nativa com Ollama e vLLM via endpoints compatíveis com OpenAI.
* **Provedores Agregadores:** OpenRouter, Groq, DeepSeek.

## Integração MCP e LSP

1. **Model Context Protocol (MCP):** Capaz de consumir servidores MCP locais para leitura de bancos de dados, scraping web e inspeção de código.
2. **Language Server Protocol (LSP):** Lê definições de tipos, diagnósticos de compilação e referências de símbolos para fornecer contexto cirúrgico ao LLM.
