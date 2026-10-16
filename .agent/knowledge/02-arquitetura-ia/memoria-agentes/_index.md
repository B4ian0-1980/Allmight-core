---
id: idx_memoria-agentes
resumo: Indice de recursos e manuais de memoria-agentes
gatilhos:
- agentes
- arquitetura
- across
- claude
- claude-mem
- context
- agent
- agents
- for
- graphiti
rotas:
- id: claude_mem_persistence
  resumo: '**Origem:** Baseado no repositório [`thedotmack/claude-mem`](https://github.com/thedotmack/claude-mem)
    **Finalidade:** Motor de memória contínua e persistente entre sessões de trabalho
    para agentes de código (Claude Code, Gemini, Copilot, Cursor).'
  gatilhos:
  - across
  - agentes
  - arquitetura
  - claude
  - claude-mem
  - context
  arquivo: ./claude_mem_persistence.md
  secoes:
  - como-funciona
  - instalação-rápida
  - quando-sugerir
  tokens_estimados: 279
- id: graphiti_agent_memory
  resumo: '**Origem:** Baseado no repositório [`getzep/graphiti`](https://github.com/getzep/graphiti)
    (Zep AI) **Finalidade:** Framework de memória contínua e grafos de conhecimento
    dinâmicos com relações temporais para agentes autônomos.'
  gatilhos:
  - agent
  - agentes
  - agents
  - arquitetura
  - for
  - graphiti
  arquivo: ./graphiti_agent_memory.md
  secoes:
  - por-que-usar-graphiti
  - exemplo-de-uso-rápido-python
  - quando-o-agente-deve-sugerir-o-graphiti
  tokens_estimados: 474
- id: vectorize-hindsight-memory
  resumo: 'Camada de memoria persistente de longo prazo biomimetica para agentes IA
    com tres verbos fundamentais: retain, recall e reflect.'
  gatilhos:
  - hindsight
  - vectorize
  - memoria-agente
  - long-term-memory
  - retain
  - recall
  arquivo: ./vectorize-hindsight-memory.md
  secoes:
  - diferença-fundamental-hindsight-vs-rag-tradicional
  - os-três-verbos-essenciais-da-api
  - arquitetura-de-recuperação-temporal-tempr
  - integração-em-python-e-typescript
  tokens_estimados: 563
---
