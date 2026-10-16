---json
{
  "id": "ambiente_desenvolvimento",
  "title": "🛠️ Ambiente de Desenvolvimento (Padrão)",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "**⚠️ Atenção:** Estas credenciais são para ambiente de **DESENVOLVIMENTO LOCAL**. Nunca utilize senhas fracas em produção.",
  "gatilhos": [
    "ambiente",
    "arquitetura",
    "desenvolvimento",
    "gestao",
    "software"
  ],
  "perguntas_tipo": [
    "Como utilizar 🛠️ Ambiente de Desenvolvimento (Padrão)?",
    "Quais as boas praticas de arquitetura-software?"
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
  "dono": "stack-arquitetura-software",
  "prioridade": 2
}
---

# 🛠️ Ambiente de Desenvolvimento (Padrão)

Este documento registra as configurações do ambiente local utilizado para desenvolvimento e manutenção dos projetos.

## 📍 Caminhos de Instalação

| Ferramenta | Caminho no Sistema | Descrição |
|---|---|---|
| **Git** | `D:\Git` | Controle de versão. |
| **Node.js** | `D:\Nodejs` | Runtime JavaScript. |
| **XAMPP** | `D:\xampp\` | Servidor Web / PHP / MySQL. |
| **PHP** | `D:\xampp\php` | Interpretador PHP (v8.x). |
| **phpMyAdmin**| `D:\xnmpp\phpMyAdmin` | Gestão de Banco de Dados via Web. |

---

## 🗄️ Banco de Dados

**SGBDs:** MariaDB / PostgreSQL

### 🔐 Credenciais Padrão (Local)

| Usuário | Senha | Acesso |
|---|---|---|
| `admin` | `mysql` | Geral |
| `root` | `mysql` | Superusuário |
| `postgres`| `mysql` | PostgreSQL Admin |

> **⚠️ Atenção:** Estas credenciais são para ambiente de **DESENVOLVIMENTO LOCAL**. Nunca utilize senhas fracas em produção.

---

## 📝 Notas Adicionais

*   Certifique-se de que o **XAMPP** (Apache/MySQL) esteja rodando antes de iniciar o desenvolvimento PHP.
*   Para projetos Node.js, verifique se o `npm` está acessível no terminal.
