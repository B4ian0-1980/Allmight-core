---json
{
  "id": "vectorize-hindsight-memory",
  "title": "Hindsight by Vectorize - Biomimetic Long-Term Agent Memory Layer",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "memoria-agentes",
  "resumo": "Camada de memoria persistente de longo prazo biomimetica para agentes IA com tres verbos fundamentais: retain, recall e reflect.",
  "gatilhos": ["hindsight", "vectorize", "memoria-agente", "long-term-memory", "retain", "recall", "reflect", "tempr"],
  "perguntas_tipo": ["Como implementar memoria de longo prazo para agentes IA?", "Qual a diferenca entre Hindsight e RAG tradicional?"],
  "nao_cobre": ["sandboxing de containers (ver substrate)", "plano de governanca de organizacao (ver paperclip)"],
  "target_agent": ["ai-architect", "backend-developer", "fullstack-developer"],
  "compatibility": {"python": ">=3.10", "node": ">=18", "storage": "PostgreSQL / SQLite"},
  "source": {"origin": "https://github.com/vectorize-io/hindsight", "original_format": "markdown"},
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-ia-memory",
  "prioridade": 1
}
---

# Hindsight by Vectorize - Biomimetic Long-Term Agent Memory Layer

> Resumo: memória contínua com os verbos retain, recall e reflect, consolidação assíncrona em background e recuperação temporal (Tempr).
> Seções: diferenca-rag · os-tres-verbos · arquitetura-tempr · integracao-codigo

## Diferença Fundamental: Hindsight vs. RAG Tradicional

* **RAG Tradicional:** Trata a base como um "saco de fragmentos de texto". A cada pergunta do usuário, busca pedaços brutos e injeta no prompt sem sintetizar fatos ou atualizar convicções.
* **Hindsight (Memória Biomimética):** Organiza o conhecimento como a memória humana (fatos consolidados sobre o mundo, experiências passadas, observações e modelos mentais). A consolidação é feita em segundo plano, transformando leituras de memória em consultas ultrarrápidas de banco de dados sem novos custos de LLM.

## Os Três Verbos Essenciais da API

1. **`retain(context, metadata)`**: Armazena novos fatos, eventos, decisões e interações ocorridas durante a sessão.
2. **`recall(query, temporal_range)`**: Recupera fatos históricos e modelos mentais relevantes utilizando inferência temporal e semântica.
3. **`reflect()`**: Processo em background que analisa o conjunto de memórias acumuladas, identifica padrões, resolve contradições e consolida novas crenças do agente.

## Arquitetura de Recuperação Temporal (Tempr)

O algoritmo **Tempr (Temporal Entity Memory Priming Retrieval)** resolve a limitação semântica tradicional:
Ele compreende expressões temporais relativas (*"o que decidimos na reunião da semana passada?"* ou *"qual foi a versão do framework adotada em agosto?"*) cruzando grafo de entidades com linha do tempo estrita.

## Integração em Python e TypeScript

### Exemplo em TypeScript:
```typescript
import { Hindsight } from "@vectorize-io/hindsight";

const memory = new Hindsight({ apiKey: process.env.HINDSIGHT_API_KEY });

// Reter um aprendizado
await memory.retain({
  agentId: "antigravity-core",
  text: "O usuario prefere TypeScript estrito com Zod para validacao de contratos de API."
});

// Recuperar informacoes para guiar o prompt
const context = await memory.recall({
  agentId: "antigravity-core",
  query: "padroes de validacao de entrada preferidos pelo usuario"
});
```
