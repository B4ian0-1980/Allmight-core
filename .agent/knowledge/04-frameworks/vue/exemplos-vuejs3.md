---json
{
  "id": "exemplos-vuejs3",
  "title": "💻 Exemplos Genéricos Vue.js 3",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 💻 Exemplos Genéricos Vue.js 3.",
  "gatilhos": [
    "exemplos",
    "frameworks",
    "vue",
    "vuejs3"
  ],
  "perguntas_tipo": [
    "Como utilizar 💻 Exemplos Genéricos Vue.js 3?",
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

# 💻 Exemplos Genéricos Vue.js 3

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Exemplos Aplicáveis a Qualquer Domínio

---

## 🎯 Objetivo

Este documento contém exemplos práticos de Vue.js 3 que são **genéricos** e aplicáveis a qualquer tipo de sistema, independente do domínio de negócio.

---

## 📋 Funcionalidades Cobertas

### 🔐 Autenticação

#### Login Simples
```vue
<template>
  <form @submit.prevent="handleLogin">
    <input v-model="form.email" type="email" placeholder="Email" />
    <input v-model="form.password" type="password" placeholder="Senha" />
    <button type="submit" :disabled="loading">
      {{ loading ? 'Entrando...' : 'Entrar' }}
    </button>
  </form>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const loading = ref(false)

const form = reactive({
  email: '',
  password: ''
})

async function handleLogin() {
  loading.value = true
  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })
    
    if (response.ok) {
      const { token } = await response.json()
      localStorage.setItem('token', token)
      router.push('/dashboard')
    }
  } catch (error) {
    console.error('Erro no login:', error)
  } finally {
    loading.value = false
  }
}
</script>
```

---

### 📝 CRUD Básico

#### Listagem com Busca e Filtros
```vue
<template>
  <div>
    <input 
      v-model="search" 
      placeholder="Buscar..."
      @input="filterItems"
    />
    
    <select v-model="selectedFilter" @change="filterItems">
      <option value="">Todos</option>
      <option value="active">Ativos</option>
      <option value="inactive">Inativos</option>
    </select>
    
    <ul>
      <li v-for="item in filteredItems" :key="item.id">
        {{ item.name }}
        <button @click="editItem(item)">Editar</button>
        <button @click="deleteItem(item.id)">Excluir</button>
      </li>
    </ul>
    
    <button @click="showCreateForm = true">Novo Item</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const items = ref([
  { id: 1, name: 'Item 1', status: 'active' },
  { id: 2, name: 'Item 2', status: 'inactive' }
])

const search = ref('')
const selectedFilter = ref('')
const showCreateForm = ref(false)

const filteredItems = computed(() => {
  let result = items.value
  
  // Filtro por busca
  if (search.value) {
    result = result.filter(item => 
      item.name.toLowerCase().includes(search.value.toLowerCase())
    )
  }
  
  // Filtro por status
  if (selectedFilter.value) {
    result = result.filter(item => item.status === selectedFilter.value)
  }
  
  return result
})

function filterItems() {
  // Reativo via computed
}

function editItem(item) {
  // Lógica de edição
}

async function deleteItem(id) {
  if (confirm('Deseja excluir este item?')) {
    await fetch(`/api/items/${id}`, { method: 'DELETE' })
    items.value = items.value.filter(item => item.id !== id)
  }
}
</script>
```

---

#### Formulário de Criação/Edição
```vue
<template>
  <form @submit.prevent="handleSubmit">
    <input v-model="form.name" placeholder="Nome" required />
    <textarea v-model="form.description" placeholder="Descrição" />
    <button type="submit">
      {{ isEditing ? 'Atualizar' : 'Criar' }}
    </button>
    <button type="button" @click="cancel">Cancelar</button>
  </form>
</template>

<script setup>
import { reactive, ref, watch } from 'vue'

const props = defineProps({
  item: Object,
  isEditing: Boolean
})

const emit = defineEmits(['submit', 'cancel'])

const form = reactive({
  name: '',
  description: ''
})

watch(() => props.item, (newItem) => {
  if (newItem) {
    form.name = newItem.name
    form.description = newItem.description
  }
}, { immediate: true })

function handleSubmit() {
  emit('submit', { ...form })
  resetForm()
}

function cancel() {
  emit('cancel')
  resetForm()
}

function resetForm() {
  form.name = ''
  form.description = ''
}
</script>
```

---

### 📤 Upload de Arquivos

#### Upload com Preview
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
      <button @click="removeFile">Remover</button>
    </div>
    
    <button @click="upload" :disabled="!file || uploading">
      {{ uploading ? 'Enviando...' : 'Enviar' }}
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const fileInput = ref(null)
const file = ref(null)
const preview = ref(null)
const uploading = ref(false)

function handleFileSelect(event) {
  const selectedFile = event.target.files[0]
  if (selectedFile) {
    file.value = selectedFile
    
    if (selectedFile.type.startsWith('image/')) {
      const reader = new FileReader()
      reader.onload = (e) => {
        preview.value = e.target.result
      }
      reader.readAsDataURL(selectedFile)
    }
  }
}

function removeFile() {
  file.value = null
  preview.value = null
  fileInput.value.value = ''
}

async function upload() {
  if (!file.value) return
  
  uploading.value = true
  const formData = new FormData()
  formData.append('file', file.value)
  
  try {
    const response = await fetch('/api/upload', {
      method: 'POST',
      body: formData
    })
    
    if (response.ok) {
      console.log('Upload concluído!')
      removeFile()
    }
  } catch (error) {
    console.error('Erro:', error)
  } finally {
    uploading.value = false
  }
}
</script>
```

---

### 🔔 Notificações

#### Sistema de Notificações
```vue
<!-- NotificationContainer.vue -->
<template>
  <Teleport to="body">
    <div class="notifications">
      <TransitionGroup name="notification">
        <div 
          v-for="notification in notifications" 
          :key="notification.id"
          :class="['notification', notification.type]"
        >
          <span>{{ notification.message }}</span>
          <button @click="remove(notification.id)">×</button>
        </div>
      </TransitionGroup>
    </div>
  </Teleport>
</template>

<script setup>
import { ref } from 'vue'

const notifications = ref([])

function add(message, type = 'info') {
  const id = Date.now()
  notifications.value.push({ id, message, type })
  
  setTimeout(() => {
    remove(id)
  }, 5000)
}

function remove(id) {
  notifications.value = notifications.value.filter(n => n.id !== id)
}

// Expor para uso global
defineExpose({
  add,
  remove
})
</script>

<style scoped>
.notifications {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1000;
}

.notification {
  padding: 1rem;
  margin-bottom: 0.5rem;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.notification.info {
  background: #2196F3;
  color: white;
}

.notification.success {
  background: #4CAF50;
  color: white;
}

.notification.error {
  background: #f44336;
  color: white;
}
</style>
```

**Composable para usar:**
```javascript
// composables/useNotifications.js
import { getCurrentInstance } from 'vue'

export function useNotifications() {
  const instance = getCurrentInstance()
  const notifications = instance.appContext.config.globalProperties.$notifications
  
  return {
    success: (message) => notifications.add(message, 'success'),
    error: (message) => notifications.add(message, 'error'),
    info: (message) => notifications.add(message, 'info')
  }
}
```

---

### 📊 Tabela com Ordenação e Paginação

```vue
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th 
            v-for="column in columns" 
            :key="column.key"
            @click="sort(column.key)"
            :class="{ sorted: sortKey === column.key }"
          >
            {{ column.label }}
            <span v-if="sortKey === column.key">
              {{ sortOrder === 'asc' ? '↑' : '↓' }}
            </span>
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

const sortKey = ref(null)
const sortOrder = ref('asc')
const currentPage = ref(1)

const sortedItems = computed(() => {
  if (!sortKey.value) return props.items
  
  return [...props.items].sort((a, b) => {
    const aVal = a[sortKey.value]
    const bVal = b[sortKey.value]
    
    if (sortOrder.value === 'asc') {
      return aVal > bVal ? 1 : -1
    } else {
      return aVal < bVal ? 1 : -1
    }
  })
})

const totalPages = computed(() => {
  return Math.ceil(sortedItems.value.length / props.itemsPerPage)
})

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage
  const end = start + props.itemsPerPage
  return sortedItems.value.slice(start, end)
})

function sort(key) {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortOrder.value = 'asc'
  }
  currentPage.value = 1
}

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

