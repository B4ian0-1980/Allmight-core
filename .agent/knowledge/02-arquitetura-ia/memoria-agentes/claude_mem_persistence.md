---json
{
  "id": "claude_mem_persistence",
  "title": "🧠 claude-mem — Persistent Context Across Sessions",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "memoria-agentes",
  "resumo": "**Origem:** Baseado no repositório [`thedotmack/claude-mem`](https://github.com/thedotmack/claude-mem) **Finalidade:** Motor de memória contínua e persistente entre sessões de trabalho para agentes de código (Claude Code, Gemini, Copilot, Cursor).",
  "gatilhos": [
    "across",
    "agentes",
    "arquitetura",
    "claude",
    "claude-mem",
    "context",
    "mem",
    "memoria"
  ],
  "perguntas_tipo": [
    "Como utilizar 🧠 claude-mem — Persistent Context Across Sessions?",
    "Quais as boas praticas de memoria-agentes?"
  ],
  "nao_cobre": [],
  "target_agent": [
    "general-assistant"
  ],
  "source": {
    "origin": "AllMight Knowledge Base",
    "original_format": "markdown"
  },
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-memoria-agentes",
  "prioridade": 2
}
---

# 🧠 claude-mem — Persistent Context Across Sessions

> **Origem:** Baseado no repositório [`thedotmack/claude-mem`](https://github.com/thedotmack/claude-mem)
> **Finalidade:** Motor de memória contínua e persistente entre sessões de trabalho para agentes de código (Claude Code, Gemini, Copilot, Cursor).

---

## 📋 Como Funciona

- **Captura Silenciosa:** O claude-mem monitora a execução do agente em segundo plano, registrando arquivos tocados, decisões tomadas, comandos executados e erros superados.
- **Compressão Inteligente:** Utiliza SQLite + embeddings locais para sumarizar o trabalho sem gerar bloat de contexto.
- **Injeção de Retomada:** Ao iniciar uma nova conversa ou reabrir o editor no dia seguinte, o agente recupera instantaneamente a linha do tempo e continua exatamente de onde parou.

---

## ⚡ Instalação Rápida

```bash
# Instalação do plugin global
npm install -g claude-mem
claude-mem init
```

---

## 💡 Quando Sugerir:
1. Projetos de longo prazo desenvolvidos ao longo de semanas ou meses.
2. Quando o usuário reclama de ter que "reexplicar o contexto" toda vez que abre uma nova sessão.
