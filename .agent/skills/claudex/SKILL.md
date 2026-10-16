---
name: claudex
description: Dual-AI adversarial planning loop where two models cross-examine and harden implementation plans through 3 rounds of review (Senior Engineer, Security/Data Integrity, Ops/SRE) until complete convergence.
---

# ⚔️ Claudex — Dual-AI Adversarial Planning Loop

> **Baseado em:** [`promptadvisers/claudex`](https://github.com/promptadvisers/claudex)  
> **Filosofia:** *Two AIs argue about your plan so you don't have to.*

---

## 🎯 Objetivo

Eliminar pontos cegos, suposições falsas e armadilhas de arquitetura antes de escrever uma única linha de código. O Claudex estabelece um **debate adversarial estruturado entre duas personas de IA**:
1. **O Redator (Planner/Writer):** Transforma uma ideia de uma linha em um plano detalhado numerado.
2. **O Sabatinador (Adversarial Reviewer / Griller):** Desmonta o plano através de 3 rodadas de críticas implacáveis com personas distintas.
3. **A Revisão (Convergence Loop):** O Redator revisa e ajusta o plano a cada rodada até convergir em uma especificação blindada.

---

## 🔄 As 3 Rodadas de Sabatina (The 3 Reviewer Hats)

```plaintext
   [ Ideia Inicial ] ──▶ [ Redator: Draft v1 ]
                                │
        ┌───────────────────────┴───────────────────────┐
        ▼                                               ▼
[ Rodada 1: Engenheiro Sênior ]               [ Rodada 2: Segurança & Integridade ]
• YAGNI, complexidade acidental               • Vazamento de dados, injeções
• Gargalos e escalabilidade                   • Permissões, BOLA/IDOR, edge cases
        │                                               │
        └───────────────────────┬───────────────────────┘
                                ▼
                   [ Rodada 3: DevOps & SRE ]
                   • Observabilidade, telemetria
                   • Rollback e resiliência a falhas
                                │
                                ▼
                      [ Plano Blindado vFinal ]
```

### Rodada 1: Engenheiro Sênior (Architecture & Pragmatism)
* **Foco:** Simplicidade radical, manutenção a longo prazo e ausência de over-engineering.
* **Perguntas-chave:**
  - *"Essa abstração é realmente necessária agora (YAGNI)?"*
  - *"Qual é o caminho crítico de falha sob carga?"*
  - *"Existe uma solução com 50% menos código que resolve o mesmo problema?"*

### Rodada 2: Segurança & Integridade de Dados (AppSec & Trust)
* **Foco:** Superfície de ataque, manipulação de estado e privacidade.
* **Perguntas-chave:**
  - *"Onde dados do usuário entram no sistema sem sanitização?"*
  - *"Se o cliente enviar um payload malformado, o banco quebra ou vaza registros?"*
  - *"As variáveis de ambiente e segredos estão isolados?"*

### Rodada 3: Operações & Confiabilidade (DevOps, SRE & Observability)
* **Foco:** Recuperabilidade, logs, monitoramento e degradação graciosa.
* **Perguntas-chave:**
  - *"Se a API externa cair por 30 segundos, como o sistema se comporta?"*
  - *"Qual é a estratégia de rollback se a migração falhar no meio?"*
  - *"Os logs possuem dados suficientes para diagnosticar um bug em produção?"*

---

## 🛠️ Comandos e Execução

### Script Auxiliar Local
Execute o avaliador adversarial para validar um plano markdown existente:
```bash
python .agent/skills/claudex/scripts/plan_cross_examiner.py caminho/para/plano.md
```

### Formato de Saída Obrigatório
Ao final de uma sessão Claudex, o plano deve conter o bloco de auditoria:
```markdown
### 🛡️ Claudex Convergence Matrix
| Rodada | Críticas Apontadas | Ajustes Implementados | Status |
| :--- | :--- | :--- | :--- |
| **R1 (Sênior)** | 3 sobre-engenharias | Eliminada fila desnecessária | ✅ Resolvido |
| **R2 (AppSec)** | Falta de rate-limit | Adicionado token-bucket no endpoint | ✅ Blindado |
| **R3 (SRE)** | Sem fallback de cache | Implementado stale-while-revalidate | ✅ Aprovado |
```
