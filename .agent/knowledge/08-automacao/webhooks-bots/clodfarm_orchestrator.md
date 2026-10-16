---json
{
  "id": "clodfarm_orchestrator",
  "title": "🚜 Clodfarm — Autonomous Agent Farm Orchestrator",
  "categoria": "08-automacao",
  "subcategoria": "webhooks-bots",
  "resumo": "**Origem:** Baseado no repositório [`matank001/clodfarm`](https://github.com/matank001/clodfarm) **Finalidade:** Fazenda de agentes autônomos que decompõe missões complexas em subagentes paralelos e gerencia o ritmo de execução com base nas cotas ...",
  "gatilhos": [
    "agent",
    "automacao",
    "autonomous",
    "bots",
    "clodfarm",
    "farm",
    "orchestrator",
    "webhooks"
  ],
  "perguntas_tipo": [
    "Como utilizar 🚜 Clodfarm — Autonomous Agent Farm Orchestrator?",
    "Quais as boas praticas de webhooks-bots?"
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
  "dono": "stack-webhooks-bots",
  "prioridade": 2
}
---

# 🚜 Clodfarm — Autonomous Agent Farm Orchestrator

> **Origem:** Baseado no repositório [`matank001/clodfarm`](https://github.com/matank001/clodfarm)
> **Finalidade:** Fazenda de agentes autônomos que decompõe missões complexas em subagentes paralelos e gerencia o ritmo de execução com base nas cotas reais de uso (5 horas e semanal).

---

## 📋 Como Funciona

- **Decomposição em Sub-Agentes:** Uma missão grande (ex: "Migrar ORM de Prisma para Drizzle em 50 modelos") é dividida em pequenas tarefas assíncronas.
- **Pacing & Rate Limiting Consciente:** Monitora continuamente os limites de taxa de cada conta/chave de API para evitar esgotar a cota prematuramente ou receber erros 429.
- **Controle Remoto:** Permite acompanhar e direcionar os sub-agentes via interface remota ou pelo aplicativo oficial.
- **Isolamento de Tarefas:** Cada agente opera em sua própria branch/sandbox, reduzindo o risco de conflitos.

---

## 💡 Quando o Agente Deve Sugerir o Clodfarm:
1. Quando houver tarefas em lote com centenas de execuções (batch processing).
2. Para usuários gerenciando múltiplas chaves ou contas que precisam maximizar a vazão de trabalho diário sem bloqueios.
3. Projetos com desenvolvimento contínuo em segundo plano durante a noite (overnight batch jobs).
