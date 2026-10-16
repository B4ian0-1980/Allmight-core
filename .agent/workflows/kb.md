```
---
description: Busca na biblioteca AllMight. Encontra padrões, documentos e conhecimento técnico.
---
# /kb

---

## Propósito

Este comando realiza uma busca estruturada na biblioteca de conhecimento AllMight para encontrar templates, arquiteturas e padrões.

---

## Comportamento

1. **Entender a Query:** O agente recebe o termo de busca.
2. **Executar Motor:** Roda o script `python .agent/knowledge/allmight/07_AUTOMACAO/scripts/allmight_search.py "termo"`.
3. **Apresentar Resultados:**
    - Exibe o Top 5 resultados.
    - Mostra [Categoria] + Título.
    - Fornece o link clicável para o arquivo.
    - Resume por que aquele arquivo é relevante para a conversa atual.

---

## Exemplos de Uso

```
/kb clean architecture
/kb n8n whatsapp
/kb manual evolução api
/kb template adr
```

---

## Regras de Resposta

- Se nenhum resultado for encontrado, sugira termos relacionados ou verifique a categoria correta.
- Se muitos resultados existirem, peça para o usuário refinar a busca.
