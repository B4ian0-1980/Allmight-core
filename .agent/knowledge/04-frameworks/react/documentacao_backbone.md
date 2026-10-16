---json
{
  "id": "documentacao_backbone",
  "title": "Documentação: Backbone.js",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Status:** Legado / Manutenção **Tipo:** Biblioteca MVC (Minimalista)",
  "gatilhos": [
    "backbone",
    "documentacao",
    "frameworks",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Backbone.js?",
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

# Documentação: Backbone.js

> **Status:** Legado / Manutenção
> **Tipo:** Biblioteca MVC (Minimalista)
> **Site Oficial:** [backbonejs.org](https://backbonejs.org)

## O que é?
Backbone.js é uma biblioteca JavaScript leve que fornece estrutura para aplicações web pesadas. Ele oferece Modelos com eventos de chave-valor e validação, Coleções com API rica de enumeração, views com tratamento de eventos declarativo e conecta tudo à sua API REST existente via interface JSON.

## Por que ainda é usado? (Contexto Legado)
Embora frameworks modernos (React, Vue) tenham dominado, o Backbone ainda é encontrado em muitos sistemas legados e sites de alto tráfego devido à sua estabilidade, tamanho minúsculo e simplicidade.

## Estrutura Principal (MV*)

### 1. Models (Modelos)
O coração da aplicação. Contém dados e lógica de negócios.

```javascript
var Todo = Backbone.Model.extend({
  defaults: {
    title: '',
    completed: false
  },
  toggle: function() {
    this.save({completed: !this.get('completed')});
  }
});
```

### 2. Collections (Coleções)
Conjuntos ordenados de modelos.

```javascript
var TodoList = Backbone.Collection.extend({
  model: Todo,
  url: '/api/todos'
});
```

### 3. Views (Visões)
Lógica de apresentação. Não contém HTML (geralmente usa templates como Underscore ou Handlebars), mas controla eventos do DOM.

```javascript
var TodoView = Backbone.View.extend({
  tagName:  'li',
  events: {
    'click .toggle': 'toggleDone',
    'dblclick .view': 'edit',
  },
  render: function() {
    this.$el.html(this.template(this.model.toJSON()));
    return this;
  }
});
```

### 4. Router (Roteador)
Gerencia o estado da aplicação e URLs.

```javascript
var Workspace = Backbone.Router.extend({
  routes: {
    "help":                 "help",    // #help
    "search/:query":        "search",  // #search/kiwis
  },
  search: function(query) {
    // ...
  }
});
```

## Instalação (Legada)
Geralmente via CDN ou baixando o arquivo.

Dependências Fortes:
*   Underscore.js (>= 1.8.3)
*   jQuery (Recomendado para manipulação de DOM e AJAX)

```html
<script src="jquery.js"></script>
<script src="underscore.js"></script>
<script src="backbone.js"></script>
```

## Referências
*   [Documentação Oficial](https://backbonejs.org/)
*   [Underscore.js](https://underscorejs.org/)
