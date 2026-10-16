---json
{
  "id": "template_modulo_usuarios",
  "title": "👤 Template - Módulo de Usuários (Genérico)",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 👤 Template - Módulo de Usuários (Genérico).",
  "gatilhos": [
    "arquitetura",
    "gestao",
    "modulo",
    "software",
    "template",
    "usuarios"
  ],
  "perguntas_tipo": [
    "Como utilizar 👤 Template - Módulo de Usuários (Genérico)?",
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

# 👤 Template - Módulo de Usuários (Genérico)

**Versão:** 1.0
**Status:** Template Base

---

## 🎯 Objetivo
Fornecer uma especificação agnóstica para implementação de autenticação e gestão de usuários.

---

## 📊 Modelo de Dados (Schema Sugerido)

| Campo | Tipo | Obrigatório | Detalhes |
| :--- | :--- | :--- | :--- |
| **id** | UUID/Int | Sim | Identificador único. |
| **name** | String | Sim | Nome completo. |
| **email** | String | Sim | Único, formato válido. |
| **password** | Hash | Sim | Mínimo 8 chars. Nunca texto plano. |
| **profile_id** | FK | Sim | Ligação com tabela de Perfis/Roles. |
| **active** | Boolean | Sim | Default: `true` (ou `false` se requerer aprovação). |
| **created_at** | Timestamp | Sim | Automático. |

---

## 🔐 Regras de Negócio Core

### 1. Autenticação (Login)
- **Input:** Email + Senha.
- **Validação:**
  - Verificar se email existe.
  - Verificar hash da senha.
  - Verificar se `active` é true.
- **Output:** Token (JWT/Sanctum) ou Sessão.

### 2. Cadastro (Register)
- **Campos:** Nome, Email, Senha, Confirmação de Senha.
- **Regras:**
  - Email deve ser único.
  - Senha deve ter complexidade mínima (ex: letras + números).
- **Pós-Cadastro:** Enviar email de boas-vindas/confirmação (opcional).

### 3. Recuperação de Senha
- **Fluxo:** Solicitar via Email -> Gerar Token Único -> Enviar Link -> Definir Nova Senha.
- **Segurança:** Token deve expirar em X minutos.

---

## 🛡️ Perfis de Acesso (RBAC)

Sugestão de estrutura inicial:

| Perfil | Permissões Típicas |
| :--- | :--- |
| **Admin** | Acesso total ao sistema. CRUD de Usuários. |
| **Gestor** | Visualizar relatórios, gerenciar equipe. |
| **Usuário** | Acesso às funcionalidades básicas. |

---

## 🔍 Casos de Uso (User Stories)

1. **Como Admin**, quero desativar um usuário, para impedir acessos indevidos.
2. **Como Usuário**, quero alterar minha senha, para manter segurança.
3. **Como Sistema**, quero bloquear tentativas excessivas de login, para evitar Brute-force.
