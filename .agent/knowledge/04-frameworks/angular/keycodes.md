---json
{
  "id": "keycodes",
  "title": "Keycodes",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Keycodes.",
  "gatilhos": [
    "angular",
    "frameworks",
    "keycodes"
  ],
  "perguntas_tipo": [
    "Como utilizar Keycodes?",
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

### KeyCodes
 
Commonly used keycode constants.

#### Example
```ts
import {Directive} from '@angular/core';
import {UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW} from '@angular/cdk/keycodes';

@Directive({
  selector: '[count-arrows]'
  host: {
    (keypress): 'handleKeyPress($event)'
  }
})
export class ArrowCounterDirective {
  arrowPressCount = 0;

  handleKeyPress(event: KeyboardEvent) {
    if ([UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW].includes(event.keyCode)) {
      this.arrowPresscount++;
    }
  }
}
```

