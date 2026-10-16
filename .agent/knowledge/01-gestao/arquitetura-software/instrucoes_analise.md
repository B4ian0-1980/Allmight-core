---json
{
  "id": "instrucoes_analise",
  "title": "🔍 Instruções para Análise e Classificação",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🔍 Instruções para Análise e Classificação.",
  "gatilhos": [
    "analise",
    "arquitetura",
    "gestao",
    "instrucoes",
    "para",
    "software"
  ],
  "perguntas_tipo": [
    "Como utilizar 🔍 Instruções para Análise e Classificação?",
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

# 🔍 Instruções para Análise e Classificação

**Data:** 2025-01-27  
**Versão:** 1.0

---

## 🎯 Objetivo

Este documento explica como solicitar análise e classificação de novos conteúdos usando IA.

---

## 📋 Fluxo de Trabalho

### 0. Converta PDFs (Opcional mas Recomendado)

**Se tiver PDFs, converta para Markdown primeiro:**

```bash
# Use o script de conversão
python _a-classificar/scripts/pdf-to-md.py _a-classificar/[subpasta]/

# Exemplo:
python _a-classificar/scripts/pdf-to-md.py _a-classificar/livros/*.pdf
```

**Vantagens da conversão:**
- ✅ IA lê mais rápido
- ✅ Análise mais profunda
- ✅ Extração mais precisa
- ✅ Pode buscar trechos específicos

**Veja:** `scripts/README.md` para instruções detalhadas

---

### 1. Prepare o Conteúdo

**Crie as subpastas necessárias** e organize seus arquivos:

```bash
# Exemplo: Nova tecnologia
mkdir -p _a-classificar/tecnologias/vuejs-3/{docs,livros,exemplos}

# Exemplo: Livros novos
mkdir -p _a-classificar/livros

# Exemplo: Documentação
50: mkdir -p _a-classificar/referencias/nextjs-14
51: ```
52: 
53: **Estrutura resultante:**
54: 
55: ```
56: _a-classificar/
57: ├── tecnologias/
58: │   └── [nome-tecnologia]/
59: │       ├── docs/
60: │       ├── livros/
61: │       ├── exemplos/
62: │       └── SOLICITACAO_INFORMACOES.md (opcional)
63: ```

---

### 2. Solicite Análise com Relatório

**Para análise por IA, use este formato:**

```
Tenho novos conteúdos em @base-estrutura-projeto/_a-classificar/[subpasta]

[Descreva brevemente o que é]

Por favor:
1. Analise cada arquivo (leia os .md se disponíveis)
2. Gere relatório usando @base-estrutura-projeto/_a-classificar/TEMPLATE_RELATORIO_ANALISE.md
3. Classifique:
   - É atual? Relevante? Útil?
   - Onde deve ir na estrutura?
   - O que extrair?
4. Integre na estrutura principal
5. Mantenha PDFs originais nos locais apropriados
6. Limpe _a-classificar/
```

**📊 A IA gerará:**
- Relatório completo de análise
- Decisão de classificação
- Plano de ação
- Integração automática

---

## 📚 Exemplos de Solicitações

### Exemplo 1: Nova Tecnologia

```
Tenho documentação de Vue.js 3 em 
@base-estrutura-projeto/_a-classificar/tecnologias/vuejs-3/

Conteúdo:
- Documentação oficial completa
- 2 livros sobre Vue.js
- Projeto exemplo

Por favor:
1. Analise o material
2. Extraia padrões e exemplos
3. Crie PADROES_VUEJS3.md
4. Sugira onde colocar cada material
```

---

### Exemplo 2: Livros Novos

```
Baixei 5 livros novos em 
@base-estrutura-projeto/_a-classificar/livros/

Por favor:
1. Analise cada livro (ano, relevância, tecnologia)
2. Sugira classificação:
   - Úteis → onde colocar (laravel/, react/, etc.)
   - Obsoletos → sugerir remoção
3. Se tiver conteúdo valioso, extraia para docs/
```

---

### Exemplo 3: Documentação de Framework

```
Tenho docs do Next.js 14 em 
@base-estrutura-projeto/_a-classificar/referencias/nextjs-14/

Por favor:
1. Analise a documentação
2. Extraia exemplos práticos
3. Crie documento de padrões
4. Integre em docs/01-arquitetura/
```

---

## 🤖 O que a IA Fará

### Análise Automática Completa

1. **Leitura do Conteúdo**
   - Lê arquivos .md (se PDFs convertidos)
   - Identifica tipo de material
   - Verifica relevância e atualidade
   - Avalia qualidade

2. **Geração de Relatório**
   - Usa template TEMPLATE_RELATORIO_ANALISE.md
   - Documenta tudo que foi encontrado
   - Justifica decisões
   - Compara com material existente

3. **Extração de Informações**
   - Padrões de código
   - Exemplos práticos
   - Conceitos importantes
   - Boas práticas

4. **Decisão de Classificação**
   - MANTER E INTEGRAR
   - MANTER COMO REFERÊNCIA
   - EXTRAIR E DESCARTAR
   - DESCARTAR

5. **Integração na Estrutura**
   - Cria documentos apropriados
   - Move/copia arquivos para locais corretos
   - Extrai conteúdo valioso para docs/
   - Atualiza índices
   - Remove da pasta de staging

6. **Documentação**
   - Salva relatório de análise
   - Atualiza CONTEUDO_INCLUIDO.md
   - Atualiza INDICE_GERAL.md

---

## ✅ Checklist para Solicitação

Antes de solicitar análise:

- [ ] Conteúdo está em subpasta apropriada de `_a-classificar/`
- [ ] Arquivos estão organizados
- [ ] Se tecnologia nova, considere usar template SOLICITACAO_INFORMACOES.md
- [ ] Descreveu brevemente o que é o conteúdo
- [ ] Especificou o que precisa (análise, extração, integração)

---

## 📊 Após a Análise

A IA irá:

1. **Criar documentos** na estrutura principal
2. **Mover arquivos** para locais apropriados
3. **Atualizar índices** (INDICE_GERAL.md, CONTEUDO_INCLUIDO.md)
4. **Limpar staging** (remover de `_a-classificar/`)
5. **Fornecer resumo** do que foi feito

---

## 🎯 Templates de Solicitação

### Template: Análise de Livros

```markdown
# Análise de Livros

**Localização:** @base-estrutura-projeto/_a-classificar/livros/

**Livros:**
1. [Título 1] - [Autor] - [Ano]
2. [Título 2] - [Autor] - [Ano]
3. [Título 3] - [Autor] - [Ano]

**Solicitação:**
Por favor analise cada livro e sugira:
- Se deve ser mantido ou removido (obsoleto?)
- Categoria apropriada (laravel/, react/, banco-dados/, etc.)
- Se tem conteúdo valioso para extrair para docs/

**Critérios:**
- Tecnologias obsoletas (>5 anos) → Remover
- Conceitos fundamentais → Extrair para docs/
- Versões antigas de frameworks → Avaliar relevância
```

---

### Template: Nova Tecnologia

```markdown
# Solicitação: Nova Tecnologia

**Localização:** @base-estrutura-projeto/_a-classificar/tecnologias/[nome]/

**Tecnologia:** [Nome e versão]
**Motivo:** [Por que preciso desta tecnologia]

**Materiais Disponíveis:**
- [ ] Documentação oficial
- [ ] Livros
- [ ] Exemplos de código
- [ ] Tutoriais

**Solicitação:**
Por favor:
1. Analise os materiais
2. Extraia padrões e boas práticas
3. Crie documentação em docs/01-arquitetura/
4. Sugira exemplos para docs/07-exemplos-por-dominio/
5. Integre na estrutura principal

**Prioridade:** [Alta/Média/Baixa]
**Deadline:** [Data, se houver]
```

---

### Template: Documentação de Framework

```markdown
# Análise: Documentação de Framework

**Localização:** @base-estrutura-projeto/_a-classificar/referencias/[framework]/

**Framework:** [Nome e versão]
**Tipo:** [Backend/Frontend/Banco/etc]

**Conteúdo:**
- [Descreva o que está incluído]

**Solicitação:**
Por favor:
1. Analise a documentação
2. Extraia exemplos práticos importantes
3. Crie PADROES_[FRAMEWORK].md em docs/01-arquitetura/
4. Mova documentação para referencia/[framework]/
5. Atualize índices

**Integração com Stack Atual:**
[Descreva como este framework se integra com o stack existente]
```

---

## 💡 Dicas

### Para Melhor Análise

1. **Organize bem** - Quanto mais organizado, melhor a análise
2. **Descreva contexto** - Explique por que precisa do material
3. **Seja específico** - Diga exatamente o que precisa
4. **Priorize** - Indique o que é mais importante

### Para Nova Tecnologia

1. **Use o template** SOLICITACAO_INFORMACOES.md
2. **Reúna materiais completos** antes de solicitar
3. **Explique uso pretendido** no projeto

### Para Livros

1. **Liste todos** antes de solicitar análise
2. **Inclua metadados** (título, autor, ano)
3. **Mencione se já leu** ou conhece o conteúdo

---

## 🔄 Manutenção

### Esta Pasta Deve Estar Vazia Após Análise

- ✅ Análise concluída → Pasta vazia
- ✅ Conteúdo integrado → Staging limpo
- ✅ Pronto para próxima análise

### Não Acumule Conteúdo

- ⚠️ Classifique regularmente
- ⚠️ Não deixe materiais antigos
- ⚠️ Mantenha organizado

---

## 📝 Exemplo Completo

### Situação: Baixei 3 Livros Laravel

**1. Crie a pasta e organize:**
```bash
# Criar pasta
mkdir _a-classificar/livros

# Copiar livros para lá
cp ~/Downloads/*.pdf _a-classificar/livros/
```

**Estrutura:**
```
_a-classificar/livros/
├── Laravel - From Apprentice to Artisan (2023).pdf
├── Laravel Up and Running (2022).pdf
└── Laravel Testing Decoded (2019).pdf
```

**2. Solicite:**
```
Tenho 3 livros Laravel em @base-estrutura-projeto/_a-classificar/livros/

1. Laravel - From Apprentice to Artisan (2023)
2. Laravel Up and Running (2022)
3. Laravel Testing Decoded (2019)

Por favor:
1. Analise se são atuais e relevantes
2. Sugira classificação (manter/remover)
3. Se tiverem conteúdo útil, extraia para docs/01-arquitetura/
4. Indique onde colocar os que forem mantidos
```

**3. IA Analisa e Responde:**
```
Análise concluída:

1. Laravel - From Apprentice to Artisan (2023)
   ✅ Manter - Atual e relevante
   📁 Mover para: livros/laravel/
   📝 Extraído: Padrões de design em PADROES_CODIGO_LARAVEL.md

2. Laravel Up and Running (2022)
   ✅ Manter - Excelente referência
   📁 Mover para: livros/laravel/
   📝 Extraído: Exemplos práticos

3. Laravel Testing Decoded (2019)
   ⚠️ Avaliar - Conceitos ainda válidos, mas alguns exemplos desatualizados
   📁 Mover para: livros/laravel/
   📝 Extraído: Estratégias de teste para docs/03-sdlc/

Ações realizadas:
- ✅ Livros movidos para livros/laravel/
- ✅ Criado EXEMPLOS_TESTES_LARAVEL.md
- ✅ Atualizado INDICE_GERAL.md
- ✅ Staging limpo
```

---

**Última Atualização:** 2025-01-27  
**Versão:** 1.0

