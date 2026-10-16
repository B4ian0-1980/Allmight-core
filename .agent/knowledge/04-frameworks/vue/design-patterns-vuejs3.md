---json
{
  "id": "design-patterns-vuejs3",
  "title": "🎨 Design Patterns Vue.js 3",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 🎨 Design Patterns Vue.js 3.",
  "gatilhos": [
    "design",
    "frameworks",
    "patterns",
    "vue",
    "vuejs3"
  ],
  "perguntas_tipo": [
    "Como utilizar 🎨 Design Patterns Vue.js 3?",
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

# 🎨 Design Patterns Vue.js 3

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Padrões de Design e Arquitetura

---

## 🎯 Objetivo

Este documento consolida **design patterns e padrões arquiteturais** para Vue.js 3, extraídos de fontes confiáveis e práticas da comunidade.

**Baseado em:**
- ✅ Vue.js 3 Design Patterns and Best Practices (Packt)
- ✅ Repositórios oficiais Vue.js 3
- ✅ Padrões de software clássicos adaptados para Vue.js

---

## 📋 Padrões de Design

### 1. Singleton Pattern

**Uso:** Garantir uma única instância de uma classe/objeto

**Exemplo:**
```javascript
// services/ConfigService.js
class ConfigService {
  constructor() {
    if (ConfigService._instance) {
      return ConfigService._instance
    }
    ConfigService._instance = this
    this.settings = {}
    return this
  }

  set(key, value) {
    this.settings[key] = value
  }

  get(key) {
    return this.settings[key]
  }
}

export default new ConfigService()
```

**Uso em Vue:**
```vue
<script setup>
import configService from '@/services/ConfigService'

configService.set('apiUrl', 'https://api.example.com')
const apiUrl = configService.get('apiUrl')
</script>
```

---

### 2. Observer Pattern

**Uso:** Sistema de eventos e notificações

**Exemplo:**
```javascript
// utils/EventBus.js
class EventBus {
  constructor() {
    this.events = {}
  }

  on(eventName, callback) {
    if (!this.events[eventName]) {
      this.events[eventName] = []
    }
    this.events[eventName].push(callback)
  }

  emit(eventName, data) {
    if (!this.events[eventName]) {
      return
    }
    this.events[eventName].forEach(callback => callback(data))
  }

  off(eventName, callback) {
    if (!this.events[eventName]) {
      return
    }
    this.events[eventName] = this.events[eventName].filter(cb => cb !== callback)
  }
}

export default new EventBus()
```

**Uso em Vue:**
```vue
<script setup>
import { onMounted, onUnmounted } from 'vue'
import eventBus from '@/utils/EventBus'

function handleUserUpdate(user) {
  console.log('User updated:', user)
}

onMounted(() => {
  eventBus.on('user:updated', handleUserUpdate)
})

onUnmounted(() => {
  eventBus.off('user:updated', handleUserUpdate)
})
</script>
```

**Alternativa Moderna:** Use `provide/inject` ou Pinia para state management

---

### 3. Dependency Injection

**Uso:** Injetar dependências ao invés de importar diretamente

**Sem DI (❌ Acoplado):**
```javascript
// services/ProjectService.js
import dbManager from '@/dbManager'

const projects = {
  getAllProjects() {
    return dbManager.getAll('projects')
  }
}

export default projects
```

**Com DI (✅ Desacoplado):**
```javascript
// services/ProjectService.js
class ProjectService {
  constructor(database) {
    this.database = database
  }

  getAllProjects() {
    return this.database.getAll('projects')
  }
}

export default ProjectService

// Uso
import ProjectService from '@/services/ProjectService'
import dbManager from '@/dbManager'

const projectService = new ProjectService(dbManager)
```

**Em Vue com provide/inject:**
```vue
<!-- App.vue -->
<script setup>
import { provide } from 'vue'
import dbManager from '@/dbManager'
import ProjectService from '@/services/ProjectService'

const projectService = new ProjectService(dbManager)
provide('projectService', projectService)
</script>

<!-- ChildComponent.vue -->
<script setup>
import { inject } from 'vue'

const projectService = inject('projectService')
const projects = await projectService.getAllProjects()
</script>
```

---

### 4. Decorator Pattern

**Uso:** Adicionar funcionalidades a componentes sem modificar sua estrutura

**Exemplo com Composables:**
```javascript
// composables/withLoading.js
export function withLoading(asyncFunction) {
  return async function(...args) {
    const loading = ref(true)
    const error = ref(null)
    
    try {
      const result = await asyncFunction(...args)
      return result
    } catch (err) {
      error.value = err
      throw err
    } finally {
      loading.value = false
    }
  }
}
```

**Uso:**
```vue
<script setup>
import { ref } from 'vue'
import { withLoading } from '@/composables/withLoading'
import { fetchUsers } from '@/services/userService'

const users = ref([])
const fetchUsersWithLoading = withLoading(fetchUsers)

async function loadUsers() {
  users.value = await fetchUsersWithLoading()
}
</script>
```

---

### 5. Factory Pattern

**Uso:** Criar objetos sem especificar a classe exata

**Exemplo:**
```javascript
// factories/ComponentFactory.js
export function createComponent(type, props) {
  const components = {
    button: () => import('@/components/Button.vue'),
    input: () => import('@/components/Input.vue'),
    card: () => import('@/components/Card.vue')
  }

  return components[type]?.() || components.button()
}
```

**Uso:**
```vue
<template>
  <component :is="componentType" v-bind="componentProps" />
</template>

<script setup>
import { computed } from 'vue'
import { createComponent } from '@/factories/ComponentFactory'

const props = defineProps({
  type: String,
  componentProps: Object
})

const componentType = computed(() => createComponent(props.type, props.componentProps))
</script>
```

---

## 🏗️ Padrões Arquiteturais

### 1. Component Composition Pattern

**Uso:** Compor funcionalidades complexas a partir de componentes menores

**Estrutura:**
```
components/
├── UserProfile/
│   ├── UserProfile.vue
│   ├── UserAvatar.vue
│   ├── UserInfo.vue
│   └── UserActions.vue
```

**Exemplo:**
```vue
<!-- UserProfile.vue -->
<template>
  <div class="user-profile">
    <UserAvatar :user="user" />
    <UserInfo :user="user" />
    <UserActions :user="user" @action="handleAction" />
  </div>
</template>

<script setup>
import UserAvatar from './UserAvatar.vue'
import UserInfo from './UserInfo.vue'
import UserActions from './UserActions.vue'

const props = defineProps({
  user: Object
})

function handleAction(action) {
  // Handle action
}
</script>
```

---

### 2. Plugin Pattern

**Uso:** Estender Vue com funcionalidades globais

**Exemplo:**
```javascript
// plugins/ModalPlugin.js
export default {
  install(app, options) {
    app.config.globalProperties.$modal = {
      open(component, props) {
        // Lógica para abrir modal
      },
      close() {
        // Lógica para fechar modal
      }
    }

    app.provide('modal', app.config.globalProperties.$modal)
  }
}
```

**Registro:**
```javascript
// main.js
import { createApp } from 'vue'
import ModalPlugin from './plugins/ModalPlugin'

const app = createApp(App)
app.use(ModalPlugin)
app.mount('#app')
```

**Uso:**
```vue
<script setup>
import { inject } from 'vue'

const modal = inject('modal')

function openModal() {
  modal.open(MyComponent, { title: 'Hello' })
}
</script>
```

---

### 3. Service Layer Pattern

**Uso:** Separar lógica de negócio dos componentes

**Estrutura:**
```
src/
├── services/
│   ├── UserService.js
│   ├── ProductService.js
│   └── OrderService.js
├── components/
└── views/
```

**Exemplo:**
```javascript
// services/UserService.js
import api from '@/utils/api'

class UserService {
  async getAll() {
    const response = await api.get('/users')
    return response.data
  }

  async getById(id) {
    const response = await api.get(`/users/${id}`)
    return response.data
  }

  async create(userData) {
    const response = await api.post('/users', userData)
    return response.data
  }

  async update(id, userData) {
    const response = await api.put(`/users/${id}`, userData)
    return response.data
  }

  async delete(id) {
    await api.delete(`/users/${id}`)
  }
}

export default new UserService()
```

**Uso em Componente:**
```vue
<script setup>
import { ref, onMounted } from 'vue'
import userService from '@/services/UserService'

const users = ref([])
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    users.value = await userService.getAll()
  } finally {
    loading.value = false
  }
})
</script>
```

---

### 4. Repository Pattern

**Uso:** Abstrair acesso a dados

**Exemplo:**
```javascript
// repositories/UserRepository.js
class UserRepository {
  constructor(apiClient) {
    this.api = apiClient
  }

  async findAll() {
    return this.api.get('/users')
  }

  async findById(id) {
    return this.api.get(`/users/${id}`)
  }

  async create(data) {
    return this.api.post('/users', data)
  }

  async update(id, data) {
    return this.api.put(`/users/${id}`, data)
  }

  async delete(id) {
    return this.api.delete(`/users/${id}`)
  }
}

export default UserRepository
```

---

### 5. State Management Pattern (Pinia)

**Uso:** Gerenciar estado global da aplicação

**Exemplo:**
```javascript
// stores/userStore.js
import { defineStore } from 'pinia'
import userService from '@/services/UserService'

export const useUserStore = defineStore('user', {
  state: () => ({
    users: [],
    currentUser: null,
    loading: false
  }),

  getters: {
    activeUsers: (state) => {
      return state.users.filter(user => user.active)
    },
    userCount: (state) => {
      return state.users.length
    }
  },

  actions: {
    async fetchUsers() {
      this.loading = true
      try {
        this.users = await userService.getAll()
      } finally {
        this.loading = false
      }
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
const { users, loading } = storeToRefs(userStore)

onMounted(() => {
  userStore.fetchUsers()
})
</script>
```

---

## 🎯 Padrões de Componentes

### 1. Container/Presentational Pattern

**Container Component (Lógica):**
```vue
<!-- UserListContainer.vue -->
<script setup>
import { ref, onMounted } from 'vue'
import UserList from './UserList.vue'
import userService from '@/services/UserService'

const users = ref([])
const loading = ref(false)
const error = ref(null)

onMounted(async () => {
  loading.value = true
  try {
    users.value = await userService.getAll()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <UserList 
    :users="users" 
    :loading="loading"
    :error="error"
  />
</template>
```

**Presentational Component (UI):**
```vue
<!-- UserList.vue -->
<script setup>
defineProps({
  users: Array,
  loading: Boolean,
  error: String
})
</script>

<template>
  <div v-if="loading">Carregando...</div>
  <div v-else-if="error">{{ error }}</div>
  <ul v-else>
    <li v-for="user in users" :key="user.id">
      {{ user.name }}
    </li>
  </ul>
</template>
```

---

### 2. Render Props Pattern (Slots)

**Uso:** Passar renderização como prop

**Exemplo:**
```vue
<!-- DataFetcher.vue -->
<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  url: String
})

const data = ref(null)
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  const response = await fetch(props.url)
  data.value = await response.json()
  loading.value = false
})
</script>

<template>
  <slot :data="data" :loading="loading" />
</template>
```

**Uso:**
```vue
<template>
  <DataFetcher url="/api/users">
    <template #default="{ data, loading }">
      <div v-if="loading">Carregando...</div>
      <ul v-else>
        <li v-for="user in data" :key="user.id">
          {{ user.name }}
        </li>
      </ul>
    </template>
  </DataFetcher>
</template>
```

---

### 3. Compound Components Pattern

**Uso:** Componentes que trabalham juntos

**Exemplo:**
```vue
<!-- Tabs.vue -->
<script setup>
import { provide, ref } from 'vue'

const activeTab = ref(0)
provide('activeTab', activeTab)
</script>

<template>
  <div class="tabs">
    <slot />
  </div>
</template>

<!-- TabList.vue -->
<script setup>
import { inject } from 'vue'

const activeTab = inject('activeTab')
</script>

<template>
  <div class="tab-list">
    <slot />
  </div>
</template>

<!-- Tab.vue -->
<script setup>
import { inject } from 'vue'

const props = defineProps({
  index: Number
})

const activeTab = inject('activeTab')
const isActive = computed(() => activeTab.value === props.index)
</script>

<template>
  <button 
    :class="{ active: isActive }"
    @click="activeTab = index"
  >
    <slot />
  </button>
</template>
```

**Uso:**
```vue
<Tabs>
  <TabList>
    <Tab :index="0">Tab 1</Tab>
    <Tab :index="1">Tab 2</Tab>
  </TabList>
  <TabPanels>
    <TabPanel :index="0">Content 1</TabPanel>
    <TabPanel :index="1">Content 2</TabPanel>
  </TabPanels>
</Tabs>
```

---

## 🔄 Padrões de Performance

### 1. Lazy Loading

**Componentes:**
```vue
<script setup>
import { defineAsyncComponent } from 'vue'

const HeavyComponent = defineAsyncComponent(() => 
  import('./HeavyComponent.vue')
)
</script>

<template>
  <Suspense>
    <HeavyComponent />
    <template #fallback>
      <div>Carregando componente...</div>
    </template>
  </Suspense>
</template>
```

---

### 2. Virtual Scrolling

**Para listas grandes:**
```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([...]) // Lista grande
const visibleItems = computed(() => {
  // Retornar apenas itens visíveis
  return items.value.slice(startIndex.value, endIndex.value)
})
</script>
```

**Recomendação:** Use bibliotecas como `vue-virtual-scroller`

---

### 3. Memoization

**v-memo (Vue 3.2+):**
```vue
<template>
  <div 
    v-for="item in list" 
    :key="item.id"
    v-memo="[item.id, item.selected]"
  >
    <!-- Conteúdo pesado -->
  </div>
</template>
```

---

## 📝 Boas Práticas

### 1. Composables para Lógica Reutilizável

**Sempre extraia lógica complexa para composables:**
```javascript
// composables/useUserList.js
export function useUserList() {
  const users = ref([])
  const loading = ref(false)
  const error = ref(null)

  async function fetchUsers() {
    loading.value = true
    try {
      users.value = await userService.getAll()
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  return {
    users,
    loading,
    error,
    fetchUsers
  }
}
```

---

### 2. Props Validation

**Sempre valide props:**
```vue
<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  count: {
    type: Number,
    default: 0,
    validator: (value) => value >= 0
  }
})
</script>
```

---

### 3. Emits Tipados

**Documente eventos emitidos:**
```vue
<script setup>
const emit = defineEmits({
  'update:modelValue': (value) => typeof value === 'string',
  'submit': (payload) => payload && typeof payload === 'object'
})
</script>
```

---

## 🔗 Referências

- **Repositório Design Patterns:** `referencia/vuejs-3/design-patterns/`
- **Exemplos Práticos:** `docs/01-arquitetura/EXEMPLOS_PRATICOS_VUEJS3.md`
- **Padrões de Código:** `docs/01-arquitetura/PADROES_VUEJS3.md`
- **Pinia (State Management):** `referencia/vuejs-3/pinia/`

---

**Última Atualização:** 2025-01-27  
**Versão Vue.js:** 3.x  
**Baseado em:** Vue.js 3 Design Patterns and Best Practices (Packt)

