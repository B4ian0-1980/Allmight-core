---json
{
  "id": "routemeta",
  "title": "接口：RouteMeta",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：RouteMeta.",
  "gatilhos": [
    "frameworks",
    "routemeta",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：RouteMeta?",
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

[API 参考](../index.md) / RouteMeta

# 接口：RouteMeta

路由记录中的 `meta` 字段的类型接口。

**`Example`**

```ts
// typings.d.ts 或 router.ts
import 'vue-router';

declare module 'vue-router' {
  interface RouteMeta {
    requiresAuth?: boolean
  }
 }
```

## 继承关系 %{#Hierarchy}%

- `Record`\<`string` \| `number` \| `symbol`, `unknown`\>

  ↳ **`RouteMeta`**
