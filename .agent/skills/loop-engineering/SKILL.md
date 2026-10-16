---
name: loop-engineering
description: "Design, audit, run, and bound autonomous AI agent loops (autoloop, loopy, Copilot agent-loop). Prevents runaway executions, enforces verification gates, and guarantees evidence-backed stopping criteria."
metadata:
  version: 1.0.0
upstream_source: https://github.com/cobusgreyling/loop-engineering
last_updated: 2026-10-10
---

# Loop Engineering — Autonomous Agent Feedback Cycles

> **Core Axiom:** A prompt asks an agent to do something once. A loop gives the agent a repeatable feedback cycle with hard terminal gates. Treat loops as control systems, never as permission for endless autonomy.

---

## 🧭 The 4 Pillars of a Sound Loop

Every agent loop MUST explicitly define these 4 components before running:

1. **Goal:** What concrete outcome is the agent trying to accomplish?
2. **Verification Check:** How will the agent know whether the latest pass succeeded or failed? (e.g., test runner, linter, metric diff, typecheck).
3. **Adaptive Action:** What should the agent do with the evidence from the previous attempt? (e.g., revert regression, mutate hypothesis, adjust parameters).
4. **Stopping Condition (Terminal Gate):** When does the loop finish or escalate to a human? (e.g., all tests pass, metric delta < threshold, max 5 iterations reached).

---

## ⚡ The Loop Engineering Matrix

| Loop Type | Origin / Pattern | Trigger / Use Case | Verificação Obrigatória | Critério de Parada |
| :--- | :--- | :--- | :--- | :--- |
| **Autoloop** | GitHub Next | Refatoração de performance, redução de bundle, aumento de cobertura. | Benchmark ou métrica numérica pré vs pós alteração. | Métrica atingida OU estagnação (3 ciclos sem melhora). Reverte se piorar. |
| **Loopy Pass** | Forward-Future | Correção de bugs recorrentes, triagem de erros, polimento iterativo. | Execução de teste específico (`test_runner.py`) ou build limpa. | Teste passa OU limite de passes (default: 3 passes) com recibo de evidência. |
| **Agent State Machine** | Copilot SDK | Orquestração de subagentes com múltiplas ferramentas encadeadas. | Validação de estado pós-chamada de ferramenta. | Contrato de saída satisfeito ou transição para estado de erro terminal. |
| **Daily Triage / Audit** | Cobus Greyling | Revisão contínua de PRs, checagem de logs de produção, varredura de débitos. | Relatório de conformidade sem falsos positivos. | 1 ciclo completo sobre a lista de itens. |

---

## 🛡️ Hard Safety Guardrails (Zero Runaway Policy)

1. **Iteration Caps:** Default cap is **3 iterations** for interactive tasks, **5 iterations** for batch tasks. Never allow unbounded loops (`while true` without hard iteration counter).
2. **Revert On Degradation:** In optimization loops (Autoloop), if pass $N+1$ causes a regression or introduces new lint/test errors, git rollback immediately to pass $N$.
3. **Evidence Receipts:** Every completed loop must return a concise execution receipt:
   - **Pass count:** Total passes executed.
   - **Baseline metric:** Score before start.
   - **Final metric:** Score after finish.
   - **Files touched:** Surgical list of modifications.
   - **Stopping reason:** Success threshold reached / Max iterations reached / Escalated to human.
4. **Project Persistence (`LOOPS.md`):** When a loop proves repeatedly useful for a project, save its prompt, verification command, and iteration cap in `LOOPS.md` for zero-setup reuse.
