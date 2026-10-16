---json
{
  "id": "como_analisar_sistema",
  "title": "🔍 Como Analisar um Sistema Usando a Base-Estrutura-Projeto",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🔍 Como Analisar um Sistema Usando a Base-Estrutura-Projeto.",
  "gatilhos": [
    "analisar",
    "arquitetura",
    "base-estrutura-projeto",
    "como",
    "gestao",
    "sistema",
    "software",
    "usando"
  ],
  "perguntas_tipo": [
    "Como utilizar 🔍 Como Analisar um Sistema Usando a Base-Estrutura-Projeto?",
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

# 🔍 Como Analisar um Sistema Usando a Base-Estrutura-Projeto

**Versão:** 1.0  
**Data:** 2025-01-28

---

## 🎯 Objetivo

Este guia explica como usar a `base-estrutura-projeto` para **identificar e analisar um sistema existente**, documentando sua estrutura, tecnologias, padrões e funcionalidades.

---

## 🚀 Processo Completo

### Fase 1: Preparação e Identificação Inicial

#### 1.1. Anexar o Sistema ao Chat

**Opção A: Sistema Completo**
```
Anexe a pasta raiz do sistema ao chat:
@caminho/para/seu-sistema
```

**Opção B: Estrutura Específica**
```
Anexe apenas partes relevantes:
@caminho/para/seu-sistema/app
@caminho/para/seu-sistema/config
@caminho/para/seu-sistema/docs
```

#### 1.2. Solicitar Análise Inicial

**Comando sugerido:**
```
Analise o sistema @caminho/para/seu-sistema e identifique:

1. Stack tecnológico (linguagem, framework, banco de dados)
2. Estrutura de pastas e organização
3. Padrões de código utilizados
4. Funcionalidades principais
5. Dependências e tecnologias auxiliares
6. Documentação existente

Use a base-estrutura-projeto como referência para:
- Identificar padrões similares
- Comparar com boas práticas
- Sugerir melhorias de organização
```

---

### Fase 2: Análise Detalhada por Área

#### 2.1. Identificação de Tecnologias

**O que a IA fará:**
- ✅ Identificar linguagem principal
- ✅ Identificar framework(s) usado(s)
- ✅ Identificar banco de dados
- ✅ Identificar ferramentas de build/test
- ✅ Identificar bibliotecas principais

**Como usar a base:**
```
Compare as tecnologias identificadas com:
- docs/01-arquitetura/ - Padrões conhecidos
- referencia/ - Documentação oficial
- livros/ - Materiais de referência
```

**Resultado esperado:**
- Lista de tecnologias identificadas
- Versões (quando possível)
- Referências à documentação na base

---

#### 2.2. Análise de Estrutura

**O que a IA fará:**
- ✅ Mapear estrutura de pastas
- ✅ Identificar organização de código
- ✅ Comparar com padrões conhecidos
- ✅ Identificar desvios de boas práticas

**Como usar a base:**
```
Compare com:
- docs/01-arquitetura/ARQUITETURA_ESTRUTURA_[TECNOLOGIA].md
- docs/01-arquitetura/PADROES_CODIGO_[TECNOLOGIA].md
```

**Resultado esperado:**
- Diagrama de estrutura
- Comparação com padrões
- Sugestões de melhorias

---

#### 2.3. Análise de Padrões de Código

**O que a IA fará:**
- ✅ Identificar padrões arquiteturais
- ✅ Identificar convenções de nomenclatura
- ✅ Identificar padrões de organização
- ✅ Identificar anti-padrões

**Como usar a base:**
```
Compare com:
- docs/01-arquitetura/PADROES_CODIGO_[TECNOLOGIA].md
- docs/01-arquitetura/LARAVEL_BEST_PRACTICES.md (se Laravel)
- docs/01-arquitetura/PADROES_REACT19.md (se React)
- docs/01-arquitetura/PADROES_VUEJS3.md (se Vue.js)
```

**Resultado esperado:**
- Padrões identificados
- Conformidade com boas práticas
- Recomendações de melhoria

---

#### 2.4. Análise de Funcionalidades

**O que a IA fará:**
- ✅ Mapear funcionalidades principais
- ✅ Identificar módulos/serviços
- ✅ Identificar integrações
- ✅ Identificar dependências entre módulos

**Como usar a base:**
```
Compare com:
- docs/07-exemplos-por-dominio/ - Exemplos por área
- docs/04-funcionalidades/ - Funcionalidades específicas
```

**Resultado esperado:**
- Lista de funcionalidades
- Mapa de dependências
- Identificação de domínio (médico, e-commerce, etc.)

---

### Fase 3: Documentação da Análise

#### 3.1. Criar Documento de Levantamento

**Usar template:**
```
docs/00-base/TEMPLATE_LEVANTAMENTO_PROJETO.md
```

**Solicitar:**
```
Crie um documento de levantamento completo do sistema 
@caminho/para/seu-sistema usando o template:

docs/00-base/TEMPLATE_LEVANTAMENTO_PROJETO.md

Inclua:
- Stack tecnológico identificado
- Estrutura de pastas
- Padrões de código
- Funcionalidades principais
- Dependências
- Documentação existente
- O que falta implementar
```

---

#### 3.2. Criar Documento de Arquitetura

**Se a tecnologia estiver na base:**
```
Use como referência:
- docs/01-arquitetura/ARQUITETURA_ESTRUTURA_[TECNOLOGIA].md
- docs/01-arquitetura/PADROES_CODIGO_[TECNOLOGIA].md
```

**Se a tecnologia NÃO estiver na base:**
```
1. Coloque materiais em _a-classificar/tecnologias/[nome]/
2. Solicite análise e integração
3. Depois use os documentos gerados
```

**Solicitar:**
```
Crie um documento de arquitetura do sistema 
@caminho/para/seu-sistema documentando:

- Arquitetura geral
- Padrões utilizados
- Estrutura de módulos
- Fluxo de dados
- Integrações

Use como referência:
- docs/01-arquitetura/ARQUITETURA_ESTRUTURA_[TECNOLOGIA].md
- docs/01-arquitetura/PADROES_CODIGO_[TECNOLOGIA].md
```

---

#### 3.3. Criar Análise de Qualidade

**Usar como referência:**
```
docs/01-arquitetura/GUIA_MELHORIA_QUALIDADE_CODIGO.md
```

**Solicitar:**
```
Analise a qualidade do código do sistema 
@caminho/para/seu-sistema e crie um relatório:

- Conformidade com padrões
- Boas práticas seguidas
- Pontos de melhoria
- Prioridades de refatoração

Use como referência:
docs/01-arquitetura/GUIA_MELHORIA_QUALIDADE_CODIGO.md
```

---

### Fase 4: Organização na Base

#### 4.1. Criar Pasta do Sistema

**Estrutura recomendada:**
```
0-fonte/
├── base-estrutura-projeto/  # Base genérica (não tocar)
└── sistema/                 # Seus sistemas
    └── [nome-do-sistema]/
        ├── docs/            # Documentação do sistema
        │   ├── LEVANTAMENTO_PROJETO.md
        │   ├── ARQUITETURA.md
        │   └── ANALISE_QUALIDADE.md
        └── [código-fonte]/   # Código do sistema
```

**⚠️ IMPORTANTE:** Não modifique `base-estrutura-projeto/` diretamente!

---

#### 4.2. Organizar Documentação

**Estrutura sugerida:**
```
sistema/[nome-do-sistema]/docs/
├── 00-base/
│   ├── LEVANTAMENTO_PROJETO.md
│   ├── REQUISITOS_NEGOCIO_FUNCIONAIS.md
│   └── DIRETRIZES_DESENVOLVIMENTO.md
├── 01-arquitetura/
│   ├── ARQUITETURA.md
│   ├── PADROES_CODIGO.md
│   └── ANALISE_QUALIDADE.md
├── 04-funcionalidades/
│   └── [funcionalidades específicas]
└── 05-analises/
    └── ANALISE_INICIAL.md
```

---

## 📋 Checklist Completo

### Preparação
- [ ] Sistema anexado ao chat
- [ ] Base-estrutura-projeto acessível
- [ ] Objetivo da análise definido

### Análise
- [ ] Stack tecnológico identificado
- [ ] Estrutura de pastas mapeada
- [ ] Padrões de código identificados
- [ ] Funcionalidades mapeadas
- [ ] Dependências listadas
- [ ] Documentação existente revisada

### Documentação
- [ ] LEVANTAMENTO_PROJETO.md criado
- [ ] ARQUITETURA.md criado
- [ ] ANALISE_QUALIDADE.md criado
- [ ] Documentação organizada na estrutura

### Organização
- [ ] Pasta do sistema criada em `sistema/`
- [ ] Documentação organizada
- [ ] Índices atualizados

---

## 🎯 Exemplos Práticos

### Exemplo 1: Sistema Laravel + React

**Solicitação:**
```
Analise o sistema @meu-sistema e identifique:

1. Stack: Laravel (backend) + React (frontend)
2. Estrutura: Compare com docs/01-arquitetura/ARQUITETURA_ESTRUTURA_LARAVEL12.md
3. Padrões: Compare com docs/01-arquitetura/PADROES_CODIGO_LARAVEL.md e PADROES_REACT19.md
4. Funcionalidades: Mapeie módulos principais
5. Crie LEVANTAMENTO_PROJETO.md usando docs/00-base/TEMPLATE_LEVANTAMENTO_PROJETO.md
```

---

### Exemplo 2: Sistema Vue.js 3

**Solicitação:**
```
Analise o sistema @meu-sistema-vue e:

1. Identifique estrutura Vue.js 3
2. Compare com docs/01-arquitetura/PADROES_VUEJS3.md
3. Compare com docs/01-arquitetura/EXEMPLOS_PRATICOS_VUEJS3.md
4. Identifique padrões utilizados
5. Crie documentação completa
```

---

### Exemplo 3: Sistema com Tecnologia Não Documentada

**Solicitação:**
```
Analise o sistema @meu-sistema-django e:

1. Identifique: Django (Python)
2. Como Django não está na base, coloque materiais em:
   _a-classificar/tecnologias/django/
3. Solicite análise e integração do Django
4. Depois use os documentos gerados para análise completa
```

---

## 🔧 Comandos Úteis

### Análise Rápida
```
Analise @sistema e identifique:
- Stack tecnológico
- Estrutura principal
- Padrões utilizados
```

### Análise Completa
```
Faça análise completa do sistema @sistema:

1. Identifique todas as tecnologias
2. Mapeie estrutura completa
3. Analise padrões de código
4. Documente funcionalidades
5. Crie LEVANTAMENTO_PROJETO.md
6. Crie ARQUITETURA.md
7. Crie ANALISE_QUALIDADE.md

Use base-estrutura-projeto como referência.
```

### Análise Específica
```
Analise apenas a arquitetura do sistema @sistema:

- Compare com docs/01-arquitetura/
- Identifique padrões arquiteturais
- Documente desvios de boas práticas
- Sugira melhorias
```

---

## 📚 Recursos da Base

### Para Identificação de Tecnologias
- `docs/01-arquitetura/` - Padrões por tecnologia
- `referencia/` - Documentação oficial
- `livros/` - Materiais de referência

### Para Análise de Padrões
- `docs/01-arquitetura/PADROES_CODIGO_*.md`
- `docs/01-arquitetura/LARAVEL_BEST_PRACTICES.md`
- `docs/01-arquitetura/GUIA_MELHORIA_QUALIDADE_CODIGO.md`

### Para Análise de Arquitetura
- `docs/01-arquitetura/ARQUITETURA_ESTRUTURA_*.md`
- `docs/01-arquitetura/DESIGN_PATTERNS_*.md`

### Para Templates
- `docs/00-base/TEMPLATE_LEVANTAMENTO_PROJETO.md`
- `docs/00-base/TEMPLATE_REQUISITOS.md`
- `docs/00-base/TEMPLATE_DIRETRIZES.md`

---

## 💡 Dicas

### 1. Comece pelo Básico
- Primeiro identifique stack tecnológico
- Depois mapeie estrutura
- Por fim, analise padrões

### 2. Use a Base como Referência
- Sempre compare com padrões conhecidos
- Use templates para documentação
- Consulte exemplos similares

### 3. Documente Progressivamente
- Não tente documentar tudo de uma vez
- Comece com levantamento geral
- Detalhe conforme necessário

### 4. Organize Bem
- Use estrutura de pastas da base
- Mantenha base genérica separada
- Organize sistemas em `sistema/`

---

## 🚨 Erros Comuns a Evitar

### ❌ Modificar a Base Diretamente
```
❌ ERRADO:
base-estrutura-projeto/docs/01-arquitetura/MEU_SISTEMA.md

✅ CORRETO:
sistema/meu-sistema/docs/01-arquitetura/ARQUITETURA.md
```

### ❌ Não Usar Templates
```
❌ ERRADO: Criar documento do zero
✅ CORRETO: Usar TEMPLATE_LEVANTAMENTO_PROJETO.md
```

### ❌ Ignorar a Base
```
❌ ERRADO: Analisar sem comparar com padrões
✅ CORRETO: Sempre comparar com docs/01-arquitetura/
```

---

## 📊 Resultado Esperado

Após seguir este processo, você terá:

1. ✅ **Stack tecnológico identificado**
2. ✅ **Estrutura mapeada e documentada**
3. ✅ **Padrões identificados e comparados**
4. ✅ **Funcionalidades documentadas**
5. ✅ **Análise de qualidade realizada**
6. ✅ **Documentação organizada**
7. ✅ **Sugestões de melhoria**

---

## 🔄 Próximos Passos

Após a análise:

1. **Use a documentação gerada** para:
   - Planejar melhorias
   - Onboarding de novos desenvolvedores
   - Manutenção do sistema

2. **Implemente melhorias sugeridas**:
   - Refatore código conforme padrões
   - Reorganize estrutura
   - Adicione documentação faltante

3. **Mantenha documentação atualizada**:
   - Atualize quando houver mudanças
   - Revise periodicamente
   - Adicione novos documentos conforme necessário

---

**Última Atualização:** 2025-01-28  
**Versão:** 1.0

