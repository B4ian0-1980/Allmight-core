---
description: Comando de depuração. Ativa o modo DEBUG para investigação sistemática de problemas seguindo o protocolo de Engenheiro Sênior.
---

# /debug - Protocolo de Depuração Sênior

$ARGUMENTS

---

## Propósito

Este comando ativa o **Modo Depurador** seguindo uma sequência rigorosa de investigação baseada em evidências, garantindo que a causa raiz seja identificada antes da implementação da correção.

---

## Protocolo de Execução (Sequência Obrigatória)

Ao acionar `/debug`, o agente DEVE seguir estes passos:

1.  **Reflexão de Hipóteses**:
    - Listar de **5 a 7 possíveis causas** para o problema.
    - Reduzir para as **1 a 2 causas mais prováveis**.

2.  **Instrumentação**:
    - Adicionar logs adicionais no código para validar suposições.
    - Rastrear a transformação das estruturas de dados ao longo do fluxo de controle.

3.  **Coleta de Evidências**:
    - Utilizar ferramentas: `getConsoleLogs`, `getConsoleErrors`, `getNetworkLogs`, `getNetworkErrors`.
    - Obter logs do servidor se acessíveis (ou solicitar ao usuário).

4.  **Análise Profunda**:
    - Produzir uma análise abrangente do problema com base nos logs coletados.
    - Se a causa ainda não estiver clara, sugerir e implementar logs adicionais.

5.  **Correção Cirúrgica**:
    - Implementar a correção focada apenas na causa raiz.
    - Refletir sobre a manutenibilidade e escalabilidade da correção.

6.  **Limpeza**:
    - Solicitar aprovação do usuário para remover os logs de depuração adicionados.

---

## Formato de Saída

```markdown
## 🔍 Depuração: [Problema]

### 🕵️ Hipóteses Iniciais
1. [Hipótese 1]
...
7. [Hipótese 7]

**Causas mais prováveis:** [1 e 2]

### 🛠️ Instrumentação de Logs
- [Arquivo]: Adicionado log para rastrear [variável] na linha [X].
- [Arquivo]: Adicionado log de fluxo em [função].

### 📊 Análise de Evidências
[Análise técnica baseada nos logs capturados]

### ✅ Correção Sugerida
[Código corrigido]

### 🧹 Próximos Passos
- Validar correção em ambiente de [dev/test].
- Solicitar remoção de logs: [Aprovar?]
```

---

## Princípios Chave

- **Evidência sobre Suposição**: Nunca corrigir sem ver o dado transformado nos logs.
- **Rastreabilidade**: Entender o caminho do dado do início ao fim.
- **Limpeza**: O código de produção não deve conter logs de depuração.
