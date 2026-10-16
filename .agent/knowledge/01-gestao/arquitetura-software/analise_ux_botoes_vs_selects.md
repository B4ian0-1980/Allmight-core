---json
{
  "id": "analise_ux_botoes_vs_selects",
  "title": "🎯 Análise UX: Botões vs Seleções - Template",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🎯 Análise UX: Botões vs Seleções - Template.",
  "gatilhos": [
    "analise",
    "arquitetura",
    "botoes",
    "gestao",
    "selects",
    "software",
    "template"
  ],
  "perguntas_tipo": [
    "Como utilizar 🎯 Análise UX: Botões vs Seleções - Template?",
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

# 🎯 Análise UX: Botões vs Seleções - Template

**Data:** [DATA_ATUAL]
**Versão:** 1.0
**Status:** Template de Análise UX
**Contexto:** Base Estrutura - Decisão de Componentes

---

## 📋 Resumo Executivo

**Objetivo:**
Substituir **Selects/Dropdowns** por **Botões de Clique Direto** sempre que possível para melhorar a eficiência e clareza da interface.

**Por Que?**
- ⏱️ **Reduz tempo de interação** (de 2-3 cliques para 1 clique).
- 🎯 **Reduz erros** (todas as decisões visíveis imediatamente).
- 📱 **Melhora mobile-first** (touch targets maiores).

---

## 🎨 Princípios de Design

### ✅ QUANDO USAR BOTÕES

1. **Poucas Opções:** Idealmente entre 2 e 5 opções.
2. **Alta Frequência:** Ações repetitivas (ex: Mudar Status).
3. **Decisão Visual:** Cores ou ícones ajudam na decisão.
4. **Mutuamente Exclusivas:** Uma opção anula a outra (Radio).

### ❌ QUANDO MANTER SELECTS

1. **Muitas Opções:** Mais de 10 itens (ex: Lista de Países).
2. **Dados Dinâmicos:** Itens carregados via API (ex: Buscar Usuário).
3. **Hierarquia:** Selects encadeados (ex: Estado > Cidade).
4. **Espaço Limitado:** Tabelas densas ou formulários compactos.

---

## 🔍 Análise Comparativa (Exemplos)

### 1. Seleção de Status

**❌ ANTES (Select)**
```
Status: [▼ Selecione]  (2 Cliques + Scroll)
```

**✅ DEPOIS (Botões)**
```
Status: [🔴 Pendente] [🟡 Em Análise] [🟢 Aprovado]  (1 Clique)
```

**Ganho:** ~60% de redução no tempo de interação. Clareza visual imediata.

---

### 2. Filtros de Lista

**❌ ANTES (Select)**
```
Filtrar por: [▼ Todos]
```

**✅ DEPOIS (Botões Toggle)**
```
Filtros: [Abertos] [Fechados] [Arquivados] (Permite Múltiplos)
```

**Ganho:** Visibilidade do estado atual sem abrir menus.

---

### 3. Ordenação

**❌ ANTES (Select)**
```
Ordenar por: [▼ Data (Crescente)]
```

**✅ DEPOIS (Botões Icon)**
```
Ordenar: [Data ⬇] [Nome ⬇] [Valor ⬇]
```

**Ganho:** Acesso rápido às ordenações mais comuns.

---

## ⚡ Impacto Esperado

### Performance Humana
- **Tempo de Decisão:** Reduzido (Carga cognitiva menor).
- **Tempo de Ação:** Reduzido (Menos cliques/movimento de mouse).

### Métricas de Sucesso (KPIs)
1. **Redução de Cliques:** Meta de -50% em formulários chave.
2. **Taxa de Erro:** Redução esperada (feedback visual mais claro).
3. **Satisfação:** Aumento na percepção de velocidade do sistema.

---

## 🚀 Plano de Adoção Padrão

### Passo 1: Identificar Candidatos
- Mapear todos os `<select>` do sistema.
- Classificar por número de opções (2-5 = Candidato Alto).

### Passo 2: Protótipo e Teste
- Implementar `ButtonGroup` em uma funcionalidade piloto.
- Medir tempo de interação antes/depois.

### Passo 3: Rollout Progressivo
- Priorizar formulários de alta rotatividade.
- Manter Selects onde a densidade de informação for crítica.
