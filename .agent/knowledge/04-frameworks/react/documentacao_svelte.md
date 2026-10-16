---json
{
  "id": "documentacao_svelte",
  "title": "Documentação Svelte — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Fonte:** [svelte.dev](https://svelte.dev/docs) **Versão:** 5.x (Runes)",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "react",
    "svelte"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação Svelte — Guia Completo?",
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

# Documentação Svelte — Guia Completo

> **Fonte:** [svelte.dev](https://svelte.dev/docs)
> **Versão:** 5.x (Runes)
> **Atualizado:** 2026-02-14

---

## Sumário

1. [O que é Svelte?](#o-que-é-svelte)
2. [Instalação (SvelteKit)](#instalação)
3. [Sintaxe Básica](#sintaxe-básica)
4. [Reatividade (Runes)](#reatividade-runes)
5. [Props e Eventos](#props-e-eventos)
6. [Bindings](#bindings)
7. [Ciclo de Vida](#ciclo-de-vida)
8. [Stores (Legado vs Novo)](#stores)
9. [Animações](#animações)

---

## O que é Svelte?

Svelte é um framework que compila seu código para JavaScript vanilla otimizado em tempo de build, ao invés de interpretar o código no navegador com um Virtual DOM (como React/Vue).

**Principais Vantagens:**
- **Zero Runtime Overhead:** Bundle minúsculo.
- **Reatividade Verdadeira:** Sem `useState` complexo, apenas atribuição.
- **HTML-first:** Sintaxe próxima do padrão web.

---

## Instalação

```bash
# Criar projeto SvelteKit (padrão oficial)
npm create svelte@latest meu-app
cd meu-app
npm install
npm run dev
```

---

## Sintaxe Básica

Um componente `.svelte` tem 3 partes opcionais:

```html
<script>
  // Lógica JS/TS
  let nome = "Mundo";
</script>

<!-- Estrutura HTML -->
<h1>Olá, {nome}!</h1>

<style>
  /* CSS escopado por padrão */
  h1 { color: #ff3e00; }
</style>
```

---

## Reatividade (Runes - Svelte 5)

Svelte 5 introduziu **Runes** para controle explícito de reatividade.

### Estado (`$state`)
```javascript
<script>
  let count = $state(0);

  function increment() {
    count += 1;
  }
</script>

<button onclick={increment}>
  Contagem: {count}
</button>
```

### Estado Derivado (`$derived`)
Calculado automaticamente quando dependências mudam.
```javascript
<script>
  let width = $state(10);
  let height = $state(20);
  
  let area = $derived(width * height);
</script>

<p>Área: {area}</p>
```

### Efeitos (`$effect`)
Executa código quando dependências mudam (similar a `useEffect` do React).
```javascript
<script>
  let count = $state(0);

  $effect(() => {
    console.log(`Nova contagem: ${count}`);
    
    return () => {
      console.log('Cleanup antes da próxima execução');
    };
  });
</script>
```

---

## Lógica nos Templates

### If / Else
```html
{#if user.loggedIn}
  <button>Sair</button>
{:else}
  <button>Entrar</button>
{/if}
```

### Each (Loop)
```html
<ul>
  {#each items as item (item.id)}
    <li>{item.name}</li>
  {/each}
</ul>
```

### Await (Promessas)
```html
{#await promise}
  <p>Carregando...</p>
{:then data}
  <p>Dados: {data}</p>
{:catch error}
  <p>Erro: {error.message}</p>
{/await}
```

---

## Props e Eventos

### Recebendo Props (`$props`)
```javascript
// Child.svelte
<script>
  let { nome, idade = 18 } = $props();
</script>

<p>{nome} tem {idade} anos.</p>
```

### Emitindo Eventos
Em Svelte 5, funções callback via props são preferidas a eventos customizados.

```javascript
// Parent.svelte
<Child onSave={(data) => console.log(data)} />

// Child.svelte
<script>
  let { onSave } = $props();
</script>
<button onclick={() => onSave('dados')}>Salvar</button>
```

---

## Bindings

Two-way binding simplificado.

```html
<!-- Input de texto -->
<input bind:value={nome} />

<!-- Checkbox -->
<input type="checkbox" bind:checked={ativo} />

<!-- Grupo -->
<input type="radio" bind:group={sabor} value="baunilha">
<input type="radio" bind:group={sabor} value="chocolate">

<!-- Elemento DOM -->
<script>
  let canvas;
  
  $effect(() => {
    // canvas está disponível aqui
    const ctx = canvas.getContext('2d');
  });
</script>

<canvas bind:this={canvas}></canvas>
```

---

## Animações e Transições

Svelte inclui animações nativas.

```html
<script>
  import { fade, fly, slide } from 'svelte/transition';
  let visivel = $state(true);
</script>

<button onclick={() => visivel = !visivel}>Alternar</button>

{#if visivel}
  <div transition:fade>
    Desapareço suavemente
  </div>
  
  <div in:fly={{ y: 200 }} out:slide>
    Entro voando, saio deslizando
  </div>
{/if}
```

---

## Svelte CLI (`sv`)

O Svelte 5 introduziu uma nova e poderosa interface de linha de comando chamada `sv`.

### Instalação e Uso
Não é necessário instalar globalmente. Use via `npx`:

```bash
npx sv
```

### Comandos Principais
*   `npx sv create`: Cria um novo projeto.
    *   Opções: `--template minimal` (ou `demo`, `library`), `--types ts` (ou `jsdoc`).
*   `npx sv add`: Adiciona integrações (Tailwind, Playwright, etc).
*   `npx sv check`: Roda checagem de tipos.

---

*Fonte: [svelte.dev](https://svelte.dev/docs/svelte/overview) e [Svelte CLI](https://svelte.dev/docs/cli/overview)*
