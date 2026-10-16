---json
{
  "id": "paperclip-agent-management",
  "title": "Paperclip - Open-Source Management Plane for Autonomous Agent Companies",
  "categoria": "01-gestao",
  "subcategoria": "startup-produto",
  "resumo": "Plataforma open-source para gestao, hierarquia organizacional (Org Charts), controle de orcamentos e governanca de agentes autonomos.",
  "gatilhos": ["paperclip", "paperclipai", "governanca", "org-chart", "orcamento", "heartbeat", "tickets", "zero-human"],
  "perguntas_tipo": ["Como gerenciar uma empresa operada por agentes IA com Paperclip?", "Como definir orcamentos e hierarquias para agentes?"],
  "nao_cobre": ["sandboxing de baixo nivel gVisor (ver substrate)", "memoria biomimetica (ver hindsight)"],
  "target_agent": ["product-manager", "ai-architect", "operations-lead"],
  "compatibility": {"node": ">=20", "database": "PostgreSQL / SQLite", "ui": "React Dashboard"},
  "source": {"origin": "https://github.com/paperclipai/paperclip", "original_format": "markdown"},
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-gestao-agentes",
  "prioridade": 1
}
---

# Paperclip - Open-Source Management Plane for Autonomous Agent Companies

> Resumo: governança de equipes de agentes IA, organogramas virtuais, orçamentos mensais em dólares/tokens e fluxo de tickets assíncronos.
> Seções: visao-geral · organograma-e-papeis · fluxo-tickets-heartbeat · controle-orcamentario

## Visão Geral

O **Paperclip** é uma plataforma que permite a fundadores e equipes de engenharia orquestrar agentes autônomos como membros de uma **"empresa virtual zero-human"**.
Em vez de scripts soltos rodando sem supervisão, o Paperclip fornece uma camada de gestão formal com painel em React, controle de custos em tempo real e rastreabilidade total de auditoria.

## Organograma e Papéis (Org Charts)

O Paperclip estrutura os agentes em hierarquias claras de subordinação e especialidade:
* **Executivos / Coordenadores (ex: Tech Lead Agent):** Recebem metas de alto nível e quebram em tickets técnicos menores.
* **Agentes Especialistas (ex: Frontend, QA, DevOps):** Executam tarefas específicas dentro de sandboxes e devolvem relatórios com diffs de código.
* **Escalação para Humanos:** Regras de parada configuráveis quando decisões exigem aprovação humana explícita.

## Fluxo de Tickets & Heartbeats

```
[Meta de Negócio] ──► [Tech Lead Agent] ──► [Ticket Gerado]
                                                   │
  ┌────────────────────────────────────────────────┘
  ▼
[Agente Especialista (Acorda via Heartbeat)] ──► [Executa Tarefa] ──► [Submete PR / Relatório]
```

* **Heartbeats:** Os agentes não precisam ficar rodando em loop infinito consumindo tokens. Eles acordam em horários ou eventos programados, checam a fila de tickets pendentes e voltam a suspender.

## Controle Orçamentário e Governança

* **Limites de Gastos:** Definição de limites rígidos em dólares (USD) ou tokens por agente e por projeto.
* **Audit Trail:** Cada tool call, prompt e retorno de LLM é persistido em log imutável para compliance e análise de performance.
