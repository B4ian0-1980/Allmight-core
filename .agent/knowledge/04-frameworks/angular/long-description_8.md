---json
{
  "id": "long-description_8",
  "title": "Long Description 8",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Long Description 8.",
  "gatilhos": [
    "angular",
    "description",
    "frameworks",
    "long"
  ],
  "perguntas_tipo": [
    "Como utilizar Long Description 8?",
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

Architect is the tool that the CLI uses to perform complex tasks such as compilation, according to provided configurations.
The CLI commands run Architect targets such as `build`, `serve`, `test`, and `lint`.
Each named target has a default configuration, specified by an `options` object,
and an optional set of named alternate configurations in the `configurations` object.

For example, the `serve` target for a newly generated app has a predefined
alternate configuration named `production`.

You can define new targets and their configuration options in the `architect` section
of the `angular.json` file which you can run them from the command line using the `ng run` command.
