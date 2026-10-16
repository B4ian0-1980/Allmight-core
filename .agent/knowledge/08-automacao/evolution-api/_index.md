---
id: idx_evolution-api
resumo: Indice de recursos e manuais de evolution-api
gatilhos:
- evolution api
- whatsapp
- webhook
- instancia
- qrcode
- mensagens
- api
- automacao
- evolution
- guardian
rotas:
- id: evolution-api-integration-guide
  resumo: Guia condensado de conexao, configuracao de instancias e envio de mensagens
    WhatsApp via Evolution API v2.
  gatilhos:
  - evolution api
  - whatsapp
  - webhook
  - instancia
  - qrcode
  - mensagens
  arquivo: ./evolution-api-integration-guide.md
  secoes:
  - configuração-inicial
  - gerenciamento-de-instâncias
  - envio-de-mensagens
  - webhooks
  tokens_estimados: 443
- id: spec
  resumo: '[!IMPORTANT] O Zap Guardian deve ser a única fonte de verdade para o status
    das instâncias. Se o Guardian diz que está OFFLINE, a IA deve avisar o administrador
    antes de tentar responder.'
  gatilhos:
  - api
  - automacao
  - evolution
  - guardian
  - protocolo
  - spec
  arquivo: ./spec.md
  secoes:
  - apis-suportadas-modo-adaptador
  - arquitetura-o-adaptador-universal
  - funcionalidades-core
  - localização-de-arquivos
  tokens_estimados: 484
---
