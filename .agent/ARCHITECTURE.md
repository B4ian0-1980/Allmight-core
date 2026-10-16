# Antigravity Kit Architecture

> Comprehensive AI Agent Capability Expansion Toolkit & Cognitive Operating System

---

## 📋 Overview

Antigravity Kit is a modular cognitive operating system consisting of:

- **21 Specialist Agents** — Role-based AI personas with calibrated context budgets
- **191 Skills** — Domain-specific playbooks, tools, and runtimes
- **17 Workflows** — Native slash command interactive procedures
- **10 Master Scripts** + **416 Skill-Level Scripts** — High-performance execution suite

---

## 🏗️ Directory Structure

```plaintext
.agent/
├── ARCHITECTURE.md          # System Architecture & Component Inventory
├── CATALOGO_SKILLS.md       # Full Skills Catalog across 13 Functional Clusters
├── skills_manifest.json     # Machine-readable healthcheck & token audit manifest
├── painel_sistema.html      # Real-time Web Control Center Dashboard
├── agents/                  # 21 Specialist Agent Personas
├── skills/                  # 191 Modular Super Skills & Toolkits
├── workflows/               # 17 Slash Command Workflows
├── rules/                   # Intelligent Routing & Coding Discipline Rules
└── scripts/                 # 10 Master Unified CLI & Runner Suite
```

---

## 🤖 Specialist Agents (21)

| Agent | Focus / Core Specialty | Key Skills Attached |
| :--- | :--- | :--- |
| [`auditor-specialist`](agents/auditor-specialist.md) | Senior Technical Auditor specialized in exhaustive software system analysis. | clean-code, system-audit, security-audit, security-scan, performance-profiling, architecture, testing-patterns |
| [`backend-specialist`](agents/backend-specialist.md) | Expert backend architect for Node.js, Python, and modern serverless/edge systems. | clean-code, nodejs-best-practices, python-patterns, api-patterns, database-design, mcp-builder, lint-and-validate, powershell-windows, bash-linux, rust-pro, coding-discipline |
| [`code-archaeologist`](agents/code-archaeologist.md) | Expert in legacy code, refactoring, and understanding undocumented systems. | clean-code, refactoring-patterns, code-review-checklist |
| [`database-architect`](agents/database-architect.md) | Expert database architect for schema design, query optimization, migrations, and modern serverless databases. | clean-code, database-design |
| [`debugger`](agents/debugger.md) | Expert in systematic debugging, root cause analysis, and crash investigation. | clean-code, systematic-debugging |
| [`devops-engineer`](agents/devops-engineer.md) | Expert in deployment, server management, CI/CD, and production operations. | clean-code, deployment-procedures, server-management, powershell-windows, bash-linux |
| [`documentation-writer`](agents/documentation-writer.md) | Expert in technical documentation. | clean-code, documentation-templates |
| [`explorer-agent`](agents/explorer-agent.md) | Advanced codebase discovery, deep architectural analysis, and proactive research agent. | clean-code, architecture, plan-writing, brainstorming, systematic-debugging |
| [`frontend-specialist`](agents/frontend-specialist.md) | Senior Frontend Architect who builds maintainable React/Next.js systems with performance-first mindset. | clean-code, laws-of-ux, nextjs-react-expert, web-design-guidelines, tailwind-patterns, frontend-design, lint-and-validate, coding-discipline |
| [`game-developer`](agents/game-developer.md) | Game development across all platforms (PC, Web, Mobile, VR/AR). | clean-code, game-development, game-development/pc-games, game-development/web-games, game-development/mobile-games, game-development/game-design, game-development/multiplayer, game-development/vr-ar, game-development/2d-games, game-development/3d-games, game-development/game-art, game-development/game-audio |
| [`mobile-developer`](agents/mobile-developer.md) | Expert in React Native and Flutter mobile development. | clean-code, mobile-design |
| [`orchestrator`](agents/orchestrator.md) | Multi-agent coordination and task orchestration. | clean-code, parallel-agents, behavioral-modes, plan-writing, brainstorming, architecture, lint-and-validate, powershell-windows, bash-linux, coding-discipline, loop-engineering, find-skills |
| [`penetration-tester`](agents/penetration-tester.md) | Expert in offensive security, penetration testing, red team operations, and vulnerability exploitation. | clean-code, vulnerability-scanner, red-team-tactics, api-patterns |
| [`performance-optimizer`](agents/performance-optimizer.md) | Expert in performance optimization, profiling, Core Web Vitals, and bundle optimization. | clean-code, performance-profiling |
| [`product-manager`](agents/product-manager.md) | Expert in product requirements, user stories, and acceptance criteria. | plan-writing, brainstorming, clean-code |
| [`product-owner`](agents/product-owner.md) | Strategic facilitator bridging business needs and technical execution. | plan-writing, brainstorming, clean-code |
| [`project-planner`](agents/project-planner.md) | Smart project planning agent. | clean-code, app-builder, plan-writing, brainstorming, pre-mortem, coding-discipline, loop-engineering |
| [`qa-automation-engineer`](agents/qa-automation-engineer.md) | Specialist in test automation infrastructure and E2E testing. | webapp-testing, testing-patterns, web-design-guidelines, clean-code, lint-and-validate |
| [`security-auditor`](agents/security-auditor.md) | Elite cybersecurity expert. | clean-code, vulnerability-scanner, security-audit, red-team-tactics, api-patterns |
| [`seo-specialist`](agents/seo-specialist.md) | SEO and GEO (Generative Engine Optimization) expert. | clean-code, seo-fundamentals, geo-fundamentals |
| [`test-engineer`](agents/test-engineer.md) | Expert in testing, TDD, and test automation. | clean-code, testing-patterns, tdd-workflow, webapp-testing, code-review-checklist, lint-and-validate |

---

## ⚡ Super Skills (191)

