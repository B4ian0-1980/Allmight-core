---json
{
  "id": "mapeamento_origem_arquivos",
  "title": "🗺️ Mapeamento de Origem dos Arquivos",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🗺️ Mapeamento de Origem dos Arquivos.",
  "gatilhos": [
    "arquitetura",
    "arquivos",
    "dos",
    "gestao",
    "mapeamento",
    "origem",
    "software"
  ],
  "perguntas_tipo": [
    "Como utilizar 🗺️ Mapeamento de Origem dos Arquivos?",
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

# 🗺️ Mapeamento de Origem dos Arquivos

**Data:** 2025-01-27  
**Versão:** 1.0

---

## 🎯 Objetivo

Este documento mapeia a origem de cada arquivo na estrutura base, identificando:
- De onde foi extraído/gerado
- Qual processo foi usado
- Como replicar para outros contextos

---

## 📋 Arquivos em docs/01-arquitetura/

### 1. EXEMPLOS_PRATICOS_LARAVEL.md

**Origem:**
- **Fonte primária:** Livro `livros/laravel/PHP e Laravel Crie aplicações web como um verdadeiro artesão.md` (223KB, 7.883 linhas)
- **Análise base:** `docs/05-analises/ANALISE_AGREGACAO_QI.md`
- **Complemento:** Documentação oficial Laravel 12.x

**Processo de Geração:**
1. Análise do livro identificando exemplos práticos
2. Extração de código funcional e testado
3. Organização por categoria (Controllers, Models, Migrations, etc.)
4. Adaptação para Laravel 12.x
5. Adição de explicações concisas

**Como Replicar:**
```
1. Leia o livro/documentação fonte
2. Identifique exemplos práticos completos
3. Organize por categoria funcional
4. Adapte para versão atual do framework
5. Adicione contexto e explicações
6. Valide que código compila/funciona
```

**Contexto:** Sistema médico (SESAU), mas exemplos são genéricos (CRUD, relacionamentos, etc.)

**Valor:** ⭐⭐⭐ ALTO - Exemplos práticos aceleram desenvolvimento

---

### 2. CONCEITOS_FUNDAMENTAIS_REACT.md

**Origem:**
- **Fontes primárias:** Livros React antigos (2015-2018) da pasta `livros/react/`
  - The Road to learn React
  - React Guia do Iniciante
  - Outros livros clássicos
- **Análise:** Identificação manual de conceitos ainda válidos

**Processo de Geração:**
1. Leitura dos livros React clássicos
2. Identificação de conceitos fundamentais imutáveis:
   - JSX
   - Props
   - State
   - Composição vs Herança
   - Fluxo unidirecional
3. **ADAPTAÇÃO CRÍTICA:** Conversão de padrões antigos para modernos
   - Classes → Hooks
   - componentDidMount → useEffect
   - setState → useState
4. Consolidação em documento único
5. Validação com React 19

**Como Replicar:**
```
1. Identifique livros/docs com conceitos fundamentais
2. Extraia APENAS conceitos que não mudam com versões
3. Adapte sintaxe para versão atual:
   - Classes → Hooks (React)
   - Callbacks → Promises/Async-Await (JS)
   - etc.
4. Valide com documentação oficial atual
5. Adicione avisos sobre adaptações
```

**Contexto:** Genérico - Conceitos fundamentais aplicam-se a qualquer projeto React

**Valor:** ⭐⭐⭐ ALTO - Conceitos fundamentais são base sólida

---

### 3. PADROES_REACT19.md

**Origem:**
- **Fonte primária:** `livros/react/Professional-React-v19.3.0-labs.md` (93KB, 2.755 linhas)
- **Fonte secundária:** The Road to learn React
- **Complemento:** Documentação oficial React 19

**Processo de Geração:**
1. Análise do curso Professional React v19
2. Extração de padrões específicos da versão 19:
   - Hooks nativos e customizados
   - Context API moderna
   - TypeScript patterns
   - Performance optimization
3. Organização por categoria
4. Adição de exemplos práticos
5. Inclusão de padrões de projeto

**Como Replicar:**
```
1. Identifique documentação da versão específica
2. Extraia padrões recomendados
3. Organize por tipo (hooks, context, performance, etc.)
4. Adicione exemplos práticos de uso
5. Inclua best practices específicas da versão
```

**Contexto:** Usa exemplo de sistema médico (usePacientes), mas padrões são genéricos

**Valor:** ⭐⭐⭐ ALTO - Padrões da versão atual evitam código obsoleto

---

### 4. PADROES_CODIGO_LARAVEL.md

**Origem:**
- **Fonte primária:** `LARAVEL_BEST_PRACTICES.md` (da comunidade)
- **Fonte secundária:** PSR Standards (PHP-FIG)
- **Complemento:** Convenções próprias do projeto

**Processo de Geração:**
1. Consolidação de boas práticas da comunidade
2. Adição de convenções de nomenclatura
3. Organização de padrões por categoria
4. Adição de exemplos práticos
5. Criação de checklist de qualidade

**Como Replicar:**
```
1. Pesquise "Laravel Best Practices" na comunidade
2. Adicione PSR Standards relevantes
3. Defina convenções de nomenclatura
4. Organize por categoria (Controllers, Models, etc.)
5. Adicione exemplos bom vs ruim
6. Crie checklist de validação
```

**Contexto:** Genérico com alguns exemplos de domínio médico

**Valor:** ⭐⭐⭐ ALTO - Padrões consistentes melhoram manutenibilidade

---

### 5. ARQUITETURA_ESTRUTURA_LARAVEL12.md

**Origem:**
- **Fonte primária:** Documentação oficial Laravel 12.x (`referencia/laravel-12/docs-12.x/structure.md`)
- **Complemento:** Experiência prática com o framework

**Processo de Geração:**
1. Leitura da documentação oficial de estrutura
2. Detalhamento de cada pasta/diretório
3. Adição de quando usar cada pattern (Repository, Service, etc.)
4. Exemplos práticos de organização
5. Regras de onde colocar cada tipo de código

**Como Replicar:**
```
1. Acesse documentação oficial do framework
2. Busque seção sobre estrutura de arquivos
3. Detalhe propósito de cada pasta
4. Adicione padrões de organização (Repository, Service, etc.)
5. Inclua exemplos de quando usar cada padrão
6. Defina regras claras de onde colocar código
```

**Contexto:** 100% genérico - Estrutura padrão do Laravel

**Valor:** ⭐⭐⭐ ALTO - Estrutura correta evita bagunça

---

### 6. LARAVEL_BEST_PRACTICES.md

**Origem:**
- **Fonte primária:** Repositório GitHub "alexeymezenin/laravel-best-practices"
- **Tradução:** Adaptado e traduzido para português

**Processo de Geração:**
1. Fork/download do repositório original
2. Tradução para português
3. Adaptação de exemplos para contexto brasileiro
4. Adição de comentários explicativos

**Como Replicar:**
```
1. Busque "Laravel Best Practices" no GitHub
2. Identifique repositório mais popular/atualizado
3. Traduza se necessário
4. Adapte exemplos para seu contexto
5. Adicione comentários explicativos
```

**Contexto:** 100% genérico - Boas práticas da comunidade

**Valor:** ⭐⭐⭐ ALTO - Comunidade validou práticas

---

### 7. GUIA_MELHORIA_QUALIDADE_CODIGO.md

**Origem:**
- **Fonte:** Análise própria de gaps na documentação
- **Base:** Experiência com desenvolvimento por IA

**Processo de Geração:**
1. Identificação de áreas sem documentação
2. Pesquisa de boas práticas para cada área
3. Priorização por impacto na qualidade
4. Sugestões de documentação adicional
5. Fontes recomendadas para cada área

**Como Replicar:**
```
1. Analise documentação existente
2. Identifique o que está faltando
3. Priorize por impacto (Alta, Média, Baixa)
4. Sugira documentação para cada gap
5. Indique fontes confiáveis
```

**Contexto:** 100% genérico - Aplicável a qualquer projeto

**Valor:** ⭐⭐ MÉDIO - Guia para melhorias futuras

---

## 📊 Resumo por Tipo de Origem

### Extraídos de Livros Técnicos
1. **EXEMPLOS_PRATICOS_LARAVEL.md** ← Livro Laravel
2. **CONCEITOS_FUNDAMENTAIS_REACT.md** ← Livros React clássicos
3. **PADROES_REACT19.md** ← Curso Professional React v19

### Extraídos de Documentação Oficial
1. **ARQUITETURA_ESTRUTURA_LARAVEL12.md** ← Docs Laravel 12.x

### Adaptados da Comunidade
1. **LARAVEL_BEST_PRACTICES.md** ← GitHub comunidade
2. **PADROES_CODIGO_LARAVEL.md** ← Best practices + PSR

### Criados por Análise
1. **GUIA_MELHORIA_QUALIDADE_CODIGO.md** ← Análise de gaps

---

## 🎯 Recomendações para Novos Arquivos

### Para Extrair de Livros
1. **Identifique valor:** Livro tem exemplos práticos?
2. **Valide atualidade:** Padrões ainda são válidos?
3. **Adapte quando necessário:** Converta para versão atual
4. **Organize por categoria:** Facilite busca
5. **Adicione contexto:** Explique quando usar

### Para Extrair de Documentação
1. **Use fonte oficial:** Sempre preferível
2. **Mantenha atualizado:** Acompanhe versões
3. **Adicione exemplos:** Docs oficiais são às vezes áridas
4. **Organize logicamente:** Não apenas copie

### Para Adaptar da Comunidade
1. **Valide fontes:** Use repositórios populares/mantidos
2. **Traduza se necessário:** Facilita uso
3. **Adapte exemplos:** Para seu contexto
4. **Credite origem:** Sempre

---

## 🔄 Como Criar Versões para Outros Domínios

### Estrutura Proposta

```
base-estrutura-projeto/
├── docs/
│   ├── 01-arquitetura/
│   │   ├── [arquivos genéricos atuais]
│   │   └── README.md
│   │
│   └── 07-exemplos-por-dominio/
│       ├── README.md
│       ├── medico/
│       │   ├── EXEMPLOS_SISTEMA_HOSPITALAR.md
│       │   ├── PADROES_DADOS_SAUDE.md
│       │   └── GLOSSARIO_MEDICO.md
│       │
│       ├── ecommerce/
│       │   ├── EXEMPLOS_LOJA_VIRTUAL.md
│       │   ├── PADROES_CARRINHO_PAGAMENTO.md
│       │   └── GLOSSARIO_ECOMMERCE.md
│       │
│       ├── financeiro/
│       │   ├── EXEMPLOS_SISTEMA_BANCARIO.md
│       │   ├── PADROES_TRANSACOES.md
│       │   └── GLOSSARIO_FINANCEIRO.md
│       │
│       └── generico/
│           ├── EXEMPLOS_CRUD_BASICO.md
│           └── PADROES_COMUNS.md
```

### Processo para Criar Novo Domínio

1. **Identifique domínio:** E-commerce, Financeiro, Educacional, etc.
2. **Analise exemplos existentes:** O que é específico do domínio atual?
3. **Extraia genéricos:** Mova para pasta genérica
4. **Crie pasta domínio:** `docs/07-exemplos-por-dominio/[dominio]/`
5. **Adapte exemplos:** Contextualize para novo domínio
6. **Crie glossário:** Termos específicos do domínio
7. **Documente padrões:** Padrões específicos (ex: carrinho para e-commerce)

---

## ✅ Checklist para Novos Arquivos

Ao criar novo arquivo gerado/extraído:

- [ ] Documentar origem claramente no início do arquivo
- [ ] Indicar processo de geração/extração
- [ ] Adicionar data e versão
- [ ] Validar que exemplos funcionam
- [ ] Organizar logicamente
- [ ] Adicionar ao índice apropriado
- [ ] Atualizar este mapeamento
- [ ] Creditar fontes originais
- [ ] Marcar se é genérico ou específico de domínio

---

**Última Atualização:** 2025-01-27  
**Próxima Revisão:** Quando adicionar novos arquivos gerados

