---json
{
  "id": "documentacao_tailwindcss",
  "title": "Tailwind CSS — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "tailwind",
  "resumo": "⚠️ **Regra:** Prefira classes inline. Use `@apply` apenas para componentes que se repetem 3+ vezes e não podem ser componentizados (ex: em `.blade.php`).",
  "gatilhos": [
    "completo",
    "css",
    "documentacao",
    "frameworks",
    "guia",
    "tailwind",
    "tailwindcss"
  ],
  "perguntas_tipo": [
    "Como utilizar Tailwind CSS — Guia Completo?",
    "Quais as boas praticas de tailwind?"
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
  "dono": "stack-tailwind",
  "prioridade": 2
}
---

# Tailwind CSS — Guia Completo

**Fonte:** [tailwindcss.com](https://tailwindcss.com) | **Versão:** 4.x / 3.x  
**Categoria:** Framework CSS Utility-First

---

## 1. Instalação

### Via Vite (React, Vue, Svelte)
```bash
npm install -D tailwindcss @tailwindcss/vite
```

```js
// vite.config.js
import tailwindcss from '@tailwindcss/vite'

export default {
  plugins: [tailwindcss()],
}
```

```css
/* src/index.css */
@import "tailwindcss";
```

### Via PostCSS (Laravel, Next.js, Nuxt)
```bash
npm install -D tailwindcss @tailwindcss/postcss autoprefixer
```

```js
// postcss.config.js
export default {
  plugins: {
    '@tailwindcss/postcss': {},
    autoprefixer: {},
  },
}
```

### Via CLI (sem bundler)
```bash
npx @tailwindcss/cli -i src/input.css -o dist/output.css --watch
```

---

## 2. Conceito: Utility-First

Em vez de classes semânticas (`.btn-primary`), usa classes utilitárias diretamente:

```html
<!-- ❌ CSS Tradicional -->
<button class="btn btn-primary">Salvar</button>

<!-- ✅ Tailwind -->
<button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">
  Salvar
</button>
```

**Vantagens:**
- Sem inventar nomes de classes
- Sem CSS morto
- Mudanças locais (sem efeitos colaterais)
- Design consistente via tokens

---

## 3. Flexbox & Grid

### Flexbox
```html
<!-- Flex row com espaçamento -->
<div class="flex items-center justify-between gap-4">
  <span>Logo</span>
  <nav class="flex gap-2">
    <a href="#">Home</a>
    <a href="#">About</a>
  </nav>
</div>

<!-- Flex column centralizado -->
<div class="flex flex-col items-center justify-center min-h-screen">
  <h1>Centralizado</h1>
</div>
```

| Classe | CSS |
|---|---|
| `flex` | `display: flex` |
| `flex-col` | `flex-direction: column` |
| `items-center` | `align-items: center` |
| `justify-between` | `justify-content: space-between` |
| `gap-4` | `gap: 1rem` |
| `flex-1` | `flex: 1 1 0%` |
| `flex-wrap` | `flex-wrap: wrap` |
| `shrink-0` | `flex-shrink: 0` |

### Grid
```html
<!-- Grid 3 colunas -->
<div class="grid grid-cols-3 gap-4">
  <div class="bg-slate-100 p-4">1</div>
  <div class="bg-slate-100 p-4">2</div>
  <div class="bg-slate-100 p-4">3</div>
</div>

<!-- Grid responsivo -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
  <!-- Cards aqui -->
</div>

<!-- Item ocupando 2 colunas -->
<div class="col-span-2">Largo</div>
```

| Classe | CSS |
|---|---|
| `grid` | `display: grid` |
| `grid-cols-3` | `grid-template-columns: repeat(3, 1fr)` |
| `col-span-2` | `grid-column: span 2 / span 2` |
| `grid-rows-2` | `grid-template-rows: repeat(2, 1fr)` |

---

## 4. Responsividade (Mobile First)

Tailwind é **mobile-first**: classes sem prefixo = mobile. Prefixos = breakpoint mínimo.

| Prefixo | Breakpoint | Viewport |
|---|---|---|
| *(nenhum)* | `0px+` | Mobile |
| `sm:` | `640px+` | Tablet pequeno |
| `md:` | `768px+` | Tablet |
| `lg:` | `1024px+` | Desktop |
| `xl:` | `1280px+` | Desktop grande |
| `2xl:` | `1536px+` | Monitor wide |

```html
<!-- Mobile: 1 col | Tablet: 2 cols | Desktop: 4 cols -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
  <!-- conteúdo -->
</div>

<!-- Mobile: stack | Desktop: side-by-side -->
<div class="flex flex-col lg:flex-row gap-6">
  <aside class="w-full lg:w-64">Sidebar</aside>
  <main class="flex-1">Conteúdo</main>
</div>

<!-- Esconder no mobile, mostrar no desktop -->
<nav class="hidden md:flex gap-4">...</nav>
```

---

## 5. Dark Mode

### Ativação automática (preferência do sistema)
```html
<div class="bg-white dark:bg-gray-900 text-black dark:text-white">
  <h1 class="text-gray-900 dark:text-gray-100">Título</h1>
  <p class="text-gray-600 dark:text-gray-400">Texto</p>
</div>
```

### Ativação manual (toggle com classe)
```js
// tailwind.config.js (v3)
module.exports = {
  darkMode: 'class', // ou 'selector' no v4
}
```

```js
// Toggle via JS
document.documentElement.classList.toggle('dark')
```

```html
<button onclick="document.documentElement.classList.toggle('dark')">
  🌙 / ☀️
</button>
```

---

## 6. Configuração do Tema (`tailwind.config.js`)

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,vue}",
    "./resources/views/**/*.blade.php",  // Laravel
  ],
  theme: {
    extend: {
      // Cores personalizadas
      colors: {
        brand: {
          50:  '#eff6ff',
          500: '#3b82f6',
          600: '#2563eb',
          900: '#1e3a8a',
        },
        sesau: '#1a5276',
      },
      // Fontes
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      // Espaçamentos extras
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      // Bordas
      borderRadius: {
        '4xl': '2rem',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),        // Estiliza inputs
    require('@tailwindcss/typography'),    // Classe `prose` para conteúdo
    require('@tailwindcss/aspect-ratio'),  // Aspect ratios
  ],
}
```

### Usando no HTML
```html
<div class="bg-brand-500 text-white font-sans">
  Usando cor e fonte customizada
