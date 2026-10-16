---json
{
  "id": "pinia_nuxt-moduleoptions",
  "title": "接口：ModuleOptions",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：ModuleOptions.",
  "gatilhos": [
    "frameworks",
    "moduleoptions",
    "nuxt.moduleoptions",
    "pinia",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：ModuleOptions?",
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

---
editLink: false
---

[API 文档](../index.md) / [@pinia/nuxt](../modules/pinia_nuxt.md) / ModuleOptions

# 接口：ModuleOptions

[@pinia/nuxt](../modules/pinia_nuxt.md).ModuleOptions

## 属性 %{#Properties}%

### autoImports %{#Properties-autoImports}%

• `Optional` **autoImports**: (`string` \| [`string`, `string`])[]

将被添加到 nuxt.config.js 文件的自动导入数组。

**`Example`**

```js
autoImports: [
 // automatically import `defineStore`
 'defineStore',
 // automatically import `defineStore` as `definePiniaStore`
 ['defineStore', 'definePiniaStore',
]
```

---

### disableVuex %{#Properties-disableVuex}%

• `Optional` **disableVuex**: `boolean`

默认情况下，Pinia 会禁用 Vuex，将此选项设置为 `false` 可启用 Vuex，然后便可同时使用 Pinia 和 Vuex（仅在 Nuxt 2 中支持）。

**`Default`**

`true`
