---json
{
  "id": "diretrizes_desenvolvimento",
  "title": "🧠 Diretrizes de Desenvolvimento",
  "categoria": "01-gestao",
  "subcategoria": "arquitetura-software",
  "resumo": "**\"Código limpo, arquitetura sólida e soluções pragmáticas.\"**",
  "gatilhos": [
    "arquitetura",
    "desenvolvimento",
    "diretrizes",
    "gestao",
    "software"
  ],
  "perguntas_tipo": [
    "Como utilizar 🧠 Diretrizes de Desenvolvimento?",
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

# 🧠 Diretrizes de Desenvolvimento

**Versão:** 1.1
**Data:** [DATA_ATUAL]
**Status:** Referência Permanente

---

## 🎯 Princípios Fundamentais

### 1. Filosofia
> **"Código limpo, arquitetura sólida e soluções pragmáticas."**

### 2. Regras de Ouro
1.  **Simplicidade:** Prefira sempre a solução mais simples que resolve o problema.
2.  **Organização:** Mantenha arquivos pequenos (< 300 linhas) e funções focadas.
3.  **Decisão antes de Código:** Nunca comece a programar sem um plano claro.
4.  **Responsabilidade:** Você é responsável pela qualidade do que entrega (testes, docs, performance).

---

## 📝 Classificação de Tarefas

Antes de iniciar, classifique sua tarefa:

| Tipo | Abordagem |
| :--- | :--- |
| **🐛 Bug** | Identificar causa raiz → Criar teste de reprodução → Corrigir. |
| **✨ Feature** | Planejar → Definir contratos (Interfaces) → Implementar → Testar. |
| **🔧 Refactor** | Garantir testes verdes → Melhorar código → Validar (comportamento imutável). |
| **🏗️ Arquitetura** | Criar ADR (Decision Record) → Discutir → Implementar PoC → Executar. |

---

## 🎭 Modos de Operação (para Agentes IA)

### 🏗️ Modo Arquiteto
- **Foco:** Decisões de alto nível, estrutura de pastas, escolha de tecnologias.
- **Saída:** Documentos de Design, Diagramas, ADRs.

### 📋 Modo Planejador
- **Foco:** Quebrar tarefas complexas em passos executáveis.
- **Saída:** Plano de Ação (Checklist), Análise de Riscos.

### 💻 Modo Executor
- **Foco:** Escrever código limpo e funcional.
- **Saída:** Codebase, Testes, Commits.

### 🐞 Modo Depurador
- **Foco:** Resolver problemas.
- **Processo:** Hipótese → Instrumentação (Logs) → Validação → Correção → Limpeza.

---

## ✅ Critérios de Aceite (DoD - Definition of Done)

Para uma tarefa ser considerada "Concluída":
1.  [ ] Código implementado conforme requisitos.
2.  [ ] Testes (Unitários/Integração) passando.
3.  [ ] Sem regressões (Build verde).
4.  [ ] Documentação atualizada (se necessário).
5.  [ ] Análise de impacto realizada (Performance/Segurança).

---

## 🔒 Segurança e Ambientes

- **Credenciais:** NUNCA commite senhas ou chaves. Use `.env`.
- **Ambientes:** Respeite a separação Dev / Staging / Prod.
- **Dados:** Nunca use dados reais de produção em desenvolvimento. Use *Seeders* ou *Factories*.
