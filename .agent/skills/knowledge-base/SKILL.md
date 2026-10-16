---
name: knowledge-base
description: Protocolo de consulta à base AllMight para busca de padrões, templates e arquitetura.
---

# Skill: Knowledge Base (AllMight)

Esta skill transforma a base `allmight` em um consultor técnico ativo para o agente.

## 🧠 Princípios

1. **Consulta Pró-ativa:** Antes de sugerir uma arquitetura, banco de dados ou fluxo de automação, o agente DEVE consultar a AllMight para verificar se já existe um template ou guia.
2. **Conformidade Técnica:** Priorize sempre os padrões documentados em `03_CONHECIMENTO` e `01_GESTAO`.
3. **Eficiência de Tokens:** Utilize o script de busca global para localizar arquivos específicos em vez de navegar em diretórios.

## 🛠️ Protocolo de Pesquisa

Sempre que encontrar uma das situações abaixo, execute a busca:

- **Novo Projeto:** `/kb template projeto`
- **Design de API:** `/kb api patterns`
- **Segurança/Audit:** `/kb segurança checklist`
- **Infra/Docker:** `/kb docker compose`

## ⌨️ Comandos Disponíveis

- **`/kb [termo]`**: Atalho para busca global na base AllMight.

## 📂 Caminho do Motor de Busca
`.agent/knowledge/allmight/07_AUTOMACAO/scripts/allmight_search.py`
