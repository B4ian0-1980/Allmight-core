# 📚 Catálogo Completo & Taxonomia das 111 Super Skills do Antigravity Kit

> **Ecossistema:** [`.agent/skills/`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/)

> **Status:** 111 Skills Mapeadas · 13 Clusters Funcionais · Zero Redundâncias Não Documentadas


---

## 📋 Sumário Executivo

Este documento apresenta a taxonomia funcional completa de todas as habilidades integradas ao assistente. 
Cada módulo foi classificado com base no seu objetivo primário, destacando quando e por que escolher uma skill em detrimento de outra para a mesma tarefa.

### 🗺️ Índice dos 13 Clusters Funcionais

1. [🌐 Proxies, Gateways & Roteadores de LLMs (Custo Zero e Failover)](#cluster-1) (2 skills)
2. [🧠 Inferência, Fine-Tuning & Modelos Locais de IA](#cluster-2) (5 skills)
3. [🐝 Orquestração de Enxames, Multi-Agentes & Automação de Loops](#cluster-3) (6 skills)
4. [🎬 Fábrica Multimodal de Mídia (Vídeo, Imagem, Áudio & Animação)](#cluster-4) (12 skills)
5. [⚔️ Segurança Ofensiva, Pentest & Red Team (24 Módulos)](#cluster-5) (24 skills)
6. [🛡️ Segurança Defensiva, Auditoria & Varredura de Riscos](#cluster-6) (3 skills)
7. [🎨 Design de Interfaces, Ergonomia & Leis de UX](#cluster-7) (12 skills)
8. [⚙️ Desenvolvimento Backend, Arquitetura & Linguagens](#cluster-8) (9 skills)
9. [✂️ Engenharia Pragmática, YAGNI, Refatoração & Simplicidade (Ponytail)](#cluster-9) (8 skills)
10. [🧪 Qualidade de Código, Depuração & Testes Científicos](#cluster-10) (9 skills)
11. [📚 Extração de Conhecimento, Livros & Documentação](#cluster-11) (9 skills)
12. [☁️ Recursos Gratuitos da Web, APIs & Hospedagem (2026)](#cluster-12) (4 skills)
13. [🔌 Sensores, Hardware, SO & Engenharia Reversa](#cluster-13) (8 skills)

---

<div id="cluster-1"></div>

## 🌐 Proxies, Gateways & Roteadores de LLMs (Custo Zero e Failover)

> **Finalidade:** Ferramentas focadas em unificar múltiplos provedores de inteligência artificial em um único endpoint OpenAI-compatível (`/v1`), oferecendo failover automático em caso de rate limit (429) e agregando cotas gratuitas mensais.

**Total de Módulos:** `2 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`freellmapi`](skills/freellmapi/SKILL.md)** | Agregador de 34 provedores gratuitos (~7.4B tokens/mês), failover automático e app desktop para Windows. | Backend unificado para qualquer aplicação web, script Python ou cliente compatível com OpenAI. |
| **[`free-claude-code`](skills/free-claude-code/SKILL.md)** | Proxy cirúrgico projetado para ferramentas CLI de desenvolvimento (Claude Code, Cline, Aider). | Uso em terminais de programação sem pagar assinaturas da Anthropic. |

---

<div id="cluster-2"></div>

## 🧠 Inferência, Fine-Tuning & Modelos Locais de IA

> **Finalidade:** Módulos para treinamento, execução e tomada de decisão com inteligência artificial diretamente no ambiente local ou com hardware de consumo, sem depender de nuvens pagas.

**Total de Módulos:** `5 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`LlamaFactory`](skills/LlamaFactory/SKILL.md)** | Fine-Tuning visual e CLI de mais de 100 LLMs (Llama 3, Qwen, DeepSeek) usando LoRA, QLoRA e DPO. | Treinar e especializar modelos com dados da sua empresa. |
| **[`airllm`](skills/airllm/SKILL.md)** | Inferência de modelos gigantes (70B+) em GPUs com pouca VRAM (4GB–8GB) por chaveamento de camadas na RAM. | Rodar LLMs enormes localmente em computadores modestos. |
| **[`laya`](skills/laya/SKILL.md)** | Motor de decisão ultra-rápido "Sistema 1" em Node.js/TypeScript. | Classificações e scores em sub-milissegundos com zero custo de tokens. |
| **[`laya-nandha`](skills/laya-nandha/SKILL.md)** | Implementação em Python do motor de decisões rápidas Laya. | Classificação local de dados e decisões imediatas em scripts Python. |
| **[`awesome-llm-apps`](skills/awesome-llm-apps/SKILL.md)** | Catálogo curado com mais de 100 arquiteturas prontas de agentes, RAG e fluxos de IA. | Referência de implementação para novas aplicações de IA. |

---

<div id="cluster-3"></div>

## 🐝 Orquestração de Enxames, Multi-Agentes & Automação de Loops

> **Finalidade:** Coordenação de múltiplos agentes de IA trabalhando de forma colaborativa, distribuindo tarefas e prevenindo loops infinitos ou desperdício de recursos.

**Total de Módulos:** `6 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`autoharness`](skills/autoharness/SKILL.md)** | Camada de auto-aprendizado para agentes: destila lições de sessões reais, mescla duplicatas e poda skills obsoletas. | Aprendizado contínuo do agente a partir de tarefas reais sem engenharia manual de prompts. |
| **[`ruflo`](skills/ruflo/SKILL.md)** | Plataforma de enxames multi-agente com mais de 300 ferramentas MCP integradas. | Tarefas massivas que necessitam de enxames hierárquicos. |
| **[`loop-engineering`](skills/loop-engineering/SKILL.md)** | Engenharia e contenção de loops autônomos com limites de parada comprovados. | Prevenir que agentes entrem em loops infinitos de execução. |
| **[`parallel-agents`](skills/parallel-agents/SKILL.md)** | Divisão e execução paralela de tarefas independentes entre múltiplos agentes. | Quando diferentes arquivos podem ser trabalhados simultaneamente. |
| **[`behavioral-modes`](skills/behavioral-modes/SKILL.md)** | Modulação de comportamento psicológico (Arquiteto, Planejador, Executor, Depurador). | Alternar o tom e o rigor metodológico conforme a fase da tarefa. |
| **[`intelligent-routing`](skills/intelligent-routing/SKILL.md)** | Triagem automática da intenção do usuário para seleção dos melhores especialistas. | Roteamento silencioso e imediato de qualquer requisição. |

---

<div id="cluster-4"></div>

## 🎬 Fábrica Multimodal de Mídia (Vídeo, Imagem, Áudio & Animação)

> **Finalidade:** Conjunto de automações para produção de ativos visuais, narração, vídeos curtos para redes sociais, animações de alta fidelidade e música interativa.

**Total de Módulos:** `12 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`MoneyPrinterTurbo`](skills/MoneyPrinterTurbo/SKILL.md)** | Fábrica ponta a ponta de vídeos verticais (Shorts/TikTok/Reels) com roteiro, TTS, B-roll e legendas. | Criação automatizada de canais no YouTube / redes sociais. |
| **[`product-launch-motion`](skills/product-launch-motion/SKILL.md)** | Filmes de lançamento programáticos em código com HTML, CSS, GSAP e render via FFmpeg. | Apresentações e vídeos cinematográficos para produtos digitais. |
| **[`media-inference-worker`](skills/media-inference-worker/SKILL.md)** | Cliente assíncrono para modelos de ponta em nuvem (Qwen Image 3, Kling 3.0, MiniMax H3, Veo 3.1). | Geração sob demanda de imagens hiper-realistas e tomadas de vídeo. |
| **[`open-generative-ai`](skills/open-generative-ai/SKILL.md)** | Alternativa open-source de estúdio generativo (vídeo, áudio e sincronização labial). | Clonagem de voz e lip-sync em vídeos. |
| **[`musica`](skills/musica/SKILL.md)** | Workstation DJ/VJ de áudio reativo com efeitos 3D em WebGL e Tauri/Rust. | Criação de ambientes audiovisuais interativos e shows de luz. |
| **Suíte `replicate-*`** | Gestão completa de modelos de imagem e vídeo comerciais na nuvem Replicate. | Quando se deseja integrar APIs oficiais de Flux, SDXL ou Cog. |

---

<div id="cluster-5"></div>

## ⚔️ Segurança Ofensiva, Pentest & Red Team (24 Módulos)

> **Finalidade:** Metodologias práticas e completas de testes de invasão ética (pentest) divididas por vetor de ataque específico, simulando agentes hostis para encontrar falhas antes que sejam exploradas.

**Total de Módulos:** `24 skills`

* **Ataques a Aplicações & Lógica de Negócios:**
  * [`claude-red-offensive-sqli`](skills/claude-red-offensive-sqli/): Injeções SQL profundas (Blind, Time-based, Error-based, Union).
  * [`claude-red-offensive-xss`](skills/claude-red-offensive-xss/SKILL.md): Cross-Site Scripting (DOM, Stored, Reflected e bypass de CSP).
  * [`claude-red-offensive-ssti`](skills/claude-red-offensive-ssti/SKILL.md): Server-Side Template Injection em Jinja2, Twig, Blade e Freemarker.
  * [`claude-red-offensive-xxe`](skills/claude-red-offensive-xxe/SKILL.md): Injeção em parsers XML para leitura de arquivos confidenciais.
  * [`claude-red-offensive-business-logic`](skills/claude-red-offensive-business-logic/SKILL.md): Fraudes em regras financeiras, acúmulo de cupons, bypass de frete e inversão de saldo.
  * [`claude-red-offensive-file-upload`](skills/claude-red-offensive-file-upload/): Bypass de validação de extensões para upload de webshells.
  * [`claude-red-offensive-deserialization`](skills/claude-red-offensive-deserialization/SKILL.md): Exploração de desserialização insegura em Java, PHP, Python e .NET.
  * [`claude-red-offensive-rce`](skills/claude-red-offensive-rce/): Execução Remota de Código em sinks de terminal e chamadas de sistema.
* **Ataques a APIs e Controle de Acesso:**
  * [`claude-red-offensive-api-security`](skills/claude-red-offensive-api-security/SKILL.md): Cobertura sistemática do OWASP API Top 10 (REST, gRPC, WebSockets).
  * [`claude-red-offensive-api-abuse`](skills/claude-red-offensive-api-abuse/SKILL.md): Evasão de rate-limit, encadeamento de chamadas e enumeração em massa.
  * [`claude-red-offensive-graphql`](skills/claude-red-offensive-graphql/SKILL.md): DoS por bombas de profundidade e extração de schema cego em GraphQL.
  * [`claude-red-offensive-jwt`](skills/claude-red-offensive-jwt/SKILL.md): Quebra de tokens (algoritmo none, injeção kid, confusão RS256/HS256).
  * [`claude-red-offensive-idor`](skills/claude-red-offensive-idor/SKILL.md): Acesso horizontal e vertical a objetos de outros usuários.
  * [`claude-red-offensive-oauth`](skills/claude-red-offensive-oauth/SKILL.md): Desvios de fluxo de consentimento, vazamento de code e tokens OAuth2.
* **Infraestrutura, Nuvem & Redes:**
  * [`claude-red-offensive-container-escape`](skills/claude-red-offensive-container-escape/SKILL.md): Fuga de contêineres Docker/Podman para o sistema operacional host.
  * [`claude-red-offensive-k8s-attacks`](skills/claude-red-offensive-k8s-attacks/SKILL.md): Exploração de pods, RBAC permissivo e comprometimento de clusters Kubernetes.
  * [`claude-red-offensive-cloud`](skills/claude-red-offensive-cloud/SKILL.md): Movimentação lateral e escalação de privilégios IAM em AWS, Azure e GCP.
  * [`claude-red-offensive-ssrf`](skills/claude-red-offensive-ssrf/SKILL.md): Ataques a serviços internos e endpoints de metadados em nuvem.
  * [`claude-red-offensive-race-condition`](skills/claude-red-offensive-race-condition/SKILL.md): Condições de corrida HTTP paralelas (TOCTOU) em transações.
  * [`claude-red-offensive-request-smuggling`](skills/claude-red-offensive-request-smuggling/SKILL.md): Desalinhamento entre proxies reversos e backends HTTP/1 e HTTP/2.
  * [`claude-red-offensive-waf-bypass`](skills/claude-red-offensive-waf-bypass/SKILL.md): Mutações e técnicas de codificação para contornar WAFs corporativos.
  * [`red-team-tactics`](skills/red-team-tactics/SKILL.md): Estratégia global de operações Red Team com base no framework MITRE ATT&CK.

---

<div id="cluster-6"></div>

## 🛡️ Segurança Defensiva, Auditoria & Varredura de Riscos

> **Finalidade:** Ferramentas para auditoria formal, conformidade de dependências, postura defensiva e diagnóstico de estabilidade de código.

**Total de Módulos:** `3 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`security-audit`](skills/security-audit/SKILL.md)** | Metodologia defensiva em 6 fases padrão Cloudflare com emissão formal de `findings.json`. | Auditorias pré-deploy e relatórios de segurança corporativa. |
| **[`vulnerability-scanner`](skills/vulnerability-scanner/SKILL.md)** | Varredura de CVEs em dependências e riscos na cadeia de suprimentos (OWASP 2025). | Inspeção contínua do `package.json`, `requirements.txt` e bibliotecas externas. |
| **[`system-audit`](skills/system-audit/SKILL.md)** | Diagnóstico e verificação abrangente de integridade em sistemas legados. | Checagens globais de robustez e estabilidade de infraestrutura. |

---

<div id="cluster-7"></div>

## 🎨 Design de Interfaces, Ergonomia & Leis de UX

> **Finalidade:** Diretrizes e utilitários para criar interfaces modernas, acessíveis, de alta conversão, livres de clichês visuais de IA e respeitando a psicologia cognitiva.

**Total de Módulos:** `12 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`taste-skill`](skills/taste-skill/SKILL.md)** | Framework anti-slop para IA: elimina layouts clichês com tipografia refinada, espaçamento fluido e micro-motion. | Transformar telas genéricas de IA em produtos de aparência artesanal e premium. |
| **[`awesome-design-md`](skills/awesome-design-md/SKILL.md)** | Especificações DESIGN.md (Google Stitch) de 73+ produtos líderes (Claude, Vercel, Linear, Cursor). | Definir o design system e linguagem visual de um projeto para agentes de IA. |
| **[`image-to-code`](skills/image-to-code/SKILL.md)** | Engenharia reversa visual: converte mockups, wireframes e capturas de tela em HTML, Tailwind e React. | Clonar telas e implementar designs a partir de imagens sem medir pixels manualmente. |
| **[`laws-of-ux`](skills/laws-of-ux/SKILL.md)** | Aplicação de 21 leis cognitivas (Fitts, Hick, Miller, Doherty <400ms, Jakob). | Reduzir o esforço mental do usuário e otimizar tempo de reação. |
| **[`frontend-design`](skills/frontend-design/SKILL.md)** | Princípios de design premium, contraste apurado e aplicação do **Purple Ban** (sem violeta genérico). | Construção de layouts autênticos e componentes web elegantes. |
| **[`impeccable-design`](skills/impeccable-design/SKILL.md)** | Refinamento extremo de micro-interações, tipografia, espaçamentos e estados de erro. | Polir uma interface comum até que pareça um produto de ponta. |
| **[`tailwind-patterns`](skills/tailwind-patterns/SKILL.md)** | Padrões de design token e configurações limpas com Tailwind CSS v4. | Estilização rápida e performática usando CSS moderno. |
| **[`diagram-design`](skills/diagram-design/SKILL.md)** | Geração de 42 estilos de diagramas arquiteturais e fluxos em HTML + SVG puro. | Apresentações e documentações executivas sem a poluição do Mermaid. |
| **[`web-design-guidelines`](skills/web-design-guidelines/SKILL.md)** | Mais de 100 regras de conformidade em acessibilidade (WCAG), contraste e UX. | Auditoria de páginas para aprovação em requisitos de acessibilidade. |
| **[`nextjs-react-expert`](skills/nextjs-react-expert/SKILL.md)** | Melhores práticas de performance para React e Next.js direto da engenharia da Vercel. | Eliminar waterfalls e reduzir tempo de carregamento de páginas. |
| **[`mobile-design`](skills/mobile-design/SKILL.md)** | Ergonomia mobile: zonas de alcance de polegar, touch targets e convenções iOS/Android. | Construção de aplicativos Flutter, React Native ou PWAs responsivos. |

---

<div id="cluster-8"></div>

## ⚙️ Desenvolvimento Backend, Arquitetura & Linguagens

> **Finalidade:** Padrões arquiteturais, modelagem de dados, regras de negócio e desenvolvimento sênior em linguagens específicas.

**Total de Módulos:** `9 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`architecture`](skills/architecture/SKILL.md)** | Avaliação de requisitos, trade-offs e documentação de ADRs (Architecture Decision Records). | Tomada de decisões fundamentadas antes de iniciar um sistema. |
| **[`api-patterns`](skills/api-patterns/SKILL.md)** | Decisão de arquitetura de APIs (REST, GraphQL, tRPC), paginação e idempotência. | Desenho de contratos de comunicação de alta performance. |
| **[`database-design`](skills/database-design/SKILL.md)** | Modelagem relacional, estratégias de indexação SQL e migrações seguras. | Criação de esquemas de banco de dados rápidos e normalizados. |
| **[`wa-akg`](skills/wa-akg/SKILL.md)** | Gateway multi-sessão de WhatsApp, Dashboard Next.js 15, automações (broadcast, auto-reply) e 109+ endpoints REST. | Automação e envio de mensagens WhatsApp para sistemas web e agentes. |
| **[`rust-pro`](skills/rust-pro/SKILL.md)** | Padrões sênior em Rust 1.75+, Tokio, Axum e concorrência sem bloqueios (lock-free). | Microsserviços e motores de ultra-alta performance. |
| **[`python-patterns`](skills/python-patterns/SKILL.md)** | Padrões modernos de Python, tipagem estática rigorosa e APIs em FastAPI. | Backends rápidos, scripts de dados e serviços assíncronos. |
| **[`nodejs-best-practices`](skills/nodejs-best-practices/SKILL.md)** | Segurança em assincronia, arquitetura modular e tratamento seguro de memória no Node.js. | Microsserviços e aplicações corporativas em Node/TypeScript. |
| **[`app-builder`](skills/app-builder/SKILL.md)** | Orquestrador para geração de scaffolds e aplicações fullstack completas a partir de comandos. | Criar novos projetos do zero já com arquitetura recomendada. |
| **[`game-development`](skills/game-development/SKILL.md)** | Arquitetura de motores de jogos, lógica de colisões, renderização e mecânicas 2D/3D. | Desenvolvimento de simuladores e jogos interativos. |

---

<div id="cluster-9"></div>

## ✂️ Engenharia Pragmática, YAGNI, Refatoração & Simplicidade (Ponytail)

> **Finalidade:** Filosofia sênior focada em eliminar over-engineering, remover complexidade desnecessária e aplicar o menor diff que soluciona o problema com máxima manutenibilidade.

**Total de Módulos:** `8 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`clean-code`](skills/clean-code/SKILL.md)** | Código conciso, direto, legível e sem abstrações prematuras ou comentários óbvios. | Escrita de código limpo no dia a dia. |
| **[`coding-discipline`](skills/coding-discipline/SKILL.md)** | Disciplina cirúrgica baseada em Karpathy: toca apenas no que foi pedido, preservando o código ao redor. | Correções sem efeitos colaterais em bases de produção. |
| **[`ponytail`](skills/ponytail/SKILL.md)** | Filosofia YAGNI (Lazy Senior Dev): aplica a menor alteração funcional que resolve a tarefa. | Simplificar tarefas e evitar que o agente crie arquiteturas gigantes para tarefas simples. |
| **[`ponytail-audit`](skills/ponytail-audit/SKILL.md)** | Varredura de repositório para localizar código morto, funções nunca chamadas e bloat. | Limpeza profunda e redução de tamanho de projetos legados. |
| **[`ponytail-debt`](skills/ponytail-debt/SKILL.md)** | Livro-razão que mapeia todos os atalhos e débitos técnicos assumidos. | Rastrear o que foi postergado para pagar dívida técnica no futuro. |
| **[`ponytail-review`](skills/ponytail-review/SKILL.md)** | Revisão focada em perguntar: *"Essa linha realmente precisa existir?"*. | Revisar Pull Requests com foco em simplicidade máxima. |

---

<div id="cluster-10"></div>

## 🧪 Qualidade de Código, Depuração & Testes Científicos

> **Finalidade:** Metodologias e verificadores para garantir estabilidade, isolar bugs com base em evidências e validar sistemas antes do deploy.

**Total de Módulos:** `9 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`playwright-cli`](skills/playwright-cli/SKILL.md)** | Automação e testes de navegador via CLI oficial da Microsoft: ultra-econômico em tokens para agentes. | Testar fluxos E2E, interagir com telas e tirar screenshots sem poluir o contexto da LLM. |
| **[`webapp-testing`](skills/webapp-testing/SKILL.md)** | Testes ponta a ponta (E2E) simulando a interação real de usuários com Playwright. | Validar fluxos completos de telas e formulários. |
| **[`systematic-debugging`](skills/systematic-debugging/SKILL.md)** | Método científico de depuração: formular 5–7 hipóteses, rastrear logs e atacar a causa-raiz. | Investigar problemas complexos ou intermitentes sem adivinhação. |
| **[`tdd-workflow`](skills/tdd-workflow/SKILL.md)** | Ciclo rigoroso de Test-Driven Development (Red → Green → Refactor). | Criar lógica crítica com garantia matemática de funcionamento. |
| **[`testing-patterns`](skills/testing-patterns/SKILL.md)** | Estrutura de testes unitários e integração seguindo o padrão AAA (Arrange, Act, Assert). | Escrever suítes de testes claras e fáceis de manter. |
| **[`pre-mortem`](skills/pre-mortem/SKILL.md)** | Simulação preventiva: supõe que o projeto fracassou no futuro para achar falhas antes de começar. | Antecipar armadilhas em tarefas arriscadas ou de grande porte. |
| **[`performance-profiling`](skills/performance-profiling/SKILL.md)** | Medição empírica de uso de CPU, alocação de memória e métricas Core Web Vitals. | Otimizar rotinas lentas e resolver vazamentos de memória. |
| **[`code-review-checklist`](skills/code-review-checklist/SKILL.md)** | Checklist formal de revisão de código cobrindo segurança, legibilidade e testes. | Usar antes de mesclar branches importantes. |
| **[`lint-and-validate`](skills/lint-and-validate/SKILL.md)** | Validação estática contínua de tipos e formatação de código. | Rodar imediatamente após cada alteração de arquivo. |

---

<div id="cluster-11"></div>

## 📚 Extração de Conhecimento, Livros & Documentação

> **Finalidade:** Mecanismos para converter documentações extensas, livros e papers em habilidades modulares que os agentes conseguem ler e aplicar sob demanda.

**Total de Módulos:** `9 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`graphify`](skills/graphify/SKILL.md)** | Construtor multimodal de Grafos de Conhecimento (código, docs, PDFs, imagens) com 71.5x menos tokens. | Mapear arquiteturas complexas, clusters e relações conceituais em qualquer diretório. |
| **[`book-to-skill`](skills/book-to-skill/SKILL.md)** | Transforma livros técnicos (PDF, EPUB, DOCX) em skills compactas com economia de 24x a 51x em tokens. | Ingerir livros de 500 páginas para o agente consultar capítulo por capítulo. |
| **[`manual-generator`](skills/manual-generator/SKILL.md)** | Raspa documentações web em HTML e compila um livro PDF offline unificado. | Baixar manuais online para consulta sem internet. |
| **[`knowledge-base`](skills/knowledge-base/SKILL.md)** | Protocolo de busca profunda na biblioteca AllMight de templates e padrões. | Recuperar boas práticas já registradas no sistema. |
| **[`find-skills`](skills/find-skills/SKILL.md)** | Busca e instalação dinâmica de novas habilidades criadas pela comunidade (`skills.sh`). | Expandir as capacidades do assistente sob demanda. |
| **[`documentation-templates`](skills/documentation-templates/SKILL.md)** | Modelos padronizados para READMEs, documentação de arquitetura e guias para IA. | Criar documentações profissionais para novos projetos. |
| **[`i18n-localization`](skills/i18n-localization/SKILL.md)** | Internacionalização, suporte a múltiplos idiomas, detecção de textos hardcoded e RTL. | Preparar softwares para o mercado global. |
| **[`brainstorming`](skills/brainstorming/SKILL.md)** & **[`plan-writing`](skills/plan-writing/SKILL.md)** | Condução de alinhamentos socráticos e redação de planos de entrega granulares. | Planejar grandes recursos antes de tocar no código. |

---

<div id="cluster-12"></div>

## ☁️ Recursos Gratuitos da Web, APIs & Hospedagem (2026)

> **Finalidade:** Guias e bancos de dados para identificar provedores de hospedagem sem custo e conectar dados abertos do mundo real aos projetos.

**Total de Módulos:** `4 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`awesome-web-hosting`](skills/awesome-web-hosting/SKILL.md)** | Catálogo curado de 150+ plataformas de nuvem gratuitas (Postgres, Docker, VPS, IA) em 2026. | Encontrar onde hospedar bancos, contêineres e sites a custo zero. |
| **[`public-apis`](skills/public-apis/SKILL.md)** | A maior biblioteca pública de APIs gratuitas organizadas por categoria. | Conectar dados do mundo real (clima, cotações, moedas) sem pagar nada. |
| **[`seo-fundamentals`](skills/seo-fundamentals/SKILL.md)** | Otimização para buscadores tradicionais com foco em Core Web Vitals e indexação. | Posicionar sites nos primeiros resultados do Google. |
| **[`geo-fundamentals`](skills/geo-fundamentals/SKILL.md)** | Generative Engine Optimization: relevância em mecanismos de resposta por IA. | Otimizar conteúdos para serem citados por ChatGPT, Claude e Perplexity. |

---

<div id="cluster-13"></div>

## 🔌 Sensores, Hardware, SO & Engenharia Reversa

> **Finalidade:** Conexão com hardware físico, sinais de rádio, descompilação de aplicativos e comandos seguros de sistema operacional.

**Total de Módulos:** `8 skills`

| Skill | Foco Principal | Melhor Caso de Uso |
| :--- | :--- | :--- |
| **[`reverse-skill`](skills/reverse-skill/SKILL.md)** | Roteador de engenharia reversa para agentes: 44 regras para APK, binários (ELF/PE), desofuscação JS e CTFs. | Triagem e orquestração determinística de descompilação e análise de binários. |
| **[`rea`](skills/rea/SKILL.md)** | Servidor MCP de engenharia reversa para inspecionar binários, pacotes Electron e executáveis. | Desmontar e entender o funcionamento interno de aplicações fechadas. |
| **[`ruview`](skills/ruview/SKILL.md)** | Sensoriamento espacial: detecção de presença humana e sinais vitais via sinal Wi-Fi puro. | Automação residencial, presença e telemetria física sem câmeras. |
| **[`mcp-builder`](skills/mcp-builder/SKILL.md)** | Desenvolvimento e arquitetura de servidores do Model Context Protocol (MCP). | Criar ferramentas personalizadas para LLMs executarem ações no computador. |
| **[`powershell-windows`](skills/powershell-windows/SKILL.md)** & **[`bash-linux`](skills/bash-linux/SKILL.md)** | Padrões de sintaxe segura e armadilhas comuns em terminais Windows e Linux. | Garantir que scripts e comandos de terminal nunca quebrem o SO host. |
| **[`server-management`](skills/server-management/SKILL.md)** & **[`deployment-procedures`](skills/deployment-procedures/SKILL.md)** | Gerenciamento de processos de servidor, deploy com rollback e resiliência de infraestrutura. | Manter servidores estáveis em ambientes de produção. |

---
