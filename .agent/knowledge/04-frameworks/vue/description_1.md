---json
{
  "id": "description_1",
  "title": "Watchers {#watchers}",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Watchers {#watchers}.",
  "gatilhos": [
    "description",
    "frameworks",
    "vue",
    "watchers"
  ],
  "perguntas_tipo": [
    "Como utilizar Watchers {#watchers}?",
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

# Watchers {#watchers}

Sometimes we may need to perform "side effects" reactively - for example, logging a number to the console when it changes. We can achieve this with watchers:

<div class="composition-api">

```js
import { ref, watch } from 'vue'

const count = ref(0)

watch(count, (newCount) => {
  // yes, console.log() is a side effect
  console.log(`new count is: ${newCount}`)
})
```

`watch()` can directly watch a ref, and the callback gets fired whenever `count`'s value changes. `watch()` can also watch other types of data sources - more details are covered in <a target="_blank" href="/guide/essentials/watchers.html">Guide - Watchers</a>.

</div>
<div class="options-api">

```js
export default {
  data() {
    return {
      count: 0
    }
  },
  watch: {
    count(newCount) {
      // yes, console.log() is a side effect
      console.log(`new count is: ${newCount}`)
    }
  }
}
```

Here, we are using the `watch` option to watch changes to the `count` property. The watch callback is called when `count` changes, and receives the new value as the argument. More details are covered in <a target="_blank" href="/guide/essentials/watchers.html">Guide - Watchers</a>.

</div>

A more practical example than logging to the console would be fetching new data when an ID changes. The code we have is fetching todos data from a mock API on component mount. There is also a button that increments the todo ID that should be fetched. Try to implement a watcher that fetches a new todo when the button is clicked.
