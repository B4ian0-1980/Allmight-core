---
description: Aprender novo conhecimento extraindo documentação de um link (Web to MD).
---

# /learn - Dynamic Knowledge Acquisition

$ARGUMENTS

---

## Purpose

Este comando permite expandir a base AllMight em tempo real capturando o conteúdo de uma URL técnica e convertendo-o em um documento Markdown indexável.

---

## Behavior

1. **Extração:** Baixa o conteúdo HTML da URL fornecida.
2. **Conversão:** Remove elementos ruidosos (scripts, menus, rodapés) e converte o conteúdo principal para Markdown.
3. **Armazenamento:** Salva o arquivo em `.agent/knowledge/allmight/00_IMPORT/external_docs/`.
4. **Indexação:** Executa automaticamente `generate_folder_maps.py` para tornar o link pesquisável via `/kb`.

---

## Examples

```
/learn https://docs.djangoproject.com/en/5.0/intro/tutorial01/
/learn https://angular.dev/docs
```

---

## Technical Flow

// turbo
1. Execute o script de captura:
`python .agent/knowledge/allmight/07_AUTOMACAO/scripts/web_to_md.py $ARGUMENTS`

// turbo
2. Atualize o índice global:
`python .agent/knowledge/allmight/07_AUTOMACAO/scripts/generate_folder_maps.py`
