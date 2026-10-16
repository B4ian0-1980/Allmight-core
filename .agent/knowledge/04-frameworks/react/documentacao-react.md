---json
{
  "id": "documentacao-react",
  "title": "React 19 — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "Guia tecnico e referencias sobre React 19 — Guia Completo.",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar React 19 — Guia Completo?",
    "Quais as boas praticas de react?"
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
  "dono": "stack-react",
  "prioridade": 2
}
---

# React 19 — Guia Completo

**Fonte:** [react.dev/learn](https://react.dev/learn) · [react.dev/reference](https://react.dev/reference/react)  
**Versão:** React 19  
**Categoria:** Frontend · Biblioteca UI  
**Última Atualização do Conteúdo:** 2026-02-14  
**Último Acesso às Fontes:** 2026-02-14

---

## 1. O que é React?

React é uma **biblioteca JavaScript para construir interfaces de usuário** com componentes reutilizáveis. Usa JSX (HTML dentro do JavaScript) e um modelo declarativo.

---

## 2. Criando Projeto

```bash
# Next.js (RECOMENDADO para produção)
npx create-next-app@latest meu-app

# Vite (SPA sem SSR)
npm create vite@latest meu-app -- --template react-ts
cd meu-app && npm install && npm run dev
```

---

## 3. Componentes

```tsx
// ✅ Function Component (PADRÃO)
function Welcome({ name }: { name: string }) {
  return <h1>Olá, {name}!</h1>
}

// ✅ Arrow function com tipos
type ButtonProps = {
  label: string
  onClick: () => void
  variant?: 'primary' | 'secondary'
}

const Button = ({ label, onClick, variant = 'primary' }: ButtonProps) => (
  <button className={`btn btn-${variant}`} onClick={onClick}>
    {label}
  </button>
)

// Usando
<Welcome name="João" />
<Button label="Salvar" onClick={() => save()} variant="primary" />
```

---

## 4. JSX

```tsx
function App() {
  const nome = 'João'
  const items = ['React', 'Next.js', 'TypeScript']
  const isAdmin = true

  return (
    <div className="app">
      {/* Expressão JavaScript */}
      <h1>Olá, {nome}!</h1>

      {/* Condicional */}
      {isAdmin && <span className="badge">Admin</span>}
      {isAdmin ? <AdminPanel /> : <UserPanel />}

      {/* Lista */}
      <ul>
        {items.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>

      {/* Estilo inline */}
      <div style={{ color: 'red', fontSize: '18px' }}>Destaque</div>
    </div>
  )
}
```

---

## 5. Hooks

### `useState` — Estado local
```tsx
import { useState } from 'react'

function Counter() {
  const [count, setCount] = useState(0)
  const [user, setUser] = useState({ name: '', email: '' })

  return (
    <>
      <p>Contagem: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
      <button onClick={() => setCount(prev => prev - 1)}>-1</button>

      {/* Atualizar objeto (spread obrigatório) */}
      <input
        value={user.name}
        onChange={e => setUser({ ...user, name: e.target.value })}
      />
    </>
  )
}
```

### `useEffect` — Efeitos colaterais
```tsx
import { useEffect, useState } from 'react'

function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        setUser(data)
        setLoading(false)
      })

    return () => { /* cleanup */ }
  }, [userId])

  if (loading) return <p>Carregando...</p>
  return <h1>{user?.name}</h1>
}
```

### `useRef` — Referência DOM / valor persistente
```tsx
import { useRef } from 'react'

function SearchBar() {
  const inputRef = useRef<HTMLInputElement>(null)
  const focusInput = () => inputRef.current?.focus()

  return (
    <>
      <input ref={inputRef} placeholder="Buscar..." />
      <button onClick={focusInput}>Focar</button>
    </>
  )
}
```

### `useMemo` e `useCallback` — Performance
```tsx
import { useMemo, useCallback } from 'react'

function ExpensiveList({ items, filter }) {
  const filtered = useMemo(() =>
    items.filter(item => item.name.includes(filter)), [items, filter])

  const handleClick = useCallback((id: string) => {
    console.log('Clicked:', id)
  }, [])

  return filtered.map(item => (
    <Item key={item.id} item={item} onClick={handleClick} />
  ))
}
```

### `useContext` — Estado global simples
```tsx
import { createContext, useContext, useState } from 'react'

const ThemeContext = createContext({ theme: 'light', toggle: () => {} })

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light')
  const toggle = () => setTheme(t => t === 'light' ? 'dark' : 'light')
  return (
    <ThemeContext.Provider value={{ theme, toggle }}>
      {children}
    </ThemeContext.Provider>
  )
}

function Header() {
  const { theme, toggle } = useContext(ThemeContext)
  return <button onClick={toggle}>{theme === 'light' ? '🌙' : '☀️'}</button>
}
```

---

## 6. Formulários

```tsx
function LoginForm() {
  const [form, setForm] = useState({ email: '', password: '' })
  const [errors, setErrors] = useState<Record<string, string>>({})

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const newErrors: Record<string, string> = {}
    if (!form.email) newErrors.email = 'Email obrigatório'
    if (!form.password) newErrors.password = 'Senha obrigatória'
    if (Object.keys(newErrors).length > 0) { setErrors(newErrors); return }

    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })
    if (res.ok) window.location.href = '/dashboard'
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" value={form.email} onChange={handleChange} />
      {errors.email && <span className="error">{errors.email}</span>}
      <input name="password" type="password" value={form.password} onChange={handleChange} />
      <button type="submit">Entrar</button>
    </form>
  )
}
```

---

## 7. Patterns Comuns

### Loading / Error
```tsx
function DataFetcher({ url }) {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(url)
      .then(r => r.json()).then(setData)
      .catch(e => setError(e.message))
      .finally(() => setLoading(false))
  }, [url])

  if (loading) return <Spinner />
  if (error) return <ErrorMessage message={error} />
  return <DataDisplay data={data} />
}
```

### Children
```tsx
function Card({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <div className="card-body">{children}</div>
    </div>
  )
}
```

---

## 8. Cheatsheet de Hooks

| Hook | Função |
|---|---|
| `useState` | Estado local do componente |
| `useEffect` | Side effects (fetch, timers, DOM) |
| `useRef` | Referência DOM / valor persistente |
| `useMemo` | Memoriza cálculo pesado |
| `useCallback` | Memoriza função |
| `useContext` | Acessa contexto global |
| `useReducer` | Estado complexo (tipo Redux) |
| `useId` | Gera ID único para acessibilidade |

---

*Fontes: [react.dev/learn](https://react.dev/learn) · [react.dev/reference](https://react.dev/reference/react) — Acessado em 2026-02-14*
