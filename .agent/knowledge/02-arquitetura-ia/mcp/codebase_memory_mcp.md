---json
{
  "id": "codebase_memory_mcp",
  "title": "🧠 Codebase Memory MCP Server",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "mcp",
  "resumo": "**Origem:** Baseado no repositório [`DeusData/codebase-memory-mcp`](https://github.com/DeusData/codebase-memory-mcp) **Finalidade:** Servidor MCP de inteligência de código de ultra-alta performance. Indexa codebases inteiros em grafo de conhecimen...",
  "gatilhos": [
    "arquitetura",
    "codebase",
    "mcp",
    "memory",
    "server"
  ],
  "perguntas_tipo": [
    "Como utilizar 🧠 Codebase Memory MCP Server?",
    "Quais as boas praticas de mcp?"
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
  "dono": "stack-mcp",
  "prioridade": 2
}
---

# 🧠 Codebase Memory MCP Server

> **Origem:** Baseado no repositório [`DeusData/codebase-memory-mcp`](https://github.com/DeusData/codebase-memory-mcp)
> **Finalidade:** Servidor MCP de inteligência de código de ultra-alta performance. Indexa codebases inteiros em grafo de conhecimento SQLite em milissegundos, reduzindo em até 99% o consumo de tokens.

---

## 📋 Principais Características

- **Indexação Instantânea:** Analisa repositórios médios em milissegundos usando Tree-sitter em C estático.
- **158 Linguagens Suportadas:** Cobertura para PHP, Python, JavaScript, TypeScript, C#, Go, Rust, Java, etc.
- **Consultas em Sub-milissegundos:** Grafo persistente em SQLite local com busca relacional via Cypher/SQL.
- **Zero Dependências:** Binário compilado nativo, sem necessidade de Node runtime pesado ou Python venv.
- **Economia Drástica de Tokens:** O agente consulta apenas nós específicos (funções, chamadores, tipos) em vez de carregar arquivos inteiros no contexto.

---

## ⚡ Como Habilitar no Antigravity / Cursor / Claude Code

Adicione ao seu `mcp_config.json`:

```json
{
  "mcpServers": {
    "codebase-memory": {
      "command": "npx",
      "args": ["-y", "codebase-memory-mcp"]
    }
  }
}
```

---

## 💡 Quando o Agente Deve Sugerir Este MCP:
1. Ao iniciar auditoria ou navegação em projetos grandes com centenas de arquivos (ex: `TurnoCertoVN`, ERPs, frameworks monolíticos).
2. Quando a IA precisar rastrear onde uma função é chamada sem ler recursivamente dezenas de arquivos.
3. Para manter o histórico semântico do código entre diferentes sessões de desenvolvimento.
