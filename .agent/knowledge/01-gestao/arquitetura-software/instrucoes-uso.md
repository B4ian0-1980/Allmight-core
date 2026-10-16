---json
{
  "id": "instrucoes-uso",
  "title": "📖 Instruções de Uso - Estrutura Base",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "🛑 **ATENÇÃO:** Você está na pasta `0-fonte`. **NÃO** desenvolva aqui. Esta pasta é uma **Bibiloteca de Referência**. Copie os arquivos para outro local antes de começar.",
  "gatilhos": [
    "arquitetura",
    "base",
    "estrutura",
    "gestao",
    "instrucoes",
    "software",
    "uso"
  ],
  "perguntas_tipo": [
    "Como utilizar 📖 Instruções de Uso - Estrutura Base?",
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

# 📖 Instruções de Uso - Estrutura Base

**Versão:** 2.0.0
**Contexto:** Pós-Consolidação (Biblioteca + Docs + Projetos)

---

## 🚀 Como Usar esta Estrutura

> 🛑 **ATENÇÃO:** Você está na pasta `0-fonte`. **NÃO** desenvolva aqui.
> Esta pasta é uma **Bibiloteca de Referência**. Copie os arquivos para outro local antes de começar.

## 🏁 Primeiros Passos

1. **Escolha seu Workspace:**
    * Crie uma pasta fora daqui (ex: `d:\xampp\htdocs\meu-novo-projeto`).
2. **Copie** todo o conteúdo da pasta `0-fonte` para o seu novo workspace.
3. **Mantenha** a estrutura de pastas:
    * `biblioteca/` (Pode ser removida se quiser um repo leve, mas recomendamos manter para consulta offline).
    * `docs/` (Essencial).
    * `servers/` (Onde seus servidores e aplicações viverão).

### 2. Personalização

1. **Renomeie** os exemplos em `servers/` ou apagueos:
    * `servers/meu-app` -> `servers/seu-sistema`.
2. **Atualize** `docs/README.md` com o nome do seu projeto.

### 3. Usando os Templates

Na pasta `docs/gestao/`, você encontrará templates prontos (prefixo `TEMPLATE_`).
Para usá-los:

1. **Duplique** o arquivo (ex: `TEMPLATE_REQUISITOS.md`).
2. **Renomeie** para o nome real (ex: `REQUISITOS_SISTEMA_V1.md`).
3. **Mova** para a pasta adequada (ex: `docs/funcionalidades/`).

---

## 📂 Organização do Código Fonte

Recomendamos fortemente manter o código fonte dentro de `servers/`.

**Por que?**

* Mantém a raiz limpa.
* Permite ter múltiplos serviços (ex: `servers/api-backend`, `servers/app-mobile`) no mesmo repositório (Monorepo).
* Separa claramente "Código" de "Documentação" e "Referência".

---

## 🔄 Fluxo de Trabalho Recomendado

1. **Planejamento:**
    * Crie um documento em `docs/funcionalidades/` descrevendo o que vai fazer.
    * Use `docs/gestao/DIRETRIZES_DESENVOLVIMENTO.md` como guia de qualidade.

2. **Pesquisa:**
    * Consulte `biblioteca/` para documentação teórica.
    * Consulte `biblioteca/exemplos-praticos/` para "Copiar e Colar" inteligente.

3. **Execução:**
    * Codifique em `servers/`.

4. **Registro:**
    * Atualize o `docs/analises/CHANGELOG.md` do seu projeto.

---

## ❓ Dúvidas Comuns

**P: Onde foram parar as pastas `livros` e `referencia`?**
R: Foram movidas para dentro de `biblioteca/` para reduzir a poluição visual na raiz.

**P: Posso criar pastas na raiz?**
R: Evite. Tente encaixar em `docs`, `biblioteca` ou `servers`. Se for configuração de CI/CD (ex: `.github`), tudo bem ficar na raiz.
