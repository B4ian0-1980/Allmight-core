---json
{
  "id": "00_template_especificacao",
  "title": "📝 Template de Especificação de Sistema",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "prompts-contexto",
  "resumo": "**Como usar:** Copie este texto, preencha os dados da sua ideia e cole no chat junto com o prompt `04_AGENTE_ARQUITETO.md`.",
  "gatilhos": [
    "arquitetura",
    "contexto",
    "especificacao",
    "prompts",
    "sistema",
    "template"
  ],
  "perguntas_tipo": [
    "Como utilizar 📝 Template de Especificação de Sistema?",
    "Quais as boas praticas de prompts-contexto?"
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
  "dono": "stack-prompts-contexto",
  "prioridade": 2
}
---

# 📝 Template de Especificação de Sistema

Use este modelo para fornecer informações ao **Agente Arquiteto (04)**. Quanto mais detalhes, melhor o projeto.

---

## 1. Visão Geral
*   **Nome do Sistema:** (Ex: Sistema de Gestão de Peixaria - "PescaSys")
*   **Objetivo:** (Ex: Controlar estoque de peixes, vendas diárias e cadastro de clientes.)
*   **Público-Alvo:** (Ex: Caixas, Gerente e Clientes Finais via App.)

## 2. Funcionalidades Principais (Requisitos Funcionais)
Liste o que o sistema DEVE fazer:
*   [ ] Login e Autenticação (Admin vs Usuário Comum)
*   [ ] Cadastro de Produtos (Peixes, Frutos do Mar) com foto e preço/kg.
*   [ ] Registro de Vendas (PDV) com cálculo automático.
*   [ ] Emissão de Nota Fiscal (Opcional/Futuro).
*   [ ] Relatório de Vendas Mensal.

## 3. Preferências Técnicas (Opcional)
*   **Plataforma:** (Ex: Web Responsivo, só Desktop, Mobile App?)
*   **Stack Preferida:** (Ex: "Prefiro PHP com Laravel pois tenho XAMPP" ou "Quero React com Node").
*   **Design:** (Ex: "Quero algo limpo, estilo Dashboard AdminLTE").

## 4. Regras de Negócio Importantes
*   (Ex: Não pode vender peixe com estoque zerado.)
*   (Ex: Clientes VIP têm 10% de desconto.)

---

> **Como usar:** Copie este texto, preencha os dados da sua ideia e cole no chat junto com o prompt `04_AGENTE_ARQUITETO.md`.
