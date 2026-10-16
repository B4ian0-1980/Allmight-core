---json
{
  "id": "documentacao-vue",
  "title": "Documentação Vue.js (Guia Rápido & Oficial)",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Documentação Vue.js (Guia Rápido & Oficial).",
  "gatilhos": [
    "documentacao",
    "frameworks",
    "guia",
    "oficial",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Vue.js (Guia Rápido & Oficial)?",
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

# Documentação Vue.js (Guia Rápido & Oficial)

**Fonte:** [https://vuejs.org/](https://vuejs.org/)

---

## 1. Visão Geral

Vue (pronuncia-se /vjuː/, como "view") é um framework JavaScript progressivo para construção de interfaces de usuário.
Ele constrói sobre o padrão HTML, CSS e JavaScript e fornece um modelo de programação declarativo e baseado em componentes.

---

## 2. Criando uma Aplicação Vue

### Pré-requisitos
*   Node.js instalado (v18.3 ou superior recomendado).

### Scaffolding (Criação Rápida)
Execute o seguinte comando no terminal:

```bash
npm create vue@latest
```

Você responderá a algumas perguntas (TypeScript, JSX, Router, Pinia, etc.).
Para iniciantes, "No" é uma opção segura para a maioria, exceto talvez Vue Router se for uma SPA.

Após criar:
```bash
cd <nome-do-projeto>
npm install
npm run dev
```

### Opção via CDN (Sem Build)
Para usar em uma página HTML existente sem Node.js:
```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

<div id="app">{{ message }}</div>

<script>
  const { createApp, ref } = Vue

  createApp({
    setup() {
      const message = ref('Hello Vue!')
      return { message }
    }
  }).mount('#app')
</script>
```

---

## 3. Conceitos Chave (Composition API)

O Vue 3 recomenda o uso da **Composition API** com `<script setup>` para componentes Single-File (SFC).

### Exemplo de Componente (.vue)

```vue
<script setup>
import { ref } from 'vue'

// Estado reativo
const count = ref(0)

// Funções (Métodos)
function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">
    Contagem é: {{ count }}
  </button>
</template>

<style scoped>
button {
  font-weight: bold;
}
</style>
```

*   **Reatividade:** `ref()` cria uma variável reativa. Acesse `.value` no script, mas apenas o nome no template.
*   **Eventos:** `@click` (atalho para `v-on:click`).
*   **Interpolação:** `{{ }}` para texto dinâmico.

---

## 4. Bindings e Diretivas

*   **v-bind (:)**: Liga atributos HTML a váriaveis JS.
    ```html
    <div :id="dynamicId"></div>
    ```
*   **v-model**: Ligação de mão dupla (Two-way binding) para formulários.
    ```html
    <input v-model="text">
    ```
*   **v-if / v-else**: Renderização condicional.
    ```html
    <h1 v-if="awesome">Vue é incrível!</h1>
    ```
*   **v-for**: Renderização de listas.
    ```html
    <li v-for="item in items" :key="item.id">
      {{ item.text }}
    </li>
    ```
