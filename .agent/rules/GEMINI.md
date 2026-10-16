---
trigger: always_on
---

# GEMINI.md - Antigravity Kit

> This file defines the base initialization protocol for this workspace. 
> **Important:** Extended rules have been modularized to optimize context. The Antigravity engine automatically loads them from `.agent/rules/`.

---

## CRITICAL: AGENT & SKILL PROTOCOL (START HERE)

> **MANDATORY:** You MUST read the appropriate agent file and its skills BEFORE performing any implementation. This is the highest priority rule.

### 1. Modular Skill Loading Protocol

Agent activated → Check frontmatter "skills:" → Read SKILL.md (INDEX) → Read specific sections.

- **Selective Reading:** DO NOT read ALL files in a skill folder. Read `SKILL.md` first, then only read sections matching the user's request.
- **Rule Priority:** P0 (GEMINI.md) > P1 (Agent .md) > P2 (SKILL.md). All rules are binding.

### 2. Enforcement Protocol

1. **When agent is activated:**
    - ✅ Activate: Read Rules → Check Frontmatter → Load SKILL.md → Apply All.
2. **Forbidden:** Never skip reading agent rules or skill instructions. "Read → Understand → Apply" is mandatory.

---

### 🗺️ System Map Read

> 🔴 **MANDATORY:** Read `ARCHITECTURE.md` at session start to understand Agents, Skills, and Scripts.
> ⚠️ **Guard:** If `ARCHITECTURE.md` does not exist, STOP and inform the user before proceeding with any implementation.

**Path Awareness:**

- Agents: `.agent/` (Project)
- Skills: `.agent/skills/` (Project)
- Runtime Scripts: `.agent/skills/<skill>/scripts/`

### 🌐 Language Handling

- **Language**: **MANDATORY Portuguese (pt-br)** for all responses.
- **Internal**: Internally translate for better comprehension if needed.
- **Code**: Comments and variables remain in **English**.