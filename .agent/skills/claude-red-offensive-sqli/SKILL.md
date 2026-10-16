# SKILL: SQL Injection (SQLi)

## Metadata
- **Skill Name**: sqli
- **Folder**: offensive-sqli
- **Source**: https://github.com/SnailSploit/offensive-checklist/blob/main/sqli.md

## Description
SQL Injection vulnerability testing checklist: In-band (UNION-based, error-based), Inferential (Boolean-blind, Time-blind), and Out-of-Band (OOB DNS/HTTP exfiltration) across MySQL, PostgreSQL, Microsoft SQL Server, Oracle, and SQLite. Covers quote escaping, comment variations, authentication bypass, second-order SQLi, WAF evasion, and automated validation via sqlmap.

## Trigger Phrases
Use this skill when the conversation involves any of:
`SQL injection, SQLi, blind sqli, time-based sqli, union-based sqli, sqlmap, error-based sqli, sql auth bypass, second-order sqli, out-of-band sqli`

## Instructions for Claude

When this skill is active:
1. Load and apply the full methodology below as your operational checklist
2. Follow steps in order unless the user specifies otherwise
3. For each technique, consider applicability to the current target/context
4. Track which checklist items have been completed
5. Suggest next steps based on findings

---

## Full Methodology

# SQL Injection (SQLi)

## Shortcut

- Identify all user inputs touching database queries (GET/POST params, headers, JSON fields, cookies).
- Inject single and double quotes (`'`, `"`), brackets, and arithmetic expressions (`-0`, `+0`, `*1`).
- Observe application behavior: database errors, HTTP 500, content discrepancies, or timing delays.
- Determine injection type:
  - Error-based: extract schema/data directly via verbose DB errors.
  - UNION-based: balance column count (`ORDER BY n`), determine compatible types, and dump tables.
  - Boolean-blind: test truth conditions (`AND 1=1` vs `AND 1=2`).
  - Time-blind: trigger database sleep functions (`SLEEP(5)`, `pg_sleep(5)`, `WAITFOR DELAY '0:0:5'`).
  - Out-of-band: DNS exfiltration via `LOAD_FILE`, `UTL_HTTP`, or `xp_dirtree`.
- Escalate impact: dump credentials, read filesystem (`LOAD_FILE`), or execute commands (`xp_cmdshell`, UDF).

## Mechanisms

SQL Injection occurs when untrusted user input is directly concatenated into dynamic SQL query strings rather than bound using parameterized statements or prepared queries, enabling arbitrary SQL command execution.

### Fingerprinting & Comment Matrix

| DBMS | String Concatenation | Inline Comment | Line Comment | Sleep Command |
| :--- | :--- | :--- | :--- | :--- |
| **MySQL** | `CONCAT('a','b')` | `/*comment*/` | `-- -`, `#` | `SLEEP(5)` |
| **PostgreSQL** | `'a' \|\| 'b'` | `/*comment*/` | `--` | `pg_sleep(5)` |
| **MSSQL** | `'a' + 'b'` | `/*comment*/` | `--` | `WAITFOR DELAY '0:0:5'` |
| **Oracle** | `'a' \|\| 'b'` | `/*comment*/` | `--` | `dbms_pipe.receive_message(5)` |
| **SQLite** | `'a' \|\| 'b'` | `/*comment*/` | `--` | `randomblob(100000000)` |
