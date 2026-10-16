---json
{
  "id": "spec",
  "title": "SPEC: Zap Guardian (Protocolo de Resiliência)",
  "categoria": "08-automacao",
  "subcategoria": "evolution-api",
  "resumo": "[!IMPORTANT] O Zap Guardian deve ser a única fonte de verdade para o status das instâncias. Se o Guardian diz que está OFFLINE, a IA deve avisar o administrador antes de tentar responder.",
  "gatilhos": [
    "api",
    "automacao",
    "evolution",
    "guardian",
    "protocolo",
    "spec",
    "zap"
  ],
  "perguntas_tipo": [
    "Como utilizar SPEC: Zap Guardian (Protocolo de Resiliência)?",
    "Quais as boas praticas de evolution-api?"
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
  "dono": "stack-evolution-api",
  "prioridade": 2
}
---

# SPEC: Zap Guardian (Protocolo de Resiliência)

O **Zap Guardian** é um sistema de monitoramento e auto-cura para APIs de WhatsApp, garantindo que o Agente AllMight nunca perca a conexão com os usuários.

## 📡 APIs Suportadas (Modo Adaptador)

| API | Endpoints Críticos | Tipo de Status |
| :--- | :--- | :--- |
| **WPPConnect** | `/api/:session/status-session` | JSON (Connected/Disconnected) |
| **Evolution API** | `/instance/connectionState/:instance` | JSON (open/close) |
| **WAHA** | `/sessions/:session` | JSON (WORKING/STOPPED) |

## 🏗️ Arquitetura: O Adaptador Universal

O Guardian não lê os logs brutos. Ele utiliza um script intermediário (`guardian_monitor.py`) que normaliza a saída para um padrão AllMight:

```json
{
  "guardian_version": "1.0",
  "instance_name": "suporte_01",
  "engine": "WPPConnect",
  "status": "ONLINE", 
  "signal_strength": 85,
  "webhook_active": true,
  "pending_messages": 0,
  "last_check": "2026-03-24T11:15:00Z"
}
```

## 🛠️ Funcionalidades Core

### 1. Health Check & Heartbeat
- Varredura a cada 5 minutos das instâncias cadastradas.
- Alerta no n8n se o status mudar de `ONLINE` para `OFFLINE`.

### 2. Auto-Cura de Webhooks
- Se o campo `webhook_active` for `false`, o Guardian dispara automaticamente um `POST` para o endpoint de registro de webhook da API específica, apontando para o n8n.

### 3. Queue Manager (Anti-Ban)
- Camada lógica que recebe mensagens da IA e as libera com delays variáveis (3s a 15s).
- Simula a digitação enviando o estado `composing` via API antes de disparar o texto.

## 📂 Localização de Arquivos
- **Script:** `07_AUTOMACAO/scripts/zap_guardian/guardian_monitor.py`
- **Config:** `07_AUTOMACAO/configs/zap_instances.json` (YAML/JSON com as credenciais)

---

> [!IMPORTANT]
> O Zap Guardian deve ser a única fonte de verdade para o status das instâncias. Se o Guardian diz que está OFFLINE, a IA deve avisar o administrador antes de tentar responder.
