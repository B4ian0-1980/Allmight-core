---json
{
  "id": "navigationhookafter",
  "title": "接口：NavigationHookAfter %{#interface-navigationhookafter}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：NavigationHookAfter %{#interface-navigationhookafter}%.",
  "gatilhos": [
    "frameworks",
    "interface-navigationhookafter",
    "navigationhookafter",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：NavigationHookAfter %{#interface-navigationhookafter}%?",
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

[API 参考](../index.md) / NavigationHookAfter

# 接口：NavigationHookAfter %{#interface-navigationhookafter}%

## 可调用函数 %{#Callable}%

### NavigationHookAfter %{#Callable-NavigationHookAfter}%

▸ **NavigationHookAfter**(`to`, `from`, `failure?`): `any`

#### 参数 %{#Callable-NavigationHookAfter-Parameters}%

| 名称 | 类型 |
| :------ | :------ |
| `to` | [`RouteLocationNormalized`](RouteLocationNormalized.md) |
| `from` | [`RouteLocationNormalized`](RouteLocationNormalized.md) |
| `failure?` | `void` \| [`NavigationFailure`](NavigationFailure.md) |

#### 返回值 %{#Callable-NavigationHookAfter-Returns}%

`any`
