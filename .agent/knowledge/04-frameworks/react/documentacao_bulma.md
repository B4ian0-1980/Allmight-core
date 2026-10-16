---json
{
  "id": "documentacao_bulma",
  "title": "Documentação: Bulma",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Tipo:** Framework CSS (Moderno/Flexbox) **Site Oficial:** [bulma.io](https://bulma.io)",
  "gatilhos": [
    "bulma",
    "documentacao",
    "frameworks",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Bulma?",
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

# Documentação: Bulma

> **Tipo:** Framework CSS (Moderno/Flexbox)
> **Site Oficial:** [bulma.io](https://bulma.io)
> **Dependências:** Nenhuma (JS Free)

## O que é?
Bulma é um framework CSS gratuito e open source baseado inteiramente em **Flexbox**. Ele é conhecido por ser fácil de aprender, ter uma sintaxe legível e ser totalmente modular (você importa apenas o que precisa).

## Instalação

### Via CDN
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
```

### Via npm
```bash
npm install bulma
```

## Conceitos Chave

### 1. Modificadores
A maioria dos elementos Bulma tem variações alternativas ativadas por classes que começam com `is-` ou `has-`.

```html
<a class="button is-primary is-large">Botão Grande</a>
<div class="box has-text-centered">Texto Centralizado</div>
```

### 2. Grid System (Columns)
O sistema de colunas é simples e automático.

```html
<div class="columns">
  <div class="column">Primeira coluna</div>
  <div class="column">Segunda coluna</div>
  <div class="column">Terceira coluna</div>
  <div class="column">Quarta coluna</div>
</div>
```
O Bulma ajusta automaticamente a largura. Para tamanhos fixos: `is-three-quarters`, `is-two-thirds`, `is-half`, etc.

### 3. Componentes
*   **Hero:** Um banner grande para títulos (muito comum em landing pages).
*   **Box:** Um container com sombra e padding.
*   **Level:** Uma barra horizontal multifuncional.
*   **Tiles:** Sistema de grid aninhado para criar layouts estilo Pinterest/Metro.

## Exemplo: Hero
```html
<section class="hero is-primary">
  <div class="hero-body">
    <p class="title">
      Título Heroico
    </p>
    <p class="subtitle">
      Subtítulo impactante
    </p>
  </div>
</section>
```

## Por que usar Bulma?
*   **JS Free:** Ele é puramente CSS. Você não precisa se preocupar com conflitos de plugins JS (como no Bootstrap ou Foundation).
*   **Legibilidade:** Classes como `is-active`, `is-loading`, `is-danger` tornam o código HTML fácil de ler.

## Referências
*   [Documentação Oficial](https://bulma.io/documentation/)
*   [Expo (Showcase)](https://bulma.io/expo/)
