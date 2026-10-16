---json
{
  "id": "addy_osmani_skills_and_setup",
  "title": "🚀 Addy Osmani Agent Skills & Claude Code Setup",
  "categoria": "01-gestao",
  "subcategoria": "lideranca-engenharia",
  "resumo": "**Origem:** Baseado em [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) (Addy Osmani, Google Chrome Lead) e [`claude-plugins-official/claude-code-setup`](https://github.com/anthropics/claude-plugins-official/tree/main/plugin...",
  "gatilhos": [
    "addy",
    "agent",
    "and",
    "claude",
    "code",
    "engenharia",
    "gestao",
    "lideranca"
  ],
  "perguntas_tipo": [
    "Como utilizar 🚀 Addy Osmani Agent Skills & Claude Code Setup?",
    "Quais as boas praticas de lideranca-engenharia?"
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
  "dono": "stack-lideranca-engenharia",
  "prioridade": 2
}
---

# 🚀 Addy Osmani Agent Skills & Claude Code Setup

> **Origem:** Baseado em [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) (Addy Osmani, Google Chrome Lead) e [`claude-plugins-official/claude-code-setup`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup) (Anthropic)
> **Finalidade:** Conjunto de habilidades de engenharia de nível de produção que cobrem o ciclo completo de vida do software (SDLC) e recomendação automatizada de plugins/MCPs para o projeto.

---

## 🏗️ As 7 Fases do SDLC Agêntico (Addy Osmani)

O catálogo de 25 skills divide a engenharia de software em 7 fases rigorosas:

| Fase SDLC | Foco & Habilidades Principais | Saída / Artefato |
| :--- | :--- | :--- |
| **1. Meta** | Descoberta dinâmica de qual skill usar para a tarefa atual. | Seleção cirúrgica de especialista. |
| **2. Define** | `spec-driven`: Escrita de especificações claras antes do código; `idea-refine`: refino de MVP e remoção de suposições. | `SPEC.md` / Contrato de requisitos. |
| **3. Plan** | `task-breakdown`: Divisão em tarefas pequenas e verificáveis; `interview-me`: perguntas focadas uma a uma. | Plano de execução em fases. |
| **4. Build** | Implementação cirúrgica, padrões de componentes modernos e limites de arquivos (200–300 linhas). | Código limpo e modular. |
| **5. Verify** | `tdd-workflow`: Test-driven development (Red-Green-Refactor); validação automatizada de regressões. | Testes unitários e de integração verdes. |
| **6. Review** | Framework de 5 eixos de revisão de código: Corretude, Legibilidade, Arquitetura, Segurança e Performance. | Checklist de qualidade pré-merge. |
| **7. Ship** | `deploy-ready`: Verificações finais de ambiente, integridade de segredos e monitoramento. | Release em produção sem surpresas. |

---

## ⚙️ Claude Code Setup Pattern

O plugin `claude-code-setup` analisa a raiz do projeto e identifica instantaneamente:
1. **Linguagens e Frameworks:** (ex: Node/TypeScript, PHP/Laravel, Python/FastAPI, Go, Rust).
2. **MCP Servers Recomendados:** Sugere e injeta servidores MCP específicos (ex: Chrome DevTools para frontend, PostgreSQL MCP para banco, Playwright MCP para E2E).
3. **Regras e Hooks:** Configura ganchos de pré-commit e checagem de tipos antes de cada push.

```bash
# Como acionar no Claude Code
/plugin install claude-code-setup@claude-plugins-official
# Solicitar recomendação
"recommend automations for this project"
```

---

## 💡 Como Usar no Nosso Sistema:
No sistema AllMight, essa estrutura é acionada nativamente:
- A fase **Define** e **Plan** integra-se ao `project-planner` e `/plan`.
- A fase **Review** em 5 eixos integra-se ao `code-review-checklist` e `checklist.py`.
- O auto-setup integra-se ao nosso fluxo de inicialização `/diagnose`.
