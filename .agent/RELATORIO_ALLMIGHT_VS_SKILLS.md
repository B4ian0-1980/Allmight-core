# 🏛️ Relatório Arquitetural: Camada Operacional (Skills) vs. Biblioteca de Referência (AllMight)

> **Destino:** [`d:/xampp/htdocs/0-fonte/.agent/RELATORIO_ALLMIGHT_VS_SKILLS.md`](file:///d:/xampp/htdocs/0-fonte/.agent/RELATORIO_ALLMIGHT_VS_SKILLS.md)  
> **Finalidade:** Esclarecer a distinção entre as ferramentas operacionais (`skills/`), a biblioteca AllMight (`knowledge/allmight/`) e o papel do radar proativo em `rules/01_routing.md`.

---

## 1. 🔍 O Que Explica a Aparente Divergência?

No arquivo de regras [`rules/01_routing.md`](file:///d:/xampp/htdocs/0-fonte/.agent/rules/01_routing.md), na seção **Context-Aware Resource Suggestions (Proactive Radar)**, são citadas diversas ferramentas de alta complexidade:
* **OmniRoute**
* **Graft**
* **Clodfarm**
* **Graphiti (Zep)**
* **OpenClaw**
* **OpenMontage**
* **AnyDoc Parser**
* **YouTube Automation Agent**
* **Agency Agents Roster**
* **Addy Osmani SDLC & Setup**

No entanto, no catálogo de **103 Super Skills** e no `painel_sistema.html`, essas ferramentas não apareciam como cards individuais. 

**O motivo é simples:** Elas pertencem a **duas camadas conceituais diferentes** dentro do ecossistema `.agent`:

```plaintext
                    CÉREBRO ANTIGRAVITY (.agent/)
                                │
       ┌────────────────────────┴────────────────────────┐
       ▼                                                 ▼
[ CAMADA OPERACIONAL ]                         [ CAMADA DE CONHECIMENTO ]
  .agent/skills/                                .agent/knowledge/allmight/
  (103 Super Skills Ativas)                     (Biblioteca Central v3.0)
  - Módulos com SKILL.md                        - Blueprints e Manuais em Markdown
  - Invocáveis pelos Agentes via Prompt         - Base conceitual acessível via /kb
  - Execução cirúrgica de código                - Padrões de arquitetura corporativa
```

---

## 2. ⚡ Comparativo Técnico entre as Duas Camadas

| Dimensão | 🧩 Camada Operacional (`.agent/skills/`) | 📚 Camada de Conhecimento (`knowledge/allmight/`) |
| :--- | :--- | :--- |
| **Formato** | Pasta individual contendo `SKILL.md` padronizado com YAML frontmatter (`name:`, `description:`). | Arquivos Markdown (`.md`) puros organizados em 8 pastas temáticas (`01_GESTAO`, `02_ESTRUTURA_IA`, etc.). |
| **Ciclo de Vida** | Carregamento dinâmico na memória do agente quando uma tarefa de código específica é acionada. | Consulta aprofundada sob demanda quando o usuário ou agente executa o workflow `/kb`. |
| **Custo de Contexto**| Ultraleve (~1.000 a 4.000 tokens por `SKILL.md`). | Documentos densos e analíticos (dossiês de arquitetura com dezenas de páginas). |
| **Propósito Principal** | **Ação Imediata:** Ditar regras de código, linting, testes ou disparar scripts locais (`generate.py`, `npm run dev`). | **Diretriz Arquitetural:** Documentar como construir, implantar e estruturar sistemas complexos. |

---

## 3. 🎯 O Papel do "Radar Proativo" em `rules/01_routing.md`

O radar no `01_routing.md` atua como um **sistema de gatilhos condicionais**. Em vez de carregar a biblioteca inteira de 70 KB da AllMight a cada conversa (o que consumiria muitos tokens), a regra instrui o assistente a vigiar o contexto da conversa:

```markdown
Quando o usuário disser...                  O assistente deve consultar...
──────────────────────────────────────────  ──────────────────────────────────────────
"Preciso de proxy gratuito com RTK"      →  knowledge/allmight/04_INFRA_OPS/OMNIROUTE_GATEWAY.md
"Preciso analisar dependências e AST"    →  knowledge/allmight/07_AUTOMACAO/GRAFT_CONTEXT_ENGINE.md
"Preciso paralelizar agentes com cotas"  →  knowledge/allmight/07_AUTOMACAO/CLODFARM_ORCHESTRATOR.md
"Preciso de memória dinâmica em grafos"  →  knowledge/allmight/02_ESTRUTURA_IA/GRAPHITI_AGENT_MEMORY.md
"Automação no desktop sem nuvem"         →  knowledge/allmight/07_AUTOMACAO/OPENCLAW_SYSTEM.md
"Estúdio de vídeo automatizado Remotion" →  knowledge/allmight/05_DESIGN_HARDWARE/OPENMONTAGE_STUDIO.md
"Ingestão e parsing de PDF/Word/Excel"   →  knowledge/allmight/07_AUTOMACAO/ANYDOC_PARSER.md
```

---

## 4. 📋 Mapeamento Completo dos Blueprints da Base AllMight

Abaixo estão todos os recursos da base AllMight citados no radar com seus respectivos caminhos e atribuições:

### 1. [`OmniRoute`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/04_INFRA_OPS/OMNIROUTE_GATEWAY.md)
* **Localização:** `knowledge/allmight/04_INFRA_OPS/OMNIROUTE_GATEWAY.md`
* **Finalidade:** Gateway de IA OpenAI-compatible com 150+ tiers gratuitos (~1.62B tokens/mês) e compressão profunda RTK/Caveman (até 89% de economia de contexto).

### 2. [`Graft Context Engine`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/07_AUTOMACAO/GRAFT_CONTEXT_ENGINE.md)
* **Localização:** `knowledge/allmight/07_AUTOMACAO/GRAFT_CONTEXT_ENGINE.md`
* **Finalidade:** Motor de engenharia de contexto que constrói o grafo sintático (AST) de código local, alimentando agentes apenas com a árvore exata de tipos e funções necessárias.

### 3. [`Clodfarm Orchestrator`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/07_AUTOMACAO/CLODFARM_ORCHESTRATOR.md)
* **Localização:** `knowledge/allmight/07_AUTOMACAO/CLODFARM_ORCHESTRATOR.md`
* **Finalidade:** Fazenda de agentes paralelos com controle de cotas (rate pacing de 5h/semana) para evitar bloqueios de API em execuções massivas.

### 4. [`Graphiti (Zep)`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/02_ESTRUTURA_IA/GRAPHITI_AGENT_MEMORY.md)
* **Localização:** `knowledge/allmight/02_ESTRUTURA_IA/GRAPHITI_AGENT_MEMORY.md`
* **Finalidade:** Sistema de memória contínua e raciocínio temporal para agentes, onde entidades e relações evoluem ao longo do tempo em um grafo de conhecimento.

### 5. [`OpenClaw System`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/07_AUTOMACAO/OPENCLAW_SYSTEM.md)
* **Localização:** `knowledge/allmight/07_AUTOMACAO/OPENCLAW_SYSTEM.md`
* **Finalidade:** Automação de tarefas de terminal e desktop com soberania local de dados, sem envio de telemetria ou dados para nuvens externas.

### 6. [`OpenMontage Studio`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/05_DESIGN_HARDWARE/OPENMONTAGE_STUDIO.md)
* **Localização:** `knowledge/allmight/05_DESIGN_HARDWARE/OPENMONTAGE_STUDIO.md`
* **Finalidade:** Pipeline completo de edição automatizada de vídeo combinando código Remotion, FFmpeg e síntese de voz ElevenLabs.

### 7. [`AnyDoc Parser`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/07_AUTOMACAO/ANYDOC_PARSER.md)
* **Localização:** `knowledge/allmight/07_AUTOMACAO/ANYDOC_PARSER.md`
* **Finalidade:** Parser ultrarrápido em Rust para conversão de PDFs, planilhas Excel, Word e apresentações PPTX em Markdown limpo para LLMs.

### 8. [`YouTube Automation Agent`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/07_AUTOMACAO/YOUTUBE_AUTOMATION_AGENT.md)
* **Localização:** `knowledge/allmight/07_AUTOMACAO/YOUTUBE_AUTOMATION_AGENT.md`
* **Finalidade:** Agente autônomo 24/7 com API gratuita do Google Gemini para roteirização, geração de miniaturas, SEO e upload contínuo no YouTube.

### 9. [`Agency Agents Roster`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/01_GESTAO/AGENCY_AGENTS_ROSTER.md)
* **Localização:** `knowledge/allmight/01_GESTAO/AGENCY_AGENTS_ROSTER.md`
* **Finalidade:** Elenco de personas de agência de produto para testes de estresse: *Reality Checker* (riscos e armadilhas) e *Whimsy Injector* (experiência do usuário).

### 10. [`Addy Osmani SDLC & Setup`](file:///d:/xampp/htdocs/0-fonte/.agent/knowledge/allmight/01_GESTAO/ADDY_OSMANI_SKILLS_AND_SETUP.md)
* **Localização:** `knowledge/allmight/01_GESTAO/ADDY_OSMANI_SKILLS_AND_SETUP.md`
* **Finalidade:** Metodologia de ciclo de vida de desenvolvimento (SDLC) em 7 fases: Define, Plan, Verify, Review de 5 eixos e Ship.

---

## 5. 🚀 Próximo Passo: Promoção de Blueprints para Skills Operacionais

Se for de interesse do usuário, podemos realizar a **"Promoção de Classe"**:
1. Criar pastas individuais dentro de `.agent/skills/` para as ferramentas que possuem código executável (como `omniroute`, `graft`, `openclaw`, `anydoc`).
2. Criar os respectivos `SKILL.md` padronizados.
3. Atualizar o catálogo `CATALOGO_SKILLS.md` e o `painel_sistema.html`, unificando a contagem de habilidades ativas.
