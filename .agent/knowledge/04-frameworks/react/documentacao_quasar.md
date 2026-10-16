---json
{
  "id": "documentacao_quasar",
  "title": "Documentação: Quasar Framework",
  "categoria": "04-frameworks",
  "subcategoria": "react",
  "resumo": "**Base:** Vue.js **Tipo:** Framework Universal (Web, Mobile, Desktop)",
  "gatilhos": [
    "documentacao",
    "framework",
    "frameworks",
    "quasar",
    "react"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Quasar Framework?",
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

# Documentação: Quasar Framework

> **Base:** Vue.js
> **Tipo:** Framework Universal (Web, Mobile, Desktop)
> **Site Oficial:** [quasar.dev](https://quasar.dev)

## O que é?
Quasar é um framework baseado em Vue.js que permite escrever código uma vez e implantá-lo simultaneamente como:
*   Website (SPA)
*   Server-side Rendered App (SSR)
*   Progressive Web App (PWA)
*   Mobile App (Android/iOS via Capacitor ou Cordova)
*   Desktop App (Electron)

## Diferencial: A Biblioteca de Componentes
O Quasar vem com uma biblioteca massiva de componentes Material Design de alta performance. Diferente de usar Vue + Biblioteca UI separada, o Quasar é integrado profundamente, oferecendo uma experiência de desenvolvimento superior.

## Instalação (Quasar CLI)

A ferramenta recomendada é o Quasar CLI com Vite.

```bash
npm init quasar
```

Responda aos prompts:
1.  **Project type:** App with Quasar CLI
2.  **Quasar version:** Quasar v2 (Vue 3)
3.  **Script type:** Javascript ou TypeScript
4.  **Vite Strategy:** Vite (Recomendado)

## Comandos Úteis

```bash
# Rodar em modo de desenvolvimento (SPA)
quasar dev

# Emular Android
quasar dev -m android

# Emular iOS
quasar dev -m ios

# Construir para produção
quasar build
```

## Componentes Vue (Q-Components)
Todos os componentes começam com `Q`.

```html
<template>
  <div class="q-pa-md">
    <q-btn color="primary" label="Primary" />
    <q-btn color="secondary" label="Secondary" />
    
    <q-input v-model="text" label="Digite algo" />
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      text: ref('')
    }
  }
}
</script>
```

## Sistema de Layout
O construtor de layout do Quasar (`QLayout`) é extremamente poderoso para criar interfaces complexas (Header, Footer, Drawers Laterais) de forma responsiva.

## Referências
*   [Documentação Oficial](https://quasar.dev/docs)
*   [Galeria de Componentes](https://quasar.dev/vue-components)
*   [Extensões de App](https://quasar.dev/app-extensions/discover)
