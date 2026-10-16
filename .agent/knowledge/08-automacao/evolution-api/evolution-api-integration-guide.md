---json
{
  "id": "evolution-api-integration-guide",
  "title": "Evolution API Integration Guide",
  "categoria": "automacao",
  "subcategoria": "evolution-api",
  "resumo": "Guia condensado de conexao, configuracao de instancias e envio de mensagens WhatsApp via Evolution API v2.",
  "gatilhos": ["evolution api", "whatsapp", "webhook", "instancia", "qrcode", "mensagens"],
  "perguntas_tipo": ["Como conectar uma instancia na Evolution API?", "Como configurar webhook de WhatsApp?"],
  "nao_cobre": ["codigo-fonte interno da api", "deploy do servidor nodejs"],
  "target_agent": ["backend-developer", "automation-engineer"],
  "compatibility": {"evolution_api": ">=2.0.0"},
  "source": {"origin": "Evolution API Official Docs", "original_format": "markdown"},
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-automacao",
  "prioridade": 1
}
---

# Evolution API Integration Guide

> Resumo: gerenciamento de instâncias, autenticação por API Key e envio de mensagens e mídias via WhatsApp.
> Seções: configuracao-inicial · gerenciamento-instancias · envio-mensagens · webhooks

## Configuração inicial

A Evolution API v2 expõe uma interface REST completa para controle de instâncias do WhatsApp (Baseado em Baileys).
As chamadas exigem autenticação via Header HTTP:

```http
apikey: SUA_GLOBAL_API_KEY_OU_INSTANCE_KEY
```

## Gerenciamento de instâncias

Para criar uma nova instância para geração de QR Code:

```bash
POST /instance/create
Content-Type: application/json

{
  "instanceName": "atendimento-01",
  "token": "token-secreto-opcional",
  "qrcode": true
}
```

Para obter o QR Code em Base64 ou texto:

```bash
GET /instance/connect/atendimento-01
```

## Envio de mensagens

### Mensagem de Texto simples
```bash
POST /message/sendText/atendimento-01
Content-Type: application/json

{
  "number": "5511999999999",
  "text": "Ola! Sua solicitacao foi processada com sucesso."
}
```

### Mensagem com Mídia / Anexos
```bash
POST /message/sendMedia/atendimento-01
Content-Type: application/json

{
  "number": "5511999999999",
  "mediatype": "document",
  "mimetype": "application/pdf",
  "caption": "Seu relatorio mensal",
  "media": "https://meudominio.com/relatorios/doc.pdf",
  "fileName": "relatorio.pdf"
}
```

## Webhooks

Configure a URL receptora de eventos para escutar mensagens recebidas e alterações de status de conexão:

```bash
POST /webhook/set/atendimento-01
Content-Type: application/json

{
  "enabled": true,
  "url": "https://meu-n8n-ou-backend/webhook/whatsapp",
  "webhook_by_events": false,
  "events": [
    "MESSAGES_UPSERT",
    "CONNECTION_UPDATE",
    "QRCODE_UPDATED"
  ]
}
```
