---json
{
  "id": "documentacao_aurelia",
  "title": "Documentação: Aurelia",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Tipo:** Framework JavaScript Moderno (Standards-based) **Site Oficial:** [aurelia.io](https://aurelia.io)",
  "gatilhos": [
    "aurelia",
    "documentacao",
    "frameworks",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Aurelia?",
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

# Documentação: Aurelia

> **Tipo:** Framework JavaScript Moderno (Standards-based)
> **Site Oficial:** [aurelia.io](https://aurelia.io)
> **Versão Atual:** Aurelia 2

## O que é?
Aurelia é um framework frontend que se orgulha de ser pouco intrusivo ("unobtrusive"). Ele permite escrever JavaScript/TypeScript puro (Vanilla) e, através de convenções inteligentes, transforma suas classes em componentes ricos. Ele evita a necessidade de aprender sintaxes proprietárias complexas comuns em outros frameworks.

## Filosofia
*   **Standards-First:** Construído sobre Web Components e padrões ES modernos.
*   **Convention over Configuration:** Menos boilerplate, mais código de negócio.
*   **Performance:** Utiliza técnicas avançadas (como batching de DOM) para alta performance.

## Estrutura de um Componente
Em Aurelia, um componente é geralmente um par de arquivos: `.js/.ts` (ViewModel) e `.html` (View).

**my-component.ts**
```typescript
export class MyComponent {
  message = "Hello World!";
  
  sayHello() {
    alert(this.message);
  }
}
```

**my-component.html**
```html
<template>
  <p>${message}</p>
  <button click.trigger="sayHello()">Diga Olá</button>
</template>
```

## Instalação (Aurelia 2)

```bash
npx makes aurelia
```
Isso iniciará um assistente interativo para criar seu projeto.

## Bindings (Vinculos)
*   `${valor}`: Interpolação de texto.
*   `value.bind="valor"`: Two-way binding (padrão para inputs).
*   `click.trigger="acao()"`: Event listener.
*   `if.bind="condicao"`: Renderização condicional.
*   `repeat.for="item of items"`: Loops.

## Referências
*   [Documentação Aurelia 2](https://docs.aurelia.io/)
*   [Guia de Migração (v1 -> v2)](https://docs.aurelia.io/migration)
