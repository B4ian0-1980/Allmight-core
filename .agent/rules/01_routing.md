---
trigger: model_decision
description: "Classificação de requisições, seleção automática de agentes especialistas e radar proativo de recursos integrados."
---

# Intelligent Routing Rules

## 📥 REQUEST CLASSIFIER (STEP 1)

**Before ANY action, classify the request:**

| Request Type     | Trigger Keywords                           | Active Tiers                   | Result                      |
| ---------------- | ------------------------------------------ | ------------------------------ | --------------------------- |
| **QUESTION**     | "what is", "how does", "explain"           | TIER 0 only                    | Text Response               |
| **SURVEY/INTEL** | "analyze", "list files", "overview"        | TIER 0 + Explorer              | Session Intel (No File)     |
| **SIMPLE CODE**  | "fix", "add", "change" (single file)       | TIER 0 + TIER 1 (lite)         | Inline Edit                 |
| **COMPLEX CODE** | "build", "create", "implement", "refactor" | TIER 0 + TIER 1 (full) + Agent | **{task-slug}.md Required** |
| **DESIGN/UI**    | "design", "UI", "page", "dashboard"        | TIER 0 + TIER 1 + Agent        | **{task-slug}.md Required** |
| **SLASH CMD**    | /create, /orchestrate, /debug              | Command-specific flow          | Variable                    |

---

## 🤖 INTELLIGENT AGENT ROUTING (STEP 2 - AUTO)

**ALWAYS ACTIVE: Before responding to ANY request, automatically analyze and select the best agent(s).**

> 🔴 **MANDATORY:** You MUST follow the protocol defined in `@[skills/intelligent-routing]`.

### Auto-Selection Protocol

1. **Analyze (Silent)**: Detect domains (Frontend, Backend, Security, etc.) from user request.
2. **Select Agent(s)**: Choose the most appropriate specialist(s).
3. **Inform User**: Concisely state which expertise is being applied.
4. **Apply**: Generate response using the selected agent's persona and rules.

### Response Format (MANDATORY)

When auto-applying an agent, inform the user:

```markdown
🤖 **Applying knowledge of `@[agent-name]`...**

[Continue with specialized response]
```

**Rules:**

1. **Silent Analysis**: No verbose meta-commentary ("I am analyzing...").
2. **Respect Overrides**: If user mentions `@agent`, use it.
3. **Complex Tasks**: For multi-domain requests, use `orchestrator` and ask Socratic questions first.

### ⚠️ AGENT ROUTING CHECKLIST (MANDATORY BEFORE EVERY CODE/DESIGN RESPONSE)

**Before ANY code or design work, you MUST complete this mental checklist:**

| Step | Check | If Unchecked |
|------|-------|--------------|
| 1 | Did I identify the correct agent for this domain? | → STOP. Analyze request domain first. |
| 2 | Did I READ the agent's `.md` file (or recall its rules)? | → STOP. Open `.agent/agents/{agent}.md` |
| 3 | Did I announce `🤖 Applying knowledge of @[agent]...`? | → STOP. Add announcement before response. |
| 4 | Did I load required skills from agent's frontmatter? | → STOP. Check `skills:` field and read them. |

**Failure Conditions:**

- ❌ Writing code without identifying an agent = **PROTOCOL VIOLATION**
- ❌ Skipping the announcement = **USER CANNOT VERIFY AGENT WAS USED**
- ❌ Ignoring agent-specific rules (e.g., Purple Ban) = **QUALITY FAILURE**

> 🔴 **Self-Check Trigger:** Every time you are about to write code or create UI, ask yourself:
> "Have I completed the Agent Routing Checklist?" If NO → Complete it first.

### 🎯 CONTEXT-AWARE RESOURCE SUGGESTIONS (PROACTIVE RADAR)

**Quando o usuário estiver realizando as tarefas abaixo, o agente DEVE sugerir ativamente os seguintes recursos integrados:**

