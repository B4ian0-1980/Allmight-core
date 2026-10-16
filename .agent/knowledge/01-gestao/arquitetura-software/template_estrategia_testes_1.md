---json
{
  "id": "template_estrategia_testes_1",
  "title": "🧪 Template - Estratégia de Testes",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🧪 Template - Estratégia de Testes.",
  "gatilhos": [
    "arquitetura",
    "estrategia",
    "gestao",
    "software",
    "template",
    "testes"
  ],
  "perguntas_tipo": [
    "Como utilizar 🧪 Template - Estratégia de Testes?",
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

# 🧪 Template - Estratégia de Testes

**Projeto:** [NOME_DO_PROJETO]
**Data:** [DATA_ATUAL]
**Versão:** 1.0

---

## 🎯 Objetivo
Garantir a qualidade do software através de uma cobertura de testes abrangente e automatizada.

---

## 🏗️ Pirâmide de Testes

### 1. Testes Unitários (70%)
- **Foco:** Funções isoladas, componentes UI, regras de negócio puras.
- **Ferramentas:** [Ex: Jest, Vitest, PHPUnit]
- **Execução:** A cada commit.

### 2. Testes de Integração (20%)
- **Foco:** Comunicação entre módulos, Banco de Dados, APIs.
- **Ferramentas:** [Ex: Testing Library, Laravel Tests]
- **Execução:** No CI (Pull Requests).

### 3. Testes E2E (10%)
- **Foco:** Fluxos críticos do usuário (Login, Checkout).
- **Ferramentas:** [Ex: Playwright, Cypress]
- **Execução:** Nightly ou Pre-release.

---

## ✅ Critérios de Aceite

Para considerar uma feature "Pronta", ela deve ter:
- [ ] Testes unitários cobrindo caminhos felizes e de erro.
- [ ] Testes de integração para novas rotas/APIs.
- [ ] Sem regressões detectadas no CI.

---

## 📝 Padrões de Código de Teste

- **Nomenclatura:** `it('deve realizar tal ação', ...)`
- **Padrão:** Arrange, Act, Assert (AAA).
- **Mocks:** Mockar tudo que for externo (APIs, DB em unitários).

---

## 📊 Métricas de Qualidade

- **Cobertura de Código:** Meta de [80]% (Unitário).
- **Tempo de Execução:** CI deve rodar em menos de [10] min.
