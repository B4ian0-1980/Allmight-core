---json
{
  "id": "documentacao_prisma",
  "title": "Prisma ORM — Guia Completo",
  "categoria": "05-banco-dados",
  "subcategoria": "prisma",
  "resumo": "⚠️ **Importante:** Sem o singleton, o Next.js (hot reload) cria múltiplas conexões e esgota o pool do banco.",
  "gatilhos": [
    "banco",
    "completo",
    "dados",
    "documentacao",
    "guia",
    "orm",
    "prisma"
  ],
  "perguntas_tipo": [
    "Como utilizar Prisma ORM — Guia Completo?",
    "Quais as boas praticas de prisma?"
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
  "dono": "stack-prisma",
  "prioridade": 2
}
---

# Prisma ORM — Guia Completo

**Fonte:** [prisma.io](https://www.prisma.io) | **Versão:** 6.x  
**Categoria:** ORM para Node.js / TypeScript  
**Prioridade:** ALTA (ORM do sistema Frequência Digital)

---

## 1. O que é Prisma?

Prisma é um ORM **moderno e type-safe** para Node.js e TypeScript. Diferente de ORMs tradicionais (Sequelize, TypeORM), Prisma usa uma abordagem **schema-first** com geração automática de cliente.

### Componentes
| Componente | Função |
|---|---|
| **Prisma Schema** | Arquivo `schema.prisma` — define modelos e relações |
| **Prisma Client** | Cliente gerado automaticamente — queries type-safe |
| **Prisma Migrate** | Sistema de migrations — versiona o schema do banco |
| **Prisma Studio** | Interface visual para explorar dados |
| **Introspection** | Gera schema a partir de banco existente |

---

## 2. Instalação e Setup

```bash
# Instalar Prisma CLI
npm install prisma --save-dev

# Instalar Prisma Client
npm install @prisma/client

# Inicializar (cria prisma/schema.prisma e .env)
npx prisma init
```

### Estrutura gerada
```
projeto/
├── prisma/
│   ├── schema.prisma     # Definição dos modelos
│   ├── migrations/       # Histórico de migrations
│   └── seed.ts           # Script de seed (dados iniciais)
├── .env                  # DATABASE_URL
└── lib/
    └── prisma.ts         # Singleton do client
```

### Configuração do `.env`
```env
# MySQL
DATABASE_URL="mysql://root:senha@localhost:3306/meu_banco"

# PostgreSQL
DATABASE_URL="postgresql://user:senha@localhost:5432/meu_banco?schema=public"

# SQLite (para dev/testes)
DATABASE_URL="file:./dev.db"
```

---

## 3. Schema Prisma (`schema.prisma`)

### Estrutura básica
```prisma
// Configuração do banco
datasource db {
  provider = "mysql"      // mysql | postgresql | sqlite | mongodb
  url      = env("DATABASE_URL")
}

// Gerador do client
generator client {
  provider = "prisma-client-js"
}

// =====================
// MODELOS
// =====================

model User {
  id        Int       @id @default(autoincrement())
  email     String    @unique
  name      String?
  password  String
  role      Role      @default(USER)
  active    Boolean   @default(true)
  createdAt DateTime  @default(now()) @map("created_at")
  updatedAt DateTime  @updatedAt @map("updated_at")

  // Relação 1:N — um user tem muitos posts
  posts     Post[]

  // Relação N:N — um user tem muitos perfis
  profiles  Profile[]

  @@map("users")           // Nome da tabela no banco
  @@index([email])         // Índice para busca rápida
}

model Post {
  id        Int       @id @default(autoincrement())
  title     String    @db.VarChar(255)
  content   String?   @db.Text
  published Boolean   @default(false)
  createdAt DateTime  @default(now()) @map("created_at")

  // Relação N:1 — muitos posts para um user
  author    User      @relation(fields: [authorId], references: [id])
  authorId  Int       @map("author_id")

  // Relação N:N
  categories Category[]

  @@map("posts")
}

model Category {
  id    Int    @id @default(autoincrement())
  name  String @unique
  posts Post[]

  @@map("categories")
}

model Profile {
  id     Int    @id @default(autoincrement())
  bio    String?
  userId Int    @unique @map("user_id")
  user   User   @relation(fields: [userId], references: [id])

  @@map("profiles")
}

// Enum
enum Role {
  USER
  ADMIN
  EDITOR
}
```

### Tipos de Campo

| Decorator | Função | Exemplo |
|---|---|---|
| `@id` | Chave primária | `id Int @id` |
| `@default()` | Valor padrão | `@default(autoincrement())`, `@default(now())`, `@default(uuid())` |
| `@unique` | Valor único | `email String @unique` |
| `@map()` | Nome no banco | `@map("created_at")` |
| `@@map()` | Nome da tabela | `@@map("users")` |
| `@db.VarChar()` | Tipo específico do banco | `@db.VarChar(255)`, `@db.Text` |
| `@relation()` | Define relação | `@relation(fields: [userId], references: [id])` |
| `@updatedAt` | Atualiza automaticamente | `updatedAt DateTime @updatedAt` |
| `@@index()` | Índice para performance | `@@index([email])` |
| `@@unique()` | Constraint unique composta | `@@unique([email, tenantId])` |
| `?` | Campo opcional (nullable) | `name String?` |

---

## 4. Relações

### 1:1 (Um para Um)
```prisma
model User {
  id      Int      @id @default(autoincrement())
  profile Profile?
}

model Profile {
  id     Int  @id @default(autoincrement())
  userId Int  @unique          // ← @unique torna 1:1
  user   User @relation(fields: [userId], references: [id])
}
```

### 1:N (Um para Muitos)
```prisma
model User {
  id    Int    @id @default(autoincrement())
  posts Post[]                   // ← Array = lado "muitos"
}

model Post {
  id       Int  @id @default(autoincrement())
  authorId Int                   // ← FK simples
  author   User @relation(fields: [authorId], references: [id])
}
```

### N:N (Muitos para Muitos)

#### Implícita (Prisma cria a tabela pivô)
```prisma
model Post {
  id         Int        @id @default(autoincrement())
  categories Category[]
}

model Category {
  id    Int    @id @default(autoincrement())
  posts Post[]
}
// Prisma cria automaticamente _CategoryToPost
```

#### Explícita (tabela pivô manual — RECOMENDADO)
```prisma
model Post {
  id         Int            @id @default(autoincrement())
  categories PostCategory[]
}

model Category {
  id    Int            @id @default(autoincrement())
  posts PostCategory[]
}

model PostCategory {
  postId     Int
  categoryId Int
  assignedAt DateTime @default(now())

  post     Post     @relation(fields: [postId], references: [id])
  category Category @relation(fields: [categoryId], references: [id])

  @@id([postId, categoryId])     // Chave primária composta
  @@map("post_categories")
}
```

---

## 5. Migrations

```bash
# Criar e aplicar migration (desenvolvimento)
npx prisma migrate dev --name init
npx prisma migrate dev --name add_user_role

# Aplicar migrations (produção)
npx prisma migrate deploy

# Resetar banco (CUIDADO: apaga tudo)
npx prisma migrate reset

# Ver status das migrations
npx prisma migrate status

# Gerar client sem migration
npx prisma generate
```

### Fluxo de trabalho
```
1. Editar schema.prisma
2. npx prisma migrate dev --name descricao
   → Cria arquivo SQL em prisma/migrations/
   → Aplica no banco
   → Regenera Prisma Client
3. Commitar migration
```

---

## 6. Introspection (Banco Existente → Schema)

Quando já tem um banco com tabelas e quer gerar o schema:

```bash
# Gerar schema a partir do banco existente
npx prisma db pull

# Depois, gerar o client
npx prisma generate
```

Isso é útil para:
- Migrar de Eloquent/Laravel para Prisma
- Sistemas legados
- Bancos gerenciados por DBA

---

## 7. Prisma Client — CRUD Completo

### Singleton Pattern (ESSENCIAL para Next.js)
```typescript
// lib/prisma.ts
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma = globalForPrisma.prisma ?? new PrismaClient()

if (process.env.NODE_ENV !== 'production') {
  globalForPrisma.prisma = prisma
}
```

> ⚠️ **Importante:** Sem o singleton, o Next.js (hot reload) cria múltiplas conexões e esgota o pool do banco.

### CREATE
```typescript
// Criar um registro
const user = await prisma.user.create({
  data: {
    email: 'joao@exemplo.com',
    name: 'João Silva',
    password: hashedPassword,
  },
})

// Criar com relação
const userWithPosts = await prisma.user.create({
  data: {
    email: 'maria@exemplo.com',
    name: 'Maria',
    posts: {
      create: [
        { title: 'Primeiro Post' },
        { title: 'Segundo Post' },
      ],
    },
  },
  include: {
    posts: true,  // Retorna os posts junto
  },
})

// Criar muitos de uma vez
const count = await prisma.user.createMany({
  data: [
    { email: 'a@a.com', name: 'A' },
    { email: 'b@b.com', name: 'B' },
    { email: 'c@c.com', name: 'C' },
  ],
  skipDuplicates: true,  // Ignora se email já existe
})
```

### READ
```typescript
// Buscar todos
const users = await prisma.user.findMany()

// Buscar com filtro
const admins = await prisma.user.findMany({
  where: {
    role: 'ADMIN',
    active: true,
  },
})

// Buscar um por ID
const user = await prisma.user.findUnique({
  where: { id: 1 },
})

// Buscar um por campo único
const user = await prisma.user.findUnique({
  where: { email: 'joao@exemplo.com' },
})

// Buscar o primeiro que bate
const user = await prisma.user.findFirst({
  where: { role: 'ADMIN' },
})

// Com relações (include)
const userWithPosts = await prisma.user.findUnique({
  where: { id: 1 },
  include: {
    posts: true,
    profile: true,
  },
})

// Selecionar campos específicos
const users = await prisma.user.findMany({
  select: {
    id: true,
    name: true,
    email: true,
    _count: { select: { posts: true } },
  },
})

// Paginação
const users = await prisma.user.findMany({
  skip: 0,       // Offset
  take: 10,      // Limit
  orderBy: {
    createdAt: 'desc',
  },
})

// Busca por texto (contains)
const results = await prisma.post.findMany({
  where: {
    OR: [
      { title: { contains: 'prisma' } },
      { content: { contains: 'prisma' } },
    ],
  },
})

// Contar
const total = await prisma.user.count({
  where: { active: true },
})

// Filtros avançados
const users = await prisma.user.findMany({
  where: {
    AND: [
      { role: 'ADMIN' },
      { createdAt: { gte: new Date('2024-01-01') } },
    ],
    NOT: { email: { endsWith: '@teste.com' } },
    name: { startsWith: 'Jo' },
  },
})
```

### UPDATE
```typescript
// Atualizar um
const user = await prisma.user.update({
  where: { id: 1 },
  data: {
    name: 'Novo Nome',
    role: 'ADMIN',
  },
})

// Atualizar muitos
const count = await prisma.user.updateMany({
  where: { active: false },
  data: { role: 'USER' },
})

// Upsert (criar se não existe, atualizar se existe)
const user = await prisma.user.upsert({
  where: { email: 'joao@exemplo.com' },
  update: { name: 'João Atualizado' },
  create: {
    email: 'joao@exemplo.com',
    name: 'João Novo',
  },
})

// Incrementar valor numérico
const post = await prisma.post.update({
  where: { id: 1 },
  data: {
    viewCount: { increment: 1 },
  },
})
```

### DELETE
```typescript
// Deletar um
const user = await prisma.user.delete({
  where: { id: 1 },
})

// Deletar muitos
const count = await prisma.user.deleteMany({
  where: {
    active: false,
    createdAt: { lt: new Date('2023-01-01') },
  },
})
```

---

## 8. Transações

```typescript
// Transação sequencial
const [user, post] = await prisma.$transaction([
  prisma.user.create({ data: { email: 'a@a.com', name: 'A' } }),
  prisma.post.create({ data: { title: 'Post', authorId: 1 } }),
])

// Transação interativa (mais controle)
const result = await prisma.$transaction(async (tx) => {
  const user = await tx.user.create({
    data: { email: 'b@b.com', name: 'B' },
  })

  const post = await tx.post.create({
    data: { title: 'Post do B', authorId: user.id },
  })

  // Se algo falhar aqui, tudo é revertido
  if (!post) throw new Error('Falha ao criar post')

  return { user, post }
})
```

---

## 9. Seeds (Dados Iniciais)

```typescript
// prisma/seed.ts
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  // Limpar dados existentes
  await prisma.post.deleteMany()
  await prisma.user.deleteMany()

  // Criar usuários
  const admin = await prisma.user.create({
    data: {
      email: 'admin@sistema.com',
      name: 'Administrador',
      role: 'ADMIN',
      password: '$2b$10$hash...',
      posts: {
        create: [
          { title: 'Primeiro Post', published: true },
          { title: 'Rascunho', published: false },
        ],
      },
    },
  })

  const user = await prisma.user.create({
    data: {
      email: 'user@sistema.com',
      name: 'Usuário Comum',
      role: 'USER',
      password: '$2b$10$hash...',
    },
  })

  console.log({ admin, user })
}

main()
  .then(async () => await prisma.$disconnect())
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })
```

```json
// package.json
{
  "prisma": {
    "seed": "tsx prisma/seed.ts"
  }
}
```

```bash
# Executar seed
npx prisma db seed
```

---

## 10. Prisma Studio (Interface Visual)

```bash
npx prisma studio
# Abre em http://localhost:5555
```

Permite visualizar, filtrar, editar e deletar registros direto no browser — muito útil para debug.

---

## 11. Eloquent (Laravel) vs Prisma — Comparação

| Operação | Eloquent (Laravel) | Prisma |
|---|---|---|
| **Buscar todos** | `User::all()` | `prisma.user.findMany()` |
| **Buscar por ID** | `User::find(1)` | `prisma.user.findUnique({ where: { id: 1 } })` |
| **Criar** | `User::create([...])` | `prisma.user.create({ data: {...} })` |
| **Atualizar** | `$user->update([...])` | `prisma.user.update({ where: {id}, data: {...} })` |
| **Deletar** | `$user->delete()` | `prisma.user.delete({ where: { id } })` |
| **With** | `User::with('posts')` | `include: { posts: true }` |
| **Where** | `User::where('role', 'admin')` | `where: { role: 'admin' }` |
| **Paginação** | `User::paginate(10)` | `findMany({ skip, take })` |
| **Migration** | `php artisan migrate` | `npx prisma migrate dev` |
| **Seed** | `php artisan db:seed` | `npx prisma db seed` |
| **Tinker** | `php artisan tinker` | `npx prisma studio` |

---

## 12. Boas Práticas

### Conexão em ambiente Serverless/Next.js
```typescript
// lib/prisma.ts — SEMPRE use singleton
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma = globalForPrisma.prisma ?? new PrismaClient({
  log: process.env.NODE_ENV === 'development'
    ? ['query', 'error', 'warn']
    : ['error'],
})

if (process.env.NODE_ENV !== 'production') {
  globalForPrisma.prisma = prisma
}
```

### Soft Delete Pattern
```prisma
model User {
  id        Int       @id @default(autoincrement())
  deletedAt DateTime? @map("deleted_at")   // null = ativo
}
```
```typescript
// Middleware de soft delete
prisma.$use(async (params, next) => {
  if (params.model === 'User') {
    if (params.action === 'delete') {
      params.action = 'update'
      params.args.data = { deletedAt: new Date() }
    }
    if (params.action === 'findMany') {
      params.args.where = { ...params.args.where, deletedAt: null }
    }
  }
  return next(params)
})
```

---

## 13. Comandos Essenciais

| Comando | Função |
|---|---|
| `npx prisma init` | Inicializar Prisma |
| `npx prisma generate` | Gerar/atualizar client |
| `npx prisma migrate dev --name xxx` | Criar + aplicar migration |
| `npx prisma migrate deploy` | Aplicar migrations (produção) |
| `npx prisma migrate reset` | Resetar banco + recriar |
| `npx prisma db push` | Sync schema → banco (sem migration) |
| `npx prisma db pull` | Introspecção: banco → schema |
| `npx prisma db seed` | Executar seed |
| `npx prisma studio` | Interface visual |
| `npx prisma format` | Formatar schema.prisma |
| `npx prisma validate` | Validar schema |

---

*Fonte: [prisma.io/docs](https://www.prisma.io/docs) — Consultado em 2026-02-14*
