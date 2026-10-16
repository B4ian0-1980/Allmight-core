---json
{
  "id": "description_3",
  "title": "Props {#props}",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Props {#props}.",
  "gatilhos": [
    "description",
    "frameworks",
    "props",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar Props {#props}?",
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

# Props {#props}

A child component can accept input from the parent via **props**. First, it needs to declare the props it accepts:

<div class="composition-api">
<div class="sfc">

```vue [ChildComp.vue]
<script setup>
const props = defineProps({
  msg: String
})
</script>
```

Note `defineProps()` is a compile-time macro and doesn't need to be imported. Once declared, the `msg` prop can be used in the child component's template. It can also be accessed in JavaScript via the returned object of `defineProps()`.

</div>

<div class="html">

```js
// in child component
export default {
  props: {
    msg: String
  },
  setup(props) {
    // access props.msg
  }
}
```

Once declared, the `msg` prop is exposed on `this` and can be used in the child component's template. The received props are passed to `setup()` as the first argument.

</div>

</div>

<div class="options-api">

```js
// in child component
export default {
  props: {
    msg: String
  }
}
```

Once declared, the `msg` prop is exposed on `this` and can be used in the child component's template.

</div>

The parent can pass the prop to the child just like attributes. To pass a dynamic value, we can also use the `v-bind` syntax:

<div class="sfc">

```vue-html
<ChildComp :msg="greeting" />
```

</div>
<div class="html">

```vue-html
<child-comp :msg="greeting"></child-comp>
```

</div>

Now try it yourself in the editor.
