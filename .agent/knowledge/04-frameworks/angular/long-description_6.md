---json
{
  "id": "long-description_6",
  "title": "Long Description 6",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Long Description 6.",
  "gatilhos": [
    "angular",
    "description",
    "frameworks",
    "long"
  ],
  "perguntas_tipo": [
    "Como utilizar Long Description 6?",
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
When a project name is not supplied, executes the `lint` builder for all projects.

To use the `ng lint` command, use `ng add` to add a package that implements linting capabilities. Adding the package automatically updates your workspace configuration, adding a lint [CLI builder](tools/cli/cli-builder).
For example:

```json
"projects": {
  "my-project": {
    ...
    "architect": {
      ...
      "lint": {
        "builder": "@angular-eslint/builder:lint",
        "options": {}
      }
    }
  }
}
```
