---
name: find-skills
description: "Discovers, recommends, and installs agent skills from the open skills ecosystem (skills.sh, npx skills, GitHub). Use when the user asks 'how do I do X', 'find a skill for X', or needs new capabilities."
metadata:
  version: 1.0.0
upstream_source: https://github.com/vercel-labs/skills/tree/main/skills/find-skills
last_updated: 2026-10-10
---

# Find Skills — Dynamic Agent Skill Discovery

> **Purpose:** Discover, evaluate, and install verified skills from the open agent skills ecosystem (`skills.sh`) when the current system doesn't have specialized tooling for the user's task.

---

## 🔍 When to Activate

Trigger this skill when the user:
- Asks *"existe alguma skill para X?"*, *"como encontro ferramentas para Y?"*
- Precisa de uma capacidade especializada não coberta pelos agentes padrão (ex: Kubernetes Helm, Three.js 3D, Solidity, WebAssembly).
- Quer expandir as ferramentas do sistema AllMight ou Claude Code.

---

## 🛠️ The Skills CLI Reference

The Skills CLI (`npx skills`) is the standard package manager for agent skills:

```bash
# 1. Buscar skills interativamente ou por palavra-chave
npx skills find [termo]

# 2. Instalar uma skill de um repositório GitHub
npx skills add [owner/repo] --skill [nome-da-skill]

# Exemplo: Instalar skills do Vercel Labs ou do Addy Osmani
npx skills add vercel-labs/skills --skill find-skills
npx skills add addyosmani/agent-skills

# 3. Atualizar todas as skills instaladas
npx skills update
```

---

## 🧭 Discovery Protocol (Passo a Passo)

1. **Check Local First:** Verifique sempre o catálogo interno `ARCHITECTURE.md` antes de buscar externamente para evitar duplicação.
2. **Search the Registry:** Se a capacidade for inexistente localmente, pesquise no catálogo do [skills.sh](https://skills.sh/) ou execute `npx skills find [query]`.
3. **Audit Security & Size:** Antes de recomendar ou instalar, avalie se a skill contém scripts perigosos ou arquivos excessivos. Priorize skills com licença permissiva e código limpo.
4. **Install & Wire:** Instale via `npx skills add` ou crie o diretório correspondente em `.agent/skills/`, vinculando ao agente especialista adequado.
