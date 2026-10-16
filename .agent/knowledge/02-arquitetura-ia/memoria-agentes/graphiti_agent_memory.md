---json
{
  "id": "graphiti_agent_memory",
  "title": "🕸️ Graphiti — Real-Time Knowledge Graphs for AI Agents",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "memoria-agentes",
  "resumo": "**Origem:** Baseado no repositório [`getzep/graphiti`](https://github.com/getzep/graphiti) (Zep AI) **Finalidade:** Framework de memória contínua e grafos de conhecimento dinâmicos com relações temporais para agentes autônomos.",
  "gatilhos": [
    "agent",
    "agentes",
    "agents",
    "arquitetura",
    "for",
    "graphiti",
    "graphs",
    "knowledge"
  ],
  "perguntas_tipo": [
    "Como utilizar 🕸️ Graphiti — Real-Time Knowledge Graphs for AI Agents?",
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

# 🕸️ Graphiti — Real-Time Knowledge Graphs for AI Agents

> **Origem:** Baseado no repositório [`getzep/graphiti`](https://github.com/getzep/graphiti) (Zep AI)
> **Finalidade:** Framework de memória contínua e grafos de conhecimento dinâmicos com relações temporais para agentes autônomos.

---

## 📋 Por que Usar Graphiti?

Modelos de RAG tradicionais baseados puramente em vetores perdem o contexto temporal e as conexões semânticas entre fatos que evoluem ao longo do tempo (ex: "o usuário mudou de endereço ontem"). 

O **Graphiti** resolve isso construindo um Grafo de Conhecimento Dinâmico em tempo real:
- **Consciência Temporal:** Rastreia quando fatos foram aprendidos, modificados ou invalidados.
- **Extração Autônoma de Entidades:** Identifica atores, regras, decisões de negócio e seus relacionamentos sem necessidade de ontologias manuais.
- **Integração com Neo4j / Memgraph / SQLite:** Compatível com os principais motores de grafos e RAG híbrido (Vetores + Grafo).

---

## 🚀 Exemplo de Uso Rápido (Python)

```python
from graphiti_core import Graphiti

# Inicializa motor de grafo
graphiti = Graphiti("neo4j://localhost:7687", auth=("neo4j", "password"))

# Adiciona episódios / interações
await graphiti.add_episode(
    name="Reunião de Requisitos",
    episode_body="O cliente solicitou que as senhas expirem a cada 90 dias.",
    source_description="Documentação do Projeto"
)

# Consulta com raciocínio relacional
results = await graphiti.search("Quais são as políticas de segurança de credenciais?")
```

---

## 💡 Quando o Agente Deve Sugerir o Graphiti:
1. Ao desenvolver assistentes virtuais ou agentes de suporte que precisam de **memória de longo prazo** sobre usuários.
2. Em sistemas corporativos com histórico complexo onde documentos se contradizem ao longo do tempo.
3. Projetos de agentes autônomos que acumulam conhecimento durante meses de operação contínua.
