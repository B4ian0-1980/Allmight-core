# 🗺️ Guia Mestre: Quando Usar Cada Skill do Sistema

> **Ecossistema:** Antigravity / AllMight Core  
> **Total de Habilidades Catalogadas:** 191 Skills em [`.agent/skills`](file:///d:/xampp/htdocs/0-fonte/.agent/skills)  
> **Como o sistema decide:** As skills são ativadas sob demanda (Progressive Disclosure) quando a intenção do usuário ou palavras-chave no prompt coincidem com o campo `description` do arquivo `SKILL.md` de cada pasta.

---

## 🧭 Sumário das Categorias

1. [🏗️ 1. Arquitetura, Código & Engenharia Limpa](#1-arquitetura-código--engenharia-limpa)
2. [🐞 2. Testes, Depuração & Qualidade](#2-testes-depuração--qualidade)
3. [🎨 3. Frontend, UI/UX & Design](#3-frontend-uiux--design)
4. [🛡️ 4. Segurança, Auditoria & Pentest](#4-segurança-auditoria--pentest)
5. [🧠 5. Modelos de IA, LLMs & Multi-Agentes](#5-modelos-de-ia-llms--multi-agentes)
6. [💼 6. Startup, Produto & Negócios](#6-startup-produto--negócios)
7. [📣 7. Marketing, Copywriting & Vendas](#7-marketing-copywriting--vendas)
8. [⚙️ 8. Infraestrutura, DevOps & Terminal](#8-infraestrutura-devops--terminal)

---

## 1. 🏗️ Arquitetura, Código & Engenharia Limpa

Use estas skills ao desenhar sistemas, criar novos módulos, refatorar ou definir limites entre serviços:

| Skill | Quando Usar / Gatilho |
| :--- | :--- |
| **`app-builder`** | Criar aplicações full-stack completas a partir de comandos em linguagem natural. |
| **`architecture-design`** | Definir limites de microsserviços, contratos de API e modelos de dados antes de codificar. |
| **`api-patterns`** | Escolher entre REST, GraphQL ou tRPC; definir paginação, versionamento e status codes. |
| **`database-design`** | Projetar schemas de banco relacional/NoSQL, estratégias de índices e escolhas de ORM. |
| **`clean-code`** | Escrever código enxuto, sem duplicações, conciso e com comentários estritamente necessários. |
| **`coding-discipline`** | Aplicar regras de Karpathy: mudanças cirúrgicas e foco radical na meta sem introduzir bloat. |
| **`ponytail`** | Modo "Senior Dev Preguiçoso": a menor alteração que resolve 100% o problema com zero over-engineering. |
| **`nodejs-best-practices`** | Desenvolver backends Node.js, gerenciar concorrência assíncrona e arquitetura de pastas. |
| **`python-patterns`** | Padrões idiomáticos de Python (type hints, assincronismo, geradores e pacotes). |
| **`rust-pro`** | Desenvolvimento de alta performance em Rust (Tokio, Axum, ownership e concorrência segura). |
| **`drawdb`** | Gerar diagramas entidade-relacionamento (ERD) e exportar schemas SQL compatíveis. |

---

## 2. 🐞 Testes, Depuração & Qualidade

Use para caçar bugs, validar tipagem ou assegurar que nenhuma regressão foi introduzida:

| Skill | Quando Usar / Gatilho |
| :--- | :--- |
| **`systematic-debugging`** | Protocolo de 4 fases para investigar bugs difíceis isolando a causa raiz com evidências. |
| **`fast-check`** | Rodar linters e checagem de tipos sem poluir a janela de contexto da IA com logs enormes. |
| **`tdd-workflow`** | Ciclo Red-Green-Refactor: escrever os testes que falham antes de escrever o código. |
| **`testing-patterns`** | Estratégias de testes unitários, mocks cirúrgicos nas bordas e testes de integração. |
| **`webapp-testing`** | Estruturação de suítes de testes End-to-End para aplicações web completas. |
| **`playwright-cli`** | Automação e navegação headless token-efficient para testar fluxos no navegador via CLI. |
| **`performance-profiling`** | Identificar gargalos de CPU, memória, queries lentas e loops bloqueantes. |
| **`code-review`** | Analisar PRs ou diffs locais com olhar de Senior Staff Engineer. |

---

## 3. 🎨 Frontend, UI/UX & Design

Use para criar interfaces que impressionem, seguir design systems e garantir acessibilidade:

| Skill | Quando Usar / Gatilho |
| :--- | :--- |
| **`frontend-design`** | Planejar layouts, harmonias de cores e tipografia profissional antes de gerar CSS. |
| **`taste-skill`** | Framework anti-slop: elimina componentes genéricos e boilerplate sem personalidade. |
| **`laws-of-ux`** | Aplicar psicologia cognitiva (Leis de Fitts, Hick, Miller) para navegação fluida. |
| **`web-design-guidelines`** | Auditar contraste, touch targets e acessibilidade segundo diretrizes WCAG. |
| **`tailwind-patterns`** | Padrões modernos de Tailwind CSS v4, container queries e arquitetura de design tokens. |
| **`react-best-practices`** | Otimizações de renderização, Server Components (RSC) e eliminação de waterfalls. |
| **`awesome-design-md`** | Consultar tokens e estilos das 73+ maiores empresas de tecnologia (Stripe, Linear, Raycast). |
| **`image-to-code`** | Converter mockups de design, capturas de tela ou wireframes em código HTML/React. |

---

## 4. 🛡️ Segurança, Auditoria & Pentest

Use para avaliar postura defensiva, detectar vulnerabilidades ou executar testes de intrusão éticos:

| Skill | Quando Usar / Gatilho |
| :--- | :--- |
| **`security-audit`** | Auditoria estática de código procurando brechas conhecidas (OWASP Top 10). |
| **`security-review`** | Modelagem de ameaças e revisão de arquitetura de autenticação/tokens. |
| **`vulnerability-scanner`** | Varredura de superfície de ataque e dependências vulneráveis da cadeia de suprimentos. |
| **`red-team-tactics`** | Simulação de táticas de adversários reais baseadas no framework MITRE ATT&CK. |
| **`offensive-ssti`** | Testar e mitigar Server-Side Template Injection (Jinja2, Twig, Blade, EJS). |
| **`soc2-prep`** | Preparar controles de compliance, criptografia e políticas de auditoria para certificação SOC 2. |

---

## 5. 🧠 Modelos de IA, LLMs & Multi-Agentes

Use ao trabalhar com agentes autônomos, chamadas de LLM, memória ou fine-tuning:

| Skill | Quando Usar / Gatilho |
| :--- | :--- |
| **`ruflo`** | Orquestrar swarms multi-agente com coordenação hierárquica e controle de memória. |
| **`parallel-agents`** | Executar tarefas independentes em paralelo com agentes especialistas simultâneos. |
| **`loop-engineering`** | Construir loops autônomos seguros com critérios de parada estritos para evitar execuções infinitas. |
| **`mcp-builder`** | Criar servidores compatíveis com o protocolo Model Context Protocol (MCP). |
| **`freellmapi`** | Roteamento unificado entre 34 provedores gratuitos de LLM com fallback automático. |
| **`airllm`** | Rodar modelos gigantes (70B+) em GPUs com pouca VRAM (4GB/8GB) via otimização de camadas. |
| **`LlamaFactory`** | Pipeline de fine-tuning local (LoRA, QLoRA, DPO) de modelos como LLaMA e DeepSeek. |

---

## 6. 💼 Startup, Produto & Negócios

Use ao estruturar um produto, falar com investidores ou priorizar o que construir:

| Skill | Quando Usar / Gatilho |
| :--- | :--- |
| **`mvp-scoping`** | Definir o escopo mínimo viável de um lançamento, cortando recursos desnecessários. |
| **`prd-writing`** / **`prd-generator`** | Escrever documentos de requisitos de produto (PRDs) claros e otimizados para IA. |
| **`pitch-deck`** | Estruturar narrativa e slides de apresentação para rodadas de investimento (Seed/Series A). |
| **`investor-research`** | Pesquisar e mapear perfil de investidores e fundos de venture capital adequados. |
| **`pricing-strategist`** | Construir modelo de precificação (freemium, tiers, pay-as-you-go). |
| **`churn-analysis`** | Identificar contas em risco de cancelamento e desenhar campanhas de retenção. |

---

## 7. 📣 Marketing, Copywriting & Vendas

Use para distribuição, criação de conteúdo e atração de usuários:

| Skill | Quando Usar / Gatilho |
| :--- | :--- |
| **`brand-copywriter`** | Redigir textos persuasivos para landing pages, anúncios e emails de conversão. |
| **`social-content`** / **`linkedin-writer`** / **`x-writer`** | Criar posts virais e posicionamento de autoridade técnica no LinkedIn e Twitter. |
| **`cold-outreach`** | Escrever mensagens frias personalizadas para prospecção B2B de alta conversão. |
| **`cro-optimization`** | Auditar landing pages existentes para aumentar a taxa de conversão de visitantes em clientes. |
| **`open-seo`** | Pesquisa de palavras-chave, análise de concorrentes e SEO programático. |

---

## 8. ⚙️ Infraestrutura, DevOps & Terminal

Use para gerenciar containers, pipelines de deploy e servidores:

| Skill | Quando Usar / Gatilho |
| :--- | :--- |
| **`cicd-setup`** | Criar ou consertar pipelines de CI/CD (GitHub Actions, GitLab CI). |
| **`deployment-procedures`** | Planejar deploys seguros com estratégias de rollback e verificação pós-voo. |
| **`server-management`** | Decisões de infraestrutura, proxies reversos (Nginx), logs e monitoramento. |
| **`powershell-windows`** | Padrões de automação, scripts e tratamento de erros no Windows. |
| **`bash-linux`** | Comandos avançados, pipelines, streams e scripts para ambientes Linux. |

---

### 💡 Dica de Utilização no Prompt:
Você não precisa se preocupar em lembrar o nome exato da skill: basta descrever a sua necessidade real (ex: *"preciso criar um teste E2E no navegador"* ou *"quero avaliar a segurança desse formulário"*). O roteador inteligente do sistema ativará automaticamente as skills correspondentes!
