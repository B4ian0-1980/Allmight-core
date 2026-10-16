---
id: idx_mcp
resumo: Indice de recursos e manuais de mcp
gatilhos:
- substrate
- agent-substrate
- sandbox
- gvisor
- runtime
- execucao
- arquitetura
- codebase
- mcp
- memory
rotas:
- id: agent-substrate-runtime
  resumo: Runtime seguro e de alta densidade baseado em gVisor e zero-trust para orquestracao,
    suspensao e retomada sub-segundo de agentes IA.
  gatilhos:
  - substrate
  - agent-substrate
  - sandbox
  - gvisor
  - runtime
  - execucao
  arquivo: ./agent-substrate-runtime.md
  secoes:
  - arquitetura-do-runtime
  - ciclo-de-vida-do-agente-no-substrate
  - isolamento-e-segurança
  - integração-com-google-ax
  tokens_estimados: 505
- id: codebase_memory_mcp
  resumo: '**Origem:** Baseado no repositório [`DeusData/codebase-memory-mcp`](https://github.com/DeusData/codebase-memory-mcp)
    **Finalidade:** Servidor MCP de inteligência de código de ultra-alta performance.
    Indexa codebases inteiros em grafo de conhecimen...'
  gatilhos:
  - arquitetura
  - codebase
  - mcp
  - memory
  - server
  arquivo: ./codebase_memory_mcp.md
  secoes:
  - principais-características
  - como-habilitar-no-antigravity--cursor--claude-code
  - quando-o-agente-deve-sugerir-este-mcp
  tokens_estimados: 399
---