</div>
```

---

## 7. `@apply` vs Classes Inline

### Classes inline (RECOMENDADO)
```html
<button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
  Salvar
</button>
```

### `@apply` (para componentes reutilizáveis)
```css
/* Apenas quando há muita repetição */
@layer components {
  .btn-primary {
    @apply bg-blue-600 text-white px-4 py-2 rounded-lg
           hover:bg-blue-700 transition-colors
           focus:outline-none focus:ring-2 focus:ring-blue-500;
  }

  .input-field {
    @apply w-full border border-gray-300 rounded-lg px-3 py-2
           focus:border-blue-500 focus:ring-1 focus:ring-blue-500
           dark:bg-gray-800 dark:border-gray-600 dark:text-white;
  }

  .card {
    @apply bg-white dark:bg-gray-800 rounded-xl shadow-md p-6;
  }
}
```

> ⚠️ **Regra:** Prefira classes inline. Use `@apply` apenas para componentes que se repetem 3+ vezes e não podem ser componentizados (ex: em `.blade.php`).

---

## 8. Estados e Pseudo-classes

```html
<!-- Hover -->
<button class="bg-blue-500 hover:bg-blue-700">Botão</button>

<!-- Focus -->
<input class="border focus:border-blue-500 focus:ring-2 focus:ring-blue-200">

<!-- Active (clicando) -->
<button class="bg-blue-500 active:bg-blue-800">Clique</button>

<!-- Disabled -->
<button class="bg-blue-500 disabled:opacity-50 disabled:cursor-not-allowed" disabled>
  Desativado
</button>

<!-- Group hover (pai controla filho) -->
<div class="group cursor-pointer">
  <h3 class="group-hover:text-blue-600">Título</h3>
  <p class="group-hover:underline">Subtítulo</p>
</div>

<!-- First/Last child -->
<li class="first:pt-0 last:pb-0 py-4 border-b last:border-0">Item</li>

<!-- Placeholder -->
<input class="placeholder:text-gray-400 placeholder:italic" placeholder="Buscar...">
```

---

## 9. Spacing & Sizing — Escala de Referência

| Valor | rem | Pixels |
|---|---|---|
| `0` | 0 | 0px |
| `1` | 0.25rem | 4px |
| `2` | 0.5rem | 8px |
| `3` | 0.75rem | 12px |
| `4` | 1rem | 16px |
| `6` | 1.5rem | 24px |
| `8` | 2rem | 32px |
| `12` | 3rem | 48px |
| `16` | 4rem | 64px |
| `24` | 6rem | 96px |
| `32` | 8rem | 128px |
| `48` | 12rem | 192px |
| `64` | 16rem | 256px |
| `96` | 24rem | 384px |

```html
<div class="p-4 m-2 w-64 h-32 max-w-xl min-h-screen">
  <!-- p = padding, m = margin, w = width, h = height -->
</div>
```

---

## 10. Tipografia

```html
<!-- Tamanhos -->
<p class="text-xs">12px</p>
<p class="text-sm">14px</p>
<p class="text-base">16px (padrão)</p>
<p class="text-lg">18px</p>
<p class="text-xl">20px</p>
<p class="text-2xl">24px</p>
<p class="text-4xl">36px</p>

