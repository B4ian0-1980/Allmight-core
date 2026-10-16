---json
{
  "id": "index_10",
  "title": "Index 10",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Index 10.",
  "gatilhos": [
    "frameworks",
    "index",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar Index 10?",
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

---
page: true
title: Tutorial
sidebar: false
aside: false
footer: false
returnToTop: false
---

<script>
import { defineAsyncComponent } from 'vue'
import ReplLoading from '@theme/components/ReplLoading.vue'

export default {
  components: {
    TutorialRepl: defineAsyncComponent({
      loader: () => import('./TutorialRepl.vue'),
      loadingComponent: ReplLoading
    })
  }
}
</script>

<ClientOnly>
  <TutorialRepl />
</ClientOnly>
