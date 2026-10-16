---json
{
  "id": "description_8",
  "title": "Attribute Bindings {#attribute-bindings}",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Attribute Bindings {#attribute-bindings}.",
  "gatilhos": [
    "attribute",
    "attribute-bindings",
    "bindings",
    "description",
    "frameworks",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar Attribute Bindings {#attribute-bindings}?",
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

# Attribute Bindings {#attribute-bindings}

In Vue, mustaches are only used for text interpolation. To bind an attribute to a dynamic value, we use the `v-bind` directive:

```vue-html
<div v-bind:id="dynamicId"></div>
```

A **directive** is a special attribute that starts with the `v-` prefix. They are part of Vue's template syntax. Similar to text interpolations, directive values are JavaScript expressions that have access to the component's state. The full details of `v-bind` and directive syntax are discussed in <a target="_blank" href="/guide/essentials/template-syntax.html">Guide - Template Syntax</a>.

The part after the colon (`:id`) is the "argument" of the directive. Here, the element's `id` attribute will be synced with the `dynamicId` property from the component's state.

Because `v-bind` is used so frequently, it has a dedicated shorthand syntax:

```vue-html
<div :id="dynamicId"></div>
```

Now, try to add a dynamic `class` binding to the `<h1>`, using the `titleClass` <span class="options-api">data property</span><span class="composition-api">ref</span> as its value. If it's bound correctly, the text should turn red.
