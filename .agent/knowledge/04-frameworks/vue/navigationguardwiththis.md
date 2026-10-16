---json
{
  "id": "navigationguardwiththis",
  "title": "接口：NavigationGuardWithThis\\<T\\> %{#interface-navigationguardwiththis-t}%",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：NavigationGuardWithThis\\<T\\> %{#interface-navigationguardwiththis-t}%.",
  "gatilhos": [
    "frameworks",
    "interface-navigationguardwiththis-t",
    "navigationguardwiththis",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：NavigationGuardWithThis\\<T\\> %{#interface-navigationguardwiththis-t}%?",
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

[API 参考](../index.md) / NavigationGuardWithThis

# 接口：NavigationGuardWithThis\<T\> %{#interface-navigationguardwiththis-t}%

导航守卫。详情可查阅[导航守卫](/zh/guide/advanced/navigation-guards.md)。

## 类型参数 %{#Type-parameters}%

| Name |
| :------ |
| `T` |

## 可调用函数 %{#Callable}%

### NavigationGuardWithThis %{#Callable-NavigationGuardWithThis}%

▸ **NavigationGuardWithThis**(`this`, `to`, `from`, `next`): `NavigationGuardReturn` \| `Promise`\<`NavigationGuardReturn`\>

#### 参数 %{#Callable-NavigationGuardWithThis-Parameters}%

| 名称 | 类型 |
| :------ | :------ |
| `this` | `T` |
| `to` | [`RouteLocationNormalized`](RouteLocationNormalized.md) |
| `from` | [`RouteLocationNormalized`](RouteLocationNormalized.md) |
| `next` | [`NavigationGuardNext`](NavigationGuardNext.md) |

#### 返回值 %{#Callable-NavigationGuardWithThis-Returns}%

`NavigationGuardReturn` \| `Promise`\<`NavigationGuardReturn`\>
