---json
{
  "id": "accordion",
  "title": "Accordion",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Accordion.",
  "gatilhos": [
    "accordion",
    "angular",
    "frameworks"
  ],
  "perguntas_tipo": [
    "Como utilizar Accordion?",
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

An accordion is a component with one or more expandable sections. CDK accordion provides a
foundation upon which you can build your own custom accordion component. CDK accordion provides
logic for the accordion interaction pattern without any styles. You can customize the accordion's
appearance based on your application's needs.

<!-- example(cdk-accordion-overview) -->

### Accessibility
The CDK accordion doesn't come with any accessibility treatment, because it doesn't have control
over its markup. We recommend to set the accordion trigger element as a `role="button"` while
the body container as a `role="region"`. Furthermore, the trigger should have `aria-controls`
pointing to the body and `aria-expanded` based on the expanded state, while the body should have
an `aria-labelledby` that points to the header. See the example above for a sample implementation.
