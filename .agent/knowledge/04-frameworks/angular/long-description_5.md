---json
{
  "id": "long-description_5",
  "title": "Long Description 5",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Long Description 5.",
  "gatilhos": [
    "angular",
    "description",
    "frameworks",
    "long"
  ],
  "perguntas_tipo": [
    "Como utilizar Long Description 5?",
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

The command takes an optional project name, as specified in the `projects` section of the `angular.json` workspace configuration file.
When a project name is not supplied, executes the `deploy` builder for the default project.

To use the `ng deploy` command, use `ng add` to add a package that implements deployment capabilities to your favorite platform.
Adding the package automatically updates your workspace configuration, adding a deployment
[CLI builder](tools/cli/cli-builder).
For example:

```json
"projects": {
  "my-project": {
    ...
    "architect": {
      ...
      "deploy": {
        "builder": "@angular/fire:deploy",
        "options": {}
      }
    }
  }
}
```
