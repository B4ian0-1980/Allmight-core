---json
{
  "id": "model-setup",
  "title": "How to set up a new LLM?",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre How to set up a new LLM?.",
  "gatilhos": [
    "angular",
    "frameworks",
    "how",
    "llm",
    "model",
    "new",
    "set",
    "setup"
  ],
  "perguntas_tipo": [
    "Como utilizar How to set up a new LLM??",
    "Quais as boas praticas de angular?"
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
  "dono": "stack-angular",
  "prioridade": 2
}
---

# How to set up a new LLM?

If you want to test out a model that isn't yet available in the runner, you can add
support for it by following these steps:

1. Ensure that the provider of the model is supported by [AI SDK](https://ai-sdk.dev/).
2. Find the provider for the model in `runner/codegen/ai-sdk`. If the provider doesn't exist,
implement it by following the pattern from the existing providers.
3. Add your model to the `SUPPORTED_MODELS` array.
4. Done! 🎉 You can now run your model by passing `--model=<your model ID>`.
