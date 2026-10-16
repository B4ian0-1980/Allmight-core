---json
{
  "id": "routerscrollbehavior",
  "title": "接口：RouterScrollBehavior",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：RouterScrollBehavior.",
  "gatilhos": [
    "frameworks",
    "routerscrollbehavior",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：RouterScrollBehavior?",
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

[API 参考](../index.md) / RouterScrollBehavior

# 接口：RouterScrollBehavior

可以被传递给 `createRouter` 的 `scrollBehavior` 选项的类型。

## 可调用函数 %{#Callable}%

### RouterScrollBehavior %{#Callable-RouterScrollBehavior}%

▸ **RouterScrollBehavior**(`to`, `from`, `savedPosition`): `Awaitable`\<``false`` \| `void` \| `ScrollPosition`\>

#### 参数 %{#Callable-RouterScrollBehavior-Parameters}%

| 名称 | 类型 | 描述 |
| :------ | :------ | :------ |
| `to` | [`RouteLocationNormalized`](RouteLocationNormalized.md) | 我们要导航到的路由地址 |
| `from` | [`RouteLocationNormalizedLoaded`](RouteLocationNormalizedLoaded.md) | 我们要离开的路由地址 |
| `savedPosition` | ``null`` \| `_ScrollPositionNormalized` | 要保存的页面位置，如果不存在则是 `null` |

#### 返回值 %{#Callable-RouterScrollBehavior-Returns}%

`Awaitable`\<``false`` \| `void` \| `ScrollPosition`\>
