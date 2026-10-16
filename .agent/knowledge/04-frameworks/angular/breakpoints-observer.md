---json
{
  "id": "breakpoints-observer",
  "title": "Breakpoints Observer",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Breakpoints Observer.",
  "gatilhos": [
    "angular",
    "breakpoints",
    "frameworks",
    "observer"
  ],
  "perguntas_tipo": [
    "Como utilizar Breakpoints Observer?",
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

### BreakpointsModule

When including the CDK's `LayoutModule`, components can inject `BreakpointsObserver` to request
the matching state of a CSS Media Query.

A set of breakpoints is provided based on the Material Design
[breakpoint system](https://material.io/guidelines/layout/responsive-ui.html#responsive-ui-breakpoints).

#### Example
```ts
@Component({ ... })
export class MyWidget {
  isHandset: Observable<BreakpointState>;

  constructor(bm: BreakpointObserver) {
    bm.observe(Handset).subscribe((state: BreakpointState) => {
      if (state.matches) {
        this.makeEverythingFitOnSmallScreen();
      } else {
        this.expandEverythingToFillTheScreen();
      }
    });
  }
}
```

