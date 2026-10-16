---
name: opencode-agent
description: OpenCode v2 coding agent for terminal and multi-session workflows. Use when the user asks to run opencode, use anomalyco/opencode, execute multi-provider AI coding sessions, or trigger terminal-based pair programming agents.
---

# 🚀 OpenCode v2 Agent Skill

O **OpenCode v2** (`anomalyco/opencode`) é um assistente de codificação open-source operado via Terminal (TUI), desktop ou extensão de IDE, com suporte nativo a 75+ provedores de LLM, servidores MCP e integração profunda com LSPs.

## 🎯 Quando Usar
* Quando o usuário quiser executar sessões autônomas de código no terminal.
* Quando precisar de alternância rápida entre múltiplos provedores de IA (Claude, GPT, Gemini, modelos locais via Ollama).
* Para pareamento de código assistido por Language Server Protocol (LSP) com diagnósticos em tempo real.

## ⚡ Como Iniciar no Sistema

Na pasta `apps/opencode`, utilize o inicializador multiplataforma:

### Windows:
```cmd
d:\xampp\htdocs\0-fonte\apps\opencode\iniciar.bat
```

### Linux / WSL:
```bash
bash d:/xampp/htdocs/0-fonte/apps/opencode/iniciar.sh
```

## ⚙️ Principais Comandos da CLI do OpenCode v2
* `opencode`: Abre o terminal interativo (TUI) no diretório atual.
* `opencode --model gemini-2.5-pro`: Define o modelo prioritário para a sessão.
* `opencode --mcp`: Conecta aos servidores Model Context Protocol configurados localmente.
