---
name: coding-discipline
description: Strict coding discipline based on Karpathy's rules - surgical changes, goal-driven execution, and radical simplicity.
allowed-tools: Read, Write, Edit, Grep
version: 1.0
priority: CRITICAL
upstream_source: https://github.com/karpathy
last_updated: 2026-10-10
---

# Coding Discipline - Karpathy's Rules for LLM Safety

> **MANDATORY SKILL** - Prioritize **safety, precision, and verification** over speed and "improvements".

---

## 1. Surgical Changes (Touch Only What You Must)

**Rule:** The agent MUST touch only the code directly related to the task. 

| ❌ AVOID (Boy Scout Rule) | ✅ DO (Surgical Mode) |
|---------------------------|-----------------------|
| Refactoring adjacent code | Mentioning messy code in chat |
| Improving comments/formatting nearby | Matching existing style exactly |
| Fixing unrelated dead code | Flagging dead code for later |
| "Cleaning up" the file | Only changing what's broken |

**The Test:** Every changed line must trace directly to the user's request.

---

## 2. Goal-Driven Execution (Verify Every Step)

**Rule:** Use the `[Passo] → verificar: [check]` format for any task involving more than one file or having side effects.

### Planning Format
```markdown
1. [Passo] → verificar: [Comando/Check para validar o sucesso]
2. [Passo] → verificar: [Comando/Check para validar o sucesso]
3. [Passo] → verificar: [Comando/Check para validar o sucesso]
```

### When to use:
- **Trivial tasks** (typos, single var rename) → Format is optional (Avoid bureaucracy).
- **Non-trivial tasks** (multi-file, logic changes, new features) → **MANDATORY**.

---

## 3. Radical Simplicity (Anti-Bloat)

**Rule:** Minimum code that solves the problem. Nothing speculative.

- **No speculations:** No "maybe we'll need this" features.
- **No over-engineering:** If 200 lines could be 50, re-evaluate.
- **No "impossible" handling:** Don't write code for scenarios that can't happen.

### Simplification Modes
1. **`simplify: flag` (Default):** Flag over-complicated code to the user ("This could be simplified from X to Y lines").
2. **`simplify: rewrite` (Explicit):** Only re-write if the user approves the suggestion.

---

## 4. Think Before Coding (Socratic Gate)

**Rule:** Never assume. Never hide confusion.

- **State assumptions explicitly:** "I am assuming X because Y."
- **Stop if confused:** Name the ambiguity and ask for clarification.
- **Present tradeoffs:** If multiple ways exist, list them before picking.
- **Push back:** If a request leads to a bad/bloated architecture, explain why and suggest a simpler alternative.

---

## 🏁 Verification
- [ ] Diffs are clean and focused ONLY on the task.
- [ ] No "drive-by" refactoring.
- [ ] Plan follows the `[Passo] → verificar: [check]` format.
- [ ] User was consulted before any aggressive simplification.
