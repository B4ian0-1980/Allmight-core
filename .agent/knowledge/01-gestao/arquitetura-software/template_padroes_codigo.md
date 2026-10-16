---json
{
  "id": "template_padroes_codigo",
  "title": "📏 Template - Padrões de Código",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "**Dica:** Configure seu editor para rodar o linter ao salvar.",
  "gatilhos": [
    "arquitetura",
    "codigo",
    "gestao",
    "padroes",
    "software",
    "template"
  ],
  "perguntas_tipo": [
    "Como utilizar 📏 Template - Padrões de Código?",
    "Quais as boas praticas de arquitetura-software?"
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
  "dono": "stack-arquitetura-software",
  "prioridade": 2
}
---

# 📏 Template - Padrões de Código

**Projeto:** [NOME_DO_PROJETO]
**Linguagem:** [LINGUAGEM]

---

## 📝 Convenções de Nomenclatura

| Elemento | Padrão | Exemplo |
| :--- | :--- | :--- |
| **Variáveis** | camelCase | `userName`, `totalCount` |
| **Funções** | camelCase | `getUser()`, `calculateTotal()` |
| **Classes** | PascalCase | `UserController`, `OrderService` |
| **Constantes** | UPPER_SNAKE_CASE | `MAX_RETRIES`, `DEFAULT_TIMEOUT` |
| **Arquivos** | [snake_case / PascalCase] | `user_controller.ts` |

---

## 🎨 Formatação (Style Guide)

Utilizamos [Ferramenta de Linting] com as seguintes regras principais:
1. Indentação: [2/4] espaços.
2. Tamanho máximo de linha: [80/120] caracteres.
3. Aspas: [Simples/Duplas].
4. Ponto e vírgula: [Obrigatório/Opcional].

> **Dica:** Configure seu editor para rodar o linter ao salvar.

---

## 🏗️ Estrutura de Arquivos

### Controllers / Renderers
- Devem ser magros. Apenas recebem requisição e chamam Serviços.
- **Não** conter lógica de negócio complexa.

### Services / Logic
- Contêm a regra de negócio pura.
- Devem ser testáveis isoladamente.

---

## 🧪 Testes

- **Unitários:** Obrigatórios para lógica de negócio complexa.
- **Nomenclatura:** `test_nome_da_funcao_comportamento_esperado`.

---

## 🚫 Anti-Patterns (O que EVITAR)

1. **Magic Numbers:** Evite números soltos no código. Use constantes.
2. **God Classes:** Classes que fazem tudo. Quebre em responsabilidades menores.
3. **Deep Nesting:** Evite muitos `if/else` aninhados. Use Early Return.
