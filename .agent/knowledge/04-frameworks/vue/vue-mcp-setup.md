---json
{
  "id": "vue-mcp-setup",
  "title": "Configuração MCP para Vue.js (`vite-plugin-vue-mcp`)",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre Configuração MCP para Vue.js (`vite-plugin-vue-mcp`).",
  "gatilhos": [
    "frameworks",
    "mcp",
    "para",
    "setup",
    "vite-plugin-vue-mcp",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar Configuração MCP para Vue.js (`vite-plugin-vue-mcp`)?",
    "Quais as boas praticas de vue?"
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
  "dono": "stack-vue",
  "prioridade": 2
}
---

# Configuração MCP para Vue.js (`vite-plugin-vue-mcp`)

Diferente de outros servidores que rodam isolados, para Vue.js utilizamos um plugin que roda junto com o seu servidor de desenvolvimento Vite.

## 📦 Instalação
No seu projeto Vue, instale a dependência:

```bash
pnpm install vite-plugin-vue-mcp -D
# ou
npm install vite-plugin-vue-mcp -D
```

## ⚙️ Configuração (`vite.config.ts`)

Edite seu arquivo de configuração do Vite para incluir o plugin:

```typescript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VueMcp } from 'vite-plugin-vue-mcp' // <--- Importe

export default defineConfig({
  plugins: [
    vue(),
    VueMcp() // <--- Adicione aos plugins
  ],
})
```

## 🚀 Como Funciona
1.  Rode seu projeto (`npm run dev`).
2.  O servidor MCP ficará disponível em `http://localhost:[porta]/__mcp/sse`.
3.  **Integração Automática:** Se você criar um arquivo `.cursor/mcp.json` na raiz do projeto, o plugin tentará atualizá-lo automaticamente com a URL correta.

## ✨ Funcionalidades
Este plugin permite que a IA:
*   📜 **get-component-tree:** Ver a árvore de componentes completa.
*   🔍 **get-component-state:** Ler o estado (data/props) de um componente.
*   ✏️ **edit-component-state:** Alterar o estado em tempo real.
*   🍍 **get-pinia-state:** Ler o estado global do Pinia.
*   🛣️ **get-router-info:** Ver rotas e navegação.

*Licença: MIT © Arlo*
