---json
{
  "id": "pinia-definesetupstoreoptions",
  "title": "接口：DefineSetupStoreOptions<Id, S, G, A\\> %{#interface-definesetupstoreoptions-id-s-g-a}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：DefineSetupStoreOptions<Id, S, G, A\\> %{#interface-definesetupstoreoptions-id-s-g-a}%.",
  "gatilhos": [
    "definesetupstoreoptions",
    "frameworks",
    "interface-definesetupstoreoptions-id-s-g-a",
    "pinia.definesetupstoreoptions",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：DefineSetupStoreOptions<Id, S, G, A\\> %{#interface-definesetupstoreoptions-id-s-g-a}%?",
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

[API 文档](../index.md) / [pinia](../modules/pinia.md) / DefineSetupStoreOptions

# 接口：DefineSetupStoreOptions<Id, S, G, A\> %{#interface-definesetupstoreoptions-id-s-g-a}%

[pinia](../modules/pinia.md).DefineSetupStoreOptions

`defineStore()` 的选项参数，用于设置 store。
可以通过插件 API 扩展来增强 store 的功能。

**`See`**

[DefineStoreOptionsBase](pinia.DefineStoreOptionsBase.md).

## 类型参数 %{#type-parameters}%

| 名称 | 类型                                                 |
| :--- | :--------------------------------------------------- |
| `Id` | extends `string`                                     |
| `S`  | extends [`StateTree`](../modules/pinia.md#statetree) |
| `G`  | `G`                                                  |
| `A`  | `A`                                                  |

## 层次结构 %{#hierarchy}%

- [`DefineStoreOptionsBase`](pinia.DefineStoreOptionsBase.md)<`S`, [`Store`](../modules/pinia.md#store)<`Id`, `S`, `G`, `A`\>\>

  ↳ **`DefineSetupStoreOptions`**

## 属性

### actions %{#actions}%

• `Optional` **actions**: `A`

提取的 action。由 useStore() 添加。不应该由用户在创建 store 时添加。
可以在插件中使用，以获得用 setup 函数定义的 store 中的 action 列表。
注意这个属性一定是会定义的。
