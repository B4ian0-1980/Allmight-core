---json
{
  "id": "interactivity-checker",
  "title": "Interactivity Checker",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Interactivity Checker.",
  "gatilhos": [
    "angular",
    "checker",
    "frameworks",
    "interactivity"
  ],
  "perguntas_tipo": [
    "Como utilizar Interactivity Checker?",
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

### InteractivityChecker
`InteractivityChecker` is used to check the interactivity of an element, capturing disabled,
visible, tabbable, and focusable states for accessibility purposes.

#### Methods

##### `isDisabled(element: HTMLElement): boolean` 
Whether the given element is disabled.

##### `isVisible(element: HTMLElement): boolean` 
Whether the given element is visible. 

This will capture states like `display: none` and `visibility: hidden`,
but not things like being clipped by an `overflow: hidden` parent or being outside the viewport.

##### `isFocusable(element: HTMLElement): boolean` 
Gets whether an element can be focused by the user.

##### `isTabbable(element: HTMLElement): boolean` 
Gets whether an element can be reached via Tab key. 
Assumes that the element has already been checked with isFocusable.
