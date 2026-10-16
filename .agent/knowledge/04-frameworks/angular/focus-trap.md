---json
{
  "id": "focus-trap",
  "title": "Focus Trap",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Focus Trap.",
  "gatilhos": [
    "angular",
    "focus",
    "frameworks",
    "trap"
  ],
  "perguntas_tipo": [
    "Como utilizar Focus Trap?",
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

### FocusTrap

The `cdkTrapFocus` directive traps <kbd>Tab</kbd> key focus within an element. This is intended to
be used to create accessible experience for components like
[modal dialogs](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/), where focus must be
constrained.

This directive is declared in `A11yModule`.

#### Example

```html
<div class="my-inner-dialog-content" cdkTrapFocus>
  <!-- Tab and Shift + Tab will not leave this element. -->
</div>
```
