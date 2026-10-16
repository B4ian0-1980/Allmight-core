---json
{
  "id": "padroes-vuejs3",
  "title": "📐 Padrões de Código Vue.js 3",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 📐 Padrões de Código Vue.js 3.",
  "gatilhos": [
    "frameworks",
    "padroes",
    "vue",
    "vuejs3"
  ],
  "perguntas_tipo": [
    "Como utilizar 📐 Padrões de Código Vue.js 3?",
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

# 📐 Padrões de Código Vue.js 3

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Padrões e Boas Práticas

---

## 🎯 Objetivo

Este documento consolida **todos os padrões de código Vue.js 3** que devem ser seguidos ao desenvolver com Vue.js 3.

**Baseado em:**
- ✅ Vue.js 3 Official Style Guide
- ✅ Repositórios oficiais Vue.js 3
- ✅ Best practices da comunidade
- ✅ Material didático validado

---

## 📋 Convenções de Nomenclatura

### Componentes

**✅ PascalCase para componentes:**
```vue
<!-- MyComponent.vue -->
<script setup>
// ...
</script>
```

**✅ kebab-case para uso em templates:**
```vue
<template>
  <my-component />
  <user-profile />
</template>
```

---

### Props

**✅ camelCase para props:**
```vue
<script setup>
defineProps({
  userName: String,
  userEmail: String
})
</script>
```

**✅ kebab-case para uso em templates:**
```vue
<template>
  <user-card 
    :user-name="name"
    :user-email="email"
  />
</template>
```

---

### Variáveis e Funções

**✅ camelCase:**
```javascript
const userName = ref('')
const fetchUserData = () => {}
```

---

## 🏗️ Estrutura de Componente

### Ordem Padrão

```vue
<template>
  <!-- Template primeiro -->
</template>

<script setup>
// 1. Imports
import { ref, computed } from 'vue'
import MyComponent from './MyComponent.vue'

// 2. Props
defineProps({
  // ...
})

// 3. Emits
defineEmits(['event-name'])

// 4. Composables
const { data } = useFetch()

// 5. Reactive state
const count = ref(0)

// 6. Computed
const double = computed(() => count.value * 2)

// 7. Methods
function increment() {
  count.value++
}

// 8. Lifecycle hooks
onMounted(() => {
  // ...
})
</script>

<style scoped>
/* Estilos por último */
</style>
```

---

## 📦 Composition API

### Sempre Use `<script setup>`

**✅ BOM:**
```vue
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>
```

**❌ EVITE:**
```vue
<script>
export default {
  setup() {
    return { count: ref(0) }
  }
}
</script>
```

---

### ref() vs reactive()

**Use `ref()` para:**
- ✅ Valores primitivos (string, number, boolean)
- ✅ Quando precisa reatividade simples

```javascript
const count = ref(0)
const name = ref('João')
const isActive = ref(true)
```

**Use `reactive()` para:**
- ✅ Objetos complexos
- ✅ Quando precisa reatividade profunda

```javascript
const user = reactive({
  name: 'João',
  email: 'joao@example.com',
  profile: {
    age: 30
  }
})
```

---

## 🎯 Diretivas

### v-if vs v-show

**Use `v-if` quando:**
- ✅ Condição raramente muda
- ✅ Componente pesado
- ✅ Precisa remover do DOM

**Use `v-show` quando:**
- ✅ Toggle frequente
- ✅ Componente leve
- ✅ Apenas ocultar/mostrar

---

### v-for

**Sempre use `:key` único:**
```vue
<!-- ✅ BOM -->
<li v-for="item in items" :key="item.id">
  {{ item.name }}
</li>

<!-- ❌ EVITE -->
<li v-for="item in items">
  {{ item.name }}
</li>
```

**Evite usar índice como key:**
```vue
<!-- ⚠️ Use apenas se não houver ID único -->
<li v-for="(item, index) in items" :key="index">
  {{ item.name }}
</li>
```

---

## 🔄 Reatividade

### Acessando Valores

**ref() precisa `.value`:**
```javascript
const count = ref(0)
count.value++  // ✅ Correto
count++         // ❌ Errado
```

**reactive() não precisa `.value`:**
```javascript
const user = reactive({ name: 'João' })
user.name = 'Maria'  // ✅ Correto
```

---

### Destructuring Reativo

**❌ Perde reatividade:**
```javascript
const user = reactive({ name: 'João', email: 'joao@example.com' })
const { name, email } = user  // ❌ Não é reativo!
```

**✅ Mantém reatividade:**
```javascript
import { toRefs } from 'vue'
const user = reactive({ name: 'João', email: 'joao@example.com' })
const { name, email } = toRefs(user)  // ✅ Reativo!
```

---

## 🎣 Composables

### Estrutura de Composable

```javascript
// composables/useFeature.js
import { ref, computed, onMounted } from 'vue'

export function useFeature(initialValue) {
  // 1. Estado
  const state = ref(initialValue)
  
  // 2. Computed
  const double = computed(() => state.value * 2)
  
  // 3. Métodos
  function increment() {
    state.value++
  }
  
  // 4. Lifecycle (se necessário)
  onMounted(() => {
    // Setup
  })
  
  // 5. Retornar API pública
  return {
    state,
    double,
    increment
  }
}
```

---

### Nomenclatura de Composables

**✅ Sempre comece com `use`:**
```javascript
useCounter()
useFetch()
useAuth()
useLocalStorage()
```

---

## 📤 Props e Emits

### Props com Validação

```vue
<script setup>
defineProps({
  // Tipo simples
  title: String,
  
  // Múltiplos tipos
  id: [String, Number],
  
  // Com default
  count: {
    type: Number,
    default: 0
  },
  
  // Obrigatório
  name: {
    type: String,
    required: true
  },
  
  // Validação customizada
  email: {
    type: String,
    validator: (value) => {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)
    }
  }
})
</script>
```

---

### Emits Tipados

```vue
<script setup>
const emit = defineEmits({
  // Sem validação
  'update:modelValue': null,
  
  // Com validação
  'submit': (payload) => {
    return payload && typeof payload === 'object'
  }
})

// Uso
emit('update:modelValue', newValue)
emit('submit', { data: 'value' })
</script>
```

---

## 🎨 Estilos

### Scoped Styles

**✅ Sempre use `scoped` quando possível:**
```vue
<style scoped>
.card {
  padding: 1rem;
}
</style>
```

---

### CSS Modules

```vue
<template>
  <div :class="$style.card">
    Conteúdo
  </div>
</template>

<style module>
.card {
  padding: 1rem;
}
</style>
```

---

## 📁 Organização de Arquivos

### Estrutura de Projeto

```
src/
├── components/          # Componentes reutilizáveis
│   ├── common/         # Componentes comuns (Button, Input, etc.)
│   └── features/       # Componentes específicos de features
├── composables/        # Composables reutilizáveis
├── views/              # Páginas/Views
├── router/             # Configuração de rotas
├── stores/             # State management (Pinia)
├── utils/              # Funções utilitárias
├── assets/             # Imagens, CSS, etc.
└── main.js             # Entry point
```

---

### Organização de Componentes

```
components/
├── UserCard/
│   ├── UserCard.vue
│   ├── UserCard.test.js
│   └── index.js        # Export default
└── ProductList/
    ├── ProductList.vue
    └── components/     # Sub-componentes
        └── ProductItem.vue
```

---

## 🔒 Performance

### Lazy Loading de Componentes

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

const HeavyComponent = defineAsyncComponent(() => 
  import('./HeavyComponent.vue')
)
</script>
```

---

### v-memo (Vue 3.2+)

```vue
<template>
  <div v-for="item in list" :key="item.id" v-memo="[item.id, item.selected]">
    <!-- Conteúdo pesado -->
  </div>
</template>
```

---

## 🧪 Testes

### Estrutura de Teste

```javascript
import { mount } from '@vue/test-utils'
import MyComponent from './MyComponent.vue'

describe('MyComponent', () => {
  it('renders correctly', () => {
    const wrapper = mount(MyComponent, {
      props: {
        title: 'Test'
      }
    })
    
    expect(wrapper.text()).toContain('Test')
  })
})
```

---

## 📝 Checklist de Qualidade

Antes de commitar código Vue.js 3:

- [ ] Usa `<script setup>`
- [ ] Props com validação adequada
- [ ] `:key` em todos os `v-for`
- [ ] Composables organizados em pasta separada
- [ ] Nomes seguem convenções (PascalCase para componentes)
- [ ] Estilos com `scoped` quando apropriado
- [ ] Código reativo (ref/reactive) usado corretamente
- [ ] Lifecycle hooks limpos (onUnmounted para cleanup)

---

## 🔗 Referências

- **Documentação Oficial:** `referencia/vuejs-3/docs/`
- **Código Fonte:** `referencia/vuejs-3/core/`
- **Exemplos Práticos:** `docs/01-arquitetura/EXEMPLOS_PRATICOS_VUEJS3.md`
- **Design Patterns:** `referencia/vuejs-3/design-patterns/`

---

**Última Atualização:** 2025-01-27  
**Versão Vue.js:** 3.x

