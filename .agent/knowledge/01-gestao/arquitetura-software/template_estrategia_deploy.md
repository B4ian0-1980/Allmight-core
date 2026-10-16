---json
{
  "id": "template_estrategia_deploy",
  "title": "🚀 Template - Estratégia de Deploy",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "Guia tecnico e referencias sobre 🚀 Template - Estratégia de Deploy.",
  "gatilhos": [
    "arquitetura",
    "deploy",
    "estrategia",
    "gestao",
    "software",
    "template"
  ],
  "perguntas_tipo": [
    "Como utilizar 🚀 Template - Estratégia de Deploy?",
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

# 🚀 Template - Estratégia de Deploy

**Projeto:** [NOME_DO_PROJETO]
**Data:** [DATA_ATUAL]
**Versão:** 1.0

---

## 🎯 Objetivo
Estabelecer um processo de deploy seguro, automatizado e reversível para garantir a entrega contínua de valor.

---

## 🌍 Ambientes

| Ambiente | URL | Branch | Finalidade |
| :--- | :--- | :--- | :--- |
| **Development** | `dev.projeto.com` | `develop` | Testes de desenvolvimento, instável. |
| **Staging** | `stage.projeto.com` | `release/*` | Homologação com QA/Cliente, espelho de produção. |
| **Production** | `projeto.com` | `main` | Ambiente final para usuários. |

---

## 🏗️ Pipeline de CI/CD

### 1. Continuous Integration (CI)
Executado a cada Push/PR.
- [ ] Linting (Código estático)
- [ ] Testes Unitários
- [ ] Build de verificação

### 2. Continuous Deployment (CD)
Executado após merge em branches principais.
- [ ] Build Otimizado
- [ ] Migrations de Banco de Dados
- [ ] Upload de Assets (CDN)
- [ ] Swap de Versão (Zero Downtime)

---

## 🚩 Estratégia de Rollback

**Em caso de falha crítica em Produção:**

1. **Rollback de Aplicação:**
   - Reverter para o último artefato estável (Docker tag anterior ou Release anterior).
   - Tempo estimado: < 5 min.

2. **Rollback de Banco de Dados:**
   - Executar `migrate:rollback` (se reversível).
   - Restaurar backup (se irreversível).

---

## 📋 Checklist de Deploy (Manual/Automático)

- [ ] Todos os testes passaram no CI?
- [ ] Migrations foram revisadas?
- [ ] Variáveis de ambiente (Secrets) atualizadas?
- [ ] Backup do banco realizado?
- [ ] Changelog atualizado?

---

## 📊 Monitoramento Pós-Deploy

- **Logs de Erro:** Verificar Sentry/Logs por 1h.
- **Performance:** Verificar métricas de APM.
- **Smoke Test:** Executar testes básicos de navegação.
