---json
{
  "id": "agent-substrate-runtime",
  "title": "Agent Substrate - Secure High-Density Agent Execution Runtime",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "mcp",
  "resumo": "Runtime seguro e de alta densidade baseado em gVisor e zero-trust para orquestracao, suspensao e retomada sub-segundo de agentes IA.",
  "gatilhos": ["substrate", "agent-substrate", "sandbox", "gvisor", "runtime", "execucao", "zero-trust", "checkpoint"],
  "perguntas_tipo": ["Como funciona o Agent Substrate?", "Como isolar agentes IA em sandboxes seguras?"],
  "nao_cobre": ["orquestracao multi-agente declarativa (ver google/ax)", "gestao de orcamento (ver paperclip)"],
  "target_agent": ["devops-engineer", "backend-developer", "security-auditor"],
  "compatibility": {"os": "Linux / GKE / Docker", "kernel": "gVisor zero-trust"},
  "source": {"origin": "https://github.com/agent-substrate/substrate", "original_format": "markdown"},
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-ia-runtime",
  "prioridade": 1
}
---

# Agent Substrate - Secure High-Density Agent Execution Runtime

> Resumo: isolamento em nível de kernel com gVisor, suspensão e retomada sub-segundo de containers de agentes e rede zero-trust.
> Seções: arquitetura-runtime · ciclo-vida-agente · isolamento-seguranca · integracao-ax

## Arquitetura do Runtime

O **Agent Substrate** é um motor de execução de agentes autônomos projetado para cenários em que milhares de agentes precisam executar comandos arbitrários, compilar código e acessar ferramentas sem comprometer a máquina hospedeira.
Ao contrário de containers Docker convencionais (que compartilham o kernel do hospedeiro), o Substrate utiliza **gVisor** para criar um limite de kernel virtualizado para cada sandbox de agente.

Principais pilares:
1. **Sub-second Suspend/Resume:** Checkpointing em tempo real da memória do processo quando o agente fica ocioso esperando resposta de LLM.
2. **Alta Densidade:** Multiplexação de centenas de sandboxes por nó hospedeiro sem overhead de VMs pesadas.
3. **Zero-Trust Egress:** Todo tráfego de rede gerado pelo agente passa por proxies de inspeção estrita com whitelisting explícito de domínios.

## Ciclo de vida do agente no Substrate

```
[Início] ──► [Provision Sandbox] ──► [Executa Ferramenta/Código]
                     ▲                               │
                     │ (Sub-second Resume)           ▼ (Espera LLM / Humano)
                     └───────────────────── [Suspend / Checkpoint]
```

## Isolamento e Segurança

- **Sandbox Boundary:** Bloqueio de syscalls perigosas via sandboxing de kernel em user-space.
- **Limites de Recursos:** Quotas rígidas de CPU, memória RAM e I/O de disco para impedir ataques DoS locais (loops infinitos ou fork bombs).
- **Ambiente Ephemeral:** Ao finalizar a sessão, o sandbox é destruído sem deixar persistência indesejada.

## Integração com Google AX

O Substrate serve como a **camada de dados e execução física** sob a qual o **Google AX** orquestra os manifestos declarativos de `Task` e `Workspace`.
