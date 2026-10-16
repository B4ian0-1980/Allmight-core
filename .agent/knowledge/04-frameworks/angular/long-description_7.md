---json
{
  "id": "long-description_7",
  "title": "Long Description 7",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Long Description 7.",
  "gatilhos": [
    "angular",
    "description",
    "frameworks",
    "long"
  ],
  "perguntas_tipo": [
    "Como utilizar Long Description 7?",
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

Creates and initializes a new Angular application that is the default project for a new workspace.

Provides interactive prompts for optional configuration, such as adding routing support.
All prompts can safely be allowed to default.

- The new workspace folder is given the specified project name, and contains configuration files at the top level.

- By default, the files for a new initial application (with the same name as the workspace) are placed in the `src/` subfolder.
- The new application's configuration appears in the `projects` section of the `angular.json` workspace configuration file, under its project name.

- Subsequent applications that you generate in the workspace reside in the `projects/` subfolder.

If you plan to have multiple applications in the workspace, you can create an empty workspace by using the `--no-create-application` option.
You can then use `ng generate application` to create an initial application.
This allows a workspace name different from the initial app name, and ensures that all applications reside in the `/projects` subfolder, matching the structure of the configuration file.
