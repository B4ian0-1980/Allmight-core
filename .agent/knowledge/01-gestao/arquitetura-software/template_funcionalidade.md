---json
{
  "id": "template_funcionalidade",
  "title": "🧩 Template - Especificação de Funcionalidade",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🧩 Template - Especificação de Funcionalidade.",
  "gatilhos": [
    "arquitetura",
    "funcionalidade",
    "gestao",
    "software",
    "template"
  ],
  "perguntas_tipo": [
    "Como utilizar 🧩 Template - Especificação de Funcionalidade?",
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

# 🧩 Template - Especificação de Funcionalidade

**Nome da Funcionalidade:** [Nome]
**Módulo:** [Ex: Financeiro, Estoque]
**Data:** [Data]

---

## 🎯 Objetivo
[Descreva o que esta funcionalidade faz e qual problema ela resolve em 1-2 frases.]

---

## 👤 Atores
- **Ator 1:** [Ex: Administrador] - [O que ele faz?]
- **Ator 2:** [Ex: Cliente] - [O que ele faz?]

---

## 📋 Requisitos Funcionais

| ID | Descrição | Critério de Aceite |
| :--- | :--- | :--- |
| **RF-01** | O sistema deve permitir... | O usuário consegue... |
| **RF-02** | O sistema deve validar... | O sistema exibe erro se... |
| **RF-03** | O sistema deve calcular... | O valor final é... |

---

## 🔄 Fluxo de Trabalho (Happy Path)

1. Usuário acessa a tela X.
2. Sistema exibe lista de Y.
3. Usuário clica em "Novo".
4. Usuário preenche formulário.
5. Sistema valida e salva.

---

## 🚫 Casos de Exceção (Sad Path)

- **E1:** Se o formulário estiver incompleto -> Exibir mensagens de erro.
- **E2:** Se a conexão falhar -> Exibir alerta de re tentativa.

---

## 💾 Modelo de Dados (Alterações)

Listar novas tabelas ou campos necessários.

```sql
-- Exemplo
TABLE pedidos (
  id INT PK,
  status VARCHAR(20)
);
```

---

## 📝 Regras de Negócio Específicas

1. **Regra A:** [Descrição]
2. **Regra B:** [Descrição]
