---json
{
  "id": "deployurl-basehref",
  "title": "Deployurl Basehref",
  "categoria": "04-frameworks",
  "subcategoria": "angular",
  "resumo": "Guia tecnico e referencias sobre Deployurl Basehref.",
  "gatilhos": [
    "angular",
    "basehref",
    "deployurl",
    "frameworks"
  ],
  "perguntas_tipo": [
    "Como utilizar Deployurl Basehref?",
    "Quais as boas praticas de angular?"
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
  "dono": "stack-angular",
  "prioridade": 2
}
---

|                                             | Deploy URL | Base HREF |
| ------------------------------------------- | :--------: | :-------: |
| Initial scripts (index.html)                |   ✅ 👍    |   ✅ 👍   |
| Initial stylesheets (index.html)            |   ✅ 👍    |   ✅ 👍   |
| Lazy scripts (routes/import()/etc.)         |   ✅ 👍    |   ✅ 👍   |
| Processed CSS resources (images/fonts/etc.) |   ✅ 👍    |   ✅ 👍   |
| Relative template (HTML) assets             |   ❌ 👎    |   ✅ 👍   |
| Angular Router Default Base (APP_BASE_HREF) |     ❌     |  ✅ \*1   |
| Single reference in deployed Application    |   ❌ 👎    |   ✅ 👍   |
| Special resource logic within CLI           |   ✅ 👎    |   ❌ 👍   |
| Relative fetch/XMLHttpRequest               |     ❌     |    ✅     |

✅ - has/affects the item/trait
❌ - does not have/affect the item/trait
👍 - favorable behavior
👎 - unfavorable behavior

\*1 -- Users with more complicated setups may need to manually configure the `APP_BASE_HREF` token within the application. (e.g., application routing base is `/` but assets/scripts/etc. are at `/assets/`)
