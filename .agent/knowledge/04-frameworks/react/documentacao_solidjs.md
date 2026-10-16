---json
{
  "id": "documentacao_solidjs",
  "title": "Documentação SolidJS — Guia Completo",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Fonte:** [solidjs.com](https://www.solidjs.com/docs/latest) **Versão:** 1.8+",
  "gatilhos": [
    "completo",
    "documentacao",
    "frameworks",
    "guia",
    "react",
    "solidjs"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação SolidJS — Guia Completo?",
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

# Documentação SolidJS — Guia Completo

> **Fonte:** [solidjs.com](https://www.solidjs.com/docs/latest)
> **Versão:** 1.8+
> **Atualizado:** 2026-02-14

---

## Sumário

1. [O que é SolidJS?](#o-que-é-solidjs)
2. [Instalação](#instalação)
3. [Sintaxe e JSX](#sintaxe-e-jsx)
4. [Reatividade (Signals)](#reatividade-signals)
5. [Efeitos e Computados](#efeitos-e-computados)
6. [Controle de Fluxo](#controle-de-fluxo)
7. [Ciclo de Vida](#ciclo-de-vida)
8. [Stores (Estado Aninhado)](#stores-estado-aninhado)

---

## O que é SolidJS?

SolidJS é um framework declarativo que parece React, mas funciona de forma **completamente diferente**.

**Diferença Chave:**
- **React:** Re-executa o componente inteiro quando o estado muda.
- **SolidJS:** Executa a função do componente **uma única vez** (setup). Apenas as partes do DOM que dependem de um Signal são atualizadas. Sem Virtual DOM.

---

## Instalação

```bash
# Templates oficiais
npx degit solidjs/templates/ts meu-projeto
cd meu-projeto
npm install
npm run dev
```

---

## Sintaxe e JSX

Usa JSX como o React, mas `class` é `class` (não `className`) e eventos são `onClick`, `onInput`.

```jsx
import { render } from 'solid-js/web';

function App() {
  return <div class="container">Olá Solid!</div>;
}

render(() => <App />, document.getElementById('root'));
```

---

## Reatividade (Signals)

Signals são a base da reatividade. Eles contêm o valor e avisam quem deve atualizar.

```jsx
import { createSignal } from 'solid-js';

function Counter() {
  // Retorna getter (count) e setter (setCount)
  // Note: count é uma FUNÇÃO, não uma variável
  const [count, setCount] = createSignal(0);

  const increment = () => setCount(count() + 1);

  return (
    <button onClick={increment}>
      {/* Chamamos a função para ler o valor */}
      Contagem: {count()}
    </button>
  );
}
```

---

## Efeitos e Computados

### Derived Signals (Memos)
Valores calculados que atualizam automaticamente. Otimizados para re-executar apenas se dependências mudarem.

```jsx
import { createSignal, createMemo } from 'solid-js';

const [count, setCount] = createSignal(0);
const double = createMemo(() => count() * 2);

console.log(double()); // 0
```

### Effects
Executam colaterais quando os sinais lidos dentro deles mudam. Renderização, chamadas de API, logs.

```jsx
import { createEffect } from 'solid-js';

createEffect(() => {
  console.log("A contagem é", count());
  // Roda sempre que count() mudar
});
```

---

## Controle de Fluxo

Em Solid, não usamos `map` ou ternários diretamente no JSX para listas grandes, pois isso recriaria todo o DOM. Usamos componentes de controle.

### Show (If/Else)
```jsx
import { Show } from 'solid-js';

<Show when={user.loggedIn} fallback={<button>Login</button>}>
  <button>Logout</button>
</Show>
```

### For (Listas Otimizadas)
Para `Keyed` rendering automático (por referência).

```jsx
import { For } from 'solid-js';

const [cats, setCats] = createSignal(['Marrie', 'Jujuba', 'Pudim']);

<ul>
  <For each={cats()}>{(cat, i) =>
    <li>{i() + 1}: {cat}</li>
  }</For>
</ul>
```
*(Se a lista mudar, Solid atualiza apenas os itens alterados, sem recriar a lista toda)*

### Switch / Match
```jsx
import { Switch, Match } from 'solid-js';

<Switch fallback={<p>Página não encontrada</p>}>
  <Match when={page() === 'home'}> <Home /> </Match>
  <Match when={page() === 'about'}> <About /> </Match>
</Switch>
```

---

## Ciclo de Vida

Como componentes rodam uma vez, `onMount` e `onCleanup` são usados.

```jsx
import { onMount, onCleanup } from 'solid-js';

onMount(() => {
  console.log("Componente montado no DOM");
    
  const timer = setInterval(() => console.log('tick'), 1000);

  onCleanup(() => {
    clearInterval(timer);
    console.log("Componente desmontado");
  });
});
```

---

## Stores (Estado Aninhado)

Para objetos complexos e arrays profundos, Signals podem ser manuais demais. `createStore` usa Proxies para permitir mutação fina.

```jsx
import { createStore } from 'solid-js/store';

const [state, setState] = createStore({
  user: {
    name: "João",
    settings: { theme: "dark" }
  },
  tasks: []
});

// Ler
console.log(state.user.name);

// Atualizar (Mutation style, mas imutável por baixo)
setState("user", "settings", "theme", "light");

setState("tasks", (tasks) => [...tasks, { id: 1, title: "Nova tarefa" }]);
```

---

*Fonte: [solidjs.com/docs](https://www.solidjs.com/docs/latest)*
