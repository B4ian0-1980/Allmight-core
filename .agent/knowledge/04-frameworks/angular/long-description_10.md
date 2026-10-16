---json
{
  "id": "long-description_10",
  "title": "Long Description 10",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Long Description 10.",
  "gatilhos": [
    "angular",
    "description",
    "frameworks",
    "long"
  ],
  "perguntas_tipo": [
    "Como utilizar Long Description 10?",
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

Perform a basic update to the current stable release of the core framework and CLI by running the following command.

```
ng update @angular/cli @angular/core
```

To update to the next beta or pre-release version, use the `--next` option.

To update from one major version to another, use the format

```
ng update @angular/cli@^<major_version> @angular/core@^<major_version>
```

We recommend that you always update to the latest patch version, as it contains fixes we released since the initial major release.
For example, use the following command to take the latest 10.x.x version and use that to update.

```
ng update @angular/cli@^10 @angular/core@^10
```

For detailed information and guidance on updating your application, see the interactive [Angular Update Guide](https://update.angular.dev/).
