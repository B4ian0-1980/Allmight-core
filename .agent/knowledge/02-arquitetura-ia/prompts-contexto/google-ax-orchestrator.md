---json
{
  "id": "google-ax-orchestrator",
  "title": "Google AX (Agent Executor) - Declarative Multi-Agent Orchestrator",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "prompts-contexto",
  "resumo": "Plano de controle e orquestrador declarativo estilo Kubernetes para frotas de agentes autonomos sobre Agent Substrate.",
  "gatilhos": ["google-ax", "ax", "agent-executor", "orquestracao", "declarativo", "task", "workspace", "gateway", "fleet"],
  "perguntas_tipo": ["Como orquestrar frotas de agentes com Google AX?", "Quais sao os quatro primitivos da API ax.io/v1alpha1?"],
  "nao_cobre": ["memoria de longo prazo (ver vectorize-io/hindsight)", "gestao de orcamento de empresas autonomas (ver paperclip)"],
  "target_agent": ["ai-architect", "devops-engineer", "backend-developer"],
  "compatibility": {"cli": "ax CLI", "api": "ax.io/v1alpha1"},
  "source": {"origin": "https://github.com/google/ax", "original_format": "markdown"},
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-ia-orchestration",
  "prioridade": 1
}
---

# Google AX (Agent Executor) - Declarative Multi-Agent Orchestrator

> Resumo: orquestração de frotas de agentes estilo Kubernetes com os 4 primitivos (Task, Workspace, Gateway, Model) e controle de ciclo de vida.
> Seções: visao-geral · os-quatro-primitivos · manifesto-exemplo · operacao-cli

## Visão Geral

O **Google AX (Agent Executor)** é um plano de controle open-source desenvolvido pelo Google para tratar agentes autônomos como **atores de longa duração com estado** em vez de microserviços sem estado ou jobs de lote.
Ele introduz um padrão declarativo com sintaxe e experiência de uso inspiradas no `kubectl`, operando em harmonia com o runtime de sandboxes **Agent Substrate**.

## Os Quatro Primitivos (`ax.io/v1alpha1`)

1. **`Task`**: Unidade fundamental de execução isolada (imagem do container, comando, variáveis e objetivo).
2. **`Workspace`**: Gerencia o pré-boot declarativo do agente (clonagem de repositórios Git, injeção de MCP Servers e skills).
3. **`Gateway`**: Políticas de saída de rede (egress filtering) para restringir conexões externas a hosts/portas aprovadas.
4. **`Model`**: Centraliza parâmetros de inferência de IA, chaves de API e seleção dinâmica de modelos (Gemini, Claude, GPT).

## Manifesto de Exemplo (`task.yaml`)

```yaml
apiVersion: ax.io/v1alpha1
kind: Workspace
metadata:
  name: workspace-antigravity
spec:
  git:
    - repo: https://github.com/meu-org/meu-projeto.git
      branch: "main"
---
apiVersion: ax.io/v1alpha1
kind: Task
metadata:
  name: agente-refactor
spec:
  workspaces:
    - name: workspace-antigravity
  goal: "Refatorar componentes legados garantindo testes unitarios verdes"
  debug: true
```

## Operação via CLI

A CLI `ax` oferece o mesmo padrão ergonômico do ecossistema Kubernetes:

```bash
# Aplicar manifesto declarativo
ax apply -f task.yaml

# Monitorar execucao em tempo real
ax watch task agente-refactor

# Inspecionar detalhes e estado do checkpoint
ax describe task agente-refactor
```
