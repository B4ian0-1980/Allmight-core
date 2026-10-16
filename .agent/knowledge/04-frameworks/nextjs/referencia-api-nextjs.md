---json
{
  "id": "referencia-api-nextjs",
  "title": "Referência da API do Next.js (App Router)",
  "categoria": "04-frameworks",
  "subcategoria": "nextjs",
  "resumo": "**Fonte Oficial**: [https://nextjs.org/docs/app/api-reference](https://nextjs.org/docs/app/api-reference) *Este documento serve como guia de consulta rápida para as principais funcionalidades do Next.js 14+.*",
  "gatilhos": [
    "api",
    "app",
    "frameworks",
    "next",
    "nextjs",
    "referencia",
    "router"
  ],
  "perguntas_tipo": [
    "Como utilizar Referência da API do Next.js (App Router)?",
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

# Referência da API do Next.js (App Router)

> **Fonte Oficial**: [https://nextjs.org/docs/app/api-reference](https://nextjs.org/docs/app/api-reference)  
> *Este documento serve como guia de consulta rápida para as principais funcionalidades do Next.js 14+.*

## 1. Diretivas (Directives)
Instruções especiais colocadas no topo dos arquivos.

- **`'use client'`**: Marca um componente e seus filhos como Client Components (executados no navegador, suportam hooks e interatividade).
- **`'use server'`**: Marca uma função (Server Action) ou arquivo como código exclusivo do servidor, que pode ser chamado pelo cliente.

## 2. Convenções de Arquivos (File Conventions)
Arquivos especiais dentro da pasta `app/` que definem o roteamento e a UI.

| Arquivo | Função |
|---------|--------|
| `layout.tsx` | UI compartilhada entre uma rota e seus filhos. Mantém estado na navegação. |
| `page.tsx` | A UI exclusiva de uma rota (ex: `/dashboard`). É o ponto principal de renderização. |
| `loading.tsx` | UI de carregamento (Suspense) exibida enquanto a página carrega. |
| `not-found.tsx` | UI exibida quando a função `notFound()` é chamada ou rota não existe. |
| `error.tsx` | UI de tratamento de erro (Error Boundary) para capturar exceções em tempo de execução. |
| `global-error.tsx` | Tratamento de erro para o layout raiz (`root layout`), capturando erros globais. |
| `route.ts` | Endpoint de API (Route Handler) para métodos HTTP (GET, POST, etc.). |
| `template.tsx` | Similar ao layout, mas cria uma nova instância a cada navegação (não preserva estado). |
| `default.tsx` | UI de fallback para Parallel Routes. |
| `opencraph-image.tsx` | Gera imagens OG (Open Graph) dinamicamente. |
| `sitemap.ts` | Gera o arquivo `sitemap.xml`. |

## 3. Funções e Hooks (Functions)
Funções essenciais para manipulação de dados e navegação.

### Data Fetching
- **`fetch()`**: API Web estendida pelo Next.js com controle de cache (`force-cache`, `no-store`) e revalidação (`next: { revalidate: 3600 }`).

### Server Components (Apenas no Servidor)
- **`cookies()`**: Ler e gravar cookies.
- **`headers()`**: Ler cabeçalhos da requisição.
- **`redirect(url)`**: Redireciona o usuário para outra rota (lança um erro interno).
- **`notFound()`**: Redireciona para a tela de 404.

### Client Components (Hooks)
- **`useRouter()`**: Controle programático de navegação (`push`, `replace`, `back`).
- **`usePathname()`**: Retorna o caminho da URL atual.
- **`useSearchParams()`**: Acessa os parâmetros da query string da URL.
- **`useParams()`**: Acessa os parâmetros dinâmicos da rota (ex: `[id]`).

## 4. Componentes Built-in
Componentes otimizados fornecidos pelo Next.js.

- **`<Link>`**: Navegação entre páginas via *client-side* (SPA). Faz prefetching automático.
- **`<Image>`**: Otimização automática de imagens (formato, tamanho, lazy load). Requer configuração local ou remota.
- **`<Script>`**: Carregamento otimizado de scripts de terceiros (Analytics, Ads).

## 5. Configuração (next.config.js)
Principais opções de configuração.

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [ ... ], // Permitir domínios externos de imagem
  },
  logging: {
    fetches: {
      fullUrl: true, // Log detalhado de requisições fetch
    },
  },
  serverActions: {
    // Configurações de segurança para Actions (padrão no Next 14)
  }
}
module.exports = nextConfig
```

## 6. CLI (Command Line Interface)
- `next dev`: Inicia servidor de desenvolvimento (HMR, Fast Refresh).
- `next build`: Compila a aplicação para produção.
- `next start`: Inicia o servidor de produção (após build).
- `next lint`: Executa verificação de código (ESLint).
