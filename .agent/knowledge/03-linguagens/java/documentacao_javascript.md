---json
{
  "id": "documentacao_javascript",
  "title": "JavaScript Moderno (ES6+) — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "java",
  "resumo": "Guia tecnico e referencias sobre JavaScript Moderno (ES6+) — Guia Completo.",
  "gatilhos": [
    "completo",
    "documentacao",
    "es6",
    "guia",
    "java",
    "javascript",
    "linguagens",
    "moderno"
  ],
  "perguntas_tipo": [
    "Como utilizar JavaScript Moderno (ES6+) — Guia Completo?",
    "Quais as boas praticas de java?"
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
  "dono": "stack-java",
  "prioridade": 2
}
---

# JavaScript Moderno (ES6+) — Guia Completo

**Fonte:** [w3schools.com/js](https://www.w3schools.com/js/) · [MDN Web Docs](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)  
**Versão:** ES2024 (ES6+)  
**Categoria:** Linguagem · Frontend & Backend  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. Variáveis

```javascript
// ✅ const — Não pode reatribuir (PADRÃO)
const nome = 'João'
const idade = 30
const lista = [1, 2, 3]  // Pode mutar o array, mas não reatribuir

// ✅ let — Pode reatribuir
let contador = 0
contador = 1

// ❌ var — NÃO USE (escopo global, hoisting problemático)
```

---

## 2. Tipos de Dados

```javascript
// Primitivos
const str = 'texto'           // String
const num = 42                // Number
const decimal = 3.14          // Number (não tem float separado)
const big = 9007199254740991n // BigInt
const bool = true             // Boolean
const vazio = null            // Null
const indefinido = undefined  // Undefined
const sym = Symbol('id')      // Symbol

// Referência
const arr = [1, 2, 3]         // Array
const obj = { name: 'João' }  // Object
const fn = () => 'hello'      // Function
const set = new Set([1, 2])   // Set
const map = new Map()         // Map
const date = new Date()       // Date
```

---

## 3. Strings

```javascript
const nome = 'João'
const sobrenome = 'Silva'

// Template Literals (RECOMENDADO)
const msg = `Olá, ${nome} ${sobrenome}! Você tem ${2026 - 1990} anos.`

// Métodos úteis
nome.length                    // 4
nome.toUpperCase()             // 'JOÃO'
nome.toLowerCase()             // 'joão'
nome.includes('oã')           // true
nome.startsWith('J')          // true
nome.endsWith('o')            // true
nome.indexOf('o')             // 2
nome.slice(0, 2)              // 'Jo'
nome.replace('João', 'Maria') // 'Maria'
nome.trim()                   // Remove espaços
nome.split('')                // ['J','o','ã','o']
nome.padStart(10, '0')        // '000000João'
nome.repeat(3)                // 'JoãoJoãoJoão'
'hello'.at(-1)                // 'o' (ES2022)
```

---

## 4. Arrays

```javascript
const frutas = ['maçã', 'banana', 'uva']

// Adicionar/Remover
frutas.push('manga')          // Adiciona no final
frutas.pop()                  // Remove do final
frutas.unshift('abacaxi')     // Adiciona no início
frutas.shift()                // Remove do início
frutas.splice(1, 1)           // Remove 1 item no índice 1

// Buscar
frutas.includes('banana')     // true
frutas.indexOf('uva')         // 2
frutas.find(f => f === 'uva') // 'uva'
frutas.findIndex(f => f === 'uva') // 2

// Transformar (NÃO mutam o original)
const upper = frutas.map(f => f.toUpperCase())
const comA = frutas.filter(f => f.includes('a'))
const texto = frutas.join(', ')              // 'maçã, banana, uva'
const flat = [[1,2],[3,4]].flat()           // [1,2,3,4]

// Reduzir
const nums = [10, 20, 30]
const soma = nums.reduce((acc, n) => acc + n, 0)  // 60

// Verificar
nums.every(n => n > 0)        // true (todos)
nums.some(n => n > 25)        // true (algum)

// Ordenar
nums.sort((a, b) => a - b)    // Crescente
nums.sort((a, b) => b - a)    // Decrescente

// Destructuring
const [primeiro, segundo, ...resto] = frutas
```

---

## 5. Objetos

```javascript
const user = {
  name: 'João',
  age: 30,
  email: 'joao@email.com',
  address: {
    city: 'São Paulo',
    state: 'SP',
  },
}

// Acessar
user.name                      // 'João'
user['name']                   // 'João'
user.address.city              // 'São Paulo'
user?.phone                    // undefined (optional chaining)
user?.address?.zip             // undefined (seguro)

// Destructuring
const { name, age, email } = user
const { address: { city } } = user

// Spread (copiar/mesclar)
const updated = { ...user, age: 31 }
const merged = { ...defaults, ...overrides }

// Métodos
Object.keys(user)              // ['name','age','email','address']
Object.values(user)            // ['João', 30, ...]
Object.entries(user)           // [['name','João'], ['age',30], ...]
Object.assign({}, user, { age: 31 })

// Verificar
'name' in user                 // true
user.hasOwnProperty('name')   // true

// Nullish coalescing
const port = config.port ?? 3000  // Usa 3000 se port é null/undefined
```

---

## 6. Funções

```javascript
// Arrow Function (RECOMENDADO)
const soma = (a, b) => a + b
const quadrado = n => n * n
const hello = () => 'Hello!'

// Parâmetros padrão
const greet = (name = 'Mundo') => `Olá, ${name}!`

// Rest parameters
const sum = (...nums) => nums.reduce((a, b) => a + b, 0)
sum(1, 2, 3, 4)  // 10

// Função tradicional (necessária para `this`)
function User(name) {
  this.name = name
}

// IIFE (executa imediatamente)
;(() => {
  console.log('Executou!')
})()
```

---

## 7. Async / Await & Promises

```javascript
// Promise
const fetchData = () => new Promise((resolve, reject) => {
  setTimeout(() => resolve({ data: 'ok' }), 1000)
})

// Async/Await (RECOMENDADO)
async function getData() {
  try {
    const result = await fetchData()
    console.log(result)
  } catch (error) {
    console.error('Erro:', error.message)
  } finally {
    console.log('Finalizado')
  }
}

// Fetch API
const res = await fetch('https://api.example.com/users')
const users = await res.json()

// Paralelo
const [users, posts] = await Promise.all([
  fetch('/api/users').then(r => r.json()),
  fetch('/api/posts').then(r => r.json()),
])

// Promise.allSettled (não para se um falhar)
const results = await Promise.allSettled([
  fetch('/api/a'), fetch('/api/b'), fetch('/api/c'),
])
```

---

## 8. Classes

```javascript
class User {
  // Propriedades privadas (ES2022)
  #password

  constructor(name, email, password) {
    this.name = name
    this.email = email
    this.#password = password
  }

  // Getter
  get displayName() {
    return `${this.name} <${this.email}>`
  }

  // Método
  greet() {
    return `Olá, ${this.name}!`
  }

  // Estático
  static create(data) {
    return new User(data.name, data.email, data.password)
  }
}

// Herança
class Admin extends User {
  constructor(name, email, password, permissions) {
    super(name, email, password)
    this.permissions = permissions
  }

  hasPermission(perm) {
    return this.permissions.includes(perm)
  }
}
```

---

## 9. Módulos (ESM)

```javascript
// math.js — Exportar
export const PI = 3.14159
export function soma(a, b) { return a + b }
export default class Calculator { /* ... */ }

// app.js — Importar
import Calculator, { PI, soma } from './math.js'
import * as math from './math.js'
```

---

## 10. Destructuring & Spread

```javascript
// Array
const [a, b, ...rest] = [1, 2, 3, 4, 5]
// a=1, b=2, rest=[3,4,5]

// Object
const { name, age, ...other } = user

// Em parâmetros de função
function createUser({ name, email, role = 'user' }) {
  return { name, email, role }
}

// Spread
const arr2 = [...arr1, 4, 5]
const obj2 = { ...obj1, newProp: 'value' }
```

---

## 11. Map, Set, WeakMap

```javascript
// Map (chaves de qualquer tipo)
const map = new Map()
map.set('name', 'João')
map.set(42, 'answer')
map.get('name')        // 'João'
map.has('name')        // true
map.size               // 2
map.delete('name')
for (const [key, value] of map) { /* ... */ }

// Set (valores únicos)
const set = new Set([1, 2, 2, 3])  // Set {1, 2, 3}
set.add(4)
set.has(2)             // true
set.size               // 4
const unique = [...new Set(arrayComDuplicatas)]
```

---

## 12. Error Handling

```javascript
try {
  const data = JSON.parse(invalidJson)
} catch (error) {
  if (error instanceof SyntaxError) {
    console.error('JSON inválido:', error.message)
  } else {
    throw error  // Re-throw se não for o erro esperado
  }
} finally {
  cleanup()
}

// Erro customizado
class ValidationError extends Error {
  constructor(field, message) {
    super(message)
    this.name = 'ValidationError'
    this.field = field
  }
}

throw new ValidationError('email', 'Email é obrigatório')
```

---

## 13. DOM (Manipulação do Browser)

```javascript
// Selecionar
const el = document.getElementById('app')
const btn = document.querySelector('.btn-primary')
const items = document.querySelectorAll('.item')

// Criar/Modificar
const div = document.createElement('div')
div.textContent = 'Hello'
div.innerHTML = '<strong>Bold</strong>'
div.classList.add('active')
div.classList.remove('hidden')
div.classList.toggle('open')
div.style.color = 'red'
div.setAttribute('data-id', '42')

// Inserir
document.body.appendChild(div)
parent.insertBefore(div, reference)
parent.removeChild(child)

// Eventos
btn.addEventListener('click', (e) => {
  e.preventDefault()
  console.log('Clicou!', e.target)
})

// Event delegation (performance)
document.querySelector('.list').addEventListener('click', (e) => {
  if (e.target.matches('.item')) {
    console.log('Item clicado:', e.target.textContent)
  }
})
```

---

## 14. LocalStorage & SessionStorage

```javascript
// Salvar
localStorage.setItem('user', JSON.stringify({ name: 'João' }))

// Ler
const user = JSON.parse(localStorage.getItem('user'))

// Remover
localStorage.removeItem('user')
localStorage.clear()  // Limpa tudo
```

---

## 15. Features Modernas (ES2020—ES2024)

```javascript
// Optional chaining (?.)
user?.address?.city

// Nullish coalescing (??)
const port = env.PORT ?? 3000

// Logical assignment
obj.name ??= 'Default'     // Atribui se null/undefined
obj.count ||= 0            // Atribui se falsy
obj.active &&= false       // Atribui se truthy

// structuredClone (deep copy)
const copy = structuredClone(complexObj)

// Array.at() (índice negativo)
const last = arr.at(-1)

// Object.groupBy (ES2024)
const grouped = Object.groupBy(users, u => u.role)

// Top-level await
const config = await loadConfig()
```

---

*Fontes: [w3schools.com/js](https://www.w3schools.com/js/) · [MDN Web Docs](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) — Acessado em 2026-02-14*
