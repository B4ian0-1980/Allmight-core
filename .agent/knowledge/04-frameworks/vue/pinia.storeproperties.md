---json
{
  "id": "pinia-storeproperties",
  "title": "接口：StoreProperties<Id\\> %{#interface-storeproperties-id}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：StoreProperties<Id\\> %{#interface-storeproperties-id}%.",
  "gatilhos": [
    "frameworks",
    "interface-storeproperties-id",
    "pinia.storeproperties",
    "storeproperties",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：StoreProperties<Id\\> %{#interface-storeproperties-id}%?",
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

[API 文档](../index.md) / [pinia](../modules/pinia.md) / StoreProperties

# 接口：StoreProperties<Id\> %{#interface-storeproperties-id}%

[pinia](../modules/pinia.md).StoreProperties

store 的属性。

## 类型参数 %{#type-parameters}%

| 名称 | 类型             |
| :--- | :--------------- |
| `Id` | extends `string` |

## 层次结构 %{#hierarchy}%

- **`StoreProperties`**

  ↳ [`_StoreWithState`](pinia._StoreWithState.md)

## 属性

### $id %{#id}%

• **$id**: `Id`

store 的唯一标识符

---

### \_customProperties %{#customproperties}%

• **\_customProperties**: `Set`<`string`\>

供 devtools 插件使用，用于检索插件添加的属性。
在生产环境中会被移除。
开发者可用于添加应在 devtools 中显示的 store 的属性键。
