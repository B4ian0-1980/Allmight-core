---json
{
  "id": "observers",
  "title": "Observers",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Observers.",
  "gatilhos": [
    "angular",
    "frameworks",
    "observers"
  ],
  "perguntas_tipo": [
    "Como utilizar Observers?",
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

The `observers` package provides convenience directives built on top of native web platform
observers, such as MutationObserver.


### cdkObserveContent

A directive for observing when the content of the host element changes. An event is emitted when a
mutation to the content is observed.

```html
<div class="projected-content-wrapper" (cdkObserveContent)="projectContentChanged()">
  <ng-content></ng-content>
</div>
```

Directive also can be used for observing any type of content
```html
<div class="content-wrapper" (click)="changeText()" (cdkObserveContent)="textChanged()">
  {{ text }}
</div>
```
