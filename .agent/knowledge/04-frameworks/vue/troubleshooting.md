---json
{
  "id": "troubleshooting",
  "title": "Trouble Shooting",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Trouble Shooting.",
  "gatilhos": [
    "frameworks",
    "shooting",
    "trouble",
    "troubleshooting",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar Trouble Shooting?",
    "Quais as boas praticas de vue?"
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
  "dono": "stack-vue",
  "prioridade": 2
}
---

# Trouble Shooting

## DevTools (vite plugin) doesn't render as expected

If you see devtools render as follows:

![issue image](/screenshots/nested-issue.png)

And you are using `vite-plugin-html`, please make sure register `vite-plugin-vue-devtools` before `vite-plugin-html`.

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import { createHtmlPlugin } from 'vite-plugin-html'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
  plugins: [
    // register vueDevTools before createHtmlPlugin
    vueDevTools(),
    createHtmlPlugin({})
  ]
})
```
