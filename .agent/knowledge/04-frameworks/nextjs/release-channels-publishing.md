---json
{
  "id": "release-channels-publishing",
  "title": "Release Channels and Publishing",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre Release Channels and Publishing.",
  "gatilhos": [
    "and",
    "channels",
    "frameworks",
    "nextjs",
    "publishing",
    "release"
  ],
  "perguntas_tipo": [
    "Como utilizar Release Channels and Publishing?",
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

# Release Channels and Publishing

Next.js has two release channels: `stable` and `canary`.

## Stable

The stable release is what is installed when you `npm install next`. This channel is used by the majority of Next.js users.

This channel is published at a regular cadence and follows [semantic versioning](https://semver.org).

Repository maintainers can publish a new stable version using: `pnpm publish-stable`.
The command will ask what version to publish `major`, `minor`, or `patch`.

## Canary

The canary channel has to be explicitly installed by users through `npm install next@canary`.

This channel is published early based on the `canary` branch. It holds all changes that are waiting to be published to the stable channel.

`canary` is used to test the latest features and bugfixes on real-world applications.

By installing `next@canary` from time to time you can check if your application is affected by any changes that have not been published yet.

Repository maintainers can publish a new canary version using: `pnpm publish-canary`.
The command will automatically decide the new version tag as it's an increment from the previous version.
