---json
{
  "id": "proposta_organizacao_estrutura",
  "title": "📁 Proposta de Organização da Estrutura do Projeto",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 📁 Proposta de Organização da Estrutura do Projeto.",
  "gatilhos": [
    "arquitetura",
    "estrutura",
    "gestao",
    "organizacao",
    "projeto",
    "proposta",
    "software"
  ],
  "perguntas_tipo": [
    "Como utilizar 📁 Proposta de Organização da Estrutura do Projeto?",
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

# 📁 Proposta de Organização da Estrutura do Projeto

**Data:** 2025-01-27  
**Versão:** 1.0  
**Status:** Proposta - Aguardando Aprovação

---

## 🎯 Objetivo

Reorganizar todos os arquivos e pastas do projeto de acordo com suas funções, facilitando navegação, manutenção e desenvolvimento.

---

## 📊 Estrutura Proposta

```
same/
├── 📚 docs/                          # Documentação principal do projeto
│   ├── 📋 00-base/                   # Documentação base e fundamental
│   │   ├── README.md                  # Índice principal (mantém)
│   │   ├── LEVANTAMENTO_PROJETO.md
│   │   ├── REQUISITOS_NEGOCIO_FUNCIONAIS.md
│   │   ├── DOCUMENTACAO_SDLC_COMPLETA.md
│   │   ├── DIRETRIZES_DESENVOLVIMENTO.md
│   │   └── AMBIENTE_DESENVOLVIMENTO.md
│   │
│   ├── 🏗️ 01-arquitetura/            # Arquitetura e padrões
│   │   ├── ARQUITETURA_ESTRUTURA_LARAVEL12.md
│   │   ├── PADROES_CODIGO_LARAVEL.md
│   │   ├── LARAVEL_BEST_PRACTICES.md
│   │   ├── PADROES_REACT19.md
│   │   ├── EXEMPLOS_PRATICOS_LARAVEL.md
│   │   └── GUIA_MELHORIA_QUALIDADE_CODIGO.md
│   │
│   ├── 🎨 02-ui-ux/                  # Design System e UX
│   │   ├── DESIGN_SYSTEM_COMPLETO.md
│   │   ├── LAYOUT_INTERFACE_PERFIS.md
│   │   ├── ANALISE_UX_BOTOES_VS_SELECTS.md
│   │   ├── REQUISITOS_UX_DETALHADOS.md
│   │   ├── IMPLEMENTACAO_COMPONENTES_UX.md
│   │   └── STORYBOOK_CONFIGURACAO_IA.md
│   │
│   ├── 🔄 03-sdlc/                    # Ciclo de vida do desenvolvimento
│   │   ├── EVOLUCAO_ANALISE_UX_SDLC.md
│   │   ├── RESUMO_EXECUTIVO_UX_COMPONENTES.md
│   │   ├── ESTRATEGIA_TESTES_UX.md
│   │   ├── ESTRATEGIA_DEPLOY_UX.md
│   │   └── PLANO_MANUTENCAO_UX.md
│   │
│   ├── ⚙️ 04-funcionalidades/         # Funcionalidades específicas
│   │   ├── DADOS_ACOLHIMENTO_PACIENTE.md
│   │   ├── SISTEMA_PERMISSOES_SESAU_AVANCADO.md
│   │   ├── IMPLEMENTACAO_PERMISSOES_TRIAGEM.md
│   │   ├── ALTERACOES_TRIAGEM_LARANJA.md
│   │   ├── GESTAO_PACIENTES_HISTORICO.md
│   │   ├── GESTAO_EVENTOS_EQUIPES.md
│   │   └── INTEGRACAO_MEDICAMENTOS_ESTOQUE.md
│   │
│   ├── 🔍 05-analises/                # Análises diversas
│   │   ├── ANALISE_AGREGACAO_QI.md
│   │   ├── ANALISE_EXTRAS_AI_TOOLS.md
│   │   ├── ANALISE_COMPLETA_REPOSITORIO_REACT.md
│   │   ├── ANALISE_FRAMEWORKS_OFFLINE.md
│   │   ├── ANALISE_DOCUMENTACAO.md
│   │   ├── APROVEITAMENTO_CURSO_REACT19.md
│   │   ├── APROVEITAMENTO_DOCUMENTACAO_LARAVEL12.md
│   │   └── CLASSIFICACAO_DOCUMENTOS.md
│   │
│   └── 📖 06-referencias-tecnicas/    # Referências técnicas
│       ├── INERTIA2_LARAVEL_REACT.md
│       ├── REACT19_BIBLIOTECA_FRONTEND.md
│       └── INDICE_DOCUMENTACAO.md
│
├── 📚 referencia/                      # Documentação de referência (renomeado de "Laravel 12")
│   ├── laravel-12/                    # Documentação Laravel 12
│   │   ├── docs-12.x/                 # Docs oficiais Laravel 12
│   │   ├── framework-12.x/            # Framework source
│   │   ├── laravel-12.x.md            # Doc completa em markdown
│   │   ├── laravel-12.x.pdf           # Doc completa em PDF
│   │   └── Laravel melhores práticas README.md
│   │
│   └── react-19/                      # Documentação React 19
│       └── (conteúdo de "Reactjs - main" se necessário)
│
├── 📚 livros/                         # Livros e materiais de estudo (renomeado de "qi")
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
├── 🛠️ extras/                         # Ferramentas e integrações extras (mantém)
│   ├── ai-integration-main/
│   ├── pace-main/
│   ├── playwright-ai-integration-main/
│   └── spot-toolkit-main/
│
└── 🔧 converter/                      # Scripts de conversão (mantém)
    └── (arquivos de conversão PDF para MD)
```

---

## 📋 Detalhamento das Categorias

### 📋 00-base/
**Propósito:** Documentação fundamental que serve como base para todo o projeto.

**Arquivos:**
- `README.md` - Índice principal da documentação
- `LEVANTAMENTO_PROJETO.md` - Estado atual e como começar
- `REQUISITOS_NEGOCIO_FUNCIONAIS.md` - Requisitos que orientam tudo
- `DOCUMENTACAO_SDLC_COMPLETA.md` - Documentação completa do SDLC
- `DIRETRIZES_DESENVOLVIMENTO.md` - Diretrizes e princípios
- `AMBIENTE_DESENVOLVIMENTO.md` - Setup do ambiente

**Quando usar:** Sempre que precisar entender o projeto, requisitos ou diretrizes.

---

### 🏗️ 01-arquitetura/
**Propósito:** Arquitetura, padrões de código e estrutura do projeto.

**Arquivos:**
- `ARQUITETURA_ESTRUTURA_LARAVEL12.md` - Estrutura de pastas Laravel
- `PADROES_CODIGO_LARAVEL.md` - Padrões e convenções Laravel
- `LARAVEL_BEST_PRACTICES.md` - Melhores práticas Laravel
- `PADROES_REACT19.md` - Padrões React 19
- `EXEMPLOS_PRATICOS_LARAVEL.md` - Exemplos práticos de código
- `GUIA_MELHORIA_QUALIDADE_CODIGO.md` - Guia de qualidade

**Quando usar:** Durante desenvolvimento, para seguir padrões e arquitetura.

---

### 🎨 02-ui-ux/
**Propósito:** Design System, layouts e componentes de interface.

**Arquivos:**
- `DESIGN_SYSTEM_COMPLETO.md` - Design System completo
- `LAYOUT_INTERFACE_PERFIS.md` - Layouts por perfil
- `ANALISE_UX_BOTOES_VS_SELECTS.md` - Análise UX de componentes
- `REQUISITOS_UX_DETALHADOS.md` - Requisitos UX detalhados
- `IMPLEMENTACAO_COMPONENTES_UX.md` - Implementação de componentes
- `STORYBOOK_CONFIGURACAO_IA.md` - Configuração Storybook

**Quando usar:** Durante desenvolvimento de interfaces e componentes.

---

### 🔄 03-sdlc/
**Propósito:** Documentação do ciclo de vida do desenvolvimento (SDLC).

**Arquivos:**
- `EVOLUCAO_ANALISE_UX_SDLC.md` - Evolução UX no SDLC
- `RESUMO_EXECUTIVO_UX_COMPONENTES.md` - Resumo executivo
- `ESTRATEGIA_TESTES_UX.md` - Estratégia de testes
- `ESTRATEGIA_DEPLOY_UX.md` - Estratégia de deploy
- `PLANO_MANUTENCAO_UX.md` - Plano de manutenção

**Quando usar:** Para entender fases do SDLC e estratégias.

---

### ⚙️ 04-funcionalidades/
**Propósito:** Documentação de funcionalidades específicas do sistema.

**Arquivos:**
- `DADOS_ACOLHIMENTO_PACIENTE.md` - Dados de acolhimento
- `SISTEMA_PERMISSOES_SESAU_AVANCADO.md` - Sistema de permissões
- `IMPLEMENTACAO_PERMISSOES_TRIAGEM.md` - Permissões de triagem
- `ALTERACOES_TRIAGEM_LARANJA.md` - Alterações triagem laranja
- `GESTAO_PACIENTES_HISTORICO.md` - Gestão de pacientes
- `GESTAO_EVENTOS_EQUIPES.md` - Gestão de eventos
- `INTEGRACAO_MEDICAMENTOS_ESTOQUE.md` - Integração medicamentos

**Quando usar:** Para implementar ou entender funcionalidades específicas.

---

### 🔍 05-analises/
**Propósito:** Análises diversas realizadas durante o projeto.

**Arquivos:**
- `ANALISE_AGREGACAO_QI.md` - Análise da pasta QI
- `ANALISE_EXTRAS_AI_TOOLS.md` - Análise de ferramentas AI
- `ANALISE_COMPLETA_REPOSITORIO_REACT.md` - Análise React
- `ANALISE_FRAMEWORKS_OFFLINE.md` - Análise frameworks offline
- `ANALISE_DOCUMENTACAO.md` - Análise da documentação
- `APROVEITAMENTO_CURSO_REACT19.md` - Aproveitamento curso React
- `APROVEITAMENTO_DOCUMENTACAO_LARAVEL12.md` - Aproveitamento Laravel
- `CLASSIFICACAO_DOCUMENTOS.md` - Classificação de documentos

**Quando usar:** Para entender análises realizadas e decisões tomadas.

---

### 📖 06-referencias-tecnicas/
**Propósito:** Referências técnicas de frameworks e tecnologias.

**Arquivos:**
- `INERTIA2_LARAVEL_REACT.md` - Inertia.js 2
- `REACT19_BIBLIOTECA_FRONTEND.md` - React 19
- `INDICE_DOCUMENTACAO.md` - Índice de documentação

**Quando usar:** Para consultar referências técnicas durante desenvolvimento.

---

## 🔄 Mudanças Propostas

### Pastas a Criar:
1. `docs/00-base/`
2. `docs/01-arquitetura/`
3. `docs/02-ui-ux/`
4. `docs/03-sdlc/`
5. `docs/04-funcionalidades/`
6. `docs/05-analises/`
7. `docs/06-referencias-tecnicas/`
8. `referencia/` (nova pasta raiz)
9. `referencia/laravel-12/`
10. `referencia/react-19/` (se necessário)
11. `livros/` (nova pasta raiz)
12. `livros/laravel/`
13. `livros/react/`
14. `livros/banco-dados/`
15. `livros/outros/`

### Pastas a Renomear:
1. `Laravel 12/` → `referencia/laravel-12/`
2. `qi/` → `livros/` (com subpastas organizadas)
3. `Reactjs - main/` → `referencia/react-19/` (se necessário manter)

### Pastas a Manter:
1. `extras/` - Mantém como está
2. `converter/` - Mantém como está
3. `docs/` - Mantém, mas reorganiza internamente

---

## ✅ Vantagens da Nova Estrutura

1. **Organização Clara:** Cada tipo de documento tem sua pasta
2. **Navegação Fácil:** Prefixos numéricos facilitam ordem lógica
3. **Manutenção Simples:** Fácil encontrar e atualizar documentos
4. **Escalabilidade:** Estrutura permite crescimento organizado
5. **Separação de Responsabilidades:** Documentação vs Referências vs Livros

---

## ⚠️ Considerações

1. **README.md:** Será atualizado com novos caminhos
2. **Links Internos:** Podem precisar de atualização
3. **Git:** Histórico será preservado com `git mv`
4. **Backup:** Recomendado fazer backup antes

---

## 📝 Próximos Passos

1. ✅ **Aprovar esta proposta**
2. ⏳ Criar estrutura de pastas
3. ⏳ Mover arquivos (usando `git mv` para preservar histórico)
4. ⏳ Atualizar `docs/README.md` com novos caminhos
5. ⏳ Verificar e atualizar links internos
6. ⏳ Testar navegação

---

**Status:** Aguardando aprovação para implementação

