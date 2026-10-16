---json
{
  "id": "add-new-provider",
  "title": "Add new provider",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre Add new provider.",
  "gatilhos": [
    "add",
    "frameworks",
    "new",
    "nextjs",
    "provider"
  ],
  "perguntas_tipo": [
    "Como utilizar Add new provider?",
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

# Add new provider

## `@ai-sdk/<provider>` vs 3rd party package

Every provider is welcome to create a 3rd party package. We are happy to link to it from our documentation.

If you would prefer a 1st party `@ai-sdk/<provider>` package, please create an issue first to discuss.

## Example

https://github.com/vercel/ai/pull/8136/files

## How

1. Create new folder `packages/<provider>`
2. Set version in `packages/<provider>/package.json` to `0.0.0`
3. Create changeset for new package with `major`
4. Add examples to `examples/ai-functions/src/*/<provider>.ts` depending on what model types the provider supports
5. Add documentation in `content/providers/01-ai-sdk-providers/<last number + 10>-<provider>.mdx`

See also [providers.md](providers.md)

## When in pre-release mode

If `main` is set up to publish `beta` releases, no further action is necessary. Just make sure not to backport it to the `vX.Y` stable branch since it will result in an npm version conflict once we exit pre-release mode on `main`
