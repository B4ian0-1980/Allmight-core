---json
{
  "id": "adding-error-links",
  "title": "Adding Warning and Error Descriptions",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre Adding Warning and Error Descriptions.",
  "gatilhos": [
    "adding",
    "and",
    "descriptions",
    "error",
    "frameworks",
    "links",
    "nextjs",
    "warning"
  ],
  "perguntas_tipo": [
    "Como utilizar Adding Warning and Error Descriptions?",
    "Quais as boas praticas de nextjs?"
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
  "dono": "stack-nextjs",
  "prioridade": 2
}
---

# Adding Warning and Error Descriptions

Next.js has a system to add helpful links to warnings and errors.

This allows the logged message to be short while giving a broader description and instructions on how to solve the warning/error on the documentation.

In general, all warnings and errors added should have these links attached.

Below are the steps to add a new link:

1. Run `pnpm new-error` which will create the error document and update the manifest automatically.
2. At the end of the command the URL for the error will be provided, add that to your error.
