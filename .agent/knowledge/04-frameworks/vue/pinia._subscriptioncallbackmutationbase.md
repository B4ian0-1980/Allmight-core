---json
{
  "id": "pinia-_subscriptioncallbackmutationbase",
  "title": "接口：\\_SubscriptionCallbackMutationBase %{#interface-subscriptioncallbackmutationbase}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：\\_SubscriptionCallbackMutationBase %{#interface-subscriptioncallbackmutationbase}%.",
  "gatilhos": [
    "_subscriptioncallbackmutationbase",
    "frameworks",
    "interface-subscriptioncallbackmutationbase",
    "pinia.",
    "subscriptioncallbackmutationbase",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：\\_SubscriptionCallbackMutationBase %{#interface-subscriptioncallbackmutationbase}%?",
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

[API 文档](../index.md) / [pinia](../modules/pinia.md) / \_SubscriptionCallbackMutationBase

# 接口：\_SubscriptionCallbackMutationBase %{#interface-subscriptioncallbackmutationbase}%

[pinia](../modules/pinia.md).\_SubscriptionCallbackMutationBase

传递给订阅回调的上下文的基本类型。内部类型。

## 层次结构 %{#hierarchy}%

- **`_SubscriptionCallbackMutationBase`**

  ↳ [`SubscriptionCallbackMutationDirect`](pinia.SubscriptionCallbackMutationDirect.md)

  ↳ [`SubscriptionCallbackMutationPatchFunction`](pinia.SubscriptionCallbackMutationPatchFunction.md)

  ↳ [`SubscriptionCallbackMutationPatchObject`](pinia.SubscriptionCallbackMutationPatchObject.md)

## 属性

### storeId %{#storeid}%

• **storeId**: `string`

执行 mutation 的 store 的`id`。

---

### 类型 %{#type}%

• **type**: [`MutationType`](../enums/pinia.MutationType.md)

mutation 的类型
