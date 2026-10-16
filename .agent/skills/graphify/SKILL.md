---
name: graphify
description: "Multimodal Knowledge Graph builder for codebases, documents, research papers, and images. Extracts concepts, detects communities, and generates interactive 2D/3D graphs, Obsidian vaults, and GraphRAG JSON with 71.5x token savings."
trigger: /graphify
---

# Graphify — Multimodal Knowledge Graph for Codebases & Docs

**graphify** turns any folder of files (code, markdown notes, research papers, architecture diagrams, whiteboard photos) into a structured, navigable **Knowledge Graph** with community clustering and graph exploration.

- **Upstream Repository:** [https://github.com/Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
- **PyPI Package:** `graphifyy` (`pip install graphifyy`)
- **Key Metric:** **71.5x fewer tokens per query** compared to feeding raw file dumps into LLM context windows.

---

## 🚀 Core Capabilities

1. **Multimodal Extraction:**
   - Ingests source code (`.py`, `.ts`, `.php`, `.rs`, `.go`), markdown, text, PDFs, diagrams, and screenshots.
   - Uses vision/LLM parsing to detect conceptual relationships across different file formats.
2. **Honest Audit Trail:**
   - Categorizes every relation edge into:
     - `EXTRACTED`: Explicitly stated in the source code or document.
     - `INFERRED`: Logically deduced by the model.
     - `AMBIGUOUS`: Flagged for human review.
3. **Cross-Document Surprise & Community Detection:**
   - Uncovers hidden architectural dependencies and "god nodes" linking disparate modules.
4. **Multi-Format Export Outputs:**
   ```text
   graphify-out/
   ├── graph.html       # Interactive 2D/3D web visualization with search and filters
   ├── obsidian/        # Ready-to-open Obsidian markdown vault with bi-directional wikilinks
   ├── wiki/            # Wikipedia-style reference articles for agent context navigation
   ├── GRAPH_REPORT.md  # Architectural summary, god nodes, and unexpected connections
   ├── graph.json       # GraphRAG persistent database (queryable across sessions)
   └── cache/           # SHA256 file cache for instant incremental updates
   ```

---

## 💻 CLI & Agent Usage Guide

### 1. Installation On-Demand (Python 3.10+)
```bash
pip install graphifyy && graphify install
```

### 2. Common Commands
```bash
# Full knowledge graph on current workspace
graphify .

# Run on a specific directory
graphify ./docs

# Deep extraction mode (richer inferred conceptual edges)
graphify . --mode deep

# Incremental update (processes only new/changed files via SHA256 cache)
graphify . --update

# Export graph for Neo4j
graphify . --neo4j

# Query concepts using GraphRAG shortest paths
graphify query "Como o módulo de autenticação se conecta ao banco de dados?"
graphify path "AuthService" "DatabasePool"
```

---

## 🧩 Integration with Antigravity Ecosystem

- **[`knowledge-base`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/knowledge-base/SKILL.md):** Utiliza o `graph.json` gerado para consultas contextuais ultra-rápidas na base AllMight sem extrapolar janelas de contexto.
- **[`book-to-skill`](file:///d:/xampp/htdocs/0-fonte/.agent/skills/book-to-skill/SKILL.md):** Complementa a digestão de livros e manuais técnicos mapeando os conceitos em grafos navegáveis.
- **[`code-archaeologist`](file:///d:/xampp/htdocs/0-fonte/.agent/agents/code-archaeologist.md):** Auxilia o agente arqueólogo a desvendar sistemas legados e mapear dependências ocultas antes de refatorações.

---

## 💡 When to Recommend this Skill

- When a new developer or agent enters a large codebase and needs to understand architecture instantly.
- When organizing a research directory with PDFs, articles, notes, and code.
- When building GraphRAG workflows that require low token consumption and persistent graph memory.
