<div align="center">

# ⚡ AllMight-Core
### Sistema Operacional Cognitivo & Suíte de Agentes Autônomos de Engenharia

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Skills: 192 Active](https://img.shields.io/badge/Agent%20Skills-192%20Active-success.svg)](.agent/skills/)
[![Knowledge: v5.0](https://img.shields.io/badge/Knowledge%20Base-v5.0%20(SQLite%20FTS5)-orange.svg)](.agent/knowledge/)
[![Python: 3.12+](https://img.shields.io/badge/Python-3.12%20%7C%203.13-yellow.svg)](https://python.org)
[![Node.js: 20+](https://img.shields.io/badge/Node.js-20+-green.svg)](https://nodejs.org)

<p align="center">
  <b>Transforme qualquer IDE e modelo de IA em uma equipe de Engenharia de Software de nível Staff.</b><br>
  Memória persistente, 192 habilidades operacionais, base enciclopédica ultraleve e orquestração multi-provedor.
</p>

</div>

---

## 🌟 O que é o AllMight-Core?

O **AllMight-Core** é um framework modular de **Engenharia de Software Autônoma Assistida por IA**. Mais do que uma simples coleção de prompts, o AllMight-Core opera como uma **camada de inteligência desacoplada e portátil**:

* 🧠 **192 Skills de Especialistas:** Habilidades ativadas sob demanda cobrindo Arquitetura de Software, Clean Code (Diretrizes Karpathy), Testes E2E (Playwright), Pentest/Segurança Ofensiva (OWASP Top 10), Modelos de IA e Negócios/Startups.
* 📚 **Knowledge Engine v5.0:** Acervo enciclopédico de mais de **1.440 manuais técnicos canônicos**, 100% padronizados com **JSON Front Matter** (`---json`), roteamento hierárquico em YAML e motor de busca semântico nativo com **SQLite FTS5 e algoritmo BM25**.
* 🛠️ **Suíte de Aplicações Executáveis (`apps/`):** Hub de ferramentas integradas e plug-and-play, incluindo **OpenCode v2** (agente de terminal compatível com Claude Code), **LlamaFactory** (fine-tuning local) e **FreeLLMAPIs** (fallback automático entre 30+ provedores gratuitos de LLM).
* 🎯 **Disciplina e Modos de Operação:** Governança estrita com 4 personas operacionais (*Arquiteto, Planejador, Executor e Depurador*) para garantir código limpo, sem regressões e com zero desperdício de tokens.

---

## 🏗️ Arquitetura do Repositório

```plaintext
AllMight-Core/
├── .agent/                    # Cérebro Cognitivo do Ecossistema
│   ├── knowledge/             # Base de Conhecimento v5.0 (1.440+ manuais em ---json)
│   │   ├── _dados/            # SQLite FTS5 (knowledge.sqlite) e Catálogos CSV
│   │   ├── _meta/             # Roteador Mestre YAML e Scripts de Validação/Build
│   │   └── 01 a 08/           # 8 Macrodomínios (Gestão, IA, Linguagens, Frameworks, etc.)
│   ├── rules/                 # Diretrizes Karpathy, Modos de Operação e Routing
│   ├── skills/                # Catálogo de 192 Habilidades de Engenharia
│   └── scripts/               # Rotinas de manutenção e diagnósticos de ambiente
│
├── apps/                      # Ferramentas Executáveis Integradas (Plug-and-Play)
│   ├── opencode/              # Agente de Código para Terminal TUI (alternativa Claude Code)
│   ├── LlamaFactory/          # Pipeline de Treinamento e Fine-Tuning de LLMs locais
│   ├── freellmapi/            # Roteador unificado de provedores gratuitos de IA
│   ├── MoneyPrinterTurbo/     # Automação e geração programática de mídia
│   └── launcher.bat           # Launcher unificado para Windows e Linux
│
├── update/                    # Blueprints técnicos e roadmaps de evolução contínua
├── AGENTS.md                  # Manifesto de diretrizes operacionais do agente
├── CLAUDE.md                  # Guia de pareamento rápido para Claude Code / OpenCode
├── agent.bat                  # Inicializador rápido de linha de comando
└── sync.bat                   # Sincronizador de compatibilidade para Google Antigravity IDE
```

---

## ⚡ Início Rápido

### 1. Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/AllMight-Core.git
cd AllMight-Core
```

### 2. Sincronizar o Ambiente (Windows / Linux)
Execute o script de sincronização para garantir as junctions da IDE e validação das regras:
```cmd
sync.bat
```

### 3. Iniciar o Assistente de Terminal (OpenCode v2)
O ecossistema já vem com o **OpenCode v2** pronto para uso (com suporte a Claude, GPT, Gemini, DeepSeek e Ollama):
```cmd
apps\opencode\iniciar.bat
```
> Dentro do OpenCode, digite `/connect` para configurar suas chaves de API com segurança.

---

## 🧭 Os 4 Modos de Operação

O agente adapta sua postura automaticamente com base no comando recebido:

| Modo | Foco Principal | Saída Esperada |
| :--- | :--- | :--- |
| **🏗️ Arquiteto** | Decisões de alto nível, estrutura de pastas e contratos | Documentos de Design, ADRs e Diagramas (Zero código) |
| **📋 Planejador** | Mapeamento cirúrgico de impacto antes da execução | Perguntas esclarecedoras e Roadmap aprovado em fases |
| **💻 Executor** | Implementação limpa e precisa seguindo o plano | Código funcional, testes passando e commits atômicos |
| **🐞 Depurador** | Investigação científica da causa raiz | Hipóteses testadas, logs direcionados e correção validada |

---

## 🔍 Motor de Busca de Conhecimento (SQLite FTS5)

A base de conhecimento em `.agent/knowledge` não realiza varreduras lentas de texto em disco. Ela conta com um banco local SQLite compilado com **Full-Text Search (FTS5)**:

```python
# Consulta instantânea (< 2ms)
import sqlite3
conn = sqlite3.connect(".agent/knowledge/_dados/knowledge.sqlite")
cur = conn.cursor()

# Busca por relevância BM25 com suporte a acentos
cur.execute("SELECT id, caminho, bm25(rotas) FROM rotas WHERE rotas MATCH '\"laravel\"' LIMIT 3;")
print(cur.fetchall())
```

---

## 🧰 Catálogo de Skills (192 Habilidades)

O AllMight-Core utiliza **Divulgação Progressiva (Progressive Disclosure)**: as skills são carregadas somente quando necessárias, economizando até 90% da janela de contexto.

* **Arquitetura & Código (30):** `clean-code`, `database-design`, `api-patterns`, `rust-pro`, `python-patterns`.
* **Qualidade & Testes (22):** `systematic-debugging`, `playwright-cli`, `fast-check`, `tdd-workflow`.
* **Frontend & Design (59):** `taste-skill`, `laws-of-ux`, `tailwind-patterns`, `react-best-practices`.
* **Segurança Ofensiva (42):** `security-audit`, `vulnerability-scanner`, `red-team-tactics`, `offensive-ssti`.
* **Modelos de IA & Multi-Agentes (7):** `ruflo`, `parallel-agents`, `mcp-builder`, `airllm`, `LlamaFactory`.
* **Produto, Negócios & Growth (32):** `mvp-scoping`, `prd-generator`, `pitch-deck`, `open-seo`, `brand-copywriter`.

👉 *Consulte o catálogo completo em [`CATALOGO_SKILLS.md`](.agent/CATALOGO_SKILLS.md).*

---

## 🤝 Como Contribuir

1. Faça um Fork do projeto.
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/nova-skill`).
3. Certifique-se de que os testes e a validação passem:
   ```bash
   python .agent/knowledge/_meta/build/validar.py
   ```
4. Envie seu Pull Request!

---

<div align="center">
  <sub>Construído com obsessão por código limpo, arquitetura desacoplada e autonomia de agentes.</sub>
</div>
