---json
{
  "id": "anydoc_parser",
  "title": "📄 AnyDoc — Ingestão e Conversão Universal de Documentos para LLM",
  "categoria": "08-automacao",
  "subcategoria": "context-engines",
  "resumo": "**Origem:** Baseado no motor de alto desempenho [`firecrawl/anydoc`](https://github.com/firecrawl/anydoc) (Firecrawl) **Finalidade:** Conversor ultra-rápido em Rust para transformar documentos de escritório (PDF, Word, Excel, PPTX, EPUB, RTF) em M...",
  "gatilhos": [
    "anydoc",
    "automacao",
    "context",
    "documentos",
    "engines",
    "llm",
    "para",
    "parser"
  ],
  "perguntas_tipo": [
    "Como utilizar 📄 AnyDoc — Ingestão e Conversão Universal de Documentos para LLM?",
    "Quais as boas praticas de context-engines?"
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
  "dono": "stack-context-engines",
  "prioridade": 2
}
---

# 📄 AnyDoc — Ingestão e Conversão Universal de Documentos para LLM

> **Origem:** Baseado no motor de alto desempenho [`firecrawl/anydoc`](https://github.com/firecrawl/anydoc) (Firecrawl)
> **Finalidade:** Conversor ultra-rápido em Rust para transformar documentos de escritório (PDF, Word, Excel, PPTX, EPUB, RTF) em Markdown limpo estruturado (GitHub-Flavored Markdown), pronto para consumo direto por agentes de IA e pipelines RAG.

---

## ⚡ Por que Usar o AnyDoc

- **Consistência Semântica:** Mapeia todos os formatos para um Modelo de Documento Único antes de serializar em Markdown. Tabelas, notas de rodapé, cabeçalhos e listas mantêm a mesma sintaxe exata seja a fonte um `.docx`, `.xlsx` ou `.pdf`.
- **Performance Nativa:** Processamento em milissegundos por página, muito mais rápido e leve que soluções baseadas em LibreOffice ou Python pesado.
- **Múltiplos Bindings:** Disponível como CLI, biblioteca Rust, módulo Node.js, pacote Python e WebAssembly para navegador.

---

## 📋 Formatos Suportados

| Formato | Extensões | Aplicação Prática no Agente |
| :--- | :--- | :--- |
| **PDF** | `.pdf` | Leitura de manuais técnicos, relatórios de auditoria e especificações. |
| **Word** | `.docx`, `.doc` | Ingestão de PRDs, briefings e documentação corporativa. |
| **Excel** | `.xlsx`, `.csv` | Conversão de matrizes de dados, orçamentos e listas para tabelas Markdown. |
| **PowerPoint** | `.pptx` | Extração de roteiros, apresentações comerciais e resumos executivos. |
| **ePub & Rich Text** | `.epub`, `.rtf`, `.odt` | Extração de e-books, normas regulatórias e termos jurídicos. |

---

## 💻 Como Executar

```bash
# Como skill do agente (Skills CLI)
npx skills add firecrawl/anydoc

# Uso via CLI / Node.js
npx anydoc input.pdf -o output.md
```

---

## 💡 Quando o Sistema Deve Sugerir o AnyDoc:
Sugerir ativamente quando o usuário solicitar:
1. *"Leia este PDF / analise este arquivo Word / importe esta planilha"*.
2. Ingestão de documentação de clientes com formatações complexas ou tabelas embutidas.
