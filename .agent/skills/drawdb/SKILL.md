---
name: drawdb
description: Visual entity-relationship diagram (ERD) editor, database schema designer, and multi-dialect SQL generator supporting PostgreSQL, MySQL, SQLite, MariaDB, and SQL Server.
---

# 📊 DrawDB — Visual Database Schema & ERD Architect

> **Baseado em:** [`drawdb-io/drawdb`](https://github.com/drawdb-io/drawdb)  
> **Filosofia:** *Free, simple, and intuitive database schema editor and SQL generator.*

---

## 🎯 Objetivo

Desenhar, documentar e exportar schemas relacionais profissionais sem complicações. O **DrawDB** atua como ferramenta de modelagem visual de entidades (ERD) e conversão bidirecional:
1. **Diagramação ERD:** Modelagem de tabelas, campos, chaves primárias, estrangeiras e restrições (`UNIQUE`, `NOT NULL`, `CHECK`).
2. **Multi-Dialeto SQL:** Geração de scripts DDL executáveis para **PostgreSQL, MySQL, SQLite, MariaDB e SQL Server**.
3. **Portabilidade:** Exportação e importação de schemas em formato JSON interoperável.

---

## 🏗️ Padrões de Modelagem Suportados

```plaintext
                              MODELAGEM DRAWDB
                                     │
      ┌──────────────────────────────┼──────────────────────────────┐
      ▼                              ▼                              ▼
[ ENTIDADES & CAMPOS ]      [ RELACIONAMENTOS ]           [ EXPORTAÇÃO DDL ]
• Tipos primitivos          • 1:1 (One-to-One)            • PostgreSQL (DDL + UUID)
• Default values            • 1:N (One-to-Many)           • MySQL / MariaDB (InnoDB)
• Índices (B-Tree, Hash)    • N:N (Tabela Associativa)    • SQLite (AUTOINCREMENT)
• Constraints & Enums       • ON DELETE CASCADE/SET NULL  • SQL Server (T-SQL)
```

---

## 📋 Regras de Design de Banco de Dados

Ao utilizar o DrawDB ou modelar schemas relacionais:
1. **Convenção de Nomenclatura:**
   - Tabelas no plural minúsculo (`usuarios`, `pedidos`, `itens_pedido`).
   - Chave primária padrão: `id` (ou `id_uuid` para sistemas distribuídos).
   - Chave estrangeira: `{entidade_singular}_id` (ex.: `usuario_id`, `departamento_id`).
2. **Integridade Referencial:**
   - Sempre declarar o comportamento em deleção (`ON DELETE RESTRICT` para dados críticos e `CASCADE` para detalhes órfãos).
3. **Indexação Estratégica:**
   - Criar índices em todas as colunas utilizadas frequentemente em cláusulas `WHERE`, `JOIN` ou ordenação `ORDER BY`.

---

## 🛠️ Comandos e Scripts Locais

### Script Validador e Exportador de Schemas
Converta ou valide uma especificação de schema em JSON diretamente para scripts SQL:
```bash
python .agent/skills/drawdb/scripts/schema_exporter.py caminho/para/schema.json --dialect postgres
python .agent/skills/drawdb/scripts/schema_exporter.py caminho/para/schema.json --dialect mysql
```

### Formato JSON Padrão DrawDB
```json
{
  "tables": [
    {
      "name": "users",
      "fields": [
        {"name": "id", "type": "SERIAL", "primary": true},
        {"name": "email", "type": "VARCHAR(255)", "unique": true, "not_null": true},
        {"name": "created_at", "type": "TIMESTAMP", "default": "NOW()"}
      ]
    }
  ]
}
```
