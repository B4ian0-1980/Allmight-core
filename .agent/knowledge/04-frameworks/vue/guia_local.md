---json
{
  "id": "guia_local",
  "title": "💻 Exemplos Práticos Vue.js 3 - Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 💻 Exemplos Práticos Vue.js 3 - Guia Completo.",
  "gatilhos": [
    "completo",
    "exemplos",
    "frameworks",
    "guia",
    "local",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 💻 Exemplos Práticos Vue.js 3 - Guia Completo?",
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

# 💻 Exemplos Práticos Vue.js 3 - Guia Completo

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Referência Prática para Desenvolvimento por IA  
**Contexto:** Base Estrutura Projeto - Vue.js 3.x

---

## 📝 Classificação de Tarefa

**Tipo:** 📚 **Documentação** - Exemplos práticos de código  
**Modo:** 🏗️ **Modo Arquiteto** - Consolidação de exemplos

---

## 🎯 Objetivo

Este documento consolida exemplos práticos de código Vue.js 3 extraídos de fontes confiáveis, organizados por categoria, para servir como referência imediata durante desenvolvimento.

**Abordagem:**
- **Exemplos Reais:** Código funcional e testado
- **Organização por Categoria:** Fácil de encontrar
- **Explicações Concisas:** Contexto claro
- **Padrões do Vue.js 3:** Composition API, `<script setup>`, Vite

---

## 📚 Fontes

**Exemplos extraídos de:**
- `livros/vuejs/Vuejs3Lab.md` - Material didático prático
- `referencia/vuejs-3/` - Repositórios oficiais e exemplos

---

## 🚀 Setup Inicial

### Criando Projeto Vue.js 3 com Vite

```bash
# Criar novo projeto
npm create vite@latest meu-projeto -- --template vue

# Entrar no diretório
cd meu-projeto

# Instalar dependências
npm install

# Executar servidor de desenvolvimento
npm run dev
```

**Estrutura de Projeto:**
```
meu-projeto/
├── src/
│   ├── main.js          # Ponto de entrada
│   ├── App.vue          # Componente raiz
│   └── components/       # Componentes aqui
├── index.html
├── package.json
└── vite.config.js
```

---

## 📦 Componentes Básicos

### Componente Simples com Composition API

```vue
<template>
  <div>
    <h1>{{ titulo }}</h1>
    <p>Contador: {{ contador }}</p>
    <button @click="incrementar">Incrementar</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const titulo = ref('Meu Componente')
const contador = ref(0)

function incrementar() {
  contador.value++
}
</script>
```

**Características:**
- ✅ Usa `<script setup>` (sintaxe moderna)
- ✅ `ref()` para reatividade
- ✅ Template simples com interpolação

---

### Componente com Props

```vue
<template>
  <div class="card">
    <h2>{{ nome }}</h2>
    <p>{{ descricao }}</p>
    <span>Preço: R$ {{ preco }}</span>
  </div>
</template>

<script setup>
defineProps({
  nome: {
    type: String,
    required: true
  },
  descricao: {
    type: String,
    default: 'Sem descrição'
  },
  preco: {
    type: Number,
    required: true
  }
})
</script>
```

**Uso:**
```vue
<Card 
  nome="Produto X" 
  descricao="Descrição do produto"
  :preco="99.90"
/>
```

---

## 🔄 Data Binding

### Two-Way Binding com v-model

```vue
<template>
  <div>
    <input v-model="nome" placeholder="Digite seu nome" />
    <p>Olá, {{ nome }}!</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const nome = ref('')
</script>
```

---

### Binding de Classes e Estilos

```vue
<template>
  <div 
    :class="{ ativo: isAtivo, desabilitado: isDesabilitado }"
    :style="{ color: corTexto, fontSize: tamanhoFonte + 'px' }"
  >
    Conteúdo
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isAtivo = ref(true)
const isDesabilitado = ref(false)
const corTexto = ref('#333')
const tamanhoFonte = ref(16)
</script>
```

---

## 🎯 Eventos

### Event Handlers

```vue
<template>
  <div>
    <button @click="handleClick">Clique Aqui</button>
    <button @click="handleClickComParametro('valor')">Com Parâmetro</button>
    <button @click="contador++">Incrementar Direto</button>
    
    <input @input="handleInput" />
    <input @keyup.enter="handleEnter" />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const contador = ref(0)

function handleClick() {
  alert('Clicado!')
}

function handleClickComParametro(valor) {
  console.log('Valor:', valor)
}

function handleInput(event) {
  console.log('Input:', event.target.value)
}

function handleEnter() {
  console.log('Enter pressionado')
}
</script>
```

---

## 📋 Listas e Loops

### Renderizando Listas

```vue
<template>
  <div>
    <ul>
      <li v-for="item in itens" :key="item.id">
        {{ item.nome }}
      </li>
    </ul>
    
    <!-- Com índice -->
    <ul>
      <li v-for="(item, index) in itens" :key="item.id">
        {{ index + 1 }}. {{ item.nome }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const itens = ref([
  { id: 1, nome: 'Item 1' },
  { id: 2, nome: 'Item 2' },
  { id: 3, nome: 'Item 3' }
])
</script>
```

---

### Renderizando Componentes em Loop

```vue
<template>
  <div>
    <ProdutoCard 
      v-for="produto in produtos" 
      :key="produto.id"
      :produto="produto"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProdutoCard from './components/ProdutoCard.vue'

const produtos = ref([
  { id: 1, nome: 'Produto A', preco: 100 },
  { id: 2, nome: 'Produto B', preco: 200 }
])
</script>
```

---

## 🎨 Diretivas Condicionais

### v-if, v-else-if, v-else

```vue
<template>
  <div>
    <p v-if="tipo === 'admin'">Você é administrador</p>
    <p v-else-if="tipo === 'user'">Você é usuário</p>
    <p v-else>Tipo desconhecido</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const tipo = ref('user')
</script>
```

---

### v-show vs v-if

```vue
<template>
  <div>
    <!-- v-if: Remove do DOM quando false -->
    <div v-if="mostrar">Renderizado condicionalmente</div>
    
    <!-- v-show: Apenas oculta com CSS (display: none) -->
    <div v-show="mostrar">Sempre no DOM, apenas oculto</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const mostrar = ref(true)
</script>
```

**Diferença:**
- `v-if`: Mais pesado, remove/adiciona do DOM
- `v-show`: Mais leve, apenas oculta (melhor para toggle frequente)

---

## 🔄 Reatividade Avançada

### reactive() vs ref()

```vue
<script setup>
import { ref, reactive } from 'vue'

// ref() - Para valores primitivos
const contador = ref(0)
const nome = ref('João')

// reactive() - Para objetos
const usuario = reactive({
  nome: 'João',
  email: 'joao@example.com',
  idade: 30
})

// Acesso
contador.value++  // ref precisa .value
usuario.nome = 'Maria'  // reactive não precisa .value
</script>
```

---

### Computed Properties

```vue
<template>
  <div>
    <p>Total: R$ {{ total }}</p>
    <p>Total com Desconto: R$ {{ totalComDesconto }}</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const itens = ref([
  { preco: 100 },
  { preco: 200 },
  { preco: 150 }
])

const desconto = ref(10)

const total = computed(() => {
  return itens.value.reduce((sum, item) => sum + item.preco, 0)
})

const totalComDesconto = computed(() => {
  return total.value * (1 - desconto.value / 100)
})
</script>
```

---

### Watchers

```vue
<script setup>
import { ref, watch } from 'vue'

const busca = ref('')
const resultados = ref([])

// Watcher simples
watch(busca, (novoValor, valorAnterior) => {
  console.log('Busca mudou:', novoValor)
  // Fazer busca...
})

// Watcher imediato
watch(busca, (novoValor) => {
  fazerBusca(novoValor)
}, { immediate: true })

// Watcher profundo (objetos)
const usuario = ref({ nome: 'João' })
watch(usuario, (novoValor) => {
  console.log('Usuário mudou:', novoValor)
}, { deep: true })
</script>
```

---

## 🎣 Lifecycle Hooks

```vue
<script setup>
import { onMounted, onUpdated, onUnmounted } from 'vue'

// Equivalente a mounted()
onMounted(() => {
  console.log('Componente montado')
  // Carregar dados, configurar listeners, etc.
})

// Equivalente a updated()
onUpdated(() => {
  console.log('Componente atualizado')
})

// Equivalente a beforeUnmount()
onUnmounted(() => {
  console.log('Componente desmontado')
  // Limpar timers, cancelar requests, etc.
})
</script>
```

---

## 📤 Emitindo Eventos

### Componente Filho Emitindo Evento

```vue
<!-- Filho.vue -->
<template>
  <button @click="enviarDados">Enviar</button>
</template>

<script setup>
const emit = defineEmits(['dados-enviados'])

function enviarDados() {
  emit('dados-enviados', { mensagem: 'Dados enviados!' })
}
</script>
```

### Componente Pai Escutando

```vue
<!-- Pai.vue -->
<template>
  <Filho @dados-enviados="handleDadosEnviados" />
</template>

<script setup>
import Filho from './components/Filho.vue'

function handleDadosEnviados(dados) {
  console.log('Recebido:', dados)
}
</script>
```

---

## 🔌 Composables (Custom Hooks)

### Exemplo: useCounter

```javascript
// composables/useCounter.js
import { ref } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)
  
  const increment = () => count.value++
  const decrement = () => count.value--
  const reset = () => count.value = initialValue
  
  return {
    count,
    increment,
    decrement,
    reset
  }
}
```

**Uso:**
```vue
<script setup>
import { useCounter } from './composables/useCounter'

const { count, increment, decrement, reset } = useCounter(10)
</script>
```

---

### Exemplo: useFetch

```javascript
// composables/useFetch.js
import { ref } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)
  
  async function fetchData() {
    loading.value = true
    error.value = null
    
    try {
      const response = await fetch(url)
      data.value = await response.json()
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }
  
  fetchData()
  
  return { data, loading, error, refetch: fetchData }
}
```

**Uso:**
```vue
<script setup>
import { useFetch } from './composables/useFetch'

const { data, loading, error } = useFetch('/api/produtos')
</script>
```

---

## 🎨 Formulários

### Formulário Simples

```vue
<template>
  <form @submit.prevent="handleSubmit">
    <input v-model="form.nome" placeholder="Nome" />
    <input v-model="form.email" type="email" placeholder="Email" />
    <button type="submit">Enviar</button>
  </form>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({
  nome: '',
  email: ''
})

function handleSubmit() {
  console.log('Formulário:', form)
  // Enviar dados...
}
</script>
```

---

### Validação de Formulário

```vue
<template>
  <form @submit.prevent="handleSubmit">
    <input 
      v-model="form.email" 
      type="email"
      :class="{ error: errors.email }"
    />
    <span v-if="errors.email" class="error-message">
      {{ errors.email }}
    </span>
    
    <button type="submit" :disabled="!isValid">Enviar</button>
  </form>
</template>

<script setup>
import { reactive, computed } from 'vue'

const form = reactive({
  email: ''
})

const errors = reactive({})

const isValid = computed(() => {
  return form.email && !errors.email
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

function handleSubmit() {
  validateEmail()
  if (isValid.value) {
    // Enviar...
  }
}
</script>
```

---

## 🔗 Integração com Backend (Laravel/Inertia)

### Usando Inertia.js

```vue
<template>
  <div>
    <form @submit.prevent="submit">
      <input v-model="form.nome" />
      <button type="submit">Salvar</button>
    </form>
  </div>
</template>

<script setup>
import { useForm } from '@inertiajs/vue3'

const form = useForm({
  nome: ''
})

function submit() {
  form.post('/api/produtos', {
    onSuccess: () => {
      console.log('Sucesso!')
    }
  })
}
</script>
```

---

## 📝 Boas Práticas

### 1. Use `<script setup>` sempre que possível

✅ **Bom:**
```vue
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>
```

❌ **Evite:**
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

### 2. Use `ref()` para primitivos, `reactive()` para objetos

✅ **Bom:**
```javascript
const count = ref(0)
const user = reactive({ nome: 'João' })
```

---

### 3. Use `computed()` para valores derivados

✅ **Bom:**
```javascript
const total = computed(() => items.value.reduce((sum, item) => sum + item.preco, 0))
```

❌ **Evite:**
```javascript
const total = items.value.reduce((sum, item) => sum + item.preco, 0) // Não reativo!
```

---

### 4. Sempre use `:key` em `v-for`

✅ **Bom:**
```vue
<li v-for="item in items" :key="item.id">{{ item.nome }}</li>
```

---

### 5. Organize composables em pasta separada

```
src/
├── components/
├── composables/
│   ├── useCounter.js
│   ├── useFetch.js
│   └── useAuth.js
└── views/
```

---

## 🔗 Referências

- **Documentação Oficial:** `referencia/vuejs-3/docs/`
- **Código Fonte:** `referencia/vuejs-3/core/`
- **Livros:** `livros/vuejs/`
- **Design Patterns:** `referencia/vuejs-3/design-patterns/`
- **Cookbook:** `referencia/vuejs-3/cookbook/`

---

**Última Atualização:** 2025-01-27  
**Versão Vue.js:** 3.x  
**Baseado em:** `livros/vuejs/Vuejs3Lab.md` + Repositórios oficiais Vue.js 3

