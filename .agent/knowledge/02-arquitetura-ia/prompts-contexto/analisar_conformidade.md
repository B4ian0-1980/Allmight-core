---json
{
  "id": "analisar_conformidade",
  "title": "Workflow: Análise de Conformidade e Padrões",
  "categoria": "02-arquitetura-ia",
  "subcategoria": "prompts-contexto",
  "resumo": "Guia tecnico e referencias sobre Workflow: Análise de Conformidade e Padrões.",
  "gatilhos": [
    "analisar",
    "arquitetura",
    "conformidade",
    "contexto",
    "prompts",
    "workflow"
  ],
  "perguntas_tipo": [
    "Como utilizar Workflow: Análise de Conformidade e Padrões?",
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

---
description: Analisar conformidade do código com a arquitetura base
---

# Workflow: Análise de Conformidade e Padrões

Este workflow deve ser acionado quando o usuário solicitar uma revisão de código ou mencionar `@[base-estrutura-projeto]`.

## Passos

1.  **Identificar o Contexto**
    - Verificar qual linguagem/framework está sendo usado no arquivo aberto pelo usuário.
    - Localizar a documentação correspondente em `biblioteca/`.

2.  **Verificar Padrões Arquiteturais**
    - Consultar `docs/arquitetura/` para verificar se o código segue a estrutura de pastas recomendada (ex: MVC, Clean Architecture).
    - Comparar com exemplos em `biblioteca/receitas-codigo`.

3.  **Verificar Regras de Negócio**
    - Se o código implementa uma funcionalidade específica, buscar em `docs/funcionalidades/` se existem regras documentadas para ela.

4.  **Verificar Stack Tecnológica**
    - Confirmar se as bibliotecas importadas estão na lista de "aprovadas" ou "documentadas" em `biblioteca/backend` ou `biblioteca/frontend`.
    - Se uma biblioteca nova for usada, alertar o usuário ou sugerir adicionar à documentação.

5.  **Relatório**
    - Gerar um breve relatório citando:
        - Conformidade com a Arquitetura (✅/❌)
        - Adesão às Regras de Negócio (✅/❌)
        - Uso de Tecnologias Padronizadas (✅/❌)
        - Sugestões de melhoria baseadas na `biblioteca`.
