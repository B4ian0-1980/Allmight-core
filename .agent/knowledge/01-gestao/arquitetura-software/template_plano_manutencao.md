---json
{
  "id": "template_plano_manutencao",
  "title": "🔧 Template - Plano de Manutenção",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🔧 Template - Plano de Manutenção.",
  "gatilhos": [
    "arquitetura",
    "gestao",
    "manutencao",
    "plano",
    "software",
    "template"
  ],
  "perguntas_tipo": [
    "Como utilizar 🔧 Template - Plano de Manutenção?",
    "Quais as boas praticas de arquitetura-software?"
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
  "dono": "stack-arquitetura-software",
  "prioridade": 2
}
---

# 🔧 Template - Plano de Manutenção

**Projeto:** [NOME_DO_PROJETO]
**Data:** [DATA_ATUAL]
**Versão:** 1.0

---

## 🎯 Objetivo
Garantir a longevidade e saúde do software através de práticas de manutenção estruturadas.

---

## 🏗️ Tipos de Manutenção

### 1. Manutenção Preventiva
**Frequência:** Mensal/Trimestral
- [ ] Atualização de dependências (Patch/Minor).
- [ ] Review de logs de erro (Sentry/Datadog).
- [ ] Auditoria de segurança básica.
- [ ] Otimização de Performance (Banco de Dados, Caches).

### 2. Manutenção Corretiva
**Frequência:** Sob demanda (Bugfix)
- **Críticos (P1):** SLA < [4h]. (Sistema fora do ar, perda de dados).
- **Alta (P2):** SLA < [24h]. (Funcionalidade core quebrada).
- **Média (P3):** SLA < [1 semana]. (Bug visual, workaround disponível).

### 3. Manutenção Evolutiva
**Frequência:** Roadmap (Sprint)
- Novas features solicitadas pelo cliente.
- Refatoração de código legado (Tech Debt).
- Melhorias de UX.

---

## 📝 Processo de Feedback e Evolução

1. **Coleta:** Canal de suporte, feedback do usuário, métricas de uso.
2. **Triagem:** PO/PM prioriza baseado em Impacto x Esforço.
3. **Desenvolvimento:** Item entra no Backlog da Sprint.
4. **Deploy:** Ciclo de Release normal.

---

## 📊 Métricas de Saúde

- **Uptime:** Meta de [99.9]%.
- **Tempo de Resposta (Backend):** Média < [300ms].
- **Taxa de Erros:** < [1]% das requisições.
- **Dívida Técnica:** Itens de refatoração resolvidos por mês.
