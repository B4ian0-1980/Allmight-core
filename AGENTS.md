# Diretrizes do Workspace — Antigravity

Este repositório adota o modelo de **Eficiência de Tokens e Fluxo Híbrido** do Google Antigravity.

## Princípios Operacionais

1. **Leitura Cirúrgica:** Priorize `grep_search` e limites de linha (`StartLine`/`EndLine`). Não leia arquivos inteiros extensos desnecessariamente.
2. **Output Conciso:** Responda direto ao ponto, com explicações mínimas e foco na alteração realizada.
3. **Sinergia com Editor:** Crie esqueletos, contratos e interfaces tipadas para permitir expansão via `Tab` (Supercomplete) e `Ctrl + I`.
4. **Regras Modulares:** Regras específicas de banco de dados, testes e arquitetura são carregadas sob demanda via *Progressive Disclosure* em `.agent/rules/`.
5. **Modo Esqueleto:** Para gerar contratos e assinaturas para preenchimento imediato no editor via `Tab`, cite `@esqueleto`.