<!-- Peso -->
<p class="font-light">Light (300)</p>
<p class="font-normal">Normal (400)</p>
<p class="font-medium">Medium (500)</p>
<p class="font-semibold">Semibold (600)</p>
<p class="font-bold">Bold (700)</p>

<!-- Cores -->
<p class="text-gray-900 dark:text-gray-100">Título</p>
<p class="text-gray-600 dark:text-gray-400">Corpo</p>
<p class="text-gray-400 dark:text-gray-500">Secundário</p>

<!-- Alinhamento -->
<p class="text-center md:text-left">Centralizado no mobile</p>

<!-- Plugin Typography (para conteúdo markdown/HTML) -->
<article class="prose prose-lg dark:prose-invert max-w-none">
  <h1>Artigo renderizado com formatação bonita</h1>
  <p>Parágrafos, listas, código — tudo estilizado automaticamente.</p>
</article>
```

---

## 11. Componentes Comuns — Receitas

### Card
```html
<div class="bg-white dark:bg-gray-800 rounded-xl shadow-md overflow-hidden">
  <img class="w-full h-48 object-cover" src="..." alt="...">
  <div class="p-6">
    <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Título</h3>
    <p class="mt-2 text-gray-600 dark:text-gray-400">Descrição do card.</p>
    <button class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
      Ação
    </button>
  </div>
</div>
```

### Navbar
```html
<nav class="bg-white dark:bg-gray-900 shadow-sm border-b dark:border-gray-800">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <span class="text-xl font-bold text-blue-600">Logo</span>
      <div class="hidden md:flex gap-6">
        <a href="#" class="text-gray-700 dark:text-gray-300 hover:text-blue-600">Home</a>
        <a href="#" class="text-gray-700 dark:text-gray-300 hover:text-blue-600">Sobre</a>
        <a href="#" class="text-gray-700 dark:text-gray-300 hover:text-blue-600">Contato</a>
      </div>
    </div>
  </div>
</nav>
```

### Formulário
```html
<form class="space-y-4 max-w-md">
  <div>
    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
      Email
    </label>
    <input type="email"
      class="w-full border border-gray-300 dark:border-gray-600 rounded-lg px-3 py-2
             bg-white dark:bg-gray-800 text-gray-900 dark:text-white
             focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
      placeholder="seu@email.com">
  </div>
  <button type="submit"
    class="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition">
    Enviar
  </button>
</form>
```

### Badge / Tag
```html
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
             bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200">
  Ativo
</span>
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
             bg-red-100 text-red-800">
  Inativo
</span>
```

---

## 12. Integração com Frameworks

### Laravel (Blade)
```bash
npm install -D tailwindcss @tailwindcss/postcss autoprefixer
```
```js
// postcss.config.js
export default {
  plugins: {
    '@tailwindcss/postcss': {},
    autoprefixer: {},
  },
}
```
```css
/* resources/css/app.css */
@import "tailwindcss";
```

### React / Next.js
```bash
npx create-next-app@latest --tailwind
# Tailwind já vem configurado!
```

### Vue 3 / Nuxt
```bash
npm install -D tailwindcss @tailwindcss/vite
```
```js
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
})
```

---

## 13. Bibliotecas de Componentes Compatíveis

| Biblioteca | Tipo | Link |
|---|---|---|
| **shadcn/ui** | Componentes copiáveis (React) | [ui.shadcn.com](https://ui.shadcn.com) |
| **Headless UI** | Componentes sem estilo (React/Vue) | [headlessui.com](https://headlessui.com) |
| **Radix UI** | Primitivos acessíveis (React) | [radix-ui.com](https://www.radix-ui.com) |
| **DaisyUI** | Plugin de componentes Tailwind | [daisyui.com](https://daisyui.com) |
| **Flowbite** | Componentes prontos | [flowbite.com](https://flowbite.com) |

---

## 14. Dicas de Performance

1. **Content paths corretos** — Garanta que `content` inclua todos os arquivos que usam classes
2. **Evite classes dinâmicas** — `bg-${color}-500` NÃO funciona. Use `bg-red-500` completo
3. **Purge automático** — Em produção, classes não usadas são removidas automaticamente
4. **Agrupamento com `@apply`** — Use apenas para componentes muito repetidos

```html
<!-- ❌ NÃO funciona (classe dinâmica) -->
<div class="bg-{{ color }}-500">

<!-- ✅ Funciona (classe completa) -->
<div class="{{ color === 'red' ? 'bg-red-500' : 'bg-blue-500' }}">
```

---

*Fonte: [tailwindcss.com/docs](https://tailwindcss.com/docs) — Consultado em 2026-02-14*
