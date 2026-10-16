---json
{
  "id": "documentacao_sql_bancos",
  "title": "SQL & Bancos de Dados — Guia Completo",
  "categoria": "05-banco-dados",
  "subcategoria": "postgresql",
  "resumo": "💡 **Regra prática:** Use **MySQL/MariaDB** com Laravel/PHP. Use **PostgreSQL** com Next.js/Prisma/Django.",
  "gatilhos": [
    "banco",
    "bancos",
    "completo",
    "dados",
    "documentacao",
    "guia",
    "postgresql",
    "sql"
  ],
  "perguntas_tipo": [
    "Como utilizar SQL & Bancos de Dados — Guia Completo?",
    "Quais as boas praticas de postgresql?"
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
  "dono": "stack-postgresql",
  "prioridade": 2
}
---

# SQL & Bancos de Dados — Guia Completo
## MySQL 8+ · MariaDB 11+ · PostgreSQL 16+

**Fontes:**
- [dev.mysql.com/doc](https://dev.mysql.com/doc/)
- [mariadb.org/documentation](https://mariadb.org/documentation/)
- [postgresql.org/docs](https://www.postgresql.org/docs/)

**Categoria:** Bancos de Dados Relacionais  
**Prioridade:** ALTA (Base de todo sistema)

---

## 1. Visão Geral — Qual Usar?

| Característica | MySQL 8 | MariaDB 11 | PostgreSQL 16 |
|---|---|---|---|
| **Licença** | GPL (Oracle) | GPL (Community) | BSD (Livre) |
| **Usado com** | Laravel, WordPress, PHP | Laravel, PHP (drop-in MySQL) | Next.js, Django, Prisma |
| **JSON** | ✅ Bom | ✅ Bom | ✅ Excelente (JSONB) |
| **Performance** | Alta (leitura) | Alta (leitura) | Alta (escrita/complexo) |
| **Full-text search** | ✅ Básico | ✅ Básico | ✅ Avançado (tsvector) |
| **Replicação** | ✅ Master-Slave | ✅ Galera Cluster | ✅ Streaming/Logical |
| **Porta padrão** | 3306 | 3306 | 5432 |
| **No XAMPP** | ✅ MariaDB incluso | ✅ (é o padrão) | ❌ Instalar separado |

> 💡 **Regra prática:** Use **MySQL/MariaDB** com Laravel/PHP. Use **PostgreSQL** com Next.js/Prisma/Django.

---

## 2. Conexão

### MySQL / MariaDB
```bash
# Via terminal
mysql -u root -p
mysql -u root -p meu_banco

# Via Docker
docker exec -it mysql-dev mysql -u root -p

# String de conexão
mysql://root:senha@localhost:3306/meu_banco
```

### PostgreSQL
```bash
# Via terminal
psql -U postgres
psql -U postgres -d meu_banco

# Via Docker
docker exec -it postgres-dev psql -U admin -d meu_banco

# String de conexão
postgresql://admin:senha@localhost:5432/meu_banco?schema=public
```

---

## 3. DDL — Criação de Estrutura

### Criar Banco
```sql
-- MySQL / MariaDB
CREATE DATABASE meu_banco CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE meu_banco;

-- PostgreSQL
CREATE DATABASE meu_banco WITH ENCODING 'UTF8';
\c meu_banco     -- conectar ao banco
```

### Criar Tabela
```sql
-- ✅ Funciona nos 3 bancos (com pequenas variações)
CREATE TABLE users (
    id          INT PRIMARY KEY AUTO_INCREMENT,  -- MySQL/MariaDB
    -- id       SERIAL PRIMARY KEY,              -- PostgreSQL
    name        VARCHAR(255) NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,
    role        ENUM('admin', 'user', 'editor') DEFAULT 'user',  -- MySQL/MariaDB
    -- role     VARCHAR(20) DEFAULT 'user' CHECK (role IN ('admin','user','editor')), -- PostgreSQL
    cpf         CHAR(14) UNIQUE,
    salary      DECIMAL(10, 2),
    bio         TEXT,
    avatar_url  VARCHAR(500),
    active      BOOLEAN DEFAULT TRUE,
    birth_date  DATE,
    login_at    TIMESTAMP NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- MySQL
    -- updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- PostgreSQL (usar trigger)
    deleted_at  TIMESTAMP NULL,  -- Soft delete

    INDEX idx_email (email),
    INDEX idx_role_active (role, active)
);

-- Tabela com Foreign Key
CREATE TABLE posts (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    title       VARCHAR(255) NOT NULL,
    slug        VARCHAR(255) NOT NULL UNIQUE,
    content     LONGTEXT,                 -- MySQL: LONGTEXT | PostgreSQL: TEXT
    published   BOOLEAN DEFAULT FALSE,
    author_id   INT NOT NULL,
    category_id INT,
    views       INT DEFAULT 0,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL,

    INDEX idx_author (author_id),
    INDEX idx_slug (slug),
    FULLTEXT INDEX idx_search (title, content)  -- MySQL/MariaDB
);

-- Tabela pivô (N:N)
CREATE TABLE post_tags (
    post_id INT NOT NULL,
    tag_id  INT NOT NULL,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);
```

### Alterar Tabela
```sql
-- Adicionar coluna
ALTER TABLE users ADD COLUMN phone VARCHAR(20) AFTER email;

-- Modificar coluna
ALTER TABLE users MODIFY COLUMN name VARCHAR(500) NOT NULL;  -- MySQL
-- ALTER TABLE users ALTER COLUMN name TYPE VARCHAR(500);     -- PostgreSQL

-- Renomear coluna
ALTER TABLE users RENAME COLUMN name TO full_name;

-- Remover coluna
ALTER TABLE users DROP COLUMN phone;

-- Adicionar índice
CREATE INDEX idx_users_name ON users(full_name);

-- Adicionar constraint unique
ALTER TABLE users ADD CONSTRAINT uk_cpf UNIQUE (cpf);

-- Remover tabela
DROP TABLE IF EXISTS posts;
```

---

## 4. DML — Manipulação de Dados

### INSERT
```sql
-- Inserir uma linha
INSERT INTO users (name, email, password, role)
VALUES ('João Silva', 'joao@email.com', '$2b$10$hash...', 'admin');

-- Inserir múltiplas linhas
INSERT INTO users (name, email, password) VALUES
  ('Maria Souza', 'maria@email.com', '$2b$10$hash1'),
  ('Pedro Santos', 'pedro@email.com', '$2b$10$hash2'),
  ('Ana Costa', 'ana@email.com', '$2b$10$hash3');

-- Insert ignorando duplicatas (MySQL)
INSERT IGNORE INTO users (name, email, password)
VALUES ('João Silva', 'joao@email.com', '$2b$10$hash...');

-- Upsert: Insert ou Update (MySQL)
INSERT INTO users (email, name, password)
VALUES ('joao@email.com', 'João Atualizado', '$2b$10$new')
ON DUPLICATE KEY UPDATE name = VALUES(name);

-- Upsert (PostgreSQL)
INSERT INTO users (email, name, password)
VALUES ('joao@email.com', 'João Atualizado', '$2b$10$new')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;
```

### SELECT
```sql
-- Básico
SELECT * FROM users;
SELECT name, email FROM users;
SELECT DISTINCT role FROM users;

-- WHERE (filtros)
SELECT * FROM users WHERE active = TRUE;
SELECT * FROM users WHERE role = 'admin' AND active = TRUE;
SELECT * FROM users WHERE role IN ('admin', 'editor');
SELECT * FROM users WHERE name LIKE '%Silva%';
SELECT * FROM users WHERE salary BETWEEN 3000 AND 8000;
SELECT * FROM users WHERE deleted_at IS NULL;          -- Soft delete
SELECT * FROM users WHERE email NOT LIKE '%teste%';

-- Ordenação
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users ORDER BY created_at DESC;
SELECT * FROM users ORDER BY role ASC, name ASC;

-- Paginação
SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 0;    -- Página 1
SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 10;   -- Página 2
SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 20;   -- Página 3

-- Alias
SELECT
  u.name AS nome,
  u.email AS email,
  COUNT(p.id) AS total_posts
FROM users u
LEFT JOIN posts p ON p.author_id = u.id
GROUP BY u.id, u.name, u.email;

-- Subquery
SELECT * FROM users
WHERE id IN (SELECT author_id FROM posts WHERE published = TRUE);
```

### JOINs
```sql
-- INNER JOIN (só correspondências)
SELECT u.name, p.title
FROM users u
INNER JOIN posts p ON p.author_id = u.id;

-- LEFT JOIN (todos da esquerda + correspondências)
SELECT u.name, COUNT(p.id) AS posts
FROM users u
LEFT JOIN posts p ON p.author_id = u.id
GROUP BY u.id, u.name;

-- Múltiplos JOINs
SELECT
  p.title,
  u.name AS author,
  c.name AS category,
  GROUP_CONCAT(t.name) AS tags     -- MySQL
  -- STRING_AGG(t.name, ', ') AS tags  -- PostgreSQL
FROM posts p
INNER JOIN users u ON u.id = p.author_id
LEFT JOIN categories c ON c.id = p.category_id
LEFT JOIN post_tags pt ON pt.post_id = p.id
LEFT JOIN tags t ON t.id = pt.tag_id
WHERE p.published = TRUE
GROUP BY p.id, p.title, u.name, c.name
ORDER BY p.created_at DESC;
```

### Funções de Agregação
```sql
SELECT COUNT(*) AS total FROM users;
SELECT COUNT(*) AS total FROM users WHERE active = TRUE;
SELECT AVG(salary) AS media_salarial FROM users;
SELECT SUM(salary) AS folha_total FROM users WHERE active = TRUE;
SELECT MIN(salary) AS menor, MAX(salary) AS maior FROM users;

-- GROUP BY + HAVING
SELECT
  role,
  COUNT(*) AS total,
  AVG(salary) AS media
FROM users
WHERE active = TRUE
GROUP BY role
HAVING COUNT(*) > 5
ORDER BY total DESC;
```

### UPDATE
```sql
-- Atualizar um registro
UPDATE users SET name = 'João Atualizado', role = 'admin' WHERE id = 1;

-- Atualizar múltiplos
UPDATE users SET active = FALSE WHERE login_at < '2024-01-01';

-- Incrementar valor
UPDATE posts SET views = views + 1 WHERE id = 42;

-- Soft delete
UPDATE users SET deleted_at = NOW() WHERE id = 5;
```

### DELETE
```sql
-- Deletar um registro
DELETE FROM users WHERE id = 1;

-- Deletar múltiplos
DELETE FROM users WHERE active = FALSE AND created_at < '2023-01-01';

-- Deletar TUDO (⚠️ cuidado!)
DELETE FROM logs;        -- Preserva AUTO_INCREMENT
TRUNCATE TABLE logs;     -- Reseta AUTO_INCREMENT (mais rápido)
```

---

## 5. Funções Úteis

### Data e Hora
```sql
-- MySQL / MariaDB
SELECT NOW();                                          -- 2026-02-14 12:00:00
SELECT CURDATE();                                      -- 2026-02-14
SELECT DATE_FORMAT(created_at, '%d/%m/%Y') FROM users; -- 14/02/2026
SELECT DATEDIFF(NOW(), created_at) AS dias FROM users; -- Dias desde criação
SELECT DATE_ADD(NOW(), INTERVAL 30 DAY);               -- +30 dias
SELECT YEAR(created_at), MONTH(created_at) FROM users;

-- PostgreSQL
SELECT NOW();
SELECT CURRENT_DATE;
SELECT TO_CHAR(created_at, 'DD/MM/YYYY') FROM users;
SELECT AGE(NOW(), created_at) FROM users;
SELECT created_at + INTERVAL '30 days' FROM users;
SELECT EXTRACT(YEAR FROM created_at) FROM users;
```

### Texto
```sql
-- Funciona nos 3 bancos
SELECT UPPER(name) FROM users;
SELECT LOWER(email) FROM users;
SELECT LENGTH(name) FROM users;
SELECT TRIM(name) FROM users;
SELECT CONCAT(name, ' (', role, ')') FROM users;
SELECT SUBSTRING(name, 1, 10) FROM users;       -- Primeiros 10 chars
SELECT REPLACE(email, '@email.com', '@novo.com') FROM users;

-- MySQL: CONCAT_WS (com separador)
SELECT CONCAT_WS(' - ', name, email, role) FROM users;

-- Busca Full-text (MySQL/MariaDB)
SELECT * FROM posts
WHERE MATCH(title, content) AGAINST('laravel prisma' IN BOOLEAN MODE);

-- Busca Full-text (PostgreSQL)
SELECT * FROM posts
WHERE TO_TSVECTOR('portuguese', title || ' ' || content)
  @@ TO_TSQUERY('portuguese', 'laravel & prisma');
```

### Condicionais
```sql
-- CASE
SELECT
  name,
  salary,
  CASE
    WHEN salary >= 10000 THEN 'Senior'
    WHEN salary >= 5000  THEN 'Pleno'
    WHEN salary >= 3000  THEN 'Junior'
    ELSE 'Estagiário'
  END AS nivel
FROM users;

-- COALESCE (primeiro não-nulo)
SELECT COALESCE(phone, email, 'Sem contato') AS contato FROM users;

-- IF (MySQL)
SELECT name, IF(active, 'Ativo', 'Inativo') AS status FROM users;

-- IFNULL (MySQL) / COALESCE (PostgreSQL)
SELECT IFNULL(phone, 'N/A') FROM users;  -- MySQL
SELECT COALESCE(phone, 'N/A') FROM users; -- PostgreSQL
```

---

## 6. Views (Consultas Salvas)

```sql
CREATE VIEW v_active_users AS
SELECT id, name, email, role, created_at
FROM users
WHERE active = TRUE AND deleted_at IS NULL;

-- Usar como tabela normal
SELECT * FROM v_active_users WHERE role = 'admin';

-- Remover
DROP VIEW IF EXISTS v_active_users;
```

---

## 7. Stored Procedures e Triggers

### Procedure (MySQL)
```sql
DELIMITER //
CREATE PROCEDURE sp_deactivate_inactive_users(IN days_limit INT)
BEGIN
    UPDATE users
    SET active = FALSE
    WHERE login_at < DATE_SUB(NOW(), INTERVAL days_limit DAY)
      AND active = TRUE;

    SELECT ROW_COUNT() AS users_deactivated;
END //
DELIMITER ;

-- Chamar
CALL sp_deactivate_inactive_users(90);
```

### Trigger
```sql
-- MySQL: Atualizar updated_at automaticamente
CREATE TRIGGER trg_users_updated
BEFORE UPDATE ON users
FOR EACH ROW
SET NEW.updated_at = NOW();

-- PostgreSQL: Trigger para updated_at
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_users_updated
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

---

## 8. Performance — Índices

```sql
-- Criar índices
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_author ON posts(author_id);
CREATE INDEX idx_posts_published_date ON posts(published, created_at);

-- Índice unique
CREATE UNIQUE INDEX idx_users_cpf ON users(cpf);

-- Ver índices
SHOW INDEX FROM users;  -- MySQL
-- \di+ users;          -- PostgreSQL

-- Analisar query (EXPLAIN)
EXPLAIN SELECT * FROM posts WHERE author_id = 5;
EXPLAIN ANALYZE SELECT * FROM posts WHERE author_id = 5;  -- PostgreSQL

-- ⚠️ Regras de índice:
-- ✅ Colunas usadas em WHERE, JOIN, ORDER BY
-- ✅ Foreign keys
-- ❌ NÃO indexe colunas com poucos valores distintos (boolean)
-- ❌ NÃO crie índices demais (afeta INSERT/UPDATE)
```

---

## 9. Backup e Restore

### MySQL / MariaDB
```bash
# Backup
mysqldump -u root -p meu_banco > backup_$(date +%Y%m%d).sql
mysqldump -u root -p --all-databases > backup_all.sql

# Restore
mysql -u root -p meu_banco < backup_20260214.sql
```

### PostgreSQL
```bash
# Backup
pg_dump -U postgres meu_banco > backup.sql
pg_dump -U postgres -Fc meu_banco > backup.dump  # Formato comprimido

# Restore
psql -U postgres meu_banco < backup.sql
pg_restore -U postgres -d meu_banco backup.dump
```

---

## 10. Segurança — Usuários e Permissões

```sql
-- MySQL / MariaDB
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'senha_forte';
GRANT SELECT, INSERT, UPDATE, DELETE ON meu_banco.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;

-- Revogar
REVOKE DELETE ON meu_banco.* FROM 'app_user'@'localhost';

-- PostgreSQL
CREATE USER app_user WITH PASSWORD 'senha_forte';
GRANT CONNECT ON DATABASE meu_banco TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
```

---

## 11. Segurança de Aplicação (Anti-SQL Injection)

❌ **NUNCA FAÇA ISSO (Vulnerável):**
```javascript
// PERIGO: Concatenação de strings permite SQL Injection
const query = "SELECT * FROM users WHERE email = '" + email + "'";
```

✅ **SEMPRE USE Prepared Statements:**

### Node.js (mysql2 / pg)
```javascript
// MySQL
const sql = 'SELECT * FROM users WHERE email = ?';
connection.execute(sql, [email], (err, results) => { ... });

// PostgreSQL
const sql = 'SELECT * FROM users WHERE email = $1';
client.query(sql, [email], (err, res) => { ... });
```

### PHP (PDO)
```php
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute(['email' => $email]);
$user = $stmt->fetch();
```

### Java (JDBC)
```java
String sql = "SELECT * FROM users WHERE email = ?";
PreparedStatement pstmt = conn.prepareStatement(sql);
pstmt.setString(1, email);
ResultSet rs = pstmt.executeQuery();
```

### Python (psycopg2 / mysql-connector)
```python
# O driver faz a sanitização automática
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
```

---

## 12. Cheatsheet Rápido

| Ação | MySQL/MariaDB | PostgreSQL |
|---|---|---|
| Listar bancos | `SHOW DATABASES;` | `\l` |
| Usar banco | `USE nome;` | `\c nome` |
| Listar tabelas | `SHOW TABLES;` | `\dt` |
| Descrever tabela | `DESCRIBE tabela;` | `\d tabela` |
| Ver processos | `SHOW PROCESSLIST;` | `SELECT * FROM pg_stat_activity;` |
| Tamanho do banco | `SELECT table_schema, SUM(data_length) FROM information_schema.tables GROUP BY table_schema;` | `SELECT pg_size_pretty(pg_database_size('nome'));` |

---

*Fontes: [dev.mysql.com/doc](https://dev.mysql.com/doc/) · [mariadb.org/documentation](https://mariadb.org/documentation/) · [postgresql.org/docs](https://www.postgresql.org/docs/) — Consultado em 2026-02-14*
