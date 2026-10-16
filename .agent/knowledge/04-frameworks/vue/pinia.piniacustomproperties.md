---json
{
  "id": "pinia-piniacustomproperties",
  "title": "接口：PiniaCustomProperties<Id, S, G, A\\> %{#interface-piniacustomproperties-id-s-g-a}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：PiniaCustomProperties<Id, S, G, A\\> %{#interface-piniacustomproperties-id-s-g-a}%.",
  "gatilhos": [
    "frameworks",
    "interface-piniacustomproperties-id-s-g-a",
    "pinia.piniacustomproperties",
    "piniacustomproperties",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：PiniaCustomProperties<Id, S, G, A\\> %{#interface-piniacustomproperties-id-s-g-a}%?",
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

[API 文档](../index.md) / [pinia](../modules/pinia.md) / PiniaCustomProperties

# 接口：PiniaCustomProperties<Id, S, G, A\> %{#interface-piniacustomproperties-id-s-g-a}%

[pinia](../modules/pinia.md).PiniaCustomProperties

当用户通过插件添加属性时，接口可被扩展。

## 类型参数 %{#type-parameters}%

| 名称 | 类型                                                                                                |
| :--- | :-------------------------------------------------------------------------------------------------- |
| `Id` | extends `string` = `string`                                                                         |
| `S`  | extends [`StateTree`](../modules/pinia.md#statetree) = [`StateTree`](../modules/pinia.md#statetree) |
| `G`  | [`_GettersTree`](../modules/pinia.md#_getterstree)<`S`\>                                            |
| `A`  | [`_ActionsTree`](../modules/pinia.md#_actionstree)                                                  |

## Accessors %{#accessors}%

### route %{#route}%

• `get` **route**(): `RouteLocationNormalized`

#### 返回值

`RouteLocationNormalized`

• `set` **route**(`value`): `void`

#### 参数

| Name    | Type                                                                       |
| :------ | :------------------------------------------------------------------------- |
| `value` | `RouteLocationNormalizedLoaded` \| `Ref`<`RouteLocationNormalizedLoaded`\> |

#### 返回值

`void`
