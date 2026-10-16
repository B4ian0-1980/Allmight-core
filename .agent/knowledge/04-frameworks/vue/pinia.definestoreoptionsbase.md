---json
{
  "id": "pinia-definestoreoptionsbase",
  "title": "接口：DefineStoreOptionsBase<S, Store\\> %{#interface-definestoreoptionsbase-s-store}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：DefineStoreOptionsBase<S, Store\\> %{#interface-definestoreoptionsbase-s-store}%.",
  "gatilhos": [
    "definestoreoptionsbase",
    "frameworks",
    "interface-definestoreoptionsbase-s-store",
    "pinia.definestoreoptionsbase",
    "store",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：DefineStoreOptionsBase<S, Store\\> %{#interface-definestoreoptionsbase-s-store}%?",
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
sidebar: 'auto'
editLinks: false
sidebarDepth: 3
---

[API 文档](../index.md) / [pinia](../modules/pinia.md) / DefineStoreOptionsBase

# 接口：DefineStoreOptionsBase<S, Store\> %{#interface-definestoreoptionsbase-s-store}%

[pinia](../modules/pinia.md).DefineStoreOptionsBase

传递给 `defineStore()` 的选项，在 option store 和 setup store 之间是通用的。
如果你想为这两种 store 添加自定义的选项，
请扩展这个接口。

## 类型参数 %{#type-parameters}%

| Name    | Type                                                 |
| :------ | :--------------------------------------------------- |
| `S`     | extends [`StateTree`](../modules/pinia.md#statetree) |
| `Store` | `Store`                                              |

## 层次结构 %{#hierarchy}%

- **`DefineStoreOptionsBase`**

  ↳ [`DefineStoreOptions`](pinia.DefineStoreOptions.md)

  ↳ [`DefineSetupStoreOptions`](pinia.DefineSetupStoreOptions.md)
