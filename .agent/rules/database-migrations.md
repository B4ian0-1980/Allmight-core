---
trigger: model_decision
description: "Aplique estas regras apenas quando estiver criando, revisando ou alterando migrações SQL, schemas de banco de dados ou queries complexas."
---

# Regras de Banco de Dados e Migrations

1. **Padrão Expand-and-Contract:** Nunca remova ou renomeie colunas em um único deploy; expanda com novas colunas, migre dados e só então deprecie.
2. **Índices Não-Bloqueantes:** Sempre utilize `CONCURRENTLY` (PostgreSQL) ao criar índices em tabelas de grande volume ou produção.
3. **Validação de Tipos e Restrições:** Valide explicitamente chaves estrangeiras, enums e períodos temporais antes de gerar migrações.
4. **Idempotência:** Scripts SQL devem ser sempre idempotentes (`IF NOT EXISTS`, `ON CONFLICT DO NOTHING / UPDATE`).
