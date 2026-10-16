---
name: playwright-cli
description: "Token-efficient Playwright CLI browser automation and testing designed specifically for coding agents. Executes concise commands (open, click, type, screenshot) without dumping verbose DOM trees into LLM context."
---

# Playwright CLI — Token-Efficient Browser Automation for Coding Agents

**playwright-cli** is Microsoft's official CLI interface into Playwright engineered specifically for **AI Coding Agents** (Claude Code, Antigravity, GitHub Copilot, Codex). 

- **Upstream Repository:** [https://github.com/microsoft/playwright-cli](https://github.com/microsoft/playwright-cli)
- **Primary Benefit:** **Ultra token-efficient.** Unlike heavy browser MCP servers that flood the LLM context window with huge accessibility trees and DOM snapshots, `playwright-cli` executes concise, high-throughput commands with zero context bloat.

---

## ⚡ CLI vs MCP: The Context Window Advantage

| Dimension | Standard Playwright MCP | Microsoft Playwright CLI (This Skill) |
| :--- | :--- | :--- |
| **Context Overhead** | **High:** Injects full DOM / accessibility trees on every page interaction (~5,000–20,000 tokens per action). | **Near Zero:** Invocations return terse status codes, snapshots only on demand (~50–200 tokens per action). |
| **Agent Speed** | Slower (waits for full serialized page payloads). | Ultra-fast CLI execution in sub-seconds. |
| **Best Fit** | Exploratory human-like web browsing. | High-throughput coding agents running E2E tests, smoke checks, and visual regression. |

---

## 🛠️ On-Demand Installation & Execution

### 1. Global Installation (Node.js 18+)
```bash
npm install -g @playwright/cli@latest
playwright-cli --help
```

### 2. Common Agent Commands

```bash
# Open URL in headless browser (or add --headed to watch visually)
playwright-cli open https://localhost:3000

# Type text into input fields
playwright-cli type "admin@empresa.com"
playwright-cli press Enter

# Click buttons or links by text/selector
playwright-cli click "Entrar"
playwright-cli check "#termos-aceite"

# Capture visual verification screenshot
playwright-cli screenshot --path ./report/dashboard.png

# Persistent browser session across multiple CLI commands
playwright-cli -s=test-session open https://localhost:3000 --persistent
```

---

## 🧩 Complementary Synergy in the Antigravity Kit

- **[`webapp-testing`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/webapp-testing/SKILL.md):** Guia a metodologia e planejamento de cenários de teste E2E antes de disparar os comandos CLI.
- **[`testing-patterns`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/testing-patterns/SKILL.md):** Aplica o padrão Arrange-Act-Assert (AAA) nas suítes automatizadas.
- **[`auto_preview.py`](file:///d:/xampp/htdocs/0-fonte/.agent/scripts/auto_preview.py):** Sobe o servidor web local para que o `playwright-cli` execute as validações de interface.

---

## 💡 When to Recommend this Skill

- When the agent needs to verify UI functionality or test a login/form flow locally.
- When capturing visual screenshots of rendered pages for regression testing.
- When running automated smoke tests before production deployment.
