---json
{
  "id": "vscode-snippets_1",
  "title": "VS Code 代码片段",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre VS Code 代码片段.",
  "gatilhos": [
    "code",
    "frameworks",
    "snippets",
    "vscode",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar VS Code 代码片段?",
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

# VS Code 代码片段

<RuleKitLink />

有一些代码片段可以让你在 VS Code 中更轻松地使用 Pinia。

通过 <kbd>⇧</kbd> <kbd>⌘</kbd> <kbd>P</kbd> / <kbd>⇧</kbd> <kbd>⌃</kbd> <kbd>P</kbd> 然后输入 `Snippets: Configure User Snippets` 就可以管理用户代码片段。

```json
{
  "Pinia Options Store Boilerplate": {
    "scope": "javascript,typescript",
    "prefix": "pinia-options",
    "body": [
      "import { defineStore, acceptHMRUpdate } from 'pinia'",
      "",
      "export const use${TM_FILENAME_BASE/^(.*)$/${1:/pascalcase}/}Store = defineStore('$TM_FILENAME_BASE', {",
      " state: () => ({",
      "   $0",
      " }),",
      " getters: {},",
      " actions: {},",
      "})",
      "",
      "if (import.meta.hot) {",
      " import.meta.hot.accept(acceptHMRUpdate(use${TM_FILENAME_BASE/^(.*)$/${1:/pascalcase}/}Store, import.meta.hot))",
      "}",
      ""
    ],
    "description": "Bootstrap the code needed for a Vue.js Pinia Options Store file"
  },
  "Pinia Setup Store Boilerplate": {
    "scope": "javascript,typescript",
    "prefix": "pinia-setup",
    "body": [
      "import { defineStore, acceptHMRUpdate } from 'pinia'",
      "",
      "export const use${TM_FILENAME_BASE/^(.*)$/${1:/pascalcase}/}Store = defineStore('$TM_FILENAME_BASE', () => {",
      " $0",
      " return {}",
      "})",
      "",
      "if (import.meta.hot) {",
      " import.meta.hot.accept(acceptHMRUpdate(use${TM_FILENAME_BASE/^(.*)$/${1:/pascalcase}/}Store, import.meta.hot))",
      "}",
      ""
    ],
    "description": "Bootstrap the code needed for a Vue.js Pinia Setup Store file"
  }
}
```
