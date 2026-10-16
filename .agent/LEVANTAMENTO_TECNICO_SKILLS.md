# 📑 Levantamento Técnico de Referência & Padrões do Ecossistema Antigravity

> **Data de Emissão:** 11/10/2026  
> **Destino:** [`d:/xampp/htdocs/0-fonte/.agent/`](file:///d:/xampp/htdocs/0-fonte/.agent/)  
> **Finalidade:** Servir de especificação técnica e referência para a implementação das melhorias estruturais (`healthcheck.py`, `agent-cli.py` e manifest dinâmico).

---

## 1. 📄 Padrão de `SKILL.md` (3 Casos Reais: READY, PLAYBOOK e BLOCKED)

Todos os arquivos `SKILL.md` do ecossistema seguem o padrão aberto da indústria com frontmatter delimitado por `---`, contendo minimamente os campos `name:` e `description:`.

### Caso A: `READY` (Ferramenta Executável com Código Local)
* **Arquivo:** [`skills/freellmapi/SKILL.md`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/freellmapi/SKILL.md)
* **Natureza:** Possui dependências locais em Node/Python e arquivos executáveis na pasta.

```yaml
---
name: freellmapi
description: "Unified proxy gateway aggregating 34 free LLM providers, 635 free model endpoints, and ~7.4 billion free tokens/month into a single OpenAI-compatible /v1 endpoint with auto-failover, quota tracking, and prompt compression."
---

# FreeLLMAPI Guide

**FreeLLMAPI** aggregates the free tiers of 34 major AI providers (Google AI Studio, Groq, Cerebras, Mistral, OpenRouter, Cloudflare Workers AI, Cohere, NVIDIA NIM, HuggingFace, ModelScope, etc.) into a unified, local OpenAI-compatible endpoint.

## Core Capabilities
- Massive Free Capacity: Access to ~7.4 billion tokens per month and 635 model endpoints across 34 providers at zero cost.
- Unified `/v1` Endpoint: Drop-in replacement for OpenAI API (`/v1/chat/completions`, embeddings, images, audio).
- Intelligent Routing & Failover: Automatically switches to the next provider when rate-limits or 429 errors occur.
- Quota & Key Tracking: Tracks usage per key so you stay under every provider's free-tier limits without paying a cent.
- Prompt Compression Pipeline: Compresses prompts using Caveman/RTK techniques to save token bandwidth.

## How to use this skill
- Point any OpenAI-compatible client, agent, or CLI (Claude Code, Cursor, Copilot, Cline, Aider) to the local FreeLLMAPI endpoint (`http://localhost:PORT/v1`).
- Run via Docker Compose or desktop application.
- Use as the primary AI inference gateway when the user wants zero-cost LLM execution with maximum reliability and redundancy.

## When to recommend
- When the user asks: "How can I run agents with free LLM APIs without hitting rate limits?"
- When setting up multi-agent swarms that require large token throughput without paying API subscriptions.
- As a fallback gateway when primary API keys run out of balance.
```

---

### Caso B: `PLAYBOOK` (Guia Conceitual / Metodologia Pura)
* **Arquivo:** [`skills/claude-red-offensive-jwt/SKILL.md`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/claude-red-offensive-jwt/SKILL.md)
* **Natureza:** Instruções conceituais de engenharia/pentest sem binários ou código local para executar.

```yaml
---
name: offensive-jwt
description: "JWT attack methodology for penetration testers. Covers algorithm confusion (alg:none, RS256→HS256), weak HMAC secret brute force, kid parameter injection (SQLi, path traversal), jku/x5u/jwk header injection, JWKS cache poisoning, JWS/JWE confusion, timing attacks, and mobile JWT storage extraction. Use when testing JWT-based authentication, hunting auth bypass via token manipulation, or evaluating JWT implementation security in web or mobile apps."
---

## Overview
Comprehensive JWT attack checklist for offensive security engagements. Follow steps in order; apply each technique to the current target context and track which items have been completed.

## Quick Reference: Misconfigurations to Check
- Algorithm set to `none` — signature verification bypassed entirely
- Algorithm switching between `RSA` and `HMAC` (confusion attack)
- Weak or guessable HMAC secret (brute-forceable)
- `kid`, `jku`, `jwk`, `x5u` header parameters accepted without validation
- Expired or tampered tokens accepted by server
- Sensitive data stored unencrypted in payload

Useful tool: [JWT Tool](https://github.com/ticarpi/jwt_tool)

## Mechanisms
JWTs (RFC 7519) consist of three Base64URL-encoded parts: `header.payload.signature`.
```

---

### Caso C: `BLOCKED` (Bloqueada por Dependência Externa Ausente no Host)
* **Arquivo:** [`skills/manual-generator/SKILL.md`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/manual-generator/SKILL.md)
* **Natureza:** Depende de compiladores ausentes no Windows (Crystal, C++ build tools, `wkhtmltopdf`).

```yaml
---
name: manual-generator
description: "Guidance for using manual-generator, a Crystal program to generate PDF manuals from HTML documentation sites. Use this skill when asked to scrape an online HTML documentation and convert it into a single, unified PDF file."
---

# Manual Generator Guide

**manual-generator** is a tool written in Crystal that downloads all links found in an HTML table of contents (TOC) and converts them into a single, comprehensive PDF using `wkhtmltopdf-crystal`.

> **Note:** This project is unmaintained upstream, but its core utility remains functional for scraping and converting HTML docs to PDF.

## Core Capabilities
- **HTML to PDF Conversion:** Fetches an entire documentation site by crawling its TOC and bundles it into one PDF document.
- **Custom CSS Support:** Allows injection of custom CSS or removal of specific elements (like navbars) before generating the PDF.
- **CLI Options:** Supports granular CSS selectors for specifying exactly where the TOC is (`-t`) and what part of the page constitutes the content (`-c`).

## How to use this skill
- Use this when the user needs to download an online documentation site as an offline PDF.
- Ensure the `crystal` compiler and `wkhtmltopdf` are installed in the environment to build and run the tool (`crystal build --release src/manual-generator.cr`).

## When to recommend
- When the user asks: "How can I convert this website's documentation into a PDF book?"
- When you need to gather offline documentation for a library or framework and want it in a unified, readable PDF format.
```

> 🎯 **Regra Heurística para o `healthcheck.py`:**
> 1. Se a pasta da skill contiver arquivos executáveis reconhecidos (`package.json`, `generate.py`, `cli.py`, `run.py`, `main.py`) **E** suas ferramentas de execução (`node`, `python`) estiverem disponíveis no Windows $\rightarrow$ **Status: `READY`**.
> 2. Se a pasta contiver apenas documentação Markdown (`SKILL.md`, `references/`) $\rightarrow$ **Status: `PLAYBOOK`**.
> 3. Se o `SKILL.md` ou dependências exigirem compiladores ausentes (`crystal`, `cargo`, `docker`, `go`) $\rightarrow$ **Status: `BLOCKED`**.

---

## 2. 🚦 Conteúdo & Funcionamento de `rules/01_routing.md`

* **Arquivo:** [`rules/01_routing.md`](file:///d:/xampp/htdocs/0-fonte/.agent/rules/01_routing.md)

### Step 1: Matriz Classificadora de Requisições
Antes de qualquer ação, o classificador lê o prompt e determina o nível de tiers ativos:

```markdown
| Request Type     | Trigger Keywords                           | Active Tiers                   | Result                      |
| ---------------- | ------------------------------------------ | ------------------------------ | --------------------------- |
| **QUESTION**     | "what is", "how does", "explain"           | TIER 0 only                    | Text Response               |
| **SURVEY/INTEL** | "analyze", "list files", "overview"        | TIER 0 + Explorer              | Session Intel (No File)     |
| **SIMPLE CODE**  | "fix", "add", "change" (single file)       | TIER 0 + TIER 1 (lite)         | Inline Edit                 |
| **COMPLEX CODE** | "build", "create", "implement", "refactor" | TIER 0 + TIER 1 (full) + Agent | **{task-slug}.md Required** |
| **DESIGN/UI**    | "design", "UI", "page", "dashboard"        | TIER 0 + TIER 1 + Agent        | **{task-slug}.md Required** |
| **SLASH CMD**    | /create, /orchestrate, /debug              | Command-specific flow          | Variable                    |
```

### Step 2: Protocolo de Auto-Seleção do Agente
1. **Análise Silenciosa:** Detecta o domínio (Frontend, Backend, Segurança, Banco de Dados, etc.).
2. **Seleção do Especialista:** Escolhe a persona em `agents/{agent}.md`.
3. **Anúncio Obrigatório:**  
   `🤖 **Applying knowledge of `@[agent-name]`...**`
4. **Agent Routing Checklist:** O modelo deve ler as `skills:` indicadas no frontmatter do agente antes de escrever código.

---

## 3. 📂 Estrutura de Pastas de Skills Executáveis (Para o `agent-cli.py`)

### Exemplo 1: `freellmapi/` (Arquitetura Monorepo Node / Fastify + React)
* **Localização:** [`skills/freellmapi/`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/freellmapi/)

```plaintext
skills/freellmapi/
├── package.json           <-- Define "dev", "build", "test"
├── docker-compose.yml     <-- Configuração de subida em container
├── .env.example           <-- Exige PORT=3001 e ENCRYPTION_KEY
├── server/                <-- Entrypoint Fastify / Express (/v1/chat/completions)
├── client/                <-- Frontend React (página de Keys e Fallback)
├── cli/                   <-- Utilitário de linha de comando nativo
└── SKILL.md
```
* **Comando padrão de despacho:** `npm run dev` (executa servidor + cliente simultaneamente).

### Exemplo 2: `media-inference-worker/` (Script Python Direto)
* **Localização:** [`skills/media-inference-worker/`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/media-inference-worker/)

```plaintext
skills/media-inference-worker/
├── generate.py            <-- Entrypoint Python (aceita: <model> "<prompt>")
├── requirements.txt       <-- Dependências (requests)
├── .env                   <-- Chaves da API Higgsfield (HF_API_KEY_ID)
├── RUNBOOK.md             <-- Tabela de endpoints e modelos suportados
└── SKILL.md
```
* **Comando padrão de despacho:** `python generate.py <model> "<prompt>"`.

---

## 4. 🌐 Arquitetura Atual de `painel_sistema.html`

* **Arquivo:** [`painel_sistema.html`](file:///d:/xampp/htdocs/0-fonte/.agent/painel_sistema.html)

### Como Ele Opera Hoje:
1. **Estrutura 100% Embutida (Self-Contained):**
   * Não realiza chamadas assíncronas `fetch()` para arquivos externos.
   * Todos os 103 cards de skills, 21 agentes e 17 workflows são elementos `<a class="card">` gravados diretamente no arquivo.
2. **Filtragem e Busca via DOM:**
   * O script no final escuta o evento `input` do campo `#searchInput` e o evento `click` das abas `.tab-btn`.
   * Alterna a visibilidade dos cards entre `display: flex` e `display: none` em memória.
3. **Plano de Evolução para o Manifest Dinâmico (P1 / P2):**
   * Em vez de o HTML ter 2.400 linhas estáticas, ele pode carregar dinamicamente um arquivo leve `skills_manifest.json` gerado pelo `healthcheck.py`, renderizando os cards em tempo real com indicador visual de status:
     * 🟢 `READY`
     * 📘 `PLAYBOOK`
     * 🔴 `BLOCKED`
