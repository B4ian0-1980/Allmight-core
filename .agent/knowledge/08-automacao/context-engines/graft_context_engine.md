---json
{
  "id": "graft_context_engine",
  "title": "⚡ Graft — Codebase Context Engine",
  "categoria": "08-automacao",
  "subcategoria": "context-engines",
  "resumo": "**Origem:** Baseado no repositório [`trailhq/graft`](https://github.com/trailhq/graft) **Finalidade:** Motor de engenharia de contexto e grafo de código para Claude Code, Cursor, Codex e Gemini. Permite aos agentes entenderem dependências de códig...",
  "gatilhos": [
    "automacao",
    "codebase",
    "context",
    "engine",
    "engines",
    "graft"
  ],
  "perguntas_tipo": [
    "Como utilizar ⚡ Graft — Codebase Context Engine?",
    "Quais as boas praticas de context-engines?"
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
  "dono": "stack-context-engines",
  "prioridade": 2
}
---

# ⚡ Graft — Codebase Context Engine

> **Origem:** Baseado no repositório [`trailhq/graft`](https://github.com/trailhq/graft)
> **Finalidade:** Motor de engenharia de contexto e grafo de código para Claude Code, Cursor, Codex e Gemini. Permite aos agentes entenderem dependências de código com precisão e menos tokens.

---

## 📋 Como Funciona

O Graft resolve o problema de **alucinação de contexto** em repositórios complexos:
1. **Indexação via AST (Tree-Sitter):** Constrói o mapa de tipos, interfaces, chamadas de funções e dependências cruzadas.
2. **Context Compression:** Entrega para a janela de contexto da LLM apenas o grafo estrito de dependência da linha/arquivo que está sendo editado.
3. **Servidor MCP Embutido:** Fornece ferramentas que agentes de IA chamam dinamicamente para obter a definição precisa de qualquer símbolo.

---

## 🚀 Como Inicializar

```bash
# Iniciar como servidor MCP
npx graft mcp

# Ou analisar dependências via CLI
npx graft inspect src/auth/service.ts
```

---

## 💡 Quando o Agente Deve Sugerir o Graft:
1. Quando houver refatorações complexas que quebram interfaces em arquivos distantes.
2. Em projetos TypeScript / Go / Python com tipagem forte e alto acoplamento modular.
3. Quando o agente de IA estiver tendo dificuldades para localizar a origem de tipos ou métodos importados.
