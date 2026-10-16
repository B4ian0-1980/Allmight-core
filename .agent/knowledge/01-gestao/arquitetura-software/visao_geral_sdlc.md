---json
{
  "id": "visao_geral_sdlc",
  "title": "🔄 Ciclo de Vida de Desenvolvimento de Software (SDLC)",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🔄 Ciclo de Vida de Desenvolvimento de Software (SDLC).",
  "gatilhos": [
    "arquitetura",
    "ciclo",
    "desenvolvimento",
    "geral",
    "gestao",
    "sdlc",
    "software",
    "vida"
  ],
  "perguntas_tipo": [
    "Como utilizar 🔄 Ciclo de Vida de Desenvolvimento de Software (SDLC)?",
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

# 🔄 Ciclo de Vida de Desenvolvimento de Software (SDLC)

**Versão:** 1.0  
**Status:** Metodologia Padrão

---

## 🎯 Objetivo
Definir as fases e entregáveis do processo de desenvolvimento de software, garantindo qualidade, previsibilidade e alinhamento com os objetivos de negócio.

---

## 🔄 Fases do SDLC

### 1. 📅 Planejamento & Requisitos
- **Entrada:** Solicitação de Negócio.
- **Atividades:**
  - Levantamento de Requisitos Funcionais e Não-Funcionais.
  - Definição de Escopo e MVP.
  - Estimativa de Esforço.
- **Saída:** Documento de Requisitos (`docs/funcionalidades/`).

### 2. 📐 Design & Arquitetura
- **Entrada:** Requisitos Aprovados.
- **Atividades:**
  - Definição da Arquitetura (Camadas, Componentes).
  - Modelagem de Dados.
  - Prototipação UI/UX.
  - Decisões Técnicas (ADRs).
- **Saída:** Documento de Arquitetura (`docs/arquitetura/`) e Protótipos (`docs/ui-ux/`).

### 3. 💻 Desenvolvimento (Implementação)
- **Entrada:** Design Aprovado.
- **Atividades:**
  - Codificação seguindo Padrões de Código.
  - Revisão de Código (Code Review).
  - Testes Unitários.
- **Saída:** Código Fonte Versionado e Buildável.

### 4. 🧪 Testes & Qualidade (QA)
- **Entrada:** Código Implementado.
- **Atividades:**
  - Testes de Integração.
  - Testes End-to-End (E2E).
  - Testes de Segurança e Performance.
- **Saída:** Relatório de Testes e Aprovação de QA.

### 5. 🚀 Deployment & Operação
- **Entrada:** Build Aprovado por QA.
- **Atividades:**
  - Deploy em Staging/Produção.
  - Monitoramento (Logs, Métricas).
- **Saída:** Software em Produção.

### 6. 🔧 Manutenção & Evolução
- **Entrada:** Feedback de Usuários e Bugs.
- **Atividades:**
  - Correção de Bugs (Hotfixes).
  - Melhorias de Performance.
  - Novas Features (Reinicia o ciclo).
- **Saída:** Versões Incrementais.

---

## 📚 Documentos Relacionados
- **[Estratégia de Testes](./TEMPLATE_ESTRATEGIA_TESTES.md)**
- **[Decisões Arquiteturais (ADRs)](./TEMPLATE_ADR.md)**
- **[Exemplos Práticos](../exemplos-por-dominio/)**
