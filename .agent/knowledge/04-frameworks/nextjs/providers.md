---json
{
  "id": "providers",
  "title": "Provider Development Notes",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre Provider Development Notes.",
  "gatilhos": [
    "development",
    "frameworks",
    "nextjs",
    "notes",
    "provider",
    "providers"
  ],
  "perguntas_tipo": [
    "Como utilizar Provider Development Notes?",
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

# Provider Development Notes

## Provider Options Schemas

Provider options schemas are user facing.
We want them to be as restrictive as possible, so that we have more flexibility with future changes and allow for meaningful `null` values.

- use `.optional()` unless `null` is meaningful

## Response Schemas

Response schemas need to be flexible enough to deal with provider API changes that do not affect our processing
to prevent unnecessary breakages.

- keep them minimal (no unused properties)
- use `.nullish()` instead of `.optional()`

## Provider Method Names

For the Provider v2 interface, we require fully specified names with a "Model" suffix,
e.g. `languageModel(id)` or `imageModel(id)`.
However, for DX reasons it is very useful to have shorter alias names,
e.g. `.chat(id)` or `.image(id)`.