### 🔍 Busca Avançada

```vue
<template>
  <div>
    <input 
      v-model="searchQuery" 
      placeholder="Buscar..."
      @input="debouncedSearch"
    />
    
    <div v-if="loading">Buscando...</div>
    <div v-else-if="results.length === 0">Nenhum resultado</div>
    <ul v-else>
      <li v-for="result in results" :key="result.id">
        {{ result.name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const searchQuery = ref('')
const results = ref([])
const loading = ref(false)

let searchTimeout = null

function debouncedSearch() {
  clearTimeout(searchTimeout)
  
  searchTimeout = setTimeout(() => {
    performSearch()
  }, 300) // Aguarda 300ms após parar de digitar
}

async function performSearch() {
  if (!searchQuery.value.trim()) {
    results.value = []
    return
  }
  
  loading.value = true
  try {
    const response = await fetch(`/api/search?q=${searchQuery.value}`)
    results.value = await response.json()
  } catch (error) {
    console.error('Erro na busca:', error)
  } finally {
    loading.value = false
  }
}
</script>
```

---

### 📅 Filtros por Data

```vue
<template>
  <div>
    <input 
      type="date" 
      v-model="startDate"
      @change="applyFilters"
    />
    <input 
      type="date" 
      v-model="endDate"
      @change="applyFilters"
    />
    
    <ul>
      <li v-for="item in filteredItems" :key="item.id">
        {{ item.name }} - {{ formatDate(item.date) }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  items: Array
})

const startDate = ref('')
const endDate = ref('')

const filteredItems = computed(() => {
  if (!startDate.value && !endDate.value) {
    return props.items
  }
  
  return props.items.filter(item => {
    const itemDate = new Date(item.date)
    const start = startDate.value ? new Date(startDate.value) : null
    const end = endDate.value ? new Date(endDate.value) : null
    
    if (start && itemDate < start) return false
    if (end && itemDate > end) return false
    
    return true
  })
})

function applyFilters() {
  // Reativo via computed
}

function formatDate(date) {
  return new Date(date).toLocaleDateString('pt-BR')
}
</script>
```

