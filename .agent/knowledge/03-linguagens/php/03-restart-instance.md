---json
{
  "id": "03-restart-instance",
  "title": "Restart Instance",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "Guia tecnico e referencias sobre Restart Instance.",
  "gatilhos": [
    "instance",
    "linguagens",
    "php",
    "restart"
  ],
  "perguntas_tipo": [
    "Como utilizar Restart Instance?",
    "Quais as boas praticas de php?"
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
  "dono": "stack-php",
  "prioridade": 2
}
---

---
sidebar_position: 3
---

# Restart Instance

| Method | Endpoint                                  |
| ------ | ----------------------------------------- |
| PUT    | [baseUrl]/instance/restart/[instance] |

### Data to be sent in the Request

```json title=Payload
This request has no payload.
```

### Data returned from the Request

```json title=Result
{
  "state": "[state]",
  "statusReason": [statusCode]
}
```
