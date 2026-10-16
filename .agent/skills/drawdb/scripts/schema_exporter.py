#!/usr/bin/env python3
"""
DrawDB — Schema Validator & DDL Exporter
=========================================
Converts DrawDB JSON schema files into executable SQL DDL statements
for PostgreSQL, MySQL, SQLite, and MariaDB.
"""

import sys
import json
import argparse
from pathlib import Path

if sys.stdout:
    sys.stdout.reconfigure(encoding="utf-8")

def export_ddl(schema_path: Path, dialect: str = "postgres"):
    if not schema_path.exists():
        print(f"❌ Arquivo não encontrado: {schema_path}")
        sys.exit(1)

    try:
        data = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"❌ Erro ao ler JSON: {e}")
        sys.exit(1)

    tables = data.get("tables", [])
    print(f"📊 Exportando {len(tables)} tabelas para o dialeto: {dialect.upper()}\n")

    sql_statements = []

    for table in tables:
        t_name = table.get("name", "unnamed_table")
        fields = table.get("fields", [])
        field_defs = []

        for f in fields:
            f_name = f.get("name")
            f_type = f.get("type", "TEXT")
            is_pk = f.get("primary", False)
            is_unique = f.get("unique", False)
            not_null = f.get("not_null", False)
            default = f.get("default")

            # Adjust auto-increment per dialect
            if is_pk:
                if dialect == "postgres":
                    f_type = "SERIAL PRIMARY KEY" if "INT" in f_type.upper() or f_type == "SERIAL" else f"{f_type} PRIMARY KEY"
                elif dialect == "sqlite":
                    f_type = "INTEGER PRIMARY KEY AUTOINCREMENT" if "INT" in f_type.upper() else f"{f_type} PRIMARY KEY"
                else:
                    f_type = f"{f_type} AUTO_INCREMENT PRIMARY KEY"
                field_defs.append(f"  {f_name} {f_type}")
                continue

            definition = f"  {f_name} {f_type}"
            if not_null:
                definition += " NOT NULL"
            if is_unique:
                definition += " UNIQUE"
            if default:
                definition += f" DEFAULT {default}"

            field_defs.append(definition)

        create_sql = f"CREATE TABLE IF NOT EXISTS {t_name} (\n" + ",\n".join(field_defs) + "\n);"
        sql_statements.append(create_sql)

    output = "\n\n".join(sql_statements)
    print(output)
    print("\n✅ DDL gerado com sucesso!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DrawDB Schema Exporter")
    parser.add_argument("schema", help="Caminho do arquivo JSON do schema")
    parser.add_argument("--dialect", choices=["postgres", "mysql", "sqlite", "mariadb"], default="postgres", help="Dialeto SQL alvo")
    args = parser.parse_args()

    export_ddl(Path(args.schema), args.dialect)
