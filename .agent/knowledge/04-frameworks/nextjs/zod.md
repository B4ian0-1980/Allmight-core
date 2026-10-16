---json
{
  "id": "zod",
  "title": "Zod and AI SDK",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre Zod and AI SDK.",
  "gatilhos": [
    "and",
    "frameworks",
    "nextjs",
    "sdk",
    "zod"
  ],
  "perguntas_tipo": [
    "Como utilizar Zod and AI SDK?",
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

# Zod and AI SDK

## Background

The AI SDK allows users to use Zod 3, Zod 4, and Zod 4 mini schemas directly.

Incorrect internal implementations can lead to infinite recursion and OOM issues such as [#7351](https://github.com/vercel/ai/issues/7351).

## Rules

For Zod 3 usage (only required in compatibility code, e.g. parsing):

- always use `import * as z3 from "zod/v3";`

For Zod 4 usage:

- always use `import * as z4 from "zod/v4";`
- always use `z4.core.$ZodType`

## Future Work

- set up linter to ensure imports are correct

## Related issues

- [OOM bug report](https://github.com/vercel/ai/issues/7351)

## References

- [Zod library authors guide](https://zod.dev/library-authors)
