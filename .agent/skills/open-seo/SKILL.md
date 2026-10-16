---
name: open-seo
description: Open-source Semrush and Ahrefs alternative with native MCP server and Agent Skills for keyword research, backlink analysis, competitor intelligence, and programmatic SEO.
---

# 🚀 OpenSEO — Open Source SEO & MCP Intelligence Suite

> **Baseado em:** [`every-app/open-seo`](https://github.com/every-app/open-seo)  
> **Filosofia:** *All-in-one SEO tool for you and your AI agent.*

---

## 🎯 Objetivo

Fornecer capacidade analítica e operacional de SEO de nível corporativo sem assinaturas abusivas. O **OpenSEO** combina:
1. **Interface Moderna:** Workflows focados em pesquisa de palavras-chave, ranking e backlinks.
2. **Servidor MCP Nativo:** Permite que agentes de IA (Claude Code, Antigravity, OpenClaw) consultem métricas de busca, concorrentes e volume de busca diretamente como ferramentas (`tools`).
3. **Pay-as-you-go:** Suporte a chaves de provedores de dados (como DataForSEO) ou auditorias locais de páginas.

---

## 🔍 Os 6 Workflows de SEO do OpenSEO

```plaintext
                              WORKFLOWS OPENSEO
                                      │
     ┌──────────────────────┬─────────┴─────────┬──────────────────────┐
     ▼                      ▼                   ▼                      ▼
[ KEYWORD RESEARCH ]   [ RANK TRACKING ]   [ COMPETITOR INSIGHTS ] [ SITE AUDIT ]
• Volume de busca      • Posição na SERP   • Domínios rivais       • Tags canônicas
• Dificuldade (KD)     • Flutuações diárias• Palavras compartilhadas• Core Web Vitals
• Intenção de busca    • Rich snippets     • Análise de lacunas    • 404 / Redirects
```

### 1. Keyword Research (Pesquisa de Palavras-Chave)
* Identificação de palavras-chave primárias e de cauda longa (*long-tail*).
* Análise de intenção de busca (informacional, transacional, navegacional).
* Agrupamento semântico (*topic clusters*) para arquitetura de conteúdo.

### 2. Site Audit & Technical SEO (Auditoria Técnica)
* Verificação de títulos `<title>`, meta descriptions e hierarquia `<h1>` a `<h6>`.
* Auditoria de links quebrados (404), redirecionamentos em cadeia e status HTTP.
* Validação de tags `canonical`, `robots.txt`, `sitemap.xml` e meta tags `OpenGraph / Twitter Card`.

### 3. Competitor Gap Analysis (Inteligência Competitiva)
* Mapeamento de quais tópicos os principais concorrentes dominam.
* Descoberta de palavras-chave de baixa concorrência e alta oportunidade.

### 4. AI Visibility & GEO (Generative Engine Optimization)
* Monitoramento de como mecanismos generativos (Perplexity, ChatGPT, Claude) citam sua marca ou domínio.

---

## 🛠️ Comandos e Scripts Locais

### Script de Auditoria Técnica Rápida
Execute a auditoria técnica de SEO em qualquer URL ou arquivo HTML local:
```bash
python .agent/skills/open-seo/scripts/seo_audit_cli.py https://seu-site.com
# ou em arquivo local:
python .agent/skills/open-seo/scripts/seo_audit_cli.py caminho/para/pagina.html
```

### Protocolo de Integração com o Agente
Quando encarregado de criar ou revisar uma página web:
1. Validar unicidade do `<h1>` por documento.
2. Garantir meta description entre 120 e 160 caracteres com chamada para ação (CTA).
3. Verificar marcação de dados estruturados JSON-LD (`schema.org`).
4. Evitar canibalização de palavras-chave entre rotas vizinhas.
