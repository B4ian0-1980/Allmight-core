---json
{
  "id": "description_11",
  "title": "Conditional Rendering {#conditional-rendering}",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Conditional Rendering {#conditional-rendering}.",
  "gatilhos": [
    "conditional",
    "conditional-rendering",
    "description",
    "frameworks",
    "rendering",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar Conditional Rendering {#conditional-rendering}?",
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

# Conditional Rendering {#conditional-rendering}

We can use the `v-if` directive to conditionally render an element:

```vue-html
<h1 v-if="awesome">Vue is awesome!</h1>
```

This `<h1>` will be rendered only if the value of `awesome` is [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy). If `awesome` changes to a [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy) value, it will be removed from the DOM.

We can also use `v-else` and `v-else-if` to denote other branches of the condition:

```vue-html
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```

Currently, the demo is showing both `<h1>`s at the same time, and the button does nothing. Try to add `v-if` and `v-else` directives to them, and implement the `toggle()` method so that we can use the button to toggle between them.

More details on `v-if`: <a target="_blank" href="/guide/essentials/conditional.html">Guide - Conditional Rendering</a>
