---json
{
  "id": "documentacao_semantic_ui",
  "title": "Documentação: Semantic UI",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Tipo:** Framework de Interface (UI) **Site Oficial:** [semantic-ui.com](https://semantic-ui.com)",
  "gatilhos": [
    "documentacao",
    "frameworks",
    "react",
    "semantic"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Semantic UI?",
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

# Documentação: Semantic UI

> **Tipo:** Framework de Interface (UI)
> **Site Oficial:** [semantic-ui.com](https://semantic-ui.com)
> **Forks Modernos:** Fomantic-UI (Ativo)

## O que é?
Semantic UI é um framework de desenvolvimento que ajuda a criar layouts bonitos e responsivos usando HTML amigável (semântico). O objetivo é tratar palavras e classes como conceitos de troca de informações.

## Filosofia
Em vez de usar abreviações crípticas (como `btn-primary`, `col-md-4`), o Semantic usa linguagem natural.

**Bootstrap:**
```html
<button class="btn btn-primary btn-lg">Button</button>
```

**Semantic UI:**
```html
<button class="ui large primary button">Button</button>
```

## Instalação

### Via CDN
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.js"></script>
```

Requer jQuery.

## Componentes Principais
O Semantic UI é extremamente rico em componentes visuais prontos:

*   **Elements:** Button, Container, Divider, Flag, Header, Icon, Image, Input, Label, List, Loader.
*   **Collections:** Breadcrumb, Form, Grid, Menu, Message, Table.
*   **Views:** Card, Feed, Item, Statistic.
*   **Modules:** Accordion, Checkbox, Dimmer, Dropdown, Modal, Popup, Sidebar.

## Exemplo: Card
```html
<div class="ui card">
  <div class="image">
    <img src="/images/avatar2/large/kristy.png">
  </div>
  <div class="content">
    <a class="header">Kristy</a>
    <div class="meta">
      <span class="date">Joined in 2013</span>
    </div>
    <div class="description">
      Kristy is an art director living in New York.
    </div>
  </div>
</div>
```

## Status do Projeto
O repositório original `Semantic-Org/Semantic-UI` teve paralisia no desenvolvimento. A comunidade criou um fork ativo e mantido chamado **Fomantic-UI**, que é retrocompatível e recomendado para novos projetos.

## Referências
*   [Semantic UI Docs](https://semantic-ui.com/)
*   [Fomantic-UI (Fork Ativo)](https://fomantic-ui.com/)
