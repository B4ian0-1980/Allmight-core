---json
{
  "id": "media-matcher",
  "title": "Media Matcher",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Media Matcher.",
  "gatilhos": [
    "angular",
    "frameworks",
    "matcher",
    "media"
  ],
  "perguntas_tipo": [
    "Como utilizar Media Matcher?",
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

### MediaMatcher
 
When including the CDK's `LayoutModule`, components can inject `MediaMatcher` to access the 
matchMedia method, if available on the platform.

#### Example
```ts
@Component({ ... }) 
export class MyWidget {  
  constructor(mm: MediaMatcher) {
    mm.matchMedia('(orientation: landscape)').matches ? 
      this.setLandscapeMode() :
      this.setPortraitMode();
  }
}  
```

