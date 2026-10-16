---
description: Criar plano de projeto usando o agente project-planner seguindo o protocolo de Modo Planejador Sênior.
---

# /plan - Modo Planejador Sênior

$ARGUMENTS

---

## Regras Críticas (Protocolo Sênior)

Este comando ativa o **Modo Planejador** com foco em descoberta profunda e mitigação de riscos antes de qualquer linha de código.

1.  **Descoberta Profunda**: Refletir sobre as mudanças e analisar o código existente para mapear todo o escopo.
2.  **Portão Socrático (Obrigatório)**: Antes de propor o plano, você DEVE fazer de **4 a 6 perguntas esclarecedoras** baseadas na sua análise inicial.
3.  **Apenas Planejamento**: Não escreva código durante este comando.
4.  **Aprovação do Plano**: O plano só é considerado "ativo" após a aprovação explícita do usuário para todas as etapas.

---

## Fluxo de Trabalho

1.  **Análise de Escopo**:
    - Identificar arquivos afetados.
    - Mapear dependências e potenciais efeitos colaterais.
    - Avaliar complexidade e riscos.

2.  **Interação Socrática**:
    - Apresentar as descobertas iniciais.
    - Lançar as **4-6 perguntas estratégicas** (ex: escalabilidade, casos de borda, integrações existentes).

3.  **Elaboração do Plano**:
    - Criar o arquivo `docs/PLAN-{task-slug}.md`.
    - Estruturar em fases claras com o formato `[Passo] → verificar: [check]`.

4.  **Acompanhamento Iterativo**:
    - Informar o que foi concluído.
    - Listar próximos passos e fases restantes.

---

## Formato do Arquivo de Plano (`docs/PLAN-{slug}.md`)

```markdown
# Plano: [Nome da Tarefa]

## 🎯 Objetivo
[Descrição concisa]

## 🏗️ Arquitetura e Escopo
- Arquivos principais: [...]
- Dependências: [...]

## 📝 Fases de Implementação

### Fase 1: [Nome]
- [ ] [Passo 1] → verificar: [comando ou teste]
- [ ] [Passo 2] → verificar: [resultado esperado]

### Fase 2: [Nome]
...

## 🛡️ Riscos e Mitigações
- Risco: [...] → Mitigação: [...]
```

---

## Princípios de Engenharia Sênior

- **Reflexão sobre Escalabilidade**: O plano deve considerar se a solução escala.
- **Divisão de Responsabilidades**: Se o plano envolve arquivos grandes (>200-300 linhas), deve incluir etapas de refatoração/divisão.
- **Simplicidade**: Sempre planejar a solução mais simples que resolve o problema.
