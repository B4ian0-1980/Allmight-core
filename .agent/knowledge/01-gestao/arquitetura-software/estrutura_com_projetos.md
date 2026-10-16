---json
{
  "id": "estrutura_com_projetos",
  "title": "🏗️ Como Usar a Base com Seus Projetos",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🏗️ Como Usar a Base com Seus Projetos.",
  "gatilhos": [
    "arquitetura",
    "base",
    "com",
    "como",
    "estrutura",
    "gestao",
    "projetos",
    "seus"
  ],
  "perguntas_tipo": [
    "Como utilizar 🏗️ Como Usar a Base com Seus Projetos?",
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

# 🏗️ Como Usar a Base com Seus Projetos

**Versão:** 1.0  
**Data:** 2025-01-27

---

## 🎯 Objetivo

Este documento explica como manter a **estrutura base genérica** enquanto adiciona seus projetos específicos.

---

## 📁 Estrutura Recomendada

```
workspace/
│
├── base-estrutura-projeto/       # ← BASE GENÉRICA (NUNCA MODIFIQUE)
│   ├── docs/
│   ├── livros/
│   ├── referencia/
│   ├── extras/
│   ├── _a-classificar/          # ← Vazia (use quando precisar analisar conteúdo)
│   └── README.md
│
└── sistema/                      # ← SEUS PROJETOS (CRIE ESTA PASTA)
    ├── [nome-projeto-1]/
    │   ├── src/
    │   ├── docs/
    │   └── README.md
    │
    ├── [nome-projeto-2]/
    │   ├── src/
    │   ├── docs/
    │   └── README.md
    │
    └── [nome-projeto-3]/
        ├── src/
        ├── docs/
        └── README.md
```

---

## 🔑 Regra de Ouro

### ✅ SEMPRE MANTENHA SEPARADO:

- **`base-estrutura-projeto/`** → Conhecimento genérico e reutilizável
- **`sistema/`** → Projetos específicos e suas particularidades

---

## 📋 Por Que Esta Separação?

### Problema Sem Separação:

```
❌ workspace/
   ├── docs/                    # Mistura genérico com específico
   ├── livros/                  # Mistura genérico com específico
   └── meu-projeto/             # Projeto específico
       └── src/
```

**Problemas:**
- ❌ Perde valor genérico da base
- ❌ Difícil reutilizar em novo projeto
- ❌ Mistura documentação genérica com específica
- ❌ Não consegue copiar base para novo projeto

---

### Solução Com Separação:

```
✅ workspace/
   ├── base-estrutura-projeto/  # Genérico - Reutilizável
   │   ├── docs/
   │   ├── livros/
   │   └── referencia/
   │
   └── sistema/                  # Específico - Por projeto
       ├── projeto-a/
       ├── projeto-b/
       └── projeto-c/
```

**Benefícios:**
- ✅ Base permanece genérica
- ✅ Fácil reutilizar em novo workspace
- ✅ Cada projeto tem sua documentação
- ✅ Pode evoluir base independente dos projetos

---

## 🚀 Como Iniciar

### Passo 1: Setup Inicial

```bash
# Crie workspace principal
mkdir meu-workspace
cd meu-workspace

# Clone/copie a base genérica
cp -r /caminho/para/base-estrutura-projeto .

# Crie pasta para seus projetos
mkdir sistema
```

### Passo 2: Crie Seu Primeiro Projeto

```bash
cd sistema

# Para projeto Laravel + React
mkdir meu-projeto
cd meu-projeto

# Inicialize projeto
composer create-project laravel/laravel .
npm install

# Crie estrutura de docs
mkdir docs
touch docs/README.md
```

### Passo 3: Configure Referências

Dentro de cada projeto, referencie a base:

**`sistema/meu-projeto/docs/README.md`:**

```markdown
# Documentação - Meu Projeto

## 📚 Referências

Para padrões e exemplos genéricos, consulte:
- **Base:** `../../base-estrutura-projeto/`
- **Padrões Laravel:** `../../base-estrutura-projeto/docs/01-arquitetura/PADROES_CODIGO_LARAVEL.md`
- **Padrões React:** `../../base-estrutura-projeto/docs/01-arquitetura/PADROES_REACT19.md`
- **Exemplos do domínio:** `../../base-estrutura-projeto/docs/07-exemplos-por-dominio/[seu-dominio]/`

## 📖 Documentação Específica

- [Requisitos](./REQUISITOS.md)
- [Arquitetura](./ARQUITETURA.md)
- [API](./API.md)
```

---

## 📁 Estrutura Detalhada de Projeto

### Estrutura Completa Recomendada:

```
sistema/
└── [nome-projeto]/
    ├── src/                      # Código fonte
    │   ├── app/
    │   ├── resources/
    │   └── ...
    │
    ├── docs/                     # Documentação ESPECÍFICA do projeto
    │   ├── README.md
    │   ├── 00-projeto/           # Informações do projeto
    │   │   ├── REQUISITOS_PROJETO.md
    │   │   ├── VISAO_GERAL.md
    │   │   └── GLOSSARIO_NEGOCIO.md
    │   │
    │   ├── 01-arquitetura/       # Arquitetura ESPECÍFICA
    │   │   ├── DECISOES_ARQUITETURA.md
    │   │   ├── DIAGRAMAS.md
    │   │   └── INTEGRACAO_SERVICOS.md
    │   │
    │   ├── 02-desenvolvimento/   # Guias de desenvolvimento
    │   │   ├── SETUP_LOCAL.md
    │   │   ├── WORKFLOWS.md
    │   │   └── TROUBLESHOOTING.md
    │   │
    │   └── 03-deploy/            # Deploy e produção
    │       ├── AMBIENTES.md
    │       ├── CI_CD.md
    │       └── MONITORAMENTO.md
    │
    ├── tests/                    # Testes
    ├── database/                 # Migrations, seeds
    ├── public/                   # Assets públicos
    ├── storage/                  # Storage local
    ├── .env.example
    ├── composer.json
    ├── package.json
    └── README.md
```

---

## 🔄 Fluxo de Trabalho

### Durante Desenvolvimento

1. **Consulte a base genérica:**
   ```
   ../../base-estrutura-projeto/docs/01-arquitetura/
   ```

2. **Documente especificidades:**
   ```
   ./docs/00-projeto/
   ```

3. **Use exemplos do domínio:**
   ```
   ../../base-estrutura-projeto/docs/07-exemplos-por-dominio/
   ```

### Quando Criar Novo Projeto

1. **Crie nova pasta em `sistema/`:**
   ```bash
   mkdir sistema/novo-projeto
   ```

2. **Copie estrutura base se necessário:**
   ```bash
   cp -r base-estrutura-projeto/docs/00-base/TEMPLATE_* sistema/novo-projeto/docs/
   ```

3. **Personalize para o novo projeto**

4. **Referencie a base para padrões genéricos**

---

## 📊 Exemplo Prático

### Workspace Real:

```
minha-software-house/
│
├── base-estrutura-projeto/         # Base genérica
│   ├── docs/
│   │   ├── 01-arquitetura/
│   │   │   ├── PADROES_CODIGO_LARAVEL.md
│   │   │   └── PADROES_REACT19.md
│   │   └── 07-exemplos-por-dominio/
│   │       ├── medico/
│   │       ├── ecommerce/
│   │       └── financeiro/
│   └── livros/
│
└── sistema/                        # Projetos específicos
    ├── clinica-saude/              # Projeto 1: Sistema médico
    │   ├── src/
    │   ├── docs/
    │   │   ├── 00-projeto/
    │   │   │   └── REQUISITOS_CLINICA.md
    │   │   └── README.md (referencia base-estrutura-projeto/docs/07-exemplos-por-dominio/medico/)
    │   └── README.md
    │
    ├── loja-virtual/               # Projeto 2: E-commerce
    │   ├── src/
    │   ├── docs/
    │   │   ├── 00-projeto/
    │   │   │   └── REQUISITOS_LOJA.md
    │   │   └── README.md (referencia base-estrutura-projeto/docs/07-exemplos-por-dominio/ecommerce/)
    │   └── README.md
    │
    └── banco-digital/              # Projeto 3: Sistema financeiro
        ├── src/
        ├── docs/
        │   ├── 00-projeto/
        │   │   └── REQUISITOS_BANCO.md
        │   └── README.md (referencia base-estrutura-projeto/docs/07-exemplos-por-dominio/financeiro/)
        └── README.md
```

---

## 🎯 Vantagens Desta Abordagem

### 1. Base Permanece Genérica

✅ Pode ser copiada para novos workspaces
✅ Pode ser compartilhada entre times
✅ Pode evoluir independentemente

### 2. Projetos Mantêm Especificidades

✅ Cada projeto tem sua documentação
✅ Requisitos específicos documentados
✅ Não poluem a base genérica

### 3. Reutilização Máxima

✅ Padrões genéricos na base
✅ Exemplos de domínio na base
✅ Cada projeto referencia o que precisa

### 4. Escalabilidade

✅ Fácil adicionar novos projetos
✅ Fácil adicionar novos domínios na base
✅ Cada parte evolui no seu ritmo

---

## ⚠️ Erros Comuns a Evitar

### ❌ Erro 1: Modificar a Base com Código Específico

```
❌ base-estrutura-projeto/
   └── docs/
       └── 01-arquitetura/
           └── CODIGO_DO_MEU_PROJETO.md  # ERRADO!
```

**Correto:**
```
✅ sistema/
   └── meu-projeto/
       └── docs/
           └── CODIGO_DO_MEU_PROJETO.md  # CERTO!
```

---

### ❌ Erro 2: Misturar Projetos na Raiz

```
❌ workspace/
   ├── base-estrutura-projeto/
   ├── projeto-a/              # ERRADO - Na raiz
   └── projeto-b/              # ERRADO - Na raiz
```

**Correto:**
```
✅ workspace/
   ├── base-estrutura-projeto/
   └── sistema/                # CERTO - Dentro de sistema/
       ├── projeto-a/
       └── projeto-b/
```

---

### ❌ Erro 3: Duplicar Base em Cada Projeto

```
❌ sistema/
   ├── projeto-a/
   │   └── base-estrutura-projeto/  # ERRADO - Duplicado
   └── projeto-b/
       └── base-estrutura-projeto/  # ERRADO - Duplicado
```

**Correto:**
```
✅ workspace/
   ├── base-estrutura-projeto/      # CERTO - Uma única base
   └── sistema/
       ├── projeto-a/               # Referencia a base
       └── projeto-b/               # Referencia a base
```

---

## 🔄 Mantendo Ambos Atualizados

### Atualizar Base Genérica

```bash
cd base-estrutura-projeto
git pull  # Se for repositório Git
# ou
# Copiar nova versão da base
```

**Quando atualizar:**
- Novos padrões genéricos
- Novos exemplos de domínio
- Novos livros/referências
- Melhorias na estrutura

---

### Atualizar Projetos

```bash
cd sistema/[nome-projeto]
git pull  # Git do projeto específico
```

**Quando atualizar:**
- Mudanças no código do projeto
- Documentação específica
- Requisitos do cliente
- Deploy e configuração

---

## 📝 Template de README do Projeto

**`sistema/[nome-projeto]/README.md`:**

```markdown
# [Nome do Projeto]

**Versão:** 1.0.0  
**Cliente:** [Nome do Cliente]  
**Domínio:** [Médico/E-commerce/Financeiro/Outro]

---

## 📚 Referências da Base

Este projeto utiliza a estrutura base genérica localizada em:

```
../../base-estrutura-projeto/
```

### Consulte:

- **Padrões de Código:** `../../base-estrutura-projeto/docs/01-arquitetura/`
- **Exemplos do Domínio:** `../../base-estrutura-projeto/docs/07-exemplos-por-dominio/[seu-dominio]/`
- **Livros Técnicos:** `../../base-estrutura-projeto/livros/`
- **Referências:** `../../base-estrutura-projeto/referencia/`

---

## 📖 Documentação Específica

- [Requisitos](./docs/00-projeto/REQUISITOS_PROJETO.md)
- [Arquitetura](./docs/01-arquitetura/DECISOES_ARQUITETURA.md)
- [Setup Local](./docs/02-desenvolvimento/SETUP_LOCAL.md)
- [Deploy](./docs/03-deploy/AMBIENTES.md)

---

## 🚀 Quick Start

[Instruções específicas do projeto]
```

---

## ✅ Checklist de Setup

Ao criar novo workspace:

- [ ] Copiar `base-estrutura-projeto/` para o workspace
- [ ] Criar pasta `sistema/`
- [ ] Adicionar `.gitignore` apropriado
- [ ] Cada projeto em `sistema/` tem seu próprio repositório Git
- [ ] Base pode ter seu próprio repositório (opcional)
- [ ] READMEs dos projetos referenciam a base

---

## 🎓 Resumo

1. **Base genérica** = `base-estrutura-projeto/`
   - Padrões, exemplos, livros, referências
   - NUNCA modificar com código específico
   - Reutilizável em qualquer workspace

2. **Projetos específicos** = `sistema/[nome-projeto]/`
   - Código fonte
   - Documentação específica
   - Requisitos do cliente
   - Configurações de deploy

3. **Separação clara** = Máxima reutilização

---

**Última Atualização:** 2025-01-27  
**Versão:** 1.0

