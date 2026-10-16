---json
{
  "id": "template_estrategia_testes",
  "title": "🧪 Estratégia de Testes",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🧪 Estratégia de Testes.",
  "gatilhos": [
    "arquitetura",
    "estrategia",
    "gestao",
    "software",
    "template",
    "testes"
  ],
  "perguntas_tipo": [
    "Como utilizar 🧪 Estratégia de Testes?",
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

# 🧪 Estratégia de Testes

**Objetivo:** Garantir a qualidade e confiabilidade do software através de testes automatizados em diferentes níveis.

---

## 🔺 Pirâmide de Testes

### 1. Testes Unitários (Base)
- **Foco:** Funções, classes e componentes isolados.
- **Ferramentas:** [PHPUnit, Jest, JUnit]
- **Volume:** Alto (70% dos testes).
- **Execução:** Rápida, a cada commit.

### 2. Testes de Integração (Meio)
- **Foco:** Interação entre módulos, banco de dados, APIs externas.
- **Ferramentas:** [PHPUnit, Supertest, TestContainers]
- **Volume:** Médio (20% dos testes).
- **Execução:** No CI/CD.

### 3. Testes End-to-End / E2E (Topo)
- **Foco:** Fluxos completos do usuário na interface real.
- **Ferramentas:** [Playwright, Cypress, Selenium]
- **Volume:** Baixo (10% dos testes).
- **Execução:** Antes do deploy (Nightly builds).

---

## 🔍 Tipos Adicionais

- **Testes de Regressão:** Garantir que bugs corrigidos não voltem.
- **Testes de Performance:** Carga e Stress (k6, JMeter).
- **Testes de Segurança:** SAST/DAST (SonarQube, OWASP ZAP).

---

## 🚀 Processo de QA
1. Desenvolvedor escreve teste unitário.
2. CI roda bateria de testes.
3. Code Review valida cobertura.
4. QA valida fluxo E2E.