| Skill | Description | Location |
| :--- | :--- | :--- |
| **[`accelerator-application`](skills/accelerator-application/SKILL.md)** | When the user wants to apply to startup accelerators, incubators, or fellowship programs. Also use when the user... | `skills/accelerator-application/SKILL.md` |
| **[`airllm`](skills/airllm/SKILL.md)** | Guidance for running and fine-tuning massive open-source LLMs (DeepSeek-V3 671B, Kimi K3 2.8T, Llama 3 70B/405B,... | `skills/airllm/SKILL.md` |
| **[`api-patterns`](skills/api-patterns/SKILL.md)** | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagi... | `skills/api-patterns/SKILL.md` |
| **[`app-builder`](skills/app-builder/SKILL.md)** | Main application building orchestrator. Creates full-stack applications from natural language requests. Determin... | `skills/app-builder/SKILL.md` |
| **[`architecture`](skills/architecture/SKILL.md)** | Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use whe... | `skills/architecture/SKILL.md` |
| **[`architecture-design`](skills/architecture-design/SKILL.md)** | When the user needs to design or evaluate system architecture — service boundaries, data models, API contracts, ... | `skills/architecture-design/SKILL.md` |
| **[`autoharness`](skills/autoharness/SKILL.md)** | Self-learning skill layer for coding agents. Automatically distills real working sessions into reusable skills, ... | `skills/autoharness/SKILL.md` |
| **[`awesome-design-md`](skills/awesome-design-md/SKILL.md)** | Curated collection and specification guide for DESIGN.md design system documents (Google Stitch standard). Conta... | `skills/awesome-design-md/SKILL.md` |
| **[`awesome-llm-apps`](skills/awesome-llm-apps/SKILL.md)** | A reference catalogue of 100+ open-source AI agents, agent skills, and RAG apps built with various LLMs (Claude,... | `skills/awesome-llm-apps/SKILL.md` |
| **[`awesome-web-hosting`](skills/awesome-web-hosting/SKILL.md)** | A definitive guide to free cloud infrastructure, PaaS, and hosting platforms. Use this skill when the user asks ... | `skills/awesome-web-hosting/SKILL.md` |
| **[`bash-linux`](skills/bash-linux/SKILL.md)** | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or... | `skills/bash-linux/SKILL.md` |
| **[`behavioral-modes`](skills/behavioral-modes/SKILL.md)** | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior bas... | `skills/behavioral-modes/SKILL.md` |
| **[`board-update`](skills/board-update/SKILL.md)** | When the user needs to write a monthly or quarterly investor update, prepare a board deck, or communicate compan... | `skills/board-update/SKILL.md` |
| **[`book-to-skill`](skills/book-to-skill/SKILL.md)** | Converts books and documents (PDF, EPUB, DOCX, HTML, Markdown, plain text, RTF, MOBI/AZW with Calibre) into stru... | `skills/book-to-skill/SKILL.md` |
| **[`brainstorming`](skills/brainstorming/SKILL.md)** | Socratic questioning protocol + user communication. MANDATORY for complex requests, new features, or unclear req... | `skills/brainstorming/SKILL.md` |
| **[`brand-copywriter`](skills/brand-copywriter/SKILL.md)** | Writes marketing copy using proven copywriting frameworks. Use when user needs copy for ads (Facebook, Instagram... | `skills/brand-copywriter/SKILL.md` |
| **[`churn-analysis`](skills/churn-analysis/SKILL.md)** | When the user needs to identify at-risk accounts, understand why customers are leaving, reduce churn rate, build... | `skills/churn-analysis/SKILL.md` |
| **[`cicd-setup`](skills/cicd-setup/SKILL.md)** | When the user needs to set up or improve CI/CD pipelines — GitHub Actions, GitLab CI, deployment automation, or ... | `skills/cicd-setup/SKILL.md` |
| **[`claude-red-offensive-api-abuse`](skills/claude-red-offensive-api-abuse/SKILL.md)** | Advanced API exploitation methodology focused on business logic abuse and sophisticated attack patterns that byp... | `skills/claude-red-offensive-api-abuse/SKILL.md` |
| **[`claude-red-offensive-api-security`](skills/claude-red-offensive-api-security/SKILL.md)** | Comprehensive API security testing methodology covering REST, gRPC, and WebSocket attack surfaces. Addresses the... | `skills/claude-red-offensive-api-security/SKILL.md` |
| **[`claude-red-offensive-business-logic`](skills/claude-red-offensive-business-logic/SKILL.md)** | Business logic vulnerability testing for web/mobile/API engagements. Covers workflow bypass, state machine viola... | `skills/claude-red-offensive-business-logic/SKILL.md` |
| **[`claude-red-offensive-cloud`](skills/claude-red-offensive-cloud/SKILL.md)** | Cloud security attack methodology covering AWS, Azure, and GCP. Includes credential harvesting (IMDS, ~/.aws, en... | `skills/claude-red-offensive-cloud/SKILL.md` |
| **[`claude-red-offensive-container-escape`](skills/claude-red-offensive-container-escape/SKILL.md)** | Container escape and breakout techniques targeting Docker, containerd, and Podman runtimes. Covers privileged co... | `skills/claude-red-offensive-container-escape/SKILL.md` |
| **[`claude-red-offensive-deserialization`](skills/claude-red-offensive-deserialization/SKILL.md)** | Insecure deserialization exploitation across Java, PHP, .NET, Python, Node.js, and Ruby. Covers gadget chain con... | `skills/claude-red-offensive-deserialization/SKILL.md` |
| **[`claude-red-offensive-file-upload`](skills/claude-red-offensive-file-upload/SKILL.md)** | Unrestricted and insecure file upload testing checklist: arbitrary file upload discovery, extension validation b... | `skills/claude-red-offensive-file-upload/SKILL.md` |
| **[`claude-red-offensive-graphql`](skills/claude-red-offensive-graphql/SKILL.md)** | Offensive methodology for attacking GraphQL APIs during penetration tests and bug bounty engagements. Covers the... | `skills/claude-red-offensive-graphql/SKILL.md` |
| **[`claude-red-offensive-idor`](skills/claude-red-offensive-idor/SKILL.md)** | IDOR (Insecure Direct Object Reference) testing checklist: object ID enumeration, horizontal/vertical privilege ... | `skills/claude-red-offensive-idor/SKILL.md` |
| **[`claude-red-offensive-jwt`](skills/claude-red-offensive-jwt/SKILL.md)** | JWT attack methodology for penetration testers. Covers algorithm confusion (alg:none, RS256→HS256), weak HMAC se... | `skills/claude-red-offensive-jwt/SKILL.md` |
| **[`claude-red-offensive-k8s-attacks`](skills/claude-red-offensive-k8s-attacks/SKILL.md)** | Kubernetes cluster attack techniques covering the full attack lifecycle from initial foothold in a pod to cluste... | `skills/claude-red-offensive-k8s-attacks/SKILL.md` |
| **[`claude-red-offensive-oauth`](skills/claude-red-offensive-oauth/SKILL.md)** | OAuth 2.0 attack checklist: authorization code interception, redirect_uri bypass, CSRF on OAuth flow, state para... | `skills/claude-red-offensive-oauth/SKILL.md` |
| **[`claude-red-offensive-open-redirect`](skills/claude-red-offensive-open-redirect/SKILL.md)** | Open redirect vulnerability checklist: parameter identification, bypass techniques (URL encoding, double slashes... | `skills/claude-red-offensive-open-redirect/SKILL.md` |
| **[`claude-red-offensive-parameter-pollution`](skills/claude-red-offensive-parameter-pollution/SKILL.md)** | HTTP parameter pollution (HPP) checklist: duplicate parameter injection, backend vs frontend parsing differences... | `skills/claude-red-offensive-parameter-pollution/SKILL.md` |
| **[`claude-red-offensive-race-condition`](skills/claude-red-offensive-race-condition/SKILL.md)** | Race condition (TOCTOU) testing checklist: identifying timing windows, Burp Suite Turbo Intruder, Last-Byte sync... | `skills/claude-red-offensive-race-condition/SKILL.md` |
| **[`claude-red-offensive-rce`](skills/claude-red-offensive-rce/SKILL.md)** | Remote Code Execution and OS Command Injection testing checklist: shell metacharacter injection (;, |, &&, `, $(... | `skills/claude-red-offensive-rce/SKILL.md` |
| **[`claude-red-offensive-request-smuggling`](skills/claude-red-offensive-request-smuggling/SKILL.md)** | HTTP request smuggling checklist: CL.TE, TE.CL, TE.TE variants, detection with timing and differential responses... | `skills/claude-red-offensive-request-smuggling/SKILL.md` |
| **[`claude-red-offensive-sqli`](skills/claude-red-offensive-sqli/SKILL.md)** | SQL Injection vulnerability testing checklist: In-band (UNION-based, error-based), Inferential (Boolean-blind, T... | `skills/claude-red-offensive-sqli/SKILL.md` |
| **[`claude-red-offensive-ssrf`](skills/claude-red-offensive-ssrf/SKILL.md)** | Server-Side Request Forgery testing checklist: SSRF discovery, blind SSRF with out-of-band, cloud metadata endpo... | `skills/claude-red-offensive-ssrf/SKILL.md` |
| **[`claude-red-offensive-ssti`](skills/claude-red-offensive-ssti/SKILL.md)** | Dense description covering Server-Side Template Injection across Jinja2, Twig, Freemarker, Velocity, Pebble, Sma... | `skills/claude-red-offensive-ssti/SKILL.md` |
| **[`claude-red-offensive-waf-bypass`](skills/claude-red-offensive-waf-bypass/SKILL.md)** | WAF bypass techniques checklist: encoding bypass (URL/HTML/Unicode/double encoding), case variation, comment inj... | `skills/claude-red-offensive-waf-bypass/SKILL.md` |
| **[`claude-red-offensive-xss`](skills/claude-red-offensive-xss/SKILL.md)** | Cross-Site Scripting testing checklist: stored/reflected/DOM/blind XSS discovery, polyglot payloads, CSP bypass,... | `skills/claude-red-offensive-xss/SKILL.md` |
| **[`claude-red-offensive-xxe`](skills/claude-red-offensive-xxe/SKILL.md)** | XML External Entity injection testing checklist: classic XXE, blind XXE (out-of-band), XXE via file upload (SVG/... | `skills/claude-red-offensive-xxe/SKILL.md` |
| **[`claudex`](skills/claudex/SKILL.md)** | Dual-AI adversarial planning loop where two models cross-examine and harden implementation plans through 3 round... | `skills/claudex/SKILL.md` |
| **[`clean-code`](skills/clean-code/SKILL.md)** | Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments | `skills/clean-code/SKILL.md` |
| **[`code-review`](skills/code-review/SKILL.md)** | When the user asks for a code review, shares code for feedback, or says "review this", "check my code", "what's ... | `skills/code-review/SKILL.md` |
| **[`code-review-checklist`](skills/code-review-checklist/SKILL.md)** | Code review guidelines covering code quality, security, and best practices. | `skills/code-review-checklist/SKILL.md` |
| **[`coding-discipline`](skills/coding-discipline/SKILL.md)** | Strict coding discipline based on Karpathy's rules - surgical changes, goal-driven execution, and radical simpli... | `skills/coding-discipline/SKILL.md` |
| **[`cold-outreach`](skills/cold-outreach/SKILL.md)** | When a founder needs to write cold emails or LinkedIn messages to prospects, partners, or investors. Activate wh... | `skills/cold-outreach/SKILL.md` |
| **[`community-discovery`](skills/community-discovery/SKILL.md)** | When the user wants to find Slack groups, Discord servers, Reddit communities, forums, or online communities whe... | `skills/community-discovery/SKILL.md` |
| **[`competitive-analysis`](skills/competitive-analysis/SKILL.md)** | When the user needs to evaluate competitors, understand the competitive landscape, or position their product aga... | `skills/competitive-analysis/SKILL.md` |
| **[`competitor-intel`](skills/competitor-intel/SKILL.md)** | Analyzes competitors using web research to provide verified business metrics, actionable leverage strategies, an... | `skills/competitor-intel/SKILL.md` |
| **[`competitor-monitoring`](skills/competitor-monitoring/SKILL.md)** | When the user wants to set up ongoing tracking of competitor activity — pricing changes, feature launches, hirin... | `skills/competitor-monitoring/SKILL.md` |
| **[`content-strategy`](skills/content-strategy/SKILL.md)** | When the user needs to plan, prioritize, or structure a content program -- including identifying content pillars... | `skills/content-strategy/SKILL.md` |
| **[`contract-review`](skills/contract-review/SKILL.md)** | When the user needs to review an existing contract, assess risk in proposed terms, or evaluate a contract before... | `skills/contract-review/SKILL.md` |
| **[`cro-optimization`](skills/cro-optimization/SKILL.md)** | Analyzes landing pages and provides detailed CRO (Conversion Rate Optimization) recommendations. Use when user p... | `skills/cro-optimization/SKILL.md` |
| **[`daily-product-digest`](skills/daily-product-digest/SKILL.md)** | When the user wants a summary of what's trending on Product Hunt, Hacker News, Indie Hackers, or other product/s... | `skills/daily-product-digest/SKILL.md` |
| **[`data-room`](skills/data-room/SKILL.md)** | When the user wants to prepare a due diligence data room for fundraising, or when an investor has requested addi... | `skills/data-room/SKILL.md` |
| **[`database-design`](skills/database-design/SKILL.md)** | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless data... | `skills/database-design/SKILL.md` |
| **[`deployment-procedures`](skills/deployment-procedures/SKILL.md)** | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verifi... | `skills/deployment-procedures/SKILL.md` |
| **[`diagram-design`](skills/diagram-design/SKILL.md)** | Create branded architecture, architecture delta, IT current-state, flowchart, sequence, state machine, ER/data m... | `skills/diagram-design/SKILL.md` |
| **[`documentation-templates`](skills/documentation-templates/SKILL.md)** | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. | `skills/documentation-templates/SKILL.md` |
| **[`drawdb`](skills/drawdb/SKILL.md)** | Visual entity-relationship diagram (ERD) editor, database schema designer, and multi-dialect SQL generator suppo... | `skills/drawdb/SKILL.md` |
| **[`earned-media-outreach`](skills/earned-media-outreach/SKILL.md)** | When the user wants to get press coverage, appear on podcasts, or build relationships with journalists and conte... | `skills/earned-media-outreach/SKILL.md` |
| **[`email-marketing`](skills/email-marketing/SKILL.md)** | When the user needs to design, write, or optimize email sequences -- including welcome series, nurture campaigns... | `skills/email-marketing/SKILL.md` |
| **[`employer-brand`](skills/employer-brand/SKILL.md)** | When the user needs to create or improve content that shapes how candidates and the public perceive the company ... | `skills/employer-brand/SKILL.md` |
| **[`event-hosting`](skills/event-hosting/SKILL.md)** | When the user wants to host a tech event, meetup, workshop, or community gathering — especially using Luma. Also... | `skills/event-hosting/SKILL.md` |
| **[`fast-check`](skills/fast-check/SKILL.md)** | Use esta skill para validar rapidamente tipagem, lint e testes locais sem poluir a janela de contexto com logs g... | `skills/fast-check/SKILL.md` |
| **[`feedback-synthesis`](skills/feedback-synthesis/SKILL.md)** | When the user needs to analyze, categorize, or extract actionable insights from customer feedback across multipl... | `skills/feedback-synthesis/SKILL.md` |
| **[`find-skills`](skills/find-skills/SKILL.md)** | Discovers, recommends, and installs agent skills from the open skills ecosystem (skills.sh, npx skills, GitHub).... | `skills/find-skills/SKILL.md` |
| **[`founder-board`](skills/founder-board/SKILL.md)** | >- | `skills/founder-board/SKILL.md` |
| **[`founder-brand`](skills/founder-brand/SKILL.md)** | >- | `skills/founder-brand/SKILL.md` |
| **[`founder-cfo`](skills/founder-cfo/SKILL.md)** | >- | `skills/founder-cfo/SKILL.md` |
| **[`founder-competitors`](skills/founder-competitors/SKILL.md)** | >- | `skills/founder-competitors/SKILL.md` |
| **[`founder-consumer`](skills/founder-consumer/SKILL.md)** | >- | `skills/founder-consumer/SKILL.md` |
| **[`founder-launch`](skills/founder-launch/SKILL.md)** | >- | `skills/founder-launch/SKILL.md` |
| **[`founder-marketing`](skills/founder-marketing/SKILL.md)** | >- | `skills/founder-marketing/SKILL.md` |
| **[`founder-offer`](skills/founder-offer/SKILL.md)** | >- | `skills/founder-offer/SKILL.md` |
| **[`founder-ops`](skills/founder-ops/SKILL.md)** | >- | `skills/founder-ops/SKILL.md` |
| **[`founder-plan`](skills/founder-plan/SKILL.md)** | >- | `skills/founder-plan/SKILL.md` |
| **[`founder-pricing`](skills/founder-pricing/SKILL.md)** | >- | `skills/founder-pricing/SKILL.md` |
| **[`founder-thought-leadership`](skills/founder-thought-leadership/SKILL.md)** | When the user wants to build personal brand, thought leadership, or IP as a founder on Twitter/X or LinkedIn. Al... | `skills/founder-thought-leadership/SKILL.md` |
| **[`free-claude-code`](skills/free-claude-code/SKILL.md)** | Guidance for setting up and using the Free Claude Code (FCC) proxy tool to route Claude Code, Cline, Aider, and ... | `skills/free-claude-code/SKILL.md` |
| **[`freellmapi`](skills/freellmapi/SKILL.md)** | Unified proxy gateway aggregating 34 free LLM providers, 635 free model endpoints, and ~7.4 billion free tokens/... | `skills/freellmapi/SKILL.md` |
| **[`frontend-design`](skills/frontend-design/SKILL.md)** | Design thinking and decision-making for web UI. Use when designing components, layouts, color schemes, typograph... | `skills/frontend-design/SKILL.md` |
| **[`fundraising-email`](skills/fundraising-email/SKILL.md)** | When the user wants to write an email to an investor — cold outreach, warm intro request, follow-up after a meet... | `skills/fundraising-email/SKILL.md` |
| **[`game-development`](skills/game-development/SKILL.md)** | Game development orchestrator. Routes to platform-specific skills based on project needs. | `skills/game-development/SKILL.md` |
| **[`geo-fundamentals`](skills/geo-fundamentals/SKILL.md)** | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). | `skills/geo-fundamentals/SKILL.md` |
| **[`go-to-market-plan`](skills/go-to-market-plan/SKILL.md)** | Analyzes the founder's business context to deliver 3 best go-to-market strategies tailored to their current stag... | `skills/go-to-market-plan/SKILL.md` |
| **[`graphify`](skills/graphify/SKILL.md)** | Multimodal Knowledge Graph builder for codebases, documents, research papers, and images. Extracts concepts, det... | `skills/graphify/SKILL.md` |
| **[`i18n-localization`](skills/i18n-localization/SKILL.md)** | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files... | `skills/i18n-localization/SKILL.md` |
| **[`image-to-code`](skills/image-to-code/SKILL.md)** | Multimodal AI converter translating UI mockups, screenshots, whiteboard wireframes, and design images directly i... | `skills/image-to-code/SKILL.md` |
| **[`impeccable-design`](skills/impeccable-design/SKILL.md)** | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize,... | `skills/impeccable-design/SKILL.md` |
| **[`intelligent-routing`](skills/intelligent-routing/SKILL.md)** | Automatic agent selection and intelligent task routing. Analyzes user requests and automatically selects the bes... | `skills/intelligent-routing/SKILL.md` |
| **[`interview-kit`](skills/interview-kit/SKILL.md)** | When the user needs to design an interview process, create interview questions, build scorecards, calibrate inte... | `skills/interview-kit/SKILL.md` |
| **[`investor-research`](skills/investor-research/SKILL.md)** | When the user wants to identify, evaluate, or prioritize potential investors for a fundraising round. Also activ... | `skills/investor-research/SKILL.md` |
| **[`job-description`](skills/job-description/SKILL.md)** | When the user needs to write, review, or improve a job posting for a startup role. | `skills/job-description/SKILL.md` |
| **[`knowledge-base`](skills/knowledge-base/SKILL.md)** | Protocolo de consulta à base AllMight para busca de padrões, templates e arquitetura. | `skills/knowledge-base/SKILL.md` |
| **[`landing-page`](skills/landing-page/SKILL.md)** | When the user needs to create, critique, or optimize a landing page for conversion -- including headline rewrite... | `skills/landing-page/SKILL.md` |
| **[`launch-strategy`](skills/launch-strategy/SKILL.md)** | When the user needs to plan or execute a product launch — including pre-launch content sequences, launch funnels... | `skills/launch-strategy/SKILL.md` |
| **[`laws-of-ux`](skills/laws-of-ux/SKILL.md)** | Psychology-based design principles, cognitive heuristics, diagnostic decision trees, and usability laws (Jon Yab... | `skills/laws-of-ux/SKILL.md` |
| **[`laya`](skills/laya/SKILL.md)** | Guidance for integrating and using Laya, an open-source System 1 decision model by Convai Innovations, inside No... | `skills/laya/SKILL.md` |
| **[`laya-nandha`](skills/laya-nandha/SKILL.md)** | Guidance for integrating and using the Python implementation of Laya (NandhaKishorM/laya), a multilingual System... | `skills/laya-nandha/SKILL.md` |
| **[`lead-magnet-generator`](skills/lead-magnet-generator/SKILL.md)** | Creates viral lead magnet posts that drive comments and DMs. Produces 2 versions - a quick punchy format and a d... | `skills/lead-magnet-generator/SKILL.md` |
| **[`lead-scoring`](skills/lead-scoring/SKILL.md)** | When a founder needs to qualify inbound leads, define their ICP, build a lead scoring model, set MQL criteria, o... | `skills/lead-scoring/SKILL.md` |
| **[`linkedin-writer`](skills/linkedin-writer/SKILL.md)** | Creates viral LinkedIn posts using proven formats, post templates, and voice matching. Use when user needs engag... | `skills/linkedin-writer/SKILL.md` |
| **[`lint-and-validate`](skills/lint-and-validate/SKILL.md)** | Automatic quality control, linting, and static analysis procedures. Use after every code modification to ensure ... | `skills/lint-and-validate/SKILL.md` |
| **[`LlamaFactory`](skills/LlamaFactory/SKILL.md)** | Guidance for integrating and using LLaMA-Factory, a zero-code fine-tuning framework for LLMs. Use this skill whe... | `skills/LlamaFactory/SKILL.md` |
| **[`loop-engineering`](skills/loop-engineering/SKILL.md)** | Design, audit, run, and bound autonomous AI agent loops (autoloop, loopy, Copilot agent-loop). Prevents runaway ... | `skills/loop-engineering/SKILL.md` |
| **[`manual-generator`](skills/manual-generator/SKILL.md)** | Guidance for using manual-generator, a Crystal program to generate PDF manuals from HTML documentation sites. Us... | `skills/manual-generator/SKILL.md` |
| **[`market-research`](skills/market-research/SKILL.md)** | When the user needs to estimate market size, understand market dynamics, or validate that a market opportunity i... | `skills/market-research/SKILL.md` |
| **[`marketing-ideas`](skills/marketing-ideas/SKILL.md)** | Produces the best marketing ideas for your business by analyzing your FOUNDER_CONTEXT and matching it against a ... | `skills/marketing-ideas/SKILL.md` |
| **[`mcp-builder`](skills/mcp-builder/SKILL.md)** | MCP (Model Context Protocol) server building principles. Tool design, resource patterns, best practices. | `skills/mcp-builder/SKILL.md` |
| **[`media-inference-worker`](skills/media-inference-worker/SKILL.md)** | Higgsfield AI media inference pipeline worker for cutting-edge text-to-image and text-to-video models (Qwen-Imag... | `skills/media-inference-worker/SKILL.md` |
| **[`mobile-design`](skills/mobile-design/SKILL.md)** | Mobile-first design thinking and decision-making for iOS and Android apps. Touch interaction, performance patter... | `skills/mobile-design/SKILL.md` |
| **[`MoneyPrinterTurbo`](skills/MoneyPrinterTurbo/SKILL.md)** | Guidance for integrating and using MoneyPrinterTurbo, an All-in-One AI Short Video Generator. Use this skill whe... | `skills/MoneyPrinterTurbo/SKILL.md` |
| **[`musica`](skills/musica/SKILL.md)** | Guidance for integrating and using Musica VJ, an open-source AI DJ + VJ desktop application built in Rust and Ta... | `skills/musica/SKILL.md` |
| **[`mvp-scoping`](skills/mvp-scoping/SKILL.md)** | When the user needs to decide what to build, cut, and defer for a first release or minimum viable version of a p... | `skills/mvp-scoping/SKILL.md` |
| **[`nextjs-react-expert`](skills/nextjs-react-expert/SKILL.md)** | React and Next.js performance optimization from Vercel Engineering. Use when building React components, optimizi... | `skills/nextjs-react-expert/SKILL.md` |
| **[`nodejs-best-practices`](skills/nodejs-best-practices/SKILL.md)** | Node.js development principles and decision-making. Framework selection, async patterns, security, and architect... | `skills/nodejs-best-practices/SKILL.md` |
| **[`onboarding-flow`](skills/onboarding-flow/SKILL.md)** | When the user needs to design, improve, or audit a post-signup activation flow to get new users to their first v... | `skills/onboarding-flow/SKILL.md` |
| **[`open-generative-ai`](skills/open-generative-ai/SKILL.md)** | Guidance for integrating Open Generative AI, an open-source alternative to AI Video/Image Platforms using MuAPI.... | `skills/open-generative-ai/SKILL.md` |
| **[`open-seo`](skills/open-seo/SKILL.md)** | Open-source Semrush and Ahrefs alternative with native MCP server and Agent Skills for keyword research, backlin... | `skills/open-seo/SKILL.md` |
| **[`outreach-specialist`](skills/outreach-specialist/SKILL.md)** | Crafts high-converting outreach messages and email sequences for cold outreach, LinkedIn DMs, and follow-ups. Us... | `skills/outreach-specialist/SKILL.md` |
| **[`parallel-agents`](skills/parallel-agents/SKILL.md)** | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise ... | `skills/parallel-agents/SKILL.md` |
| **[`partnership-outreach`](skills/partnership-outreach/SKILL.md)** | When a founder needs to write partnership or BD emails, craft integration pitches, or create co-marketing propos... | `skills/partnership-outreach/SKILL.md` |
| **[`performance-profiling`](skills/performance-profiling/SKILL.md)** | Performance profiling principles. Measurement, analysis, and optimization techniques. | `skills/performance-profiling/SKILL.md` |
| **[`pitch-deck`](skills/pitch-deck/SKILL.md)** | When the user wants to create, review, or restructure a fundraising pitch deck for seed or Series A. Also activa... | `skills/pitch-deck/SKILL.md` |
| **[`plan-writing`](skills/plan-writing/SKILL.md)** | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing f... | `skills/plan-writing/SKILL.md` |
| **[`playwright-cli`](skills/playwright-cli/SKILL.md)** | Token-efficient Playwright CLI browser automation and testing designed specifically for coding agents. Executes ... | `skills/playwright-cli/SKILL.md` |
| **[`ponytail`](skills/ponytail/SKILL.md)** | > | `skills/ponytail/SKILL.md` |
| **[`ponytail-audit`](skills/ponytail-audit/SKILL.md)** | > | `skills/ponytail-audit/SKILL.md` |
| **[`ponytail-debt`](skills/ponytail-debt/SKILL.md)** | > | `skills/ponytail-debt/SKILL.md` |
| **[`ponytail-gain`](skills/ponytail-gain/SKILL.md)** | > | `skills/ponytail-gain/SKILL.md` |
| **[`ponytail-help`](skills/ponytail-help/SKILL.md)** | > | `skills/ponytail-help/SKILL.md` |
| **[`ponytail-review`](skills/ponytail-review/SKILL.md)** | > | `skills/ponytail-review/SKILL.md` |
| **[`powershell-windows`](skills/powershell-windows/SKILL.md)** | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. | `skills/powershell-windows/SKILL.md` |
| **[`prd-generator`](skills/prd-generator/SKILL.md)** | Generates professional PRD (Product Requirements Document) files optimized for AI coding tools. Takes a rough pr... | `skills/prd-generator/SKILL.md` |
| **[`prd-writing`](skills/prd-writing/SKILL.md)** | When the user needs to define a product feature, write a product requirements document, or translate an idea int... | `skills/prd-writing/SKILL.md` |
| **[`pre-mortem`](skills/pre-mortem/SKILL.md)** | Cognitive risk discovery and failure anticipation methodology. Run before writing code or launching features: as... | `skills/pre-mortem/SKILL.md` |
| **[`pricing-strategist`](skills/pricing-strategist/SKILL.md)** | Builds comprehensive pricing strategies by reading business context and asking targeted questions interactively.... | `skills/pricing-strategist/SKILL.md` |
| **[`privacy-policy`](skills/privacy-policy/SKILL.md)** | When the user needs to draft, review, or update a privacy policy for their product, or needs to understand data ... | `skills/privacy-policy/SKILL.md` |
| **[`process-docs`](skills/process-docs/SKILL.md)** | When the user needs to create SOPs, playbooks, runbooks, or other operational documentation that defines how a r... | `skills/process-docs/SKILL.md` |
| **[`product-hunt-launch-plan`](skills/product-hunt-launch-plan/SKILL.md)** | Creates a comprehensive, personalized Product Hunt launch plan to rank #1. Use when user needs a step-by-step Pr... | `skills/product-hunt-launch-plan/SKILL.md` |
| **[`product-launch-motion`](skills/product-launch-motion/SKILL.md)** | Guidance for creating programmatic product launch videos from code using HTML, CSS, and GSAP. Use this skill whe... | `skills/product-launch-motion/SKILL.md` |
| **[`proposal-generation`](skills/proposal-generation/SKILL.md)** | When a founder needs to create a sales proposal, statement of work, contract, NDA, or master service agreement. ... | `skills/proposal-generation/SKILL.md` |
| **[`public-apis`](skills/public-apis/SKILL.md)** | A collective list of free APIs for use in software and web development. Use this skill as a knowledge base when ... | `skills/public-apis/SKILL.md` |
| **[`python-patterns`](skills/python-patterns/SKILL.md)** | Python development principles and decision-making. Framework selection, async patterns, type hints, project stru... | `skills/python-patterns/SKILL.md` |
| **[`rea`](skills/rea/SKILL.md)** | REA (Reverse Engineer Anything): One MCP for reverse engineering across binaries, applications, and runtime beha... | `skills/rea/SKILL.md` |
| **[`red-team-tactics`](skills/red-team-tactics/SKILL.md)** | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. | `skills/red-team-tactics/SKILL.md` |
| **[`replicate-build-models`](skills/replicate-build-models/SKILL.md)** | > | `skills/replicate-build-models/SKILL.md` |
| **[`replicate-compare-models`](skills/replicate-compare-models/SKILL.md)** | Compare Replicate models by cost, speed, quality, and capabilities. | `skills/replicate-compare-models/SKILL.md` |
| **[`replicate-find-models`](skills/replicate-find-models/SKILL.md)** | Find AI models on Replicate using search and curated collections. | `skills/replicate-find-models/SKILL.md` |
| **[`replicate-prompt-images`](skills/replicate-prompt-images/SKILL.md)** | > | `skills/replicate-prompt-images/SKILL.md` |
| **[`replicate-prompt-videos`](skills/replicate-prompt-videos/SKILL.md)** | > | `skills/replicate-prompt-videos/SKILL.md` |
| **[`replicate-publish-models`](skills/replicate-publish-models/SKILL.md)** | > | `skills/replicate-publish-models/SKILL.md` |
| **[`replicate-run-models`](skills/replicate-run-models/SKILL.md)** | Run AI models on Replicate via predictions, webhooks, and streaming. | `skills/replicate-run-models/SKILL.md` |
| **[`reverse-skill`](skills/reverse-skill/SKILL.md)** | Cybersecurity Skills Router and Reverse Engineering framework for AI agents. Routes tasks across APK decompilati... | `skills/reverse-skill/SKILL.md` |
| **[`review-mining`](skills/review-mining/SKILL.md)** | When the user wants to research customer pain points, complaints, or sentiment using review platforms like Trust... | `skills/review-mining/SKILL.md` |
| **[`roadmap-planning`](skills/roadmap-planning/SKILL.md)** | When the user needs to organize product initiatives into a prioritized, time-sequenced plan with outcomes and de... | `skills/roadmap-planning/SKILL.md` |
| **[`ruflo`](skills/ruflo/SKILL.md)** | Ruflo is a multi-agent orchestration platform for AI coding agents (Claude Code, Cursor, Codex, Copilot, Gemini,... | `skills/ruflo/SKILL.md` |
| **[`rust-pro`](skills/rust-pro/SKILL.md)** | Master Rust 1.75+ with modern async patterns, advanced type system | `skills/rust-pro/SKILL.md` |
| **[`ruview`](skills/ruview/SKILL.md)** | Guidance for integrating and using RuView (WiFi DensePose), an MCP server and WiFi sensing platform that turns o... | `skills/ruview/SKILL.md` |
| **[`sales-script`](skills/sales-script/SKILL.md)** | When a founder needs demo scripts, discovery call frameworks, objection handling, RFP/RFI responses, competitive... | `skills/sales-script/SKILL.md` |
| **[`security-audit`](skills/security-audit/SKILL.md)** | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use... | `skills/security-audit/SKILL.md` |
| **[`security-review`](skills/security-review/SKILL.md)** | When the user needs a security assessment — threat modeling, vulnerability review, auth flow audit, dependency s... | `skills/security-review/SKILL.md` |
| **[`sentiment-monitoring`](skills/sentiment-monitoring/SKILL.md)** | When the user wants to monitor reviews, mentions, and community sentiment about their own product. Also use when... | `skills/sentiment-monitoring/SKILL.md` |
| **[`seo-fundamentals`](skills/seo-fundamentals/SKILL.md)** | SEO fundamentals, E-E-A-T, Core Web Vitals, and Google algorithm principles. | `skills/seo-fundamentals/SKILL.md` |
| **[`seo-technical`](skills/seo-technical/SKILL.md)** | When the user needs a technical SEO audit, on-page optimization guidance, or help resolving crawlability, indexa... | `skills/seo-technical/SKILL.md` |
| **[`server-management`](skills/server-management/SKILL.md)** | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions... | `skills/server-management/SKILL.md` |
| **[`soc2-prep`](skills/soc2-prep/SKILL.md)** | When the user needs to prepare for SOC 2, build a compliance roadmap, assess security posture, quantify security... | `skills/soc2-prep/SKILL.md` |
| **[`social-content`](skills/social-content/SKILL.md)** | When the user needs to build a LinkedIn authority system, create social content strategy, define content pillars... | `skills/social-content/SKILL.md` |
| **[`sop-creator`](skills/sop-creator/SKILL.md)** | Creates detailed Standard Operating Procedures (SOPs) for business processes. Use when user needs SOPs, process ... | `skills/sop-creator/SKILL.md` |
| **[`sourcing-outreach`](skills/sourcing-outreach/SKILL.md)** | When the user needs to write recruiting outreach messages to attract passive candidates or request referrals. | `skills/sourcing-outreach/SKILL.md` |
| **[`spec-kit`](skills/spec-kit/SKILL.md)** | GitHub's official Spec-Driven Development (SDD) toolkit for AI coding agents. Provides structured processes for ... | `skills/spec-kit/SKILL.md` |
| **[`startup-context`](skills/startup-context/SKILL.md)** | When the user wants to create or update their startup context document. Also use when the user mentions "set up ... | `skills/startup-context/SKILL.md` |
| **[`strategic-planning`](skills/strategic-planning/SKILL.md)** | Analyzes the founder's business context to deliver the 3 highest-impact next moves for growth (marketing or sale... | `skills/strategic-planning/SKILL.md` |
| **[`support-docs`](skills/support-docs/SKILL.md)** | When the user needs to create help center articles, FAQs, troubleshooting guides, API documentation, or getting-... | `skills/support-docs/SKILL.md` |
| **[`system-audit`](skills/system-audit/SKILL.md)** | Comprehensive checklists and methodology for software system auditing, diagnostics, and verification. Based on u... | `skills/system-audit/SKILL.md` |
| **[`systematic-debugging`](skills/systematic-debugging/SKILL.md)** | 4-phase systematic debugging methodology with root cause analysis and evidence-based verification. Use when debu... | `skills/systematic-debugging/SKILL.md` |
| **[`tailwind-patterns`](skills/tailwind-patterns/SKILL.md)** | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. | `skills/tailwind-patterns/SKILL.md` |
| **[`taste-skill`](skills/taste-skill/SKILL.md)** | Anti-slop frontend framework for AI agents. Eliminates generic boilerplate UIs by enforcing sophisticated layout... | `skills/taste-skill/SKILL.md` |
| **[`tdd-workflow`](skills/tdd-workflow/SKILL.md)** | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. | `skills/tdd-workflow/SKILL.md` |
| **[`tech-stack-eval`](skills/tech-stack-eval/SKILL.md)** | When the user needs to choose between technologies, frameworks, or tools — or says "which framework should I use... | `skills/tech-stack-eval/SKILL.md` |
| **[`terms-of-service`](skills/terms-of-service/SKILL.md)** | When the user needs to draft, review, or update terms of service for their SaaS product or web application. | `skills/terms-of-service/SKILL.md` |
| **[`testing-patterns`](skills/testing-patterns/SKILL.md)** | Testing patterns and principles. Unit, integration, mocking strategies. | `skills/testing-patterns/SKILL.md` |
| **[`user-research-synthesis`](skills/user-research-synthesis/SKILL.md)** | When the user has raw customer interview transcripts, survey responses, support tickets, or other qualitative da... | `skills/user-research-synthesis/SKILL.md` |
| **[`viral-hook-creator`](skills/viral-hook-creator/SKILL.md)** | Creates viral social media hooks using proven psychological patterns and trigger words. Use when user needs atte... | `skills/viral-hook-creator/SKILL.md` |
| **[`vulnerability-scanner`](skills/vulnerability-scanner/SKILL.md)** | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prio... | `skills/vulnerability-scanner/SKILL.md` |
| **[`wa-akg`](skills/wa-akg/SKILL.md)** | Professional multi-session WhatsApp Gateway, Dashboard, and Automation System powered by Next.js 15, Baileys (@w... | `skills/wa-akg/SKILL.md` |
| **[`web-design-guidelines`](skills/web-design-guidelines/SKILL.md)** | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility",... | `skills/web-design-guidelines/SKILL.md` |
| **[`webapp-testing`](skills/webapp-testing/SKILL.md)** | Web application testing principles. E2E, Playwright, deep audit strategies. | `skills/webapp-testing/SKILL.md` |
| **[`x-writer`](skills/x-writer/SKILL.md)** | Creates viral X (Twitter) posts using proven formats, post templates, and creator voice matching. Use when user ... | `skills/x-writer/SKILL.md` |

---

## 🔄 Interactive Workflows (17)

| Command | Description | Path |
| :--- | :--- | :--- |
| **`/audit`** | Realizar auditoria técnica completa de segurança, performance e arquitetura. | [`workflows/audit.md`](workflows/audit.md) |
| **`/brainstorm`** | Brainstorming estruturado para projetos e recursos. Explora múltiplas opções antes da implementação. | [`workflows/brainstorm.md`](workflows/brainstorm.md) |
| **`/brainstorm1`** | BrainStorm - Extrai contexto, explora opções de conservadora a não-convencional, pontua em 5 dimensões (esforço, risco, reversibilidade, tempo de valor, fit) e entrega recomendação direta com caso dissidente e premissa a validar. | [`workflows/brainstorm1.md`](workflows/brainstorm1.md) |
| **`/create`** | Comando para criar nova aplicação. Aciona a skill App Builder e inicia diálogo interativo. | [`workflows/create.md`](workflows/create.md) |
| **`/debug`** | Comando de depuração. Ativa o modo DEBUG para investigação sistemática de problemas seguindo o protocolo de Engenheiro Sênior. | [`workflows/debug.md`](workflows/debug.md) |
| **`/deploy`** | Comando de implantação para lançamentos de produção. Verificações pré-voo e execução da implantação. | [`workflows/deploy.md`](workflows/deploy.md) |
| **`/diagnose`** | Realizar diagnóstico rápido de stack, estrutura e status funcional do sistema. | [`workflows/diagnose.md`](workflows/diagnose.md) |
| **`/enhance`** | Adicionar ou atualizar recursos em aplicação existente. Usado para desenvolvimento iterativo. | [`workflows/enhance.md`](workflows/enhance.md) |
| **`/kb`** | Busca na biblioteca AllMight. Encontra padrões, documentos e conhecimento técnico. | [`workflows/kb.md`](workflows/kb.md) |
| **`/learn`** | Aprender novo conhecimento extraindo documentação de um link (Web to MD). | [`workflows/learn.md`](workflows/learn.md) |
| **`/orchestrate`** | Coordenar múltiplos agentes para tarefas complexas. Permite análises multi-perspectiva e revisões abrangentes. | [`workflows/orchestrate.md`](workflows/orchestrate.md) |
| **`/orchestrate1`** | Orquestra agentes especializados com avaliação de complexidade em 3 tiers, grafo de dependências, quality gates por agente, protocolo de falha e rollback. Produz relatório unificado com rastreabilidade completa de decisões. | [`workflows/orchestrate1.md`](workflows/orchestrate1.md) |
| **`/plan`** | Criar plano de projeto usando o agente project-planner seguindo o protocolo de Modo Planejador Sênior. | [`workflows/plan.md`](workflows/plan.md) |
| **`/preview`** | Gerenciamento do servidor de visualização. Iniciar, parar e check de status do servidor local. | [`workflows/preview.md`](workflows/preview.md) |
| **`/status`** | Exibir status do agente e do projeto. Acompanhamento de progresso e quadro de status. | [`workflows/status.md`](workflows/status.md) |
| **`/test`** | Comando de geração e execução de testes. Cria e executa testes para o código. | [`workflows/test.md`](workflows/test.md) |
| **`/ui-ux-pro-max`** | Planejar e implementar interfaces UI/UX com 50+ estilos e paletas premium. | [`workflows/ui-ux-pro-max.md`](workflows/ui-ux-pro-max.md) |

---

## 🛠️ Execution & Tooling Suite (`.agent/scripts/`)

The consolidated script layer powers the system via **`agent-cli.py`** and modular utilities:

- **`agent-cli.py`**: Unified operational entrypoint for all subsystems (`healthcheck`, `checklist`, `preview`, `session`, `update`, `skills`).
- **`_common.py`**: Shared ANSI colors, loggers, safe Windows UTF-8 runner, and manifest loader.
- **`healthcheck.py`**: Dynamic auditor classifying skills (`READY`, `PLAYBOOK`, `BLOCKED`, `BROKEN`) and computing agent token taxes.
- **`checklist.py`**: Unified verification suite with `--full` flag covering Security, Quality, Schema, Test, UX, A11y, SEO, GEO, Mobile, and i18n.
- **`safety_gate.py`**: Interceptor blocking destructive commands across Windows PowerShell, CMD, Git, K8s, AWS, Azure, and GCP.
- **`session_manager.py`**: Project state analyzer detecting Node.js, Python (FastAPI/Django/Flask), Flutter, and PHP stacks.
- **`auto_preview.py`**: Multi-framework dev server manager persisting port, PID, and URL in `.agent/preview.json`.
- **`updater.py`**: Upstream repository auditor checking commits with GitHub API and `GITHUB_TOKEN` support.

---

## 📊 Verified System Statistics

| Metric | Current Count | Verification Source |
| :--- | :---: | :--- |
| **Specialist Agents** | `21` | `agents/*.md` |
| **Super Skills** | `191` | `skills/*/SKILL.md` |
| **Workflows** | `17` | `workflows/*.md` |
| **Master Scripts** | `10` | `.agent/scripts/*.py` |
| **Skill-Level Scripts** | `416` | `skills/*/scripts/*` |
| **Healthcheck Status** | `100% Validated` | `skills_manifest.json` |

---
