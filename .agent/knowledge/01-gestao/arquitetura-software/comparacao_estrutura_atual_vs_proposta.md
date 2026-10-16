---json
{
  "id": "comparacao_estrutura_atual_vs_proposta",
  "title": "📊 Comparação: Estrutura Atual vs Proposta",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 📊 Comparação: Estrutura Atual vs Proposta.",
  "gatilhos": [
    "arquitetura",
    "atual",
    "comparacao",
    "estrutura",
    "gestao",
    "proposta",
    "software"
  ],
  "perguntas_tipo": [
    "Como utilizar 📊 Comparação: Estrutura Atual vs Proposta?",
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

# 📊 Comparação: Estrutura Atual vs Proposta

**Data:** 2025-01-27  
**Status:** Visualização Comparativa

---

## 🔴 ESTRUTURA ATUAL (Desorganizada)

```
same/
├── docs/                              # 40+ arquivos misturados
│   ├── README.md
│   ├── LEVANTAMENTO_PROJETO.md
│   ├── REQUISITOS_NEGOCIO_FUNCIONAIS.md
│   ├── ARQUITETURA_ESTRUTURA_LARAVEL12.md
│   ├── PADROES_CODIGO_LARAVEL.md
│   ├── DESIGN_SYSTEM_COMPLETO.md
│   ├── LAYOUT_INTERFACE_PERFIS.md
│   ├── EVOLUCAO_ANALISE_UX_SDLC.md
│   ├── DADOS_ACOLHIMENTO_PACIENTE.md
│   ├── ANALISE_AGREGACAO_QI.md
│   ├── INERTIA2_LARAVEL_REACT.md
│   └── ... (mais 30+ arquivos sem organização)
│
├── Laravel 12/                        # Nome com espaço (problema)
│   ├── docs-12.x/
│   ├── framework-12.x/
│   └── laravel-12.x.md
│
├── qi/                                # Nome não descritivo
│   ├── PHP e Laravel Crie aplicações web como um verdadeiro artesão.md
│   ├── Professional-React-v19.3.0-labs.md
│   └── ... (14 arquivos misturados)
│
├── Reactjs - main/                    # Nome com espaço e hífen
│   └── Professional-React-v19.3.0-labs.md
│
├── extras/                            # OK
└── converter/                         # OK
```

**Problemas:**
- ❌ 40+ arquivos na raiz de `docs/` sem organização
- ❌ Nomes de pastas com espaços (problemas em scripts)
- ❌ Nomes não descritivos (`qi`)
- ❌ Documentação, referências e livros misturados
- ❌ Difícil encontrar arquivos específicos
- ❌ Sem lógica de agrupamento

---

## 🟢 ESTRUTURA PROPOSTA (Organizada)

```
same/
├── 📚 docs/                           # Documentação do projeto
│   ├── 📋 00-base/                    # 6 arquivos fundamentais
│   │   ├── README.md
│   │   ├── LEVANTAMENTO_PROJETO.md
│   │   ├── REQUISITOS_NEGOCIO_FUNCIONAIS.md
│   │   ├── DOCUMENTACAO_SDLC_COMPLETA.md
│   │   ├── DIRETRIZES_DESENVOLVIMENTO.md
│   │   └── AMBIENTE_DESENVOLVIMENTO.md
│   │
│   ├── 🏗️ 01-arquitetura/             # 6 arquivos de arquitetura
│   │   ├── ARQUITETURA_ESTRUTURA_LARAVEL12.md
│   │   ├── PADROES_CODIGO_LARAVEL.md
│   │   ├── LARAVEL_BEST_PRACTICES.md
│   │   ├── PADROES_REACT19.md
│   │   ├── EXEMPLOS_PRATICOS_LARAVEL.md
│   │   └── GUIA_MELHORIA_QUALIDADE_CODIGO.md
│   │
│   ├── 🎨 02-ui-ux/                   # 6 arquivos de UI/UX
│   │   ├── DESIGN_SYSTEM_COMPLETO.md
│   │   ├── LAYOUT_INTERFACE_PERFIS.md
│   │   ├── ANALISE_UX_BOTOES_VS_SELECTS.md
│   │   ├── REQUISITOS_UX_DETALHADOS.md
│   │   ├── IMPLEMENTACAO_COMPONENTES_UX.md
│   │   └── STORYBOOK_CONFIGURACAO_IA.md
│   │
│   ├── 🔄 03-sdlc/                    # 5 arquivos de SDLC
│   │   ├── EVOLUCAO_ANALISE_UX_SDLC.md
│   │   ├── RESUMO_EXECUTIVO_UX_COMPONENTES.md
│   │   ├── ESTRATEGIA_TESTES_UX.md
│   │   ├── ESTRATEGIA_DEPLOY_UX.md
│   │   └── PLANO_MANUTENCAO_UX.md
│   │
│   ├── ⚙️ 04-funcionalidades/         # 7 arquivos de funcionalidades
│   │   ├── DADOS_ACOLHIMENTO_PACIENTE.md
│   │   ├── SISTEMA_PERMISSOES_SESAU_AVANCADO.md
│   │   ├── IMPLEMENTACAO_PERMISSOES_TRIAGEM.md
│   │   ├── ALTERACOES_TRIAGEM_LARANJA.md
│   │   ├── GESTAO_PACIENTES_HISTORICO.md
│   │   ├── GESTAO_EVENTOS_EQUIPES.md
│   │   └── INTEGRACAO_MEDICAMENTOS_ESTOQUE.md
│   │
│   ├── 🔍 05-analises/                # 8 arquivos de análises
│   │   ├── ANALISE_AGREGACAO_QI.md
│   │   ├── ANALISE_EXTRAS_AI_TOOLS.md
│   │   ├── ANALISE_COMPLETA_REPOSITORIO_REACT.md
│   │   ├── ANALISE_FRAMEWORKS_OFFLINE.md
│   │   ├── ANALISE_DOCUMENTACAO.md
│   │   ├── APROVEITAMENTO_CURSO_REACT19.md
│   │   ├── APROVEITAMENTO_DOCUMENTACAO_LARAVEL12.md
│   │   └── CLASSIFICACAO_DOCUMENTOS.md
│   │
│   └── 📖 06-referencias-tecnicas/    # 3 arquivos de referências
│       ├── INERTIA2_LARAVEL_REACT.md
│       ├── REACT19_BIBLIOTECA_FRONTEND.md
│       └── INDICE_DOCUMENTACAO.md
│
├── 📚 referencia/                     # Referências técnicas (renomeado)
│   └── laravel-12/                    # Sem espaços no nome
│       ├── docs-12.x/
│       ├── framework-12.x/
│       ├── laravel-12.x.md
│       └── Laravel melhores práticas README.md
│
├── 📚 livros/                         # Livros organizados por tema
│   ├── laravel/
│   │   └── PHP e Laravel Crie aplicações web como um verdadeiro artesão.md
│   ├── react/
│   │   ├── Professional-React-v19.3.0-labs.md
│   │   ├── react-guia-do-iniciate.md
│   │   └── The Road to learn React - Português (Robin Wieruch).md
│   ├── banco-dados/
│   │   ├── PostgreSQL Banco de dados para aplicações web modernas.md
│   │   └── Armazenando dados com Redis.md
│   └── outros/
│       ├── Big Data Técnicas e tecnologias para extração de valor dos dados.md
│       ├── Business Intelligence Implementar do jeito certo e a custo zero.md
│       ├── Elasticsearch Consumindo dados real-time com ELK.md
│       ├── kubernetes-management-for-dummies-ebook.md
│       ├── livro-bootstrap.md
│       ├── livro-vue.md
│       ├── PHP, MySQL, JavaScript &HTML5 All-in-One For Dummies.md
│       └── Backtrack Linux.md
│
├── 🛠️ extras/                         # Mantém (OK)
└── 🔧 converter/                      # Mantém (OK)
```

**Vantagens:**
- ✅ Organização clara por função
- ✅ Prefixos numéricos facilitam ordem
- ✅ Nomes sem espaços (compatível com scripts)
- ✅ Separação: docs vs referências vs livros
- ✅ Fácil encontrar arquivos
- ✅ Estrutura escalável

---

## 📊 Estatísticas

### Estrutura Atual
- **Total de arquivos em `docs/`:** 40+
- **Pastas na raiz:** 6
- **Nomes com espaços:** 2 (`Laravel 12`, `Reactjs - main`)
- **Nomes não descritivos:** 1 (`qi`)

### Estrutura Proposta
- **Total de arquivos em `docs/`:** 40+ (organizados em 7 subpastas)
- **Pastas na raiz:** 4 (docs, referencia, livros, extras, converter)
- **Nomes com espaços:** 0
- **Nomes descritivos:** 100%

---

## 🎯 Mapeamento de Arquivos

### 📋 00-base/ (6 arquivos)
```
LEVANTAMENTO_PROJETO.md                    → docs/00-base/
REQUISITOS_NEGOCIO_FUNCIONAIS.md           → docs/00-base/
DOCUMENTACAO_SDLC_COMPLETA.md              → docs/00-base/
DIRETRIZES_DESENVOLVIMENTO.md               → docs/00-base/
AMBIENTE_DESENVOLVIMENTO.md                 → docs/00-base/
README.md                                   → docs/00-base/ (mantém também na raiz)
```

### 🏗️ 01-arquitetura/ (6 arquivos)
```
ARQUITETURA_ESTRUTURA_LARAVEL12.md          → docs/01-arquitetura/
PADROES_CODIGO_LARAVEL.md                  → docs/01-arquitetura/
LARAVEL_BEST_PRACTICES.md                  → docs/01-arquitetura/
PADROES_REACT19.md                         → docs/01-arquitetura/
EXEMPLOS_PRATICOS_LARAVEL.md               → docs/01-arquitetura/
GUIA_MELHORIA_QUALIDADE_CODIGO.md          → docs/01-arquitetura/
```

### 🎨 02-ui-ux/ (6 arquivos)
```
DESIGN_SYSTEM_COMPLETO.md                  → docs/02-ui-ux/
LAYOUT_INTERFACE_PERFIS.md                 → docs/02-ui-ux/
ANALISE_UX_BOTOES_VS_SELECTS.md            → docs/02-ui-ux/
REQUISITOS_UX_DETALHADOS.md                → docs/02-ui-ux/
IMPLEMENTACAO_COMPONENTES_UX.md            → docs/02-ui-ux/
STORYBOOK_CONFIGURACAO_IA.md              → docs/02-ui-ux/
```

### 🔄 03-sdlc/ (5 arquivos)
```
EVOLUCAO_ANALISE_UX_SDLC.md                → docs/03-sdlc/
RESUMO_EXECUTIVO_UX_COMPONENTES.md          → docs/03-sdlc/
ESTRATEGIA_TESTES_UX.md                    → docs/03-sdlc/
ESTRATEGIA_DEPLOY_UX.md                    → docs/03-sdlc/
PLANO_MANUTENCAO_UX.md                     → docs/03-sdlc/
```

### ⚙️ 04-funcionalidades/ (7 arquivos)
```
DADOS_ACOLHIMENTO_PACIENTE.md               → docs/04-funcionalidades/
SISTEMA_PERMISSOES_SESAU_AVANCADO.md        → docs/04-funcionalidades/
IMPLEMENTACAO_PERMISSOES_TRIAGEM.md         → docs/04-funcionalidades/
ALTERACOES_TRIAGEM_LARANJA.md               → docs/04-funcionalidades/
GESTAO_PACIENTES_HISTORICO.md               → docs/04-funcionalidades/
GESTAO_EVENTOS_EQUIPES.md                   → docs/04-funcionalidades/
INTEGRACAO_MEDICAMENTOS_ESTOQUE.md          → docs/04-funcionalidades/
```

### 🔍 05-analises/ (8 arquivos)
```
ANALISE_AGREGACAO_QI.md                    → docs/05-analises/
ANALISE_EXTRAS_AI_TOOLS.md                 → docs/05-analises/
ANALISE_COMPLETA_REPOSITORIO_REACT.md       → docs/05-analises/
ANALISE_FRAMEWORKS_OFFLINE.md              → docs/05-analises/
ANALISE_DOCUMENTACAO.md                    → docs/05-analises/
APROVEITAMENTO_CURSO_REACT19.md            → docs/05-analises/
APROVEITAMENTO_DOCUMENTACAO_LARAVEL12.md    → docs/05-analises/
CLASSIFICACAO_DOCUMENTOS.md                 → docs/05-analises/
```

### 📖 06-referencias-tecnicas/ (3 arquivos)
```
INERTIA2_LARAVEL_REACT.md                  → docs/06-referencias-tecnicas/
REACT19_BIBLIOTECA_FRONTEND.md             → docs/06-referencias-tecnicas/
INDICE_DOCUMENTACAO.md                     → docs/06-referencias-tecnicas/
```

### 📚 referencia/laravel-12/
```
Laravel 12/docs-12.x/                      → referencia/laravel-12/docs-12.x/
Laravel 12/framework-12.x/                 → referencia/laravel-12/framework-12.x/
Laravel 12/laravel-12.x.md                 → referencia/laravel-12/laravel-12.x.md
Laravel 12/laravel-12.x.pdf                → referencia/laravel-12/laravel-12.x.pdf
Laravel 12/Laravel melhores práticas README.md → referencia/laravel-12/
```

### 📚 livros/
```
qi/PHP e Laravel Crie aplicações web como um verdadeiro artesão.md
    → livros/laravel/

qi/Professional-React-v19.3.0-labs.md
    → livros/react/

qi/react-guia-do-iniciate.md
    → livros/react/

qi/The Road to learn React - Português (Robin Wieruch).md
    → livros/react/

qi/PostgreSQL Banco de dados para aplicações web modernas.md
    → livros/banco-dados/

qi/Armazenando dados com Redis.md
    → livros/banco-dados/

qi/* (outros 8 arquivos)
    → livros/outros/
```

---

## ✅ Checklist de Implementação

### Fase 1: Criar Estrutura
- [ ] Criar `docs/00-base/`
- [ ] Criar `docs/01-arquitetura/`
- [ ] Criar `docs/02-ui-ux/`
- [ ] Criar `docs/03-sdlc/`
- [ ] Criar `docs/04-funcionalidades/`
- [ ] Criar `docs/05-analises/`
- [ ] Criar `docs/06-referencias-tecnicas/`
- [ ] Criar `referencia/laravel-12/`
- [ ] Criar `livros/laravel/`
- [ ] Criar `livros/react/`
- [ ] Criar `livros/banco-dados/`
- [ ] Criar `livros/outros/`

### Fase 2: Mover Arquivos (usando `git mv`)
- [ ] Mover arquivos para `docs/00-base/`
- [ ] Mover arquivos para `docs/01-arquitetura/`
- [ ] Mover arquivos para `docs/02-ui-ux/`
- [ ] Mover arquivos para `docs/03-sdlc/`
- [ ] Mover arquivos para `docs/04-funcionalidades/`
- [ ] Mover arquivos para `docs/05-analises/`
- [ ] Mover arquivos para `docs/06-referencias-tecnicas/`
- [ ] Mover `Laravel 12/` → `referencia/laravel-12/`
- [ ] Mover arquivos de `qi/` para `livros/`

### Fase 3: Atualizar Referências
- [ ] Atualizar `docs/README.md` com novos caminhos
- [ ] Verificar e atualizar links internos
- [ ] Atualizar `INDICE_DOCUMENTACAO.md`
- [ ] Verificar referências em outros documentos

### Fase 4: Validação
- [ ] Testar navegação
- [ ] Verificar que todos os arquivos foram movidos
- [ ] Confirmar que não há links quebrados
- [ ] Validar estrutura final

---

## ⚠️ Observações Importantes

1. **Git History:** Usar `git mv` preserva histórico
2. **Links Internos:** Podem precisar atualização
3. **README.md:** Manter na raiz de `docs/` como índice principal
4. **Backup:** Recomendado fazer backup antes

---

**Status:** Aguardando aprovação para implementação

