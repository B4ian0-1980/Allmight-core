---json
{
  "id": "documentacao_sails",
  "title": "Documentação: Sails.js",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Linguagem:** Node.js **Tipo:** Framework MVC Realtime",
  "gatilhos": [
    "documentacao",
    "linguagens",
    "php",
    "sails"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Sails.js?",
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

# Documentação: Sails.js

> **Linguagem:** Node.js
> **Tipo:** Framework MVC Realtime
> **Site Oficial:** [sailsjs.com](https://sailsjs.com)

## O que é?
Sails.js é o framework MVC mais popular para Node.js. Ele é projetado para emular o padrão familiar de frameworks como Ruby on Rails, mas com suporte a aplicações modernas orientadas a dados e arquitetura orientada a serviços.

## Destaque: Waterline ORM
O Sails possui um ORM poderoso chamado Waterline, que permite usar o mesmo código para acessar diferentes bancos de dados (MySQL, MongoDB, PostgreSQL, LocalDisk, etc).

## Instalação

```bash
# Instalar CLI
npm install sails -g

# Criar nova app
sails new meu-app

# Iniciar
cd meu-app
sails lift
```

## Blueprints API
Um dos recursos mais úteis. O Sails pode gerar automaticamente uma API REST JSON completa para seus modelos sem escrever código.

1.  Gere uma API: `sails generate api user`
2.  Inicie o servidor: `sails lift`
3.  Pronto! Rotas como `POST /user`, `GET /user`, `GET /user/:id` já funcionam.

## Estrutura
*   `api/controllers`: Lógica da aplicação.
*   `api/models`: Modelos de dados (Waterline).
*   `api/policies`: Middleware de autorização.
*   `config/`: Configurações globais.

## Exemplo de Modelo

```javascript
// api/models/User.js
module.exports = {
  attributes: {
    username: { type: 'string', required: true },
    email: { type: 'string', isEmail: true },
    password: { type: 'string', protect: true } // 'protect' oculta em respostas JSON
  }
};
```

## WebSocket Integrado
O Sails abstrai socket.io, permitindo que você trate requisições via Socket da mesma forma que requisições HTTP nos controllers.

## Referências
*   [Conceitos](https://sailsjs.com/documentation/concepts)
*   [Referência da API](https://sailsjs.com/documentation/reference)
