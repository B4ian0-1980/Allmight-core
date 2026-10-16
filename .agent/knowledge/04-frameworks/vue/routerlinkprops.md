---json
{
  "id": "routerlinkprops",
  "title": "接口：RouterLinkProps",
  "categoria": "04-frameworks",
  "subcategoria": "vue",
  "resumo": "Guia tecnico e referencias sobre 接口：RouterLinkProps.",
  "gatilhos": [
    "frameworks",
    "routerlinkprops",
    "vue"
  ],
  "perguntas_tipo": [
    "Como utilizar 接口：RouterLinkProps?",
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

[API 参考](../index.md) / RouterLinkProps

# 接口：RouterLinkProps

## 继承关系 %{#Hierarchy}%

- `RouterLinkOptions`

  ↳ **`RouterLinkProps`**

## 属性 %{#Properties}%

### activeClass %{#Properties-activeClass}%

• `可选` **activeClass**: `string`

链接在匹配当前路由时被应用到 class。

___

### ariaCurrentValue %{#Properties-ariaCurrentValue}%

• `可选` **ariaCurrentValue**: ``"location"`` \| ``"time"`` \| ``"page"`` \| ``"step"`` \| ``"date"`` \| ``"true"`` \| ``"false"``

链接在匹配当前路由时传入 `aria-current` attribute 的值。

**`Default Value`**

`'page'`

___

### custom %{#Properties-custom}%

• `可选` **custom**: `boolean`

RouterLink 是否应该将其内容包裹在一个 `a` 标签里。用于通过 `v-slot` 创建自定义 RouterLink。

___

### exactActiveClass %{#Properties-exactActiveClass}%

• `可选` **exactActiveClass**: `string`

链接在严格匹配当前路由时被应用到 class。

___

### replace %{#Properties-replace}%

• `可选` **replace**: `boolean`

调用 `router.replace` 以替换 `router.push`。

#### 继承自 %{#Properties-replace-Inherited-from}%

RouterLinkOptions.replace

___

### to %{#Properties-to}%

• **to**: [`RouteLocationRaw`](../index.md#Type-Aliases-RouteLocationRaw)

当点击该链接时应该进入的路由地址。

#### 继承自 %{#Properties-to-Inherited-from}%

RouterLinkOptions.to
