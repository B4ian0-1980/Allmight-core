---json
{
  "id": "live-announcer",
  "title": "Live Announcer",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Live Announcer.",
  "gatilhos": [
    "angular",
    "announcer",
    "frameworks",
    "live"
  ],
  "perguntas_tipo": [
    "Como utilizar Live Announcer?",
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

### LiveAnnouncer
`LiveAnnouncer` is used to announce messages for screen-reader users using an `aria-live` region.
See [the W3C's WAI-ARIA](https://www.w3.org/TR/wai-aria/states_and_properties#aria-live)
for more information on aria-live regions.

#### Methods

##### `announce(message: string, politeness?: 'off' | 'polite' | 'assertive'): void`
Announce the given message via aria-live region. The politeness argument determines the
`aria-live` attribute on the announcer element, defaulting to 'polite'.

#### Examples
The LiveAnnouncer is injected into a component:
```ts
@Component({
  selector: 'my-component'
  providers: [LiveAnnouncer]
})
export class MyComponent {

  constructor(liveAnnouncer: LiveAnnouncer) {
    liveAnnouncer.announce("Hey Google");
  }
}
```
