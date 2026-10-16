---json
{
  "id": "documentacao_typescript",
  "title": "TypeScript — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "typescript",
  "resumo": "Guia tecnico e referencias sobre TypeScript — Guia Completo.",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "typescript"
  ],
  "perguntas_tipo": [
    "Como utilizar TypeScript — Guia Completo?",
    "Quais as boas praticas de typescript?"
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
  "dono": "stack-typescript",
  "prioridade": 2
}
---

# TypeScript — Guia Completo

**Fonte:** [typescriptlang.org](https://www.typescriptlang.org) | **Versão:** 5.x  
**Categoria:** Superset Tipado de JavaScript  
**Prioridade:** ALTA (Usado em React, Next.js, Angular, Vue, Prisma)

---

## 1. O que é TypeScript?

TypeScript adiciona **tipagem estática** ao JavaScript. Erros são pegos em tempo de compilação, não em produção. Todo JavaScript válido é TypeScript válido.

```bash
# Instalar
npm install -D typescript

# Compilar
npx tsc arquivo.ts

# Inicializar config
npx tsc --init
```

---

## 2. Tipos Básicos

```typescript
// Primitivos
let nome: string = "João"
let idade: number = 30
let ativo: boolean = true

// Arrays
let numeros: number[] = [1, 2, 3]
let nomes: Array<string> = ["Ana", "Bob"]

// Tuple (array com tipos fixos)
let coordenada: [number, number] = [10, 20]
let registro: [string, number] = ["João", 30]

// Enum
enum Status {
  Ativo = "ATIVO",
  Inativo = "INATIVO",
  Pendente = "PENDENTE",
}
let estado: Status = Status.Ativo

// Any (evitar — desabilita tipagem)
let qualquer: any = "string"
qualquer = 42 // Sem erro, mas perigoso

// Unknown (any seguro — exige verificação)
let valor: unknown = "hello"
if (typeof valor === "string") {
  console.log(valor.toUpperCase()) // ✅ OK após verificação
}

// Void (funções sem retorno)
function logMsg(msg: string): void {
  console.log(msg)
}

// Null e Undefined
let nulo: null = null
let indefinido: undefined = undefined
let talvez: string | null = null // Nullable
```

---

## 3. Interfaces e Types

### Interface (para objetos — RECOMENDADO)
```typescript
interface User {
  id: number
  name: string
  email: string
  age?: number           // Opcional
  readonly cpf: string   // Somente leitura
}

const user: User = {
  id: 1,
  name: "João",
  email: "joao@email.com",
  cpf: "123.456.789-00",
}

// Extensão
interface Admin extends User {
  role: "admin" | "superadmin"
  permissions: string[]
}
```

### Type (para tipos complexos, unions, intersections)
```typescript
// Union Types
type Status = "ativo" | "inativo" | "pendente"
type ID = string | number

// Intersection Types
type Employee = User & {
  department: string
  salary: number
}

// Utility Types
type UserPreview = Pick<User, "id" | "name">        // Só id e name
type UserWithoutEmail = Omit<User, "email">          // Tudo menos email
type UserPartial = Partial<User>                     // Todos opcionais
type UserRequired = Required<User>                   // Todos obrigatórios
type ReadonlyUser = Readonly<User>                   // Todos readonly
type UserRecord = Record<string, User>               // Dicionário
```

### Quando usar Interface vs Type?

| Use `interface` | Use `type` |
|---|---|
| Objetos e classes | Unions e intersections |
| Quando pode ser extendido | Tipos primitivos |
| APIs públicas | Tipos utilitários complexos |

---

## 4. Funções

```typescript
// Tipagem de parâmetros e retorno
function soma(a: number, b: number): number {
  return a + b
}

// Arrow function tipada
const multiplicar = (a: number, b: number): number => a * b

// Parâmetros opcionais e default
function saudar(nome: string, titulo?: string, prefixo: string = "Olá"): string {
  return titulo
    ? `${prefixo}, ${titulo} ${nome}`
    : `${prefixo}, ${nome}`
}

// Rest parameters
function total(...valores: number[]): number {
  return valores.reduce((acc, v) => acc + v, 0)
}

// Callback tipado
function processar(dados: string[], callback: (item: string) => void): void {
  dados.forEach(callback)
}

// Tipo de função separado
type Comparador<T> = (a: T, b: T) => number
const compareByAge: Comparador<User> = (a, b) => a.age! - b.age!
```

---

## 5. Generics

```typescript
// Função genérica
function primeiro<T>(array: T[]): T | undefined {
  return array[0]
}
const num = primeiro([1, 2, 3])      // tipo: number
const str = primeiro(["a", "b"])     // tipo: string

// Interface genérica
interface ApiResponse<T> {
  data: T
  status: number
  message: string
}

const response: ApiResponse<User[]> = {
  data: [{ id: 1, name: "João", email: "j@j.com", cpf: "123" }],
  status: 200,
  message: "OK",
}

// Genérico com restrição (extends)
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key]
}
const name = getProperty(user, "name") // tipo: string

// Genérico com default
interface Pagination<T = any> {
  data: T[]
  page: number
  total: number
}
```

---

## 6. Type Guards e Narrowing

```typescript
// typeof
function formatValue(value: string | number): string {
  if (typeof value === "string") {
    return value.toUpperCase()
  }
  return value.toFixed(2)
}

// instanceof
function handleError(error: Error | string): string {
  if (error instanceof Error) {
    return error.message
  }
  return error
}

// in operator
interface Dog { bark(): void }
interface Cat { meow(): void }

function makeSound(animal: Dog | Cat): void {
  if ("bark" in animal) {
    animal.bark()
  } else {
    animal.meow()
  }
}

// Discriminated Unions (PATTERN RECOMENDADO)
interface Success {
  type: "success"
  data: User
}
interface Failure {
  type: "error"
  message: string
}
type Result = Success | Failure

function handleResult(result: Result) {
  switch (result.type) {
    case "success":
      console.log(result.data.name) // TS sabe que é Success
      break
    case "error":
      console.log(result.message)   // TS sabe que é Failure
      break
  }
}

// Custom Type Guard
function isUser(obj: unknown): obj is User {
  return (
    typeof obj === "object" &&
    obj !== null &&
    "email" in obj &&
    "name" in obj
  )
}
```

---

## 7. Async/Await com Tipos

```typescript
// Função async retorna Promise<T>
async function fetchUser(id: number): Promise<User> {
  const res = await fetch(`/api/users/${id}`)
  if (!res.ok) throw new Error("Usuário não encontrado")
  return res.json()
}

// Múltiplas promises
async function loadDashboard(): Promise<{
  users: User[]
  posts: Post[]
}> {
  const [users, posts] = await Promise.all([
    fetchUsers(),
    fetchPosts(),
  ])
  return { users, posts }
}
```

---

## 8. Classes

```typescript
class UserService {
  private prisma: PrismaClient

  constructor(prisma: PrismaClient) {
    this.prisma = prisma
  }

  async findAll(): Promise<User[]> {
    return this.prisma.user.findMany()
  }

  async findById(id: number): Promise<User | null> {
    return this.prisma.user.findUnique({ where: { id } })
  }

  async create(data: Omit<User, "id">): Promise<User> {
    return this.prisma.user.create({ data })
  }
}

// Abstract class
abstract class BaseRepository<T> {
  abstract findAll(): Promise<T[]>
  abstract findById(id: number): Promise<T | null>
  abstract create(data: Partial<T>): Promise<T>
  abstract delete(id: number): Promise<void>
}

// Implementação
class UserRepository extends BaseRepository<User> {
  async findAll() { /* ... */ }
  async findById(id: number) { /* ... */ }
  async create(data: Partial<User>) { /* ... */ }
  async delete(id: number) { /* ... */ }
}
```

---

## 9. tsconfig.json — Configuração

```json
{
  "compilerOptions": {
    // Básico
    "target": "ES2022",                    // Versão JS de saída
    "module": "ESNext",                    // Sistema de módulos
    "moduleResolution": "bundler",         // Resolução de imports
    "lib": ["DOM", "DOM.Iterable", "ESNext"],

    // Strictness (RECOMENDADO: tudo true)
    "strict": true,                        // Ativa todas as verificações
    "noImplicitAny": true,                 // Proíbe `any` implícito
    "strictNullChecks": true,              // null/undefined são tipos distintos

    // Paths
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]                   // Import alias
    },

    // Output
    "outDir": "./dist",
    "declaration": true,                   // Gera .d.ts
    "sourceMap": true,

    // Interop
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,

    // JSX (para React)
    "jsx": "react-jsx",

    // Skip type checking de node_modules
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "isolatedModules": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

---

## 10. Patterns Comuns no Dia a Dia

### Props de componente React
```tsx
interface ButtonProps {
  label: string
  variant?: "primary" | "secondary" | "danger"
  size?: "sm" | "md" | "lg"
  disabled?: boolean
  onClick?: () => void
  children?: React.ReactNode
}

function Button({ label, variant = "primary", onClick }: ButtonProps) {
  return <button onClick={onClick}>{label}</button>
}
```

### API Response tipada
```typescript
interface PaginatedResponse<T> {
  data: T[]
  meta: {
    page: number
    perPage: number
    total: number
    lastPage: number
  }
}

async function fetchUsers(page = 1): Promise<PaginatedResponse<User>> {
  const res = await fetch(`/api/users?page=${page}`)
  return res.json()
}
```

### Form Data tipado
```typescript
interface LoginForm {
  email: string
  password: string
  rememberMe: boolean
}

function handleSubmit(data: LoginForm) {
  // data.email é string (garantido)
  // data.rememberMe é boolean (garantido)
}
```

### Event Handlers no React
```tsx
// Input
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  setValue(e.target.value)
}

