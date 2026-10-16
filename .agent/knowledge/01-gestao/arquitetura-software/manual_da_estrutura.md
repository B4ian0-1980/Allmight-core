---json
{
  "id": "manual_da_estrutura",
  "title": "🗺️ Manual de Navegação e Uso da Estrutura",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "\"Analise meu código com base em `@[base-estrutura-projeto]`\"",
  "gatilhos": [
    "arquitetura",
    "estrutura",
    "gestao",
    "manual",
    "software",
    "uso"
  ],
  "perguntas_tipo": [
    "Como utilizar 🗺️ Manual de Navegação e Uso da Estrutura?",
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

# 🗺️ Manual de Navegação e Uso da Estrutura

**Bem-vindo ao Novo Ecossistema do Projeto!**
Este guia explica onde encontrar cada tipo de informação e como utilizar a estrutura para acelerar o desenvolvimento.

---

## 🏗️ Os 3 Pilares

A estrutura foi simplificada para 3 diretórios principais:

### 1. 📚 `biblioteca/` (Central de Conhecimento)

**"Onde eu aprendo como fazer?"**
Aqui fica todo o conhecimento externo, categorizado por domínio técnico.

* **`backend/`**: Django, Laravel, Python, Bancos de Dados, SQL.
* **`frontend/`**: React, Vue, Angular, HTML/CSS.
* **`devops/`**: Docker, AWS, Linux, Segurança.
* **`fundamentos/`**: Algoritmos, Arquitetura de Software, Metodologias Ágeis.
* **`ferramentas/`**: Ferramentas de IA, Scripts e Utilitários.
* **`receitas-codigo/`**: Snippets prontos ("receitas de bolo") para copiar e colar.

### 2. 📋 `docs/` (O Projeto Atual)

**"Quais são as regras deste sistema?"**
Aqui fica a documentação específica do software que estamos construindo.

* **`gestao/`**: Requisitos, Processos, Manuais (como este!).
* **`funcionalidades/`**: Regras de Negócio detalhadas (ex: "Como calcular imposto X").
* **`arquitetura/`**: Decisões técnicas do projeto (ex: "Por que escolhemos Django?").
* **`analises/`**: Relatórios de performance, auditorias e estudos de caso.

### 3. 🚀 `servers/` (O Código Fonte)

**"Onde está o código?"**
Aqui ficam as aplicações reais.

* Cada subpasta é um projeto ou módulo independente (ex: `ui-lab`, `api-core`, `app-cliente`).

---

## 🤖 Como Pedir Análise Automática

Se você quiser que uma IA (como eu!) verifique se o seu código está seguindo os padrões definidos nesta estrutura, use o seguinte comando/referência em sua solicitação:

> "Analise meu código com base em `@[base-estrutura-projeto]`"

**O que eu farei:**

1. **Verificarei a Stack:** Olharei em `biblioteca/` para ver quais tecnologias são "oficiais" (ex: Usar Django 4.x e não Flask, se for o padrão).
2. **Verificarei a Arquitetura:** Consultarei `docs/arquitetura` para ver se você está seguindo os padrões de pastas e camadas.
3. **Verificarei Regras:** Consultarei `docs/funcionalidades` para garantir que a lógica de negócio está correta.

---

## ⚡ Guia Rápido: "Onde eu salvo isso?"

| Se você tem... | Salve em... |
| :--- | :--- |
| Um PDF de um livro de Python | `biblioteca/backend/linguagens/python` |
| A documentação oficial do React | `biblioteca/frontend/react` |
| Um script `.ps1` para backup | `biblioteca/ferramentas/scripts` |
| O desenho do Banco de Dados do Projeto | `docs/arquitetura` |
| A regra de "Desconto para Cliente VIP" | `docs/funcionalidades` |
| O código Python do sistema | `servers/[nome-do-sistema]` |

---
**Mantenha a casa arrumada!** 🧹
Uma estrutura limpa é a base de um código escalável.
