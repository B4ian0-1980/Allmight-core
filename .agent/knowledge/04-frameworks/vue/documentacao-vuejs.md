---json
{
  "id": "documentacao-vuejs",
  "title": "Vue.js 3 — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Vue.js 3 — Guia Completo.",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "vue",
    "vuejs"
  ],
  "perguntas_tipo": [
    "Como utilizar Vue.js 3 — Guia Completo?",
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

# Vue.js 3 — Guia Completo

**Fonte:** [vuejs.org/guide](https://vuejs.org/guide/introduction) · [vuejs.org/api](https://vuejs.org/api/) · [vuejs.org/examples](https://vuejs.org/examples)  
**Versão:** Vue 3.x (Composition API)  
**Categoria:** Frontend · Framework Progressivo  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. O que é Vue.js?

Vue é um **framework progressivo** para construir interfaces de usuário. Oferece **duas APIs**: Options API (clássica) e Composition API (moderna, recomendada).

---

## 2. Criando Projeto

```bash
npm create vue@latest    # Scaffolding oficial (Vite + Vue 3)
# ou
npm create vite@latest meu-app -- --template vue-ts

cd meu-app
npm install
npm run dev
```

---

## 3. Single File Component (SFC)

```vue
<!-- UserCard.vue -->
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

// Props
const props = defineProps<{
  name: string
  email: string
  role?: string
}>()

// Emits
const emit = defineEmits<{
  delete: [id: string]
  update: [data: { name: string }]
}>()

// Estado reativo
const isExpanded = ref(false)
const counter = ref(0)

// Computado
const displayName = computed(() => `${props.name} (${props.role ?? 'user'})`)

// Lifecycle
onMounted(() => {
  console.log('Componente montado')
})

// Métodos
function toggle() {
  isExpanded.value = !isExpanded.value
}
</script>

<template>
  <div class="user-card" :class="{ expanded: isExpanded }">
    <h3>{{ displayName }}</h3>
    <p>{{ email }}</p>
    <p>Cliques: {{ counter }}</p>

    <button @click="counter++">+1</button>
    <button @click="toggle">{{ isExpanded ? 'Fechar' : 'Abrir' }}</button>
    <button @click="emit('delete', email)">Deletar</button>

    <div v-if="isExpanded">
      <p>Conteúdo expandido</p>
    </div>
  </div>
</template>

<style scoped>
.user-card {
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
}
.expanded { background: #f0f9ff; }
</style>
```

---

## 4. Diretivas Template

```vue
<template>
  <!-- Interpolação -->
  <p>{{ mensagem }}</p>
  <p v-text="mensagem"></p>
  <p v-html="htmlContent"></p>

  <!-- Condicional -->
  <div v-if="status === 'loading'">Carregando...</div>
  <div v-else-if="status === 'error'">Erro!</div>
  <div v-else>{{ dados }}</div>

  <p v-show="isVisible">Visível (CSS display:none)</p>

  <!-- Loop -->
  <ul>
    <li v-for="(item, index) in items" :key="item.id">
      {{ index }}: {{ item.name }}
    </li>
  </ul>

  <!-- Bind de atributos -->
  <img :src="imageUrl" :alt="imageAlt" />
  <div :class="{ active: isActive, disabled: isDisabled }"></div>
  <div :class="['base', isActive ? 'active' : '']"></div>
  <div :style="{ color: textColor, fontSize: size + 'px' }"></div>

  <!-- Eventos -->
  <button @click="handleClick">Click</button>
  <button @click.prevent="submit">Submit (preventDefault)</button>
  <input @keyup.enter="search" />
  <form @submit.prevent="onSubmit">...</form>

  <!-- Two-way binding -->
  <input v-model="nome" />
  <input v-model.trim="email" />
  <input v-model.number="idade" type="number" />
  <textarea v-model="bio"></textarea>
  <select v-model="role">
    <option value="admin">Admin</option>
    <option value="user">User</option>
  </select>
</template>
```

---

## 5. Composition API — Reatividade

```vue
<script setup lang="ts">
import { ref, reactive, computed, watch, watchEffect } from 'vue'

// ref → Para primitivos (acesso via .value no script)
const count = ref(0)
const name = ref('João')

// reactive → Para objetos (sem .value)
const user = reactive({
  name: 'João',
  email: 'joao@email.com',
  preferences: { theme: 'dark' }
})

// computed → Derivado, com cache
const fullName = computed(() => `${user.name} <${user.email}>`)

// watch → Observa mudanças específicas
watch(count, (newVal, oldVal) => {
  console.log(`Count: ${oldVal} → ${newVal}`)
})

watch(() => user.name, (newName) => {
  console.log('Nome mudou:', newName)
})

// watchEffect → Rastreia dependências automaticamente
watchEffect(() => {
  console.log(`User: ${user.name}, Count: ${count.value}`)
})
</script>
```

---

## 6. Composables (Hooks do Vue)

```typescript
// composables/useFetch.ts
import { ref, watchEffect } from 'vue'

export function useFetch<T>(url: string) {
  const data = ref<T | null>(null)
  const error = ref<string | null>(null)
  const loading = ref(true)

  watchEffect(async () => {
    loading.value = true
    error.value = null
    try {
      const res = await fetch(url)
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      data.value = await res.json()
    } catch (e: any) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  })

  return { data, error, loading }
}

// Usando em componente
<script setup lang="ts">
import { useFetch } from '@/composables/useFetch'

const { data: users, loading, error } = useFetch<User[]>('/api/users')
</script>
```

---

## 7. Vue Router

```typescript
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: () => import('@/views/Home.vue') },
    { path: '/about', component: () => import('@/views/About.vue') },
    { path: '/user/:id', component: () => import('@/views/UserDetail.vue'), props: true },
    { path: '/:pathMatch(.*)*', component: () => import('@/views/NotFound.vue') },
  ],
})

// Guard de autenticação
router.beforeEach((to, from) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    return '/login'
  }
})

export default router
```

```vue
<!-- App.vue -->
<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </nav>
  <RouterView />
</template>
```

---

## 8. Pinia (Estado Global)

```typescript
// stores/user.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  const user = ref<User | null>(null)
  const token = ref('')

  const isLoggedIn = computed(() => !!token.value)
  const displayName = computed(() => user.value?.name ?? 'Visitante')

  async function login(email: string, password: string) {
    const res = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    })
    const data = await res.json()
    user.value = data.user
    token.value = data.token
  }

  function logout() {
    user.value = null
    token.value = ''
  }

  return { user, token, isLoggedIn, displayName, login, logout }
})
```

```vue
<script setup>
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
</script>
<template>
  <p>{{ userStore.displayName }}</p>
  <button v-if="userStore.isLoggedIn" @click="userStore.logout()">Sair</button>
</template>
```

---

## 9. Comparação: Options vs Composition API

| Aspecto | Options API | Composition API |
|---|---|---|
| **Dados** | `data()` | `ref()` / `reactive()` |
| **Computados** | `computed:` | `computed()` |
| **Methods** | `methods:` | Funções normais |
| **Watch** | `watch:` | `watch()` / `watchEffect()` |
| **Lifecycle** | `mounted()` | `onMounted()` |
| **Reuso** | Mixins | Composables |

---

*Fontes: [vuejs.org/guide](https://vuejs.org/guide/introduction) · [vuejs.org/api](https://vuejs.org/api/) — Acessado em 2026-02-14*