// Form
const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
  e.preventDefault()
}

// Click
const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
  // ...
}
```

---

## 11. Erros Comuns e Soluções

```typescript
// ❌ "Object is possibly undefined"
const user = users.find(u => u.id === 1)
console.log(user.name) // Erro!

// ✅ Solução 1: Optional chaining
console.log(user?.name)

// ✅ Solução 2: Guard
if (user) {
  console.log(user.name)
}

// ✅ Solução 3: Non-null assertion (se tem certeza)
console.log(user!.name)

// ❌ "Type 'string' is not assignable to type 'Status'"
const status: Status = someVariable // Erro se someVariable é string

// ✅ Solução: Type assertion
const status: Status = someVariable as Status

// ❌ "Property does not exist on type"
const data: unknown = await response.json()
console.log(data.name) // Erro!

// ✅ Solução: Type assertion ou guard
const user = data as User
console.log(user.name)
```

---

## 12. Dicas de Produtividade

1. **Infira quando possível** — TypeScript é inteligente
   ```typescript
   const x = 42            // TS sabe que é number
   const names = ["a", "b"] // TS sabe que é string[]
   ```

2. **Use `as const` para literais**
   ```typescript
   const ROLES = ["admin", "user", "editor"] as const
   type Role = typeof ROLES[number] // "admin" | "user" | "editor"
   ```

3. **Use `satisfies` para validar sem perder tipo**
   ```typescript
   const config = {
     port: 3000,
     host: "localhost",
   } satisfies Record<string, string | number>
   // config.port ainda é `number`, não `string | number`
   ```

4. **Export types para reuso**
   ```typescript
   // types/index.ts
   export type { User, Post, ApiResponse }
   ```

---

*Fonte: [typescriptlang.org](https://www.typescriptlang.org) — Consultado em 2026-02-14*
