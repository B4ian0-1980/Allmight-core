---json
{
  "id": "receitas_comuns",
  "title": "🍳 Receitas Vue.js 3 - Soluções Práticas",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 🍳 Receitas Vue.js 3 - Soluções Práticas.",
  "gatilhos": [
    "comuns",
    "frameworks",
    "receitas",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 🍳 Receitas Vue.js 3 - Soluções Práticas?",
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

# 🍳 Receitas Vue.js 3 - Soluções Práticas

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Receitas e Soluções Comuns

---

## 🎯 Objetivo

Este documento consolida **receitas práticas** (soluções para problemas comuns) em Vue.js 3, extraídas do Vue.js 3 Cookbook e outras fontes confiáveis.

**Baseado em:**
- ✅ Vue.js 3 Cookbook (Packt)
- ✅ Comunidade Vue.js
- ✅ Casos de uso reais

---

## 📋 Índice de Receitas

### Componentes e Templates
1. [Criar componente com múltiplos elementos raiz](#1-criar-componente-com-múltiplos-elementos-raiz)
2. [Herança de atributos](#2-herança-de-atributos)
3. [Componentes funcionais](#3-componentes-funcionais)

### Data Binding e Formulários
4. [Validação de formulários](#4-validação-de-formulários)
5. [Formulário com múltiplas etapas](#5-formulário-com-múltiplas-etapas)
6. [Upload de arquivos](#6-upload-de-arquivos)

### HTTP e APIs
7. [Fazer requisições HTTP](#7-fazer-requisições-http)
8. [Interceptadores de requisição](#8-interceptadores-de-requisição)
9. [Cache de requisições](#9-cache-de-requisições)

### Rotas e Navegação
10. [Rotas aninhadas](#10-rotas-aninhadas)
11. [Guards de rota](#11-guards-de-rota)
12. [Rotas dinâmicas](#12-rotas-dinâmicas)

### State Management
13. [Gerenciar estado com Pinia](#13-gerenciar-estado-com-pinia)
14. [Persistir estado](#14-persistir-estado)

### Animações
15. [Transições entre componentes](#15-transições-entre-componentes)
16. [Animações de lista](#16-animações-de-lista)

### UI e Layout
17. [Criar modal](#17-criar-modal)
18. [Criar dropdown](#18-criar-dropdown)
19. [Criar tabela paginada](#19-criar-tabela-paginada)

---

## 📝 Receitas Detalhadas

### 1. Criar Componente com Múltiplos Elementos Raiz

**Problema:** Vue 2 exigia um único elemento raiz. Vue 3 permite múltiplos.

**Solução:**
```vue
<template>
  <!-- Múltiplos elementos raiz são permitidos em Vue 3 -->
  <header>
    <h1>{{ title }}</h1>
  </header>
  <main>
    <slot />
  </main>
  <footer>
    <p>Footer content</p>
  </footer>
</template>

<script setup>
defineProps({
  title: String
})
</script>
```

---

### 2. Herança de Atributos

**Problema:** Passar atributos HTML para elemento raiz.

**Solução:**
```vue
<template>
  <!-- $attrs contém todos os atributos não declarados como props -->
  <div v-bind="$attrs">
    <slot />
  </div>
</template>

<script setup>
// Desabilitar herança automática
defineOptions({
  inheritAttrs: false
})
</script>
```

**Uso:**
```vue
<MyComponent class="custom" data-id="123" />
<!-- class e data-id serão aplicados ao div -->
```

---

### 3. Componentes Funcionais

**Problema:** Componente simples sem estado.

**Solução:**
```vue
<script setup>
defineProps({
  title: String,
  description: String
})
</script>

<template>
  <div class="card">
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
  </div>
</template>
```

**Ou usando função:**
```javascript
// FunctionalComponent.js
export default function FunctionalComponent(props) {
  return h('div', { class: 'card' }, [
    h('h3', props.title),
    h('p', props.description)
  ])
}
```

---

### 4. Validação de Formulários

**Solução Completa:**
```vue
<template>
  <form @submit.prevent="handleSubmit">
    <div>
      <input 
        v-model="form.email" 
        type="email"
        :class="{ error: errors.email }"
      />
      <span v-if="errors.email" class="error">{{ errors.email }}</span>
    </div>
    
    <div>
      <input 
        v-model="form.password" 
        type="password"
        :class="{ error: errors.password }"
      />
      <span v-if="errors.password" class="error">{{ errors.password }}</span>
    </div>
    
    <button type="submit" :disabled="!isValid">Enviar</button>
  </form>
</template>

<script setup>
import { reactive, computed } from 'vue'

const form = reactive({
  email: '',
  password: ''
})

const errors = reactive({})

const isValid = computed(() => {
  return form.email && form.password && !errors.email && !errors.password
})

function validateEmail() {
  if (!form.email) {
    errors.email = 'Email é obrigatório'
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
    errors.email = 'Email inválido'
  } else {
    errors.email = ''
  }
}

function validatePassword() {
  if (!form.password) {
    errors.password = 'Senha é obrigatória'
  } else if (form.password.length < 8) {
    errors.password = 'Senha deve ter pelo menos 8 caracteres'
  } else {
    errors.password = ''
  }
}

function handleSubmit() {
  validateEmail()
  validatePassword()
  
  if (isValid.value) {
    // Enviar formulário
    console.log('Formulário válido:', form)
  }
}
</script>
```

---

### 5. Formulário com Múltiplas Etapas

**Solução:**
```vue
<template>
  <div class="multi-step-form">
    <div class="steps">
      <div 
        v-for="(step, index) in steps" 
        :key="index"
        :class="{ active: currentStep === index }"
      >
        {{ step.title }}
      </div>
    </div>
    
    <form @submit.prevent="handleSubmit">
      <component :is="currentComponent" v-model="formData" />
      
      <div class="actions">
        <button v-if="currentStep > 0" @click="previousStep">Anterior</button>
        <button v-if="currentStep < steps.length - 1" @click="nextStep">Próximo</button>
        <button v-else type="submit">Enviar</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Step1 from './Step1.vue'
import Step2 from './Step2.vue'
import Step3 from './Step3.vue'

const currentStep = ref(0)

const steps = [
  { title: 'Dados Pessoais', component: Step1 },
  { title: 'Endereço', component: Step2 },
  { title: 'Confirmação', component: Step3 }
]

const currentComponent = computed(() => steps[currentStep.value].component)

const formData = ref({})

function nextStep() {
  if (currentStep.value < steps.length - 1) {
    currentStep.value++
  }
}

function previousStep() {
  if (currentStep.value > 0) {
    currentStep.value--
  }
}

function handleSubmit() {
  console.log('Dados finais:', formData.value)
}
</script>
```

---

### 6. Upload de Arquivos

**Solução:**
```vue
<template>
  <div>
    <input 
      type="file" 
      @change="handleFileSelect"
      accept="image/*"
      ref="fileInput"
    />
    
    <div v-if="preview" class="preview">
      <img :src="preview" alt="Preview" />
    </div>
    
    <button @click="uploadFile" :disabled="!selectedFile || uploading">
      {{ uploading ? 'Enviando...' : 'Enviar' }}
    </button>
    
    <div v-if="uploadProgress > 0" class="progress">
      <div :style="{ width: uploadProgress + '%' }"></div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const fileInput = ref(null)
const selectedFile = ref(null)
const preview = ref(null)
const uploading = ref(false)
const uploadProgress = ref(0)

function handleFileSelect(event) {
  const file = event.target.files[0]
  if (file) {
    selectedFile.value = file
    
    // Preview de imagem
    if (file.type.startsWith('image/')) {
      const reader = new FileReader()
      reader.onload = (e) => {
        preview.value = e.target.result
      }
      reader.readAsDataURL(file)
    }
  }
}

async function uploadFile() {
  if (!selectedFile.value) return
  
  uploading.value = true
  uploadProgress.value = 0
  
  const formData = new FormData()
  formData.append('file', selectedFile.value)
  
  try {
    const xhr = new XMLHttpRequest()
    
    xhr.upload.addEventListener('progress', (e) => {
      if (e.lengthComputable) {
        uploadProgress.value = (e.loaded / e.total) * 100
      }
    })
    
    xhr.addEventListener('load', () => {
      if (xhr.status === 200) {
        console.log('Upload concluído!')
        // Reset
        selectedFile.value = null
        preview.value = null
        fileInput.value.value = ''
      }
    })
    
    xhr.open('POST', '/api/upload')
    xhr.send(formData)
  } catch (error) {
    console.error('Erro no upload:', error)
  } finally {
    uploading.value = false
  }
}
</script>
```

---

### 7. Fazer Requisições HTTP

**Solução com Fetch API:**
```vue
<script setup>
import { ref, onMounted } from 'vue'

const data = ref(null)
const loading = ref(false)
const error = ref(null)

async function fetchData() {
  loading.value = true
  error.value = null
  
  try {
    const response = await fetch('/api/data')
    if (!response.ok) {
      throw new Error('Erro na requisição')
    }
    data.value = await response.json()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchData()
})
</script>
```

**Solução com Axios:**
```javascript
// utils/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000
})

export default api
```

```vue
<script setup>
import { ref, onMounted } from 'vue'
import api from '@/utils/api'

const data = ref(null)
const loading = ref(false)
const error = ref(null)

async function fetchData() {
  loading.value = true
  try {
    const response = await api.get('/data')
    data.value = response.data
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchData()
})
</script>
```

---

### 8. Interceptadores de Requisição

**Solução:**
```javascript
// utils/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: '/api'
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // Adicionar token
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Redirecionar para login
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default api
```

---

### 9. Cache de Requisições

**Solução:**
```javascript
// composables/useCachedFetch.js
import { ref } from 'vue'

const cache = new Map()

export function useCachedFetch(url, options = {}) {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)
  
  const cacheKey = `${url}-${JSON.stringify(options)}`
  const cacheTimeout = options.cacheTimeout || 5 * 60 * 1000 // 5 minutos
  
  async function fetchData() {
    // Verificar cache
    const cached = cache.get(cacheKey)
    if (cached && Date.now() - cached.timestamp < cacheTimeout) {
      data.value = cached.data
      return
    }
    
    loading.value = true
    try {
      const response = await fetch(url, options)
      const result = await response.json()
      
      // Salvar no cache
      cache.set(cacheKey, {
        data: result,
        timestamp: Date.now()
      })
      
      data.value = result
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }
  
  return {
    data,
    loading,
    error,
    fetchData
  }
}
```

---

### 10. Rotas Aninhadas

**Solução:**
```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Layout from '@/layouts/Layout.vue'
import Dashboard from '@/views/Dashboard.vue'
import UserList from '@/views/users/UserList.vue'
import UserDetail from '@/views/users/UserDetail.vue'

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '',
        component: Dashboard
      },
      {
        path: 'users',
        children: [
          {
            path: '',
            component: UserList
          },
          {
            path: ':id',
            component: UserDetail
          }
        ]
      }
    ]
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
```

---

### 11. Guards de Rota

**Solução:**
```javascript
// router/index.js
import { createRouter } from 'vue-router'

const router = createRouter({
  // ...
})

// Global guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('token')
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'login' })
  } else {
    next()
  }
})

// Per-route guard
{
  path: '/dashboard',
  component: Dashboard,
  meta: { requiresAuth: true },
  beforeEnter: (to, from, next) => {
    // Lógica específica
    next()
  }
}
```

---

### 12. Rotas Dinâmicas

**Solução:**
```javascript
// router/index.js
{
  path: '/user/:id',
  component: UserDetail,
  props: true // Passa params como props
}
```

```vue
<!-- UserDetail.vue -->
<script setup>
defineProps({
  id: String
})
</script>
```

---

### 13. Gerenciar Estado com Pinia

**Solução:**
```javascript
// stores/userStore.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    users: [],
    currentUser: null
  }),
  
  getters: {
    activeUsers: (state) => state.users.filter(u => u.active),
    userCount: (state) => state.users.length
  },
  
  actions: {
    async fetchUsers() {
      const response = await fetch('/api/users')
      this.users = await response.json()
    },
    
    setCurrentUser(user) {
      this.currentUser = user
    }
  }
})
```

**Uso:**
```vue
<script setup>
import { useUserStore } from '@/stores/userStore'
import { storeToRefs } from 'pinia'

const userStore = useUserStore()
const { users, currentUser } = storeToRefs(userStore)

onMounted(() => {
  userStore.fetchUsers()
})
</script>
```

---

### 14. Persistir Estado

**Solução com Pinia Plugin:**
```javascript
// plugins/persistedState.js
import { createPersistedState } from 'pinia-plugin-persistedstate'

app.use(createPinia().use(createPersistedState()))
```

```javascript
// stores/userStore.js
export const useUserStore = defineStore('user', {
  state: () => ({
    preferences: {}
  }),
  
  persist: {
    key: 'user-preferences',
    storage: localStorage,
    paths: ['preferences'] // Apenas persistir preferences
  }
})
```

---

### 15. Transições entre Componentes

**Solução:**
```vue
<template>
  <Transition name="fade" mode="out-in">
    <component :is="currentComponent" :key="key" />
  </Transition>
</template>

<script setup>
import { ref } from 'vue'

const currentComponent = ref('ComponentA')
const key = ref(0)

function switchComponent() {
  key.value++
  currentComponent.value = currentComponent.value === 'ComponentA' 
    ? 'ComponentB' 
    : 'ComponentA'
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
```

---

### 16. Animações de Lista

**Solução:**
```vue
<template>
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.3s;
}

.list-enter-from {
  opacity: 0;
  transform: translateX(-30px);
}

.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.list-move {
  transition: transform 0.3s;
}
</style>
```

---

### 17. Criar Modal

**Solução:**
```vue
<!-- Modal.vue -->
<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="isOpen" class="modal-overlay" @click.self="close">
        <div class="modal-content">
          <header>
            <h2>{{ title }}</h2>
            <button @click="close">×</button>
          </header>
          <main>
            <slot />
          </main>
          <footer>
            <slot name="footer">
              <button @click="close">Fechar</button>
            </slot>
          </footer>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  isOpen: Boolean,
  title: String
})

const emit = defineEmits(['update:isOpen'])

function close() {
  emit('update:isOpen', false)
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  max-width: 500px;
  width: 90%;
}
</style>
```

**Uso:**
```vue
<template>
  <button @click="showModal = true">Abrir Modal</button>
  
  <Modal v-model:isOpen="showModal" title="Título">
    <p>Conteúdo do modal</p>
    <template #footer>
      <button @click="handleSave">Salvar</button>
      <button @click="showModal = false">Cancelar</button>
    </template>
  </Modal>
</template>
```

---

### 18. Criar Dropdown

**Solução:**
```vue
<template>
  <div class="dropdown" v-click-outside="close">
    <button @click="toggle">{{ selected || placeholder }}</button>
    <Transition name="dropdown">
      <ul v-if="isOpen" class="dropdown-menu">
        <li 
          v-for="option in options" 
          :key="option.value"
          @click="select(option)"
        >
          {{ option.label }}
        </li>
      </ul>
    </Transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  options: Array,
  placeholder: String
})

const emit = defineEmits(['update:modelValue'])

const isOpen = ref(false)
const selected = ref(null)

function toggle() {
  isOpen.value = !isOpen.value
}

function select(option) {
  selected.value = option.label
  emit('update:modelValue', option.value)
  isOpen.value = false
}

function close() {
  isOpen.value = false
}

// Diretiva para fechar ao clicar fora
const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = (event) => {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value()
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted(el) {
    document.removeEventListener('click', el.clickOutsideEvent)
  }
}
</script>
```

---

### 19. Criar Tabela Paginada

**Solução:**
```vue
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th v-for="column in columns" :key="column.key">
            {{ column.label }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in paginatedItems" :key="item.id">
          <td v-for="column in columns" :key="column.key">
            {{ item[column.key] }}
          </td>
        </tr>
      </tbody>
    </table>
    
    <div class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">
        Anterior
      </button>
      <span>Página {{ currentPage }} de {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">
        Próximo
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  items: Array,
  columns: Array,
  itemsPerPage: {
    type: Number,
    default: 10
  }
})

const currentPage = ref(1)

const totalPages = computed(() => {
  return Math.ceil(props.items.length / props.itemsPerPage)
})

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage
  const end = start + props.itemsPerPage
  return props.items.slice(start, end)
})

function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

function previousPage() {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}
</script>
```

---

## 🔗 Referências

- **Cookbook Completo:** `referencia/vuejs-3/cookbook/`
- **Exemplos Práticos:** `docs/01-arquitetura/EXEMPLOS_PRATICOS_VUEJS3.md`
- **Design Patterns:** `docs/01-arquitetura/DESIGN_PATTERNS_VUEJS3.md`

---

**Última Atualização:** 2025-01-27  
**Versão Vue.js:** 3.x  
**Baseado em:** Vue.js 3 Cookbook (Packt)

