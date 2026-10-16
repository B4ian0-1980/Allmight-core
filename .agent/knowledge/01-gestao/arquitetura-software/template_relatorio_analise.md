---json
{
  "id": "template_relatorio_analise",
  "title": "📊 Relatório de Análise - [Nome do Material]",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 📊 Relatório de Análise - [Nome do Material].",
  "gatilhos": [
    "analise",
    "arquitetura",
    "gestao",
    "material",
    "nome",
    "relatorio",
    "software",
    "template"
  ],
  "perguntas_tipo": [
    "Como utilizar 📊 Relatório de Análise - [Nome do Material]?",
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

# 📊 Relatório de Análise - [Nome do Material]

**Data da Análise:** [data]  
**Tipo de Material:** [Livro/Documentação/Artigo/Tutorial/Outro]  
**Localização Original:** `_a-classificar/[caminho]`

---

## 📋 Identificação

### Informações Básicas
- **Título:** [título completo]
- **Autor(es):** [nome(s)]
- **Ano de Publicação:** [ano]
- **Versão:** [se aplicável]
- **Idioma:** [português/inglês/outro]
- **Páginas/Tamanho:** [quantidade de páginas ou tamanho]

### Tecnologias Cobertas
- **Tecnologia Principal:** [ex: Laravel, React, PostgreSQL]
- **Versão da Tecnologia:** [ex: Laravel 11, React 18]
- **Tecnologias Secundárias:** [lista]

---

## 🔍 Análise de Relevância

### Atualidade
- [ ] **Atual** - Tecnologia e práticas ainda relevantes (< 3 anos)
- [ ] **Parcialmente Atual** - Conceitos válidos, mas exemplos desatualizados
- [ ] **Desatualizado** - Tecnologia obsoleta ou práticas antigas (> 5 anos)

**Justificativa:**
[Explique por que é atual ou desatualizado]

---

### Qualidade do Conteúdo
- [ ] **Excelente** - Referência definitiva, altamente recomendado
- [ ] **Bom** - Conteúdo útil e bem escrito
- [ ] **Médio** - Conteúdo básico ou com lacunas
- [ ] **Fraco** - Conteúdo superficial ou mal escrito

**Justificativa:**
[Comente sobre a qualidade]

---

### Utilidade para a Base
- [ ] **Essencial** - Deve ser integrado imediatamente
- [ ] **Útil** - Bom para ter como referência
- [ ] **Opcional** - Pode ser útil em casos específicos
- [ ] **Desnecessário** - Já coberto por outros materiais ou não relevante

**Justificativa:**
[Explique a utilidade]

---

## 📖 Análise de Conteúdo

### Estrutura do Material

**Capítulos/Seções Principais:**
1. [Capítulo 1] - [Breve descrição]
2. [Capítulo 2] - [Breve descrição]
3. [Capítulo 3] - [Breve descrição]
[...]

---

### Tópicos Relevantes

#### ⭐ Conteúdo de Alto Valor
[Liste os tópicos mais valiosos que devem ser extraídos]

1. **[Tópico 1]**
   - **Páginas/Seções:** [localização]
   - **Valor:** [Por que é importante]
   - **Ação:** [Extrair para onde]

2. **[Tópico 2]**
   - **Páginas/Seções:** [localização]
   - **Valor:** [Por que é importante]
   - **Ação:** [Extrair para onde]

---

#### ✓ Conteúdo Útil
[Liste conteúdo útil mas não essencial]

- [Tópico A] - [Breve descrição]
- [Tópico B] - [Breve descrição]

---

#### ⚠️ Conteúdo Desatualizado
[Liste o que está desatualizado]

- [Tópico X] - [Por que está desatualizado]
- [Tópico Y] - [Por que está desatualizado]

---

### Exemplos de Código

**Quantidade:** [número aproximado de exemplos]

**Qualidade:**
- [ ] Excelentes - Prontos para uso
- [ ] Bons - Precisam adaptação mínima
- [ ] Médios - Precisam refatoração
- [ ] Fracos - Apenas didáticos

**Linguagem/Framework:** [ex: PHP 8.3, Laravel 11]

**Exemplos Destacados:**
1. [Exemplo 1] - [Localização] - [Por que é bom]
2. [Exemplo 2] - [Localização] - [Por que é bom]

---

## 🎯 Decisão de Classificação

### Decisão Final
- [ ] **MANTER E INTEGRAR** - Material será incluído na base
- [ ] **MANTER COMO REFERÊNCIA** - Arquivo será arquivado sem integração
- [ ] **EXTRAIR E DESCARTAR** - Extrair conteúdo útil e descartar original
- [ ] **DESCARTAR** - Material não será utilizado

---

### Destino na Estrutura

#### Arquivo Original
**Destino:** `[caminho na estrutura]`

**Exemplos:**
- Livro completo → `livros/[categoria]/[nome-arquivo]`
- Documentação → `referencia/[framework]/[nome-arquivo]`
- Artigo/Tutorial → `docs/05-analises/[nome-arquivo]`

---

#### Conteúdo Extraído

##### 1. Padrões e Boas Práticas
**Criar:** `docs/01-arquitetura/PADROES_[TECNOLOGIA].md`

**Conteúdo a extrair:**
- [Padrão 1] - [De onde extrair]
- [Padrão 2] - [De onde extrair]

---

##### 2. Exemplos Práticos
**Criar/Adicionar a:** `docs/01-arquitetura/EXEMPLOS_PRATICOS_[TECNOLOGIA].md`

**Exemplos a extrair:**
- [Exemplo 1] - [Páginas]
- [Exemplo 2] - [Páginas]

---

##### 3. Exemplos de Domínio
**Criar/Adicionar a:** `docs/07-exemplos-por-dominio/[dominio]/EXEMPLOS_[TIPO].md`

**Domínio:** [medico/ecommerce/financeiro/generico]

**Exemplos específicos do domínio:**
- [Exemplo 1]
- [Exemplo 2]

---

##### 4. Conceitos Fundamentais
**Criar/Adicionar a:** `docs/01-arquitetura/CONCEITOS_FUNDAMENTAIS_[TECNOLOGIA].md`

**Conceitos a extrair:**
- [Conceito 1]
- [Conceito 2]

---

## 📊 Comparação com Material Existente

### Material Similar na Base
[Liste materiais similares já existentes]

1. **[Arquivo existente 1]**
   - **Localização:** [caminho]
   - **Comparação:** [Este novo é melhor/pior/complementar?]

2. **[Arquivo existente 2]**
   - **Localização:** [caminho]
   - **Comparação:** [Este novo é melhor/pior/complementar?]

---

### Gaps Preenchidos
[Liste que gaps este material preenche na base atual]

- ✅ [Gap 1] - [Como este material preenche]
- ✅ [Gap 2] - [Como este material preenche]

---

### Redundâncias
[Identifique sobreposições desnecessárias]

- ⚠️ [Redundância 1] - [Como resolver]
- ⚠️ [Redundância 2] - [Como resolver]

---

## 🔄 Plano de Ação

### Ações Imediatas

1. [ ] Mover arquivo original para: `[destino]`
2. [ ] Criar `PADROES_[TECNOLOGIA].md`
3. [ ] Criar `EXEMPLOS_PRATICOS_[TECNOLOGIA].md`
4. [ ] Atualizar `INDICE_GERAL.md`
5. [ ] Atualizar `CONTEUDO_INCLUIDO.md`
6. [ ] Limpar `_a-classificar/`

---

### Conteúdo a Criar

#### Documento 1: [Nome]
**Localização:** `[caminho]`
**Conteúdo:**
- [Seção 1]
- [Seção 2]
- [Seção 3]

#### Documento 2: [Nome]
**Localização:** `[caminho]`
**Conteúdo:**
- [Seção 1]
- [Seção 2]

---

### Atualizações Necessárias

1. **`INDICE_GERAL.md`**
   - Adicionar link para novo material
   - Atualizar contadores

2. **`CONTEUDO_INCLUIDO.md`**
   - Adicionar à seção apropriada
   - Atualizar estatísticas

3. **Documentos existentes** (se aplicável)
   - [Documento X] - [O que adicionar]
   - [Documento Y] - [O que adicionar]

---

## 📝 Notas Adicionais

### Observações Importantes
[Qualquer observação relevante sobre o material]

### Recomendações Futuras
[Sugestões de outros materiais a buscar ou criar]

### Dependências
[Material que deve ser analisado junto ou antes deste]

---

## ✅ Checklist de Conclusão

- [ ] Relatório de análise completo
- [ ] Decisão de classificação tomada
- [ ] Plano de ação definido
- [ ] Arquivo original movido/copiado
- [ ] Documentos extraídos criados
- [ ] Índices atualizados
- [ ] `_a-classificar/` limpo
- [ ] Material testado/validado (se código)

---

## 📊 Resumo Executivo

**Decisão:** [MANTER/EXTRAIR/DESCARTAR]

**Destino:** `[caminho final]`

**Valor para a Base:** [Alto/Médio/Baixo]

**Ações Realizadas:**
- ✅ [Ação 1]
- ✅ [Ação 2]
- ✅ [Ação 3]

**Tempo de Análise:** [tempo gasto]

---

**Analista:** IA Assistant  
**Data do Relatório:** [data]  
**Versão:** 1.0

