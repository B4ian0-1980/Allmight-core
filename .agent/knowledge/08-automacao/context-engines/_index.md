---
id: idx_context-engines
resumo: Indice de recursos e manuais de context-engines
gatilhos:
- automacao
- context
- engines
- anydoc
- documentos
- llm
- codebase
- engine
- graft
rotas:
- id: anydoc_parser
  resumo: '**Origem:** Baseado no motor de alto desempenho [`firecrawl/anydoc`](https://github.com/firecrawl/anydoc)
    (Firecrawl) **Finalidade:** Conversor ultra-rápido em Rust para transformar documentos
    de escritório (PDF, Word, Excel, PPTX, EPUB, RTF) em M...'
  gatilhos:
  - anydoc
  - automacao
  - context
  - documentos
  - engines
  - llm
  arquivo: ./anydoc_parser.md
  secoes:
  - por-que-usar-o-anydoc
  - formatos-suportados
  - como-executar
  - quando-o-sistema-deve-sugerir-o-anydoc
  tokens_estimados: 506
- id: graft_context_engine
  resumo: '**Origem:** Baseado no repositório [`trailhq/graft`](https://github.com/trailhq/graft)
    **Finalidade:** Motor de engenharia de contexto e grafo de código para Claude
    Code, Cursor, Codex e Gemini. Permite aos agentes entenderem dependências de códig...'
  gatilhos:
  - automacao
  - codebase
  - context
  - engine
  - engines
  - graft
  arquivo: ./graft_context_engine.md
  secoes:
  - como-funciona
  - como-inicializar
  - quando-o-agente-deve-sugerir-o-graft
  tokens_estimados: 332
---
