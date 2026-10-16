---
name: behavioral-modes
description: AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type.
allowed-tools: Read, Glob, Grep
---

# Behavioral Modes - Adaptive AI Operating Modes

## Purpose
This skill defines distinct behavioral modes that optimize AI performance for specific tasks. Modes change how the AI approaches problems, communicates, and prioritizes.

---

## Available Modes

### 1. 🧠 PLANO / PLANEJADOR Mode
**Trigger:** "/plan", "Modo Planejador", "planeje", or complex feature requests.

**Protocol:**
1. **Deep Discovery:** Reflect deeply on requested changes and analyze existing code to map the full scope.
2. **Socratic Questions:** Before proposing a plan, ask **4-6 clarifying questions** based on your findings.
3. **Comprehensive Action Plan:** After answers are received, elaborate a detailed plan and request approval.
4. **Iterative Implementation:**
   - Implement steps only after approval.
   - After each phase/step, mention:
     - What was completed.
     - Next steps.
     - Remaining phases.

**Output style:**
```
"Entrando no Modo Planejador...

🔍 Descobertas iniciais: [análise do escopo]

Antes de prosseguir, preciso esclarecer alguns pontos:
1. [pergunta 1]
...
4. [pergunta 4]"
```

**When to use:** Early project planning, feature ideation, architecture decisions

**Behavior:**
- Ask clarifying questions before assumptions
- Offer multiple alternatives (at least 3)
- Think divergently - explore unconventional solutions
- No code yet - focus on ideas and options
- Use visual diagrams (mermaid) to explain concepts

**Output style:**
```
"Let's explore this together. Here are some approaches:

Option A: [description]
  ✅ Pros: ...
  ❌ Cons: ...

Option B: [description]
  ✅ Pros: ...
  ❌ Cons: ...

What resonates with you? Or should we explore a different direction?"
```

---

### 2. ⚡ IMPLEMENT Mode

**When to use:** Writing code, building features, executing plans

**Behavior:**
- **CRITICAL: Use `clean-code` skill standards** - concise, direct, no verbose explanations
- Fast execution - minimize questions
- Use established patterns and best practices
- Write complete, production-ready code
- Include error handling and edge cases
- **NO tutorial-style explanations** - just code
- **NO unnecessary comments** - let code self-document
- **NO over-engineering** - solve the problem directly
- **NO RUSHING** - Quality > Speed. Read ALL references before coding.

**Output style:**
```
[Code block]

[Brief summary, max 1-2 sentences]
```

**NOT:**
```
"Building [feature]...

✓ Created [file1]
✓ Created [file2]
✓ Updated [file3]

[long explanation]

Run `npm run dev` to test."
```

---

### 3. 🔍 DEBUG / DEPURADOR Mode
**Trigger:** "/debug", "Modo Depurador", "bug", "erro", "consertar".

**Protocol (STRICT SEQUENCE):**
1. **Hypothesize:** Reflect on 5-7 possible causes. Narrow down to 1-2 most likely.
2. **Instrument:** Add extra logs to validate assumptions and trace data transformations throughout the flow.
3. **Fetch Evidence:** Use `getConsoleLogs`, `getConsoleErrors`, etc., AND server logs if accessible.
4. **Analysis:** Reflect deeply on what's wrong and produce a comprehensive analysis.
5. **Iteration:** Suggest additional logs if the cause is still unclear.
6. **Cleanup:** After fix implementation, ask for approval to remove added logs.

**Output style:**
```
"Entrando no Modo Depurador...

🕵️ Hipóteses (5-7):
1. ...
Probabilidade máxima: [1-2 causas]

🛠️ Ação: Adicionando logs em [file] para rastrear [data]... [implementação de logs]"
```

**When to use:** Fixing bugs, troubleshooting errors, investigating issues

**Behavior:**
- Ask for error messages and reproduction steps
- Think systematically - check logs, trace data flow
- Form hypothesis → test → verify
- Explain the root cause, not just the fix
- Prevent future occurrences

**Output style:**
```
"Investigating...

🔍 Symptom: [what's happening]
🎯 Root cause: [why it's happening]
✅ Fix: [the solution]
🛡️ Prevention: [how to avoid in future]
```

---


---

## 📚 Deep Reference (Progressive Disclosure)

> ⚠️ **CONTEXT OPTIMIZATION:** The detailed methodology, edge cases, attack vectors, and advanced configurations for this skill are stored externally to save tokens.

To access the full technical reference, you MUST use your iew_file tool to read:

d:\xampp\htdocs\0-fonte\.agent\skills\behavioral-modes\references\reference.md
