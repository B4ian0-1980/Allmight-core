---json
{
  "id": "documentacao_nextjs",
  "title": "Next.js 14+ — Guia Completo (App Router)",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "Guia tecnico e referencias sobre Next.js 14+ — Guia Completo (App Router).",
  "gatilhos": [
    "app",
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "next",
    "nextjs",
    "router"
  ],
  "perguntas_tipo": [
    "Como utilizar Next.js 14+ — Guia Completo (App Router)?",
    "Quais as boas praticas de nextjs?"
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
  "dono": "stack-nextjs",
  "prioridade": 2
}
---

# Next.js 14+ — Guia Completo (App Router)

**Fonte:** [nextjs.org](https://nextjs.org) | **Versão:** 14+ (App Router)  
**Categoria:** Framework Fullstack React  
**Prioridade:** ALTA (Tecnologia Core)

---

## 1. O que é Next.js?

Next.js é um framework **fullstack** baseado em React que adiciona:
- **Server-Side Rendering (SSR)** — páginas renderizadas no servidor
- **Static Site Generation (SSG)** — páginas pré-geradas no build
- **Server Components** — componentes que rodam apenas no servidor
- **Server Actions** — funções servidor chamadas como se fossem locais
- **App Router** — sistema de rotas baseado em diretórios
- **API Routes / Route Handlers** — backend integrado
- **Otimização automática** — imagens, fontes, code splitting

---

## 2. Instalação e Setup

```bash
# Criar projeto
npx create-next-app@latest meu-projeto

# Opções recomendadas:
# ✔ TypeScript? Yes
# ✔ ESLint? Yes
# ✔ Tailwind CSS? Yes
# ✔ src/ directory? Yes
# ✔ App Router? Yes
# ✔ Import alias? @/*
```

### Estrutura do Projeto
```
meu-projeto/
├── src/
│   ├── app/                    # App Router (rotas)
│   │   ├── layout.tsx          # Layout raiz
│   │   ├── page.tsx            # Página inicial (/)
│   │   ├── globals.css         # Estilos globais
│   │   ├── loading.tsx         # Loading UI
│   │   ├── error.tsx           # Error UI
│   │   ├── not-found.tsx       # 404
│   │   ├── users/
│   │   │   ├── page.tsx        # /users
│   │   │   └── [id]/
│   │   │       └── page.tsx    # /users/:id
│   │   └── api/
│   │       └── route.ts        # API endpoint
│   ├── components/             # Componentes reutilizáveis
│   ├── lib/                    # Utilitários (db, auth, etc.)
│   └── types/                  # Tipos TypeScript
├── public/                     # Arquivos estáticos
├── prisma/                     # Schema do banco (se usar Prisma)
├── next.config.js
├── tailwind.config.ts
└── package.json
```

---

## 3. Roteamento (App Router)

### Rotas baseadas em pastas
```
src/app/
├── page.tsx                → /
├── about/page.tsx          → /about
├── blog/
│   ├── page.tsx            → /blog
│   └── [slug]/page.tsx     → /blog/:slug (dinâmico)
├── (auth)/                 → Grupo de rotas (sem afetar URL)
│   ├── login/page.tsx      → /login
│   └── register/page.tsx   → /register
└── dashboard/
    ├── layout.tsx          → Layout compartilhado
    ├── page.tsx            → /dashboard
    └── settings/page.tsx   → /dashboard/settings
```

### Arquivos especiais por pasta

| Arquivo | Função |
|---|---|
| `page.tsx` | Página da rota (obrigatório para rota existir) |
| `layout.tsx` | Layout compartilhado (persiste entre navegações) |
| `loading.tsx` | UI de loading (Suspense automático) |
| `error.tsx` | UI de erro (Error Boundary automático) |
| `not-found.tsx` | Página 404 personalizada |
| `template.tsx` | Como layout, mas recria a cada navegação |

### Rotas Dinâmicas
```tsx
// app/users/[id]/page.tsx
export default async function UserPage({
  params
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const user = await getUser(id)

  return <h1>{user.name}</h1>
}
```

### Grupos de Rotas `(nome)`
```
app/
├── (marketing)/        # Grupo - não aparece na URL
│   ├── layout.tsx      # Layout para marketing
│   ├── page.tsx        → /
│   └── about/page.tsx  → /about
└── (dashboard)/        # Grupo separado
    ├── layout.tsx      # Layout para dashboard
    └── panel/page.tsx  → /panel
```

---

## 4. Server Components vs Client Components

### Server Components (PADRÃO)
Todos os componentes no App Router são **Server Components por padrão**.

```tsx
// ✅ Server Component (padrão) — roda NO SERVIDOR
// NÃO pode usar useState, useEffect, onClick, etc.
export default async function UsersPage() {
  // Fetch direto no componente — sem useEffect!
  const users = await prisma.user.findMany()

  return (
    <div>
      <h1>Usuários ({users.length})</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  )
}
```

**Vantagens:**
- Acesso direto ao banco de dados
- Sem JavaScript enviado ao cliente
- Segredos (API keys, tokens) ficam seguros
- Melhor performance (menos JS no browser)

### Client Components
Necessários quando precisa de **interatividade**.

```tsx
'use client' // ← Obrigatório na primeira linha

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <button onClick={() => setCount(count + 1)}>
      Cliques: {count}
    </button>
  )
}
```

### Quando usar qual?

| Necessidade | Server | Client |
|---|---|---|
| Fetch de dados | ✅ | ❌ |
| Acesso ao banco | ✅ | ❌ |
| API keys/segredos | ✅ | ❌ |
| useState / useEffect | ❌ | ✅ |
| onClick / onChange | ❌ | ✅ |
| Browser APIs (localStorage) | ❌ | ✅ |
| Bibliotecas de UI interativas | ❌ | ✅ |

### Padrão recomendado: Server wrapping Client
```tsx
// app/dashboard/page.tsx (Server Component)
import { getStats } from '@/lib/data'
import StatsChart from '@/components/StatsChart' // Client

export default async function DashboardPage() {
  const stats = await getStats() // Busca no servidor

  return (
    <div>
      <h1>Dashboard</h1>
      <StatsChart data={stats} /> {/* Passa dados para componente interativo */}
    </div>
  )
}
```

---

## 5. Data Fetching

### No Server Component (RECOMENDADO)
```tsx
// Fetch direto — sem useEffect, sem useState
export default async function PostsPage() {
  // Opção 1: Fetch API
  const res = await fetch('https://api.exemplo.com/posts', {
    cache: 'no-store',        // SSR (sempre fresco)
    // cache: 'force-cache',  // SSG (cache estático)
    // next: { revalidate: 60 }, // ISR (revalida a cada 60s)
  })
  const posts = await res.json()

  // Opção 2: Prisma direto
  const users = await prisma.user.findMany()

  return <ul>{posts.map(p => <li key={p.id}>{p.title}</li>)}</ul>
}
```

### Estratégias de Cache

| Estratégia | Como | Quando |
|---|---|---|
| **SSR** (Dinâmico) | `cache: 'no-store'` | Dados que mudam sempre |
| **SSG** (Estático) | `cache: 'force-cache'` | Dados que raramente mudam |
| **ISR** (Híbrido) | `next: { revalidate: 60 }` | Dados que mudam periodicamente |

### Parallel Data Fetching
```tsx
export default async function DashboardPage() {
  // ✅ Paralelo (mais rápido)
  const [users, posts, stats] = await Promise.all([
    getUsers(),
    getPosts(),
    getStats(),
  ])

  return (
    <div>
      <UsersList users={users} />
      <PostsList posts={posts} />
      <StatsCard stats={stats} />
    </div>
  )
}
```

---

## 6. Server Actions

Server Actions substituem as API Routes para mutações de dados. São funções que rodam no servidor, chamadas diretamente do cliente.

### Definindo uma Server Action
```tsx
// app/actions/users.ts
'use server'

import { prisma } from '@/lib/prisma'
import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createUser(formData: FormData) {
  const name = formData.get('name') as string
  const email = formData.get('email') as string

  // Validação
  if (!name || !email) {
    return { error: 'Nome e email são obrigatórios' }
  }

  // Criar no banco
  await prisma.user.create({
    data: { name, email }
  })

  // Revalidar cache da página
  revalidatePath('/users')

  // Redirecionar
  redirect('/users')
}

export async function deleteUser(id: number) {
  await prisma.user.delete({ where: { id } })
  revalidatePath('/users')
}
```

### Usando em formulário (Server Component)
```tsx
// app/users/new/page.tsx
import { createUser } from '@/app/actions/users'

export default function NewUserPage() {
  return (
    <form action={createUser}>
      <input name="name" placeholder="Nome" required />
      <input name="email" type="email" placeholder="Email" required />
      <button type="submit">Criar Usuário</button>
    </form>
  )
}
```

### Usando em Client Component (com feedback)
```tsx
'use client'

import { createUser } from '@/app/actions/users'
import { useActionState } from 'react'

export default function UserForm() {
  const [state, formAction, isPending] = useActionState(createUser, null)

  return (
    <form action={formAction}>
      <input name="name" placeholder="Nome" required />
      <input name="email" type="email" placeholder="Email" required />

      {state?.error && (
        <p className="text-red-500">{state.error}</p>
      )}

      <button type="submit" disabled={isPending}>
        {isPending ? 'Salvando...' : 'Criar Usuário'}
      </button>
    </form>
  )
}
```

---

## 7. Layouts

```tsx
// app/layout.tsx — Layout Raiz (OBRIGATÓRIO)
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Meu Sistema',
  description: 'Sistema de gestão',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>
        <header>...</header>
        <main>{children}</main>
        <footer>...</footer>
      </body>
    </html>
  )
}
```

```tsx
// app/dashboard/layout.tsx — Layout aninhado
import Sidebar from '@/components/Sidebar'

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">{children}</div>
    </div>
  )
}
```

---

## 8. Middleware e Autenticação

```tsx
// middleware.ts (na raiz do projeto)
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const token = request.cookies.get('auth-token')?.value

  // Proteger rotas do dashboard
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url))
    }
  }

  // Redirecionar se já logado
  if (request.nextUrl.pathname === '/login' && token) {
    return NextResponse.redirect(new URL('/dashboard', request.url))
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/dashboard/:path*', '/login'],
}
```

### Autenticação com Cookies HttpOnly
```tsx
// app/actions/auth.ts
'use server'

import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

export async function login(formData: FormData) {
  const email = formData.get('email') as string
  const password = formData.get('password') as string

  // Verificar credenciais
  const user = await verifyCredentials(email, password)
  if (!user) {
    return { error: 'Credenciais inválidas' }
  }

  // Criar token JWT
  const token = await createJWT(user)

  // Salvar em cookie HttpOnly (seguro)
  const cookieStore = await cookies()
  cookieStore.set('auth-token', token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    maxAge: 60 * 60 * 24 * 7, // 7 dias
  })

  redirect('/dashboard')
}

export async function logout() {
  const cookieStore = await cookies()
  cookieStore.delete('auth-token')
  redirect('/login')
}

export async function getSession() {
  const cookieStore = await cookies()
  const token = cookieStore.get('auth-token')?.value
  if (!token) return null
  return await verifyJWT(token)
}
```

---

## 9. Route Handlers (API Routes)

```tsx
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { prisma } from '@/lib/prisma'

// GET /api/users
export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams
  const page = Number(searchParams.get('page')) || 1

  const users = await prisma.user.findMany({
    take: 10,
    skip: (page - 1) * 10,
  })

  return NextResponse.json(users)
}

// POST /api/users
export async function POST(request: NextRequest) {
  const body = await request.json()

  const user = await prisma.user.create({
    data: {
      name: body.name,
      email: body.email,
    },
  })

  return NextResponse.json(user, { status: 201 })
}
```

```tsx
// app/api/users/[id]/route.ts
// GET /api/users/:id
export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params
  const user = await prisma.user.findUnique({
    where: { id: Number(id) },
  })

  if (!user) {
    return NextResponse.json({ error: 'Not found' }, { status: 404 })
  }

  return NextResponse.json(user)
}
```

---

## 10. CRUD Completo — Exemplo Prático

### Estrutura
```
app/
├── actions/
│   └── users.ts        # Server Actions
├── users/
│   ├── page.tsx         # Lista (Server Component)
│   ├── new/
│   │   └── page.tsx     # Formulário de criação
│   └── [id]/
│       ├── page.tsx     # Detalhes
│       └── edit/
│           └── page.tsx # Formulário de edição
```

### Server Actions
```tsx
// app/actions/users.ts
'use server'

import { prisma } from '@/lib/prisma'
import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'

export async function getUsers() {
  return prisma.user.findMany({ orderBy: { name: 'asc' } })
}

export async function getUser(id: number) {
  return prisma.user.findUnique({ where: { id } })
}

export async function createUser(formData: FormData) {
  await prisma.user.create({
    data: {
      name: formData.get('name') as string,
      email: formData.get('email') as string,
    },
  })
  revalidatePath('/users')
  redirect('/users')
}

export async function updateUser(id: number, formData: FormData) {
  await prisma.user.update({
    where: { id },
    data: {
      name: formData.get('name') as string,
      email: formData.get('email') as string,
    },
  })
  revalidatePath('/users')
  redirect('/users')
}

export async function deleteUser(id: number) {
  await prisma.user.delete({ where: { id } })
  revalidatePath('/users')
}
```

### Página de Lista
```tsx
// app/users/page.tsx
import Link from 'next/link'
import { getUsers, deleteUser } from '@/app/actions/users'

export default async function UsersPage() {
  const users = await getUsers()

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Usuários</h1>
        <Link href="/users/new"
          className="bg-blue-600 text-white px-4 py-2 rounded-lg">
          + Novo Usuário
        </Link>
      </div>

      <table className="w-full">
        <thead>
          <tr className="border-b">
            <th className="text-left py-2">Nome</th>
            <th className="text-left py-2">Email</th>
            <th className="text-right py-2">Ações</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id} className="border-b">
              <td className="py-2">{user.name}</td>
              <td className="py-2">{user.email}</td>
              <td className="py-2 text-right space-x-2">
                <Link href={`/users/${user.id}/edit`}
                  className="text-blue-600 hover:underline">
                  Editar
                </Link>
                <form action={deleteUser.bind(null, user.id)} className="inline">
                  <button type="submit" className="text-red-600 hover:underline">
                    Excluir
                  </button>
                </form>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
```

---

## 11. Otimizações Automáticas

### Imagens
```tsx
import Image from 'next/image'

<Image
  src="/logo.png"
  alt="Logo"
  width={200}
  height={50}
  priority  // Carrega imediatamente (acima do fold)
/>

// Imagem responsiva
<Image
  src="/hero.jpg"
  alt="Hero"
  fill                    // Preenche o container
  className="object-cover"
  sizes="(max-width: 768px) 100vw, 50vw"
/>
```

### Fontes
```tsx
// app/layout.tsx
import { Inter, Roboto_Mono } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
})

const robotoMono = Roboto_Mono({
  subsets: ['latin'],
  variable: '--font-roboto-mono',
})

export default function Layout({ children }) {
  return (
    <html className={`${inter.variable} ${robotoMono.variable}`}>
      <body className="font-sans">{children}</body>
    </html>
  )
}
```

### Metadata (SEO)
```tsx
// app/layout.tsx ou app/page.tsx
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    default: 'Meu Sistema',
    template: '%s | Meu Sistema'
  },
  description: 'Sistema de gestão corporativo',
  openGraph: {
    title: 'Meu Sistema',
    description: 'Sistema de gestão corporativo',
    images: ['/og-image.png'],
  },
}
```

```tsx
// Metadata dinâmica (páginas com parâmetros)
export async function generateMetadata({ params }) {
  const { id } = await params
  const user = await getUser(id)
  return {
    title: user.name,
    description: `Perfil de ${user.name}`,
  }
}
```

---

## 12. Variáveis de Ambiente

```env
# .env.local (NÃO commitar)
DATABASE_URL="postgresql://..."
JWT_SECRET="minha-chave-secreta"

# Variáveis que o BROWSER pode acessar (prefixo NEXT_PUBLIC_)
NEXT_PUBLIC_APP_URL="http://localhost:3000"
NEXT_PUBLIC_API_URL="https://api.exemplo.com"
```

```tsx
// Server-only
const secret = process.env.JWT_SECRET        // ✅ Funciona no servidor
// Client + Server
const url = process.env.NEXT_PUBLIC_APP_URL  // ✅ Funciona em ambos
```

---

## 13. Deploy

### Vercel (Recomendado)
```bash
npm i -g vercel
vercel
```

### Docker
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public

EXPOSE 3000
CMD ["node", "server.js"]
```

```js
// next.config.js (para Docker)
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
}
module.exports = nextConfig
```

---

## 14. Comandos Essenciais

| Comando | Descrição |
|---|---|
| `npm run dev` | Servidor de desenvolvimento |
| `npm run build` | Build de produção |
| `npm start` | Iniciar build de produção |
| `npx next lint` | Verificar ESLint |
| `npx prisma studio` | Interface visual do banco |
| `npx prisma migrate dev` | Aplicar migrations |

---

*Fonte: [nextjs.org/docs](https://nextjs.org/docs) — Consultado em 2026-02-14*
