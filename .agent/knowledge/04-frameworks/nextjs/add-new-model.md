---json
{
  "id": "add-new-model",
  "title": "Adding a new model",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre Adding a new model.",
  "gatilhos": [
    "add",
    "adding",
    "frameworks",
    "model",
    "new",
    "nextjs"
  ],
  "perguntas_tipo": [
    "Como utilizar Adding a new model?",
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

# Adding a new model

1. Add model id to settings (model ids) for auto-complete
1. Add model id to list in provider page under `/content/providers/...` (Model Capabilities table at the bottom)
1. If the model is notable, add to
   - `content/providers/01-ai-sdk-providers/index.mdx`
   - `content/docs/02-foundations/02-providers-and-models.mdx`
1. PR with changeset
1. NPM publish through Changesets PR

Example PR: https://github.com/vercel/ai/pull/7313