| Contexto / O que você está fazendo | Recurso Integrado | Como o Agente Sugere / Ação Recomendada |
| :--- | :--- | :--- |
| **Geração de Imagens, Vídeos, Áudio ou Modelos Open-Source** | `replicate-*` (`prompt-images`, `prompt-videos`, `run-models`) | Sugerir as skills da Replicate para gerar assets visuais reais (Flux, SDXL, Kling) ou integrar modelos multimodais via API/MCP. |
| **Diagramas Editoriais, Arquitetura Visual, Fluxos sem Mermaid** | `diagram-design` (`skills/diagram-design`) | Sugerir a skill com 42 tipos de diagramas em HTML + SVG puro de nível editorial executivo (sem shadows ou diagramas poluídos). |
| **Refatoração Cirúrgica, Redução de Dívida Técnica, Filosofia YAGNI** | `ponytail-*` (`ponytail`, `ponytail-debt`, `ponytail-audit`) | Sugerir o mindset de engenheiro sênior pragmático: eliminar código desnecessário e simplificar a arquitetura ao mínimo viável. |
| **Pentest Autorizado, Testes Ofensivos, Injeção, BOLA, JWT, Cloud** | `claude-red-*` (`claude-red-offensive-*`) | Sugerir as skills ofensivas especializadas do claude-red para testes direcionados de BOLA/IDOR, SQLi, SSRF, JWT e container escape. |
| **Navegação e Memória em Repositórios Gigantes (Economia de 99% Tokens)** | `codebase-memory-mcp` (`mcp_config.json`) | Sugerir a ativação do servidor MCP em C com grafo Tree-sitter SQLite para consultas relacionais instantâneas no codebase. |
| **Análise de Dependências AST / Engenharia de Contexto para Agentes** | `Graft` (`knowledge/allmight/07_AUTOMACAO/GRAFT_CONTEXT_ENGINE.md`) | Sugerir o Graft para construir o grafo de código local e alimentar agentes com o contexto exato da árvore de tipos e funções. |
| **Produção Automatizada de Vídeos, Demos de Produto, Remotion** | `OpenMontage` (`knowledge/allmight/05_DESIGN_HARDWARE/OPENMONTAGE_STUDIO.md`) | Sugerir o estúdio OpenMontage para pipelines completos de vídeo automatizado com Remotion, FFmpeg e voz neural ElevenLabs. |
| **Automação 24/7 de Canais no YouTube com Custo Zero (Gemini)** | `YouTube Automation Agent` (`07_AUTOMACAO/YOUTUBE_AUTOMATION_AGENT.md`) | Sugerir o agente autônomo com API gratuita do Google Gemini para roteiros, thumbnails, SEO e upload contínuo no YouTube. |
| **Fazenda de Agentes Paralelos com Controle de Cotas (Pacing 5h/Semana)** | `Clodfarm` (`knowledge/allmight/07_AUTOMACAO/CLODFARM_ORCHESTRATOR.md`) | Sugerir o Clodfarm para paralelizar dezenas de tarefas assíncronas respeitando rigorosamente limites de API e cotas de uso. |
| **Memória Contínua, Raciocínio Temporal e Grafos para Agentes** | `Graphiti (Zep)` (`02_ESTRUTURA_IA/GRAPHITI_AGENT_MEMORY.md`) | Sugerir o Graphiti para construir grafos de conhecimento dinâmicos onde entidades e fatos evoluem com o passar do tempo. |
| **Validação de Ideias, Persona de Agência, Delight, Reality Check** | `Agency Agents Roster` (`01_GESTAO/AGENCY_AGENTS_ROSTER.md`) | Sugerir chamar especialistas como *Reality Checker* (riscos de produto) ou *Whimsy Injector* (experiência e personalidade). |
| **Automação de Tarefas no SO com Soberania Local de Dados** | `OpenClaw` (`knowledge/allmight/07_AUTOMACAO/OPENCLAW_SYSTEM.md`) | Sugerir o OpenClaw para automações no desktop/terminal sem depender de nuvens externas. |
| **Consumo de IA no Backend, Custo Zero, ou Fallback de APIs** | `OmniRoute` (`knowledge/allmight/04_INFRA_OPS/OMNIROUTE_GATEWAY.md`) | Sugerir o OmniRoute como proxy OpenAI-compatible local com 150+ provedores gratuitos (~1.62B tokens/mês) e compressão RTK/Caveman. |
| **Testes de Novas APIs de LLM sem Cartão de Crédito** | `Free LLM Resources` (`knowledge/allmight/02_ESTRUTURA_IA/FREE_LLM_APIS.md`) | Sugerir provedores gratuitos de alta velocidade como Groq, Cerebras, Google AI Studio ou OpenRouter free tier. |
| **Auditoria de Vulnerabilidades, Pentest ou Revisão de Segurança** | `security-audit` (Cloudflare Harness) | Sugerir a execução das 6 fases de auditoria defensiva da Cloudflare com validação de candidatos e emissão de `findings.json`. |
| **Ergonomia, Psicologia Cognitiva e UX de Telas** | `laws-of-ux` (`skills/laws-of-ux`) | Sugerir aplicação das 21 leis de UX (Fitts, Hick, Miller, Doherty <400ms, Jakob, Peak-End) e thresholds numéricos em interfaces web/mobile. |
| **Análise Preventiva de Riscos e Falhas (Pre-Mortem)** | `pre-mortem` (`skills/pre-mortem`) | Sugerir simulação prospectiva de falhas para antecipar pontos cegos de arquitetura, regressões e riscos antes de implementar. |
| **Engenharia de Loops Autônomos, Self-Healing ou Otimização** | `loop-engineering` (`skills/loop-engineering`) | Sugerir desenho de loops delimitados (Autoloop/Loopy) com métrica de verificação, limite de passes e reversão em regressões. |
| **Descoberta Dinâmica de Habilidades da Comunidade** | `find-skills` (`skills/find-skills`) | Sugerir busca e instalação de skills sob demanda via Skills CLI (`npx skills find/add`) para stacks ou domínios novos. |
| **Ingestão Universal de Documentos (PDF, Word, Excel, PPTX)** | `AnyDoc Parser` (`knowledge/allmight/07_AUTOMACAO/ANYDOC_PARSER.md`) | Sugerir conversão ultra-rápida via AnyDoc (Rust) de PDFs ou planilhas/documentos Office para Markdown limpo para LLM. |
| **Engenharia de Produção SDLC (Addy Osmani) & Setup** | `Addy Osmani SDLC & Setup` (`01_GESTAO/ADDY_OSMANI_SKILLS_AND_SETUP.md`) | Sugerir framework de 7 fases (Define, Plan, Verify, Review 5 eixos, Ship) e recomendação automática de automações para a stack. |
| **Startup Founder, Pitch, Ofertas Hormozi, GTM & Enxames de Personas** | `founder-*`, `cro-optimization`, `pitch-deck` (`01_GESTAO/STARTUP_FOUNDER_ECOSYSTEM.md`) | Sugerir o ecossistema Founder (11 skills de conselho/oferta de Hormozi/Thiel, 15 de GTM/copy e 50 de operação de startup de ponta a ponta). |

---