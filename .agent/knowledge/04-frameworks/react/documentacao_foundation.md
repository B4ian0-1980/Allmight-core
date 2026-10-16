---json
{
  "id": "documentacao_foundation",
  "title": "Documentação: Foundation",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Tipo:** Framework CSS / Frontend Responsivo **Desenvolvedor:** ZURB",
  "gatilhos": [
    "documentacao",
    "foundation",
    "frameworks",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Foundation?",
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

# Documentação: Foundation

> **Tipo:** Framework CSS / Frontend Responsivo
> **Desenvolvedor:** ZURB
> **Site Oficial:** [get.foundation](https://get.foundation)

## O que é?
Foundation é um framework front-end responsivo avançado. Conhecido por ser profissional, flexível e semântico. É frequentemente escolhido por designers que querem controle total e personalização via Sass, em oposição à estética "padrão" do Bootstrap.

## Principais Recursos
*   **Grid XY:** Um sistema de grid flexível e moderno (inspirado em Flexbox).
*   **Componentes de UI:** Botões, navegação, cards, callouts, modais (Reveal), tooltips.
*   **Acessibilidade:** Foco nativo em a11y (ARIA attributes).
*   **Sass:** Arquitetura modular construída sobre SCSS.

## Instalação

### Via CDN (Rápido)
```html
<!-- CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/foundation-sites@6.7.5/dist/css/foundation.min.css" crossorigin="anonymous">

<!-- JS -->
<script src="https://cdn.jsdelivr.net/npm/foundation-sites@6.7.5/dist/js/foundation.min.js" crossorigin="anonymous"></script>
```

### Via CLI (Recomendado para customização)
```bash
npm install --global foundation-cli
foundation new --framework sites
```

## Exemplo de Grid (Grid XY)
```html
<div class="grid-x grid-margin-x">
  <div class="cell small-4">1/3 da largura</div>
  <div class="cell small-4">1/3 da largura</div>
  <div class="cell small-4">1/3 da largura</div>
</div>
```

## JavaScript
O Foundation requer jQuery. A inicialização padrão ativa todos os plugins:

```javascript
$(document).foundation();
```

## Diferenças vs Bootstrap
*   **Filosofia:** Foundation é mais um "esqueleto" para ser estilizado; Bootstrap vem com um estilo visual mais forte.
*   **Grid:** Foundation usa classes como `.cell` e `.grid-x`; Bootstrap usa `.col` e `.row`.
*   **Mobile-First:** Ambos são, mas Foundation tem uma abordagem agressiva de design responsivo.

## Referências
*   [Documentação (Sites)](https://get.foundation/sites/docs/)
*   [Building Blocks](https://get.foundation/building-blocks/)