---

### 🎨 Tema Claro/Escuro

```vue
<template>
  <div :class="theme">
    <button @click="toggleTheme">
      {{ theme === 'dark' ? '☀️' : '🌙' }}
    </button>
    <slot />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const theme = ref('light')

onMounted(() => {
  const saved = localStorage.getItem('theme')
  if (saved) {
    theme.value = saved
  }
  applyTheme()
})

watch(theme, (newTheme) => {
  localStorage.setItem('theme', newTheme)
  applyTheme()
})

function toggleTheme() {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
}

function applyTheme() {
  document.documentElement.setAttribute('data-theme', theme.value)
}
</script>

<style>
[data-theme="dark"] {
  --bg-color: #1a1a1a;
  --text-color: #ffffff;
}

[data-theme="light"] {
  --bg-color: #ffffff;
  --text-color: #000000;
}
</style>
```

---

### 🔄 Sincronização com Backend (Laravel/Inertia)

```vue
<template>
  <form @submit.prevent="submit">
    <input v-model="form.name" />
    <button type="submit" :disabled="form.processing">
      {{ form.processing ? 'Salvando...' : 'Salvar' }}
    </button>
  </form>
</template>

<script setup>
import { useForm } from '@inertiajs/vue3'

const form = useForm({
  name: ''
})

function submit() {
  form.post('/api/items', {
    onSuccess: () => {
      console.log('Sucesso!')
    },
    onError: (errors) => {
      console.error('Erros:', errors)
    }
  })
}
</script>
```

---

## 🔗 Referências

- **Exemplos Práticos:** `docs/01-arquitetura/EXEMPLOS_PRATICOS_VUEJS3.md`
- **Padrões:** `docs/01-arquitetura/PADROES_VUEJS3.md`
- **Design Patterns:** `docs/01-arquitetura/DESIGN_PATTERNS_VUEJS3.md`
- **Receitas:** `docs/01-arquitetura/RECEITAS_VUEJS3.md`

---

**Última Atualização:** 2025-01-27  
**Versão Vue.js:** 3.x

