---json
{
  "id": "navigationguard",
  "title": "接口：NavigationGuard %{#interface-navigationguard}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：NavigationGuard %{#interface-navigationguard}%.",
  "gatilhos": [
    "frameworks",
    "interface-navigationguard",
    "navigationguard",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：NavigationGuard %{#interface-navigationguard}%?",
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

[API 参考](../index.md) / NavigationGuard

# 接口：NavigationGuard %{#interface-navigationguard}%

导航守卫。详情可查阅[导航守卫](/zh/guide/advanced/navigation-guards.md)。

## 可调用函数 %{#Callable}%

### NavigationGuard %{#Callable-NavigationGuard}%

▸ **NavigationGuard**(`to`, `from`, `next`): `NavigationGuardReturn` \| `Promise`\<`NavigationGuardReturn`\>

#### 参数 %{#Callable-NavigationGuard-Parameters}%

| 名称 | 类型 |
| :------ | :------ |
| `to` | [`RouteLocationNormalized`](RouteLocationNormalized.md) |
| `from` | [`RouteLocationNormalized`](RouteLocationNormalized.md) |
| `next` | [`NavigationGuardNext`](NavigationGuardNext.md) |

#### 返回值 %{#Callable-NavigationGuard-Returns}%

`NavigationGuardReturn` \| `Promise`\<`NavigationGuardReturn`\>
