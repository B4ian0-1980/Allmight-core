---json
{
  "id": "layout_interface_perfis",
  "title": "🎨 Layout e Interface por Perfil - Template Base",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "**ℹ️ NOTA:** Este documento é um **TEMPLATE**. Adapte os perfis e layouts para a realidade do seu sistema específico.",
  "gatilhos": [
    "arquitetura",
    "base",
    "gestao",
    "interface",
    "layout",
    "perfil",
    "perfis",
    "por"
  ],
  "perguntas_tipo": [
    "Como utilizar 🎨 Layout e Interface por Perfil - Template Base?",
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

# 🎨 Layout e Interface por Perfil - Template Base

**Data:** [DATA_ATUAL]
**Versão:** 1.0
**Status:** Template de Especificação de UI/UX
**Contexto:** Base Estrutura - Exemplo Genérico

> **ℹ️ NOTA:** Este documento é um **TEMPLATE**. Adapte os perfis e layouts para a realidade do seu sistema específico.

---

## 📋 Índice

1. [Estrutura Geral da Interface](#estrutura-geral-da-interface)
2. [Layout por Perfil (Exemplos)](#layout-por-perfil-exemplos)
   - [Admin (Acesso Total)](#1-admin-acesso-total)
   - [Gestor (Visão Tática)](#2-gestor-visão-tática)
   - [Operador (Execução)](#3-operador-execução)
   - [Atendimento (Front Desk)](#4-atendimento-front-desk)
3. [Componentes Visuais Comuns](#componentes-visuais-comuns)

---

## 🏗️ Estrutura Geral da Interface

### Layout Base (Dashboard App)

Layout padrão com Sidebar lateral e Header superior.

```
┌─────────────────────────────────────────────────────────────────┐
│ 🚀 NOME DO SISTEMA                 [🔔 3] [👤 User] [⚙️] [🚪] │ ← Header
├──────────┬──────────────────────────────────────────────────────┤
│          │                                                      │
│  📊      │                                                      │
│ Dash     │                                                      │
│          │                                                      │
│  📂      │                    CONTEÚDO                         │
│ Módulo A │                    PRINCIPAL                         │
│          │                    (Router Outlet)                   │
│  📝      │                                                      │
│ Módulo B │                                                      │
│          │                                                      │
│  👥      │                                                      │
│ Usuários │                                                      │
│          │                                                      │
│  ⚙️      │                                                      │
│ Config   │                                                      │
│          │                                                      │
└──────────┴──────────────────────────────────────────────────────┘
   ↑              ↑
Sidebar      Área de Trabalho
```

### Componentes do Header
- **Logo:** Identidade do sistema/cliente.
- **Global Actions:** Busca global, Notificações.
- **User Menu:** Perfil, Configurações, Logout.

---

## 👥 Layout por Perfil (Exemplos)

### 1. ADMIN (Acesso Total)

**Foco:** Configuração, Manutenção, Auditoria e Visão Macro.

#### Dashboard Admin
```
┌─────────────────────────────────────────────────────────────────┐
│ 🚀 Admin Dashboard                 [🔔 5] [👤 Admin] [⚙️] [🚪]  │
├──────────┬──────────────────────────────────────────────────────┤
│          │  📊 VISÃO GERAL DO SISTEMA                           │
│  📊      │  ┌──────────────────────────────────────────────┐  │
│ Dash     │  │ 📈 Métricas de Uso (KPIs)                    │  │
│          │  │ [Gráfico de Acessos / Performance]           │  │
│  👥      │  └──────────────────────────────────────────────┘  │
│ Usuários │                                                      │
│          │  ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  🛡️      │  │ ✅ Ativos│ │ ⚠️ Alertas│ │ 🔴 Erros │            │
│ Seguranç │  │   150    │ │    12    │ │    03    │            │
│          │  └──────────┘ └──────────┘ └──────────┘            │
│  ⚙️      │                                                      │
│ Config   │  ┌──────────────────────────────────────────────┐  │
│          │  │ 👥 GESTÃO DE ACESSOS                         │  │
│  📜      │  │ • 5 novos usuários aguardando aprovação      │  │
│ Logs     │  │ [Gerenciar Usuários]                         │  │
│          │  └──────────────────────────────────────────────┘  │
└──────────┴──────────────────────────────────────────────────────┘
```

---

### 2. GESTOR (Visão Tática)

**Foco:** Relatórios, Aprovações, Monitoramento de Equipe.

#### Dashboard Gestor
```
┌─────────────────────────────────────────────────────────────────┐
│ 🚀 Gestão                        [🔔 3] [👤 Gestor] [⚙️] [🚪]   │
├──────────┬──────────────────────────────────────────────────────┤
│          │  📊 DASHBOARD TÁTICO                                 │
│  📊      │  ┌──────────────────────────────────────────────┐  │
│ Dash     │  │ 🎯 Metas do Mês                               │  │
│          │  │ [Progress Bar: 78% Concluído]                │  │
│  📋      │  └──────────────────────────────────────────────┘  │
│ Tarefas  │                                                      │
│          │  ┌──────────────────────────────────────────────┐  │
│  👥      │  │ 📋 PENDÊNCIAS DE APROVAÇÃO (3)               │  │
│ Equipe   │  │ • Solicitação #123 - Urgente                 │  │
│          │  │ • Relatório #456 - Revisão                   │  │
│  📈      │  └──────────────────────────────────────────────┘  │
│ Relatóri │                                                      │
└──────────┴──────────────────────────────────────────────────────┘
```

---

### 3. OPERADOR / ESPECIALISTA (Execução)

**Foco:** Fila de Trabalho, Execução de Tarefas, Input de Dados.

#### Dashboard Operacional
```
┌─────────────────────────────────────────────────────────────────┐
│ 🚀 Operacional                     [🔔 1] [👤 User]  [⚙️] [🚪]  │
├──────────┬──────────────────────────────────────────────────────┤
│          │  🏭 ÁREA DE TRABALHO                                 │
│  🏠      │  ┌──────────────────────────────────────────────┐  │
│ Início   │  │ 📥 MINHA FILA DE TRABALHO (5 itens)          │  │
│          │  │ ┌──────────────────────────────────────────┐ │  │
│  📝      │  │ │ 🔴 Tarefa A - Prioridade Alta - 10min    │ │  │
│ Executar │  │ │ [Iniciar]                                │ │  │
│          │  │ └──────────────────────────────────────────┘ │  │
│  🕒      │  │ ┌──────────────────────────────────────────┐ │  │
│ Históric │  │ │ 🟡 Tarefa B - Prioridade Média - 2h      │ │  │
│          │  │ │ [Detalhes]                               │ │  │
│          │  │ └──────────────────────────────────────────┘ │  │
│          │  └──────────────────────────────────────────────┘  │
└──────────┴──────────────────────────────────────────────────────┘
```

#### Tela de Execução (Kanban/Lista)
```
┌─────────────────────────────────────────────────────────┐
│ 📋 FILA DE ATIVIDADES                                   │
├──────────┬──────────────┬──────────────┬────────────────┤
│ 📥       │ ⏳           │ ✅           │ 🚀             │
│ A Fazer  │ Em Andamento │ Revisão      │ Concluído      │
│──────────┼──────────────┼──────────────┼────────────────┤
│ Item 01  │ Item 04      │ Item 02      │ Item 00        │
│ Item 03  │              │              │                │
└──────────┴──────────────┴──────────────┴────────────────┘
```

---

### 4. ATENDIMENTO (Front Desk)

**Foco:** Cadastro Rápido, Busca, Triagem Inicial.

#### Tela de Entrada/Cadastro
```
┌─────────────────────────────────────────────────────────┐
│ ➕ NOVO REGISTRO / CADASTRO                             │
├─────────────────────────────────────────────────────────┤
│ 🔍 Buscar Existente                                     │
│    [CPF/CNPJ/ID ou Nome...] [Buscar]                    │
│                                                           │
│ OU                                                       │
│                                                           │
│ 📝 Novo Cadastro                                        │
│    Nome: [________________]                             │
│    Categoria: [🔴 A] [🟡 B] [🟢 C] (Botões Rápidos)     │
│                                                           │
│ [Salvar e Iniciar]                                      │
└─────────────────────────────────────────────────────────┘
```

---

## 🧩 Componentes Visuais Comuns

### Cards de Resumo (KPIs)
Usados em dashboards para métricas rápidas.
- **Ícone:** Representação visual.
- **Valor:** Número ou dado principal.
- **Label:** Descrição.
- **Delta:** Variação (ex: +5% vs mês anterior).

### Tabelas de Dados
Para listagens densas (Admin/Gestor).
- **Filtros:** Barra superior.
- **Paginação:** Rodapé.
- **Ações:** Coluna direita (Editar, Excluir).

### Listas de Cards
Para itens visuais (Operacional).
- **Status:** Cor de borda ou badge indicativo.
- **Ações Rápidas:** Botões diretos no card.
