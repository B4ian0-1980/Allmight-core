---json
{
  "id": "pinia-subscriptioncallbackmutationpatchobject",
  "title": "接口：SubscriptionCallbackMutationPatchObject<S\\> %{#interface-subscriptioncallbackmutationpatchobject-s}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：SubscriptionCallbackMutationPatchObject<S\\> %{#interface-subscriptioncallbackmutationpatchobject-s}%.",
  "gatilhos": [
    "frameworks",
    "interface-subscriptioncallbackmutationpatchobject-s",
    "pinia.subscriptioncallbackmutationpatchobject",
    "subscriptioncallbackmutationpatchobject",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：SubscriptionCallbackMutationPatchObject<S\\> %{#interface-subscriptioncallbackmutationpatchobject-s}%?",
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

[API 文档](../index.md) / [pinia](../modules/pinia.md) / SubscriptionCallbackMutationPatchObject

# 接口：SubscriptionCallbackMutationPatchObject<S\> %{#interface-subscriptioncallbackmutationpatchobject-s}%

[pinia](../modules/pinia.md).SubscriptionCallbackMutationPatchObject

当 `store.$patch()` 与一个对象一起被调用时，
传递给订阅回调的上下文。

## 类型参数 %{#type-parameters}%

| 名称 |
| :--- |
| `S`  |

## 层次结构 %{#hierarchy}%

- [`_SubscriptionCallbackMutationBase`](pinia._SubscriptionCallbackMutationBase.md)

  ↳ **`SubscriptionCallbackMutationPatchObject`**

## 属性

### 事件 %{#events}%

• **events**: `DebuggerEvent`[]

仅限 DEV， patch 调用的数组。

---

### payload %{#payload}%

• **payload**: [`_DeepPartial`](../modules/pinia.md#_deeppartial)<`S`\>

传递给 `store.$patch()` 的对象

---

### storeId %{#storeid}%

• **storeId**: `string`

执行 mutation 的 store 的 `id`

#### 继承于

[\_SubscriptionCallbackMutationBase](pinia._SubscriptionCallbackMutationBase.md).[storeId](pinia._SubscriptionCallbackMutationBase.md#storeid)

---

### 类型 %{#type}%

• **type**: [`patchObject`](../enums/pinia.MutationType.md#patchobject)

mutation 的类型

#### 重写 %{#overrides}%

[\_SubscriptionCallbackMutationBase](pinia._SubscriptionCallbackMutationBase.md).[type](pinia._SubscriptionCallbackMutationBase.md#type)
