---
description: Realizar auditoria técnica completa de segurança, performance e arquitetura.
---

# /audit - Auditoria Técnica Completa

$ARGUMENTS

---

## Propósito

Este comando aciona o agente `auditor-specialist` para realizar uma varredura exaustiva do sistema, identificando vulnerabilidades, gargalos de performance e desvios arquiteturais.

---

## Fluxo de Execução

1. **Ativar Auditor**: Invoca o `auditor-specialist`.
2. **Varredura de Camadas**:
   - Back-end (Segurança, Lógica, DB).
   - Front-end (UI/UX, Vitals, Segurança).
   - Integração (API, Auth).
3. **Análise de Risco**: Classificação de achados (Crítico a Baixo).
4. **Relatório**: Geração de `docs/AUDIT-{timestamp}.md`.

---

## Opções de Comando

- `/audit security`: Foco exclusivo em vulnerabilidades OWASP.
- `/audit performance`: Foco em gargalos de backend e frontend.
- `/audit cloudflare`: Auditoria formal de 6 fases da Cloudflare com validação de candidatos (harness com coverage ledger e findings JSON).
- `/audit full`: Auditoria completa de todas as fases.

---

## Entrega Esperada

- Relatório detalhado com status ✅, ⚠️, ❌, 🔧.
- Código real para correções imediatas.
- Plano de remediação priorizado.
